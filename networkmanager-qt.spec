#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: cmake
# autospec version: v21
# autospec commit: 5424026
#
# Source0 file verified with key 0x2C8DF587A6D4AAC1 (nicolas.fella@kde.org)
#
Name     : networkmanager-qt
Version  : 6.9.0
Release  : 90
URL      : https://download.kde.org/stable/frameworks/6.9/networkmanager-qt-6.9.0.tar.xz
Source0  : https://download.kde.org/stable/frameworks/6.9/networkmanager-qt-6.9.0.tar.xz
Source1  : https://download.kde.org/stable/frameworks/6.9/networkmanager-qt-6.9.0.tar.xz.sig
Source2  : 2C8DF587A6D4AAC1.pkey
Summary  : No detailed summary available
Group    : Development/Tools
License  : BSD-3-Clause CC0-1.0 GPL-2.0 GPL-3.0 LGPL-2.1 LGPL-3.0
Requires: networkmanager-qt-data = %{version}-%{release}
Requires: networkmanager-qt-lib = %{version}-%{release}
Requires: networkmanager-qt-license = %{version}-%{release}
BuildRequires : NetworkManager-dev
BuildRequires : buildreq-cmake
BuildRequires : buildreq-kde
BuildRequires : extra-cmake-modules-data
BuildRequires : gnupg
BuildRequires : pkg-config
BuildRequires : qt6base-dev
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

%description
# NetworkManagerQt
Qt wrapper for NetworkManager DBus API.
## Introduction
NetworkManagerQt provides access to all NetworkManager features
exposed on DBus. It allows you to manage your connections and control
your network devices and also provides a library for parsing connection
settings which are used in DBus communication.

%package data
Summary: data components for the networkmanager-qt package.
Group: Data

%description data
data components for the networkmanager-qt package.


%package dev
Summary: dev components for the networkmanager-qt package.
Group: Development
Requires: networkmanager-qt-lib = %{version}-%{release}
Requires: networkmanager-qt-data = %{version}-%{release}
Provides: networkmanager-qt-devel = %{version}-%{release}
Requires: networkmanager-qt = %{version}-%{release}

%description dev
dev components for the networkmanager-qt package.


%package lib
Summary: lib components for the networkmanager-qt package.
Group: Libraries
Requires: networkmanager-qt-data = %{version}-%{release}
Requires: networkmanager-qt-license = %{version}-%{release}

%description lib
lib components for the networkmanager-qt package.


%package license
Summary: license components for the networkmanager-qt package.
Group: Default

%description license
license components for the networkmanager-qt package.


%prep
mkdir .gnupg
chmod 700 .gnupg
gpg --homedir .gnupg --import %{SOURCE2}
gpg --homedir .gnupg --status-fd 1 --verify %{SOURCE1} %{SOURCE0} > gpg.status
grep -E '^\[GNUPG:\] (GOODSIG|EXPKEYSIG) 2C8DF587A6D4AAC1' gpg.status
%setup -q -n networkmanager-qt-6.9.0
cd %{_builddir}/networkmanager-qt-6.9.0
pushd ..
cp -a networkmanager-qt-6.9.0 buildavx2
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1735238078
mkdir -p clr-build
pushd clr-build
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
export GOAMD64=v2
%cmake ..   -G 'Unix Makefiles'
make  %{?_smp_mflags}
popd
pushd ../buildavx2/
mkdir -p clr-build-avx2
pushd clr-build-avx2
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
GOAMD64=v3
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -march=x86-64-v3 -Wl,-z,x86-64-v3 "
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -march=x86-64-v3 -Wl,-z,x86-64-v3 "
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -march=x86-64-v3 -Wl,-z,x86-64-v3 "
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS -march=x86-64-v3 "
%cmake ..   -G 'Unix Makefiles'
make  %{?_smp_mflags}
popd
popd

