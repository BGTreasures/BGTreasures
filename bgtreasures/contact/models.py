from django import forms

class ContactForm(forms.Form):
    name = forms.CharField(max_length=100, label="Name")
    email = forms.EmailField(label="Email Address")
    message = forms.CharField(widget=forms.Textarea, label="Message")

    def __init__(self, *args, **kwargs):
        super(ContactForm, self).__init__(*args, **kwargs)
        # name
        self.fields['name'].widget.attrs['placeholder'] = self.fields['name'].label
        self.fields['name'].widget.attrs['class'] = "span3"
        # email
        self.fields['email'].widget.attrs['placeholder'] = self.fields['email'].label
        self.fields['email'].widget.attrs['class'] = "span3"
        # message
        self.fields['message'].widget.attrs['class'] = "input-xlarge span5"
