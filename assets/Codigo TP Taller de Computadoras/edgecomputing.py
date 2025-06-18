import time
import numpy as np

# Ejemplo de una tarea de procesamiento intensiva
def intensive_task():
    result = np.random.rand(1000, 1000)
    return np.linalg.inv(result)

start_time = time.time()
intensive_task()
end_time = time.time()

print(f"Tiempo de ejecución: {end_time - start_time} segundos")