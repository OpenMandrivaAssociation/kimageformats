%define major 5
%define debug_package %{nil}
%define stable %([ "`echo %{version} |cut -d. -f3`" -ge 80 ] && echo -n un; echo -n stable)

Name: kimageformats
Version:	5.67.0
Release:	3
Source0: http://download.kde.org/%{stable}/frameworks/%(echo %{version} |cut -d. -f1-2)/%{name}-%{version}.tar.xz
Source10: imageformat-package
Source20: %{name}.rpmlintrc
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
Requires: %{name}-dds = %{EVRD}
Requires: %{name}-eps = %{EVRD}
Requires: %{name}-exr = %{EVRD}
Requires: %{name}-hdr = %{EVRD}
Requires: %{name}-jp2 = %{EVRD}
Requires: %{name}-pcx = %{EVRD}
Requires: %{name}-pic = %{EVRD}
Requires: %{name}-psd = %{EVRD}
Requires: %{name}-ras = %{EVRD}
Requires: %{name}-rgb = %{EVRD}
Requires: %{name}-tga = %{EVRD}
Requires: %{name}-xcf = %{EVRD}

%description
Qt5 support for handling various additional image formats.

%{expand:%(sh %{SOURCE10} dds)}
%{expand:%(sh %{SOURCE10} eps)}
%{expand:%(sh %{SOURCE10} exr)}
%{expand:%(sh %{SOURCE10} hdr)}
%{expand:%(sh %{SOURCE10} jp2)}
%{expand:%(sh %{SOURCE10} kra)}
%{expand:%(sh %{SOURCE10} pcx)}
%{expand:%(sh %{SOURCE10} pic)}
%{expand:%(sh %{SOURCE10} psd)}
%{expand:%(sh %{SOURCE10} ora)}
%{expand:%(sh %{SOURCE10} ras)}
%{expand:%(sh %{SOURCE10} rgb)}
%{expand:%(sh %{SOURCE10} tga)}
%{expand:%(sh %{SOURCE10} xcf)}

%prep
%setup -q
%cmake_kde5

%build
%ninja -C build

%install
%ninja_install -C build

%files
