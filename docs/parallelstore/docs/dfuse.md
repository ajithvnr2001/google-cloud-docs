---
url: https://docs.cloud.google.com/parallelstore/docs/dfuse/
title: Managed Lustre \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-15T10:22:12.540867+00:00
---

# Managed Lustre  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/parallelstore/docs/dfuse/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Storage ](https://docs.cloud.google.com/docs/storage)
  * [ Managed Lustre ](https://docs.cloud.google.com/managed-lustre/docs/overview)



Send feedback 

#  Managed Lustre Stay organized with collections  Save and categorize content based on your preferences. 

Google Cloud Managed Lustre delivers a high-performance, fully managed parallel file system optimized for AI and HPC applications. With multi-petabyte-scale capacity and up to 10 TBps throughput, Managed Lustre facilitates the migration of demanding workloads to the cloud.

## Highlights

  * Developed in collaboration with DDN, the leading provider and primary maintainer of the Lustre file system.
  * Supports extreme IOPs and low latency.
  * POSIX compliance ensures compatibility with existing applications, tools, and workflows.
  * Integrated with Compute Engine and Google Kubernetes Engine, allowing you to mount high-performance storage to your virtual machines and containerized applications.
  * Provides high-speed and fully managed transfers into and out of Cloud Storage.
  * [Maintenance policies](https://docs.cloud.google.com/managed-lustre/docs/maintenance) give you control over when instance maintenance occurs.



## Specifications

Metric | Result  
---|---  
Storage capacity  | From 9,000 GiB up to 84,016,000 GiB (80.1 PiB)  
Throughput | Up to 10 TBps  
IOPS  | Up to 5,800 read IOPS per TiB  
Up to 5,600 write IOPS per TiB  
Metadata performance  | Per 72 GBps of throughput, up to:

  * 410,000 stats per second
  * 115,000 creates per second
  * 95,000 deletes per second

Up to a maximum of 22 times the base value.  
Maximum file size | 0.5 PiB  
  
For more information about the different performance tiers available, see [Performance tiers](https://docs.cloud.google.com/managed-lustre/docs/performance-tiers). For more information about quotas and limits, see [Quotas and limits](https://docs.cloud.google.com/managed-lustre/docs/quotas).

## Use Cases

  * **High-performance computing** : Managed Lustre excels in HPC environments where multiple compute nodes need fast and consistent access to shared data for simulations, modeling, and analysis.

  * **Machine learning** : Managed Lustre can handle the large datasets and high throughput requirements of machine learning workloads, enabling efficient training and inference.




## Data protection

Managed Lustre encrypts data at rest and data in transit.

## Encryption at rest

All data stored in a Managed Lustre file system is encrypted at rest.

For more information, see [Encryption at rest](https://docs.cloud.google.com/docs/security/encryption/default-encryption).

## Encryption in transit

While the Lustre protocol itself doesn't encrypt traffic between clients and servers, all in-transit data to and within Google Cloud is encrypted. This includes data transfers between Managed Lustre and Cloud Storage.

For more information, see [Encryption in transit](https://docs.cloud.google.com/docs/security/encryption-in-transit).

## Pricing

See the [Pricing](https://cloud.google.com/products/managed-lustre/pricing) page for details.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
