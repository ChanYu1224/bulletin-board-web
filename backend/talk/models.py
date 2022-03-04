from django.db import models
import uuid

from user.models import User

# Create your models here.
class Talk(models.Model):
  class Meta:
    db_table = 'talk'

  id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
  send_by = models.ForeignKey(User, verbose_name='送信者', on_delete=models.PROTECT)
  content = models.TextField()
  created_by = models.DateTimeField(verbose_name='登録日時', auto_now_add=True)
  updated_by = models.DateTimeField(verbose_name='更新日時', auto_now=True)

  def __str__(self) -> str:
    return 'talk id: '+ str(self.id)

