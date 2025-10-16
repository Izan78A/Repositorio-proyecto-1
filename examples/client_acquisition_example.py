"""
Example: Client Acquisition Campaign
Demonstrates how to use the agentic system for acquiring clients
"""

import sys
from pathlib import Path

# Add parent directory to path
sys.path.insert(0, str(Path(__file__).parent.parent))

from main import AgenticSystem
from core import Task


def run_client_acquisition_example():
    """Run a complete client acquisition workflow"""
    
    print("=" * 70)
    print("Ejemplo: Campaña de Adquisición de Clientes")
    print("=" * 70)
    print()
    
    # Initialize system
    system = AgenticSystem()
    
    # Create specialized team
    team = system.create_niche_team(
        team_id="client_acquisition_team",
        niche="Adquisición de clientes para agencias de IA"
    )
    
    print(f"✓ Equipo creado: {team.niche}")
    print()
    
    # Define the campaign context
    context = {
        "industry": "Tecnología",
        "target_market": "Empresas medianas (50-500 empleados)",
        "service": "Automatización e Inteligencia Artificial",
        "geography": "España y Latinoamérica",
        "budget": "Medio",
        "timeline": "3 meses"
    }
    
    print("Contexto de la campaña:")
    for key, value in context.items():
        print(f"  - {key}: {value}")
    print()
    
    # Step 1: Market Research
    print("=" * 70)
    print("PASO 1: Investigación de Mercado")
    print("=" * 70)
    
    market_research_agent = team.get_agent("client_acquisition_team_market_research")
    
    market_task = Task(
        task_id="market_research_001",
        description="Realizar investigación de mercado profunda para identificar los mejores clientes potenciales",
        context=context
    )
    
    print("Ejecutando investigación de mercado...")
    market_result = market_research_agent.execute_task(market_task)
    print("\nResultado de investigación de mercado:")
    print("-" * 70)
    print(market_result)
    print()
    
    # Step 2: Content Creation
    print("=" * 70)
    print("PASO 2: Creación de Contenido")
    print("=" * 70)
    
    content_agent = team.get_agent("client_acquisition_team_content_creator")
    
    content_task = Task(
        task_id="content_creation_001",
        description="Crear contenido persuasivo para campaña de outreach en LinkedIn y email",
        context={
            **context,
            "market_research": market_result
        }
    )
    
    print("Creando contenido de marketing...")
    content_result = content_agent.execute_task(content_task)
    print("\nContenido creado:")
    print("-" * 70)
    print(content_result)
    print()
    
    # Step 3: Sales Strategy
    print("=" * 70)
    print("PASO 3: Estrategia de Ventas")
    print("=" * 70)
    
    sales_agent = team.get_agent("client_acquisition_team_sales_specialist")
    
    sales_task = Task(
        task_id="sales_strategy_001",
        description="Desarrollar estrategia de ventas y plan de prospección",
        context={
            **context,
            "market_research": market_result,
            "content": content_result
        }
    )
    
    print("Desarrollando estrategia de ventas...")
    sales_result = sales_agent.execute_task(sales_task)
    print("\nEstrategia de ventas:")
    print("-" * 70)
    print(sales_result)
    print()
    
    # Step 4: Technical Implementation
    print("=" * 70)
    print("PASO 4: Implementación Técnica")
    print("=" * 70)
    
    tech_agent = team.get_agent("client_acquisition_team_technical_expert")
    
    tech_task = Task(
        task_id="technical_impl_001",
        description="Diseñar automatización con N8N para ejecutar la campaña",
        context={
            **context,
            "sales_strategy": sales_result,
            "content": content_result
        }
    )
    
    print("Diseñando automatización...")
    tech_result = tech_agent.execute_task(tech_task)
    print("\nSolución técnica:")
    print("-" * 70)
    print(tech_result)
    print()
    
    # Step 5: Quality Assurance
    print("=" * 70)
    print("PASO 5: Validación de Calidad")
    print("=" * 70)
    
    qa_agent = team.get_agent("client_acquisition_team_qa_validator")
    
    qa_task = Task(
        task_id="qa_validation_001",
        description="Validar toda la campaña antes de ejecutar",
        context={
            "work": {
                "market_research": market_result,
                "content": content_result,
                "sales_strategy": sales_result,
                "technical_implementation": tech_result
            }
        }
    )
    
    print("Validando calidad de todos los componentes...")
    qa_result = qa_agent.execute_task(qa_task)
    print("\nResultado de validación:")
    print("-" * 70)
    print(qa_result.get("feedback", ""))
    print()
    
    if qa_result.get("approved", False):
        print("✓ ¡CAMPAÑA APROBADA! Lista para ejecutar")
    else:
        print("⚠ Campaña requiere revisión antes de ejecutar")
    
    print()
    print("=" * 70)
    print("Estadísticas del equipo:")
    print("=" * 70)
    
    stats = team.get_team_stats()
    for agent_stat in stats['agents']:
        print(f"\n{agent_stat['role']}:")
        print(f"  - Tareas completadas: {agent_stat['completed_tasks']}")
        print(f"  - Tareas fallidas: {agent_stat['failed_tasks']}")
        print(f"  - Equipo de expertos: {agent_stat['expert_team_size']} agentes")
    
    print()
    print("=" * 70)
    print("¡Ejemplo completado!")
    print("=" * 70)


if __name__ == "__main__":
    run_client_acquisition_example()
