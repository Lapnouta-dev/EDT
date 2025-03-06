from sched import scheduler
from.models import Edt, Prof, Salle, Utilisateur
from.models import Mention
from django import forms
from django.core.exceptions import ValidationError

class Ajoututile(forms.ModelForm):
    class Meta:
        model= Utilisateur
        fields=['nomutilisateur','mdput']
        widgets={
            'nomutilisateur':forms.TextInput(attrs={'class':'form-control'}) ,
            'mdput':forms.PasswordInput(attrs={'class':'form-control'}) ,
            
             }
        labels={
            'nomutilisateur':'Utilisateur',
            'mdput':'Mot de passe'
        }
class Ajoutprof(forms.ModelForm):
    class Meta:
        model= Prof
        fields=['nomprof','prenomprof','telprof','specialite']
        widgets={
            'nomprof':forms.TextInput(attrs={'class':'form-control'}) ,
            'prenomprof':forms.TextInput(attrs={'class':'form-control'}) ,
            'telprof':forms.TextInput(attrs={'class':'form-control'}) ,
            'specialite':forms.TextInput(attrs={'class':'form-control'}) ,
             }
    # def __int__(self, *args , **kwargs):
    #     super(Ajoutprof , self).__int__(*args, **kwargs)
    #     self.fields['nomprof'].choices=[(memt.nomprof,str(memt)) for memt in Mention.objects.all()]
     
class AjoutMent(forms.ModelForm):
    class Meta:
        model= Mention
        fields=['mention','code']
        widgets={
            'mention':forms.TextInput(attrs={'class':'form-control'}) ,
            'code':forms.TextInput(attrs={'class':'form-control'}) ,            
        }
    def __int__(self, *args , **kwargs):
        super(AjoutMent , self).__int__(*args, **kwargs)
        self.fields['mention'].choices=[(nomprof.mention,str(nomprof)) for nomprof  in Prof.objects.all()]
        
class AjoutSalle(forms.ModelForm):
    class Meta:
        model=Salle
        fields=['nomsalle']
        widgets={
            'nomsalle':forms.TextInput(attrs={'class':'form-control'}) ,
                        
        }
class AjoutEdt(forms.ModelForm):
     Jours_CHOICES =[
        ('Luindi','Luindi'),
        ('Mardi','Mardi'),
        ('Mercredi','Luindi'),
        ('Jeudi','Jeudi'),
        ('Vendredi','vendredi'),

    ]
     Niveau_CHOICES =[
        ('L1','L1'),
        ('L2','L2'),
        ('L3','L3'),
        ('M1','M1'),
        ('M2','M2'),

    ] 
     jours=forms.ChoiceField(choices=Jours_CHOICES, widget=forms.Select(attrs={'class':'form-control' }))
     niveau=forms.ChoiceField(choices=Niveau_CHOICES, widget=forms.Select(attrs={'class':'form-control' }))

     class Meta:
        model= Edt
        fields=['jours','matiere','date','heurede','heurefin','salles','prof','mention','niveau','matricule','numm','numsalle' ]     
        
        widgets={
            'jours':forms.TextInput(attrs={'class':'form-control'}) ,
            'matiere':forms.TextInput(attrs={'class':'form-control'}) ,
            'date':forms.DateInput(attrs={'class':'form-control','type':'date'}) ,
            'heurede':forms.TimeInput(attrs={'class':'form-control','type':'time'}) ,
            'heurefin':forms.TimeInput(attrs={'class':'form-control','type':'time'}) ,
            'salles':forms.Select(attrs={'class':'form-control'}) ,
            'mention':forms.Select(attrs={'class':'form-control'}) ,
            'prof':forms.Select(attrs={'class':'form-control'}) ,
            # 'numm':forms.Select(attrs={'class':'form-control'}) ,
             'niveau':forms.Select(attrs={'class':'form-control'}) ,
            # 'matricule':forms.Select(attrs={'class':'form-control'}) ,    
        }

    
        # if numsalle and heurede and heurefin and date:
        #     overlapping_schedules=Edt.objects.filter(
        #        idsalle=numsalle,
        #        HD_lt=heurefin,
        #        HF_gt=heurede,
        #        DT=date,
        #     )
        #     if overlapping_schedules.exists():
        #         conflicts=",".join([f"{schedule.heurede}-{schedule.heurefin}" for schedule in  overlapping_schedules ])
        #         raise forms.ValidationError(_("cette salle est dejà occupé:{0}.").format(conflicts))




class ProfForm(forms.ModelForm):
    class Meta:
        model=Prof
        fields=['nomprof','prenomprof','telprof','specialite']
class EdtForm(forms.ModelForm):
    class Meta:
        model=Edt
        fields= fields=['jours','matiere','date','heurede','heurefin','salles','prof','mention','niveau','matricule','numm','numsalle' ] 

class showmention(forms.Form):
     mention = forms.ModelChoiceField(queryset=Prof.objects.all(),empty_label="select nom",
                                      widget=forms.Select(attrs={'class':'form-control'}),
                                      )
class LoginForm(forms.ModelForm):
    class Meta:
        model=Utilisateur
        fields=['nomutilisateur','mdput']
        widgets={
            'mdput':forms.PasswordInput(attrs={'class':'form-control'})
            }
        labels={
            'nomutilisateur':'Utilisateur',
            'mdput':'Mot de passe'
        }

