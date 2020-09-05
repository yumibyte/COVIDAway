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
    long = models.DecimalField(max_digits=9, decimal_places=6, default=0)
    lat = models.DecimalField(max_digits=9, decimal_places=6, default=0)

    def __str__(self):
        return str([self.name, self.email, self.people, [self.need_gloves, self.need_faceshields, self.need_facemasks], self.notes, self.long, self.lat])

#from main.models import Individual
#i = Individual(name='Jerry Smith', email='jerrybear@gmail.com', people=4, need_facemasks=True)
#i.save()
#Individual.objects.all()