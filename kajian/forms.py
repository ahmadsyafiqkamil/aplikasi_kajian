from django.contrib.auth.forms import AuthenticationForm


class CustomLoginForm(AuthenticationForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].widget.attrs.update(
            {
                'class': 'form-control',
                'type': 'text',
                'placeholder': 'username',
            }
        )

        self.fields['password'].widget.attrs.update(
            {
                'class': 'form-control',
                'type': 'password',
                'placeholder': 'Enter your password',
            }
        )
