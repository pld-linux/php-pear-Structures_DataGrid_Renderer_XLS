%include	/usr/lib/rpm/macros.php
%define		_class		Structures
%define		_subclass	DataGrid_Renderer_XLS
%define		_status		beta
%define		_pearname	Structures_DataGrid_Renderer_XLS

Summary:	%{_pearname} - Renderer driver using PEAR::Spreadsheet_Excel_Writer
Summary(pl):	%{_pearname} - sterownik renderera korzystaj±cy z PEAR::Spreadsheet_Excel_Writer
Name:		php-pear-%{_pearname}
Version:	0.1.1
Release:	1
License:	PHP License
Group:		Development/Languages/PHP
Source0:	http://pear.php.net/get/%{_pearname}-%{version}.tgz
# Source0-md5:	b36196dbc631900dffa505f3d8a680c7
URL:		http://pear.php.net/package/Structures_DataGrid_Renderer_XLS/
BuildRequires:	php-pear-PEAR
BuildRequires:	rpm-php-pearprov >= 4.4.2-11
Requires:	php-pear
Requires:	php-pear-PEAR >= 1:1.4.-0.9
Requires:	php-pear-Spreadsheet_Excel_Writer >= 0.9.0
Requires:	php-pear-Structures_DataGrid >= 0.7.0
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This is a Renderer driver for Structures_DataGrid using
PEAR::Spreadsheet_Excel_Writer.

In PEAR status of this package is: %{_status}.

%description -l pl
Ten pakiet dostarcza sterownik renderera dla Structures_DataGrid
korzystaj±cy z PEAR::Spreadsheet_Excel_Writer.

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
%doc install.log
%{php_pear_dir}/.registry/*.reg
%{php_pear_dir}/Structures/DataGrid/Renderer/XLS.php
