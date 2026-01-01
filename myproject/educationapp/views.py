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


# 生徒情報をフィルターするビュー関数
def filter_students(request):
    # 初期クエリセット： 全生徒
    students = Student.objects.all()

    # GET パラメータからフィルタ条件(名前)を取得
    name_query = request.GET.get("name")

    # 名前の部分一致フィルタ
    if name_query:
        students = students.filter(name__icontains=name_query)

    # GET パラメータからフィルタ条件(年齢)を取得
    age_query = request.GET.get("age")
    age_operator = request.GET.get("age_operator")

    # 年齢の条件フィルタ
    if age_query and age_operator:
        try:
            age_value = int(age_query)
            if age_operator == "lt":
                students = students.filter(age__lt=age_value)
            elif age_operator == "eq":
                students = students.filter(age=age_value)
            elif age_operator == "gt":
                students = students.filter(age__gt=age_value)
        except ValueError:
            # 年齢が整数でない場合はフィルタをスキップ
            pass

    return render(request, "educationapp/student_list.html", {"students": students})
