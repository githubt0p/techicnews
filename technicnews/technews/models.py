from django.db import models

class User(models.Model):
    id = models.AutoField('ID', primary_key = True)
    name = models.CharField('Имя', max_length = 35, null = False)
    subname = models.CharField('Фамилия', max_length = 35, null = False)

    def __str__(self):
        return self.name


    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'


class Post(models.Model):
    id = models.AutoField('ID', primary_key = True)
    title = models.CharField('Название', max_length = 35, null = False)
    text = models.TextField('Текст')
    date = models.DateTimeField('Дата')
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.title


    class Meta:
        verbose_name = 'Пост'
        verbose_name_plural = 'Посты'