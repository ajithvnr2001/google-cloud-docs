---
url: https://docs.cloud.google.com/vmware-engine/docs/vmware-ecosystem/sql-server-licensing/
title: Microsoft SQL Server licensing options \u00a0|\u00a0 Google Cloud VMware Engine \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T03:27:00.653275+00:00
---

# Microsoft SQL Server licensing options  |  Google Cloud VMware Engine  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/vmware-engine/docs/vmware-ecosystem/sql-server-licensing/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ VMware Engine ](https://docs.cloud.google.com/vmware-engine/docs)
  * [ Guides ](https://docs.cloud.google.com/vmware-engine/docs/overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Microsoft SQL Server licensing options

This document describes Microsoft licensing options for running Microsoft SQL Server in Google Cloud VMware Engine private clouds. You can license Microsoft SQL Server in VMware Engine in one of the following ways: 

  * Purchase on-demand licenses through License Manager (Preview).
  * Bring your own licenses (BYOL) using Microsoft's License Mobility through Software Assurance program. 

## Purchase on-demand licenses with License Manager (Preview)

**Preview**

This product or feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA products and features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

You can purchase on-demand licenses for Microsoft SQL Server running on Google Cloud VMware Engine through License Manager. License Manager lets you activate, manage, and track licenses without long-term commitments or managing compliance yourself. 

With License Manager, you purchase licenses in the form of "2 Core Packs" for a fixed monthly price per pack. Assign a core license to each virtual CPU (vCPU) on your virtual machine instance. Each instance requires a minimum of four cores. Instances with fewer than 4 vCPUs are charged for 4 vCPUs to comply with Microsoft requirements.

### Supported versions and editions

License Manager supports the following editions of SQL Server:

    * Microsoft SQL Server Enterprise
    * Microsoft SQL Server Standard
    * Microsoft SQL Server Web

License Manager supports the following versions of SQL Server:

    * 2017
    * 2019
    * 2022

### Before you begin

To use License Manager for SQL Server on VMware Engine, you must first enroll in the Preview program. Contact `license-manager-onboarding@google.com` with your project numbers, VM locations, and administrator email address to request enrollment.

After you are enrolled, follow the instructions in [Configure and use License Manager](https://docs.cloud.google.com/compute/docs/instances/windows/license-manager) to enable the API, create a license configuration, and update license settings on your VMs.

## Bring your own SQL Server licenses with License Mobility

If you have Microsoft SQL Server licenses with active Software Assurance (SA), you can use [License Mobility](https://www.microsoft.com/licensing/licensing-programs/software-assurance-license-mobility) to bring these licenses to VMware Engine. License Mobility is a Software Assurance benefit that lets you deploy eligible server application licenses on-premises or in the cloud in an authorized partner's data center, including Google Cloud.

With License Mobility, you can use your existing SQL Server licenses for virtual machines in your private cloud without needing to purchase new licenses from Google or pay for software licenses on Compute Engine VMs.

### Eligibility requirements

To use License Mobility with VMware Engine, you must meet the following requirements:

    * Your SQL Server licenses must have active Software Assurance (SA).
    * SQL Server is an eligible product for License Mobility.
    * You must follow Microsoft's License Mobility terms, including completing a license verification process with Microsoft within 10 days of deployment.

For more information about License Mobility, see [Software Assurance License Mobility](https://www.microsoft.com/licensing/licensing-programs/software-assurance-license-mobility) and [Customer License Mobility Verification Guide](https://download.microsoft.com/download/3/d/4/3d42bdc2-6725-4b29-b75a-a5b04179958b/licensemobilityverificationguide.pdf).

### Licensing SQL Server with License Mobility

When using License Mobility, you license the individual virtual machines running SQL Server based on the number of vCPUs, according to your Microsoft licensing agreement. This is different from the Windows Server BYOL option for licenses purchased before October 1, 2019, which requires licensing all physical cores in a node.

## Other options

If you choose not to use the License Manager Preview or if you don't have SQL Server licenses with active Software Assurance for BYOL, consider the following alternatives to running SQL Server on VMware Engine:

    * **Run SQL Server on Compute Engine:** You can run SQL Server on Compute Engine VMs using [pay-as-you-go licenses or BYOL](https://docs.cloud.google.com/compute/docs/instances/sql-server/pricing).
    * **Use Cloud SQL:** Migrate to [Cloud SQL](https://docs.cloud.google.com/sql), Google's fully managed relational database service for MySQL, PostgreSQL, and SQL Server.
    * **Purchase licenses with Software Assurance:** Purchase or renew SQL Server licenses with Software Assurance to become eligible for License Mobility.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
