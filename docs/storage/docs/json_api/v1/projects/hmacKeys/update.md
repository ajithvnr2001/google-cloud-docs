---
url: https://docs.cloud.google.com/storage/docs/json_api/v1/projects/hmacKeys/update/
title: Projects.hmacKeys: update \u00a0|\u00a0 Cloud Storage \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T09:41:35.085100+00:00
---

# Projects.hmacKeys: update  |  Cloud Storage  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/storage/docs/json_api/v1/projects/hmacKeys/update/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Storage ](https://docs.cloud.google.com/docs/storage)
  * [ Cloud Storage ](https://docs.cloud.google.com/storage/docs)
  * [ Reference ](https://docs.cloud.google.com/storage/docs/apis)



Send feedback 

#  Projects.hmacKeys: update Stay organized with collections  Save and categorize content based on your preferences. 

Updates the state of an HMAC key. See the [HMAC Key resource descriptor](https://docs.cloud.google.com/storage/docs/json_api/v1/projects/hmacKeys#resource) for valid states.

For general information about HMAC keys in Cloud Storage, see [HMAC Keys](https://docs.cloud.google.com/storage/docs/authentication/hmackeys).

## Required permissions

In order to use this method, the authenticated user must have the `storage.hmacKeys.update` IAM permission for the project in which the key exists.

## Request

### HTTP request
    
    
    PUT https://storage.googleapis.com/storage/v1/projects/projectIdentifier/hmacKeys/accessId

In addition to [standard query parameters](https://docs.cloud.google.com/storage/docs/json_api/v1/parameters#query), the following query parameters apply to this method.

To see an example of how to include query parameters in a request, see the [JSON API Overview](https://docs.cloud.google.com/storage/docs/json_api#query_parameters) page.

### Parameters

Parameter name | Value | Description  
---|---|---  
**Path parameters**  
`accessId` | `string` |  The access ID of the HMAC key being updated.   
`projectIdentifier` | `string` |  The project ID or project number of the project that owns the service account of the specified HMAC key.   
  
### Request body

In the request body, supply the metadata portion of a [Projects.hmacKeys resource](https://docs.cloud.google.com/storage/docs/json_api/v1/projects/hmacKeys#resource) with the following properties:

Property name | Value | Description | Notes  
---|---|---|---  
**Optional Properties**  
`etag` | `string` | HTTP 1.1 [Entity tag](https://datatracker.ietf.org/doc/html/rfc7232#section-2.3) for the HMAC key. Inclusion of an etag makes the operation's success conditional on the HMAC key's current etag matching the given value. |   
`state` | `string` | The state of the key. Can be updated to ACTIVE or INACTIVE. To set the state of the key to DELETED, use the `hmacKeys.delete` method. | writable  
  
## Response

If successful, this method returns the metadata portion of a [Projects.hmacKeys resource](https://docs.cloud.google.com/storage/docs/json_api/v1/projects/hmacKeys#resource) in the response body.

For information about status and error codes returned by this API, see the [reference page](https://docs.cloud.google.com/storage/docs/json_api/v1/status-codes).

## Try it!

Use the APIs Explorer below to call this method on live data and see the response.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
