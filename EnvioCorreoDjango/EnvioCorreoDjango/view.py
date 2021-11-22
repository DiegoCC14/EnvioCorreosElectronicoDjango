from django.shortcuts import render, redirect
from django.http import HttpResponse , JsonResponse #Retornara datos JSON a la pagina
from django.core import serializers

from django.conf import settings

from django.template.loader import get_template
from django.core.mail import EmailMultiAlternatives

from pathlib import Path

def Envio_Correo( email_receptor ):
	context = {'email':'diego.xmen123@gmail.com'}
	templateCorreo = get_template("CorreoCuerpo.html")
	htmlRenderizado = templateCorreo.render( context )
	email = EmailMultiAlternatives(
		'Correo Prueba',
		"DiegoCazon",
		settings.EMAIL_HOST_USER,
		[email_receptor]
		#[cc] copia correos donde enviar
		)

	email.attach_alternative( htmlRenderizado , 'text/html' )
	email.send()

def EnvioCorreo(request):
	
	if request.method == 'POST': 
		
		Envio_Correo( 'diego.xmen123@gmail.com' )

	return render(request,'Inicio.html', {} )