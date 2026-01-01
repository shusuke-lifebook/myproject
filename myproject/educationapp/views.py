from django.shortcuts import get_object_or_404, render

from .models import Profile, SchoolClass, Student

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


# 生徒とプロフィールを統合するビュー関数
def student_with_profile(request):
    # StudentとProfileを内部結合して、すべてのデータを取得
    students_with_profiles = Student.objects.select_related("profile")

    # テンプレートにデータを渡して表示
    return render(
        request,
        "educationapp/student_profile_list.html",
        {"students_with_profiles": students_with_profiles},
    )


# クラスを選択して
# そのクラスに所属する生徒を表示するビュー関数
def class_students(request):
    # すべてのクラスを取得してプルダウン用に提供
    classes = SchoolClass.objects.all()

    # GETパラメータから選択されたクラスのIDを取得
    selected_class_id = request.GET.get("class_id")

    # 選択されたクラスに基づいて生徒を取得(1対多の関係を利用)
    if selected_class_id:
        # 選択されたクラスを取得
        selected_class = SchoolClass.objects.get(id=selected_class_id)
        # 1体多の関係を利用する
        # クラスに所属する生徒を取得(related_nameを使用)
        students = selected_class.students.all()  # type: ignore
    else:
        # クラスが選択されていない場合は、Noneを設定
        selected_class = None
        students = None

    # テンプレートにデータを渡して表示
    return render(
        request,
        "educationapp/class_students.html",
        {"classes": classes, "students": students, "selected_class": selected_class},
    )
