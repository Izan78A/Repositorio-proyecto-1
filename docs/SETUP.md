# Setup Guide - Sistema Agéntico Local

## 🚀 Instalación Paso a Paso

### 1. Clonar el Repositorio

```bash
git clone https://github.com/Izan78A/Repositorio-proyecto-1.git
cd Repositorio-proyecto-1
```

### 2. Instalar Dependencias Python

```bash
# Opción 1: Usar pip directamente
pip install -r requirements.txt

# Opción 2: Usar entorno virtual (recomendado)
python -m venv venv
source venv/bin/activate  # En Windows: venv\Scripts\activate
pip install -r requirements.txt
```

### 3. Configurar API Keys

Crea un archivo `.env` en la raíz del proyecto:

```bash
# Opción OpenAI
OPENAI_API_KEY=sk-tu-clave-aqui

# O Opción Anthropic
ANTHROPIC_API_KEY=sk-ant-tu-clave-aqui
```

**Nota**: Puedes obtener API keys en:
- OpenAI: https://platform.openai.com/api-keys
- Anthropic: https://console.anthropic.com/

### 4. Verificar Instalación

```bash
# Ejecutar el script de demostración
python main.py
```

Si ves el mensaje "Sistema listo para ejecutar tareas!", ¡está funcionando! 🎉

## 📋 Dependencias del Sistema

### Python (requerido)
- Python 3.8 o superior
- pip (gestor de paquetes)

### N8N (opcional pero recomendado)
Para automatizaciones avanzadas:

```bash
# Instalación global
npm install -g n8n

# O usando npx (sin instalación)
npx n8n
```

## 🎯 Primeros Pasos

### Script de Inicio Rápido

Usa el script interactivo:

```bash
./quickstart.sh
```

Este script te permite:
1. Ejecutar demo del sistema
2. Probar ejemplo de adquisición de clientes
3. Crear equipos personalizados
4. Iniciar API server
5. Ver documentación

### Opción Manual

```bash
# Demo del sistema
python main.py

# Ejemplo de adquisición de clientes
python examples/client_acquisition_example.py

# Ejemplo de equipo personalizado
python examples/custom_niche_team.py

# Iniciar API server
python examples/api_server.py
```

## 🔧 Configuración Personalizada

### Editar config.yaml

Personaliza el sistema editando `config.yaml`:

```yaml
# Cambiar proveedor de IA
ai_models:
  default_provider: "openai"  # o "anthropic"

# Ajustar parámetros del modelo
openai:
  model: "gpt-4"  # o "gpt-3.5-turbo" para más económico
  temperature: 0.7
  max_tokens: 2000

# Configurar agentes
agents:
  base_config:
    max_iterations: 10
    timeout: 300
```

## 🌐 Configuración de N8N

### 1. Iniciar N8N

```bash
n8n start
```

Accede a: http://localhost:5678

### 2. Importar Workflows

1. En N8N, click en "Workflows" → "Import from File"
2. Importa los archivos de `/workflows/`:
   - `n8n_client_acquisition.json`
   - `n8n_content_creation.json`

### 3. Activar Workflows

1. Abre cada workflow importado
2. Click en "Active" para activarlo
3. ¡Listo para recibir webhooks!

## 🔌 Integración API + N8N

### 1. Iniciar API Server

```bash
python examples/api_server.py
```

El servidor estará en: http://localhost:5000

### 2. Configurar N8N para llamar a la API

En N8N, añade un nodo "HTTP Request":

```json
{
  "method": "POST",
  "url": "http://localhost:5000/execute",
  "body": {
    "team_id": "mi_equipo",
    "agent_type": "market_research",
    "task": "Analizar mercado de IA en España",
    "niche": "Agencias de IA"
  }
}
```

## 🐛 Solución de Problemas

### Error: "Module not found"

**Solución**:
```bash
pip install -r requirements.txt
```

### Error: "API key not found"

**Solución**:
1. Verifica que `.env` existe
2. Verifica que tu API key está correctamente configurada
3. Reinicia el script

### Error: "YAML load error"

**Solución**:
```bash
pip install pyyaml
```

### N8N no se conecta

**Solución**:
1. Verifica que N8N está corriendo: `ps aux | grep n8n`
2. Verifica el puerto 5678: `netstat -an | grep 5678`
3. Reinicia N8N: `n8n start`

## 📦 Estructura del Proyecto

```
Repositorio-proyecto-1/
├── core/                      # Framework base
│   ├── __init__.py
│   ├── agent_framework.py     # Clases base
│   └── ai_provider.py         # Proveedores de IA
│
├── agents/                    # Agentes especializados
│   ├── __init__.py
│   └── specialized_agents.py  # Implementaciones
│
├── workflows/                 # Workflows N8N
│   ├── n8n_client_acquisition.json
│   └── n8n_content_creation.json
│
├── examples/                  # Ejemplos de uso
│   ├── client_acquisition_example.py
│   ├── custom_niche_team.py
│   └── api_server.py          # API REST
│
├── docs/                      # Documentación
│   ├── GUIA_COMPLETA.md
│   ├── N8N_INTEGRATION.md
│   └── SETUP.md               # Este archivo
│
├── .gitignore                 # Archivos ignorados
├── .env                       # Variables de entorno
├── config.yaml                # Configuración
├── requirements.txt           # Dependencias
├── main.py                    # Punto de entrada
├── quickstart.sh              # Script de inicio rápido
└── README.md                  # Documentación principal
```

## ✅ Checklist de Instalación

- [ ] Python 3.8+ instalado
- [ ] Repositorio clonado
- [ ] Dependencias instaladas (`pip install -r requirements.txt`)
- [ ] Archivo `.env` creado con API key
- [ ] Demo ejecutado exitosamente (`python main.py`)
- [ ] (Opcional) N8N instalado
- [ ] (Opcional) Workflows importados en N8N
- [ ] (Opcional) API server funcionando

## 🎓 Próximos Pasos

1. **Lee la documentación completa**: `docs/GUIA_COMPLETA.md`
2. **Explora los ejemplos**: Revisa `/examples/` para ver casos de uso
3. **Personaliza tu equipo**: Crea agentes especializados para tu nicho
4. **Integra con N8N**: Automatiza tus flujos de trabajo
5. **Usa la API**: Integra con tus sistemas existentes

## 💬 Soporte

Si tienes problemas:

1. Revisa esta guía de setup
2. Consulta `docs/GUIA_COMPLETA.md`
3. Revisa los ejemplos en `/examples/`
4. Abre un issue en GitHub

## 🚀 Listo para Producción

Para usar en producción:

1. **Seguridad**: Nunca commitear `.env` con API keys reales
2. **Escalabilidad**: Considera usar servicios cloud para N8N
3. **Monitoreo**: Implementa logging y métricas
4. **Testing**: Prueba exhaustivamente antes de lanzar
5. **Backup**: Respalda tus configuraciones y workflows

---

**¡Todo listo! Ahora puedes empezar a construir tu sistema agéntico** 🎯
