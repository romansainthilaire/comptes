from django.urls import path
from utilisateurs import views

app_name = "utilisateurs"

urlpatterns = [
    path("", views.index_view, name="index"),
    path("profil/<int:pk>/", views.profil_view, name="profil"),
    path("inscription/", views.inscription_view, name="inscription"),
    path("connexion/", views.connexion_view, name="connexion"),
    path("deconnexion/", views.deconnexion_view, name="deconnexion")
]

