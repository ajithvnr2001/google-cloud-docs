---
url: https://docs.cloud.google.com/service-mesh/v1.21/docs/reference/network-services/rest/v1/projects.locations.tcpRoutes
title: REST Resource: projects.locations.tcpRoutes \u00a0|\u00a0 Cloud Service Mesh v1.21 \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T19:07:15.673051+00:00
---

# REST Resource: projects.locations.tcpRoutes  |  Cloud Service Mesh v1.21  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/service-mesh/v1.21/docs/reference/network-services/rest/v1/projects.locations.tcpRoutes

You are viewing archived v1.21 Service Mesh documentation.

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
  * [ v1.21 ](https://docs.cloud.google.com/service-mesh/v1.21/docs)



Send feedback 

#  REST Resource: projects.locations.tcpRoutes Stay organized with collections  Save and categorize content based on your preferences. 

  * Resource: TcpRoute
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



## Resource: TcpRoute

TcpRoute is the resource defining how TCP traffic should be routed by a Mesh/Gateway resource.

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
          object ([RouteRule](https://docs.cloud.google.com/service-mesh/v1.21/docs/reference/network-services/rest/v1/projects.locations.tcpRoutes#RouteRule))
        }
      ],
      "meshes": [
        string
      ],
      "gateways": [
        string
      ],
      "labels": {
        string: string,
        ...
      }
    }  
  
