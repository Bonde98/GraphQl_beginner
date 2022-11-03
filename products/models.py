from django.db import models

#categorie
class Category(models.Model):
    title = models.CharField(max_length=255)
    
    class Meta:
        verbose_name_plural = 'Categories'
        
    def __str__(self):
        return self.title
    
#Class Livre
class Book(models.Model):
    title = models.CharField(max_length=150)
    author = models.CharField(max_length=100, default='Reddington')
    isbn = models.CharField(max_length=13)
    pages = models.IntegerField()
    price = models.IntegerField()
    quantity = models.IntegerField()
    description = models.TextField()
    status = models.BooleanField()
    date_created = models.DateField(auto_now_add=True)
    
    class Meta:
        ordering = ['-date_created']
        
    def __str__(self):
        return self.title
    
#Class Epicerie
class Grocery(models.Model):
    product_tag = models.CharField(max_length=10)
    name = models.CharField(max_length=100)
    category = models.ForeignKey(Category, related_name='grocery', on_delete=models.CASCADE)
    price = models.IntegerField()
    quantity = models.IntegerField()
    imageur1 = models.URLField()
    status = models.BooleanField()
    date_created = models.DateField(auto_now_add=True)
    
    class Meta:
        ordering = ['-date_created']
        
    def __str__(self):
        return self.name
    
    
    
    