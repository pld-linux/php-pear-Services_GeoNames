%define		_status		stable
%define		_pearname	Services_GeoNames
Summary:	%{_pearname} - A PHP5 interface to the GeoNames public API
Summary(pl.UTF-8):	%{_pearname} - interfejs PHP5 do publicznego API GeoNames
Name:		php-pear-%{_pearname}
Version:	1.0.1
Release:	2
License:	MIT
Group:		Development/Languages/PHP
Source0:	http://pear.php.net/get/%{_pearname}-%{version}.tgz
# Source0-md5:	151339867e57d0b33f3d08b796c15a21
URL:		http://pear.php.net/package/Services_GeoNames/
BuildRequires:	php-pear-PEAR >= 1:1.4.0-0.b1
BuildRequires:	rpm-php-pearprov >= 4.4.2-11
BuildRequires:	rpmbuild(macros) >= 1.300
Requires:	php-pear
Requires:	php-pear-HTTP_Request2 >= 0.1.0
Requires:	php-pear-PEAR >= 1.4.0
Obsoletes:	php-pear-Services_GeoNames-tests
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Services_GeoNames is a PHP5 interface to the various webservices
offered by the GeoNames project.

The GeoNames database contains over 8,000,000 geographical names
corresponding to over 6,500,000 unique features. All features are
categorized into one out of nine feature classes and further
subcategorized into one out of 645 feature codes. Beyond names of
places in various languages, data stored include latitude, longitude,
elevation, population, administrative subdivision and postal codes.
All coordinates use the WGS84 system (World Geodetic System 1984).

Those data are accessible free of charge through a number of Web
services and a daily database export. The Web services include direct
and reverse geocoding, finding places through postal codes, finding
places next to a given place, and finding Wikipedia articles about
neighbouring places.

For more information please visit:
 - http://www.geonames.org
 - http://www.geonames.org/export/ws-overview.html
 - http://en.wikipedia.org/wiki/GeoNames

In PEAR status of this package is: %{_status}.

%description -l pl.UTF-8
Services_GeoNames to interfejs PHP5 do różnych usług webowych
udostępnianych przez projekt GeoNames.

Baza danych GeoNames zawiera ponad 8 000 000 nazw geograficznych
odpowiadających ponad 6 500 000 różnym punktom. Każdy z punktów
sklasyfikowany jest w jednej z dziewięciu głównych kategorii i
kolejnych podkategoriach za pomocą jednego z 645 kodów. Poza nazwami
miejsc wyrażonymi w różnych językach, przechowywane są takie
informacje jak współrzędne geograficzne, wysokość, populacja,
informacje o podziale administracyjnym czy kodach pocztowych.
Wszystkie współrzędne zapisane w systemie WGS84 (World Geodetic System
1984).

Dane dostępne są bez opłat za pomocą różnych interfejsów oraz w
postaci dziennego eksportu bazy danych. Usługi umożliwiają
bezpośrednią i odwrotną lokalizację, znajdywanie miejsc na podstawie
kodów pocztowych, znajdowanie miejsc w pobliżu danej lokalizacji czy
odszukiwanie artykułów wikipedii o okolicznych miejscach.

Więcej informacji na stronach:
 - http://www.geonames.org
 - http://www.geonames.org/export/ws-overview.html
 - http://en.wikipedia.org/wiki/GeoNames

Ta klasa ma w PEAR status: %{_status}.

%prep
%pear_package_setup

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{php_pear_dir}
%pear_package_install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc install.log docs/Services_GeoNames/examples/examples1.php
%{php_pear_dir}/.registry/*.reg
%{php_pear_dir}/Services/GeoNames.php
%{php_pear_dir}/Services/GeoNames
