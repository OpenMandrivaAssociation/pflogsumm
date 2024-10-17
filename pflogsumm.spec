%define	name pflogsumm
%define	version	1.1.5
%define release	2

Summary: 	Postfix Log Entry Summarizer
Name: 		%{name}
Version: 	%{version}
Release:	%{release}
License: 	GPL
Group:		Monitoring
Source0:	http://jimsun.LinxNet.com/downloads/pflogsumm-%{version}.tar.gz
Url:		https://jimsun.LinxNet.com/
Buildarch:	noarch

%description
Pflogsumm is a log analyzer/summarizer for the Postfix MTA.  It is
designed to provide an over-view of Postfix activity, with just enough
detail to give the administrator a "heads up" for potential trouble
spots.
Pflogsumm generates summaries and, in some cases, detailed reports of
mail server traffic volumes, rejected and bounced email, and server
warnings, errors and panics.

%prep
%setup -q

%install
mkdir -p %buildroot/%{_sbindir}
mkdir -p %buildroot/%{_mandir}/man1
install -m755 pflogsumm.pl %buildroot/%{_sbindir}/pflogsumm
install -m644 pflogsumm.1 %buildroot/%{_mandir}/man1/pflogsumm.1

%files
%defattr(-,root,root,755)
%doc ChangeLog pflogsumm-faq.txt README ToDo
%{_sbindir}/pflogsumm
%{_mandir}/man1/pflogsumm.1*



%changelog
* Wed Feb 08 2012 Alexander Khrukin <akhrukin@mandriva.org> 1.1.5-1
+ Revision: 771858
- version update 1.1.5

* Fri Sep 04 2009 Thierry Vignaud <tv@mandriva.org> 1.1.0-9mdv2010.0
+ Revision: 430678
- rebuild

* Fri Aug 08 2008 Thierry Vignaud <tv@mandriva.org> 1.1.0-8mdv2009.0
+ Revision: 267989
+ rebuild (emptylog)

* Fri Aug 01 2008 Thierry Vignaud <tv@mandriva.org> 1.1.0-7mdv2009.0
+ Revision: 258925
- rebuild

* Thu Jul 24 2008 Thierry Vignaud <tv@mandriva.org> 1.1.0-6mdv2009.0
+ Revision: 246831
- rebuild

* Fri Dec 21 2007 Olivier Blin <blino@mandriva.org> 1.1.0-4mdv2008.1
+ Revision: 136373
- restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

