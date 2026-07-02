%global _hardened_build 1
%global minor_version 4.7
%global xfceversion 4.16

Name:           xfce4-eyes-plugin
Version:        4.7.0
Release:        %autorelease
Summary:        Eyes for the Xfce panel

# Automatically converted from old format: GPLv2+ - review is highly recommended.
License:        GPL-2.0-or-later
URL:            http://goodies.xfce.org/projects/panel-plugins/%{name}
Source0:        https://gitlab.xfce.org/panel-plugins/xfce4-eyes-plugin/-/archive/master/xfce4-eyes-plugin-master.tar.gz

BuildRequires:  make
BuildRequires:  gcc-c++
BuildRequires:  xfce4-panel-devel >= %{xfceversion}
BuildRequires:  libxfce4ui-devel >= %{xfceversion}
BuildRequires:  libxml2-devel
BuildRequires:  meson

Requires:       xfce4-panel >= %{xfceversion}

%description
A xfce4 panel plugin that adds eyes which watch your every step. Scary!

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

%files -f %{name}.lang
%doc AUTHORS
%license COPYING
%{_datadir}/xfce4/panel/plugins/*.desktop
%{_libdir}/xfce4/panel/plugins/libeyes.so
%{_datadir}/icons/hicolor/*/apps/xfce4-eyes.png
%{_datadir}/xfce4/eyes

%changelog
%autochangelog
