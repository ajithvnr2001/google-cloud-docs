---
url: https://docs.cloud.google.com/alloydb/docs/free-trial-cluster/
title: AlloyDB free trial clusters overview \u00a0|\u00a0 AlloyDB for PostgreSQL \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-20T20:45:56.825861+00:00
---

# AlloyDB free trial clusters overview  |  AlloyDB for PostgreSQL  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/alloydb/docs/free-trial-cluster/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ AlloyDB for PostgreSQL ](https://docs.cloud.google.com/alloydb/docs)
  * [ Guides ](https://docs.cloud.google.com/alloydb/docs/overview)



Send feedback 

#  AlloyDB free trial clusters overview Stay organized with collections  Save and categorize content based on your preferences. 

This page provides information about the AlloyDB for PostgreSQL free trial cluster.

An AlloyDB free trial cluster lets you test majority of AlloyDB features for up to 30 days without any financial commitment through a 8 vCPU basic primary instance that automatically scales storage up to 1TB.

After you create a free trial cluster, you can start trying out AlloyDB capabilities, including but not limited to the following:

  * [Increased transactional performance and scalability](https://docs.cloud.google.com/alloydb/docs/overview)
  * [Accelerated analytical queries with columnar engine](https://docs.cloud.google.com/alloydb/docs/columnar-engine/about)
  * [Built-in generative AI with Gemini Enterprise Agent Platform integration](https://docs.cloud.google.com/alloydb/docs/ai)
  * [Optimized queries with Index advisor](https://docs.cloud.google.com/alloydb/docs/index-advisor-overview)
  * [AI-driven development with Database Studio](https://docs.cloud.google.com/alloydb/docs/manage-data-using-studio)



The following table gives information about AlloyDB free trial cluster:

Eligibility  |  Both existing and new Google Cloud customers are eligible. The free trial cluster is open only to new AlloyDB projects.  If you're a new Google Cloud customer, you might also be eligible for the [Google Cloud 90-day, $300 free trial](https://docs.cloud.google.com/free/docs/free-cloud-features#free-trial) that offers $300 in free Cloud Billing credits to pay for any Google Cloud resources. The AlloyDB free trial clusters is in addition to the $300 free trial credits offered by the Google Cloud free trial.   
---|---  
Billing  |  Before you create an AlloyDB trial cluster, understand the following: 

  * **Existing user** : Ensure [Cloud Billing is enabled](https://docs.cloud.google.com/billing/docs/how-to/verify-billing-enabled#console) for your project.
  * **New user** : Sign in to the Google Cloud console with your Google Account and [set up a Cloud Billing account](https://docs.cloud.google.com/billing/docs/how-to/verify-billing-enabled#console) with your credit card or other payment method.

We don't charge you for free trial clusters and instance resources, but you are charged for data transfer costs for connections outside the region, through the public internet, and for taking and storing your final backup. For more information, see [Trial inclusions and conditions](https://docs.cloud.google.com/alloydb/docs/free-trial-cluster#trial-inclusion").   
Duration  |  You can explore AlloyDB features with free trial clusters until one of the following occurs: 

  * 30 days have elapsed since you first created your free trial cluster. 
  * You have deleted your free trial cluster. 

You can [upgrade to a paid cluster](https://docs.cloud.google.com/alloydb/docs/create-free-trial-cluster#upgrade) at any time during your 30-day trial period.  If you don't upgrade your free trial cluster before the trial period, then your instance stops serving requests. Your cluster along with your data is maintained at no cost for an additional 15-day grace period. After the 15-day grace period completes, your cluster is scheduled for deletion. If you explicitly delete the free trial cluster before the 30-day trial period or the 15-day grace period, then the cluster, along with the data in it, is deleted. No backups are taken.   
Service level agreement (SLA)  |  SLAs don't apply to free trial clusters. These clusters are designed for testing and experimenting with AlloyDB, and are not recommended for running applications in a production environment.   
Available regions  |  AlloyDB is available in all regions. For more information, see [AlloyDB locations.](https://docs.cloud.google.com/alloydb/docs/locations)  
  
## Trial inclusions and conditions

The following inclusions and conditions apply to a free trial cluster:

  * One free trial cluster allowed per project lifecycle.
  * 30-day free trial cluster.
  * No [SLA](https://cloud.google.com/alloydb/sla) guarantees.
  * All AlloyDB [quotas and limits](https://docs.cloud.google.com/alloydb/quotas) apply.
  * One free trial cluster provides up to 1 TB of storage capacity and 8 vCPU of single zone primary instance for testing purposes. You can't edit a free trial cluster to increase its storage or compute capacity limits. To increase the storage and compute capacity of a free trial cluster, [upgrade to a paid instance](https://docs.cloud.google.com/alloydb/docs/create-free-trial-cluster#upgrade-free-trial).
  * Maximum of one read pool with 8 vCPU compute capacity.
  * Free trial clusters don't support [backup and restore](https://docs.cloud.google.com/alloydb/docs/backup/overview).
  * Cross region replication setups are not supported.
  * High availability is not supported.
  * No charge for free trial clusters and instance resources, but you are charged for data transfer costs for connections outside the region, through the public internet, and for taking and storing your final backup.

**Note:** Trial inclusions and conditions may be changed, suspended, or discontinued at any time without prior notice.

## Free trial cluster monitoring

You can monitor your free trial cluster using the following:

  * [AlloyDB System Insights dashboard](https://docs.cloud.google.com/alloydb/docs/monitor-instance#monitoring)
  * [Active or long-running queries](https://docs.cloud.google.com/alloydb/docs/monitor-active-queries)
  * [Query Insights tool](https://docs.cloud.google.com/alloydb/docs/query-insights-overview)



For more information about Online Transactional Processing (OLTP) benchmark and Online Analytical (OLAP) benchmark, see [AlloyDB for PostgreSQL Transactional (OLTP) Benchmarking Guide](https://services.google.com/fh/files/misc/alloydb_oltp_benchmarking_guide.pdf) and [AlloyDB for PostgreSQL Analytical (OLAP) Benchmarking Guide](https://services.google.com/fh/files/misc/alloydb_olap_benchmarking_guide.pdf) respectively.

## Upgrade your free trial cluster

You can upgrade your free trial cluster any time during your 30-day free trial cluster period or 15-day grace period.

During the trial, you are not charged for free trial clusters and instance resources, but you are charged for data transfer costs for connections outside the region, through the public internet, and for taking and storing your final backup.

After you upgrade your cluster to a paid cluster, you get the following benefits:

  * Instant switch to a paid cluster without loss of data or downtime.
  * Scale compute capacity by upgrading machine size to any size within the range of 2 vCPU to 128 vCPUs.
  * Ability to add multiple read pools, and add up to 20 read nodes per cluster.
  * Option to create backups and restore your backups.
  * Ability to create cross region replication setups.
  * Support for high availability.



For more information, see [Upgrade free trial cluster](https://docs.cloud.google.com/alloydb/docs/create-free-trial-cluster#upgrade).

## Post-trial period

If you don't upgrade and your trial period ends, then your instance is deleted and your cluster is maintained at no cost for an additional 15-day grace period.

After the 15-day grace period completes, the instance stops serving requests and is scheduled for deletion. A final backup of your data is retained for up to one year or until you explicitly delete it. Charges related to storing backups apply.

You can access your backups from the AlloyDB Backups page, and restore it to a paid AlloyDB cluster.

For more information, see [Restore from a backup](https://docs.cloud.google.com/alloydb/docs/backup/restore#backup).

## What's next

  * Learn about how to [create a free trial cluster](https://docs.cloud.google.com/alloydb/docs/create-free-trial-cluster).
  * Understand [AlloyDB quotas and limits](https://docs.cloud.google.com/alloydb/quotas).
  * Learn more about [AlloyDB pricing](https://cloud.google.com/alloydb/pricing).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
