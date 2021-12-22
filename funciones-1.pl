#!/bin/perl
use strict;
# funciones son parte de codigo reservadas para realizar una tarea en concreto
# es decir, una funcion es un nombre con serie de instrucciones que 
# posteriormente pueden ser llamados en una o varias partes del script,
# las funciones permiten simplificar, ordenatr, y disminuir el numero
# de lineas de codigo necesarias para realizar determinadas tareas que
# pueden ser repetitivas
# las funciones se declaran a traves de la palabra serevada "sub".
sub mensaje{ return "Hola mundo \n"; } 
print mensaje(); 
sub saluda{ 
	my ($saludo) = @_;
	return $saludo;
}
print saluda("Te estoy saludando \n");
sub sumar{
	my ($n1, $n2) = @_;
	return $n1 + $n2;
}
print sumar(1,2)."\n";