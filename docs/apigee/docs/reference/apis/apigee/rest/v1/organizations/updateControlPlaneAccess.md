---
url: https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations/updateControlPlaneAccess/
title: Method: organizations.updateControlPlaneAccess \u00a0|\u00a0 Apigee \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:54:15.058161+00:00
---

# Method: organizations.updateControlPlaneAccess  |  Apigee  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations/updateControlPlaneAccess/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Apigee ](https://docs.cloud.google.com/apigee/docs)
  * [ Reference ](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest)



Send feedback 

#  Method: organizations.updateControlPlaneAccess Stay organized with collections  Save and categorize content based on your preferences. 

  * HTTP request
  * Path parameters
  * Query parameters
  * Request body
  * Response body
  * Authorization scopes
  * Try it!



Updates the permissions required to allow Apigee runtime-plane components access to the control plane. Currently, the permissions required are to: 1. Allow runtime components to publish analytics data to the control plane.

**Note** : Available to Apigee hybrid only.

### HTTP request

`PATCH https://apigee.googleapis.com/v1/{controlPlaneAccess.name=organizations/*/controlPlaneAccess}`

The URL uses [gRPC Transcoding](https://google.aip.dev/127) syntax.

### Path parameters

Parameters  
---  
`controlPlaneAccess.name` |  `string` Identifier. The resource name of the ControlPlaneAccess. Format: "organizations/{org}/controlPlaneAccess"  
  
### Query parameters

Parameters  
---  
`updateMask` |  `string (`[FieldMask](https://protobuf.dev/reference/protobuf/google.protobuf/#field-mask)` format)` List of fields to be updated. Fields that can be updated: synchronizerIdentities, publisher_identities.This is a comma-separated list of fully qualified names of fields. Example: `"user.displayName,photo"`.  
  
### Request body

The request body contains an instance of `[ControlPlaneAccess](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/ControlPlaneAccess)`.

### Response body

If successful, the response body contains an instance of `[Operation](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.operations#Operation)`.

### Authorization scopes

Requires the following OAuth scope:

  * `https://www.googleapis.com/auth/cloud-platform`



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
