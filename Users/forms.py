from django import forms
from .models import User, Articles, Guest


class LoginForm(forms.Form):
    email = forms.EmailField()
    password = forms.CharField(
        widget=forms.PasswordInput()
    )

    email = forms.EmailField(
        label="",
        widget=forms.TextInput(
            attrs={
                'class': 'form-control form-control-user',
                'style': 'margin:10px',
                'placeholder': 'email',

            }
        )
    )

    password = forms.CharField(
        label="",
        widget=forms.PasswordInput(
            attrs={
                'class': 'form-control form-control-user',
                'style': 'margin:10px',
                'placeholder': 'password',

            }
        )
    )


class RegisterForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('name', 'password', 'email', 'mobile')

    email = forms.EmailField(
        label="",
        widget=forms.TextInput(
            attrs={
                'class': 'form-control form-control-user',
                'style': 'margin:10px',
                'placeholder': 'email',

            }
        )
    )

    name = forms.CharField(
        label="",
        widget=forms.TextInput(
            attrs={
                'class': 'form-control form-control-user',
                'style': 'margin:10px',
                'placeholder': 'name',

            }
        )
    )

    password = forms.CharField(
        label="",
        widget=forms.PasswordInput(
            attrs={
                'class': 'form-control form-control-user',
                'style': 'margin:10px',
                'placeholder': 'password',

            }
        )
    )

    mobile = forms.IntegerField(
        label="",
        widget=forms.TextInput(
            attrs={
                'class': 'form-control form-control-user',
                'style': 'margin:10px',
                'placeholder': 'mobile',

            }
        )
    )


class AddArticleform(forms.ModelForm):
    class Meta:
        model = Articles
        fields = ('Section', 'SubSection', 'title', 'article')

    Section = forms.CharField(
        label="",
        widget=forms.TextInput(
            attrs={
                'class': 'form-control form-control-user',
                'style': 'margin:10px',
                'placeholder': 'Enter the section',

            }
        )

    )

    SubSection = forms.CharField(
        label="",
        widget=forms.TextInput(
            attrs={
                'class': 'form-control form-control-user',
                'style': 'margin:10px',
                'placeholder': 'Enter the Sub-section',

            }
        )

    )
    title = forms.CharField(
        label="",
        widget=forms.TextInput(
            attrs={
                'class': 'form-control form-control-user',
                'style': 'margin:10px',
                'placeholder': 'title',

            }
        )
    )

    article = forms.Textarea()


class GuestinfoForm(forms.ModelForm):
    class Meta:
        model = Guest
        fields = ('name', 'emailid', 'contact')

    emailid = forms.EmailField(
        label="",
        widget=forms.TextInput(
            attrs={
                'class': 'form-control form-control-user',
                'style': 'margin:10px',
                'placeholder': 'email Id',

            }
        )
    )

    name = forms.CharField(
        label="",
        widget=forms.TextInput(
            attrs={
                'class': 'form-control form-control-user',
                'style': 'margin:10px',
                'placeholder': 'name',

            }
        )
    )



    contact = forms.CharField(
        label="",
        widget=forms.TextInput(
            attrs={
                'class': 'form-control form-control-user',
                'style': 'margin:10px',
                'placeholder': 'mobile',

            }
        )
    )