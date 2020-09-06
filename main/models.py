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
    address = models.CharField(max_length=255)
    time = models.DateTimeField(auto_now_add=True, blank=True, null=True)

    def __str__(self):
        return str([self.time.strftime("%m/%d/%Y - %H:%M"), self.name, self.email, self.people, [self.need_gloves, self.need_faceshields, self.need_facemasks], self.notes, self.address])

class Distributor(models.Model):
    name = models.CharField(max_length=255)
    website = models.CharField(max_length=255)
    desc = models.TextField(max_length=5000, default="Default desc.")
    nogloves = models.PositiveIntegerField()
    noshields = models.PositiveIntegerField()
    nomasks = models.PositiveIntegerField()
    address = models.CharField(max_length=255)

    def __str__(self):
        return str([self.name, self.website, self.desc, [self.nogloves, self.noshields, self.nomasks], self.address])

#from main.models import Individual
#i = Individual(name='Jerry Smith', email='jerrybear@gmail.com', people=4, need_facemasks=True)
#i.save()
#Individual.objects.all()