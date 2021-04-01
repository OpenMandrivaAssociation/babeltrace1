%define _disable_ld_no_undefined 1

%define devname %mklibname -d babeltrace

Summary:	An open source trace format converter
Name:		babeltrace
Version:	1.5.8
Release:	1
License:	GPLv2
Group:		System/Libraries
Url:		http://diamon.org/babeltrace
Source0:	http://www.efficios.com/files/babeltrace/babeltrace-%{version}.tar.bz2
BuildRequires:	pkgconfig(glib-2.0)
BuildRequires:	pkgconfig(libdw)
BuildRequires:	pkgconfig(libelf)
BuildRequires:	pkgconfig(python3)
BuildRequires:	pkgconfig(popt)
BuildRequires:	pkgconfig(uuid)
BuildRequires:	swig

%libpackage babeltrace 1
%libpackage babeltrace-lttng-live 1
%libpackage babeltrace-dummy 1
%libpackage babeltrace-ctf 1
%libpackage babeltrace-ctf-metadata 1
%libpackage babeltrace-ctf-text 1

%description
An open source trace format converter.

%package -n %{devname}
Summary:	Development files for the babeltrace trace format converter
Group:		Development/Other
Provides:	lib%{name} = %{EVRD}
Requires:	%mklibname babeltrace 1
Requires:	%mklibname babeltrace-lttng-live 1
Requires:	%mklibname babeltrace-dummy 1
Requires:	%mklibname babeltrace-ctf 1
Requires:	%mklibname babeltrace-ctf-metadata 1
Requires:	%mklibname babeltrace-ctf-text 1

%description -n %{devname}
Development files for the babeltrace trace format converter.

%package -n python-%{name}
Summary:	Python bindings to the babeltrace trace format converter
Group:		Development/Python

%description -n python-%{name}
Python bindings to the babeltrace trace format converter.

%prep
%autosetup -p1
%configure --enable-python-bindings

%build
%make_build

%install
%make_install

%files
%{_bindir}/babeltrace
%{_bindir}/babeltrace-log

%files -n %{devname}
%{_includedir}/babeltrace
%{_libdir}/*.so
%{_libdir}/pkgconfig/*.pc
%{_mandir}/man1/*
%doc %{_docdir}/%{name}/*

%files -n python-%{name}
%{py_platsitedir}/*.egg-info
%{py_platsitedir}/%{name}/*.so
%{py_platsitedir}/%{name}/*.py
%{py_platsitedir}/%{name}/__pycache__
