from django.db import models



class wallet(models.Model):
    Username = models.CharField(max_length=30, unique=True) 
    CurrentBalance= models.CharField(max_length=50)  
    FormerBalance = models.CharField(max_length=50)  
    ModifiedBy= models.CharField(max_length=30)  
    DateModified= models.DateTimeField()  

    def __str__(self):
        return self.Username 
    

class transaction(models.Model):
    Username = models.CharField(max_length=30, unique=True) 
    TransactionType= models.CharField(max_length=50)    
    ModifiedBy= models.CharField(max_length=30)  
    DateModified= models.DateTimeField() 

    def __str__(self):
        return self.Username 
    


    
# Create your models here.
