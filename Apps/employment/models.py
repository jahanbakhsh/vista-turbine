from django.db import models

class PersonalInformation(models.Model):
    full_name = models.CharField(max_length=60)
    futher_name = models.CharField(max_length=30)
    gender = models.CharField(max_length=10)
    military = models.CharField(max_length=20)
    status = models.CharField(max_length=15)
    child_num = models.CharField(max_length=2)
    email = models.CharField(max_length=30)
    mobil = models.CharField(max_length=15)

class Eucation(models.Model):
    person = models.ForeignKey(PersonalInformation,on_delete=models.CASCADE )
    level = models.CharField(max_length=10)
    majored = models.CharField(max_length=40)
    field = models.CharField(max_length=50)
    date_from = models.CharField(max_length=12)
    date_to = models.CharField(max_length=12)
    school = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    average = models.CharField(max_length=5)

class Job(models.Model):
    person = models.ForeignKey(PersonalInformation,on_delete=models.CASCADE )
    company = models.CharField(max_length=50)
    employment = models.CharField(max_length=20)
    date_from = models.CharField(max_length=12)
    date_to = models.CharField(max_length=12)
    position = models.CharField(max_length=30)
    salary = models.CharField(max_length=100)
    reason = models.CharField(max_length=1000)
    description = models.CharField(max_length=1000)

class Certificate(models.Model):
    person = models.ForeignKey(PersonalInformation,on_delete=models.CASCADE )
    certificate = models.CharField(max_length=150)
    score = models.CharField(max_length=4)
    issued = models.CharField(max_length=50)
    date = models.CharField(max_length=12)

class LanguageLevel(models.Model):
    person = models.ForeignKey(PersonalInformation,on_delete=models.CASCADE )
    level = models.CharField(max_length=20)
    language = models.CharField(max_length=30)

class ComputerLevel(models.Model):
    person = models.ForeignKey(PersonalInformation,on_delete=models.CASCADE )
    level = models.CharField(max_length=20)
    program = models.CharField(max_length=100)



