"""
Core Agent Framework
Base classes and utilities for the agentic system
"""

from abc import ABC, abstractmethod
from typing import Dict, List, Any, Optional
from datetime import datetime
from enum import Enum
import json


class AgentStatus(Enum):
    """Agent execution status"""
    IDLE = "idle"
    WORKING = "working"
    COMPLETED = "completed"
    FAILED = "failed"
    VALIDATING = "validating"


class AgentRole(Enum):
    """Types of agents in the system"""
    MARKET_RESEARCH = "market_research"
    CONTENT_CREATOR = "content_creator"
    SALES_SPECIALIST = "sales_specialist"
    TECHNICAL_EXPERT = "technical_expert"
    QA_VALIDATOR = "qa_validator"
    COORDINATOR = "coordinator"


class Task:
    """Represents a task to be executed by an agent"""
    
    def __init__(self, task_id: str, description: str, context: Dict[str, Any] = None):
        self.task_id = task_id
        self.description = description
        self.context = context or {}
        self.created_at = datetime.now()
        self.completed_at: Optional[datetime] = None
        self.status = AgentStatus.IDLE
        self.result: Optional[Any] = None
        self.errors: List[str] = []
    
    def to_dict(self) -> Dict[str, Any]:
        return {
            "task_id": self.task_id,
            "description": self.description,
            "context": self.context,
            "status": self.status.value,
            "result": self.result,
            "errors": self.errors,
            "created_at": self.created_at.isoformat(),
            "completed_at": self.completed_at.isoformat() if self.completed_at else None
        }


class BaseAgent(ABC):
    """Base class for all agents in the system"""
    
    def __init__(self, agent_id: str, role: AgentRole, config: Dict[str, Any] = None):
        self.agent_id = agent_id
        self.role = role
        self.config = config or {}
        self.status = AgentStatus.IDLE
        self.task_history: List[Task] = []
        self.expert_team: List['BaseAgent'] = []
        self._consultation_depth = 0
        self._max_consultation_depth = 1
        
    @abstractmethod
    def execute_task(self, task: Task) -> Any:
        """Execute a specific task - must be implemented by subclasses"""
        pass
    
    def add_expert(self, expert: 'BaseAgent'):
        """Add an expert to this agent's team"""
        self.expert_team.append(expert)
    
    def consult_experts(self, query: str, context: Dict[str, Any]) -> List[Dict[str, Any]]:
        """Consult expert team for assistance"""
        # Prevent infinite recursion by limiting consultation depth
        if self._consultation_depth >= self._max_consultation_depth:
            return []
        
        consultations = []
        self._consultation_depth += 1
        
        try:
            for expert in self.expert_team:
                task = Task(
                    task_id=f"consult_{expert.agent_id}_{datetime.now().timestamp()}",
                    description=query,
                    context=context
                )
                result = expert.execute_task(task)
                consultations.append({
                    "expert": expert.agent_id,
                    "role": expert.role.value,
                    "advice": result
                })
        finally:
            self._consultation_depth -= 1
        
        return consultations
    
    def validate_work(self, validator: 'BaseAgent', work: Any) -> Dict[str, Any]:
        """Have a QA validator check the work"""
        validation_task = Task(
            task_id=f"validate_{self.agent_id}_{datetime.now().timestamp()}",
            description="Validate the following work for quality and correctness",
            context={"work": work, "agent": self.agent_id}
        )
        return validator.execute_task(validation_task)
    
    def log_task(self, task: Task):
        """Log a completed task"""
        self.task_history.append(task)
    
    def get_stats(self) -> Dict[str, Any]:
        """Get agent statistics"""
        completed = len([t for t in self.task_history if t.status == AgentStatus.COMPLETED])
        failed = len([t for t in self.task_history if t.status == AgentStatus.FAILED])
        
        return {
            "agent_id": self.agent_id,
            "role": self.role.value,
            "status": self.status.value,
            "total_tasks": len(self.task_history),
            "completed_tasks": completed,
            "failed_tasks": failed,
            "expert_team_size": len(self.expert_team)
        }


class AgentTeam:
    """Manages a team of agents working together"""
    
    def __init__(self, team_id: str, niche: str):
        self.team_id = team_id
        self.niche = niche
        self.agents: Dict[str, BaseAgent] = {}
        self.qa_validator: Optional[BaseAgent] = None
    
    def add_agent(self, agent: BaseAgent):
        """Add an agent to the team"""
        self.agents[agent.agent_id] = agent
        if agent.role == AgentRole.QA_VALIDATOR:
            self.qa_validator = agent
    
    def get_agent(self, agent_id: str) -> Optional[BaseAgent]:
        """Get an agent by ID"""
        return self.agents.get(agent_id)
    
    def execute_workflow(self, workflow: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
        """Execute a workflow across multiple agents"""
        results = []
        context = {}
        
        for step in workflow:
            agent_role = step.get("agent_role")
            task_description = step.get("task")
            
            # Find agent with matching role
            agent = next((a for a in self.agents.values() if a.role.value == agent_role), None)
            
            if not agent:
                results.append({
                    "step": step,
                    "status": "failed",
                    "error": f"No agent found with role {agent_role}"
                })
                continue
            
            # Create and execute task
            task = Task(
                task_id=f"workflow_{self.team_id}_{len(results)}",
                description=task_description,
                context=context
            )
            
            try:
                result = agent.execute_task(task)
                
                # Validate with QA if available
                if self.qa_validator and agent.role != AgentRole.QA_VALIDATOR:
                    validation = agent.validate_work(self.qa_validator, result)
                    if not validation.get("approved", False):
                        results.append({
                            "step": step,
                            "status": "failed_validation",
                            "result": result,
                            "validation": validation
                        })
                        continue
                
                # Add result to context for next steps
                context[agent_role] = result
                
                results.append({
                    "step": step,
                    "status": "success",
                    "result": result
                })
            except Exception as e:
                results.append({
                    "step": step,
                    "status": "error",
                    "error": str(e)
                })
        
        return results
    
    def get_team_stats(self) -> Dict[str, Any]:
        """Get statistics for the entire team"""
        return {
            "team_id": self.team_id,
            "niche": self.niche,
            "agent_count": len(self.agents),
            "has_qa": self.qa_validator is not None,
            "agents": [agent.get_stats() for agent in self.agents.values()]
        }
