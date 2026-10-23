---
url: https://docs.cloud.google.com/storage/docs/interoperability/
title: Interoperability with other storage providers \u00a0|\u00a0 Cloud Storage \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T09:36:28.984059+00:00
---

# Interoperability with other storage providers  |  Cloud Storage  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/storage/docs/interoperability/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Storage ](https://docs.cloud.google.com/docs/storage)
  * [ Cloud Storage ](https://docs.cloud.google.com/storage/docs)
  * [ Guides ](https://docs.cloud.google.com/storage/docs/discover-object-storage-console)



Send feedback 

#  Interoperability with other storage providers Stay organized with collections  Save and categorize content based on your preferences. 

Cloud Storage is compatible with some other object storage platforms so you can seamlessly integrate data from different sources. This page describes Cloud Storage tools you can use to manage your cross-platform object data.

## XML API

The Cloud Storage [XML API](https://docs.cloud.google.com/storage/docs/xml-api/overview) is interoperable with some tools and libraries that work with services such as Amazon Simple Storage Service (Amazon S3). To use these tools and libraries with Cloud Storage, change the [request endpoint](https://docs.cloud.google.com/storage/docs/request-endpoints) that the tool or library uses to the Cloud Storage URI `https://storage.googleapis.com`, and then configure the tool or library to use your Cloud Storage [HMAC keys](https://docs.cloud.google.com/storage/docs/authentication/hmackeys). See [Simple migration from Amazon Simple Storage Service (Amazon S3)](https://docs.cloud.google.com/storage/docs/aws-simple-migration) for detailed instructions on getting started.

### Authenticate with the V4 signing process

The V4 signing process lets you make signed header requests to the Cloud Storage XML API. After creating a signature using the V4 signing process, you include the signature in the `Authorization` header of a subsequent request, which provides authentication. You can create a signature using an RSA signature or your Amazon S3 workflow and HMAC credentials. For more details about authenticating requests, see [Signatures](https://docs.cloud.google.com/storage/docs/authentication/signatures).

## Google Cloud CLI

The gcloud CLI is the preferred command line tool for accessing Cloud Storage. It also lets you access and work with other cloud storage services that use HMAC authentication, like Amazon S3. After you add your Amazon S3 credentials to ~/.aws/credentials, you can start using `gcloud storage` commands to manage objects in your Amazon S3 buckets. For example:

  * The following command lists the objects in the Amazon S3 bucket `my-aws-bucket`:
        
        gcloud storage ls s3://my-aws-bucket

  * The following command synchronizes data between an Amazon S3 bucket and a Cloud Storage bucket:
        
        gcloud storage rsync s3://my-aws-bucket gs://example-bucket --delete-unmatched-destination-objects --recursive




For more information, including details on how to optimize this synchronization, see the [`gcloud storage rsync` documentation](https://docs.cloud.google.com/sdk/gcloud/reference/storage/rsync).

#### **Invalid certificate** from Amazon S3 bucket names containing dots

If you attempt to use the gcloud CLI to access an Amazon S3 bucket that contains a dot in its name, you might receive an `invalid certificate` error. This is because Amazon S3 does not support virtual-hosted bucket URLs with dots in their name. When working with Amazon S3 resources, you can configure the gcloud CLI to attempt to use path-style bucket URLs by setting the `storage/s3_endpoint_url` property to be the following:
    
    
    storage/s3_endpoint_url https://s3.REGION_CODE.amazonaws.com

Where `REGION_CODE` is the region containing the bucket you are requesting. For example, `us-east-2`.

You can modify the `storage/s3_endpoint_url` property in one of the following ways:

  * Using the [`gcloud config set` command](https://docs.cloud.google.com/sdk/gcloud/reference/config/set), which applies the property to all gcloud CLI commands.

  * Creating a [named configuration](https://docs.cloud.google.com/sdk/gcloud/reference/topic/configurations) and applying it on a per-command basis using the [`--configuration` project-wide flag](https://docs.cloud.google.com/sdk/gcloud/reference#--configuration).




## Importing data with Storage Transfer Service

[Storage Transfer Service](https://docs.cloud.google.com/storage-transfer/docs/overview) lets you import large amounts of online data into Cloud Storage from Amazon S3 buckets, Microsoft Azure Blob Storage containers, and general HTTP/HTTPS locations. Storage Transfer Service can be used to schedule recurring transfers, delete source objects, and select which objects are transferred.

Additionally, if you use Amazon S3 Event Notifications, you can set up Storage Transfer Service [event-driven transfers](https://docs.cloud.google.com/storage-transfer/docs/event-driven-transfers) to listen for such notifications and automatically keep a Cloud Storage bucket in sync with a Amazon S3 source.

## What's next

  * Quickly complete a [simple migration from Amazon S3 to Cloud Storage](https://docs.cloud.google.com/storage/docs/aws-simple-migration).
  * [Create a signature](https://docs.cloud.google.com/storage/docs/authentication/signatures) for authenticating requests.



_Amazon Simple Storage Service ™ and Amazon S3™ are trademarks of Amazon.com, Inc. or its affiliates in the United States and/or other countries._

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
