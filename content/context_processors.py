from .models import MenuItem


def menu(request):
    return {"menu_items": MenuItem.objects.all()}