%install
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
export SOURCE_DATE_EPOCH=1735238078
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/networkmanager-qt
cp %{_builddir}/networkmanager-qt-%{version}/LICENSES/BSD-3-Clause.txt %{buildroot}/usr/share/package-licenses/networkmanager-qt/9950d3fdce1cff1f71212fb5abd31453c6ee2f8c || :
cp %{_builddir}/networkmanager-qt-%{version}/LICENSES/CC0-1.0.txt %{buildroot}/usr/share/package-licenses/networkmanager-qt/82da472f6d00dc5f0a651f33ebb320aa9c7b08d0 || :
cp %{_builddir}/networkmanager-qt-%{version}/LICENSES/GPL-2.0-only.txt %{buildroot}/usr/share/package-licenses/networkmanager-qt/2a638514c87c4923c0570c55822620fad56f2a33 || :
cp %{_builddir}/networkmanager-qt-%{version}/LICENSES/GPL-3.0-only.txt %{buildroot}/usr/share/package-licenses/networkmanager-qt/6091db0aead0d90182b93d3c0d09ba93d188f907 || :
cp %{_builddir}/networkmanager-qt-%{version}/LICENSES/LGPL-2.1-only.txt %{buildroot}/usr/share/package-licenses/networkmanager-qt/3c3d7573e137d48253731c975ecf90d74cfa9efe || :
cp %{_builddir}/networkmanager-qt-%{version}/LICENSES/LGPL-3.0-only.txt %{buildroot}/usr/share/package-licenses/networkmanager-qt/757b86330df80f81143d5916b3e92b4bcb1b1890 || :
cp %{_builddir}/networkmanager-qt-%{version}/LICENSES/LicenseRef-KDE-Accepted-GPL.txt %{buildroot}/usr/share/package-licenses/networkmanager-qt/7d9831e05094ce723947d729c2a46a09d6e90275 || :
cp %{_builddir}/networkmanager-qt-%{version}/LICENSES/LicenseRef-KDE-Accepted-GPL.txt %{buildroot}/usr/share/package-licenses/networkmanager-qt/7d9831e05094ce723947d729c2a46a09d6e90275 || :
cp %{_builddir}/networkmanager-qt-%{version}/LICENSES/LicenseRef-KDE-Accepted-LGPL.txt %{buildroot}/usr/share/package-licenses/networkmanager-qt/e458941548e0864907e654fa2e192844ae90fc32 || :
cp %{_builddir}/networkmanager-qt-%{version}/LICENSES/LicenseRef-KDE-Accepted-LGPL.txt %{buildroot}/usr/share/package-licenses/networkmanager-qt/e458941548e0864907e654fa2e192844ae90fc32 || :
export GOAMD64=v2
pushd ../buildavx2/
GOAMD64=v3
pushd clr-build-avx2
%make_install_v3  || :
popd
popd
GOAMD64=v2
pushd clr-build
%make_install
popd
/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)

%files data
%defattr(-,root,root,-)
/usr/share/qlogging-categories6/networkmanagerqt.categories
/usr/share/qlogging-categories6/networkmanagerqt.renamecategories

