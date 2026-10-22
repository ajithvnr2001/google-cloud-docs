---
url: https://docs.cloud.google.com/billing/docs/how-to/infra-mgmt-essentials/
title: About Infrastructure Management Essentials \u00a0|\u00a0 Cloud Billing \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T12:38:37.620301+00:00
---

# About Infrastructure Management Essentials  |  Cloud Billing  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/billing/docs/how-to/infra-mgmt-essentials/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Costs and usage management ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Cloud Billing ](https://docs.cloud.google.com/billing/docs)
  * [ Guides ](https://docs.cloud.google.com/billing/docs/concepts)



Send feedback 

#  About Infrastructure Management Essentials Stay organized with collections  Save and categorize content based on your preferences. 

**Preview**

This product or feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA products and features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

Infrastructure Management Essentials lets you use a set of infrastructure management and data protection services at scale. These services are metered as a single fixed SKU that is based on the compute core (vCPU) hours that you consume each billing cycle.

This feature is designed for cloud architects, platform administrators, enterprise infrastructure managers, and billing administrators who want to scale operational consumption with more predictability.

Infrastructure Management Essentials works at the Google Cloud project level and provides you with integrated billing management for your use of the included services. Because you pay a single fixed price for use of these services, you get to consume these services at a fixed price, no matter how much you use them.

## Availability

Infrastructure Management Essentials is designed to be used at scale in production environments. However, its availability is subject to the following:

  * It's a Preview offering and therefore might cease to be available for the participating projects at any given time.
  * Whenever Infrastructure Management Essentials becomes unavailable, your usage of the included services is not interrupted, but your usage reverts to the standard billing for each service.



## Included services and use cases

When you enable Infrastructure Management Essentials in your Google Cloud project, your usage of the included Google Cloud services is bundled and billed by using a single SKU.

Note that usage of these services is still subject to respective quotas, rate limits, and the enablement of service-specific APIs in the target Google Cloud project.

The following table lists the use cases for the Google Cloud services that are included with Infrastructure Management Essentials, and the SKUs that are applied when you don't use it:

Use case | Google Cloud services included with Infrastructure Management Essentials | SKUs used when Infrastructure Management Essentials is not enabled  
---|---|---  
Infrastructure management | [VM Manager](https://docs.cloud.google.com/compute/docs/vm-manager) | [VM Manager Usage](https://cloud.google.com/skus?e=48754805&filter=VM%20Manager%20Usage&currency=USD)  
The [evaluation service of Workload Manager](https://docs.cloud.google.com/workload-manager/docs/about-evaluations) | [Rule Evaluation](https://cloud.google.com/skus?e=48754805&filter=Workload%20Manager%20Rule%20Evaluation&currency=USD)  
Data protection | [Asynchronous Replication](https://docs.cloud.google.com/compute/docs/disks/async-pd/about) |  [Async Replication Protection](https://cloud.google.com/skus?e=48754805&filter=Async%20Replication%20Protection&currency=USD)  
[Instant Snapshot operation costs](https://docs.cloud.google.com/compute/docs/disks/instant-snapshots#billing) | [Instant Snapshot operations in all regions](https://cloud.google.com/skus?e=48754805&filter=Instant%20Snapshot%20Operations&currency=USD)  
The backup management dimension of [Google Cloud Backup and DR Service](https://docs.cloud.google.com/backup-disaster-recovery/docs/concepts/backup-dr) | 

  * [Backup SKU for DB2, Oracle, SAP HANA, SAP ASE and SAP MAXdb](https://cloud.google.com/skus?e=48754805&filter=Backup%20SKU%20for%20DB2%2C%20Oracle%2C%20SAP%20HANA%2C%20SAP%20ASE%20and%20SAP%20MAXdb&currency=USD)
  * [Backup SKU for Microsoft SQL Server, MySQL, PostgreSQL and MongoDB](https://cloud.google.com/skus?e=48754805&filter=Backup%20SKU%20for%20Microsoft%20SQL%20Server%2C%20MySQL%2C%20PostgreSQL%20and%20MongoDB&currency=USD)
  * [Default Backup SKU for VM (GCE and VMware) and File system data](https://cloud.google.com/skus?e=48754805&filter=Default%20Backup%20SKU%20for%20VM%20\(GCE%20and%20VMware\)%20and%20File%20system%20data&currency=USD)
  * [Virtual Clone usage](https://cloud.google.com/skus?e=48754805&filter=Backup%20and%20DR%20Service%20Virtual%20clone%20usage&currency=USD)

  
The backup management dimension of [Backup for GKE](https://docs.cloud.google.com/kubernetes-engine/docs/add-on/backup-for-gke/concepts/backup-for-gke) | [Backup for GKE management](https://cloud.google.com/skus?e=48754805&filter=Backup%20for%20GKE%20management&currency=USD)  
  
## Pricing

When you enable Infrastructure Management Essentials for your Google Cloud project, your usage of the included services is metered by using a single SKU, the details of which are as follows:

Service | SKU description | SKU ID | Usage unit | Unit price  
---|---|---|---|---  
Compute | **Infrastructure Management Essentials** | `5C7D-DA7B-FCC6` | vCPU hour | 0.006 USD  
  
To learn about the savings potential of Infrastructure Management Essentials, contact [Google Cloud Sales](https://cloud.google.com/contact).

## Billing cycle

Infrastructure Management Essentials has a minimum subscription term of 30 days, after which you can cancel your subscription to it at any time.

After you enable Infrastructure Management Essentials in your Google Cloud project, you cannot revert to the standard billing for the included services until this 30-day term concludes.

## What's next

  * [Enable or disable Infrastructure Management Essentials](https://docs.cloud.google.com/billing/docs/how-to/infra-mgmt-essentials-enable-disable).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
