from django.contrib.auth import get_user_model
from django.db import models
from django.utils import timezone


User = get_user_model()


class PostQuerySet(models.QuerySet):
    """Объединение таблиц и выполнение фильтраций."""

    def with_related_data(self):
        """Объединение таблиц."""
        return self.select_related('category', 'author', 'location')

    def published(self):
        """Фильтрация по статусу публикации."""
        return self.filter(is_published=True, category__is_published=True)

    def new_date(self):
        """Фильтрация по времени публикации."""
        return self.filter(pub_date__lte=timezone.now())


class PublishedPostModel(models.Manager):
    """Менеджер публикаций."""

    def get_queryset(self):
        """Фильтрация публикаций."""
        return (
            PostQuerySet(self.model)
            .with_related_data()
            .published()
            .new_date()
        )


class BaseModel(models.Model):
    """Базовая модель."""

    is_published = models.BooleanField('Опубликовано',
                                       default=True,
                                       help_text=('Снимите галочку,'
                                                  ' чтобы скрыть публикацию.'))
    created_at = models.DateTimeField('Добавлено', auto_now_add=True)

    class Meta:
        """Специальный класс Meta."""

        abstract = True


class Category(BaseModel):
    """Модель категории."""

    title = models.CharField('Заголовок', max_length=256)
    description = models.TextField('Описание')
    slug = models.SlugField('Идентификатор',
                            unique=True,
                            help_text=('Идентификатор страницы для URL; '
                                       'разрешены символы латиницы, '
                                       'цифры, дефис и подчёркивание.'))

    class Meta:
        """Специальный класс Meta."""

        verbose_name = 'категория'
        verbose_name_plural = 'Категории'

    def __str__(self):
        """Информация о модели."""
        return self.title


class Location(BaseModel):
    """Модель местоположения."""

    name = models.CharField('Название места', max_length=256)

    class Meta:
        """Специальный класс Meta."""

        verbose_name = 'местоположение'
        verbose_name_plural = 'Местоположения'

    def __str__(self):
        """Информация о модели."""
        return self.name


class Post(BaseModel):
    """Модель публикации."""

    title = models.CharField('Заголовок', max_length=256)
    text = models.TextField('Текст')
    pub_date = models.DateTimeField('Дата и время публикации',
                                    help_text=('Если установить дату и время'
                                               ' в будущем — можно делать'
                                               ' отложенные публикации.'))
    author = models.ForeignKey(User, verbose_name='Автор публикации',
                               on_delete=models.CASCADE)
    location = models.ForeignKey(Location, verbose_name='Местоположение',
                                 on_delete=models.SET_NULL,
                                 null=True, blank=True)
    category = models.ForeignKey(Category, verbose_name='Категория',
                                 on_delete=models.SET_NULL,
                                 null=True)
    objects = PostQuerySet.as_manager()
    published = PublishedPostModel()

    class Meta:
        """Специальный класс Meta."""

        verbose_name = 'публикация'
        verbose_name_plural = 'Публикации'

    def __str__(self):
        """Информация о модели."""
        return self.title
