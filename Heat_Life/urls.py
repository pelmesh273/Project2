from django.urls import path
from . import views

urlpatterns = [
    path('', views.Main_page , name = "Main_page" ),
    path('News_page', views.News_page.as_view() , name = "News_page" ),
    
    path('News_dv/<int:pk>' , views.News_dv , name = 'News_dv'),
    path('product_dv/<int:pk>' , views.soon_dv , name = 'product_dv'),
    
    path('feedback' , views.feedback_page , name = 'feedback'),
    path('coop' , views.coop_page , name = 'coop'),
    path('News_page_search/' , views.News_page_search.as_view() , name= 'News_page_search'),
    
    path('sauna', views.page_sauna , name = "sauna" ),
    path('sush', views.page_sush , name = "sush" ),
    path('tepl', views.page_tepl , name = "tepl" ),
    path('soon', views.page_soon.as_view() , name = "soon" ),
    path('faq', views.page_faq.as_view() , name = "faq"),
    path('rev', views.page_rev.as_view() , name = "rev"),
    ]
