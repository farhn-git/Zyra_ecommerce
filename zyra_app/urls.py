from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from zyra_app import views



urlpatterns=[
    path('',views.viewhome,name='homepage'),
    path('products/',views.view_product,name='products'),
    path('adminhome/',views.adminhome,name='adminhome'),



    
    path('viewproducts/',views.viewproducts,name='viewproducts'),
    path('addproducts/',views.addproducts,name='addproducts'),
    path('addproducts_post/',views.addproducts_post,name='addproducts_post'),
    path('addcollection/',views.addcollection,name='addcollection'),
    path('addcollection_post/',views.addcollection_post,name='addcollection_post'),

    path('viewdashboard/',views.viewdashbaord,name='viewdashboard'),
    path('viewcustomers/',views.viewcustomers,name='viewcustomers'),
    path('vieworders/',views.vieworder,name='vieworders'),
    path('viewpayments/',views.viewpayments,name='viewpayments'),
    
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

