from django.views.generic import ListView

from .models import JutyuHead, JutyuDetail


class JutyuListView(ListView):
    model = JutyuHead
    template_name = 'jutyu/jutyu_list.html'
