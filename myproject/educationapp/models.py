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


# ===================================================
# プロフィール(Profile) テーブル
# ===================================================
class Profile(models.Model):
    # 生徒と1対1の関係を持つ
    # OneToOneFieldを使用し、生徒とプロフィールが1対1の関係を保つ
    # on_delete=models.CASCADEにより、生徒が削除された場合に対応するプロフィールも削除される
    student = models.OneToOneField(Student, on_delete=models.CASCADE)
    # 住所
    address = models.CharField(max_length=255)
    # 電話番号
    phone_number = models.CharField(max_length=20)
    # その他の情報
    bio = models.TextField(null=True, blank=True)


# ===================================================
# クラス(SchoolClass) テーブル
# ===================================================
class SchoolClass(models.Model):
    # クラス名
    name = models.CharField(max_length=100)
    # クラスの説明
    description = models.TextField()
