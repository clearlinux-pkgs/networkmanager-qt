#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
# Source0 file verified with key 0x58D0EE648A48B3BB (faure@kde.org)
#
Name     : networkmanager-qt
Version  : 5.57.0
Release  : 15
URL      : https://download.kde.org/stable/frameworks/5.57/networkmanager-qt-5.57.0.tar.xz
Source0  : https://download.kde.org/stable/frameworks/5.57/networkmanager-qt-5.57.0.tar.xz
Source99 : https://download.kde.org/stable/frameworks/5.57/networkmanager-qt-5.57.0.tar.xz.sig
Summary  : Qt wrapper for NetworkManager API
Group    : Development/Tools
License  : LGPL-2.1
Requires: networkmanager-qt-data = %{version}-%{release}
Requires: networkmanager-qt-lib = %{version}-%{release}
Requires: networkmanager-qt-license = %{version}-%{release}
BuildRequires : buildreq-cmake
BuildRequires : buildreq-kde
BuildRequires : pkg-config
BuildRequires : qtbase-dev mesa-dev

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
%setup -q -n networkmanager-qt-5.57.0

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1555349818
mkdir -p clr-build
pushd clr-build
%cmake ..
make  %{?_smp_mflags}
popd

%install
export SOURCE_DATE_EPOCH=1555349818
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/networkmanager-qt
cp COPYING.LIB %{buildroot}/usr/share/package-licenses/networkmanager-qt/COPYING.LIB
pushd clr-build
%make_install
popd

%files
%defattr(-,root,root,-)

%files data
%defattr(-,root,root,-)
/usr/share/xdg/networkmanager-qt.categories

