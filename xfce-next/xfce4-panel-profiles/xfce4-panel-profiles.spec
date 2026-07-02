%global majorver 1.0
%global app_org_name org.xfce.PanelProfiles

Name:		xfce4-panel-profiles
Version:	1.0.14
Release:	%autorelease
Summary:	A simple application to manage Xfce panel layouts

# Automatically converted from old format: GPLv3 - review is highly recommended.
License:	GPL-3.0-only
URL:		https://git.xfce.org/apps/xfce4-panel-profiles/about/
Source0:        https://gitlab.xfce.org/apps/xfce4-panel-profiles/-/archive/master/xfce4-panel-profiles-master.tar.gz

BuildRequires: make
BuildRequires:  meson
BuildRequires:  ninja-build
BuildRequires:	python3-devel
BuildRequires:	gettext
BuildRequires:	intltool
BuildRequires:	libappstream-glib
BuildRequires:	desktop-file-utils

BuildArch:	noarch

Requires:	xfce4-panel
Requires:	python3-psutil

Provides:	xfpanel-switch = %{version}-%{release}
Obsoletes:	xfpanel-switch <= 1.0.7

%description
A simple application to manage Xfce panel layouts

With the modular Xfce Panel, a multitude of panel layouts can be created. 
This tool makes it possible to backup, restore, import, and export these 
panel layouts.

%prep
%setup -q -c
shopt -s dotglob
mv */* . 2>/dev/null || :

%build
./configure --prefix=%{_prefix}
  %meson_build

%install
  %meson_install

%find_lang %{name}

# fix executable permissions on tarballs
chmod -x %{buildroot}%{_datadir}/%{name}/layouts/*

# get rid of INSTALL and extra license file
rm -f %{buildroot}%{_docdir}/%{name}/INSTALL
rm -f %{buildroot}%{_docdir}/%{name}/COPYING

%check
desktop-file-validate %{buildroot}/%{_datadir}/applications/%{app_org_name}.desktop
appstream-util validate-relax --nonet %{buildroot}%{_datadir}/metainfo/%{app_org_name}.appdata.xml

%files -f %{name}.lang
%license COPYING
%doc NEWS AUTHORS README.md
%{_mandir}/man1/%{name}*
%{_datadir}/%{name}
%{_bindir}/%{name}
%{_datadir}/applications/%{app_org_name}.desktop
%{_datadir}/metainfo/%{app_org_name}.appdata.xml
%{_datadir}/icons/hicolor/*/apps/%{app_org_name}.*

%changelog
%autochangelog
