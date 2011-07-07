%define module	blockcanvas
%define name 	python-%{module}
%define version 4.0.0
%define release %mkrel 1

Summary: 	Enthought Tool Suite - blockcanvas project
Name:		%{name}
Version:	%{version}
Release:	%{release}
Source0:	http://www.enthought.com/repo/ets/%{module}-%{version}.tar.gz
License:	BSD
Group:		Development/Python
Url:		http://code.enthought.com/projects/block_canvas.php
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot
Obsoletes:	python-enthought-blockcanvas
Requires:	python-configobj
Requires:	python-apptools >= 4.0.0
Requires:	python-chaco >= 4.0.0
Requires:	python-codetools >= 4.0.0
Requires:	python-etsdevtools >= 4.0.0
Requires:	python-scimath >= 4.0.0
Requires:	python-traitsui >= 4.0.0
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

%build

%__python setup.py build
pushd docs
make html
popd

%install
%__rm -rf %{buildroot}

PYTHONDONTWRITEBYTECODE= %__python setup.py install --root=%{buildroot} --record=FILE_LIST

%clean
%__rm -rf %{buildroot}

%files -f FILE_LIST
%defattr(-,root,root)
%doc *.txt *.rst docs/build/html/
