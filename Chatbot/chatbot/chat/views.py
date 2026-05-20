from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from django.conf import settings
import json

from google import genai

client = genai.Client(api_key=settings.GOOGLE_API_KEY)

chat = client.chats.create(model="gemini-2.5-flash")


@csrf_exempt
def chatbot_view(request):
    if request.method == "POST":
        data = json.loads(request.body)
        user_message = data.get("message")

        response = chat.send_message(user_message)

        bot_reply = response.text

        return JsonResponse({"reply": bot_reply})

    return render(request, "chat.html")
