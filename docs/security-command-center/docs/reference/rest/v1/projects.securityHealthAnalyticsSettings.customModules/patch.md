---
url: https://docs.cloud.google.com/security-command-center/docs/reference/rest/v1/projects.securityHealthAnalyticsSettings.customModules/patch/
title: Method: projects.securityHealthAnalyticsSettings.customModules.patch \u00a0|\u00a0 Security Command Center \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:21:21.966078+00:00
---

# Method: projects.securityHealthAnalyticsSettings.customModules.patch  |  Security Command Center  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/security-command-center/docs/reference/rest/v1/projects.securityHealthAnalyticsSettings.customModules/patch/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Security Command Center ](https://docs.cloud.google.com/security-command-center/docs)
  * [ Reference ](https://docs.cloud.google.com/security-command-center/docs/vulnerability-findings-index)



Send feedback 

#  Method: projects.securityHealthAnalyticsSettings.customModules.patch Stay organized with collections  Save and categorize content based on your preferences. 

  * HTTP request
  * Path parameters
  * Query parameters
  * Request body
  * Response body
  * Authorization scopes
  * Try it!



Updates the SecurityHealthAnalyticsCustomModule under the given name based on the given update mask. Updating the enablement state is supported on both resident and inherited modules (though resident modules cannot have an enablement state of "inherited"). Updating the display name and custom config of a module is supported on resident modules only.

### HTTP request

Choose an endpoint:

globalme-central2useu

  
`PATCH https://securitycenter.googleapis.com/v1/{securityHealthAnalyticsCustomModule.name=projects/*/securityHealthAnalyticsSettings/customModules/*}`

The URLs use [gRPC Transcoding](https://google.aip.dev/127) syntax.

### Path parameters

Parameters  
---  
`securityHealthAnalyticsCustomModule.name` |  `string` Immutable. The resource name of the custom module. Its format is "organizations/{organization}/securityHealthAnalyticsSettings/customModules/{customModule}", or "folders/{folder}/securityHealthAnalyticsSettings/customModules/{customModule}", or "projects/{project}/securityHealthAnalyticsSettings/customModules/{customModule}"The id {customModule} is server-generated and is not user settable. It will be a numeric id containing 1-20 digits.  
  
### Query parameters

Parameters  
---  
`updateMask` |  `string (`[FieldMask](https://protobuf.dev/reference/protobuf/google.protobuf/#field-mask)` format)` The list of fields to be updated. The only fields that can be updated are `enablementState` and `customConfig`. If empty or set to the wildcard value `*`, both `enablementState` and `customConfig` are updated.  
  
### Request body

The request body contains an instance of `[SecurityHealthAnalyticsCustomModule](https://docs.cloud.google.com/security-command-center/docs/reference/rest/v1/folders.securityHealthAnalyticsSettings.customModules#SecurityHealthAnalyticsCustomModule)`.

### Response body

If successful, the response body contains an instance of `[SecurityHealthAnalyticsCustomModule](https://docs.cloud.google.com/security-command-center/docs/reference/rest/v1/folders.securityHealthAnalyticsSettings.customModules#SecurityHealthAnalyticsCustomModule)`.

### Authorization scopes

Requires one of the following OAuth scopes:

  * `https://www.googleapis.com/auth/cloud-platform`
  * `https://www.googleapis.com/auth/securitycenter`



For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-08 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-08 UTC."],[],[]] 
