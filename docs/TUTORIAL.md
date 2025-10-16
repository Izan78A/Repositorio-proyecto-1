# Tutorial: Crea Tu Primer Equipo de Agentes

## 🎯 Objetivo

En este tutorial aprenderás a crear tu primer equipo de agentes especializados para adquirir clientes para tu agencia de IA.

## 📝 Requisitos Previos

- Sistema instalado y funcionando (ver [SETUP.md](SETUP.md))
- API key configurada en `.env`
- Python 3.8+

## 🚀 Paso 1: Crear el Script Base

Crea un archivo `mi_primer_equipo.py`:

```python
from main import AgenticSystem
from core import Task

# Inicializar el sistema
system = AgenticSystem()
print("✓ Sistema inicializado")
```

## 👥 Paso 2: Crear un Equipo Especializado

Define tu nicho y crea el equipo:

```python
# Definir tu nicho de mercado
MI_NICHO = "Agencias de marketing digital que quieren integrar IA"

# Crear equipo especializado
team = system.create_niche_team(
    team_id="marketing_ai_team",
    niche=MI_NICHO
)

print(f"✓ Equipo creado para: {MI_NICHO}")
print(f"✓ Agentes en el equipo: {len(team.agents)}")
```

## 🔍 Paso 3: Investigación de Mercado

Usa el agente de investigación de mercado:

```python
# Obtener el agente de investigación
market_agent = team.get_agent("marketing_ai_team_market_research")

# Crear tarea de investigación
market_task = Task(
    task_id="research_001",
    description="Identificar las 10 mejores agencias de marketing en España que podrían beneficiarse de IA",
    context={
        "geography": "España",
        "size": "10-50 empleados",
        "services": "Marketing digital, redes sociales, contenido",
        "pain_points": "Procesos manuales, escalabilidad limitada"
    }
)

# Ejecutar investigación
print("\n🔍 Ejecutando investigación de mercado...")
market_result = market_agent.execute_task(market_task)
print(market_result)
```

## ✍️ Paso 4: Crear Contenido de Outreach

Usa el contenido generado para crear mensajes:

```python
# Obtener agente de contenido
content_agent = team.get_agent("marketing_ai_team_content_creator")

# Crear tarea de contenido
content_task = Task(
    task_id="content_001",
    description="Crear secuencia de emails para outreach en LinkedIn",
    context={
        "target": "Directores de agencias de marketing",
        "channel": "LinkedIn + Email",
        "value_prop": "Automatizar creación de contenido con IA",
        "cta": "Agendar demo de 15 minutos",
        "market_research": market_result  # Usar resultados anteriores
    }
)

# Generar contenido
print("\n✍️ Generando contenido de outreach...")
content_result = content_agent.execute_task(content_task)
print(content_result)
```

## 💰 Paso 5: Desarrollar Estrategia de Ventas

Crea tu estrategia de prospección:

```python
# Obtener agente de ventas
sales_agent = team.get_agent("marketing_ai_team_sales_specialist")

# Crear estrategia
sales_task = Task(
    task_id="sales_001",
    description="Desarrollar estrategia de prospección y cierre",
    context={
        "target_clients": 20,
        "timeline": "30 días",
        "budget": "Bajo (principalmente tiempo)",
        "channels": ["LinkedIn", "Email", "Llamadas"],
        "content": content_result
    }
)

print("\n💰 Desarrollando estrategia de ventas...")
sales_result = sales_agent.execute_task(sales_task)
print(sales_result)
```

## 🔧 Paso 6: Implementación Técnica con N8N

Automatiza tu proceso:

```python
# Obtener agente técnico
tech_agent = team.get_agent("marketing_ai_team_technical_expert")

# Diseñar automatización
tech_task = Task(
    task_id="tech_001",
    description="Diseñar workflow de N8N para automatizar outreach",
    context={
        "requirements": [
            "Buscar prospectos en LinkedIn",
            "Enviar mensajes personalizados",
            "Hacer seguimiento automático",
            "Registrar interacciones en CRM"
        ],
        "tools": ["N8N", "LinkedIn API", "Gmail API"],
        "sales_strategy": sales_result
    }
)

print("\n🔧 Diseñando automatización técnica...")
tech_result = tech_agent.execute_task(tech_task)
print(tech_result)
```

## ✅ Paso 7: Validación de Calidad

Valida todo antes de ejecutar:

```python
# Obtener agente QA
qa_agent = team.get_agent("marketing_ai_team_qa_validator")

# Validar todo el trabajo
qa_task = Task(
    task_id="qa_001",
    description="Validar estrategia completa antes de ejecutar",
    context={
        "work": {
            "market_research": market_result,
            "content": content_result,
            "sales_strategy": sales_result,
            "technical_implementation": tech_result
        }
    }
)

print("\n✅ Validando calidad...")
qa_result = qa_agent.execute_task(qa_task)

if qa_result.get("approved", False):
    print("\n🎉 ¡ESTRATEGIA APROBADA!")
    print("Puedes proceder a ejecutar tu campaña de adquisición")
else:
    print("\n⚠️ Se encontraron problemas:")
    print(qa_result.get("feedback", ""))
```

## 📊 Paso 8: Ver Estadísticas

Revisa el rendimiento de tu equipo:

