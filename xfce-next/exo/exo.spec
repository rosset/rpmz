%global xfceversion 4.20

Name:           exo
Version:        4.20.0
Release:        %autorelease
Summary:        Application library for the Xfce desktop environment

# libexo-hal exo-helper mount-notify and exo-mount are all GPLv2+
# everything else is LGPLv2+
# Automatically converted from old format: LGPLv2+ and GPLv2+ - review is highly recommended.
License:        LicenseRef-Callaway-LGPLv2+ AND GPL-2.0-or-later
URL:            http://xfce.org/
Source0:        https://gitlab.xfce.org/xfce/exo/-/archive/master/exo-master.tar.gz

BuildRequires:  libtool
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  xfce4-dev-tools >= 4.20.0
BuildRequires:  gtk-doc
BuildRequires:  gettext
BuildRequires:  perl-URI
BuildRequires:  pkgconfig(glib-2.0) >= 2.24.0
BuildRequires:  pkgconfig(libxfce4util-1.0) >= %{xfceversion}
BuildRequires:  pkgconfig(libxfce4ui-2) >= %{xfceversion}
BuildRequires:  libnotify-devel
BuildRequires:  intltool >= 0.31
BuildRequires:  chrpath
BuildRequires:  desktop-file-utils
BuildRequires:  gobject-introspection-devel
BuildRequires:  make

%description
Extension library for Xfce, targeted at application development.

%package        devel
Summary:        Development tools for exo library
Requires:       %{name} = %{version}-%{release}
Requires:       libxfce4util-devel
Requires:       pkgconfig

%description devel
Development tools and static libraries and header files for the exo library.

%prep
%setup -q -c
shopt -s dotglob
mv */* . 2>/dev/null || :

%build
  autoreconf -vfi
  %configure --disable-static --enable-gtk-doc
  %make_build

%install
  %make_install

find %{buildroot} -type f -name "*.la" -exec rm -f {} ';'

%find_lang exo

%files -f exo.lang
%license COPYING
%doc AUTHORS ChangeLog NEWS THANKS
%{_bindir}/exo-desktop-item-edit
%{_bindir}/exo-open
%{_libdir}/libexo-2.so.0
%{_libdir}/libexo-2.so.0.1.0
%{_datadir}/pixmaps/exo
%{_mandir}/man1/exo-open.1.*

%files devel
%doc %{_datadir}/gtk-doc
%{_includedir}/exo*
%{_libdir}/lib*.so
%{_libdir}/pkgconfig/*.pc

%changelog
%autochangelog
