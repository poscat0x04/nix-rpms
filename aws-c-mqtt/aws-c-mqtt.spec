Name:           aws-c-mqtt
Version:        0.10.4
Release:        %autorelease
Summary:        C99 implementation of the MQTT 3.1.1 specification

License:        Apache-2.0
URL:            https://github.com/awslabs/%{name}
Source0:        %{url}/archive/v%{version}/%{name}-%{version}.tar.gz

BuildRequires:  aws-c-common-devel
BuildRequires:  aws-c-http-devel
BuildRequires:  cmake
BuildRequires:  gcc

ExcludeArch: s390x

%description
C99 implementation of the MQTT 3.1.1 specification


%package devel
Summary:        C99 implementation of the MQTT 3.1.1 specification
Requires:       aws-c-common-devel
Requires:       aws-c-http-devel
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description devel
This package contains the header files, libraries and cmake supplementals
needed to develop applications that use aws-c-mqtt.


%prep
%autosetup
sed -i 's|\${PROJECT_NAME}/cmake|cmake/${PROJECT_NAME}|g' CMakeLists.txt


%build
%cmake
%cmake_build


%install
%cmake_install


%files
%license LICENSE NOTICE
%doc README.md
%{_libdir}/libaws-c-mqtt.so.1{,.*}
%{_bindir}/{elastipubsub{,5},mqtt5canary}


%files devel
%{_libdir}/libaws-c-mqtt.so
%{_includedir}/aws/mqtt
%{_libdir}/cmake/aws-c-mqtt


%changelog
%autochangelog
