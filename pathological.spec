Name: 		pathological
Summary: 	Logical game
Version: 	1.1.3
Release: 	8
License: 	GPLv2+
Group: 		Games/Puzzles
Source0:	http://downloads.sourceforge.net/%{name}/%{name}-%{version}.tar.bz2
# Don't install something to /usr/X11R6 - AdamW 2008/09
Patch0:		pathological-1.1.3-location.patch
# fix #35077
Patch1:     pathological-1.1.3-fix_encoding.patch
URL: 		http://pathological.sourceforge.net/
BuildRequires:	netpbm
BuildRequires:	imagemagick
Requires:	pygame
BuildArch:	noarch

%description
To solve a level, you fill each wheel with four marbles of matching 
colors. Various board elements such as teleporters, switches, filters, 
etc., make the game interesting and challenging. New levels can be 
created using your favorite text editor.

%prep
%setup -q  
%patch0 -p1 -b .location
%patch1 -p0

sed -i -e 's,/usr/lib,%{_libdir},g' Makefile

%build

%install
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
Categories=Game;LogicGame;
Icon=%{name}
EOF

%files
%doc README LICENSE
%{_gamesbindir}/*
%{_mandir}/man6/*
%{_datadir}/games/%{name}
%{_libdir}/%{name}/bin/*
%{_includedir}/X11/pixmaps/*
%{_datadir}/applications/mandriva-*.desktop
%{_iconsdir}/hicolor/*/apps/%{name}.png
%{_localstatedir}/games/*



%changelog
* Tue Dec 07 2010 Oden Eriksson <oeriksson@mandriva.com> 1.1.3-8mdv2011.0
+ Revision: 614476
- the mass rebuild of 2010.1 packages

* Mon Sep 14 2009 Thierry Vignaud <tv@mandriva.org> 1.1.3-7mdv2010.1
+ Revision: 440498
- rebuild

* Fri Apr 03 2009 Michael Scherer <misc@mandriva.org> 1.1.3-6mdv2009.1
+ Revision: 363942
- also fix the menu

* Fri Apr 03 2009 Michael Scherer <misc@mandriva.org> 1.1.3-5mdv2009.1
+ Revision: 363909
- fix the rm group
- fix bug 35077

* Sun Sep 07 2008 Adam Williamson <awilliamson@mandriva.org> 1.1.3-3mdv2009.0
+ Revision: 282295
- replace hardcoded /usr/lib in Makefile to fix x86-64 build
- buildrequires imagemagick
- generate fd.o icons from shipped .xpm file
- add location.patch: don't use /usr/X11R6
- clean up the docs mess
- s,$RPM_BUILD_ROOT,%%{buildroot}
- source location
- new license policy
- drop unncessary defines

  + Thierry Vignaud <tv@mandriva.org>
    - rebuild
    - fix no-buildroot-tag
    - auto convert menu to XDG
    - BR netpbm
    - kill re-definition of %%buildroot on Pixel's request
    - use %%mkrel
    - import pathological

  + Pixel <pixel@mandriva.com>
    - rpm filetriggers deprecates update_menus/update_scrollkeeper/update_mime_database/update_icon_cache/update_desktop_database/post_install_gconf_schemas


* Sun Mar 20 2005 Michael Scherer <misc@mandrake.org> 1.1.3-2mdk
- requires pygame, fix #12744
- fix spec

* Tue Feb 10 2004 Lenny Cartier <lenny@mandrakesoft.com> 1.1.3-1mdk
- 1.1.3
