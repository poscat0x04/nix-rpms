%define commit ff6af6fc683159deb51c543b065eba14dfcf329b

Name:           rapidcheck
Version:        0
Release:        %autorelease
Summary:        A C++ framework for property based testing

License:        BSD-2-Clause
URL:            https://github.com/emil-e/%{name}
Source0:        %{url}/archive/%{commit}.tar.gz

BuildRequires:  cmake
BuildRequires:  gcc-c++

%description
A C++ framework for property based testing


%package devel
Summary:        A C++ framework for property based testing
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description devel
A C++ framework for property based testing


%prep
%autosetup -n %{name}-%{commit}
sed 's|share/rapidcheck/cmake|${CMAKE_INSTALL_LIBDIR}/cmake/rapidcheck|g' -i CMakeLists.txt


%build
%cmake -DRC_ENABLE_TESTS=OFF -DRC_INSTALL_ALL_EXTRAS=ON
%cmake_build


%install
%cmake_install


%files
%license LICENSE.md
%doc README.md
%{_libdir}/librapidcheck.so


%files devel
%{_includedir}/rapidcheck
%{_includedir}/rapidcheck.h
%{_libdir}/pkgconfig/rapidcheck*.pc
%{_libdir}/cmake/rapidcheck


%changelog
%autochangelog
