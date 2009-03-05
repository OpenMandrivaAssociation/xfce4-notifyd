Summary: 	Notification daemon for Xfce desktop environment
Name: 		xfce4-notifyd
Version: 	0.1.0
Release: 	%mkrel 4
License:	GPLv3
Group: 		Graphical desktop/Xfce
URL:		http://spuriousinterrupt.org/projects/xfce4-notifyd
Source0:	http://spuriousinterrupt.org/files/xfce4-notifyd/%{name}-%{version}.tar.bz2
BuildRequires:	xfconf-devel
BuildRequires:	libsexy-devel
BuildRequires:	dbus-glib-devel
BuildRequires:	intltool
BuildRequires:	libxfce4util-devel
BuildRequires:	libxfcegui4-devel
Provides:	virtual-notification-daemon
Obsoletes:	notification-daemon-xfce
Conflicts:	notification-daemon
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
%{_libdir}/xfce4-notifyd
%{_datadir}/applications/*.desktop
%{_datadir}/dbus-1/services/org.freedesktop.Notifications.service
%{_iconsdir}/hicolor/*/apps/*.png
%{_datadir}/themes/Default/xfce-notify-4.0
%{_datadir}/themes/Smoke
%{_datadir}/themes/ZOMG-PONIES!
