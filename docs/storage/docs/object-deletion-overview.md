---
url: https://docs.cloud.google.com/storage/docs/object-deletion-overview/
title: About object deletion \u00a0|\u00a0 Cloud Storage \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T09:40:55.949703+00:00
---

# About object deletion  |  Cloud Storage  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/storage/docs/object-deletion-overview/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Storage ](https://docs.cloud.google.com/docs/storage)
  * [ Cloud Storage ](https://docs.cloud.google.com/storage/docs)
  * [ Guides ](https://docs.cloud.google.com/storage/docs/discover-object-storage-console)



Send feedback 

#  About object deletion Stay organized with collections  Save and categorize content based on your preferences. 

Deleting objects that you no longer need helps you reduce storage costs, comply with data retention requirements, and keep your buckets organized. Cloud Storage supports two primary methods for deleting objects:

  * **Single-object deletion** : deletes individual objects for targeted updates.
  * **Bulk object deletion** : deletes multiple objects simultaneously or on an automated schedule.



For each deletion method, Cloud Storage provides various tools to delete objects manually, programmatically, or through automated policies. Review these deletion methods and available tools to choose the best approach for your workload.

For step-by-step instructions to delete objects, see [Delete objects](https://docs.cloud.google.com/storage/docs/deleting-objects).

## Single-object deletion

Single-object deletion provides precise control over specific data. You typically delete single objects when you need to perform immediate, targeted updates to your bucket's data. Common use cases for single-object deletion include the following:

  * **Correcting errors** : removing an object that you uploaded accidentally or an object that contains incorrect data.

  * **Cleanup** : manually removing temporary objects or logs after completing a task.

  * **Application logic** : automatically removing an object when an application event occurs, such as a user deleting a profile photo.

  * **Security and compliance** : deleting objects to remove sensitive information.




### Tools for single-object deletion

To delete a single object from your bucket, use any of the following tools. Each tool sends an individual `DELETE` request per object.

Tool | Description  
---|---  
[Google Cloud console](https://docs.cloud.google.com/storage/docs/deleting-objects#delete-object) | Deletes an individual object in the Google Cloud console.  
[Google Cloud CLI](https://docs.cloud.google.com/storage/docs/deleting-objects#delete-object) | Deletes an object by using the [`gcloud storage rm`](https://docs.cloud.google.com/sdk/gcloud/reference/storage/rm) command.  
[Client libraries](https://docs.cloud.google.com/storage/docs/deleting-objects#delete-object) | Deletes an object programmatically by using a supported language, such as C++, C#, Go, Java, Node.js, PHP, Python, or Ruby.  
[REST APIs](https://docs.cloud.google.com/storage/docs/deleting-objects#rest-delete-object) | Deletes an object by using the JSON API or XML API.  
  
## Bulk object deletion

Bulk object deletion is designed for high-efficiency operations on large datasets. Use bulk deletion to manage storage costs and automate data hygiene across buckets. Common use cases for bulk object deletion include the following:

  * **Cost optimization** : removing large datasets that you no longer need for operations, such as old logs or temporary build artifacts.

  * **Compliance automation** : automatically enforcing data retention policies by deleting objects after a specific retention period, such as 30 days.

  * **Bucket migration or decommissioning** : clearing millions or billions of objects when migrating data or closing a project.

  * **Data pipeline cleanup** : removing intermediate processing objects after a pipeline generates a final report or dataset.




### Tools for bulk object deletion

To delete objects in bulk, use any of the following tools. These tools are optimized for higher throughput and reduced overhead compared to individual requests.

Tool | Description  
---|---  
[Google Cloud console](https://docs.cloud.google.com/storage/docs/deleting-objects#bulk-delete) | Deletes up to one million objects interactively. After you initiate a deletion request, Cloud Storage processes the deletion in the background. You can check the status of your bulk deletion by clicking the **Notifications** button (_notifications_) in the Google Cloud console header.  
[Google Cloud CLI](https://docs.cloud.google.com/storage/docs/deleting-objects#delete-objects-with-prefix) | Deletes all objects that share a common prefix by using the [`gcloud storage rm --recursive`](https://docs.cloud.google.com/sdk/gcloud/reference/storage/rm) command. This command is suitable for small-to-medium-scale bulk deletions from the command line.  
[Multi-object delete XML API](https://docs.cloud.google.com/storage/docs/xml-api/post-bucket) | Deletes up to 1,000 objects programmatically in a single `POST` request. The multi-object delete XML API is interoperable with the Amazon S3 API. As a result, you can use your existing Amazon S3 tools, libraries, and workflows to manage objects in Cloud Storage. The XML API is useful if you are migrating data or managing resources across both platforms. When you use the XML API to delete multiple objects, Cloud Storage generates data access audit logs. If you enable data access audit logs, these logs include details about the overall request and individual object deletions. For details, see [Audit logs for multi-object delete XML API](https://docs.cloud.google.com/storage/docs/audit-logging#xml-multi-object-delete-audit-logs). The multi-object delete XML API has the following limitations:

  * **Governance mode bypass** : Unlike Amazon S3, Cloud Storage doesn't allow bypassing governance mode during deletion. In Amazon S3, you can delete objects locked in governance mode by specifying the `x-amz-bypass-governance-retention` header. Cloud Storage strictly enforces object retention policies to maintain data immutability.
  * **Delete markers** : Cloud Storage doesn't support Amazon S3 delete markers for single-object or multi-object deletions. To restore a noncurrent object in Cloud Storage, you must copy the specific version to the live object by using an XML API [`PUT` request](https://docs.cloud.google.com/storage/docs/using-versioned-objects#restore).
  * **Conditional delete operations** : The Cloud Storage multi-object delete XML API doesn't support conditional deletions based on `ETag`, `Last-Modified`, or `Size`. Requests that include these parameters return an HTTP `400 Bad Request` status code. To perform conditional operations in Cloud Storage, use headers such as [`x-goog-if-generation-match`](https://docs.cloud.google.com/storage/docs/xml-api/reference-headers#xgoogifgenerationmatch) or [`x-goog-if-metageneration-match`](https://docs.cloud.google.com/storage/docs/xml-api/reference-headers#xgoogifmetagenerationmatch).

  
[Storage batch operations](https://docs.cloud.google.com/storage/docs/batch-operations/overview) | Deletes up to billions of objects based on a manifest file by using a fully managed service with built-in tracking and retries. Use storage batch operations to perform the following tasks:

  * Delete millions or billions of objects.
  * Enhance reliability with built-in tracking, retries, and error handling.
  * Reduce client-side overhead compared to scripting individual API calls.

  
[Object Lifecycle Management](https://docs.cloud.google.com/storage/docs/lifecycle) | Deletes objects automatically based on user-defined lifecycle rules, such as object age or storage class. To delete objects in bulk, [configure an Object Lifecycle Management rule](https://docs.cloud.google.com/storage/docs/managing-lifecycles#set) on your bucket. Set the condition `Age` to `0` days and the action to `Delete`. After you set the rule, Cloud Storage [performs the bulk deletion asynchronously](https://docs.cloud.google.com/storage/docs/lifecycle#behavior). **Caution:** Setting an Object Lifecycle Management rule with `Age` set to `0` days permanently deletes all existing and newly added objects in the bucket. Apply this configuration only when you intend to delete all objects in the bucket.  
[Batch API requests](https://docs.cloud.google.com/storage/docs/batch) | Batches multiple deletion requests into a single HTTP request when you use supported client libraries or the JSON API directly. This batching reduces client-side connection overhead and latency.  
  
## Choose a deletion method

The optimal method and tool for object deletion depend on the object count and your workflow requirements. Use the following decision matrix to select an approach for your use case:

Use case | Deletion method | Recommended tool  
---|---|---  
Delete an individual object or a small number of specific objects | Single-object deletion | [Google Cloud console](https://docs.cloud.google.com/storage/docs/deleting-objects#delete-object), [`gcloud storage rm`](https://docs.cloud.google.com/sdk/gcloud/reference/storage/rm), client libraries, or REST APIs  
Delete up to 1,000 objects in a single programmatic request | Bulk object deletion | [Multi-object delete XML API](https://docs.cloud.google.com/storage/docs/deleting-objects#bulk-delete), Amazon S3 CLI, or Amazon S3-compatible client libraries (such as Boto3)  
Delete objects that share a common prefix | Bulk object deletion | [`gcloud storage rm --recursive`](https://docs.cloud.google.com/storage/docs/deleting-objects#delete-objects-with-prefix)  
Delete up to one million objects interactively in the browser | Bulk object deletion | [Google Cloud console](https://docs.cloud.google.com/storage/docs/deleting-objects#bulk-delete)  
Delete millions or billions of objects asynchronously with built-in tracking | Bulk object deletion | [Storage batch operations](https://docs.cloud.google.com/storage/docs/batch-operations/overview)  
Delete objects automatically based on conditions (such as age or storage class) | Bulk object deletion | [Object Lifecycle Management](https://docs.cloud.google.com/storage/docs/lifecycle)  
  
## What's next

  * [Delete a bucket](https://docs.cloud.google.com/storage/docs/deleting-buckets) when you no longer need the bucket.
  * Learn about [Object Versioning](https://docs.cloud.google.com/storage/docs/object-versioning) to retain multiple versions of an object in the same bucket.
  * Configure [Object Lifecycle Management](https://docs.cloud.google.com/storage/docs/lifecycle) to automate object deletions based on custom conditions.
  * Perform large-scale object deletions with [storage batch operations](https://docs.cloud.google.com/storage/docs/batch-operations/overview).
  * Protect objects from accidental deletion by using [soft delete](https://docs.cloud.google.com/storage/docs/soft-delete).
  * Enforce data retention policies by using [Object Retention Lock](https://docs.cloud.google.com/storage/docs/object-lock) and [Bucket Lock](https://docs.cloud.google.com/storage/docs/bucket-lock).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
