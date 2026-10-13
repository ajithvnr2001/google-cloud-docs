---
url: https://docs.cloud.google.com/chronicle/docs/reference/rest/v1alpha/projects.locations.instances.legacySearches/legacyEntitySearchCount/
title: Method: legacySearches.legacyEntitySearchCount \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T17:07:11.358208+00:00
---

# Method: legacySearches.legacyEntitySearchCount  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/reference/rest/v1alpha/projects.locations.instances.legacySearches/legacyEntitySearchCount/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Reference ](https://docs.cloud.google.com/chronicle/docs/reference/google-secops-api-libraries-overview)



Send feedback 

#  Method: legacySearches.legacyEntitySearchCount Stay organized with collections  Save and categorize content based on your preferences. 

  * HTTP request
  * Path parameters
  * Request body
    * JSON representation
  * Response body
    * JSON representation
  * Authorization scopes
  * IAM Permissions



**Full name** : projects.locations.instances.legacySearches.legacyEntitySearchCount

Returns the total count of security entities matching the provided search criteria.

### HTTP request

`POST https://{endpoint}/v1alpha/{instance}/legacySearches:legacyEntitySearchCount`

Where `{endpoint}` is one of the [supported service endpoints](https://docs.cloud.google.com/chronicle/docs/reference/rest#rest_endpoints).

### Path parameters

Parameters  
---  
`instance` |  `string` Required. The instance to get the search results for. Format: projects/{project}/locations/{location}/instances/{instance}  
  
### Request body

The request body contains data with the following structure:

JSON representation  
---  
      
    
    {
      "term": string,
      "type": [
        string
      ],
      "networkName": [
        string
      ],
      "environmentsName": [
        string
      ],
      "requestedPage": integer,
      "pageSize": integer,
      "requestingUser": string,
      "isSuspicious": boolean,
      "isInternalAsset": boolean,
      "isEnriched": boolean
    }  
  
Fields  
---  
`term` |  `string` Optional. Search term.  
`type[]` |  `string` Optional. List of entity types.  
`networkName[]` |  `string` Optional. List of network names.  
`environmentsName[]` |  `string` Optional. List of environment names.  
`requestedPage` |  `integer` Optional. The requested page.  
`pageSize` |  `integer` Optional. Number of entries to return.  
`requestingUser` |  `string` Optional. Requesting user.  
`isSuspicious` |  `boolean` Optional. Is suspicious.  
`isInternalAsset` |  `boolean` Optional. Is internal asset.  
`isEnriched` |  `boolean` Optional. Is enriched.  
  
### Response body

Response for legacySearches.legacyEntitySearchCount.

If successful, the response body contains data with the following structure:

JSON representation  
---  
      
    
    {
      "payload": integer
    }  
  
Fields  
---  
`payload` |  `integer` Optional. The count.  
  
### Authorization scopes

Requires one of the following OAuth scopes:

  * `https://www.googleapis.com/auth/cloud-platform`
  * ` https://www.googleapis.com/auth/chronicle`



For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).

### IAM Permissions

Requires the following [IAM](https://cloud.google.com/iam/docs) permission on the `instance` resource:

  * `chronicle.legacySearches.searchEntities`



For more information, see the [IAM documentation](https://cloud.google.com/iam/docs).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-08-27 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-08-27 UTC."],[],[]] 
