Name: 		pathological
Summary: 	Logical game
Version: 	1.1.3
Release: 	%{mkrel 3}
License: 	GPLv2+
Group: 		Games/Strategy
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot
Source:		http://downloads.sourceforge.net/%{name}/%{name}-%{version}.tar.bz2
URL: 		http://pathological.sourceforge.net/
BuildRequires:	netpbm
Requires:	pygame

%description
To solve a level, you fill each wheel with four marbles of matching 
colors. Various board elements such as teleporters, switches, filters, 
etc., make the game interesting and challenging. New levels can be 
created using your favorite text editor.

%prep
%setup -q  

%build

%install
rm -rf %{buildroot}
%makeinstall_std

chmod 755 %{buildroot}%{_libdir}/%{name}/bin/*
rm -rf %{buildroot}%{_docdir}/%{name}

mkdir -p %{buildroot}%{_datadir}/applications/
cat << EOF > %{buildroot}%{_datadir}/applications/mandriva-%{name}.desktop
[Desktop Entry]
Type=Application
Exec=%{_gamesbindir}/pathological
Name=Pathological
Comment=Logic game
Categories=Game;StrategyGame;
Icon=strategy_section
EOF

%if %mdkversion < 200900
%post
%update_menus
%endif
 
%if %mdkversion < 200900
%postun
%update_menus 
%endif

%clean
rm -rf %{buildroot}

%files
%defattr (-,root,root)
%doc README LICENSE
%{_gamesbindir}/*
%{_mandir}/man6/*
%{_datadir}/games/%{name}
%{_libdir}/%{name}/bin/*
%{_prefix}/X11R6/include/X11/pixmaps/*
%{_datadir}/applications/mandriva-*.desktop
%{_localstatedir}/games/*

