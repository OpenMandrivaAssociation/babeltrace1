%define _disable_ld_no_undefined 1

%define devname %mklibname -d babeltrace1

Summary:	An open source trace format converter
Name:		babeltrace
Version:	1.5.11
Release:	1
License:	GPLv2
Group:		System/Libraries
Url:		http://diamon.org/babeltrace
Source0:	http://www.efficios.com/files/babeltrace/babeltrace-%{version}.tar.bz2
Patch0:		babeltrace-1.5.11-fix-keywords.patch
BuildRequires:	pkgconfig(glib-2.0)
BuildRequires:	pkgconfig(libdw)
BuildRequires:	pkgconfig(libelf)
BuildRequires:	pkgconfig(python)
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
Requires:	%mklibname babeltrace = %{EVRD}
Requires:	%mklibname babeltrace-lttng-live = %{EVRD}
Requires:	%mklibname babeltrace-dummy = %{EVRD}
Requires:	%mklibname babeltrace-ctf = %{EVRD}
Requires:	%mklibname babeltrace-ctf-metadata = %{EVRD}
Requires:	%mklibname babeltrace-ctf-text = %{EVRD}

%description -n %{devname}
Development files for the babeltrace trace format converter.

%package -n python-%{name}
Summary:	Python bindings to the babeltrace trace format converter
Group:		Development/Python

%description -n python-%{name}
Python bindings to the babeltrace trace format converter.

%prep
%autosetup -p1

%build
%configure --enable-python-bindings
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
%doc %{_mandir}/man1/*
%doc %{_docdir}/%{name}/*

%files -n python-%{name}
%{py_platsitedir}/*.egg-info
%dir %{py_platsitedir}/%{name}
%{py_platsitedir}/%{name}/*.so
%{py_platsitedir}/%{name}/*.py
