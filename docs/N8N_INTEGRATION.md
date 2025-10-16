# Guía de Inicio Rápido - N8N Integration

## 🔗 Integración con N8N

N8N es una herramienta de automatización de código abierto que permite crear workflows sin programar. Este sistema está diseñado para integrarse perfectamente con N8N.

## 📦 Instalación de N8N

### Opción 1: Instalación Global (Recomendado)

```bash
npm install -g n8n
```

### Opción 2: Docker

```bash
docker run -it --rm \
  --name n8n \
  -p 5678:5678 \
  -v ~/.n8n:/home/node/.n8n \
  n8nio/n8n
```

### Opción 3: npx (Sin instalación)

```bash
npx n8n
```

## 🚀 Iniciar N8N

```bash
# Iniciar N8N
n8n start

# N8N estará disponible en:
# http://localhost:5678
```

## 📥 Importar Workflows

1. **Accede a N8N**: Abre http://localhost:5678 en tu navegador

2. **Crea una nueva cuenta** (primera vez)

3. **Importa workflows**:
   - Click en "Workflows" en el menú
   - Click en "Import from File"
   - Selecciona los archivos `.json` de la carpeta `/workflows/`:
     - `n8n_client_acquisition.json`
     - `n8n_content_creation.json`

## 🔄 Workflows Disponibles

### 1. Client Acquisition Workflow

**Propósito**: Automatizar el proceso completo de adquisición de clientes

**Flujo**:
```
Webhook Trigger
    ↓
Market Research Agent (Investigación de mercado)
    ↓
Content Creator Agent (Crear contenido de outreach)
    ↓
Sales Specialist Agent (Ejecutar campaña)
    ↓
QA Validator Agent (Validar antes de enviar)
    ↓
Response (Devolver resultados)
```

**Usar el workflow**:
```bash
# POST request al webhook
curl -X POST http://localhost:5678/webhook/client-acquisition \
  -H "Content-Type: application/json" \
  -d '{
    "niche": "Agencia de IA",
    "industry": "Tecnología",
    "target_market": "Empresas medianas",
    "geography": "España"
  }'
```

### 2. Content Creation Workflow

**Propósito**: Generar contenido de marketing validado

**Flujo**:
```
Webhook Trigger
    ↓
Technical Expert Agent (Configurar automatización)
    ↓
Content Creator Agent (Generar contenido)
    ↓
QA Validator Agent (Validar calidad)
    ↓
Response (Contenido validado)
```

**Usar el workflow**:
```bash
curl -X POST http://localhost:5678/webhook/content-creation \
  -H "Content-Type: application/json" \
  -d '{
    "requirements": "Post de LinkedIn sobre IA",
    "specs": {
      "tone": "profesional",
      "length": "300 palabras",
      "keywords": ["IA", "automatización", "negocios"]
    }
  }'
```

## 🔧 Configuración Avanzada

### Conectar N8N con el Sistema Python

Puedes crear un nodo HTTP Request en N8N que llame a tu sistema Python:

1. **Crear API Server en Python**:

```python
# api_server.py
from flask import Flask, request, jsonify
from main import AgenticSystem
from core import Task

app = Flask(__name__)
system = AgenticSystem()

@app.route('/execute-agent', methods=['POST'])
def execute_agent():
    data = request.json
    team_id = data.get('team_id')
    agent_type = data.get('agent_type')
    task_description = data.get('task')
    context = data.get('context', {})
    
    team = system.get_team(team_id)
    if not team:
        # Crear equipo si no existe
        team = system.create_niche_team(
            team_id=team_id,
            niche=data.get('niche', 'General')
        )
    
    agent = team.get_agent(f"{team_id}_{agent_type}")
    
    task = Task(
        task_id=f"api_{agent_type}_{len(agent.task_history)}",
        description=task_description,
        context=context
    )
    
    result = agent.execute_task(task)
    
    return jsonify({
        'success': True,
        'result': result,
        'agent': agent_type
    })

if __name__ == '__main__':
    app.run(port=5000)
```

2. **Instalar Flask**:
```bash
pip install flask
```

