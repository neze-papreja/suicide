from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.contrib.humanize.templatetags.humanize import naturaltime
from django.utils.html import escape
from django.views import View
from .models import Message, Chat
from .model_api import ResponseModel


resp_model = ResponseModel()


class MessageListView(LoginRequiredMixin, View):
    template_name = "chat/message_list.html"

    def get(self, request):
        chat, _ = Chat.objects.get_or_create(owner=request.user)
        message_list = chat.message_set.all().order_by('created_at')
        ctx = {'message_list': message_list}
        return render(request, self.template_name, ctx)

    def post(self, request):
        chat = Chat.objects.get(owner=request.user)
        message = Message(text=request.POST['message'], is_reply=False, chat=chat)
        message.save()

        response_text = resp_model.get_response()
        response = Message(text=response_text, is_reply=True, chat=chat)
        response.save()

        return redirect(reverse_lazy('chat:all_messages'))


