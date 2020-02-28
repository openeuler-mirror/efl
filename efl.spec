Name:             efl
Version:          1.21.0
Release:          3
Summary:          Collection of Enlightenment libraries
License:          BSD and LGPLv2+ and GPLv2 and zlib
URL:              http://enlightenment.org/
Source0:          http://download.enlightenment.org/rel/libs/efl/efl-%{version}.tar.xz
Patch0001:        efl-1.21.0-use-pragma-to-ignore-safe-printf.patch
BuildRequires:    gcc-c++
BuildRequires:    bullet-devel libpng-devel libjpeg-devel gstreamer1-devel zlib-devel
BuildRequires:    gstreamer1-plugins-base-devel libtiff-devel openssl-devel
BuildRequires:    curl-devel dbus-devel glibc-devel fontconfig-devel freetype-devel
BuildRequires:    fribidi-devel pulseaudio-libs-devel libsndfile-devel libX11-devel
BuildRequires:    libXau-devel libXcomposite-devel libXdamage-devel libXdmcp-devel
BuildRequires:    libXext-devel libXfixes-devel libXinerama-devel libXrandr-devel
BuildRequires:    libXrender-devel libXScrnSaver-devel libXtst-devel libXcursor-devel
BuildRequires:    libXp-devel libXi-devel mesa-libGL-devel mesa-libEGL-devel
BuildRequires:    libblkid-devel libmount-devel systemd-devel harfbuzz-devel
BuildRequires:    libwebp-devel tslib-devel SDL2-devel SDL-devel c-ares-devel
BuildRequires:    libxkbcommon-devel uuid-devel libxkbcommon-x11-devel
BuildRequires:    pkgconfig(poppler-cpp) >= 0.12 pkgconfig(libspectre) pkgconfig(libraw)
BuildRequires:    pkgconfig(librsvg-2.0) >= 2.14.0 pkgconfig(cairo) >= 1.0.0 ibus-devel
BuildRequires:    doxygen systemd giflib-devel openjpeg2-devel libdrm-devel
BuildRequires:    mesa-libwayland-egl-devel libwayland-client-devel >= 1.11.0
BuildRequires:    libwayland-cursor-devel libwayland-server-devel wayland-protocols-devel >= 1.7
BuildRequires:    autoconf automake libtool gettext-devel mesa-libGLES-devel
BuildRequires:    mesa-libgbm-devel libinput-devel lua-devel cmake
Provides:         e_dbus = %{version}-%{release} ecore = %{version}-%{release} edje = %{version}-%{release}
Provides:         eet = %{version}-%{release} eeze = %{version}-%{release} efreet = %{version}-%{release}
Provides:         eina = %{version}-%{release} eio = %{version}-%{release} eldbus = %{version}-%{release}
Provides:         elementary = %{version}-%{release} elocation = %{version}-%{release} elua = %{version}-%{release}
Provides:         embryo = %{version}-%{release} emotion = %{version}-%{release} eo = %{version}-%{release}
Provides:         eolian = %{version}-%{release} ephysics = %{version}-%{release} ethumb = %{version}-%{release}
Provides:         evas = %{version}-%{release} evas-generic-loaders = %{version}-%{release} libeina = %{version}-%{release}
Obsoletes:        e_dbus <= 1.7.10 ecore <= 1.7.10 edje <= 1.7.10 eet <= 1.7.10 eeze <= 1.7.10
Obsoletes:        efreet <= 1.7.10 eio <= 1.7.10 elementary <= 1.17.1 embryo <= 1.7.10 emotion <= 1.7.10
Obsoletes:        ethumb <= 1.7.10 evas <= 1.7.10 evas-generic-loaders <= 1.17.0 libeina <= 1.7.10

%description
Enlightenment Foundation Libraries, or EFL, are the set of libraries
used to create the Enlightenment Window Manager DR17 (E17). This set
of libraries is not restricted to X11 as Enlightenment WM itself.

