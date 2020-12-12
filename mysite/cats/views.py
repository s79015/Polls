from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

from .models import Cat, Breed
from .forms import CatForm, BreedForm

# Create your views here.


class CatList(LoginRequiredMixin, View):
    def get(self, request):
        cat_count = Cat.objects.all().count()
        cat = Cat.objects.all()
        breed_count = Breed.objects.all().count()
        breed = Breed.objects.all()
        ctx = { 'cat_count': cat_count, 
                'cat_list': cat,
                'breed_count': breed_count,
                'breed_list': breed}
        return render(request, 'cats/cat_list.html', ctx)

class CatCreate(LoginRequiredMixin, View):
    template = 'cats/cat_form.html'
    success_url = reverse_lazy('cats:all')

    def get(self, request):
        form = CatForm()
        ctx = {'form': form}
        return render(request, self.template, ctx)

    def post(self, request):
        form = CatForm(request.POST)
        if not form.is_valid():
            ctx = {'form': form}
            return render(request, self.template, ctx)

        make = form.save()
        return redirect(self.success_url)


# MakeUpdate has code to implement the get/post/validate/store flow
# AutoUpdate (below) is doing the same thing with no code
# and no form by extending UpdateView
class CatUpdate(LoginRequiredMixin, View):
    model = Cat
    success_url = reverse_lazy('cats:all')
    template = 'cats/cat_form.html'

    def get(self, request, pk):
        make = get_object_or_404(self.model, pk=pk)
        form = CatForm(instance=make)
        ctx = {'form': form}
        return render(request, self.template, ctx)

    def post(self, request, pk):
        make = get_object_or_404(self.model, pk=pk)
        form = CatForm(request.POST, instance=make)
        if not form.is_valid():
            ctx = {'form': form}
            return render(request, self.template, ctx)

        form.save()
        return redirect(self.success_url)

class CatDelete(LoginRequiredMixin, DeleteView):
    model = Cat
    fields = '__all__'
    success_url = reverse_lazy('cats:all')


        #Breed

class BreedView(LoginRequiredMixin, View):
    def get(self, request):
        ml = Breed.objects.all()
        ctx = {'breed_list': ml}
        return render(request, 'cats/breed_list.html', ctx)

class BreedCreate(LoginRequiredMixin, View):
    template = 'cats/cat_form.html'
    success_url = reverse_lazy('cats:all')

    def get(self, request):
        form = BreedForm()
        ctx = {'form': form}
        return render(request, self.template, ctx)

    def post(self, request):
        form = BreedForm(request.POST)
        if not form.is_valid():
            ctx = {'form': form}
            return render(request, self.template, ctx)

        make = form.save()
        return redirect(self.success_url)


# MakeUpdate has code to implement the get/post/validate/store flow
# AutoUpdate (below) is doing the same thing with no code
# and no form by extending UpdateView
class BreedUpdate(LoginRequiredMixin, View):
    model = Breed
    success_url = reverse_lazy('cats:all')
    template = 'cats/breed_form.html'

    def get(self, request, pk):
        make = get_object_or_404(self.model, pk=pk)
        form = BreedForm(instance=make)
        ctx = {'form': form}
        return render(request, self.template, ctx)

    def post(self, request, pk):
        make = get_object_or_404(self.model, pk=pk)
        form = BreedForm(request.POST, instance=make)
        if not form.is_valid():
            ctx = {'form': form}
            return render(request, self.template, ctx)

        form.save()
        return redirect(self.success_url)

class BreedDelete(LoginRequiredMixin, View):
    model = Breed
    success_url = reverse_lazy('cats:all')
    template = 'cats/breed_confirm_delete.html'

    def get(self, request, pk):
        make = get_object_or_404(self.model, pk=pk)
        form = BreedForm(instance=make)
        ctx = {'make': make}
        return render(request, self.template, ctx)

    def post(self, request, pk):
        make = get_object_or_404(self.model, pk=pk)
        make.delete()
        return redirect(self.success_url)