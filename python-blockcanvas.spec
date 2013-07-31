%define module	blockcanvas

Summary: 	Enthought Tool Suite - blockcanvas project
Name:		python-%{module}
Version:	4.0.3
Release:	1
Source0:	https://www.enthought.com/repo/ets/blockcanvas-%{version}.tar.gz
Patch0:		blockcanvas-4.0.0-link.patch
License:	BSD
Group:		Development/Python
Url:		https://github.com/enthought/blockcanvas/
Obsoletes:	python-enthought-blockcanvas
Requires:	python-configobj
Requires:	python-apptools >= 4.0.1
Requires:	python-chaco >= 4.1.0
Requires:	python-codetools >= 4.0.0
Requires:	python-etsdevtools >= 4.0.0
Requires:	python-scimath >= 4.0.1
Requires:	python-traitsui >= 4.1.0
Requires:	python-numpy >= 1.1.0
BuildRequires:	python-setuptools >= 0.6c8
BuildRequires:	python-sphinx

%description
The blockcanvas project provides a visual environment for creating
simulation experiments, where function and data are separated. Thus,
you can define your simulation algorithm by visually connecting
function blocks into a data flow network, and then run it with various
data sets (known as "contexts"); likewise, you can use the same
context in a different functional simulation.

The project provides support for plotting, function searching and
inspection, and optimization. It includes a stand-alone application
that demonstrates the block-canvas environment, but the same
functionality can be incorporated into other applications.

%prep
%setup -q -n %{module}-%{version}
%patch0 -p1

%build

%__python setup.py build
pushd docs
make html
popd

%install
PYTHONDONTWRITEBYTECODE= %__python setup.py install --root=%{buildroot} --record=FILE_LIST
sed -i 's/.*egg-info$//' FILE_LIST

%files -f FILE_LIST
%doc *.txt *.rst docs/build/html/


%changelog
* Tue Dec 27 2011 Lev Givon <lev@mandriva.org> 4.0.1-1
+ Revision: 745665
- Update to 4.0.1.

* Thu Jul 07 2011 Lev Givon <lev@mandriva.org> 4.0.0-1
+ Revision: 689219
- import python-blockcanvas



