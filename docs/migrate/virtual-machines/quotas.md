---
url: https://docs.cloud.google.com/migrate/virtual-machines/quotas/
title: Quotas and limits \u00a0|\u00a0 Migrate to Virtual Machines \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:56:21.388319+00:00
---

# Quotas and limits  |  Migrate to Virtual Machines  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/migrate/virtual-machines/quotas/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Migration ](https://docs.cloud.google.com/docs/migration)
  * [ Migrate to Virtual Machines ](https://docs.cloud.google.com/migrate/virtual-machines/docs/5.0)



Send feedback 

#  Quotas and limits Stay organized with collections  Save and categorize content based on your preferences. 

To reduce the risk of abuse, Google Cloud enforces limits on the usage of Google Cloud services. New Google Cloud customers using Migrate to Virtual Machines should familiarize themselves with the limits that are applicable to their migration. 

Migrate to Virtual Machines uses the following Google Cloud resources which are subject to limits:

Google Cloud Resource | How used in Migrate to Virtual Machines  
---|---  
[Compute instances](https://docs.cloud.google.com/compute/quotas) | Needed to support migrated VMs, Migrate to Virtual Machines Manager, Cloud Extensions, and worker nodes.  
[Persistent disks](https://docs.cloud.google.com/compute/quotas#disk_quotas) | When deploying Cloud Extensions, ensure that you have SSD (solid-state disk) Persistent Disk quota set high enough to support the number of Cloud Extensions you intend to create. For more, see [Cloud Extensions Overview](https://docs.cloud.google.com/migrate/virtual-machines/docs/5.0/concepts/cloud-extensions/overview).  
External [IP addresses](https://docs.cloud.google.com/compute/quotas#ip_addresses) | The migration process creates Compute Engine VMs, and can create IP addresses for access over the public Internet (such as for inbound access from your corporate data center).  
[Cloud Storage](https://docs.cloud.google.com/storage/quotas) | While you are migrating, Migrate to Virtual Machines uses Cloud Storage to hold data that is used by your applications on Compute Engine VMs.  
[VPC networks](https://docs.cloud.google.com/vpc/docs/quota) | Migrate to Virtual Machines uses Virtual Private Cloud (VPC) for secure access to Google Cloud during migration. Ensure that your quotas for networks, subnets, IP addresses, and more will support your migration.  
  
The number of worker nodes is equal to the number of VMs that are in [Detach](https://docs.cloud.google.com/migrate/virtual-machines/docs/5.0/concepts/planning-a-migration/vm-migration-lifecycle#detach) phase.

## Viewing your current quota usage

###  Console 

The [quotas page](https://console.cloud.google.com/iam-admin/quotas) on the Google Cloud console shows your project's current quotas and their usage.

## Requesting increases to your quotas

See the [Compute Engine documentation](https://docs.cloud.google.com/compute/quotas#request_quotas) for instructions on how to request a quota increase.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
