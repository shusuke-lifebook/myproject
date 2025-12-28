from django.shortcuts import get_object_or_404, render

from .models import Student

# Create your views here.


# 生徒情報をすべて取得するビュー関数
def get_all_students(request):
    # ☆ SELECT * FROM Student; と同じ
    student_list = Student.objects.all()
    return render(request, "educationapp/student_list.html", {"students": student_list})


# 生徒情報をIDで取得するビュー関数
def get_student_by_id(request, id):
    # ☆ SELECT * FROM Student WHERE id = 値と同じ
    student = get_object_or_404(Student, id=id)
    return render(request, "educationapp/student_detail.html", {"student": student})
