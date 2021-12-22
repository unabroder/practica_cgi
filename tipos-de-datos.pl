#!/bin/perl
use strict;
#string
my $string = "Hola soy un string";
print $string."\n";
$string = 'Con comillas simples '."\n";
print $string;
my $variable = "incluyo texto: $string \n";
print $variable;
#integer
my $entero = 230;
print $entero."\n";
my $decimal = 2.34;
print $decimal."\n";
my $octal = 033445566;
print $octal."\n";
my $hexa = 0xFF00FF11;
print $hexa."\n";