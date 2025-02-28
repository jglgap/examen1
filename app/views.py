from django.shortcuts import render
from django.views import View
from django.views.generic import ListView, DetailView
from .models import Degree, Student
# Create your views here.
class Index(View):
    def get(self,request):
        return render(request,"exam1/index.html")
    
class ListOfStudents(ListView):
    template_name="exam1/student.html"
    model = Student
    context_object_name = "students"

class ListOfDegrees(ListView):
    template_name = "exam1/degree.html"
    model = Degree
    context_object_name = "degrees"

class StudentDetail(DetailView):
    template_name = "exam1/studentDetail.html"
    model = Student
