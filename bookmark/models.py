from django.db import models
from django.urls import reverse

# Create your models here.
# ORM : 데이터베이스(sql 등)를 몰라도 데이터를 객체화시켜서 관리해보자
# 모델 : 데이터베이스를 SQL없이 다루려고 모델을 사용
# 모델 = 테이블(데이터베이스)
# 모델의 필드 = 테이블의 컬럼 (열)
# 인스턴스 = 테이블의 레코드 (행)
# 필드의 값(인스턴스의 필드값) = 레코드의 컬럼 데이터값 (값)

class Bookmark(models.Model):
    site_name = models.CharField(max_length=100)
    url = models.URLField('URL')
    # *** 필드의 종류가 결정하는 것  ***
    # 1. 데이터베이스의 컬럼 종류
    # 2. 제약 사항 (몇글자까지, 한글들어간다 등등)
    # 3. Form의 종류
    # 4. Form에서 제약 사항

    def __str__(self):
        return "이름 : " + self.site_name+", 주소 :" +self.url

    def get_absolute_url(self):
        return reverse('detail', args=[str(self.id)])
