"""
Specialized Agent Implementations
Each agent is an expert in a specific domain
"""

from typing import Dict, Any
from core.agent_framework import BaseAgent, AgentRole, Task, AgentStatus
from core.ai_provider import AIProvider


class MarketResearchAgent(BaseAgent):
    """Expert in market research and analysis"""
    
    def __init__(self, agent_id: str, ai_provider: AIProvider, config: Dict[str, Any] = None):
        super().__init__(agent_id, AgentRole.MARKET_RESEARCH, config)
        self.ai_provider = ai_provider
        self.expertise = [
            "Identificación de mercados objetivo",
            "Análisis de competencia",
            "Identificación de tendencias",
            "Análisis de datos de mercado",
            "Segmentación de clientes"
        ]
    
    def execute_task(self, task: Task) -> Any:
        """Execute market research task"""
        self.status = AgentStatus.WORKING
        task.status = AgentStatus.WORKING
        
        try:
            # Build comprehensive prompt
            prompt = f"""
Eres un experto en investigación de mercado con las siguientes especialidades:
{', '.join(self.expertise)}

Tarea: {task.description}

Por favor, proporciona un análisis detallado de mercado que incluya:
1. Identificación del mercado objetivo
2. Análisis de competidores principales
3. Oportunidades y amenazas
4. Recomendaciones estratégicas

Contexto adicional: {task.context}
"""
            
            # Get expert consultations if available
            if self.expert_team:
                consultations = self.consult_experts(
                    "¿Qué insights puedes proporcionar para esta investigación de mercado?",
                    task.context
                )
                prompt += f"\n\nConsultas de expertos:\n{consultations}"
            
            # Generate response using AI
            result = self.ai_provider.generate_response(prompt, task.context)
            
            task.result = result
            task.status = AgentStatus.COMPLETED
            self.status = AgentStatus.IDLE
            
            self.log_task(task)
            return result
            
        except Exception as e:
            task.status = AgentStatus.FAILED
            task.errors.append(str(e))
            self.status = AgentStatus.IDLE
            raise


class ContentCreatorAgent(BaseAgent):
    """Expert in creating marketing content"""
    
    def __init__(self, agent_id: str, ai_provider: AIProvider, config: Dict[str, Any] = None):
        super().__init__(agent_id, AgentRole.CONTENT_CREATOR, config)
        self.ai_provider = ai_provider
        self.expertise = [
            "Copywriting persuasivo",
            "Optimización SEO",
            "Storytelling",
            "Creación de contenido viral",
            "Estrategias de contenido multicanal"
        ]
    
    def execute_task(self, task: Task) -> Any:
        """Execute content creation task"""
        self.status = AgentStatus.WORKING
        task.status = AgentStatus.WORKING
        
        try:
            prompt = f"""
Eres un experto en creación de contenido de marketing con especialidades en:
{', '.join(self.expertise)}

Tarea: {task.description}

Crea contenido de alta calidad que:
1. Capture la atención del público objetivo
2. Comunique claramente el valor propuesto
3. Incluya llamadas a la acción efectivas
4. Esté optimizado para conversión

Contexto: {task.context}
"""
            
            if self.expert_team:
                consultations = self.consult_experts(
                    "¿Qué elementos deberían incluirse en este contenido?",
                    task.context
                )
                prompt += f"\n\nConsultas de expertos:\n{consultations}"
            
            result = self.ai_provider.generate_response(prompt, task.context)
            
            task.result = result
            task.status = AgentStatus.COMPLETED
            self.status = AgentStatus.IDLE
            
            self.log_task(task)
            return result
            
        except Exception as e:
            task.status = AgentStatus.FAILED
            task.errors.append(str(e))
            self.status = AgentStatus.IDLE
            raise


