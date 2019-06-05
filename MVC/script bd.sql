create database Emi;
use Emi;
create table usuario(
	patente varchar(7) primary key,
    dni varchar(8),
    nombre varchar(50),
    apellido varchar(50),
    saldo decimal(5,2));
    
create table factura(
	id int auto_increment,
    ingreso datetime,
    salida datetime,
    tiempo float,
    monto decimal(5,2),
    tarifa decimal(3,2),
    patente varchar(7),
    primary key (id),
    foreign key(patente) references usuario(patente));

create table estacionamiento(
	id int auto_increment,
    ingreso datetime,
    salida datetime,
    precio_base decimal(3,2),
    direccion varchar(50),
    patente varchar(7),
    primary key (id),
    foreign key(patente) references usuario(patente));
    
    
    