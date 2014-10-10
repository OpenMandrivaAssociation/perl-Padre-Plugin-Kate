%define upstream_name    Padre-Plugin-Kate
%define upstream_version 0.06

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	4

Summary:	Using the Kate syntax highlighter
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}
Source0:	http://www.cpan.org/modules/by-module/Padre/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires:	perl-devel
BuildRequires:	perl(ExtUtils::MakeMaker)
BuildRequires:	perl(Module::Install)
BuildRequires:	perl(Padre)
BuildRequires:	perl(Syntax::Highlight::Engine::Kate)
BuildRequires:	perl(Test::More)
BuildArch:	noarch

%description
Padre plugin using the Kate syntax highlighter.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
perl Build.PL installdirs=vendor
./Build

%check
#./Build test

%install
./Build install destdir=%{buildroot}

%files
%doc Changes README
%{_mandir}/man3/*
%{perl_vendorlib}/*


%changelog
* Sat Apr 23 2011 Funda Wang <fwang@mandriva.org> 0.60.0-2mdv2011.0
+ Revision: 656952
- rebuild for updated spec-helper

* Sun Dec 19 2010 Guillaume Rousse <guillomovitch@mandriva.org> 0.60.0-1mdv2011.0
+ Revision: 623018
- new version

* Sun Aug 15 2010 Jérôme Quelin <jquelin@mandriva.org> 0.40.0-1mdv2011.0
+ Revision: 569950
- update to 0.04

* Fri Nov 13 2009 Jérôme Quelin <jquelin@mandriva.org> 0.20.0-1mdv2010.1
+ Revision: 465733
- import perl-Padre-Plugin-Kate


* Fri Nov 13 2009 cpan2dist 0.02-1mdv
- initial mdv release, generated with cpan2dist
