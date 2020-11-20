#!c:/Strawberry/perl/bin/perl.exe
use strict;
use CGI;
use POSIX qw(strftime);
my  $f = new CGI;
my %clases = ('end_div' => '</div>');
encabezado();
my $datestring = strftime "%A %d de %B  de %Y a las %I:%M %p ", localtime;
printf(uc "$datestring\n");
formulario();
reporte();
print $clases{"end_div"};
print $f->end_html();
sub encabezado{
	print $f->header('Content-Type: text/html;charset=iso-8859-1');
	print $f->start_html(
				-title => 'Formulario con CGI',
				-encoding => 'utf-8',
				-meta => {
					'description' => 'Formulario con CGI de perl',
					'keysworks' => 'formulario, prueba, CGI',
					'language' => 'spanish',
					'robots' => 'ALL'
				},
				-style   => [{'src'=>'https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css'}],
				-script =>  [{'src'=>'https://code.jquery.com/jquery-3.2.1.slim.min.js'},
							{'src'=>'https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.12.9/umd/popper.min.js'},
							{'src'=>'https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/js/bootstrap.min.js'}]
	);
	print $f->div({'class'=> 'container'});
}
sub formulario{
	print $f->h1({'class'=>'text-center text-info'},'Formulario para registro')."\n";
	print $f->start_form(-class => 'form', -method => 'post');
	#--------------------------------------------------------------
	print $f->div({'class' =>'form-group row'});
	print $f->label({'class' => 'col-sm-2 col-form-label'}, 'Nombres &nbsp;');
	print $f->div({'class' =>'col-sm-10'});
	print $f->input({'class'=> 'form-control', 'type'=>'text','name' => 'nombre',  'required'});
	print $clases{"end_div"}.$clases{"end_div"};
	#---------------------------------------------------------------------------
	print $f->div({'class' =>'form-group row'});
	print $f->label({'class' => 'col-sm-2 col-form-label'},'Apellidos ');
	print $f->div({'class' =>'col-sm-10'});
	print $f->input({'class'=> 'form-control','type'=>'text','name'=>'apellido','required'});
	print $clases{"end_div"}.$clases{"end_div"};
	#--------------------------------------------------------------------------------
	print $f->div({'class' =>'form-group row'});
	print $f->label({'class' => 'col-sm-2 col-form-label'},'Salario &nbsp');
	print $f->div({'class' =>'col-sm-10'});
	print $f->popup_menu( -class => 'form-control', -name => 'salario',
				-values =>  ['Seleccione un salario','minimo','medio','alto'],
				-default  =>  'Seleccione un salario',
				-labels => {'minimo' =>'300', 'medio' =>  '600',  'alto'  => '2000'}
			);
	print $clases{"end_div"}.$clases{"end_div"};
	#----------------------------------------------------------------------------------
	print $f->div({'class' =>'form-group row'});
	print $f->label({'class' => 'col-sm-2 col-form-label'},'Correo ');
	print $f->div({'class' =>'col-sm-10'});
	print $f->input({'class'=> 'form-control','type'=>'email','name'=>'correo','required'});
	print $clases{"end_div"}.$clases{"end_div"};
	#-------------------------------------------------------------------------------
	print $f->div({'class' =>'form-group row'});
	print $f->label({'class' => 'col-sm-2 col-form-label'},'Password ');
	print $f->div({'class' =>'col-sm-10'});
	print$f->password_field(-class => 'form-control', -name =>'pass', -value => 'default va', -size => 35, -maxlength =>  50);
	print $clases{"end_div"}.$clases{"end_div"};
	#---------------------------------------------------------------------------------
	#print $f->input({'class'=>'form-control', 'type'=>'submit', 'value'=>'Registrar'});
	print $f->submit(-class => 'btn btn-primary mt-3 text-center', -name => 'Registrar');
	print $f->end_form();
}

sub reporte{
	my $file = 'ejemplo.csv';
	open (F, $file) || die ("Could not open $file!");
	print $f->start_table({'class' => 'table table-responsive table-hover mt-2'});
	print $f->start_Tr({'class' => 'bg-primary text-white'});
	print $f->td(['Columna 1','Columna 2','Columna 3','Columna 4','Columna 5']);
	print $f->end_Tr();
	while (my $line = <F>){
		print $f->start_Tr({'class' => 'text-center'});
		(my $field1, my $field2, my $field3, my $field4, my $field5) = split ',', $line;
		print $f->td([$field1, $field2,  $field3,  $field4, $field5]);
		print $f->end_Tr();
	}
	print $f->end_table();
	close (F);
}

sub leer{
	#C:\Program Files (x86)/Apache24/cgi-bin\
	my $file = 'ejemplo.csv';
	open (F, $file) || die ("Could not open $file!");
	while (my $line = <F>){
	  (my $field1, my $field2, my $field3, my $field4) = split ',', $line;
	  print "$field1 : $field2 : $field3 : $field4";
	}
	close (F);
}
=begin comment
comentario extenso
--------------------------------
Los hashes grandes se recorren con el loop while 
y los pequeños con el loop foreach
--------------------------------
my %salario = ('minimo' => 45, 'medio' => 30, 'alto' => 40);
my @names = keys %salario; 
print "$names[0]\n";
print "$names[1]\n"; 
print "$names[2]\n";
	#utilizar cuado son hashes extensos
while ((my $key, my $value) = each (%salario)){
	# do whatever you want with $key and $value here ...
	$value = $salario{$key};
	print $f->div({'class', 'container-fluid'},"$key costs $value\n");
}
--------------------------------
=end comment
=cut
