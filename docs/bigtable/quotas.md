---
url: https://docs.cloud.google.com/bigtable/quotas/
title: Quotas and limits \u00a0|\u00a0 Bigtable \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T12:36:56.076100+00:00
---

# Quotas and limits  |  Bigtable  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/bigtable/quotas/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Bigtable ](https://docs.cloud.google.com/bigtable/docs)
  * [ Resources ](https://docs.cloud.google.com/bigtable/docs/resources)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Quotas and limits

**Note:** This page includes features that are available only in the Enterprise Plus edition. For more information, see [Editions overview](https://docs.cloud.google.com/bigtable/docs/editions-overview).

This document lists the quotas and system limits that apply to Bigtable.

  * _Quotas_ have default values, but you can typically request adjustments.
  * _System limits_ are fixed values that can't be changed.



Google Cloud uses quotas to help ensure fairness and reduce spikes in resource use and availability. A quota restricts how much of a Google Cloud resource your Google Cloud project can use. Quotas apply to a range of resource types, including hardware, software, and network components. For example, quotas can restrict the number of API calls to a service, the number of load balancers used concurrently by your project, or the number of projects that you can create. Quotas protect the community of Google Cloud users by preventing the overloading of services. Quotas also help you to manage your own Google Cloud resources.

The Cloud Quotas system does the following:

  * Monitors your consumption of Google Cloud products and services
  * Restricts your consumption of those resources
  * Provides a way to [request changes to the quota value](https://docs.cloud.google.com/docs/quotas/help/request_increase) and [automate quota adjustments](https://docs.cloud.google.com/docs/quotas/quota-adjuster)



In most cases, when you attempt to consume more of a resource than its quota allows, the system blocks access to the resource, and the task that you're trying to perform fails.

Quotas generally apply at the Google Cloud project level. Your use of a resource in one project doesn't affect your available quota in another project. Within a Google Cloud project, quotas are shared across all applications and IP addresses. 

For more information, see the [Cloud Quotas overview](https://docs.cloud.google.com/docs/quotas/overview). 

To adjust most quotas, use the Google Cloud console. For more information, see [Request a quota adjustment](https://docs.cloud.google.com/docs/quotas/help/request_increase). 

There are also _system limits_ on Bigtable resources. System limits can't be changed. 

**Note:** When you send multiple operations in a single batch, each operation in the batch counts towards the quota or limit.

## Quotas

This section describes default quotas that apply to all of your Bigtable usage.

### Admin operation quotas

The following quotas affect the number of Bigtable administrative operations (calls to the Admin API) that you can perform within a given time.

In general, you are not able to request an increase in admin operation quotas, except where indicated. Exceptions are sometimes granted when strong justification is provided. However, the number of calls that your application makes to the admin API shouldn't increase when usage increases. If this occurs, it is often a sign that your application code is making unnecessary calls to the admin API, and you should change your application instead of requesting an admin operation quota increase.

Daily quotas reset at midnight Pacific Time.

Name | Description | Default quota  
---|---|---  
**Instances and clusters**  
Instance and cluster read requests |  Reading the configuration for an instance or cluster (for example, the instance name or the number of nodes in a cluster), or reading a list of instances  |  **Per day per project:** 864,000 ops (average of 10 ops/second) **Per minute per user:** 1,000 ops  
Instance and cluster write requests |  Changing the configuration for an instance or cluster (for example, the instance name or the number of nodes in a cluster), or creating a new instance  |  **Per day per project:** 500 ops **Per minute per user:** 100 ops  
**Application profiles**  
App profile read requests | Reading the configuration for an app profile |  **Per minute per project:** 5,000 ops **Per minute per user:** 1,000 ops  
App profile write requests | Changing the configuration for an app profile |  **Per minute per project:** 500 ops **Per minute per user:** 100 ops  
**Tables**  
Table admin read requests |  Reading the configuration for a table (for example, details about its column families), or reading a list of tables  |  **Per day per project:** 864,000 ops (average of 10 ops/second) **Per minute per user:** 1,000 ops  
Table admin write requests |  Changing the configuration for a table (for example, the garbage collection settings for a column family)  |  **Per day per project:** 5,000 ops **Per minute per user:** 100 ops  
`DropRowRange` method |  Delete a range of rows from a table in a single operation.  |  **Per day per project:** 5,000 ops **Per minute per user:** 100 ops  
**Backups**  
Backup operations |  Creating, updating, and deleting a backup.  |  **Per day per project:** 1,000 ops **Per minute per user:** 10 ops1  
Backup retrieval requests |  Getting and listing backups.  |  **Per day per project:** 864,000 ops  
`RestoreTable` method |  Restoring a backup to a new table.  |  **Per day per project:** 5,000 ops **Per minute per user:** 100 ops  
**Identity and Access Management**  
Fine-grained ACL get requests |  Reading information about the IAM policy for a Bigtable instance, or testing the IAM permissions for an instance.  |  **Per day per project:** 864,000 ops (average of 10 ops/second) **Per minute per user:** 1,000 ops  
Fine-grained ACL set requests |  Changing the IAM policy for a Bigtable instance.  |  **Per day per project:** 864,000 ops (average of 10 ops/second) **Per minute per user:** 1,000 ops  
  
  1. Eligible for quota limit increase. 

  
  
### Node quotas

A Google Cloud project contains Bigtable [instances](https://docs.cloud.google.com/bigtable/docs/instances-clusters-nodes#instances), which are containers for [clusters](https://docs.cloud.google.com/bigtable/docs/instances-clusters-nodes#clusters). A cluster represents the actual Bigtable service running in a single zone. Clusters contain [nodes](https://docs.cloud.google.com/bigtable/docs/instances-clusters-nodes#nodes), which are compute resources that enable Bigtable to manage your data.

The default number of nodes that you can provision per zone in each project depends on the region. You are able to provision up to the default number of HDD nodes and up to the default number of SSD nodes per zone in a project.

The default node quotas are as follows:

Region | SSD | HDD  
---|---|---  
asia-east1 | 100 | 100  
europe-west1 | 200 | 200  
us-central1 | 200 | 200  
us-east1 | 50 | 50  
us-east4 | 50 | 50  
us-west1 | 100 | 100  
All other Bigtable locations | 30 | 30  
  
If you enable autoscaling for a cluster, the configured maximum number of nodes counts toward this limit, even if the cluster is not scaled to that number of nodes. If you need to provision more nodes than the default limits, you can request an increase.

### Quotas and node availability

Node quota is the maximum number of nodes that you can provision per zone in each project. Quotas don't guarantee that you are always able to add nodes to a cluster. If a zone is out of nodes, you might not be able to add nodes to a cluster in that zone, even if you have remaining quota in your project.

For example, if you attempt to add 10 SSD nodes to a cluster that already has 20 nodes, but the zone is out of nodes, you are not able to add those 10 nodes, even if the node quota for SSD nodes in that region is 30.

In these situations, we attempt to increase a zone's node resources and then grant your requests after those resources are available, with no guarantee of timing and completion.

Nodes that you have provisioned are always guaranteed to be available.

### Data Boost quotas

The following server processing unit (SPU) quotas apply per project per region.

Region | SPUs  
---|---  
asia-east1 | 100,000  
europe-west1 | 200,000  
us-central1 | 200,000  
us-east1 | 100,000  
us-east4 | 100,000  
us-west1 | 100,000  
All other Bigtable locations | 30,000  
  
For more information about Data Boost, see the [Data Boost overview](https://docs.cloud.google.com/bigtable/docs/data-boost-overview).

### View quota information

To find the number of SSD and HDD nodes that your Google Cloud project already has in each zone, use the [Google Cloud console](https://console.cloud.google.com/). In the left navigation pane, point to **IAM & admin**, click **Quotas** , and then use the **Service** drop-down to select the Bigtable Admin API service.

The page displays rows showing quotas for each combination of service, node type, and location. Look for the rows that are subtitled **SSD nodes per zone** or **HDD nodes per zone**. The **Limit** column shows the maximum number of nodes allowed for the given node type and location, and the **Current usage** column shows the number of nodes that exist. The difference between those two numbers is the number of nodes you can add without requesting more.

### Request a node quota increase

To ensure that there is enough time to process your request, always plan ahead and request additional resources a few days before you might need them. Requests for node quota increases are not guaranteed to be granted. For more information, see [Working with quotas](https://docs.cloud.google.com/docs/quota).

You must have at least [editor-level permissions](https://docs.cloud.google.com/iam/docs/roles-overview#basic) on the project that contains the instance you are requesting a node quota increase for.

There is no charge for requesting an increase in node quota. Your costs increase only if you use more resources.

  1. Go to the **Quotas** page. 

[Go to the Quotas page](https://console.cloud.google.com/iam-admin/quotas)

  2. On the **Quotas** page, select the quotas you want to change.
  3. Click the **Edit Quotas** button on the top of the page.
  4. In the right pane, type your name, email, and phone number, then click **Next**.
  5. Enter the requested new quota limit, then click **Next**.
  6. Submit your request.



## Limits

This section describes limits that apply to your usage of Bigtable. Limits are built into the service and cannot be changed.

### App profiles per instance limits

The maximum number of [application profiles](https://docs.cloud.google.com/bigtable/docs/app-profiles) each instance can have is 2,000.

### Authorized views limits

  * Authorized views per Bigtable instance: up to 10,000
  * Column qualifier prefixes per authorized view: 10



### Backups limits

  * Maximum number of standard backups that can be created: 150 per table per cluster
  * Maximum number of hot backups that can be created: 10 per table per cluster
  * Minimum retention period of a backup: 6 hours after initial creation time
  * Maximum retention period of a backup: 90 days in the Enterprise edition or 365 days in the Enterprise Plus edition, counted after the initial creation date



### Change streams limits

The maximum retention period of a change stream for a table is seven days.

### Continuous materialized views limits

  * Continuous materialized views per instance: 50
  * Continuous materialized views per table: 5



### Data Boost limits

A cluster can't receive more than 1,000 Data Boost read requests per second.

### Data size within tables limits

**Recommended limits**

[Design your schema](https://docs.cloud.google.com/bigtable/docs/schema-design) to keep the size of your data under these recommended limits.

  * **Column families per table:** 100
  * **A single column qualifier:** 16 KB
  * **A single value in a table cell:** 10 MB
  * **All values in a single row:** 100 MB



**Hard limits**

In addition, you _must_ ensure that your data fits within these hard limits:

  * **A single row key:** 4 KB
  * **A single value in a table cell:** 100 MB
  * **All values in a single row:** 256 MB
  * **A single mutation:** 200 MB



These size limits are measured in binary kilobytes (KB), where 1 KB is 210 bytes, and binary megabytes (MB), where 1 MB is 220 bytes. These units of measurement are also known as [kibibytes (KiB)](https://en.wikipedia.org/wiki/Kibibyte) and [mebibytes (MiB)](https://en.wikipedia.org/wiki/Mebibyte).

### ID length limits

The following are the minimum and maximum ID lengths (number of characters) supported by Bigtable.

  * App profile: 1-50
  * authorized view: 1-50
  * Backup: 1-50
  * Cluster: 6-40
  * Column family: 1-64
  * Instance: 6-33
  * Table: 1-50
  * View: 1-128



### In-memory tier limits

**Preview — In-memory tier**

This feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

The following limits apply to the in-memory tier:

  * **Scaling** : the in-memory tier supports both horizontal scaling (through autoscaling) and vertical scaling. Each Enterprise Plus node includes a base capacity of 40,000 in-memory QPS. With in-memory tier enabled, the node can vertically scale to support higher volumes in 40,000 QPS increments, up to a maximum of 120,000 in-memory QPS per node. For more information, see [Understand performance](https://docs.cloud.google.com/bigtable/docs/performance).
  * **Row size** : the in-memory tier doesn't serve rows larger than 1 MiB per row key.



### Logical views per instance limits

Bigtable supports a maximum of 1,000 logical views in each instance.

### Operation limits

When you send multiple mutations to Bigtable as a single batch, the following limits apply:

  * A batch of conditional mutations, which call `CheckAndMutate`, can include up to 100,000 true mutations _and_ up to 100,000 false mutations in the batch.

  * In batches of all other types of mutations, you can include no more than 100,000 mutations in the batch.




### Regions per instance limits

A Bigtable instance can have clusters in up to 8 regions where Bigtable is available. You can create one cluster in each zone in a region. For a list of available zones, see [Bigtable locations](https://docs.cloud.google.com/bigtable/docs/locations).

### Row filters limits

A row filter cannot exceed 20 KB. If you receive an error message, you should redesign or shorten your filter.

### Saved queries limits

**Preview — Saved queries**

This feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

Value | Limit  
---|---  
Maximum number of saved queries per project (including saved queries for other Google Cloud products) | 10,000  
Maximum size for each query | 1 MiB  
  
### Schema bundles limits

**Preview — Schema bundles**

This feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

The following limits apply to schema bundles:

  * **Schema bundles per table** : You can create a maximum of 10 schema bundles per table.
  * **Schema bundle size** : The total size of the serialized protocol buffer descriptors within a schema bundle can't exceed 4 MB.



### Storage per node limits

If a cluster does not have enough nodes, based on its current workload and the amount of data it stores, Bigtable will not have enough CPU resources to manage all of the tablets that are associated with the cluster. Bigtable will also not be able to perform essential maintenance tasks in the background. As a result, the cluster may not be able to handle incoming requests, and latency will go up. See [Trade-offs between storage usage and performance](https://docs.cloud.google.com/bigtable/docs/performance#storage-performance) for more details.

To prevent these issues, [monitor storage utilization for your clusters](https://docs.cloud.google.com/bigtable/docs/monitoring-instance#disk) to make sure they have enough nodes to support the amount of data in the cluster, based on the following limits:

Storage configuration | Enterprise Edition | Enterprise Plus edition  
---|---|---  
**SSD clusters without[tiered storage](https://docs.cloud.google.com/bigtable/docs/tiered-storage) ([Preview](https://docs.cloud.google.com/products#product-launch-stages))** | 5 TB per node | 5 TB per node  
**SSD clusters with tiered storage** | 32 TB per node, of which a maximum of 5 TB is SSD storage. | 64 TB per node, of which a maximum of 5 TB is SSD storage.  
**HDD clusters** | 16 TB per node | 16 TB per node  
**In-memory tier ([Preview](https://docs.cloud.google.com/products#product-launch-stages))** | Not supported | 8 GB per node  
  
TB values are measured in binary terabytes (TB), where 1 TB is 240 bytes. This unit of measurement is also known as a [tebibyte (TiB)](https://en.wikipedia.org/wiki/Tebibyte). 

**Important** : If any cluster in an instance exceeds the hard limit on the amount of storage per node, writes to all clusters in that instance will fail until you [add nodes to each cluster that is over the limit](https://docs.cloud.google.com/bigtable/docs/modifying-instance#nodes). Also, if you try to remove nodes from a cluster, and the change would cause the cluster to exceed the hard limit on storage, Bigtable will deny the request.

As a best practice, add enough nodes to your cluster so you are only using 70% of these limits, which helps accommodate any sudden spikes in storage usage. For example, if you are storing 50 TB of data in a cluster that uses SSD storage, you should provision at least 15 nodes, which will handle up to 75 TB of data. If you are not adding significant amounts of data to the cluster, you can exceed this recommendation and store up to 100% of the limit. 

### Tables per instance limits

Bigtable supports a maximum of 1,000 tables in each instance. Materialized views count toward the number of tables.

## Usage policies

The use of this service must adhere to the [Terms of Service](https://docs.cloud.google.com/cloud/terms) as well as Google's [Privacy Policy](https://policies.google.com/privacy).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
