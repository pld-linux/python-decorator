%define module decorator
Summary:	Bunch of nice decorators for Python
Summary(pl.UTF-8):	Zbiór ładnych dekoratorów dla Pythona
Name:		python-%{module}
Version:	3.0.0
Release:	1
License:	BSD
Group:		Python/Libraries
Source0:	http://pypi.python.org/packages/source/d/decorator/%{module}-%{version}.tar.gz
# Source0-md5:	8831085521109323ab6b016dfe200aec
URL:		http://pypi.python.org/pypi/decorator/
BuildRequires:	python-devel >= 1:2.4
%pyrequires_eq	python-libs
Requires:	python-pygtk-gtk >= 2:2.8.4
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Bunch of nice decorators for Python like memoize, tracing,
redirecting_stdout, locked.

%description -l pl.UTF-8
Zbiór ładnych dekoratorów dla Pythona: memoize, tracing,
redirecting_stdout, locked...

%prep
%setup -q -n %{module}-%{version}

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
