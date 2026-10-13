---
url: https://docs.cloud.google.com/service-mesh/v1.23/docs/reference/network-services/rest/v1/projects.locations.grpcRoutes
title: REST Resource: projects.locations.grpcRoutes \u00a0|\u00a0 Cloud Service Mesh v1.23 \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T16:24:44.780761+00:00
---

# REST Resource: projects.locations.grpcRoutes  |  Cloud Service Mesh v1.23  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/service-mesh/v1.23/docs/reference/network-services/rest/v1/projects.locations.grpcRoutes

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

#  REST Resource: projects.locations.grpcRoutes Stay organized with collections  Save and categorize content based on your preferences. 

  * Resource: GrpcRoute
    * JSON representation
  * RouteRule
    * JSON representation
  * RouteMatch
    * JSON representation
  * MethodMatch
    * JSON representation
  * Type
  * HeaderMatch
    * JSON representation
  * Type
  * RouteAction
    * JSON representation
  * Destination
    * JSON representation
  * FaultInjectionPolicy
    * JSON representation
  * Delay
    * JSON representation
  * Abort
    * JSON representation
  * RetryPolicy
    * JSON representation
  * StatefulSessionAffinityPolicy
    * JSON representation
  * Methods



## Resource: GrpcRoute

GrpcRoute is the resource defining how gRPC traffic routed by a Mesh or Gateway resource is routed.