```python
# Obtener estadísticas
stats = team.get_team_stats()

print("\n" + "="*60)
print("📊 ESTADÍSTICAS DEL EQUIPO")
print("="*60)
print(f"Equipo: {stats['team_id']}")
print(f"Nicho: {stats['niche']}")
print(f"Agentes: {stats['agent_count']}")
print(f"Validador QA: {'✓' if stats['has_qa'] else '✗'}")
print()
print("Rendimiento por agente:")
for agent_stat in stats['agents']:
    print(f"\n  {agent_stat['role']}:")
    print(f"    - Tareas completadas: {agent_stat['completed_tasks']}")
    print(f"    - Tareas fallidas: {agent_stat['failed_tasks']}")
    print(f"    - Equipo de expertos: {agent_stat['expert_team_size']}")
```

## 💾 Script Completo

Guarda todo en `mi_primer_equipo.py`:

```python
"""
Mi Primer Equipo de Agentes - Tutorial Completo
Campaña de adquisición de clientes para agencia de IA
"""

from main import AgenticSystem
from core import Task

def main():
    print("="*60)
    print("MI PRIMER EQUIPO DE AGENTES")
    print("="*60)
    print()
    
    # 1. Inicializar sistema
    system = AgenticSystem()
    print("✓ Sistema inicializado")
    
    # 2. Crear equipo
    MI_NICHO = "Agencias de marketing digital que quieren integrar IA"
    team = system.create_niche_team(
        team_id="marketing_ai_team",
        niche=MI_NICHO
    )
    print(f"✓ Equipo creado: {MI_NICHO}")
    print()
    
    # 3. Investigación de mercado
    print("🔍 PASO 1: Investigación de Mercado")
    market_agent = team.get_agent("marketing_ai_team_market_research")
    market_task = Task(
        task_id="research_001",
        description="Identificar mejores agencias de marketing en España para IA",
        context={
            "geography": "España",
            "size": "10-50 empleados",
            "services": "Marketing digital"
        }
    )
    market_result = market_agent.execute_task(market_task)
    print("✓ Investigación completada\n")
    
    # 4. Crear contenido
    print("✍️ PASO 2: Creación de Contenido")
    content_agent = team.get_agent("marketing_ai_team_content_creator")
    content_task = Task(
        task_id="content_001",
        description="Crear emails para outreach",
        context={
            "target": "Directores de marketing",
            "channel": "LinkedIn + Email"
        }
    )
    content_result = content_agent.execute_task(content_task)
    print("✓ Contenido creado\n")
    
    # 5. Estrategia de ventas
    print("💰 PASO 3: Estrategia de Ventas")
    sales_agent = team.get_agent("marketing_ai_team_sales_specialist")
    sales_task = Task(
        task_id="sales_001",
        description="Desarrollar estrategia de prospección",
        context={
            "target_clients": 20,
            "timeline": "30 días"
        }
    )
    sales_result = sales_agent.execute_task(sales_task)
    print("✓ Estrategia desarrollada\n")
    
    # 6. Validación QA
    print("✅ PASO 4: Validación de Calidad")
    qa_agent = team.get_agent("marketing_ai_team_qa_validator")
    qa_task = Task(
        task_id="qa_001",
        description="Validar toda la estrategia",
        context={
            "work": {
                "market_research": market_result,
                "content": content_result,
                "sales_strategy": sales_result
            }
        }
    )
    qa_result = qa_agent.execute_task(qa_task)
    
    if qa_result.get("approved", False):
        print("🎉 ¡ESTRATEGIA APROBADA!\n")
    else:
        print("⚠️ Requiere revisión\n")
    
    # 7. Estadísticas
    stats = team.get_team_stats()
    print("="*60)
    print("📊 RESUMEN FINAL")
    print("="*60)
    print(f"Tareas completadas: {sum(a['completed_tasks'] for a in stats['agents'])}")
    print(f"Agentes utilizados: {stats['agent_count']}")
    print()
    print("¡Tu equipo está listo para adquirir clientes! 🚀")

if __name__ == "__main__":
    main()
```

## 🎯 Ejecutar el Tutorial

```bash
python mi_primer_equipo.py
```

## 🚀 Próximos Pasos

Ahora que tienes tu primer equipo funcionando:

1. **Personaliza el nicho**: Cambia `MI_NICHO` a tu mercado objetivo
2. **Ajusta contextos**: Modifica los contextos de las tareas para tu caso
3. **Añade más pasos**: Incorpora más agentes en tu flujo
4. **Integra con N8N**: Automatiza la ejecución completa
5. **Mide resultados**: Implementa tracking de conversiones

## 💡 Tips Pro

- **Itera rápido**: Empieza simple y añade complejidad gradualmente
- **Usa el QA**: Siempre valida antes de ejecutar en producción
- **Guarda resultados**: Documenta lo que funciona bien
- **Experimenta**: Prueba diferentes prompts y contextos
- **Automatiza**: Usa N8N para ejecutar el flujo completo

## 📚 Recursos Adicionales

- [GUIA_COMPLETA.md](GUIA_COMPLETA.md) - Documentación completa
- [N8N_INTEGRATION.md](N8N_INTEGRATION.md) - Automatización avanzada
- [SETUP.md](SETUP.md) - Guía de instalación

---

**¡Felicidades! Has creado tu primer equipo de agentes para adquirir clientes** 🎉
