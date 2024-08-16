from django.db import models

# Create your models here.
class Department(models.Model):
    department_id=models.AutoField(primary_key=True)
    department_name=models.CharField(max_length=200)
    class Meta:
        db_table="department"
    
    def __str__(self):
        return self.department_name

class Employee(models.Model):
    employee_id=models.AutoField(primary_key=True)
    employee_name=models.CharField(max_length=200)
    employee_salary=models.FloatField()
    department_id=models.ForeignKey(Department,on_delete=models.CASCADE)
    class Meta:
        db_table="employee"
    
    def __str__(self):
        return self.employee_name+", working in "+self.department_id.department_name
