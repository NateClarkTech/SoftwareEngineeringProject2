from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods
from django.shortcuts import get_object_or_404
import json
from .models import Task


@require_http_methods(["POST"])
@csrf_exempt
def add_task(request):
    if request.method == 'POST':
        data = json.loads(request.body.decode('utf-8'))

        new_task = Task(
            title=data.get('title'),
            date=data.get('date'),
            freq=data.get('freq'),
            type=data.get('type'),
            time=data.get('time'),
            desc=data.get('desc'),
        )
        new_task.save()
        print(new_task)
        return JsonResponse({'message': 'Task added successfully', 'data': new_task.id})
    else:
        return JsonResponse({'error': 'Invalid request method'}, status=400)


@csrf_exempt
def get_tasks(request):
    if request.method == 'GET':
        tasks = Task.objects.all()
        got_tasks = [
            {
                "id": task.id,
                "title": task.title,
                "date": task.date,
                "freq": task.freq,
                "type": task.type,
                "time": task.time,

            } for task in tasks
        ]
        return JsonResponse({'tasks': got_tasks})
    else:
        return JsonResponse({'error': 'Invalid request method'}, status=400)


@require_http_methods(["DELETE"])
@csrf_exempt
def delete_task(request, task_id):
    if request.method == 'DELETE':
        task = get_object_or_404(Task, id=task_id)
        task.delete()
        return JsonResponse({'message': 'Task deleted successfully'})
    else:
        return JsonResponse({'error': 'Invalid request method'}, status=400)
