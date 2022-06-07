import datetime
from django.utils import timezone
from django.db import models


class Arcticle(models.Model):
    bbb_title = models.CharField('Название статьи', max_length=200)
    bbb_text = models.TextField('Текст статьи')
    bbb_date = models.DateTimeField('Дата публикации')

    def __str__(self):
        return self.bbb_title

    def was_publish_recently(self):
        return self.bbb_date >= (timezone.now() - datetime.timedelta(days=7))

    class Meta:
        verbose_name = 'Статья'
        verbose_name_plural = 'Статьи'


class Comment(models.Model):
    article = models.ForeignKey(Arcticle, on_delete=models.CASCADE)
    author_name = models.CharField('Имя автора', max_length=55)
    comment_text = models.CharField('Текст комментария', max_length=150)

    def __str__(self):
        return self.author_name

    class Meta:
        verbose_name = 'Комментарий'
        verbose_name_plural = 'Комментарии'