3. **Ejecutar API**:
```bash
python api_server.py
```

4. **En N8N, usar nodo HTTP Request**:
   - Method: POST
   - URL: http://localhost:5000/execute-agent
   - Body: JSON con los parámetros

### Ejemplo de Nodo en N8N

```json
{
  "nodes": [
    {
      "parameters": {
        "url": "http://localhost:5000/execute-agent",
        "method": "POST",
        "jsonParameters": true,
        "options": {},
        "bodyParametersJson": "={\n  \"team_id\": \"{{ $json.team_id }}\",\n  \"agent_type\": \"market_research\",\n  \"task\": \"{{ $json.task }}\",\n  \"context\": {{ $json.context }},\n  \"niche\": \"{{ $json.niche }}\"\n}"
      },
      "name": "Call Python Agent",
      "type": "n8n-nodes-base.httpRequest",
      "typeVersion": 1,
      "position": [450, 300]
    }
  ]
}
```

## 🎯 Casos de Uso con N8N

### 1. Automatización de Prospección

**Workflow**:
1. Trigger: Nuevas empresas en base de datos
2. Market Research Agent: Analizar empresa
3. Content Creator: Generar email personalizado
4. Sales Specialist: Crear estrategia de acercamiento
5. QA Validator: Validar todo
6. Enviar email (nodo Email de N8N)

### 2. Generación de Contenido Programado

**Workflow**:
1. Trigger: Cron (diario/semanal)
2. Market Research: Identificar tendencias
3. Content Creator: Generar posts
4. QA Validator: Validar calidad
5. Publicar en redes sociales (nodos de N8N)

### 3. Análisis de Competencia Automatizado

**Workflow**:
1. Trigger: Webhook o cron
2. Market Research: Analizar competidores
3. Technical Expert: Procesar datos
4. Content Creator: Crear reporte
5. QA Validator: Validar
6. Enviar reporte por email

## 📊 Monitoreo de Workflows

N8N proporciona:
- **Dashboard**: Ver ejecuciones de workflows
- **Logs**: Historial detallado de cada ejecución
- **Errores**: Notificaciones cuando algo falla
- **Métricas**: Tiempo de ejecución, tasa de éxito, etc.

## 🔐 Seguridad en N8N

### Variables de Entorno

En N8N, puedes usar credenciales para API keys:

1. **Ir a Settings → Credentials**
2. **Crear nueva credencial** (ej: "OpenAI API")
3. **Añadir tu API key**
4. **Referenciar en nodos**: `{{ $credentials.openai.apiKey }}`

### Webhooks Seguros

```bash
# En config de N8N, habilitar seguridad de webhook
export N8N_BASIC_AUTH_ACTIVE=true
export N8N_BASIC_AUTH_USER=admin
export N8N_BASIC_AUTH_PASSWORD=tu-password
```

## 🛠️ Troubleshooting

### Problema: Workflow no se ejecuta

**Solución**:
- Verifica que N8N esté corriendo: `ps aux | grep n8n`
- Verifica que el webhook esté activo (botón "Active" en ON)
- Revisa los logs de N8N

### Problema: Error al conectar con Python API

**Solución**:
- Verifica que el servidor Python esté corriendo: `curl http://localhost:5000/health`
- Revisa que los puertos no estén bloqueados
- Verifica CORS si es necesario

### Problema: Timeout en ejecuciones largas

**Solución**:
```bash
# Aumentar timeout de N8N
export N8N_TIMEOUT_EXECUTION=300  # 5 minutos
```

## 📚 Recursos Adicionales

- **Documentación N8N**: https://docs.n8n.io/
- **Templates N8N**: https://n8n.io/workflows/
- **Comunidad N8N**: https://community.n8n.io/

## 🚀 Próximos Pasos

1. Experimenta con los workflows incluidos
2. Crea tus propios workflows personalizados
3. Integra con otros servicios (Slack, Email, CRM)
4. Automatiza tu pipeline de adquisición de clientes

---

**¿Necesitas ayuda?** Revisa los ejemplos en `/examples/` o consulta la guía completa en `/docs/GUIA_COMPLETA.md`
