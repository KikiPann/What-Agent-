from fastapi import FastAPI, Request, Form, HTTPException
from fastapi.responses import HTMLResponse, JSONResponse, FileResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
import pandas as pd
import joblib
import random
import os
import logging
from typing import Optional
from agent_data import AGENT_DATA, MAP_MAPPING, ROLE_MAPPING, DIFFICULTY_MAPPING

# --- Configuración (sin cambios) ---
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = FastAPI(title="What Agent? - Recomendador de Agentes de Valorant")
app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")

# --- Carga del modelo (sin cambios) ---
try:
    model_path = os.path.join("models", "catboost_model.pkl")
    cat_model = joblib.load(model_path)
    logger.info("Modelo cargado correctamente")
except Exception as e:
    logger.error(f"Error al cargar el modelo: {e}")
    cat_model = None

# --- Rutas (la ruta principal sin cambios) ---
@app.get("/", response_class=HTMLResponse)
async def get_index(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

# --- Ruta de recomendación (¡¡¡COMPLETAMENTE REVISADA!!!) ---
@app.post("/api/recomendar-agente")
async def recomendar_agente(
    map: Optional[str] = Form(None),
    role: Optional[str] = Form(None),
    difficulty: Optional[str] = Form(None),
):
    logger.info(f"Solicitud recibida: Mapa={map}, Rol={role}, Dificultad={difficulty}")

    if cat_model is None:
        raise HTTPException(status_code=500, detail="El modelo no está disponible")

    try:
        # --- Manejo de valores aleatorios y mapeo (sin cambios importantes) ---
        if map == "Aleatorio" or not map:
            map = random.choice(list(MAP_MAPPING.keys()))
        if role == "Aleatorio" or not role:
            role = random.choice(list(ROLE_MAPPING.keys()))
        if difficulty == "Aleatorio" or not difficulty:
            difficulty = random.choice(list(DIFFICULTY_MAPPING.keys()))

        map_value = MAP_MAPPING.get(map.lower(), "Ascent")  # Valor por defecto
        role_value = ROLE_MAPPING.get(role.lower(), "Duelista")  # Valor por defecto
        difficulty_value = DIFFICULTY_MAPPING.get(difficulty.lower(), "Media")  # Valor por defecto
        logger.info(f"Valores procesados: Mapa={map_value}, Rol={role_value}, Dificultad={difficulty_value}")

        # --- Creación del DataFrame (sin cambios) ---
        input_data = pd.DataFrame([[map_value, role_value, difficulty_value, 0, 0, 0, 0, 0]],
                                    columns=['Map', 'Role', 'Difficulty', 'ACS', 'Kills', 'Assists', 'Deaths', 'ADR'])

        # --- Predicción del modelo (sin cambios) ---
        probabilities = cat_model.predict_proba(input_data)
        best_agent_index = probabilities.argmax()
        best_agent = cat_model.classes_[best_agent_index]


        # --- 1.  Depuración:  Verifica el valor de best_agent ---
        logger.info(f"Agente recomendado (best_agent): '{best_agent}'")
        logger.info(f"Claves en AGENT_DATA: {list(AGENT_DATA.keys())}")

        # --- 2. Obtención de la información del agente (¡¡¡CORREGIDO!!!) ---
        agent_info = AGENT_DATA.get(best_agent)  # ¡¡¡Sin valor por defecto!!!

        # --- 3. Construcción de la respuesta (¡¡¡MANEJO DE ERRORES!!!) ---
        if agent_info:  # Si agent_info NO es None (se encontró el agente)
            response = {
                "agente": best_agent,
                "rol": agent_info["role"],  # Acceso directo
                "imagen": agent_info["image"].replace("static/images/", ""),  # Acceso directo, solo el nombre
                "habilidades": agent_info["abilities"],  # Acceso directo
                "mapa": map_value,
                "dificultad": difficulty_value
            }
        else:  # Si agent_info ES None (NO se encontró el agente)
            logger.error(f"¡¡¡ERROR: Agente '{best_agent}' NO ENCONTRADO en AGENT_DATA!!!")  # ¡¡¡Mensaje de error claro!!!
            response = {  # Respuesta de error
                "agente": best_agent,  # Incluimos el nombre del agente predicho
                "rol": "Rol no especificado",
                "imagen": "default.jpg",
                "habilidades": ["Información no disponible"],
                "mapa": map_value,
                "dificultad": difficulty_value
            }

        return JSONResponse(content=response)

    except Exception as e:
        logger.error(f"Error en la recomendación: {e}")
        raise HTTPException(status_code=500, detail=f"Error al procesar la solicitud: {str(e)}")

# --- Ruta para servir imágenes (sin cambios) ---
@app.get("/images/{filename}")
async def get_image(filename: str):
    image_path = os.path.join("static", "images", filename)
    if os.path.exists(image_path):
        return FileResponse(image_path)
    else:
        return FileResponse(os.path.join("static", "images", "default.jpg"))


if __name__ == "__main__":
    import uvicorn
    uvicorn.run("app:app", host="127.0.0.1", port=8000, reload=True)