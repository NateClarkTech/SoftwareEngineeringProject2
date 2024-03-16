from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods
from django.shortcuts import get_object_or_404
import json
from .models import Task, Message
from django.db import models
from django.contrib.auth.models import User

from channels.layers import get_channel_layer
from asgiref.sync import async_to_sync

"""
RestAPi endpoint to add a new task to DB
"""
@require_http_methods(["POST"])
@csrf_exempt
def add_task(request):
    if request.method == 'POST':
        data = json.loads(request.body.decode('utf-8'))
        # Get data from  requat and create the new task
        new_task = Task(
            title=data.get('title'),
            date=data.get('date'),
            freq=data.get('freq'),
            type=data.get('type'),
            time=data.get('time'),
            desc=data.get('desc'),
            userid=int(data.get('userid'))
        )
        # add task to DB
        new_task.save()
        print(new_task)
        return JsonResponse({'message': 'Task added successfully', 'data': new_task.id})
    else:
        return JsonResponse({'error': 'Invalid request method'}, status=400)

"""
Returns all task for a given userid
"""
@csrf_exempt
def get_tasks(request, userid):
    if request.method == 'GET':
        # Get all task matching a given userid
        tasks = Task.objects.filter(userid=userid)
        # convert the tasks into a list
        got_tasks = [
            {
                "id": task.id,
                "title": task.title,
                "date": task.date,
                "freq": task.freq,
                "type": task.type,
                "time": task.time,
                'userid': task.userid,
            } for task in tasks
        ]
        # send tasks back
        return JsonResponse({'tasks': got_tasks})
    else:
        return JsonResponse({'error': 'Invalid request method'}, status=400)


"""
Delete a task using its Id
"""
@require_http_methods(["DELETE"])
@csrf_exempt
def delete_task(request, task_id):
    if request.method == 'DELETE':
        # get the task with the given ID
        task = get_object_or_404(Task, id=task_id)
        # Delete the task
        task.delete()
        return JsonResponse({'message': 'Task deleted successfully'})
    else:
        return JsonResponse({'error': 'Invalid request method'}, status=400)


"""
Add a new message to DB
"""
@require_http_methods(["POST"])
@csrf_exempt
def add_message(request):
    if request.method == 'POST':
        # user = models.OneToOneField(User, on_delete=models.CASCADE)
        data = json.loads(request.body.decode('utf-8'))
        sender = data.get('sender')

        if request.user and request.user.username != "":
            sender = request.user.username
        # create new message using request data
        new_mes = Message(
            val=data.get('val'),
            sender=sender,
            time=data.get('time'),
        )
        # add message to DB
        new_mes.save()
        # notify clients
        send_update_signal()
        print(new_mes)
        print(new_mes.sender)
        return JsonResponse({'message': 'Task added successfully', 'data': new_mes.id})
    else:
        return JsonResponse({'error': 'Invalid request method'}, status=400)

"""
Get all messages from the DB
"""
@csrf_exempt
def get_messages(request):
    if request.method == 'GET':
        # fetch all messages
        mes = Message.objects.all()
        # convert messages into a list
        got_mes = [
            {
                "id": message.id,
                "sender": message.sender,
                "val": message.val,
                "time": message.time,

            } for message in mes
        ]
        # send messages back
        return JsonResponse({'mes': got_mes})
    else:
        return JsonResponse({'error': 'Invalid request method'}, status=400)

"""
Delete a message using an ID
"""
@require_http_methods(["DELETE"])
@csrf_exempt
def delete_message(request, message_id):
    if request.method == 'DELETE':
        # get message using ID
        mes = get_object_or_404(Message, id=message_id)
        # delete the message
        mes.delete()
        send_update_signal()
        return JsonResponse({'message': 'Task deleted successfully'})
    else:
        return JsonResponse({'error': 'Invalid request method'}, status=400)


@login_required  # won't work bc APIs aren't actually pages
def get_username(request):
    if request.method == 'GET':
        return JsonResponse({'name': request.user.username})

"""
Test the chat update signal 
"""
def test_chat(request):
    data_to_send = {
        'key': 'value',
        # Add more data as needed
    }
    channel_layer = get_channel_layer()
    # send update signal to all clients
    async_to_sync(channel_layer.group_send)(
        'default_group',
        {
            'type': 'chat_message',
            'message': data_to_send,
        }
    )

    return JsonResponse({'data': "Data sent to channels successfully"})

"""
Send an update signal to all connected chat clients
"""
def send_update_signal():
    channel_layer = get_channel_layer()
    async_to_sync(channel_layer.group_send)(
        'default_group',
        {
            'type': 'chat_message',
            'message': 'update',
        }
    )
    print('sent update')
