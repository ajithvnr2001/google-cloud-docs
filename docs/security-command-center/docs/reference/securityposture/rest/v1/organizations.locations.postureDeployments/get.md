---
url: https://docs.cloud.google.com/security-command-center/docs/reference/securityposture/rest/v1/organizations.locations.postureDeployments/get/
title: Method: organizations.locations.postureDeployments.get \u00a0|\u00a0 Security Command Center \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T15:00:44.342018+00:00
---

# Method: organizations.locations.postureDeployments.get  |  Security Command Center  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/security-command-center/docs/reference/securityposture/rest/v1/organizations.locations.postureDeployments/get/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Security Command Center ](https://docs.cloud.google.com/security-command-center/docs)
  * [ Reference ](https://docs.cloud.google.com/security-command-center/docs/vulnerability-findings-index)



Send feedback 

#  Method: organizations.locations.postureDeployments.get Stay organized with collections  Save and categorize content based on your preferences. 

  * HTTP request
  * Path parameters
  * Request body
  * Response body
  * Authorization scopes
  * IAM Permissions



Gets details for a `[PostureDeployment](https://docs.cloud.google.com/security-command-center/docs/reference/securityposture/rest/v1/organizations.locations.postureDeployments#PostureDeployment)`.

### HTTP request

`GET https://securityposture.googleapis.com/v1/{name=organizations/*/locations/*/postureDeployments/*}`

The URL uses [gRPC Transcoding](https://google.aip.dev/127) syntax.

### Path parameters

Parameters  
---  
`name` |  `string` Required. The name of the `[PostureDeployment](https://docs.cloud.google.com/security-command-center/docs/reference/securityposture/rest/v1/organizations.locations.postureDeployments#PostureDeployment)`, in the format `organizations/{organization}/locations/global/postureDeployments/{postureDeploymentId}`.  
  
### Request body

The request body must be empty.

### Response body

If successful, the response body contains an instance of `[PostureDeployment](https://docs.cloud.google.com/security-command-center/docs/reference/securityposture/rest/v1/organizations.locations.postureDeployments#PostureDeployment)`.

### Authorization scopes

Requires the following OAuth scope:

  * `https://www.googleapis.com/auth/cloud-platform`



For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).

### IAM Permissions

Requires the following [IAM](https://cloud.google.com/iam/docs) permission on the `name` resource:

  * `securityposture.postureDeployments.get`



For more information, see the [IAM documentation](https://cloud.google.com/iam/docs).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-08-14 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-08-14 UTC."],[],[]] 
