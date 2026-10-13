---
url: https://docs.cloud.google.com/iam/docs/reference/rest/v1/projects.locations.workloadIdentityPools.namespaces.managedIdentities/listAttestationRules/
title: Method: projects.locations.workloadIdentityPools.namespaces.managedIdentities.listAttestationRules \u00a0|\u00a0 Identity and Access Management (IAM) \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:54:01.016497+00:00
---

# Method: projects.locations.workloadIdentityPools.namespaces.managedIdentities.listAttestationRules  |  Identity and Access Management (IAM)  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/iam/docs/reference/rest/v1/projects.locations.workloadIdentityPools.namespaces.managedIdentities/listAttestationRules/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ IAM ](https://docs.cloud.google.com/iam/docs)
  * [ Reference ](https://docs.cloud.google.com/iam/docs/apis)



Send feedback 

#  Method: projects.locations.workloadIdentityPools.namespaces.managedIdentities.listAttestationRules Stay organized with collections  Save and categorize content based on your preferences. 

  * HTTP request
  * Path parameters
  * Query parameters
  * Request body
  * Response body
    * JSON representation
  * Authorization scopes
  * IAM Permissions
  * Examples
  * Try it!



List all `[AttestationRule](https://docs.cloud.google.com/iam/docs/reference/rest/v1/AttestationRule)` on a `[WorkloadIdentityPoolManagedIdentity](https://docs.cloud.google.com/iam/docs/reference/rest/v1/projects.locations.workloadIdentityPools.namespaces.managedIdentities#WorkloadIdentityPoolManagedIdentity)`.

### HTTP request

`GET https://iam.googleapis.com/v1/{resource=projects/*/locations/*/workloadIdentityPools/*/namespaces/*/managedIdentities/*}:listAttestationRules`

The URL uses [gRPC Transcoding](https://google.aip.dev/127) syntax.

### Path parameters

Parameters  
---  
`resource` |  `string` Required. The resource name of the managed identity or namespace resource to list attestation rules of.  
  
### Query parameters

Parameters  
---  
`filter` |  `string` Optional. A query filter. Supports the following function:

  * `container_ids()`: Returns only the AttestationRules under the specific container ids. The function expects a comma-delimited list with only project numbers and must use the format `projects/<project-number>`. For example: `container_ids(projects/<project-number-1>, projects/<project-number-2>,...)`.

  
`pageSize` |  `integer` Optional. The maximum number of AttestationRules to return. If unspecified, at most 50 AttestationRules are returned. The maximum value is 100; values above 100 are truncated to 100.  
`pageToken` |  `string` Optional. A page token, received from a previous `keys.list` call. Provide this to retrieve the subsequent page.  
  
### Request body

The request body must be empty.

### Response body

Response message for managedIdentities.listAttestationRules.

If successful, the response body contains data with the following structure:

JSON representation  
---  
      
    
    {
      "attestationRules": [
        {
          object ([AttestationRule](https://docs.cloud.google.com/iam/docs/reference/rest/v1/AttestationRule))
        }
      ],
      "nextPageToken": string
    }  
  
Fields  
---  
`attestationRules[]` |  `object (`[AttestationRule](https://docs.cloud.google.com/iam/docs/reference/rest/v1/AttestationRule)`)` A list of AttestationRules.  
`nextPageToken` |  `string` Optional. A token, which can be sent as `pageToken` to retrieve the next page. If this field is omitted, there are no subsequent pages.  
  
### Authorization scopes

Requires one of the following OAuth scopes:

  * `https://www.googleapis.com/auth/cloud-platform`
  * ` https://www.googleapis.com/auth/iam`



For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).

### IAM Permissions

Requires the following [IAM](https://cloud.google.com/iam/docs) permission on the `resource` resource:

  * `CALLBACK`



For more information, see the [IAM documentation](https://cloud.google.com/iam/docs).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-05-21 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-05-21 UTC."],[],[]] 
