from lib.util import BaseAPIView
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework import status
from Apps.employment.models import *
import json
from Apps.employment.serializers import HierdSerializer



class Hierd(APIView, BaseAPIView):
    # permission_classes = (AllowAny,)
    serializer_classes = HierdSerializer
    def post(self, request, format=None, *args, **kwargs):
        try:
            serializer = self.serializer_classes(data=request.data)
            serializer.is_valid(raise_exception = True)
            validate_data = serializer.validated_data
        except:
            pass
        try:
            personal_information = validate_data.get('personal_information')
            person = PersonalInformation(
                full_name =personal_information.get('full_name',None) ,
                futher_name =personal_information.get('futher_name',None) ,
                gender =personal_information.get('gender',None) ,
                military =personal_information.get('military',None) ,
                status =personal_information.get('status',None) ,
                child_num =personal_information.get('child_num',None) ,
                email =personal_information.get('email',None) ,
                mobil =personal_information.get('mobil',None) ,
                )
            person.save()
        except Exception as e:
            print(e)

        try:
            education = validate_data.get('education')
            education = education[1:]
            for item in education:
                if item.get('majored') != '':
                    Eucation(
                        person = person,
                        level = item.get('level',None),
                        majored = item.get('majored',None),
                        field = item.get('field',None),
                        date_from = item.get('date_from',None),
                        date_to = item.get('date_to',None),
                        school = item.get('level',None),
                        city = item.get('level',None),
                        average = item.get('level',None)
                    ).save()
        except Exception as e:
            print(e)

        try:
            jobs = validate_data.get('jobs')[1:]
            for item in jobs:
                if item.get('company') != '':
                    Job(
                        person = person,
                        company = item.get('company',None),
                        employment = item.get('employment',None),
                        date_from = item.get('date_from',None),
                        date_to = item.get('date_to',None),
                        position = item.get('position',None),
                        salary = item.get('salary',None),
                        reason = item.get('reason',None),
                        description = item.get('description',None),
                    ).save()
        except Exception as e:
            print(e)
        try:
            certificates = validate_data.get('certificates')[1:]
            for item in certificates:
                if item.get('certificate') != '':
                    Certificate(
                        person = person,
                        certificate = item.get('certificate',None),
                        score = item.get('score',None),
                        issued = item.get('issued',None),
                        date = item.get('date',None),
                    ).save()
        except Exception as e:
            print(e)

        try:
            computer_level = validate_data.get('computer_level')[1:]
            for item in computer_level:
                if item.get('level') != '':
                    ComputerLevel(
                        person = person,
                        level = item.get('level',None),
                        program = item.get('program',None),
                    ).save()
        except Exception as e:
            print(e)

        try:
            language_level = validate_data.get('language_level')[1:]
            for item in language_level:
                if item.get('level') != '':
                    LanguageLevel(
                        person = person,
                        level = item.get('level',None),
                        language = item.get('language',None),
                    ).save()
        except Exception as e:
            print(e)
        self.response.status_code=200
        return Response(data=self.response.as_dict(), status=status.HTTP_200_OK)
