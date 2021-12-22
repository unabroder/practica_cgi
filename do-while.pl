#!/bin/perl
use strict;
my @nombres = ('raul', 'dade','fernando', 'mario', 'pepe', 'manuel');
my $x = 0;
do{
	print $nombres[$x]."\n";
	$x++;
}while($x < @nombres);