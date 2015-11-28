#
# Conditional build:
%bcond_without	python2	# CPython 2.x module
%bcond_without	python3	# CPython 3.x module

%define		module decorator
Summary:	Bunch of nice decorators for Python 2
Summary(pl.UTF-8):	Zbiór ładnych dekoratorów dla Pythona 2
Name:		python-%{module}
Version:	3.4.0
Release:	5
License:	BSD
Group:		Libraries/Python
Source0:	https://pypi.python.org/packages/source/d/decorator/%{module}-%{version}.tar.gz
# Source0-md5:	1e8756f719d746e2fc0dd28b41251356
URL:		https://pypi.python.org/pypi/decorator/
%if %{with python2}
BuildRequires:	python-devel >= 1:2.4
BuildRequires:	python-modules >= 1:2.4
%endif
%if %{with python3}
BuildRequires:	python3-devel >= 3.2
BuildRequires:	python3-modules >= 3.2
%endif
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.612
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

%prep
%setup -q -n %{module}-%{version}

%build
%if %{with python2}
%py_build \
	--build-base build-2
%endif
%if %{with python3}
%py3_build \
	--build-base build-3
%endif

%install
rm -rf $RPM_BUILD_ROOT

%if %{with python2}
%{__python} setup.py \
	build \
		--build-base build-2 \
	install \
		--optimize=2 \
		--root=$RPM_BUILD_ROOT

%py_postclean
%endif

%if %{with python3}
%{__python3} setup.py \
	build \
		--build-base build-3 \
	install \
		--optimize=2 \
		--root=$RPM_BUILD_ROOT
%endif

%clean
rm -rf $RPM_BUILD_ROOT

%if %{with python2}
%files
%defattr(644,root,root,755)
%doc README.txt documentation.py
%{py_sitescriptdir}/decorator.py[co]
%{py_sitescriptdir}/decorator-%{version}-py*.egg-info
%endif

%if %{with python3}
%files -n python3-%{module}
%defattr(644,root,root,755)
%doc README.txt documentation.py
%{py3_sitescriptdir}/decorator.py
%{py3_sitescriptdir}/__pycache__/decorator.*.py[co]
%{py3_sitescriptdir}/decorator-%{version}-py*.egg-info
%endif
