---
url: https://docs.cloud.google.com/vmware-engine/docs/concepts-vmware-engine-protected/
title: VMware Engine Protected offering \u00a0|\u00a0 Google Cloud VMware Engine \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T09:34:50.901096+00:00
---

# VMware Engine Protected offering  |  Google Cloud VMware Engine  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/vmware-engine/docs/concepts-vmware-engine-protected/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ VMware Engine ](https://docs.cloud.google.com/vmware-engine/docs)
  * [ Resources ](https://docs.cloud.google.com/vmware-engine/docs/resources)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# VMware Engine Protected offering

This page describes the Google Cloud VMware Engine Protected offering. Google Cloud offers bundled pricing for both VMware Engine and Backup and DR Service. You can backup and restore all of the virtual machines on a VMware Engine node with first-party Backup and DR software for only an incremental add-on cost per VMware Engine node. This gives you centralized, fast, and cost-efficient backup and recovery capabilities for your VMware Engine VMs.

## Capabilities

VMware Engine Protected offers the following capabilities:

  * Dedicated, managed VMware Engine private-cloud-as-a-service that's available globally, and sold and supported directly through Google Cloud.
  * Backup management: Centrally managed, fast, and cost-efficient incremental-forever backups.
  * Disaster recovery: Recover VMs across regions and projects.
  * Ransomware recovery: Instantly access different point-in-time backup copies in parallel to quickly identify a desirable recovery candidate.
  * Test data management: Reduce time-to-test new patches and features, and run business reporting and analytics against production data. Reduce management burden with self-service auto refresh of data.



## Key benefits

VMware Engine Protected offers several key benefits, including the following:

  * Google-native solution: The Google Cloud-native Backup and DR Service integrates with the Google Cloud ecosystem, including simplified sign-on via SSO, seamless integration with Identity and Access Management (IAM), Cloud Logging, Cloud Monitoring, Key Management, and more.
  * Centralized management: You can manage backups for various [Google Cloud and hybrid workloads](https://cloud.google.com/backup-disaster-recovery/docs/supportmatrix-backupdr) all from one place.
  * Low TCO: Efficient, incremental-forever backup leveraging changed-block tracking significantly reduces the time it takes for you to perform backups, minimizes impact on production servers, and optimizes bandwidth and storage utilization to lower costs.
  * Achieve lower RTO: Instantly mount and access VMware Engine VMs from backups stored in Cloud Storage. No need to first move backup data to warm storage to access it.
  * Simplified pricing: VMware Engine Protected is offered at a fixed price per node, regardless of the amount of data you protect or the number of VMs, simplifying pricing and offering better cost predictability.



See the [ VMware Engine pricing](https://cloud.google.com/vmware-engine/pricing) page to review the pricing for protecting VMware Engine nodes in your region.

## Pricing details

Pricing is only for protecting VMware Engine—whole VM backups. It does not include backup management charges for any agent-based backups, such as charges for application consistent backups for SAP HANA, SQL Server, MySQL, Postgres, or File System agents, for example. To estimate charges for agent-based backups, the production size for each of these database types is needed. Agent-based backups are priced according to standard [ Backup and DR Service pricing](https://cloud.google.com/backup-disaster-recovery/pricing). Backup landing storage costs are separate and additional— VMware Engine Protected does not include storage.

To learn more about how to get started with VMware Engine Protected, refer to [Configure Google Cloud VMware Engine for Backup and DR protection](https://cloud.google.com/backup-disaster-recovery/docs/configuration/prepare-vmware).

## What's next

  * Learn about [committed use discounts](https://docs.cloud.google.com/vmware-engine/docs/cud).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
