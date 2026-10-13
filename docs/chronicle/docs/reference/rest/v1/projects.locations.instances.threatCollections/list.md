---
url: https://docs.cloud.google.com/chronicle/docs/reference/rest/v1/projects.locations.instances.threatCollections/list/
title: Method: threatCollections.list \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T18:45:36.016718+00:00
---

# Method: threatCollections.list  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/reference/rest/v1/projects.locations.instances.threatCollections/list/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Reference ](https://docs.cloud.google.com/chronicle/docs/reference/google-secops-api-libraries-overview)



Send feedback 

#  Method: threatCollections.list Stay organized with collections  Save and categorize content based on your preferences. 

  * HTTP request
  * Path parameters
  * Query parameters
  * Request body
  * Response body
    * JSON representation
  * Authorization scopes
  * IAM Permissions



**Full name** : projects.locations.instances.threatCollections.list

Lists threat collections, which contain reports and tracked threat campaigns from Google Threat Intelligence.

### HTTP request

`GET https://{endpoint}/v1/{parent}/threatCollections`

Where `{endpoint}` is one of the [supported service endpoints](https://docs.cloud.google.com/chronicle/docs/reference/rest#rest_endpoints).

### Path parameters

Parameters  
---  
`parent` |  `string` Required. The parent resource of the threat collections. Format: projects/{project}/locations/{location}/instances/{instance}  
  
### Query parameters

Parameters  
---  
`pageSize` |  `integer` Optional. The maximum number of threat collections to return. The default is 10, and the maximum value is 40.  
`pageToken` |  `string` Optional. A page token, received from a previous `threatCollections.list` call. Provide this to retrieve the subsequent page. When paginating, all other parameters provided to `threatCollections.list` must match the call that provided the page token.  
`filter` |  `string` Optional. A filter that can be used to retrieve specific threat collection. Supported filters: - Search literal (<https://google.aip.dev/160#literals>) to perform an open search matching on the threat collection's display name or description. - Filtering by a specific field value in the format: `field:value`. Supported fields: - displayName - description - createTime - updateTime Filters can be combined using `AND`, `OR`, `NOT`.  
`orderBy` |  `string` Optional. The order to sort the returned threat collections by. The default is `createTime desc`. Fields that are supported for sorting are: - createTime - updateTime - firstSeenTime - lastSeenTime - displayName  
  
### Request body

The request body must be empty.

### Response body

Response containing a list of threat collections.

If successful, the response body contains data with the following structure:

JSON representation  
---  
      
    
    {
      "threatCollections": [
        {
          object ([ThreatCollection](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1/projects.locations.instances.threatCollections#ThreatCollection))
        }
      ],
      "nextPageToken": string
    }  
  
Fields  
---  
`threatCollections[]` |  `object (`[ThreatCollection](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1/projects.locations.instances.threatCollections#ThreatCollection)`)` Output only. List of threat collections. This is sorted by creation time in descending order by default.  
`nextPageToken` |  `string` Output only. A token that can be sent as `pageToken` to retrieve the next page. If this field is omitted, there are no subsequent pages.  
  
### Authorization scopes

Requires one of the following OAuth scopes:

  * `https://www.googleapis.com/auth/cloud-platform`
  * ` https://www.googleapis.com/auth/chronicle`



For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).

### IAM Permissions

Requires the following [IAM](https://cloud.google.com/iam/docs) permission on the `parent` resource:

  * `chronicle.threatCollections.list`



For more information, see the [IAM documentation](https://cloud.google.com/iam/docs).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-08-27 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-08-27 UTC."],[],[]] 
