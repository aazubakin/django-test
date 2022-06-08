from tabnanny import verbose
from django.db import models

# Create your models here.
class Clinet(models.Model):
    """Клиент"""

    name = models.CharField('Имя клиента', max_length=255)

    class Meta:
        verbose_name = "Клиент"
        verbose_name = "Клиенты"

    def __str__(self) -> str:
        return self.name

class Bill(models.Model):
    """Счет"""

    number = models.IntegerField('Номер счета')
    organization = models.ForeignKey(
        'main.Organization', verbose_name='Организация', on_delete=models.CASCADE
        )
    sum_bill = models.CharField('Сумма', max_length=255)
    date_created = models.DateTimeField('Дата', auto_now_add=True, db_index=True)

    class Meta:
        verbose_name = "Счет"
        verbose_name = "Счета"

    def __str__(self) -> str:
        return f'Счет №: {self.number}'
        

class Organization(models.Model):
    """Организация"""

    clients = models.ForeignKey(
        'main.Client', verbose_name='Клиент', on_delete=models.SET_NULL, blank=True, null=True
        )
    name = models.CharField('Название организации', max_length=255)
    class Meta:
        verbose_name = "Организация"
        verbose_name = "Организации"

    def __str__(self) -> str:
        return self.name