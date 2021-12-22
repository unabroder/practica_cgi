#!/bin/perl
use strict;
#mediante <STDIN> se puede realizar una entrada de datos a traves
# del teclado y utilizar esos datos para jecutar acciones en el programa
print "Ingrese el primer numero: ";
my $n1 = <STDIN>;
print "Ingrese el segundo numero: ";
my $n2 = <STDIN>;
my $total = $n1 + $n2;
#la funcion chomp() elimina el salto de linea
chomp($n1);
chomp($n2);
print "El total de la suma de $n1 y $n2 es igual a $total";