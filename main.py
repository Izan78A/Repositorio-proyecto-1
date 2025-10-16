"""
Sistema Agéntico Local - Main Orchestrator
Coordinates the entire agentic system
"""

import yaml
from typing import Dict, Any, List
from pathlib import Path

from core import AgentTeam, AgentRole
from core.ai_provider import AIProviderFactory
from agents import (
    MarketResearchAgent,
    ContentCreatorAgent,
    SalesSpecialistAgent,
    TechnicalExpertAgent,
    QAValidatorAgent
)


class AgenticSystem:
    """Main orchestrator for the agentic system"""
    
    def __init__(self, config_path: str = "config.yaml"):
        """Initialize the agentic system"""
        self.config = self._load_config(config_path)
        self.teams: Dict[str, AgentTeam] = {}
        self.ai_provider = None
        self._initialize_ai_provider()
    
    def _load_config(self, config_path: str) -> Dict[str, Any]:
        """Load system configuration"""
        config_file = Path(config_path)
        if config_file.exists():
            with open(config_file, 'r', encoding='utf-8') as f:
                return yaml.safe_load(f)
        return {}
    
    def _initialize_ai_provider(self):
        """Initialize the AI provider"""
        provider_config = self.config.get('ai_models', {})
        default_provider = provider_config.get('default_provider', 'openai')
        
        provider_settings = provider_config.get(default_provider, {})
        
        self.ai_provider = AIProviderFactory.create_provider(
            default_provider,
            provider_settings
        )
    
    def create_niche_team(self, team_id: str, niche: str, team_config: Dict[str, Any] = None) -> AgentTeam:
        """
        Create a specialized team of agents for a specific market niche
        
        Args:
            team_id: Unique identifier for the team
            niche: Market niche this team specializes in
            team_config: Optional configuration for the team
        
        Returns:
            AgentTeam instance
        """
        team = AgentTeam(team_id, niche)
        team_config = team_config or {}
        
        # Create specialized agents
        agents_to_create = team_config.get('agents', [
            'market_research',
            'content_creator',
            'sales_specialist',
            'technical_expert',
            'qa_validator'
        ])
        
        agent_instances = []
        
        for agent_type in agents_to_create:
            agent_id = f"{team_id}_{agent_type}"
            
            if agent_type == 'market_research':
                agent = MarketResearchAgent(agent_id, self.ai_provider)
                agent_instances.append(agent)
                team.add_agent(agent)
                
            elif agent_type == 'content_creator':
                agent = ContentCreatorAgent(agent_id, self.ai_provider)
                agent_instances.append(agent)
                team.add_agent(agent)
                
            elif agent_type == 'sales_specialist':
                agent = SalesSpecialistAgent(agent_id, self.ai_provider)
                agent_instances.append(agent)
                team.add_agent(agent)
                
            elif agent_type == 'technical_expert':
                agent = TechnicalExpertAgent(agent_id, self.ai_provider)
                agent_instances.append(agent)
                team.add_agent(agent)
                
            elif agent_type == 'qa_validator':
                agent = QAValidatorAgent(agent_id, self.ai_provider)
                agent_instances.append(agent)
                team.add_agent(agent)
        
        # Create expert teams for each agent (excluding QA)
        for agent in agent_instances:
            if agent.role != AgentRole.QA_VALIDATOR:
                # Each agent gets other agents as experts (except themselves and QA)
                for expert in agent_instances:
                    if expert.agent_id != agent.agent_id and expert.role != AgentRole.QA_VALIDATOR:
                        agent.add_expert(expert)
        
        self.teams[team_id] = team
        return team
    
    def get_team(self, team_id: str) -> AgentTeam:
        """Get a team by ID"""
        return self.teams.get(team_id)
    
    def execute_workflow(self, team_id: str, workflow_name: str, context: Dict[str, Any] = None) -> List[Dict[str, Any]]:
        """
        Execute a predefined workflow on a team
        
        Args:
            team_id: ID of the team to execute workflow on
            workflow_name: Name of the workflow (from config)
            context: Execution context
        
        Returns:
            List of workflow step results
        """
        team = self.get_team(team_id)
        if not team:
            raise ValueError(f"Team {team_id} not found")
        
        # Get workflow definition from config
        workflows = self.config.get('workflows', {})
        workflow_def = workflows.get(workflow_name)
        
        if not workflow_def:
            raise ValueError(f"Workflow {workflow_name} not found in config")
        
        # Execute the workflow
        steps = workflow_def.get('steps', [])
        return team.execute_workflow(steps)
    
    def get_system_stats(self) -> Dict[str, Any]:
        """Get statistics for the entire system"""
        return {
            "system_name": self.config.get('system', {}).get('name', 'Sistema Agéntico Local'),
            "version": self.config.get('system', {}).get('version', '1.0.0'),
            "total_teams": len(self.teams),
            "teams": [team.get_team_stats() for team in self.teams.values()],
            "ai_provider": self.config.get('ai_models', {}).get('default_provider', 'openai')
        }
    
    def list_workflows(self) -> List[str]:
        """List available workflows"""
        return list(self.config.get('workflows', {}).keys())


def main():
    """Main entry point for demonstration"""
    print("=" * 60)
    print("Sistema Agéntico Local - Autonomous AI Agent System")
    print("=" * 60)
    print()
    
    # Initialize system
    system = AgenticSystem()
    
    print("✓ Sistema inicializado")
    print(f"✓ Proveedor de IA: {system.config.get('ai_models', {}).get('default_provider', 'openai')}")
    print()
    
    # Create a specialized team for AI agency
    print("Creando equipo especializado para agencia de IA...")
    team = system.create_niche_team(
        team_id="ai_agency_team",
        niche="Agencia de Inteligencia Artificial y Automatizaciones"
    )
    
    print(f"✓ Equipo creado: {team.team_id}")
    print(f"✓ Nicho: {team.niche}")
    print(f"✓ Agentes: {len(team.agents)}")
    print()
    
    # Show team structure
    print("Estructura del equipo:")
    for agent_id, agent in team.agents.items():
        print(f"  - {agent.role.value}: {agent_id}")
        print(f"    Equipo de expertos: {len(agent.expert_team)} agentes")
    print()
    
    # List available workflows
    print("Workflows disponibles:")
    for workflow in system.list_workflows():
        print(f"  - {workflow}")
    print()
    
    # Show system stats
    stats = system.get_system_stats()
    print("Estadísticas del sistema:")
    print(f"  - Nombre: {stats['system_name']}")
    print(f"  - Versión: {stats['version']}")
    print(f"  - Equipos totales: {stats['total_teams']}")
    print()
    
    print("=" * 60)
    print("Sistema listo para ejecutar tareas!")
    print("=" * 60)
    print()
    print("Próximos pasos:")
    print("1. Configurar tus API keys en variables de entorno")
    print("2. Instalar N8N para automatizaciones: npm install -g n8n")
    print("3. Importar workflows desde /workflows/")
    print("4. Ejecutar ejemplos desde /examples/")
    print()


if __name__ == "__main__":
    main()
