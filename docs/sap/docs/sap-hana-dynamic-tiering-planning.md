---
url: https://docs.cloud.google.com/sap/docs/sap-hana-dynamic-tiering-planning/
title: SAP HANA dynamic tiering on Google Cloud planning guide \u00a0|\u00a0 SAP on Google Cloud \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T17:58:15.557324+00:00
---

# SAP HANA dynamic tiering on Google Cloud planning guide  |  SAP on Google Cloud  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sap/docs/sap-hana-dynamic-tiering-planning/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ SAP on Google Cloud ](https://docs.cloud.google.com/sap/docs)
  * [ Guides ](https://docs.cloud.google.com/sap/docs/overview-of-sap-on-google-cloud)



Send feedback 

#  SAP HANA dynamic tiering on Google Cloud planning guide Stay organized with collections  Save and categorize content based on your preferences. 

SAP HANA Dynamic Tiering is approved by SAP to run on Google Cloud.

## About SAP HANA dynamic tiering on Google Cloud

SAP HANA dynamic tiering provides disk-based, large-volume extended storage for your SAP HANA warm data.

The storage is provided by Compute Engine SSD persistent disks that are attached to the SAP HANA dynamic tiering VM.

For more information from SAP about SAP HANA Dynamic Tiering and its support on Google Cloud, see the following SAP Notes:

  * [2555629 - SAP HANA 2.0 Dynamic Tiering – Hypervisor and Cloud Support](https://launchpad.support.sap.com/#/notes/2555629)
  * [ SAP Note 2456432 - SAP Applications on Google Cloud: Supported Products and Google Cloud machine types](https://launchpad.support.sap.com/#/notes/2456432)



## Resource requirements

### VM types

On Google Cloud, the SAP HANA dynamic tiering server must run on a dedicated Compute Engine virtual machine (VM). Running dynamic tiering on the same VM as SAP HANA is not supported.

SAP recommends specific Compute Engine high-memory VM types for SAP HANA dynamic tiering on Google Cloud. The recommended VM types offer a range of sizes to choose from that cover most use cases.

Dynamic tiering data capacity | VM type | Memory  
---|---|---  
512 GB | `n1-highmem-8` | 52 GB  
1,300 GB | `n1-highmem-16` | 104 GB  
5,000 GB | `n1-highmem-32` | 208 GB  
10,000 GB | `m1-megamem-96` | 1433 GB  
  
If, after deploying SAP HANA dynamic tiering on one of the recommended VM types, your monitoring indicates a need for more resources, you can switch to one of the larger recommended VM types.

If, after switching to one of the larger recommended VM types, your monitoring still indicates a problem, such as a performance bottleneck, SAP supports switching to a custom VM in which you adjust the vCPUs, memory, or both to meet your performance objectives.

For guidance on sizing resources for SAP HANA dynamic tiering, see the [SAP HANA Dynamic Tiering documentation](https://help.sap.com/viewer/product/SAP_HANA_DYNAMIC_TIERING).

For more information about different VM instance types and their use cases, see [machine types](https://docs.cloud.google.com/compute/docs/machine-types).

### Storage configuration

Use a single SSD persistent disk for the SAP HANA dynamic tiering store and transaction logs. The minimum size for the disk is 550 GB.

Use LVM to partition the disk into three volumes for the `/usr/sap`, `/hana/data_es`, and `/hana/log_es` directories. To size the volumes, follow the guidance in the [SAP HANA Dynamic Tiering documentation](https://help.sap.com/viewer/product/SAP_HANA_DYNAMIC_TIERING). [SAP Note 2140959](https://launchpad.support.sap.com/#/notes/2140959) also contains information about sizing the dynamic tiering directories.

SAP HANA dynamic tiering shares the `/hana/shared` and `/hanabackup` directories with SAP HANA, which must be on persistent disks that are mounted on both the VMs for SAP HANA and the dynamic tiering server.

You may need to increase the size of the backup disk to accommodate the SAP HANA in-memory data and the data on disk. SAP HANA backs up both in the same backup operation.

### Memory configuration

The memory allocations included with the recommended VM types for SAP HANA dynamic tiering are sufficient in most cases.

If your monitoring indicates that the recommended VM type you are using is causing a performance bottleneck, you can switch to a custom VM and adjust the vCPUs or memory to fix the problem.

For guidance on determining the amount of memory you need, see the [SAP HANA Dynamic Tiering documentation](https://help.sap.com/viewer/product/SAP_HANA_DYNAMIC_TIERING).

### Operating system selection

SAP HANA dynamic tiering must run on the same type and version of operating system as the SAP HANA system it supports.

For the operating systems that SAP certifies for SAP HANA on Google Cloud, see [Certified operating systems for SAP HANA](https://docs.cloud.google.com/sap/docs/certifications-sap-hana#hana-cert-table-oss).

## Pricing and quota considerations for SAP HANA dynamic tiering

You are responsible for the costs incurred by the resources you deploy by following this guide. Use the [pricing calculator](https://cloud.google.com/pricing/calculator) to help estimate your actual costs.

**Important** : RHEL and SLES are premium images and all prices for premium images are in addition to charges for using a machine type. For details about premium image pricing, refer to the [Premium images](https://cloud.google.com/compute/pricing#premiumimages). 

For pricing considerations for the base SAP HANA system, see the [SAP HANA Planning Guide](https://docs.cloud.google.com/sap/docs/sap-hana-planning-guide#costs).

### Quotas

Include the Google Cloud resources that SAP HANA dynamic tiering uses, such as vCPUs and persistent disks, when calculating your resource quotas for your SAP HANA system.

For quota requirements for the base SAP HANA system, see the [SAP HANA Planning Guide](https://docs.cloud.google.com/sap/docs/sap-hana-planning-guide#quotas).

You can view your current quotas in the [Google Cloud console](https://console.cloud.google.com/iam-admin/quotas).

## Licensing

Running SAP HANA dynamic tiering on Google Cloud requires you to bring your own SAP HANA dynamic tiering license (BYOL). SAP HANA dynamic tiering requires its own license, separate from the SAP HANA license.

A new installation of dynamic tiering includes a temporary license that is good for a period of time determined by SAP, typically 90 days. If a temporary license expires before a permanent license is installed, dynamic tiering ceases to function.

For more information about SAP licensing, see [Dynamic Tiering Licensing](https://help.sap.com/viewer/88f82e0d010e4da1bc8963f18346f46e/2.00.04/en-US/9750fddb354b4384baab7720dbf3efc9.html).

## Deployment architecture

SAP HANA dynamic tiering must be deployed on a dedicated VM in the same Compute Engine zone as the SAP HANA system it supports.

The following diagram shows a SAP HANA system on one Compute Engine VM instance and a dynamic tiering server on another. Both VM instances are in the same Virtual Private Cloud subnetwork and the same Compute Engine zone.

The `/hana/shared` and `/hanabackup` directories are stored on persistent disks that are mounted directly to the VM for SAP HANA and mounted via NFS to the VM for the dynamic tiering server. The dynamic tiering server uses a single persistent disk that is partitioned into three volumes for the `usr/sap`, `/hana/data_es`, and `/hana/log_es` directories.

![Deployment Layout](https://docs.cloud.google.com/static/sap/docs/images/hana-dynamic-tiering.png)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
