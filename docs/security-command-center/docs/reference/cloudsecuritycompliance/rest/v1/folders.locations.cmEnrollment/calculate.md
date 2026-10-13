---
url: https://docs.cloud.google.com/security-command-center/docs/reference/cloudsecuritycompliance/rest/v1/folders.locations.cmEnrollment/calculate/
title: Method: folders.locations.cmEnrollment.calculate \u00a0|\u00a0 Security Command Center \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T20:11:49.297138+00:00
---

# Method: folders.locations.cmEnrollment.calculate  |  Security Command Center  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/security-command-center/docs/reference/cloudsecuritycompliance/rest/v1/folders.locations.cmEnrollment/calculate/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Security Command Center ](https://docs.cloud.google.com/security-command-center/docs)
  * [ Reference ](https://docs.cloud.google.com/security-command-center/docs/vulnerability-findings-index)



Send feedback 

#  Method: folders.locations.cmEnrollment.calculate Stay organized with collections  Save and categorize content based on your preferences. 

  * HTTP request
  * Path parameters
  * Request body
  * Response body
  * Authorization scopes
  * IAM Permissions



Calculates the effective Compliance Manager enrollment for a resource. An effective enrollment is either a direct enrollment of a resource (if it exists), or an enrollment of the closest parent of a resource that's enrolled in Compliance Manager.

### HTTP request

`GET https://cloudsecuritycompliance.googleapis.com/v1/{name=folders/*/locations/*/cmEnrollment}:calculate`

The URL uses [gRPC Transcoding](https://google.aip.dev/127) syntax.

### Path parameters

Parameters  
---  
`name` |  `string` Required. The name of the Compliance Manager enrollment to calculate.Supported formats are the following:

  * `organizations/{organization_id}/locations/{location}/cmEnrollment`
  * `folders/{folder_id}/locations/{location}/cmEnrollment`
  * `projects/{projectId}/locations/{location}/cmEnrollment`

  
  
### Request body

The request body must be empty.

### Response body

If successful, the response body contains an instance of `[CalculateEffectiveCmEnrollmentResponse](https://docs.cloud.google.com/security-command-center/docs/reference/cloudsecuritycompliance/rest/v1/CalculateEffectiveCmEnrollmentResponse)`.

### Authorization scopes

Requires the following OAuth scope:

  * `https://www.googleapis.com/auth/cloud-platform`



For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).

### IAM Permissions

Requires the following [IAM](https://cloud.google.com/iam/docs) permission on the `name` resource:

  * `cloudsecuritycompliance.cmEnrollments.get`



For more information, see the [IAM documentation](https://cloud.google.com/iam/docs).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-11-07 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-11-07 UTC."],[],[]] 
