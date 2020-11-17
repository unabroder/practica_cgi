#!c:/Strawberry/perl/bin/perl.exe
use strict;
use CGI;
my $cgi = new CGI;
my $n1 = $cgi->param('n1');
my $n2 = $cgi->param('n2');
my $total = $n1 + $n2;
if($n1 !~  /^[0-9] + $/ or $n2  !~  /^[0-9] + $/){
	print $cgi->header('text/html');
	print 'solo se aceptan numeros';
	return;#envio error al testearlo
}else{
	print $cgi->header("text/html");
	print "El total es: ".$total;
}