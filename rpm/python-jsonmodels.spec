%global pypi_name jsonmodels
# Tests require invoke, which is only available for Fedora
%global use_tests 0%{?fedora:1}
Summary: Models to make easier to deal with structures that are converted to, or read from JSON.
Name: python-jsonmodels
Version: 2.2
Release: 1%{dist}
Source0: https://github.com/beregond/%{pypi_name}/archive/%{version}.tar.gz#/%{name}-%{version}.tar.gz
License: BSD
BuildArch: noarch
Url: https://github.com/beregond/jsonmodels

BuildRequires: python2-devel
%if %{use_tests}
BuildRequires: python3-devel
BuildRequires: python-invoke
BuildRequires: python3-invoke
%endif

%description
%{summary}

%changelog \
* Mon Aug 21 2017 Szczepan Cieślik <szczepan.cieslik@gmail.com> 2.2 \
- add nullable param for fields \
- Handle None values in parse_value for Time and Date Fields \
- Add tests \
- Drop support for py 2.6, add for 3.6 \
- fix coverage \
- add documentation \
- Add field values to model's repr() \
 \
* Wed Feb 1 2017 Szczepan Cieślik <szczepan.cieslik@gmail.com> 2.1.5 \
- Update history \
- fix raise error if DateTimeField is None \
- add comment to test \
- Fix __eq__ for models with missing required fields \
- Version 2.1.5 \
 \
* Tue Jan 24 2017 +0100 Szczepan Cieślik <szczepan.cieslik@gmail.com> 2.1.4 \
- Add __eq__ to models that compare based on fields \
- Version 2.1.4 \
 \
* Mon Jan 16 2017 +0100 Szczepan Cieślik <szczepan.cieslik@amsterdam-standard.pl> 2.1.3 \
- Update builders.py \
- Add python3.5 tox env \
- Drop python 3.2 job on Travis CI \
- Fix issue#72: when creating a struct from a json model use the field's to_struct method \
- Fix json schema types \
- Unpin requirements from specific versions \
- Exclude flake8 from 2.7, 3.2, 3.3 builds \
- Install libenchant package \
- Make to_struct recursive on custom fields \
- Version 2.1.3 \
 \
