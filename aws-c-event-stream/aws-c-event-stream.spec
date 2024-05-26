Name:           aws-c-event-stream
Version:        0.4.2
Release:        %autorelease
Summary:        C99 implementation of the vnd.amazon.event-stream content-type

License:        Apache-2.0
URL:            https://github.com/awslabs/%{name}
Source0:        %{url}/archive/v%{version}/%{name}-%{version}.tar.gz

BuildRequires:  aws-checksums-devel
BuildRequires:  aws-c-common-devel
BuildRequires:  aws-c-io-devel
BuildRequires:  cmake
BuildRequires:  gcc

ExcludeArch: s390x

%description
C99 implementation of the vnd.amazon.event-stream content-type


%package devel
Summary:        C99 implementation of the vnd.amazon.event-stream content-type
Requires:       aws-checksums-devel
Requires:       aws-c-common-devel
Requires:       aws-c-io
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description devel
This package contains the header files, libraries and cmake supplementals
needed to develop applications that use aws-c-event-stream.


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
%{_libdir}/libaws-c-event-stream.so.1{,.*}


%files devel
%{_libdir}/libaws-c-event-stream.so
%{_includedir}/aws/event-stream
%{_libdir}/cmake/aws-c-event-stream


%changelog
%autochangelog
