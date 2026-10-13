---
url: https://docs.cloud.google.com/security-command-center/docs/reference/rest/v2/projects.locations.notificationConfigs/get/
title: Method: projects.locations.notificationConfigs.get \u00a0|\u00a0 Security Command Center \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:48:40.844218+00:00
---

# Method: projects.locations.notificationConfigs.get  |  Security Command Center  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/security-command-center/docs/reference/rest/v2/projects.locations.notificationConfigs/get/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Security Command Center ](https://docs.cloud.google.com/security-command-center/docs)
  * [ Reference ](https://docs.cloud.google.com/security-command-center/docs/vulnerability-findings-index)



Send feedback 

#  Method: projects.locations.notificationConfigs.get Stay organized with collections  Save and categorize content based on your preferences. 

  * HTTP request
  * Path parameters
  * Request body
  * Response body
  * Authorization scopes
  * Try it!



Gets a notification config.

### HTTP request

Choose an endpoint:

globalme-central2useu

  
`GET https://securitycenter.googleapis.com/v2/{name=projects/*/locations/*/notificationConfigs/*}`

The URLs use [gRPC Transcoding](https://google.aip.dev/127) syntax.

### Path parameters

Parameters  
---  
`name` |  `string` Required. Name of the notification config to get. The following list shows some examples of the format:\+ `organizations/[organizationId]/locations/[locationId]/notificationConfigs/[configId]` \+ `folders/[folder_id]/locations/[locationId]/notificationConfigs/[configId]` \+ `projects/[projectId]/locations/[locationId]/notificationConfigs/[configId]`  
  
### Request body

The request body must be empty.

### Response body

If successful, the response body contains an instance of `[NotificationConfig](https://docs.cloud.google.com/security-command-center/docs/reference/rest/v2/folders.locations.notificationConfigs#NotificationConfig)`.

### Authorization scopes

Requires one of the following OAuth scopes:

  * `https://www.googleapis.com/auth/cloud-platform`
  * `https://www.googleapis.com/auth/securitycenter`



For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-08 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-08 UTC."],[],[]] 
