from fastapi import FastAPI, BackgroundTasks
import time, uuid

app = FastAPI()
tareas = {} # Diccionario para guardar el estado

def tarea_pesada(task_id: str):
    time.sleep(5)  # Simula el procesamiento (5 seg)
    tareas[task_id] = "Completado: Resultado listo"

@app.post("/procesar")
def procesar(bg_tasks: BackgroundTasks):
    task_id = str(uuid.uuid4())
    tareas[task_id] = "Procesando..."
    
    bg_tasks.add_task(tarea_pesada, task_id) # Lanza tarea en 2do plano
    return {"mensaje": "Procesando...", "task_id": task_id}

@app.get("/resultado/{task_id}")
def resultado(task_id: str):
    return {"estado": tareas.get(task_id, "Tarea no encontrada")}