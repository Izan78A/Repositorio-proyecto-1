# Arquitectura y Flujo del Sistema

## 🏗️ Diagrama de Arquitectura

```
┌─────────────────────────────────────────────────────────────────┐
│                    SISTEMA AGÉNTICO LOCAL                        │
│                                                                   │
│  ┌────────────────────────────────────────────────────────┐     │
│  │              AGENTES ESPECIALIZADOS                     │     │
│  │                                                         │     │
│  │  ┌─────────────┐  ┌─────────────┐  ┌─────────────┐   │     │
│  │  │   Market    │  │  Content    │  │    Sales    │   │     │
│  │  │  Research   │◄─┤  Creator    │◄─┤ Specialist  │   │     │
│  │  │   Agent     │  │   Agent     │  │   Agent     │   │     │
│  │  └──────┬──────┘  └──────┬──────┘  └──────┬──────┘   │     │
│  │         │                │                │            │     │
│  │         └────────────────┼────────────────┘            │     │
│  │                          ▼                             │     │
│  │                  ┌──────────────┐                      │     │
│  │                  │  Technical   │                      │     │
│  │                  │   Expert     │                      │     │
│  │                  │   Agent      │                      │     │
│  │                  └──────┬───────┘                      │     │
│  │                         │                              │     │
│  │                         ▼                              │     │
│  │                  ┌──────────────┐                      │     │
│  │                  │      QA      │                      │     │
│  │                  │  Validator   │◄─── Valida Todo     │     │
│  │                  │   Agent      │                      │     │
│  │                  └──────────────┘                      │     │
│  └────────────────────────────────────────────────────────┘     │
│                                                                   │
│  ┌────────────────────────────────────────────────────────┐     │
│  │                   CORE FRAMEWORK                        │     │
│  │                                                         │     │
│  │  ┌──────────┐  ┌──────────┐  ┌──────────────────┐    │     │
│  │  │BaseAgent │  │AgentTeam │  │   AI Provider    │    │     │
│  │  │Framework │  │ Manager  │  │ (OpenAI/Claude)  │    │     │
│  │  └──────────┘  └──────────┘  └──────────────────┘    │     │
│  └────────────────────────────────────────────────────────┘     │
│                                                                   │
└───────────────────────────┬───────────────────────────────────────┘
                           │
        ┌──────────────────┼──────────────────┐
        │                  │                  │
        ▼                  ▼                  ▼
   ┌─────────┐      ┌──────────┐      ┌──────────┐
   │   N8N   │      │   API    │      │  Python  │
   │Workflows│      │  Server  │      │ Scripts  │
   └─────────┘      └──────────┘      └──────────┘
```

## 🔄 Flujo de Trabajo Completo

### Campaña de Adquisición de Clientes

```
1. INICIO
   └─► Usuario define nicho de mercado
       │
       ▼
2. INVESTIGACIÓN DE MERCADO
   └─► Market Research Agent analiza:
       │  • Mercado objetivo
       │  • Competidores
       │  • Oportunidades
       │  • [Consulta expertos GPT]
       │
       ▼
3. CREACIÓN DE CONTENIDO
   └─► Content Creator Agent genera:
       │  • Emails de outreach
       │  • Posts de LinkedIn
       │  • Scripts de llamadas
       │  • [Consulta expertos GPT]
       │  • [Usa resultados paso 2]
       │
       ▼
4. ESTRATEGIA DE VENTAS
   └─► Sales Specialist Agent diseña:
       │  • Plan de prospección
       │  • Estrategia de cierre
       │  • Seguimiento
       │  • [Consulta expertos GPT]
       │  • [Usa resultados pasos 2 y 3]
       │
       ▼
5. IMPLEMENTACIÓN TÉCNICA
   └─► Technical Expert Agent crea:
       │  • Workflow de N8N
       │  • Automatizaciones
       │  • Integraciones
       │  • [Consulta expertos GPT]
       │  • [Usa resultados pasos 2-4]
       │
       ▼
6. VALIDACIÓN DE CALIDAD
   └─► QA Validator Agent verifica:
       │  • Completitud
       │  • Calidad
       │  • Coherencia
       │  • Errores
       │  • Cumplimiento objetivos
       │
       ├─► SI APROBADO ──────┐
       │                     │
       └─► SI RECHAZADO      │
           └─► Volver a paso │
               correspondiente│
                             ▼
7. ENTREGA AL USUARIO
   └─► Campaña completa validada
       • Lista para ejecutar
       • Sin errores
       • Calidad asegurada
```

## 🤝 Sistema de Consulta de Expertos

```
Agent Principal
      │
      ├─► Tarea recibida
      │
      ├─► Consulta Experto 1 ──┐
      │                          │
      ├─► Consulta Experto 2 ──┼─► Recopila consejos
      │                          │
      └─► Consulta Experto 3 ──┘
              │
              ▼
      Combina conocimiento
              │
              ▼
      Genera solución mejorada
              │
              ▼
      Envía a QA Validator
              │
              ▼
      Resultado final
```

