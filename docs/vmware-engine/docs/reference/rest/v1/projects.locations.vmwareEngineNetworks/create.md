---
url: https://docs.cloud.google.com/vmware-engine/docs/reference/rest/v1/projects.locations.vmwareEngineNetworks/create/
title: Method: projects.locations.vmwareEngineNetworks.create \u00a0|\u00a0 Google Cloud VMware Engine \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:53:35.902280+00:00
---

# Method: projects.locations.vmwareEngineNetworks.create  |  Google Cloud VMware Engine  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/vmware-engine/docs/reference/rest/v1/projects.locations.vmwareEngineNetworks/create/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ VMware Engine ](https://docs.cloud.google.com/vmware-engine/docs)



Send feedback 

#  Method: projects.locations.vmwareEngineNetworks.create Stay organized with collections  Save and categorize content based on your preferences. 

  * HTTP request
  * Path parameters
  * Query parameters
  * Request body
  * Response body
  * Authorization scopes



Creates a new VMware Engine network that can be used by a private cloud.

### HTTP request

`POST https://vmwareengine.googleapis.com/v1/{parent=projects/*/locations/*}/vmwareEngineNetworks`

The URL uses [gRPC Transcoding](https://google.aip.dev/127) syntax.

### Path parameters

Parameters  
---  
`parent` |  `string` Required. The resource name of the location to create the new VMware Engine network in. A VMware Engine network of type `LEGACY` is a regional resource, and a VMware Engine network of type `STANDARD` is a global resource. Resource names are schemeless URIs that follow the conventions in <https://cloud.google.com/apis/design/resource_names>. For example: `projects/my-project/locations/global` Authorization requires the following [IAM](https://cloud.google.com/iam/docs/) permission on the specified resource `parent`:

  * `vmwareengine.vmwareEngineNetworks.create`

  
  
### Query parameters

Parameters  
---  
`vmwareEngineNetworkId` |  `string` Required. The user-provided identifier of the new VMware Engine network. This identifier must be unique among VMware Engine network resources within the parent and becomes the final token in the name URI. The identifier must meet the following requirements:

  * For networks of type LEGACY, adheres to the format: `{region-id}-default`. Replace `{region-id}` with the region where you want to create the VMware Engine network. For example, "us-central1-default".
  * Only contains 1-63 alphanumeric characters and hyphens
  * Begins with an alphabetical character
  * Ends with a non-hyphen character
  * Not formatted as a UUID
  * Complies with [RFC 1034](https://datatracker.ietf.org/doc/html/rfc1034) (section 3.5)

  
`requestId` |  `string` Optional. A request ID to identify requests. Specify a unique request ID so that if you must retry your request, the server will know to ignore the request if it has already been completed. The server guarantees that a request doesn't result in creation of duplicate commitments for at least 60 minutes.For example, consider a situation where you make an initial request and the request times out. If you make the request again with the same request ID, the server can check if original operation with the same request ID was received, and if so, will ignore the second request. This prevents clients from accidentally creating duplicate commitments.The request ID must be a valid UUID with the exception that zero UUID is not supported (00000000-0000-0000-0000-000000000000).  
  
### Request body

The request body contains an instance of `[VmwareEngineNetwork](https://docs.cloud.google.com/vmware-engine/docs/reference/rest/v1/projects.locations.vmwareEngineNetworks#VmwareEngineNetwork)`.

### Response body

If successful, the response body contains a newly created instance of `[Operation](https://docs.cloud.google.com/vmware-engine/docs/reference/rest/v1/projects.locations.operations#Operation)`.

### Authorization scopes

Requires the following OAuth scope:

  * `https://www.googleapis.com/auth/cloud-platform`



For more information, see the [Authentication Overview](https://cloud.google.com/docs/authentication/external/authorization-gcp).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-06-30 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-06-30 UTC."],[],[]] 
