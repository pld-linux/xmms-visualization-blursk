# $Revision: 1.2 $
# TODO: configure macro (if it uses ac) or/and optflags
Summary:	Blursk - visualization plugin inspired by Blur Scope
Summary(pl):	Blursk - wtyczka wizualizuj±ca zainspirowana Blur Scope
Name:		xmms-visualization-blursk
Version:	1.3
Release:	0.1
License:	GPL
Group:		X11/Applications/Multimedia
Source0:	http://www.cs.pdx.edu/~kirkenda/blursk/Blursk-%{version}.tar.gz
# Source0-md5:	d5f3b2785ba5148b23ffe335f4560b7e
URL:		http://www.cs.pdx.edu/~kirkenda/blursk/
BuildRequires:	xmms-devel >= 1.2.3
Requires:	xmms
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Blursk is a visualization plugin for the XMMS player. It was inspired
by the "Blur Scope" plugin, but Blursk goes far beyond that. It
supports a wide variety of colormaps, blur patterns, plotting styles,
and other options. The only things that haven't changed are portions
of the XMMS interface and configuration code.

%description -l pl
Blursk to wtyczka wizualizuj±ca dla odtwarzacza XMMS. Jest
zainspirowana wtyczk± "Blur Scope", ale Blursk posuwa siê dalej.
Obs³uguje szeroki zakres map kolorów, wzorów plam, stylów rysowania i
innych opcji. Jedyn± rzecz± która nie zosta³a zmieniona to fragmenty
interfejsu XMMS i kod konfiguracyjny.

%prep
%setup -q -n Blursk-%{version}

%build
./configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	libdir=%{xmms_visualization_plugindir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS NEWS README ChangeLog
%attr(755,root,root) %{xmms_visualization_plugindir}/*.so
