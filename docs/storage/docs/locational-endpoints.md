---
url: https://docs.cloud.google.com/storage/docs/locational-endpoints/
title: Locational endpoints \u00a0|\u00a0 Cloud Storage \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T10:28:49.601558+00:00
---

# Locational endpoints  |  Cloud Storage  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/storage/docs/locational-endpoints/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Storage ](https://docs.cloud.google.com/docs/storage)
  * [ Cloud Storage ](https://docs.cloud.google.com/storage/docs)
  * [ Guides ](https://docs.cloud.google.com/storage/docs/discover-object-storage-console)



Send feedback 

#  Locational endpoints Stay organized with collections  Save and categorize content based on your preferences. 

This page describes how to use locational endpoints to access Cloud Storage. Using locational endpoints helps you make sure that your at-rest data stays within jurisdiction to meet [data residency](https://docs.cloud.google.com/assured-workloads/docs/data-residency) requirements.

**Note:** Locational endpoints can be used to access Cloud Storage in a manner that's compliant with the [International Traffic in Arms Regulations (ITAR)](https://www.pmddtc.state.gov/ddtc_public?id=ddtc_kb_article_page&sys_id=24d528fddbfc930044f9ff621f961987) under a shared responsibility model. To maintain compliance, you must understand and operate within the limitations and responsibilities listed in this page. [Regional endpoints](https://docs.cloud.google.com/storage/docs/regional-endpoints) are designed to prevent accidental out-of-region routing and are the preferred method for meeting ITAR compliance. We recommend that you use regional endpoints if possible.

## Overview

Locational endpoints are [request endpoints](https://docs.cloud.google.com/storage/docs/request-endpoints) that only allow requests to proceed if the affected resource exists in the location specified by the endpoint. For example, when you use the endpoint `https://us-central1-storage.googleapis.com` in a delete bucket request, the request only proceeds if the bucket is located in `US-CENTRAL1`.

Unlike global endpoints, where requests can be processed in a different location from where the resource resides, locational endpoints guarantee that your requests are processed only within the location specified by the endpoint, where the resource resides.

**Note:** Cloud Load Balancing uses [global request endpoints](https://docs.cloud.google.com/storage/docs/request-endpoints) when routing requests to Cloud Storage buckets. You cannot configure Cloud Load Balancing to use locational endpoints.

Using locational endpoints guarantees that:

  * Your data stored in Cloud Storage does not leave the specified location.

  * Your data is TLS terminated in the region specified by the endpoint when transiting from on-premises to Google Cloud.




When using locational endpoints, you assume the following responsibilities:

  * In order to get data residency guarantees, requests made to a locational endpoint must originate from the same location that's specified by the endpoint. For example, if you're using a Compute Engine virtual machine to perform a request to a bucket residing in `US-CENTRAL1` via the `us-central1-storage.googleapis.com` endpoint, the virtual machine must also reside in `US-CENTRAL1`.

  * Locational endpoints must only be used when performing supported operations. Performing unsupported operations result in an error.




Locational endpoints support traffic between on-premises to Google Cloud via Interconnect or VPN, and traffic between Google Cloud services (for example, from BigQuery to Cloud Storage). Internet traffic is not supported.

## Supported operations

The following table summarizes the operations that can and cannot be performed with locational endpoints. In general, intra-location operations can be performed with locational endpoints, while cross-location operations cannot.

If you attempt to perform an unsupported operation using a locational endpoint, Cloud Storage returns a 400 HTTP error code with the message: "This endpoint does not implement this operation. Please use the global endpoint."

Operation | Mutates object data | Supported for usage with locational endpoints  
---|---|---  
objects compose | Yes | Yes1  
objects delete | No | Yes1  
objects get | Yes | Yes1  
objects insert | Yes | Yes1  
objects list | No | Yes1  
objects patch | No | Yes1  
objects copy | Yes | Yes4  
objects rewrite | Yes | Yes4  
buckets insert | No | Yes2  
buckets delete | No | Yes3  
buckets get | No | Yes2  
buckets patch | No | Yes2  
buckets update | No | Yes2  
buckets getIamPolicy | No | Yes2  
buckets setIamPolicy | No | Yes2  
buckets testIamPermissions | No | Yes2  
buckets lockRetentionPolicy | No | Yes2  
buckets BucketAccessControls | No | Yes2  
buckets DefaultObjectAccessControls | No | Yes2  
buckets ObjectAccessControls | No | Yes2  
[HMAC key operations](https://docs.cloud.google.com/storage/docs/json_api/v1/projects/hmacKeys) | No | No  
[Service account operations](https://docs.cloud.google.com/storage/docs/json_api/v1/projects/serviceAccount) | No | No  
[Pub/Sub notification operations](https://docs.cloud.google.com/storage/docs/json_api/v1#notifications) | Varies by operation | No  
[Batched operations](https://docs.cloud.google.com/storage/docs/batch) | Varies by operation | No  
  
1 To perform this operation using locational endpoints, the bucket containing the affected object must exist in the location specified by the endpoint. For example: an object delete request to `us-central1-storage.googleapis.com` can only be used to delete objects in buckets that reside in the `US-CENTRAL1` region. If you try to delete an object in a location that's not `US-CENTRAL1`, the operation returns a `NOT_FOUND` error.

2 To perform this operation using locational endpoints, the bucket must exist in the location specified by the endpoint. For example: a bucket create request to `us-central1-storage.googleapis.com` can only be used to create a bucket in the `US-CENTRAL1` region. If you try to create the bucket in a location that's not `US-CENTRAL1`, the operation returns an `INVALID_ARGUMENT` error.

3 To perform this operation using locational endpoints, the bucket must exist in the location specified by the endpoint. For example: a bucket delete request to `us-central1-storage.googleapis.com` can only be used to delete a bucket in the `US-CENTRAL1` region. If you try to delete a bucket in a location that's not `US-CENTRAL1`, the operation returns a `NOT_FOUND` error.

4 To perform this operation using locational endpoints, the source and destination buckets must both exist in the location specified by the endpoint. For example: you can use locational endpoints to copy an object from one bucket to another if both buckets exist in the same location. However, you cannot use locational endpoints to copy an object from one bucket to another if the buckets exist in different locations. If the source or destination bucket exists in a different location than the location specified by the endpoint, the operation returns a `NOT_FOUND` error.

## Supported regions

Locational endpoints are supported for all US regions, the `US` multi-region, and the `NAM4` predefined dual-region. For more information about what regions can be specified, see [Bucket locations](https://docs.cloud.google.com/storage/docs/locations).

## Making requests

### Console

To maintain ITAR compliance, it is your responsibility to use the Jurisdictional Google Cloud console. For more information, see the [ITAR control package for Cloud Storage](https://docs.cloud.google.com/assured-workloads/docs/control-packages/itar#storage).

### Command line

To configure the Google Cloud CLI for use with locational endpoints:

  1. Set the `api_endpoint_overrides/storage` property to the locational endpoint you want to use:
         
         gcloud config set api_endpoint_overrides/storage https://LOCATION-storage.googleapis.com/




Once this property is set, you can use gcloud CLI commands as you normally would.

Alternatively, you can use locational endpoints for individual commands by setting the `CLOUDSDK_API_ENDPOINT_OVERRIDES_STORAGE` environment variable in each command. For example:
    
    
    CLOUDSDK_API_ENDPOINT_OVERRIDES_STORAGE=https://LOCATION-storage.googleapis.com/ gcloud ls gs://my-bucket

### Client libraries

Cloud Storage client libraries manage request endpoints automatically, but you can manually set locational endpoints. To learn how to set locational endpoints, see the [client library code samples using request endpoints](https://docs.cloud.google.com/storage/docs/request-endpoints#client-libraries).

### REST APIs

### JSON API

When making requests to locational endpoints, use the following URIs:

  * For general JSON API requests, excluding object uploads, use the following endpoint:
        
        https://LOCATION-storage.googleapis.com

Replace LOCATION with a supported bucket location. For example, `us-central1`.

  * For JSON API object uploads, use the following endpoint:
        
        https://LOCATION-storage.googleapis.com/upload/storage/v1/b/BUCKET_NAME/o

Replace:

    * LOCATION with a supported bucket location. For example, `us-central1`.

    * BUCKET_NAME with the name of the bucket to which you want to upload an object. For example, `my-example-bucket`.

  * For JSON API object downloads, use the following endpoint:
        
        https://LOCATION-storage.googleapis.com/download/storage/v1/b/BUCKET_NAME/o/OBJECT_NAME?alt=media

Replace:

    * LOCATION with a supported bucket location. For example, `us-central1`.

    * BUCKET_NAME with the name of the bucket that contains the object you want to download. For example, `my-example-bucket`.

    * OBJECT_NAME with the name of the object you want to download. For example, `waterfall.png`.




Note that the JSON API endpoints only support HTTPS requests.

### XML API

When using the XML API to make requests to locational endpoints, you can use a virtual hosted style endpoint or a path-style endpoint:

  * Virtual hosted style endpoint:
        
        https://BUCKET_NAME.LOCATION-storage.googleapis.com

  * Path-style endpoint:
        
        https://LOCATION-storage.googleapis.com/BUCKET_NAME




For both endpoint types, replace:

  * LOCATION with a supported bucket location. For example, `us-central1`.

  * BUCKET_NAME with a valid bucket name. For example, `my-example-bucket`.


**Note:** Virtual hosted-style endpoints cannot be used to access domain-named buckets. Use either path-style endpoints or a redirect instead.

The XML API endpoints support secure sockets layer (SSL) encryption, which means you can use either HTTP or HTTPS. Using HTTPS is recommended, especially if you authenticate to Cloud Storage using OAuth 2.0.

### Properly format requests

To ensure that your requests are compatible across Cloud Storage tools:

  * Ensure that you [properly encode special characters](https://docs.cloud.google.com/storage/docs/request-endpoints#encoding) that appear in the object name or query string of a request URI.

  * Familiarize yourself with [bucket naming](https://docs.cloud.google.com/storage/docs/buckets#naming) and [object naming considerations](https://docs.cloud.google.com/storage/docs/objects#naming).




## Known constraints

There is no support for [mTLS endpoints](https://docs.cloud.google.com/storage/docs/request-endpoints#mtls).

## Restricting global API endpoint usage

To help enforce the use of locational endpoints, you can use the `constraints/gcp.restrictEndpointUsage` organization policy constraint to block requests to the global API endpoint. For more information, see the [Restrict Endpoint Usage](https://docs.cloud.google.com/docs/security/compliance/restrict-endpoint-usage) documentation.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-21 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-21 UTC."],[],[]] 
