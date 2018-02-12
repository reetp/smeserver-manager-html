%define name smeserver-manager-html
%define version 0.1
%define release 1
Summary: Plugin to enable IPSEC connections
Name: %{name}
Version: %{version}
Release: %{release}%{dist}
License: GNU GPL version 2
URL: http://libreswan.org/
Group: SMEserver/addon
Source: %{name}-%{version}.tar.gz
BuildRoot: /var/tmp/%{name}-%{version}
BuildArchitectures: noarch
BuildRequires: e-smith-devtools
Requires:  e-smith-release >= 9.0
Requires: smeserver-manager
AutoReqProv: no

%description
RPM with html templating for server-manager

%changelog
* Mon Feb 12 2018 John Crisp <jcrisp@safeandsoundit.co.uk> 0.1-1.sme
- Initial build

%prep
%setup

%build
perl createlinks

%install
rm -rf $RPM_BUILD_ROOT
(cd root ; find . -depth -print | cpio -dump $RPM_BUILD_ROOT)
rm -f %{name}-%{version}-filelist
/sbin/e-smith/genfilelist $RPM_BUILD_ROOT > %{name}-%{version}-filelist
echo "%doc COPYING" >> %{name}-%{version}-filelist


%clean
cd ..
rm -rf %{name}-%{version}

%files -f %{name}-%{version}-filelist
%defattr(-,root,root)

%pre
%preun
%post

%postun
