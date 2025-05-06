from django.db import models

class Feedback(models.Model):
    username = models.CharField(max_length=100, verbose_name="Никнейм пользователя")
    avatar_path = models.CharField(max_length=255, blank=True, null=True, verbose_name="Путь к аватарке")
    short_msg = models.CharField(max_length=40, verbose_name="Заголовок", default="Отзыв")
    text = models.TextField(verbose_name="Текст отзыва")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")

    class Meta:
        verbose_name = "Отзыв"
        verbose_name_plural = "Отзывы"
        ordering = ['-created_at']

    def __str__(self):
        return f"{self.username} - {self.created_at.strftime('%Y-%m-%d %H:%M')}"

class GalleryImages(models.Model):
    name = models.CharField(max_length=100)
    image = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    upload_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
