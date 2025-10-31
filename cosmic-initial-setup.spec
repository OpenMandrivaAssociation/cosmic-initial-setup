%undefine _debugsource_packages
#define         appname com.system76.CosmicPlayer
Name:           cosmic-initial-setup
Version:        1.0.0
%define beta beta.4
Release:        %{?beta:0.%{beta}.}1
Summary:        COSMIC Initial Setup 
Group:          System
License:        GPL-3.0-only
URL:            https://github.com/pop-os/cosmic-initial-setup
Source0:        https://github.com/pop-os/cosmic-initial-setup/archive/epoch-%{version}%{?beta:-%{beta}}/%{name}-epoch-%{version}%{?beta:-%{beta}}.tar.gz
Source1:        vendor.tar.xz
Source2:        cargo_config

BuildRequires:  rust-packaging
BuildRequires:  clang-devel
BuildRequires:  curl
BuildRequires:  just
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(xkbcommon)
BuildRequires:  pkgconfig(glib-2.0)


%description
%{summary}.

%prep
%autosetup -n %{name}-epoch-%{version}%{?beta:-%{beta}} -a1 -p1
mkdir .cargo
cp %{SOURCE2} .cargo/config
%cargo_prep -v vendor

%build
%cargo_build

%install
#just rootdir=%{buildroot} prefix=%{_prefix} install

%files
%license LICENSE
%doc README.md
%{_bindir}/cosmic-initial-setup
%{_datadir}/applications/com.system76.CosmicInitialSetup.desktop
%dir %{_datadir}/cosmic-layouts
%{_datadir}/cosmic-layouts/**
%dir %{_datadir}/cosmic-themes
%{_datadir}/cosmic-themes/**
%{_datadir}/icons/hicolor/scalable/apps/com.system76.CosmicInitialSetup.svg
%{_datadir}/polkit-1/rules.d/20-cosmic-initial-setup.rules
%{_sysconfdir}/xdg/autostart/com.system76.CosmicInitialSetup.desktop
