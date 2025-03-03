# What-Agent

What-Agent es una aplicación que utiliza Machine Learning para predecir el mejor agente de Valorant según el mapa, rol y dificultad del jugador.  

## Características

- Predicción del mejor agente según el mapa, dificultad y el rol.
- Implementación de modelos de Machine Learning con **CatBoost**.
- Interfaz web sencilla para facilitar el uso.
- Análisis de datos y estadísticas.

## Instalación y Uso

### Clona el repositorio
```bash
git clone https://github.com/KikiPann/What-Agent.git
cd What-Agent

# Instala las dependencias

pip install -r requirements.txt

#  Ejecuta la aplicación

python app.py

# Abre el navegador en:

http://127.0.0.1:8000/


📦 What-Agent
├── 📂 Data              # Datos de entrenamiento y pruebas
├── 📂 models            # Modelos entrenados
├── 📂 static            # Archivos estáticos (CSS, JS, imágenes)
├── 📂 templates         # Archivos HTML para la interfaz
├── agent_data.py       # Procesamiento de datos de agentes
├── app.py              # Código principal de la aplicación
├── valo.py             # Entrenamiento del modelo
├── requirements.txt    # Dependencias del proyecto


🛠 Tecnologías Utilizadas

Python 
Flask (para la interfaz web)
CatBoost (para la predicción)
SQLite (para el manejo de datos)
HTML/CSS (para la visualización)
