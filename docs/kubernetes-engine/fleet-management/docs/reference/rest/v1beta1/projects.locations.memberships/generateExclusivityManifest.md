---
url: https://docs.cloud.google.com/kubernetes-engine/fleet-management/docs/reference/rest/v1beta1/projects.locations.memberships/generateExclusivityManifest/
title: Method: projects.locations.memberships.generateExclusivityManifest \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:06:25.595068+00:00
---

# Method: projects.locations.memberships.generateExclusivityManifest  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/fleet-management/docs/reference/rest/v1beta1/projects.locations.memberships/generateExclusivityManifest/

  * [ Reference ](https://docs.cloud.google.com/kubernetes-engine/fleet-management/docs/reference/rest)



#  Method: projects.locations.memberships.generateExclusivityManifest Stay organized with collections  Save and categorize content based on your preferences. 

  * HTTP request
  * Path parameters
  * Query parameters
  * Request body
  * Response body
    * JSON representation
  * Authorization scopes
  * Examples
  * Try it!



memberships.generateExclusivityManifest generates the manifests to update the exclusivity artifacts in the cluster if needed.

Exclusivity artifacts include the Membership custom resource definition (CRD) and the singleton Membership custom resource (CR). Combined with memberships.validateExclusivity, exclusivity artifacts guarantee that a Kubernetes cluster is only registered to a single GKE Hub.

The Membership CRD is versioned, and may require conversion when the GKE Hub API server begins serving a newer version of the CRD and corresponding CR. The response will be the converted CRD and CR if there are any differences between the versions.

### HTTP request

`GET https://gkehub.googleapis.com/v1beta1/{name=projects/*/locations/*/memberships/*}:generateExclusivityManifest`

The URL uses [gRPC Transcoding](https://google.aip.dev/127) syntax.

### Path parameters

Parameters  
---  
`name` |  `string` Required. The Membership resource name in the format `projects/*/locations/*/memberships/*`. Authorization requires the following [IAM](https://cloud.google.com/iam/docs/) permission on the specified resource `name`:

  * `gkehub.memberships.generateConnectManifest`

  
  
### Query parameters

Parameters  
---  
`crdManifest` |  `string` Optional. The YAML manifest of the membership CRD retrieved by `kubectl get customresourcedefinitions membership`. Leave empty if the resource does not exist.  
`crManifest` |  `string` Optional. The YAML manifest of the membership CR retrieved by `kubectl get memberships membership`. Leave empty if the resource does not exist.  
  
### Request body

The request body must be empty.

### Response body

The response of the exclusivity artifacts manifests for the client to apply.

If successful, the response body contains data with the following structure:

JSON representation  
---  
      
    
    {
      "crdManifest": string,
      "crManifest": string
    }  
  
Fields  
---  
`crdManifest` |  `string` The YAML manifest of the membership CRD to apply if a newer version of the CRD is available. Empty if no update needs to be applied.  
`crManifest` |  `string` The YAML manifest of the membership CR to apply if a new version of the CR is available. Empty if no update needs to be applied.  
  
### Authorization scopes

Requires the following OAuth scope:

  * `https://www.googleapis.com/auth/cloud-platform`



For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-06-12 UTC.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-06-12 UTC."],[],[]] 
