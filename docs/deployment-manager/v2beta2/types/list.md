---
url: https://docs.cloud.google.com/deployment-manager/v2beta2/types/list/
title: Types: list \u00a0|\u00a0 Cloud Deployment Manager \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T05:32:38.921472+00:00
---

# Types: list  |  Cloud Deployment Manager  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/deployment-manager/v2beta2/types/list/

Cloud Deployment Manager reached end of support on **March 31, 2026**.   
If you currently use Deployment Manager, please migrate to Infrastructure Manager or an alternative deployment technology.  
  
For more information on the deprecation and shutdown, see [Deployment Manager deprecation](https://docs.cloud.google.com/deployment-manager/docs/deprecations). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Infrastructure as code ](https://docs.cloud.google.com/docs/iac)
  * [ Cloud Deployment Manager ](https://docs.cloud.google.com/deployment-manager/docs)
  * [ Reference ](https://docs.cloud.google.com/deployment-manager/docs/apis)



Send feedback 

#  Types: list Stay organized with collections  Save and categorize content based on your preferences. 

**Caution:** This is a **deprecated** version of the Deployment Manager API. Please use the [latest API version](https://docs.cloud.google.com/deployment-manager/latest) instead.

**Requiresauthorization**

Lists all resource types for Deployment Manager. Try it now. 

## Request

### HTTP request
    
    
    GET https://www.googleapis.com/deploymentmanager/v2beta2/projects/project/global/types

### Parameters

Parameter name | Value | Description  
---|---|---  
**Path parameters**  
`project` | `string` |  The project ID for this request.   
**Optional query parameters**  
`filter` | `string` |  Sets a filter expression for filtering listed resources, in the form `filter={expression}`. Your `{expression}` must be in the format: `field_name comparison_string literal_string`.   
  
The `field_name` is the name of the field you want to compare. Only atomic field types are supported (string, number, boolean). The `comparison_string` must be either `eq` (equals) or `ne` (not equals). The `literal_string` is the string value to filter to. The literal value must be valid for the type of field you are filtering by (string, number, boolean). For string fields, the literal value is interpreted as a regular expression using [RE2](https://github.com/google/re2) syntax. The literal value must match the entire field.   
  
For example, `filter=name ne example-instance`.   
  
**Compute Engine Beta API Only:** If you use filtering in the [Beta API](https://docs.cloud.google.com/compute/docs/reference/beta), you can also filter on nested fields. For example, you could filter on instances that have set the `scheduling.automaticRestart` field to `true`. In particular, use filtering on nested fields to take advantage of [instance labels](https://docs.cloud.google.com/compute/docs/instances#instance_labels) to organize and filter results based on label values.   
  
The Beta API also supports filtering on multiple expressions by providing each separate expression within parentheses. For example, `(scheduling.automaticRestart eq true) (zone eq us-central1-f)`. Multiple expressions are treated as `AND` expressions meaning that resources must match all expressions to pass the filters.   
`maxResults` | `unsigned integer` |  The maximum number of results per page that should be returned. If the number of available results is larger than `maxResults`, Compute Engine returns a `nextPageToken` that can be used to get the next page of results in subsequent list requests. Acceptable values are `0` to `500`, inclusive. (Default: `500`)   
`pageToken` | `string` |  Specifies a page token to use. Set `pageToken` to the `nextPageToken` returned by a previous list request to get the next page of results.   
  
### Authorization

This request requires authorization with at least one of the following scopes ([read more about authentication and authorization](https://docs.cloud.google.com/deployment-manager/docs/reference/latest/authorization)).

Scope  
---  
`https://www.googleapis.com/auth/ndev.cloudman.readonly`  
`https://www.googleapis.com/auth/cloud-platform`  
`https://www.googleapis.com/auth/ndev.cloudman`  
`https://www.googleapis.com/auth/cloud-platform.read-only`  
  
### Request body

Do not supply a request body with this method.

## Response

If successful, this method returns a response body with the following structure:
    
    
    {
      "types": [
        [types Resource](https://docs.cloud.google.com/deployment-manager/v2beta2/types#resource)
      ],
      "nextPageToken": string
    }

Property name | Value | Description | Notes  
---|---|---|---  
`types[]` | `list` | [Output Only] A list of resource types supported by Deployment Manager. |   
`nextPageToken` | `string` | A token used to continue a truncated list request. |   
  
## Try it!

Use the APIs Explorer below to call this method on live data and see the response. Alternatively, try the [standalone Explorer](https://developers.google.com/apis-explorer/#p/deploymentmanager/v2beta2/deploymentmanager.types.list). 

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-04-30 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-04-30 UTC."],[],[]] 
