Name:           busybox-nix
Version:        1.35.0
Release:        %autorelease
Summary:        Busybox for Nix

License:        GPL-2.0-or-later
URL:            https://www.busybox.net
Source0:        %{url}/downloads/busybox-%{version}.tar.bz2
Source1:        https://github.com/sabotage-linux/kernel-headers/releases/download/v4.19.88-2/linux-headers-4.19.88-2.tar.xz
Source2:        config

%define debug_package %{nil}

BuildRequires:  ncurses-devel
BuildRequires:  musl-gcc
BuildRequires:  musl-devel
BuildRequires:  musl-libc-static

%description
Busybox for Nix


%prep
%autosetup -n busybox-%{version}
tar -xvf %{SOURCE1}
cp %{SOURCE2} .config


%build
export KCONFIG_NOTIMESTAMP=1
make V=1 CC="musl-gcc -static" \
EXTRA_CFLAGS="-Ilinux-headers-4.19.88-2/%{_arch}/include %{_hardening_cflags} -fstack-clash-protection" \
CFLAGS_BUSYBOX="-L%{_prefix}/%{_arch}-linux-musl/ %{_hardening_ldflags} -Wl,-z,relro,-z,now" \


%install
install -vDm755 -t %{buildroot}%{_libexecdir}/nix/ busybox


%files
%{_libexecdir}/nix/busybox


%changelog
%autochangelog
