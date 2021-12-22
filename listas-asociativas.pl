#!/bin/perl
use strict;
#las listas asociativas son aquellas listas en la que sus elementos
# estan asociados a traves de una clave-valor
my %imagen = ('width' => 200, 'heigh' => 60, 'color_fondo' => 'azul');
print "Anchura de la imagen: ".$imagen{'width'}."\n";
print "Altura de la imagen: ".$imagen{'heigh'}."\n";
print "Color de fondo: ".$imagen{'color_fondo'}."\n";