from .models import Link

def ctx_dict(request):
    # Esta función crea un diccionario de contexto para las plantillas, extendiendo el contexto global
    # Esto debe permitir utilizar la variable 'text' como una variable en cualquier template.
    # Para ello se debe agregar en la aplicación principal a context_processors en settings.py
    ctx = {}
    links = Link.objects.all()
    for link in links:
        ctx[link.key] = link.url
    return ctx