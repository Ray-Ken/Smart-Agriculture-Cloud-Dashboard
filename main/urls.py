from django.urls import path
from . import views

urlpatterns = [
	path('', views.home, name='main-home'),
	path('<int:id>', views.home, name='main-home'),

	path('allfarmersmaps/', views.allfarmersmaps, name='main-allfarmersmaps'),
	path('allfarmersmaps/<str:username>', views.allfarmersmaps, name='main-allfarmersmaps'),

	path('allnetworks/', views.allnetworks, name='main-allnetworks'),

	path('allfarms/', views.allfarms, name='main-allfarms'),
	path('allfarms/<str:networkname>', views.allfarms, name='main-allfarms'),

	path('adminmapdetails/', views.adminmapdetails, name='main-adminmapdetails'),
	path('adminmapdetails/<str:farmname>/<str:farmid>', views.adminmapdetails, name='main-adminmapdetails'),

	path('editFarm/<str:farmid>', views.editFarm, name='main-editFarm'),

	path('addClusterNode/<str:farmid>', views.addClusterNode, name='main-addClusterNode'),
	path('addSensorNode/<str:farmid>', views.addSensorNode, name='main-addSensorNode'),
]

