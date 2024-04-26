Name:           hyprpicker
Version:        0.2.0
Release:        1
Summary:        A wlroots-compatible Wayland color picker that does not suck.

License:        BSD-3-Clause
URL:            https://github.com/hyprwm/hyprpicker
Source:         %{url}/archive/v%{version}/%{name}-%{version}.tar.gz

BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  git

BuildRequires:  pkgconfig(cairo)
BuildRequires:  pkgconfig(glesv2)
BuildRequires:  pkgconfig(hyprlang)
BuildRequires:  pkgconfig(libjpeg)
BuildRequires:  pkgconfig(libmagic)
BuildRequires:  pkgconfig(libwebp)
BuildRequires:  pkgconfig(pango)
BuildRequires:  pkgconfig(pangocairo)
BuildRequires:  pkgconfig(wayland-client)
BuildRequires:  pkgconfig(wayland-protocols)
BuildRequires:  pkgconfig(xkbcommon)

%description
A wlroots-compatible Wayland color picker that does not suck.

%prep
%autosetup

%build
rm -rf ./* ./.*
git clone %{url} .
git checkout v%{version}
make protocols
%cmake
%cmake_build

%install
install -m 755 -Dp %{__cmake_builddir}/%{name} %{buildroot}%{_bindir}/%{name}

%files
%license LICENSE
%doc README.md
%{_bindir}/%{name}

%changelog
* Fri Apr 26 2024 Vineel Sai <mail@vineelsai.com> 0.2.0-1
- new package built with tito
