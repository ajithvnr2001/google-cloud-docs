---
url: https://docs.cloud.google.com/monitoring/api/ref_v3/rest/v3/services/list/
title: Method: services.list \u00a0|\u00a0 Cloud Monitoring \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:37:31.848440+00:00
---

# Method: services.list  |  Cloud Monitoring  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/monitoring/api/ref_v3/rest/v3/services/list/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Google Cloud Observability ](https://docs.cloud.google.com/stackdriver/docs)
  * [ Monitoring ](https://docs.cloud.google.com/monitoring/docs)
  * [ Reference ](https://docs.cloud.google.com/monitoring/docs/apis)



Send feedback 

#  Method: services.list Stay organized with collections  Save and categorize content based on your preferences. 

  * HTTP request
  * Path parameters
  * Query parameters
  * Request body
  * Response body
    * JSON representation
  * Authorization scopes
  * Try it!



List `Service`s for this Metrics Scope.

### HTTP request

`GET https://monitoring.googleapis.com/v3/{parent}/services`

### Path parameters

Parameters  
---  
`parent` |  `string` Required. Resource name of the parent containing the listed services, either a [project](https://cloud.google.com/monitoring/api/v3#project_name) or a Monitoring Metrics Scope. The formats are:
    
    
    projects/[PROJECT_ID_OR_NUMBER]
    workspaces/[HOST_PROJECT_ID_OR_NUMBER]
      
  
### Query parameters

Parameters  
---  
`filter` |  `string` A filter specifying what `Service`s to return. The filter supports filtering on a particular service-identifier type or one of its attributes.To filter on a particular service-identifier type, the `identifier_case` refers to which option in the `identifier` field is populated. For example, the filter `identifier_case = "CUSTOM"` would match all services with a value for the `custom` field. Valid options include "CUSTOM", "APP_ENGINE", "MESH_ISTIO", and the other options listed at <https://cloud.google.com/monitoring/api/ref_v3/rest/v3/services#Service>To filter on an attribute of a service-identifier type, apply the filter name by using the snake case of the service-identifier type and the attribute of that service-identifier type, and join the two with a period. For example, to filter by the `meshUid` field of the `MeshIstio` service-identifier type, you must filter on `meshIstio.mesh_uid = "123"` to match all services with mesh UID "123". Service-identifier types and their attributes are described at <https://cloud.google.com/monitoring/api/ref_v3/rest/v3/services#Service>  
`pageSize` |  `integer` A non-negative number that is the maximum number of results to return. When 0, use default page size.  
`pageToken` |  `string` If this field is not empty then it must contain the `nextPageToken` value returned by a previous call to this method. Using this field causes the method to return additional results from the previous method call.  
  
### Request body

The request body must be empty.

### Response body

The `services.list` response.

If successful, the response body contains data with the following structure:

JSON representation  
---  
      
    
    {
      "services": [
        {
          object ([Service](https://docs.cloud.google.com/monitoring/api/ref_v3/rest/v3/services#Service))
        }
      ],
      "nextPageToken": string
    }  
  
Fields  
---  
`services[]` |  `object (`[Service](https://docs.cloud.google.com/monitoring/api/ref_v3/rest/v3/services#Service)`)` The `Service`s matching the specified filter.  
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
