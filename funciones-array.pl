#!/bin/perl
use strict;
#evitar caracteres extranios en windows
binmode(STDOUT, ":encoding(cp850)");
binmode(STDIN, ":encoding(cp850)");
# scalar devuelve el numero total de elementos de un array
my @lista = (0..5);
print scalar(@lista);
#join convierte un array en un string mediante el separador indicado
my $string = join('-',@lista);
print $string;
# split divide un string para convertirlo en un array a partir del patron indicado
my @numeros = split('-',$string);
foreach(@numeros){
	print $_."\n";
}
# shift: elimina el primer elemento de un array
my @nombres = ('raul','Antonio','pepe');
shift(@nombres);
foreach(@nombres){
	print $_."\n";
}
#unshift permite agregar nuevos elementos al principio de un array
#igual puede agregar un solo elemento o un array dentro de la lista
unshift(@nombres, 'Mario');
foreach my $x (@nombres) {
	print $x."\n";
}
#pop: elimina el ultimo elemento de un array
my @paises = ('Argentina','Peru','Colombia','Venezuela');
pop(@paises);
foreach(@paises){
	print $_."\n";
}
#push: permite agregar nuevos elementos al final del array
my @frutas = ('apple','banana');
push(@frutas, 'Watermelon');
foreach(@frutas){
	print $_."\n";
}