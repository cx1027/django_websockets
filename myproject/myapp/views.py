from django.shortcuts import render

# Create your views here.
from django.http import JsonResponse
import asyncio
from .client_script import hello

def trigger_websocket(request):
    asyncio.run(hello())
    return JsonResponse({"status": "WebSocket connection initiated"})