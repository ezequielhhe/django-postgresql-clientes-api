from django.db import models

class Cliente(models.Model):
    nombre = models.CharField(max_length=100)
    tel = models.CharField(max_length=150)
    provincia = models.CharField(max_length=150)
    calle = models.CharField(max_length=150)
    altura = models.IntegerField()

    def __str__(self):
        return self.nombre, self.tel, self.provincia, self.calle

    class Meta:
        db_table = 'clientes'
