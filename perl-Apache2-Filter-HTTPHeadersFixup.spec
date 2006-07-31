#
# Conditional build:
%bcond_without	tests		# do not perform "make test"
#
%define	apxs	/usr/sbin/apxs
%include	/usr/lib/rpm/macros.perl
%define	pdir	Apache2
%define	pnam	Filter-HTTPHeadersFixup
Summary:	Apache2::Filter::HTTPHeadersFixup - Manipulate Apache 2 HTTP Headers
#Summary(pl):	
Name:		perl-Apache2-Filter-HTTPHeadersFixup
Version:	0.06
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	253f4df9d395dbb4735c0708aa809968
Patch0:		%{name}-mpver.patch
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
%if %{with tests}
BuildRequires:	apache-apxs
BuildRequires:	perl-Apache-Test >= 1.25
BuildRequires:	perl-mod_perl >= 2.000001
%endif
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Apache2::Filter::HTTPHeadersFixup is a super class which provides an
easy way to manipulate HTTP headers without invoking any mod_perl HTTP
handlers. This is accomplished by using input and/or output connection
filters.

# %description -l pl
# TODO

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}
%patch0 -p1

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

APACHE_TEST_APXS="%{apxs}" \
%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes TODO
%{perl_vendorlib}/Apache2/Filter/*.pm
%{_mandir}/man3/*