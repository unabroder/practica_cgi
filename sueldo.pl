#!/bin/perl
use strict;
use Sueldo;
my $sueldo = new Sueldo();
print "El nombre del empleado es: ".$sueldo->setNombre('Roberto')."\n";
$sueldo->{dias_trabajados} = 18;
$sueldo->{sueldo_diario} = 13;
my $total = $sueldo->sueldo();
print "El salario del empleado es: ".$total."\n";