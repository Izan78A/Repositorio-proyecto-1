# Sistema Agéntico Local - Guía Completa

## 📋 Descripción

Sistema agéntico local diseñado para crear agentes de inteligencia artificial autónomos especializados en nichos de mercado específicos. El sistema permite crear equipos de expertos GPT que colaboran entre sí, con validación de calidad integrada antes de entregar resultados al usuario.

## 🎯 Características Principales

- ✅ **Agentes Autónomos Especializados**: Cada agente es experto en un dominio específico
- ✅ **Equipos de Expertos GPT**: Los agentes consultan entre sí para mejorar resultados
- ✅ **Validación de Calidad (QA)**: Agente especializado valida todo antes de entregar al usuario
- ✅ **Integración con N8N**: Automatización sin código usando N8N (no Make)
- ✅ **Personalizable por Nicho**: Crea equipos especializados para cualquier nicho de mercado
- ✅ **Multi-Proveedor IA**: Soporte para OpenAI, Anthropic y otros

## 🏗️ Arquitectura del Sistema

```
Sistema Agéntico Local
│
├── Core Framework
│   ├── BaseAgent (clase base)
│   ├── AgentTeam (coordinador de equipos)
│   ├── Task (gestor de tareas)
│   └── AI Provider (integración con modelos IA)
│
├── Agentes Especializados
│   ├── Market Research Agent
│   ├── Content Creator Agent
│   ├── Sales Specialist Agent
│   ├── Technical Expert Agent
│   └── QA Validator Agent
│
├── Workflows N8N
│   ├── Client Acquisition
│   └── Content Creation
│
└── Examples
    ├── Client Acquisition Example
    └── Custom Niche Team Example
```

## 📦 Instalación

### Requisitos Previos

- Python 3.8+
- N8N (para automatizaciones)
- API Keys de OpenAI o Anthropic

### Pasos de Instalación

1. **Clonar el repositorio**
```bash
git clone https://github.com/Izan78A/Repositorio-proyecto-1.git
cd Repositorio-proyecto-1
```

2. **Instalar dependencias Python**
```bash
pip install -r requirements.txt
```

3. **Configurar variables de entorno**
```bash
# Crear archivo .env
echo "OPENAI_API_KEY=tu-api-key-aqui" > .env
# o
echo "ANTHROPIC_API_KEY=tu-api-key-aqui" > .env
```

4. **Instalar N8N (opcional pero recomendado)**
```bash
npm install -g n8n
```

## 🚀 Uso Rápido

### Ejecutar el Sistema Base

```python
from main import AgenticSystem

# Inicializar sistema
system = AgenticSystem()

# Crear equipo especializado
team = system.create_niche_team(
    team_id="mi_equipo",
    niche="Tu nicho de mercado aquí"
)

# Ver estadísticas
stats = system.get_system_stats()
print(stats)
```

### Ejecutar Ejemplos

```bash
# Ejemplo de adquisición de clientes
python examples/client_acquisition_example.py

# Ejemplo de equipo personalizado
python examples/custom_niche_team.py

# Demo del sistema
python main.py
```

## 🤖 Tipos de Agentes

### 1. Market Research Agent
**Especialidades:**
- Identificación de mercados objetivo
- Análisis de competencia
- Identificación de tendencias
- Análisis de datos de mercado
- Segmentación de clientes

### 2. Content Creator Agent
**Especialidades:**
- Copywriting persuasivo
- Optimización SEO
- Storytelling
- Creación de contenido viral
- Estrategias de contenido multicanal

### 3. Sales Specialist Agent
**Especialidades:**
- Prospección de clientes
- Estrategias de cierre
- Construcción de relaciones
- Negociación
- Seguimiento y retención

### 4. Technical Expert Agent
**Especialidades:**
- Diseño de sistemas
- Automatización con N8N
- Integración de APIs
- Desarrollo de workflows
- Optimización de procesos

### 5. QA Validator Agent
**Especialidades:**
- Validación de calidad
- Detección de errores
- Testing de soluciones
- Verificación de completitud
- Aseguramiento de estándares

## 🔄 Workflows con N8N

El sistema incluye plantillas de workflows para N8N que puedes importar:

### Importar Workflows

1. Iniciar N8N:
```bash
n8n start
```

2. Acceder a http://localhost:5678

3. Importar workflows desde `/workflows/`:
   - `n8n_client_acquisition.json` - Flujo de adquisición de clientes
   - `n8n_content_creation.json` - Flujo de creación de contenido

### Workflows Disponibles

- **Client Acquisition**: Flujo completo de investigación → contenido → ventas → QA
- **Content Creation**: Flujo de setup técnico → generación → validación

