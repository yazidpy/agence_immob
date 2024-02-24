from django.db import models
from django.core.validators import MinValueValidator
from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver


class UserProfile(models.Model):
    class UserType(models.TextChoices):
        AGENCE = 'AGENCE'
        PARTICULIER = 'PARTICULIER'

    phone=models.CharField(unique=True,max_length=10)
    adress=models.CharField(max_length=100)
    birthday=models.DateField()
    user_type=models.CharField(max_length=20,choices=UserType.choices)
    user=models.OneToOneField(settings.AUTH_USER_MODEL,on_delete=models.CASCADE,primary_key=True)

    def __str__(self):
        return f'{self.user.first_name} {self.user.last_name}'
    
    def first_name(self):
        return self.user.first_name
    
    def last_name(self):
        return self.user.last_name


class Property(models.Model):
    class PropState(models.TextChoices):
        DISPONIBLE = 'DISPONIBLE'
        VENDUE = 'VENDUE'
        EN_ATTENTE='EN_ATTENTE'
        ARCHIVE='ARCHIVE'

    class PropType(models.TextChoices):
        Villa = 'Villa'
        Terrain = 'Terrain'
        Appartement='Appartement'
        

    title=models.CharField(max_length=100)
    description=models.TextField(null=True,default="")
    price=models.DecimalField(max_digits=10, decimal_places=2)
    adress=models.CharField(max_length=150)
    area=models.IntegerField()
    state=models.CharField(max_length=20,choices=PropState.choices)
    type_propriete = models.CharField(max_length=50,choices=PropType.choices,null=False,default="NON")
    img_1= models.ImageField(upload_to='images/',null=True)
    img_2= models.ImageField(upload_to='images/',null=True)
    img_3= models.ImageField(upload_to='images/',null=True)

    def __str__(self):
        return f'{self.title}'


class Apartment(Property):
    class viewAppar(models.TextChoices):
        EXCELLENTE = 'Excellente'
        BONNE = 'Bonne'
        NORMAL='Normal'
        MAUVAISE='Mauvaise'
    rooms=models.IntegerField(validators=[MinValueValidator(1)],null=True)
    bathrooms=models.IntegerField(validators=[MinValueValidator(1)],null=True)
    floors=models.IntegerField(validators=[MinValueValidator(1)],null=True)
    waterfront=models.BooleanField()
    view=models.CharField(max_length=20,choices=viewAppar.choices)
    year_built=models.IntegerField()
    year_renovted=models.IntegerField()
    


class Villa(Property):
    rooms=models.IntegerField(validators=[MinValueValidator(1)],null=True)
    bathrooms=models.IntegerField(validators=[MinValueValidator(1)],null=True)
    garden=models.BooleanField(null=True)
    pool=models.BooleanField(null=True)
    floors=models.IntegerField(validators=[MinValueValidator(1)],null=True)
    year_built=models.IntegerField()

class Ground(Property):
    class GroundType(models.TextChoices):
        AGRICOLE = 'Agricole'
        FORESTIER = 'Forestier'
        URBAIN='Urbain'

    Ground_type=models.CharField(max_length=20,choices=GroundType.choices)

class Annonce(models.Model):
    publication_date=models.DateTimeField(auto_now_add=True)
    Property=models.OneToOneField(Property,on_delete=models.CASCADE,primary_key=True)
    Customer=models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
    def __str__(self):
     return f'{self.Property}'
    
class Favoris(models.Model):
    Customer=models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
    Annonce=models.ForeignKey(Annonce,on_delete=models.CASCADE)