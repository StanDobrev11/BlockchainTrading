from django.contrib.auth import forms as auth_forms, get_user_model

UserModel = get_user_model()


class UserCreateForm(auth_forms.UserCreationForm):
    pass
    # class Meta(auth_forms.UserCreationForm.Meta):
    #     model = UserModel
    #     fields = (
    #         'email',
    #         'password1',
    #         'password2'
    #     )
