%global minorver 1.7
%global _hardened_build 1

Name:		xfce4-timer-plugin
Version:	1.7.3
Release:	%autorelease
Summary:	Timer for the Xfce panel
# Automatically converted from old format: GPLv2+ - review is highly recommended.
License:	GPL-2.0-or-later
URL:		http://goodies.xfce.org/projects/panel-plugins/%{name}
Source0:        https://gitlab.xfce.org/panel-plugins/xfce4-timer-plugin/-/archive/master/xfce4-timer-plugin-master.tar.gz

BuildRequires: make
BuildRequires:  meson
BuildRequires:  ninja-build
BuildRequires:	gcc-c++
BuildRequires:	xfce4-panel-devel
BuildRequires:	libxfce4ui-devel
BuildRequires:	libxml2-devel
BuildRequires:	gettext
BuildRequires:	intltool
BuildRequires:	perl(XML::Parser)

Requires:	xfce4-panel

%description
A timer for the Xfce panel. It supports countdown periods and alarms at 
certain times.

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
%doc AUTHORS ChangeLog
%license COPYING
%{_libdir}/xfce4/panel/plugins/libxfcetimer*
%{_datadir}/xfce4/panel/plugins/xfce4-timer-plugin.desktop
%{_datadir}/icons/hicolor/*/apps/xfce4-timer-plugin.*g

%changelog
%autochangelog
