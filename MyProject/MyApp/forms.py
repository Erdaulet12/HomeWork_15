from django import forms


class UserSearchForm(forms.Form):
    user_id = forms.IntegerField(label='User ID', required=True)
