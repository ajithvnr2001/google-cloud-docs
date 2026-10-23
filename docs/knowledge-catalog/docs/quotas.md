---
url: https://docs.cloud.google.com/knowledge-catalog/docs/quotas/
title: Quotas and limits \u00a0|\u00a0 Knowledge Catalog \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:21:26.352197+00:00
---

# Quotas and limits  |  Knowledge Catalog  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/knowledge-catalog/docs/quotas/

As of April 10, 2026, Dataplex Universal Catalog is now called Knowledge Catalog. The API, client library, CLI, and IAM names remain unchanged. For more information, see [Introducing the Google Cloud Knowledge Catalog](https://docs.cloud.google.com/blog/products/data-analytics/introducing-the-google-cloud-knowledge-catalog). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Knowledge Catalog ](https://docs.cloud.google.com/knowledge-catalog/docs)
  * [ Resources ](https://docs.cloud.google.com/knowledge-catalog/docs/resources)



Send feedback 

#  Quotas and limits Stay organized with collections  Save and categorize content based on your preferences. 

This document lists the _quotas_ that apply to Knowledge Catalog (formerly Dataplex Universal Catalog).

Google Cloud uses quotas to help ensure fairness and reduce spikes in resource use and availability. A quota restricts how much of a Google Cloud resource your Google Cloud project can use. Quotas apply to a range of resource types, including hardware, software, and network components. For example, quotas can restrict the number of API calls to a service, the number of load balancers used concurrently by your project, or the number of projects that you can create. Quotas protect the community of Google Cloud users by preventing the overloading of services. Quotas also help you to manage your own Google Cloud resources.

The Cloud Quotas system does the following:

  * Monitors your consumption of Google Cloud products and services
  * Restricts your consumption of those resources
  * Provides a way to [request changes to the quota value](https://docs.cloud.google.com/docs/quotas/help/request_increase) and [automate quota adjustments](https://docs.cloud.google.com/docs/quotas/quota-adjuster)



In most cases, when you attempt to consume more of a resource than its quota allows, the system blocks access to the resource, and the task that you're trying to perform fails.

Quotas generally apply at the Google Cloud project level. Your use of a resource in one project doesn't affect your available quota in another project. Within a Google Cloud project, quotas are shared across all applications and IP addresses. 

For more information, see the [Cloud Quotas overview](https://docs.cloud.google.com/docs/quotas/overview). 

There are also _system limits_ on Knowledge Catalog resources. System limits can't be changed. 

Knowledge Catalog enforces quotas on the number of API requests during a specific period of time and the number of resources that can be created in a project. Quotas protect you from unforeseen spikes in usage and overloaded services. Learn more about why [quotas are enforced](https://docs.cloud.google.com/docs/quotas/overview).

Your quota needs might increase the more that you use Knowledge Catalog. If a quota is too low to meet your needs, or you expect an upcoming increase in usage, you can proactively request a quota increase.

## Understand API request types

API requests across various Knowledge Catalog features, such as resource management, metadata, tasks, and data scans, are categorized into generic buckets to manage service usage and protection.

### Read requests

Read requests are operations designed to retrieve information about existing resources, metadata, or execution history without modifying any configuration or state. These operations are non-mutating and don't trigger new processing jobs.

Read request operations include `Get`, `List`, and `Describe`. For example, viewing the definition of a data scan or the status of a scan job is a read request.

### Write requests

Write requests include all operations that create, update, or delete resource definitions, as well as those that modify security policies. These are operations that change the state of the environment.

Write request operations include `Create`, `Update`, `Delete`, `Cancel`, and `SetIamPolicy`. For example, configuring a data quality scan or updating an existing data profile scan is a write request.

### Run requests

Run requests specifically refer to triggering the active execution of a pre-configured resource. Unlike a write request (which might create a recurring schedule), a run request is often used for on-demand execution of the configured logic.

For example, manually starting a data scan execution is a run request.

## Quotas for Dataplex API requests

The Dataplex API enforces quotas for Knowledge Catalog resource management and search requests at different levels, regardless of their origination. This includes the requests originating from API calls directly, client libraries, Google Cloud CLI, and Google Cloud console.

The following quotas apply to Knowledge Catalog requests:

Quota | Default  
---|---  
Read requests for entries and aspects per project per region per minute | 6,000  
Write requests for entries and aspects per project per region per minute | 1,500  
Read requests for aspect types, entry types, and entry groups per project per user per region per minute | 100  
Read requests for aspect types, entry types, and entry groups per project per region per minute | 200  
Write requests for aspect types, entry types, and entry groups per project per user per region per minute | 10  
Write requests for aspect types, entry types, and entry groups per project per region per minute | 20  
Search requests per project per user per minute | 900  
Search requests per project per minute | 1,200  
Search requests per organization per minute | 2,400  
Search requests per organization per day | 345,600  
Read requests for metadata jobs per project per region per minute | 400  
Read requests for metadata jobs per project per user per region per minute | 200  
Write requests for metadata jobs per project per region per minute | 20  
Write requests for metadata jobs per project per user per region per minute | 10  
Read requests for data scans per project per region per minute | 1,200  
Read requests for data scans per project per user per region per minute | 600  
Write requests for data scans per project per region per minute | 200  
Write requests for data scans per project per user per region per minute | 100  
Run requests for data scans per project per region per minute | 60  
Run requests for data scans per project per user per region per minute | 30  
Total daily executions of data profile scans for unstructured data on BigQuery object tables per project | 140  
Amount of metadata that is exported by metadata export jobs, per organization per day | 10 GB  
Amount of metadata that is scanned for export by metadata export jobs, per organization per day This quota evaluates the total volume of metadata that exists in either the organization, the projects, or the entry groups that are in scope for the metadata export job. | 100 GB  
  
For every Knowledge Catalog request that is listed in the following table, quota is enforced at both the per-project and per-project-per-user levels.

Quota | Examples  
---|---  
Read requests for resource management | Get a lake, list zones  
Write requests for resource management | Create a lake, delete an asset  
Get requests for metadata | Get an entity, get a partition  
List requests for metadata | List entities, list partitions  
Write requests for metadata | Update an entity, delete a partition  
Read requests for task and job resources | Get a task, list jobs  
Write requests for task and job resources | Create a task, cancel a job  
Set IAM policy requests | Set an IAM policy  
  
## Quotas for Data Lineage API requests

The Data Lineage API enforces quotas for the following:

  * Read requests that only return the data
  * Write requests that create or change the data
  * Create [Open Lineage](https://docs.cloud.google.com/knowledge-catalog/docs/open-lineage)



The following quotas apply to data lineage requests:

Quota | Default value  
---|---  
Read requests (`SearchLinks`, `BatchSearchLinkProcesses`, `Get*`, `List*`) per project per region (for example, `us-central1`) per minute | 2,000  
Read requests (`SearchLinks`, `BatchSearchLinkProcesses`, `Get*`, `List*`) per project per multi-region (`us`, `eu`, `asia`) per minute | 1,000  
Write requests (`Create*`, `Update*`, `Delete*`) per project per region (for example, `us-central1`) per minute | 12,000  
Write requests (`Create*`, `Update*`, `Delete*`) per project per multi-region (`us`, `eu`, `asia`) per minute | 6,000  
OpenLineage requests (`ProcessOpenLineageRunEvent`) per project per region (for example, `us-central1`) per minute | 2,000  
OpenLineage requests (`ProcessOpenLineageRunEvent`) per project per multi-region (`us`, `eu`, `asia`) per minute | 1,000  
  
## Quotas for Dataplex API requests for data products

The Dataplex API enforces rate limits on metadata operations and lifecycle requests for data products and data assets. These limits apply regardless of whether the requests originate from the Google Cloud console, the Google Cloud CLI, client libraries, or direct API calls.

The following quotas apply to data products and data assets requests:

Quota | Default value  
---|---  
Read requests for data products per project per region per minute | 500  
Read requests for data products per project per user per region per minute | 250  
Create and delete requests for data products per project per region per minute | 250  
Create and delete requests for data products per project per user per region per minute | 125  
Update requests for data products per project per minute | 10  
Update requests for data products per project per user per minute | 5  
Read requests for data assets per project per region per minute | 500  
Read requests for data assets per project per user per region per minute | 250  
Write requests for data assets per project per region per minute | 30  
Write requests for data assets per project per user per region per minute | 15  
  
## Quotas and limits for Knowledge Studio enrichment tasks

**Preview**

This product or feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA products and features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

The Dataplex API enforces rate and resource quotas on Knowledge Studio enrichment tasks (`AgentTask` resources) and task runs (`AgentRun` resources).

The following quotas apply to Knowledge Studio enrichment tasks:

Quota | Default value  
---|---  
Read requests for enrichment task resources (such as `Get` and `List` for tasks and runs) per project per region per minute | 1,200  
Write requests for enrichment task resources (such as `Create`, `Update`, and `Delete`) per project per region per minute | 60  
Run requests for enrichment task resources per project per region per minute | 20  
Maximum number of enrichment tasks (`AgentTask` resources) per project per region | 100  
  
## Quotas for resources

Resource quota is enforced at per-project level for the following resource types: lake, zone, asset, on-demand task, recurring task. You can check your current usage of Knowledge Catalog quota on the **Quotas** page in the Google Cloud console.

## Request a quota increase

  1. In the Google Cloud console, go to the **Quotas** page.

[Go to Quotas](https://console.cloud.google.com/iam-admin/quotas)

  2. Select the quota you want to modify.

  3. Click more_vert**More actions > Edit quota**.

  4. Enter the new quota value and a request description.

  5. Click **Next**.

  6. Enter the contact details.

  7. Click **Submit request**.




To adjust most quotas, use the Google Cloud console. For more information, see [Request a quota adjustment](https://docs.cloud.google.com/docs/quotas/help/request_increase). 

## Quota dependencies

Your Knowledge Catalog usage might involve other Google Cloud products. For example, data discovery requires invoking Cloud Storage or BigQuery APIs to interact with the underlying resources. These products have project-level quotas, which include quotas that apply to Knowledge Catalog use.

Quota pages of other products that you might use with Knowledge Catalog:

  * [BigQuery quotas](https://docs.cloud.google.com/bigquery/quotas)
  * [Cloud Storage quotas](https://docs.cloud.google.com/storage/quotas)
  * [Dataproc Metastore quotas](https://docs.cloud.google.com/dataproc-metastore/docs/quotas)



This list is not exhaustive.

## Limits

The following limits apply to Knowledge Catalog:

Limit | Value  
---|---  
Size of a request for entry and aspects (including schema aspect) | 2 MB  
Length of an entry ID | 4,000 characters  
Length of a fully qualified name in an entry | 4,000 characters  
Length of the entry source display name in an entry | 500 characters  
Length of the entry source description in an entry | 2,000 characters  
Length of the entry source resource in an entry | 4,000 characters  
Length of the entry source system in an entry | 64 characters  
Length of the entry source platform in an entry | 64 characters  
Length of the entry source labels in an entry | 128 characters for each key and value  
Size of the JSON content in an aspect (except schema and data profile aspects) | 120 KB  
Size of the JSON content in a data profile aspect | 1 MB  
Total size of an entry | 5 MB  
Maximum number of aspects in an entry  | 10,000  
Length of the display name of entry type, aspect type, and entry group | 256  
Length of the description of entry type, aspect type, and entry group | 1,024  
Length of the field name in an aspect type template | 63  
Maximum number of required aspect types in an entry type | 20  
Maximum number of enum values in an aspect type template | 1,024  
Maximum number of items in Knowledge Catalog search results | 500 (keyword-only search mode in the Google Cloud console or `semanticSearch=false` when using API)  
  
100 (all other search cases)  
Maximum number of data scans per project per region | 1,000  
Maximum number of data products per project per region | 1,000  
Maximum number of data assets per data product | 50  
Maximum number of policy tags per taxonomy | 100  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
