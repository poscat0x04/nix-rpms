%global __brp_check_rpaths %{nil}
%global selinuxtype targeted
%global modulename nix

Name:           nix
Version:        2.23.0
Release:        1%{?dist}
Summary:        A purely functional package manager

License:        LGPL-2.1-or-later
URL:            https://github.com/NixOS/nix
Source0:        %{URL}/archive/refs/tags/%{VERSION}.tar.gz
Source1:        nix.sysusers
Source2:        nix.user.tmpfiles
Source3:        nix.tmpfiles
Source4:        nix.te
Source5:        nix.fc
Source6:        nix.conf
Source7:        99-build-dir.conf

BuildRequires:  gcc-c++
BuildRequires:  autoconf-archive
BuildRequires:  automake
BuildRequires:  bison
BuildRequires:  flex
BuildRequires:  graphviz
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
BuildRequires:  libseccomp-devel >= 2.5.5

%if "%{?__isa}" == "x86-64"
BuildRequires:  libcpuid-devel
%endif

BuildRequires:  libsodium-devel
BuildRequires:  libgit2-devel
BuildRequires:  lowdown-devel
BuildRequires:  json-devel
BuildRequires:  sqlite-devel

# selinux macros
BuildRequires:  selinux-policy
# selinux policy
BuildRequires:  checkpolicy
BuildRequires:  policycoreutils

Requires:       %{name}-libs = %{version}-%{release}
Requires:       (%{name}-selinux = %{version}-%{release} if selinux-policy-%{selinuxtype})
Requires:       busybox-nix

Requires(post):  systemd
Requires(preun): systemd

Recommends:     %{name}-docs = %{version}-%{release}

%description
A powerful package manager for Linux and other Unix systems
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


%package docs
Summary:        Nix reference manual

%description docs
Reference manual for Nix


%package selinux
Summary:        SELinux policies for Nix
Requires:       selinux-policy-%{selinuxtype}
Requires(post): selinux-policy-%{selinuxtype}
Requires(post): selinux-policy-base >= 40.20
Requires(post): libselinux-utils
Requires(post): policycoreutils
Requires(post): policycoreutils-python-utils

%description selinux
SELinux policy modules for Nix


%prep
%autosetup
cp COPYING LICENSE


%build
#build selinux policy
checkmodule -M -m -c 5 -o %{modulename}.mod %{SOURCE4}
semodule_package -o %{modulename}.pp -m %{modulename}.mod -f %{SOURCE5}

#build nix
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
rm -rf %{buildroot}%{_sysconfdir}/init
install -Dm644 %{SOURCE1} %{buildroot}%{_sysusersdir}/nix.conf
install -Dm644 %{SOURCE2} %{buildroot}%{_user_tmpfilesdir}/nix.conf
install -Dm644 %{SOURCE3} %{buildroot}%{_tmpfilesdir}/nix.conf
install -Dm644 %{modulename}.pp %{buildroot}%{_datadir}/selinux/packages/%{selinuxtype}/%{modulename}.pp
install -Dm644 %{SOURCE6} %{buildroot}%{_sysconfdir}/nix/nix.conf
install -Dm644 %{SOURCE7} %{buildroot}%{_unitdir}/nix-daemon.service.d/99-build-dir.conf


%check


%files
%license LICENSE
%doc README.md

%config(noreplace) %{_sysconfdir}/nix/nix.conf
%{_sysconfdir}/profile.d/nix*sh

%{_bindir}/nix*
%{_libexecdir}/nix/build-remote

%{_unitdir}/nix-daemon.{service,service.d,socket}
%{_tmpfilesdir}/nix.conf
%{_user_tmpfilesdir}/nix.conf
%{_sysusersdir}/nix.conf

%{bash_completions_dir}/nix
%{fish_completions_dir}/nix.fish
%{zsh_completions_dir}/{_nix,run-help-nix}

%{_mandir}/man1/nix*.gz
%{_mandir}/man5/nix*.gz
%{_mandir}/man8/nix*.gz


%files libs
%license LICENSE
%{_libdir}/libnix*.so


%files docs
%{_docdir}/nix/manual


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
