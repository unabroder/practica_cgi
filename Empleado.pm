package Empleado;
use strict;
#metodo constructor
sub new {
	#self hace referencia al objeto Empleado
	my $self = {};
	$self->{nombre} = 'Introduzaca un nombre';
	$self->{apellidos} = 'Introduzaca los apellidos';
	$self->{domicilio} = 'Introduzaca el domicilio';
	$self->{email} = 'Introduzaca el email';
	$self->{telefono} = 'Introduzaca un telefono';
	#se crea el objeto Empleado
	bless $self, 'Empleado';
	return $self;
}
#metodos set
sub setNombre{
	my($self, $nombre) = @_;
	$self->{nombre} = $nombre if defined($nombre);
	return $self->{nombre};
}
sub setApellidos{
	my($self, $apellidos) = @_;
	$self->{apellidos} = $apellidos if defined($apellidos);
	return $self->{apellidos};
}
sub setDomicilio{
	my($self,$domicilio) = @_;
	$self->{domicilio} = $domicilio if defined($domicilio);
	return $self->{domicilio};
}
sub setEmail{
	my($self,$email) = @_;
	$self->{email} = $email if defined($email);
	return $self->{email};
}
sub setTelefono{
	my($self,$telefono) = @_;
	$self->{telefono} = $telefono if defined($telefono);
	return $self->{telefono};
}
1;