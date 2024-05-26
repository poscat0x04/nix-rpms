Name:           aws-c-io
Version:        0.14.8
Release:        %autorelease
Summary:        AWS SDK module to handle all IO and TLS work for application protocols
License:        Apache-2.0
URL:            https://github.com/awslabs/%{name}
Source0:        %{url}/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz

BuildRequires:  aws-c-cal-devel
BuildRequires:  aws-c-common-devel
BuildRequires:  s2n-tls-devel
BuildRequires:  cmake
BuildRequires:  gcc

%description
This is a module for the Amazon Web Services (AWS) SDK for C. It handles all
I/O and TLS work for application protocols.


%package devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       aws-c-cal-devel
Requires:       aws-c-common-devel
Requires:       s2n-tls-devel

%description devel
This package contains the header files, libraries and cmake supplementals
needed to develop applications that use aws-c-io.


%prep
%autosetup
sed -i 's|\${PROJECT_NAME}/cmake|cmake/${PROJECT_NAME}|g' CMakeLists.txt


# tests require network access
%build
%cmake -DBUILD_TESTING:BOOL=FALSE
%cmake_build


%install
%cmake_install


%files
%license LICENSE
%doc README.md
%{_libdir}/libaws-c-io.so.*


%files devel
%{_libdir}/libaws-c-io.so
%{_libdir}/cmake/%{name}
%{_includedir}/aws/{io,testing}


%changelog
%autochangelog
