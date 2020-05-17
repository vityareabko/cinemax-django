from django.forms import ModelForm, TextInput
from allauth.account.forms import LoginForm, SignupForm, ChangePasswordForm, SetPasswordForm, AddEmailForm, ResetPasswordForm, ResetPasswordKeyForm
from .models import Comments
class MyCustomLoginForm(LoginForm):

    def __init__(self, *args, **kwargs):
        super(MyCustomLoginForm, self).__init__(*args, **kwargs)
        self.fields['login'].widget.attrs.update({
            'class': 'form-control',
            'id': 'formGroupExampleInput',
            'placeholder': ''     
         })
        self.fields['password'].widget.attrs.update({
            'class': 'form-control',
            'id': 'formGroupExampleInput2',
            'placeholder': ''
        })
        
class MyCustomSignupForm(SignupForm):
    def __init__(self, *args, **kwargs):
        super(MyCustomSignupForm, self).__init__(*args, **kwargs)
        for fieldname, field in self.fields.items():
            field.widget.attrs.update({
                'class': 'form-control'
        })
        
class MyCustomChangePasswordForm(ChangePasswordForm):
    def __init__(self, *args, **kwargs):
        super(MyCustomChangePasswordForm, self).__init__(*args, **kwargs)
        for fieldname, field in self.fields.items():
            field.widget.attrs.update({
                'class': 'form-control'
        })

class MyCustomSetPasswordForm(SetPasswordForm):
    def __init__(self, *args, **kwargs):
        super(MyCustomSetPasswordForm, self).__init__(*args, **kwargs)
        for fieldname, field in self.fields.items():
            field.widget.attrs.update({
                'class': 'form-control'
        })

class MyCustomAddEmailForm(AddEmailForm):
    def __init__(self, *args, **kwargs):
        super(MyCustomAddEmailForm, self).__init__(*args, **kwargs)
        for fieldname, field in self.fields.items():
            field.widget.attrs.update({
                'class': 'form-control'
        })

class MyCustomResetPasswordForm(ResetPasswordForm):
    def __init__(self, *args, **kwargs):
        super(MyCustomResetPasswordForm, self).__init__(*args, **kwargs)
        for fieldname, field in self.fields.items():
            field.widget.attrs.update({
                'class': 'form-control'
        })
        
class MyCustomResetPasswordKeyForm(ResetPasswordKeyForm):
    def __init__(self, *args, **kwargs):
        super(MyCustomResetPasswordKeyForm, self).__init__(*args, **kwargs)
        for fieldname, field in self.fields.items():
            field.widget.attrs.update({
                'class': 'form-control'
        })

############################################################

# class Comment(ModelForm):
#     class Meta:
#         model = Comments
#         fields = ['comment']
#     # comment = Forms.TextField()
    


   