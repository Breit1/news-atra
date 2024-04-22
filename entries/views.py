from django.views.generic import (
   ListView,
   DetailView,
)
from .models import Entry

class EntryListView(ListView):
    model = Entry
    queryset = Entry.objects.all().order_by("-date_created") # Это ключевой запрос — он возвращает все существующие записи по нашему первичному ключу, сортируя их по дате создания.
   
class EntryDetailView(DetailView): # Дополнительно создаём представление с подклассом DetailView. Будем использовать его позже.
    model = Entry


from django.views.generic import CreateView
from .models import Entry

class EntryCreateView(CreateView):
    model = Entry
    fields = ['title', 'content', 'image']  # добавляем поле image для загрузки изображения
    template_name = 'entry_list.html'  # шаблон для формы создания записи


from django.shortcuts import render

def base_template(request):
    return render(request, 'entries/base_template.html')

def stockanalytics(request):
    entries = Entry.objects.all()
    return render(request, 'entries/stockanalytics.html', {'entry_list': entries})

from django.shortcuts import render
from .models import Entry

def stockanalytics_view(request):
    entry_list = Entry.objects.all()
    print(entry_list)  # Добавьте эту строку для вывода в консоль содержимого entry_list
    return render(request, 'entries/stockanalytics.html', {'entry_list': entry_list})


from django.views.generic import DetailView
from .models import Entry

class EntryDetailAnalView(DetailView):
    model = Entry
    template_name = 'entries/entry_detail_anal.html'  # Укажите путь к вашему шаблону entry_detail_anal.html
