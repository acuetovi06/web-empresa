from django.shortcuts import render, redirect
from django.urls import reverse
from django.core.mail import EmailMessage
from .forms import ContactForm
import logging

# Configuración del logger
logger = logging.getLogger(__name__)

# Create your views here.
    
def contact(request): 
    contact_form = ContactForm()
    
    if request.method == 'POST':
        contact_form = ContactForm(data=request.POST)
        if contact_form.is_valid():
            # Process the data in form.cleaned_data
            # For example, send an email or save to the database
            
            # name = request.POST.get('name', '')
            # email = request.POST.get('email', '')
            # content = request.POST.get('content', '')
            name = contact_form.cleaned_data['name']
            email = contact_form.cleaned_data['email']  
            content = contact_form.cleaned_data['content']
            
            # Enviamos el correo y redireccionamos
            email_msg = EmailMessage(
                # Formato:
                # Asunto, mensaje, de, para, reply_to
                "La Caffettiera: Nuevo mensaje de contacto",
                "De {} <{}>\n\nEscribió:\n\n{}".format(name, email, content),
                "no-contestar@inbox.mailtrap.io",
                ["acuetovi@yahoo.com"],
                reply_to=[email]
            )
            try:
                email_msg.send()
                return redirect(reverse('contact') + "?ok")
            except Exception as e:
                # Si no se pudo enviar el correo, redireccionamos a la misma página
                logger.error(f"Error sending email: {e}")
                print (f"Error sending email: {e}")
                return redirect(reverse('contact') + "?fail")
    

    return render(request, 'contact/contact.html', {'form': contact_form})   