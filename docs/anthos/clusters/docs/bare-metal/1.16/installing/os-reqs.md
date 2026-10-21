---
url: https://docs.cloud.google.com/anthos/clusters/docs/bare-metal/1.16/installing/os-reqs/
title: Select your operating system \u00a0|\u00a0 Google Distributed Cloud Virtual for Bare Metal \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-15T20:46:11.037575+00:00
---

# Select your operating system  |  Google Distributed Cloud Virtual for Bare Metal  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/anthos/clusters/docs/bare-metal/1.16/installing/os-reqs/

**Version 1.16**. This version is no longer supported. For information about how to upgrade to version 1.28, see [ Upgrade clusters](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/how-to/upgrade) in the latest documentation. For more information about supported and unsupported versions, see the [Versioning](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/version-history) page in the latest documentation.

  * [ Home ](https://docs.cloud.google.com/)
  * [ Google Distributed Cloud ](https://docs.cloud.google.com/distributed-cloud)
  * [ Documentation ](https://docs.cloud.google.com/kubernetes-engine/enterprise/clusters/docs)
  * [ GDCV for Bare Metal 1.16 ](https://docs.cloud.google.com/anthos/clusters/docs/bare-metal/1.16)
  * [ Guides ](https://docs.cloud.google.com/anthos/clusters/docs/bare-metal/1.16/concepts/about-bare-metal)



Send feedback 

#  Select your operating system Stay organized with collections  Save and categorize content based on your preferences. 

Version 1.16 keyboard_arrow_down

  * [ Latest ](https://docs.cloud.google.com/anthos/clusters/docs/bare-metal/latest/installing/os-reqs)
  * [ Version 1.16 ](https://docs.cloud.google.com/anthos/clusters/docs/bare-metal/1.16/installing/os-reqs)
  * [ Earlier versions (unsupported) ](https://docs.cloud.google.com/anthos/clusters/docs/bare-metal/1.16/getting-support#version-support)



Google Distributed Cloud runs on Linux. Google Distributed Cloud version 1.16.0 and subsequent patch releases support the following Linux distributions and versions. Google Distributed Cloud supports only kernels supplied with supported distributions.

## Red Hat Enterprise Linux (RHEL)

Google Distributed Cloud is tested on and supports the following Red Hat Enterprise Linux (RHEL) minor releases:

###  Google Distributed Cloud 1.28 

  * RHEL 9.2 ([Preview](https://cloud.google.com/products/#product-launch-stages): qualified and supported for Google Distributed Cloud 1.28.0 and higher)
  * RHEL 8.10 (qualified and supported for Google Distributed Cloud 1.28.600 and higher)
  * RHEL 8.8
  * RHEL 8.6



###  Google Distributed Cloud 1.16 

  * RHEL 8.8
  * RHEL 8.6



###  Google Distributed Cloud 1.15 

  * RHEL 8.8
  * RHEL 8.6



Google Distributed Cloud supports only RHEL minor releases that are covered under Red Hat's Full and Maintenance support phases. OS versions that go out of support are removed from the list. For information about the support phases for RHEL, see [Red Hat Enterprise Linux Life Cycle](https://access.redhat.com/support/policy/updates/errata#RHEL8_and_9_Life_Cycle).

For instructions about how to configure RHEL on your node machines, see [Configure RHEL](https://docs.cloud.google.com/anthos/clusters/docs/bare-metal/1.16/installing/configure-os/rhel).

## Ubuntu

Google Distributed Cloud is tested on and supports the following Long Term Support (LTS) versions of Ubuntu:

###  Google Distributed Cloud 1.28 

  * 22.04 LTS
  * 20.04 LTS



###  Google Distributed Cloud 1.16 

  * 22.04 LTS
  * 20.04 LTS



###  Google Distributed Cloud 1.15 

  * 22.04 LTS
  * 20.04 LTS



For each LTS version, Ubuntu maintains multiple kernel packages, but the support lifecycle for individual LTS version and kernel version pairings varies. Google Distributed Cloud supports only LTS and kernel pairings that are covered by Ubuntu's Standard support offering. OS versions that go out of support are removed from the list. For more information about the Ubuntu kernel support lifecycle, see [The Ubuntu lifecycle and release cadence](https://ubuntu.com/about/release-cycle#ubuntu-kernel-release-cycle).

To successfully install Google Distributed Cloud, you must use an Ubuntu Hardware Enablement (HWE) kernel.

For instructions to configure Ubuntu on your node machines, see [Configure Ubuntu](https://docs.cloud.google.com/anthos/clusters/docs/bare-metal/1.16/installing/configure-os/ubuntu).

## CentOS (support deprecated)

CentOS Linux 8 reached its end of life (EOL) on December 31st, 2021. We strongly recommend that you migrate to one of the other supported operating systems for Google Distributed Cloud. **All support for CentOS is removed from the upcoming release of Google Distributed Cloud (December 2023) and subsequent releases.**

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
