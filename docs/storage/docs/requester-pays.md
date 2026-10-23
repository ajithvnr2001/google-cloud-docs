---
url: https://docs.cloud.google.com/storage/docs/requester-pays/
title: Requester Pays \u00a0|\u00a0 Cloud Storage \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T09:40:54.350556+00:00
---

# Requester Pays  |  Cloud Storage  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/storage/docs/requester-pays/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Storage ](https://docs.cloud.google.com/docs/storage)
  * [ Cloud Storage ](https://docs.cloud.google.com/storage/docs)
  * [ Guides ](https://docs.cloud.google.com/storage/docs/discover-object-storage-console)



Send feedback 

#  Requester Pays Stay organized with collections  Save and categorize content based on your preferences. 

The Requester Pays feature lets you share data from your Cloud Storage buckets, while requiring users who access the data to pay for the associated costs. Requester Pays is useful when you want to make large amounts of data available to users without being charged for their access to that data.

For steps to enable or disable Requester Pays on a bucket, see [Use Requester Pays](https://docs.cloud.google.com/storage/docs/using-requester-pays).

## Overview of Requester Pays

Whenever a user accesses a Cloud Storage resource such as a bucket or object, there are [charges](https://docs.cloud.google.com/storage/pricing) associated with making and executing the request. Such charges include:

  * [**Data processing charges**](https://docs.cloud.google.com/storage/pricing#process-pricing) for operations, replication, and data retrieval.

  * [**Network usage charges**](https://docs.cloud.google.com/storage/pricing#network-pricing) for reading the data.




Normally, the project owner of the resource is billed for these charges; however, if the requester provides a _billing project_ with their request, the requester's project is billed instead. With Requester Pays enabled on your bucket, you can _require_ requesters to include a billing project in their requests, thus billing the requester's project.

**Note:** You currently incur no charges when you use the [Cloud Storage Transfer Service](https://docs.cloud.google.com/storage-transfer) and have a billing project in your request. This is a promotional price.

#### Charges not covered

[**Data storage charges**](https://docs.cloud.google.com/storage/pricing#storage-pricing), including [**early deletion charges**](https://docs.cloud.google.com/storage/pricing#early-delete), are always applied to the project that contains the bucket, even if Requester Pays is enabled.

### Restrictions

The following restrictions apply when using Requester Pays:

  * You cannot use a bucket that has Requester Pays enabled for imports and exports from Cloud SQL.
  * You cannot use a bucket that has Requester Pays enabled for [exports from Pub/Sub](https://docs.cloud.google.com/pubsub/docs/cloudstorage).



## Use and access requirements

To enable Requester Pays on a bucket, [enable the metadata flag](https://docs.cloud.google.com/storage/docs/using-requester-pays#set) on the bucket. Once enabled, only the following users can access the bucket or its contents:

  * Requesters who [include a billing project in their request](https://docs.cloud.google.com/storage/docs/using-requester-pays#using). The project used in the request must be in good standing, and the user must [have a role](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access#grant-single-role) in the project that contains the `serviceusage.services.use` permission. The **Service Usage Consumer** role contains the required permission.

  * Requesters who don't include a billing project but have `resourcemanager.projects.createBillingAssignment` permission for the project that contains the bucket. The **Billing Project Manager** role contains the required permission. Access charges associated with these requests are billed to the project that contains the bucket.




All other requests to the bucket fail with a `400 UserProjectMissing` error.

In addition to these requirements, the requester must have sufficient [permission](https://docs.cloud.google.com/storage/docs/access-control) to perform the requested action. For example, a user that provides a valid billing project in their request cannot upload objects to the bucket unless they also have explicit permission to do so, such as by having `storage.objects.create` permission for that bucket or the project that contains it.

When disabling Requester pays, you must include a billing project in your request, or have the `resourcemanager.projects.createBillingAssignment` permission.

**Important:** Buckets that have Requester Pays disabled still accept requests that include a billing project, and charges are applied to the billing project supplied in the request. Consider any billing implications prior to including a billing project in all of your requests.

## Source-billed operations

Operations that have both a source bucket and a destination bucket, such as a copy or rewrite, charge to the project that contains the source bucket. In most cases, such as direct calls using the JSON and XML APIs, you only need to include a billing project if the **source** bucket has Requester Pays enabled.

In some cases, such as `gcloud storage cp` with a `--no-clobber` flag, you need to include a billing project if either the source bucket or destination bucket (or both) have Requester Pays enabled. This is because such operations make calls to both the source and destination buckets in the course of performing the action.

## Multi-request operations

For operations that require multiple requests to complete, the use of billing projects in your requests have the following behaviors:

  * For [resumable uploads](https://docs.cloud.google.com/storage/docs/resumable-uploads), only the first request needs to [include a billing project](https://docs.cloud.google.com/storage/docs/using-requester-pays#using), and it applies to the entire upload. Billing projects specified in subsequent requests are ignored.

  * For [rewrites with the JSON API](https://docs.cloud.google.com/storage/docs/json_api/v1/objects/rewrite) and [XML API multipart uploads](https://docs.cloud.google.com/storage/docs/multipart-uploads), each request can use a different billing project, and a billing project specified in an earlier request does not apply to subsequent requests.




## Billing

Charges associated with including a billing project in your request do not appear separately in your billing. For example, say you make several downloads from a Requester Pays bucket, and you use the project `my-project` as the project to bill for the request. If `my-project` also contains a bucket from which you perform downloads, your bill only shows the total charges for your combined downloads. It does not distinguish between the downloads from your own bucket and those from the Requester Pays bucket.

If you want to distinguish between charges from your own Cloud Storage resources and charges from including billing projects in your requests, you should [create a project](https://docs.cloud.google.com/resource-manager/docs/creating-managing-projects#creating_a_project) that contains no Cloud Storage resources: this project is thus dedicated to making requests to resources in other projects, such as Requester Pays buckets.

## What's next

  * Learn how to [use Requester Pays](https://docs.cloud.google.com/storage/docs/using-requester-pays).
  * [Make data publicly available](https://docs.cloud.google.com/storage/docs/access-control/making-data-public).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
