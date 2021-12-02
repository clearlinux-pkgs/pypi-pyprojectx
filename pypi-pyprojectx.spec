#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : pypi-pyprojectx
Version  : 0.9.1
Release  : 2
URL      : https://files.pythonhosted.org/packages/de/51/2afe0f2cd0ce24cf0a58cf22b92dc06c5aaa23d6278aaaf112b628dd7daf/pyprojectx-0.9.1.tar.gz
Source0  : https://files.pythonhosted.org/packages/de/51/2afe0f2cd0ce24cf0a58cf22b92dc06c5aaa23d6278aaaf112b628dd7daf/pyprojectx-0.9.1.tar.gz
Summary  : Execute scripts from pyproject.toml, installing tools on-the-fly
Group    : Development/Tools
License  : MIT
Requires: pypi-pyprojectx-bin = %{version}-%{release}
Requires: pypi-pyprojectx-license = %{version}-%{release}
Requires: pypi-pyprojectx-python = %{version}-%{release}
Requires: pypi-pyprojectx-python3 = %{version}-%{release}
BuildRequires : buildreq-distutils3
BuildRequires : pypi(poetry_core)

%description
# pyprojectx
Execute scripts from pyproject.toml, installing tools on-the-fly
Getting started with a Python project should be a one-liner:
```shell
git clone https://github.com/houbie/pyprojectx.git && cd pyprojectx && ./pw build
```

%package bin
Summary: bin components for the pypi-pyprojectx package.
Group: Binaries
Requires: pypi-pyprojectx-license = %{version}-%{release}

%description bin
bin components for the pypi-pyprojectx package.


%package license
Summary: license components for the pypi-pyprojectx package.
Group: Default

%description license
license components for the pypi-pyprojectx package.


%package python
Summary: python components for the pypi-pyprojectx package.
Group: Default
Requires: pypi-pyprojectx-python3 = %{version}-%{release}

%description python
python components for the pypi-pyprojectx package.


%package python3
Summary: python3 components for the pypi-pyprojectx package.
Group: Default
Requires: python3-core
Provides: pypi(pyprojectx)
Requires: pypi(tomli)
Requires: pypi(virtualenv)

%description python3
python3 components for the pypi-pyprojectx package.


%prep
%setup -q -n pyprojectx-0.9.1
cd %{_builddir}/pyprojectx-0.9.1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1638465211
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=auto "
export FCFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export FFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=auto "
export MAKEFLAGS=%{?_smp_mflags}
python3 -m build --wheel --skip-dependency-check --no-isolation

%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/pypi-pyprojectx
cp %{_builddir}/pyprojectx-0.9.1/LICENSE %{buildroot}/usr/share/package-licenses/pypi-pyprojectx/113e02ca67ac0915072617d98ef2242cfea81a03
pip install --root=%{buildroot} --no-deps --ignore-installed dist/*.whl
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/pyprojectx

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/pypi-pyprojectx/113e02ca67ac0915072617d98ef2242cfea81a03

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
