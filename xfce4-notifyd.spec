%define url_ver %(echo %{version} | cut -c 1-3)

Summary: 	Notification daemon for Xfce desktop environment
Name: 		xfce4-notifyd
Version: 	0.2.2
Release: 	3
License:	GPLv3
Group: 		Graphical desktop/Xfce
URL:		http://goodies.xfce.org/projects/applications/xfce4-notifyd
Source0:	http://archive.xfce.org/src/apps/%{name}/%{url_ver}/%{name}-%{version}.tar.bz2
BuildRequires:	xfconf-devel
BuildRequires:	libsexy-devel
BuildRequires:	dbus-glib-devel
BuildRequires:	intltool
BuildRequires:	libxfce4util-devel >= 4.9.0
BuildRequires:	libxfce4ui-devel >= 4.9.1
BuildRequires:	libnotify-devel
Requires:	xfconf
Provides:	virtual-notification-daemon
Obsoletes:	notification-daemon-xfce
#Conflicts:	notification-daemon

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
%makeinstall_std

%find_lang %{name} %{name}.lang

%files -f %{name}.lang
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


%changelog
* Thu Apr 05 2012 Tomasz Pawel Gajc <tpg@mandriva.org> 0.2.2-3
+ Revision: 789489
- rebuild

* Sun Aug 14 2011 Tomasz Pawel Gajc <tpg@mandriva.org> 0.2.2-2
+ Revision: 694562
- revert drop of virtual-notification-daemon provide

* Sun Aug 14 2011 Tomasz Pawel Gajc <tpg@mandriva.org> 0.2.2-1
+ Revision: 694551
- update to new version 0.2.2
- drop confilts with notification-daemon
- do not provide virtual-notification-daemon anymore

* Sat Mar 12 2011 Funda Wang <fwang@mandriva.org> 0.2.1-2
+ Revision: 643887
- rebuild to obsolete old packages

* Wed Feb 02 2011 Tomasz Pawel Gajc <tpg@mandriva.org> 0.2.1-1
+ Revision: 635386
- update to new version 0.2.1

* Wed Jan 26 2011 Tomasz Pawel Gajc <tpg@mandriva.org> 0.2.0-2
+ Revision: 633056
- rebuild for new Xfce 4.8.0

* Sat Nov 27 2010 Tomasz Pawel Gajc <tpg@mandriva.org> 0.2.0-1mdv2011.0
+ Revision: 601903
- update to new version 0.2.0
- update urls
- drop patch 0
- fix file list

* Fri May 07 2010 Tomasz Pawel Gajc <tpg@mandriva.org> 0.1.0-7mdv2010.1
+ Revision: 543311
- rebuild for mdv 2010.1

* Sun Aug 30 2009 Tomasz Pawel Gajc <tpg@mandriva.org> 0.1.0-6mdv2010.0
+ Revision: 422646
- add requires on xfconf (mdvbz #51336)

* Sun May 24 2009 Tomasz Pawel Gajc <tpg@mandriva.org> 0.1.0-5mdv2010.0
+ Revision: 379282
- Patch0:correctly send two arguments with NotificationClosed

* Thu Mar 05 2009 Tomasz Pawel Gajc <tpg@mandriva.org> 0.1.0-4mdv2009.1
+ Revision: 349225
- rebuild whole xfce

* Fri Nov 28 2008 Tomasz Pawel Gajc <tpg@mandriva.org> 0.1.0-3mdv2009.1
+ Revision: 307474
- conflicts with notification-daemon

* Fri Nov 28 2008 Tomasz Pawel Gajc <tpg@mandriva.org> 0.1.0-2mdv2009.1
+ Revision: 307472
- provides virtual-notification-daemon
- obsolete notification-daemon-xfce

* Wed Nov 26 2008 Tomasz Pawel Gajc <tpg@mandriva.org> 0.1.0-1mdv2009.1
+ Revision: 306810
- add source and spec files
- Created package structure for xfce4-notifyd.

