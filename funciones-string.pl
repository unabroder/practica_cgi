#!/bin/perl
use strict;
# binmode: permite indicar la codificacion correcta para la entrada
# y la salida de datos esta funcion permite indicar la codificacion 
# cp850 de la consola de windows para evitar que aparezcan 
# caracteres raros.
binmode(STDOUT, ":encoding(cp850)");
my $string = "La codicion";
# chop: elimina el ultimo caracter de un string
# uc convierte el string a mayusculas
# ucfirst convirte la primera letra en mayuscula
# lc: convierte el string en minusculas
# length: regresa la lingitud total del string
# substr: regresa el substring a traves de las coordenadas inicio, final
# si es negativo la extraccion se realiza a la derecha a izquierda
# index: devuelve la posicion de la primera ocurrencia del substring la
# posicion inicial es 0 asi el substring no es encontrado devuelve -1
