%global debug_package %{nil}
%global __strip /bin/true

Name:           makemkv
Version:        1.17.6
Release:        1%{?dist}
Summary:        DVD and Blu-ray to MKV converter
ExclusiveArch:  %{arm} %{arm64} %{ix86} %{x86_64}

License:        Apache-2.0 AND GPL-1.0-or-later AND GuinpinSoft Inc EULA AND LGPL-2.1-or-later
URL:            https://www.makemkv.com
Source0:        %{url}/download/%{name}-bin-%{version}.tar.gz
Source1:        %{url}/download/%{name}-oss-%{version}.tar.gz

BuildRequires:  coreutils
BuildRequires:  desktop-file-utils
BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  glibc-devel
BuildRequires:  make
BuildRequires:  pkgconf
BuildRequires:  pkgconfig(dri)
BuildRequires:  pkgconfig(expat)
BuildRequires:  pkgconfig(libavcodec)
BuildRequires:  pkgconfig(openssl)
BuildRequires:  pkgconfig(Qt5)
BuildRequires:  pkgconfig(zlib)
Requires:       makemkvcon = %{version}
Recommends:     java-headless

%description
MakeMKV is your one-click solution to convert video that you own into free and
patents-unencumbered format that can be played everywhere. MakeMKV is a format
converter, otherwise called "transcoder". It converts the video clips from
proprietary (and usually encrypted) disc into a set of MKV files, preserving
most information but not changing it in any way. The MKV format can store
multiple video/audio tracks with all meta-information and preserve chapters.
There are many players that can play MKV files nearly on all platforms, and
there are tools to convert MKV files to many formats, including DVD and Blu-ray
discs.

Additionally MakeMKV can instantly stream decrypted video without intermediate
conversion to wide range of players, so you may watch Blu-ray and DVD discs with
your favorite player on your favorite OS or on your favorite device.

%package libs
Summary:        Libraries required by MakeMKV
Provides:       bundled(libdvdnav) = 6.1.1
Provides:       bundled(libdvdread) = 6.1.2
Provides:       bundled(libebml) = 1.3.10
Provides:       bundled(libmatroska) = 1.5.2

%description libs
This package contains libraries for MakeMKV

%package -n makemkvcon
Summary:        MakeMKV cli
Requires:       makemkv-libs = %{version}

%description -n makemkvcon
This package contains MakeMKV cli tools

%prep
%autosetup -b 0 -n %{name}-bin-%{version}
%autosetup -b 1 -n %{name}-oss-%{version}

%build
cd %{_builddir}/%{name}-oss-%{version}
%configure
%make_build
cd ../%{name}-bin-%{version}
mkdir tmp
echo accepted > tmp/eula_accepted
%make_build

%install
cd %{_builddir}/%{name}-oss-%{version}
%make_install
chmod 0755 %{buildroot}%{_libdir}/*.so.*
cd ../%{name}-bin-%{version}
%make_install

%check
desktop-file-validate %{buildroot}%{_datadir}/applications/%{name}.desktop

%files
%license License.txt
%{_bindir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_iconsdir}/hicolor/16x16/apps/%{name}.png
%{_iconsdir}/hicolor/22x22/apps/%{name}.png
%{_iconsdir}/hicolor/32x32/apps/%{name}.png
%{_iconsdir}/hicolor/64x64/apps/%{name}.png
%{_iconsdir}/hicolor/128x128/apps/%{name}.png
%{_iconsdir}/hicolor/256x256/apps/%{name}.png

%files libs
%license License.txt
%{_libdir}/libdriveio.so.*
%{_libdir}/libmakemkv.so.*
%{_libdir}/libmmbd.so.*

%files -n makemkvcon
%license ../%{name}-bin-%{version}/src/eula_en_linux.txt License.txt
%{_bindir}/makemkvcon
%{_bindir}/mmccextr
%{_bindir}/mmgplsrv
%{_bindir}/sdftool
%dir %{_datadir}/MakeMKV
%{_datadir}/MakeMKV/appdata.tar
%{_datadir}/MakeMKV/blues.jar
%{_datadir}/MakeMKV/blues.policy

%changelog
* Mon Mar 11 2024 Release <siliconwaffle@trilbyproject.org> - 1.17.6-1
- Initial RPM Release
