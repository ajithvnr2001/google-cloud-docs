---
url: https://docs.cloud.google.com/security-command-center/docs/reference/rest/v1beta2/organizations/getEventThreatDetectionSettings/
title: Method: organizations.getEventThreatDetectionSettings \u00a0|\u00a0 Security Command Center \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T20:16:28.149634+00:00
---

# Method: organizations.getEventThreatDetectionSettings  |  Security Command Center  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/security-command-center/docs/reference/rest/v1beta2/organizations/getEventThreatDetectionSettings/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Security Command Center ](https://docs.cloud.google.com/security-command-center/docs)
  * [ Reference ](https://docs.cloud.google.com/security-command-center/docs/vulnerability-findings-index)



Send feedback 

#  Method: organizations.getEventThreatDetectionSettings Stay organized with collections  Save and categorize content based on your preferences. 

  * HTTP request
  * Path parameters
  * Request body
  * Response body
  * Authorization scopes
  * Try it!



Get the EventThreatDetectionSettings resource.

In the returned settings response, a missing field only indicates that it was not explicitly set, so no assumption should be made about these fields. In other words, organizations.getEventThreatDetectionSettings does not calculate the effective service settings for the resource, which accounts for inherited settings and defaults. Instead, use eventThreatDetectionSettings.calculate for this purpose.

### HTTP request

Choose an endpoint:

globalme-central2useu

  
`GET https://securitycenter.googleapis.com/v1beta2/{name=organizations/*/eventThreatDetectionSettings}`

The URLs use [gRPC Transcoding](https://google.aip.dev/127) syntax.

### Path parameters

Parameters  
---  
`name` |  `string` Required. The name of the EventThreatDetectionSettings to retrieve.Formats:

  * organizations/{organization}/eventThreatDetectionSettings
  * folders/{folder}/eventThreatDetectionSettings
  * projects/{project}/eventThreatDetectionSettings

  
  
### Request body

The request body must be empty.

### Response body

If successful, the response body contains an instance of `[EventThreatDetectionSettings](https://docs.cloud.google.com/security-command-center/docs/reference/rest/v1beta2/EventThreatDetectionSettings)`.

### Authorization scopes

Requires one of the following OAuth scopes:

  * `https://www.googleapis.com/auth/cloud-platform`
  * `https://www.googleapis.com/auth/securitycenter`



For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-08 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-08 UTC."],[],[]] 
