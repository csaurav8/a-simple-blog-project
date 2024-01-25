from .models import Category, SocialLinks

def get_categories(request):
    categories = Category.objects.all()
    return dict(categories = categories)
    
def get_links(request):
    social_links = SocialLinks.objects.all()
    return dict(social_links = social_links)