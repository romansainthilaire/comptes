from django import forms
from django.contrib.auth.models import User
from utilisateurs.models import ProfilUtilisateur

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput(), label="Mot de passe")
    class Meta:
        model = User
        fields = ["username", "email", "password"]

class ProfilUtilisateurForm(forms.ModelForm):
    class Meta:
        model = ProfilUtilisateur
        fields = ["site_portfolio", "photo_de_profil"]
