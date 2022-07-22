Name:           nftwatch
Version:        67104f3f3415a222ba1937edf0e62d8deda92352
Release:        2%{?dist}
Summary:        nft policy viewer

License:        GPLv3
URL:            https://github.com/flyingrhinonz/nftwatch
Source0:        https://github.com/flyingrhinonz/nftwatch/archive/%{version}.tar.gz

Requires:       python3 python3-pyyaml

%description
View your nftables configuration.

%prep
%autosetup

#make install
install -m 0755 -D %{name} %{buildroot}/%{_bindir}/%{name}
install -m 0644 -D %{name}.yml %{buildroot}/%{_sysconfdir}/%{name}.yml

%files
%license LICENSE
%{_bindir}/%{name}
%{_sysconfdir}/%{name}.yml

%changelog
* Fri Jun 17 2022 Seth Kenlon <seth@redhat.com>
- SPEC file
