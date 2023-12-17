from email.mime import text
from os import name
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db.models import CharField
from phonenumber_field.modelfields import PhoneNumberField
import uuid
from uuid import uuid4

class CustomUser(AbstractUser):

    email = models.EmailField(null=False, blank=False, unique=False) #НЕ ЗАБУДЬ ПОМЕНЯТЬ #НЕ ЗАБУДЬ ПОМЕНЯТЬ #НЕ ЗАБУДЬ ПОМЕНЯТЬ
    phone = PhoneNumberField(null=False, blank=False, unique=False) #НЕ ЗАБУДЬ ПОМЕНЯТЬ #НЕ ЗАБУДЬ ПОМЕНЯТЬ #НЕ ЗАБУДЬ ПОМЕНЯТЬ
    code = CharField(max_length=16, blank = True)
    adress = models.CharField (max_length=200, default ='Adress' , blank = True)   
    is_active = models.BooleanField(default = True) #НЕ ЗАБУДЬ ПОМЕНЯТЬ #НЕ ЗАБУДЬ ПОМЕНЯТЬ #НЕ ЗАБУДЬ ПОМЕНЯТЬ
    is_send = models.BooleanField(default = False)
    def __str__(self):
        return self.username + "" + str(self.phone)


#------------------------------product-------------------------------------#
class category(models.Model):
    name = models.CharField (max_length=200, default ='Название')     
    def get_absolute_url(self):
         return f'/ctg/{self.pk}/'     
#-------------------------------------------------------------------------#
#------------------------------product------------------------------------#
class news_block(models.Model):
    name = models.CharField (max_length=200, default ='Название')   
    image = models.ImageField(upload_to='static\media\img',  blank = True)
    full_desc = models.TextField('Текст блока' , blank = True)
    def get_absolute_url(self):
         return f'/news_block/{self.pk}/'     
#-------------------------------------------------------------------------#

class new(models.Model):
    name = models.CharField (max_length=200, default ='Название')  
    preview = models.ImageField(upload_to='static\media\img',  blank = True)
    preview_text =  models.TextField('Текст превью' , blank = True)
    news_block = models.ManyToManyField(news_block , null = True , blank = True , related_name='news')
    CAT = models.ManyToManyField(category , null = True , blank = True , related_name='news')
    my_id = models.UUIDField(primary_key=False, default=uuid.uuid4, editable=False)
    language = models.CharField (max_length=200, default ='EN')  
    def __str__ (self):
       return self.name;
#-------------------------------------------------------------------------#

class feedback(models.Model):
    name = models.CharField (max_length=200, blank=False)  
    email = models.EmailField(null=False, blank=False, unique=False) #НЕ ЗАБУДЬ ПОМЕНЯТЬ #НЕ ЗАБУДЬ ПОМЕНЯТЬ #НЕ ЗАБУДЬ ПОМЕНЯТЬ
    phone = PhoneNumberField(null=False, blank=False, unique=False) #НЕ ЗАБУДЬ ПОМЕНЯТЬ #НЕ ЗАБУДЬ ПОМЕНЯТЬ #НЕ ЗАБУДЬ ПОМЕНЯТЬ
    adress = models.CharField (max_length=300, blank=True)
    text = models.TextField('Сообщение' , blank = True)
    def __str__ (self):
       return self.name;



class coop(models.Model):
    org_name = models.CharField (max_length=200, blank=False)  
    site = models.CharField (max_length=300, blank=False)  
    place = models.CharField (max_length=200, blank=False)  
    activity = models.CharField (max_length=200, blank=False)  
    adress = models.CharField (max_length=300, blank=True)
    name = models.CharField (max_length=200, blank=False)  
    email = models.EmailField(null=False, blank=False, unique=False) #НЕ ЗАБУДЬ ПОМЕНЯТЬ #НЕ ЗАБУДЬ ПОМЕНЯТЬ #НЕ ЗАБУДЬ ПОМЕНЯТЬ
    phone = PhoneNumberField(null=False, blank=False, unique=False) #НЕ ЗАБУДЬ ПОМЕНЯТЬ #НЕ ЗАБУДЬ ПОМЕНЯТЬ #НЕ ЗАБУДЬ ПОМЕНЯТЬ
    jt = models.CharField (max_length=200, blank=False)  
    text = models.TextField('Сообщение' , blank = True)
   
    def __str__ (self):
       return self.name;

