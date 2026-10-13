---
url: https://docs.cloud.google.com/deployment-manager/docs/reference/latest/deployments/list/
title: Deployments: list \u00a0|\u00a0 Cloud Deployment Manager \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T19:05:04.782564+00:00
---

# Deployments: list  |  Cloud Deployment Manager  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/deployment-manager/docs/reference/latest/deployments/list/

Cloud Deployment Manager reached end of support on **March 31, 2026**.   
If you currently use Deployment Manager, please migrate to Infrastructure Manager or an alternative deployment technology.  
  
For more information on the deprecation and shutdown, see [Deployment Manager deprecation](https://docs.cloud.google.com/deployment-manager/docs/deprecations). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Infrastructure as code ](https://docs.cloud.google.com/docs/iac)
  * [ Cloud Deployment Manager ](https://docs.cloud.google.com/deployment-manager/docs)
  * [ Reference ](https://docs.cloud.google.com/deployment-manager/docs/apis)



Send feedback 

#  Deployments: list Stay organized with collections  Save and categorize content based on your preferences. 

**Requiresauthorization**

Lists all deployments for a given project. Try it now. 

## Request

### HTTP request
    
    
    GET https://www.googleapis.com/deploymentmanager/v2/projects/project/global/deployments

### Parameters

Parameter name | Value | Description  
---|---|---  
**Path parameters**  
`project` | `string` |  The project ID for this request.   
**Optional query parameters**  
`filter` | `string` |  A filter expression that filters resources listed in the response. The expression must specify the field name, a comparison operator, and the value that you want to use for filtering. The value must be a string, a number, or a boolean. The comparison operator must be either `=`, `!=`, `>`, or `<`.   
  
For example, if you are filtering Compute Engine instances, you can exclude instances named `example-instance` by specifying `name != example-instance`.   
  
You can also filter nested fields. For example, you could specify `scheduling.automaticRestart = false` to include instances only if they are not scheduled for automatic restarts. You can use filtering on nested fields to filter based on [resource labels](https://docs.cloud.google.com/compute/docs/labeling-resources).   
  
To filter on multiple expressions, provide each separate expression within parentheses. For example, `(scheduling.automaticRestart = true) (cpuPlatform = "Intel Skylake")`. By default, each expression is an `AND` expression. However, you can include `AND` and `OR` expressions explicitly. For example, `(cpuPlatform = "Intel Skylake") OR (cpuPlatform = "Intel Broadwell") AND (scheduling.automaticRestart = true)`.   
`maxResults` | `unsigned integer` |  The maximum number of results per page that should be returned. If the number of available results is larger than `maxResults`, Compute Engine returns a `nextPageToken` that can be used to get the next page of results in subsequent list requests. Acceptable values are `0` to `500`, inclusive. (Default: `500`)   
`orderBy` | `string` |  Sorts list results by a certain order. By default, results are returned in alphanumerical order based on the resource name.   
  
You can also sort results in descending order based on the creation timestamp using `orderBy="creationTimestamp desc"`. This sorts results based on the `creationTimestamp` field in reverse chronological order (newest result first). Use this to sort resources like operations so that the newest operation is returned first.   
  
Currently, only sorting by `name` or `creationTimestamp desc` is supported.   
`pageToken` | `string` |  Specifies a page token to use. Set `pageToken` to the `nextPageToken` returned by a previous list request to get the next page of results.   
  
### Authorization

This request requires authorization with at least one of the following scopes ([read more about authentication and authorization](https://docs.cloud.google.com/deployment-manager/latest/authorization)).

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
      "deployments": [
        [deployments Resource](https://docs.cloud.google.com/deployment-manager/docs/reference/latest/deployments#resource)
      ],
      "nextPageToken": string
    }

Property name | Value | Description | Notes  
---|---|---|---  
`deployments[]` | `list` | Output only. The deployments contained in this response. |   
`nextPageToken` | `string` | Output only. A token used to continue a truncated list request. |   
  
## Try it!

Use the APIs Explorer below to call this method on live data and see the response. Alternatively, try the [standalone Explorer](https://developers.google.com/apis-explorer/#p/deploymentmanager/v2/deploymentmanager.deployments.list). 

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-04-30 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-04-30 UTC."],[],[]] 
