from django.core.cache import cache
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.views import LoginView
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import View
from .forms import *
from .generate import *
from .createcard import *
from django.contrib.auth.hashers import make_password


class Indexing(View):
    def get(self, request):
        return render(request, 'index.html', {})


class RegisterView(View):
    def post(self, request):
        form = RegisterPersonForm(request.POST)
        if form.is_valid():
            if form.cleaned_data['password'] == form.cleaned_data['password2']:
                userdata = form.save(commit=False)
                userdata.password = make_password(form.cleaned_data['password2'])
                userdata.save()
                userdata = form.save(commit=True)
                if userdata.id is not None:
                    person = Person.objects.get(pk=userdata.id)
                    username = form.cleaned_data.get('login')
                    password1 = form.cleaned_data.get('password')
                    user = User.objects.create_user(username=username, password=password1)
                    user = authenticate(username=username, password=password1)
                    login(request, user)
                    response = redirect('main')
                return response

    def get(self, request):
        form = RegisterPersonForm(request.POST, request.FILES)
        context = {'form': form, }
        return render(request, "registration.html", context)


class GenerateBackground(View):
    def get(self, request):
        form = GenerateBackgroundForm(request.POST)
        context = {'form': form, }
        return render(request, "background.html", context)

    def post(self, request):
        form = GenerateBackgroundForm(request.POST)
        if form.is_valid():
            data = form.save(commit=False)
            data.image = gen(data.prompt, data.neg_prompt, data.style, 1088, 576)
            data.save()
            cache.set('background', data.id)
            cache.set('blur', data.transparency)
            return redirect('text')


class EnterText(View):
    def get(self, request):
        form = TextForm(request.POST)
        background = Background.objects.get(id=cache.get('background')).image
        # для отображения с логотипом - а надо ли???
        # background = mask(Logo.objects.get(id=cache.get('logo')).image, Background.objects.get(id=cache.get('background')).image, cache.get('blur'))
        context = {'form_text': form,
                   'back': background}
        return render(request, "text.html", context)

    def post(self, request):
        form = TextForm(request.POST)
        if form.is_valid():
            data = form.save(commit=False)

            data.person = Person.objects.get(pk=request.user.id)
            data.logo = Logo.objects.get(id=cache.get('logo'))
            data.background = Background.objects.get(id=cache.get('background'))
            data.image = create(data.logo.image, data.background.image, data.name, data.description, data.phone, data.address, data.text, data.text_size, data.text_color)

            data.save()
            return redirect('main')


class PersonDetailView(View):
    def get(self, request, **kwargs):
        person = Person.objects.get(pk=kwargs['pk'])
        cards = Card.objects.filter(person=person)
        context = {
            "person": person,
            "cards": cards,
        }
        return render(request, 'detail.html', context=context)


class GenerateLogo(View):
    def get(self, request):
        form = GenerateLogoForm(request.POST)
        context = {'form': form, }
        return render(request, "logo.html", context)

    def post(self, request):
        form = GenerateLogoForm(request.POST)
        if form.is_valid():
            data = form.save(commit=False)
            data.image = gen(data.prompt, data.neg_prompt, data.style, 256, 256)
            data.save()
            cache.set('logo', data.id)
            return redirect('gen_back' )


def instruction(request):
    return render(request, 'instruction.html')


class PersonDjangoLogin(LoginView):
    form_class = PersonLoginForm
    template_name = 'login.html'

    def get_success_url(self):
        return reverse_lazy('main')


def logout_person(request):
    logout(request)
    return redirect('login')