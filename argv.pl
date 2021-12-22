#!/bin/perl
use strict;
# $ARGV es un array especial de perl que nos va a permitir incluir parametros al script
my ($n1, $n2) = ($ARGV[0], $ARGV[1]);
my $total = $n1 + $n2;
print "El total de la suma de $n1 y $n2 es igual a $total \n";
