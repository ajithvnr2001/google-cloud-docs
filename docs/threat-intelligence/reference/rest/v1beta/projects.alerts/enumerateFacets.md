---
url: https://docs.cloud.google.com/threat-intelligence/reference/rest/v1beta/projects.alerts/enumerateFacets/
title: Method: projects.alerts.enumerateFacets \u00a0|\u00a0 Google Threat Intelligence \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:37:49.444419+00:00
---

# Method: projects.alerts.enumerateFacets  |  Google Threat Intelligence  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/threat-intelligence/reference/rest/v1beta/projects.alerts/enumerateFacets/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Threat Intelligence ](https://docs.cloud.google.com/threat-intelligence)
  * [ REST Reference ](https://docs.cloud.google.com/threat-intelligence/reference/rest)



Send feedback 

#  Method: projects.alerts.enumerateFacets Stay organized with collections  Save and categorize content based on your preferences. 

  * HTTP request
  * Path parameters
  * Query parameters
  * Request body
  * Response body
    * JSON representation
  * Authorization scopes
  * IAM Permissions
  * Facet
    * JSON representation
  * FacetCount
    * JSON representation



alerts.enumerateFacets returns the facets and the number of alerts that meet the filter criteria and have that value for each facet.

### HTTP request

`GET https://threatintelligence.googleapis.com/v1beta/{parent=projects/*}/alerts:enumerateFacets`

The URL uses [gRPC Transcoding](https://google.aip.dev/127) syntax.

### Path parameters

Parameters  
---  
`parent` |  `string` Required. Parent of the alerts.  
  
### Query parameters

Parameters  
---  
`filter` |  `string` Optional. Filter on what alerts will be enumerated.  
  
### Request body

The request body must be empty.

### Response body

Response message for alerts.enumerateFacets.

If successful, the response body contains data with the following structure:

JSON representation  
---  
      
    
    {
      "facets": [
        {
          object ([Facet](https://docs.cloud.google.com/threat-intelligence/reference/rest/v1beta/projects.alerts/enumerateFacets#Facet))
        }
      ]
    }  
  
Fields  
---  
`facets[]` |  `object (`[Facet](https://docs.cloud.google.com/threat-intelligence/reference/rest/v1beta/projects.alerts/enumerateFacets#Facet)`)` List of facets and the counts.  
  
### Authorization scopes

Requires the following OAuth scope:

  * `https://www.googleapis.com/auth/cloud-platform`



For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).

### IAM Permissions

Requires the following [IAM](https://cloud.google.com/iam/docs) permission on the `parent` resource:

  * `threatintelligence.alerts.list`



For more information, see the [IAM documentation](https://cloud.google.com/iam/docs).

## Facet

Facet represents a sub element of a resource for filtering. The results from this method are used to populate the filterable facets in the UI.

JSON representation  
---  
      
    
    {
      "facet": string,
      "facetCounts": [
        {
          object ([FacetCount](https://docs.cloud.google.com/threat-intelligence/reference/rest/v1beta/projects.alerts/enumerateFacets#FacetCount))
        }
      ],
      "facetType": string,
      "minValue": string,
      "maxValue": string,
      "totalCount": string
    }  
  
Fields  
---  
`facet` |  `string` Name of the facet. This is also the string that needs to be used in the filtering expression.  
`facetCounts[]` |  `object (`[FacetCount](https://docs.cloud.google.com/threat-intelligence/reference/rest/v1beta/projects.alerts/enumerateFacets#FacetCount)`)` List of counts for the facet (if categorical).  
`facetType` |  `string` The type of the facet. Options include "string", "int", "float", "bool", "enum", "timestamp", "user" and are useful to show the right sort of UI controls when building a AIP-160 style filtering string.  
`minValue` |  `string` Min value of the facet stringified based on type. This is only populated for facets that have a clear ordering, for types like enum it will be left empty. Timestamps will be formatted using RFC3339.  
`maxValue` |  `string` Max value of the facet stringified based on type. Will be populated and formatted the same as minValue.  
`totalCount` |  `string ([int64](https://developers.google.com/discovery/v1/type-format) format)` Total number of records that contain this facet with ANY value.  
  
## FacetCount

FacetCount represents a count of records with each facet value.

JSON representation  
---  
      
    
    {
      "value": string,
      "count": integer
    }  
  
Fields  
---  
`value` |  `string` Value of the facet stringified. Timestamps will be formatted using RFC3339.  
`count` |  `integer` Count of records with the value.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-02-19 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-02-19 UTC."],[],[]] 
