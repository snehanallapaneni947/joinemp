from django.shortcuts import render

# Create your views here.
from app.models import *
from django.db.models.functions import Length

def empdept(request):
    
    LEDO=Emp.objects.select_related('deptno').all()
    LEDO=Emp.objects.select_related('deptno').filter(empsal__gt=40000)
    LEDO=Emp.objects.select_related('deptno').filter(empsal__lt=40000)
    LEDO=Emp.objects.select_related('deptno').order_by('empname')
    LEDO=Emp.objects.select_related('deptno').order_by('-empname')
    LEDO=Emp.objects.select_related('deptno').order_by(Length('empname'))
    LEDO=Emp.objects.select_related('deptno').order_by(Length('empname').desc())
    LEDO=Emp.objects.select_related('deptno').filter(empcomm__isnull=True)
    LEDO=Emp.objects.select_related('deptno').filter(empname='sneha')
    LEDO=Emp.objects.select_related('deptno').filter(empjob='salesman')
    LEDO=Emp.objects.select_related('deptno').exclude(empmgr__isnull=False)
    LEDO=Emp.objects.select_related('deptno').filter(empjob__startswith='s')
    LEDO=Emp.objects.select_related('deptno').exclude(empname__regex='W+\s')
    d={'LEDO':LEDO}
    
    return render(request,'empdept.html',d)
