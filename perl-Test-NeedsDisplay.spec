#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: cpan
# autospec version: v21
# autospec commit: 94c6be0
#
Name     : perl-Test-NeedsDisplay
Version  : 1.07
Release  : 20
URL      : https://cpan.metacpan.org/authors/id/A/AD/ADAMK/Test-NeedsDisplay-1.07.tar.gz
Source0  : https://cpan.metacpan.org/authors/id/A/AD/ADAMK/Test-NeedsDisplay-1.07.tar.gz
Summary  : 'Ensure that tests needing a display have one'
Group    : Development/Tools
License  : Artistic-1.0 Artistic-1.0-Perl GPL-2.0
Requires: perl-Test-NeedsDisplay-license = %{version}-%{release}
Requires: perl-Test-NeedsDisplay-perl = %{version}-%{release}
Requires: xauth
Requires: xkbcomp
Requires: xkeyboard-config
Requires: xvfb-run
BuildRequires : buildreq-cpan
BuildRequires : perl(Module::Install)
BuildRequires : util-linux
BuildRequires : xauth
BuildRequires : xkbcomp
BuildRequires : xkeyboard-config
BuildRequires : xvfb-run
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

%description
NAME
Test::NeedsDisplay - Ensure that tests needing a display have one
SYNOPSIS
In your Makefile.PL...

%package dev
Summary: dev components for the perl-Test-NeedsDisplay package.
Group: Development
Provides: perl-Test-NeedsDisplay-devel = %{version}-%{release}
Requires: perl-Test-NeedsDisplay = %{version}-%{release}

%description dev
dev components for the perl-Test-NeedsDisplay package.


%package license
Summary: license components for the perl-Test-NeedsDisplay package.
Group: Default

%description license
license components for the perl-Test-NeedsDisplay package.


%package perl
Summary: perl components for the perl-Test-NeedsDisplay package.
Group: Default
Requires: perl-Test-NeedsDisplay = %{version}-%{release}

%description perl
perl components for the perl-Test-NeedsDisplay package.


%prep
%setup -q -n Test-NeedsDisplay-1.07
cd %{_builddir}/Test-NeedsDisplay-1.07

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
if test -f Makefile.PL; then
%{__perl} -I. Makefile.PL
make  %{?_smp_mflags}
else
%{__perl} Build.PL
./Build
fi

%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make TEST_VERBOSE=1 test

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/perl-Test-NeedsDisplay
cp %{_builddir}/Test-NeedsDisplay-%{version}/LICENSE %{buildroot}/usr/share/package-licenses/perl-Test-NeedsDisplay/f11692fc652e231edd2a23a60c72d9be8a840e0c || :
if test -f Makefile.PL; then
make pure_install PERL_INSTALL_ROOT=%{buildroot} INSTALLDIRS=vendor
else
./Build install --installdirs=vendor --destdir=%{buildroot}
fi
find %{buildroot} -type f -name .packlist -exec rm -f {} ';'
find %{buildroot} -depth -type d -exec rmdir {} 2>/dev/null ';'
find %{buildroot} -type f -name '*.bs' -empty -exec rm -f {} ';'
%{_fixperms} %{buildroot}/*

%files
%defattr(-,root,root,-)

%files dev
%defattr(-,root,root,-)
/usr/share/man/man3/Test::NeedsDisplay.3

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/perl-Test-NeedsDisplay/f11692fc652e231edd2a23a60c72d9be8a840e0c

%files perl
%defattr(-,root,root,-)
/usr/lib/perl5/*
