from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.
class ChaiVariety(models.Model):
    CHAI_TYPE_CHOICE = [
        ('Black', 'Black'),
        ('Green', 'Green'),
        ('Masala', 'Masala'),
        ('Herbal', 'Herbal'),
        ('Oolong', 'Oolong'),
        ('White', 'White'),
        ('Yellow', 'Yellow'),
        ('Pu-erh', 'Pu-erh'),
        ('Matcha', 'Matcha'),
        ('Chai', 'Chai'),
        ('Chamomile', 'Chamomile'),
        ('Peppermint', 'Peppermint'),
        ('Ginger', 'Ginger'),
        ('Lemon', 'Lemon'),
        ('Hibiscus', 'Hibiscus'),
        ('Rooibos', 'Rooibos'),
        ('Yerba Mate', 'Yerba Mate'),
        ('Lavender', 'Lavender'),
        ('Jasmine', 'Jasmine'),
        ('Earl Grey', 'Earl Grey'),
        ('English Breakfast', 'English Breakfast'),
        ('Assam', 'Assam'),
        ('Darjeeling', 'Darjeeling'),
        ('Nilgiri', 'Nilgiri'),
        ('Ceylon', 'Ceylon'),
        ('Keemun', 'Keemun'),
        ('Lapsang Souchong', 'Lapsang Souchong'),
        ('Sencha', 'Sencha'),
        ('Genmaicha', 'Genmaicha'),
        ('Gunpowder', 'Gunpowder'),
        ('Longjing', 'Longjing'),
        ('Matcha', 'Matcha'),
        ('Chun Mee', 'Chun Mee'),
        ('Gyokuro', 'Gyokuro'),
        ('Kukicha', 'Kukicha'),
        ('Pi Lo Chun', 'Pi Lo Chun'),
        ('Tencha', 'Tencha'),
        ('Yabukita', 'Yabukita'),
        ('Yame', 'Yame'),
        ('Yun Wu', 'Yun Wu'),
        ('Chamomile', 'Chamomile'),
        ('Peppermint', 'Peppermint'),
        ('Ginger', 'Ginger'),
        ('Lemon', 'Lemon'),
        ('Hibiscus', 'Hibiscus'),
        ('Rooibos', 'Rooibos'),
        ('Yerba Mate', 'Yerba Mate'),
        ('Lavender', 'Lavender'),
        ('Jasmine', 'Jasmine'),
        ('Earl Grey', 'Earl Grey'),
    ]
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to="chais/")
    date_added = models.DateTimeField(default=timezone.now)
    type = models.CharField(max_length=100, choices=CHAI_TYPE_CHOICE)
    description = models.TextField(default="")
    price = models.DecimalField(max_digits=5, decimal_places=2, default=0.00)
    
    def __str__(self):
        return self.name
    
# one to many relationship 
class ChaiReview(models.Model):
    chai = models.ForeignKey(ChaiVariety, on_delete=models.CASCADE, related_name='reviews')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    rating = models.IntegerField()
    comment = models.TextField()
    date_added = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f'{self.chai.name} review by {self.user.username}' 
    
# many to many relationship
class Store(models.Model):
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    chai_varieties = models.ManyToManyField(ChaiVariety, related_name='stores')

    def __str__(self):
        return self.name

# one to one relationship  

class ChaiCertificate(models.Model):
    chai = models.OneToOneField(ChaiVariety, on_delete=models.CASCADE, related_name='certificate')
    certificate_number = models.CharField(max_length=100)
    issue_date = models.DateTimeField(default=timezone.now)
    valid_until = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f' certificate for {self.chai.name} ' 

   

    