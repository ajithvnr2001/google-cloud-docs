---
url: https://docs.cloud.google.com/kubernetes-engine/fleet-management/docs/reference/rest/v1alpha/projects.locations.memberships/validateExclusivity/
title: Method: projects.locations.memberships.validateExclusivity \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:06:07.240513+00:00
---

# Method: projects.locations.memberships.validateExclusivity  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/fleet-management/docs/reference/rest/v1alpha/projects.locations.memberships/validateExclusivity/

  * [ Reference ](https://docs.cloud.google.com/kubernetes-engine/fleet-management/docs/reference/rest)



#  Method: projects.locations.memberships.validateExclusivity Stay organized with collections  Save and categorize content based on your preferences. 

  * HTTP request
  * Path parameters
  * Query parameters
  * Request body
  * Response body
    * JSON representation
  * Authorization scopes
  * Examples
  * Try it!



memberships.validateExclusivity validates the state of exclusivity in the cluster. The validation does not depend on an existing Hub membership resource.

### HTTP request

`GET https://gkehub.googleapis.com/v1alpha/{parent=projects/*/locations/*}/memberships:validateExclusivity`

The URL uses [gRPC Transcoding](https://google.aip.dev/127) syntax.

### Path parameters

Parameters  
---  
`parent` |  `string` Required. The parent (project and location) where the Memberships will be created. Specified in the format `projects/*/locations/*`. Authorization requires the following [IAM](https://cloud.google.com/iam/docs/) permission on the specified resource `parent`:

  * `gkehub.memberships.generateConnectManifest`

  
  
### Query parameters

Parameters  
---  
`crManifest` |  `string` Optional. The YAML of the membership CR in the cluster. Empty if the membership CR does not exist.  
`intendedMembership` |  `string` Required. The intended membership name under the `parent`. This method only does validation in anticipation of a memberships.create call with the same name.  
  
### Request body

The request body must be empty.

### Response body

The response of exclusivity artifacts validation result status.

If successful, the response body contains data with the following structure:

JSON representation  
---  
      
    
    {
      "status": {
        object ([Status](https://docs.cloud.google.com/kubernetes-engine/fleet-management/docs/reference/rest/Shared.Types/ListOperationsResponse#Status))
      }
    }  
  
Fields  
---  
`status` |  `object (`[Status](https://docs.cloud.google.com/kubernetes-engine/fleet-management/docs/reference/rest/Shared.Types/ListOperationsResponse#Status)`)` The validation result.

  * `OK` means that exclusivity is validated, assuming the manifest produced by memberships.generateExclusivityManifest is successfully applied.
  * `ALREADY_EXISTS` means that the Membership CRD is already owned by another Hub. See `status.message` for more information.

  
  
### Authorization scopes

Requires the following OAuth scope:

  * `https://www.googleapis.com/auth/cloud-platform`



For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-06-12 UTC.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-06-12 UTC."],[],[]] 
