#!c:/Strawberry/perl/bin/perl.exe
use strict;
use CGI;
my $cgi = new CGI;
my $n1 = $cgi->param("n1");
my $n2 = $cgi->param("n2");
my $op = $cgi->param("oper");
my $total;
print $cgi->header("text/html");
encabezado();
if($op eq 'suma'){
	$total = $n1 + $n2;
}elsif($op eq 'div'){
	if($n2 eq 0){
		$total = $cgi->h1('No se puede realizar la division');
	}else{
		$total = sprintf("%.2f", $n1 / $n2);
	}
}elsif($op eq 'res'){
	$total = $n1 - $n2;
}elsif($op eq 'mul'){
	$total = $n1 * $n2;
}else{
	print $total = $cgi->h1('No se pudo realizar ninguna operacion');
}
if($n1 !~  /^[0-9]+$/ or $n2  !~  /^[0-9]+$/){
	print $cgi->div({'class'=> 'col bg-warning text-center text-secondary  p-2'});
	print $cgi->h1({'class'=> 'display-4'},'Solo se aceptan numeros');
	print $cgi->img({
		'src'=> 'https://assets.stickpng.com/images/5a81af7d9123fa7bcc9b0793.png',
		'class' => 'img-fluid rounder-circle',
		'width' => '100',
		'height' => '100'
		});
	fin_html();
	return;#envio error al testearlo
}else{
	print $cgi->div({'class'=> 'col bg-success text-center text-secondary p-2'});
	print $cgi->h1({'class'=> 'display-2'},'El resultado es: '.$total);
	print $cgi->img({
		'src'=> 'https://assets.stickpng.com/images/5aa78e387603fc558cffbf1d.png',
		'class' => 'img-fluid rounder-circle',
		'width' => '100',
		'height' => '100'
	});
	fin_html();
}
#{}>
sub encabezado{
	print $cgi->start_html(
			-title => 'Operaciones Aritmeticas',
			-encoding => 'iso-8859-1',
			-meta => {
				'description' => 'Operaciones Aritmeticas con CGI-PERL',
				'keyswords' => 'Estas, son, las, palabras, clave',
				'language'  => 'es',
				'robots'       => 'ALL'
			},
			-style => [{'src' => 'https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/css/bootstrap.min.css'}],
			-script => [{'src' => 'https://code.jquery.com/jquery-3.3.1.slim.min.js'},
						{'src' => 'https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.14.7/umd/popper.min.js'},
						{'src' => 'https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/js/bootstrap.min.js'}]
	);
}
sub fin_html{
	print $cgi->end_html();
}