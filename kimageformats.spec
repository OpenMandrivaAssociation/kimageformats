%define major 5
%define stable %([ "`echo %{version} |cut -d. -f3`" -ge 80 ] && echo -n un; echo -n stable)

Name: kimageformats
Version:	5.99.0
Release:	5
Source0: http://download.kde.org/%{stable}/frameworks/%(echo %{version} |cut -d. -f1-2)/%{name}-%{version}.tar.xz
Source10: imageformat-package
Source20: %{name}.rpmlintrc
Patch0: kimageformats-5.99.0-libavif-0.11.patch
Patch1: https://invent.kde.org/frameworks/kimageformats/-/commit/350ce1b990460cb2178f369f22fe80803f5645f3.patch
Patch2: https://invent.kde.org/frameworks/kimageformats/-/commit/1190e53e9b69da6f9663ceb75c4813c5708b7cbd.patch
Summary: Qt5 support for handling various additional image formats
URL: http://kde.org/
License: GPL
Group: System/Libraries
BuildRequires: pkgconfig(Qt5Core)
BuildRequires: pkgconfig(Qt5Widgets)
BuildRequires: pkgconfig(Qt5PrintSupport)
BuildRequires: pkgconfig(Qt5Test)
BuildRequires: cmake(ECM)
BuildRequires: cmake(KF5Archive)
BuildRequires: pkgconfig(jasper)
BuildRequires: pkgconfig(OpenEXR)
BuildRequires: pkgconfig(libavif)
BuildRequires: pkgconfig(zlib)
BuildRequires: pkgconfig(libjxl)
BuildRequires: pkgconfig(libraw)
BuildRequires: pkgconfig(libopenjp2)
Requires: %{name}-ani = %{EVRD}
Requires: %{name}-avif = %{EVRD}
Requires: %{name}-dds = %{EVRD}
Requires: %{name}-eps = %{EVRD}
Requires: %{name}-exr = %{EVRD}
Requires: %{name}-hdr = %{EVRD}
Requires: %{name}-jp2 = %{EVRD}
Requires: %{name}-jxl = %{EVRD}
Requires: %{name}-pcx = %{EVRD}
Requires: %{name}-pic = %{EVRD}
Requires: %{name}-psd = %{EVRD}
Requires: %{name}-ras = %{EVRD}
Requires: %{name}-raw = %{EVRD}
Requires: %{name}-rgb = %{EVRD}
Requires: %{name}-tga = %{EVRD}
Requires: %{name}-xcf = %{EVRD}

%description
Qt5 support for handling various additional image formats.

%{expand:%(sh %{SOURCE10} ani)}
%{expand:%(sh %{SOURCE10} avif)}
%{expand:%(sh %{SOURCE10} dds)}
%{expand:%(sh %{SOURCE10} eps)}
%{expand:%(sh %{SOURCE10} exr)}
%{expand:%(sh %{SOURCE10} hdr)}
%{expand:%(sh %{SOURCE10} jp2)}
%{expand:%(sh %{SOURCE10} jxl)}
%{expand:%(sh %{SOURCE10} kra)}
%{expand:%(sh %{SOURCE10} pcx)}
%{expand:%(sh %{SOURCE10} pic)}
%{expand:%(sh %{SOURCE10} psd)}
%{expand:%(sh %{SOURCE10} ora)}
%{expand:%(sh %{SOURCE10} ras)}
%{expand:%(sh %{SOURCE10} raw)}
%{expand:%(sh %{SOURCE10} rgb)}
%{expand:%(sh %{SOURCE10} tga)}
%{expand:%(sh %{SOURCE10} xcf)}

%prep
%autosetup -p1
%cmake_kde5

%build
%ninja -C build

%install
%ninja_install -C build

%files
