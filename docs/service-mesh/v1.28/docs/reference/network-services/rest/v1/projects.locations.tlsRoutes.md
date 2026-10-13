---
url: https://docs.cloud.google.com/service-mesh/v1.28/docs/reference/network-services/rest/v1/projects.locations.tlsRoutes
title: REST Resource: projects.locations.tlsRoutes \u00a0|\u00a0 Cloud Service Mesh \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T14:31:32.914155+00:00
---

# REST Resource: projects.locations.tlsRoutes  |  Cloud Service Mesh  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/service-mesh/v1.28/docs/reference/network-services/rest/v1/projects.locations.tlsRoutes

You are viewing v1.28 Service Mesh documentation.

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
  * [ Cloud Service Mesh ](https://docs.cloud.google.com/service-mesh/v1.28/docs)
  * [ Guides ](https://docs.cloud.google.com/service-mesh/v1.28/docs/overview)



Send feedback 

#  REST Resource: projects.locations.tlsRoutes Stay organized with collections  Save and categorize content based on your preferences. 

  * Resource: TlsRoute
    * JSON representation
  * RouteRule
    * JSON representation
  * RouteMatch
    * JSON representation
  * RouteAction
    * JSON representation
  * RouteDestination
    * JSON representation
  * Methods



## Resource: TlsRoute

TlsRoute defines how traffic should be routed based on SNI and other matching L3 attributes.

JSON representation  
---  
      
    
    {
      "name": string,
      "selfLink": string,
      "createTime": string,
      "updateTime": string,
      "description": string,
      "rules": [
        {
          object ([RouteRule](https://docs.cloud.google.com/service-mesh/v1.28/docs/reference/network-services/rest/v1/projects.locations.tlsRoutes#RouteRule))
        }
      ],
      "meshes": [
        string
      ],
      "gateways": [
        string
      ],
      "targetProxies": [
        string
      ],
      "labels": {
        string: string,
        ...
      }
    }  
  
Fields  
---  
`name` |  `string` Identifier. Name of the TlsRoute resource. It matches pattern `projects/*/locations/*/tlsRoutes/tls_route_name>`.  
`selfLink` |  `string` Output only. Server-defined URL of this resource  
`createTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Output only. The timestamp when the resource was created.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`updateTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Output only. The timestamp when the resource was updated.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`description` |  `string` Optional. A free-text description of the resource. Max length 1024 characters.  
`rules[]` |  `object (`[RouteRule](https://docs.cloud.google.com/service-mesh/v1.28/docs/reference/network-services/rest/v1/projects.locations.tlsRoutes#RouteRule)`)` Required. Rules that define how traffic is routed and handled. At least one RouteRule must be supplied. If there are multiple rules then the action taken will be the first rule to match.  
`meshes[]` |  `string` Optional. Meshes defines a list of meshes this TlsRoute is attached to, as one of the routing rules to route the requests served by the mesh.Each mesh reference should match the pattern: `projects/*/locations/*/meshes/<mesh_name>`The attached Mesh should be of a type SIDECAR  
`gateways[]` |  `string` Optional. Gateways defines a list of gateways this TlsRoute is attached to, as one of the routing rules to route the requests served by the gateway.Each gateway reference should match the pattern: `projects/*/locations/*/gateways/<gateway_name>`  
`targetProxies[]` |  `string` Optional. TargetProxies defines a list of TargetTcpProxies this TlsRoute is attached to, as one of the routing rules to route the requests served by the TargetTcpProxy.Each TargetTcpProxy reference should match the pattern: `projects/*/locations/*/targetTcpProxies/<target_tcp_proxy_name>`  
`labels` |  `map (key: string, value: string)` Optional. Set of label tags associated with the TlsRoute resource.An object containing a list of `"key": value` pairs. Example: `{ "name": "wrench", "mass": "1.3kg", "count": "3" }`.  
  
## RouteRule

Specifies how to match traffic and how to route traffic when traffic is matched.

JSON representation  
---  
      
    
    {
      "matches": [
        {
          object ([RouteMatch](https://docs.cloud.google.com/service-mesh/v1.28/docs/reference/network-services/rest/v1/projects.locations.tlsRoutes#RouteMatch))
        }
      ],
      "action": {
        object ([RouteAction](https://docs.cloud.google.com/service-mesh/v1.28/docs/reference/network-services/rest/v1/projects.locations.tlsRoutes#RouteAction))
      }
    }  
  
Fields  
---  
`matches[]` |  `object (`[RouteMatch](https://docs.cloud.google.com/service-mesh/v1.28/docs/reference/network-services/rest/v1/projects.locations.tlsRoutes#RouteMatch)`)` Required. RouteMatch defines the predicate used to match requests to a given action. Multiple match types are "OR"ed for evaluation. Atleast one RouteMatch must be supplied.  
`action` |  `object (`[RouteAction](https://docs.cloud.google.com/service-mesh/v1.28/docs/reference/network-services/rest/v1/projects.locations.tlsRoutes#RouteAction)`)` Required. The detailed rule defining how to route matched traffic.  
  
## RouteMatch

RouteMatch defines the predicate used to match requests to a given action. Multiple match types are "AND"ed for evaluation.

JSON representation  
---  
      
    
    {
      "sniHost": [
        string
      ],
      "alpn": [
        string
      ]
    }  
  
Fields  
---  
`sniHost[]` |  `string` Optional. SNI (server name indicator) to match against. SNI will be matched against all wildcard domains, i.e. `www.example.com` will be first matched against `www.example.com`, then `*.example.com`, then `*.com.` Partial wildcards are not supported, and values like *w.example.com are invalid. At least one of sniHost and alpn is required. Up to 100 sni hosts across all matches can be set.  
`alpn[]` |  `string` Optional. ALPN (Application-Layer Protocol Negotiation) to match against. Examples: "http/1.1", "h2". At least one of sniHost and alpn is required. Up to 5 alpns across all matches can be set.  
  
## RouteAction

The specifications for routing traffic and applying associated policies.

JSON representation  
---  
      
    
    {
      "destinations": [
        {
          object ([RouteDestination](https://docs.cloud.google.com/service-mesh/v1.28/docs/reference/network-services/rest/v1/projects.locations.tlsRoutes#RouteDestination))
        }
      ],
      "idleTimeout": string
    }  
  
Fields  
---  
`destinations[]` |  `object (`[RouteDestination](https://docs.cloud.google.com/service-mesh/v1.28/docs/reference/network-services/rest/v1/projects.locations.tlsRoutes#RouteDestination)`)` Required. The destination services to which traffic should be forwarded. At least one destination service is required.  
`idleTimeout` |  `string (`[Duration](https://protobuf.dev/reference/protobuf/google.protobuf/#duration)` format)` Optional. Specifies the idle timeout for the selected route. The idle timeout is defined as the period in which there are no bytes sent or received on either the upstream or downstream connection. If not set, the default idle timeout is 1 hour. If set to 0s, the timeout will be disabled.A duration in seconds with up to nine fractional digits, ending with '`s`'. Example: `"3.5s"`.  
  
## RouteDestination

Describe the destination for traffic to be routed to.

JSON representation  
---  
      
    
    {
      "serviceName": string,
      "weight": integer
    }  
  
Fields  
---  
`serviceName` |  `string` Required. The URL of a BackendService to route traffic to.  
`weight` |  `integer` Optional. Specifies the proportion of requests forwarded to the backend referenced by the serviceName field. This is computed as: - weight/Sum(weights in destinations) Weights in all destinations does not need to sum up to 100.  
  
## Methods  
  
---  
  
### `[create](https://docs.cloud.google.com/service-mesh/v1.28/docs/reference/network-services/rest/v1/projects.locations.tlsRoutes/create)`

|  Creates a new TlsRoute in a given project and location.  
  
### `[delete](https://docs.cloud.google.com/service-mesh/v1.28/docs/reference/network-services/rest/v1/projects.locations.tlsRoutes/delete)`

|  Deletes a single TlsRoute.  
  
### `[get](https://docs.cloud.google.com/service-mesh/v1.28/docs/reference/network-services/rest/v1/projects.locations.tlsRoutes/get)`

|  Gets details of a single TlsRoute.  
  
### `[list](https://docs.cloud.google.com/service-mesh/v1.28/docs/reference/network-services/rest/v1/projects.locations.tlsRoutes/list)`

|  Lists TlsRoute in a given project and location.  
  
### `[patch](https://docs.cloud.google.com/service-mesh/v1.28/docs/reference/network-services/rest/v1/projects.locations.tlsRoutes/patch)`

|  Updates the parameters of a single TlsRoute.  
  
### `[setIamPolicy](https://docs.cloud.google.com/service-mesh/v1.28/docs/reference/network-services/rest/v1/projects.locations.tlsRoutes/setIamPolicy)`

|  Sets the access control policy on the specified resource.  
  
### `[testIamPermissions](https://docs.cloud.google.com/service-mesh/v1.28/docs/reference/network-services/rest/v1/projects.locations.tlsRoutes/testIamPermissions)`

|  Returns permissions that a caller has on the specified resource.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-04-28 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-04-28 UTC."],[],[]] 
