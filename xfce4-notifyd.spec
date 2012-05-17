Summary:	XFCE Notify Daemon
Summary(pl.UTF-8):	Demon powiadomień XFCE
Name:		xfce4-notifyd
Version:	0.2.2
Release:	2
License:	GPL v2
Group:		Applications/System
Source0:	http://www.xfce.org/archive/src/apps/xfce4-notifyd/0.2/%{name}-%{version}.tar.bz2
# Source0-md5:	8687fb7a0f270231ada265e363b6ffcc
#URL:		http://www.xfce.org/projects/xfce4-notifyd/
URL:		http://git.xfce.org/apps/xfce4-notifyd/
BuildRequires:	dbus-devel
BuildRequires:	dbus-glib-devel
BuildRequires:	gtk+2-devel >= 2:2.10.6
BuildRequires:	libxfce4ui-devel >= 4.8.0
BuildRequires:	libxfce4util-devel >= 4.8.0
BuildRequires:	pkgconfig >= 1:0.9.0
BuildRequires:	xfce4-dev-tools >= 4.8.0
BuildRequires:	xfconf-devel >= 4.8.0
Requires(post,postun):	gtk-update-icon-cache
Requires(post,postun):	hicolor-icon-theme
Requires:	dbus >= 0.91
Provides:	dbus(org.freedesktop.Notifications)
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The XFCE Notify Daemon (xfce4-notifyd for short) is a smallish program
that implements the "server-side" portion of the Freedesktop desktop
notifications specification.  Applications that wish to pop up
a notification bubble in a standard way can implicitly make use of
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

%{__rm} -r $RPM_BUILD_ROOT%{_datadir}/locale/pt_PT

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%post
%update_icon_cache hicolor

%postun
%update_icon_cache hicolor

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README TODO
%attr(755,root,root) %{_bindir}/xfce4-notifyd-config
%dir %{_libdir}/xfce4/notifyd
%attr(755,root,root) %{_libdir}/xfce4/notifyd/xfce4-notifyd
%{_datadir}/dbus-1/services/org.xfce.xfce4-notifyd.Notifications.service
%{_desktopdir}/xfce4-notifyd-config.desktop
%{_iconsdir}/hicolor/*/apps/xfce4-notifyd.png
%{_datadir}/themes/Default/xfce-notify-4.0
%{_datadir}/themes/Smoke
%{_datadir}/themes/ZOMG-PONIES!
%{_mandir}/man1/xfce4-notifyd-config.1*