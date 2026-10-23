---
url: https://docs.cloud.google.com/storage/docs/getting-storage-layout/
title: Get a bucket's storage layout \u00a0|\u00a0 Cloud Storage \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T13:08:39.343479+00:00
---

# Get a bucket's storage layout  |  Cloud Storage  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/storage/docs/getting-storage-layout/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Storage ](https://docs.cloud.google.com/docs/storage)
  * [ Cloud Storage ](https://docs.cloud.google.com/storage/docs)
  * [ Guides ](https://docs.cloud.google.com/storage/docs/discover-object-storage-console)



Send feedback 

#  Get a bucket's storage layout Stay organized with collections  Save and categorize content based on your preferences. 

This page describes how to determine the storage layout of your bucket. Storage layout refers to how objects are organized within a bucket, either in a flat namespace or a [hierarchical namespace](https://docs.cloud.google.com/storage/docs/hns-overview). The layout is important for applications that interact with the bucket, as object access and manipulation methods vary depending on the layout. Storage layout also includes information about the bucket's location.

By using the [`getStorageLayout`](https://docs.cloud.google.com/storage/docs/json_api/v1/buckets/getStorageLayout) API, your application can adapt its behavior based on whether a bucket uses hierarchical namespace or not, ensuring optimal compatibility and leveraging the appropriate features based on the bucket configuration.

#### Roles required

In order to get the required permissions for getting the storage layout of a Cloud Storage bucket , ask your administrator to grant you the Storage Object User (`roles/storage.objectUser`) role on the bucket.

The role contains the `storage.objects.list` permission, which is required to get the storage layout of the bucket.

You might also be able to get this permission with other [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or [predefined roles](https://docs.cloud.google.com/iam/docs/roles-permissions). To see which roles are associated with which permissions, refer to [IAM roles for Cloud Storage.](https://docs.cloud.google.com/storage/docs/access-control/iam-roles)

For instructions on granting roles on buckets, see [Use IAM with buckets.](https://docs.cloud.google.com/storage/docs/access-control/using-iam-permissions)

## Get a bucket's storage layout

### Command line

Use the [`gcloud storage buckets describe`](https://docs.cloud.google.com/sdk/gcloud/reference/storage/buckets/describe) command with the `--format` flag:
    
    
    gcloud storage buckets describe gs://BUCKET_NAME --raw --format="default(hierarchicalNamespace)"

Where:

  * `BUCKET_NAME` is the name of the relevant bucket. For example, `my-bucket`.



If successful and hierarchical namespace is enabled, the response looks similar to the following example:
    
    
      hierarchicalNamespace:
        enabled: true
    

### JSON API

  1. Have gcloud CLI [installed and initialized](https://docs.cloud.google.com/sdk/docs/install), which lets you generate an access token for the `Authorization` header.

  2. Use [`cURL`](http://curl.haxx.se/) to call the [JSON API](https://docs.cloud.google.com/storage/docs/json_api) with a [`getStorageLayout`](https://docs.cloud.google.com/storage/docs/json_api/v1/buckets/getStorageLayout) request:
         
         curl -X GET \
           -H "Authorization: Bearer $(gcloud auth print-access-token)" \
           "https://storage.googleapis.com/storage/v1/b/BUCKET_NAME/storageLayout"

Where `BUCKET_NAME` is the name of the relevant bucket. For example, `my-bucket`.

If successful, the response looks like the following example:
         
         {
               "kind": "storage#storageLayout",
               "bucket": "my-bucket",
               "location": "us-central1",
               "locationType": "region",
               "hierarchicalNamespace":{enabled: true},
           }




## What's next

  * [Understand folders](https://docs.cloud.google.com/storage/docs/folders-overview).
  * [Create and manage folders](https://docs.cloud.google.com/storage/docs/create-folders).
  * [Rename folders](https://docs.cloud.google.com/storage/docs/rename-hns-folders).



##  Try it for yourself 

If you're new to Google Cloud, create an account to evaluate how Cloud Storage performs in real-world scenarios. New customers also get $300 in free credits to run, test, and deploy workloads. 

[ Try Cloud Storage free ](https://console.cloud.google.com/freetrial)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-23 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-23 UTC."],[],[]] 
