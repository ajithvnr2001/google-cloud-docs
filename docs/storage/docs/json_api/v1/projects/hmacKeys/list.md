---
url: https://docs.cloud.google.com/storage/docs/json_api/v1/projects/hmacKeys/list/
title: Projects.hmacKeys: list \u00a0|\u00a0 Cloud Storage \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T09:41:35.932288+00:00
---

# Projects.hmacKeys: list  |  Cloud Storage  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/storage/docs/json_api/v1/projects/hmacKeys/list/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Storage ](https://docs.cloud.google.com/docs/storage)
  * [ Cloud Storage ](https://docs.cloud.google.com/storage/docs)
  * [ Reference ](https://docs.cloud.google.com/storage/docs/apis)



Send feedback 

#  Projects.hmacKeys: list Stay organized with collections  Save and categorize content based on your preferences. 

Retrieves a list of HMAC keys matching the criteria..

For general information about HMAC keys in Cloud Storage, see [HMAC Keys](https://docs.cloud.google.com/storage/docs/authentication/hmackeys).

## Required permissions

In order to use this method, the authenticated user must have the `storage.hmacKeys.list` IAM permission for the project in which the keys exist.

## Request

### HTTP request
    
    
    GET https://storage.googleapis.com/storage/v1/projects/projectIdentifier/hmacKeys

In addition to [standard query parameters](https://docs.cloud.google.com/storage/docs/json_api/v1/parameters#query), the following query parameters apply to this method.

To see an example of how to include query parameters in a request, see the [JSON API Overview](https://docs.cloud.google.com/storage/docs/json_api#query_parameters) page.

### Parameters

Parameter name | Value | Description  
---|---|---  
**Path parameters**  
`projectIdentifier` | `string` |  The project ID or project number of the project in which to look for HMAC keys.   
**Optional query parameters**  
`maxResults` | `unsigned integer` |  Maximum number of `items` to return in a single page of responses.   
  
The service may return fewer results than `maxResults`. If the response includes a `nextPageToken`, there are more results not included in this response.   
`pageToken` | `string` |  A previously-returned page token representing part of the larger set of results to view.   
`serviceAccountEmail` | `string` | If present, only HMAC keys for the given service account are returned.  
`showDeletedKeys` | `boolean` | If true, include keys in the `DELETED` state. Default is false.  
  
### Request body

Do not supply a request body with this method.

## Response

If successful, this method returns a response body with the following structure:
    
    
    {
      "kind": "storage#hmacKeysMetadata",
      "nextPageToken": string,
      "items": [
        Metadata portion of an [hmacKeys resource](https://docs.cloud.google.com/storage/docs/json_api/v1/projects/hmacKeys#resource)
      ]
    }

Property name | Value | Description | Notes  
---|---|---|---  
`kind` | `string` | The kind of item this is. For lists of hmacKeys, this is always `"storage#hmacKeysMetadata"`. |   
`nextPageToken` | `string` | The continuation token. Provide this value as the `pageToken` of a subsequent request in order to return the next page of results. Note that the next page may be empty. If this is the last page of results, then no continuation token is returned. The presence of this parameter in the response should always be checked to ensure a complete listing of all the results. |   
`items[]` | `list` | The list of items. |   
  
For information about status and error codes returned by this API, see the [reference page](https://docs.cloud.google.com/storage/docs/json_api/v1/status-codes).

## Try it!

Use the APIs Explorer below to call this method on live data and see the response.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
