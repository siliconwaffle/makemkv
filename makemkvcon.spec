%global __strip /bin/true
%global debug_package %{nil}

Name:           makemkvcon
Version:        1.17.7
Release:        %autorelease
Summary:        MakeMKV console application
ExclusiveArch:  %{arm} %{arm64} %{ix86} %{x86_64}

License:        GPL-2.0-only WITH Classpath-exception-2.0 AND GuinpinSoft Inc EULA
URL:            https://www.makemkv.com
# Run verify-makemkv first to verify the hash and sig of the tarball.
# Verification script used because the tarball is distributed with a signed hash, rather than being a signed tarball.
Source0:        %{url}/download/makemkv-bin-%{version}.tar.gz
Source1:        https://salsa.debian.org/BenTheTechGuy/makemkv-bin/-/raw/debian/master/debian/%{name}.1

BuildRequires:  make
Recommends:     ccextractor
# Java is required for some functionality, but I'm not sure what.
Recommends:     java-1.8.0
# Required to read(and conversely to rip) DVDs.
Recommends:     mmgplsrv

%description
Command-line options for MakeMKV.

%prep
%autosetup -n makemkv-bin-%{version}

%build
%__mkdir tmp
%{echo:accepted} > tmp/eula_accepted
%make_build

%install
%make_install
%__install -Dm 644 %{SOURCE1} %{buildroot}%{_mandir}/man1/%{name}.1

%files
%license src/eula_en_linux.txt
%{_bindir}/%{name}
%{_bindir}/sdftool
%dir %{_datadir}/MakeMKV
%{_datadir}/MakeMKV/appdata.tar
%{_datadir}/MakeMKV/blues.jar
%{_datadir}/MakeMKV/blues.policy
%{_mandir}/man1/%{name}.1*

%changelog
* Wed Mar 20 2024 Release <siliconwaffle@trilbyproject.org> - 1.17.7-1
- Initial RPM release
