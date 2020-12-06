![Workflow Status](https://github.com/abn/throttled-rpm/workflows/Build/badge.svg?branch=master)
[![Copr Build Status](https://copr.fedorainfracloud.org/coprs/abn/throttled/package/throttled/status_image/last_build.png)](https://copr.fedorainfracloud.org/coprs/abn/throttled/)

# RPM Package: throttled

This repository holds the RPM package source for [throttled](https://github.com/erpalma/throttled).

## Usage
You can use this package by enabling the copr repository at [abn/throttled](https://copr.fedorainfracloud.org/coprs/abn/throttled/) as described [here](https://fedorahosted.org/copr/wiki/HowToEnableRepo).

```sh
dnf copr enable abn/throttled
dnf copr install throttled
```

### Activation
The package also installs a [systemd.unit](https://www.freedesktop.org/software/systemd/man/systemd.unit.html) file. Which can be activated as shown below.

```sh
systemctl enable --now throttled
```

> **Note:** The configuration used is installed at /etc/throttled.conf