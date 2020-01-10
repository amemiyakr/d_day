import uuid
from django.db import models


class EventDay(models.Model):
    """　記念日モデル　"""

    # 項目ID
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    # イベント名称
    name = models.CharField(max_length=25, default="")
    # イベント日時
    date = models.DateField()
    # イベント場所
    local = models.CharField(max_length=30, default="")
    # イベント内容
    content = models.CharField(max_length=100, default='')
    # ユーザID（ユーザテーブル）
    user = models.ForeignKey('User', on_delete=models.PROTECT)
    # 基本項目　作成日、作成日時、更新日、更新日時、削除
    create_at = models.DateTimeField(null=False, auto_now_add=True)
    create_user = models.SlugField(null=False, default=None, max_length=50)
    update_at = models.DateTimeField(null=False, auto_now=True)
    updated_user = models.SlugField(null=False, default=None, max_length=50)
    is_delete = models.IntegerField(null=False, default='0', max_length=1)

    class Meta:
        db_table = "event_day"


class User(models.Model):
    """　ユーザモデル　"""

    # 項目ID
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    # ユーザ名
    name = models.CharField(max_length=25, default="")
    # ユーザパスワード
    password = models.CharField(max_length=32, default="")
    # ユーザメール
    mail = models.CharField(max_length=100, default='')
    # 基本項目　作成日、作成日時、更新日、更新日時、削除
    create_at = models.DateTimeField(null=False, auto_now_add=True)
    create_user = models.SlugField(null=False, default=None, max_length=50)
    update_at = models.DateTimeField(null=False, auto_now=True)
    updated_user = models.SlugField(null=False, default=None, max_length=50)
    is_delete = models.IntegerField(null=False, default='0', max_length=1)

    class Meta:
        db_table = "user"
