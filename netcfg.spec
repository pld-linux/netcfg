Summary:	A network configuration tool
Name:		netcfg
Version:	2.20
Release:	2
License:	GPL
Group:		Utilities/System
Group(pl):	Narzêdzia/System
Source0:	netcfg-%{PACKAGE_VERSION}.tar.gz
Requires:	pythonlib >= 1.20, python, tkinter, initscripts >= 3.24
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
A Red Hat Linux tool which provides a graphical user interface for
setting up and configuring networking for your machine.

%prep
%setup -q

%build
unset DISPLAY || true
export PYTHONPATH=%{_libdir}/rhs/python
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

unset DISPLAY || true
export PYTHONPATH=%{_libdir}/rhs/python

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	INSTALLBIN="install -m755" INSTALLDATA="install -m644"

( cd $RPM_BUILD_ROOT
  install -d .%{_datadir}/icons
  cp .%{_libdir}/rhs/control-panel/netcfg.xpm .%{_datadir}/icons
)

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/netcfg
%{_libdir}/rhs/netcfg
%{_libdir}/rhs/control-panel/netcfg.init
%{_libdir}/rhs/control-panel/netcfg.xpm
%{_datadir}/icons/netcfg.xpm
%attr(0600,root,root) %config(missingok) %{_sysconfdir}/X11/wmconfig/netcfg
