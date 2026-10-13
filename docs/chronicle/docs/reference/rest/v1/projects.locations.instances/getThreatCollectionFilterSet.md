---
url: https://docs.cloud.google.com/chronicle/docs/reference/rest/v1/projects.locations.instances/getThreatCollectionFilterSet/
title: Method: instances.getThreatCollectionFilterSet \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T15:36:24.095655+00:00
---

# Method: instances.getThreatCollectionFilterSet  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/reference/rest/v1/projects.locations.instances/getThreatCollectionFilterSet/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Reference ](https://docs.cloud.google.com/chronicle/docs/reference/google-secops-api-libraries-overview)



Send feedback 

#  Method: instances.getThreatCollectionFilterSet Stay organized with collections  Save and categorize content based on your preferences. 

  * HTTP request
  * Path parameters
  * Request body
  * Response body
    * JSON representation
  * Authorization scopes
  * IAM Permissions
  * Filter
    * JSON representation
  * FilterOption
    * JSON representation



**Full name** : projects.locations.instances.getThreatCollectionFilterSet

Get the set of threat collection filter options.

### HTTP request

`GET https://{endpoint}/v1/{name}`

Where `{endpoint}` is one of the [supported service endpoints](https://docs.cloud.google.com/chronicle/docs/reference/rest#rest_endpoints).

### Path parameters

Parameters  
---  
`name` |  `string` Required. The resource name. Format: projects/{project}/locations/{location}/instances/{instance}/threatCollectionFilterSet  
  
### Request body

The request body must be empty.

### Response body

Represents threat collection filters and their available values to be used when requesting a filtered list of threat collections.

If successful, the response body contains data with the following structure:

JSON representation  
---  
      
    
    {
      "name": string,
      "filters": [
        {
          object ([Filter](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1/projects.locations.instances/getThreatCollectionFilterSet#Filter))
        }
      ]
    }  
  
Fields  
---  
`name` |  `string` Output only. Identifier. Resource name for threat collection filters, in the format '.../instances/{instance}/threatCollectionFilterSet'.  
`filters[]` |  `object (`[Filter](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1/projects.locations.instances/getThreatCollectionFilterSet#Filter)`)` Output only. List of filters that threat collections feed supports.  
  
### Authorization scopes

Requires one of the following OAuth scopes:

  * `https://www.googleapis.com/auth/cloud-platform`
  * ` https://www.googleapis.com/auth/chronicle`



For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).

### IAM Permissions

Requires the following [IAM](https://cloud.google.com/iam/docs) permission on the `name` resource:

  * `chronicle.threatCollectionFilterSet.get`



For more information, see the [IAM documentation](https://cloud.google.com/iam/docs).

## Filter

Represents a threat collection filter and its available values to be used when requesting a filtered list of threat collections.

JSON representation  
---  
      
    
    {
      "displayName": string,
      "options": [
        {
          object ([FilterOption](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1/projects.locations.instances/getThreatCollectionFilterSet#FilterOption))
        }
      ]
    }  
  
Fields  
---  
`displayName` |  `string` Output only. Display name of the filter. Example: "Source Regions".  
`options[]` |  `object (`[FilterOption](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1/projects.locations.instances/getThreatCollectionFilterSet#FilterOption)`)` Output only. List of options under this filter.  
  
## FilterOption

Threat collection filter option. Example: 'filter=(source_region:"US")'. "source_region" is the filterKey. "US" is the value.

JSON representation  
---  
      
    
    {
      "displayName": string,
      "filterKey": string,
      "value": string,
      "options": [
        {
          object ([FilterOption](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1/projects.locations.instances/getThreatCollectionFilterSet#FilterOption))
        }
      ]
    }  
  
Fields  
---  
`displayName` |  `string` Output only. Display name of the filter option. Example: "United States".  
`filterKey` |  `string` Output only. The filtering key used to use when requesting a filtered list of threat collections. Example: "source_region".  
`value` |  `string` Output only. Value of the filter to use when requesting a filtered list of threat collections. Example: "US".  
`options[]` |  `object (`[FilterOption](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1/projects.locations.instances/getThreatCollectionFilterSet#FilterOption)`)` Output only. Nested list of options for a given filter option.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-08-27 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-08-27 UTC."],[],[]] 
