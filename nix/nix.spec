%global __brp_check_rpaths %{nil}
%global selinuxtype targeted
%global modulename nix

Name:           nix
Version:        2.21.2
Release:        %autorelease
Summary:        Nix, the purely functional package manager

License:        LGPL-2.1-or-later
URL:            https://github.com/NixOS/nix
Source0:        %{URL}/archive/refs/tags/%{VERSION}.tar.gz
Source1:        nix.sysusers
Source2:        nix.user.tmpfiles
Source3:        nix.tmpfiles
# selinux policy module
Source4:        https://github.com/DeterminateSystems/nix-installer/raw/main/src/action/linux/selinux/nix.pp

BuildRequires:  gcc-c++
BuildRequires:  autoconf-archive
BuildRequires:  automake
BuildRequires:  bison
BuildRequires:  flex
BuildRequires:  jq
BuildRequires:  mdbook
BuildRequires:  mdbook-linkcheck
BuildRequires:  lowdown

BuildRequires:  systemd-rpm-macros

BuildRequires:  gmock-devel
BuildRequires:  gtest-devel
BuildRequires:  rapidcheck-devel

BuildRequires:  aws-sdk-cpp-devel
BuildRequires:  aws-crt-cpp-devel
BuildRequires:  boost-devel
BuildRequires:  brotli-devel
BuildRequires:  busybox-nix
BuildRequires:  editline-devel
BuildRequires:  gc-devel >= 8.2.5
BuildRequires:  libarchive-devel
BuildRequires:  libcurl-devel
BuildRequires:  libseccomp-devel

%if "%{?__isa}" == "x86-64"
BuildRequires:  libcpuid-devel
%endif

BuildRequires:  libsodium-devel
BuildRequires:  libgit2-devel
BuildRequires:  json-devel
BuildRequires:  sqlite-devel

# selinux macros
BuildRequires:  selinux-policy

Requires:       %{name}-libs = %{version}-%{release}
Requires:       (%{name}-selinux = %{version}-%{release} if selinux-policy-%{selinuxtype})

Requires(post):  systemd
Requires(preun): systemd

%description
Nix is a powerful package manager for Linux and other Unix systems
that makes package management reliable and reproducible.


%package libs
Summary:        Library files for %{name}

%description libs
Library files for %{name}


%package devel
Summary:        Development files for %{name}
Requires:       %{name}-libs = %{version}-%{release}

%description devel
Header files, libraries and pkg-config files for %{name}-libs


%package selinux
Summary:        SELinux policies for Nix
Requires:       selinux-policy-%{selinuxtype}
Requires(post): selinux-policy-%{selinuxtype}
%{?selinux_requires}

%description selinux
SELinux policy modules for Nix



%prep
%autosetup
cp COPYING LICENSE


%build
autoreconf -vfi
%configure \
--prefix=%{_prefix} \
--libexecdir=%{_libexecdir} \
--sysconfdir=%{_sysconfdir} \
--localstatedir=%{_localstatedir} \
--with-sandbox-shell=%{_libexecdir}/nix/busybox \
--enable-gc \
--enable-lto \
--enable-static=rapidcheck
%make_build


%install
%make_install
rm %{buildroot}%{_docdir}/nix/manual/.nojekyll
rm %{buildroot}%{_tmpfilesdir}/nix-daemon.conf
install -Dm644 %{SOURCE1} %{buildroot}%{_sysusersdir}/nix.conf
install -Dm644 %{SOURCE2} %{buildroot}%{_user_tmpfilesdir}/nix.conf
install -Dm644 %{SOURCE3} %{buildroot}%{_tmpfilesdir}/nix.conf
install -Dm644 %{SOURCE4} %{buildroot}%{_datadir}/selinux/packages/%{selinuxtype}/%{modulename}.pp


%check


%files
%license LICENSE
%doc README.md

%config(noreplace) /etc/init/nix-daemon.conf
%{_sysconfdir}/profile.d/nix*sh

%{_bindir}/nix*
%{_libexecdir}/nix/build-remote

%{_unitdir}/nix-daemon.{service,socket}
%{_tmpfilesdir}/nix.conf
%{_user_tmpfilesdir}/nix.conf
%{_sysusersdir}/nix.conf

%{bash_completions_dir}/nix
%{fish_completions_dir}/nix.fish
%{zsh_completions_dir}/{_nix,run-help-nix}

%{_docdir}/nix
%{_mandir}/man1/nix*.gz
%{_mandir}/man5/nix*.gz
%{_mandir}/man8/nix*.gz


%files libs
%license LICENSE
%{_libdir}/libnix*.so


%files devel
%{_libdir}/pkgconfig/nix*.pc
%{_includedir}/nix

%files selinux
%{_datadir}/selinux/packages/%{selinuxtype}/%{modulename}.pp


%post
# create users and directories
%sysusers_create_package nix %{SOURCE1}
%tmpfiles_create_package nix %{SOURCE3}
# load units
%systemd_post nix-daemon.service nix-daemon.socket


%preun
%systemd_preun nix-daemon.service nix-daemon.socket


%pre selinux
%selinux_relabel_pre -s %{selinuxtype}


%post selinux
%selinux_modules_install -s %{selinuxtype} %{_datadir}/selinux/packages/%{selinuxtype}/%{modulename}.pp


%postun selinux
if [ $1 -eq 0 ]; then
    %selinux_modules_uninstall -s %{selinuxtype} %{modulename}
fi


%posttrans selinux
%selinux_relabel_post -s %{selinuxtype}


%changelog
%autochangelog
