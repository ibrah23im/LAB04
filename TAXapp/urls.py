from django.urls import path 
from.import views
urlpatterns=[
    path("",views.defaultView,name="tax"),
    path("<int:number>",views.view2,name="number"),
    path("taxrate",views.TaxRate,name="rate")

]

