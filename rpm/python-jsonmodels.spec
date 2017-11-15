%global pypi_name jsonmodels
# Tests require invoke, which is only available for Fedora
%global use_tests 0%{?fedora:1}
Summary: Create Python structures that are converted to, or read from JSON
Name: python-jsonmodels
Version: 2.2
Release: 1%{?dist}
Source0: https://github.com/beregond/%{pypi_name}/archive/%{version}.tar.gz#/%{name}-%{version}.tar.gz
License: BSD
BuildArch: noarch
Url: https://github.com/beregond/jsonmodels

BuildRequires: python2-devel
%if 0%{?use_tests:1}
BuildRequires: python3-devel
BuildRequires: python-invoke
BuildRequires: python3-invoke
%endif

%description
Models to make it easier to deal with structures that are converted to, or
read from JSON.

%package -n     python2-%{pypi_name}
Summary: %summary

BuildRequires: python-dateutil
BuildRequires: pytest
BuildRequires: python-pytest-cov
BuildRequires: python-six
Requires: python-dateutil
Requires: python-six

%description -n     python2-%{pypi_name}
Python 2 models to make it easier to deal with structures that are
converted to, or read from JSON.


%if %{use_tests}
%package -n     python3-%{pypi_name}
Summary: %summary

BuildRequires: python3-dateutil
BuildRequires: python3-pytest
BuildRequires: python3-pytest-cov
BuildRequires: python3-six
Requires: python3-dateutil
Requires: python3-six

%description -n     python3-%{pypi_name}
Python 3 models to make it easier to deal with structures that are
converted to, or read from JSON.
%endif

%prep
%setup -q -n %{pypi_name}-%{version}

%build
%py2_build
%if 0%{?py3_build:1}
%py3_build
%endif

%install
%py2_install
%if 0%{?py3_install:1}
%py3_install
%endif

%if %{use_tests}
%check
PYTHONPATH=$(pwd) %{__python2} setup.py test
PYTHONPATH=$(pwd) %{__python3} setup.py test
%endif

%files -n python2-%{pypi_name}
%license LICENSE
%doc README.rst
%{python2_sitelib}/%{pypi_name}-%{version}-py%{python2_version}.egg-info
%{python2_sitelib}/%{pypi_name}/

%if %{use_tests}
%files -n python3-%{pypi_name}
%license LICENSE
%doc README.rst
%{python3_sitelib}/%{pypi_name}-%{version}-py%{python3_version}.egg-info
%{python3_sitelib}/%{pypi_name}/
%endif

%changelog
* Wed Nov 15 2017 Omer Anson <oaanson@gmail.com> 2.2-1
- Initial release
