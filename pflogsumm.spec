%define	name pflogsumm
%define	version	1.1.0
%define	release	%mkrel 4

Summary: 	Postfix Log Entry Summarizer
Name: 		%{name}
Version: 	%{version}
Release:	%{release}
License: 	GPL
Group:		Monitoring
Source:		http://jimsun.LinxNet.com/downloads/pflogsumm-%{version}.tar.bz2
Patch0:		pflogsumm-conn-delays-dsn-patch
Url:		http://jimsun.LinxNet.com/
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
%patch0

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p %buildroot/%{_sbindir}
mkdir -p %buildroot/%{_mandir}/man1
install -m755 pflogsumm.pl %buildroot/%{_sbindir}/pflogsumm
install -m644 pflogsumm.1 %buildroot/%{_mandir}/man1/pflogsumm.1

%clean 
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,755)
%doc ChangeLog pflogsumm-faq.txt README ToDo
%{_sbindir}/pflogsumm
%{_mandir}/man1/pflogsumm.1*

