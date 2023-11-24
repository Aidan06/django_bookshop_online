from django.db import models
from django.contrib.auth.models import User


class Genre(models.Model):
    name = models.CharField(verbose_name='Наименование', max_length=255, db_index=True)
    slug = models.SlugField(max_length=255, unique=True)

    class Meta:
        verbose_name = 'Жанр'
        verbose_name_plural = 'Жанры'

    def __str__(self):
        return self.name


class Book(models.Model):
    genre = models.ForeignKey(Genre, verbose_name='Жанр', related_name='product', on_delete=models.CASCADE)
    created_by = models.ForeignKey(User, verbose_name='Создан', on_delete=models.CASCADE, related_name='product_creator')
    title = models.CharField(verbose_name='Название',max_length=255)
    author = models.CharField(verbose_name='Автор', max_length=255, default='admin')
    hard_book_cover = models.BooleanField(verbose_name='Мягкая обложка', default=False)
    description = models.TextField(verbose_name='Описание', blank=True)
    image = models.ImageField(verbose_name='Фото', upload_to='images/')
    slug = models.SlugField(max_length=255)
    price = models.DecimalField(verbose_name='Цена', max_digits=4, decimal_places=2)
    in_stock = models.BooleanField(verbose_name='В наличии', default=True)
    is_active = models.BooleanField(verbose_name='Активно', default=True)
    created = models.DateTimeField(verbose_name='Создано', auto_now_add=True)
    updated = models.DateTimeField(verbose_name='Обновлено', auto_now=True)

    class Meta:
        verbose_name = 'Книга'
        verbose_name_plural = 'Книги'
        ordering = ('-created',)

    def __str__(self):
        return self.title
