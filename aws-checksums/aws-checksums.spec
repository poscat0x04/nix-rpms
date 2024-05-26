Name:           aws-checksums
Version:        0.1.18
Release:        %autorelease
Summary:        Cross-Platform HW accelerated CRC32c and CRC32 implementation

License:        Apache-2.0
URL:            https://github.com/awslabs/%{name}
Source0:        %{url}/archive/v%{version}/%{name}-%{version}.tar.gz

BuildRequires:  aws-c-common-devel
BuildRequires:  cmake
BuildRequires:  gcc

ExcludeArch: s390x

%description
Cross-Platform HW accelerated CRC32c and CRC32
with fallback to efficient SW implementations


%package devel
Summary:        Cross-Platform HW accelerated CRC32c and CRC32 implementation
Requires:       aws-c-common-devel
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description devel
This package contains the header files, libraries and cmake supplementals
needed to develop applications that use aws-checksums.


%prep
%autosetup
sed -i 's|\${PROJECT_NAME}/cmake|cmake/${PROJECT_NAME}|g' CMakeLists.txt


%build
%cmake
%cmake_build


%install
%cmake_install


%files
%license LICENSE
%doc README.md
%{_libdir}/libaws-checksums.so.1{,.*}


%files devel
%{_libdir}/libaws-checksums.so
%{_includedir}/aws/checksums
%{_libdir}/cmake/aws-checksums


%changelog
%autochangelog
