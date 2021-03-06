%define		_status		beta
%define		_pearname	Structures_DataGrid_Renderer_XLS
Summary:	%{_pearname} - Renderer driver using PEAR::Spreadsheet_Excel_Writer
Summary(pl.UTF-8):	%{_pearname} - sterownik renderera korzystający z PEAR::Spreadsheet_Excel_Writer
Name:		php-pear-%{_pearname}
Version:	0.1.3
Release:	2
License:	PHP License
Group:		Development/Languages/PHP
Source0:	http://pear.php.net/get/%{_pearname}-%{version}.tgz
# Source0-md5:	373b154195dfeb368eb4038bb1583768
URL:		http://pear.php.net/package/Structures_DataGrid_Renderer_XLS/
BuildRequires:	php-pear-PEAR >= 1:1.6.0
BuildRequires:	rpm-php-pearprov >= 4.4.2-11
BuildRequires:	rpmbuild(macros) >= 1.300
Requires:	php-pear
Requires:	php-pear-Spreadsheet_Excel_Writer >= 0.9.0
Requires:	php-pear-Structures_DataGrid >= 0.9.0
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This is a Renderer driver for Structures_DataGrid using
PEAR::Spreadsheet_Excel_Writer.

In PEAR status of this package is: %{_status}.

%description -l pl.UTF-8
Ten pakiet dostarcza sterownik renderera dla Structures_DataGrid
korzystający z PEAR::Spreadsheet_Excel_Writer.

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
