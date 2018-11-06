from django.shortcuts import render,redirect
from .forms import ContactForm
from django.core.mail import EmailMessage
from django.urls import reverse

# Create your views here.
def contact(request):
	# print("Tipo de peticion: {}".format(request.method))
	contact_form = ContactForm()

	if request.method == 'POST':
		contact_form = ContactForm(data=request.POST)
		if contact_form.is_valid():
			name = request.POST.get('name','')
			email = request.POST.get('email','')
			content = request.POST.get('content','')
			print ("este es el email" + email)
			# suponer que todo fue bien
			# enviamos el correo
			# email = EmailMessage(
			# 	asunto,
			# 	cuerpo,
			# 	emailorigen,
			# 	emaildestino,
			# 	repply_to=[email]

			# )
			email = EmailMessage(
				"La Cafetierra - nuevo mensaje de contacto",
				"De {} <{}>\n\nEscribio\n\n{}".format(name,email,content),
				"no-contestar@inbox.mailtrap.io",
				['renesoriapabon@gmail.com'],
				reply_to=[email]
			)
			try:
				email.send()
				return redirect(reverse('contact') + "?ok")
			except:
				return redirect(reverse('contact') + "?fail")

	return render(request, 'contact/contact.html',{'form': contact_form})
