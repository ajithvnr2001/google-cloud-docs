---
url: https://docs.cloud.google.com/kubernetes-engine/config-sync/docs/reference/rest/v1alpha/projects.locations.fleetPackages.rollouts/list/
title: Method: projects.locations.fleetPackages.rollouts.list \u00a0|\u00a0 Config Sync \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:15:41.752424+00:00
---

# Method: projects.locations.fleetPackages.rollouts.list  |  Config Sync  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/config-sync/docs/reference/rest/v1alpha/projects.locations.fleetPackages.rollouts/list/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ Google Kubernetes Engine (GKE) ](https://docs.cloud.google.com/kubernetes-engine/docs)
  * [ Config Sync ](https://docs.cloud.google.com/kubernetes-engine/config-sync/docs)
  * [ Reference ](https://docs.cloud.google.com/kubernetes-engine/config-sync/docs/reference)



Send feedback 

#  Method: projects.locations.fleetPackages.rollouts.list Stay organized with collections  Save and categorize content based on your preferences. 

  * HTTP request
  * Path parameters
  * Query parameters
  * Request body
  * Response body
    * JSON representation
  * Authorization scopes



Lists Rollouts in a given project, location, and Fleet Package.

### HTTP request

`GET https://configdelivery.googleapis.com/v1alpha/{parent=projects/*/locations/*/fleetPackages/*}/rollouts`

The URL uses [gRPC Transcoding](https://google.aip.dev/127) syntax.

### Path parameters

Parameters  
---  
`parent` |  `string` Required. Parent value for ListRolloutsRequest  
  
### Query parameters

Parameters  
---  
`pageSize` |  `integer` Optional. Requested page size. Server may return fewer items than requested. If unspecified, server will pick an appropriate default.  
`pageToken` |  `string` Optional. A token identifying a page of results the server should return.  
`filter` |  `string` Optional. Filtering results  
`orderBy` |  `string` Optional. Hint for how to order the results  
  
### Request body

The request body must be empty.

### Response body

Message for response to listing Rollouts

If successful, the response body contains data with the following structure:

JSON representation  
---  
      
    
    {
      "rollouts": [
        {
          object ([Rollout](https://docs.cloud.google.com/kubernetes-engine/config-sync/docs/reference/rest/v1alpha/projects.locations.fleetPackages.rollouts#Rollout))
        }
      ],
      "nextPageToken": string,
      "unreachable": [
        string
      ]
    }  
  
Fields  
---  
`rollouts[]` |  `object (`[Rollout](https://docs.cloud.google.com/kubernetes-engine/config-sync/docs/reference/rest/v1alpha/projects.locations.fleetPackages.rollouts#Rollout)`)` The list of Rollouts  
`nextPageToken` |  `string` A token identifying a page of results the server should return.  
`unreachable[]` |  `string` Unordered list. Locations that could not be reached.  
  
### Authorization scopes

Requires the following OAuth scope:

  * `https://www.googleapis.com/auth/cloud-platform`



For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-11-28 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-11-28 UTC."],[],[]] 
