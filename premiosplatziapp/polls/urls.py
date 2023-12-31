from django.urls import path

from . import views

app_name = "polls" # Variable para evitar el hardcodeo en mi template

urlpatterns = [
    path("", views.IndexView.as_view(), name="index"),
    path("<int:pk>/detail/", views.DetailView.as_view(), name="detail"),
    path("<int:pk>/results/", views.ResultView.as_view(), name="results"),
    path("<int:question_id>/vote/", views.vote, name="vote"),
]