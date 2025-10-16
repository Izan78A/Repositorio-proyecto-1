# Sistema Agéntico Local 🤖

> Sistema de agentes de IA autónomos especializados para conseguir clientes para tu agencia de inteligencia artificial y automatizaciones

## 🚀 ¿Qué es esto?

Un sistema completo de agentes de inteligencia artificial que trabajan en equipo para ayudarte a conseguir clientes. Cada agente es un experto en su área y colaboran entre sí, con validación de calidad integrada antes de entregar resultados.

## ✨ Características Principales

- 🧠 **Agentes Especializados**: Investigación de mercado, creación de contenido, ventas, implementación técnica
- 🤝 **Equipos de Expertos**: Los agentes se consultan entre sí para mejorar resultados
- ✅ **Control de Calidad**: Agente QA valida todo antes de entregar
- 🔄 **Automatización con N8N**: Workflows sin código (no Make)
- 🎯 **Personalizable**: Crea equipos especializados para cualquier nicho de mercado
- 🔌 **Multi-Proveedor**: Soporte para OpenAI, Anthropic y otros

## 📦 Instalación Rápida

```bash
# 1. Clonar repositorio
git clone https://github.com/Izan78A/Repositorio-proyecto-1.git
cd Repositorio-proyecto-1

# 2. Instalar dependencias
pip install -r requirements.txt

# 3. Configurar API key
echo "OPENAI_API_KEY=tu-api-key" > .env

# 4. Ejecutar demo
python main.py
```

## 🎯 Uso Rápido

### Ejecutar Ejemplo de Adquisición de Clientes

```bash
python examples/client_acquisition_example.py
```

### Crear Tu Propio Equipo Especializado

```python
from main import AgenticSystem

# Inicializar sistema
system = AgenticSystem()

# Crear equipo para tu nicho
team = system.create_niche_team(
    team_id="mi_equipo",
    niche="Tu nicho de mercado aquí"
)

# ¡Listo para trabajar!
```

## 🤖 Agentes Disponibles

| Agente | Especialidad | Funciones |
|--------|-------------|-----------|
| **Market Research** | Investigación de mercado | Análisis de mercado, identificación de clientes, competencia |
| **Content Creator** | Creación de contenido | Copywriting, SEO, contenido de marketing |
| **Sales Specialist** | Ventas | Prospección, estrategias de cierre, seguimiento |
| **Technical Expert** | Implementación técnica | Automatización N8N, integraciones, desarrollo |
| **QA Validator** | Control de calidad | Validación, detección de errores, aseguramiento |

## 🔄 Integración con N8N

El sistema incluye workflows pre-configurados para N8N:

1. **Instalar N8N**: `npm install -g n8n`
2. **Iniciar N8N**: `n8n start`
3. **Importar workflows** desde `/workflows/`
4. **¡Automatizar!**

Ver [Guía de N8N](docs/N8N_INTEGRATION.md) para más detalles.

## 📚 Documentación

- 📖 [Guía Completa](docs/GUIA_COMPLETA.md) - Documentación detallada del sistema
- 🔗 [Integración N8N](docs/N8N_INTEGRATION.md) - Cómo usar N8N con el sistema
- 💡 [Ejemplos](examples/) - Ejemplos de uso práctico

## 🎓 Ejemplos

### Ejemplo 1: Campaña de Adquisición de Clientes

```python
# Ver: examples/client_acquisition_example.py
# Flujo completo: Investigación → Contenido → Ventas → QA
```

### Ejemplo 2: Equipo Personalizado

```python
# Ver: examples/custom_niche_team.py
# Crear equipo para cualquier nicho de mercado
```

## 🛠️ Estructura del Proyecto

```
Repositorio-proyecto-1/
├── core/                    # Framework base
│   ├── agent_framework.py   # Clases base de agentes
│   └── ai_provider.py       # Integración con IA
├── agents/                  # Agentes especializados
│   └── specialized_agents.py
├── workflows/               # Workflows de N8N
│   ├── n8n_client_acquisition.json
│   └── n8n_content_creation.json
├── examples/                # Ejemplos de uso
│   ├── client_acquisition_example.py
│   └── custom_niche_team.py
├── docs/                    # Documentación
│   ├── GUIA_COMPLETA.md
│   └── N8N_INTEGRATION.md
├── config.yaml              # Configuración del sistema
├── requirements.txt         # Dependencias Python
└── main.py                  # Punto de entrada principal
```

## ⚙️ Configuración

Edita `config.yaml` para personalizar:

- Proveedor de IA (OpenAI, Anthropic)
- Modelos y parámetros
- Configuración de agentes
- Workflows predefinidos
- Integración N8N

## 🎯 Casos de Uso

### Para Agencias de IA
- Automatizar prospección de clientes
- Generar contenido de marketing
- Crear estrategias de ventas personalizadas
- Validar deliverables antes de entregar

### Para Consultores
- Análisis de mercado automatizado
- Desarrollo de estrategias de negocio
- Implementación técnica de soluciones
- Control de calidad de proyectos

### Para E-commerce
- Investigación de productos y tendencias
- Creación de descripciones optimizadas
- Estrategias de ventas online
- Automatización de procesos

## 🚀 Roadmap

- [ ] Interfaz web para gestionar equipos
- [ ] Más proveedores de IA (Google, Mistral)
- [ ] Sistema de memoria persistente
- [ ] Analytics y reportes avanzados
- [ ] Templates para más industrias
- [ ] API REST completa

## 🤝 Contribución

Las contribuciones son bienvenidas. Por favor:

1. Fork el proyecto
2. Crea una rama para tu feature
3. Commit tus cambios
4. Push a la rama
5. Abre un Pull Request

## 📄 Licencia

MIT License - Libre para uso personal y comercial

## 💬 Soporte

- 📖 Consulta la [documentación completa](docs/GUIA_COMPLETA.md)
- 💡 Revisa los [ejemplos](examples/)
- 🐛 Reporta issues en GitHub

---

**Desarrollado para ayudarte a conseguir clientes para tu agencia de IA y automatizaciones** 🎯🚀
