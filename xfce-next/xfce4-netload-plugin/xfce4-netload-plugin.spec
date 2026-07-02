%global _hardened_build 1
%global minor_version 1.5
%global xfceversion 4.20

Name:           xfce4-netload-plugin
Version:        1.5.0
Release:        %autorelease
Summary:        Network-load monitor for the Xfce panel

# Automatically converted from old format: GPLv2+ - review is highly recommended.
License:        GPL-2.0-or-later
URL:            http://goodies.xfce.org/projects/panel-plugins/%{name}
Source0:        https://gitlab.xfce.org/panel-plugins/xfce4-netload-plugin/-/archive/master/xfce4-netload-plugin-master.tar.gz

BuildRequires:  make
BuildRequires:  gcc-c++
BuildRequires:  pkgconfig(libxfce4panel-2.0) >= %{xfceversion}
BuildRequires:  pkgconfig(libxfce4ui-2) >= %{xfceversion}
BuildRequires:  libxml2-devel
BuildRequires:  meson

Requires:       xfce4-panel >= %{xfceversion}

%description
A network-load monitor plugin for the Xfce panel.

%prep
%setup -q -c
shopt -s dotglob
mv */* . 2>/dev/null || :

%build
%meson
%meson_build

%install
%meson_install

%find_lang %{name}
chmod 755 %{buildroot}/%{_libdir}/xfce4/panel/plugins/libnetload.so

%files -f %{name}.lang
%doc AUTHORS README
%license COPYING
%{_datadir}/icons/hicolor/*/*/*
%{_libdir}/xfce4/panel/plugins/libnetload.so
%{_datadir}/xfce4/panel/plugins/*.desktop

%changelog
%autochangelog
