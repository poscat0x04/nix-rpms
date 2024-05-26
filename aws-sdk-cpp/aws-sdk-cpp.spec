Name:           aws-sdk-cpp
Version:        1.11.335
Release:        %autorelease
Summary:        AWS SDK for C++

License:        Apache-2.0
URL:            https://github.com/awslabs/%{name}
Source0:        %{url}/archive/%{version}/%{name}-%{version}.tar.gz
Source1:        toolchain.cmake

BuildRequires:  aws-crt-cpp-devel
BuildRequires:  aws-c-common-devel
BuildRequires:  aws-c-event-stream-devel
BuildRequires:  libcurl-devel
BuildRequires:  openssl-devel
BuildRequires:  pulseaudio-libs-devel
BuildRequires:  zlib-ng-compat-devel
BuildRequires:  cmake
BuildRequires:  gcc-c++

ExcludeArch: s390x

%description
The AWS SDK for C++ provides a modern C++ (version C++ 11 or later)
interface for Amazon Web Services (AWS).


%package devel
Summary:        AWS SDK for C++
Requires:       aws-crt-cpp-devel
Requires:       aws-c-common-devel
Requires:       aws-c-event-stream-devel
Requires:       libcurl-devel
Requires:       openssl-devel
Requires:       pulseaudio-libs-devel
Requires:       zlib-ng-compat-devel
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description devel
This package contains the header files, libraries and cmake supplementals
needed to develop applications that use aws-sdk-cpp.


%prep
%autosetup


%build
%cmake -DBUILD_DEPS=OFF \
       -DCUSTOM_MEMORY_MANAGEMENT=OFF \
       -DCMAKE_TOOLCHAIN_FILE=%{SOURCE1}
%cmake_build


%install
%cmake_install


%files
%license LICENSE
%doc README.md
%{_libdir}/libaws-cpp-sdk-*.so
%{_libdir}/libtesting-resources.so


%files devel
%{_includedir}/aws/*
%{_includedir}/smithy
%{_libdir}/cmake/*
%{_libdir}/pkgconfig/aws-cpp-sdk-*.pc
%{_libdir}/pkgconfig/testing-resources.pc


%changelog
%autochangelog
