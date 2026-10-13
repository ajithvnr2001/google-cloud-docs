---
url: https://docs.cloud.google.com/firewall/docs/reference/network-security/rest/v1/organizations.locations.securityProfileGroups/get/
title: Method: organizations.locations.securityProfileGroups.get \u00a0|\u00a0 Cloud Next Generation Firewall \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T18:55:15.522462+00:00
---

# Method: organizations.locations.securityProfileGroups.get  |  Cloud Next Generation Firewall  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/firewall/docs/reference/network-security/rest/v1/organizations.locations.securityProfileGroups/get/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Networking ](https://docs.cloud.google.com/docs/networking)
  * [ Cloud NGFW ](https://docs.cloud.google.com/firewall/docs)
  * [ Reference ](https://docs.cloud.google.com/firewall/docs/apis)



Send feedback 

#  Method: organizations.locations.securityProfileGroups.get Stay organized with collections  Save and categorize content based on your preferences. 

Gets details of a single SecurityProfileGroup.

### HTTP request

`GET https://networksecurity.googleapis.com/v1/{name=organizations/*/locations/*/securityProfileGroups/*}`

The URL uses [gRPC Transcoding](https://google.aip.dev/127) syntax.

### Path parameters

Parameters  
---  
`name` |  `string` Required. A name of the SecurityProfileGroup to get. Must be in the format `projects|organizations/*/locations/{location}/securityProfileGroups/{securityProfileGroup}`.  
  
### Request body

The request body must be empty.

### Response body

If successful, the response body contains an instance of `[SecurityProfileGroup](https://docs.cloud.google.com/firewall/docs/reference/network-security/rest/v1/organizations.locations.securityProfileGroups#SecurityProfileGroup)`.

### Authorization scopes

Requires the following OAuth scope:

  * `https://www.googleapis.com/auth/cloud-platform`



For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-09-24 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-09-24 UTC."],[],[]] 
