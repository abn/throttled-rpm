%global _hardened_build 1
%define debug_package %{nil}

Name:     throttled
Version:  0.5
Release:  1
Summary:  Workaround for Intel throttling issues in Linux
License:  MIT
URL:      https://github.com/erpalma/throttled
Source0:  https://github.com/erpalma/throttled/archive/v%{version}.tar.gz
Source1:  throttled.service

BuildRequires: systemd-units

Requires: python3
Requires: python3-gobject
Requires: python3-configparser
Requires: systemd

%description
This tool was originally developed to fix Linux CPU throttling issues affecting 
Lenovo T480 / T480s / X1C6.

The CPU package power limit (PL1/2) is forced to a value of 44 W (29 W on 
battery) and the temperature trip point to 95 'C (85 'C on battery) by 
overriding default values in MSR and MCHBAR every 5 seconds (30 on battery) to 
block the Embedded Controller from resetting these values to default.

%prep
%autosetup

%build

%install
install -D lenovo_fix.py %{buildroot}/%{_bindir}/throttled
install -D mmio.py %{buildroot}/%{python3_sitelib}/mmio.py
install -D %{SOURCE1} %{buildroot}/%{_unitdir}/%{name}.service

%post
%systemd_post %{name}.service

%preun
%systemd_preun %{name}.service

%postun
%systemd_postun_with_restart %{name}.service

%files
%defattr(-,root,root)
%{_bindir}/throttled
%{python3_sitelib}/mmio.py
%{python3_sitelib}/__pycache__/*
%{_unitdir}/%{name}.service


%changelog
* Mon Mar 11 2019 Arun Babu Neelicattu <arun.neelicattu@gmail.com> - 0.5-1
- Initial release of version 0.5


