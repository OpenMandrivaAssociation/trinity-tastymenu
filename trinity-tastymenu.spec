%bcond clang 1

# TDE variables
%if "%{?tde_version}" == ""
%define tde_version 14.1.5
%endif

%define tde_pkg tastymenu
%define tde_prefix /opt/trinity

%undefine __brp_remove_la_files
%define dont_remove_libtool_files 1
%define _disable_rebuild_configure 1

# fixes error: Empty %files file …/debugsourcefiles.list
%define _debugsource_template %{nil}

%define tarball_name %{tde_pkg}-trinity


Name:		trinity-%{tde_pkg}
Version:	1.0.8
Release:	%{?tde_version:%{tde_version}_}3
Summary:	Replacement for TMenu
Group:		Applications/Multimedia
URL:		http://www.trinitydesktop.org/

License:	GPLv2+


Source0:		https://mirror.ppa.trinitydesktop.org/trinity/releases/R%{tde_version}/main/applications/system/%{tarball_name}-%{tde_version}.tar.xz

BuildSystem:  cmake

BuildOption:    -DCMAKE_BUILD_TYPE="RelWithDebInfo" 
BuildOption:    -DCMAKE_INSTALL_PREFIX=%{tde_prefix}
BuildOption:    -DSHARE_INSTALL_PREFIX=%{tde_prefix}/share
BuildOption:    -DWITH_ALL_OPTIONS=ON
BuildOption:    -DBUILD_ALL=ON 
BuildOption:    -DBUILD_DOC=ON 
BuildOption:    -DBUILD_TRANSLATIONS=ON 
BuildOption:    -DWITH_GCC_VISIBILITY=%{!?with_clang:ON}%{?with_clang:OFF}

BuildRequires:	trinity-tdelibs-devel >= %{tde_version}
BuildRequires:	trinity-tdebase-devel >= %{tde_version}
BuildRequires:	desktop-file-utils


BuildRequires:	trinity-tde-cmake >= %{tde_version}

%{!?with_clang:BuildRequires:	gcc-c++}

BuildRequires:	pkgconfig
BuildRequires:	libtool

# ACL support
BuildRequires:  pkgconfig(libacl)

# IDN support
BuildRequires:	pkgconfig(libidn)

# OPENSSL support
BuildRequires:  pkgconfig(openssl)


BuildRequires:  pkgconfig(xrender)
BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(ice)
BuildRequires:  pkgconfig(sm)


%description
Tasty Menu is a TMenu replacement aiming to provide the maximum usability and flexibility.


%conf -p
unset QTDIR QTINC QTLIB
export PATH="%{tde_prefix}/bin:${PATH}"
export PKG_CONFIG_PATH="%{tde_prefix}/%{_lib}/pkgconfig"


%install -a
%find_lang %{tde_pkg}


%files -f %{tde_pkg}.lang
%defattr(-,root,root,-)
%{tde_prefix}/%{_lib}/trinity/tastymenu_panelapplet.la
%{tde_prefix}/%{_lib}/trinity/tastymenu_panelapplet.so
%{tde_prefix}/share/apps/kicker/applets/tastymenu.desktop
%{tde_prefix}/share/config.kcfg/tastymenu.kcfg
%{tde_prefix}/share/doc/tde/HTML/en/tastymenu/

