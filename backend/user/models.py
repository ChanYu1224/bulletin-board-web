from uuid import uuid4
from django.utils import timezone
from django.db import models
from django.utils.translation import ugettext_lazy as _

#AbstractBaseUserを利用してUserモデルをカスタマイズ
from django.contrib.auth.models import AbstractBaseUser
#PermissionMixinを用いてUserの認証を行う
from django.contrib.auth.models import PermissionsMixin
#BaseUserManagerを利用してUserManagerモデルをカスタマイズ
from django.contrib.auth.models import BaseUserManager

class UserManager(BaseUserManager):
  """manager for user profiles"""
  def create_user(self, request_data):
    """create a new user profile"""
    # 現在時刻
    now = timezone.now()
    # emailが入力されていないときはValueErrorを呼び出す
    if not request_data['email']:
      raise ValueError('User must have an email address')
    # ユーザのプロフィール
    profile = ""
    if request_data.get('profile'):
      profile = request_data['profile']
    # Userモデルを参照してuserを定義
    user = self.model(
      name=request_data['name'],
      email=self.normalize_email(request_data['email']),
      is_active=True,
      last_login=now,
      profile=profile,
    )
    # userが入力したパスワードをハッシュ化
    user.set_password(request_data['password'])
    # settings.pyでdefaultに設定されているDBに保存
    user.save(using=self._db)

    return user

  def create_superuser(self, name, email, password):
    """create and save a new superuser with given details"""
    request_data = {
      'name': name,
      'email': email,
      'password': password,
    }
    # 上記create_userを使用
    user = self.create_user(request_data)
    user.is_active = True
    # superuserの権限を適用
    user.is_superuser = True
    user.is_staff = True
    user.save(using=self._db)

    return user


class User(AbstractBaseUser, PermissionsMixin):
  """database model for users in the system"""

  id = models.UUIDField(default=uuid4, primary_key=True)
  email = models.EmailField(max_length=255, unique=True)
  name = models.CharField(max_length=255)
  is_active = models.BooleanField(default=True)
  is_staff = models.BooleanField(default=False)
  profile = models.TextField(blank=True)
  date_joined = models.DateTimeField(auto_now_add=True)

  # Managerのメソッドを使えるようにする
  objects = UserManager()
  # emailを利用したログイン認証に変更
  USERNAME_FIELD = 'email'
  # 必須項目追加
  REQUIRED_FIELDS = ['name']

  # 1つのnameフィールドで表示したいので、既存のメソッドをオーバーライド
  def get_full_name(self):
    return self.name

  def get_short_name(self):
    return self.name

  def __str__(self) -> str:
    return self.name

  class Meta:
    db_table = 'api_user'
    swappable = 'AUTH_USER_MODEL'