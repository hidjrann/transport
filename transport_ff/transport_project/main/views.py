from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import TemplateView, ListView, DetailView, CreateView, UpdateView, DeleteView

# Create your views here.
from main import models
from main import forms


class HomePageView(TemplateView):
    template_name = 'home.html'

class CarListView(ListView):
    model = models.Car
    template_name = 'car_list.html'

class CarDetailView(DetailView):
    model = models.Car
    template_name = 'main/car_detail.html'

class BookCreateView(CreateView):
    models = models.Booking
    template_name = 'main/book_new.html'
    form_class = forms.BookForm
    success_url = reverse_lazy('book_list')

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.customer_name = self.request.user
        return super(BookCreateView, self).form_valid(form)



class BookListView(ListView):
    model = models.Booking
    template_name = 'main/book_list.html'
    def get_queryset(self):
        return models.Booking.objects.filter(customer_name=self.request.user)
    

class BookDetailView(DetailView):
    model = models.Booking
    template_name = 'main/book_detail.html'

class BookUpdateView(UpdateView):
    model = models.Booking
    form_class = forms.BookForm
    template_name = 'main/book_edit.html'
    success_url = reverse_lazy('book_list')

class BookDeleteView(DeleteView):
    model = models.Booking
    template_name = 'main/book_delete.html'
    success_url = reverse_lazy('book_list')


class RideCreateView(CreateView):
    models = models.Ride
    template_name = 'main/ride_new.html'
    form_class = forms.RideForm
    success_url = reverse_lazy('ride_list')

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.customer_name = self.request.user
        return super(RideCreateView, self).form_valid(form)

class RideListView(ListView):
    model = models.Ride
    template_name = 'main/ride_list.html'


class RideDetailView(DetailView):
    model = models.Ride
    template_name = 'main/ride_detail.html'


class RideUpdateView(UpdateView):
    model = models.Ride
    form_class = forms.RideForm
    template_name = 'main/ride_edit.html'
    success_url = reverse_lazy('ride_list')

class RideDeleteView(DeleteView):
    model = models.Ride
    template_name = 'main/ride_delete.html'
    success_url = reverse_lazy('ride_list')