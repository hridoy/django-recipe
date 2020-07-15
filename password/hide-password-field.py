class UserForm(UserChangeForm):
    # To Hide the password field from default form
    password = None

    class Meta:
        model = User
        fields = (
            'first_name',
            'last_name',
            'email',
            )