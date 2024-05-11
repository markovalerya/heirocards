from django import forms
from django.contrib.auth.forms import AuthenticationForm

from .models import *


class RegisterPersonForm(forms.ModelForm):
    field_order = ['surname', 'name', 'login', 'password', 'password2']

    class Meta:
        model = Person
        fields = '__all__'

    surname = forms.CharField(
        label='Фамилия',
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Фамилия'
            }
        ),
    )
    name = forms.CharField(
        label='Имя',
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Имя'
            }
        ),
    )
    login = forms.CharField(
        label='Логин',
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Логин'
            }
        ),
    )
    password = forms.CharField(
        label='Пароль',
        widget=forms.PasswordInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Введите пароль'
            }
        ),
    )
    password2 = forms.CharField(
        label='Повторите пароль',
        widget=forms.PasswordInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Введите пароль повторно'
            }
        ),
    )


class GenerateBackgroundForm(forms.ModelForm):
    field_order = ['prompt', 'neg_prompt', 'style', 'transparency']

    class Meta:
        model = Background
        fields = 'prompt', 'neg_prompt', 'style', 'transparency'

    prompt = forms.CharField(
        max_length=1000,
        label='Промпт',
        widget=forms.TextInput(
            attrs={
                'placeholder': 'Введите запрос'
            }
        ),
    )
    neg_prompt = forms.CharField(
        max_length=1000,
        label='Негативный промпт',
        widget=forms.TextInput(
            attrs={
                'placeholder': 'Введите то, что не хотелось видеть на изображении'
            }
        ),
    )
    style = forms.ChoiceField(
        label='Стиль',
        choices=(("KANDINSKY", "Кандинский"), ("UHD", "Детальное фото"), ("ANIME", "Аниме"), ("DEFAULT", "Без стиля"), )

    )
    transparency = forms.ChoiceField(
        label='Размытие',
        choices=((0, "Без размытия"), (3, "Среднее"), (5, "Большое"), )
    )


class GenerateLogoForm(forms.ModelForm):
    field_order = ['prompt', 'neg_prompt', 'style']

    class Meta:
        model = Logo
        fields = 'prompt', 'neg_prompt', 'style'

    prompt = forms.CharField(
        max_length=1000,
        label='Промпт',
        widget=forms.TextInput(
            attrs={
                'placeholder': 'Введите запрос'
            }
        ),
    )
    neg_prompt = forms.CharField(
        max_length=1000,
        label='Негативный промпт',
        widget=forms.TextInput(
            attrs={
                'placeholder': 'Введите то, что не хотелось видеть на изображении'
            }
        ),
    )
    style = forms.ChoiceField(
        label='Стиль',
        choices=(("KANDINSKY", "Кандинский"), ("UHD", "Детальное фото"), ("ANIME", "Аниме"), ("DEFAULT", "Без стиля"), )
    )


class TextForm(forms.ModelForm):
    field_order = ['name', 'description', 'phone', 'address', 'text', 'text_size']

    class Meta:
        model = Card
        fields = 'name', 'description', 'phone',  'address', 'text', 'text_size'

    name = forms.CharField(
        max_length=100,
        label='Название',
        widget=forms.TextInput(
            attrs={
                'placeholder': 'Введите название'
            }
        ),
    )
    description = forms.CharField(
        max_length=100,
        label='Описание',
        widget=forms.TextInput(
            attrs={
                'placeholder': 'Описание компании'
            }
        ),
    )
    phone = forms.CharField(
        max_length=20,
        label='Телефон',
        widget=forms.TextInput(
            attrs={
                'placeholder': 'Введите ваш номер телефона'
            }
        ),
    )
    address = forms.CharField(
        max_length=30,
        label='Адрес',
        widget=forms.TextInput(
            attrs={
                'placeholder': 'Введите ваш адрес'
            }
        ),
    )
    text = forms.ChoiceField(
        label='Шрифт',
        choices=(("card/font/Merriweather-BoldItalic.ttf", "Merriweather"), ("card/font/Geologica-VariableFont.ttf", "Geologica"), )
    )
    text_size = forms.ChoiceField(
        label='Размер шрифта',
        choices=((30, "Стандарный"), (20, "Маленький"),)
    )
    text_color = forms.ChoiceField(
        label='Цвет шрифта',
        choices=(("black", "Черный"), ("white", "Белый"),)
    )


class PersonLoginForm(AuthenticationForm):
    username = forms.CharField(label="Логин", widget=forms.TextInput(attrs={"class": "form-control",
                                                                            "placeholder": "Введите логин"}))
    password = forms.CharField(label="Пароль", widget=forms.PasswordInput(
        attrs={"class": "form-control", "placeholder": "Введите пароль"}))

