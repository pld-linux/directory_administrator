Summary:	LDAP directory user/group/access control manager
Summary(es):	Administrador de usuarios/grupos y control de acceso LDAP
Summary(pl):	Administrator u¿ytkowników/grup POSIX us³ug katalogowych LDAP
Summary(pt_BR):	Administrador de usuários/controle de acesso/grupos para LDAP
Name:		directory_administrator
Version:	1.1.8
Release:	0.1
License:	GPL
Group:		X11/Applications
Source0:	http://diradmin.open-it.org/%{name}-%{version}.tar.gz
Patch0:		%{name}-desktop.patch
URL:		http://diradmin.open-it.org/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	gnome-libs-devel
BuildRequires:	gtk+-devel >= 1.2.3
BuildRequires:	openldap-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)
Requires:	openldap

%define         _prefix         /usr/X11R6
%define         _mandir         %{_prefix}/man

%description
Directory administrator is a POSIX user/group manager for LDAP
directories. It can also manage access controls, departmental and
e-mail routing information.

%description -l es
Directory administrator es un administrador de usuarios/grupos POSIX
para servidores de directorio LDAP. Directory administrator permite
administrar también controles de acceso, información departamental y
rutas de correo electrónico para aquellos servidores de correo que lo
soporten.

%description -l pl
Directory Administrator jest zarz±dc± u¿ytkowników/grup POSIX us³ug
katalogowych LDAP. Umo¿liwia równie¿ zarz±dzanie prawami dostêpu oraz
przekierowaniem poczty.

%prep
%setup -q
%patch0 -p1

%build
rm -f missing
libtoolize --copy --force
aclocal -I macros
%{__autoconf}
%{__automake}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
%{__make} install DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README ChangeLog AUTHORS CREDITS NEWS
%attr(0755,root,root) %{_bindir}/directory_administrator
#%attr(0644,root,root) %{_libdir}/menu/directory_administrator
%attr(0644,root,root) %{_applnkdir}/System/*
%attr(0644,root,root) %{_datadir}/pixmaps/directory_administrator/*
