from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.urls import reverse, reverse_lazy
from django.views import generic
from .forms import MakerForm, LabelForm

from .models import Maker, Label

from leeblog.plus import *

from .forms import IngredientFormSet, InstructionFormSet, RecipeForm
from .models import Recipe


class RecipeCreateView(generic.edit.CreateView):
    template_name = 'leeblog/testfolder/recipe_add.html'
    model = Recipe
    form_class = RecipeForm
    success_url = 'success/'

    def get(self, request, *args, **kwargs):
        """
        Handles GET requests and instantiates blank versions of the form
        and its inline formsets.
        """
        self.object = None
        form_class = self.get_form_class()
        form = self.get_form(form_class)
        ingredient_form = IngredientFormSet()
        instruction_form = InstructionFormSet()
        return self.render_to_response(
            self.get_context_data(form=form,
                                  ingredient_form=ingredient_form,
                                  instruction_form=instruction_form))

    def post(self, request, *args, **kwargs):
        """
        Handles POST requests, instantiating a form instance and its inline
        formsets with the passed POST variables and then checking them for
        validity.
        """
        self.object = None
        form_class = self.get_form_class()
        form = self.get_form(form_class)
        ingredient_form = IngredientFormSet(self.request.POST)
        instruction_form = InstructionFormSet(self.request.POST)
        if (form.is_valid() and ingredient_form.is_valid() and
            instruction_form.is_valid()):
            return self.form_valid(form, ingredient_form, instruction_form)
        else:
            return self.form_invalid(form, ingredient_form, instruction_form)

    def form_valid(self, form, ingredient_form, instruction_form):
        """
        Called if all forms are valid. Creates a Recipe instance along with
        associated Ingredients and Instructions and then redirects to a
        success page.
        """
        self.object = form.save()
        ingredient_form.instance = self.object
        ingredient_form.save()
        instruction_form.instance = self.object
        instruction_form.save()
        return HttpResponseRedirect(self.get_success_url())

    def form_invalid(self, form, ingredient_form, instruction_form):
        """
        Called if a form is invalid. Re-renders the context data with the
        data-filled forms and errors.
        """
        return self.render_to_response(
            self.get_context_data(form=form,
                                  ingredient_form=ingredient_form,
                                  instruction_form=instruction_form))

















class MakerView(generic.ListView):
    form_class = MakerForm
    model = Maker
    template_name = 'leeblog/maker/index.html'
    context_object_name = 'makers'

class MakerCreateView(generic.edit.CreateView):
    model = Maker
    template_name = 'leeblog/maker/create.html'
    success_url = reverse_lazy('lee:maker_index')

    fields = '__all__'

class LabelView(generic.ListView):
    model = Label
    template_name = 'leeblog/label/index.html'
    context_object_name = 'labels'

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        # Add in a QuerySet of all the books
        makerid = self.kwargs.get('pk')
        context['maker'] = Maker.objects.get(id=makerid)
        context['labels'] = Label.objects.filter(maker=context['maker'])
        context['atest'] = add(1,2)
        return context

class LabelCreateView(generic.edit.CreateView):
    form_class = LabelForm
    model = Label
    template_name = 'leeblog/label/create.html'

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        # Add in a QuerySet of all the books
        makerid = self.kwargs.get('pk')
        context['maker'] = Maker.objects.get(id=makerid)
        return context

    def form_valid(self, form):
        makerid = self.kwargs.get('pk')
        label = form.save(commit=False)
        label.maker = Maker.objects.get(id=makerid)
        return super(LabelCreateView, self).form_valid(form)

    def get_success_url(self):
        makerid = self.kwargs.get('pk')
        return reverse_lazy('lee:label_index',
                                kwargs={'pk': makerid},
                                current_app='lee')

class LabelDetailView(generic.detail.DetailView):
    model = Label
    template_name = 'leeblog/label/detail.html'
    context_object_name = 'label'














posts = [
    {
        'author': 'Lee',
        'title': 'Blog Post 1',
        'content': 'First post content',
        'date_posted': 'August 27, 2018'
    },
    {
        'author': 'Han',
        'title': 'Blog Post 2',
        'content': 'Second post content',
        'date_posted': 'August 28, 2018'
    }
]

# Create your views here.
def index(request):
    return render(request, 'leeblog/index.html')

def home(request):
    context ={
        'posts': posts
    }
    return render(request, 'leeblog/home.html', context)

def about(request):
    return render(request, 'leeblog/about.html', {'title': 'About'})
