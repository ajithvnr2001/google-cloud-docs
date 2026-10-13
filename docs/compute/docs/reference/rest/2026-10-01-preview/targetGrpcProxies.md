---
url: https://docs.cloud.google.com/compute/docs/reference/rest/2026-10-01-preview/targetGrpcProxies/
title: REST Resource: targetGrpcProxies \u00a0|\u00a0 Compute Engine \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:12:58.085288+00:00
---

# REST Resource: targetGrpcProxies  |  Compute Engine  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/compute/docs/reference/rest/2026-10-01-preview/targetGrpcProxies/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ Compute Engine ](https://docs.cloud.google.com/compute/docs)
  * [ APIs & Reference ](https://docs.cloud.google.com/compute/docs/apis)



Send feedback 

#  REST Resource: targetGrpcProxies Stay organized with collections  Save and categorize content based on your preferences. 

  * Resource: TargetGrpcProxy
    * JSON representation
  * Methods



## Resource: TargetGrpcProxy

Represents a Target gRPC Proxy resource.

A target gRPC proxy is a component of load balancers intended for load balancing gRPC traffic. Only global forwarding rules with load balancing scheme INTERNAL_SELF_MANAGED can reference a target gRPC proxy. The target gRPC Proxy references a URL map that specifies how traffic is routed to gRPC backend services.

JSON representation  
---  
      
    
    {
      "kind": string,
      "id": string,
      "creationTimestamp": string,
      "name": string,
      "description": string,
      "selfLink": string,
      "selfLinkWithId": string,
      "urlMap": string,
      "validateForProxyless": boolean,
      "fingerprint": string
    }  
  
Fields  
---  
`kind` |  `string` Output only. Type of the resource. Always `compute#targetGrpcProxy` for target grpc proxies.  
`id` |  `string ([uint64](https://developers.google.com/discovery/v1/type-format) format)` Output only. The unique identifier for the resource type. The server generates this identifier.  
`creationTimestamp` |  `string` Output only. Creation timestamp in [RFC3339](https://www.ietf.org/rfc/rfc3339.txt) text format.  
`name` |  `string` Name of the resource. Provided by the client when the resource is created. The name must be 1-63 characters long, and comply with [RFC1035](https://www.ietf.org/rfc/rfc1035.txt). Specifically, the name must be 1-63 characters long and match the regular expression `[a-z]([-a-z0-9]*[a-z0-9])?` which means the first character must be a lowercase letter, and all following characters must be a dash, lowercase letter, or digit, except the last character, which cannot be a dash.  
`description` |  `string` An optional description of this resource. Provide this property when you create the resource.  
`selfLink` |  `string` Output only. Server-defined URL for the resource.  
`selfLinkWithId` |  `string` Output only. Server-defined URL with id for the resource.  
`urlMap` |  `string` URL to the UrlMap resource that defines the mapping from URL to the BackendService. The protocol field in the BackendService must be set to GRPC.  
`validateForProxyless` |  `boolean` If true, indicates that the BackendServices referenced by the urlMap may be accessed by gRPC applications without using a sidecar proxy. This will enable configuration checks on urlMap and its referenced BackendServices to not allow unsupported features. A gRPC application must use "xds:///" scheme in the target URI of the service it is connecting to. If false, indicates that the BackendServices referenced by the urlMap will be accessed by gRPC applications via a sidecar proxy. In this case, a gRPC application must not use "xds:///" scheme in the target URI of the service it is connecting to  
`fingerprint` |  `string ([bytes](https://developers.google.com/discovery/v1/type-format) format)` Fingerprint of this resource. A hash of the contents stored in this object. This field is used in optimistic locking. This field will be ignored when inserting a `TargetGrpcProxy`. An up-to-date fingerprint must be provided in order to patch/update the TargetGrpcProxy; otherwise, the request will fail with error `412 conditionNotMet`. To see the latest fingerprint, make a `get()` request to retrieve the TargetGrpcProxy.A base64-encoded string.  
  
## Methods  
  
---  
  
### `[delete](https://docs.cloud.google.com/compute/docs/reference/rest/2026-10-01-preview/targetGrpcProxies/delete)`

|  Deletes the specified TargetGrpcProxy in the given scope  
  
### `[get](https://docs.cloud.google.com/compute/docs/reference/rest/2026-10-01-preview/targetGrpcProxies/get)`

|  Returns the specified TargetGrpcProxy resource in the given scope.  
  
### `[insert](https://docs.cloud.google.com/compute/docs/reference/rest/2026-10-01-preview/targetGrpcProxies/insert)`

|  Creates a TargetGrpcProxy in the specified project in the given scope using the parameters that are included in the request.  
  
### `[list](https://docs.cloud.google.com/compute/docs/reference/rest/2026-10-01-preview/targetGrpcProxies/list)`

|  Lists the TargetGrpcProxies for a project in the given scope.  
  
### `[patch](https://docs.cloud.google.com/compute/docs/reference/rest/2026-10-01-preview/targetGrpcProxies/patch)`

|  Patches the specified TargetGrpcProxy resource with the data included in the request.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-01 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-01 UTC."],[],[]] 
