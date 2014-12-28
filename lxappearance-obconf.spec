#
# Conditional build:
%bcond_with		gtk3		# build GTK+3 disables GTK+2
%bcond_without		gtk2	# build with GTK+2

%if %{with gtk3}
%undefine	with_gtk2
%endif

Summary:	LXAppearance ObConf plugin
Name:		lxappearance-obconf
Version:	0.2.1
Release:	2
License:	GPL v2
Group:		X11/Applications
Source0:	http://downloads.sourceforge.net/lxde/%{name}-%{version}.tar.gz
# Source0-md5:	1f061c96e0c78a6476421ca294ac24aa
URL:		http://wiki.lxde.org/en/LXAppearance
BuildRequires:	gettext-tools
%{?with_gtk2:BuildRequires:	gtk+2-devel >= 2:2.12.0}
%{?with_gtk3:BuildRequires:	gtk+3-devel}
BuildRequires:	intltool
BuildRequires:	lxappearance-devel
BuildRequires:	openbox-devel
BuildRequires:	pkgconfig
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
LXAppearance integrated ObConf to provide a better user experience.

ObConf is a program used to configure OpenBox window manager.

%prep
%setup -q

%build
%configure \
	--disable-static \
	%{?with_gtk3:--enable-gtk3}
%{__make} V=1

%install
rm -rf $RPM_BUILD_ROOT
%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%{__rm} $RPM_BUILD_ROOT%{_libdir}/lxappearance/plugins/obconf.la
%{__rm} -r $RPM_BUILD_ROOT%{_datadir}/locale/tt_RU

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS CHANGELOG README
%attr(755,root,root) %{_libdir}/lxappearance/plugins/obconf.so
%dir %{_datadir}/lxappearance/obconf
%{_datadir}/lxappearance/obconf/obconf.glade
