from django.urls import path
from . import views

urlpatterns = [
    path("",views.predictor,name="predictor"),
    #path("result",views.result,name="result"),
    #path("result", views.predictor, name="result")

]
