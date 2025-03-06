
from django.db import models
class Prof(models.Model):
    matricule = models.AutoField(db_column='Matricule', primary_key=True)  # Field name made lowercase.
    nomprof = models.CharField(db_column='NomProf', max_length=51, blank=True, null=True)  # Field name made lowercase.
    prenomprof = models.CharField(db_column='PrenomProf', max_length=50, blank=True, null=True)  # Field name made lowercase.
    telprof = models.IntegerField(db_column='TelProf', blank=True, null=True)  # Field name made lowercase.
    specialite = models.CharField(db_column='Specialite', max_length=50, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'prof'
    def __str__(self):
        return f"{self.nomprof}"

class Mention(models.Model):
    numment = models.AutoField(db_column='NumMent', primary_key=True)  # Field name made lowercase.
    mention = models.CharField(db_column='Mention', max_length=51, blank=True, null=True)  # Field name made lowercase.
    code = models.CharField(max_length=50, blank=True, null=True)
    

    class Meta:
        managed = False
        db_table = 'mention'
    def __str__(self):
        return f"{self.code}"

class Salle(models.Model):
    numsalle = models.AutoField(primary_key=True)
    nomsalle = models.CharField(db_column='Nomsalle', max_length=11, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'salle'
    def __str__(self):
        return f"{self.nomsalle}"

        
class Edt(models.Model):
    numedt = models.AutoField(db_column='Numedt', primary_key=True)  # Field name made lowercase.
    jours = models.CharField(db_column='Jours', max_length=22, blank=True, null=True)  # Field name made lowercase.
    matiere = models.CharField(db_column='Matiere', max_length=50, blank=True, null=True)  # Field name made lowercase.
    date = models.DateField(db_column='Date', blank=True, null=True)  # Field name made lowercase.
    heurede = models.TimeField(db_column='HeureDe')  # Field name made lowercase.
    heurefin = models.TimeField(db_column='HeureFin')  # Field name made lowercase.
    salles = models.CharField(db_column='Salles', max_length=11, blank=True, null=True)  # Field name made lowercase.
    prof = models.CharField(db_column='Prof', max_length=51, blank=True, null=True)  # Field name made lowercase.
    mention = models.CharField(db_column='Mention', max_length=51, blank=True, null=True)  # Field name made lowercase.
    niveau = models.CharField(db_column='Niveau', max_length=50)  # Field name made lowercase.
    matricule = models.ForeignKey('Prof', models.DO_NOTHING, db_column='Matricule')  # Field name made lowercase.
    numm = models.ForeignKey('Mention', models.DO_NOTHING, db_column='Numm')  # Field name made lowercase.
    numsalle = models.ForeignKey('Salle', models.DO_NOTHING, db_column='numsalle')
    class Meta:
        managed = False
        db_table = 'edt'

    def __str__(self):
        return f"{self.matiere} le {self.jours} de {self.date} {self.heurede}, {self.matricule}-{self.numsalle}({self.date}{self.heurede }-{self.heurefin }) "
      

class Utilisateur(models.Model):
    nomutilisateur = models.CharField(max_length=70)
    mdput = models.CharField(max_length=56)
    idut = models.AutoField(primary_key=True)

    class Meta:
        managed = False
        db_table = 'utilisateur'
