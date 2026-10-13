---
url: https://docs.cloud.google.com/kubernetes-engine/fleet-management/docs/reference/rest/v1beta/projects.locations.memberships/generateConnectManifest/
title: Method: projects.locations.memberships.generateConnectManifest \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:06:16.927402+00:00
---

# Method: projects.locations.memberships.generateConnectManifest  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/fleet-management/docs/reference/rest/v1beta/projects.locations.memberships/generateConnectManifest/

  * [ Reference ](https://docs.cloud.google.com/kubernetes-engine/fleet-management/docs/reference/rest)



#  Method: projects.locations.memberships.generateConnectManifest Stay organized with collections  Save and categorize content based on your preferences. 

  * HTTP request
  * Path parameters
  * Query parameters
  * Request body
  * Response body
    * JSON representation
  * Authorization scopes
  * ConnectAgentResource
    * JSON representation
  * TypeMeta
    * JSON representation
  * Examples
  * Try it!



Generates the manifest for deployment of the GKE connect agent.

**This method is used internally by Google-provided libraries.** Most clients should not need to call this method directly.

### HTTP request

`GET https://gkehub.googleapis.com/v1beta/{name=projects/*/locations/*/memberships/*}:generateConnectManifest`

The URL uses [gRPC Transcoding](https://google.aip.dev/127) syntax.

### Path parameters

Parameters  
---  
`name` |  `string` Required. The Membership resource name the Agent will associate with, in the format `projects/*/locations/*/memberships/*`. Authorization requires the following [IAM](https://cloud.google.com/iam/docs/) permission on the specified resource `name`:

  * `gkehub.memberships.generateConnectManifest`

  
  
### Query parameters

Parameters  
---  
`namespace` |  `string` Optional. Namespace for GKE Connect agent resources. Defaults to `gke-connect`.The Connect Agent is authorized automatically when run in the default namespace. Otherwise, explicit authorization must be granted with an additional IAM binding.  
`proxy` |  `string ([bytes](https://developers.google.com/discovery/v1/type-format) format)` Optional. URI of a proxy if connectivity from the agent to gkeconnect.googleapis.com requires the use of a proxy. Format must be in the form `http(s)://{proxy_address}`, depending on the HTTP/HTTPS protocol supported by the proxy. This will direct the connect agent's outbound traffic through a HTTP(S) proxy.A base64-encoded string.  
`version` |  `string` Optional. The Connect agent version to use. Defaults to the most current version.  
`isUpgrade` |  `boolean` Optional. If true, generate the resources for upgrade only. Some resources generated only for installation (e.g. secrets) will be excluded.  
`registry` |  `string` Optional. The registry to fetch the connect agent image from. Defaults to gcr.io/gkeconnect.  
`imagePullSecretContent` |  `string ([bytes](https://developers.google.com/discovery/v1/type-format) format)` Optional. The image pull secret content for the registry, if not public.A base64-encoded string.  
  
### Request body

The request body must be empty.

### Response body

GenerateConnectManifestResponse contains manifest information for installing/upgrading a Connect agent.

If successful, the response body contains data with the following structure:

JSON representation  
---  
      
    
    {
      "manifest": [
        {
          object ([ConnectAgentResource](https://docs.cloud.google.com/kubernetes-engine/fleet-management/docs/reference/rest/v1beta/projects.locations.memberships/generateConnectManifest#ConnectAgentResource))
        }
      ]
    }  
  
Fields  
---  
`manifest[]` |  `object (`[ConnectAgentResource](https://docs.cloud.google.com/kubernetes-engine/fleet-management/docs/reference/rest/v1beta/projects.locations.memberships/generateConnectManifest#ConnectAgentResource)`)` The ordered list of Kubernetes resources that need to be applied to the cluster for GKE Connect agent installation/upgrade.  
  
### Authorization scopes

Requires the following OAuth scope:

  * `https://www.googleapis.com/auth/cloud-platform`



For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).

## ConnectAgentResource

ConnectAgentResource represents a Kubernetes resource manifest for Connect Agent deployment.

JSON representation  
---  
      
    
    {
      "type": {
        object ([TypeMeta](https://docs.cloud.google.com/kubernetes-engine/fleet-management/docs/reference/rest/v1beta/projects.locations.memberships/generateConnectManifest#TypeMeta))
      },
      "manifest": string
    }  
  
Fields  
---  
`type` |  `object (`[TypeMeta](https://docs.cloud.google.com/kubernetes-engine/fleet-management/docs/reference/rest/v1beta/projects.locations.memberships/generateConnectManifest#TypeMeta)`)` Kubernetes type of the resource.  
`manifest` |  `string` YAML manifest of the resource.  
  
## TypeMeta

TypeMeta is the type information needed for content unmarshalling of Kubernetes resources in the manifest.

JSON representation  
---  
      
    
    {
      "kind": string,
      "apiVersion": string
    }  
  
Fields  
---  
`kind` |  `string` Kind of the resource (e.g. Deployment).  
`apiVersion` |  `string` APIVersion of the resource (e.g. v1).  
  
Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-06-12 UTC.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-06-12 UTC."],[],[]] 
