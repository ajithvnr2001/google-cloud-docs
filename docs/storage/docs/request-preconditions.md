---
url: https://docs.cloud.google.com/storage/docs/request-preconditions/
title: Request preconditions \u00a0|\u00a0 Cloud Storage \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T01:01:14.547728+00:00
---

# Request preconditions  |  Cloud Storage  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/storage/docs/request-preconditions/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Storage ](https://docs.cloud.google.com/docs/storage)
  * [ Cloud Storage ](https://docs.cloud.google.com/storage/docs)
  * [ Guides ](https://docs.cloud.google.com/storage/docs/discover-object-storage-console)



Send feedback 

#  Request preconditions Stay organized with collections  Save and categorize content based on your preferences. 

This page discusses _request preconditions_ , which you use to prevent requests from applying to a resource when the resource is in an unexpected state.

## Introduction

When preconditions are used in a request to Cloud Storage, the request only proceeds if the targeted resource meets the criteria defined in the preconditions. Precondition checks ensure that a bucket or object is in the expected state, allowing you to perform safe read-modify-write updates and conditional operations.

Preconditions are often used to prevent [race conditions](https://en.wikipedia.org/wiki/Race_condition#File_systems) in mutating requests, such as uploads, deletes, or metadata updates. Race conditions can arise when the same request is sent repeatedly or when independent processes each attempt to modify the same resource. See Examples of race conditions and data corruption for more information. Preconditions are also often used when retrieving object metadata and data in successive requests, to ensure the object did not change in the time between the two requests.

### Precondition criteria

Cloud Storage supports using several different immutable resource properties in preconditions:

  * [Generation and metageneration numbers](https://docs.cloud.google.com/storage/docs/metadata#generation-number)
  * [ETags](https://docs.cloud.google.com/storage/docs/metadata#etags)
  * The `Last-Modified` date (only available when getting object data or metadata using the XML API)



The following table lists preconditions supported by the JSON API and XML API:

JSON API | XML API | Description  
---|---|---  
`ifGenerationMatch` query parameter | [`x-goog-if-generation-match`](https://docs.cloud.google.com/storage/docs/xml-api/reference-headers#xgoogifgenerationmatch) header | Request proceeds if the `generation` of the target resource matches the value used in the precondition. If the values don't match, the request fails with a `412 Precondition Failed` response.  
`ifMetagenerationMatch` query parameter | [`x-goog-if-metageneration-match`](https://docs.cloud.google.com/storage/docs/xml-api/reference-headers#xgoogifmetagenerationmatch) header | Request proceeds if the `metageneration` of the target resource matches the value used in the precondition. If the values don't match, the request fails with a `412 Precondition Failed` response.  
`ifGenerationNotMatch` query parameter | N/A | Request proceeds if the `generation` of the target resource does not match the value used in the precondition. If the values match, the request fails with a `304 Not Modified` response.  
`ifMetagenerationNotMatch` query parameter | N/A | Request proceeds if the `metageneration` of the target resource does not match the value used in the precondition. If the values match, the request fails with a `304 Not Modified` response.  
[`If-Match`](https://docs.cloud.google.com/storage/docs/json_api/v1/parameters#ifmatch) header | [`If-Match`](https://docs.cloud.google.com/storage/docs/xml-api/reference-headers#ifmatch) header | Applicable for requests that retrieve data. Request proceeds if the `ETag` of the target resource matches the value used in the precondition. If the values don't match, the request fails with a `412 Precondition Failed` response.  
[`If-None-Match`](https://docs.cloud.google.com/storage/docs/json_api/v1/parameters#ifnonematch) header | [`If-None-Match`](https://docs.cloud.google.com/storage/docs/xml-api/reference-headers#ifnonematch) header | Applicable for requests that retrieve data. Request proceeds if the `ETag` of the target resource does not match the value used in the precondition. If the values match, the request fails with a `304 Not Modified` response.  
N/A | [`If-Modified-Since`](https://docs.cloud.google.com/storage/docs/xml-api/reference-headers#ifmodifiedsince) header | Request proceeds if the target resource has a `Last-Modified` date after the value used in the precondition. If the target resource does not meet this precondition, the request fails with a `304 Not Modified` response.  
N/A | [`If-Unmodified-Since`](https://docs.cloud.google.com/storage/docs/xml-api/reference-headers#ifunmodifiedsince) header | Request proceeds if the target resource has a `Last-Modified` date earlier than or equal to the value used in the precondition. If the target resource does not meet this precondition, the request fails with a `412 Precondition Failed` response.  
  
#### Object composition preconditions

When performing [object composition](https://docs.cloud.google.com/storage/docs/composing-objects), both the [JSON API](https://docs.cloud.google.com/storage/docs/json_api/v1/objects/compose) and the [XML API](https://docs.cloud.google.com/storage/docs/xml-api/put-object-compose) support the following:

  * The generation-match and metageneration-match preconditions for the destination object.

  * The generation-match precondition for each source object. Using this precondition prevents incorrect components from being used in the case where an independent process overwrites one of the intended components of the composition. If you use preconditions and such an overwrite occurs, the `compose` operations fails with a `412 Precondition Failed` response.




#### Object copy preconditions

When copying or rewriting an object within Cloud Storage, both the [JSON API](https://docs.cloud.google.com/storage/docs/json_api/v1/objects/rewrite) and [XML API](https://docs.cloud.google.com/storage/docs/xml-api/put-object-copy) support using standard preconditions for the destination object. Each API has additional precondition support for source objects:

  * The JSON API supports generation and metageneration preconditions for the source object, which are specified by using query parameters that are prefixed with `ifSource`.

  * All preconditions supported by the XML API can be used for the source object. These preconditions are specified in headers prefixed with `x-goog-copy-source-`.




#### The `0` value in a generation-match precondition

The generation-match precondition accepts the value `0` as a special case. When a generation-match precondition with a value of `0` is included in a request, the request only proceeds if no object with the specified name exists in the bucket or if there are only noncurrent versions of the object in the bucket. If there is a live version with the specified name, the request fails with a status code of `412 Precondition Failed`.

**Note:** The `0` value should only be used when writing object data: no other requests can succeed with a `0` precondition.

### Best practices and considerations

  * You can use multiple preconditions in a single request. If any of the preconditions are not met, the overall request fails.

  * Buckets do not have a generation number, although they do have a metageneration number. You shouldn't use preconditions that specify a generation number in a bucket request.

  * If you use a metageneration precondition in an object request, you should always use a generation precondition as well. This prevents the request from succeeding on a different object that coincidentally has a metageneration number which passes the precondition.

  * For buckets that have both [live and non-current object versions](https://docs.cloud.google.com/storage/docs/object-versioning#intro), object requests don't apply to non-current versions, unless a generation number is [explicitly included in the request](https://docs.cloud.google.com/storage/docs/using-versioned-objects#access). This means that for a general request that uses preconditions, the request fails if the live version doesn't match the precondition, regardless of whether or not a non-current version matches the preconditions.

  * You should generally use generation and metageneration preconditions instead of ETag preconditions. Together, generation and metageneration numbers keep track of all object updates, including metadata changes, providing a stronger guarantee than ETags. Additionally, generation and metageneration numbers are consistent across APIs, whereas [ETags are not](https://docs.cloud.google.com/storage/docs/metadata#etags).

  * Preconditions cannot be used in [XML API multipart uploads](https://docs.cloud.google.com/storage/docs/multipart-uploads). Attempting to do so results in a `400 NotImplemented` error.




## Cost of preconditions

Many architectures that utilize preconditions require you to make an object metadata request before the main request, in order to determine the current generation and/or metageneration number:

  * An additional request means you can up to double the network portion of the overall operation latency by adding an extra round trip, which may be an important factor in latency-sensitive operations.


  * An additional request incurs an [operation charge](https://docs.cloud.google.com/storage/pricing#operations-pricing) and in most cases a [networking charge](https://docs.cloud.google.com/storage/pricing#network-pricing).



Depending on your application, there are ways to reduce the impacts of using preconditions, such as:

  * Storing the generation and metageneration numbers of your objects locally so that you already know the correct numbers to use in your precondition.
  * Having application knowledge of which objects are newly created, so you already know when to use the `if-generation-match:0` precondition.



## Example: Using a precondition

The following example uses the generation-match precondition in a request to upload an object. In order for the request to proceed, there must be a pre-existing object stored in the bucket with the specified name, and the generation number for the pre-existing object must match the number provided in the precondition:

### Command line

Use the `--if-generation-match` flag along with the normal command:
    
    
    gcloud storage cp OBJECT_LOCATION gs://DESTINATION_BUCKET_NAME --if-generation-match=GENERATION

Where:

  * `GENERATION` is the intended generation number of the object you are replacing. For example, `1122334455667788`.

  * `OBJECT_LOCATION` is the local path to your object. For example, `Desktop/dog.png`.

  * `DESTINATION_BUCKET_NAME` is the name of the bucket to which you are uploading your object. For example, `my-bucket`.




### JSON API

  1. Have gcloud CLI [installed and initialized](https://docs.cloud.google.com/sdk/docs/install), which lets you generate an access token for the `Authorization` header.

  2. Use [`cURL`](https://curl.haxx.se/) to call the JSON API with a [`POST` Object](https://docs.cloud.google.com/storage/docs/json_api/v1/objects/insert) request:
         
         curl -X POST --data-binary @OBJECT_LOCATION \
           -H "Authorization: Bearer $(gcloud auth print-access-token)" \
           -H "Content-Type: OBJECT_CONTENT_TYPE" \
           "https://storage.googleapis.com/upload/storage/v1/b/BUCKET_NAME/o?uploadType=media&name=OBJECT_NAME"&ifGenerationMatch=GENERATION"

Where:

     * `OBJECT_LOCATION` is the local path to your object. For example, `Desktop/dog.png`.
     * `OBJECT_CONTENT_TYPE` is the content type of the object. For example, `image/png`.
     * `BUCKET_NAME` is the name of the bucket to which you are uploading your object. For example, `my-bucket`.
     * `OBJECT_NAME` is the name you want to give your object. For example, `dog.png`.
     * `GENERATION` is the intended generation number of the object you are replacing. For example, `1122334455667788`.



### XML API

  1. Have gcloud CLI [installed and initialized](https://docs.cloud.google.com/sdk/docs/install), which lets you generate an access token for the `Authorization` header.

  2. Use [`cURL`](https://docs.cloud.google.com/storage/docs/xml-api/reference-headers#ifmodifiedsince) to call the XML API with a [`PUT` Object](https://docs.cloud.google.com/storage/docs/xml-api/put-object-upload) request:
         
         curl -X PUT --data-binary @OBJECT_LOCATION \
           -H "Authorization: Bearer $(gcloud auth print-access-token)" \
           -H "Content-Type: OBJECT_CONTENT_TYPE" \
           -H "x-goog-if-generation-match: GENERATION" \
           "https://storage.googleapis.com/BUCKET_NAME/OBJECT_NAME"

Where:

     * `OBJECT_LOCATION` is the local path to your object. For example, `Desktop/dog.png`.
     * `OBJECT_CONTENT_TYPE` is the content type of the object. For example, `image/png`.
     * `GENERATION` is the intended generation number of the object you are replacing. For example, `1122334455667788`.
     * `BUCKET_NAME` is the name of the bucket to which you are uploading your object. For example, `my-bucket`.
     * `OBJECT_NAME` is the name you want to give your object. For example, `dog.png`.



## Scenarios for using preconditions

The following scenarios explore race conditions and caching examples that benefit from the use of preconditions.

### Multiple request retries

Cloud Storage is a distributed system. Because requests can fail due to network or service conditions, the recommended way to retry failures is with [exponential backoff](https://en.wikipedia.org/wiki/Exponential_backoff). However, due to the nature of distributed systems, sometimes these retries can cause surprising behavior.

Consider the following case: you want to delete an object, `file.txt`, stored in one of your buckets. Afterward, you want to add a new object with the same name to the bucket. To accomplish this, you issue a delete request to delete the object. However, a network condition — such as an intermediate router temporarily losing connectivity — prevents the request from reaching Cloud Storage, and you don't receive a response.

Because you didn't receive a response to the first request, you issue a second delete request for the object, which is successful, and you receive a response confirming the deletion. A minute later, you upload a new `file.txt`, and your upload is successful.

A race condition arises if the router that lost connectivity subsequently regains it and sends your original, seemingly lost, delete request onward to Cloud Storage. When the request arrives at Cloud Storage, it succeeds because there is a new `file.txt` present. Cloud Storage sends a response that you do not receive because your client stopped listening for it. Not only does the new file get deleted, contrary to your intentions, but also you are not aware the second deletion occurred.

The following diagram shows what happened:

![](https://docs.cloud.google.com/static/storage/images/race-condition-request-retry.svg)

#### Preventing the race condition

To prevent the above situation from occurring, you should begin by getting the metadata for `file.txt` in order to determine its current generation. You then use the generation in a generation-match precondition which you include as part of the delete request. The precondition ensures that _only_ the object with that specific generation number gets deleted, regardless of when the delete request reaches Cloud Storage or how many times the delete request with the precondition is sent. Any unintended attempts to delete a different generation of `file.txt` fail with the response code `412 Precondition Failed`.

Since similar network interruptions could cause race conditions for the upload request that followed your delete request, you can avoid many such race conditions by using the `0` value in a generation-match precondition included in the upload request. Using this precondition ensures that retries of the upload don't accidentally write the object twice, because the precondition allows the request to proceed only if there aren't any current generations of the object.

With these preconditions in place, you protect your data from accidentally being lost when performing the delete and upload requests. This can be seen in the following diagram:

![](https://docs.cloud.google.com/static/storage/images/precondition-request-retry.svg)

### Object metadata association

An object's data and metadata are separate entities that together define the object in Cloud Storage. Because they exist separately, it's possible for the object data to change while you are working with the object metadata.

Consider the following cases:

  * You want to download the metadata and data for an object, which have to be retrieved from Cloud Storage in two separate requests. You request the object metadata first, but before you're able to request the object data, an independent process or user replaces the object. Your request for the object data is still successful, but now you have the metadata of the old object and the data of the new object.

  * You want to update the metadata for an object, so you retrieve the current metadata for the object to determine its current state. Before you're able to send the request to update the metadata with your desired modifications, an independent process or user replaces the object. Your request to change the metadata for the new object is still successful, but is now associated with different object data than you intended.




#### Preventing the race condition

To prevent these situations from occurring, you should use the generation number that's returned in the initial request for object metadata, and then use this value in a generation-match precondition in the second request. Doing so ensures either the metadata properly matches up with the data, or the second request fails with a `412 Precondition Failed` response code, allowing you to request the correct metadata for the new object.

If you're concerned that the object metadata could change between the first and second request, you can also copy the metageneration number found in the initial request and use it in a metageneration-match precondition in the second request.

### Local copy freshness

In cases where you have a local copy of an object that's stored in Cloud Storage, you often want your local copy to stay up to date with the copy stored in your bucket. However, if the object stored in your bucket doesn't change, you don't want to waste time and resources downloading it again, especially if the object is large.

To prevent needless downloads of content that is still fresh, you can use the generation number of your local copy as the value in a generation-not-match precondition, which you include in your download request:

  * If the data in your bucket continues to match your local copy, the generation numbers match, causing the precondition to fail. As a result, the overall request fails with a `304 Not Modified` response, and the data is not needlessly downloaded.

  * If the data in your bucket has changed, the generation numbers do not match, and the precondition succeeds. This means the overall request proceeds normally and downloads the updated version of the content.




## What's next

  * Learn about [generation and metageneration numbers](https://docs.cloud.google.com/storage/docs/metadata#generation-number).
  * [Get metadata for an object](https://docs.cloud.google.com/storage/docs/viewing-editing-metadata#view), such as its generation number.
  * Learn about [consistency in Cloud Storage](https://docs.cloud.google.com/storage/docs/consistency).
  * Learn about [conditionally idempotent operations](https://docs.cloud.google.com/storage/docs/retry-strategy#idempotency) that should use preconditions.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
