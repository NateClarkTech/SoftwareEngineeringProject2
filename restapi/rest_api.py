from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods
from django.shortcuts import get_object_or_404
import json
from .models import Task, Message
from django.db import models
from django.contrib.auth.models import User


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


@require_http_methods(["POST"])
@csrf_exempt
def add_message(request):
    if request.method == 'POST':
        #user = models.OneToOneField(User, on_delete=models.CASCADE)
        data = json.loads(request.body.decode('utf-8'))
        sender = data.get('sender')

        if request.user and request.user.username != "":
            sender = request.user.username

        new_mes = Message(
            val=data.get('val'),
            sender=sender,
            time=data.get('time'),
        )
        new_mes.save()
        print(new_mes)
        print(new_mes.sender)
        return JsonResponse({'message': 'Task added successfully', 'data': new_mes.id})
    else:
        return JsonResponse({'error': 'Invalid request method'}, status=400)


@csrf_exempt
def get_messages(request):
    if request.method == 'GET':
        mes = Message.objects.all()
        got_mes = [
            {
                "id": message.id,
                "sender": message.sender,
                "val": message.val,
                "time": message.time,

            } for message in mes
        ]
        return JsonResponse({'mes': got_mes})
    else:
        return JsonResponse({'error': 'Invalid request method'}, status=400)


@require_http_methods(["DELETE"])
@csrf_exempt
def delete_message(request, message_id):
    if request.method == 'DELETE':
        mes = get_object_or_404(Message, id=message_id)
        mes.delete()
        return JsonResponse({'message': 'Task deleted successfully'})
    else:
        return JsonResponse({'error': 'Invalid request method'}, status=400)


@login_required
@csrf_exempt
def get_username(request):
    if request.method == 'GET':
        return JsonResponse({'name': request.user.username})