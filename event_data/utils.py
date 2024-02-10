from django.utils.text import slugify

import uuid

def generate_slug(title:str) -> str:
    from .models import Event
    title = slugify(title)

    while(Event.objects.filter(slug = title).exists()):
        title = f'{slugify(title)}-{str(uuid.uuid4())[:4]}'

    return title

def generate_slug_comapny(title:str) -> str:
    from .models import Company
    title = slugify(title)

    while(Company.objects.filter(slug = title).exists()):
        title = f'{slugify(title)}-{str(uuid.uuid4())[:4]}'

    return title

def generate_slug_workhand(title:str) -> str:
    from .models import Workhand
    title = slugify(title)

    while(Workhand.objects.filter(slug = title).exists()):
        title = f'{slugify(title)}-{str(uuid.uuid4())[:4]}'

    return title
