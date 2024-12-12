from django.shortcuts import render

# Create your views here.
from django.http import JsonResponse
import asyncio
from .client_script import hello
from django.views.generic import TemplateView

# def trigger_websocket(request):
#     asyncio.run(hello())
#     return JsonResponse({"status": "WebSocket connection initiated"})


class HomePageView(TemplateView):
    template_name = "index1.html"  # Make sure this matches your template path

def trigger_websocket(request):
    # asyncio.run(hello())
    return render(request, 'index1.html')