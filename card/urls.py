from django.conf import settings
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.urls import path, re_path, include
from . import views
from .views import *


urlpatterns = [
    #re_path(r'edit', Edit.as_view()),
    re_path(r'^person/registration', RegisterView.as_view()),
    re_path(r'^$', Indexing.as_view(), name='main'),

    re_path(r'^text/', EnterText.as_view(), name='text'),
    re_path(r'^logo/', GenerateLogo.as_view(), name='gen_logo'),
    re_path(r'^background/', GenerateBackground.as_view(), name='gen_back'),
    re_path(r'^instruction', views.instruction),


    re_path(r'^login/', views.PersonDjangoLogin.as_view(), name='login'),
    re_path(r'^logout/', logout_person, name='logout'),
    path('person/detail/<int:pk>', PersonDetailView.as_view(), name='person_detail'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)