JSON representation  
---  
      
    
    {
      "name": string,
      "selfLink": string,
      "createTime": string,
      "updateTime": string,
      "labels": {
        string: string,
        ...
      },
      "description": string,
      "hostnames": [
        string
      ],
      "meshes": [
        string
      ],
      "gateways": [
        string
      ],
      "rules": [
        {
          object ([RouteRule](https://docs.cloud.google.com/service-mesh/v1.23/docs/reference/network-services/rest/v1/projects.locations.grpcRoutes#RouteRule))
        }
      ]
    }  
  
Fields  
---  
`name` |  `string` Required. Name of the GrpcRoute resource. It matches pattern `projects/*/locations/global/grpcRoutes/<grpc_route_name>`  
`selfLink` |  `string` Output only. Server-defined URL of this resource  
`createTime` |  `string (`[Timestamp](https://developers.google.com/protocol-buffers/docs/reference/google.protobuf#google.protobuf.Timestamp)` format)` Output only. The timestamp when the resource was created.A timestamp in RFC3339 UTC "Zulu" format, with nanosecond resolution and up to nine fractional digits. Examples: `"2014-10-02T15:01:23Z"` and `"2014-10-02T15:01:23.045123456Z"`.  
`updateTime` |  `string (`[Timestamp](https://developers.google.com/protocol-buffers/docs/reference/google.protobuf#google.protobuf.Timestamp)` format)` Output only. The timestamp when the resource was updated.A timestamp in RFC3339 UTC "Zulu" format, with nanosecond resolution and up to nine fractional digits. Examples: `"2014-10-02T15:01:23Z"` and `"2014-10-02T15:01:23.045123456Z"`.  
`labels` |  `map (key: string, value: string)` Optional. Set of label tags associated with the GrpcRoute resource.An object containing a list of `"key": value` pairs. Example: `{ "name": "wrench", "mass": "1.3kg", "count": "3" }`.  
`description` |  `string` Optional. A free-text description of the resource. Max length 1024 characters.  
`hostnames[]` |  `string` Required. Service hostnames with an optional port for which this route describes traffic.Format: [:]Hostname is the fully qualified domain name of a network host. This matches the RFC 1123 definition of a hostname with 2 notable exceptions: - IPs are not allowed. - A hostname may be prefixed with a wildcard label (`*.`). The wildcard label must appear by itself as the first label.Hostname can be "precise" which is a domain name without the terminating dot of a network host (e.g. `foo.example.com`) or "wildcard", which is a domain name prefixed with a single wildcard label (e.g. `*.example.com`).Note that as per RFC1035 and RFC1123, a label must consist of lower case alphanumeric characters or '-', and must start and end with an alphanumeric character. No other punctuation is allowed.The routes associated with a Mesh or Gateway must have unique hostnames. If you attempt to attach multiple routes with conflicting hostnames, the configuration will be rejected.For example, while it is acceptable for routes for the hostnames `*.foo.bar.com` and `*.bar.com` to be associated with the same route, it is not possible to associate two routes both with `*.bar.com` or both with `bar.com`.If a port is specified, then gRPC clients must use the channel URI with the port to match this rule (i.e. "xds:///service:123"), otherwise they must supply the URI without a port (i.e. "xds:///service").  
`meshes[]` |  `string` Optional. Meshes defines a list of meshes this GrpcRoute is attached to, as one of the routing rules to route the requests served by the mesh.Each mesh reference should match the pattern: `projects/*/locations/global/meshes/<mesh_name>`  
`gateways[]` |  `string` Optional. Gateways defines a list of gateways this GrpcRoute is attached to, as one of the routing rules to route the requests served by the gateway.Each gateway reference should match the pattern: `projects/*/locations/global/gateways/<gateway_name>`  
`rules[]` |  `object (`[RouteRule](https://docs.cloud.google.com/service-mesh/v1.23/docs/reference/network-services/rest/v1/projects.locations.grpcRoutes#RouteRule)`)` Required. A list of detailed rules defining how to route traffic.Within a single GrpcRoute, the GrpcRoute.RouteAction associated with the first matching GrpcRoute.RouteRule will be executed. At least one rule must be supplied.  
  
## RouteRule

Describes how to route traffic.

JSON representation  
---  
      
    
    {
      "matches": [
        {
          object ([RouteMatch](https://docs.cloud.google.com/service-mesh/v1.23/docs/reference/network-services/rest/v1/projects.locations.grpcRoutes#RouteMatch))
        }
      ],
      "action": {
        object ([RouteAction](https://docs.cloud.google.com/service-mesh/v1.23/docs/reference/network-services/rest/v1/projects.locations.grpcRoutes#RouteAction))
      }
    }  
  
Fields  
---  
`matches[]` |  `object (`[RouteMatch](https://docs.cloud.google.com/service-mesh/v1.23/docs/reference/network-services/rest/v1/projects.locations.grpcRoutes#RouteMatch)`)` Optional. Matches define conditions used for matching the rule against incoming gRPC requests. Each match is independent, i.e. this rule will be matched if ANY one of the matches is satisfied. If no matches field is specified, this rule will unconditionally match traffic.  
`action` |  `object (`[RouteAction](https://docs.cloud.google.com/service-mesh/v1.23/docs/reference/network-services/rest/v1/projects.locations.grpcRoutes#RouteAction)`)` Required. A detailed rule defining how to route traffic. This field is required.  
  
## RouteMatch

Criteria for matching traffic. A RouteMatch will be considered to match when all supplied fields match.

JSON representation  
---  
      
    
    {
      "headers": [
        {
          object ([HeaderMatch](https://docs.cloud.google.com/service-mesh/v1.23/docs/reference/network-services/rest/v1/projects.locations.grpcRoutes#HeaderMatch))
        }
      ],
      "method": {
        object ([MethodMatch](https://docs.cloud.google.com/service-mesh/v1.23/docs/reference/network-services/rest/v1/projects.locations.grpcRoutes#MethodMatch))
      }
    }  
  
Fields  
---  
`headers[]` |  `object (`[HeaderMatch](https://docs.cloud.google.com/service-mesh/v1.23/docs/reference/network-services/rest/v1/projects.locations.grpcRoutes#HeaderMatch)`)` Optional. Specifies a collection of headers to match.  
`method` |  `object (`[MethodMatch](https://docs.cloud.google.com/service-mesh/v1.23/docs/reference/network-services/rest/v1/projects.locations.grpcRoutes#MethodMatch)`)` Optional. A gRPC method to match against. If this field is empty or omitted, will match all methods.  
  
## MethodMatch

Specifies a match against a method.

JSON representation  
---  
      
    
    {
      "type": enum ([Type](https://docs.cloud.google.com/service-mesh/v1.23/docs/reference/network-services/rest/v1/projects.locations.grpcRoutes#Type)),
      "grpcService": string,
      "grpcMethod": string,
      "caseSensitive": boolean
    }  
  
Fields  
---  
`type` |  `enum (`[Type](https://docs.cloud.google.com/service-mesh/v1.23/docs/reference/network-services/rest/v1/projects.locations.grpcRoutes#Type)`)` Optional. Specifies how to match against the name. If not specified, a default value of "EXACT" is used.  
`grpcService` |  `string` Required. Name of the service to match against. If unspecified, will match all services.  
`grpcMethod` |  `string` Required. Name of the method to match against. If unspecified, will match all methods.  
`caseSensitive` |  `boolean` Optional. Specifies that matches are case sensitive. The default value is true. caseSensitive must not be used with a type of REGULAR_EXPRESSION.  
  
## Type

The type of the match.

Enums  
---  
`TYPE_UNSPECIFIED` | Unspecified.  
`EXACT` | Will only match the exact name provided.  
`REGULAR_EXPRESSION` | Will interpret grpcMethod and grpcService as regexes. RE2 syntax is supported.  
  
## HeaderMatch

A match against a collection of headers.

JSON representation  
---  
      
    
    {
      "type": enum ([Type](https://docs.cloud.google.com/service-mesh/v1.23/docs/reference/network-services/rest/v1/projects.locations.grpcRoutes#Type_1)),
      "key": string,
      "value": string
    }  
  
Fields  
---  
`type` |  `enum (`[Type](https://docs.cloud.google.com/service-mesh/v1.23/docs/reference/network-services/rest/v1/projects.locations.grpcRoutes#Type_1)`)` Optional. Specifies how to match against the value of the header. If not specified, a default value of EXACT is used.  
`key` |  `string` Required. The key of the header.  
`value` |  `string` Required. The value of the header.  
  
## Type

The type of match.

Enums  
---  
`TYPE_UNSPECIFIED` | Unspecified.  
`EXACT` | Will only match the exact value provided.  
`REGULAR_EXPRESSION` | Will match paths conforming to the prefix specified by value. RE2 syntax is supported.  
  
## RouteAction

Specifies how to route matched traffic.

JSON representation  
---  
      
    
    {
      "destinations": [
        {
          object ([Destination](https://docs.cloud.google.com/service-mesh/v1.23/docs/reference/network-services/rest/v1/projects.locations.grpcRoutes#Destination))
        }
      ],
      "faultInjectionPolicy": {
        object ([FaultInjectionPolicy](https://docs.cloud.google.com/service-mesh/v1.23/docs/reference/network-services/rest/v1/projects.locations.grpcRoutes#FaultInjectionPolicy))
      },
      "timeout": string,
      "retryPolicy": {
        object ([RetryPolicy](https://docs.cloud.google.com/service-mesh/v1.23/docs/reference/network-services/rest/v1/projects.locations.grpcRoutes#RetryPolicy))
      },
      "statefulSessionAffinity": {
        object ([StatefulSessionAffinityPolicy](https://docs.cloud.google.com/service-mesh/v1.23/docs/reference/network-services/rest/v1/projects.locations.grpcRoutes#StatefulSessionAffinityPolicy))
      },
      "idleTimeout": string
    }  
  
Fields  
---  
`destinations[]` |  `object (`[Destination](https://docs.cloud.google.com/service-mesh/v1.23/docs/reference/network-services/rest/v1/projects.locations.grpcRoutes#Destination)`)` Optional. The destination services to which traffic should be forwarded. If multiple destinations are specified, traffic will be split between Backend Service(s) according to the weight field of these destinations.  
`faultInjectionPolicy` |  `object (`[FaultInjectionPolicy](https://docs.cloud.google.com/service-mesh/v1.23/docs/reference/network-services/rest/v1/projects.locations.grpcRoutes#FaultInjectionPolicy)`)` Optional. The specification for fault injection introduced into traffic to test the resiliency of clients to destination service failure. As part of fault injection, when clients send requests to a destination, delays can be introduced on a percentage of requests before sending those requests to the destination service. Similarly requests from clients can be aborted by for a percentage of requests.timeout and retryPolicy will be ignored by clients that are configured with a faultInjectionPolicy  
`timeout` |  `string (`[Duration](https://developers.google.com/protocol-buffers/docs/reference/google.protobuf#google.protobuf.Duration)` format)` Optional. Specifies the timeout for selected route. Timeout is computed from the time the request has been fully processed (i.e. end of stream) up until the response has been completely processed. Timeout includes all retries.A duration in seconds with up to nine fractional digits, ending with '`s`'. Example: `"3.5s"`.  
`retryPolicy` |  `object (`[RetryPolicy](https://docs.cloud.google.com/service-mesh/v1.23/docs/reference/network-services/rest/v1/projects.locations.grpcRoutes#RetryPolicy)`)` Optional. Specifies the retry policy associated with this route.  
`statefulSessionAffinity` |  `object (`[StatefulSessionAffinityPolicy](https://docs.cloud.google.com/service-mesh/v1.23/docs/reference/network-services/rest/v1/projects.locations.grpcRoutes#StatefulSessionAffinityPolicy)`)` Optional. Specifies cookie-based stateful session affinity.  
`idleTimeout` |  `string (`[Duration](https://developers.google.com/protocol-buffers/docs/reference/google.protobuf#google.protobuf.Duration)` format)` Optional. Specifies the idle timeout for the selected route. The idle timeout is defined as the period in which there are no bytes sent or received on either the upstream or downstream connection. If not set, the default idle timeout is 1 hour. If set to 0s, the timeout will be disabled.A duration in seconds with up to nine fractional digits, ending with '`s`'. Example: `"3.5s"`.  
  
## Destination

The destination to which traffic will be routed.

JSON representation  
---  
      
    
    {
    
      // Union field destination_type can be only one of the following:
      "serviceName": string
      // End of list of possible types for union field destination_type.
      "weight": integer
    }  
  
Fields  
---  
Union field `destination_type`. Specifies the kind of destination to which traffic will be routed. `destination_type` can be only one of the following:  
`serviceName` |  `string` Required. The URL of a destination service to which to route traffic. Must refer to either a BackendService or ServiceDirectoryService.  
`weight` |  `integer` Optional. Specifies the proportion of requests forwarded to the backend referenced by the serviceName field. This is computed as: - weight/Sum(weights in this destination list). For non-zero values, there may be some epsilon from the exact proportion defined here depending on the precision an implementation supports.If only one serviceName is specified and it has a weight greater than 0, 100% of the traffic is forwarded to that backend.If weights are specified for any one service name, they need to be specified for all of them.If weights are unspecified for all services, then, traffic is distributed in equal proportions to all of them.  
  
## FaultInjectionPolicy

The specification for fault injection introduced into traffic to test the resiliency of clients to destination service failure. As part of fault injection, when clients send requests to a destination, delays can be introduced on a percentage of requests before sending those requests to the destination service. Similarly requests from clients can be aborted by for a percentage of requests.

JSON representation  
---  
      
    
    {
      "delay": {
        object ([Delay](https://docs.cloud.google.com/service-mesh/v1.23/docs/reference/network-services/rest/v1/projects.locations.grpcRoutes#Delay))
      },
      "abort": {
        object ([Abort](https://docs.cloud.google.com/service-mesh/v1.23/docs/reference/network-services/rest/v1/projects.locations.grpcRoutes#Abort))
      }
    }  
  
Fields  
---  
`delay` |  `object (`[Delay](https://docs.cloud.google.com/service-mesh/v1.23/docs/reference/network-services/rest/v1/projects.locations.grpcRoutes#Delay)`)` The specification for injecting delay to client requests.  
`abort` |  `object (`[Abort](https://docs.cloud.google.com/service-mesh/v1.23/docs/reference/network-services/rest/v1/projects.locations.grpcRoutes#Abort)`)` The specification for aborting to client requests.  
  
## Delay

Specification of how client requests are delayed as part of fault injection before being sent to a destination.

JSON representation  
---  
      
    
    {
      "fixedDelay": string,
      "percentage": integer
    }  
  
Fields  
---  
`fixedDelay` |  `string (`[Duration](https://developers.google.com/protocol-buffers/docs/reference/google.protobuf#google.protobuf.Duration)` format)` Specify a fixed delay before forwarding the request.A duration in seconds with up to nine fractional digits, ending with '`s`'. Example: `"3.5s"`.  
`percentage` |  `integer` The percentage of traffic on which delay will be injected.The value must be between [0, 100]  
  
## Abort

Specification of how client requests are aborted as part of fault injection before being sent to a destination.

JSON representation  
---  
      
    
    {
      "httpStatus": integer,
      "percentage": integer
    }  
  
Fields  
---  
`httpStatus` |  `integer` The HTTP status code used to abort the request.The value must be between 200 and 599 inclusive.  
`percentage` |  `integer` The percentage of traffic which will be aborted.The value must be between [0, 100]  
  
## RetryPolicy

The specifications for retries.

JSON representation  
---  
      
    
    {
      "retryConditions": [
        string
      ],
      "numRetries": integer
    }  
  
Fields  
---  
`retryConditions[]` |  `string`

  * connect-failure: Router will retry on failures connecting to Backend Services, for example due to connection timeouts.
  * refused-stream: Router will retry if the backend service resets the stream with a REFUSED_STREAM error code. This reset type indicates that it is safe to retry.
  * cancelled: Router will retry if the gRPC status code in the response header is set to cancelled
  * deadline-exceeded: Router will retry if the gRPC status code in the response header is set to deadline-exceeded
  * resource-exhausted: Router will retry if the gRPC status code in the response header is set to resource-exhausted
  * unavailable: Router will retry if the gRPC status code in the response header is set to unavailable

  
`numRetries` |  `integer ([uint32](https://developers.google.com/discovery/v1/type-format) format)` Specifies the allowed number of retries. This number must be > 0\. If not specified, default to 1.  
  
## StatefulSessionAffinityPolicy

The specification for cookie-based stateful session affinity where the date plane supplies a “session cookie” with the name "GSSA" which encodes a specific destination host and each request containing that cookie will be directed to that host as long as the destination host remains up and healthy.

The gRPC proxyless mesh library or sidecar proxy will manage the session cookie but the client application code is responsible for copying the cookie from each RPC in the session to the next.

JSON representation  
---  
      
    
    {
      "cookieTtl": string
    }  
  
Fields  
---  
`cookieTtl` |  `string (`[Duration](https://developers.google.com/protocol-buffers/docs/reference/google.protobuf#google.protobuf.Duration)` format)` Required. The cookie TTL value for the Set-Cookie header generated by the data plane. The lifetime of the cookie may be set to a value from 1 to 86400 seconds (24 hours) inclusive.A duration in seconds with up to nine fractional digits, ending with '`s`'. Example: `"3.5s"`.  
  
## Methods  
  
---  
  
### `[create](https://docs.cloud.google.com/service-mesh/v1.23/docs/reference/network-services/rest/v1/projects.locations.grpcRoutes/create)`

|  Creates a new GrpcRoute in a given project and location.  
  
### `[delete](https://docs.cloud.google.com/service-mesh/v1.23/docs/reference/network-services/rest/v1/projects.locations.grpcRoutes/delete)`

|  Deletes a single GrpcRoute.  
  
### `[get](https://docs.cloud.google.com/service-mesh/v1.23/docs/reference/network-services/rest/v1/projects.locations.grpcRoutes/get)`

|  Gets details of a single GrpcRoute.  
  
### `[list](https://docs.cloud.google.com/service-mesh/v1.23/docs/reference/network-services/rest/v1/projects.locations.grpcRoutes/list)`

|  Lists GrpcRoutes in a given project and location.  
  
### `[patch](https://docs.cloud.google.com/service-mesh/v1.23/docs/reference/network-services/rest/v1/projects.locations.grpcRoutes/patch)`

|  Updates the parameters of a single GrpcRoute.  
  
### `[setIamPolicy](https://docs.cloud.google.com/service-mesh/v1.23/docs/reference/network-services/rest/v1/projects.locations.grpcRoutes/setIamPolicy)`

|  Sets the access control policy on the specified resource.  
  
### `[testIamPermissions](https://docs.cloud.google.com/service-mesh/v1.23/docs/reference/network-services/rest/v1/projects.locations.grpcRoutes/testIamPermissions)`

|  Returns permissions that a caller has on the specified resource.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-06-18 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-06-18 UTC."],[],[]] 
