# Your code here!
use strict;
use CGI;
my $cgi = new CGI;
print $cgi->header('text/html');
print $cgi->start_html(
-head => (
	$cgi->Link({'rel' => 'shortcut icon ', 'href' =>  '../img/icon-ico'}),
	-title => 'Hola Mundo',
	-encoding => 'UTF-8',
	-meta => {
		'description' => 'Esta es la descripcion',
		'keyswords' => 'Estas, son, las, palabras, clave',
		'language'  => 'spanish',
		'robots'       => 'ALL'
		},
	-style => [{'src' => '../css(styñe-1.css'}, {'src' => '../css(styñe-2.css'}],
	-script => [{'src' => '../js/script_1.js'},{'src' => '../js/script_1.js'}]
	)
);
print $cgi->h1({'class' => 'titulos', 'id' => 'titulos'}, 'Hola Mundo')."\n";
print $cgi->p({'class' => 'parrafos', 'id' => 'parrafos'}, 'Hola soy un parrafo')."\n";
print $cgi->br()  ."\m";
print $cgi->br()  ."\m";
print $cgi->strong('A comtinuacion vamos a crear una lista');
print $cgi->ul({'id' => 'lista'}, ['uno', 'dos', 'tres', 'cuatro'])."\n";
print $cgi->table({'id' => 'tabla',  'cellpadding' => '10', 'border' => '1' },
	$cgi->Tr([
		$cgi->th(['Nombre', 'Email', 'Edad']),
		$cgi->td(['Pepito',  'pepito@gmail.com', '15']),
		$cgi->td(['Bartolo',  'bartolo@gmail.com', '10']),
		])
	);
print $cgi->img({
	'src' => '../img/img1.png',
	'width' => '150',
	'heigth' => '100'
	});
print $cgi->end_html();