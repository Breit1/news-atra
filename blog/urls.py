from django.contrib import admin
from django.urls import path, include #Импортируем функцию include.
urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("entries.urls")), #Явно указываем на то, что требуется обратиться к приложению Entries.

]
