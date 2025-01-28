import requests
import concurrent.futures
import random
import time

# Configuración de la prueba
endpoint = "http://localhost:8000/api/bands"  # Ruta a evaluar
request_number = 250  # Número de usuarios concurrentes
test_type = "estrés"  # Tipo de prueba: "estrés" o "carga"

def make_request(request):
    start_time = time.time()
    try:
        response = requests.get(f'{endpoint}/{random.randint(1, 3)}')
        response_time = (time.time() - start_time) * 1000  # Convertir a milisegundos
        if response.status_code == 200:
            return {"status": "success", "response_time": response_time}
        else:
            return {"status": "failure", "response_time": response_time}
    except Exception as e:
        return {"status": "error", "response_time": None, "error": str(e)}

responses = []
start_test = time.time()

with concurrent.futures.ThreadPoolExecutor(max_workers=request_number) as executor:
    pending_tasks = []
    for i in range(request_number):
        pending_task = executor.submit(make_request, i)
        pending_tasks.append(pending_task)
    
    for pending_task in pending_tasks:
        responses.append(pending_task.result())

end_test = time.time()

# Filtrar resultados
success_responses = [r["response_time"] for r in responses if r["status"] == "success"]
failure_responses = [r for r in responses if r["status"] == "failure" or r["status"] == "error"]

# Calcular métricas
total_requests = len(responses)
successful_requests = len(success_responses)
failed_requests = len(failure_responses)

average_response_time = sum(success_responses) / successful_requests if successful_requests > 0 else 0
max_response_time = max(success_responses) if successful_requests > 0 else 0
success_rate = (successful_requests / total_requests) * 100 if total_requests > 0 else 0

# Mostrar resultados
print(f"=========================================")
print(f"RESULTADOS DE LA PRUEBA")
print(f"=========================================")
print(f"Tipo de prueba: {test_type.capitalize()}")
print(f"Ruta evaluada: {endpoint}/:id")
print(f"Usuarios concurrentes: {request_number}")
print(f"Total de solicitudes: {total_requests}")
print(f"Solicitudes exitosas: {successful_requests}")
print(f"Solicitudes fallidas: {failed_requests}")
print(f"Tiempo de respuesta promedio: {average_response_time:.2f} ms")
print(f"Tiempo de respuesta máximo: {max_response_time:.2f} ms")
print(f"Tasa de éxito: {success_rate:.2f}%")
print(f"Duración total de la prueba: {end_test - start_test:.2f} segundos")
print(f"=========================================")
