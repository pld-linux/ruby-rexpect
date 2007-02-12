Summary:	Ruby Expect module
Summary(pl.UTF-8):   Moduł Expect dla języka Ruby
Name:		ruby-rexpect
Version:	0.5
Release:	1
License:	Ruby's license
Group:		Development/Libraries
Source0:	http://rubyforge.org/frs/download.php/5147/rexpect-%{version}.tgz
# Source0-md5:	d138c618325890e8a18392c83e40c638
Patch0:		%{name}-open3.patch
URL:		http://rexpect.rubyforge.org/
BuildRequires:	rpmbuild(macros) >= 1.277
BuildRequires:	ruby-modules
BuildRequires:	setup.rb
%{?ruby_mod_ver_requires_eq}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
RExpect is a drop in replacement for the expect.rb module in the Ruby
standard library that is faster and more robust, cabable of driving
many devices simultaneously.

%description -l pl.UTF-8
RExpect to zamiennik dla modułu expect.rb w standardowej bibliotece
języka Ruby. Jest szybszy i bogatszy w możliwości, potrafi obsługiwać
wiele urządzeń jednocześnie.

%prep
%setup -q -n rexpect-%{version}
%patch0 -p1
cp %{_datadir}/setup.rb .
mkdir lib
mv RExpect.rb lib

%build
ruby setup.rb config \
	--rbdir=%{ruby_rubylibdir} \
	--sodir=%{ruby_archdir}

ruby setup.rb setup
rdoc --inline-source --op rdoc lib
rdoc --ri --op ri lib

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{ruby_rubylibdir},%{ruby_ridir}}

ruby setup.rb install \
	--prefix=$RPM_BUILD_ROOT

cp -a ri/ri/* $RPM_BUILD_ROOT%{ruby_ridir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc rdoc examples
%{ruby_rubylibdir}/*
%{ruby_ridir}/*
