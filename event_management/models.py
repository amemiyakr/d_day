import uuid
from django.db import models
from common.models import BaseModel


class EventDay(BaseModel):
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

    class Meta:
        db_table = "event_day"


class EventUser(BaseModel):
    """　イベント参加者モデル　"""

    # 項目ID
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    # イベントID
    event_day = models.ForeignKey('EventDay', on_delete=models.PROTECT)
    # ユーザID
    user = models.ForeignKey('User', on_delete=models.PROTECT)

    class Meta:
        db_table = "event_user"


class User(BaseModel):
    """ ユーザモデル """

    # 姓
    last_name = models.CharField(max_length=20, default='')
    # 名
    first_name = models.CharField(max_length=20, default='')
    # 生年月日
    birthday = models.DateField(null=True)
    # 性別
    sex = models.CharField(max_length=6, default='')
    # メールアドレス
    email = models.EmailField(max_length=50, default='')

    class Meta:
        db_table = 'user'


class Menu(BaseModel):
    """　メニュー　"""

    # メニュー名
    title = models.CharField(max_length=20, default='')
    # アクセスURL
    url = models.CharField(max_length=20, default='')
    # 親メニューID
    parent = models.ForeignKey('self', on_delete=models.PROTECT)
    # Level
    level = models.CharField(max_length=20, default='')
    # 並び順
    order = models.CharField(max_length=20, default='')
    # icon
    icon = models.CharField(max_length=50, default='')

    class Meta:
        db_table = "menu"

