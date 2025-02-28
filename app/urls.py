from django.urls import path
from . import views
urlpatterns = [
    path("",views.Index.as_view(),name="index"),
    path("listStudents",views.ListOfStudents.as_view(),name="students"),
    path("listDegrees",views.ListOfDegrees.as_view(),name="degrees"),
    path("<slug:slug>",views.StudentDetail.as_view(),name="student-detail"),
]
# Degree.objects.get(name="matematicas").fkstudents.filter(finishedDegree=True)