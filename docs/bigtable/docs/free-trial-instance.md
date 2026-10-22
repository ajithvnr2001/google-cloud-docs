---
url: https://docs.cloud.google.com/bigtable/docs/free-trial-instance/
title: Free trial instances overview \u00a0|\u00a0 Bigtable \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T12:36:51.370514+00:00
---

# Free trial instances overview  |  Bigtable  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/bigtable/docs/free-trial-instance/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Bigtable ](https://docs.cloud.google.com/bigtable/docs)
  * [ Guides ](https://docs.cloud.google.com/bigtable/docs/overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Free trial instances overview

Bigtable free trial instances let you explore database features and test high-throughput read and write workloads for up to 90 days at no cost. With a 1-node SSD cluster and up to 500 GB of storage, you can ingest large datasets, query your data, and connect to services like BigQuery and Dataflow.

## Key use cases

You can [create a Bigtable free trial instance](https://docs.cloud.google.com/bigtable/docs/create-free-trial-instance) to evaluate the following capabilities:

  * Ingesting large volumes of data

Bigtable instances are designed to store massive datasets, capable of handling petabytes of information. A Bigtable free trial instance provides up to **500 GB of storage**. You can begin by importing large quantities of data, such as time-series, telemetry logs, or machine learning data, into your tables.

  * Executing high-throughput queries

Bigtable is optimized for high read and write throughput with low latency, supporting millions of operations per second. A **1-node SSD cluster** in your Bigtable free trial instance lets you test your application's performance by running high-volume read and write operations against your tables with [SSD-backed performance](https://docs.cloud.google.com/bigtable/docs/performance#typical-workloads).

  * Querying data with SQL

You can use Bigtable Studio to run familiar SQL queries to explore and query your Bigtable data. This lets you use a language you already know to interact with Bigtable's flexible, adaptable data model.

  * Integrating with Google Cloud services

Bigtable **integrates with other Google Cloud products** like BigQuery for complex analytical queries and Dataflow for building data processing pipelines. You can connect your Bigtable free trial instance to these services to analyze and process your data at scale.




## Cost and eligibility

A Bigtable free trial instance is available at no cost to both existing and new Google Cloud customers.

**Note:** If you're a new Google Cloud customer, you might also be eligible for the [Google Cloud 90-day, $300 free trial](https://docs.cloud.google.com/free/docs/free-cloud-features#free-trial) that offers $300 in free Cloud Billing credits to pay for any Google Cloud resources. The Bigtable free trial instance is in addition to the $300 free trial credits offered by the Google Cloud free trial, and you don't need to use any free Cloud Billing credits to create a Bigtable free trial instance.

For more information about the Bigtable free trial instance, see the following table:

Eligibility  |  A 10-day trial period is available to any user with a Google Account.   
---|---  
Initiation  |  The 10-day period starts automatically when you create a Bigtable free trial instance.  A billing account isn't required to create a Bigtable free trial instance. As an option, you can extend the trial to 90 days by enabling billing.   
Free trial extension  |  You can extend the 10-day trial period to 90 days by enabling billing for the project with your Bigtable free trial instance.  If you already have an active Cloud Billing account, you can [extend the free trial period](https://docs.cloud.google.com/bigtable/docs/create-free-trial-instance#extend) in the Google Cloud console.  If you are a new Google Cloud customer, sign in to the Google Cloud console with your Google Account and set up a Cloud Billing account with your [ credit card or other payment method](https://docs.cloud.google.com/billing/docs/how-to/payment-methods#available_payment_methods) first before creating a Bigtable free trial instance. Google uses this payment information to verify your identity. We don't charge your Bigtable instance unless you explicitly [ upgrade your Cloud Billing account to a paid account](https://docs.cloud.google.com/free/docs/free-cloud-features#how-to-upgrade), and you [ upgrade your Bigtable free trial instance](https://docs.cloud.google.com/bigtable/docs/create-free-trial-instance#upgrade).   
Duration  |  The free trial ends when one of the following occurs: 

  * 10 days have elapsed since you created your Bigtable free trial instance, and you didn't extend the free trial period. 
  * You have extended the free trial period to 90 days and 90 days have elapsed since you created your Bigtable free trial instance. 
  * You upgrade your Bigtable free trial instance. 
  * You delete the Bigtable free trial instance. You can't create another Bigtable free trial instance after you've deleted your first Bigtable free trial instance. 

If you don't upgrade your Bigtable free trial instance after the 10-day trial period or a 90-day extended trial period, the instance stops serving requests and enters a 30-day grace period. During the grace period, the data in the instance is retained and you can still upgrade your Bigtable free trial instance. If you don't upgrade your Bigtable free trial instance by the end of the 30-day grace period, the instance, along with the data in it, is deleted.  **Note:** An active Cloud Billing account is required to keep using your Bigtable free trial instance. If your [ Google Cloud free trial ends](https://docs.cloud.google.com/free/docs/free-cloud-features#end) before the end of your Bigtable free trial instance free trial period, then you need to [ upgrade your Cloud Billing account to a paid account](https://docs.cloud.google.com/free/docs/free-cloud-features#how-to-upgrade) to continue using your Bigtable free trial instance.   
Service level agreement (SLA)  |  SLAs don't apply to Bigtable free trial instances. The Bigtable free trial instance is intended to help you learn and explore Bigtable. We don't recommend running production applications in your Bigtable free trial instance.   
Location availability  |  Region availability for Bigtable free trial instances might be different compared to standard Bigtable instances and not all regions might be available at all times.   
Trial capabilities  |  Your Bigtable free trial instance has the following limitations compared to standard Bigtable instances. 

  * **Scaling is disabled**. Bigtable free trial instance provides one cluster with one node. You can't [add extra clusters or scale nodes manually or automatically](https://docs.cloud.google.com/bigtable/docs/modifying-instance) in the Bigtable free trial instance cluster. 
  * **Replication is disabled**. [Replication](https://docs.cloud.google.com/bigtable/docs/replication-overview) is disabled for a Bigtable free trial instance. 
  * **Only Google-managed encryption**. You can't use [Customer-managed encryption keys (CMEK)](https://docs.cloud.google.com/bigtable/docs/cmek) with a Bigtable free trial instance. 
  * **500 GB SSD storage**. Because scaling isn't available, You can't increase the amount of available storage by changing the number of nodes in a cluster or by setting a storage utilization target. 
  * **10 tables per instance**. You can create a maximum of 10 tables in a free trial instance. Continuous materialized views count as tables. 
  * **One continuous materialized view per table**. You can create one [continuous materialized view](https://docs.cloud.google.com/bigtable/docs/continuous-materialized-views) per table. 
  * **Three standard or automated backups per table**. You can retain a maximum of three [standard or automated backups](https://docs.cloud.google.com/bigtable/docs/backup) per table. 
  * **One hot backup per table**. You can retain a maximum of one [hot backup](https://docs.cloud.google.com/bigtable/docs/backup) per table. 
  * **No Data Boost**. You can't configure a [Data Boost](https://docs.cloud.google.com/bigtable/docs/data-boost-overview) app profile for a Bigtable free trial instance or convert an existing standard app profile to a Data Boost app profile. 

  
Quotas and limits  |  All Bigtable [quotas and limits](https://docs.cloud.google.com/bigtable/quotas) apply to Bigtable free trial instances.   
  
## Upgrading Bigtable free trial instances

After you upgrade your Bigtable free trial instance you get the following benefits:

  * Instant switch to a standard instance without loss of data or downtime.
  * Your Bigtable free trial instance runs uninterrupted beyond the 10-day free trial period.
  * Access to scaling and replication for your Bigtable instance. You can add extra clusters in more locations and scale each cluster by adding more nodes to it.



You can [upgrade your Bigtable free trial instance](https://docs.cloud.google.com/bigtable/docs/create-free-trial-instance#upgrade) at any time during the free trial period. You aren't charged unless you explicitly upgrade your Bigtable free trial instance to a standard instance.

## Troubleshooting FAQs

Why can't I create a Bigtable free trial instance in my project?
    You can create one Bigtable free trial instance per project. If you've already created a Bigtable free trial instance in your project, you can't create another one, even if you delete the original instance.
How can I create more than one cluster in a Bigtable free trial instance or add extra nodes ?
    If you want to create more than one cluster or change the number of nodes, [upgrade your Bigtable free trial instance](https://docs.cloud.google.com/bigtable/docs/create-free-trial-instance#upgrade).
My Bigtable free trial instance has been disabled. How can I re-enable it?
    If you've completed the Bigtable 10-day free trial period or an extended 90-day free trial period the Bigtable free trial instance is disabled and enters a 30-day grace period. You can start using your instance again by [upgrading your Bigtable free trial instance](https://docs.cloud.google.com/bigtable/docs/create-free-trial-instance#upgrade) during the 30-day grace period.

## Support

For more information about getting support for your Bigtable free trial instance instance, see [Get support](https://docs.cloud.google.com/bigtable/docs/support/getting-support).

## What's next

  * [Create a Bigtable free trial instance](https://docs.cloud.google.com/bigtable/docs/create-free-trial-instance)
  * Learn more about Bigtable [Instances, clusters, and nodes](https://docs.cloud.google.com/bigtable/docs/instances-clusters-nodes).
  * For details on Bigtable pricing after the free trial period, see the [Pricing page](https://docs.cloud.google.com/bigtable/pricing).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
