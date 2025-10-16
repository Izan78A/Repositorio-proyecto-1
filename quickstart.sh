#!/bin/bash

# Quick Start Script for Sistema Agéntico Local
# This script helps you get started quickly

echo "=========================================="
echo "Sistema Agéntico Local - Quick Start"
echo "=========================================="
echo ""

# Check Python version
echo "Verificando Python..."
python_version=$(python3 --version 2>&1 | awk '{print $2}')
echo "✓ Python $python_version"
echo ""

# Check if requirements are installed
echo "Verificando dependencias..."
if ! python3 -c "import yaml" 2>/dev/null; then
    echo "⚠ Instalando dependencias..."
    pip3 install -r requirements.txt
    echo "✓ Dependencias instaladas"
else
    echo "✓ Dependencias ya instaladas"
fi
echo ""

# Check for .env file
if [ ! -f .env ]; then
    echo "⚠ Archivo .env no encontrado"
    echo "Creando archivo .env de ejemplo..."
    cat > .env << EOF
# Configuración de API Keys
# Descomenta y configura la que vayas a usar

# OpenAI
# OPENAI_API_KEY=sk-your-key-here

# Anthropic
# ANTHROPIC_API_KEY=sk-ant-your-key-here
EOF
    echo "✓ Archivo .env creado"
    echo "  Edita .env y añade tu API key"
else
    echo "✓ Archivo .env encontrado"
fi
echo ""

# Menu
echo "¿Qué deseas hacer?"
echo ""
echo "1) Ejecutar demo del sistema"
echo "2) Ejecutar ejemplo de adquisición de clientes"
echo "3) Ejecutar ejemplo de equipo personalizado"
echo "4) Iniciar API server"
echo "5) Mostrar documentación"
echo "6) Salir"
echo ""
read -p "Selecciona una opción (1-6): " option

case $option in
    1)
        echo ""
        echo "Ejecutando demo del sistema..."
        python3 main.py
        ;;
    2)
        echo ""
        echo "Ejecutando ejemplo de adquisición de clientes..."
        python3 examples/client_acquisition_example.py
        ;;
    3)
        echo ""
        echo "Ejecutando ejemplo de equipo personalizado..."
        python3 examples/custom_niche_team.py
        ;;
    4)
        echo ""
        echo "Iniciando API server en http://localhost:5000..."
        python3 examples/api_server.py
        ;;
    5)
        echo ""
        echo "Documentación disponible en:"
        echo "  - README.md - Vista general del proyecto"
        echo "  - docs/GUIA_COMPLETA.md - Guía completa del sistema"
        echo "  - docs/N8N_INTEGRATION.md - Integración con N8N"
        echo ""
        ;;
    6)
        echo "¡Hasta luego!"
        exit 0
        ;;
    *)
        echo "Opción no válida"
        exit 1
        ;;
esac
