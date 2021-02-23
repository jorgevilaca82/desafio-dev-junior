"""desafio_dev_junior URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.http.response import StreamingHttpResponse
from django.urls import path

from django.views import View
import time


class SSEView(View):
    def get(self, request):
        def stream():
            while True:
                yield f"data: minha mensagem\n\n"
                time.sleep(3)

        stream_resp = StreamingHttpResponse(stream(), content_type="text/event-stream")

        stream_resp["Connection"] = "Keep-Alive"
        stream_resp["Cache-Control"] = "no-cache"
        stream_resp["Keep-Alive"] = "timeout=9007199254740991"

        return stream_resp


urlpatterns = [
    path("sse", SSEView.as_view()),
    path("admin/", admin.site.urls),
]