## 🔌 Integración N8N

```
┌─────────────────────────────────────────────────────────┐
│                    WORKFLOW N8N                          │
│                                                           │
│  [Webhook]                                               │
│      │                                                    │
│      ├─► Datos de entrada                               │
│      │                                                    │
│      ▼                                                    │
│  [Nodo Python API]                                       │
│      │                                                    │
│      ├─► POST /execute                                   │
│      ├─► {agent_type: "market_research"}                │
│      │                                                    │
│      ▼                                                    │
│  [Sistema Agéntico]                                      │
│      │                                                    │
│      ├─► Ejecuta agente                                 │
│      ├─► Consulta expertos                              │
│      ├─► Genera resultado                               │
│      │                                                    │
│      ▼                                                    │
│  [Procesar Resultado]                                    │
│      │                                                    │
│      ├─► Enviar email                                    │
│      ├─► Guardar en CRM                                 │
│      ├─► Notificar Slack                                │
│      │                                                    │
│      ▼                                                    │
│  [Response]                                              │
│                                                           │
└─────────────────────────────────────────────────────────┘
```

## 📊 Flujo de Datos

```
Usuario Input
    │
    ▼
┌─────────────┐
│   Config    │
│  (YAML)     │──┐
└─────────────┘  │
                 │
┌─────────────┐  │
│  AI Model   │  │
│  (GPT/Claude)│◄─┤
└─────────────┘  │
                 │
┌─────────────┐  │
│   Agent     │  │
│   Team      │◄─┘
└──────┬──────┘
       │
       ├─► Task Execution
       │
       ├─► Expert Consultation
       │
       └─► QA Validation
           │
           ▼
       Results
           │
           ├─► API Response
           │
           ├─► N8N Workflow
           │
           └─► User Output
```

## 🎯 Ejemplo Práctico: Flujo Real

```
INPUT: "Necesito 10 clientes para mi agencia de IA"

PASO 1 - Market Research Agent:
├─► Analiza mercado de agencias que necesitan IA
├─► Identifica sectores prometedores
├─► Lista competidores
└─► OUTPUT: Reporte de mercado con 10 prospectos ideales

PASO 2 - Content Creator Agent:
├─► Toma datos de investigación
├─► Consulta a Market Research como experto
├─► Genera 3 emails personalizados por prospecto
└─► OUTPUT: 30 emails listos para enviar

PASO 3 - Sales Specialist Agent:
├─► Revisa contenido creado
├─► Consulta a ambos agentes anteriores
├─► Diseña secuencia de seguimiento
└─► OUTPUT: Plan de prospección de 30 días

PASO 4 - Technical Expert Agent:
├─► Toma plan de ventas
├─► Diseña workflow de N8N
├─► Configura automatizaciones
└─► OUTPUT: Workflow N8N listo para importar

PASO 5 - QA Validator Agent:
├─► Valida investigación: ✓
├─► Valida contenido: ✓
├─► Valida estrategia: ✓
├─► Valida implementación: ✓
└─► OUTPUT: "APROBADO - Todo listo para ejecutar"

RESULTADO FINAL:
✅ Estrategia completa de adquisición
✅ 30 emails personalizados
✅ Plan de seguimiento de 30 días
✅ Automatización N8N configurada
✅ Validado y listo para usar
```

## 🔐 Seguridad y Validación

```
Cada Tarea
    │
    ├─► Validación de Input
    │
    ├─► Ejecución del Agente
    │   └─► Max iterations limit
    │   └─► Timeout protection
    │   └─► Error handling
    │
    ├─► Consulta de Expertos
    │   └─► Depth limit (evita recursión)
    │
    ├─► Generación de Resultado
    │
    └─► Validación QA
        │
        ├─► SI pasa ──► Entregar
        │
        └─► SI falla ──► Revisar y re-ejecutar
```

## 🚀 Escalabilidad

```
1 Nicho = 1 Team
    │
    ├─► 5 Agentes especializados
    ├─► Sistema de expertos
    └─► QA integrada

Múltiples Nichos:

Sistema Principal
    │
    ├─► Team 1: E-commerce Fashion
    │   ├─► 5 Agentes
    │   └─► Workflows específicos
    │
    ├─► Team 2: SaaS B2B
    │   ├─► 5 Agentes
    │   └─► Workflows específicos
    │
    └─► Team 3: Consulting Agencies
        ├─► 5 Agentes
        └─► Workflows específicos

Todos comparten:
- Core Framework
- AI Providers
- N8N Integration
```

---

**Este diagrama muestra cómo todos los componentes trabajan juntos para crear un sistema completo de adquisición de clientes automatizado y validado.**