class SalesSpecialistAgent(BaseAgent):
    """Expert in sales strategies and client acquisition"""
    
    def __init__(self, agent_id: str, ai_provider: AIProvider, config: Dict[str, Any] = None):
        super().__init__(agent_id, AgentRole.SALES_SPECIALIST, config)
        self.ai_provider = ai_provider
        self.expertise = [
            "Prospección de clientes",
            "Estrategias de cierre",
            "Construcción de relaciones",
            "Negociación",
            "Seguimiento y retención"
        ]
    
    def execute_task(self, task: Task) -> Any:
        """Execute sales task"""
        self.status = AgentStatus.WORKING
        task.status = AgentStatus.WORKING
        
        try:
            prompt = f"""
Eres un experto en ventas y adquisición de clientes con especialidades en:
{', '.join(self.expertise)}

Tarea: {task.description}

Desarrolla una estrategia de ventas que incluya:
1. Métodos de prospección efectivos
2. Estrategias de acercamiento inicial
3. Técnicas de cierre
4. Plan de seguimiento
5. KPIs para medir éxito

Contexto: {task.context}
"""
            
            if self.expert_team:
                consultations = self.consult_experts(
                    "¿Qué estrategias de ventas recomiendas para este caso?",
                    task.context
                )
                prompt += f"\n\nConsultas de expertos:\n{consultations}"
            
            result = self.ai_provider.generate_response(prompt, task.context)
            
            task.result = result
            task.status = AgentStatus.COMPLETED
            self.status = AgentStatus.IDLE
            
            self.log_task(task)
            return result
            
        except Exception as e:
            task.status = AgentStatus.FAILED
            task.errors.append(str(e))
            self.status = AgentStatus.IDLE
            raise


class TechnicalExpertAgent(BaseAgent):
    """Expert in technical implementation and automation"""
    
    def __init__(self, agent_id: str, ai_provider: AIProvider, config: Dict[str, Any] = None):
        super().__init__(agent_id, AgentRole.TECHNICAL_EXPERT, config)
        self.ai_provider = ai_provider
        self.expertise = [
            "Diseño de sistemas",
            "Automatización con N8N",
            "Integración de APIs",
            "Desarrollo de workflows",
            "Optimización de procesos"
        ]
    
    def execute_task(self, task: Task) -> Any:
        """Execute technical task"""
        self.status = AgentStatus.WORKING
        task.status = AgentStatus.WORKING
        
        try:
            prompt = f"""
Eres un experto técnico especializado en:
{', '.join(self.expertise)}

Tarea: {task.description}

Proporciona una solución técnica que incluya:
1. Arquitectura del sistema
2. Flujos de automatización (N8N)
3. Integraciones necesarias
4. Pasos de implementación
5. Consideraciones de escalabilidad

Contexto: {task.context}
"""
            
            if self.expert_team:
                consultations = self.consult_experts(
                    "¿Qué soluciones técnicas recomiendas?",
                    task.context
                )
                prompt += f"\n\nConsultas de expertos:\n{consultations}"
            
            result = self.ai_provider.generate_response(prompt, task.context)
            
            task.result = result
            task.status = AgentStatus.COMPLETED
            self.status = AgentStatus.IDLE
            
            self.log_task(task)
            return result
            
        except Exception as e:
            task.status = AgentStatus.FAILED
            task.errors.append(str(e))
            self.status = AgentStatus.IDLE
            raise


class QAValidatorAgent(BaseAgent):
    """Expert in quality assurance and validation"""
    
    def __init__(self, agent_id: str, ai_provider: AIProvider, config: Dict[str, Any] = None):
        super().__init__(agent_id, AgentRole.QA_VALIDATOR, config)
        self.ai_provider = ai_provider
        self.expertise = [
            "Validación de calidad",
            "Detección de errores",
            "Testing de soluciones",
            "Verificación de completitud",
            "Aseguramiento de estándares"
        ]
    
    def execute_task(self, task: Task) -> Any:
        """Execute validation task"""
        self.status = AgentStatus.VALIDATING
        task.status = AgentStatus.VALIDATING
        
        try:
            work_to_validate = task.context.get("work", "")
            
            prompt = f"""
Eres un experto en control de calidad con especialidades en:
{', '.join(self.expertise)}

Tarea: Validar el siguiente trabajo antes de entregarlo al usuario.

Trabajo a validar:
{work_to_validate}

Realiza una revisión exhaustiva verificando:
1. Completitud de la solución
2. Calidad y precisión
3. Coherencia y claridad
4. Ausencia de errores
5. Cumplimiento de objetivos

Proporciona:
- Lista de problemas encontrados (si hay)
- Recomendaciones de mejora
- Aprobación final (SÍ/NO)

Contexto: {task.context}
"""
            
            result = self.ai_provider.generate_response(prompt, task.context)
            
            # Parse validation result
            validation_result = {
                "approved": "aprobado" in result.lower() or "sí" in result.lower(),
                "feedback": result,
                "validated_at": task.created_at.isoformat()
            }
            
            task.result = validation_result
            task.status = AgentStatus.COMPLETED
            self.status = AgentStatus.IDLE
            
            self.log_task(task)
            return validation_result
            
        except Exception as e:
            task.status = AgentStatus.FAILED
            task.errors.append(str(e))
            self.status = AgentStatus.IDLE
            raise
