from django.db import models
from django_resized import ResizedImageField

# Create your models here.
class Setting(models.Model):
    title = models.CharField(
        max_length = 255,
        verbose_name = 'Название сайта'
    )
    logo = ResizedImageField(
        force_format="WEBP", 
        quality=100, default='no_image.jpg',
        upload_to='logo/',
        verbose_name="Логотип",
        blank=True, null=True
    )
    phone = models.CharField(
        max_length = 255,
        verbose_name = 'Номер телефона'
    )
    email = models.EmailField(
        verbose_name = 'Почта',
        blank=True, null=True
    )
    facebook = models.URLField(
        verbose_name = 'URL facebook',
        blank=True, null=True
    )
    instagram = models.URLField(
        verbose_name = 'URL instagram',
        blank=True, null=True
    )

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = 'Настройки сайта'
        verbose_name_plural = 'Настройки сайта'