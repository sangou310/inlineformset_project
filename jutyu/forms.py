from django import forms

from .models import JutyuHead, JutyuDetail


class JutyuCreateForm(forms.ModelForm):
    class Meta:
        model = JutyuHead
        fields = ['jutyu_date', 'customer']


JutyuDetailFormset = forms.inlineformset_factory(
    JutyuHead, JutyuDetail,
    fields=['part', 'quantity'],
    extra=1,
)
