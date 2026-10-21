---
url: https://docs.cloud.google.com/storage/docs/using-long-running-operations/
title: Use long-running operations in Cloud Storage \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T01:01:00.114381+00:00
---

# Use long-running operations in Cloud Storage  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/storage/docs/using-long-running-operations/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Storage ](https://docs.cloud.google.com/docs/storage)
  * [ Cloud Storage ](https://docs.cloud.google.com/storage/docs)
  * [ Guides ](https://docs.cloud.google.com/storage/docs/discover-object-storage-console)



Send feedback 

#  Use long-running operations in Cloud Storage Stay organized with collections  Save and categorize content based on your preferences. 

This page describes how to use [long-running operations](https://google.aip.dev/151) that get initiated from using method calls in Cloud Storage. For detailed information about the semantics of a long-running operation that gets returned from a specific method call, see the feature-specific documentation.

## Get required roles

To get the permissions that you need to manage long-running operations in Cloud Storage, ask your administrator to grant you the Storage Admin (`roles/storage.admin`) role or the Storage Legacy Bucket Owner (`roles/storage.legacyBucketOwner`) role on the bucket or the project used to perform the underlying operation.

These predefined roles contain the following permissions, which are required to manage long-running operations in Cloud Storage:

  * `storage.bucketOperations.cancel`
  * `storage.bucketOperations.get`
  * `storage.bucketOperations.list`
  * `storage.buckets.list` (this permission is required only when using the Google Cloud console)

**Note:** The user who initiates a long-running operation can always get the details of the long-running operation, regardless of whether or not they have the `storage.bucketOperations.get` IAM permission. Users who did not initiate the long-running operation must have the `storage.bucketOperations.get` in order to get the details of the long-running operation. The `storage.bucketOperations.list` and `storage.bucketOperations.cancel` permissions are always required in order to list and cancel long-running operations.

For information about granting roles on buckets, see [Set and manage IAM policies on buckets](https://docs.cloud.google.com/storage/docs/access-control/using-iam-permissions). For information about granting roles on projects, see [Manage access](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access).

## Get the details of a long-running operation

### Console

  1. In the Google Cloud console, go to the Cloud Storage **Buckets** page.  


[Go to Buckets](https://console.cloud.google.com/storage/browser)

  2. In the bucket list, click the name of the bucket associated with the long-running operation.

  3. Click the **Operations** tab.




### Command line

**Note:** The Google Cloud CLI automatically specifies a default project, which can be controlled using the `--project` flag.

To get the details or check the status of a long-running operation, use the [`gcloud storage operations describe`](https://docs.cloud.google.com/sdk/gcloud/reference/storage/operations/describe) command:
    
    
    gcloud storage operations describe projects/_/buckets/BUCKET_NAME/operations/OPERATION_ID

Replace:

  * `BUCKET_NAME` with the name of the bucket that contains the long-running operation. For example, `my-bucket`.

  * `OPERATION_ID` with the ID of the long-running operation, which is returned in the response of methods you call. For example, the following response is returned from calling `gcloud storage restore` and the long-running operation ID is `BcazhBlHv2uZwnlh1UdamOfKbpVpb67drEwVoI2hlkE1e0eaXqw7fPBWP0802TJry4pInGC4h3wxtOi31RmpCC_lvnSocj_-jP`:
        
        Created: projects/_/buckets/my-bucket/operations/BcazhBlHv2uZwnlh1UdamOfKbpVpb67drEwVoI2hlkE1e0eaXqw7fPBWP0802TJry4pInGC4h3wxtOi31RmpCC_lvnSocj_-jP




### REST APIs

### JSON API

  1. Have gcloud CLI [installed and initialized](https://docs.cloud.google.com/sdk/docs/install), which lets you generate an access token for the `Authorization` header.

  2. Use [`cURL`](http://curl.haxx.se/) to call the [JSON API](https://docs.cloud.google.com/storage/docs/json_api) with an [`operations.get`](https://docs.cloud.google.com/storage/docs/json_api/v1/operations/get) request:
         
         curl -X GET -H "Authorization: Bearer $(gcloud auth print-access-token)" \
         "https://storage.googleapis.com/storage/v1/b/BUCKET_NAME/operations/OPERATION_ID"

Replace:

     * `BUCKET_NAME` with the name of the bucket associated with the long-running operation.

     * `OPERATION_ID` with the ID of the long-running operation, which is returned in the response of methods you call. For example, the following response is returned from calling [`gcloud storage restore`](https://docs.cloud.google.com/sdk/gcloud/reference/storage/restore) and the long-running operation ID is `BcazhBlHv2uZwnlh1UdamOfKbpVpb67drEwVoI2hlkE1e0eaXqw7fPBWP0802TJry4pInGC4h3wxtOi31RmpCC_lvnSocj_-jP`:
           
           Created: projects/_/buckets/my-bucket/operations/BcazhBlHv2uZwnlh1UdamOfKbpVpb67drEwVoI2hlkE1e0eaXqw7fPBWP0802TJry4pInGC4h3wxtOi31RmpCC_lvnSocj_-jP




If the request is successful, an [`operations` resource](https://docs.cloud.google.com/storage/docs/json_api/v1/operations) is returned:
    
    
    {
      "kind": "storage#operation",
      "name": "projects/_/buckets/bucket/operations/operation_id",
      "metadata": {
        "@type": OperationMetadataType*,
        metadata OperationMetadata*
      },
      "done": boolean,
      "response": {
        "@type": ResponseResourceType*,
        response ResponseResource*
      }
    }

## List the long-running operations in a bucket

### Console

  1. In the Google Cloud console, go to the Cloud Storage **Buckets** page.  


[Go to Buckets](https://console.cloud.google.com/storage/browser)

  2. In the bucket list, click the name of the bucket.

  3. Click the **Operations** tab.




### Command line

To list the long-running operations in a bucket, use the [`gcloud storage operations list`](https://docs.cloud.google.com/sdk/gcloud/reference/storage/operations/list) command:
    
    
    gcloud storage operations list gs://BUCKET_NAME

Replace:

  * `BUCKET_NAME` with the name of the bucket that contains the long-running operations. For example, `my-bucket`.



### REST APIs

### JSON API

  1. Have gcloud CLI [installed and initialized](https://docs.cloud.google.com/sdk/docs/install), which lets you generate an access token for the `Authorization` header.

  2. Use [`cURL`](http://curl.haxx.se/) to call the [JSON API](https://docs.cloud.google.com/storage/docs/json_api) with an [`operations.get`](https://docs.cloud.google.com/storage/docs/json_api/v1/operations/list) request:
         
         curl -X GET -H "Authorization: Bearer $(gcloud auth print-access-token)" \
         "https://storage.googleapis.com/storage/v1/b/BUCKET_NAME/operations"

Replace:

     * `BUCKET_NAME` with the name of the bucket associated with the long-running operations you want to list.



If the request is successful, you get a response similar to the following:
    
    
    {
      "kind": "storage#operations",
      "nextPageToken": string,
      "operations": [
        operations Resource
      ]
    }

## Cancel a long-running operation

**Note:** Cancelling a long-running operation is asynchronous and done at best-effort. A cancel request on a running long-running operation sets the `requested cancellation` field, but there's no guarantee that the request will be honored.

### Console

  1. In the Google Cloud console, go to the Cloud Storage **Buckets** page.  


[Go to Buckets](https://console.cloud.google.com/storage/browser)

  2. In the bucket list, click the name of the bucket associated with the long-running operation that you want to cancel.

  3. Click the **Operations** tab.

  4. In the row for the long-running operation, click more_vert**More options** , and then click **Cancel**.




### Command line

**Note:** The Google Cloud CLI automatically specifies a default project, which can be controlled using the `--project` flag.

To cancel a long-running operation, use the [`gcloud storage operations cancel`](https://docs.cloud.google.com/sdk/gcloud/reference/storage/operations/cancel) command:
    
    
    gcloud storage operations cancel projects/_/buckets/BUCKET_NAME/operations/OPERATION_ID

Replace:

  * `BUCKET_NAME` with the name of the bucket that contains the long-running operation. For example, `my-bucket`.

  * `OPERATION_ID` with the ID of the long-running operation, which is returned in the response of methods you call. For example, the following response is returned from calling [`gcloud storage restore`](https://docs.cloud.google.com/sdk/gcloud/reference/storage/restore) and the long-running operation ID is `BcazhBlHv2uZwnlh1UdamOfKbpVpb67drEwVoI2hlkE1e0eaXqw7fPBWP0802TJry4pInGC4h3wxtOi31RmpCC_lvnSocj_-jP`:
        
        Created: projects/_/buckets/my-bucket/operations/BcazhBlHv2uZwnlh1UdamOfKbpVpb67drEwVoI2hlkE1e0eaXqw7fPBWP0802TJry4pInGC4h3wxtOi31RmpCC_lvnSocj_-jP




### REST APIs

### JSON API

  1. Have gcloud CLI [installed and initialized](https://docs.cloud.google.com/sdk/docs/install), which lets you generate an access token for the `Authorization` header.

  2. Use [`cURL`](http://curl.haxx.se/) to call the [JSON API](https://docs.cloud.google.com/storage/docs/json_api) with an [`operations.post`](https://docs.cloud.google.com/storage/docs/json_api/v1/operations/cancel) request:
         
         curl -X POST -H "Authorization: Bearer $(gcloud auth print-access-token)" \
         "https://storage.googleapis.com/storage/v1/b/BUCKET_NAME/operations/OPERATION_ID/cancel"

Replace:

     * `BUCKET_NAME` with the name of the bucket associated with the long-running operation you want to cancel.

     * `OPERATION_ID` with the ID of the long-running operation, which is returned in the response of methods you call. For example, the following response is returned from calling [`gcloud storage restore`](https://docs.cloud.google.com/sdk/gcloud/reference/storage/restore) and the long-running operation ID is `BcazhBlHv2uZwnlh1UdamOfKbpVpb67drEwVoI2hlkE1e0eaXqw7fPBWP0802TJry4pInGC4h3wxtOi31RmpCC_lvnSocj_-jP`:
           
           Created: projects/_/buckets/my-bucket/operations/BcazhBlHv2uZwnlh1UdamOfKbpVpb67drEwVoI2hlkE1e0eaXqw7fPBWP0802TJry4pInGC4h3wxtOi31RmpCC_lvnSocj_-jP




## Metadata

Long-running operations have metadata associated with them. The following metadata identify properties of a long-running operation:

  * Create time: The time the long-running operation was created.

  * End time: The time the long-running operation finished running.

  * Update time: The time the long-running operation was last modified.

  * Type: The API call that initiated the long-running operation.

  * Requested cancellation: Indicates whether the user has requested cancellation of the long-running operation.

  * Progress percent: The estimated progress of the long-running operation, in percentage. A value of `-1` means the progress is unknown.




In the Google Cloud console, the progress percent and requested cancellation metadata are displayed in a combined **Status** field.

## Error handling

Long-running operations are initiated from asynchronous APIs and require different error handling practices than synchronous APIs. Unlike synchronous APIs, the response to asynchronous API calls can indicate success even if the long-running operation eventually fails. Instead of relying on the status code that gets returned in the response headers, you should parse the long-running operation metadata in the body of the response to determine whether an API call was successful.

For example, if you make a soft delete bulk restore request, it returns a successful HTTP status code (`200 OK`) even if an error occurs over the course of the operation. To check whether the bulk restore operation was successful, get the status of the long-running operation.

Note that the long-running operation APIs (Get, List, Cancel) are synchronous and return normal errors.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
