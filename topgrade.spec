%define debug_package %nil

Name:		topgrade
Version:	17.12.1
Release:	1
Summary:	Upgrade all the things

Group:		System/Tools
License:	GPLv3+
URL:		https://github.com/topgrade-rs/topgrade
Source0:	%{url}/archive/v%{version}/%{name}-%{version}.tar.gz

BuildRequires:	rust-packaging
BuildRequires:	cmake
BuildRequires:	clang

%description
Topgrade detects which tools you use and runs the appropriate commands to
update them. Keeping your system up to date usually involves invoking multiple
package managers. This results in big, non-portable shell one-liners saved in
your shell. To remedy this, Topgrade detects which tools you use and runs the
appropriate commands to update them.

%prep
%autosetup
rm -f rust-toolchain.toml

%build
%cargo_build

%install
install -m 0755 -Dp target/release/topgrade %{buildroot}%{_bindir}/topgrade

%files
%license LICENSE
%doc README.md CHANGELOG.md
%{_bindir}/topgrade

%changelog
* Tue Sep 22 2026 Garrus - 17.12.1-1
- Initial build for OpenMandriva Cooker