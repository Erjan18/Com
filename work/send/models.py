from django.db import models
from django.utils.translation import gettext_lazy as _

class Header(models.Model):
    class Meta:
        verbose_name = _("Главная")
        verbose_name_plural = _("Главная")

    image = models.ImageField(blank=True)
    name = models.TextField()

    def __str__(self):
        return self.name

class Information(models.Model):
    class Meta:
        verbose_name = _("Информация о конференции")
        verbose_name_plural = _("Информация о конференции")

    name = models.TextField()
    image = models.ImageField(blank=True)

    def __str__(self):
        return self.name

class Conference(models.Model):
    class Meta:
        verbose_name = _("Программа конференции")
        verbose_name_plural = _("Программа конференции")

    name = models.TextField()

    def __str__(self):
        return self.name

class Ads(models.Model):
    class Meta:
        verbose_name = _("Объявление и регламент конференции")
        verbose_name_plural = _("Объявление и регламент конференции")

    name = models.TextField()

    def __str__(self):
        return self.name

class Commitet(models.Model):
    class Meta:
        verbose_name = _("Коммитет конференции")
        verbose_name_plural = _("Коммитет конференции")

    name = models.TextField()

    def __str__(self):
        return self.name

class Event(models.Model):
    class Meta:
        verbose_name = _("Общественные мероприятия")
        verbose_name_plural = _("Общественные мероприятия")

    name = models.TextField()
    image = models.ImageField(blank=True)

    def __str__(self):
        return self.name

class Donat(models.Model):
    class Meta:
        verbose_name = _("Регистрация")
        verbose_name_plural = _("Регистрация")

    name = models.TextField()

    def __str__(self):
        return self.name

class Registration(models.Model):
    class Meta:
        verbose_name = _("Регистрация")
        verbose_name_plural = _("Регистрация")

    Status = (
        ('Физическое лицо', 'Физическое лицо'),
        ('Юридическое лицо', 'Юридическое лицо')
    )
    Category = (
        ('Очно','Очно'),
        ('Заочно','Заочно'),
        ('Дистанционно','Дистанционно'),
        ('Слушатель','Слушатель'),
        ('Докладчик','Докладчик'),
    )
    status = models.CharField(max_length=50, null=True, choices=Status)
    full_name = models.CharField(max_length=150, null=True)
    rank = models.CharField(max_length=200, null=True)
    subject = models.CharField(max_length=200,null=True)
    category = models.CharField(max_length=100,null=True,choices=Category)
    organization = models.CharField(max_length=200,null=True)
    position = models.CharField(max_length=200,null=True)
    mail = models.CharField(max_length=100,null=True)
    number = models.FloatField(null=True)
    city = models.CharField(max_length=150,null=True)
    country = models.CharField(max_length=150,null=True)
    field = models.FileField(blank=True,upload_to='uploads')

    def __str__(self):
        return self.rank
