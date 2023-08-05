from django.db import models

# Create your models here.
class Mobile(models.Model):
    """model for storing mobiles information"""
    AVAILABILTY = [('Y','Yes'),('N','No')]
    
    brand_name    = models.CharField(max_length=32, help_text="brand name of mobile")
    nationality   = models.CharField(max_length=64, help_text="main country that investigate this mobile" )
    model         = models.CharField(max_length=128, unique=True, help_text="model of mobile and must be unique")
    price         = models.IntegerField( help_text="price of this model [$]")
    color         = models.CharField(max_length=64, help_text="color of this mobile")
    screen_size   = models.IntegerField( help_text="size of screen [inch]")
    available     = models.CharField(max_length=1,choices=AVAILABILTY, help_text="it is available or not")
    country_maker = models.CharField(max_length=64, help_text="the contry that makes this mobile")
    insert_time   = models.DateTimeField(auto_now_add=True, help_text="time of saving this row to database")
    update_time   = models.DateTimeField(auto_now=True, help_text="time of last update of this row")
    
    def __str__(self) -> str:
        """defingin way of showing mobile model in brief"""
        return f"{self.brand_name}_{self.model}"
    
    