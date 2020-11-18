# practica_cgi
# Utilizar CGI-PERL en apache

Para utilizar el CGI se debe realizar una configuracion en el archivo httpd.conf

## Los cambios que se deben hacer en este archivo

Este se encuentra en la carpeta conf de apache en windows

```bash
#se descomentan estas linias
LoadModule authnz_fcgi_module modules/mod_authnz_fcgi.so
LoadModule cgi_module modules/mod_cgi.so
ScriptAlias /cgi-bin/ "${SRVROOT}/cgi-bin/"
#se establece que se pueda ejecutar archivos CGI
<Directory "${SRVROOT}/cgi-bin">
    AllowOverride None
    Options +ExecCGI
    Require all granted
</Directory>
#se agregan las extensiones permitidas 
AddHandler cgi-script .cgi .pl
#para que muestre los errores
ErrorDocument 404 "/cgi-bin/missing_handler.pl"
```

## Para utilizar Perl en windows se recomienda utilizar Strawberry


## Para poder utilizar Perl 
Para utilizar perl se crea una variable de entorno en windows para poder utilizar perl de forma global en el sistema operativo windows
