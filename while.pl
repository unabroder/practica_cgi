#!/bin/perl
use strict; 
my @numeros = (0..9); 
my $x = 0;
while($x < @numeros){
	print $numeros[$x]."\n";
	$x++;
}
while($x >= 0){
	if($x == 5){
		#salir
		last;
	}
	print $numeros[$x]."\n";
	$x--;
}