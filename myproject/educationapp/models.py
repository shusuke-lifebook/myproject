from django.db import models

# Create your models here.


# ===================================================
# 生徒(Student) テーブル
# ===================================================
class Student(models.Model):
    # 生徒の名前
    name = models.CharField(max_length=100)
    # 生徒の年齢
    age = models.IntegerField()
    # 入学日
    enrollment_date = models.DateField()
