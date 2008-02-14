%define name pathological
%define version 1.1.3
%define release %mkrel 2


Version: 	%{version}
Summary: 	Logical game
Name: 		%{name}
Release: 	%{release}
License: 	GPL
Group: 		Games/Strategy
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
Source: 	%{name}-%{version}.tar.bz2
URL: 		http://pathological.sourceforge.net/
BuildRequires:   netpbm
Requires:   pygame

%description
To solve a level, you fill each wheel with four marbles of matching 
colors. Various board elements such as teleporters, switches, filters, 
etc., make the game interesting and challenging. New levels can be 
created using your favorite text editor.

%prep
%setup -q  

%build

%install
rm -rf $RPM_BUILD_ROOT

make DESTDIR=$RPM_BUILD_ROOT install

chmod 755 $RPM_BUILD_ROOT%_libdir/%name/bin/*

(cd $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT%{_datadir}/applications/
cat << EOF > %buildroot%{_datadir}/applications/mandriva-%{name}.desktop
[Desktop Entry]
Type=Application
Exec=%_gamesbindir/pathological
Name=Pathological
Comment=Logical game
Categories=Game;StrategyGame;
Icon=strategy_section
EOF
)

%post
%update_menus
 
%postun
%update_menus 

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr (-,root,root)
%doc README LICENSE
%_gamesbindir/*
%_mandir/man6/*
%_datadir/games/%name
%_libdir/%name/bin/*
%_prefix/X11R6/include/X11/pixmaps/*
%_docdir/%name
%{_datadir}/applications/mandriva-*.desktop
/var/games/*

