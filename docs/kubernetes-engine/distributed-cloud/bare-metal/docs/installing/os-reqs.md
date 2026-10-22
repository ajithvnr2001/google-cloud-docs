---
url: https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/installing/os-reqs/
title: Select your operating system \u00a0|\u00a0 Google Distributed Cloud software only for bare metal \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T10:24:23.567035+00:00
---

# Select your operating system  |  Google Distributed Cloud software only for bare metal  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/installing/os-reqs/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Distributed, hybrid, and multicloud ](https://docs.cloud.google.com/docs/dhm-cloud)
  * [ Google Distributed Cloud ](https://docs.cloud.google.com/distributed-cloud/docs)
  * [ GDC for bare metal ](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs)
  * [ Guides ](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/concepts/about-bare-metal)



Send feedback 

#  Select your operating system Stay organized with collections  Save and categorize content based on your preferences. 

Google Distributed Cloud runs on Linux. Google Distributed Cloud version 1.36.0 and subsequent patch releases support the following Linux distributions and versions.

**Important:** To be eligible for assistance from Cloud Customer Care, your Google Distributed Cloud environment must run on one of the supported operating system versions listed on this page. It must also use the original kernel supplied with that distribution. Environments running on unsupported OS versions, or on supported OS versions with custom or third-party kernels, are not eligible for support from Cloud Customer Care.

This document is for Admins and architects and Operators who define IT solutions and system architecture in accordance with company strategy. To learn more about common roles and example tasks that we reference in Google Cloud content, see [Common GKE user roles and tasks](https://docs.cloud.google.com/kubernetes-engine/enterprise/docs/concepts/roles-tasks).

Starting in version 1.35, Google Distributed Cloud requires `cgroupsv2`. Google Distributed Cloud prevents creating or upgrading clusters during preflight checks if `cgroupsv1` is detected. For instructions on how to migrate your operating system to `cgroupsv2`, see [Migrating to cgroup v2](https://kubernetes.io/docs/concepts/architecture/cgroups/#migrating-cgroupv2) in the Kubernetes documentation.

Starting in 1.36, If you use RHEL 8 or Rocky Linux, you must install Python 3.9 or later on your target nodes before you upgrade. To find and update your Python version, see [Validate the Python version](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/installing/configure-os/rhel#update-python).

## Red Hat Enterprise Linux (RHEL)

Google Distributed Cloud is tested on and supports the following Red Hat Enterprise Linux (RHEL) minor releases:

###  1.36 

  * RHEL 9.6
  * RHEL 9.4
  * RHEL 8.10 1



###  1.35 

**Note:** Starting in version 1.35, you must use a RHEL version that supports cgroupsv2.

  * RHEL 9.6
  * RHEL 9.4
  * RHEL 8.10 1



###  1.34 

  * RHEL 9.6
  * RHEL 9.4
  * RHEL 8.10



1 For version 1.35 and later, you must enable `cgroupsv2`. If you use RHEL 8, you must install Python 3.9 or later on your target nodes before you upgrade.

2 RHEL 9.6 is supported for Google Distributed Cloud version 1.33.200 and later.

When we test and qualify a minor version for support, we target RHEL minor versions that provide optimal stability and longevity. For example, Google Distributed Cloud doesn't support odd-numbered RHEL minor releases, because they typically have a short lifecycle without extended update support. Google Distributed Cloud doesn't support RHEL OS versions that are no longer covered under Red Hat's Full and Maintenance support phases. For information about the support phases for RHEL, see [Red Hat Enterprise Linux Life Cycle](https://access.redhat.com/support/policy/updates/errata#RHEL8_and_9_Life_Cycle).

We evaluate major and minor versions as they're released for inclusion into our support matrix. If you have questions about recent, unsupported versions, contact [Google Cloud Support](https://cloud.google.com/support-hub).

For supported kernel versions, see [Red Hat Enterprise Linux Release Dates](https://access.redhat.com/articles/3078).

For instructions about how to configure RHEL on your node machines, see [Configure RHEL](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/installing/configure-os/rhel).

## Ubuntu

All supported versions of Google Distributed Cloud software are tested on and support the following Long Term Support (LTS) versions of Ubuntu:

  * 24.04 LTS1, 2
  * 22.04 LTS



1 Ubuntu 24.04 LTS is supported for Google Distributed Cloud version 1.33.0 and later.

2 The 6.14 kernel package, patch versions 6.14.0-27 and higher, is supported for use with Ubuntu 24.04 LTS for Google Distributed Cloud version 1.34.0 and later.

For each LTS version, Ubuntu maintains multiple kernel packages, but the support lifecycle for individual LTS version and kernel version pairings varies. Google Distributed Cloud supports only LTS and kernel pairings that are covered by Ubuntu's Standard support offering. OS versions that go out of support are removed from the list. For more information about the Ubuntu kernel support lifecycle, see [The Ubuntu lifecycle and release cadence](https://ubuntu.com/about/release-cycle#ubuntu-kernel-release-cycle).

To successfully install Google Distributed Cloud, you must use an Ubuntu Hardware Enablement (HWE) kernel.

For instructions to configure Ubuntu on your node machines, see [Configure Ubuntu](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/installing/configure-os/ubuntu).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-21 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-21 UTC."],[],[]] 
