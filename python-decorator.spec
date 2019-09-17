#
# Conditional build:
%bcond_without	python2	# CPython 2.x module
%bcond_without	python3	# CPython 3.x module
%bcond_without	tests	# test suite

%define		module decorator
Summary:	Bunch of nice decorators for Python 2
Summary(pl.UTF-8):	Zbiór ładnych dekoratorów dla Pythona 2
Name:		python-%{module}
Version:	4.4.0
Release:	1
License:	BSD
Group:		Libraries/Python
#Source0Download: https://pypi.org/simple/decorator/
Source0:	https://files.pythonhosted.org/packages/source/d/decorator/%{module}-%{version}.tar.gz
# Source0-md5:	a565a98581c0d110bc247323e89df9b1
Source1:	https://raw.githubusercontent.com/micheles/decorator/%{version}/docs/documentation.md
# Source1-md5:	854f55d03fd6453846d079f22693f45c
URL:		https://pypi.org/project/decorator/
%if %{with python2}
BuildRequires:	python-devel >= 1:2.6
BuildRequires:	python-modules >= 1:2.6
BuildRequires:	python-setuptools
%endif
%if %{with python3}
BuildRequires:	python3-devel >= 1:3.2
BuildRequires:	python3-modules >= 1:3.2
BuildRequires:	python3-setuptools
%endif
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.714
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Bunch of nice decorators for Python 2 like memoize, tracing,
redirecting_stdout, locked.

%description -l pl.UTF-8
Zbiór ładnych dekoratorów dla Pythona 2: memoize, tracing,
redirecting_stdout, locked...

%package -n python3-%{module}
Summary:	Bunch of nice decorators for Python 3
Summary(pl.UTF-8):	Zbiór ładnych dekoratorów dla Pythona 3
Group:		Libraries/Python

%description -n python3-%{module}
Bunch of nice decorators for Python 3 like memoize, tracing,
redirecting_stdout, locked.

%description -n python3-%{module} -l pl.UTF-8
Zbiór ładnych dekoratorów dla Pythona 3: memoize, tracing,
redirecting_stdout, locked...

%package doc
Summary:	Documentation for decorator module in PDF format
Summary(pl.UTF-8):	Dokumentacja modułu decorator w formacie PDF
Group:		Documentation

%description doc
Documentation for decorator module in PDF format.

%description doc -l pl.UTF-8
Dokumentacja modułu decorator w formacie PDF.

%prep
%setup -q -n %{module}-%{version}

cp -p %{SOURCE1} .

%build
%if %{with python2}
%py_build %{?with_tests:test}
%endif

%if %{with python3}
%py3_build %{?with_tests:test}
%endif

%install
rm -rf $RPM_BUILD_ROOT

%if %{with python2}
%py_install

%py_postclean
%endif

%if %{with python3}
%py3_install
%endif

%clean
rm -rf $RPM_BUILD_ROOT

%if %{with python2}
%files
%defattr(644,root,root,755)
%doc CHANGES.md LICENSE.txt README.md
%{py_sitescriptdir}/decorator.py[co]
%{py_sitescriptdir}/decorator-%{version}-py*.egg-info
%endif

%if %{with python3}
%files -n python3-%{module}
%defattr(644,root,root,755)
%doc CHANGES.md LICENSE.txt README.md
%{py3_sitescriptdir}/decorator.py
%{py3_sitescriptdir}/__pycache__/decorator.cpython-*.py[co]
%{py3_sitescriptdir}/decorator-%{version}-py*.egg-info
%endif

%files doc
%defattr(644,root,root,755)
%doc documentation.md
