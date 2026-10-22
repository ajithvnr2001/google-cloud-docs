---
url: https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/installing/package-server/
title: Use a private package repository server \u00a0|\u00a0 Google Distributed Cloud software only for bare metal \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:57:15.393000+00:00
---

# Use a private package repository server  |  Google Distributed Cloud software only for bare metal  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/installing/package-server/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Distributed, hybrid, and multicloud ](https://docs.cloud.google.com/docs/dhm-cloud)
  * [ Google Distributed Cloud ](https://docs.cloud.google.com/distributed-cloud/docs)
  * [ GDC for bare metal ](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs)
  * [ Guides ](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/concepts/about-bare-metal)



Send feedback 

#  Use a private package repository server Stay organized with collections  Save and categorize content based on your preferences. 

Google Distributed Cloud supports using your own private package repository server. Use this feature to skip adding package repositories to each bare metal machine in your deployment. To ensure Google Distributed Cloud has all the required packages available, this page lists all the packages and dependencies you need to prepare in your private package repository server.

## Before you begin

Ensure your package repository includes all needed packages and dependencies for your Linux distribution.

Ensure that all your bare metal machines can reach and already use your own package repository server.

## Skip adding the default package repository

By default, Google Distributed Cloud adds a Docker repository for Linux (`apt` or `rpm`, depending on the operating system) and the needed GPG key to your machines.

To use your own package repository instead, set the `addPackageRepo` field to `false` under the `osEnvironmentConfig` section in your cluster's configuration file.

The entry in your configuration should look similar to the following example:
    
    
    apiVersion: baremetal.cluster.gke.io/v1
    kind: Cluster
    metadata:
      name: cluster1
      namespace: cluster-cluster1
    spec:
      osEnvironmentConfig:
        addPackageRepo: false
    

## Needed packages and their dependencies

Google Distributed Cloud tries to install the following packages in your machines. Your private package repository server must contain all the packages and their dependencies with the versions listed in the following table for your operating system:

### Ubuntu 20.04 and 22.04

Package | Dependencies  
---|---  
python3 (>= 3.6.7-1) | python3.6 (>= 3.6.7-1~)  
libpython3-stdlib (= 3.6.7-1~18.04)  
  
apt-transport-https (>= 1.6.12) | apt (>= 1.5)  
ca-certificates (>=20210119) | openssl (>= 1.1.0)  
debconf (>= 0.5) | debconf-2.0  
  
conntrack (>= 1:1.4.4+snapshot20161117-6) | libc6 (>= 2.14)  
libmnl0 (>= 1.0.3-4~)  
libnetfilter-conntrack3  
libnfnetlink  
  
curl (>= 7.58.0) | libc6 (>= 2.17)  
libcurl4 (= 7.58.0-2ubuntu3.12)  
zlib1g (>= 1:1.1.4)  
  
software-properties-common (>= 0.96.24.32.14) | python3:any (>= 3.3.2-2~)  
python3  
python3-gi  
gir1.2-glib-2.0  
python-apt-common (>= 0.9)  
python3-dbus  
python3-software-properties (= 0.96.24.32.14)  
ca-certificates  
  
gnupg2 (>= 2.2.4) | gnupg (>= 2.2.4-1ubuntu1.4)  
socat (>= 1.7.3.2) | libc6 (>= 2.15)  
libssl1.1 (>= 1.1.0)  
libwrap0 (>= 7.6-4~)  
  
iproute2 (>= 4.15.0) | libc6 (>= 2.27)  
libdb5.3  
libelf1 (>= 0.131)  
libmnl0 (>= 1.0.3-4~)  
libselinux1 (>= 2.0.15)  
  
ebtables (>= 2.0.10.4-3.5) | libc6 (>= 2.14)  
ethtool (>= 1:4.15-0) |   
logrotate (>= 3.11.0) | libacl1 (>= 2.2.51-8)  
libc6 (>= 2.14)  
libpopt0 (>= 1.14)  
libselinux1 (>= 1.32)  
cron | anacron | cron-daemon  
base-passwd (>= 2.0.3.4)  
  
libseccomp-dev (>= 2.5) | libseccomp2  
  
###  RHEL 9 

**Note:** Google Distributed Cloud supports RHEL 9 as [Preview](https://cloud.google.com/products/#product-launch-stages) for release 1.28. For more information, see [Select your operating system](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/installing/os-reqs).Package | Dependencies  
---|---  
python36 (>= 3.6.8) | /bin/sh  
/usr/libexec/platform-python  
/usr/sbin/alternatives  
python3-pip  
python3-setuptools  
conntrack (>= 1.4.4-10.el9) | /bin/sh  
libc.so.6(GLIBC_2.15)(64bit)  
libdl.so.2()(64bit)  
libdl.so.2(GLIBC_2.2.5)(64bit)  
libmnl.so.0()(64bit)  
libmnl.so.0(LIBMNL_1.0)(64bit)  
libnetfilter_conntrack.so.3()(64bit)  
libnetfilter_cthelper.so.0()(64bit)  
libnetfilter_cthelper.so.0(LIBNETFILTER_CTHELPER_1.0)(64bit)  
libnetfilter_cttimeout.so.1()(64bit)  
libnetfilter_cttimeout.so.1(LIBNETFILTER_CTTIMEOUT_1.0)(64bit)  
libnetfilter_cttimeout.so.1(LIBNETFILTER_CTTIMEOUT_1.1)(64bit)  
libnetfilter_queue.so.1()(64bit)  
libnfnetlink.so.0()(64bit)  
libsystemd.so.0()(64bit)  
libsystemd.so.0(LIBSYSTEMD_209)(64bit)  
rtld(GNU_HASH)  
systemd  
device-mapper-persistent-data (>= 0.8.5-4.el9) | expat  
libaio.so.1()(64bit)  
libaio.so.1(LIBAIO_0.1)(64bit)  
libaio.so.1(LIBAIO_0.4)(64bit)  
libc.so.6(GLIBC_2.16)(64bit)  
libdl.so.2()(64bit)  
libdl.so.2(GLIBC_2.2.5)(64bit)  
libexpat.so.1()(64bit)  
libgcc_s.so.1()(64bit)  
libgcc_s.so.1(GCC_3.0)(64bit)  
libm.so.6()(64bit)  
libm.so.6(GLIBC_2.2.5)(64bit)  
libstdc++.so.6()(64bit)  
libstdc++.so.6(CXXABI_1.3)(64bit)  
libstdc++.so.6(GLIBCXX_3.4)(64bit)  
libstdc++.so.6(GLIBCXX_3.4.11)(64bit)  
libstdc++.so.6(GLIBCXX_3.4.15)(64bit)  
libstdc++.so.6(GLIBCXX_3.4.20)(64bit)  
libstdc++.so.6(GLIBCXX_3.4.21)(64bit)  
libstdc++.so.6(GLIBCXX_3.4.9)(64bit)  
rtld(GNU_HASH)  
dnf-plugins-core (>= 4.0.17-5.el9) | python3-dnf-plugins-core = 4.0.17-5.el9  
lvm2 (>= 8:2.03.09-5.el9) | /bin/bash  
/bin/sh  
bash >= 4.0  
device-mapper-persistent-data >= 0.7.0-0.1.rc6  
libaio.so.1()(64bit)  
libaio.so.1(LIBAIO_0.1)(64bit)  
libaio.so.1(LIBAIO_0.4)(64bit)  
libblkid.so.1()(64bit)  
libblkid.so.1(BLKID_1.0)(64bit)  
libblkid.so.1(BLKID_2.15)(64bit)  
libblkid.so.1(BLKID_2.17)(64bit)  
libblkid.so.1(BLKID_2.23)(64bit)  
libc.so.6(GLIBC_2.28)(64bit)  
libdevmapper-event.so.1.02()(64bit)  
libdevmapper-event.so.1.02(Base)(64bit)  
libdevmapper.so.1.02()(64bit)  
libm.so.6()(64bit)  
libm.so.6(GLIBC_2.2.5)(64bit)  
libpthread.so.0()(64bit)  
libpthread.so.0(GLIBC_2.2.5)(64bit)  
libreadline.so.7()(64bit)  
libselinux.so.1()(64bit)  
libsepol.so.1()(64bit)  
libsystemd.so.0()(64bit)  
libsystemd.so.0(LIBSYSTEMD_221)(64bit)  
libsystemd.so.0(LIBSYSTEMD_222)(64bit)  
libudev.so.1()(64bit)  
libudev.so.1(LIBUDEV_183)(64bit)  
lvm2-libs = 8:2.03.09-5.el9  
module-init-tools  
rtld(GNU_HASH)  
systemd-sysv  
systemd-units >= 189-3  
socat (>= 1.7.3.3-2.el9) | libc.so.6(GLIBC_2.15)(64bit)  
libcrypto.so.1.1()(64bit)  
libcrypto.so.1.1(OPENSSL_1_1_0)(64bit)  
libreadline.so.7()(64bit)  
librt.so.1()(64bit)  
librt.so.1(GLIBC_2.2.5)(64bit)  
libssl.so.1.1()(64bit)  
libssl.so.1.1(OPENSSL_1_1_0)(64bit)  
libutil.so.1()(64bit)  
libutil.so.1(GLIBC_2.2.5)(64bit)  
rtld(GNU_HASH)  
iproute (>= 5.3.0-5.el9) | /bin/sh  
libc.so.6(GLIBC_2.27)(64bit)  
libdb-5.3.so()(64bit)  
libdl.so.2()(64bit)  
libdl.so.2(GLIBC_2.2.5)(64bit)  
libelf.so.1()(64bit)  
libelf.so.1(ELFUTILS_1.0)(64bit)  
libm.so.6()(64bit)  
libm.so.6(GLIBC_2.2.5)(64bit)  
libmnl.so.0()(64bit)  
libmnl.so.0(LIBMNL_1.0)(64bit)  
libselinux.so.1()(64bit)  
rtld(GNU_HASH)  
iproute-tc (>= 5.3.0-5.el9) |   
iptables-ebtables (>= 1.8.4-15.el9_3.3) | /bin/bash  
/bin/sh  
iptables = 1.8.4-15.el9_3.3  
ethtool (>= 2:5.0-2.el9 ) | libc.so.6(GLIBC_2.14)(64bit)  
libm.so.6()(64bit)  
libm.so.6(GLIBC_2.2.5)(64bit)  
rtld(GNU_HASH)  
logrotate (>= 3.14.0) | /bin/sh  
coreutils  
libacl.so.1()(64bit)  
libacl.so.1(ACL_1.0)(64bit)  
libc.so.6(GLIBC_2.27)(64bit)  
libpopt.so.0()(64bit)  
libpopt.so.0(LIBPOPT_0)(64bit)  
libselinux.so.1()(64bit)  
rtld(GNU_HASH)  
  
libseccomp-devel (>= 2.5)  
  
### RHEL 8

Package | Dependencies  
---|---  
python36 (>= 3.6.8) | /bin/sh  
/usr/libexec/platform-python  
/usr/sbin/alternatives  
python3-pip  
python3-setuptools  
conntrack (>= 1.4.4-10.el8) | /bin/sh  
libc.so.6(GLIBC_2.15)(64bit)  
libdl.so.2()(64bit)  
libdl.so.2(GLIBC_2.2.5)(64bit)  
libmnl.so.0()(64bit)  
libmnl.so.0(LIBMNL_1.0)(64bit)  
libnetfilter_conntrack.so.3()(64bit)  
libnetfilter_cthelper.so.0()(64bit)  
libnetfilter_cthelper.so.0(LIBNETFILTER_CTHELPER_1.0)(64bit)  
libnetfilter_cttimeout.so.1()(64bit)  
libnetfilter_cttimeout.so.1(LIBNETFILTER_CTTIMEOUT_1.0)(64bit)  
libnetfilter_cttimeout.so.1(LIBNETFILTER_CTTIMEOUT_1.1)(64bit)  
libnetfilter_queue.so.1()(64bit)  
libnfnetlink.so.0()(64bit)  
libsystemd.so.0()(64bit)  
libsystemd.so.0(LIBSYSTEMD_209)(64bit)  
rtld(GNU_HASH)  
systemd  
device-mapper-persistent-data (>= 0.8.5-4.el8) | expat  
libaio.so.1()(64bit)  
libaio.so.1(LIBAIO_0.1)(64bit)  
libaio.so.1(LIBAIO_0.4)(64bit)  
libc.so.6(GLIBC_2.16)(64bit)  
libdl.so.2()(64bit)  
libdl.so.2(GLIBC_2.2.5)(64bit)  
libexpat.so.1()(64bit)  
libgcc_s.so.1()(64bit)  
libgcc_s.so.1(GCC_3.0)(64bit)  
libm.so.6()(64bit)  
libm.so.6(GLIBC_2.2.5)(64bit)  
libstdc++.so.6()(64bit)  
libstdc++.so.6(CXXABI_1.3)(64bit)  
libstdc++.so.6(GLIBCXX_3.4)(64bit)  
libstdc++.so.6(GLIBCXX_3.4.11)(64bit)  
libstdc++.so.6(GLIBCXX_3.4.15)(64bit)  
libstdc++.so.6(GLIBCXX_3.4.20)(64bit)  
libstdc++.so.6(GLIBCXX_3.4.21)(64bit)  
libstdc++.so.6(GLIBCXX_3.4.9)(64bit)  
rtld(GNU_HASH)  
dnf-plugins-core (>= 4.0.17-5.el8) | python3-dnf-plugins-core = 4.0.17-5.el8  
lvm2 (>= 8:2.03.09-5.el8) | /bin/bash  
/bin/sh  
bash >= 4.0  
device-mapper-persistent-data >= 0.7.0-0.1.rc6  
libaio.so.1()(64bit)  
libaio.so.1(LIBAIO_0.1)(64bit)  
libaio.so.1(LIBAIO_0.4)(64bit)  
libblkid.so.1()(64bit)  
libblkid.so.1(BLKID_1.0)(64bit)  
libblkid.so.1(BLKID_2.15)(64bit)  
libblkid.so.1(BLKID_2.17)(64bit)  
libblkid.so.1(BLKID_2.23)(64bit)  
libc.so.6(GLIBC_2.28)(64bit)  
libdevmapper-event.so.1.02()(64bit)  
libdevmapper-event.so.1.02(Base)(64bit)  
libdevmapper.so.1.02()(64bit)  
libm.so.6()(64bit)  
libm.so.6(GLIBC_2.2.5)(64bit)  
libpthread.so.0()(64bit)  
libpthread.so.0(GLIBC_2.2.5)(64bit)  
libreadline.so.7()(64bit)  
libselinux.so.1()(64bit)  
libsepol.so.1()(64bit)  
libsystemd.so.0()(64bit)  
libsystemd.so.0(LIBSYSTEMD_221)(64bit)  
libsystemd.so.0(LIBSYSTEMD_222)(64bit)  
libudev.so.1()(64bit)  
libudev.so.1(LIBUDEV_183)(64bit)  
lvm2-libs = 8:2.03.09-5.el8  
module-init-tools  
rtld(GNU_HASH)  
systemd-sysv  
systemd-units >= 189-3  
socat (>= 1.7.3.3-2.el8) | libc.so.6(GLIBC_2.15)(64bit)  
libcrypto.so.1.1()(64bit)  
libcrypto.so.1.1(OPENSSL_1_1_0)(64bit)  
libreadline.so.7()(64bit)  
librt.so.1()(64bit)  
librt.so.1(GLIBC_2.2.5)(64bit)  
libssl.so.1.1()(64bit)  
libssl.so.1.1(OPENSSL_1_1_0)(64bit)  
libutil.so.1()(64bit)  
libutil.so.1(GLIBC_2.2.5)(64bit)  
rtld(GNU_HASH)  
iproute (>= 5.3.0-5.el8) | /bin/sh  
libc.so.6(GLIBC_2.27)(64bit)  
libdb-5.3.so()(64bit)  
libdl.so.2()(64bit)  
libdl.so.2(GLIBC_2.2.5)(64bit)  
libelf.so.1()(64bit)  
libelf.so.1(ELFUTILS_1.0)(64bit)  
libm.so.6()(64bit)  
libm.so.6(GLIBC_2.2.5)(64bit)  
libmnl.so.0()(64bit)  
libmnl.so.0(LIBMNL_1.0)(64bit)  
libselinux.so.1()(64bit)  
rtld(GNU_HASH)  
iproute-tc (>= 5.3.0-5.el8) |   
iptables-ebtables (>= 1.8.4-15.el8_3.3) | /bin/bash  
/bin/sh  
iptables = 1.8.4-15.el8_3.3  
ethtool (>= 2:5.0-2.el8 ) | libc.so.6(GLIBC_2.14)(64bit)  
libm.so.6()(64bit)  
libm.so.6(GLIBC_2.2.5)(64bit)  
rtld(GNU_HASH)  
logrotate (>= 3.14.0) | /bin/sh  
coreutils  
libacl.so.1()(64bit)  
libacl.so.1(ACL_1.0)(64bit)  
libc.so.6(GLIBC_2.27)(64bit)  
libpopt.so.0()(64bit)  
libpopt.so.0(LIBPOPT_0)(64bit)  
libselinux.so.1()(64bit)  
rtld(GNU_HASH)  
  
libseccomp-devel (>= 2.5)  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-14 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-14 UTC."],[],[]] 
