from django.db import models

# Create your models here.
class marca(models.Model):
    id = models.AutoField(primary_key=True,verbose_name='Imagen')
    Nombre=models.CharField(max_length=100)
    imagen=models.ImageField(upload_to='imagenes/',verbose_name='Imagen',null=True)
    rubro=models.TextField(null=True, max_length=120,verbose_name='Rubro de la marca')

    def __str__(self):
        fila="Nombre: "+ self.Nombre+ " - " + "Rubro de la marca: "+ self.rubro
        return fila
    def delete(self,using=None,keep_parent=False):
        self.imagen.storage.delete(self.imagen.name)
        super().delete()
