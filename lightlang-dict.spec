%define version 0.0.2
%define	rel	2
%define release %mkrel %{rel}

Summary: Dictionary for LightLang
Name: lightlang-dict
Version:	%{version}
Release:	%{release}
License: GPL2+
Group: Office
URL: https://code.google.com/p/lightlang/
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
mkdir -p %{buildroot}/%{_datadir}/sl/dicts
cp ./* %{buildroot}/%{_datadir}/sl/dicts

%build

%clean
%{__rm} -rf %{buildroot}


%files
%defattr(-, root, root, 0755)
%{_datadir}/sl/dicts/*


%changelog
* Sun Sep 11 2011 Александр Казанцев <kazancas@mandriva.org> 0.0.2-2mdv2012.0
+ Revision: 699430
- fix error from build only src.rpm

* Fri Jul 22 2011 Александр Казанцев <kazancas@mandriva.org> 0.0.2-1
+ Revision: 690911
+ rebuild (emptylog)

* Mon Jul 04 2011 Александр Казанцев <kazancas@mandriva.org> 0.0.1-5
+ Revision: 688695
+ rebuild (emptylog)

* Sat Jan 22 2011 Александр Казанцев <kazancas@mandriva.org> 0.0.1-4
+ Revision: 632358
+ rebuild (emptylog)

* Thu Dec 30 2010 Александр Казанцев <kazancas@mandriva.org> 0.0.1-3mdv2011.0
+ Revision: 626490
+ rebuild (emptylog)

* Thu Dec 30 2010 Александр Казанцев <kazancas@mandriva.org> 0.0.1-2mdv2011.0
+ Revision: 626211
- initial release
- import lightlang-dict


* Thu Apr 23 2009 root <root@mandriva.com> 0.0.1-2mdk
- rebuild


* Sun Oct 26 2008 Alexandr kazancev <kazancas@mandriva.ru> - 0.0.1
- Build for 2009.0

* Sun Feb 3 2008 Alexandr kazancev <kazancas@mail.ru> - 0.0.1
- First release