%define module decorator
Summary:	Bunch of nice decorators for Python
Summary(pl.UTF-8):	Zbiór ładnych dekoratorów dla Pythona
Name:		python-%{module}
Version:	2.3.1
Release:	1
License:	BSD
Group:		Python/Libraries
Source0:	http://www.phyast.pitt.edu/~micheles/python/%{module}-%{version}.zip
# Source0-md5:	40c2d7a566a5f5264ef8d2a88d9261e9
URL:		http://www.phyast.pitt.edu/~micheles/python/documentation.html
BuildRequires:	python-devel >= 1:2.4
%pyrequires_eq	python-libs
Requires:	python-pygtk-gtk >= 2.8.4
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Bunch of nice decorators for Python like memoize, tracing,
redirecting_stdout, locked.

%description -l pl.UTF-8
Zbiór ładnych dekoratorów dla Pythona: memoize, tracing,
redirecting_stdout, locked...

%prep
%setup -qc

%build
%{__python} setup.py build

%install
rm -rf $RPM_BUILD_ROOT

%{__python} setup.py install \
	--optimize=2 \
	--root=$RPM_BUILD_ROOT

%py_postclean

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc documentation.* README.txt CHANGES.txt
%{py_sitescriptdir}/decorator*
