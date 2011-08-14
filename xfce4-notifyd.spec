%define url_ver %(echo %{version} | cut -c 1-3)

Summary: 	Notification daemon for Xfce desktop environment
Name: 		xfce4-notifyd
Version: 	0.2.2
Release: 	%mkrel 2
License:	GPLv3
Group: 		Graphical desktop/Xfce
URL:		http://goodies.xfce.org/projects/applications/xfce4-notifyd
Source0:	http://archive.xfce.org/src/apps/%{name}/%{url_ver}/%{name}-%{version}.tar.bz2
BuildRequires:	xfconf-devel
BuildRequires:	libsexy-devel
BuildRequires:	dbus-glib-devel
BuildRequires:	intltool
BuildRequires:	libxfce4util-devel
BuildRequires:	libxfce4ui-devel
BuildRequires:	libnotify-devel
Requires:	xfconf
Provides:	virtual-notification-daemon
Obsoletes:	notification-daemon-xfce
#Conflicts:	notification-daemon
BuildRoot: 	%{_tmppath}/%{name}-%{version}-buildroot

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
%configure2_5x \
	--disable-static
%make

%install
rm -rf %{buildroot}
%makeinstall_std 

%find_lang %{name}

%clean
rm -rf %{buildroot}

%files -f %{name}.lang
%defattr(-,root,root)
%doc ChangeLog AUTHORS README TODO
%{_bindir}/xfce4-notifyd-config
%{_libdir}/xfce4/notifyd
%{_datadir}/applications/*.desktop
%{_datadir}/dbus-1/services/org.xfce.xfce4-notifyd.Notifications.service
%{_iconsdir}/hicolor/*/apps/*.png
%{_datadir}/themes/Default/xfce-notify-4.0
%{_datadir}/themes/Smoke
%{_datadir}/themes/ZOMG-PONIES!
%{_mandir}/man1/xfce4-notifyd-config*
