from django.db import models
from django.forms import ValidationError
import re



# Create your models here.





#경도위도 검증 함수 구현하여 아래 모델에 적용하기
def lnglat_validator(value):
    if not re.match(r'^([+-]?\d+\.?\d*),([+-]?\d+\.?\d*)$',value):
        raise ValidationError('Invalid Lnglat Type')



class Post(models.Model):
    title = models.CharField(max_length=100,
                             # choices=(
                             #     ('제목1','제목1 레이블'), #선택 박스를 넣어 줄 수 있다
                             #     ('제목2','제목2 레이블'),
                             #     ('제목3','제목3 레이블'),
                             #     )
                             verbose_name="제목", help_text='포스팅 제목을 입력해주세요. 최대 100자 내외.') #길이제한
    content = models.TextField(verbose_name="내용") #길이제한 없음
    tags = models.CharField(max_length=100, blank=True)
    lnglat = models.CharField(max_length=50, validators = [lnglat_validator] ,help_text="경도/위도 포맷으로 입력." ,blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
