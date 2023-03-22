from django import forms 

class LoginForms(forms.Form):
    name_login = forms.CharField(
        label="Nome de Login: ",
        required=True,
        max_length=30,
        widget=forms.TextInput(
            attrs={
                "class": "form-control",
                "placeholder": "alura-test"
            }
        )
    )

    password = forms.CharField(
        label="Senha: ",
        required=True,
        max_length=100,
        widget=forms.PasswordInput(
            attrs={
                "class": "form-control",
                "placeholder": "password"
            }
        )
    )


class CadastroForms(forms.Form):
    name_cadastro = forms.CharField(
        label="Name: ",
        required=True,
        max_length=100,
        widget=forms.TextInput(
            attrs={
                "class":"form-control",
                "placeholder": "alura-test"
            }
        )
    )

    password = forms.CharField(
        label="Password: ",
        required=True,
        max_length=100,
        widget=forms.PasswordInput(
            attrs={
                "class":"form-control",
                "placeholder":"Password"
            }
        )
    )

    email = forms.EmailField(
        label="Email: ", 
        required=True,
        max_length=100,
        widget=forms.EmailInput(
            attrs={
                "class":"form-control",
                "placeholder":"alura@email.com"
            }
        )
    )

    password2 = forms.CharField(
        label="Confirm Password: ",
        required=True,
        max_length=100,
        widget=forms.PasswordInput(
            attrs={
                "class":"form-control",
                "placeholder":"Confirm Password"
            }
        )
    )