from django.db import models

# Create your models here.
class dept(models.Model):
    dept_name=models.CharField(max_length=100,primary_key=True)
    d_loc=models.CharField(max_length=100)
    hod=models.CharField(max_length=100)
    dno=models.BigIntegerField()
    def __str__(self):
        return self.dept_name
class emp(models.Model):
    dept_name=models.ForeignKey(dept,on_delete=models.CASCADE)
    ename=models.CharField(max_length=100)
    sal=models.BigIntegerField()
    mgr=models.CharField(max_length=100)
    empno=models.BigIntegerField()
    
    def __str__(self):
        return self.ename



