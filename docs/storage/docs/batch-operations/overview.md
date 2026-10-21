---
url: https://docs.cloud.google.com/storage/docs/batch-operations/overview/
title: Storage batch operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T01:01:03.959306+00:00
---

# Storage batch operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/storage/docs/batch-operations/overview/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Storage ](https://docs.cloud.google.com/docs/storage)
  * [ Cloud Storage ](https://docs.cloud.google.com/storage/docs)
  * [ Guides ](https://docs.cloud.google.com/storage/docs/discover-object-storage-console)



Send feedback 

#  Storage batch operations Stay organized with collections  Save and categorize content based on your preferences. 

Storage batch operations is available only if you've configured [Storage Intelligence](https://docs.cloud.google.com/storage/docs/storage-intelligence/overview).

Storage batch operations let you automate bulk tasks, such as deleting objects or updating metadata, across billions of objects in a serverless environment. This automation helps you avoid writing and maintaining custom scripts, especially in large enterprise setups with data spread across thousands of buckets.

To learn how to create storage batch operations jobs, see [Create and manage storage batch operations jobs](https://docs.cloud.google.com/storage/docs/batch-operations/create-manage-batch-operation-jobs). For changes to individual objects, you don't need to create a batch operations job. Instead, see standard task guides such as [deleting objects](https://docs.cloud.google.com/storage/docs/deleting-objects) or [viewing and editing object metadata](https://docs.cloud.google.com/storage/docs/viewing-editing-metadata).

## Overview

Use storage batch operations to manage large numbers of files across your project. To get started, create a job configuration. The configuration defines which transformations to apply to specific objects. These transformations include placing object holds, deleting objects, updating object metadata and contexts, rewriting objects, and patching access controls.

When you submit a batch operation job, you can monitor its status to verify when the job applies all specified transformations.

### Benefits

The following are the benefits of storage batch operations:

  * **Scalability** : Perform transformations on millions of objects with a single storage batch operations job.
  * **Serverless execution** : Run batch jobs in a serverless environment, which eliminates the need to manage infrastructure.
  * **Automation** : Automate complex and repetitive tasks to improve operational efficiency.
  * **Reduced development time** : Avoid writing and maintaining complex custom scripts.
  * **Storage Insights dataset integration** : Select objects directly by specifying conditions that match fields in your [Storage Insights datasets](https://docs.cloud.google.com/storage/docs/insights/datasets). This direct selection eliminates the need to manually assemble a CSV manifest or run queries to [export your dataset from BigQuery](https://docs.cloud.google.com/storage/docs/batch-operations/create-manage-batch-operation-jobs#create-manifest-using-insights-datasets).
  * **Performance** : Complete time-sensitive operations by running multiple concurrent batch jobs. For example, you can process up to one billion objects within three hours.
  * **Automatic retries** : Retry failed operations automatically.
  * **Job monitoring** : Track progress in detail to monitor the status and completion of all jobs.



### Use cases

Storage batch operations automate and simplify organization-wide storage management. The following common scenarios describe how they help protect, organize, and manage your resources:

  * **Help protect your data** : Manage your security posture at scale. For example, you can rotate encryption keys on millions of objects, apply or remove object holds to enforce immutability, and patch [Access Control Lists (ACLs)](https://docs.cloud.google.com/storage/docs/access-control/lists) in bulk to remove public read access to private data.

  * **Maintain compliance** : Help meet data-retention regulations. Use targeted object holds to enforce retention rules, set specific expiration timelines, and delete objects within a specific period to satisfy wipeout policies.

  * **Transform data at scale** : Perform bulk updates to object properties. For example, you can update custom or fixed object metadata, and tag files for downstream systems by updating or clearing object custom contexts.

  * **Manage storage costs** : Help optimize your Cloud Storage expenditures. For example, you can bulk delete unnecessary live objects, purge stale records by permanently deleting noncurrent object versions, and move Standard storage objects to colder [storage classes](https://docs.cloud.google.com/storage/docs/storage-classes), such as Archive storage, at scale.




## Job configurations

To create a storage batch operations job, set the following job configurations. Job configurations are parameters that control how the job processes objects.

  * **Job name** : A unique name to identify the storage batch operations job. Use this name to track, monitor, and reference the job. Job names are alphanumeric, for example, `job-01`.

  * **Job description** (Optional): A brief description of the purpose of the job. This description helps you understand and document what the job does. For example, `Deletes all objects in a bucket`.

  * **Bucket list** : A comma-separated list of one or more bucket names containing the objects that you want to process. You can specify up to 1,000 buckets from any project, as long as each bucket is enrolled in a storage intelligence plan.

  * **Object selection** : The selection criteria that define which objects to process. You can specify the criteria using any of the following options:

    * **Dataset filters** : Use Common Expression Language (CEL) to filter objects based on metadata fields in your Storage Insights dataset. You can run batch jobs on objects across multiple buckets in a project. When you use dataset filters for object selection, storage batch operations targets objects that are live and current as of the selected dataset snapshot. Consequently, the job only includes objects that have a `NULL` value for both `softDeleteTime` and `timeDeleted` at the time of the snapshot. For details, see [Create a job using advanced filters](https://docs.cloud.google.com/storage/docs/batch-operations/create-manage-batch-operation-jobs#advanced-filters).

    * **Manifest** : Create a manifest and specify its location when you create the storage batch operations job. The manifest is a CSV file uploaded to Google Cloud containing the list of objects to process. Each row in the manifest must include the `bucket` and `name` of the object. You can optionally specify the `generation` of the object. If you omit the `generation` value, the job processes the live version of the object.

The manifest file must include a header row with the following format:

`bucket,name,generation`

The following is an example of the manifest:
          
          bucket,name,generation
          bucket_1,object_1,generation_1
          bucket_1,object_2,generation_2
          bucket_2,object_3,generation_3
          

**Caution:** For single-bucket jobs, verify that the manifest includes objects only from the bucket provided in the job. For multi-bucket jobs, the CSV rows can reference different buckets within the project.

You can also create a manifest using Storage Insights datasets. For details, see [Create a manifest using Storage Insights datasets](https://docs.cloud.google.com/storage/docs/batch-operations/create-manage-batch-operation-jobs#create-manifest-using-insights-datasets).

    * **Object prefixes** : Specify a list of prefixes to filter objects in the bucket. The job only processes objects that match these prefixes. If you leave the prefix list empty, the job processes all objects in the bucket.

  * **Job type** : Storage batch operations supports the following job types, running a single job per batch operation.

    * **Object deletion** : [Delete objects](https://docs.cloud.google.com/storage/docs/deleting-objects) within a bucket to help optimize costs, manage your data lifecycle, and comply with data deletion policies.

**Caution:** By default, Cloud Storage retains soft-deleted objects for seven days. If you accidentally delete objects, you can restore them during this seven-day period. However, if you have disabled [soft delete](https://docs.cloud.google.com/storage/docs/soft-delete) for your bucket, you cannot recover deleted objects.
    * **Metadata updates** : You can modify the following object metadata:

      * [Custom metadata](https://docs.cloud.google.com/storage/docs/metadata#custom-metadata): You can update any user-defined key-value pairs associated with the object.

      * [Fixed metadata](https://docs.cloud.google.com/storage/docs/metadata#mutable): You can update `Cache-Control`, `Content-Disposition`, `Content-Encoding`, `Content-Language`, `Content-Type`, `Custom-Time`, and [retention configuration](https://docs.cloud.google.com/storage/docs/metadata#retention-config). For modifying object holds, use the object hold updates job type.

    * **Object hold updates** : You can enable or disable [object holds](https://docs.cloud.google.com/storage/docs/object-holds). Object holds prevent objects from being deleted or modified. These holds are essential for compliance and data retention.

    * **Object encryption key updates** : You can manage the [customer-managed encryption keys](https://docs.cloud.google.com/storage/docs/encryption/customer-managed-keys) for one or more objects. This capability includes applying or changing encryption keys using the [rewrite object](https://docs.cloud.google.com/storage/docs/json_api/v1/objects/rewrite) method.

    * **Object context updates** : Manage the [object contexts](https://docs.cloud.google.com/storage/docs/object-contexts) associated with the objects. You can either clear all existing object contexts or make specific updates, such as removing keys or inserting and updating key-value pairs.

    * **Object storage class updates** : You can change the storage class of objects in bulk to help optimize costs.

**Note:** Changing the storage class of an object involves rewriting its data. A rewrite is a Class A operation. These operations might incur additional charges depending on the age, location, and storage class of the data. For more information, see [Cloud Storage pricing](https://docs.cloud.google.com/storage/pricing). If you enable [Object Versioning](https://docs.cloud.google.com/storage/docs/using-object-versioning) for your bucket, Cloud Storage retains the original object as a noncurrent version. This version remains in the bucket until you explicitly delete it.
    * **Object access control list (ACL) updates** : You can patch object ACLs to add, update, or remove grants for entities like `allUsers` and `allAuthenticatedUsers`.

  * **Dry run** (Optional): Use dry-run mode to prevent accidental large-scale misconfigurations. A dry run simulates the operation without performing transformations. This simulation helps you validate your job configuration before you run the actual job. The dry run results provide a preview of the following details before you execute the job:

    * The number of objects that the job affects.

    * Potential errors.

    * The total size of the affected objects, if you filter by object prefixes.




## Pricing

To estimate the charges for your job or dry run, see [ Cloud Storage](https://docs.cloud.google.com/storage/pricing) pricing.

You can use a dry run to validate your configuration without incurring operation costs, although the dry run might incur object listing costs.

## Limitations

Storage batch operations has the following limitations:

  * Storage batch operations jobs have a maximum lifetime of 14 days. Any ongoing job that doesn't complete within 14 days of its creation is automatically cancelled.

  * You can include a maximum of 1,000 object prefixes in a single job.

  * Running more than 10 concurrent jobs on the same bucket degrades the performance of each job.

  * You can run a single batch job across a maximum of 1,000 buckets in a project.

  * Bucket filters and object filters are each limited to a maximum of 150 characters.

  * Storage batch operations automatically selects the Storage Insights dataset snapshot time based on the global manifest. This selection matches all targeted buckets to the same snapshot time for object discovery. The selected global snapshot time is returned in the [API response](https://docs.cloud.google.com/storage/docs/storagebatchoperations/reference/rest/v1/projects.locations.jobs#Job). If the snapshot time is older than two days, job creation fails. For information about how to resolve this failure, see [Troubleshooting Storage batch operations issues](https://docs.cloud.google.com/storage/docs/storage-intelligence/troubleshooting#batchops-stale-snapshot).

  * Storage batch operations is not supported on buckets that have [Requester Pays](https://docs.cloud.google.com/storage/docs/requester-pays) enabled.

  * When you use Storage Insights datasets for object selection, storage batch operations targets objects that are live and current as of the selected dataset snapshot.




## What's next

  * Learn how to [create and manage storage batch operations jobs](https://docs.cloud.google.com/storage/docs/batch-operations/create-manage-batch-operation-jobs).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
