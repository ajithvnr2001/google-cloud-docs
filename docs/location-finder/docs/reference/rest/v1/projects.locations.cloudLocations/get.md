---
url: https://docs.cloud.google.com/location-finder/docs/reference/rest/v1/projects.locations.cloudLocations/get/
title: Method: projects.locations.cloudLocations.get \u00a0|\u00a0 Cloud Location Finder \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T18:34:18.776103+00:00
---

# Method: projects.locations.cloudLocations.get  |  Cloud Location Finder  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/location-finder/docs/reference/rest/v1/projects.locations.cloudLocations/get/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Distributed, hybrid, and multicloud ](https://docs.cloud.google.com/docs/dhm-cloud)
  * [ Cloud Location Finder ](https://docs.cloud.google.com/location-finder/docs)
  * [ Reference ](https://docs.cloud.google.com/location-finder/docs/reference/rest)



Send feedback 

#  Method: projects.locations.cloudLocations.get Stay organized with collections  Save and categorize content based on your preferences. 

  * HTTP request
  * Path parameters
  * Request body
  * Response body
  * Authorization scopes
  * IAM Permissions



Retrieves a resource containing information about a cloud location.

### HTTP request

`GET https://cloudlocationfinder.googleapis.com/v1/{name=projects/*/locations/*/cloudLocations/*}`

The URL uses [gRPC Transcoding](https://google.aip.dev/127) syntax.

### Path parameters

Parameters  
---  
`name` |  `string` Required. Name of the resource.  
  
### Request body

The request body must be empty.

### Response body

If successful, the response body contains an instance of `[CloudLocation](https://docs.cloud.google.com/location-finder/docs/reference/rest/v1/projects.locations.cloudLocations#CloudLocation)`.

### Authorization scopes

Requires the following OAuth scope:

  * `https://www.googleapis.com/auth/cloud-platform`



For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).

### IAM Permissions

Requires the following [IAM](https://cloud.google.com/iam/docs) permission on the `name` resource:

  * `cloudlocationfinder.cloudLocations.get`



For more information, see the [IAM documentation](https://cloud.google.com/iam/docs).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-01-06 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-01-06 UTC."],[],[]] 
