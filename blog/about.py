from django.views.generic import TemplateView

class About(TemplateView):
    template_name = 'blog/about.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        data = {
        'username': 'SuperCoder99', 
        'age': 25, 
        'is_premium': True,
        'movies': ['movie1', 'movie2']
        }

        context.update(data)
        return context