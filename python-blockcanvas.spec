%define module	blockcanvas
%define name 	python-%{module}
%define version 4.0.1
%define	rel		2
%if %mdkversion < 201100
%define release %mkrel %{rel}
%else
%define	release %{rel}

Summary: 	Enthought Tool Suite - visual environment for creating simulation experiments
Name:		%{name}
Version:	%{version}
Release:	%{release}
Source0:	http://www.enthought.com/repo/ets/%{module}-%{version}.tar.gz
Patch0:		blockcanvas-4.0.0-link.patch
License:	BSD
Group:		Development/Python
Url:		https://github.com/enthought/blockcanvas/
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot
Obsoletes:	python-enthought-blockcanvas
Requires:	python-configobj
Requires:	python-apptools >= 4.1.0
Requires:	python-chaco >= 4.2.0
Requires:	python-codetools >= 4.0.0
Requires:	python-etsdevtools >= 4.0.0
Requires:	python-scimath >= 4.1.0
Requires:	python-traitsui >= 4.2.0
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
%__rm -rf %{buildroot}

PYTHONDONTWRITEBYTECODE= %__python setup.py install --root=%{buildroot}

%clean
%__rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc *.txt *.rst docs/build/html/
%py_platsitedir/%{module}*
