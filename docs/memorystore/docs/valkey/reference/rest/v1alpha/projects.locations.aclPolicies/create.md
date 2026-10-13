---
url: https://docs.cloud.google.com/memorystore/docs/valkey/reference/rest/v1alpha/projects.locations.aclPolicies/create/
title: Method: projects.locations.aclPolicies.create \u00a0|\u00a0 Memorystore for Valkey \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T15:04:32.070591+00:00
---

# Method: projects.locations.aclPolicies.create  |  Memorystore for Valkey  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/memorystore/docs/valkey/reference/rest/v1alpha/projects.locations.aclPolicies/create/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Memorystore ](https://docs.cloud.google.com/memorystore/docs)
  * [ Memorystore for Valkey ](https://docs.cloud.google.com/memorystore/docs/valkey)
  * [ Reference ](https://docs.cloud.google.com/memorystore/docs/valkey/apis)



Send feedback 

#  Method: projects.locations.aclPolicies.create Stay organized with collections  Save and categorize content based on your preferences. 

  * HTTP request
  * Path parameters
  * Query parameters
  * Request body
  * Response body
  * Authorization scopes
  * IAM Permissions



Creates an ACL policy. The creation is executed synchronously and the policy is available for use immediately after the RPC returns.

### HTTP request

Choose an endpoint:

globalafrica-south1asia-east1asia-east2asia-northeast1asia-northeast2asia-northeast3asia-south1asia-south2asia-southeast1asia-southeast2asia-southeast3australia-southeast1australia-southeast2europe-central2europe-north1europe-north2europe-southwest1europe-west1europe-west10europe-west12europe-west15europe-west2europe-west3europe-west4europe-west6europe-west8europe-west9me-central1me-central2me-west1northamerica-northeast1northamerica-northeast2northamerica-south1southamerica-east1southamerica-west1us-central1us-central2us-east1us-east4us-east5us-east7us-south1us-west1us-west2us-west3us-west4us-west8

  
`POST https://memorystore.googleapis.com/v1alpha/{parent=projects/*/locations/*}/aclPolicies`

The URLs use [gRPC Transcoding](https://google.aip.dev/127) syntax.

### Path parameters

Parameters  
---  
`parent` |  `string` Required. The resource name of the ACL policy location using the form: `projects/{project}/locations/{location}` where `location` refers to a Google Cloud region.  
  
### Query parameters

Parameters  
---  
`aclPolicyId` |  `string` Required. The logical name of the ACL policy in the customer project with the following restrictions:

  * Must contain only lowercase letters, numbers, and hyphens.
  * Must start with a letter.
  * Must be between 1-63 characters.
  * Must end with a number or a letter.
  * Must be unique within the customer project / location

  
`requestId` |  `string` Optional. Idempotent request UUID. .  
  
### Request body

The request body contains an instance of `[AclPolicy](https://docs.cloud.google.com/memorystore/docs/valkey/reference/rest/v1alpha/projects.locations.aclPolicies#AclPolicy)`.

### Response body

If successful, the response body contains a newly created instance of `[AclPolicy](https://docs.cloud.google.com/memorystore/docs/valkey/reference/rest/v1alpha/projects.locations.aclPolicies#AclPolicy)`.

### Authorization scopes

Requires one of the following OAuth scopes:

  * `https://www.googleapis.com/auth/cloud-platform`
  * `https://www.googleapis.com/auth/memorystore.read-write`



### IAM Permissions

Requires the following [IAM](https://cloud.google.com/iam/docs) permission on the `parent` resource:

  * `memorystore.aclPolicies.create`



For more information, see the [IAM documentation](https://cloud.google.com/iam/docs).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-09-28 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-09-28 UTC."],[],[]] 
