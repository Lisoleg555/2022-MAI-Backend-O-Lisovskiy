from django.db import models
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy

# Create your models here.

def is_positive(value):
    if value < 0:
        raise ValidationError(gettext_lazy("%d < 0" % value))
    
class Author(models.Model):
    name = models.CharField(max_length=64, blank=False, null=False,verbose_name="Имя автора")
    year = models.IntegerField(null=True, validators=[is_positive],verbose_name="Год рождения")
    class Meta:
        verbose_name = "Автор"
        verbose_name_plural = "Авторы"

class Music(models.Model):
    name = models.CharField(max_length=64, blank=False, null=False,verbose_name="Название трека")
    year = models.IntegerField(null=True, validators=[is_positive],verbose_name="Год выпуска")
    author = models.ManyToManyField(Author)
    class Meta:
        verbose_name = "Трек"
        verbose_name_plural = "Треки"
    def __str__(self):
        return self.name + ", " + str(self.genre) + " - " + str(self.date)