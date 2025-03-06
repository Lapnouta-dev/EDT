from pyexpat.errors import messages
from django.shortcuts import render,get_object_or_404, redirect

from .forms import*
from.models import Prof, Salle, Edt
from django.http import HttpResponse
from django.contrib import messages
from django.template.loader import render_to_string




def salut(request):
         
    return render(request,'inscription.html')



def hello(request):
    last_entry=Prof.objects.last()   
    lastS=Salle.objects.last()
    lastF=Mention.objects.last()
    lastE=Edt.objects.last()
    return render(request,'index.html',{'last_entry': last_entry,'lastS': lastS,'lastF': lastF,'lastE':lastE})

def salut(request):
         
    return render(request,'inscription.html')
def imprime(request):         
    return render(request,'pdf.html')
def edt(request):
        last_entry=Prof.objects.last()  
        lastS=Salle.objects.last()
        lastF=Mention.objects.last()
        lastE=Edt.objects.last()
        form =AjoutEdt()
        edt = Edt.objects.all() 
        et= Edt.objects.all().order_by('date','heurede')
        return render(request,'edt.html',{'edt':edt,'last_entry': last_entry,'lastS': lastS,'lastF': lastF,'lastE':lastE,'et':et})

def salle(request):
    last_entry=Prof.objects.last()  
    lastS=Salle.objects.last()
    lastF=Mention.objects.last()
    lastE=Edt.objects.last()
    form = AjoutSalle()
    salle = Salle.objects.all()
    return render(request,'salle.html',{'salle':salle,'last_entry': last_entry,'lastS': lastS,'lastF': lastF,'lastE':lastE})

def ModiPro(request):
         
    return render(request,'ModifiProf.html')
def ModiEdt(request):
         
    return render(request,'ModifiEdt.html')

def pro(request):
    last_entry=Prof.objects.last() 
    lastS=Salle.objects.last()
    lastF=Mention.objects.last()
    lastE=Edt.objects.last() 
    form= Ajoutprof()
    prof = Prof.objects.all()
    return render(request,'prof.html',{'prof':prof,'last_entry': last_entry,'lastS': lastS,'lastF': lastF,'lastE':lastE})

def ment(request):
    last_entry=Prof.objects.last()  
    lastS=Salle.objects.last()
    lastF=Mention.objects.last()
    lastE=Edt.objects.last()
    form=AjoutMent ()
    mention = Mention.objects.all()
    return render(request,'filiere.html',{'mention':mention,'last_entry': last_entry,'lastS': lastS,'lastF': lastF,'lastE':lastE})



def ajout(request):
    if request.method =='POST':
        form = Ajoutprof(request.POST)
        if form.is_valid():

            form.save()
            return render(request,'ajoutprof.html',{'form':form})
    else:
        form=Ajoutprof()
         
    return render(request,'ajoutprof.html',{'form':form})  

def ajoutM(request):
    if request.method =='POST':
        form = AjoutMent(request.POST)
        if form.is_valid():

            form.save()
            return render(request,'ajoutment.html',{'forma':form})
    else:
        form=AjoutMent()
         
    return render(request,'ajoutment.html',{'form':form}) 

def ajoutUti(request):
    if request.method =='POST':
        form = Ajoututile(request.POST)
        if form.is_valid():

            form.save()
            return render(request,'inscription.html',{'form':form})
    else:
        form=Ajoututile()
         
    return render(request,'inscription.html',{'formi':form}) 

def ajoutS(request):
    if request.method =='POST':
        form = AjoutSalle(request.POST)
        if form.is_valid():
            form.save()
            return render(request,'ajoutsalle.html',{'form':form})
    else:
        form=AjoutSalle()         
    return render(request,'ajoutsalle.html',{'form':form}) 

def ajoutE(request):
    if request.method =='POST':
        form = AjoutEdt(request.POST)
        if form.is_valid():
            form.save() 
            return render(request,'ajoutedt.html',{'form':form})
    else:
        form=AjoutEdt()         
    return render(request,'ajoutedt.html',{'form':form}) 
 
def suppro(request):
    if request.method =='POST' and 'delete' in request.POST:
        pro_id= request.POST.get('pro_id')
        if pro_id:
            prof=get_object_or_404(Prof,matricule=pro_id)
            prof.delete()
    return render(request,'prof.html')

def supedt(request):
    if request.method =='POST' and 'delete' in request.POST:
        edt_id= request.POST.get('edt_id')
        if edt_id:
            edt=get_object_or_404(Edt,numedt=edt_id)
            edt.delete()
    return render(request,'edt.html')
    
def modifierP(request,id):
    prof=Prof.objects.get(pk=id)
    if request.method=='POST':
        fore= ProfForm(request.POST,instance=prof)
        if fore.is_valid():
          fore.save()
          return redirect('prof')
    else:
        fore= ProfForm(instance=prof)
        pro=Prof.objects.all()
    return render(request,'ModifiProf.html',{'form':fore,'prof':pro})

def modifierE(request,id):
    edt=Edt.objects.get(pk=id)
    prot=Edt.objects.all()
    if request.method=='POST':
        fore= EdtForm(request.POST,instance=edt)
        if fore.is_valid():
          fore.save()
          return redirect('emploi')
    else:
        fore= EdtForm(instance=edt)
        prot=Edt.objects.all()
    return render(request,'ModifiEdt.html',{'form':fore,'edt':prot})

def ito(request):
    form = showmention()
    return render(request,'ajoutedt.html',{'forma':form})

# def generate_pdf(request):
#     # Créer le contexte des données à passer au template
#     context = {
#         'title': 'Mon PDF',
#         'content': 'Ceci est le contenu du PDF.',
#     }
    
#     # Rendre le template HTML
#     html_string = render_to_string('pdf.html', context)
    
#     # Créer un fichier temporaire pour le PDF
#     with tempfile.NamedTemporaryFile(delete=True, suffix=".pdf") as output:
#         HTML(string=html_string).write_pdf(output.name)
        
#         # Lire le fichier temporaire pour l'envoyer en réponse HTTP
#         output.seek(0)
#         response = HttpResponse(output.read(), content_type='application/pdf')
#         response['Content-Disposition'] = 'attachment; filename="generated_pdf.pdf"'
#         return response

def login(request):
    if request.method =='POST':
        loginForm=LoginForm(request.POST)
        if loginForm.is_valid():
            try:
                utilisateur=Utilisateur.objects.get(nomutilisateur=loginForm.cleaned_data["nomutilisateur"],
                mdput=loginForm.cleaned_data["mdput"])
                return redirect ('index')
            except Utilisateur.DoesNotExist:
                return redirect ('miditra')
            
    else:
        form = LoginForm()
    return render(request,'login.html',{'form':form})