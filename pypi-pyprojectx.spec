#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: pyproject
#
Name     : pypi-pyprojectx
Version  : 1.0.1
Release  : 20
URL      : https://files.pythonhosted.org/packages/2e/f0/64d285773a10d944892a6f72ed2f163bf13dd27fadb9bf5d6bcf0a6db855/pyprojectx-1.0.1.tar.gz
Source0  : https://files.pythonhosted.org/packages/2e/f0/64d285773a10d944892a6f72ed2f163bf13dd27fadb9bf5d6bcf0a6db855/pyprojectx-1.0.1.tar.gz
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
![pyprojectx](docs/docs/assets/px.png)
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
Requires: pypi(click)
Requires: pypi(distlib)
Requires: pypi(filelock)
Requires: pypi(platformdirs)
Requires: pypi(tomli)
Requires: pypi(userpath)
Requires: pypi(virtualenv)

%description python3
python3 components for the pypi-pyprojectx package.


%prep
%setup -q -n pyprojectx-1.0.1
cd %{_builddir}/pyprojectx-1.0.1
pushd ..
cp -a pyprojectx-1.0.1 buildavx2
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1689696037
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
export FCFLAGS="$FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
export FFLAGS="$FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
export CXXFLAGS="$CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
export MAKEFLAGS=%{?_smp_mflags}
pypi-dep-fix.py . filelock
pypi-dep-fix.py . platformdirs
pypi-dep-fix.py . virtualenv
pypi-dep-fix.py . click
pypi-dep-fix.py . distlib
pypi-dep-fix.py . userpath
python3 -m build --wheel --skip-dependency-check --no-isolation
pushd ../buildavx2/
export CFLAGS="$CFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export CXXFLAGS="$CXXFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FFLAGS="$FFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FCFLAGS="$FCFLAGS -m64 -march=x86-64-v3 "
export LDFLAGS="$LDFLAGS -m64 -march=x86-64-v3 "
pypi-dep-fix.py . filelock
pypi-dep-fix.py . platformdirs
pypi-dep-fix.py . virtualenv
pypi-dep-fix.py . click
pypi-dep-fix.py . distlib
pypi-dep-fix.py . userpath
python3 -m build --wheel --skip-dependency-check --no-isolation

popd

%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/pypi-pyprojectx
cp %{_builddir}/pyprojectx-%{version}/LICENSE %{buildroot}/usr/share/package-licenses/pypi-pyprojectx/113e02ca67ac0915072617d98ef2242cfea81a03 || :
pip install --root=%{buildroot} --no-deps --ignore-installed dist/*.whl
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
export CFLAGS="$CFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export CXXFLAGS="$CXXFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FFLAGS="$FFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FCFLAGS="$FCFLAGS -m64 -march=x86-64-v3 "
export LDFLAGS="$LDFLAGS -m64 -march=x86-64-v3 "
pip install --root=%{buildroot}-v3 --no-deps --ignore-installed dist/*.whl
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
