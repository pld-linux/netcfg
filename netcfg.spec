Summary: A network configuration tool.
Name: netcfg
Version: 2.20
Release: 2
Copyright: GPL
Group: Applications/System
Source: netcfg-%{PACKAGE_VERSION}.tar.gz
Requires: pythonlib >= 1.20, python, tkinter, initscripts >= 3.24
BuildArchitectures: noarch
BuildRoot: /var/tmp/netcfg-root

%description
A Red Hat Linux tool which provides a graphical user interface for
setting up and configuring networking for your machine.

%prep
%setup -q

%build
unset DISPLAY || true
export PYTHONPATH=/usr/lib/rhs/python
make

%install
rm -rf $RPM_BUILD_ROOT

unset DISPLAY || true
export PYTHONPATH=/usr/lib/rhs/python

make	DESTDIR=$RPM_BUILD_ROOT \
	INSTALLBIN="install -m755" INSTALLDATA="install -m644" \
	install

( cd $RPM_BUILD_ROOT
  mkdir -p ./usr/share/icons
  cp ./usr/lib/rhs/control-panel/netcfg.xpm ./usr/share/icons
)

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
/usr/bin/netcfg
/usr/lib/rhs/netcfg
/usr/lib/rhs/control-panel/netcfg.init
/usr/lib/rhs/control-panel/netcfg.xpm
/usr/share/icons/netcfg.xpm
%attr(0600,root,root)	%config(missingok) /etc/X11/wmconfig/netcfg