Fields  
---  
`name` |  `string` Required. Name of the TcpRoute resource. It matches pattern `projects/*/locations/global/tcpRoutes/tcp_route_name>`.  
`selfLink` |  `string` Output only. Server-defined URL of this resource  
`createTime` |  `string (`[Timestamp](https://developers.google.com/protocol-buffers/docs/reference/google.protobuf#google.protobuf.Timestamp)` format)` Output only. The timestamp when the resource was created.A timestamp in RFC3339 UTC "Zulu" format, with nanosecond resolution and up to nine fractional digits. Examples: `"2014-10-02T15:01:23Z"` and `"2014-10-02T15:01:23.045123456Z"`.  
`updateTime` |  `string (`[Timestamp](https://developers.google.com/protocol-buffers/docs/reference/google.protobuf#google.protobuf.Timestamp)` format)` Output only. The timestamp when the resource was updated.A timestamp in RFC3339 UTC "Zulu" format, with nanosecond resolution and up to nine fractional digits. Examples: `"2014-10-02T15:01:23Z"` and `"2014-10-02T15:01:23.045123456Z"`.  
`description` |  `string` Optional. A free-text description of the resource. Max length 1024 characters.  
`rules[]` |  `object (`[RouteRule](https://docs.cloud.google.com/service-mesh/v1.21/docs/reference/network-services/rest/v1/projects.locations.tcpRoutes#RouteRule)`)` Required. Rules that define how traffic is routed and handled. At least one RouteRule must be supplied. If there are multiple rules then the action taken will be the first rule to match.  
`meshes[]` |  `string` Optional. Meshes defines a list of meshes this TcpRoute is attached to, as one of the routing rules to route the requests served by the mesh.Each mesh reference should match the pattern: `projects/*/locations/global/meshes/<mesh_name>`The attached Mesh should be of a type SIDECAR  
`gateways[]` |  `string` Optional. Gateways defines a list of gateways this TcpRoute is attached to, as one of the routing rules to route the requests served by the gateway.Each gateway reference should match the pattern: `projects/*/locations/global/gateways/<gateway_name>`  
`labels` |  `map (key: string, value: string)` Optional. Set of label tags associated with the TcpRoute resource.An object containing a list of `"key": value` pairs. Example: `{ "name": "wrench", "mass": "1.3kg", "count": "3" }`.  
  
## RouteRule

Specifies how to match traffic and how to route traffic when traffic is matched.

JSON representation  
---  
      
    
    {
      "matches": [
        {
          object ([RouteMatch](https://docs.cloud.google.com/service-mesh/v1.21/docs/reference/network-services/rest/v1/projects.locations.tcpRoutes#RouteMatch))
        }
      ],
      "action": {
        object ([RouteAction](https://docs.cloud.google.com/service-mesh/v1.21/docs/reference/network-services/rest/v1/projects.locations.tcpRoutes#RouteAction))
      }
    }  
  
Fields  
---  
`matches[]` |  `object (`[RouteMatch](https://docs.cloud.google.com/service-mesh/v1.21/docs/reference/network-services/rest/v1/projects.locations.tcpRoutes#RouteMatch)`)` Optional. RouteMatch defines the predicate used to match requests to a given action. Multiple match types are "OR"ed for evaluation. If no routeMatch field is specified, this rule will unconditionally match traffic.  
`action` |  `object (`[RouteAction](https://docs.cloud.google.com/service-mesh/v1.21/docs/reference/network-services/rest/v1/projects.locations.tcpRoutes#RouteAction)`)` Required. The detailed rule defining how to route matched traffic.  
  
## RouteMatch

RouteMatch defines the predicate used to match requests to a given action. Multiple match types are "OR"ed for evaluation. If no routeMatch field is specified, this rule will unconditionally match traffic.

JSON representation  
---  
      
    
    {
      "address": string,
      "port": string
    }  
  
Fields  
---  
`address` |  `string` Required. Must be specified in the CIDR range format. A CIDR range consists of an IP Address and a prefix length to construct the subnet mask. By default, the prefix length is 32 (i.e. matches a single IP address). Only IPV4 addresses are supported. Examples: "10.0.0.1" - matches against this exact IP address. "10.0.0.0/8" - matches against any IP address within the 10.0.0.0 subnet and 255.255.255.0 mask. "0.0.0.0/0" - matches against any IP address'.  
`port` |  `string` Required. Specifies the destination port to match against.  
  
## RouteAction

The specifications for routing traffic and applying associated policies.

JSON representation  
---  
      
    
    {
      "destinations": [
        {
          object ([RouteDestination](https://docs.cloud.google.com/service-mesh/v1.21/docs/reference/network-services/rest/v1/projects.locations.tcpRoutes#RouteDestination))
        }
      ],
      "originalDestination": boolean,
      "idleTimeout": string
    }  
  
Fields  
---  
`destinations[]` |  `object (`[RouteDestination](https://docs.cloud.google.com/service-mesh/v1.21/docs/reference/network-services/rest/v1/projects.locations.tcpRoutes#RouteDestination)`)` Optional. The destination services to which traffic should be forwarded. At least one destination service is required. Only one of route destination or original destination can be set.  
`originalDestination` |  `boolean` Optional. If true, Router will use the destination IP and port of the original connection as the destination of the request. Default is false. Only one of route destinations or original destination can be set.  
`idleTimeout` |  `string (`[Duration](https://developers.google.com/protocol-buffers/docs/reference/google.protobuf#google.protobuf.Duration)` format)` Optional. Specifies the idle timeout for the selected route. The idle timeout is defined as the period in which there are no bytes sent or received on either the upstream or downstream connection. If not set, the default idle timeout is 30 seconds. If set to 0s, the timeout will be disabled.A duration in seconds with up to nine fractional digits, ending with '`s`'. Example: `"3.5s"`.  
  
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
`weight` |  `integer` Optional. Specifies the proportion of requests forwarded to the backend referenced by the serviceName field. This is computed as: - weight/Sum(weights in this destination list). For non-zero values, there may be some epsilon from the exact proportion defined here depending on the precision an implementation supports.If only one serviceName is specified and it has a weight greater than 0, 100% of the traffic is forwarded to that backend.If weights are specified for any one service name, they need to be specified for all of them.If weights are unspecified for all services, then, traffic is distributed in equal proportions to all of them.  
  
## Methods  
  
---  
  
### `[create](https://docs.cloud.google.com/service-mesh/v1.21/docs/reference/network-services/rest/v1/projects.locations.tcpRoutes/create)`

|  Creates a new TcpRoute in a given project and location.  
  
### `[delete](https://docs.cloud.google.com/service-mesh/v1.21/docs/reference/network-services/rest/v1/projects.locations.tcpRoutes/delete)`

|  Deletes a single TcpRoute.  
  
### `[get](https://docs.cloud.google.com/service-mesh/v1.21/docs/reference/network-services/rest/v1/projects.locations.tcpRoutes/get)`

|  Gets details of a single TcpRoute.  
  
### `[list](https://docs.cloud.google.com/service-mesh/v1.21/docs/reference/network-services/rest/v1/projects.locations.tcpRoutes/list)`

|  Lists TcpRoute in a given project and location.  
  
### `[patch](https://docs.cloud.google.com/service-mesh/v1.21/docs/reference/network-services/rest/v1/projects.locations.tcpRoutes/patch)`

|  Updates the parameters of a single TcpRoute.  
  
### `[setIamPolicy](https://docs.cloud.google.com/service-mesh/v1.21/docs/reference/network-services/rest/v1/projects.locations.tcpRoutes/setIamPolicy)`

|  Sets the access control policy on the specified resource.  
  
### `[testIamPermissions](https://docs.cloud.google.com/service-mesh/v1.21/docs/reference/network-services/rest/v1/projects.locations.tcpRoutes/testIamPermissions)`

|  Returns permissions that a caller has on the specified resource.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-06-18 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-06-18 UTC."],[],[]] 
