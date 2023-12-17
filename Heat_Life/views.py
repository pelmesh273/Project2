from os import name
from pickle import NONE
from turtle import title
from typing import Any, Dict
from django.db.models.query import QuerySet
from django.shortcuts import render
from django.utils.translation import get_language_from_request
from django.utils.translation import to_locale, get_language
from django.http import HttpResponse , JsonResponse
from Heat_Life.forms import feedback_form , coop_form ,order_form
from .models import *
from django.views.generic import CreateView , UpdateView , TemplateView , FormView , DetailView
from django.views.generic.list import ListView
#ad 1234

ses_lang = "ru"
def lang_mech (x):
    if x.session.get('ses_lang') is None:
        x.session['ses_lang'] = to_locale(get_language())
        print("session reset , try again")

    post_lang = x.POST.get ('post_lang');

    if 'post_lang' in x.POST:            
        if x.session['ses_lang'] != None :
            x.session['ses_lang'] = post_lang

def get_lang(x): #or get default
     lang_mech(x);

     if x.session.get('ses_lang') != None:
         return x.session.get('ses_lang');
     else:
         return 'ru' #управление языком

def get_client_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip

def Main_page(x):
     #print (get_language_from_request(x, check_path=False))   
     lang_mech(x);
     LANG = x.session.get('ses_lang');
     LINK = 'Heat_Life_' + LANG + '/Main_page.html';
     New = new.objects.filter(language = LANG).order_by('id')[:1]
     if x.session.get('ses_lang') != None:
         return render (x , LINK , {'NEW':New})
     else:
         return render (x , 'Heat_Life_default/Main_page.html' , {'NEW':New})
  
class News_page(ListView): 
    paginate_by = 7
    context_object_name = 'new'
    
    def get_queryset(self):
        lang_mech(self.request);
        LANG = self.request.session.get('ses_lang');
        return new.objects.filter(language = LANG).order_by('name');
    
    def get_context_data(self, * , object_list=None , **kwargs):
        context = super().get_context_data(**kwargs)     
        New = new.objects.filter(language = self.request.session.get('ses_lang')).order_by('id')[:1]
        new_unsorted = new.objects.all()           
        context.update({'new_unsorted' : new_unsorted , 'NEW':New})       
        return context 
    
    def get_template_names(self):
        LINK = 'Heat_Life_' + get_lang(self.request) + '/News.html';
        return [LINK]
 
class News_page_search(ListView): 
    paginate_by = 7
    context_object_name = 'new'
    def get_queryset(self):
        return new.objects.filter(name__iregex=self.request.GET.get("q"))
    
    def get_context_data(self, * , object_list=None , **kwargs):
        context = super().get_context_data(**kwargs)
        context['q'] = self.request.GET.get('q')
        New = new.objects.filter(language = self.request.session.get('ses_lang')).order_by('id')[:1]
        context.update({'NEW':New})   
        return context 
    
    def get_template_names(self):
        LINK = 'Heat_Life_' + get_lang(self.request) + '/News.html';
        return [LINK]

def News_dv(x, pk):
    New = new.objects.get(id = pk) 
    print(New)
    lang_mech(x);
    LANG = x.session.get('ses_lang');
    LINK = 'Heat_Life_' + LANG + '/New.html';

    if x.session.get('ses_lang') != None:
        print(LINK)
        return render (x , LINK , {'New':New})     
    else:
        return render (x , 'Heat_Life_default/New.html' , {'New':New})

#---------------#
class page_soon(ListView):
    paginate_by = 20
    context_object_name = 'product'
    
    def get_queryset(self):
        return product.objects.all();
    
    def get_context_data(self, * , object_list=None , **kwargs):
            context = super().get_context_data(**kwargs)
            context['q'] = self.request.GET.get('q')
            New = new.objects.filter(language = self.request.session.get('ses_lang')).order_by('id')[:1]
            context.update({'NEW':New})   
            return context 

    def get_template_names(self):
        LINK = 'Heat_Life_' + get_lang(self.request) + '/soon.html';
        return [LINK] 
    
class page_faq(ListView):
    paginate_by = 20
    context_object_name = 'questions'
    
    def get_queryset(self):
        return questions.objects.all();
    
    def get_context_data(self, * , object_list=None , **kwargs):
            context = super().get_context_data(**kwargs)
            context['q'] = self.request.GET.get('q')
            New = new.objects.filter(language = self.request.session.get('ses_lang')).order_by('id')[:1]
            context.update({'NEW':New})   
            return context 

    def get_template_names(self):
        LINK = 'Heat_Life_' + get_lang(self.request) + '/faq.html';
        return [LINK]   
    
class page_rev(ListView):
    paginate_by = 10
    context_object_name = 'rev'
    
    def get_queryset(self):
        return rev.objects.all();
    
    def get_context_data(self, * , object_list=None , **kwargs):
            context = super().get_context_data(**kwargs)
            context['q'] = self.request.GET.get('q')
            New = new.objects.filter(language = self.request.session.get('ses_lang')).order_by('id')[:1]
            context.update({'NEW':New})   
            return context     

    def get_template_names(self):
        LINK = 'Heat_Life_' + get_lang(self.request) + '/rev.html';
        return [LINK] 
     
