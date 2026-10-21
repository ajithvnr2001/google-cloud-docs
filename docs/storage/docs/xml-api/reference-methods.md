---
url: https://docs.cloud.google.com/storage/docs/xml-api/reference-methods/
title: Overview of request methods for the XML API \u00a0|\u00a0 Cloud Storage \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T02:50:05.006173+00:00
---

# Overview of request methods for the XML API  |  Cloud Storage  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/storage/docs/xml-api/reference-methods/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Storage ](https://docs.cloud.google.com/docs/storage)
  * [ Cloud Storage ](https://docs.cloud.google.com/storage/docs)
  * [ Reference ](https://docs.cloud.google.com/storage/docs/apis)



Send feedback 

#  Overview of request methods for the XML API Stay organized with collections  Save and categorize content based on your preferences. 

The Cloud Storage XML API supports several standard HTTP request methods. Each method can use numerous request headers and response headers. The XML API documentation describes all of the supported HTTP methods as well as the most frequently used headers for each method.

Some methods are used to work with both data and metadata depending on context. For example, you can use one PUT Bucket request to create a bucket followed by a second PUT Bucket request to configure logging for the bucket.

The following list shows which XML API method you use to accomplish bucket and object tasks.

  * [GET Service](https://docs.cloud.google.com/storage/docs/xml-api/get-service)
    * List Buckets in the project
  * [DELETE Bucket](https://docs.cloud.google.com/storage/docs/xml-api/delete-bucket)
    * Delete a Bucket
  * [GET Bucket](https://docs.cloud.google.com/storage/docs/xml-api/get-bucket)
    * [List Objects in a Bucket](https://docs.cloud.google.com/storage/docs/xml-api/get-bucket-list)
    * [List Multipart Uploads in a Bucket](https://docs.cloud.google.com/storage/docs/xml-api/get-bucket-uploads)
    * [Get Bucket ACLs](https://docs.cloud.google.com/storage/docs/xml-api/get-bucket-acls)
    * [Get Bucket Metadata](https://docs.cloud.google.com/storage/docs/xml-api/get-bucket-metadata)
  * [HEAD Bucket](https://docs.cloud.google.com/storage/docs/xml-api/head-bucket)
    * Checks bucket existence
  * [POST Bucket](https://docs.cloud.google.com/storage/docs/xml-api/post-bucket)
    * Delete multiple objects
  * [PUT Bucket](https://docs.cloud.google.com/storage/docs/xml-api/put-bucket)
    * [Creates a Bucket](https://docs.cloud.google.com/storage/docs/xml-api/put-bucket-create)
    * [Set Bucket ACLs](https://docs.cloud.google.com/storage/docs/xml-api/put-bucket-acls)
    * [Set Bucket Metadata](https://docs.cloud.google.com/storage/docs/xml-api/put-bucket-metadata)
  * DELETE Object 
    * [Delete an object](https://docs.cloud.google.com/storage/docs/xml-api/delete-object)
    * [Abort a multipart upload](https://docs.cloud.google.com/storage/docs/xml-api/delete-multipart)
  * [GET Object](https://docs.cloud.google.com/storage/docs/xml-api/get-object)
    * [Download an Object](https://docs.cloud.google.com/storage/docs/xml-api/get-object-download)
    * [List Object Parts](https://docs.cloud.google.com/storage/docs/xml-api/get-object-multipart)
    * [List Object ACLs](https://docs.cloud.google.com/storage/docs/xml-api/get-object-acls)
    * [Get Object Encryption](https://docs.cloud.google.com/storage/docs/xml-api/get-object-encryption)
    * [Get Object Retention](https://docs.cloud.google.com/storage/docs/xml-api/get-object-retention)
  * [HEAD Object](https://docs.cloud.google.com/storage/docs/xml-api/head-object)
    * Gets Object Metadata
  * [POST Object](https://docs.cloud.google.com/storage/docs/xml-api/post-object)
    * [Initiate a Resumable Upload](https://docs.cloud.google.com/storage/docs/xml-api/post-object-resumable)
    * [Initiate a Multipart Upload](https://docs.cloud.google.com/storage/docs/xml-api/post-object-multipart)
    * [Complete a Multipart Upload](https://docs.cloud.google.com/storage/docs/xml-api/post-object-complete)
    * [Upload an Object with a Form](https://docs.cloud.google.com/storage/docs/xml-api/post-object-forms)
  * [PUT Object](https://docs.cloud.google.com/storage/docs/xml-api/put-object)
    * [Upload an Object](https://docs.cloud.google.com/storage/docs/xml-api/put-object-upload)
    * [Upload an Object Part](https://docs.cloud.google.com/storage/docs/xml-api/put-object-multipart)
    * [Copy an Object](https://docs.cloud.google.com/storage/docs/xml-api/put-object-copy)
    * [Compose an Object](https://docs.cloud.google.com/storage/docs/xml-api/put-object-compose)
    * [Set Object ACLs](https://docs.cloud.google.com/storage/docs/xml-api/put-object-acls)
    * [Set Object Retention](https://docs.cloud.google.com/storage/docs/xml-api/put-object-retention)
  * [GET HMAC Key](https://docs.cloud.google.com/storage/docs/xml-api/get-hmac-list)
  * [POST HMAC Key](https://docs.cloud.google.com/storage/docs/xml-api/post-hmac-key)
    * [Create an HMAC key](https://docs.cloud.google.com/storage/docs/xml-api/post-hmac-create)
    * [Update an HMAC key](https://docs.cloud.google.com/storage/docs/xml-api/post-hmac-update)
    * [Delete an HMAC key](https://docs.cloud.google.com/storage/docs/xml-api/post-hmac-delete)



## Conventions used

Conventions used in the XML API documentation:

  * The `Authorization` header is represented as `<authentication string>`. If you are using the XML API to migrate from another storage provider, then the `Authorization` has the format discussed in [Authentication in a Simple Migration Scenario](https://docs.cloud.google.com/storage/docs/aws-simple-migration#authentication). Otherwise, the `Authorization` header has the format discussed in [OAuth 2.0 Authentication](https://docs.cloud.google.com/storage/docs/migrating#fully-migrate).

If you don't provide authorization information when required to perform a request, the Cloud Storage issues a 401 unauthorized error. For more information, see [Status Codes](https://docs.cloud.google.com/storage/docs/xml-api/reference-status).

  * The `Host` header used in the XML API documentation is of the form: 
        
        Host: BUCKET-NAME.storage.googleapis.com

where the bucket name is specified as part of the hostname. In all operations except GET service, you can also specify the bucket as part of the URL path. For more information, see [Request Endpoints](https://docs.cloud.google.com/storage/docs/request-endpoints).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
