Name:           mdbook-linkcheck
Version:        0.7.7
Release:        %autorelease
Summary:        A backend for mdbook which will check your links for you

License:        MIT
URL:            https://github.com/Michael-F-Bryan/mdbook-linkcheck
Source0:        %{url}/releases/download/v%{version}/mdbook-linkcheck.x86_64-unknown-linux-gnu.zip

%description
A backend for mdbook which will check your links for you
For use alongside the built-in HTML renderer


%prep
unzip %{SOURCE0}
chmod +x mdbook-linkcheck


%build


%install
install -Dm755 mdbook-linkcheck %{buildroot}%{_bindir}/mdbook-linkcheck


%check


%files
%license LICENSE
%doc README.md
%{_bindir}/mdbook-linkcheck


%changelog
%autochangelog
