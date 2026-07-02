# Review: https://bugzilla.redhat.com/bugzilla/show_bug.cgi?id=187569
%global minorversion 1.4
%global xfceversion 4.20

Name:           xfce4-mailwatch-plugin
Version:        1.4.0
Release:        %autorelease
Summary:        Mail Watcher plugin for the Xfce panel

# Automatically converted from old format: GPLv2 - review is highly recommended.
License:        GPL-2.0-only
URL:            http://goodies.xfce.org/projects/panel-plugins/%{name}
#VCS: git:git://git.xfce.org/panel-plugins/xfce4-weather-plugin
Source0:        https://gitlab.xfce.org/panel-plugins/xfce4-mailwatch-plugin/-/archive/master/xfce4-mailwatch-plugin-master.tar.gz

BuildRequires:  make
BuildRequires:  gcc-c++
BuildRequires:  libxfce4ui-devel >= %{xfceversion}
BuildRequires:  xfce4-panel-devel >= %{xfceversion}
BuildRequires:  exo-devel >= 0.7.2
BuildRequires:  gnutls-devel >= 1.2.0
BuildRequires:  libgcrypt-devel >= 1.2.0
BuildRequires:  meson
Requires:       xfce4-panel >= %{xfceversion}

%description
Mailwatch is a plugin for the Xfce 4 panel. It is intended to replace the 
current (4.0, 4.2) mail checker plugin in Xfce 4.4. It supports IMAP and POP, 
local mailboxes in Mbox, Maildir and MH-Maildir format as well as Gmail.

%prep
%setup -q -c
shopt -s dotglob
mv */* . 2>/dev/null || :

%build
%meson
%meson_build

%install
%meson_install

# make sure debuginfo is generated properly
chmod -c +x %{buildroot}%{_libdir}/xfce4/panel/plugins/*.so

%find_lang %{name}

%files -f %{name}.lang
%license COPYING
%doc AUTHORS README
%{_libdir}/xfce4/panel/plugins/*.so
%{_datadir}/xfce4/panel/plugins/*.desktop
%{_datadir}/icons/hicolor/*/*/*

%changelog
%autochangelog
