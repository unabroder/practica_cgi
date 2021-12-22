#!/bin/perl
use strict;
#operador de seleccion es un operador triario que permite hacer una cosa u otra
#dependiendo de la condicion dada se puede describir como el
# equivalente a una condicional simple con las sentencias if else
#estructura: condicion ? accion1 : accion2
my ($v1, $v2) = (2,4);
$v1 < $v2 ? print "OK \n" : print "ERROR \n";
