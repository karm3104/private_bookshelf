from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse_lazy

from ..models import Bookshelf


class LoggedInTestCase(TestCase):
    """各テストクラスで共通の事前準備処理をオーバーライドした独自TestCaseクラス"""

    def setUp(self):
        """テストメソッド実行前の事前設定"""

        # テストユーザーのパスワード
        self.password = '12345@12345'

        # 各インスタンスメソッドで使うテスト用ユーザーを生成しインスタンス変数に格納しておく
        self.test_user = get_user_model().objects.create_user(
            username= 'testBsUser',
            email = 'test@example.com',
            password = self.password
        )

        #テスト用ユーザーでログインする
        self.client.login(email = self.test_user.email,password = self.password)

class TestBookshelfCreateView(LoggedInTestCase):
    """BookshelfCreateView用のテストクラス"""

    def test_create_bookshelf_success(self):
        """作成処理が成功することを検証する"""

        #Postパラメータ
        params = {'title': 'テストタイトル',
                'auther': 'z',
                'publisher': 'z',
                'isbnum': 'z',
                'comment': '3',
                'group': 'z',
                'readpage': '3',
                'evalution': '3',
                'photo': ''}

        #新規作成処理(POST)を実行
        response = self.client.post(reverse_lazy('bookshelf:book_create'), params)

        # 本棚リストページへのリダイレクトを検証
        self.assertRedirects(response, reverse_lazy('bookshelf:book_list'))

        # データがDBに登録されたかを検証
        self.assertEqual(Bookshelf.objects.filter(title='テストタイトル').count(), 1)

    def test_create_bookshelf_failure(self):
        """新規作成処理が失敗する事を検証する"""

        # 新規日記作成処理(Post)を実行
        response = self.client.post(reverse_lazy('bookshelf:book_create'))

        # 必須フォームフィールドが未入力によりエラーになる事を検証
        self.assertFormError(response, 'form', 'title', 'このフィールドは必須です。')


class TestBookshelfUpdateView(LoggedInTestCase):
    """BookshelfUpdateView用のテストクラス"""

    def test_update_bookshelf_success(self):
        """編集処理が成功する事を検証する"""

        # テスト用データの作成
        books = Bookshelf.objects.create(user=self.test_user, title='タイトル編集前')

        # Postパラメータ
        params = {'title': 'タイトル編集後'}

        # 編集処理(Post)を実行
        response = self.client.post(reverse_lazy('bookshelf:book_update', kwargs={'pk': books.pk}), params)

        # 詳細ページへのリダイレクトを検証
        self.assertRedirects(response, reverse_lazy('bookshelf:book_detail', kwargs={'pk': books.pk}))

        # データが編集されたかを検証
        self.assertEqual(Bookshelf.objects.get(pk=books.pk).title, 'タイトル編集後')

    def test_update_bookshelf_failure(self):
        """編集処理が失敗する事を検証する"""

        # 編集処理(Post)を実行
        response = self.client.post(reverse_lazy('bookshelf:book_update', kwargs={'pk': 999}))

        # 存在しないデータを編集しようとしてエラーになる事を検証
        self.assertEqual(response.status_code, 404)


class TestBookshelfDeleteView(LoggedInTestCase):
    """BookshelfDeleteView用のテストクラス"""

    def test_delete_bookshelf_success(self):
        """削除処理が成功する事を検証する"""

        # テスト用本データの作成
        books = Bookshelf.objects.create(user=self.test_user, title='タイトル')

        # 削除処理(Post)を実行
        response = self.client.post(reverse_lazy('bookshelf:book_delete', kwargs={'pk': books.pk}))

        # リストページへのリダイレクトを検証
        self.assertRedirects(response, reverse_lazy('bookshelf:book_list'))

        # データが削除されたかを検証
        self.assertEqual(Bookshelf.objects.filter(pk=books.pk).count(), 0)

    def test_delete_booklist_failure(self):
        """削除処理が失敗する事を検証する"""

        # 削除処理(Post)を実行
        response = self.client.post(reverse_lazy('bookshelf:book_delete', kwargs={'pk': 999}))

        # 存在しない日記データを削除しようとしてエラーになる事を検証
        self.assertEqual(response.status_code, 404)