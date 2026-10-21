---
url: https://docs.cloud.google.com/monitoring/api/ref_v3/rest/v3/services.serviceLevelObjectives/list/
title: Method: services.serviceLevelObjectives.list \u00a0|\u00a0 Cloud Monitoring \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T07:05:57.972464+00:00
---

# Method: services.serviceLevelObjectives.list  |  Cloud Monitoring  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/monitoring/api/ref_v3/rest/v3/services.serviceLevelObjectives/list/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Google Cloud Observability ](https://docs.cloud.google.com/stackdriver/docs)
  * [ Monitoring ](https://docs.cloud.google.com/monitoring/docs)
  * [ Reference ](https://docs.cloud.google.com/monitoring/docs/apis)



Send feedback 

#  Method: services.serviceLevelObjectives.list Stay organized with collections  Save and categorize content based on your preferences. 

  * HTTP request
  * Path parameters
  * Query parameters
  * Request body
  * Response body
    * JSON representation
  * Authorization scopes
  * Try it!



List the `ServiceLevelObjective`s for the given `Service`.

### HTTP request

`GET https://monitoring.googleapis.com/v3/{parent}/serviceLevelObjectives`

### Path parameters

Parameters  
---  
`parent` |  `string` Required. Resource name of the parent containing the listed SLOs, either a project or a Monitoring Metrics Scope. The formats are:
    
    
    projects/[PROJECT_ID_OR_NUMBER]/services/[SERVICE_ID]
    workspaces/[HOST_PROJECT_ID_OR_NUMBER]/services/-
      
  
### Query parameters

Parameters  
---  
`filter` |  `string` A filter specifying what `ServiceLevelObjective`s to return.  
`pageSize` |  `integer` A non-negative number that is the maximum number of results to return. When 0, use default page size.  
`pageToken` |  `string` If this field is not empty then it must contain the `nextPageToken` value returned by a previous call to this method. Using this field causes the method to return additional results from the previous method call.  
`view` |  `enum (`[View](https://docs.cloud.google.com/monitoring/api/ref_v3/rest/v3/View)`)` View of the `ServiceLevelObjective`s to return. If `DEFAULT`, return each `ServiceLevelObjective` as originally defined. If `EXPLICIT` and the `ServiceLevelObjective` is defined in terms of a `BasicSli`, replace the `BasicSli` with a `RequestBasedSli` spelling out how the SLI is computed.  
  
### Request body

The request body must be empty.

### Response body

The `serviceLevelObjectives.list` response.

If successful, the response body contains data with the following structure:

JSON representation  
---  
      
    
    {
      "serviceLevelObjectives": [
        {
          object ([ServiceLevelObjective](https://docs.cloud.google.com/monitoring/api/ref_v3/rest/v3/services.serviceLevelObjectives#ServiceLevelObjective))
        }
      ],
      "nextPageToken": string
    }  
  
Fields  
---  
`serviceLevelObjectives[]` |  `object (`[ServiceLevelObjective](https://docs.cloud.google.com/monitoring/api/ref_v3/rest/v3/services.serviceLevelObjectives#ServiceLevelObjective)`)` The `ServiceLevelObjective`s matching the specified filter.  
`nextPageToken` |  `string` If there are more results than have been returned, then this field is set to a non-empty value. To see the additional results, use that value as `pageToken` in the next call to this method.  
  
### Authorization scopes

Requires one of the following OAuth scopes:

  * `https://www.googleapis.com/auth/cloud-platform`
  * ` https://www.googleapis.com/auth/monitoring`
  * ` https://www.googleapis.com/auth/monitoring.read`



For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-07-23 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-07-23 UTC."],[],[]] 