%files dev
%defattr(-,root,root,-)
/usr/include/KF5/NetworkManagerQt/NetworkManagerQt/AccessPoint
/usr/include/KF5/NetworkManagerQt/NetworkManagerQt/ActiveConnection
/usr/include/KF5/NetworkManagerQt/NetworkManagerQt/AdslDevice
/usr/include/KF5/NetworkManagerQt/NetworkManagerQt/AdslSetting
/usr/include/KF5/NetworkManagerQt/NetworkManagerQt/BluetoothDevice
/usr/include/KF5/NetworkManagerQt/NetworkManagerQt/BluetoothSetting
/usr/include/KF5/NetworkManagerQt/NetworkManagerQt/BondDevice
/usr/include/KF5/NetworkManagerQt/NetworkManagerQt/BondSetting
/usr/include/KF5/NetworkManagerQt/NetworkManagerQt/BridgeDevice
/usr/include/KF5/NetworkManagerQt/NetworkManagerQt/BridgePortSetting
/usr/include/KF5/NetworkManagerQt/NetworkManagerQt/BridgeSetting
/usr/include/KF5/NetworkManagerQt/NetworkManagerQt/CdmaSetting
/usr/include/KF5/NetworkManagerQt/NetworkManagerQt/Connection
/usr/include/KF5/NetworkManagerQt/NetworkManagerQt/ConnectionSettings
/usr/include/KF5/NetworkManagerQt/NetworkManagerQt/Device
/usr/include/KF5/NetworkManagerQt/NetworkManagerQt/DeviceStatistics
/usr/include/KF5/NetworkManagerQt/NetworkManagerQt/Dhcp4Config
/usr/include/KF5/NetworkManagerQt/NetworkManagerQt/Dhcp6Config
/usr/include/KF5/NetworkManagerQt/NetworkManagerQt/DnsConfiguration
/usr/include/KF5/NetworkManagerQt/NetworkManagerQt/DnsDomain
/usr/include/KF5/NetworkManagerQt/NetworkManagerQt/GenericDevice
/usr/include/KF5/NetworkManagerQt/NetworkManagerQt/GenericSetting
/usr/include/KF5/NetworkManagerQt/NetworkManagerQt/GenericTypes
/usr/include/KF5/NetworkManagerQt/NetworkManagerQt/GreDevice
/usr/include/KF5/NetworkManagerQt/NetworkManagerQt/GsmSetting
/usr/include/KF5/NetworkManagerQt/NetworkManagerQt/InfinibandDevice
/usr/include/KF5/NetworkManagerQt/NetworkManagerQt/InfinibandSetting
/usr/include/KF5/NetworkManagerQt/NetworkManagerQt/IpAddress
/usr/include/KF5/NetworkManagerQt/NetworkManagerQt/IpConfig
/usr/include/KF5/NetworkManagerQt/NetworkManagerQt/IpRoute
/usr/include/KF5/NetworkManagerQt/NetworkManagerQt/IpTunnelDevice
/usr/include/KF5/NetworkManagerQt/NetworkManagerQt/IpTunnelSetting
/usr/include/KF5/NetworkManagerQt/NetworkManagerQt/Ipv4Setting
/usr/include/KF5/NetworkManagerQt/NetworkManagerQt/Ipv6Setting
/usr/include/KF5/NetworkManagerQt/NetworkManagerQt/MacVlanDevice
/usr/include/KF5/NetworkManagerQt/NetworkManagerQt/Manager
/usr/include/KF5/NetworkManagerQt/NetworkManagerQt/ModemDevice
/usr/include/KF5/NetworkManagerQt/NetworkManagerQt/OlpcMeshDevice
/usr/include/KF5/NetworkManagerQt/NetworkManagerQt/OlpcMeshSetting
/usr/include/KF5/NetworkManagerQt/NetworkManagerQt/PppSetting
/usr/include/KF5/NetworkManagerQt/NetworkManagerQt/PppoeSetting
/usr/include/KF5/NetworkManagerQt/NetworkManagerQt/SecretAgent
/usr/include/KF5/NetworkManagerQt/NetworkManagerQt/Security8021xSetting
/usr/include/KF5/NetworkManagerQt/NetworkManagerQt/SerialSetting
/usr/include/KF5/NetworkManagerQt/NetworkManagerQt/Setting
/usr/include/KF5/NetworkManagerQt/NetworkManagerQt/Settings
/usr/include/KF5/NetworkManagerQt/NetworkManagerQt/TeamDevice
/usr/include/KF5/NetworkManagerQt/NetworkManagerQt/TeamSetting
/usr/include/KF5/NetworkManagerQt/NetworkManagerQt/TunDevice
/usr/include/KF5/NetworkManagerQt/NetworkManagerQt/TunSetting
/usr/include/KF5/NetworkManagerQt/NetworkManagerQt/Utils
/usr/include/KF5/NetworkManagerQt/NetworkManagerQt/VethDevice
/usr/include/KF5/NetworkManagerQt/NetworkManagerQt/VlanDevice
/usr/include/KF5/NetworkManagerQt/NetworkManagerQt/VlanSetting
/usr/include/KF5/NetworkManagerQt/NetworkManagerQt/VpnConnection
/usr/include/KF5/NetworkManagerQt/NetworkManagerQt/VpnPlugin
/usr/include/KF5/NetworkManagerQt/NetworkManagerQt/VpnSetting
/usr/include/KF5/NetworkManagerQt/NetworkManagerQt/WimaxDevice
/usr/include/KF5/NetworkManagerQt/NetworkManagerQt/WimaxNsp
/usr/include/KF5/NetworkManagerQt/NetworkManagerQt/WimaxSetting
/usr/include/KF5/NetworkManagerQt/NetworkManagerQt/WiredDevice
/usr/include/KF5/NetworkManagerQt/NetworkManagerQt/WiredSetting
/usr/include/KF5/NetworkManagerQt/NetworkManagerQt/WireguardSetting
/usr/include/KF5/NetworkManagerQt/NetworkManagerQt/WirelessDevice
/usr/include/KF5/NetworkManagerQt/NetworkManagerQt/WirelessNetwork
/usr/include/KF5/NetworkManagerQt/NetworkManagerQt/WirelessSecuritySetting
/usr/include/KF5/NetworkManagerQt/NetworkManagerQt/WirelessSetting
/usr/include/KF5/NetworkManagerQt/networkmanagerqt/accesspoint.h
/usr/include/KF5/NetworkManagerQt/networkmanagerqt/activeconnection.h
/usr/include/KF5/NetworkManagerQt/networkmanagerqt/adsldevice.h
/usr/include/KF5/NetworkManagerQt/networkmanagerqt/adslsetting.h
/usr/include/KF5/NetworkManagerQt/networkmanagerqt/bluetoothdevice.h
/usr/include/KF5/NetworkManagerQt/networkmanagerqt/bluetoothsetting.h
/usr/include/KF5/NetworkManagerQt/networkmanagerqt/bonddevice.h
/usr/include/KF5/NetworkManagerQt/networkmanagerqt/bondsetting.h
/usr/include/KF5/NetworkManagerQt/networkmanagerqt/bridgedevice.h
/usr/include/KF5/NetworkManagerQt/networkmanagerqt/bridgeportsetting.h
/usr/include/KF5/NetworkManagerQt/networkmanagerqt/bridgesetting.h
/usr/include/KF5/NetworkManagerQt/networkmanagerqt/cdmasetting.h
/usr/include/KF5/NetworkManagerQt/networkmanagerqt/connection.h
/usr/include/KF5/NetworkManagerQt/networkmanagerqt/connectionsettings.h
/usr/include/KF5/NetworkManagerQt/networkmanagerqt/device.h
/usr/include/KF5/NetworkManagerQt/networkmanagerqt/devicestatistics.h
/usr/include/KF5/NetworkManagerQt/networkmanagerqt/dhcp4config.h
/usr/include/KF5/NetworkManagerQt/networkmanagerqt/dhcp6config.h
/usr/include/KF5/NetworkManagerQt/networkmanagerqt/dnsconfiguration.h
/usr/include/KF5/NetworkManagerQt/networkmanagerqt/dnsdomain.h
/usr/include/KF5/NetworkManagerQt/networkmanagerqt/genericdevice.h
/usr/include/KF5/NetworkManagerQt/networkmanagerqt/genericsetting.h
/usr/include/KF5/NetworkManagerQt/networkmanagerqt/generictypes.h
/usr/include/KF5/NetworkManagerQt/networkmanagerqt/gredevice.h
/usr/include/KF5/NetworkManagerQt/networkmanagerqt/gsmsetting.h
/usr/include/KF5/NetworkManagerQt/networkmanagerqt/infinibanddevice.h
/usr/include/KF5/NetworkManagerQt/networkmanagerqt/infinibandsetting.h
/usr/include/KF5/NetworkManagerQt/networkmanagerqt/ipaddress.h
/usr/include/KF5/NetworkManagerQt/networkmanagerqt/ipconfig.h
/usr/include/KF5/NetworkManagerQt/networkmanagerqt/iproute.h
/usr/include/KF5/NetworkManagerQt/networkmanagerqt/iptunneldevice.h
/usr/include/KF5/NetworkManagerQt/networkmanagerqt/iptunnelsetting.h
/usr/include/KF5/NetworkManagerQt/networkmanagerqt/ipv4setting.h
/usr/include/KF5/NetworkManagerQt/networkmanagerqt/ipv6setting.h
/usr/include/KF5/NetworkManagerQt/networkmanagerqt/macvlandevice.h
/usr/include/KF5/NetworkManagerQt/networkmanagerqt/manager.h
/usr/include/KF5/NetworkManagerQt/networkmanagerqt/modemdevice.h
/usr/include/KF5/NetworkManagerQt/networkmanagerqt/networkmanagerqt_export.h
/usr/include/KF5/NetworkManagerQt/networkmanagerqt/olpcmeshdevice.h
/usr/include/KF5/NetworkManagerQt/networkmanagerqt/olpcmeshsetting.h
/usr/include/KF5/NetworkManagerQt/networkmanagerqt/pppoesetting.h
/usr/include/KF5/NetworkManagerQt/networkmanagerqt/pppsetting.h
/usr/include/KF5/NetworkManagerQt/networkmanagerqt/secretagent.h
/usr/include/KF5/NetworkManagerQt/networkmanagerqt/security8021xsetting.h
/usr/include/KF5/NetworkManagerQt/networkmanagerqt/serialsetting.h
/usr/include/KF5/NetworkManagerQt/networkmanagerqt/setting.h
/usr/include/KF5/NetworkManagerQt/networkmanagerqt/settings.h
/usr/include/KF5/NetworkManagerQt/networkmanagerqt/teamdevice.h
/usr/include/KF5/NetworkManagerQt/networkmanagerqt/teamsetting.h
/usr/include/KF5/NetworkManagerQt/networkmanagerqt/tundevice.h
/usr/include/KF5/NetworkManagerQt/networkmanagerqt/tunsetting.h
/usr/include/KF5/NetworkManagerQt/networkmanagerqt/utils.h
/usr/include/KF5/NetworkManagerQt/networkmanagerqt/vethdevice.h
/usr/include/KF5/NetworkManagerQt/networkmanagerqt/vlandevice.h
/usr/include/KF5/NetworkManagerQt/networkmanagerqt/vlansetting.h
/usr/include/KF5/NetworkManagerQt/networkmanagerqt/vpnconnection.h
/usr/include/KF5/NetworkManagerQt/networkmanagerqt/vpnplugin.h
/usr/include/KF5/NetworkManagerQt/networkmanagerqt/vpnsetting.h
/usr/include/KF5/NetworkManagerQt/networkmanagerqt/wimaxdevice.h
/usr/include/KF5/NetworkManagerQt/networkmanagerqt/wimaxnsp.h
/usr/include/KF5/NetworkManagerQt/networkmanagerqt/wimaxsetting.h
/usr/include/KF5/NetworkManagerQt/networkmanagerqt/wireddevice.h
/usr/include/KF5/NetworkManagerQt/networkmanagerqt/wiredsetting.h
/usr/include/KF5/NetworkManagerQt/networkmanagerqt/wireguardsetting.h
/usr/include/KF5/NetworkManagerQt/networkmanagerqt/wirelessdevice.h
/usr/include/KF5/NetworkManagerQt/networkmanagerqt/wirelessnetwork.h
/usr/include/KF5/NetworkManagerQt/networkmanagerqt/wirelesssecuritysetting.h
/usr/include/KF5/NetworkManagerQt/networkmanagerqt/wirelesssetting.h
/usr/include/KF5/networkmanagerqt_version.h
/usr/lib64/cmake/KF5NetworkManagerQt/KF5NetworkManagerQtConfig.cmake
/usr/lib64/cmake/KF5NetworkManagerQt/KF5NetworkManagerQtConfigVersion.cmake
/usr/lib64/cmake/KF5NetworkManagerQt/KF5NetworkManagerQtTargets-relwithdebinfo.cmake
/usr/lib64/cmake/KF5NetworkManagerQt/KF5NetworkManagerQtTargets.cmake
/usr/lib64/libKF5NetworkManagerQt.so
/usr/lib64/qt5/mkspecs/modules/qt_NetworkManagerQt.pri

%files lib
%defattr(-,root,root,-)
/usr/lib64/libKF5NetworkManagerQt.so.5.57.0
/usr/lib64/libKF5NetworkManagerQt.so.6

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/networkmanager-qt/COPYING.LIB
