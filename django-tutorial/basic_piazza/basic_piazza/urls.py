"""basic_piazza URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin

urlpatterns = [
    url(r'^$', views.home, name="homepage"), # Acceses the home page if the string is empty
    url(r'add', views.add_a_question,, name="addquestion") # Takes us to the add_a_question view
    url(r'[0-9]+', views.current_question, name="yourquestion") # Acceses the current question
    url(r'^admin/', admin.site.urls), # Access the admin page
]
