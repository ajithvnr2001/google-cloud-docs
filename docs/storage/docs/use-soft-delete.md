---
url: https://docs.cloud.google.com/storage/docs/use-soft-delete/
title: Set and manage soft delete policies \u00a0|\u00a0 Cloud Storage \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T09:37:44.763870+00:00
---

# Set and manage soft delete policies  |  Cloud Storage  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/storage/docs/use-soft-delete/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Storage ](https://docs.cloud.google.com/docs/storage)
  * [ Cloud Storage ](https://docs.cloud.google.com/storage/docs)
  * [ Guides ](https://docs.cloud.google.com/storage/docs/discover-object-storage-console)



Send feedback 

#  Set and manage soft delete policies Stay organized with collections  Save and categorize content based on your preferences. 

[Overview](https://docs.cloud.google.com/storage/docs/soft-delete) [Usage](https://docs.cloud.google.com/storage/docs/use-soft-deleted-objects)

This page describes how to set and manage [soft delete policies](https://docs.cloud.google.com/storage/docs/soft-delete#soft-delete-policy). You can set new policies on buckets to enable soft delete, as well as update and check the status of existing policies. To learn how to disable soft delete, see [Disable soft delete](https://docs.cloud.google.com/storage/docs/disable-soft-delete).

To learn how to list and restore soft-deleted objects, see [Use soft-deleted objects](https://docs.cloud.google.com/storage/docs/use-soft-deleted-objects). To learn how to list and restore soft-deleted buckets, see [Use soft-deleted buckets](https://docs.cloud.google.com/storage/docs/use-soft-deleted-buckets).

## Required roles

To get the permissions that you need to enable and manage soft delete policies, ask your administrator to grant you the [Storage Admin ](https://docs.cloud.google.com/iam/docs/roles-permissions/storage#storage.admin) (`roles/storage.admin`) IAM role on the bucket or the project that contains the bucket. 

This predefined role contains the permissions required to enable and manage soft delete policies. To see the exact permissions that are required, expand the **Required permissions** section: 

#### Required permissions

The following permissions are required to enable and manage soft delete policies:

  * `storage.buckets.get`
  * `storage.buckets.update`
  * `storage.buckets.list` (this permission is only required if you plan to use the Google Cloud console to perform the instructions on this page) 



For information about granting roles, see [Set and manage IAM policies on buckets](https://docs.cloud.google.com/storage/docs/access-control/using-iam-permissions) or [Manage access to projects](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access).

## Edit a bucket's soft delete policy

The new soft delete retention duration only applies to objects or buckets that you delete after the soft delete policy takes effect. Existing soft-deleted objects aren't affected by updates made to the soft delete policy and are retained for the duration that was in effect when they were deleted.

Use the following instructions to edit a bucket's soft delete policy:

### Console

  1. In the Google Cloud console, go to the Cloud Storage **Buckets** page.  


[Go to Buckets](https://console.cloud.google.com/storage/browser)

  2. In the list of buckets, click the name of the bucket whose soft delete policy you want to edit.

  3. Click the **Protection** tab.

  4. In the **Soft delete policy (for data recovery)** section, add a new soft delete policy or edit the [retention duration](https://docs.cloud.google.com/storage/docs/soft-delete#retention-duration) of an existing policy by using the following steps:

     1. Click **Edit**.

     2. In the **Set a soft delete policy** dialogue that appears, specify a [soft delete retention duration](https://docs.cloud.google.com/storage/docs/soft-delete#retention-duration) by choosing a unit of time and a length of time.

     3. Click **Save**.




To learn how to get detailed error information about failed Cloud Storage operations in the Google Cloud console, see [Troubleshooting](https://docs.cloud.google.com/storage/docs/troubleshooting#trouble-console).

### Command line

To add or edit the soft delete policy on a bucket, use the [`gcloud storage buckets update`](https://docs.cloud.google.com/sdk/gcloud/reference/storage/buckets#update) command with the `--soft-delete-duration` flag:
    
    
      gcloud storage buckets update gs://BUCKET_NAME --soft-delete-duration=SOFT_DELETE_DURATION
    

Where:

  * `BUCKET_NAME` is the name of the bucket. For example, `my-bucket`.

  * `SOFT_DELETE_DURATION` specifies the [soft delete retention duration](https://docs.cloud.google.com/storage/docs/soft-delete#retention-duration).

    * The unit `s` represents seconds.
    * The unit `d` represents days.
    * The unit `m` represents months.

For example:

    * `7d43200s` sets a retention duration of seven and a half days (7 days and 43,200 seconds).

    * `2w1d` sets a retention duration of two weeks and one day.




### REST APIs

### JSON API

  1. Have gcloud CLI [installed and initialized](https://docs.cloud.google.com/sdk/docs/install), which lets you generate an access token for the `Authorization` header.

  2. Create a JSON file that contains the following information:
         
         {
           "softDeletePolicy": {
             "retentionDurationSeconds": "TIME_IN_SECONDS"
           }
         }

Where `TIME_IN_SECONDS` is the amount of time in seconds you want to set the [soft delete retention duration](https://docs.cloud.google.com/storage/docs/soft-delete#retention-duration) to. For example, `2678400` for 2,678,400 seconds (31 days).

  3. Use [`cURL`](http://curl.haxx.se/) to call the [JSON API](https://docs.cloud.google.com/storage/docs/json_api) with a [`PATCH` Bucket](https://docs.cloud.google.com/storage/docs/json_api/v1/buckets/patch) request:
         
         curl -X PATCH --data-binary @JSON_FILE_NAME \
           -H "Authorization: Bearer $(gcloud auth print-access-token)" \
           -H "Content-Type: application/json" \
           "https://storage.googleapis.com/storage/v1/b/BUCKET_NAME"

Where:

     * `JSON_FILE_NAME` is the path for the JSON file that you created in Step 2.
     * `BUCKET_NAME` is the name of the relevant bucket. For example, `my-bucket`.



## Check if the soft delete policy is enabled on a bucket

### Console

  1. In the Google Cloud console, go to the Cloud Storage **Buckets** page.  


[Go to Buckets](https://console.cloud.google.com/storage/browser)

  2. In the list of buckets, click the name of the bucket whose soft delete policy you want to check.

  3. Click the **Protection** tab.

The status displays in the **Soft delete policy (for data recovery)** section.




You can also use the **Protection tab** to check if there's a soft delete policy on your bucket.

To learn how to get detailed error information about failed Cloud Storage operations in the Google Cloud console, see [Troubleshooting](https://docs.cloud.google.com/storage/docs/troubleshooting#trouble-console).

### Command line

To check the soft delete policy status of a bucket, use the [`gcloud storage buckets describe`](https://docs.cloud.google.com/sdk/gcloud/reference/storage/buckets/describe) command:
    
    
      gcloud storage buckets describe gs://BUCKET_NAME \
          --format="default(soft_delete_policy)"
    

Where:

  * `BUCKET_NAME` is the name of the bucket. For example, `my-bucket`.



### REST APIs

### JSON API

  1. Have gcloud CLI [installed and initialized](https://docs.cloud.google.com/sdk/docs/install), which lets you generate an access token for the `Authorization` header.

  2. Use [`cURL`](http://curl.haxx.se/) to call the [JSON API](https://docs.cloud.google.com/storage/docs/json_api) with a [`GET` Bucket](https://docs.cloud.google.com/storage/docs/json_api/v1/buckets/get) request:
         
         curl -X GET \
           -H "Authorization: Bearer $(gcloud auth print-access-token)" \
           -H "Content-Type: application/json" \
           "https://storage.googleapis.com/storage/v1/b/BUCKET_NAME?fields=softDeletePolicy"

Where `BUCKET_NAME` is the name of the relevant bucket. For example, `my-bucket`.




## What's next

  * Learn how to [use soft-deleted objects](https://docs.cloud.google.com/storage/docs/use-soft-deleted-objects).
  * Learn how to [use soft-deleted buckets](https://docs.cloud.google.com/storage/docs/use-soft-deleted-buckets).
  * Learn how to [disable soft delete](https://docs.cloud.google.com/storage/docs/disable-soft-delete).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
