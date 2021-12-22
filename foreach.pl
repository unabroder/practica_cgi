#!/bin/perl
use strict;
my @nombres = ('mario','manuel','fernando','alberto');
foreach(@nombres){
	# $_ que obtiene el elemento principal del array
	#print $_."\n";
}
foreach my $e (@nombres){
	print $e."\n";
}
my %asociativa = (
					2 => 'dos',
					1 => 'uno',
					3 => 'tres'
				);
foreach(keys %asociativa){
	print "Clave $_ /// valor ".$asociativa{$_}."\n";
}