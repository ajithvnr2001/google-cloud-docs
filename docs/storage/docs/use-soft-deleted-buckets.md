---
url: https://docs.cloud.google.com/storage/docs/use-soft-deleted-buckets/
title: Use soft-deleted buckets \u00a0|\u00a0 Cloud Storage \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T10:29:28.678047+00:00
---

# Use soft-deleted buckets  |  Cloud Storage  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/storage/docs/use-soft-deleted-buckets/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Storage ](https://docs.cloud.google.com/docs/storage)
  * [ Cloud Storage ](https://docs.cloud.google.com/storage/docs)
  * [ Guides ](https://docs.cloud.google.com/storage/docs/discover-object-storage-console)



Send feedback 

#  Use soft-deleted buckets Stay organized with collections  Save and categorize content based on your preferences. 

[Soft delete feature overview](https://docs.cloud.google.com/storage/docs/soft-delete)

This page describes how to list and restore soft-deleted buckets.

## Overview

After a bucket is soft-deleted, it's retained by Cloud Storage until its hard delete time, and cannot be modified while in a soft-deleted state. The hard delete time is at least as long as the latest hard delete time of the bucket's objects. After the hard delete time has elapsed, Cloud Storage permanently deletes the bucket. When you restore a soft-deleted bucket, it is returned to a live state, and objects that were in the bucket at the time of deletion can also be restored.

## Considerations

  * To protect against malicious deletion, a soft-deleted bucket cannot be permanently deleted until the bucket has been retained for its full soft delete retention duration.

  * After a bucket is soft deleted, you must restore the bucket before you can list or restore the soft-deleted objects in it.

  * To restore a soft-deleted bucket, you must have the bucket's generation number. To retrieve a soft-deleted bucket's generation number, see List soft-deleted buckets.

  * A soft-deleted bucket can only be restored if there is no live bucket with the same name. If you or anyone else creates a bucket with the same name as a soft-deleted bucket, you cannot restore the soft-deleted bucket until the new bucket is deleted.

  * When you restore a soft-deleted bucket by using the gcloud CLI or JSON API, the objects in the bucket aren't restored. To restore soft-deleted objects, you'll need to perform an object restore operation after you restore the soft-deleted bucket.

  * Tag bindings might not be recovered when you restore a soft-deleted bucket with tags. To avoid data loss, when you restore a soft-deleted bucket with tag bindings, we recommend checking to ensure the bucket's tag bindings were recovered. If the bucket's tag bindings weren't recovered, you'll need to [manually bind the unrecovered tags to the bucket](https://docs.cloud.google.com/resource-manager/docs/tags/tags-creating-and-managing#attaching).




## Required permissions

To get the permissions that you need to restore soft-deleted buckets, ask your administrator to grant you the [Storage Admin ](https://docs.cloud.google.com/iam/docs/roles-permissions/storage#storage.admin) (`roles/storage.admin`) IAM role on the Cloud Storage project. 

This predefined role contains the permissions required to restore soft-deleted buckets. To see the exact permissions that are required, expand the **Required permissions** section: 

#### Required permissions

The following permissions are required to restore soft-deleted buckets:

  * `storage.buckets.list`
  * `storage.buckets.restore`
  * Restore objects when you use the Google Cloud console to restore a soft-deleted bucket: 
    * `storage.objects.restore`
    * `storage.objects.create`



## List soft-deleted buckets

You can perform list operations to retrieve your soft-deleted buckets' metadata.

**Note:** A bucket cannot be listed if its hard delete time has elapsed.

Use the following instructions to list the soft-deleted buckets in your project:

### Console

  1. In the Google Cloud console, go to the Cloud Storage **Buckets** page.  


[Go to Buckets](https://console.cloud.google.com/storage/browser)

  2. Click **View options**.

  3. Select **Soft deleted buckets only**.

  4. Click **Save**.

A list of soft-deleted buckets is displayed. If a soft-deleted bucket has multiple generations, each bucket generation appears in a separate row.




### Command line

To list soft-deleted buckets, use the [`gcloud storage ls`](https://docs.cloud.google.com/sdk/gcloud/reference/storage/buckets/list) command:
    
    
    gcloud storage ls --buckets --soft-deleted --full
    

### REST APIs

### JSON API

  1. Have gcloud CLI [installed and initialized](https://docs.cloud.google.com/sdk/docs/install), which lets you generate an access token for the `Authorization` header.

  2. Use [`cURL`](http://curl.haxx.se/) to call the [JSON API](https://docs.cloud.google.com/storage/docs/json_api) with a [`Buckets: list`](https://docs.cloud.google.com/storage/docs/json_api/v1/buckets/list) request that uses the `softDeleted` query parameter:
         
         curl -X GET \
           -H "Authorization: Bearer $(gcloud auth print-access-token)" \
           -H "Content-Type: application/json" \
           "https://storage.googleapis.com/storage/v1/b?project=PROJECT_IDENTIFIER&softDeleted=true"

Replace `PROJECT_IDENTIFIER` with the ID or number of the project containing the soft-deleted buckets that you want to list.




## Restore a soft-deleted bucket

Use the following instructions to restore a soft-deleted bucket.

When you restore a soft-deleted bucket using the Google Cloud console, you can also restore the soft-deleted objects that were in the bucket.

### Console

  1. In the Google Cloud console, go to the Cloud Storage **Buckets** page.  


[Go to Buckets](https://console.cloud.google.com/storage/browser)

  2. Display soft-deleted buckets in the list of buckets, if they don't already appear. For steps, see List soft-deleted buckets.

  3. In the row for the bucket that you want to restore, click **Restore**.

  4. If the bucket has multiple generations, on the **Specify bucket generation** tab, select the generation to restore.

  5. Click the **Specify objects to restore** tab.

  6. In the **Specify objects to restore** section, select whether you want to restore the soft-deleted objects that were in the bucket. The following options are available:

     * **Don't restore objects**.

You can restore soft-deleted objects later if needed.

     * **Restore all objects**.

     * **Restore objects that match criteria**. Do the following:

       1. Select the time range that you want to restore objects from.

       2. Optional: To restore only the objects that match a [glob pattern](https://docs.cloud.google.com/storage/docs/json_api/v1/objects/list#list-objects-and-prefixes-using-glob), select **Filter by glob pattern** and enter a glob pattern.

  7. Optional: Specify additional restore behaviors in the **Additional options** section.

  8. Click **Restore**.

Cloud Storage restores the soft-deleted bucket to a live state.

If you restore the objects in the bucket, Cloud Storage creates a bulk restore operation for the objects. The operation occurs asynchronously and might take an hour or more to begin. You can track the progress of the operation by clicking the **Notifications** button (_notifications_) in the Google Cloud console header. Or, you can use the gcloud CLI to track the status of the associated [long-running operation](https://docs.cloud.google.com/storage/docs/use-soft-deleted-objects#use-lros).




### Command line

To restore a soft-deleted bucket, use the [`gcloud storage restore`](https://docs.cloud.google.com/sdk/gcloud/reference/storage/restore) command:
    
    
      gcloud storage restore gs://BUCKET_NAME#GENERATION_NUMBER
    

Replace the following:

  * `BUCKET_NAME`: the name of the soft-deleted bucket you want to restore.

  * `GENERATION_NUMBER`: the permanent, unique generation number of the soft-deleted bucket you want to restore. To get your bucket's generation number, see List soft-deleted buckets.




Cloud Storage restores the soft-deleted bucket to a live state. Note that restoring the bucket doesn't restore the objects that were in the bucket. To restore the soft-deleted objects, see [Restore a soft-deleted object](https://docs.cloud.google.com/storage/docs/use-soft-deleted-objects#restore).

### REST APIs

### JSON API

  1. Have gcloud CLI [installed and initialized](https://docs.cloud.google.com/sdk/docs/install), which lets you generate an access token for the `Authorization` header.

  2. Use [`cURL`](http://curl.haxx.se/) to call the [JSON API](https://docs.cloud.google.com/storage/docs/json_api) with a [`Buckets: restore`](https://docs.cloud.google.com/storage/docs/json_api/v1/buckets/restore) request:
         
         curl -X POST \
           -H "Authorization: Bearer $(gcloud auth print-access-token)" \
           -H "Content-Type: application/json" \
           "https://storage.googleapis.com/storage/v1/b/BUCKET_NAME/restore?generation=GENERATION_NUMBER

Where:

     * `BUCKET_NAME` is the name of the bucket you want to restore. For example, `my-bucket`.

     * `GENERATION_NUMBER` is the permanent, unique generation number of the soft-deleted bucket you want to restore. To get your bucket's generation number, see List soft-deleted buckets.

Cloud Storage restores the soft-deleted bucket to a live state. Note that restoring the bucket doesn't restore the objects that were in the bucket. To restore the soft-deleted objects, see [Restore a soft-deleted object](https://docs.cloud.google.com/storage/docs/use-soft-deleted-objects#restore).




## What's next

  * [Restore soft-deleted objects in your bucket](https://docs.cloud.google.com/storage/docs/use-soft-deleted-objects#restore).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-21 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-21 UTC."],[],[]] 
