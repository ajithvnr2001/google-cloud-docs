---
url: https://docs.cloud.google.com/storage/docs/storage-intelligence/overview/
title: About Storage Intelligence \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T10:30:36.790418+00:00
---

# About Storage Intelligence  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/storage/docs/storage-intelligence/overview/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Storage ](https://docs.cloud.google.com/docs/storage)
  * [ Cloud Storage ](https://docs.cloud.google.com/storage/docs)
  * [ Guides ](https://docs.cloud.google.com/storage/docs/discover-object-storage-console)



Send feedback 

#  About Storage Intelligence Stay organized with collections  Save and categorize content based on your preferences. 

**Note:** Google Cloud offers a 30-day introductory trial for Storage Intelligence. To evaluate recommendations and explore your storage usage before subscribing, see [30-day introductory trial for Storage Intelligence](https://docs.cloud.google.com/storage/docs/storage-intelligence/30-day-introductory-trial/overview).[ ![What is Google Cloud Storage Intelligence?](https://docs.cloud.google.com/static/storage/docs/images/storage-intelligence-demo.png)](https://www.youtube.com/watch?v=r5Z_z1bgcw0) [What is Google Cloud Storage Intelligence?](https://www.youtube.com/watch?v=r5Z_z1bgcw0)

Storage Intelligence provides centralized visibility and control over your Cloud Storage data at scale. Instead of managing individual buckets with custom scripts, you can govern storage across your entire resource hierarchy to identify cost savings, analyze usage trends, and automate bulk operations.

To get started, see [Configure and manage Storage Intelligence](https://docs.cloud.google.com/storage/docs/storage-intelligence/configure-and-manage-storage-intelligence).

## Storage Intelligence use cases

Storage Intelligence helps you accomplish two primary operational tasks:

  * Analyze and optimize your storage
  * Manage and automate storage operations at scale



### Analyze and optimize your storage

To evaluate your data distribution, track usage trends, and discover cost savings, you can do the following:

  * **Track storage trends and recommendations** : Use [Storage Intelligence advisor](https://docs.cloud.google.com/storage/docs/storage-intelligence/advisor-overview) to monitor capacity growth, detect usage anomalies, and identify cost-saving opportunities, such as idle buckets and unoptimized storage classes, across your organization, folders, or projects.
  * **Query metadata and activity using SQL** : Use [Storage Insights datasets](https://docs.cloud.google.com/storage/docs/insights/datasets) to generate queryable metadata and activity indexes provided as [BigQuery linked datasets](https://docs.cloud.google.com/bigquery/docs/analytics-hub-introduction#linked_datasets). You can analyze data distribution, audit access patterns, and evaluate storage costs across your entire resource hierarchy.
  * **Ask questions using AI** : Use [data storage insights with Gemini Cloud Assist](https://docs.cloud.google.com/storage/docs/analyze-data-gemini-cloud-assist) to ask natural-language questions about your storage environment. When you configure Storage Insights datasets, you can prompt Gemini to identify your largest buckets without Autoclass enabled or list objects in the Standard storage storage class smaller than 50 MB.
  * **Audit bucket inventory** : Use [inventory reports](https://docs.cloud.google.com/storage/docs/insights/inventory-reports) to generate per-bucket reports that catalog objects and metadata. A Storage Intelligence subscription includes inventory reports and covers all object scan fees.



### Manage and automate storage operations at scale

To manage buckets across regions and run operations at scale without custom scripts, you can do the following:

  * **Relocate buckets across regions** : Use [bucket relocation](https://docs.cloud.google.com/storage/docs/bucket-relocation/overview) to move buckets between geographic locations with minimal downtime, preserving bucket names, object metadata, and storage classes.

  * **Execute operations across billions of objects** : Use [Storage batch operations](https://docs.cloud.google.com/storage/docs/batch-operations/overview) to automate bulk tasks, such as updating metadata, transforming storage classes, or deleting expired objects—across large collections of objects without writing custom scripts.




## Configuration options

When you configure Storage Intelligence, you make three decisions:

  1. Choose a resource level in your Google Cloud resource hierarchy.
  2. Apply bucket filters to include or exclude specific buckets by location or name.
  3. Select an edition configuration to control activation for each resource.



### Choose a resource

You can configure Storage Intelligence at different levels of your [Google Cloud resource hierarchy](https://docs.cloud.google.com/resource-manager/docs/cloud-platform-resource-hierarchy#resource-hierarchy-detail). The configuration automatically applies to all buckets and objects within that resource:

  * **[Organization](https://docs.cloud.google.com/resource-manager/docs/cloud-platform-resource-hierarchy#organizations)** : Applies to the entire organization. All current and new folders and projects inherit this configuration unless overridden.
  * **[Folder](https://docs.cloud.google.com/resource-manager/docs/cloud-platform-resource-hierarchy#folders)** : Applies to all current and new projects in the folder unless overridden.
  * **[Project](https://docs.cloud.google.com/resource-manager/docs/cloud-platform-resource-hierarchy#projects)** : Applies to all current and new buckets in the project. Configuring at the project level is ideal for teams that manage storage independently.



### Apply bucket filters

Bucket filters let you control which buckets Storage Intelligence manages, helping you focus analysis on relevant data and reduce processing costs:

  * **Filter by location** : Include or exclude specific Google Cloud locations to focus on high-activity regions or omit regulated data.
  * **Filter by name** : Include or exclude buckets that match a regular expression pattern, such as environment prefixes or department identifiers.



For instructions on applying filters, see [Configure Storage Intelligence](https://docs.cloud.google.com/storage/docs/storage-intelligence/configure-and-manage-storage-intelligence#configure-storage-intelligence).

### Select an edition configuration

The edition configuration controls whether Storage Intelligence capabilities are active for a resource:

  * **`INHERIT`** : Inherits the edition configuration of the parent resource.
  * **`STANDARD`** : Enables Storage Intelligence capabilities. `STANDARD` is the default edition when you configure Storage Intelligence for a resource.
  * **`DISABLED`** : Disables Storage Intelligence for the specified resource. Child resources inherit the disabled state unless explicitly configured with `STANDARD` or `INHERIT`.
  * **`TRIAL`** : Activates the [30-day introductory trial for Storage Intelligence](https://docs.cloud.google.com/storage/docs/storage-intelligence/30-day-introductory-trial/overview).



Figure 1 shows an example of edition configurations across different levels of the resource hierarchy:

![Figure 1. Edition configurations across different levels of resource hierarchy.](https://docs.cloud.google.com/static/storage/docs/images/management-hub-hierarchy.png)**Figure 1.** Edition configurations across different levels of resource hierarchy.

Table 1 describes how edition configurations apply across your Google Cloud resources:

Resource | Edition configuration | Storage Intelligence status | Description  
---|---|---|---  
Organization A | `STANDARD` | Enabled | Enables Storage Intelligence for the entire organization. By default, all folders and projects in Organization A inherit this configuration.  
Folder C | `DISABLED` | Disabled | Disables Storage Intelligence for Folder C and its child projects, overriding the inherited `STANDARD` configuration from Organization A.  
Project E | `DISABLED` | Disabled | Disables Storage Intelligence for Project E, overriding the inherited configuration from its parent folder or organization.  
  
## Pricing

Pricing for Storage Intelligence depends on the capabilities you use and the volume of data you manage. For details, see [Storage Intelligence pricing](https://docs.cloud.google.com/storage/pricing#storage-intelligence).

## What's next

  * [Configure and manage Storage Intelligence](https://docs.cloud.google.com/storage/docs/storage-intelligence/configure-and-manage-storage-intelligence).
  * [Review storage trends and recommendations with Storage Intelligence advisor](https://docs.cloud.google.com/storage/docs/storage-intelligence/advisor-overview).
  * [Analyze metadata and activity with Storage Insights datasets](https://docs.cloud.google.com/storage/docs/insights/datasets).
  * [Generate inventory reports for your buckets](https://docs.cloud.google.com/storage/docs/insights/inventory-reports).
  * [Relocate a bucket to another region](https://docs.cloud.google.com/storage/docs/bucket-relocation/overview).
  * [Run batch operations on objects at scale](https://docs.cloud.google.com/storage/docs/batch-operations/overview).
  * [Activate the 30-day introductory trial for Storage Intelligence](https://docs.cloud.google.com/storage/docs/storage-intelligence/30-day-introductory-trial/overview).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-21 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-21 UTC."],[],[]] 
