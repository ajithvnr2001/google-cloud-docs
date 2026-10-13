---
url: https://docs.cloud.google.com/advisory-notifications/docs/reference/rest/v1/organizations.locations/updateSettings/
title: Method: organizations.locations.updateSettings \u00a0|\u00a0 Advisory Notifications \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T18:44:05.767823+00:00
---

# Method: organizations.locations.updateSettings  |  Advisory Notifications  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/advisory-notifications/docs/reference/rest/v1/organizations.locations/updateSettings/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Advisory Notifications ](https://docs.cloud.google.com/advisory-notifications/docs)
  * [ Reference ](https://docs.cloud.google.com/advisory-notifications/docs/apis)



Send feedback 

#  Method: organizations.locations.updateSettings Stay organized with collections  Save and categorize content based on your preferences. 

  * HTTP request
  * Path parameters
  * Request body
  * Response body
  * Authorization scopes
  * IAM Permissions



Update notification settings.

### HTTP request

`PATCH https://advisorynotifications.googleapis.com/v1/{settings.name=organizations/*/locations/*/settings}`

The URL uses [gRPC Transcoding](https://google.aip.dev/127) syntax.

### Path parameters

Parameters  
---  
`settings.name` |  `string` Identifier. The resource name of the settings to retrieve. Format: organizations/{organization}/locations/{location}/settings or projects/{projects}/locations/{location}/settings.  
  
### Request body

The request body contains an instance of `[Settings](https://docs.cloud.google.com/advisory-notifications/docs/reference/rest/v1/Settings)`.

### Response body

If successful, the response body contains an instance of `[Settings](https://docs.cloud.google.com/advisory-notifications/docs/reference/rest/v1/Settings)`.

### Authorization scopes

Requires the following OAuth scope:

  * `https://www.googleapis.com/auth/cloud-platform`



For more information, see the [Authentication Overview](https://cloud.google.com/docs/authentication/).

### IAM Permissions

Requires the following [IAM](https://cloud.google.com/iam/docs) permission on the `name` resource:

  * `advisorynotifications.settings.update`



For more information, see the [IAM documentation](https://cloud.google.com/iam/docs).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-04-23 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-04-23 UTC."],[],[]] 
