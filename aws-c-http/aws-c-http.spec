Name:           aws-c-http
Version:        0.8.1
Release:        %autorelease
Summary:        C99 implementation of HTTP/1.1 and HTTP/2 specifications

License:        Apache-2.0
URL:            https://github.com/awslabs/%{name}
Source0:        %{url}/archive/v%{version}/%{name}-%{version}.tar.gz

BuildRequires:  aws-c-common-devel
BuildRequires:  aws-c-compression-devel
BuildRequires:  aws-c-io-devel
BuildRequires:  cmake
BuildRequires:  gcc


%description
C99 implementation of HTTP/1.1 and HTTP/2 specifications


%package devel
Summary:        C99 implementation of the HTTP/1.1 and HTTP/2 specifications
Requires:       aws-c-common-devel
Requires:       aws-c-compression-devel
Requires:       aws-c-io-devel
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description devel
This package contains the header files, libraries and cmake supplementals
needed to develop applications that use aws-c-http.


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
%{_libdir}/libaws-c-http.so.1{,.*}
%{_bindir}/elasticurl


%files devel
%{_libdir}/libaws-c-http.so
%{_includedir}/aws/http
%{_libdir}/cmake/aws-c-http


%changelog
%autochangelog
