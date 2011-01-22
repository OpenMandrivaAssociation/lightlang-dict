%define version 0.0.1
%define	rel	3
%define release %mkrel %{rel}

Summary: Dictionary for LightLang
Name: lightlang-dict
Version:	%{version}
Release:	%{release}
License: GPL2+
Group: Office
URL: http://code.google.com/p/lightlang/
Source: %{name}-%{version}.tar.bz2
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root
BuildArch: noarch

Requires: lightlang

%description
Dictionary for LightLang

%prep
%setup -q

%install
%{__rm} -rf %{buildroot}
mkdir %{buildroot}
mkdir %{buildroot}/usr
mkdir %{buildroot}/usr/share
mkdir -p %{buildroot}/%{_datadir}/sl
mkdir %{buildroot/%{_datadir}/sl/dicts
cp ./* %{buildroot}/%{_datadir}/sl/dicts

%build

%clean
%{__rm} -rf %{buildroot}


%files
%defattr(-, root, root, 0755)

%{_datadir}/sl/dicts/*
