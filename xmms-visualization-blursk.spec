# $Revision: 1.1 $
Summary:	Blursk
Summary(pl):	Blursk
Name:		xmms-visualization-blursk
Version:	1.3
Release:	1
License:	GPL
Group:		X11/Applications/Multimedia
Source0:	http://www.cs.pdx.edu/~kirkenda/blursk/Blursk-%{version}.tar.gz
# Source0-md5:	d5f3b2785ba5148b23ffe335f4560b7e
URL:		http://www.cs.pdx.edu/~kirkenda/blursk/
BuildRequires:	xmms-devel >= 1.2.3
Requires:	xmms
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Blursk.

%description -l pl
Blursk.

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
