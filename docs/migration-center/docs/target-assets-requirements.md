---
url: https://docs.cloud.google.com/migration-center/docs/target-assets-requirements/
title: Review target server configuration requirements \u00a0|\u00a0 Migration Center \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:54:23.544127+00:00
---

# Review target server configuration requirements  |  Migration Center  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/migration-center/docs/target-assets-requirements/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Migration ](https://docs.cloud.google.com/docs/migration)
  * [ Migration Center ](https://docs.cloud.google.com/migration-center/docs)
  * [ Guides ](https://docs.cloud.google.com/migration-center/docs/migration-center-overview)



Send feedback 

#  Review target server configuration requirements Stay organized with collections  Save and categorize content based on your preferences. 

The physical machines and VMs that the discovery client collects data from are referred to as _target servers_ in Migration Center. This page describes the specific configurations that the target servers must have, depending on the OS type and the collection method.

## Windows machines

To allow the discovery client to scan your physical or virtual Windows machines, you provide it with [authentication credentials for the operating system](https://docs.cloud.google.com/migration-center/docs/create-and-manage-credentials). Windows machines must meet the following requirements:

  * WMI (Windows Management Instrumentation) Service is running.
  * Windows Firewall is disabled. Alternatively, a firewall exception to allow for Remote WMI.
  * The discovery client must be able to connect to each asset.
  * An account with administrator rights to the operating system.



## Linux machines

To allow the discovery client to scan your physical or virtual Linux machines, you provide it with authentication credentials for the operating system. Linux machines must meet the following requirements:

  * SSH enabled with support for the following encryption algorithms: 
    * RSA and DSA in PEM format
    * ECDSA 256/384/521, ED25519 in OpenSSL or PEM formats
  * The discovery client must be able to connect to each asset.
  * An account with user-level access (no sudo or root privileges required).

**Note:** HP-UX, AIX, Solaris, FreeBSD and other UNIX-like systems are not supported.

## VMware vCenter

To allow the discovery client to scan your vCenter source you provide the following:

  * The credentials required to access vCenter.
  * The vCenter URL. Optionally, the vCenter Inventory Path to limit the scope of the collection.



In addition, you must configure vCenter and meet the requirements as described in the following sections.

### vCenter configuration

Before you run a vCenter discovery, you need to configure your vCenter environment. The data you collect with the discovery client, in fact, depend on the settings for statistics in vCenter.

vCenter supports four levels of statistics:

  * Level 1 exposes only CPU and memory performance.
  * Level 2 exposes the network performance.
  * Level 3 exposes input/output operations per second (IOPS).
  * Level 4 exposes all the available metrics.



For a detailed list of the available metrics for all statistics levels, see [Data collection levels](https://techdocs.broadcom.com/us/en/vmware-cis/vsphere/vsphere/7-0/vcenter-configuration/configuring-vcenter-server-using-the-vsphere-client/configuring-vcenter-server-in-the-vsphere-client/configuring-statistics-settings-in-the-vsphere-client/data-collection-levels.html).

By default, the statistics level is set to level 1. Levels 1 and 2 let you collect partial data about your infrastructure, while level 3 lets you collect everything you need to generate a complete total cost of ownership (TCO) report. After the statistics level is changed in vCenter, it might take several hours for performance data to become available.

For more information on how to change statistics levels in vCenter, see [Configure statistics collection intervals in the vSphere client](https://techdocs.broadcom.com/us/en/vmware-cis/vsphere/vsphere/7-0/vcenter-configuration/configuring-vcenter-server-using-the-vsphere-client/configuring-vcenter-server-in-the-vsphere-client/configuring-statistics-settings-in-the-vsphere-client/configure-statistics-intervals-for-vcenter-server-in-the-vsphere-client.html).

### VMs running on vCenter

VMs running on vCenter must meet the following requirements:

  * You can add up to 100 vCenter sources (URL + inventory path).


  * The machine running the discovery client must be able to connect to your vCenter and ESX hosts. This includes opening all necessary ports in firewall rules and ensuring network connectivity between the discovery client host machine and target vCenter server and ESX hosts.
  * The vSphere vCenter server must be version 5.5 or later.
  * The vSphere vCenter server must support TLS version 1.2 or later.
  * The username you pass to the discovery client must have read privileges on one or more VMs. The discovery client is only able to discover information about VMs that are accessible to the specified user. The read privilege is typically assigned to all roles except for `No Access`.
  * The username you pass to the discovery client must have read privileges on the host ESX. If there are multiple ESX servers, then read privileges are required for every ESX that hosts a discovered VM.
  * The user running discovery client must have read, write, execute privileges on the machine running the discovery client.



## What's next

  * Learn about the [installation requirements for the discovery client](https://docs.cloud.google.com/migration-center/docs/installation-requirements).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
