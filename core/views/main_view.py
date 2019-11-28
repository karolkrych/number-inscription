from django.http import HttpResponseRedirect
from django.urls import reverse_lazy, reverse
from django.views.generic import FormView

from core.forms import NumberInscriptionForm


class MainView(FormView):
    initial = {'number': '123456'}
    form_class = NumberInscriptionForm
    template_name = 'main.html'

    def get_success_url(self):
        return reverse('inscription-output', kwargs={'number': self.number})

    def form_valid(self, form):
        """If the form is valid, redirect to the supplied URL."""
        self.number = form.cleaned_data.get('number')
        return HttpResponseRedirect(self.get_success_url())
