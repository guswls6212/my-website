from django.urls import path
from . import views
from leeblog.views import (
    MakerView,
    MakerCreateView,
    LabelView,
    LabelDetailView
)


app_name = 'lee'
urlpatterns = [

    #Maker
    path('camera/maker/index/', views.MakerView.as_view(), name='camera-maker_index'),
    path('maker/create/', views.MakerCreateView.as_view(), name='maker_create'),

    #Label
    path('label/maker/index/', views.MakerView.as_view(), name='label-maker_index'),
    path('label/<int:pk>/index/', views.LabelView.as_view(), name='label_index'),
    path('label/detail/<int:pk>/', views.LabelDetailView.as_view(), name='label_detail'),
    path('label/<int:pk>/create/', views.LabelCreateView.as_view(), name='label_create'),



    # path('', views.index, name='index'),
    path('', views.home, name='blog-home'),
    path('about/', views.about, name='blog-about'),
]
