#
# Conditional build:
%bcond_with	gtk3	# use GTK+3 instead of GTK+2

Summary:	LXAppearance ObConf plugin
Summary(pl.UTF-8):	Wtyczka ObConf dla LXAppearance
Name:		lxappearance-obconf
Version:	0.2.3
Release:	1
License:	GPL v2+
Group:		X11/Applications
Source0:	https://downloads.sourceforge.net/lxde/%{name}-%{version}.tar.xz
# Source0-md5:	ae0076d489aa786f5d573f7ff592a4ab
URL:		http://www.lxde.org/
BuildRequires:	gdk-pixbuf2-devel >= 2.0
BuildRequires:	gettext-tools
%{!?with_gtk3:BuildRequires:	gtk+2-devel >= 2:2.12.0}
%{?with_gtk3:BuildRequires:	gtk+3-devel >= 3.0.0}
BuildRequires:	intltool >= 0.40.0
BuildRequires:	lxappearance-devel
BuildRequires:	openbox-devel >= 1:3.5
BuildRequires:	pkgconfig
BuildRequires:	tar >= 1:1.22
BuildRequires:	xz
%{!?with_gtk3:Requires:	gtk+2 >= 2:2.12.0}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
LXAppearance integrated ObConf to provide a better user experience.

ObConf is a program used to configure OpenBox window manager.

%description -l pl.UTF-8
Wtyczka LXAppearance zawierająca zintegrowanego ObConfa w celu
zapewnienia lepszej obsługi.

ObConf to program służący do konfigurowania zarządcy okien OpenBox.

%prep
%setup -q

%build
%configure \
	%{?with_gtk3:--enable-gtk3} \
	--disable-silent-rules \
	--disable-static

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%{__rm} $RPM_BUILD_ROOT%{_libdir}/lxappearance/plugins/obconf.la

# unify name
%{__mv} $RPM_BUILD_ROOT%{_localedir}/{tt_RU,tt}
# duplicate of ur
%{__rm} -r $RPM_BUILD_ROOT%{_localedir}/ur_PK

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS CHANGELOG README
%attr(755,root,root) %{_libdir}/lxappearance/plugins/obconf.so
%{_datadir}/lxappearance/obconf
