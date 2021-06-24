





from django.urls import path

from Inventory import views

urlpatterns = [
    path('' , views.index,name='index'),
    path('display_laptops/',views.display_laptop,name='display_laptops'),
    path('display_desktops/',views.display_desktops,name='display_desktops'),
    path('display_mobiles/',views.display_mobiles,name='display_mobiles'),
    path('add_laptop/',views.add_Laptops,name='add_laptop'),
    path('add_desktops/',views.add_Desktop,name='add_desktops'),
    path('add_mobiles/',views.add_Mobiles,name='add_mobiles'),
    path('edit_laptops/<int:pk>',views.edit_laptops,name='edit_laptops'),
    path('edit_desktops/<int:pk>',views.edit_desktops,name='edit_desktops'),
    path('edit_mobiles/<int:pk>',views.edit_mobiles,name='edit_mobiles')
]
