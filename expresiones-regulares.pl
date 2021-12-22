#!/bin/perl
use strict;
#expresiones regulares
#url(https://jquery-manuales.blogspot.com.es/2013/09/expresiones-regulares-con-pregmatch.html)
# =~ Si el patron es encontrado
# !~ si el patron no es encontrado
my $email = 'email@email';
if($email !~ /^[a-zA-Z0-9\._-]+@[a-zA-Z0-9]{2,}[.][a-zA-Z]{2,4}$/){
	print "Error el formato del email es incorrecto \n";
}else{
	print "El formato del email es correcto \n";
}
