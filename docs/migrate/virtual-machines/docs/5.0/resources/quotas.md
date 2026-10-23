---
url: https://docs.cloud.google.com/migrate/virtual-machines/docs/5.0/resources/quotas/
title: Quotas and limits \u00a0|\u00a0 Migrate to Virtual Machines \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:53:53.224845+00:00
---

# Quotas and limits  |  Migrate to Virtual Machines  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/migrate/virtual-machines/docs/5.0/resources/quotas/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Migration ](https://docs.cloud.google.com/docs/migration)
  * [ Migrate to Virtual Machines ](https://docs.cloud.google.com/migrate/virtual-machines/docs/5.0)
  * [ Resources ](https://docs.cloud.google.com/migrate/virtual-machines/docs/5.0/resources)



Send feedback 

#  Quotas and limits Stay organized with collections  Save and categorize content based on your preferences. 

To reduce the risk of abuse, Google Cloud enforces limits on the usage of Google Cloud services. New Google Cloud customers using Migrate to Virtual Machines should familiarize themselves with the limits that are applicable to their migration. 

Migrate to Virtual Machines uses the following Google Cloud resources which are subject to limits:

Google Cloud Resource | How used in Migrate to Virtual Machines  
---|---  
[Compute instances](https://docs.cloud.google.com/compute/quotas) | Needed to support migrated VMs.  
[Persistent disks](https://docs.cloud.google.com/compute/quotas#disk_quotas) | Persistent disks are attached to migrated VMs. Ensure that you set the quota high enough for the persistent disk types you intend to use.  
External [IP addresses](https://docs.cloud.google.com/compute/quotas#ip_addresses) | The migration process creates Compute Engine VMs, and can create IP addresses for access over the public Internet (such as for inbound access from your corporate data center).  
[VPC networks](https://docs.cloud.google.com/vpc/docs/quota) | Ensure that your quotas for networks, subnets, IP addresses, and more will support your migration.  
  
## Viewing your current quota usage

###  Console 

The [quotas page](https://console.cloud.google.com/iam-admin/quotas) on the Google Cloud console shows your project's current quotas and their usage.

## Requesting increases to your quotas

See the [Compute Engine documentation](https://docs.cloud.google.com/compute/quotas#request_quotas) for instructions on how to request a quota increase.

## Cloud sources limitations

You can host a maximum of 15 cloud sources (AWS sources, Azure sources, or both the sources combined) on a host project at a time. For example, you can host 10 AWS sources and 5 Azure sources on a host project at a time. Conversely, you can host 7 AWS sources and 8 Azure sources on a host project at a time. If you want to add a new cloud source to a project that already hosts 15 cloud sources, you must delete an existing source, and then add the new source. You can also try using a different project to host the new cloud source if you don't want to delete any existing sources.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
