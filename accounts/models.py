from django.db import models
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import AbstractUser, UserManager
 

class CustomUser(AbstractUser, UserManager):
    
    email = models.EmailField(_('email address'), unique=True)  #emailを必須＆ユニークに設定
    thumbnail = models.ImageField(upload_to="images/thumbnail/", verbose_name="サムネイル", default="images/thumbnail/user_image.jpg")

    USERNAME_FIELD = 'email'   #ログオンIDをユーザ名→Emailへ変更
    REQUIRED_FIELDS = ['username']       #デフォルトのemailからusernameへ変更
    
    def __str__(self):
        return self.email
