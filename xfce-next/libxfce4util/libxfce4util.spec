%global xfceversion 4.20

%global namespc Libxfce4util

Name:           libxfce4util
Version:        4.20.1
Release:        %autorelease
Summary:        Utility library for the Xfce4 desktop environment

# Automatically converted from old format: LGPLv2+ - review is highly recommended.
License:        LicenseRef-Callaway-LGPLv2+
URL:            http://www.xfce.org/
Source0:        https://gitlab.xfce.org/xfce/libxfce4util/-/archive/master/libxfce4util-master.tar.gz
#VCS: git:git://git.xfce.org/xfce/libxfce4util

BuildRequires:  gcc-c++
BuildRequires:  xfce4-dev-tools
BuildRequires:  meson
BuildRequires:  ninja-build
BuildRequires:  pkgconfig(glib-2.0) >= 2.24.0
BuildRequires:  gettext
BuildRequires:  intltool
BuildRequires:  gtk-doc
BuildRequires:  gobject-introspection-devel
BuildRequires:  vala
BuildRequires:  make

%description
This package includes basic utility non-GUI functions for Xfce4.

%package devel
Summary: Developpment tools for libxfce4util library
Requires: %{name} = %{version}-%{release}
Requires: glib2-devel
Requires: gtk3-devel
Requires: pkgconfig

%description devel
This package includes static libraries and header files for the
libxfce4util library.

%prep
%setup -q -c
shopt -s dotglob
mv */* . 2>/dev/null || :
touch ChangeLog

%build
  %meson -Dgtk-doc=true
# Remove rpaths

  %meson_build

%install
  %meson_install

# kevin identified the issue - fixes wrong library permissions
chmod 755 %{buildroot}/%{_libdir}/*.so

rm -f %{buildroot}%{_libdir}/*.la

%find_lang %{name}

%ldconfig_scriptlets

%files -f %{name}.lang
%license COPYING
%doc AUTHORS ChangeLog NEWS
%{_libdir}/lib*.so.*
%{_sbindir}/xfce4-kiosk-query
%{_libdir}/girepository-1.0/%{namespc}-1.0.typelib
%{_datadir}/gir-1.0/%{namespc}-1.0.gir
%{_datadir}/vala/vapi/%{name}-1.0.vapi

%files devel
%{_libdir}/lib*.so
%{_libdir}/pkgconfig/*.pc
%{_includedir}/xfce4
%doc %{_datadir}/gtk-doc/

%changelog
%autochangelog
