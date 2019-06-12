from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from . import models
from django.views.generic import View, TemplateView, ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy, reverse
from .forms import TelefonForm, EmailForm
from django.shortcuts import get_list_or_404, get_object_or_404
from django.db.models import Q



class IndexView(TemplateView):
    template_name = 'phone_book_app/index.html'


class OsobaListView(ListView):
    context_object_name = 'people'
    model = models.Osoba
    template_name = 'phone_book_app/index.html'
    ordering = ['nazwisko']


class OsobaDetailView(DetailView):
    context_object_name = 'people_detail'
    model = models.Osoba
    template_name = 'phone_book_app/contact_detail.html'


class OsobaCreateView(CreateView):
    fields = ('imie', 'nazwisko')
    model = models.Osoba
    template_name = 'phone_book_app/osoba_form.html'


class OsobaUpdateView(UpdateView):
    fields = ('imie','nazwisko')
    model = models.Osoba

class OsobaDeletelView(DeleteView):
    model = models.Osoba
    success_url = reverse_lazy("list")


class TelefonFormView(CreateView):
    template_name = 'phone_book_app/telefon_form.html'

    def get(self, request,  pk):
        form = TelefonForm()
        telefon = models.Telefon.objects.all()

        args = {
            'form': form, 'telefony': telefon
        }
        return render(request, self.template_name, args)

    def post(self, request, pk):
        osoba =  get_object_or_404(models.Osoba, pk=pk)
        form = TelefonForm(data=request.POST)
        if form.is_valid():
            telefon = form.save(commit=False)
            telefon.osoba = osoba
            telefon.save()
            return redirect('detail', pk=osoba.pk)

        else:
            return render(request, 'index.html', {'form': form})

        args = {'form': form}
        return render(request, self.template_name, args)



class EmailFormView(CreateView):
    template_name = 'phone_book_app/email_form.html'

    def get(self, request,  pk):
        form = EmailForm()
        email = models.Email.objects.all()

        args = {
            'form': form, 'emaile': email
        }
        return render(request, self.template_name, args)

    def post(self, request, pk):
        osoba =  get_object_or_404(models.Osoba, pk=pk)
        form = EmailForm(data=request.POST)
        if form.is_valid():
            email = form.save(commit=False)
            email.osoba = osoba
            email.save()
            return redirect('detail', pk=osoba.pk)

        else:
            return render(request, 'index.html', {'form': form})

        args = {'form': form}
        return render(request, self.template_name, args)



class SearchView(ListView):
    template_name = 'phone_book_app/search.html'
    paginate_by = 20

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['query'] = self.request.GET.get('q')
        return context
    def get_queryset(self):
        tele = []
        e_mail =[]
        request = self.request
        query = request.GET.get('q', None)
        if query is not None:
            imie_results =  models.Osoba.objects.filter(Q(imie__icontains=query))
            nazwisko_results =  models.Osoba.objects.filter(Q(nazwisko__icontains=query))
            telefon_results = models.Telefon.objects.filter(Q(telefon__icontains=query))
            email_results = models.Email.objects.filter(Q(email__icontains=query))

            if telefon_results:
                for i in range(len(telefon_results)-1):
                    tel = telefon_results[i].telefon
                    tele.append(get_object_or_404(models.Osoba, id=models.Telefon.objects.get(telefon=tel).osoba.id))
                return tel
            if email_results:
                for i in range(len(email_results)):
                    mail = email_results[i].email
                    e_mail.append(get_object_or_404(models.Osoba, id=models.Email.objects.get(email=mail).osoba.id))
                return e_mail
            qs = imie_results or nazwisko_results or tele or e_mail

            return qs
        return models.Osoba.objects.all()
