---
url: https://docs.cloud.google.com/migration-center/docs/review-collector-cli-requirements/
title: Review requirements \u00a0|\u00a0 Migration Center \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T15:13:46.577727+00:00
---

# Review requirements  |  Migration Center  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/migration-center/docs/review-collector-cli-requirements/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Migration ](https://docs.cloud.google.com/docs/migration)
  * [ Migration Center ](https://docs.cloud.google.com/migration-center/docs)
  * [ Guides ](https://docs.cloud.google.com/migration-center/docs/migration-center-overview)



Send feedback 

#  Review requirements Stay organized with collections  Save and categorize content based on your preferences. 

This document lists the requirements for downloading and running the Migration Center discovery client CLI and guest collection scripts.

## Requirements for downloading and running `mcdc` CLI

To download and run the `mcdc` CLI, you need to meet the following requirements.

### Hardware requirements

To optimize performance, make sure that the virtual machine (VM) hosting the discovery client meets these specifications:

  * 2 CPU cores
  * 4 GB RAM
  * 30 GB free space



### Requirements for Linux

The `mcdc` CLI runs on all Linux machines with `glibc` version 2.25 or later, which includes the following Linux operating systems:

  * Ubuntu 18 or later
  * CentOS 8 or later
  * RHEL 8 or later
  * Debian 11 or later
  * openSUSE Leap 15 or later



### Requirements for Windows

The `mcdc` CLI runs on machines with the following operating systems:

  * Windows 10 or later
  * Windows Server 2016 or later

**Warning:** The local database is encrypted by using the [Windows Data Protection API](https://learn.microsoft.com/en-us/previous-versions/ms995355\(v%3Dmsdn.10\)). Resetting the Windows user password can cause the loss of all locally collected data.

### Requirements for VMware VMs

To use the `mcdc` CLI to collect data using VMware inventory discovery:

  * The machine running the `mcdc` CLI must be able to connect to your vCenter and ESX hosts. This includes opening all necessary ports in firewall rules and ensuring network connectivity between the `mcdc` CLI host machine and target vCenter server and ESX hosts.
  * The vSphere vCenter server must be version 5.5 or later.
  * The vSphere vCenter server must support TLS version 1.2 or later.
  * The username you pass to the `mcdc` CLI must have read privileges on one or more VMs. The `mcdc` CLI is only able to discover information about VMs that are accessible to the specified user. The read privilege is typically assigned to all roles except for `No Access`.
  * The username you pass to the `mcdc` CLI must have read privileges on the host ESX. If there are multiple ESX servers, then read privileges are required for every ESX that hosts a discovered VM.
  * The user running `mcdc` CLI must have read, write, execute privileges on the machine running the `mcdc` CLI.



To use the `mcdc` CLI to run the guest collection scripts remotely for VMware VMs:

  * You need the same permissions to run VMware discovery described earlier.
  * The username you pass to the `mcdc` CLI to connect to vSphere must have the following privileges on the VM: Guest operation modifications, Guest operation program execution, and Guest operation queries.
  * The VM user credentials used by the `mcdc` CLI to execute the script must have administrator privileges on the target guest machine for Windows VM.
  * Port 443 must be open from the `mcdc` CLI Linux station to all ESXI hosts.



### Requirements for SSH collection

To use the `mcdc` CLI to run the guest collection scripts remotely using SSH:

  * The machine hosting the `mcdc` CLI must have SSH access to the target Linux machines.

**Note:** `mcdc` CLI doesn't support running the guest collection scripts remotely using SSH on Windows machines.



### Requirements for IP range scan

To use the `mcdc` CLI to run an IP range scan:

  * Configure your network firewalls to enable ICMP requests on the network or machines in your infrastructure.
  * Give permissions to unprivileged users to perform a ping from the host machine. Alternatively, before running an IP range scan, run `sudo setcap cap_net_raw-ep ./mcdc`.



## Requirements for downloading and running guest collection scripts

  * `mcdc-linux-collect.sh` runs on the following Linux operating systems or later: 

    * CentOS 7
    * Red Hat Enterprise Linux (RHEL) 8
    * Ubuntu 14.04
    * Debian 9
    * openSUSE 15

On older operating system versions, the script might fail to run or might collect incomplete data.

  * `mcdc-windows-collect.ps1` requires PowerShell 2.0 or later (not PowerShell Core), and either a GUI shell (not server core) or .Net framework 4.5 or later. All Windows versions greater than or equal to Windows 8 and Windows Server 2012 support these requirements, as do the vast majority of Windows 7 and Windows Server 2008 R2 machines.




## What's next

  * Learn how to [download the `mcdc` CLI](https://docs.cloud.google.com/migration-center/docs/download-collector-cli).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
