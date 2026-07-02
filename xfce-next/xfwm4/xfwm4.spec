%global xfceversion 4.20

Name:           xfwm4
Version:        4.20.0
Release:        %autorelease
Summary:        Next generation window manager for Xfce

# Automatically converted from old format: GPLv2+ - review is highly recommended.
License:        GPL-2.0-or-later
URL:            http://www.xfce.org/
#VCS git:git://git.xfce.org/xfce/xfwm4
Source0:        https://gitlab.xfce.org/xfce/xfwm4/-/archive/master/xfwm4-master.tar.gz

BuildRequires:  make
BuildRequires:  meson
BuildRequires:  ninja-build
BuildRequires:  gcc-c++
BuildRequires:  libxfce4ui-devel >= %{xfceversion}
BuildRequires:  libXext-devel
%if 0%{?fedora}
BuildRequires:  libXpresent-devel
%endif
BuildRequires:  gettext
BuildRequires:  intltool
BuildRequires:  libXcomposite-devel
BuildRequires:  libXdamage-devel
BuildRequires:  startup-notification-devel >= 0.5
BuildRequires:  libwnck3-devel >= 3.14
BuildRequires:  xfconf-devel >= %{xfceversion}
BuildRequires:  desktop-file-utils

Provides:       firstboot(windowmanager) = xfwm4

%description
xfwm4 is a window manager compatible with GNOME, GNOME2, KDE2, KDE3 and Xfce.

%prep
%setup -q -c
shopt -s dotglob
mv */* . 2>/dev/null || :

%build
export export CFLAGS="%{optflags} -DSHOW_POSITION"
  %meson
  %meson_build

%install
  %meson_install

%find_lang %{name}

for file in %{buildroot}/%{_datadir}/applications/*.desktop; do
    desktop-file-validate $file
done

%files -f %{name}.lang
%license COPYING
%doc example.gtkrc-2.0 TODO AUTHORS COMPOSITOR
%{_bindir}/xfwm4
%{_bindir}/xfwm4-settings
%{_bindir}/xfwm4-tweaks-settings
%{_bindir}/xfwm4-workspace-settings
%{_datadir}/applications/*.desktop
%{_datadir}/icons/hicolor/*/*/*
%{_datadir}/xfwm4
%{_datadir}/themes/*
%dir %{_libdir}/xfce4/xfwm4/
%{_libdir}/xfce4/xfwm4/helper-dialog

%changelog
%autochangelog
