---
url: https://docs.cloud.google.com/compute/docs/about-confidential-vm/
title: About Confidential VM \u00a0|\u00a0 Compute Engine \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:19:08.474518+00:00
---

# About Confidential VM  |  Compute Engine  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/compute/docs/about-confidential-vm/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ Compute Engine ](https://docs.cloud.google.com/compute/docs)
  * [ Guides ](https://docs.cloud.google.com/compute/docs/overview)



Send feedback 

#  About Confidential VM Stay organized with collections  Save and categorize content based on your preferences. 

A Confidential VM is a Compute Engine VM that uses a [specific machine type](https://docs.cloud.google.com/confidential-computing/confidential-vm/docs/supported-configurations#machine-type-cpu-zone) and keeps your sensitive code and other data encrypted in memory during processing, that is, it performs _encryption-in-use_. Together with [_encryption-at-rest_](https://docs.cloud.google.com/docs/security/encryption/default-encryption) and [_encryption-in-transit_](https://docs.cloud.google.com/docs/security/encryption-in-transit), Confidential VM can help keep your data and applications encrypted at all times.

For a more detailed conceptual overview, see [Confidential VM overview](https://docs.cloud.google.com/confidential-computing/confidential-vm/docs/confidential-vm-overview).

To get started using Confidential VM, see [Create a Confidential VM instance](https://docs.cloud.google.com/confidential-computing/confidential-vm/docs/create-a-confidential-vm-instance).

You can manage your Confidential VMs in some of the following ways:

  * You can use organization policy constraints to [ensure that instances created in your organization are Confidential VMs](https://docs.cloud.google.com/confidential-computing/confidential-vm/docs/enforce-confidential-vm-use).

  * You can use Cloud Monitoring and Cloud Logging to [monitor and validate your Confidential VM instances](https://docs.cloud.google.com/confidential-computing/confidential-vm/docs/monitor-integrity).

  * You can use shared Virtual Private Cloud (VPC) networks, organization policy constraints, and firewall rules to [set up a security perimeter](https://docs.cloud.google.com/confidential-computing/confidential-vm/docs/restrict-confidential-vm-interaction) that ensures your Confidential VM instances can only interact with other Confidential VM instances.

  * With the A3 machine type, you can create a Confidential VM instance that uses Intel TDX and has an attached NVIDIA H100 GPU. For more information, see [Confidential VM supported configurations](https://docs.cloud.google.com/confidential-computing/confidential-vm/docs/supported-configurations).

  * With the G4 machine type, you can create a Confidential VM instance that uses AMD SEV and has an attached NVIDIA RTX PRO 6000 GPU. For more information, see [Confidential VM supported configurations](https://docs.cloud.google.com/confidential-computing/confidential-vm/docs/supported-configurations).




For enhanced block storage security with Confidential VM, you can use [Confidential mode for Hyperdisk Balanced](https://docs.cloud.google.com/compute/docs/disks/disk-encryption#conf_hdb). Confidential mode for Hyperdisk Balanced adds another layer of security by enabling hardware-based encryption of disk data. Hyperdisk volumes in Confidential mode use [Cloud HSM](https://docs.cloud.google.com/kms/docs/hsm) and Trusted Execution Environments (TEE) to provide additional cryptographic isolation. For more information about TEEs, see [Trusted Execution Environment Explainer](https://services.google.com/fh/files/misc/confidential_computing_overview.pdf).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
