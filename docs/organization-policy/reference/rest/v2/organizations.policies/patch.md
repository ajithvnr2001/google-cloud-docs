---
url: https://docs.cloud.google.com/organization-policy/reference/rest/v2/organizations.policies/patch/
title: Method: organizations.policies.patch \u00a0|\u00a0 Organization Policy \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T16:00:41.862448+00:00
---

# Method: organizations.policies.patch  |  Organization Policy  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/organization-policy/reference/rest/v2/organizations.policies/patch/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Organization Policy ](https://docs.cloud.google.com/organization-policy)
  * [ Reference ](https://docs.cloud.google.com/organization-policy/apis)



Send feedback 

#  Method: organizations.policies.patch Stay organized with collections  Save and categorize content based on your preferences. 

  * HTTP request
  * Path parameters
  * Query parameters
  * Request body
  * Response body
  * Authorization scopes
  * Try it!



Updates a policy.

Returns a `google.rpc.Status` with `google.rpc.Code.NOT_FOUND` if the constraint or the policy doesn't exist. Returns a `google.rpc.Status` with `google.rpc.Code.ABORTED` if the ETag supplied in the request doesn't match the persisted ETag of the policy.

Note: the supplied policy will perform a full overwrite of all fields.

### HTTP request

`PATCH https://orgpolicy.googleapis.com/v2/{policy.name=organizations/*/policies/*}`

The URL uses [gRPC Transcoding](https://google.aip.dev/127) syntax.

### Path parameters

Parameters  
---  
`policy.name` |  `string` Immutable. The resource name of the policy. Must be one of the following forms, where `constraint_name` is the name of the constraint that this policy configures:

  * `projects/{project_number}/policies/{constraint_name}`
  * `folders/{folder_number}/policies/{constraint_name}`
  * `organizations/{organization_number}/policies/{constraint_name}`

For example, `projects/123/policies/compute.disableSerialPortAccess`.Note: `projects/{projectId}/policies/{constraint_name}` is also an acceptable name for API requests, but responses will return the name using the equivalent project number.  
  
### Query parameters

Parameters  
---  
`updateMask` |  `string (`[FieldMask](https://protobuf.dev/reference/protobuf/google.protobuf/#field-mask)` format)` Field mask used to specify the fields to be overwritten in the policy. The fields specified in the updateMask are relative to the policy, not the full request.This is a comma-separated list of fully qualified names of fields. Example: `"user.displayName,photo"`.  
  
### Request body

The request body contains an instance of `[Policy](https://docs.cloud.google.com/organization-policy/reference/rest/v2/folders.policies#Policy)`.

### Response body

If successful, the response body contains an instance of `[Policy](https://docs.cloud.google.com/organization-policy/reference/rest/v2/folders.policies#Policy)`.

### Authorization scopes

Requires one of the following OAuth scopes:

  * `https://www.googleapis.com/auth/cloud-platform`
  * `https://www.googleapis.com/auth/organizationpolicy`



For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-07-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-07-22 UTC."],[],[]] 
