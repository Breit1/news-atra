from django.db import models
from django.utils import timezone
 
class Entry(models.Model): # Создаём новый класс, который будет служить для блога моделью, указывая все необходимые элементы.
   title = models.CharField(max_length=200)
   content = models.TextField()
   date_created = models.DateTimeField(default=timezone.now)
   image = models.ImageField(upload_to='images/') # продолжение пути media
 
   def __str__(self): # С помощью функции меняем то, как будет представлена запись в модели.
       return self.title # Указываем, что она будет идентифицироваться с помощью своего заголовка.
 
   class Meta:
       verbose_name_plural = "Entries" # Указываем правильное написание для множественного числа слова Entry.
       

# class Entry_Analytics(models.Model):
#     title = models.CharField(max_length=200)
#     content = models.TextField()
#     date_created = models.DateTimeField(default=timezone.now)
#     image = models.ImageField(upload_to='images/') # продолжение пути media
