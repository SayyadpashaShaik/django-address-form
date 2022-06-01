from django.urls import path
from . import views

#enter urls here

urlpatterns = [
    path('',views.createandretrieve,name='candr'),
    path('update/<int:pk>',views.update,name='update'),
    path('delete/<int:pk>',views.remove,name='delete')
]

