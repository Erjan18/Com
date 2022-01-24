from django.db import models

class Registration(models.Model):
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


