from django.shortcuts import render
from django.http import JsonResponse
from .models import Department,Employee
from .serializers import DepartmentSerializers,EmployeeSerializers
# Create your views here.

def department_api(request):
    if request.method=="GET":
        departments = Department.objects.all();     #department is python object or query  
        department_serializer = DepartmentSerializers(departments,many=True)
        return JsonResponse(department_serializer.data,safe=False)



def employee_api(request):
    if request.method=="GET":
        employees = Employee.objects.all();
        employee_serializer = EmployeeSerializers(employees,many=True)
        return JsonResponse( employee_serializer.data,safe=False)