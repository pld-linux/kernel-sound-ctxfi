#
# Conditional build:
%bcond_without	dist_kernel		# without distribution kernel
#
%define		_orig_name	ctxfi

%define	_rel	0.1
Summary:	Creative X-Fi driver
Summary(pl.UTF-8):	Sterowniki dla Linuksa dla kart dźwiękowych Creative X-Fi
Name:		kernel%{_alt_kernel}-sound-%{_orig_name}
Version:	1.00
Release:	%{_rel}@%{_kernel_ver_str}
License:	GPL v2
Group:		Base/Kernel
Source0:	http://files2.europe.creative.com/manualdn/Drivers/AVP/10792/0x0343D29A/XFiDrv_Linux_Public_US_%{version}.tar.gz
# Source0-md5:	908cad28ee4fdbee1216e96ff1eba4cc
URL:		http://www.creative.com/
%{?with_dist_kernel:BuildRequires:	kernel-headers}
BuildRequires:	rpmbuild(macros) >= 1.379
%{?with_dist_kernel:%requires_releq_kernel_up}
Requires(post,postun):	/sbin/depmod
Provides:	kernel(ctxfi)
ExclusiveArch:	%{ix86}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Creative X-Fi opensource driver, it supports:
- Creative Sound Blaster X-Fi Titanium Fatal1ty Champion Series
- Creative Sound Blaster X-Fi Titanium Fatal1ty Professional Series
- Creative Sound Blaster X-Fi Titanium Professional Audio
- Creative Sound Blaster X-Fi Titanium
- Creative Sound Blaster X-Fi Elite Pro
- Creative Sound Blaster X-Fi Platinum
- Creative Sound Blaster X-Fi Fatal1ty
- Creative Sound Blaster X-Fi XtremeGamer
- Creative Sound Blaster X-Fi XtremeMusic

%description -l pl.UTF-8
Sterowniki do kart dźwiękowychCreative X-Fi. Wspiera:
- Creative Sound Blaster X-Fi Titanium Fatal1ty Champion Series
- Creative Sound Blaster X-Fi Titanium Fatal1ty Professional Series
- Creative Sound Blaster X-Fi Titanium Professional Audio
- Creative Sound Blaster X-Fi Titanium
- Creative Sound Blaster X-Fi Elite Pro
- Creative Sound Blaster X-Fi Platinum
- Creative Sound Blaster X-Fi Fatal1ty
- Creative Sound Blaster X-Fi XtremeGamer
- Creative Sound Blaster X-Fi XtremeMusic

%prep
%setup -q -n XFiDrv_Linux_Public_US_%{version}

%build
%build_kernel_modules -m ctxfi

%install
rm -rf $RPM_BUILD_ROOT
%install_kernel_modules -m ctxfi -d misc

%clean
rm -rf $RPM_BUILD_ROOT

%post
%depmod %{_kernel_ver}

%postun
%depmod %{_kernel_ver}

%files
%defattr(644,root,root,755)
%doc README
/lib/modules/%{_kernel_ver}/misc/*
