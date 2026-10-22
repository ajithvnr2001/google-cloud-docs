---
url: https://docs.cloud.google.com/storage/docs/using-cross-bucket-replication/
title: Use cross-bucket replication \u00a0|\u00a0 Cloud Storage \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T10:29:14.093302+00:00
---

# Use cross-bucket replication  |  Cloud Storage  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/storage/docs/using-cross-bucket-replication/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Storage ](https://docs.cloud.google.com/docs/storage)
  * [ Cloud Storage ](https://docs.cloud.google.com/storage/docs)
  * [ Guides ](https://docs.cloud.google.com/storage/docs/discover-object-storage-console)



Send feedback 

#  Use cross-bucket replication Stay organized with collections  Save and categorize content based on your preferences. 

This page describes how to use [cross-bucket replication](https://docs.cloud.google.com/storage/docs/availability-durability#cross-bucket-replication), which uses [Storage Transfer Service](https://docs.cloud.google.com/storage-transfer/docs/overview) to copy new and updated objects asynchronously from a source bucket to a destination bucket. When you use cross-bucket replication, you create and manage replication jobs, which are a type of job in Storage Transfer Service.

## Before you begin

To use cross-bucket replication, you must complete prerequisite steps. For instructions, refer to [Before you begin](https://docs.cloud.google.com/storage-transfer/docs/cross-bucket-replication#before-you-begin) in the Storage Transfer Service documentation.

## Create a replication job

### Console

When you create a cross-bucket replication job using the Google Cloud console, the Storage Transfer Service service agent is automatically granted the `storage.legacyBucketOwner` role on the source bucket and the `storage.legacyBucketWriter` role on the destination bucket.

When using the Google Cloud console, you can create a replication job for existing buckets or for new buckets during the bucket creation process.

To create a replication job for a new bucket, follow the instructions for [creating a new bucket](https://docs.cloud.google.com/storage/docs/creating-buckets#create-bucket).

To create a replication job for an existing bucket, complete the following steps:

  1. In the Google Cloud console, go to the Cloud Storage **Buckets** page.  


[Go to Buckets](https://console.cloud.google.com/storage/browser)

  2. In the list of buckets, click the name of the source bucket whose objects you want to replicate.

  3. On the **Bucket details** page, click the **Configuration** tab.

  4. Locate the **Cross-bucket replication** option and click edit **Edit**.

  5. In the **Edit cross-bucket replication** pane that opens, click **Add a destination**.

  6. In the **Choose a destination** section, select a destination bucket, then click **Next**.

  7. In the **Choose replication settings** section, do the following:

     * Optional: To filter objects to replicate by object name prefix, select the **Replicate objects based on prefix** checkbox in the **Choose which objects to replicate** section.

       * To include objects by prefix, enter a prefix in the **Include objects with prefix** section, then click add **Add a prefix**.

       * To exclude objects by prefix, enter a prefix in the **Exclude objects with prefix** section, then click add **Add a prefix**.

     * Optional: To set a storage class for replicated objects, select a storage class from the menu in the **Set storage class for replicated objects** section.

If you skip this step, replicated objects use the destination bucket's storage class by default.

     1. Click **Save**.



### Command line

For Google Cloud CLI instructions on how to create a replication job, refer to [Create a replication job using the Google Cloud CLI](https://docs.cloud.google.com/storage-transfer/docs/cross-bucket-replication#create-replication-job).

### REST APIs

### JSON API

For JSON API instructions on how to create a replication job, refer to [Create a replication job using the JSON API](https://docs.cloud.google.com/storage-transfer/docs/cross-bucket-replication#create-replication-job).

To check the status of the replication job, [view Cloud Logging for Storage Transfer Service logs](https://docs.cloud.google.com/storage-transfer/docs/transfer-logs#view-logs).

## List replication jobs

### Console

You cannot list replication jobs using the Google Cloud console. See View replication job for instructions on how to view a single replication job at a time.

### Command line

For Google Cloud CLI instructions on how to list replication jobs, refer to [List replication jobs using the Google Cloud CLI](https://docs.cloud.google.com/storage-transfer/docs/cross-bucket-replication#list-replication-jobs).

### REST APIs

### JSON API

For JSON API instructions on how to list replication jobs, refer to [List replication jobs using the JSON API](https://docs.cloud.google.com/storage-transfer/docs/cross-bucket-replication#list-replication-jobs).

## View a replication job

### Console

  1. In the Google Cloud console, go to the Cloud Storage **Buckets** page.  


[Go to Buckets](https://console.cloud.google.com/storage/browser)

  2. In the list of buckets, click the name of the source bucket whose cross-bucket replication job you want to view.

  3. On the **Bucket details** page, click the **Configuration** tab.

  4. Locate the **Cross-bucket replication** option and click edit **Edit**.

The **Edit cross-bucket replication** pane appears, which displays the replication job for each destination bucket.




On the **Buckets** page, you can view the **Replication** column, which displays whether a bucket has a Turbo replication job or a cross-bucket replication job running. For instructions on displaying the **Replication** column, see [Show columns](https://docs.cloud.google.com/storage/docs/cloud-console#show-columns).

### Command line

For Google Cloud CLI instructions on how to view a replication job, refer to [View a replication job using the Google Cloud CLI](https://docs.cloud.google.com/storage-transfer/docs/cross-bucket-replication#view-replication-job).

### REST APIs

### JSON API

For JSON API instructions on how to view a replication job, refer to [View a replication job using the JSON API](https://docs.cloud.google.com/storage-transfer/docs/cross-bucket-replication#view-replication-job).

## Update a replication job

You can update the following fields of a replication job:

  * The description of the replication job

  * The configuration for running a replication job

  * The configuration of notifications published to Pub/Sub

  * The logging behavior for replication job operations

  * The status of the replication job (whether it's enabled, disabled, or deleted)




### Console

When using the Google Cloud console, you can only update a replication job by pausing or unpausing the job.

  1. In the Google Cloud console, go to the Cloud Storage **Buckets** page.  


[Go to Buckets](https://console.cloud.google.com/storage/browser)

  2. In the list of buckets, click the name of the source bucket that you want to pause or unpause replicating.

  3. On the **Bucket details** page, click the **Configuration** tab.

  4. Locate the **Cross-bucket replication** option and click edit **Edit**.

  5. In the **Edit cross-bucket replication** pane that appears, click pause **Pause** or play_arrow **Unpause** next to the replication job you want to update.




### Command line

For Google Cloud CLI instructions on how to update a replication job, refer to [Update a replication job using the Google Cloud CLI](https://docs.cloud.google.com/storage-transfer/docs/cross-bucket-replication#update-replication-job).

### REST APIs

### JSON API

For JSON API instructions on how to update a replication job, refer to [Update a replication job using the JSON API](https://docs.cloud.google.com/storage-transfer/docs/cross-bucket-replication#update-replication-job).

## Delete a replication job

### Console

  1. In the Google Cloud console, go to the Cloud Storage **Buckets** page.  


[Go to Buckets](https://console.cloud.google.com/storage/browser)

  2. In the list of buckets, click the name of the source bucket you want to stop replicating.

  3. On the **Bucket details** page, click the **Configuration** tab.

  4. Locate the **Cross-bucket replication** option and click edit **Edit**.

  5. In the **Edit cross-bucket replication** pane that appears, click delete **Delete** next to the replication job you want to delete.

  6. In the dialogue that appears, click **Confirm**.




### Command line

For Google Cloud CLI instructions on how to delete a replication job, refer to [Delete a replication job using the Google Cloud CLI](https://docs.cloud.google.com/storage-transfer/docs/cross-bucket-replication#delete-replication-job).

### REST APIs

### JSON API

For JSON API instructions on how to delete a replication job, refer to [Delete a replication job using the JSON API](https://docs.cloud.google.com/storage-transfer/docs/cross-bucket-replication#delete-replication-job).

## What's next

[Monitor your replicated objects](https://docs.cloud.google.com/storage/docs/monitoring#cross-bucket_replication_graphs).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-21 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-21 UTC."],[],[]] 
