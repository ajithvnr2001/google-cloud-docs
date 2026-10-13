---
url: https://docs.cloud.google.com/storage/docs/use-soft-deleted-objects/
title: Use soft-deleted objects \u00a0|\u00a0 Cloud Storage \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T20:12:37.132818+00:00
---

# Use soft-deleted objects  |  Cloud Storage  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/storage/docs/use-soft-deleted-objects/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Storage ](https://docs.cloud.google.com/docs/storage)
  * [ Cloud Storage ](https://docs.cloud.google.com/storage/docs)
  * [ Guides ](https://docs.cloud.google.com/storage/docs/discover-object-storage-console)



Send feedback 

#  Use soft-deleted objects Stay organized with collections  Save and categorize content based on your preferences. 

[Overview](https://docs.cloud.google.com/storage/docs/soft-delete) [Setup](https://docs.cloud.google.com/storage/docs/use-soft-delete)

This page describes how to list, access, and restore soft-deleted objects.

## Before you begin

To get the permissions that you need to list, access, and restore soft-deleted objects, ask your administrator to grant you the [Storage Admin ](https://docs.cloud.google.com/iam/docs/roles-permissions/storage#storage.admin) (`roles/storage.admin`) IAM role on the bucket, managed folder, or project. 

This predefined role contains the permissions required to list, access, and restore soft-deleted objects. To see the exact permissions that are required, expand the **Required permissions** section: 

#### Required permissions

The following permissions are required to list, access, and restore soft-deleted objects:

  * `storage.buckets.get` (this permission is only required for using the Google Cloud console to perform the instructions on this page) 
  * `storage.buckets.list` (this permission is only required for using the Google Cloud console to perform the instructions on this page) 
  * `storage.objects.get` (this permission is only required for using the Google Cloud console to perform the instructions on this page) 
  * `storage.objects.list`
  * `storage.objects.restore`
  * `storage.objects.create`
  * `storage.objects.delete` (this permission is only required for restoring objects in a way that causes existing objects to be overwritten) 
  * `storage.buckets.restore` (this permission is only required for bulk restoring soft-deleted objects) 



For information about granting roles on buckets, see [Set and manage IAM policies on buckets](https://docs.cloud.google.com/storage/docs/access-control/using-iam-permissions). For information about granting roles on projects, see [Manage access to projects](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access).

In order to manage [long-running operations](https://google.aip.dev/151) that get initiated from soft delete methods, you might need additional roles and permissions. See [required roles for long-running operations](https://docs.cloud.google.com/storage/docs/using-long-running-operations#required-roles) to learn more.

## List all of the soft-deleted objects in a bucket

Use the following instructions to list all of the soft-deleted objects in a bucket:

### Console

  1. In the Google Cloud console, go to the Cloud Storage **Buckets** page.  


[Go to Buckets](https://console.cloud.google.com/storage/browser)

  2. In the list of buckets, click the name of the bucket you want to view the soft-deleted objects of. The **Bucket details** page opens with the **Objects** tab selected.

  3. In the **Show** list, select **Soft-deleted objects only**. A list of soft-deleted objects is displayed.




### Command line

To display a list of all the soft-deleted objects in a bucket, use the [`gcloud storage ls`](https://docs.cloud.google.com/sdk/gcloud/reference/storage/ls) command with the `--soft-deleted` flag and the [`**` wildcard](https://docs.cloud.google.com/storage/docs/wildcards#surprising-behavior). Note that you might need to surround the wildcard expression with quotes.
    
    
      gcloud storage ls gs://BUCKET_NAME/** --soft-deleted
    

Replace the following:

  * `BUCKET_NAME`: the name of the bucket. For example, `my-bucket`.



### REST APIs

### JSON API

  1. Have gcloud CLI [installed and initialized](https://docs.cloud.google.com/sdk/docs/install), which lets you generate an access token for the `Authorization` header.

  2. Use [`cURL`](http://curl.haxx.se/) to call the [JSON API](https://docs.cloud.google.com/storage/docs/json_api) with a [request to list objects](https://docs.cloud.google.com/storage/docs/json_api/v1/objects/list) that uses the `?softDeleted` query parameter:
         
         curl -X GET \
           -H "Authorization: Bearer $(gcloud auth print-access-token)" \
           -H "Content-Type: application/json" \
           "https://storage.googleapis.com/storage/v1/b/BUCKET_NAME/o?softDeleted=true"

Where `BUCKET_NAME` is the name of the relevant bucket. For example, `my-bucket`.




## View all of the soft-deleted versions of an object

Use the following instructions to view all the soft-deleted versions of a specific object in your bucket:

### Console

  1. In the Google Cloud console, go to the Cloud Storage **Buckets** page.  


[Go to Buckets](https://console.cloud.google.com/storage/browser)

  2. In the list of buckets, click the name of the bucket that contains the object you want to view soft-deleted versions of. The **Bucket details** page opens with the **Objects** tab selected.

  3. Click the object that you want to view all the soft-deleted versions of. The **Object details** page displays.

  4. Click the **Version History** tab.

  5. In the **Show** list, select **Soft-deleted objects only**. A list of all the soft-deleted versions for that object displays.




### Command line

To display a list of all the soft-deleted versions of an object in a bucket, use the [`gcloud storage ls`](https://docs.cloud.google.com/sdk/gcloud/reference/storage/ls) command:
    
    
      gcloud storage ls gs://BUCKET_NAME/OBJECT_NAME --soft-deleted
    

Replace the following:

  * `BUCKET_NAME`: the name of the bucket. For example, `my-bucket`.
  * `OBJECT_NAME`: the name of the object you want to view all the versions of.



### REST APIs

### JSON API

  1. Have gcloud CLI [installed and initialized](https://docs.cloud.google.com/sdk/docs/install), which lets you generate an access token for the `Authorization` header.

  2. Use [`cURL`](http://curl.haxx.se/) to call the [JSON API](https://docs.cloud.google.com/storage/docs/json_api) with a [request to list objects](https://docs.cloud.google.com/storage/docs/json_api/v1/objects/list) that uses the `?softDeleted` query parameter:
         
         curl -X GET \
           -H "Authorization: Bearer OAUTH2_TOKEN" \
           -H "Content-Type: application/json" \
           "https://storage.googleapis.com/storage/v1/b/BUCKET_NAME/o?matchGlob=OBJECT_NAME&softDeleted=true"

Replace the following:

     * `BUCKET_NAME`: the name of the bucket. For example, `my-bucket`.
     * `OBJECT_NAME`: the name of the object for which you want to view all versions.



## Restore a soft-deleted object

You can restore a specific version of a soft-deleted object in your bucket. Note that you cannot restore objects in a soft-deleted bucket. To restore objects in a soft-deleted bucket, you must first [restore the soft-deleted bucket](https://docs.cloud.google.com/storage/docs/use-soft-deleted-buckets).

Use the following instructions to restore a soft-deleted object:

### Console

  1. In the Google Cloud console, go to the Cloud Storage **Buckets** page.  


[Go to Buckets](https://console.cloud.google.com/storage/browser)

  2. In the list of buckets, click the name of the bucket that contains the soft-deleted objects that you want to restore. The **Bucket details** page opens with the **Objects** tab selected.

  3. In the **Show** list, select **Soft-deleted objects only**.

  4. Navigate to the object, which may be located in a folder.

  5. Click the soft-deleted object. The **Object details** page displays.

  6. In the **Show** list, select **Soft-deleted objects only**. A list of all the soft-deleted versions of that object displays.

  7. To restore a specific soft-deleted version of an object, click **Restore** next to that object version. The restore object version pane opens.

  8. Click **Confirm**.




### Command line

To restore a soft-deleted version of an object, use the [`gcloud storage restore`](https://docs.cloud.google.com/sdk/gcloud/reference/storage/restore) command:
    
    
      gcloud storage restore gs://BUCKET_NAME/OBJECT_NAME#GENERATION_NUMBER
    

Replace the following:

  * `BUCKET_NAME`: the name of the bucket. For example, `my-bucket`.
  * `OBJECT_NAME`: the name of the object for which you want to view all the versions.
  * `GENERATION_NUMBER`: the generation number of the soft-deleted object you want to restore. For example, `1560468815691234`. If you don't specify the generation number, the latest version is restored.



For additional options for restoring multiple objects in bulk, including restoring all versions of an object with the `all-versions` flag, see the [`gcloud storage restore` reference](https://docs.cloud.google.com/sdk/gcloud/reference/storage/restore).

### REST APIs

### JSON API

  1. Have gcloud CLI [installed and initialized](https://docs.cloud.google.com/sdk/docs/install), which lets you generate an access token for the `Authorization` header.

  2. Use [`cURL`](http://curl.haxx.se/) to call the [JSON API](https://docs.cloud.google.com/storage/docs/json_api) with a [`POST` Object](https://docs.cloud.google.com/storage/docs/json_api/v1/objects/restore) request:
         
         curl -X POST \
           -H "Authorization: Bearer $(gcloud auth print-access-token)" \
           -H "Content-Type: application/json" \
           "https://storage.googleapis.com/storage/v1/b/BUCKET_NAME/o/OBJECT_NAME/restore?generation=GENERATION_NUMBER"

Where:

     * `BUCKET_NAME` is the name of the relevant bucket. For example, `my-bucket`.
     * `OBJECT_NAME` is the name of the soft-deleted object you want to restore. For example, `cat.jpeg`.
     * `GENERATION_NUMBER` is the generation number of the soft-deleted object you want to restore. For example, `1560468815691234`.



## Bulk restore soft-deleted objects in a bucket

If you want to restore a large number of objects, or don't know the specific objects that you want to restore, use a bulk restore operation. Note that bulk restore operations occur asynchronously and can, in some cases, take an hour or more to begin.

Bulk restore operation initiates a [long-running operation](https://google.aip.dev/151) on a bucket. You can use the Google Cloud CLI to get and list long-running operations so you can view the details and status of the bulk restore operation while it's in progress.

Use the following instructions to bulk restore soft-deleted objects in a bucket:

### Console

  1. In the Google Cloud console, go to the Cloud Storage **Buckets** page.  


[Go to Buckets](https://console.cloud.google.com/storage/browser)

  2. In the list of buckets, find the bucket that contains the objects you want to restore.

  3. Click the **Bucket overflow** menu (_more_vert_) associated with the bucket and select **Create restore job**.

The **Create a restore job** pane opens.

  4. In the **Choose which soft-deleted objects to restore** section, select the time range that you want to restore objects from.

  5. Optional: To restore only the objects that match a [glob pattern](https://docs.cloud.google.com/storage/docs/json_api/v1/objects/list#list-objects-and-prefixes-using-glob), select **Filter by glob pattern** and then enter a glob pattern.

  6. Optional: Specify additional restore behaviors in the **Restore options** section.

  7. Click **Create**.




You can track the progress of your bulk restore operation by clicking the **Notifications** button (_notifications_) in the Google Cloud console header.

### Command line

To use the bulk restore operation to restore all objects in a bucket, use the [`gcloud storage restore`](https://docs.cloud.google.com/sdk/gcloud/reference/storage/restore) command.

For example, the following command performs bulk restore operation to asynchronously restore all the objects of the bucket that were deleted during a specific time period:
    
    
      gcloud storage restore gs://BUCKET_NAME/** \
          --async --deleted-after-time=DELETED_AFTER_TIME \
          --deleted-before-time=DELETED_BEFORE_TIME
    

Replace the following:

  * `BUCKET_NAME`: the name of the bucket. For example, `my-bucket`.
  * `DELETED_AFTER_TIME`: an optional argument to specify the date after which the objects are restored. For example, `2022-12-01`.
  * `DELETED_BEFORE_TIME`: an optional argument to specify the date before which the objects are restored. For example, `2022-12-21`.



For additional options that you can use to filter the objects to be bulk restored, see the [`gcloud storage restore`](https://docs.cloud.google.com/sdk/gcloud/reference/storage/restore) reference.

If successful, the command returns the ID of the long-running operation associated with the bulk restore operation. You can get the details of the long-running operation or cancel the long-running operation to stop the bulk restore operation before it completes. For more information, see [Use long-running operations](https://docs.cloud.google.com/storage/docs/using-long-running-operations).

### REST APIs

### JSON API

  1. Have gcloud CLI [installed and initialized](https://docs.cloud.google.com/sdk/docs/install), which lets you generate an access token for the `Authorization` header.

  2. Use [`cURL`](http://curl.haxx.se/) to call the [JSON API](https://docs.cloud.google.com/storage/docs/json_api) with a [`POST` Object](https://docs.cloud.google.com/storage/docs/json_api/v1/objects/bulkRestore) request:
         
         curl -X POST \
           -H "Authorization: Bearer $(gcloud auth print-access-token)" \
           -H "Content-Type: application/json" \
           "https://storage.googleapis.com/storage/v1/b/BUCKET_NAME/o/bulkRestore"

Where `BUCKET_NAME` is the name of the relevant bucket. For example, `my-bucket`.




If successful, the command returns the ID of the long-running operation associated with the bulk restore operation. You can get the details of the long-running operation or cancel the long-running operation to stop the bulk restore operation before it completes. For more information, see [Use long-running operations](https://docs.cloud.google.com/storage/docs/using-long-running-operations).

## Use long-running operations for bulk restore

The bulk restore operation for objects initiates a [long-running operation](https://google.aip.dev/151). You can get and list long-running operations in order to view the details and status of a bulk restore operation, or delete a long-running operation in order to cancel a bulk restore operation while it's in progress.

For instructions on using long-running operations that get initiated from operations in Cloud Storage, such as the bulk restore operation, see [Use long-running operations](https://docs.cloud.google.com/storage/docs/using-long-running-operations).

The following example shows a long-running operation that's returned from a bulk restore operation:
    
    
    done: false
    {
      "kind": "storage@operation",
      "name": "projects/_/buckets/my-bucket/operations/CiQyODRlMTY0My0wNGExLTQ3MWItOTE2Zi1hZmQ0ZmM4ZDc4MjQQAg",
      "metadata": {
        "@type": "type.googleapis.com/google.storage.v2.BulkRestoreObjectsMetadata",
        "commonMetadata": {
          "type": "bulk-restore-objects",
          "createTime": "2023-10-20T21:08:11.289Z",
          "updateTime": "2023-10-20T21:18:37.583Z",
          "endTime": "2023-10-20T21:18:37.583Z",
          "requestedCancellation": false,
          "progressPercent": -1,
        },
        "allow_overwrite": false,
        "matchGlobs": ["*"],
        "succeededCount": "0",
        "failedCount": "0",
        "skippedCount": "0",
      },
      "done": true,
      "response": {
        "@type": "type.googleapis.com/google.storage.v2.BulkRestoreObjectsResponse"
      }
    }

## What's next

  * Learn more about [soft delete](https://docs.cloud.google.com/storage/docs/soft-delete).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
