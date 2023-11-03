from uuid import uuid4
from pytils.translit import slugify


def unique_slugify(instance, slug):
    """
    Generates unique slug fields for models.
    """
    model = instance.__class__
    unique_slug = slugify(slug)
    while model.objects.filter(slug=unique_slug).exists():
        unique_slug = f'{unique_slug}-{uuid4().hex[:4]}'
    return unique_slug
