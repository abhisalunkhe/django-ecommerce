from django.db import models

# Create your models here.
class registerCust(models.Model):
    name = models.CharField(max_length=100)
    uname = models.CharField(max_length=30)
    email = models.EmailField()
    psw = models.CharField(max_length=50)
    
class getintouch(models.Model):
    name = models.CharField(max_length=60)
    email = models.EmailField()
    subject = models.CharField(max_length=50)
    message = models.TextField()

class feature_items(models.Model):
    name = models.CharField(max_length=25)
    price = models.IntegerField()
    image = models.ImageField(upload_to='feature_items')
    is_sold = models.BooleanField(default=False)
    visible = models.BooleanField(default=False)
    
class cate_tshirt(models.Model):
    name = models.CharField(max_length=25)
    price = models.IntegerField()
    image = models.ImageField(upload_to='cate_tshirt')
    visible = models.BooleanField(default=False)
    
class cate_blazer(models.Model):
    name = models.CharField(max_length=25)
    price = models.IntegerField()
    image = models.ImageField(upload_to='cate_blazer')
    visible = models.BooleanField(default=False)
    
class cate_sunglass(models.Model):
    name = models.CharField(max_length=25)
    price = models.IntegerField()
    image = models.ImageField(upload_to='cate_sunglass')
    visible = models.BooleanField(default=False)
    
class cate_kids(models.Model):
    name = models.CharField(max_length=25)
    price = models.IntegerField()
    image = models.ImageField(upload_to='cate_kids')
    visible = models.BooleanField(default=False)
    
class cate_poloshirt(models.Model):
    name = models.CharField(max_length=25)
    price = models.IntegerField()
    image = models.ImageField(upload_to='cate_poloshirt')
    visible = models.BooleanField(default=False)
    
class categ_nike(models.Model):
    name = models.CharField(max_length=25)
    price = models.IntegerField()
    image = models.ImageField(upload_to='categ_nike')
    visible = models.BooleanField(default=False)
    
class categ_underarmour(models.Model):
    name = models.CharField(max_length=25)
    price = models.IntegerField()
    image = models.ImageField(upload_to='categ_underarmour')
    visible = models.BooleanField(default=False)
    
class categ_adidas(models.Model):
    name = models.CharField(max_length=25)
    price = models.IntegerField()
    image = models.ImageField(upload_to='categ_adidas')
    visible = models.BooleanField(default=False)
    
class categ_puma(models.Model):
    name = models.CharField(max_length=25)
    price = models.IntegerField()
    image = models.ImageField(upload_to='categ_puma')
    visible = models.BooleanField(default=False)
    
class categ_asics(models.Model):
    name = models.CharField(max_length=25)
    price = models.IntegerField()
    image = models.ImageField(upload_to='categ_asics')
    visible = models.BooleanField(default=False)
    
class categ_men_fendi(models.Model):
    name = models.CharField(max_length=25)
    price = models.IntegerField()
    image = models.ImageField(upload_to='categ_men_fendi')
    visible = models.BooleanField(default=False)
    
class categ_men_guess(models.Model):
    name = models.CharField(max_length=25)
    price = models.IntegerField()
    image = models.ImageField(upload_to='categ_men_guess')
    visible = models.BooleanField(default=False)
    
class categ_men_valentino(models.Model):
    name = models.CharField(max_length=25)
    price = models.IntegerField()
    image = models.ImageField(upload_to='categ_men_valentino')
    visible = models.BooleanField(default=False)
    
class categ_men_dior(models.Model):
    name = models.CharField(max_length=25)
    price = models.IntegerField()
    image = models.ImageField(upload_to='categ_men_dior')
    visible = models.BooleanField(default=False)
    
class categ_men_versace(models.Model):
    name = models.CharField(max_length=25)
    price = models.IntegerField()
    image = models.ImageField(upload_to='categ_men_versace')
    visible = models.BooleanField(default=False)
    
class categ_men_armani(models.Model):
    name = models.CharField(max_length=25)
    price = models.IntegerField()
    image = models.ImageField(upload_to='categ_men_armani')
    visible = models.BooleanField(default=False)
    
class categ_men_prada(models.Model):
    name = models.CharField(max_length=25)
    price = models.IntegerField()
    image = models.ImageField(upload_to='categ_men_prada')
    visible = models.BooleanField(default=False)
    
class categ_men_dolceandgabbana(models.Model):
    name = models.CharField(max_length=25)
    price = models.IntegerField()
    image = models.ImageField(upload_to='categ_men_dolceandgabbana')
    visible = models.BooleanField(default=False)

class categ_men_chanel(models.Model):
    name = models.CharField(max_length=25)
    price = models.IntegerField()
    image = models.ImageField(upload_to='categ_men_chanel')
    visible = models.BooleanField(default=False)
    
class categ_men_gucci(models.Model):
    name = models.CharField(max_length=25)
    price = models.IntegerField()
    image = models.ImageField(upload_to='categ_men_gucci')
    visible = models.BooleanField(default=False)
    
class categ_women_fendi(models.Model):
    name = models.CharField(max_length=25)
    price = models.IntegerField()
    image = models.ImageField(upload_to='categ_women_fendi')
    visible = models.BooleanField(default=False)
    
class categ_women_guess(models.Model):
    name = models.CharField(max_length=25)
    price = models.IntegerField()
    image = models.ImageField(upload_to='categ_women_guess')
    visible = models.BooleanField(default=False)
    
class categ_women_valentino(models.Model):
    name = models.CharField(max_length=25)
    price = models.IntegerField()
    image = models.ImageField(upload_to='categ_women_valentino')
    visible = models.BooleanField(default=False)
    
class categ_women_dior(models.Model):
    name = models.CharField(max_length=25)
    price = models.IntegerField()
    image = models.ImageField(upload_to='categ_women_dior')
    visible = models.BooleanField(default=False)
    
class categ_women_versace(models.Model):
    name = models.CharField(max_length=25)
    price = models.IntegerField()
    image = models.ImageField(upload_to='categ_women_versace')
    visible = models.BooleanField(default=False)
    
class categ_kids(models.Model):
    name = models.CharField(max_length=25)
    price = models.IntegerField()
    image = models.ImageField(upload_to='categ_kids')
    visible = models.BooleanField(default=False)
    
class categ_fashion(models.Model):
    name = models.CharField(max_length=25)
    price = models.IntegerField()
    image = models.ImageField(upload_to='categ_fashion')
    visible = models.BooleanField(default=False)
    
class categ_households(models.Model):
    name = models.CharField(max_length=25)
    price = models.IntegerField()
    image = models.ImageField(upload_to='categ_households')
    visible = models.BooleanField(default=False)
    
class categ_interiors(models.Model):
    name = models.CharField(max_length=25)
    price = models.IntegerField()
    image = models.ImageField(upload_to='categ_interiors')
    visible = models.BooleanField(default=False)
    
class categ_clothing(models.Model):
    name = models.CharField(max_length=25)
    price = models.IntegerField()
    image = models.ImageField(upload_to='categ_clothing')
    visible = models.BooleanField(default=False)
    
class categ_bags(models.Model):
    name = models.CharField(max_length=25)
    price = models.IntegerField()
    image = models.ImageField(upload_to='categ_bags')
    visible = models.BooleanField(default=False)
    
class categ_shoes(models.Model):
    name = models.CharField(max_length=25)
    price = models.IntegerField()
    image = models.ImageField(upload_to='categ_shoes')
    visible = models.BooleanField(default=False)