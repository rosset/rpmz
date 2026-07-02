# Review: https://bugzilla.redhat.com/show_bug.cgi?id=173105

%global minorversion 0.11

%global xfceversion 4.16

Name:           xfce4-weather-plugin
Version:        0.11.3
Release:        %autorelease
Summary:        Weather plugin for the Xfce panel

# Automatically converted from old format: BSD - review is highly recommended.
License:        LicenseRef-Callaway-BSD
URL:            http://goodies.xfce.org/projects/panel-plugins/%{name}
#VCS: git:git://git.xfce.org/panel-plugins/xfce4-weather-plugin
Source0:        https://gitlab.xfce.org/panel-plugins/xfce4-weather-plugin/-/archive/master/xfce4-weather-plugin-master.tar.gz

BuildRequires:  make
BuildRequires:  meson
BuildRequires:  ninja-build
BuildRequires:  gcc-c++
BuildRequires:  libxfce4ui-devel >= %{xfceversion}
BuildRequires:  xfce4-panel-devel >= %{xfceversion}
BuildRequires:  libsoup-devel >= 2.26.0
BuildRequires:  upower-devel >= 0.9.0
BuildRequires:  gettext
BuildRequires:  intltool
BuildRequires:  libxml2-devel >= 2.4.0
BuildRequires:  json-c-devel
Requires:       xfce4-panel >= %{xfceversion}

%description
A weather plugin for the Xfce panel. It shows the current temperature and 
weather condition, using weather data provided by xoap.weather.com.

%prep
%setup -q -c
shopt -s dotglob
mv */* . 2>/dev/null || :

%build
  %meson
  %meson_build

%install
  %meson_install

# remove la file
find %{buildroot} -name '*.la' -exec rm -f {} ';'

# make sure debuginfo is generated properly
chmod -c +x %{buildroot}%{_libdir}/xfce4/panel/plugins/*.so

%find_lang %{name}

%files -f %{name}.lang
%license COPYING
%doc AUTHORS ChangeLog README
%{_libdir}/xfce4/panel/plugins/*.so
%{_datadir}/xfce4/panel/plugins/*.desktop
%{_datadir}/icons/hicolor/*/*/*
%{_datadir}/xfce4/weather

%changelog
%autochangelog
