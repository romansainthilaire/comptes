from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from utilisateurs.models import ProfilUtilisateur
from utilisateurs.forms import UserForm, ProfilUtilisateurForm

def index_view(request):
    return render(request, "utilisateurs/index.html")

@login_required
def profil_view(request, pk) :
    if request.user.pk != pk :
        return redirect("utilisateurs:profil", request.user.pk)
    profil = ProfilUtilisateur.objects.get(utilisateur__pk=pk)
    context = {"profil": profil}
    return render(request, "utilisateurs/profil.html", context)

def inscription_view(request):
    user_form = UserForm()
    profil_utilisateur_form = ProfilUtilisateurForm()
    inscrit = False
    if request.method == "POST":
        user_form = UserForm(data=request.POST)
        profil_utilisateur_form = ProfilUtilisateurForm(data=request.POST)
        if user_form.is_valid() and profil_utilisateur_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()
            profil_utilisateur = profil_utilisateur_form.save(commit=False)
            profil_utilisateur.utilisateur = user
            if "photo_de_profil" in request.FILES:
                profil_utilisateur.photo_de_profil = request.FILES["photo_de_profil"]
            profil_utilisateur.save()
            inscrit = True
        else:
            print(user_form.errors, profil_utilisateur_form.errors)
    context = {"user_form": user_form, "profil_utilisateur_form": profil_utilisateur_form, "inscrit": inscrit}
    return render(request, "utilisateurs/inscription.html", context)

def connexion_view(request):
    if request.method == "POST":
        nom_utilisateur = request.POST.get("nom_utilisateur")
        mot_de_passe = request.POST.get("mot_de_passe")
        utilisateur = authenticate(username=nom_utilisateur, password=mot_de_passe)
        if utilisateur:
            if utilisateur.is_active:
                login(request, utilisateur)
                return redirect("utilisateurs:index")
            else:
                return HttpResponse("Compte innactif")
        else:
            return HttpResponse("Identifiants invalides")
    else:
        return render(request, "utilisateurs/connexion.html")

@login_required
def deconnexion_view(request):
    logout(request)
    return redirect("utilisateurs:index")
