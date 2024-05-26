Name:           aws-crt-cpp
Version:        0.26.8
Release:        %autorelease
Summary:        C++ wrapper around the aws-c-* libraries

License:        Apache-2.0
URL:            https://github.com/awslabs/%{name}
Source0:        %{url}/archive/v%{version}/%{name}-%{version}.tar.gz

BuildRequires:  aws-c-auth-devel
BuildRequires:  aws-c-common-devel
BuildRequires:  aws-c-event-stream-devel
BuildRequires:  aws-c-http-devel
BuildRequires:  aws-c-mqtt-devel
BuildRequires:  aws-c-s3-devel
BuildRequires:  cmake
BuildRequires:  gcc-c++

ExcludeArch: s390x

%description
C++ wrapper around the aws-c-* libraries. Provides Cross-Platform
Transport Protocols and SSL/TLS implementations for C++


%package devel
Summary:        C++ wrapper around the aws-c-* libraries
Requires:       aws-c-auth-devel
Requires:       aws-c-common-devel
Requires:       aws-c-event-stream-devel
Requires:       aws-c-http-devel
Requires:       aws-c-mqtt-devel
Requires:       aws-c-s3-devel
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description devel
This package contains the header files, libraries and cmake supplementals
needed to develop applications that use aws-crt-cpp.


%prep
%autosetup
sed -i 's|\${PROJECT_NAME}/cmake|cmake/${PROJECT_NAME}|g' CMakeLists.txt


%build
%cmake -DBUILD_DEPS=OFF
%cmake_build


%install
%cmake_install


%files
%license LICENSE NOTICE
%doc README.md
%{_bindir}/{mqtt5_app,mqtt5_canary,elasticurl_cpp}
%{_libdir}/libaws-crt-cpp.so


%files devel
%{_includedir}/aws/crt
%{_includedir}/aws/iot
%{_libdir}/cmake/aws-crt-cpp


%changelog
%autochangelog
