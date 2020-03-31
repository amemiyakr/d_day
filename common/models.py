import uuid
from sequences import get_next_value
from django.db import models


class CommonModel(models.Model):
    """ Common Model """
    # id
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    # 削除Check
    is_deleted = models.CharField(null=False, default='0', max_length=1)
    # 作者
    created_user = models.SlugField(null=False, default=None, max_length=50)
    # 更新者
    updated_user = models.SlugField(null=False, default=None, max_length=50)
    # 作成日
    created_at = models.DateTimeField(null=False, auto_now_add=True)
    # 更新日
    updated_at = models.DateTimeField(null=False, auto_now=True)

    class Meta:
        abstract = True


class BaseModel(CommonModel):
    """ Base Model """

    def __init__(self, *args, **kwargs):
        from common.middleware import get_auth
        # insert時にユーザのアドレスを指定
        super(BaseModel, self).__init__(*args, **kwargs)
        self.created_user = self.created_user if self.created_user else get_auth().user.email
        # bulk_create時に必要
        self.updated_user = get_auth().user.email

    def save(self, *args, **kwargs):
        from common.middleware import get_auth
        # update時にユーザのアドレスを指定
        self.updated_user = get_auth().user.email
        super(BaseModel, self).save(*args, **kwargs)

    def get_next(self, field_name):
        key = f'{self._meta.db_table}.{field_name}'
        field_value = getattr(self, field_name)
        return get_next_value(key) if field_value is None else field_value

    class Meta:
        abstract = True