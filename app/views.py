from django.shortcuts import render

# Create your views here.
from app.models import *
from django.db.models.functions import Length
from django.db.models import Q

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

def empmgrdata(request):
    LMDO=Emp.objects.select_related('empmgr').all()
    m={'LMDO':LMDO}

    return render(request,'empmgrdata.html',m)

def empdeptmgr(request):
    LEDMO=Emp.objects.select_related('empmgr','deptno').all()
    LEDMO=Emp.objects.select_related('empmgr','deptno').filter(empname__startswith='s',empmgr__empjob='clark')
    LEDMO=Emp.objects.select_related('empmgr','deptno').filter(deptno__deptname='Accounting')
    LEDMO=Emp.objects.select_related('empmgr','deptno').filter(Q(empsal__gt=30000) & Q(deptno__deptloc='chicago'))
    LEDMO=Emp.objects.select_related('empmgr','deptno').order_by('empname')
    LEDMO=Emp.objects.select_related('empmgr','deptno').filter(empcomm__isnull=False)

    e={'LEDMO':LEDMO}
    return render(request,'empdeptmgr.html',e)

def empDeptpr(request):
    LDEO=Dept.objects.prefetch_related('emp_set').all()
    print(LDEO)
    d={'LDEO':LDEO}
    return render (request,'empDeptpr.html',d)