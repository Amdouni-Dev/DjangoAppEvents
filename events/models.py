from django.db import models
from users.models import *
from datetime import date
from django.core.exceptions import *

def isDateIsValid(value):
    if value <=  date.today():
        raise ValidationError("invalid date")
    return value
        
# Create your models here.
class Event(models.Model): # heritage ==> models.Model
    categories=(('musique','musique'),
                ('cinema','cinema'),
                ('sport','sport')
                )
    title= models.CharField(max_length=255) # maxLength est obligatoire 
    description=models.TextField() # nafsha chartfield ema akber 
    image=models.ImageField(upload_to='images/')  # /Media/Images 
    category=models.CharField(max_length=255,choices=categories)
    state=models.BooleanField(default=False)
    nbrParticipants=models.ImageField(default=0)
    dateEvent=models.DateField(validators=[isDateIsValid])
    created_at=models.DateTimeField(auto_now_add=True) #  auto_now_add==> tetbadel l created At 
    updated_at=models.DateTimeField(auto_now=True)# ki naamel update
    
    
    # associations
    organizer=models.ForeignKey(Person, on_delete=models.CASCADE) # 
    participations=models.ManyToManyField(Person,related_name='Participation',through='Participation')
    #related name==> esm l objet 
class Participation(models.Model):   
    participationDate=models.DateField( auto_now=True)
    person=models.ForeignKey(Person,on_delete=models.CASCADE)
    event=models.ForeignKey(Event,on_delete=models.CASCADE)        