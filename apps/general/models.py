from django.db import models

# Create your models here.

class Grupo(models.Model):
	letra = models.CharField(max_length=1)

	def __str__(self):
		return "GRUPO " + self.letra

class Equipo(models.Model):
	pais = models.CharField(max_length=45)
	pj = models.IntegerField(null=True, blank=True)
	gf = models.IntegerField(null=True, blank=True)
	gc = models.IntegerField(null=True, blank=True)
	df = models.IntegerField(null=True, blank=True)
	pt = models.IntegerField(null=True, blank=True)
	grupo = models.ForeignKey(Grupo)

	def __str__(self):
		return self.pais

class Encuentro(models.Model):
	local = models.ForeignKey(Equipo, related_name="equipo_local")
	visita = models.ForeignKey(Equipo, related_name="equipo_visita")
	goleslocal = models.IntegerField(null=True, blank=True)
	golesvisita = models.IntegerField(null=True, blank=True)
	fecha = models.DateTimeField()

	def __str__(self):
		return self.local.pais + " vs " + self.visita.pais + " - " + self.fecha.strftime('%d-%m-%Y - %H:%M')