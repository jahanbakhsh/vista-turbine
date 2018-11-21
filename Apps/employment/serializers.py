from rest_framework import serializers
from Apps.employment.models import PersonalInformation
class PersonalInformationSerializer(serializers.Serializer):
    full_name = serializers.CharField(max_length=60)
    futher_name = serializers.CharField(max_length=30)
    gender = serializers.CharField(max_length=10)
    military = serializers.CharField(max_length=20)
    status = serializers.CharField(max_length=15)
    child_num = serializers.CharField(max_length=2)
    email = serializers.CharField(max_length=30)
    mobil = serializers.CharField(max_length=15)

class EducationSerializer(serializers.ListField):
    level = serializers.CharField(max_length=10)
    majored = serializers.CharField(max_length=40)
    field = serializers.CharField(max_length=50)
    date_from = serializers.CharField(max_length=12)
    date_to = serializers.CharField(max_length=12)
    school = serializers.CharField(max_length=50)
    city = serializers.CharField(max_length=50)
    average = serializers.CharField(max_length=5)

class JobSerializer(serializers.ListField):
    company = serializers.CharField(max_length=50)
    employment = serializers.CharField(max_length=20)
    date_from = serializers.CharField(max_length=12)
    date_to = serializers.CharField(max_length=12)
    position = serializers.CharField(max_length=30)
    salary = serializers.CharField(max_length=100)
    reason = serializers.CharField(max_length=1000)
    description = serializers.CharField(max_length=255)

class CertificateSerializer(serializers.ListField):
    certificate = serializers.CharField(max_length=150)
    score = serializers.CharField(max_length=4)
    issued = serializers.CharField(max_length=50)
    date = serializers.CharField(max_length=12)

class LanguageLevelSerializer(serializers.ListField):
    level = serializers.CharField(max_length=20)
    language = serializers.CharField(max_length=30)

class ComputerLevelSerializer(serializers.ListField):
    level = serializers.CharField(max_length=20)
    program = serializers.CharField(max_length=100)


class HierdSerializer(serializers.Serializer):
    personal_information = PersonalInformationSerializer()
    education = EducationSerializer()
    jobs = JobSerializer()
    certificates = CertificateSerializer()
    language_level = LanguageLevelSerializer()
    computer_level = ComputerLevelSerializer()