* Wed Jan 6 2016 +0100 Szczepan Cieślik <szczepan.cieslik@gmail.com> 2.1.2 \
- Fixed memory leak (fixes #64). \
- Removed PyPy from memory test. \
- Improved docs. \
- Fixed coverage command, docs typos and test setup. \
- Fixed default skip of spelling test. \
- Version 2.1.2. \
 \
* Sun Nov 15  2015 +0100 Szczepan Cieślik <szczepan.cieslik@gmail.com> 2.1.1 \
- Added support for Python 2.6 and 3.5. \
- Changed support from 3.5 to 3.2. \
- Fixed requirements for coverage for Py3.2. \
- Added support for Python3.5. \
- Small ordering of code. \
- Updated docs. \
- Improved coverage. \
- Moved builders to distinct module. \
- Fixed coverage. \
- Version 2.1.1. \
 \
* Mon Nov 2  2015 +0100 Szczepan Cieślik <szczepan.cieslik@gmail.com> 2.1 \
- Fixed tox config, updated test values. \
- Fixed download shield. \
- Added first case of embedded lazy loading. \
- Fixed readme badge. \
- Improved initialization of allowed types. \
- Added support for absolute embedded path. \
- Added support for relative embedded paths. \
- Improved relative paths support. \
- Refactor. \
- Small refactor in gneration of schema. \
- Moved cration of json schema to builders. \
- Improved building schema. \
- Draft of definitions. \
- Fixed structure generation for list field. \
- Made generation of circular schema work. \
- Improved generation of circular schema. \
- Added failing test case, removed trash file. \
- Improved readability of validation error. \
- Fixed lazy loading for lists. \
- Fixed schema generation for lists. \
- Added docs and history. \
- Fixed code blocks in readme. \
- Version 2.1. \
 \
* Sat Nov 15  2014 +0100 Szczepan Cieślik <szczepan.cieslik@gmail.com> 2.0.1 \
- Fixed schema generation for primitives (fixes #42). \
- Added missing history entry. \
- Version 2.0.1. \
 \
* Fri Nov 14  2014 +0100 Szczepan Cieślik <szczepan.cieslik@gmail.com> 2.0 \
- Removed data transformers (closes #36). \
- Renamed _types to types (closes #3). \
- Updated requirements and history. \
- Fixed typos in history file. \
- Renamed module error to errors (closes #14). \
- Fixed requirements. \
- Improved test suite. \
- Fixed assignation of metaclass (fixes #39). \
- Fixed readme file. \
- Moved fields to be descriptors (fixes #44). \
- Reorganized code. \
- Improved behaviour of required fields. \
- Renamed field method (fixes #46). \
- Fixed name in exception message. \
- Revert "Fixed name in exception message." \
- Removed field name from validation errors. \
- Fixed validation of list fields (fixes #47). \
- Improved technical docs. \
- Refactor. \
- Removed unused requirement. \
- Moved to PyTest. \
- Moved to PyTest (closes #50). \
- Fixed syntax in tests. \
- Added coverage reports. \
- Added coverage info (closes #51). \
- Tidy up requirements. \
- Improved documentation. \
- Renamed `utils` to `utilities`. \
- Added missing history entry. \
- Improved coverage report and setup file. \
- Hacked `pytest-cov` to integrate fully. \
- Updated docs (closes #48). \
- Improved validation section in docs. \
- Fixed readme file. \
- Version 2.0. \
 \
* Tue Jul 22  2014 +0200 Szczepan Cieślik <szczepan.cieslik@gmail.com> 1.4 \
- Allowed validators to modify generated schema (closes #32). \
- Added validator for minimum value (closes #30). \
- Fixed doctrings. \
- Added validator for maximum value (closes #31). \
- Added regex validator (closes #29). \
- Improved typo. \
- Improved tests. \
- Fixed import for Python 3. \
- Refactored regex validator (fixes #37). \
- Improved tests. \
- Renamed attribute with flags. \
- Added length validator (closes #28). \
- Improved docs (closes #38). \
- Small fix of readme file. \
- Version 1.4. \
 \
* Sun Jul 13  2014 +0200 Szczepan Cieślik <szczepan.cieslik@gmail.com> 1.3.1 \
- Updated readme. \
- Changed description. \
- Fixed generation of schema for BoolField. \
- Version 1.3.1. \
 \
* Sun Jul 13  2014 +0200 Szczepan Cieślik <szczepan.cieslik@gmail.com> 1.3 \
- Tidied up support for Python versions. \
- Improved schema generation (fixes #19). \
- Added pyhistory package and BoolField (closes #20). \
- Fixed docs. \
- Arranged things with required for embedded and list field (closes #10). \
- Added TimeField. \
- Fixed dependency bug. \
- Added DateField. \
- Added DateTimeField. \
- Fixed docs and syntax. \
- Fixed schema generation for datetime fields. \
- Version 1.3. \
 \
* Thu Jun 19  2014 +0200 Szczepan Cieślik <szczepan.cieslik@gmail.com> 1.2.0.2 \
- Added missing history. \
- Fixed import errors. \
- Version 1.2.0.2. \
 \
* Thu Jun 19  2014 +0200 Szczepan Cieślik <szczepan.cieslik@gmail.com> 1.2.0.1 \
- Spell checking is now not obligatory. \
- Version 1.2.0.1. \
 \
* Wed Jun 18  2014 +0200 Szczepan Cieślik <szczepan.cieslik@gmail.com> 1.2 \
- Updated HISTORY.rst. \
- Added validators. \
- Added validators as functions. \
- Added docs for custom validators (closes #17). \
- Updated contributing file (closes #15). \
- Added docs checking (closes #18). \
- Fixed tests. \
- Version 1.2. \
 \
* Sat Jun 7  2014 +0200 Szczepan Cieślik <szczepan.cieslik@gmail.com> 1.1.1 \
- Updated history. \
- Fixed population to EmbeddedField (fixes #13). \
- Made  public (fixes #12). \
- Updated HISTORY.rst. \
- Fixed README.rst. \
- Version 1.1.1. \
 \
* Mon May 19  2014 +0200 Szczepan Cieślik <szczepan.cieslik@gmail.com> 1.1 \
- Improved JSON schemes, added tool for comparison. \
- Improved schema generation. \
- Improved tests for schema generation. \
- Added help text to fields (fixes #2). \
- Improved requirements. \
- Hacked unittests, so now 'quick test' are possible. \
- Added PEP257 compatibility (closes #6). \
- Fixed requirements, moved to Python 3.4. \
- Added tests for PEP8 and complexity. \
- Added oneOf to generated schema. \
- Fixed problems with schema comparison. \
- Updated readme file. \
- Added docs (fixes #4). \
- Version 1.1. \
 \
* Mon Apr 14  2014 +0200 Szczepan Cieślik <szczepan.cieslik@amsterdam-standard.pl> 1.0.5 \
- Added data transformers. \
 \
* Sun Apr 13  2014 +0200 Szczepan Cieślik <szczepan.cieslik@gmail.com> 1.0.4 \
- Fixed setup.py requirements. Fixes #1. \
- List field now supports simple types. \
 \
* Thu Apr 10  2014 +0200 Szczepan Cieślik <szczepan.cieslik@amsterdam-standard.pl> 1.0.3 \
- Fixed history, improved tests. \
- Fixed compatibility with Python 3. \
- Fixed and improved repr and str methods. \
- Version 1.0.3 \
 \
* Thu Apr 3  2014 +0200 Szczepan Cieślik <szczepan.cieslik@gmail.com> 1.0.2 \
- Added deep data initialization. \
 \
* Thu Apr 3  2014 +0200 Szczepan Cieślik <szczepan.cieslik@amsterdam-standard.pl> 1.0.1 \
- Added populate method. \
 \
* Wed Apr 2  2014 +0200 Szczepan Cieślik <szczepan.cieslik@amsterdam-standard.pl> 1.0 \
- Added basic to_struct method. \
- Improved to_struct method. \
- Added initialization, get_field and iteration. \
- Refactored to_struct method. \
- First draft of json schema generation. \
- Version 1.0 \
 \
* Mon Mar 17  2014 +0100 Szczepan Cieślik <szczepan.cieslik@gmail.com> 0.1.0 \
- Hello World! \
- Added base models and validation. \
- Added validation of types. \
- Added basic implementation of list field. \
- Ended implementation of list field. \
- Added embedded field.

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

%clean
rm -rf $RPM_BUILD_ROOT

%if %{use_tests}
%check
PYTHONPATH=$(pwd) %{__python2} setup.py test
PYTHONPATH=$(pwd) %{__python3} setup.py test
%endif

%package -n     python2-%{name}
Summary: Models to make easier to deal with structures that are converted to, or read from JSON.

BuildRequires: python-dateutil
BuildRequires: pytest
BuildRequires: python-pytest-cov
BuildRequires: python-six
Requires: python-dateutil
Requires: python-six

%description -n     python2-%{name}
%{summary}

%files -n python2-%{name}
%license LICENSE
%doc README.rst
%{python2_sitelib}/%{pypi_name}-%{version}-py%{python2_version}.egg-info
%{python2_sitelib}/%{pypi_name}/

%if %{use_tests}
%package -n     python3-%{name}
Summary: Models to make easier to deal with structures that are converted to, or read from JSON.

BuildRequires: python3-dateutil
BuildRequires: python3-pytest
BuildRequires: python3-pytest-cov
BuildRequires: python3-six
Requires: python3-dateutil
Requires: python3-six

%description -n     python3-%{name}
%{summary}

%files -n python3-%{name}
%license LICENSE
%doc README.rst
%{python3_sitelib}/%{pypi_name}-%{version}-py%{python3_version}.egg-info
%{python3_sitelib}/%{pypi_name}/
%endif

