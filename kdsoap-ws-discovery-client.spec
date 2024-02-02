Name:           kdsoap-ws-discovery-client
Version:        0.3.0
Release:        1
Summary:        Library for finding WS-Discovery devices in the network using Qt6 and KDSoap

License:        GPL-3.0-or-later AND LicenseRef-OASIS AND LicenseRef-WS-Addressing AND LicenseRef-Discovery AND W3C
URL:            https://invent.kde.org/libraries/kdsoap-ws-discovery-client/
Source0:        https://download.kde.org/unstable/%{name}/%{name}-%{version}.tar.xz

BuildRequires:  cmake
BuildRequires:  ninja

BuildRequires:  cmake(ECM)
BuildRequires:  cmake(Qt6)
BuildRequires:  cmake(Qt6Core)
BuildRequires:  cmake(Qt6Network)
BuildRequires:	cmake(Qt6Xml)
BuildRequires:  cmake(KDSoap-qt6)

%description
%{summary}.


%package        devel
Summary:        Development libraries and header files for Qt6 %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       cmake(KDSoap-qt6)
%description    devel
%{summary}.

%package        doc
Summary:        Developer Documentation files for %{name}
%description    doc
%{summary}.

%prep
%autosetup -p1
%cmake \
	-DBUILD_WITH_QT6=ON \
	-G Ninja

%build
%ninja_build -C build

%install
%ninja_install -C build

%check
# Tests fail without internet
ctest || :

%files
%doc README.md
%license LICENSES/*
%{_libdir}/libKDSoapWSDiscoveryClient.so.0{,.*}

%files devel
%{_includedir}/KDSoapWSDiscoveryClient/
%{_libdir}/cmake/KDSoapWSDiscoveryClient/
%{_libdir}/libKDSoapWSDiscoveryClient.so

%files doc
%{_docdir}/KDSoapWSDiscoveryClient/
