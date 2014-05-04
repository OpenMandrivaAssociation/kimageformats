%define major 5
%define debug_package %{nil}

Name: kimageformats
Version: 4.98.0
Release: 1
Source0: http://ftp5.gwdg.de/pub/linux/kde/unstable/frameworks/%{version}/%{name}-%{version}.tar.xz
Source10: imageformat-package
Source20: %{name}.rpmlintrc
Summary: Qt5 support for handling various additional image formats
URL: http://kde.org/
License: GPL
Group: System/Libraries
BuildRequires: cmake
BuildRequires: pkgconfig(Qt5Core)
BuildRequires: pkgconfig(Qt5Widgets)
BuildRequires: qmake5
BuildRequires: extra-cmake-modules5
BuildRequires: pkgconfig(jasper)
BuildRequires: pkgconfig(OpenEXR)

%description
Qt5 support for handling various additional image formats

%{expand:%(sh %{SOURCE10} dds)}
%{expand:%(sh %{SOURCE10} eps)}
%{expand:%(sh %{SOURCE10} exr)}
%{expand:%(sh %{SOURCE10} jp2)}
%{expand:%(sh %{SOURCE10} pcx)}
%{expand:%(sh %{SOURCE10} pic)}
%{expand:%(sh %{SOURCE10} psd)}
%{expand:%(sh %{SOURCE10} ras)}
%{expand:%(sh %{SOURCE10} rgb)}
%{expand:%(sh %{SOURCE10} tga)}
%{expand:%(sh %{SOURCE10} xcf)}

%prep
%setup -q
%cmake -DLIB_INSTALL_DIR=%{_libdir}/qt5

%build
%make -C build

%install
%makeinstall_std -C build
