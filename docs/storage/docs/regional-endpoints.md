---
url: https://docs.cloud.google.com/storage/docs/regional-endpoints/
title: Regional endpoints \u00a0|\u00a0 Cloud Storage \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T01:01:22.355893+00:00
---

# Regional endpoints  |  Cloud Storage  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/storage/docs/regional-endpoints/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Storage ](https://docs.cloud.google.com/docs/storage)
  * [ Cloud Storage ](https://docs.cloud.google.com/storage/docs)
  * [ Guides ](https://docs.cloud.google.com/storage/docs/discover-object-storage-console)



Send feedback 

#  Regional endpoints Stay organized with collections  Save and categorize content based on your preferences. 

This page describes how to use regional endpoints to access resources in Cloud Storage. Using regional endpoints lets you run your workloads in a manner that complies with [data residency](https://docs.cloud.google.com/assured-workloads/docs/data-residency) and data sovereignty requirements, where your request traffic is routed directly to the region specified in the endpoint.

## Overview

Regional endpoints are request endpoints that only allow requests to proceed if the affected resource exists in the location specified by the endpoint. For example, when you use the endpoint `https://storage.me-central2.rep.googleapis.com` in a delete bucket request, the request only proceeds if the bucket is located in `ME-CENTRAL2`.

Unlike global endpoints, where requests can be processed in a different location from where the resource resides, regional endpoints guarantee that your requests are processed only within the location specified by the endpoint where the resource resides. Regional endpoints terminate TLS sessions in the location specified by the endpoint for requests received from the Internet, other Google Cloud resources (such as Compute Engine virtual machines), on-premise services using VPN or Interconnect, and Virtual Private Clouds (VPCs).

Regional endpoints guarantee data residency by ensuring that your object's data at rest and in transit does not get moved out of the location specified by the endpoint. This guarantee excludes resource metadata, such as object names and bucket IAM policies. For more information, see [Note on service data](https://docs.cloud.google.com/assured-workloads/docs/data-residency#service-data).

## Supported locations

You can use regional endpoints to keep your data within the following [locations](https://docs.cloud.google.com/storage/docs/locations):

  * All regions

  * `US` multi-region

  * `EU` multi-region




## Supported operations

Regional endpoints can only be used to perform operations that access or mutate resources within the location specified by the endpoint. Regional endpoints cannot be used to perform operations that access or mutate resources outside of the location specified by the endpoint.

For example, when you use the regional endpoint `https://storage.me-central2.rep.googleapis.com`, you can read objects in buckets located in `ME-CENTRAL2`, and copy an object from a source bucket to a destination bucket only when both buckets are located in `ME-CENTRAL2`. If you attempt to read or copy an object outside of `ME-CENTRAL2`, you get an error.

Regional endpoints can be used to perform supported bucket, object, and inventory report operations, as long as the operations are performed on resources stored in the location specified by the endpoint.

For a full list of operations that are supported in Cloud Storage, expand the **Supported operations** section:

#### Supported operations

  * Object operations 
    * Creating objects
    * Composing objects
    * Copying objects1
    * Deleting objects
    * Getting object metadata2
    * Listing objects
    * Patching objects
    * Rewriting objects1
    * Updating objects
  * Bucket operations 
    * Creating buckets
    * Deleting buckets
    * Getting bucket metadata2
    * Listing buckets
    * Locking bucket retention policies
    * Patching buckets
    * Updating buckets
  * Operations on IAM policies 
    * Getting bucket IAM policies2
    * Updating bucket IAM policies2
    * Testing bucket IAM policies2
  * Operations on ACLs 
    * Creating object ACLs2
    * Creating default object ACLs for a bucket2
    * Deleting object ACLs2
    * Deleting default object ACLs for a bucket2
    * Getting object ACLs2
    * Getting default object ACLs for a bucket2
    * Listing object ACLs2
    * Listing default object ACLs for a bucket2
    * Patching object ACLs2
    * Patching default object ACLs for a bucket2
    * Updating object ACLs2
    * Updating default object ACLs for a bucket2
  * Storage Insights operations 
    * Creating inventory report configurations
    * Deleting inventory report configurations
    * Getting inventory reports
    * Getting inventory report configurations
    * Listing inventory reports
    * Listing inventory report configurations
    * Patching inventory report configurations



1This operation only succeeds if the source and destination buckets are in the location specified by the endpoint.

2This operation accesses or mutates metadata. Compliance with data residency and data sovereignty requirements are not guaranteed for this operation.

## Limitations and restrictions

Regional endpoints cannot be used to perform the following operations:

  * Copying or rewriting resources from one location to another

  * [HMAC key](https://docs.cloud.google.com/storage/docs/authentication/hmackeys) operations

  * [Service account](https://docs.cloud.google.com/storage/docs/projects#service-accounts) operations

  * [Pub/Sub notification](https://docs.cloud.google.com/storage/docs/pubsub-notifications) operations

  * [JSON batch](https://docs.cloud.google.com/storage/docs/batch) operations




Keep in mind the following restrictions when using regional endpoints:

  * Regional endpoints only support HTTPS. HTTP is not supported.

  * Operations using regional endpoints can only be performed using the Cloud Storage JSON and XML APIs. [gRPC](https://docs.cloud.google.com/storage/docs/enable-grpc-api) is not supported.




For more details, guidance, and restrictions on using regional endpoints to maintain compliance with the [International Traffic in Arms Regulations (ITAR)](https://www.pmddtc.state.gov/ddtc_public?id=ddtc_kb_article_page&sys_id=24d528fddbfc930044f9ff621f961987), see the [ITAR control package for Cloud Storage](https://docs.cloud.google.com/assured-workloads/docs/control-packages/itar#storage).

## Tools for using regional endpoints

### Console

To access Cloud Storage resources in a manner that's compliant with data residency or sovereignty requirements, use the jurisdictional Google Cloud console URLs:

Resource | URL  
---|---  
Bucket list for a project | `https://console.JURISDICTION.cloud.google.com/storage/browser?project=PROJECT_ID`  
Object list for a bucket | `https://console.JURISDICTION.cloud.google.com/storage/browser/BUCKET_NAME`  
Details for an object | `https://console.JURISDICTION.cloud.google.com/storage/browser/_details/BUCKET_NAME/OBJECT_NAME`  
  
Replace `JURISDICTION` with one of the following values:

  * `eu` if the resource is located in the European Union

  * `sa` if the resource is located in the Kingdom of Saudi Arabia

  * `us` if the resource is located in the United States


**Note:** You cannot use the jurisdictional Google Cloud console to upload or download objects.

### Command line

To configure the Google Cloud CLI for use with regional endpoints, complete the following steps:

  1. Make sure you're using the Google Cloud CLI version 402.0.0 or later.

  2. Set the `api_endpoint_overrides/storage` property to the regional endpoint you want to use:
         
         gcloud config set api_endpoint_overrides/storage https://storage.LOCATION.rep.googleapis.com/

Alternatively, you can set the `CLOUDSDK_API_ENDPOINT_OVERRIDES_STORAGE` environment variable to the endpoint:
         
         CLOUDSDK_API_ENDPOINT_OVERRIDES_STORAGE=https://storage.LOCATION.rep.googleapis.com/ gcloud ls gs://my-bucket




### REST APIs

### JSON API

When making requests to regional endpoints, use the following URIs:

  * For general JSON API requests, excluding object uploads, use the following endpoint, replacing LOCATION with a supported bucket location:
        
        https://storage.LOCATION.rep.googleapis.com

For example, the following endpoint is used to create a bucket in the `ME-CENTRAL2` region:
        
        https://storage.me-central2.rep.googleapis.com

  * For JSON API object uploads, use the following endpoint:
        
        https://storage.LOCATION.rep.googleapis.com/upload/storage/v1/b/BUCKET_NAME/o

Replace:

    * LOCATION with a supported bucket location.

    * BUCKET_NAME with the name of the bucket to which you want to upload an object.

For example, the following endpoint is used to upload an object to a bucket in the `ME-CENTRAL2` region:
    
    https://storage.me-central2.rep.googleapis.com/upload/storage/v1/b/my-example-bucket/o

  * For JSON API object downloads, use the following endpoint:
        
        https://storage.LOCATION.rep.googleapis.com/download/storage/v1/b/BUCKET_NAME/o/OBJECT_NAME?alt=media

Replace:

    * LOCATION with a supported bucket location.

    * BUCKET_NAME with the name of the bucket that contains the object you want to download.

    * OBJECT_NAME with the name of the object you want to download.




### XML API

When making requests to regional endpoints, use the path-style or virtual hosted-style endpoint:

  * Path-style endpoint: 
        
        https://storage.LOCATION.rep.googleapis.com/BUCKET_NAME/OBJECT_NAME

  * Virtual hosted-style endpoint: 
        
        https://BUCKET_NAME.storage.LOCATION.rep.googleapis.com/OBJECT_NAME

Replace:

    * LOCATION with a supported bucket location.

    * BUCKET_NAME with the name of a bucket.

    * OBJECT_NAME with the name of an object.




For example, the following sample can be used to upload an object to a bucket in the `ME-CENTRAL2` region:
    
    
    https://storage.me-central2.rep.googleapis.com/my-example-bucket/my-example-object

## Restricting global API endpoint usage

To help enforce the use of regional endpoints, you can use the `constraints/gcp.restrictEndpointUsage` organization policy constraint to block requests to the global API endpoint. For more information, see the [Restrict Endpoint Usage](https://docs.cloud.google.com/docs/security/compliance/restrict-endpoint-usage) documentation.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
