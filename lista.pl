#!/bin/perl
use strict;
# lista es un conjunto de elementos indexados, hay que tener en cuente
# que el primer elemento de una lista le corresponde el index 0, incrementando
# su valor en 1 por ciente cada nuevo elemento que integre la lista
my @empleos = ('Fontanero','Programador','Camarero','Carpintero');
print $empleos[0]."\n";
#las listas multidimensionales es una lista en la cual entre sys elementos
# hay otras listas
my @empleados = (['Antonio', 24], ['Fernando',30, ['Calle Rosario',34]], ['Mario', 21]);
print "Nombre del empleado: ".$empleados[1][0]."\n";
print "Edad del empleado: ".$empleados[1][1]."\n";
print "Direccion del empleado: ".$empleados[1][2][0]."\n";