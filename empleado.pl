#!/bin/perl
use strict;
use Empleado;
my $empleado = new Empleado();
# my $empleado = Empleado::new();
print "El nombre del empleado es: ".$empleado->setNombre("Roberto")."\n";