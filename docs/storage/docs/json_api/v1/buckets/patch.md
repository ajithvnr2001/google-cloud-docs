---
url: https://docs.cloud.google.com/storage/docs/json_api/v1/buckets/patch/
title: Buckets: patch \u00a0|\u00a0 Cloud Storage \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T02:51:40.698771+00:00
---

# Buckets: patch  |  Cloud Storage  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/storage/docs/json_api/v1/buckets/patch/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Storage ](https://docs.cloud.google.com/docs/storage)
  * [ Cloud Storage ](https://docs.cloud.google.com/storage/docs)
  * [ Reference ](https://docs.cloud.google.com/storage/docs/apis)



Send feedback 

#  Buckets: patch Stay organized with collections  Save and categorize content based on your preferences. 

Updates a bucket. Changes to the bucket will be readable immediately after writing, but configuration changes may take time to propagate. This method supports [patch](https://docs.cloud.google.com/storage/docs/json_api#patch) semantics.

## Required permissions

To use this method, the authenticated user must have the `storage.buckets.update` IAM permission. Additionally, to perform specific actions on a bucket, the authenticated user must have the following permissions:

  * To update public access prevention policies or access control lists (ACLs): `storage.buckets.setIamPolicy`
  * To return ACLs on a bucket as part of the response: `storage.buckets.getIamPolicy`
  * To update bucket IP filtering rules: `storage.buckets.setIpFilter`
  * To return bucket IP filtering rules as part of the response: `storage.buckets.getIpFilter`



## Request

### HTTP request
    
    
    PATCH https://storage.googleapis.com/storage/v1/b/bucket

In addition to [standard query parameters](https://docs.cloud.google.com/storage/docs/json_api/v1/parameters#query), the following query parameters apply to this method.

To see an example of how to include query parameters in a request, see the [JSON API Overview](https://docs.cloud.google.com/storage/docs/json_api#query_parameters) page.

### Parameters

Parameter name | Value | Description  
---|---|---  
**Path parameters**  
`bucket` | `string` |  Name of a bucket.   
**Optional query parameters**  
`ifMetagenerationMatch` | `long` |  Makes the return of the bucket metadata conditional on whether the bucket's current metageneration matches the given value.   
`ifMetagenerationNotMatch` | `long` |  Makes the return of the bucket metadata conditional on whether the bucket's current metageneration does not match the given value.   
`predefinedAcl` | `string` |  Apply a predefined set of access controls to this bucket.   
  
Acceptable values are: 

  * `authenticatedRead`: Project team owners get `OWNER` access, and `allAuthenticatedUsers` get `READER` access.
  * `private`: Project team owners get `OWNER` access.
  * `projectPrivate`: Project team members get access according to their roles.
  * `publicRead`: Project team owners get `OWNER` access, and `allUsers` get `READER` access.
  * `publicReadWrite`: Project team owners get `OWNER` access, and `allUsers` get `WRITER` access.

If `iamConfiguration.uniformBucketLevelAccess.enabled` is set to `true`, requests that include this parameter fail with a `400 Bad Request` response.   
`predefinedDefaultObjectAcl` | `string` |  Apply a predefined set of default object access controls to this bucket.   
  
Acceptable values are: 

  * `authenticatedRead`: Object owner gets `OWNER` access, and `allAuthenticatedUsers` get `READER` access.
  * `bucketOwnerFullControl`: Object owner gets `OWNER` access, and project team owners get `OWNER` access.
  * `bucketOwnerRead`: Object owner gets `OWNER` access, and project team owners get `READER` access.
  * `private`: Object owner gets `OWNER` access.
  * `projectPrivate`: Object owner gets `OWNER` access, and project team members get access according to their roles.
  * `publicRead`: Object owner gets `OWNER` access, and `allUsers` get `READER` access.

If `iamConfiguration.uniformBucketLevelAccess.enabled` is set to `true`, requests that include this parameter fail with a `400 Bad Request` response.   
`projection` | `string` |  Set of properties to return. Defaults to `noacl`.  
  
To use this parameter, override the default and specify `full`.   
  
Acceptable values are: 

  * `full`: Include all properties. 
  * `noAcl`: Omit `owner`, `acl`, and `defaultObjectAcl` properties.

  
  
### Request body

In the request body, supply the relevant portions of a [bucket resource](https://docs.cloud.google.com/storage/docs/json_api/v1/buckets#resource), according to the rules of patch semantics.

For information about status and error codes returned by this API, see the [reference page](https://docs.cloud.google.com/storage/docs/json_api/v1/status-codes).

## Response

If successful, this method returns a [bucket resource](https://docs.cloud.google.com/storage/docs/json_api/v1/buckets#resource) in the response body.

## Try it!

Use the APIs Explorer below to call this method on live data and see the response. 

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
