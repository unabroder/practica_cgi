#!c:/Strawberry/perl/bin/perl.exe
use strict;
use CGI;
use CGI::Session;
use CGI::Carp qw(fatlasToBrowser);
use DBI;

#crear un objeto
my $cgi = new CGI;
#objeto session
my $session = new CGI::Session;
#cargar datos de sesion
$session->load();
my @auntenticar = $session->param;
if(@auntenticar eq 0){
	$session->delete();
	$session->flush();
	print $cgi->header("text/html");
	print "<meta http-equiv='refresh' content='3; ../login.html'>";
	print "<h3 style='color: red;'> Usted no tiene permisos para estar aqui, redireccionando ...";
}elsif($session->is_expired){
	$session->delete();
	$session->flush();
	print $cgi->header("text/html");
	print "<meta http-equiv='refresh' content='3; ../login.html'>";
	print "<h3 style='color: red;'> Su sesion a expirado, redireccionando ...";
}else{
	print $cgi->header("text/html");
	print "<h3>Bienvenido ".$session->param("user")." a su panel de administracion</h3>";
	print "<br> <br>";
	print "<a href='exit.cgi'>Salir de la aplicacion</a>";
}
