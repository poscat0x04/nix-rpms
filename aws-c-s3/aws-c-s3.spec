Name:           aws-c-s3
Version:        0.5.9
Release:        %autorelease
Summary:        C99 library implementation for communicating with the S3 service

License:        Apache-2.0
URL:            https://github.com/awslabs/%{name}
Source0:        %{url}/archive/v%{version}/%{name}-%{version}.tar.gz

BuildRequires:  aws-checksums-devel
BuildRequires:  aws-c-auth-devel
BuildRequires:  aws-c-common-devel
BuildRequires:  cmake
BuildRequires:  gcc

ExcludeArch: s390x

%description
C99 library implementation for communicating with the S3 service,
designed for maximizing throughput on high bandwidth EC2 instances


%package devel
Summary:        C99 library implementation for communicating with the S3 service
Requires:       aws-c-common-devel
Requires:       aws-c-auth-devel
Requires:       aws-checksums-devel
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description devel
This package contains the header files, libraries and cmake supplementals
needed to develop applications that use aws-c-s3.


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
%{_bindir}/s3
%{_libdir}/libaws-c-s3.so.1{,.*}
%{_libdir}/libaws-c-s3.so.0unstable


%files devel
%{_libdir}/libaws-c-s3.so
%{_includedir}/aws/s3
%{_libdir}/cmake/aws-c-s3/


%changelog
%autochangelog
