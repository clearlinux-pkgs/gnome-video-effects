#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : gnome-video-effects
Version  : 0.5.0
Release  : 8
URL      : https://download.gnome.org/sources/gnome-video-effects/0.5/gnome-video-effects-0.5.0.tar.xz
Source0  : https://download.gnome.org/sources/gnome-video-effects/0.5/gnome-video-effects-0.5.0.tar.xz
Summary  : A collection of GStreamer effects to be used in different GNOME Modules
Group    : Development/Tools
License  : GPL-2.0
Requires: gnome-video-effects-data = %{version}-%{release}
Requires: gnome-video-effects-license = %{version}-%{release}
BuildRequires : buildreq-gnome
BuildRequires : buildreq-meson

%description
Introduction
============
Writing effects is very easy: just create a file with the extion ".effect" and
use the following format for it:

%package data
Summary: data components for the gnome-video-effects package.
Group: Data

%description data
data components for the gnome-video-effects package.


%package dev
Summary: dev components for the gnome-video-effects package.
Group: Development
Requires: gnome-video-effects-data = %{version}-%{release}
Provides: gnome-video-effects-devel = %{version}-%{release}
Requires: gnome-video-effects = %{version}-%{release}

%description dev
dev components for the gnome-video-effects package.


%package license
Summary: license components for the gnome-video-effects package.
Group: Default

%description license
license components for the gnome-video-effects package.


%prep
%setup -q -n gnome-video-effects-0.5.0
cd %{_builddir}/gnome-video-effects-0.5.0
pushd ..
cp -a gnome-video-effects-0.5.0 buildavx2
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1632416625
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=auto "
export FCFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export FFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=auto "
CFLAGS="$CFLAGS" CXXFLAGS="$CXXFLAGS" LDFLAGS="$LDFLAGS" meson --libdir=lib64 --prefix=/usr --buildtype=plain   builddir
ninja -v -C builddir
CFLAGS="$CFLAGS -m64 -march=haswell" CXXFLAGS="$CXXFLAGS -m64 -march=haswell " LDFLAGS="$LDFLAGS -m64 -march=haswell" meson --libdir=lib64/haswell --prefix=/usr --buildtype=plain   builddiravx2
ninja -v -C builddiravx2

%install
mkdir -p %{buildroot}/usr/share/package-licenses/gnome-video-effects
cp %{_builddir}/gnome-video-effects-0.5.0/COPYING %{buildroot}/usr/share/package-licenses/gnome-video-effects/1f199f2dcc0341653fc919334d9c26d0d2098f93
DESTDIR=%{buildroot} ninja -C builddiravx2 install
DESTDIR=%{buildroot} ninja -C builddir install

%files
%defattr(-,root,root,-)

%files data
%defattr(-,root,root,-)
/usr/share/gnome-video-effects/bulge.effect
/usr/share/gnome-video-effects/cartoon.effect
/usr/share/gnome-video-effects/cheguevara.effect
/usr/share/gnome-video-effects/chrome.effect
/usr/share/gnome-video-effects/dicetv.effect
/usr/share/gnome-video-effects/distortion.effect
/usr/share/gnome-video-effects/edgetv.effect
/usr/share/gnome-video-effects/flip.effect
/usr/share/gnome-video-effects/heat.effect
/usr/share/gnome-video-effects/historical.effect
/usr/share/gnome-video-effects/hulk.effect
/usr/share/gnome-video-effects/inversion.effect
/usr/share/gnome-video-effects/kaleidoscope.effect
/usr/share/gnome-video-effects/mauve.effect
/usr/share/gnome-video-effects/mirror.effect
/usr/share/gnome-video-effects/noir.effect
/usr/share/gnome-video-effects/optv.effect
/usr/share/gnome-video-effects/pinch.effect
/usr/share/gnome-video-effects/quarktv.effect
/usr/share/gnome-video-effects/radioactv.effect
/usr/share/gnome-video-effects/revtv.effect
/usr/share/gnome-video-effects/ripple.effect
/usr/share/gnome-video-effects/saturation.effect
/usr/share/gnome-video-effects/sepia.effect
/usr/share/gnome-video-effects/shagadelictv.effect
/usr/share/gnome-video-effects/sobel.effect
/usr/share/gnome-video-effects/square.effect
/usr/share/gnome-video-effects/streaktv.effect
/usr/share/gnome-video-effects/stretch.effect
/usr/share/gnome-video-effects/timedelay.effect
/usr/share/gnome-video-effects/twirl.effect
/usr/share/gnome-video-effects/vertigotv.effect
/usr/share/gnome-video-effects/warptv.effect
/usr/share/gnome-video-effects/xray.effect

%files dev
%defattr(-,root,root,-)
/usr/share/pkgconfig/gnome-video-effects.pc

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/gnome-video-effects/1f199f2dcc0341653fc919334d9c26d0d2098f93
