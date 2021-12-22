#!/bin/perl
use strict;
#la estructura if es una estructura que permite establecer condiciones
my ($parametro) = ($ARGV[0]);
print "Ingrese el primer numero: ";
my $n1 = <STDIN>;
print "Ingrese el segundo numero: ";
my $n2 = <STDIN>;
chomp($n1); chomp($n2);
my $total;
if($parametro eq 'sumar'){
	$total = $n1 + $n2;
	print "El total de $n1 mas $n2 es igual a $total \n";
}elsif($parametro eq 'restar'){
	$total = $n1 - $n2;
	print "El total de $n1 menos $n2 es igual a $total \n";
}elsif($parametro eq 'producto'){
	$total = $n1 * $n2;
	print "El total de $n1 por $n2 es igual a $total \n";
}elsif($parametro eq 'dividir'){
	$total = $n1 / $n2;
	print "El total de $n1 entre $n2 es igual a $total \n";
}else{
	print "Escribar sumar, restar, producto o dividir \n";
}