%files dev
%defattr(-,root,root,-)
/usr/include/KF6/NetworkManagerQt/NetworkManagerQt/AccessPoint
/usr/include/KF6/NetworkManagerQt/NetworkManagerQt/ActiveConnection
/usr/include/KF6/NetworkManagerQt/NetworkManagerQt/AdslDevice
/usr/include/KF6/NetworkManagerQt/NetworkManagerQt/AdslSetting
/usr/include/KF6/NetworkManagerQt/NetworkManagerQt/BluetoothDevice
/usr/include/KF6/NetworkManagerQt/NetworkManagerQt/BluetoothSetting
/usr/include/KF6/NetworkManagerQt/NetworkManagerQt/BondDevice
/usr/include/KF6/NetworkManagerQt/NetworkManagerQt/BondSetting
/usr/include/KF6/NetworkManagerQt/NetworkManagerQt/BridgeDevice
/usr/include/KF6/NetworkManagerQt/NetworkManagerQt/BridgePortSetting
/usr/include/KF6/NetworkManagerQt/NetworkManagerQt/BridgeSetting
/usr/include/KF6/NetworkManagerQt/NetworkManagerQt/CdmaSetting
/usr/include/KF6/NetworkManagerQt/NetworkManagerQt/Connection
/usr/include/KF6/NetworkManagerQt/NetworkManagerQt/ConnectionSettings
/usr/include/KF6/NetworkManagerQt/NetworkManagerQt/Device
/usr/include/KF6/NetworkManagerQt/NetworkManagerQt/DeviceStatistics
/usr/include/KF6/NetworkManagerQt/NetworkManagerQt/Dhcp4Config
/usr/include/KF6/NetworkManagerQt/NetworkManagerQt/Dhcp6Config
/usr/include/KF6/NetworkManagerQt/NetworkManagerQt/DnsConfiguration
/usr/include/KF6/NetworkManagerQt/NetworkManagerQt/DnsDomain
/usr/include/KF6/NetworkManagerQt/NetworkManagerQt/GenericDevice
/usr/include/KF6/NetworkManagerQt/NetworkManagerQt/GenericSetting
/usr/include/KF6/NetworkManagerQt/NetworkManagerQt/GenericTypes
/usr/include/KF6/NetworkManagerQt/NetworkManagerQt/GreDevice
/usr/include/KF6/NetworkManagerQt/NetworkManagerQt/GsmSetting
/usr/include/KF6/NetworkManagerQt/NetworkManagerQt/InfinibandDevice
/usr/include/KF6/NetworkManagerQt/NetworkManagerQt/InfinibandSetting
/usr/include/KF6/NetworkManagerQt/NetworkManagerQt/IpAddress
/usr/include/KF6/NetworkManagerQt/NetworkManagerQt/IpConfig
/usr/include/KF6/NetworkManagerQt/NetworkManagerQt/IpRoute
/usr/include/KF6/NetworkManagerQt/NetworkManagerQt/IpTunnelDevice
/usr/include/KF6/NetworkManagerQt/NetworkManagerQt/IpTunnelSetting
/usr/include/KF6/NetworkManagerQt/NetworkManagerQt/Ipv4Setting
/usr/include/KF6/NetworkManagerQt/NetworkManagerQt/Ipv6Setting
/usr/include/KF6/NetworkManagerQt/NetworkManagerQt/MacVlanDevice
/usr/include/KF6/NetworkManagerQt/NetworkManagerQt/Manager
/usr/include/KF6/NetworkManagerQt/NetworkManagerQt/ModemDevice
/usr/include/KF6/NetworkManagerQt/NetworkManagerQt/OlpcMeshDevice
/usr/include/KF6/NetworkManagerQt/NetworkManagerQt/OlpcMeshSetting
/usr/include/KF6/NetworkManagerQt/NetworkManagerQt/PppSetting
/usr/include/KF6/NetworkManagerQt/NetworkManagerQt/PppoeSetting
/usr/include/KF6/NetworkManagerQt/NetworkManagerQt/SecretAgent
/usr/include/KF6/NetworkManagerQt/NetworkManagerQt/Security8021xSetting
/usr/include/KF6/NetworkManagerQt/NetworkManagerQt/SerialSetting
/usr/include/KF6/NetworkManagerQt/NetworkManagerQt/Setting
/usr/include/KF6/NetworkManagerQt/NetworkManagerQt/Settings
/usr/include/KF6/NetworkManagerQt/NetworkManagerQt/TeamDevice
/usr/include/KF6/NetworkManagerQt/NetworkManagerQt/TeamSetting
/usr/include/KF6/NetworkManagerQt/NetworkManagerQt/TunDevice
/usr/include/KF6/NetworkManagerQt/NetworkManagerQt/TunSetting
/usr/include/KF6/NetworkManagerQt/NetworkManagerQt/Utils
/usr/include/KF6/NetworkManagerQt/NetworkManagerQt/VethDevice
/usr/include/KF6/NetworkManagerQt/NetworkManagerQt/VlanDevice
/usr/include/KF6/NetworkManagerQt/NetworkManagerQt/VlanSetting
/usr/include/KF6/NetworkManagerQt/NetworkManagerQt/VpnConnection
/usr/include/KF6/NetworkManagerQt/NetworkManagerQt/VpnPlugin
/usr/include/KF6/NetworkManagerQt/NetworkManagerQt/VpnSetting
/usr/include/KF6/NetworkManagerQt/NetworkManagerQt/WimaxDevice
/usr/include/KF6/NetworkManagerQt/NetworkManagerQt/WimaxNsp
/usr/include/KF6/NetworkManagerQt/NetworkManagerQt/WimaxSetting
/usr/include/KF6/NetworkManagerQt/NetworkManagerQt/WireGuardDevice
/usr/include/KF6/NetworkManagerQt/NetworkManagerQt/WiredDevice
/usr/include/KF6/NetworkManagerQt/NetworkManagerQt/WiredSetting
/usr/include/KF6/NetworkManagerQt/NetworkManagerQt/WireguardSetting
/usr/include/KF6/NetworkManagerQt/NetworkManagerQt/WirelessDevice
/usr/include/KF6/NetworkManagerQt/NetworkManagerQt/WirelessNetwork
/usr/include/KF6/NetworkManagerQt/NetworkManagerQt/WirelessSecuritySetting
/usr/include/KF6/NetworkManagerQt/NetworkManagerQt/WirelessSetting
/usr/include/KF6/NetworkManagerQt/networkmanagerqt/accesspoint.h
/usr/include/KF6/NetworkManagerQt/networkmanagerqt/activeconnection.h
/usr/include/KF6/NetworkManagerQt/networkmanagerqt/adsldevice.h
/usr/include/KF6/NetworkManagerQt/networkmanagerqt/adslsetting.h
/usr/include/KF6/NetworkManagerQt/networkmanagerqt/bluetoothdevice.h
/usr/include/KF6/NetworkManagerQt/networkmanagerqt/bluetoothsetting.h
/usr/include/KF6/NetworkManagerQt/networkmanagerqt/bonddevice.h
/usr/include/KF6/NetworkManagerQt/networkmanagerqt/bondsetting.h
/usr/include/KF6/NetworkManagerQt/networkmanagerqt/bridgedevice.h
/usr/include/KF6/NetworkManagerQt/networkmanagerqt/bridgeportsetting.h
/usr/include/KF6/NetworkManagerQt/networkmanagerqt/bridgesetting.h
/usr/include/KF6/NetworkManagerQt/networkmanagerqt/cdmasetting.h
/usr/include/KF6/NetworkManagerQt/networkmanagerqt/connection.h
/usr/include/KF6/NetworkManagerQt/networkmanagerqt/connectionsettings.h
/usr/include/KF6/NetworkManagerQt/networkmanagerqt/device.h
/usr/include/KF6/NetworkManagerQt/networkmanagerqt/devicestatistics.h
/usr/include/KF6/NetworkManagerQt/networkmanagerqt/dhcp4config.h
/usr/include/KF6/NetworkManagerQt/networkmanagerqt/dhcp6config.h
/usr/include/KF6/NetworkManagerQt/networkmanagerqt/dnsconfiguration.h
/usr/include/KF6/NetworkManagerQt/networkmanagerqt/dnsdomain.h
/usr/include/KF6/NetworkManagerQt/networkmanagerqt/genericdevice.h
/usr/include/KF6/NetworkManagerQt/networkmanagerqt/genericsetting.h
/usr/include/KF6/NetworkManagerQt/networkmanagerqt/generictypes.h
/usr/include/KF6/NetworkManagerQt/networkmanagerqt/gredevice.h
/usr/include/KF6/NetworkManagerQt/networkmanagerqt/gsmsetting.h
/usr/include/KF6/NetworkManagerQt/networkmanagerqt/infinibanddevice.h
/usr/include/KF6/NetworkManagerQt/networkmanagerqt/infinibandsetting.h
/usr/include/KF6/NetworkManagerQt/networkmanagerqt/ipaddress.h
/usr/include/KF6/NetworkManagerQt/networkmanagerqt/ipconfig.h
/usr/include/KF6/NetworkManagerQt/networkmanagerqt/iproute.h
/usr/include/KF6/NetworkManagerQt/networkmanagerqt/iptunneldevice.h
/usr/include/KF6/NetworkManagerQt/networkmanagerqt/iptunnelsetting.h
/usr/include/KF6/NetworkManagerQt/networkmanagerqt/ipv4setting.h
/usr/include/KF6/NetworkManagerQt/networkmanagerqt/ipv6setting.h
/usr/include/KF6/NetworkManagerQt/networkmanagerqt/macvlandevice.h
/usr/include/KF6/NetworkManagerQt/networkmanagerqt/manager.h
/usr/include/KF6/NetworkManagerQt/networkmanagerqt/modemdevice.h
/usr/include/KF6/NetworkManagerQt/networkmanagerqt/networkmanagerqt_export.h
/usr/include/KF6/NetworkManagerQt/networkmanagerqt/olpcmeshdevice.h
/usr/include/KF6/NetworkManagerQt/networkmanagerqt/olpcmeshsetting.h
/usr/include/KF6/NetworkManagerQt/networkmanagerqt/pppoesetting.h
/usr/include/KF6/NetworkManagerQt/networkmanagerqt/pppsetting.h
/usr/include/KF6/NetworkManagerQt/networkmanagerqt/secretagent.h
/usr/include/KF6/NetworkManagerQt/networkmanagerqt/security8021xsetting.h
/usr/include/KF6/NetworkManagerQt/networkmanagerqt/serialsetting.h
/usr/include/KF6/NetworkManagerQt/networkmanagerqt/setting.h
/usr/include/KF6/NetworkManagerQt/networkmanagerqt/settings.h
/usr/include/KF6/NetworkManagerQt/networkmanagerqt/teamdevice.h
/usr/include/KF6/NetworkManagerQt/networkmanagerqt/teamsetting.h
/usr/include/KF6/NetworkManagerQt/networkmanagerqt/tundevice.h
/usr/include/KF6/NetworkManagerQt/networkmanagerqt/tunsetting.h
/usr/include/KF6/NetworkManagerQt/networkmanagerqt/utils.h
/usr/include/KF6/NetworkManagerQt/networkmanagerqt/vethdevice.h
/usr/include/KF6/NetworkManagerQt/networkmanagerqt/vlandevice.h
/usr/include/KF6/NetworkManagerQt/networkmanagerqt/vlansetting.h
/usr/include/KF6/NetworkManagerQt/networkmanagerqt/vpnconnection.h
/usr/include/KF6/NetworkManagerQt/networkmanagerqt/vpnplugin.h
/usr/include/KF6/NetworkManagerQt/networkmanagerqt/vpnsetting.h
/usr/include/KF6/NetworkManagerQt/networkmanagerqt/wimaxdevice.h
/usr/include/KF6/NetworkManagerQt/networkmanagerqt/wimaxnsp.h
/usr/include/KF6/NetworkManagerQt/networkmanagerqt/wimaxsetting.h
/usr/include/KF6/NetworkManagerQt/networkmanagerqt/wireddevice.h
/usr/include/KF6/NetworkManagerQt/networkmanagerqt/wiredsetting.h
/usr/include/KF6/NetworkManagerQt/networkmanagerqt/wireguarddevice.h
/usr/include/KF6/NetworkManagerQt/networkmanagerqt/wireguardsetting.h
/usr/include/KF6/NetworkManagerQt/networkmanagerqt/wirelessdevice.h
/usr/include/KF6/NetworkManagerQt/networkmanagerqt/wirelessnetwork.h
/usr/include/KF6/NetworkManagerQt/networkmanagerqt/wirelesssecuritysetting.h
/usr/include/KF6/NetworkManagerQt/networkmanagerqt/wirelesssetting.h
/usr/include/KF6/NetworkManagerQt/networkmanagerqt_version.h
/usr/lib64/cmake/KF6NetworkManagerQt/KF6NetworkManagerQtConfig.cmake
/usr/lib64/cmake/KF6NetworkManagerQt/KF6NetworkManagerQtConfigVersion.cmake
/usr/lib64/cmake/KF6NetworkManagerQt/KF6NetworkManagerQtTargets-relwithdebinfo.cmake
/usr/lib64/cmake/KF6NetworkManagerQt/KF6NetworkManagerQtTargets.cmake
/usr/lib64/libKF6NetworkManagerQt.so

