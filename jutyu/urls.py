from django.urls import path

from .views import JutyuListView

urlpatterns = [
    path('', JutyuListView.as_view(), name='jutyu_list'),
]
