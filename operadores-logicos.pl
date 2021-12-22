#!/bin/perl
use strict;
#operadores logicos sirven para evaluar condiciones
#tipos de operadores logicos
# && : AND evaluara si las dos condiciones son ciertas
# || : OR evaluara si al menos una de las dos condiciones son ciertas
# ! : NOT evaluara si la condicion no es cierta
my ($n1,$n2,$n3,$n4) = (2,2,4,4);
if($n1 == $n2 && $n3 == $n4){
	print "Verdadero \n";
}else{
	print "Falso \n";
}