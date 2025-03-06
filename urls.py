from django.contrib import admin
from django.urls import path,include
# from .views import generate_pdf
from .views import*

urlpatterns = [
    path('/yy',hello,name='index'),
    path('gg/', salut , name='inscri'),
     path('pdf/', imprime , name='PDF'),
    path('prof/', pro , name='prof'),
    path('ET/', edt , name='emploi'),
    path('', login , name='miditra'),
    path('SALLE/', salle , name='Salle'),
    path('ajoutprof//', ajout , name='ajoutprof'),
    path('filiere/', ment , name='mention'),
    path('ajoutment//', ajoutM , name='ajoutment'),
     path('ajoutilisateur//', ajoutUti , name='ajoututili'),
    path('ajoutsalle//', ajoutS , name='ajoutsalle'),
     path('ajoutedt//', ajoutE , name='ajoutedt'),
    path('Suprimmer/',suppro, name='deleteprof' ),
    path('Suprimmeredt/',supedt, name='deletedt' ),
    # path('prof/', modifierP, name='editpro' ), 
    path('Modifierpro/', ModiPro, name='formuledit' ),
     path('Modifier/', ModiEdt, name='formule' ),
    path('editpro/<int:id>/',modifierP, name='EP'),  
    path('editedt/<int:id>/',modifierE, name='ET'),  
    path('test/', ito, name='formuleit' ),
    # path('generate-pdf/', generate_pdf, name='generate_pdf')

]