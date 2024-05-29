%global __strip /bin/true

Name:           makemkv
Version:        1.17.7
Release:        %autorelease
Summary:        DVD and Blu-ray to MKV converter
ExclusiveArch:  %{arm} %{arm64} %{ix86} %{x86_64}

License:        Apache-2.0 AND GPL-1.0-or-later AND LGPL-2.1-or-later
URL:            https://www.makemkv.com
# Run verify-makemkv %%{version} first to verify the hash and sig of the tarball.
# Verification script used because the tarball is distributed with a signed hash, rather than being a signed tarball.
Source0:        %{url}/download/%{name}-oss-%{version}.tar.gz
# Fixes library permissions, upstream notified via email.
# CCExtractor excluded in favor of an upstream, more up-to-date version.
Patch0:         makemkv-fix-makefile.patch

BuildRequires:  desktop-file-utils
BuildRequires:  gcc-c++
BuildRequires:  glibc-devel
BuildRequires:  make
BuildRequires:  pkgconfig(dri)
BuildRequires:  pkgconfig(expat)
BuildRequires:  pkgconfig(libavcodec)
BuildRequires:  pkgconfig(openssl)
BuildRequires:  pkgconfig(Qt5)
BuildRequires:  pkgconfig(zlib)
Requires:       makemkvcon = %{version}

%prep
%autosetup -n %{name}-oss-%{version}

%build
%configure --enable-debug
%make_build

%install
%make_install

%check
desktop-file-validate %{buildroot}%{_datadir}/applications/%{name}.desktop

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

%package -n libdriveio
Summary: MMC drive interrogation library

%description -n libdriveio
%{summary}

%package -n libmakemkv
Summary: Matroska multiplexer library

%description -n libmakemkv
%{summary}

%package -n libmmbd
Version:        1.8.0
Summary:        MakeMKV decryption api
Requires:       makemkvcon = 1.17.7
# Required in order to play Java menus for blu-ray disks on platforms such as vlc.
# Doesn't work with java-headless or any version other than 1.8.0.
Recommends:     java-1.8.0
Recommends:     libbluray-bdj
Conflicts:      libaacs
Conflicts:      libbdplus

%description -n libmmbd
In addition to being an application, MakeMKV provides a simple API that any
application can use to decrypt M2TS/SSIF files from a blu-ray disc (including 4k
UHD discs). This API is implemented as an open-source library called LibMMBD.
The way this library works, it launches a MakeMKV instance in background and
communicates with MakeMKV in order to get decryption keys - so working MakeMKV
is required for the library to function.

All programs that use libbluray library (that list includes VLC, mplayer, mpv,
Kodi, JMC and many more) can use this API for on-the-fly decryption, enabling
direct blu-ray playback. In order to enable this functionality a simple
configuration settings change is required - there is no need to install any sort
of device drivers or virtual drive emulators.

Starting from version 1.15.0 the integration settings of libmmbd can be changed
in MakeMKV preferencs dialog. Depending on the operating system type and version
the API can be enabled either for all programs or per application basis. Please
see the specific OS sub-forum for details.

%package -n mmgplsrv
Summary:        A libdvdnav/libdvdread server used to read DVDs
Provides:       bundled(libdvdnav) = 6.1.1
Provides:       bundled(libdvdread) = 6.1.2

%description -n mmgplsrv
%{summary}

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

%files -n libdriveio
%license License.txt
%{_libdir}/libdriveio.so.*

%files -n libmakemkv
%license License.txt
%{_libdir}/libmakemkv.so.*

%files -n libmmbd
%license License.txt
%{_libdir}/libmmbd.so.*

%files -n mmgplsrv
%license License.txt
%{_bindir}/mmgplsrv

%changelog
* Mon Mar 11 2024 Release <siliconwaffle@trilbyproject.org> - 1.17.7-1
- Initial RPM Release
