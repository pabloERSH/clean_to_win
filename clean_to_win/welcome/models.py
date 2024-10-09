from django.db import models

class Feedback(models.Model):
    username = models.CharField(max_length=100, verbose_name="Никнейм пользователя")
    avatar = models.ImageField(upload_to='images/', blank=True, null=True, verbose_name="Аватарка")
    text = models.TextField(verbose_name="Текст отзыва")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")

    class Meta:
        verbose_name = "Отзыв"
        verbose_name_plural = "Отзывы"
        ordering = ['-created_at']

    def __str__(self):
        return f"{self.username} - {self.created_at.strftime('%Y-%m-%d %H:%M')}"


