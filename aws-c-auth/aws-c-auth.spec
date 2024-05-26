Name:           aws-c-auth
Version:        0.7.22
Release:        %autorelease
Summary:        C99 library implementation of AWS client-side authentication

License:        Apache-2.0
URL:            https://github.com/awslabs/%{name}
Source0:        %{url}/archive/v%{version}/%{name}-%{version}.tar.gz

BuildRequires:  aws-c-common-devel
BuildRequires:  aws-c-http-devel
BuildRequires:  aws-c-sdkutils-devel
BuildRequires:  cmake
BuildRequires:  gcc

ExcludeArch: s390x

%description
C99 library implementation of AWS client-side authentication:
standard credentials providers and signing


%package devel
Summary:        C99 library implementation of AWS client-side authentication
Requires:       aws-c-common-devel
Requires:       aws-c-http-devel
Requires:       aws-c-sdkutils-devel
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description devel
This package contains the header files, libraries and cmake supplementals
needed to develop applications that use aws-c-auth.


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
%{_libdir}/libaws-c-auth.so.1{,.*}


%files devel
%{_libdir}/libaws-c-auth.so
%{_includedir}/aws/auth
%{_libdir}/cmake/aws-c-auth


%changelog
%autochangelog
