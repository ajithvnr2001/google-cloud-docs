---
url: https://docs.cloud.google.com/storage/docs/json_api/v1/operations/list/
title: Operations: list \u00a0|\u00a0 Cloud Storage \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T09:41:29.262150+00:00
---

# Operations: list  |  Cloud Storage  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/storage/docs/json_api/v1/operations/list/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Storage ](https://docs.cloud.google.com/docs/storage)
  * [ Cloud Storage ](https://docs.cloud.google.com/storage/docs)
  * [ Reference ](https://docs.cloud.google.com/storage/docs/apis)



Send feedback 

#  Operations: list Stay organized with collections  Save and categorize content based on your preferences. 

Lists long-running operations that match the specified filter in the request.

## Required permissions

The authenticated user must have the following IAM permissions on the bucket to use this method: 

  * `storage.bucketOperations.list`



## Request

### HTTP request
    
    
    GET https://storage.googleapis.com/storage/v1/b/bucket/operations

In addition to [standard query parameters](https://docs.cloud.google.com/storage/docs/json_api/v1/parameters#query), the following query parameters apply to this method.

To see an example of how to include query parameters in a request, see the [JSON API Overview](https://docs.cloud.google.com/storage/docs/json_api#query_parameters) page.

### Parameters

Parameter name | Value | Description  
---|---|---  
**Path parameters**  
`bucket` | `string` |  Name of a bucket.   
**Optional query parameters**  
`pageSize` | `string` |  The maximum number of items to return in a single response.   
`pageToken` | `string` |  A previously-returned page token representing part of the larger set of results to view. The `pageToken` is an encoded field containing the name of the last item in the returned list. In a subsequent request using the `pageToken`, items that come after the `pageToken` are shown (up to `pageSize`).  
`filter` | `string` |  A filter for returning items. Items can be filtered using the following metadata:

  * `createTime`
  * `completeTime`
  * `updateTime`
  * `type`
  * `requestedCancellation`
  * `done`

The syntax requires [EBNF grammar](https://google.aip.dev/assets/misc/ebnf-filtering.txt).  
  
### Request body

Do not supply a request body with this method.

## Response

If successful, this method returns a response body with the following structure:
    
    
    {
      "kind": "storage#operations",
      "nextPageToken": string,
      "operations": [
        [operations Resource](https://docs.cloud.google.com/storage/docs/json_api/v1/operations#resource)
      ]
    }

Property name | Value | Description | Notes  
---|---|---|---  
`kind` | `string` | The kind of item this is. For lists of long-running operations, this is always `"storage#operations"`. |   
`nextPageToken` | `string` | The continuation token. Provide this value as the `pageToken` of a subsequent request in order to return the next page of results. Note that the next page may be empty. If this is the last page of results, then no continuation token is returned. The presence of this parameter in the response should always be checked to ensure a complete listing of all the results.   
  
The `nextPageToken` is the name of the last long-running operation in the returned list. In a subsequent list request using the `pageToken`, items that come after the token are shown (up to `maxResults`). |   
`operations[]` | `list` | The list of [long-running operations](https://docs.cloud.google.com/storage/docs/json_api/v1/operations). |   
  
For information about status and error codes returned by this API, see the [reference page](https://docs.cloud.google.com/storage/docs/json_api/v1/status-codes).

## Try it!

Use the APIs Explorer below to call this method on live data and see the response. 

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
