"""ticket_platform URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.urls import path

from .views import event_list_view, event_detail_view, reserve_ticket_for_event, basket_view, \
    release_ticket_from_basket, stats, buy_tickets

urlpatterns = [
    path('', event_list_view, name='main'),
    path('stats', stats, name='stats'),
    path('basket', basket_view, name='basket_view'),
    path('basket/buy', buy_tickets, name='buy_tickets'),
    path('basket/release/<event_id>/<category>', release_ticket_from_basket, name='release_ticket'),
    path('<event_id>', event_detail_view, name='event_detail'),
    path('<event_id>/reserve/<category>', reserve_ticket_for_event, name='reserve_ticket'),
]