class rev(models.Model):
    title_ru = models.CharField (max_length=200, default ='Заголовок')  
    review_ru = models.TextField('Отзыв' , blank = True)
    name_ru = models.CharField (max_length=200, default ='Имя')

    title_en = models.CharField (max_length=200, default ='Title')  
    review_en = models.TextField('Review' , blank = True)
    name_en = models.CharField (max_length=200, default ='Name') 
    
    title_gr = models.CharField (max_length=200, default ='Επικεφαλίδα')     
    review_gr = models.TextField('Ανασκόπηση' , blank = True)
    name_gr = models.CharField (max_length=200, default ='Ονομα') 
    
    img = models.ImageField(upload_to='static\media\img',  blank = True)
    def __str__ (self):
       return self.title_ru + '(' + self.title_en + ')';

class product(models.Model):
    name_ru = models.CharField (max_length=200, default ='Название')  
    short_desc_ru = models.TextField('Краткое описание' , blank = True)
    full_desc_ru = models.TextField('Полное описание' , blank = True)   
    extra_desc_ru = models.TextField('Дополнительная информация' , blank = True)
    tech_desc_ru = models.TextField('Технические характеристики' , blank = True)

    name_en = models.CharField (max_length=200, default ='Name')      
    short_desc_en = models.TextField('Short description' , blank = True)
    full_desc_en = models.TextField('Full description' , blank = True)   
    extra_desc_en = models.TextField('Additional Information' , blank = True)
    tech_desc_en = models.TextField('Specifications' , blank = True)

    name_gr = models.CharField (max_length=200, default ='Ονομα')   
    short_desc_gr = models.TextField('Σύντομη περιγραφή' , blank = True)
    full_desc_gr = models.TextField('Πλήρης περιγραφή' , blank = True)   
    extra_desc_gr = models.TextField('Επιπλέον πληροφορίες' , blank = True)
    tech_desc_gr = models.TextField('Προδιαγραφές' , blank = True)
  
    img = models.ImageField(upload_to='static\media\img',  blank = True)
    price = models.CharField (max_length=200, default ='Цена')   
    def __str__ (self):
       return self.name_ru;

class questions(models.Model):
    name_ru = models.CharField (max_length=200, default ='Вопрос')  
    desc_ru = models.TextField('Ответ' , blank = True)

    name_en = models.CharField (max_length=200, default ='Question')  
    desc_en = models.TextField('answer' , blank = True)
    
    name_gr = models.CharField (max_length=200, default ='ερώτηση')  
    desc_gr = models.TextField('απάντηση' , blank = True)
    def __str__ (self):
       return self.name_ru + '(' + self.name_en + ')';

class order(models.Model): #Форма заказа
    name = models.CharField (max_length=200, blank=False)  
    email = models.EmailField(null=False, blank=False, unique=False) #НЕ ЗАБУДЬ ПОМЕНЯТЬ #НЕ ЗАБУДЬ ПОМЕНЯТЬ #НЕ ЗАБУДЬ ПОМЕНЯТЬ
    phone = PhoneNumberField(null=False, blank=False, unique=False) #НЕ ЗАБУДЬ ПОМЕНЯТЬ #НЕ ЗАБУДЬ ПОМЕНЯТЬ #НЕ ЗАБУДЬ ПОМЕНЯТЬ
    adress = models.CharField (max_length=300, blank=True)
    text = models.TextField('Сообщение' , blank = True)
    prod = models.CharField (max_length=200, blank=False , default='default')  
    def __str__ (self):
       return self.name;