from django.db import models

# Create your models here.

class Individual(models.Model):
    name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    people = models.PositiveIntegerField()
    need_gloves = models.BooleanField(default=False)
    need_faceshields = models.BooleanField(default=False)
    need_facemasks = models.BooleanField(default=False)
    notes = models.TextField(max_length=5000, default="Default desc.")
    lat = models.DecimalField(max_digits=9, decimal_places=6, default=0)
    long = models.DecimalField(max_digits=9, decimal_places=6, default=0)
    time = models.DateTimeField(auto_now_add=True, blank=True, null=True)

    def __str__(self):
        return str([self.time.strftime("%m/%d/%Y - %H:%M"), self.name, self.email, self.people, [self.need_gloves, self.need_faceshields, self.need_facemasks], self.notes, self.lat, self.long])
class Distributor(models.Model):
    name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    nomasks = models.IntegerField(max_length=255)
    noshields = models.IntegerField(max_length=255)
    nogloves= models.IntegerField(max_length=255)
    lat = models.DecimalField(max_digits=9, decimal_places=6, default=0)
    long = models.DecimalField(max_digits=9, decimal_places=6, default=0)
    time = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    notes = models.TextField(max_length=5000, default="Default desc.")
def __str__(self):
   return str([self.time.strftime("%m/%d/%Y - %H:%M"), self.name, self.email,  [self.nogloves, self.noshields, self.nomasks], self.notes, self.lat, self.long])
#from main.models import Individual
#i = Individual(name='Jerry Smith', email='jerrybear@gmail.com', people=4, need_facemasks=True)
#i.save()
#Individual.objects.all()