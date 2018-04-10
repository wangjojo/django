from django import forms

class CommentForm(forms.Form):
    name = forms.CharField(label = '称呼',max_length = 16,error_messages = {
        'required':'请填写您的称呼',
        'max_length':'称呼太长了'
        })

    content = forms.CharField(label = '内容',error_messages = {
        'required': '请填写您的评论',
        'max_length':'评论内容太长了'
        })
