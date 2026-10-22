---
url: https://docs.cloud.google.com/storage/docs/json_api/v1/buckets/list/
title: Buckets: list \u00a0|\u00a0 Cloud Storage \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T10:37:52.633434+00:00
---

# Buckets: list  |  Cloud Storage  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/storage/docs/json_api/v1/buckets/list/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Storage ](https://docs.cloud.google.com/docs/storage)
  * [ Cloud Storage ](https://docs.cloud.google.com/storage/docs)
  * [ Reference ](https://docs.cloud.google.com/storage/docs/apis)



Send feedback 

#  Buckets: list Stay organized with collections  Save and categorize content based on your preferences. 

Retrieves a list of buckets for a given project, ordered in the list lexicographically by name.

## Required permissions

The authenticated user must have the `storage.buckets.list` IAM permission to use this method. Additionally, to list specific bucket properties, the authenticated user must have the following permissions:

  * To list the IAM policies: `storage.buckets.getIamPolicy`
  * To list the bucket IP filtering rules: `storage.buckets.getIpFilter`



## Request

### HTTP request
    
    
    GET https://storage.googleapis.com/storage/v1/b

In addition to [standard query parameters](https://docs.cloud.google.com/storage/docs/json_api/v1/parameters#query), the following query parameters apply to this method.

To see an example of how to include query parameters in a request, see the [JSON API Overview](https://docs.cloud.google.com/storage/docs/json_api#query_parameters) page.

### Parameters

Parameter name | Value | Description  
---|---|---  
**Required query parameters**  
`project` | `string` |  A valid API project identifier.   
**Optional query parameters**  
`maxResults` | `unsigned integer` |  Maximum number of buckets to return in a single response. The service may return fewer results than `maxResults` so the presence of `nextPageToken` should always be checked. The service limits to: 

  * 200 items if `projection=full`.
  * 1,000 items if `projection=noAcl`.

  
`pageToken` | `string` |  A previously-returned page token representing part of the larger set of results to view. The `pageToken` is an encoded field containing the name of the last item (bucket) in the returned list. In a subsequent request, using the `pageToken`, items that come after the `pageToken` are shown (up to `maxResults`). For soft-deleted bucket list requests, the `pageToken` also contains the generation of the bucket. If you start a listing and then create a new bucket before using a `pageToken` to continue listing, you will not see the new bucket in subsequent listing results if it is in part of the bucket namespace already listed.  
`prefix` | `string` |  Filter results to buckets whose names begin with this prefix.   
`projection` | `string` |  Set of properties to return. Defaults to `noAcl`. Acceptable values are: 

  * `full`: Include all properties. 
  * `noAcl`: Omit `owner`, `acl`, and `defaultObjectAcl` properties. 

  
`returnPartialSuccess` | `boolean` |  Whether to return a list of buckets even when some buckets can't be reached because a location is temporarily unavailable.

  * `true`: The service returns a list of buckets that are available and the names of any buckets that can't be reached, if applicable.
  * `false`: The service returns a list of buckets only if all locations can be reached. If a location is temporarily unavailable, the service returns an error.

The default value is `false`.  
`softDeleted` | `boolean` |  If set to `true`, only soft-deleted bucket versions are listed as distinct results in order of bucket name and generation number. The default value is `false`.   
  
### Request body

Do not supply a request body with this method.

## Response

If successful, this method returns a response body with the following structure:
    
    
    {
      "kind": "storage#buckets",
      "nextPageToken": string,
      "items": [
        [buckets Resource](https://docs.cloud.google.com/storage/docs/json_api/v1/buckets#resource)
      ],
      "unreachable": [
        string
      ]
    }

Property name | Value | Description | Notes  
---|---|---|---  
`kind` | `string` | The kind of item this is. For lists of buckets, this is always `"storage#buckets"`. |   
`nextPageToken` | `string` | The continuation token. Provide this value as the `pageToken` of a subsequent request in order to return the next page of results. Note that the next page may be empty. If this is the last page of results, then no continuation token is returned. The presence of this parameter in the response should always be checked to ensure a complete listing of all the results. The `nextPageToken` is the name of the last bucket in the returned list. In a subsequent list request using the `pageToken`, items that come after the token are shown (up to `maxResults`). |   
`items[]` | `list` | The list of [buckets](https://docs.cloud.google.com/storage/docs/json_api/v1/buckets). |   
`unreachable[]` | `list` | The names of any buckets that can't be reached, in the format `projects/PROJECT/buckets/BUCKET_NAME`. Returned only if the `returnPartialSuccess` request parameter is set to `true`. |   
  
For information about status and error codes returned by this API, see the [reference page](https://docs.cloud.google.com/storage/docs/json_api/v1/status-codes).

## Try it!

Use the APIs Explorer below to call this method on live data and see the response. 

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-21 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-21 UTC."],[],[]] 
