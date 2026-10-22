---
url: https://docs.cloud.google.com/bare-metal/docs/known-issues/
title: Known issues and limitations in Bare Metal Solution \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:37:11.880201+00:00
---

# Known issues and limitations in Bare Metal Solution  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/bare-metal/docs/known-issues/

The availability of Bare Metal Solution is transitioning to a specialized, allowlist-only model. If you are an existing customer, please contact your Google account team to explore the value of migrating to new [Oracle and Google Cloud strategic partnership offerings](https://docs.cloud.google.com/bare-metal/docs/explore-oracle-partnership-offerings). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Bare Metal ](https://docs.cloud.google.com/bare-metal/docs)
  * [ Resources ](https://docs.cloud.google.com/bare-metal/docs/resource)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Known issues and limitations in Bare Metal Solution

This page describes known issues and limitations that you might run into when using Bare Metal Solution.

## Limitations

### Modification to BIOS settings is not supported

Bare Metal Solution does not support modifications to BIOS settings, including disabling C-states and P-states at the BIOS level.

To work around this issue, you can utilize the OS-level controls of C-states and P-states through your OS's power management functionality. To learn how to do this, refer to your OS documentation.

### Bare Metal Solution regional extension doesn't support VPC Service Controls parameters

Connecting a VPC with service controls enabled to your Bare Metal Solution environment doesn't uphold any service control guarantees.

The Bare Metal Solution API can be added to a secure perimeter. However, the VPC Service Controls perimeters don't extend to the Bare Metal Solution environment in the regional extensions. For more information, see [Supported products and limitations](https://docs.cloud.google.com/vpc-service-controls/docs/supported-products#table_baremetalsolution).

If you still want to use Bare Metal Solution with VPC Service Controls enabled, contact [Customer Care](https://cloud.google.com/support-hub) to add your Google Cloud project to allowlist for using this feature.

### Changing ASN is not supported

Bare Metal Solution and Partner Interconnect do not support custom autonomous system numbers (ASN). The Bare Metal Solution client network ASN is set to `65500`. For Partner Interconnect, all Cloud Routers must have a local ASN of `16550`.

We recommend that you plan your deployments accordingly.

### Maximum number of LUNs attached to a server

You can attach a maximum of 200 LUNs (including the boot LUN) to a Bare Metal Solution server.

### MTU modifications on VLAN attachments are not supported

Modifying the MTU of the VPC side does not automatically update the MTU in your Bare Metal Solution side of the connection.

To change the MTU, you must request the change through support or recreate the VLAN attachment with the new MTU.

## Known issues

### Cold shutdown after the first reboot through OVM Manager

For servers provisioned with OVM 3.4.6, the first reboot initiated through the OVM Manager, either after the initial provisioning or re-imaging, results in a cold shutdown.

To learn how to power on a server, see [Operate your Bare Metal Solution server](https://docs.cloud.google.com/bare-metal/docs/bms-maintenance#restart_a_bare_metal_solution_server).

### Server takes a long time to boot

The boot time may vary depending on the size of your server and the number of shared LUNs.

The larger the server, the longer it takes to boot.

The number of shared LUNs on a server also impacts its boot time. For instance, a `o2-highmem-224-metal` server with ~100 shared LUNs might take over an hour to boot compared to a `o2-highmem-224-metal` server with fewer LUNs that would take ~45 minutes. This is because of the time required to run all the checks and is normal.

### Buffer overflow when using ethtool with the debug flag

A bug causing a buffer overflow when using `ethtool -d` was [fixed in Linux 5.8 kernel](https://git.kernel.org/pub/scm/linux/kernel/git/stable/linux.git/commit/?id=da3287111ab43b32cec54d7ca6b48640f210a196). This bug can cause a kernel panic and might impact your Bare Metal Solution server depending on the OS and hypervisor that you are using.

Following are our recommendations and workaround for this bug:

###  Red Hat Enterprise Linux (RHEL) 

If you are using **RHEL 7.x** , then follow these guidelines:

  * Do not run `ethtool` with the debug flag: `ethtool -d`.
  * Prevent the `sosreport` utility from invoking `ethtool -d` by disabling the networking plugin.

In the `/etc/sos/sos.conf` file, add the following lines:
        
        [plugins]
        disable = networking
        




If you are using **RHEL 8.x** , then follow these guidelines:

  * Update to kernel version **RHEL 8.3 (kernel 4.18.0-240)** or later.
  * For systems with kernel versions lower than **4.18.0-240** that can't be updated, prevent the `sosreport` utility from invoking `ethtool -d` by disabling the networking plugin.

In the `/etc/sos/sos.conf` file, add the following lines:
        
        [report]
        skip-plugins = networking
        




For more information, see the [Red Hat Solution](https://access.redhat.com/solutions/5352911).

###  SUSE Linux Enterprise Server(SLES) 

This bug was fixed in **SLES 15 SP4 (kernel version 5.14.21-150400.22.1)**. Update to **SLES 15 SP4 (kernel version 5.14.21-150400.22.1)** or later.

###  Oracle Enterprise Linux 

If you are using **Oracle Linux 7.x** , then follow these guidelines:

  * Do not run `ethtool` with the debug flag: `ethtool -d`.
  * Prevent the `sosreport` utility from invoking `ethtool -d` by disabling the networking plugin.

In the `/etc/sos/sos.conf` file, add the following lines:
        
        [plugins]
        disable = networking
        




If you are using **Oracle 8.x** , then follow these guidelines:

  * This bug was fixed in **OL8U7 (kernel-uek-5.15.0-3.60.5.1)**. You can update to the most recent kernel by following the [update instructions from Oracle](https://docs.oracle.com/en/operating-systems/oracle-linux/8/relnotes8.7/ol8-NewFeaturesandChanges.html#ol8-features-install).
  * If you can't update to kernel version **kernel-uek-5.15.0-3.60.5.1** , prevent the `sosreport` utility from invoking `ethtool -d` by disabling the networking plugin.

In the `/etc/sos/sos.conf` file, add the following lines:
        
        [report]
        skip-plugins = networking
        




###  Oracle VM Server 

  * Do not run `ethtool` in `dom0` domain with the debug flag: `ethtool -d`.
  * Prevent the `sosreport` utility from invoking `ethtool -d` by disabling the networking plugin.

In the `/etc/sos/sos.conf` file, add the following lines:
        
        [plugins]
        disable = networking
        




### OVM server can't connect to OVM Manager after TS54 firmware upgrade

If you have upgraded your Bare Metal Solution server running Oracle VM (OVM) and it cannot connect to the OVM Manager, then this issue might be the reason. Upgrading firmware of a Bare Metal Solution server changes its SMBIOS UUID. The OVM uses this UUID to identify itself with the OVM Manager. Therefore, the change of UUID can cause issues with the communication between the two. To prevent this, before upgrading the firmware of your Bare Metal Solution server, apply the workaround described in [Oracle Doc ID 1534416.1](https://support.oracle.com/knowledge/Oracle%20Linux%20and%20Virtualization/1534416_1.html). For assistance in implementing this workaround, contact [Customer Care](https://cloud.google.com/support-hub).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
