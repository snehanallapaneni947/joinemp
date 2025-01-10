from django.shortcuts import render

# Create your views here.
from app.models import *
from django.db.models.functions import Length
from django.db.models import Q,Prefetch,Max,Min,Count,Sum,Avg

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
    LEDO=Emp.objects.select_related('deptno').all()

    MO=Emp.objects.select_related('deptno').aggregate(Max('empsal'))
    AO=Emp.objects.select_related('deptno').aggregate(Avg('empcomm'))
    print(MO)
    print(AO)
    
    LEDO=Emp.objects.select_related('deptno').annotate(LOE=Length('empname')).filter(LOE=5)
    LEDO=Emp.objects.select_related('deptno').annotate(LOE=Length('empname')).filter(LOE__gt=5)
    DO=Dept.objects.filter(deptno=10)
    MA=Emp.objects.filter(deptno__in=DO).select_related('deptno').aggregate(Max('empsal'))['empsal__max']
    print(MA)
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
     #all dept objects and all related emp objects
    
    LDEO=Dept.objects.prefetch_related('emp_set').filter(deptno=10)
     # only dept 10 object and all related emp objects

    LDEO=Dept.objects.prefetch_related(Prefetch('emp_set',queryset=Emp.objects.filter(empname='sneha')))
     # all dept objects but specific emp object
    
    DO=Dept.objects.filter(deptno=10)
    LDEO=Dept.objects.filter(deptno__in=DO).prefetch_related(Prefetch('emp_set',queryset=Emp.objects.filter(empname='sneha')))
     # only specific dept object and emp object
    DO=Dept.objects.filter(deptno=30)
    
    LDEO=Dept.objects.filter(deptno__in=DO).prefetch_related(Prefetch('emp_set',queryset=Emp.objects.filter(empsal__gt=1000)))

    

   # DO=Dept.objects.filter(deptno=10).values('deptname','deptloc')

   # EO=Emp.objects.filter(empname='sneha').values_list('empsal','empcomm','deptno')
   # print(EO)
    #print(DO)
    print(LDEO)
    d={'LDEO':LDEO}
    return render (request,'empDeptpr.html',d)

