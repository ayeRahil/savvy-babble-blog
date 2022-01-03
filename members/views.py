from django.shortcuts import get_object_or_404, render
from django.views import generic
from django.views.generic import CreateView
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, PasswordChangeForm
from django.urls import reverse_lazy
from .forms import EditProfileForm, SignUpForm, ProfilePageForm
from django.contrib.auth.views import PasswordChangeView
from main.models import Profile
from django.views.decorators.csrf import requires_csrf_token

# Create your views here.

@requires_csrf_token
class UserRegisterView(generic.CreateView):
    form_class = SignUpForm
    template_name = 'registration/register.html'
    success_url = reverse_lazy('login')

@requires_csrf_token
class UserEditView(generic.UpdateView):
    #form_class = UserChangeForm
    form_class = EditProfileForm
    template_name = 'registration/edit_account.html'
    success_url = reverse_lazy('home')

    def get_object(self):
        return self.request.user


class PasswordsChangeView(PasswordChangeView):
    form_class = PasswordChangeForm
    success_url = reverse_lazy('home')

@requires_csrf_token
class EditProfileView(generic.UpdateView):
    model = Profile
    template_name = 'registration/edit_profile.html'
    fields = ['bio', 'authorImage', 'instagram_url', 'linkedin_url', 'github_url', 'twitter_url', 'facebook_url', 'mail_id']
    success_url = reverse_lazy('home')
    """ def get_object(self):
        return self.request.user """
    """ def get_context_data(self, *args, **kwargs):
        context = super(EditProfileView, self).get_context_data(*args, **kwargs)
        page_user = get_object_or_404(Profile, id =self.kwargs['pk'])
        context['page_user'] = page_user
        return context """

@requires_csrf_token
class CreateProfileView(CreateView):
    model = Profile
    form_class = ProfilePageForm
    #fields = '__all__'
    template_name = 'registration/create_profile.html'

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


