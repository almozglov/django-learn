import datetime
from django.db import models
from django.utils import timezone

# Create your models here.
class Article(models.Model):
	a_title = models.CharField('Название статьи', max_length = 200)
	a_text = models.TextField("Текст Статьи")
	pud_date = models.DateTimeField("Дата публикации")
	#При вызове статьи из консоли возвращает не объект, а название статьи
	def __str__(self):
		return self.a_title

	def was_pub_recently(self):
		return self.pud_date >=(timezone.now() - datetime.timedelta(days=7))
	
	#Привязка моделей к статье. Делается функцией 
	#ForeignKey со ссылкой на модель, к которой прив.
	#CASCADE - удаление комментариев вместе со статьей (из базы)
class Comment(models.Model):
	article = models.ForeignKey(Article, on_delete = models.CASCADE)
	c_name = models.CharField('Имя автора', max_length = 50)
	c_text = models.CharField('Текст комментария', max_length = 200)
	c_date = models.DateTimeField('Дата публикации')

	def __str__(self):
		return self.c_name