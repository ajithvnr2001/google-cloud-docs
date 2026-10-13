---
url: https://docs.cloud.google.com/security-command-center/docs/reference/rest/v1beta1/organizations.assets/updateSecurityMarks/
title: Method: organizations.assets.updateSecurityMarks \u00a0|\u00a0 Security Command Center \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:46:30.563140+00:00
---

# Method: organizations.assets.updateSecurityMarks  |  Security Command Center  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/security-command-center/docs/reference/rest/v1beta1/organizations.assets/updateSecurityMarks/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Security Command Center ](https://docs.cloud.google.com/security-command-center/docs)
  * [ Reference ](https://docs.cloud.google.com/security-command-center/docs/vulnerability-findings-index)



Send feedback 

#  Method: organizations.assets.updateSecurityMarks Stay organized with collections  Save and categorize content based on your preferences. 

  * HTTP request
  * Path parameters
  * Query parameters
  * Request body
  * Response body
  * Authorization scopes
  * Try it!



Updates security marks.

### HTTP request

Choose an endpoint:

globalme-central2useu

  
`PATCH https://securitycenter.googleapis.com/v1beta1/{securityMarks.name=organizations/*/assets/*/securityMarks}`

The URLs use [gRPC Transcoding](https://google.aip.dev/127) syntax.

### Path parameters

Parameters  
---  
`securityMarks.name` |  `string` The relative resource name of the SecurityMarks. See: <https://cloud.google.com/apis/design/resource_names#relative_resource_name> Examples: "organizations/{organizationId}/assets/{asset_id}/securityMarks" "organizations/{organizationId}/sources/{source_id}/findings/{findingId}/securityMarks".  
  
### Query parameters

Parameters  
---  
`updateMask` |  `string (`[FieldMask](https://protobuf.dev/reference/protobuf/google.protobuf/#field-mask)` format)` The FieldMask to use when updating the security marks resource.  
`startTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` The time at which the updated SecurityMarks take effect.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
  
### Request body

The request body contains an instance of `[SecurityMarks](https://docs.cloud.google.com/security-command-center/docs/reference/rest/v1beta1/organizations.sources.findings#SecurityMarks)`.

### Response body

If successful, the response body contains an instance of `[SecurityMarks](https://docs.cloud.google.com/security-command-center/docs/reference/rest/v1beta1/organizations.sources.findings#SecurityMarks)`.

### Authorization scopes

Requires one of the following OAuth scopes:

  * `https://www.googleapis.com/auth/cloud-platform`
  * `https://www.googleapis.com/auth/securitycenter`



For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-08 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-08 UTC."],[],[]] 
