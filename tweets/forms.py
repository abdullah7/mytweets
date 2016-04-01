from django import forms

class TweetForm(forms.Form):
    """
    Tweet Form
    """
    text = forms.CharField(
        widget=forms.Textarea(attrs={'rows': 1, 'cols': 85}),
        max_length=160,
    )
    country = forms.CharField(widget=forms.HiddenInput(), required=False)

