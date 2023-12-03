from django import forms
from django.contrib.auth.models import User
from .models import Property, Event, Profile


class RegistrationForm(forms.ModelForm):
    password = forms.CharField(label='Password', widget=forms.PasswordInput)
    confirm_password = forms.CharField(label='Confirm Password', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name']

    def clean_confirm_password(self):
        password = self.cleaned_data.get('password')
        confirm_password = self.cleaned_data.get('confirm_password')
        if password and confirm_password and password != confirm_password:
            raise forms.ValidationError("Passwords don't match")
        return confirm_password

    def save(self, commit=True):
        user = super(RegistrationForm, self).save(commit=False)
        user.set_password(self.cleaned_data['password'])
        if commit:
            user.save()
        return user


class PropertyForm(forms.ModelForm):
    class Meta:
        model = Property
        fields = ['name','status', 'description', 'address', 'bedrooms', 'bathrooms', 'square_feet', 'price',
                  'featured_property', 'property_image_main', 'property_image_1', 'property_image_2',
                  'property_image_3', 'property_type', 'property_neighborhood', 'property_type_price_range']


class EventForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = ['picture', 'description']


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['profile_image', 'phonenumber', 'email', 'address']
