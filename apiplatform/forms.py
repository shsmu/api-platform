from .models import *
from django import forms


Mothod  = (
    ('POST', 'POST'),
    ('GET', 'GET'),
    ('HEAD', 'HEAD'),
)

class ApiForm(forms.ModelForm):
    # projectid = forms.CharField(label='项目', initial=2)
    name = forms.CharField(label='接口名称')
    uri = forms.CharField(label='URI')
    mothod = forms.ChoiceField(label='Method', choices=Mothod)
    contenttype = forms.CharField(label='Content-Type', initial='application/json')
    charset = forms.CharField(label='字符集', initial='charset=utf-8')
    # reqdata = forms.ChoiceField(label='request data')
    # respdata = forms.CharField(label='response data')
    chk_field = forms.CharField(label='检查项', initial='err_code')
    expect_rst = forms.CharField(label='期望值', initial='0')
    timeout = forms.CharField(label='超时时间', initial='200')

class Meta:
    forms.model = Api


