%define url_ver %(echo %{version} | cut -d. -f 1,2)
%define _disable_rebuild_configure 1

Summary: 	Notification daemon for Xfce desktop environment
Name: 		xfce4-notifyd
Version:	0.6.1
Release:	1
License:	GPLv3
Group: 		Graphical desktop/Xfce
URL:		http://goodies.xfce.org/projects/applications/xfce4-notifyd
Source0:	http://archive.xfce.org/src/apps/%{name}/%{url_ver}/%{name}-%{version}.tar.bz2
Source1:	xfce4-notifyd.rpmlintrc
BuildRequires:	pkgconfig(libxfconf-0)
BuildRequires:	pkgconfig(libsexy)
BuildRequires:	pkgconfig(dbus-glib-1)
BuildRequires:	intltool
BuildRequires:	pkgconfig(libxfce4util-1.0) >= 4.11
BuildRequires:	pkgconfig(libxfce4ui-2) >= 4.9.1
BuildRequires:	pkgconfig(libxfce4panel-2.0)
BuildRequires:	pkgconfig(libnotify)
Requires:	xfconf
Provides:	virtual-notification-daemon
Obsoletes:	notification-daemon-xfce

%description
Xfce4-notifyd is a simple, visually-appealing notification daemon for 
Xfce that implements the Freedesktop.org Desktop Notifications 
Specification.

Features:
* Themable using the GTK+ theming mechanism
* Visually appealing: rounded corners, shaped windows
* Supports transparency and fade effects

%prep
%setup -q

%build
%configure \
	--disable-static
%make_build

%install
%make_install

%find_lang %{name} %{name}.lang

%files -f %{name}.lang
%doc ChangeLog AUTHORS README TODO
%_userunitdir/xfce4-notifyd.service
%{_bindir}/xfce4-notifyd-config
%{_libdir}/xfce4/notifyd
%{_datadir}/applications/*.desktop
%{_datadir}/dbus-1/services/org.xfce.xfce4-notifyd.Notifications.service
%{_iconsdir}/hicolor/*/apps/*.png
%{_iconsdir}/hicolor/*/*/*.svg
%{_datadir}/themes/Default/xfce-notify-4.0
%{_datadir}/themes/Smoke
%{_datadir}/themes/ZOMG-PONIES!
%{_datadir}/themes/Bright
%{_datadir}/themes/Retro
%{_datadir}/xfce4/panel/plugins/notification-plugin.desktop
%{_mandir}/man1/xfce4-notifyd-config*
%{_libdir}/xfce4/panel/plugins/libnotification-plugin.so
