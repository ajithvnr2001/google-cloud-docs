---
url: https://docs.cloud.google.com/number-registry/reference/rest/v1alpha/projects.locations.discoveredRanges/showUtilization/
title: Method: projects.locations.discoveredRanges.showUtilization \u00a0|\u00a0 Cloud Number Registry \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T12:34:12.130478+00:00
---

# Method: projects.locations.discoveredRanges.showUtilization  |  Cloud Number Registry  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/number-registry/reference/rest/v1alpha/projects.locations.discoveredRanges/showUtilization/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Networking ](https://docs.cloud.google.com/docs/networking)
  * [ Cloud Number Registry ](https://docs.cloud.google.com/number-registry)
  * [ Reference ](https://docs.cloud.google.com/number-registry/apis)



Send feedback 

#  Method: projects.locations.discoveredRanges.showUtilization Stay organized with collections  Save and categorize content based on your preferences. 

  * HTTP request
  * Path parameters
  * Request body
  * Response body
    * JSON representation
  * Authorization scopes
  * IAM Permissions
  * Try it!



Gets the details of a single DiscoveredRange and its utilization.

### HTTP request

`GET https://cloudnumberregistry.googleapis.com/v1alpha/{name=projects/*/locations/*/discoveredRanges/*}:showUtilization`

The URL uses [gRPC Transcoding](https://google.aip.dev/127) syntax.

### Path parameters

Parameters  
---  
`name` |  `string` Required. The resource name of the DiscoveredRange.  
  
### Request body

The request body must be empty.

### Response body

Response message for the `[CloudNumberRegistry.ShowDiscoveredRangeUtilization](https://docs.cloud.google.com/number-registry/reference/rest/v1alpha/projects.locations.discoveredRanges/showUtilization#google.cloud.numberregistry.v1alpha.CloudNumberRegistry.ShowDiscoveredRangeUtilization)` method.

If successful, the response body contains data with the following structure:

JSON representation  
---  
      
    
    {
      "discoveredRange": {
        object ([DiscoveredRange](https://docs.cloud.google.com/number-registry/reference/rest/v1alpha/projects.locations.discoveredRanges#DiscoveredRange))
      },
      "rangeUtilization": {
        object ([RangeUtilization](https://docs.cloud.google.com/number-registry/reference/rest/v1alpha/RangeUtilization))
      }
    }  
  
Fields  
---  
`discoveredRange` |  `object (`[DiscoveredRange](https://docs.cloud.google.com/number-registry/reference/rest/v1alpha/projects.locations.discoveredRanges#DiscoveredRange)`)` The DiscoveredRange resource.  
`rangeUtilization` |  `object (`[RangeUtilization](https://docs.cloud.google.com/number-registry/reference/rest/v1alpha/RangeUtilization)`)` The utilization details of the DiscoveredRange.  
  
### Authorization scopes

Requires the following OAuth scope:

  * `https://www.googleapis.com/auth/cloud-platform`



For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).

### IAM Permissions

Requires the following [IAM](https://cloud.google.com/iam/docs) permission on the `name` resource:

  * `cloudnumberregistry.discoveredRanges.get`



For more information, see the [IAM documentation](https://cloud.google.com/iam/docs).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-06-02 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-06-02 UTC."],[],[]] 
