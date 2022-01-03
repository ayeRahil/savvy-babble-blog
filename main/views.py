from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.views.generic.base import View
from .models import Post, Category, Profile
from django.views.generic.detail import SingleObjectMixin
from django.views.generic import FormView
from django.urls import reverse
from .forms import PostForm, UpdateForm, CommentForm
from django.urls import reverse_lazy
from django.views.decorators.csrf import requires_csrf_token



# Create your views here.

class HomeView(ListView):
    
    model = Post
    template_name = 'main/index.html'
    context_object_name = 'article'
    

    def get_queryset(self):
        queryset = {'all_articles': Post.objects.all().order_by('-created_on'), 
                    'latest_10_articles': Post.objects.all().order_by('-created_on')[:10],
                    }
        return queryset


    



#'filter_author': Post.objects.filter(author = "self.author.user")
class AuthorView(ListView):
    model = Profile
    template_name = 'main/author.html'
    

    def get_queryset(self):
        return Post.objects.filter(author = self.request.user).order_by('created_on').reverse()


    def get_context_data(self,**kwargs):
        context = super(AuthorView, self).get_context_data(**kwargs)
        context['authorpost_list'] = Post.objects.filter(author = self.request.user).order_by('-created_on')
        return context

class ArticleDetailView(DetailView):
    model = Post
    template_name = 'main/article_details.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = CommentForm()
        return context

@requires_csrf_token
class PostComment(SingleObjectMixin, FormView):
    model = Post
    form_class = CommentForm
    template_name = 'main/article_details.html'

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        return super().post(request, *args, **kwargs)

    def get_form_kwargs(self):
        kwargs = super(PostComment, self).get_form_kwargs()
        kwargs['request'] = self.request
        return kwargs

    def form_valid(self, form):
        comment = form.save(commit=False)
        comment.post = self.object
        comment.save()
        return super().form_valid(form)

    def get_success_url(self):
        post = self.get_object()
        return reverse('article-detail', kwargs={'pk': post.pk}) + '#comments'
    

class PostDetailView(View):

    def get(self, request, *args, **kwargs):
        view = ArticleDetailView.as_view()
        return view(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        view = PostComment.as_view()
        return view(request, *args, **kwargs)


@requires_csrf_token
class CreateArticleView(CreateView):
    model = Post
    form_class = PostForm
    template_name = 'main/create_article.html'
    #fields = '__all__'


class CreateCategoryView(CreateView):
    model = Category
    #form_class = PostForm
    template_name = 'main/create_category.html'
    fields = '__all__'

def CategoryView(request, cats):
    category_post = Post.objects.filter(category = cats.replace('-', ' '))
    return render(request, 'main/categories.html', {'cats':cats.title().replace('-', ' '),'category_post':category_post})


@requires_csrf_token
class UpdateArticleView(UpdateView):
    model = Post
    form_class = UpdateForm
    template_name = 'main/update_article.html'
    #fields = ['title', 'title_tag', 'body']


class DeleteArticleView(DeleteView):
    model = Post
    template_name = 'main/delete_article.html'
    success_url = reverse_lazy('home')




        