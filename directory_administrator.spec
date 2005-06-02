Summary:	LDAP directory user/group/access control manager
Summary(es):	Administrador de usuarios/grupos y control de acceso LDAP
Summary(pl):	Administrator u�ytkownik�w/grup POSIX us�ug katalogowych LDAP
Summary(pt_BR):	Administrador de usu�rios/controle de acesso/grupos para LDAP
Name:		directory_administrator
Version:	1.6.0
Release:	1
License:	GPL
Group:		X11/Applications
Source0:	http://diradmin.open-it.org/releases/%{name}-%{version}.tar.gz
# Source0-md5:	ab0631f5e91c0dfe48c1be240eb01437
Patch0:		%{name}-desktop.patch
URL:		http://diradmin.open-it.org/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	gnome-libs-devel
BuildRequires:	openldap-devel
Requires:	openldap
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Directory administrator is a POSIX user/group manager for LDAP
directories. It can also manage access controls, departmental and
e-mail routing information.

%description -l es
Directory administrator es un administrador de usuarios/grupos POSIX
para servidores de directorio LDAP. Directory administrator permite
administrar tambi�n controles de acceso, informaci�n departamental y
rutas de correo electr�nico para aquellos servidores de correo que lo
soporten.

%description -l pl
Directory Administrator jest zarz�dc� u�ytkownik�w/grup POSIX us�ug
katalogowych LDAP. Umo�liwia r�wnie� zarz�dzanie prawami dost�pu oraz
przekierowaniem poczty.

%prep
%setup -q -n diradmin-%{version}
%patch0 -p1

%build
rm -f missing
%{__aclocal} -I macros
%{__autoconf}
%{__automake}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_desktopdir},%{_pixmapsdir}/directory_administrator}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

install pixmaps/*.{xpm,png} $RPM_BUILD_ROOT%{_pixmapsdir}/directory_administrator

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README ChangeLog AUTHORS CREDITS NEWS
%attr(755,root,root) %{_bindir}/directory_administrator
%{_desktopdir}/*.desktop
%{_pixmapsdir}/directory_administrator
