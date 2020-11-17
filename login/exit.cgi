#!c:/Strawberry/perl/bin/perl.exe
use strict;
use CGI;
use CGI::Session;
use CGI::Carp qw(fatalsToBrowser);
use DBI;
my $session = new CGI::Session;
$session->load();
$session->delete();
$session->flush();
print $session->header(-location => "../login.html");