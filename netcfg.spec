Summary:	A network configuration tool
Summary(pl):	Narzêdzie do konfiguracji sieci
Name:		netcfg
Version:	2.20
Release:	2
License:	GPL
Group:		Applications/System
Source0:	%{name}-%{version}.tar.gz
# Source0-md5:	dd4ba06d9ee22ec0afbca7fd73823ca5
Requires:	pythonlib >= 1.20, python, tkinter, initscripts >= 3.24
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
A Red Hat Linux tool which provides a graphical user interface for
setting up and configuring networking for your machine.

%description -l pl
Narzêdzie Red Hata daj±ce graficzny interfejs u¿ytkownika do
ustawiania i konfigurowania sieci.

%prep
%setup -q

%build
unset DISPLAY || true
PYTHONPATH=%{_libdir}/rhs/python
export PYTHONPATH
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

unset DISPLAY || true
PYTHONPATH=%{_libdir}/rhs/python
export PYTHONPATH

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	INSTALLBIN="install -m755" INSTALLDATA="install -m644"

( cd $RPM_BUILD_ROOT
  install -d .%{_pixmapsdir}
  cp .%{_libdir}/rhs/control-panel/netcfg.xpm .%{_pixpapsdir}
)

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/netcfg
%{_libdir}/rhs/netcfg
%{_libdir}/rhs/control-panel/netcfg.init
%{_libdir}/rhs/control-panel/netcfg.xpm
%{_pixmapsdir}/netcfg.xpm
%attr(0600,root,root) %config(missingok) %{_sysconfdir}/X11/wmconfig/netcfg
