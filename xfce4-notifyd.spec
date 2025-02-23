Summary:	XFCE Notify Daemon
Summary(pl.UTF-8):	Demon powiadomień XFCE
Name:		xfce4-notifyd
Version:	0.9.7
Release:	1
License:	GPL v2
Group:		Applications/System
Source0:	https://archive.xfce.org/src/apps/xfce4-notifyd/0.9/%{name}-%{version}.tar.bz2
# Source0-md5:	d5bfe1fd8e8da9d64367a1f520d88633
URL:		https://git.xfce.org/apps/xfce4-notifyd/
BuildRequires:	dbus-devel >= 1.0
BuildRequires:	dbus-glib-devel
BuildRequires:	glib2-devel >= 1:2.68
BuildRequires:	gtk+3-devel >= 3.22
BuildRequires:	gtk-layer-shell-devel >= 0.7.0
BuildRequires:	libcanberra-gtk3-devel >= 0.30
BuildRequires:	libnotify-devel >= 0.7.0
BuildRequires:	libxfce4ui-devel >= 4.14.0
BuildRequires:	libxfce4util-devel >= 4.14.0
BuildRequires:	pkgconfig >= 1:0.9.0
BuildRequires:	sqlite3-devel >= 3.34
BuildRequires:	systemd-devel >= 245
BuildRequires:	xfce4-dev-tools >= 4.14.0
BuildRequires:	xfce4-panel-devel >= 4.14.0
BuildRequires:	xfconf-devel >= 4.14.0
Requires(post,postun):	gtk-update-icon-cache
Requires(post,postun):	hicolor-icon-theme
Requires:	dbus >= 0.91
Provides:	dbus(org.freedesktop.Notifications)
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The XFCE Notify Daemon (xfce4-notifyd for short) is a smallish program
that implements the "server-side" portion of the Freedesktop desktop
notifications specification. Applications that wish to pop up a
notification bubble in a standard way can implicitly make use of
xfce4-notifyd to do so by sending standard messages over D-Bus using
the org.freedesktop.Notifications interface.

%description -l pl.UTF-8
Demon powiadomień XFCE (w skrócie xfce4-notifyd) jest niewielkim
programem implementującym serwerową część specyfikacji powiadomień.

%prep
%setup -q

%build
%configure

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%{__rm} $RPM_BUILD_ROOT%{_libdir}/xfce4/panel/plugins/libnotification-plugin.la
%{__rm} -r $RPM_BUILD_ROOT%{_localedir}/{hye,hy_AM,ie}

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%post
%update_icon_cache hicolor

%postun
%update_icon_cache hicolor

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS NEWS README.md TODO
%attr(755,root,root) %{_bindir}/xfce4-notifyd-config
%dir %{_libdir}/xfce4/notifyd
%attr(755,root,root) %{_libdir}/xfce4/notifyd/xfce4-notifyd
%{_sysconfdir}/xdg/autostart/xfce4-notifyd.desktop
%{_desktopdir}/xfce4-notifyd-config.desktop
%{_iconsdir}/hicolor/*/apps/org.xfce.notification.*
%{_datadir}/themes/Bright
%{_datadir}/themes/Default/xfce-notify-4.0
%{_datadir}/themes/Retro
%{_datadir}/themes/Smoke
%{_datadir}/themes/XP-Balloon
%{_datadir}/themes/ZOMG-PONIES!
%{systemduserunitdir}/xfce4-notifyd.service
%{_datadir}/dbus-1/services/org.xfce.xfce4-notifyd.Notifications.service
%{_datadir}/dbus-1/services/org.xfce.xfce4-notifyd.Notifyd.service
%{_mandir}/man1/xfce4-notifyd-config.1*
%attr(755,root,root) %{_libdir}/xfce4/panel/plugins/libnotification-plugin.so
%{_datadir}/xfce4/panel/plugins/notification-plugin.desktop
%{_iconsdir}/hicolor/scalable/status/notification-disabled-symbolic.svg
%{_iconsdir}/hicolor/scalable/status/org.xfce.notification.unread-emblem-symbolic.svg
%{_iconsdir}/hicolor/scalable/status/notification-symbolic.svg
