Summary:	Blursk - visualization plugin inspired by Blur Scope
Summary(pl.UTF-8):	Blursk - wtyczka wizualizująca zainspirowana Blur Scope
Name:		xmms-visualization-blursk
Version:	1.3
Release:	0.1
License:	GPL
Group:		X11/Applications/Multimedia
Source0:	http://www.cs.pdx.edu/~kirkenda/blursk/Blursk-%{version}.tar.gz
# Source0-md5:	d5f3b2785ba5148b23ffe335f4560b7e
URL:		http://www.cs.pdx.edu/~kirkenda/blursk/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	gtk+-devel >= 1.2.2
BuildRequires:	libtool
BuildRequires:	xmms-devel >= 1.2.3
BuildRequires:	xorg-lib-libXv-devel
BuildRequires:	xorg-proto-videoproto-devel
Requires:	xmms
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Blursk is a visualization plugin for the XMMS player. It was inspired
by the "Blur Scope" plugin, but Blursk goes far beyond that. It
supports a wide variety of colormaps, blur patterns, plotting styles,
and other options. The only things that haven't changed are portions
of the XMMS interface and configuration code.

%description -l pl.UTF-8
Blursk to wtyczka wizualizująca dla XMMS-a. Jest zainspirowana wtyczką
"Blur Scope", ale Blursk posuwa się dalej. Obsługuje szeroki zakres
map kolorów, wzorów plam, stylów rysowania i innych opcji. Jedynymi
rzeczami, które nie zostały zmienione, są fragmenty interfejsu XMMS i
kod konfiguracyjny.

%prep
%setup -q -n Blursk-%{version}

%{__perl} -pi -e 's@X11R6/lib"@X11R6/%{_lib}"@' configure.in
%{__perl} -pi -e 's@(AC_PROG_CC)@$1\nAM_PROG_AS@' configure.in
%{__perl} -pi -e 's/\@PTHREAD_LIBS\@/-lpthread/' Makefile.am
rm -f acinclude.m4

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	XMMS_PATH=%{_bindir}/xmms
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	libdir=%{xmms_visualization_plugindir}

rm -f $RPM_BUILD_ROOT%{xmms_visualization_plugindir}/*.la

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS NEWS README ChangeLog
%attr(755,root,root) %{xmms_visualization_plugindir}/*.so
