#!/bin/perl
#evitar caracteres raros
binmode(STDIN, ':encoding(cp850)');
binmode(STDOUT, ':encoding(cp850)');
use strict;
#ejemplo para solo un reemplazo
my $string = "hola " x 4;
$string =~ s/hola/adios/;
print $string."\n";
#reemplazar todas coincidencias
$string =~ s/hola/adios/g;
print $string."\n";
# para reemplazar todas las coincidencias ignorando mayusculas
# y minusculas
$string .= "HOLA "  x 2;
$string .= "hola " x 2;
print $string."\n";
$string =~ s/hola/adios/gi;
print $string."\n";
#ejemplo de reemplazos a traves de arrays
my @buscar = ('a'..'z');
my $j = 0;
my @reemplazar = (0..25);
foreach(@buscar){
	print $_.$j."/".$reemplazar[$j]."\n";
	$j++;
}

$string = "En este string se reemplazara las vocales por
			los numeros";
for(my $x = 0; $x < @buscar; $x++){
	my $buscarletra = $buscar[$x];
	my $_reemplazar = $reemplazar[$x];
	$string =~ s/$buscarletra/$_reemplazar/gi;
}
print $string."\n";