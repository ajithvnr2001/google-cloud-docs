---
url: https://docs.cloud.google.com/storage/docs/insights/datasets/
title: Storage Insights datasets \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T13:08:43.003228+00:00
---

# Storage Insights datasets  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/storage/docs/insights/datasets/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Storage ](https://docs.cloud.google.com/docs/storage)
  * [ Cloud Storage ](https://docs.cloud.google.com/storage/docs)
  * [ Guides ](https://docs.cloud.google.com/storage/docs/discover-object-storage-console)



Send feedback 

#  Storage Insights datasets Stay organized with collections  Save and categorize content based on your preferences. 

Storage Insights datasets is available only if you've configured [Storage Intelligence](https://docs.cloud.google.com/storage/docs/storage-intelligence/overview).

Storage Insights datasets help you manage your Cloud Storage resources by generating a queryable index of metadata and activity across organizations, folders, projects, or specific buckets. After you link the dataset to BigQuery, you can analyze, query, and visualize your bucket and object data.

## Dataset contents and schemas

A Storage Insights dataset provides a rolling snapshot of metadata, activity data, errors, and events for all projects, buckets, and objects within the defined scope. The dataset collects and indexes information to provide a view of your data. This view lets you monitor your Cloud Storage resources and manage your storage estate.

The dataset is available as a BigQuery linked dataset, with a set of tables that have the following schemas:

  * **Metadata** : a snapshot of metadata for projects, buckets, and objects. For details about the metadata schema, see [Dataset schema of metadata](https://docs.cloud.google.com/storage/docs/insights/dataset-tables-and-schemas#metadata-schema).

  * **Activity data** : mutation and error records for objects and aggregated activity insights for your buckets and projects. For details about the activity data schema, see [Dataset schema of activity data](https://docs.cloud.google.com/storage/docs/insights/dataset-tables-and-schemas#activity-data-schema).

  * **Errors and events** : information about snapshot processing events and errors. For details about the errors and events schema, see [Dataset schema of events and errors](https://docs.cloud.google.com/storage/docs/insights/dataset-tables-and-schemas#schema-error-events).




## Use cases for Storage Insights datasets

Storage Insights datasets provide views for gaining organization-wide and granular insights about your data. The following sections describe use cases for datasets.

### Understand your storage estate

You can gain insights into your data by viewing project, bucket, and object metadata. The metadata views help you with the following tasks:

  * Spot anomalies, such as data in an unexpected region.
  * Identify optimization opportunities, such as locating temporary or duplicate files.
  * Query for specific insights, such as objects created in the last 24 hours or the total count of `PDF` files.
  * Drill down to objects you want to act on by extracting a prefix list of a set of objects based on query results.



### Perform batch operations using dataset filters

By integrating Storage Insights datasets with [ storage batch operations](https://docs.cloud.google.com/storage/docs/batch-operations/overview), you can perform large-scale actions on objects identified in your datasets. This integration lets you select specific subsets of data across multiple buckets project-wide and apply transformations based on fields in your dataset. This approach eliminates the need for manual manifest files.

#### Direct object selection

Use Common Expression Language (CEL) filter flags (`--bucket-filters` and `--object-filters`) directly in Google Cloud CLI to select and process objects at scale. This direct selection lets you evaluate dataset fields and run batch actions project-wide. This method eliminates the need to create manual manifest CSV files. You don't need to query your dataset in BigQuery, export search results, and upload manifests to your buckets. This project-wide scope lets you run a single batch job across up to 1,000 buckets.

For example, you can specify filter criteria directly in Google Cloud CLI:

`--object-filters="size >= 5000 && name.endsWith('.pdf')"`

For information about the available fields and operators you can use in these filters, see the [CEL filters reference](https://docs.cloud.google.com/storage/docs/batch-operations/cel-filters-reference).

### Analyze activity patterns

Using the bucket activity view, project activity view, and object events view, you can do the following:

  * Analyze operational patterns and identify inactive buckets.

  * Monitor operations on your objects to see how your storage estate is changing over time.

  * Map your most active projects, buckets, and prefixes.




### Understand regional bucket activity

The bucket regional activity view displays fields such as request and response bytes, showing the regions that frequently interact with your bucket. Analyze regional bucket activity to determine if [bucket relocation](https://docs.cloud.google.com/storage/docs/bucket-relocation/overview) is necessary:

  * View the total egress and ingress for a bucket in a region to identify buckets that may be better suited for a regional, rather than multi-region class.

  * Assess total data traffic within and across all regions.




### Assess security status

You can use bucket and object metadata to identify publicly exposed objects, active encryption types, and expiration timelines for data retention. The following sections describe how Storage Insights datasets help you assess potential security vulnerabilities.

#### Identify publicly accessible objects

You can use Storage Insights datasets to identify objects that are publicly accessible. The public access status of your objects helps you govern your storage data and mitigate data exfiltration risks by letting you identify the objects exposed to the public internet.

The object metadata schema provides the public access status, a computed metric that helps simplify security analysis. To determine an object's public access status, Storage Insights datasets validate all the following configurations:

  * The bucket and object metadata, that include the following configurations: 
    * [Public access prevention](https://docs.cloud.google.com/storage/docs/public-access-prevention)
    * [Uniform bucket-level access](https://docs.cloud.google.com/storage/docs/uniform-bucket-level-access)
    * [Access control lists](https://docs.cloud.google.com/storage/docs/access-control/lists)
    * [IAM policies](https://docs.cloud.google.com/iam/docs/policy-types)
  * The organization policies, that include the following configurations: 
    * Policy constraints, such as public access prevention
    * IAM deny policies
    * IAM policies with [tags](https://docs.cloud.google.com/storage/docs/tags-and-labels#tags) attached



To help you identify the specific configuration that grants public access, Storage Insights datasets include information when an object is publicly readable or writable. For publicly readable objects, this information indicates if the permission originates at the object, bucket, or managed folder level. For publicly writable objects, it provides details about whether access is granted by an object ACL, bucket ACL, or IAM policy.

You can query the public access status of objects using BigQuery and then monitor those objects using Looker dashboards to list all publicly readable or writable objects. For more information about the public access status fields, see [`securityInsights`](https://docs.cloud.google.com/storage/docs/insights/dataset-tables-and-schemas#securityInsights) in the object metadata schema.

#### Audit encryption configurations

You can use bucket and object metadata views to audit encryption configurations. These views include encryption information at both the bucket and object level, with fields such as `encryption` in bucket metadata and `encryptionType` in object metadata. You can use this information to do the following:

  * Verify that buckets have default encryption configured by checking `encryption.defaultEncryptionType` and `encryption.defaultKmsKeyName`.
  * Validate compliance with encryption enforcement policies by checking `encryptionType` to see if objects use Google-managed, customer-managed, or customer-supplied encryption keys.
  * Identify all objects encrypted with a specific Cloud Key Management Service key or customer-supplied encryption keys.



#### Monitor data retention policies

You can use bucket and object metadata views to monitor data retention policies. These views include fields such as `retentionExpirationTime` in object metadata and `softDeletePolicy` in bucket metadata. You can use these fields to do the following:

  * Track objects nearing retention expiration.
  * Identify buckets with soft delete enabled and monitor their retention duration.
  * Identify objects in a soft-deleted state by checking `softDeleteTime`.



### Speed up troubleshooting

The `object_events_view` view contains error information that can help with troubleshooting. You can use this view to inspect operations that resulted in errors, identify error reasons, and detect projects and buckets with high error rates. For example, you can troubleshoot `429` errors by identifying the affected bucket, project, and the root cause, such as resource quota or bandwidth limits.

### Analyze object data and metadata using BigQuery

You can analyze the data in your Storage Insights datasets by using BigQuery `ObjectRef` functions. For example, you can build queries to help detect sensitive information in documents or to generate image descriptions.

To analyze object content, use the [`ref`](https://docs.cloud.google.com/storage/docs/insights/dataset-tables-and-schemas#ref) column from the object metadata tables with [`ObjectRef` functions](https://docs.cloud.google.com/bigquery/docs/reference/standard-sql/objectref_functions). For details, see [Analyze object data and metadata using BigQuery](https://docs.cloud.google.com/storage/docs/insights/configure-datasets#analyze-object-data).

## Benefits of Storage Insights datasets

Storage Insights datasets provide metadata and activity information about your storage estate in a queryable format in BigQuery. The following are the benefits of using Storage Insights datasets:

  * Analyze your storage estate within a customizable scope to gain organization-wide insights, or specify folders, projects, or buckets for analysis.

  * With data available in BigQuery, use SQL and natural language queries with Gemini to analyze your data. For details, see [Analyze data with Gemini assistance](https://docs.cloud.google.com/bigquery/docs/gemini-analyze-data).

  * You can visualize your data by connecting to a Looker dashboard. You can use the [Storage Intelligence dashboard](https://lookerstudio.google.com/c/u/0/reporting/670eee3f-ad6d-45ea-a169-853ab023dc84/page/p_k94oydxikd) as a template that provides an example of the insights you can derive from datasets. You can use the template to connect to your datasets or add custom charts. For information about how to use the template, see [ Storage Intelligence dashboard connection instructions](https://lookerstudio.google.com/c/reporting/670eee3f-ad6d-45ea-a169-853ab023dc84/page/6kP1D).




## How Storage Insights datasets work

To use Storage Insights datasets, first configure a dataset within a project. Specify the organization, folders, or projects for which you want to track data. After creation, [grant the necessary permissions](https://docs.cloud.google.com/storage/docs/insights/configure-datasets#grant-permissions-to-service-account) to the service agent to generate the dataset. You can then [link the dataset](https://docs.cloud.google.com/storage/docs/insights/configure-datasets#link-dataset) to BigQuery for querying. Once configured, the service automatically collects and ingests daily snapshots of object metadata, bucket metadata, operations, and errors into a Cloud Storage-owned BigQuery instance. The data is retained according to the configured retention period and stored in an optimized way to minimize storage and analysis costs.

In the dataset configuration, you define which data is collected, where it is stored, and how it is managed.

The following table describes the key properties you must define when configuring a dataset:

Property | Description | Details and limits  
---|---|---  
**Dataset scope** | Specifies the resources (organizations, projects, or folders) that contain the buckets and objects you want to include in the dataset.|  You can specify projects or folders individually or using a CSV file. Each configuration allows only one dataset scope. You can specify up to `10,000` projects or folders.   
**Bucket filters** | Filters used to include or exclude specific buckets from the dataset.| You can filter by bucket name using regular expressions or filter by bucket location.  
**Retention period for dataset** | The number of days the dataset captures and retains metadata and activity data, including the dataset creation date. For activity data tables, you can override the data retention period by using the Retention period for activity data property. |  This retention period is a rolling window and can be up to `90` days. Datasets update with new metadata every `24` hours. The system automatically deletes data captured outside the retention window. For example, if you create a dataset on October 1, 2023, with a retention window set to `30` days. On October 30, the dataset reflects the past `30` days of data (October 1 to October 30). On October 31, the dataset reflects the data from October 2 to October 31. You can modify the retention window at any time. By default, the retention period applies to the [metadata tables](https://docs.cloud.google.com/storage/docs/insights/dataset-tables-and-schemas#metadata-schema) and also to the [activity data tables](https://docs.cloud.google.com/storage/docs/insights/dataset-tables-and-schemas#activity-data-schema) when the retention period for activity data is not specified.   
**Retention period for activity data** | The number of days the dataset captures and retains activity data. When defined, this value overrides the Retention period for dataset. |  The retention period can be up to `365 days`. The retention period for activity data is applicable for [activity data tables](https://docs.cloud.google.com/storage/docs/insights/dataset-tables-and-schemas#activity-data-schema).   
**Location** | The BigQuery location used to store the linked dataset and its associated data. |  The linked dataset must be in a [location supported by BigQuery](https://docs.cloud.google.com/bigquery/docs/locations), such as `us-central1`, although source buckets can be in any [Cloud Storage location](https://docs.cloud.google.com/storage/docs/locations). We recommend selecting the location of your BigQuery tables if you have existing BigQuery tables.   
**Service agent type** | Determines the scope of the service agent that reads and writes data for the dataset configuration. This can be either a configuration-scoped service agent or a project-scoped service agent |  **Project-scoped** service agents can access and write datasets for _all_ dataset configurations in the project. For example, if you have multiple dataset configurations within a project, you only need to grant [required permissions](https://docs.cloud.google.com/storage/docs/insights/configure-datasets#grant-permissions-to-service-account) to the project-scoped service agent once. This enables it to read and write datasets for all dataset configurations within the project. When a dataset configuration is deleted, the project-scoped service agent is not deleted.  
  
**Configuration-scoped** service agents can only access and write the dataset generated by the particular dataset configuration. Consequently, if you have multiple dataset configurations, you must grant [required permissions](https://docs.cloud.google.com/storage/docs/insights/configure-datasets#grant-permissions-to-service-account) to each configuration-scoped service agent. When a dataset configuration is deleted, the configuration-scoped service agent is deleted.   
  
After specifying the configuration properties and granting the necessary permissions to the service agent, link the dataset to BigQuery for querying.

For details about the properties you set when creating or updating a dataset configuration, see the [`DatasetConfigs` resource in the JSON API documentation](https://docs.cloud.google.com/storage/docs/insights/reference/rest/v1/projects.locations.datasetConfigs).

After configuration, the service automatically collects and ingests data into a Cloud Storage-owned BigQuery instance. The timeline for data population in the datasets is as follows:

  * The initial dataset load and activity data for newly added buckets or objects might take 24 to 48 hours to appear as a linked dataset in BigQuery.

  * Activity data is typically included within four hours of the activity (latency might occasionally be higher).

  * Metadata snapshots (for projects, buckets, and objects) are updated every 24 hours.




## Considerations

Consider the following for dataset configurations:

  * When you rename a folder in a bucket with [hierarchical namespace](https://docs.cloud.google.com/storage/docs/hns-overview) enabled, the object names in that bucket update. When the linked dataset ingests these object snapshots, they are considered new entries.

  * CRC32C checksums and MD5 hashes are not available in the [`object metadata`](https://docs.cloud.google.com/storage/docs/insights/dataset-tables-and-schemas#object-schema) table for objects encrypted with customer-managed encryption keys (CMEK).

  * Storage Insights datasets can ingest metadata from source buckets in any [Cloud Storage location](https://docs.cloud.google.com/storage/docs/locations), including locations not listed here. However, the linked dataset must reside in one of the following supported BigQuery locations:

    * `EU`
    * `US`
    * `asia-south1`
    * `asia-south2`
    * `asia-southeast1`
    * `europe-west1`
    * `us-central1`
    * `us-east1`
    * `us-east4`
  * The following limitations apply when determining the public access status for objects using Storage Insights datasets:

    * Public access status isn't available for objects within [managed folders](https://docs.cloud.google.com/storage/docs/managed-folders).

    * Storage Insights datasets don't consider the bucket's VPC Service Controls or [IP filtering](https://docs.cloud.google.com/storage/docs/ip-filtering-overview) configuration when determining the public access status of an object.




## What's next

  * [Configure Storage Insights datasets](https://docs.cloud.google.com/storage/docs/insights/configure-datasets).
  * [Learn about Storage Intelligence](https://docs.cloud.google.com/storage/docs/storage-intelligence/overview).
  * [Explore the 30-day introductory trial for Storage Intelligence](https://docs.cloud.google.com/storage/docs/storage-intelligence/30-day-introductory-trial/overview).
  * [Run SQL queries on the datasets in BigQuery](https://docs.cloud.google.com/bigquery/docs/running-queries).
  * [Learn about BigQuery analytics](https://docs.cloud.google.com/bigquery/docs/query-overview).
  * [Check the CEL filters reference for batch operations](https://docs.cloud.google.com/storage/docs/batch-operations/cel-filters-reference).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-23 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-23 UTC."],[],[]] 
