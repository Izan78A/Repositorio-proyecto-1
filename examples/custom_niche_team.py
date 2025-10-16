"""
Example: Create Custom Niche Team
Shows how to create a team specialized in a specific market niche
"""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent))

from main import AgenticSystem
from core import Task


def create_custom_niche_team():
    """Create a team for a specific market niche"""
    
    print("=" * 70)
    print("Ejemplo: Crear Equipo Especializado en Nicho de Mercado")
    print("=" * 70)
    print()
    
    # Initialize system
    system = AgenticSystem()
    
    # Define your niche
    niche = "E-commerce de moda sostenible"
    
    print(f"Creando equipo especializado en: {niche}")
    print()
    
    # Create team with specific configuration
    team = system.create_niche_team(
        team_id="ecommerce_fashion_team",
        niche=niche,
        team_config={
            "agents": [
                "market_research",
                "content_creator",
                "sales_specialist",
                "technical_expert",
                "qa_validator"
            ]
        }
    )
    
    print("✓ Equipo creado exitosamente")
    print()
    
    # Show team composition
    print("Composición del equipo:")
    print("-" * 70)
    for agent_id, agent in team.agents.items():
        print(f"\n{agent.role.value}:")
        print(f"  ID: {agent_id}")
        print(f"  Expertos disponibles: {len(agent.expert_team)}")
        
        if hasattr(agent, 'expertise'):
            print(f"  Especialidades:")
            for skill in agent.expertise:
                print(f"    • {skill}")
    
    print()
    print("=" * 70)
    print("Ejecutando tarea de ejemplo...")
    print("=" * 70)
    print()
    
    # Example task: Create marketing strategy
    market_research = team.get_agent("ecommerce_fashion_team_market_research")
    
    task = Task(
        task_id="niche_analysis_001",
        description="Analizar el mercado de e-commerce de moda sostenible y identificar oportunidades",
        context={
            "target_audience": "Millennials y Gen Z conscientes del medio ambiente",
            "geography": "Europa Occidental",
            "competitors": "Patagonia, Reformation, Everlane",
            "unique_value": "Transparencia total en cadena de suministro"
        }
    )
    
    print("Tarea: Análisis de mercado")
    print(f"Agente: {market_research.role.value}")
    print()
    
    result = market_research.execute_task(task)
    
    print("Resultado:")
    print("-" * 70)
    print(result)
    print()
    
    # Show statistics
    stats = team.get_team_stats()
    print("=" * 70)
    print("Estadísticas del equipo:")
    print("=" * 70)
    print(f"Equipo: {stats['team_id']}")
    print(f"Nicho: {stats['niche']}")
    print(f"Total de agentes: {stats['agent_count']}")
    print(f"Validador QA: {'✓' if stats['has_qa'] else '✗'}")
    print()
    
    print("=" * 70)
    print("¡Ejemplo completado!")
    print("=" * 70)


if __name__ == "__main__":
    create_custom_niche_team()
