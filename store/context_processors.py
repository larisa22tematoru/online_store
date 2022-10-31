from .models import Category


def categories(request):
    return {"categories": Category.objects.filter(level=0)}


# from .models import Category
#
# def categories(request):
#     return {
#         'categories': Category.objects.all()
#     }

# “A context processor has a simple interface: it’s a Python function that takes one argument,
# an HttpRequest object, and returns a dictionary that gets added to the template context.
# Each context processor must return a dictionary.
