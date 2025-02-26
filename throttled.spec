%global _hardened_build 1
%define debug_package %{nil}

Name:     throttled
Version:  0.11
Release:  1
Summary:  Workaround for Intel throttling issues in Linux
License:  MIT
URL:      https://github.com/erpalma/throttled
Source0:  https://github.com/erpalma/throttled/archive/v%{version}.tar.gz
Source1:  throttled.service

BuildRequires: python3-devel
BuildRequires: systemd-units

Requires: python3
Requires: python3-gobject
Requires: python3-dbus
Requires: systemd
Requires: pciutils

Conflicts: thermald

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
install -D throttled.py %{buildroot}/%{_bindir}/%{name}
install -D mmio.py %{buildroot}/%{python3_sitelib}/mmio.py
install -D etc/throttled.conf %{buildroot}/%{_sysconfdir}/%{name}.conf
install -D %{SOURCE1} %{buildroot}/%{_unitdir}/%{name}.service

%post
%systemd_post %{name}.service

%preun
%systemd_preun %{name}.service

%postun
%systemd_postun_with_restart %{name}.service

%files
%defattr(-,root,root,-)
%attr(755, root, root) %{_bindir}/%{name}
%attr(644, root, root) %{python3_sitelib}/mmio.py
%attr(644, root, root) %{python3_sitelib}/__pycache__/*
%config(noreplace) %attr(640, root, root) %{_sysconfdir}/%{name}.conf
%attr(644, root, root) %{_unitdir}/%{name}.service

%changelog
* Sat Jan 25 2025 Arun Babu Neelicattu <arun.neelicattu@gmail.com> - 0.11-1
- Upgrade to 0.11 (pre-release)

* Tue Jan 10 2023 Arun Babu Neelicattu <arun.neelicattu@gmail.com> - 0.10.0-1
- Upgrade to 0.10.0
- Add python3-dbus requirement
- Update source script name from lenovo_fix.py to throttled.py
- Update source config name from lenovo_fix.py to throttled.conf

* Wed Nov 03 2021 Arun Babu Neelicattu <arun.neelicattu@gmail.com> - 0.9.2-1
- Upgrade to 0.9.2

* Mon Mar 29 2021 Arun Babu Neelicattu <arun.neelicattu@gmail.com> - 0.8-3
- Bump release for new fedora release

* Sun Dec  6 2020 Arun Babu Neelicattu <arun.neelicattu@gmail.com> - 0.8-2
- Remove dependency on configparser backport

* Sat Dec  5 2020 Arun Babu Neelicattu <arun.neelicattu@gmail.com> - 0.8-1
- Upgrade to 0.8
- Remove deprecated systemd-unit configuration (https://github.com/erpalma/throttled/pull/212)

* Mon Mar 16 2020 Arun Babu Neelicattu <arun.neelicattu@gmail.com> - 0.7-1
- Upgrade to 0.7

* Fri Nov 08 2019 Alan Ivey <alanivey@gmail.com> - 0.6-2
- Fix file ownership on /etc/throttled.conf

* Thu May 02 2019 Arun Babu Neelicattu <arun.neelicattu@twyla.ai> - 0.6-1
- Upgrade to 0.6

* Mon Mar 11 2019 Arun Babu Neelicattu <arun.neelicattu@gmail.com> - 0.5-4
- Add conflict for thermald

* Mon Mar 11 2019 Arun Babu Neelicattu <arun.neelicattu@gmail.com> - 0.5-3
- Fix unit file to use configuration

* Mon Mar 11 2019 Arun Babu Neelicattu <arun.neelicattu@gmail.com> - 0.5-2
- Add default configuration file
- Fix file permissions

* Mon Mar 11 2019 Arun Babu Neelicattu <arun.neelicattu@gmail.com> - 0.5-1
- Initial release of version 0.5