def soon_dv(x, pk):
    if x.is_ajax():
        if x.method == 'POST':
            form = order_form(x.POST)          
            if form.is_valid():
                name = form.cleaned_data["name"]
                email = form.cleaned_data["email"]
                phone = form.cleaned_data["phone"]
                adress = form.cleaned_data["adress"]
                text = form.cleaned_data["text"]
                prod = x.POST.get ('to_like');
                STORY = order.objects.create(name = name , email  = email , phone = phone, adress = adress , text=text , prod=prod)
                STORY.save()
                return JsonResponse({'success': True})
            else:                
                return JsonResponse({'success': False, 'errors': form.errors})    
    else:
        form = order_form()        

        prod = product.objects.get(id = pk) 
        lang_mech(x);
        LANG = x.session.get('ses_lang');
        LINK = 'Heat_Life_' + LANG + '/d_soon.html';
        
        New = new.objects.filter(language = LANG).order_by('id')[:1]
        
        if x.session.get('ses_lang') != None:
            print(LINK)
            return render (x , LINK , {'prod':prod , 'form': form , 'pk': pk , 'NEW':New})     
        else:
            return render (x , 'Heat_Life_default/d_soon.html' , {'prod':prod , 'form': form , 'pk': pk , 'NEW':New})
#---------------#

def feedback_page(x): 

    if x.is_ajax():
        if x.method == 'POST':
            form = feedback_form(x.POST)          
            if form.is_valid():
                name = form.cleaned_data["name"]
                email = form.cleaned_data["email"]
                phone = form.cleaned_data["phone"]
                adress = form.cleaned_data["adress"]
                text = form.cleaned_data["text"]
                
                STORY = feedback.objects.create(name = name , email  = email , phone = phone, adress = adress , text=text)
                STORY.save()
                return JsonResponse({'success': True})
            else:                
                return JsonResponse({'success': False, 'errors': form.errors})
    else:
        form = feedback_form()
        
        lang_mech(x);
        LANG = x.session.get('ses_lang');
        LINK = 'Heat_Life_' + LANG + '/Feedback.html';
        
        New = new.objects.filter(language = LANG).order_by('id')[:1]
        
        if x.session.get('ses_lang') != None:
            return render (x , LINK , {'form': form , 'NEW':New})
        else:            
             return render (x , 'Heat_Life_default/Feedback.html' , {'form': form , 'NEW':New})

def coop_page(x):          
    if x.is_ajax():
        if x.method == 'POST':
            form = coop_form(x.POST)          
            if form.is_valid():
                org_name = form.cleaned_data["name"]
                site = form.cleaned_data["email"]
                place = form.cleaned_data["phone"]
                activity = form.cleaned_data["adress"]
                adress = form.cleaned_data["text"]
                name = form.cleaned_data["name"]
                email = form.cleaned_data["email"]
                phone = form.cleaned_data["phone"]
                jt = form.cleaned_data["adress"]
                text = form.cleaned_data["text"]
                
                STORY = coop.objects.create(org_name=org_name , site=site , place=place , activity=activity , adress=adress , name=name , email=email , phone=phone ,jt=jt , text=text)
                STORY.save()
                return JsonResponse({'success': True})
            else:                
                return JsonResponse({'success': False, 'errors': form.errors})
    else:
        form = coop_form()
              
        lang_mech(x);
        LANG = x.session.get('ses_lang');
        LINK = 'Heat_Life_' + LANG + '/coop.html';
        New = new.objects.filter(language = LANG).order_by('id')[:1]
        if x.session.get('ses_lang') != None:
            return render (x , LINK , {'form': form , 'NEW':New})
        else:            
             return render (x , 'Heat_Life_default/coop.html' , {'form': form , 'NEW':New})
        
def page_sauna (x):  
     lang_mech(x);
     LANG = x.session.get('ses_lang');
     LINK = 'Heat_Life_' + LANG + '/sauna.html';
     New = new.objects.filter(language = LANG).order_by('id')[:1]
     if x.session.get('ses_lang') != None:
         return render (x , LINK, {'NEW':New})
     else:
         return render (x , 'Heat_Life_default/sauna.html' , {'NEW':New})
def page_sush (x):  
     lang_mech(x);
     LANG = x.session.get('ses_lang');
     LINK = 'Heat_Life_' + LANG + '/sush.html';
     New = new.objects.filter(language = LANG).order_by('id')[:1]
     if x.session.get('ses_lang') != None:
         return render (x , LINK, {'NEW':New})
     else:
         return render (x , 'Heat_Life_default/sush.html' , {'NEW':New})
def page_tepl (x):  
     lang_mech(x);
     LANG = x.session.get('ses_lang');
     LINK = 'Heat_Life_' + LANG + '/tepl.html';
     New = new.objects.filter(language = LANG).order_by('id')[:1]
     if x.session.get('ses_lang') != None:
         return render (x , LINK, {'NEW':New})
     else:
         return render (x , 'Heat_Life_default/tepl.html', {'NEW':New})
     

import datetime
now = datetime.datetime.now()
import random
def email_code(x):

        now = datetime.datetime.now()
        x.session['pho'] = x.GET.get('phone', None)
        print(x.session['pho'] , "<-----" , x.GET.get('phone', None))
        random.seed(now.microsecond)
        four = []; four.append (int(random.randrange(0 , 9)));four.append (int(random.randrange(0 , 9)));four.append (int(random.randrange(0 , 9)));four.append (int(random.randrange(0 , 9)));
        x.session['cod'] = []
        x.session['cod'] = four

        print(x.session['cod'])

def basket_page (x):

    if x.is_ajax():  

        if x.GET.get('result', None) and 'send_code' in x.GET.get('result', None):
            email_code(x)
            data = {'code': ''.join([str(x) for x in x.session['cod']])} 
            return JsonResponse(data)

    return render (x , 'main/basket.html' ,{})