from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.views.generic import TemplateView

from core.forms import NumberInscriptionForm
from core.utils import NumberInscriptionBuilder


class InscriptionOutputView(TemplateView):
    template_name = 'inscription_output.html'

    def get(self, request, **kwargs):
        form = NumberInscriptionForm(kwargs)
        if not form.is_valid():
            return HttpResponseRedirect(reverse('main'))
        builder = NumberInscriptionBuilder(**kwargs)
        return render(request, self.template_name, {'inscription': builder.get_inscription()})
