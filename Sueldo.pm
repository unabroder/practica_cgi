package Sueldo;
use Empleado;
#arreglo ISA para crear la herencia
@ISA = qw(Empleado);
use strict;
sub new {
	my $self = new Empleado();
	$self->{dias_trabajados} = 0;
	$self->{sueldo_diario} = 0;
	bless $self, 'Sueldo';
	return $self;
}
sub sueldo{
	my($self) = @_;
	return $self->{dias_trabajados} * $self->{sueldo_diario};
}
1;