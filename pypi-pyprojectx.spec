#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: pyproject
# autospec version: v4
# autospec commit: 1ab68ca
#
Name     : pypi-pyprojectx
Version  : 2.1.1
Release  : 30
URL      : https://files.pythonhosted.org/packages/b2/f4/05a9ec3273ca62a8d5173dbac05c3a2f8a9230c728a4f17162d94dbbaeaf/pyprojectx-2.1.1.tar.gz
Source0  : https://files.pythonhosted.org/packages/b2/f4/05a9ec3273ca62a8d5173dbac05c3a2f8a9230c728a4f17162d94dbbaeaf/pyprojectx-2.1.1.tar.gz
Summary  : Execute scripts from pyproject.toml, installing tools on-the-fly
Group    : Development/Tools
License  : MIT
Requires: pypi-pyprojectx-bin = %{version}-%{release}
Requires: pypi-pyprojectx-license = %{version}-%{release}
Requires: pypi-pyprojectx-python = %{version}-%{release}
Requires: pypi-pyprojectx-python3 = %{version}-%{release}
BuildRequires : buildreq-distutils3
BuildRequires : pypi(pdm_backend)
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

%description
![pyprojectx](https://pyprojectx.github.io/assets/px.png)
# Pyprojectx: All-inclusive Python Projects

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
Requires: pypi(tomlkit)
Requires: pypi(userpath)
Requires: pypi(virtualenv)

%description python3
python3 components for the pypi-pyprojectx package.


%prep
%setup -q -n pyprojectx-2.1.1
cd %{_builddir}/pyprojectx-2.1.1
pushd ..
cp -a pyprojectx-2.1.1 buildavx2
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1709827413
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
export MAKEFLAGS=%{?_smp_mflags}
pypi-dep-fix.py . filelock
pypi-dep-fix.py . platformdirs
pypi-dep-fix.py . virtualenv
pypi-dep-fix.py . click
pypi-dep-fix.py . distlib
pypi-dep-fix.py . userpath
python3 -m build --wheel --skip-dependency-check --no-isolation
pushd ../buildavx2/
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -march=x86-64-v3 -Wl,-z,x86-64-v3 "
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -march=x86-64-v3 -Wl,-z,x86-64-v3 "
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -march=x86-64-v3 -Wl,-z,x86-64-v3 "
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS -march=x86-64-v3 "
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS -march=x86-64-v3 "
pypi-dep-fix.py . filelock
pypi-dep-fix.py . platformdirs
pypi-dep-fix.py . virtualenv
pypi-dep-fix.py . click
pypi-dep-fix.py . distlib
pypi-dep-fix.py . userpath
python3 -m build --wheel --skip-dependency-check --no-isolation

popd

%install
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/pypi-pyprojectx
cp %{_builddir}/pyprojectx-%{version}/LICENSE %{buildroot}/usr/share/package-licenses/pypi-pyprojectx/113e02ca67ac0915072617d98ef2242cfea81a03 || :
python3 -m installer --destdir=%{buildroot} dist/*.whl
pypi-dep-fix.py %{buildroot} filelock
pypi-dep-fix.py %{buildroot} platformdirs
pypi-dep-fix.py %{buildroot} virtualenv
pypi-dep-fix.py %{buildroot} click
pypi-dep-fix.py %{buildroot} distlib
pypi-dep-fix.py %{buildroot} userpath
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----
pushd ../buildavx2/
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -march=x86-64-v3 -Wl,-z,x86-64-v3 "
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -march=x86-64-v3 -Wl,-z,x86-64-v3 "
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -march=x86-64-v3 -Wl,-z,x86-64-v3 "
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS -march=x86-64-v3 "
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS -march=x86-64-v3 "
python3 -m installer --destdir=%{buildroot}-v3 dist/*.whl
popd
/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

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
