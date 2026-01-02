from django.test import TestCase
from django.urls import reverse

from .models import Sample


# Create your tests here.
# Sampleモデルをテストするクラス
class SampleTest(TestCase):
    # ===================================================
    # テストデータを準備するメソッド
    # ===================================================
    def setUp(self) -> None:
        self.sample1 = Sample.objects.create(name="テスト1")
        self.sample2 = Sample.objects.create(name="テスト2")

    # ===================================================
    # モデルの基本動作を確認するテスト
    # ===================================================
    def test_sample_model(self):
        # Sampleモデルのデータ件数が2件であることを確認
        self.assertEqual(Sample.objects.count(), 2)
        # 特定のデータが正しく登録されているかを確認
        sample = Sample.objects.get(name="テスト1")
        self.assertEqual(sample.name, "テスト1")

    # ===================================================
    # URLが正しく設定されているかを確認するテスト
    # ===================================================
    def test_urls(self):
        # /ex05/samples/にアクセスしてステータスコードが200を確認
        response = self.client.get("/exe05/samples/")
        self.assertEqual(response.status_code, 200)

    # ===================================================
    # 名前付きURLが正しく設定されているかを確認するテスト
    # ===================================================
    def test_sample_list_view(self):
        # 名前付きURL(reverse)でアクセスしてステータスコード200を確認
        response = self.client.get(reverse("sample_list"))
        self.assertEqual(response.status_code, 200)

    # ===================================================
    # サンプル詳細ビューが正しく動作しているかを確認するテスト
    # ===================================================
    def test_sample_detail(self):
        # サンプル1の詳細ページにアクセスしてステータスコード200を確認
        response = self.client.get(reverse("sample_detail", args=[self.sample1.id]))  # type: ignore
        self.assertEqual(response.status_code, 200)

    # ===================================================
    # サンプル作成ビューが正しく動作しているかを確認するテスト
    # ===================================================
    def test_sample_create(self):
        # POSTリクエストで新しいデータを作成
        data = {"name": "新しいテスト"}
        self.client.post(reverse("sample_create"), data)
        # データベースに新しいデータが作成されていること
        self.assertTrue(Sample.objects.filter(name="新しいテスト").exists())
