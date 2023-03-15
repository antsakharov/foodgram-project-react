from django.contrib.auth.models import AbstractUser
from django.contrib.auth.validators import UnicodeUsernameValidator
from django.db import models
from django.core.exceptions import ValidationError


class User(AbstractUser):
    """ Кастомная модель пользователя. """

    email = models.EmailField('Почта', max_length=254, unique=True)
    first_name = models.CharField('Имя', max_length=150, blank=False)
    last_name = models.CharField('Фамилия', max_length=150, blank=False)
    username = models.CharField(
        'Юзернейм',
        max_length=150,
        validators=[UnicodeUsernameValidator()])
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', 'first_name', 'last_name']

    class Meta:
        ordering = ['-pk']

    def __str__(self):
        return self.username


class Subscription(models.Model):
    """ Модель подписок. """

    user = models.ForeignKey(
        User,
        related_name='follower',
        on_delete=models.CASCADE,
        verbose_name='Подписчик'
    )
    author = models.ForeignKey(
        User,
        related_name='author',
        on_delete=models.CASCADE,
        verbose_name='Автор'
    )

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=('user', 'author'),
                name='unique_subscription'
            ),
            models.CheckConstraint(
                check=~models.Q(user=models.F('author')),
                name='prevent_self_subscription'
            )
        ]

    def clean(self):
        if self.user == self.author:
            raise ValidationError('Нельзя подписаться на себя!')

    def __str__(self):
        return f'Пользователь {self.user} подписался на {self.author}'
