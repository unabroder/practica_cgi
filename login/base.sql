create table login(
id int not null auto_increment,
usuario varchar(50) not null,
password varchar(50) not null,
primary key (id)
);
insert into login(usuario, password) values('admin', 'admin');