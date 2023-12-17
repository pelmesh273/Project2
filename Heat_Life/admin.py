from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser, order 
from .forms import CustomUserCreationForm, CustomUserChangeForm 
from .models import category , news_block , new , feedback ,coop , questions , product , rev , order


class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser
    fieldsets = (*UserAdmin.fieldsets,('доп. инфо:',{'fields':('phone' , 'adress' , 'is_send')}))
#-------------------------------------------------------------#

 
class cat_Inline(admin.TabularInline):
    model = new.CAT.through
    extra = 0
class categoryAdmin(admin.ModelAdmin):  
    model = category   
    inlines = [
        cat_Inline,
    ]

class block_Inline(admin.TabularInline):
    model = new.news_block.through
    extra = 0    
class blockAdmin(admin.ModelAdmin):  
    model = news_block   
    inlines = [
        block_Inline,
    ]    

#----------------------------------#
class new_Admin(admin.ModelAdmin):
    inlines = [
        cat_Inline,block_Inline,
    ]
    exclude = ('CAT','news_block',)


admin.site.register(news_block , blockAdmin)
admin.site.register(category , categoryAdmin)
admin.site.register(new , new_Admin)
admin.site.register(feedback)
admin.site.register(coop)
admin.site.register(order)
admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(questions)
admin.site.register(product)
admin.site.register(rev)
# Register your models here.
