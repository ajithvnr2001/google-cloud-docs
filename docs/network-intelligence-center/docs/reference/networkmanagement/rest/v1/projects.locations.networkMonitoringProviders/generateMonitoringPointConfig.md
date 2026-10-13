---
url: https://docs.cloud.google.com/network-intelligence-center/docs/reference/networkmanagement/rest/v1/projects.locations.networkMonitoringProviders/generateMonitoringPointConfig/
title: Method: projects.locations.networkMonitoringProviders.generateMonitoringPointConfig \u00a0|\u00a0 Network Intelligence Center \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T17:22:30.188286+00:00
---

# Method: projects.locations.networkMonitoringProviders.generateMonitoringPointConfig  |  Network Intelligence Center  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/network-intelligence-center/docs/reference/networkmanagement/rest/v1/projects.locations.networkMonitoringProviders/generateMonitoringPointConfig/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Networking ](https://docs.cloud.google.com/docs/networking)
  * [ Network Intelligence Center ](https://docs.cloud.google.com/network-intelligence-center/docs)
  * [ Reference ](https://docs.cloud.google.com/network-intelligence-center/docs/apis)



Send feedback 

#  Method: projects.locations.networkMonitoringProviders.generateMonitoringPointConfig Stay organized with collections  Save and categorize content based on your preferences. 

  * HTTP request
  * Path parameters
  * Query parameters
  * Request body
  * Response body
    * JSON representation
  * Authorization scopes
  * Try it!



Generates Monitoring Point configuration of a NetworkMonitoringProvider resource.

### HTTP request

`GET https://networkmanagement.googleapis.com/v1/{name=projects/*/locations/*/networkMonitoringProviders/*}:generateMonitoringPointConfig`

The URL uses [gRPC Transcoding](https://google.aip.dev/127) syntax.

### Path parameters

Parameters  
---  
`name` |  `string` Required. Name of the resource. Format: projects/{project}/locations/{location}/networkMonitoringProviders/{networkMonitoringProvider}  
  
### Query parameters

Parameters  
---  
`privateConnectivityEnabled` |  `boolean` Optional. For Google Cloud MPs, this field indicates whether the Monitoring Point is deployed in a Private Service Connect deployment. Not used for non-Google Cloud MPs.  
  
### Request body

The request body must be empty.

### Response body

Message for response for getting Monitoring Point configuration of a NetworkMonitoringProvider resource.

If successful, the response body contains data with the following structure:

JSON representation  
---  
      
    
    {
      "config": {
        object
      }
    }  
  
Fields  
---  
`config` |  `object (`[Struct](https://protobuf.dev/reference/protobuf/google.protobuf/#struct)` format)` The Monitoring Point configuration of the provider in JSON format.  
  
### Authorization scopes

Requires the following OAuth scope:

  * `https://www.googleapis.com/auth/cloud-platform`



For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-07-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-07-22 UTC."],[],[]] 
