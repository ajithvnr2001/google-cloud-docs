---
url: https://docs.cloud.google.com/compute/docs/osconfig/rest/v1alpha/projects.locations.instanceOSPoliciesCompliances/get/
title: Method: projects.locations.instanceOSPoliciesCompliances.get \u00a0|\u00a0 Compute Engine \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T10:27:20.622992+00:00
---

# Method: projects.locations.instanceOSPoliciesCompliances.get  |  Compute Engine  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/compute/docs/osconfig/rest/v1alpha/projects.locations.instanceOSPoliciesCompliances/get/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ Compute Engine ](https://docs.cloud.google.com/compute/docs)
  * [ APIs & Reference ](https://docs.cloud.google.com/compute/docs/apis)



Send feedback 

#  Method: projects.locations.instanceOSPoliciesCompliances.get Stay organized with collections  Save and categorize content based on your preferences. 

  * HTTP request
  * Path parameters
  * Request body
  * Response body
  * Authorization scopes
  * Try it!



GetInstanceOSPoliciesCompliance is deprecated. Instead, use GetOSPolicyAssignmentReport.

Get OS policies compliance data for the specified Compute Engine VM instance.

### HTTP request

`GET https://osconfig.googleapis.com/v1alpha/{name=projects/*/locations/*/instanceOSPoliciesCompliances/*}`

The URL uses [gRPC Transcoding](https://google.aip.dev/127) syntax.

### Path parameters

Parameters  
---  
`name` |  `string` Required. API resource name for instance OS policies compliance resource.Format: `projects/{project}/locations/{location}/instanceOSPoliciesCompliances/{instance}`For `{project}`, either Compute Engine project-number or project-id can be provided. For `{instance}`, either Compute Engine VM instance-id or instance-name can be provided.  
  
### Request body

The request body must be empty.

### Response body

If successful, the response body contains an instance of `[InstanceOSPoliciesCompliance](https://docs.cloud.google.com/compute/docs/osconfig/rest/v1alpha/projects.locations.instanceOSPoliciesCompliances#InstanceOSPoliciesCompliance)`.

### Authorization scopes

Requires the following OAuth scope:

  * `https://www.googleapis.com/auth/cloud-platform`



For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-07-28 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-07-28 UTC."],[],[]] 
