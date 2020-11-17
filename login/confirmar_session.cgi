#!c:/Strawberry/perl/bin/perl.exe
use strict;
use CGI;
use CGI::Session;
use CGI::Carp qw(fatalsToBrowser);
use DBI;
my $cgi = new CGI;
my $user = $cgi->param("user", $cgi->param('user'));
my $pass = $cgi->param("pass", $cgi->param('pass'));
#filtrar datos
if ($user !~ /^[a-zA-Z] + $/ or $pass !~ /^[a-zA-Z0-9] + $/){
	print $cgi->header("text/html");
	print "<meta http-equiv='refresh' content='3; ../login.html>'";
	print "<h3 style='color: red;'>Los tipo de datos no son correctos<h3>";
}else{
	my $root = "root";
	my $pass = "bandera1933mdg";
	my $host = "localhost";
	my $db = "tutorial_cgi";
	my $mysql = DBI->connect("DBI:mysql:$db;host=$host",$root, $pass);
#preparar la consulta
	my $consulta = $mysql->prepare("SELECT * FROM login WHERE usuario ='$user' AND pass='$pass')";	
	$consulta->execute();
	my $encontrar = 0;
	while($consulta->fetch()){
		$encontrar = 1;
		}
	if($encontrar eq 1){
		my $sesion = new CGI::Session;
		$sesion->save_param($cgi);
		$sesion->expires("+1h");
		$sesion->flush();
		$sesion->header(-location => "privado-cgi");
	}else{
		print $cgi->header("text/html");
		print "meta http-equiv='refresh' content='3; ../login.html>"; 
		print "<h3 style='color: red;'>Los datos son incorrectos</h3>";
	}
	$consulta->disconnect();
}
