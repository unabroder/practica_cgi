#!/bin/perl
binmode(STDOUT, ':encoding(cp850)');
binmode(STDIN, ':encoding(cp850)');
use strict;
#modos < read | > write | >> append
open (ARCHIVO, '>>', 'prueba.txt');
print "Agrega contenido al archivo de texto \n";
my $contenido = <STDIN>;
print ARCHIVO $contenido;
close(ARCHIVO);
open(ARCHIVO, '<', 'prueba.txt');
while(<ARCHIVO>){
	print $_;
}
close(ARCHIVO);