%package          devel
Summary:          Development files for the EFL library
Requires:         efl = %{version}-%{release} pkgconfig, libX11-devel
Requires(post):   systemd
Requires(preun):  systemd
Requires(postun): systemd
Provides:         e_dbus-devel = %{version}-%{release} ecore-devel = %{version}-%{release} edje-devel = %{version}-%{release}
Provides:         eet-devel = %{version}-%{release} eeze-devel = %{version}-%{release} efreet-devel = %{version}-%{release}
Provides:         eio-devel = %{version}-%{release} eldbus-devel = %{version}-%{release} elementary-devel = %{version}-%{release}
Provides:         elocation-devel = %{version}-%{release} embryo-devel = %{version}-%{release} emotion-devel = %{version}-%{release}
Provides:         eo-devel = %{version}-%{release} eolian-devel = %{version}-%{release} ephysics-devel = %{version}-%{release}
Provides:         ethumb-devel = %{version}-%{release} evas-devel = %{version}-%{release} libeina-devel = %{version}-%{release}
Obsoletes:        e_dbus-devel <= 1.7.10 ecore-devel <= 1.7.10 edje-devel <= 1.7.10 eet-devel <= 1.7.10 eeze-devel <= 1.7.10
Obsoletes:        efreet-devel <= 1.7.10 eio-devel <= 1.7.10 elementary-devel <= 1.17.1 embryo-devel <= 1.7.10 emotion-devel <= 1.7.10
Obsoletes:        ethumb-devel <= 1.7.10 evas-devel <= 1.7.10 libeina-devel <= 1.7.10

%description devel
The efl-devel package includes header files and libraries necessary
for the efl library.

%prep
%autosetup -n %{name}-%{version} -p1
autoreconf -ifv
sed -i -e 's|/opt/efl-%{version}/share/|%{_datadir}/|' data/libeo.so.%{version}-gdb.py

%build
%configure --enable-xinput22 --enable-systemd --enable-image-loader-webp --enable-harfbuzz --enable-sdl --enable-ibus --disable-scim \
    --enable-i-really-know-what-i-am-doing-and-that-this-will-probably-break-things-and-i-will-fix-them-myself-and-send-patches-abb \
    --enable-fb --enable-wayland --enable-elput --enable-drm --enable-drm-hw-accel --with-opengl=full --disable-cocoa \
    --with-profile=release --disable-neon --enable-lua-old --with-systemdunitdir=%{_userunitdir}
%make_build V=1

%install
%make_install
sed -i 's|ecore_sdl|ecore-sdl|g' %{buildroot}%{_libdir}/pkgconfig/elementary.pc
sed -i 's|ecore_sdl|ecore-sdl|g' %{buildroot}%{_libdir}/pkgconfig/elementary-cxx.pc
chmod 644 src/bin/edje/edje_cc_out.c
%delete_la
%find_lang %{name}

%post
/sbin/ldconfig
%systemd_user_post ethumb.service

%postun
/sbin/ldconfig
%systemd_user_postun ethumb.service

%preun
%systemd_user_preun ethumb.service

%files -f %{name}.lang
%doc COPYING licenses/COPYING.BSD licenses/COPYING.GPL licenses/COPYING.LGPL licenses/COPYING.SMALL
%doc AUTHORS COMPLIANCE NEWS README
%{_libdir}/libe*.so.*
%{_libdir}/e*
%{_bindir}/diffeet
%{_bindir}/ecore_evas_convert
%{_bindir}/edje*
%{_bindir}/ee*
%{_bindir}/efreetd
%{_bindir}/efl_debug*
%{_bindir}/eina_btlog
%{_bindir}/eina_modinfo
%{_bindir}/el*
%{_bindir}/embryo_cc
%{_bindir}/eo*
%{_bindir}/ethumb*
%{_bindir}/evas_*
%{_bindir}/vieet
%attr(0755,root,root) %caps(cap_audit_write,cap_chown,cap_setuid,cap_sys_admin=pe) %{_bindir}/eeze_scanner
%dir %{_datadir}/dbus-1/
%dir %{_datadir}/dbus-1/services/
%{_datadir}/applications/elementary*.desktop
%{_datadir}/dbus-1/services/org.enlightenment.Ethumb.service
%{_datadir}/ecore*
%{_datadir}/elementary/
%{_datadir}/ethumb*
%{_datadir}/evas/
%{_datadir}/gdb/auto-load/%{_libdir}/libeo.so.1*
%{_datadir}/icons/Enlightenment-X/
%{_datadir}/icons/hicolor/*/apps/elementary.png
%{_datadir}/mime/packages/edje.xml
%{_userunitdir}/ethumb.service
%exclude %{_datadir}/elua/

%files devel
%{_includedir}/*
%{_bindir}/efl_wl_test*
%{_bindir}/eina-bench-cmp
%{_libdir}/cmake/*
%{_libdir}/libe*.so
%{_libdir}/pkgconfig/*
%{_datadir}/edje
%{_datadir}/eeze/
%{_datadir}/efreet/
%{_datadir}/em*
%{_datadir}/eo*
%exclude %{_libdir}/cmake/Elua/

%changelog
* Fri Dec 06 2019 gulining<gulining1@huawei.com> - 1.21.0-3
- Pakcage init
