
from rest_framework import serializers
from .models import Department,Employee

class DepartmentSerializers(serializers.ModelSerializer):
    class Meta:
        model=Department
        fields=("department_id","department_name")


class EmployeeSerializers(serializers.ModelSerializer):
    class Meta:
        model=Employee
        fields=("employee_id","employee_name","employee_salary","department_id")
