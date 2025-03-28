from django.http import JsonResponse 
from django.views.decorators.csrf import csrf_exempt
import json

# Base de datos en memoria (simulación)
items = [{"id": 1, "nombre": "Laptop"}, {"id": 2, "nombre": "Telefono"}]

@csrf_exempt # Desactiva la verificación CSRF para pruebas
def obtener_agregar_items(request):
    if request.method == 'GET': # Devolver la lista de ítems en formato JSON
        return JsonResponse(items, safe=False) 
    elif request.method == 'POST':
        try:
            data = json.loads(request.body) # Convertir JSON en diccionario
            nuevo_item = { "id": len(items) + 1,
                        "nombre": data.get("nombre", "Sin nombre")}
            items.append(nuevo_item) # Agregar el nuevo ítem a la lista
            return JsonResponse(nuevo_item, status=201) # Respuesta
        except json.JSONDecodeError:
            return JsonResponse({"error": "Formato JSON inválido"}, status=400) 

@csrf_exempt
def obtener_item(request, item_id):
    if request.method == 'GET':
        for item in items:
            if item["id"] == item_id:
                return JsonResponse(item)
        return JsonResponse({"error": "Item no encontrado"}, status=404)


@csrf_exempt
def modificar_item(request, item_id):
    """Modifica un ítem existente"""
    if request.method == 'PUT':
        item = next((i for i in items if i["id"] == item_id), None)
        if not item:
            return JsonResponse({"error": "Ítem no encontrado"}, status=404)
        try:
            data = json.loads(request.body)
            item["nombre"] = data.get("nombre", item["nombre"])
            return JsonResponse(item)
        except json.JSONDecodeError:
            return JsonResponse({"error": "Formato JSON inválido"}, status=400)
    return JsonResponse({"error": "Método no permitido"}, status=405)

@csrf_exempt
def eliminar_item(request, item_id):
    """Elimina un ítem existente"""
    global items
    if request.method == 'DELETE':
        items = [i for i in items if i["id"] != item_id]
        return JsonResponse({"mensaje": "Ítem eliminado"}, status=204)
    return JsonResponse({"error": "Método no permitido"}, status=405)
