---
url: https://docs.cloud.google.com/spanner-omni/system-requirements/
title: Spanner Omni system requirements \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T04:28:28.633500+00:00
---

# Spanner Omni system requirements  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/spanner-omni/system-requirements/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Spanner Omni ](https://docs.cloud.google.com/spanner-omni)
  * [ Guides ](https://docs.cloud.google.com/spanner-omni/overview)



Send feedback 

#  Spanner Omni system requirements Stay organized with collections  Save and categorize content based on your preferences. 

This document describes the hardware and software requirements for deploying Spanner Omni on-premises and in cloud environments.

## On-premises requirements

Deploying Spanner Omni on-premises requires the following:

### Hardware requirements

The right hardware helps Spanner Omni and the CLI run reliably and efficiently on-premises. Check these minimum and recommended configurations to optimize your deployment.

#### Server hardware

Server hardware should meet the following recommended configurations:

OS and platform | Recommended hardware configuration  
---|---  
**Linux** | 

  * x86-64 CPU
  * 4 GB of RAM for every vCPU allocated to Spanner
  * 20 or more GB of disk space

  
**macOS** (Developer version) | 

  * M1, M2, or M3 CPU
  * 4 GB of RAM
  * 10 GB of disk space

  
  
#### Spanner Omni CLI hardware

The Spanner Omni CLI should meet the following recommended hardware configurations:

OS and platform | Recommended hardware configuration  
---|---  
**Linux** | 

  * x86-64 or ARM CPU
  * 256 MB of RAM
  * 2 GB of disk space

  
**macOS** | 

  * M1, M2, or M3 CPU
  * 256 MB of RAM
  * 2 GB of disk space

  
  
### Software requirements

For stable and secure operation, Spanner Omni needs supported operating systems and container environments. Confirm your environment meets these software specifications before you proceed.

#### Server software

Server software should meet the following requirements:

OS and platform | Recommended software requirements  
---|---  
**Linux** | 

  * RHEL 9, Ubuntu 22
  * Linux kernel version 5.3+
  * For container deployments: 
    * Docker Engine 24.0+
    * Podman 3.0+
    * Kubernetes 1.31+

  
**macOS** (Developer version) | 

  * macOS 14.7+
  * Docker Engine 24.0+
  * Podman 3.0+

  
  
#### Spanner Omni CLI software

The Spanner Omni CLI software should meet the following requirements:

OS and platform | Software requirements  
---|---  
**Linux** | RHEL 8+, Ubuntu 20+  
**macOS** | macOS 14.7+  
  
### Storage

Proper storage setup is important for data durability and high performance. Use these recommendations for SSDs, file systems, and disk I/O to meet high-availability standards.

  * For each VM, use a dedicated, persistent, and attachable solid-state drive (SSD) with an `ext4` file system to store your data.
  * Allocate 500 GB of storage per vCPU.
  * Make sure the storage is durable enough for a high-availability system.
  * Spanner Omni is tested with Dell PowerFlex block storage, which is recommended for production usage.
  * Local disks aren't supported.



#### Disk I/O

Your disk I/O should achieve 500 IOPS and 30 MB per second per vCPU.

## Cloud requirements

Deploying Spanner Omni in cloud environments requires the following:

### Google Cloud

Review the compute and storage specifications for Google Kubernetes Engine (GKE) and Compute Engine. Meeting these requirements optimizes database performance on the cloud infrastructure.

#### GKE-based deployment

A GKE-based deployment has the following requirements:

  * Nodes with at least 4 vCPU and at least 16 GB RAM

  * Zonal persistent disk (`pd-ssd`) or Hyperdisk Balanced for storage




#### VM-based deployment on Google Cloud

A VM-based deployment on Google Cloud requires a VM with 4 vCPUs and 16 GB RAM. For storage, use a zonal persistent disk (`pd-ssd`) or Hyperdisk Balanced.

### Amazon Web Services (AWS)

To deploy Spanner Omni on AWS, follow the Amazon Elastic Kubernetes Service (EKS) and Amazon Elastic Compute Cloud (EC2) configuration requirements. These requirements ensure compatibility with AWS-specific features, such as `/dev/vmclock0` for precise timekeeping.

All AWS deployments must access the `/dev/vmclock0` device. To support this, do the following:

  1. Configure your environment with a supported machine type (for example, `M7a`) and Amazon Linux 2023.

  2. Enable read permissions on the host by running `sudo chmod a+r /dev/vmclock0`.

  3. Ensure the application can access the device:

     * For Docker, pass the device using `--device /dev/vmclock0`.

     * For Kubernetes, mount the device path into the Pod specification.




#### EKS-based deployment

An EKS-based deployment requires nodes with 4 vCPU and 16 GB. For storage, use SSD-backed EBS (Zonal, `io2` Block Express or `gp3`) volumes.

#### VM-based deployment on AWS

A VM-based deployment on AWS requires a minimum of 4 vCPUs and 16 GB RAM. For storage, use SSD-backed EBS (Zonal, `io2` Block Express or `gp3`) volumes.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
