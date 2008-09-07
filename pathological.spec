Name: 		pathological
Summary: 	Logical game
Version: 	1.1.3
Release: 	%{mkrel 3}
License: 	GPLv2+
Group: 		Games/Strategy
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot
Source0:	http://downloads.sourceforge.net/%{name}/%{name}-%{version}.tar.bz2
# Don't install something to /usr/X11R6 - AdamW 2008/09
Patch0:		pathological-1.1.3-location.patch
URL: 		http://pathological.sourceforge.net/
BuildRequires:	netpbm
BuildRequires:	ImageMagick
Requires:	pygame

%description
To solve a level, you fill each wheel with four marbles of matching 
colors. Various board elements such as teleporters, switches, filters, 
etc., make the game interesting and challenging. New levels can be 
created using your favorite text editor.

%prep
%setup -q  
%patch0 -p1 -b .location

%build

%install
rm -rf %{buildroot}
%makeinstall_std

chmod 755 %{buildroot}%{_libdir}/%{name}/bin/*
rm -rf %{buildroot}%{_docdir}/%{name}

mkdir -p %{buildroot}%{_iconsdir}/hicolor/{16x16,32x32}/apps
convert %{name}.xpm %{buildroot}%{_iconsdir}/hicolor/32x32/apps/%{name}.png
convert -scale 16 %{name}.xpm %{buildroot}%{_iconsdir}/hicolor/16x16/apps/%{name}.png

mkdir -p %{buildroot}%{_datadir}/applications/
cat << EOF > %{buildroot}%{_datadir}/applications/mandriva-%{name}.desktop
[Desktop Entry]
Type=Application
Exec=%{_gamesbindir}/pathological
Name=Pathological
Comment=Logic game
Categories=Game;StrategyGame;
Icon=%{name}
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
%{_includedir}/X11/pixmaps/*
%{_datadir}/applications/mandriva-*.desktop
%{_iconsdir}/hicolor/*/apps/%{name}.png
%{_localstatedir}/games/*

