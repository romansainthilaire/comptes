from django.db import models
from django.contrib.auth.models import User

class ProfilUtilisateur(models.Model):
    utilisateur = models.OneToOneField(User, on_delete=models.CASCADE)
    site_portfolio = models.URLField(blank=True)
    photo_de_profil = models.ImageField(upload_to="photos_de_profil", blank=True)

    def __str__(self):
        return self.utilisateur.username

