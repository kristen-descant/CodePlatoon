from django.shortcuts import render
from django.core.serializers import serialize
import json
from rest_framework.views import APIView, Response
from .models import Class
from grade_app.models import Grade
from django.http import Http404


# Create your views here.
class All_Classes(APIView):

    def get(self, request):
        all_classes = Class.objects.all()
        serialized_classes = serialize("json", all_classes)
        json_classes = json.loads(serialized_classes)

        for current_class in range(len(json_classes)):
            class_grades = list(Grade.objects.filter(a_class = json_classes[current_class]['pk']).values())
            average_class_grade = sum([x['grade'] for x in class_grades])/len(class_grades) if len(class_grades) > 0 else 0
            json_classes[current_class]['fields']['grade_average']= average_class_grade
            json_classes[current_class]['fields']['students'] = json.loads(serialize('json', all_classes[current_class].students.all()))

        return Response(json_classes)
    
class A_Class(APIView):
    
    def get(self, request, id):
        try:
            serialized_class = serialize('json', [Class.objects.get(subject = id.title())])
            select_class = json.loads(serialized_class)

            class_grades = list(Grade.objects.filter(a_class = select_class[0]['pk']).values())
            average_class_grade = sum([x['grade'] for x in class_grades])/len(class_grades) if len(class_grades) > 0 else 0
            select_class[0]['fields']['grade_average'] = average_class_grade
            class_object = Class.objects.get(subject=id.title())
            select_class[0]['fields']['students'] = json.loads(serialize('json', class_object.students.all()))

            return Response(select_class[0])
    
        except Class.DoesNotExist:
            raise Http404("Class not found")