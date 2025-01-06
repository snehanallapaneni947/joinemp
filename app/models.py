from django.db import models

# Create your models here.
class Dept(models.Model):
    deptno=models.IntegerField(max_length=50,primary_key=True)
    
    deptname=models.CharField(max_length=100)
    deptloc=models.CharField(max_length=100)

    


class Emp(models.Model):
    deptno=models.ForeignKey(Dept,on_delete=models.CASCADE)
    empid=models.IntegerField(max_length=10,primary_key=True)
    empname=models.CharField(max_length=30)
    empjob=models.CharField(max_length=10)
    empsal=models.DecimalField(max_digits=10,decimal_places=2)
    empcomm=models.DecimalField(max_digits=10,decimal_places=3,null=True,blank=True)
    emphirdate=models.DateField()
    empmgr=models.ForeignKey('self',on_delete=models.SET_NULL,null=True,blank=True)
    

    