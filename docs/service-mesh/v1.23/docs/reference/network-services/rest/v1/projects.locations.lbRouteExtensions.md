---
url: https://docs.cloud.google.com/service-mesh/v1.23/docs/reference/network-services/rest/v1/projects.locations.lbRouteExtensions
title: REST Resource: projects.locations.lbRouteExtensions \u00a0|\u00a0 Cloud Service Mesh v1.23 \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T19:05:42.182085+00:00
---

# REST Resource: projects.locations.lbRouteExtensions  |  Cloud Service Mesh v1.23  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/service-mesh/v1.23/docs/reference/network-services/rest/v1/projects.locations.lbRouteExtensions

You are viewing archived v1.23 Service Mesh documentation.

Available versions

[Cloud Service Mesh latest](https://docs.cloud.google.com/service-mesh/docs)  
[Cloud Service Mesh 1.28 archive](https://docs.cloud.google.com/service-mesh/v1.28/docs)  
[Cloud Service Mesh 1.27 archive](https://docs.cloud.google.com/service-mesh/v1.27/docs)  
[Cloud Service Mesh 1.26 archive](https://docs.cloud.google.com/service-mesh/v1.26/docs)  
[Cloud Service Mesh 1.25 archive](https://docs.cloud.google.com/service-mesh/v1.25/docs)  
[Cloud Service Mesh 1.24 archive](https://docs.cloud.google.com/service-mesh/v1.24/docs)  
[Cloud Service Mesh 1.23 archive](https://docs.cloud.google.com/service-mesh/v1.23/docs)  
[Cloud Service Mesh 1.22 archive](https://docs.cloud.google.com/service-mesh/v1.22/docs)  
[Cloud Service Mesh 1.21 archive](https://docs.cloud.google.com/service-mesh/v1.21/docs)  
[Cloud Service Mesh 1.20 archive](https://docs.cloud.google.com/service-mesh/v1.20/docs)  
[Anthos Service Mesh 1.19 archive](https://docs.cloud.google.com/service-mesh/v1.19/docs)  


  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Networking ](https://docs.cloud.google.com/docs/networking)
  * [ Cloud Service Mesh ](https://docs.cloud.google.com/service-mesh/docs)
  * [ v1.23 ](https://docs.cloud.google.com/service-mesh/v1.23/docs)



Send feedback 

#  REST Resource: projects.locations.lbRouteExtensions Stay organized with collections  Save and categorize content based on your preferences. 

  * Resource: LbRouteExtension
    * JSON representation
  * Methods



## Resource: LbRouteExtension

`LbRouteExtension` is a resource that lets you control where traffic is routed to for a given request.

JSON representation  
---  
      
    
    {
      "name": string,
      "createTime": string,
      "updateTime": string,
      "description": string,
      "labels": {
        string: string,
        ...
      },
      "forwardingRules": [
        string
      ],
      "extensionChains": [
        {
          object ([ExtensionChain](https://docs.cloud.google.com/service-mesh/v1.23/docs/reference/network-services/rest/v1/ExtensionChain))
        }
      ],
      "loadBalancingScheme": enum ([LoadBalancingScheme](https://docs.cloud.google.com/service-mesh/v1.23/docs/reference/network-services/rest/v1/LoadBalancingScheme)),
      "metadata": {
        object
      }
    }  
  
Fields  
---  
`name` |  `string` Required. Identifier. Name of the `LbRouteExtension` resource in the following format: `projects/{project}/locations/{location}/lbRouteExtensions/{lbRouteExtension}`.  
`createTime` |  `string (`[Timestamp](https://developers.google.com/protocol-buffers/docs/reference/google.protobuf#google.protobuf.Timestamp)` format)` Output only. The timestamp when the resource was created.A timestamp in RFC3339 UTC "Zulu" format, with nanosecond resolution and up to nine fractional digits. Examples: `"2014-10-02T15:01:23Z"` and `"2014-10-02T15:01:23.045123456Z"`.  
`updateTime` |  `string (`[Timestamp](https://developers.google.com/protocol-buffers/docs/reference/google.protobuf#google.protobuf.Timestamp)` format)` Output only. The timestamp when the resource was updated.A timestamp in RFC3339 UTC "Zulu" format, with nanosecond resolution and up to nine fractional digits. Examples: `"2014-10-02T15:01:23Z"` and `"2014-10-02T15:01:23.045123456Z"`.  
`description` |  `string` Optional. A human-readable description of the resource.  
`labels` |  `map (key: string, value: string)` Optional. Set of labels associated with the `LbRouteExtension` resource.The format must comply with [the requirements for labels](https://cloud.google.com/compute/docs/labeling-resources#requirements) for Google Cloud resources.An object containing a list of `"key": value` pairs. Example: `{ "name": "wrench", "mass": "1.3kg", "count": "3" }`.  
`forwardingRules[]` |  `string` Required. A list of references to the forwarding rules to which this service extension is attached to. At least one forwarding rule is required. There can be only one `LbRouteExtension` resource per forwarding rule.  
`extensionChains[]` |  `object (`[ExtensionChain](https://docs.cloud.google.com/service-mesh/v1.23/docs/reference/network-services/rest/v1/ExtensionChain)`)` Required. A set of ordered extension chains that contain the match conditions and extensions to execute. Match conditions for each extension chain are evaluated in sequence for a given request. The first extension chain that has a condition that matches the request is executed. Any subsequent extension chains do not execute. Limited to 5 extension chains per resource.  
`loadBalancingScheme` |  `enum (`[LoadBalancingScheme](https://docs.cloud.google.com/service-mesh/v1.23/docs/reference/network-services/rest/v1/LoadBalancingScheme)`)` Required. All backend services and forwarding rules referenced by this extension must share the same load balancing scheme. Supported values: `INTERNAL_MANAGED`, `EXTERNAL_MANAGED`. For more information, refer to [Choosing a load balancer](https://cloud.google.com/load-balancing/docs/backend-service).  
`metadata` |  `object (`[Struct](https://developers.google.com/protocol-buffers/docs/reference/google.protobuf#google.protobuf.Struct)` format)` Optional. The metadata provided here will be included as part of the `metadata_context` (of type `google.protobuf.Struct`) in the `ProcessingRequest` message sent to the extension server. The metadata will be available under the namespace `com.google.lb_route_extension.<resourceName>`. The following variables are supported in the metadata Struct:`{forwarding_rule_id}` \- substituted with the forwarding rule's fully qualified resource name.  
  
## Methods  
  
---  
  
### `[create](https://docs.cloud.google.com/service-mesh/v1.23/docs/reference/network-services/rest/v1/projects.locations.lbRouteExtensions/create)`

|  Creates a new `LbRouteExtension` resource in a given project and location.  
  
### `[delete](https://docs.cloud.google.com/service-mesh/v1.23/docs/reference/network-services/rest/v1/projects.locations.lbRouteExtensions/delete)`

|  Deletes the specified `LbRouteExtension` resource.  
  
### `[get](https://docs.cloud.google.com/service-mesh/v1.23/docs/reference/network-services/rest/v1/projects.locations.lbRouteExtensions/get)`

|  Gets details of the specified `LbRouteExtension` resource.  
  
### `[list](https://docs.cloud.google.com/service-mesh/v1.23/docs/reference/network-services/rest/v1/projects.locations.lbRouteExtensions/list)`

|  Lists `LbRouteExtension` resources in a given project and location.  
  
### `[patch](https://docs.cloud.google.com/service-mesh/v1.23/docs/reference/network-services/rest/v1/projects.locations.lbRouteExtensions/patch)`

|  Updates the parameters of the specified `LbRouteExtension` resource.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-06-18 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-06-18 UTC."],[],[]] 