## ⚙️ Configuración

Edita `config.yaml` para personalizar:

```yaml
# Modelo de IA
ai_models:
  default_provider: "openai"  # o "anthropic"
  openai:
    model: "gpt-4"
    temperature: 0.7

# Agentes
agents:
  base_config:
    max_iterations: 10
    timeout: 300

# N8N Integration
n8n:
  enabled: true
  webhook_url: "http://localhost:5678/webhook"
```

## 💡 Ejemplos de Uso

### Crear Equipo para un Nicho Específico

```python
from main import AgenticSystem

system = AgenticSystem()

# Crear equipo para e-commerce de moda
team = system.create_niche_team(
    team_id="fashion_team",
    niche="E-commerce de moda sostenible",
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
```

### Ejecutar una Tarea

```python
from core import Task

# Obtener agente
agent = team.get_agent("fashion_team_market_research")

# Crear tarea
task = Task(
    task_id="task_001",
    description="Analizar mercado de moda sostenible en Europa",
    context={
        "target_audience": "Millennials conscientes",
        "geography": "Europa Occidental"
    }
)

# Ejecutar
result = agent.execute_task(task)
print(result)
```

### Validar con QA

```python
# Obtener validador QA
qa_agent = team.get_agent("fashion_team_qa_validator")

# Validar trabajo
validation = agent.validate_work(qa_agent, result)

if validation["approved"]:
    print("✓ Trabajo aprobado")
else:
    print("⚠ Requiere revisión:", validation["feedback"])
```

## 🎯 Casos de Uso

### 1. Agencia de Marketing
- Investigación de mercado automatizada
- Generación de contenido de marketing
- Estrategias de adquisición de clientes
- Validación antes de entregar al cliente

### 2. Consultoría de Negocios
- Análisis de industria y competencia
- Desarrollo de estrategias de negocio
- Planes de implementación técnica
- Control de calidad de deliverables

### 3. E-commerce
- Investigación de productos y tendencias
- Creación de descripciones y contenido
- Estrategias de ventas online
- Automatización de procesos

## 🔧 Personalización

### Crear un Nuevo Tipo de Agente

```python
from core.agent_framework import BaseAgent, AgentRole, Task, AgentStatus
from core.ai_provider import AIProvider

class CustomAgent(BaseAgent):
    def __init__(self, agent_id: str, ai_provider: AIProvider):
        super().__init__(agent_id, AgentRole.CUSTOM, {})
        self.ai_provider = ai_provider
        self.expertise = ["skill1", "skill2", "skill3"]
    
    def execute_task(self, task: Task):
        self.status = AgentStatus.WORKING
        # Tu lógica personalizada aquí
        result = self.ai_provider.generate_response(
            task.description,
            task.context
        )
        task.result = result
        task.status = AgentStatus.COMPLETED
        self.status = AgentStatus.IDLE
        return result
```

### Crear Workflow Personalizado

Edita `config.yaml`:

```yaml
workflows:
  mi_workflow_custom:
    steps:
      - agent: "market_research"
        task: "Tu tarea aquí"
      - agent: "custom_agent"
        task: "Otra tarea"
      - agent: "qa_validator"
        task: "Validar todo"
```

## 📊 Monitoreo y Estadísticas

```python
# Estadísticas del sistema
system_stats = system.get_system_stats()

# Estadísticas de un equipo
team_stats = team.get_team_stats()

# Estadísticas de un agente
agent_stats = agent.get_stats()
```

## 🔐 Seguridad

- **API Keys**: Nunca commitear keys en el código. Usar variables de entorno.
- **Datos Sensibles**: Los agentes no almacenan datos entre sesiones por defecto.
- **Validación**: El agente QA siempre valida antes de entregar al usuario.

## 🤝 Contribución

Este es un sistema base que puedes extender:

1. Añadir nuevos tipos de agentes
2. Crear workflows específicos para tu industria
3. Integrar con más proveedores de IA
4. Añadir métricas y analytics
5. Crear interfaces de usuario

## 📝 Roadmap

- [ ] Interfaz web para gestionar equipos
- [ ] Integración con más proveedores de IA
- [ ] Sistema de memoria persistente para agentes
- [ ] Analytics y reportes avanzados
- [ ] Templates para más industrias
- [ ] API REST para integración externa

## 📄 Licencia

MIT License - Libre para uso personal y comercial

## 📞 Soporte

Para preguntas y soporte:
- Abre un issue en GitHub
- Consulta la documentación en `/docs/`
- Revisa los ejemplos en `/examples/`

---

**Construido para ayudarte a conseguir clientes para tu agencia de IA y automatizaciones** 🚀
