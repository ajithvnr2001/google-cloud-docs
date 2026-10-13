---
url: https://docs.cloud.google.com/knowledge-catalog/docs/reference/rest/v1/organizations.locations.encryptionConfigs/list/
title: Method: organizations.locations.encryptionConfigs.list \u00a0|\u00a0 Knowledge Catalog \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:48:02.337835+00:00
---

# Method: organizations.locations.encryptionConfigs.list  |  Knowledge Catalog  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/knowledge-catalog/docs/reference/rest/v1/organizations.locations.encryptionConfigs/list/

As of April 10, 2026, Dataplex Universal Catalog is now called Knowledge Catalog. The API, client library, CLI, and IAM names remain unchanged. For more information, see [Introducing the Google Cloud Knowledge Catalog](https://docs.cloud.google.com/blog/products/data-analytics/introducing-the-google-cloud-knowledge-catalog). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Knowledge Catalog ](https://docs.cloud.google.com/knowledge-catalog/docs)
  * [ Reference ](https://docs.cloud.google.com/knowledge-catalog/docs/reference)



Send feedback 

#  Method: organizations.locations.encryptionConfigs.list Stay organized with collections  Save and categorize content based on your preferences. 

  * HTTP request
  * Path parameters
  * Query parameters
  * Request body
  * Response body
    * JSON representation
  * Authorization scopes
  * Try it!



List EncryptionConfigs.

### HTTP request

`GET https://dataplex.googleapis.com/v1/{parent=organizations/*/locations/*}/encryptionConfigs`

The URL uses [gRPC Transcoding](https://google.aip.dev/127) syntax.

### Path parameters

Parameters  
---  
`parent` |  `string` Required. The location for which the EncryptionConfig is to be listed. Authorization requires the following [IAM](https://cloud.google.com/iam/docs/) permission on the specified resource `parent`:

  * `dataplex.encryptionConfig.list`

  
  
### Query parameters

Parameters  
---  
`pageSize` |  `integer` Optional. Maximum number of EncryptionConfigs to return. The service may return fewer than this value. If unspecified, at most 10 EncryptionConfigs will be returned. The maximum value is 1000; values above 1000 will be coerced to 1000.  
`pageToken` |  `string` Optional. Page token received from a previous `encryptionConfigs.list` call. Provide this to retrieve the subsequent page. When paginating, the parameters - filter and orderBy provided to `encryptionConfigs.list` must match the call that provided the page token.  
`filter` |  `string` Optional. Filter the EncryptionConfigs to be returned. Using bare literals: (These values will be matched anywhere it may appear in the object's field values) * filter=some_value Using fields: (These values will be matched only in the specified field) * filter=some_field=some_value Supported fields: * name, key, createTime, updateTime, encryptionState Example: * filter=name=organizations/123/locations/us-central1/encryptionConfigs/test-config conjunctions: (AND, OR, NOT) * filter=name=organizations/123/locations/us-central1/encryptionConfigs/test-config AND mode=CMEK logical operators: (>, <, >=, <=, !=, =, :), * filter=createTime>2024-05-01T00:00:00.000Z  
`orderBy` |  `string` Optional. Order by fields for the result.  
  
### Request body

The request body must be empty.

### Response body

List EncryptionConfigs Response

If successful, the response body contains data with the following structure:

JSON representation  
---  
      
    
    {
      "encryptionConfigs": [
        {
          object ([EncryptionConfig](https://docs.cloud.google.com/knowledge-catalog/docs/reference/rest/v1/organizations.locations.encryptionConfigs#EncryptionConfig))
        }
      ],
      "nextPageToken": string,
      "unreachableLocations": [
        string
      ]
    }  
  
Fields  
---  
`encryptionConfigs[]` |  `object (`[EncryptionConfig](https://docs.cloud.google.com/knowledge-catalog/docs/reference/rest/v1/organizations.locations.encryptionConfigs#EncryptionConfig)`)` The list of EncryptionConfigs under the given parent location.  
`nextPageToken` |  `string` Token to retrieve the next page of results, or empty if there are no more results in the list.  
`unreachableLocations[]` |  `string` Locations that could not be reached.  
  
### Authorization scopes

Requires one of the following OAuth scopes:

  * `https://www.googleapis.com/auth/cloud-platform`
  * ` https://www.googleapis.com/auth/dataplex.read-write`



For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-09-21 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-09-21 UTC."],[],[]] 
