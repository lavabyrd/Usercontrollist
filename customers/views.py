from django.views.generic import TemplateView, View

class CustomerView(TemplateView, View):
    template_name = 'customers/customers.html'

    def get(self, request, *args, **kwargs):
        return self.render_to_response({})
