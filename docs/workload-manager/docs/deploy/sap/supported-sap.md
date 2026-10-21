---
url: https://docs.cloud.google.com/workload-manager/docs/deploy/sap/supported-sap/
title: Supported SAP systems \u00a0|\u00a0 Workload Manager \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T02:28:35.553548+00:00
---

# Supported SAP systems  |  Workload Manager  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/workload-manager/docs/deploy/sap/supported-sap/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ Workload Manager ](https://docs.cloud.google.com/workload-manager/docs)
  * [ Guides ](https://docs.cloud.google.com/workload-manager/docs/overview)



Send feedback 

#  Supported SAP systems Stay organized with collections  Save and categorize content based on your preferences. 

This document provides the list of SAP systems that you can deploy using the Guided Deployment Automation tool in Workload Manager.

For additional information about the required installation files for each supported workload, see [Prepare SAP installation files for deployment](https://docs.cloud.google.com/workload-manager/docs/deploy/sap/sap-install-files). 

## Supported SAP systems

This section lists the SAP systems and operating systems that Workload Manager supports.

For more information about the operating systems that SAP HANA supports and to find the SAP HANA version that is compatible with your operating system version, see [SAP Note 2235581 - SAP HANA: Supported Operating Systems](https://launchpad.support.sap.com/#/notes/2235581).

### SAP application and versions

**SAP Application** | **Version** | **Service Pack Stacks**  
---|---|---  
SAP S/4HANA | 2021, 2022, 2023 | FPS00  
  
### Databases

**Database** | **Version** | **Service Pack Stacks**  
---|---|---  
SAP HANA | 2.0 | SPS 05, SPS 06, SPS 07  
  
### Database scaling method

**Database Scale Type** | **Description**  
---|---  
Scale-Up | Single-node configuration  
  
### Supported architecture

**Architecture** | **Description**  
---|---  
Distributed | A S/4HANA system using a distributed deployment model, which includes an ASCS/PAS server, a single HANA server, and multiple application servers.  
  
ASCS and PAS are on different VM instances than the DB and application servers.  
Distributed with high availability (HA) | A S/4HANA system using a distributed deployment model across two zones, with application servers running across two zones.  
  
Set up the SAP system across multiple zones.  
  
### Supported operating systems

The following table shows the Red Hat Enterprise Linux (RHEL) and SUSE Linux Enterprise Server (SLES) operating systems that are certified by SAP for production use with SAP HANA on Google Cloud.

**Operating System** | **Version**  
---|---  
Red Hat Enterprise Linux (RHEL) 8 | 
* RHEL for SAP with HA and Update Services 8.8
* RHEL for SAP with HA and Update Services 8.6
* RHEL for SAP with HA and Update Services 8.4  
SUSE Linux Enterprise Server (SLES) 15 | 
* SLES 15 SP5 for SAP x86_84
* SLES 15 SP4 for SAP x86_84
* SLES 15 SP3 for SAP x86_84  
  
During the configuration process, you can specify a custom operating system image instead of using the supported public images. We recommend using a custom image that is based on one of the supported `for SAP` images to reduce the possibility of errors during the deployment process. Workload Manager supports custom images, but customization or image hardening can cause unexpected issues.

The preceding operating systems are considered [premium images](https://docs.cloud.google.com/compute/disks-image-pricing#premiumimages) and are charged as on-demand or pay-as-you-go (PAYG). You can also [purchase commitments](https://docs.cloud.google.com/compute/docs/committed-use-discounts/purchase-license-commitments) for these licenses. Bring your own license (BYOL) is not supported.

### Supported machine types

The following sections list the machine types that Workload Manager supports for deploying your SAP HANA database and SAP application on Google Cloud.

#### Supported machine types for SAP HANA

Workload Manager supports deploying your SAP HANA database on the following machine types:

  * General-purpose machine types: N1, N2, C3
  * Memory-optimized machine types: M1, M2, M3, X4



For detailed information about each supported machine type, see [Certified Compute Engine VMs for SAP HANA](https://docs.cloud.google.com/sap/docs/sap-hana-planning-guide#certified-vms).

#### Supported machine types for SAP applications

Workload Manager supports the following machine types for ABAP SAP Central Services (ASCS) VMs and application servers:

  * General-purpose machine types: N1, N2, N2D, T2D, C3, C3D
  * Compute-optimized machine types: C2, C2D
  * Memory-optimized machine types: M1, M2, M3



For detailed information about each supported machine type, see [Certified machine types for SAP applications](https://docs.cloud.google.com/sap/docs/certifications-sap-apps#sap-certified-vms).

## What's next

  * Read the [prerequisites for deploying a SAP S/4HANA system](https://docs.cloud.google.com/workload-manager/docs/deploy/prerequisites).
  * Learn how to [deploy an SAP S/4HANA workload](https://docs.cloud.google.com/workload-manager/docs/deploy/deploy-sap).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
