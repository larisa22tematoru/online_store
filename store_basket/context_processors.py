from store_basket.basket import Basket


def basket(request):
    return {'basket': Basket(request)}

# A context processor is a Python function that takes the request object as an argument
# and returns a dictionary that gets added to the request context.
# They come in handy when you need to make something available globally to all templates.
# By default, when you create a new project using the startproject command,
# your project contains the following template context processors,
# in the context_processors option inside the TEMPLATES setting
