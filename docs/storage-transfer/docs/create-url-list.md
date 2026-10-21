---
url: https://docs.cloud.google.com/storage-transfer/docs/create-url-list/
title: Transfer from public URLs to Cloud Storage \u00a0|\u00a0 Storage Transfer Service \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T03:52:45.781053+00:00
---

# Transfer from public URLs to Cloud Storage  |  Storage Transfer Service  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/storage-transfer/docs/create-url-list/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Storage ](https://docs.cloud.google.com/docs/storage)
  * [ Storage Transfer Service ](https://docs.cloud.google.com/storage-transfer/docs/overview)



Send feedback 

#  Transfer from public URLs to Cloud Storage Stay organized with collections  Save and categorize content based on your preferences. 

Storage Transfer Service can copy files from a list of public URLs to your Cloud Storage bucket.

When creating a transfer, you provide a link to a tab-separated values (TSV) file containing the URLs and details of the objects to transfer. The TSV file can be hosted in any publicly-accessible HTTP or HTTPS location; or can be stored in a Cloud Storage bucket.

This page explains how to create a URL list and pass it to the job creation command.

## Source file requirements

  * URLs must be publicly-accessible and use HTTP or HTTPS protocols.
  * The server hosting each object: 
    * Must not deny access to the object with a `robots.txt`.
    * Supports `Range` requests.
    * Returns a `Content-Length` header in each response.



## URL list format

A URL list must adhere to the following requirements:

  * The file must be formatted as tab-separated values.
  * URLs must be in UTF-8 lexicographical order.
  * The first line must specify `TsvHttpData-1.0`.
  * After the first line, specify one object per row.
  * Each row must contain the URL, and may also contain the file size and the base64-encoded MD5 checksum of the object.



The following is a sample TSV file that specifies two objects to transfer. Note that on this page the tabs are rendered as spaces; for your own file, make sure to use tabs between fields.
    
    
    TsvHttpData-1.0
    https://example.com/myfile.pdf    1357    wHENa08V36iPYAsOa2JAdw==
    https://example2.com/images/dataset1/flower.png    2468    R9acAaveoPd2y8nniLUYbw==
    

Each line contains:

  * The HTTP or HTTPS URL of a source object.
  * (Optional) The size of the object in bytes.

Ensure that the specified size matches the actual size of the object when it is fetched. If the size of the object received by Cloud Storage does not match the size specified, the object transfer will fail.

  * (Optional) The base64-encoded MD5 checksum of the object.

Ensure that the specified MD5 checksum matches the MD5 checksum computed from the transferred bytes. If the MD5 checksum of the object received by Cloud Storage does not match the MD5 checksum specified, the object transfer will fail.

**Note:** Many checksumming tools output an object's MD5 checksum in base16-encoded format. Ensure the values provided are in base64-encoded format.



While the object size and MD5 checksum values are optional, we strongly recommend including them to help ensure data integrity.

## Hosting the URL list

The URL list can be hosted in one of two locations:

  * A publicly-accessible URL.
  * A Cloud Storage bucket, to which the service agent for Storage Transfer Service has been granted access.




###  Publicly-accessible URLs 

When storing the URL list at a publicly-accessible URL, the following requirements apply:

  * The URL must begin with `http://` or `https://`.
  * The server must set a strong `Etag` header in the HTTP response when it returns the URL list.



For example, you can store the list in a Cloud Storage bucket and [share the object publicly](https://docs.cloud.google.com/storage/docs/cloud-console#_sharingdata) to get a link to it.

###  Cloud Storage buckets 

To avoid storing your list in a public location, you can store it in a Cloud Storage bucket, and grant access to the service agent for Storage Transfer Service.

The service agent must be granted the following permissions:

  * The `storage.object.get` permission on the object. This can be granted by granting the `roles/storage.legacyObjectReader` role on the bucket, or with a custom role.
  * The `storage.buckets.get` permission on the bucket. This can be granted by granting the `roles/storage.legacyBucketReader` role, or with a custom role.



To grant permissions to the service agent:

#### Find the service agent's email

  1. Go to the [`googleServiceAccounts.get` reference page](https://docs.cloud.google.com/storage-transfer/docs/reference/rest/v1/googleServiceAccounts/get).

An interactive panel opens, titled **Try this method**.

  2. In the panel, under **Request parameters** , enter your project ID. The project you specify here must be the project you're using to manage Storage Transfer Service, which might be different from the URL list bucket's project.

  3. Click **Execute**.




Your service agent's email is returned as the value of `accountEmail` and uses the format `project-PROJECT_NUMBER@storage-transfer-service.iam.gserviceaccount.com`.

Copy this value.

#### Grant the required roles

To grant the `roles/storage.objectViewer` role and the `roles/storage.bucketViewer` role to the service agent on the bucket containing the URL list, follow the instructions in [Set and manage IAM policies on buckets](https://docs.cloud.google.com/storage/docs/access-control/using-iam-permissions).

The principal you are adding is the service agent's email address. If required, the principal identifier is `serviceAccount`. For example, `serviceAccount:project-PROJECT_NUMBER@storage-transfer-service.iam.gserviceaccount.com`.

## Create a URL list transfer job

To specify a URL list when creating a transfer job, follow these instructions:

###  Google Cloud console 

Follow the instructions in [Create a transfer job](https://docs.cloud.google.com/storage-transfer/docs/create-transfers#google-cloud-console).

When choosing a source:

  1. Under **Source type** , select **URL list** and click **Next step**.

  2. Under **URL of TSV file** , provide the URL to your tab-separated values (TSV) file. The URL is either an HTTP/HTTPS address (e.g. `https://example.com/urllist.tsv`) or a Cloud Storage path (e.g. `gs://my-bucket/urllist.tsv`).




###  gcloud CLI 

To create a new transfer job, use the `gcloud transfer jobs create` command.
    
    
    gcloud transfer jobs create \
      SOURCE DESTINATION
    

For URL list transfers, the value of SOURCE is the URL of the TSV file. The URL is either an HTTP/HTTPS address (e.g. `https://example.com/urllist.tsv`) or a Cloud Storage path (e.g. `gs://my-bucket/urllist.tsv`).

For more information on creating transfers using gcloud CLI, see [Create transfer jobs](https://docs.cloud.google.com/storage-transfer/docs/create-transfers#gcloud-cli).

###  REST 

To create a URL list transfer job using the REST API, specify the URL of the TSV file in the `listUrl` field:
    
    
    {
      "projectId": "PROJECT_ID",
      "transferSpec": {
        "httpDataSource": {
          "listUrl": "URL"
        },
        "gcsDataSink": {
          "bucketName": "DESTINATION_BUCKET"
        }
      },
      "status": "ENABLED"
    }
    

The value of URL is either an HTTP/HTTPS address (e.g. `https://example.com/urllist.tsv`) or a Cloud Storage path (e.g. `gs://my-bucket/urllist.tsv`).

For more details on creating transfers using the REST API, see the [REST API reference](https://docs.cloud.google.com/storage-transfer/docs/reference/rest/v1/transferJobs/create).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
