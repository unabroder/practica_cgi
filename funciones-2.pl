#!/bin/perl
use strict;
sub multiplicar{
	my ($n, $op) = @_;
	if(!defined($op)){
		$op = 5;
	}
	return $n * $op;
}
print multiplicar(5,0)."\n";
sub imagen{
	my(%opciones) = @_;
	my %default = (
			'width' => 250,
			'heigh' => 250,
			'color' => 'negro'
		);
	foreach(keys %default){
		if($opciones{$_} eq undef){
			$opciones{$_} = $default{$_}; 
		}
	}
	my $rs = "La anchura de la imagen es: ".$opciones{'width'}."\n";
	 $rs .= "La altura de la imagen es: ".$opciones{'heigh'}."\n";
	 $rs .= "El color de fondo de la imagen es: ".$opciones{'color'}."\n";
	 return $rs;
}
print imagen(('width' => 100));