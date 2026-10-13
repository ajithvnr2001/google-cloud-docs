---
url: https://docs.cloud.google.com/security-command-center/docs/reference/rest/v1p1beta1/organizations.sources.findings/patch/
title: Method: organizations.sources.findings.patch \u00a0|\u00a0 Security Command Center \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T16:33:57.631589+00:00
---

# Method: organizations.sources.findings.patch  |  Security Command Center  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/security-command-center/docs/reference/rest/v1p1beta1/organizations.sources.findings/patch/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Security Command Center ](https://docs.cloud.google.com/security-command-center/docs)
  * [ Reference ](https://docs.cloud.google.com/security-command-center/docs/vulnerability-findings-index)



Send feedback 

#  Method: organizations.sources.findings.patch Stay organized with collections  Save and categorize content based on your preferences. 

  * HTTP request
  * Path parameters
  * Query parameters
  * Request body
  * Response body
  * Authorization scopes
  * Try it!



Creates or updates a finding. The corresponding source must exist for a finding creation to succeed.

### HTTP request

Choose an endpoint:

globalme-central2useu

  
`PATCH https://securitycenter.googleapis.com/v1p1beta1/{finding.name=organizations/*/sources/*/findings/*}`

The URLs use [gRPC Transcoding](https://google.aip.dev/127) syntax.

### Path parameters

Parameters  
---  
`finding.name` |  `string` The relative resource name of this finding. See: <https://cloud.google.com/apis/design/resource_names#relative_resource_name> Example: "organizations/{organizationId}/sources/{source_id}/findings/{findingId}"  
  
### Query parameters

Parameters  
---  
`updateMask` |  `string (`[FieldMask](https://protobuf.dev/reference/protobuf/google.protobuf/#field-mask)` format)` The FieldMask to use when updating the finding resource. This field should not be specified when creating a finding.When updating a finding, an empty mask is treated as updating all mutable fields and replacing sourceProperties. Individual sourceProperties can be added/updated by using "sourceProperties." in the field mask.  
  
### Request body

The request body contains an instance of `[Finding](https://docs.cloud.google.com/security-command-center/docs/reference/rest/v1p1beta1/organizations.sources.findings#Finding)`.

### Response body

If successful, the response body contains an instance of `[Finding](https://docs.cloud.google.com/security-command-center/docs/reference/rest/v1p1beta1/organizations.sources.findings#Finding)`.

### Authorization scopes

Requires one of the following OAuth scopes:

  * `https://www.googleapis.com/auth/cloud-platform`
  * `https://www.googleapis.com/auth/securitycenter`



For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-08 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-08 UTC."],[],[]] 