%files lib
%defattr(-,root,root,-)
/V3/usr/lib64/libKF6NetworkManagerQt.so.6.9.0
/V3/usr/lib64/qt6/qml/org/kde/networkmanager/libnetworkmanagerqtqml.so
/usr/lib64/libKF6NetworkManagerQt.so.6
/usr/lib64/libKF6NetworkManagerQt.so.6.9.0
/usr/lib64/qt6/qml/org/kde/networkmanager/kde-qmlmodule.version
/usr/lib64/qt6/qml/org/kde/networkmanager/libnetworkmanagerqtqml.so
/usr/lib64/qt6/qml/org/kde/networkmanager/networkmanagerqtqml.qmltypes
/usr/lib64/qt6/qml/org/kde/networkmanager/qmldir

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/networkmanager-qt/2a638514c87c4923c0570c55822620fad56f2a33
/usr/share/package-licenses/networkmanager-qt/3c3d7573e137d48253731c975ecf90d74cfa9efe
/usr/share/package-licenses/networkmanager-qt/6091db0aead0d90182b93d3c0d09ba93d188f907
/usr/share/package-licenses/networkmanager-qt/757b86330df80f81143d5916b3e92b4bcb1b1890
/usr/share/package-licenses/networkmanager-qt/7d9831e05094ce723947d729c2a46a09d6e90275
/usr/share/package-licenses/networkmanager-qt/82da472f6d00dc5f0a651f33ebb320aa9c7b08d0
/usr/share/package-licenses/networkmanager-qt/9950d3fdce1cff1f71212fb5abd31453c6ee2f8c
/usr/share/package-licenses/networkmanager-qt/e458941548e0864907e654fa2e192844ae90fc32
