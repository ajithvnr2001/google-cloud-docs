---
url: https://docs.cloud.google.com/iam/docs/reference/pam/rest/v1/projects.locations.entitlements/patch/
title: Method: projects.locations.entitlements.patch \u00a0|\u00a0 Identity and Access Management (IAM) \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:47:33.775282+00:00
---

# Method: projects.locations.entitlements.patch  |  Identity and Access Management (IAM)  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/iam/docs/reference/pam/rest/v1/projects.locations.entitlements/patch/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ IAM ](https://docs.cloud.google.com/iam/docs)
  * [ Reference ](https://docs.cloud.google.com/iam/docs/apis)



Send feedback 

#  Method: projects.locations.entitlements.patch Stay organized with collections  Save and categorize content based on your preferences. 

  * HTTP request
  * Path parameters
  * Query parameters
  * Request body
  * Response body
  * Authorization scopes
  * IAM Permissions
  * Examples
  * Try it!



Updates the entitlement specified in the request. Updated fields in the entitlement need to be specified in an update mask. The changes made to an entitlement are applicable only on future grants of the entitlement. However, if new approvers are added or existing approvers are removed from the approval workflow, the changes are effective on existing grants.

The following fields are not supported for updates:

  * All immutable fields
  * Entitlement name
  * Resource name
  * Resource type
  * Adding an approval workflow in an entitlement which previously had no approval workflow.
  * Deleting the approval workflow from an entitlement.
  * Adding or deleting a step in the approval workflow (only one step is supported)



Note that updates are allowed on the list of approvers in an approval workflow step.

### HTTP request

`PATCH https://privilegedaccessmanager.googleapis.com/v1/{entitlement.name=projects/*/locations/*/entitlements/*}`

The URL uses [gRPC Transcoding](https://google.aip.dev/127) syntax.

### Path parameters

Parameters  
---  
`entitlement.name` |  `string` Identifier. Name of the entitlement. Possible formats:

  * `organizations/{organization-number}/locations/{region}/entitlements/{entitlement-id}`
  * `folders/{folder-number}/locations/{region}/entitlements/{entitlement-id}`
  * `projects/{project-id|project-number}/locations/{region}/entitlements/{entitlement-id}`

  
  
### Query parameters

Parameters  
---  
`updateMask` |  `string (`[FieldMask](https://protobuf.dev/reference/protobuf/google.protobuf/#field-mask)` format)` Required. The list of fields to update. A field is overwritten if, and only if, it is in the mask. Any immutable fields set in the mask are ignored by the server. Repeated fields and map fields are only allowed in the last position of a `paths` string and overwrite the existing values. Hence an update to a repeated field or a map should contain the entire list of values. The fields specified in the updateMask are relative to the resource and not to the request. (e.g. `MaxRequestDuration`; _not_ `entitlement.MaxRequestDuration`) A value of '*' for this field refers to full replacement of the resource.This is a comma-separated list of fully qualified names of fields. Example: `"user.displayName,photo"`.  
  
### Request body

The request body contains an instance of `[Entitlement](https://docs.cloud.google.com/iam/docs/reference/pam/rest/v1/folders.locations.entitlements#Entitlement)`.

### Response body

If successful, the response body contains an instance of `[Operation](https://docs.cloud.google.com/iam/docs/reference/pam/rest/Shared.Types/ListOperationsResponse#Operation)`.

### Authorization scopes

Requires the following OAuth scope:

  * `https://www.googleapis.com/auth/cloud-platform`



For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).

### IAM Permissions

Requires the following [IAM](https://cloud.google.com/iam/docs) permission on the `name` resource:

  * `privilegedaccessmanager.entitlements.update`



For more information, see the [IAM documentation](https://cloud.google.com/iam/docs).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-09-26 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-09-26 UTC."],[],[]] 
