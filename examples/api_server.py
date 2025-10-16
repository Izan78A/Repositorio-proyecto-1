"""
Example: Flask API Server
Exposes the agentic system via REST API for integration with N8N and other tools
"""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent))

from flask import Flask, request, jsonify
from main import AgenticSystem
from core import Task

app = Flask(__name__)
system = AgenticSystem()

# Store active teams
active_teams = {}


@app.route('/health', methods=['GET'])
def health():
    """Health check endpoint"""
    return jsonify({
        'status': 'healthy',
        'system': system.config.get('system', {}).get('name', 'Sistema Agéntico Local')
    })


@app.route('/teams', methods=['POST'])
def create_team():
    """Create a new specialized team"""
    data = request.json
    team_id = data.get('team_id')
    niche = data.get('niche')
    
    if not team_id or not niche:
        return jsonify({'error': 'team_id and niche are required'}), 400
    
    team = system.create_niche_team(
        team_id=team_id,
        niche=niche,
        team_config=data.get('config', {})
    )
    
    active_teams[team_id] = team
    
    return jsonify({
        'success': True,
        'team_id': team_id,
        'niche': niche,
        'agent_count': len(team.agents)
    })


@app.route('/teams/<team_id>', methods=['GET'])
def get_team(team_id):
    """Get team information"""
    team = system.get_team(team_id)
    
    if not team:
        return jsonify({'error': 'Team not found'}), 404
    
    return jsonify(team.get_team_stats())


@app.route('/teams', methods=['GET'])
def list_teams():
    """List all teams"""
    return jsonify({
        'teams': [team.get_team_stats() for team in system.teams.values()]
    })


@app.route('/execute', methods=['POST'])
def execute_task():
    """Execute a task on a specific agent"""
    data = request.json
    team_id = data.get('team_id')
    agent_type = data.get('agent_type')
    task_description = data.get('task')
    context = data.get('context', {})
    
    # Validate input
    if not all([team_id, agent_type, task_description]):
        return jsonify({
            'error': 'team_id, agent_type, and task are required'
        }), 400
    
    # Get or create team
    team = system.get_team(team_id)
    if not team:
        niche = data.get('niche', 'General')
        team = system.create_niche_team(team_id=team_id, niche=niche)
    
    # Get agent
    agent_id = f"{team_id}_{agent_type}"
    agent = team.get_agent(agent_id)
    
    if not agent:
        return jsonify({
            'error': f'Agent {agent_type} not found in team {team_id}'
        }), 404
    
    # Create and execute task
    task = Task(
        task_id=f"api_{agent_type}_{len(agent.task_history)}",
        description=task_description,
        context=context
    )
    
    try:
        result = agent.execute_task(task)
        
        return jsonify({
            'success': True,
            'task_id': task.task_id,
            'agent': agent_type,
            'result': result,
            'status': task.status.value
        })
    except Exception as e:
        return jsonify({
            'success': False,
            'error': str(e)
        }), 500


@app.route('/execute-workflow', methods=['POST'])
def execute_workflow():
    """Execute a complete workflow on a team"""
    data = request.json
    team_id = data.get('team_id')
    workflow_name = data.get('workflow')
    context = data.get('context', {})
    
    if not all([team_id, workflow_name]):
        return jsonify({
            'error': 'team_id and workflow are required'
        }), 400
    
    # Get or create team
    team = system.get_team(team_id)
    if not team:
        niche = data.get('niche', 'General')
        team = system.create_niche_team(team_id=team_id, niche=niche)
    
    try:
        results = system.execute_workflow(team_id, workflow_name, context)
        
        return jsonify({
            'success': True,
            'workflow': workflow_name,
            'team_id': team_id,
            'results': results
        })
    except Exception as e:
        return jsonify({
            'success': False,
            'error': str(e)
        }), 500


@app.route('/validate', methods=['POST'])
def validate_work():
    """Validate work using QA agent"""
    data = request.json
    team_id = data.get('team_id')
    work = data.get('work')
    
    if not all([team_id, work]):
        return jsonify({
            'error': 'team_id and work are required'
        }), 400
    
    team = system.get_team(team_id)
    if not team:
        return jsonify({'error': 'Team not found'}), 404
    
    if not team.qa_validator:
        return jsonify({'error': 'No QA validator in team'}), 404
    
    # Create validation task
    task = Task(
        task_id=f"validation_{team_id}",
        description="Validate work quality",
        context={'work': work}
    )
    
    try:
        validation_result = team.qa_validator.execute_task(task)
        
        return jsonify({
            'success': True,
            'validation': validation_result
        })
    except Exception as e:
        return jsonify({
            'success': False,
            'error': str(e)
        }), 500


@app.route('/stats', methods=['GET'])
def system_stats():
    """Get system statistics"""
    return jsonify(system.get_system_stats())


@app.route('/workflows', methods=['GET'])
def list_workflows():
    """List available workflows"""
    return jsonify({
        'workflows': system.list_workflows()
    })


if __name__ == '__main__':
    print("=" * 60)
    print("API Server del Sistema Agéntico Local")
    print("=" * 60)
    print()
    print("Endpoints disponibles:")
    print("  - GET  /health              - Health check")
    print("  - POST /teams               - Crear equipo")
    print("  - GET  /teams               - Listar equipos")
    print("  - GET  /teams/<id>          - Info de equipo")
    print("  - POST /execute             - Ejecutar tarea")
    print("  - POST /execute-workflow    - Ejecutar workflow")
    print("  - POST /validate            - Validar trabajo")
    print("  - GET  /stats               - Estadísticas del sistema")
    print("  - GET  /workflows           - Listar workflows")
    print()
    print("Servidor corriendo en: http://localhost:5000")
    print("=" * 60)
    print()
    
    app.run(debug=True, host='0.0.0.0', port=5000)
