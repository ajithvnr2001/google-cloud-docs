---
url: https://docs.cloud.google.com/service-mesh/v1.28/docs/reference/network-services/rest/v1/projects.locations.gateways
title: REST Resource: projects.locations.gateways \u00a0|\u00a0 Cloud Service Mesh \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T14:31:21.382252+00:00
---

# REST Resource: projects.locations.gateways  |  Cloud Service Mesh  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/service-mesh/v1.28/docs/reference/network-services/rest/v1/projects.locations.gateways

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

#  REST Resource: projects.locations.gateways Stay organized with collections  Save and categorize content based on your preferences. 

  * Resource: Gateway
    * JSON representation
  * Type
  * IpVersion
  * RoutingMode
  * Methods



## Resource: Gateway

Gateway represents the configuration for a proxy, typically a load balancer. It captures the ip:port over which the services are exposed by the proxy, along with any policy configurations. Routes have reference to to Gateways to dictate how requests should be routed by this Gateway.

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
      "type": enum ([Type](https://docs.cloud.google.com/service-mesh/v1.28/docs/reference/network-services/rest/v1/projects.locations.gateways#Type)),
      "addresses": [
        string
      ],
      "ports": [
        integer
      ],
      "allPorts": boolean,
      "scope": string,
      "serverTlsPolicy": string,
      "certificateUrls": [
        string
      ],
      "gatewaySecurityPolicy": string,
      "network": string,
      "subnetwork": string,
      "ipVersion": enum ([IpVersion](https://docs.cloud.google.com/service-mesh/v1.28/docs/reference/network-services/rest/v1/projects.locations.gateways#IpVersion)),
      "routingMode": enum ([RoutingMode](https://docs.cloud.google.com/service-mesh/v1.28/docs/reference/network-services/rest/v1/projects.locations.gateways#RoutingMode)),
      "allowGlobalAccess": boolean,
      "envoyHeaders": enum ([EnvoyHeaders](https://docs.cloud.google.com/service-mesh/v1.28/docs/reference/network-services/rest/v1/EnvoyHeaders))
    }  
  
Fields  
---  
`name` |  `string` Identifier. Name of the Gateway resource. It matches pattern `projects/*/locations/*/gateways/<gateway_name>`.  
`selfLink` |  `string` Output only. Server-defined URL of this resource  
`createTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Output only. The timestamp when the resource was created.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`updateTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Output only. The timestamp when the resource was updated.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`labels` |  `map (key: string, value: string)` Optional. Set of label tags associated with the Gateway resource.An object containing a list of `"key": value` pairs. Example: `{ "name": "wrench", "mass": "1.3kg", "count": "3" }`.  
`description` |  `string` Optional. A free-text description of the resource. Max length 1024 characters.  
`type` |  `enum (`[Type](https://docs.cloud.google.com/service-mesh/v1.28/docs/reference/network-services/rest/v1/projects.locations.gateways#Type)`)` Immutable. The type of the customer managed gateway. This field is required. If unspecified, an error is returned.  
`addresses[]` |  `string` Optional. Zero or one IPv4 or IPv6 address on which the Gateway will receive the traffic. When no address is provided, an IP from the subnetwork is allocatedThis field only applies to gateways of type 'SECURE_WEB_GATEWAY'. Gateways of type 'OPEN_MESH' listen on 0.0.0.0 for IPv4 and :: for IPv6.  
`ports[]` |  `integer` Required. One or more port numbers (1-65535), on which the Gateway will receive traffic. The proxy binds to the specified ports. Gateways of type 'SECURE_WEB_GATEWAY' are limited to 5 ports. Gateways of type 'OPEN_MESH' listen on 0.0.0.0 for IPv4 and :: for IPv6 and support multiple ports.  
`allPorts` |  `boolean` Optional. If true, the Gateway will listen on all ports. This is mutually exclusive with the `ports` field. This field only applies to gateways of type 'SECURE_WEB_GATEWAY'.  
`scope` |  `string` Optional. Scope determines how configuration across multiple Gateway instances are merged. The configuration for multiple Gateway instances with the same scope will be merged as presented as a single configuration to the proxy/load balancer.Max length 64 characters. Scope should start with a letter and can only have letters, numbers, hyphens.  
`serverTlsPolicy` |  `string` Optional. A fully-qualified ServerTLSPolicy URL reference. Specifies how TLS traffic is terminated. If empty, TLS termination is disabled.  
`certificateUrls[]` |  `string` Optional. A fully-qualified Certificates URL reference. The proxy presents a Certificate (selected based on SNI) when establishing a TLS connection. This feature only applies to gateways of type 'SECURE_WEB_GATEWAY'.  
`gatewaySecurityPolicy` |  `string` Optional. A fully-qualified GatewaySecurityPolicy URL reference. Defines how a server should apply security policy to inbound (VM to Proxy) initiated connections.For example: `projects/*/locations/*/gatewaySecurityPolicies/swg-policy`.This policy is specific to gateways of type 'SECURE_WEB_GATEWAY'.  
`network` |  `string` Optional. The relative resource name identifying the VPC network that is using this configuration. For example: `projects/*/global/networks/network-1`.Currently, this field is specific to gateways of type 'SECURE_WEB_GATEWAY'.  
`subnetwork` |  `string` Optional. The relative resource name identifying the subnetwork in which this SWG is allocated. For example: `projects/*/regions/us-central1/subnetworks/network-1`Currently, this field is specific to gateways of type 'SECURE_WEB_GATEWAY".  
`ipVersion` |  `enum (`[IpVersion](https://docs.cloud.google.com/service-mesh/v1.28/docs/reference/network-services/rest/v1/projects.locations.gateways#IpVersion)`)` Optional. The IP Version that will be used by this gateway. Valid options are IPV4 or IPV6. Default is IPV4.  
`routingMode` |  `enum (`[RoutingMode](https://docs.cloud.google.com/service-mesh/v1.28/docs/reference/network-services/rest/v1/projects.locations.gateways#RoutingMode)`)` Optional. The routing mode of the Gateway. This field is configurable only for gateways of type SECURE_WEB_GATEWAY. This field is required for gateways of type SECURE_WEB_GATEWAY.  
`allowGlobalAccess` |  `boolean` Optional. If true, the gateway will allow traffic from clients outside of the region where the gateway is located. This field is configurable only for gateways of type SECURE_WEB_GATEWAY.  
`envoyHeaders` |  `enum (`[EnvoyHeaders](https://docs.cloud.google.com/service-mesh/v1.28/docs/reference/network-services/rest/v1/EnvoyHeaders)`)` Optional. Determines if envoy will insert internal debug headers into upstream requests. Other Envoy headers may still be injected. By default, envoy will not insert any debug headers.  
  
## Type

The type of the customer-managed gateway. Possible values are: * OPEN_MESH * SECURE_WEB_GATEWAY

Enums  
---  
`TYPE_UNSPECIFIED` | The type of the customer managed gateway is unspecified.  
`OPEN_MESH` | The type of the customer managed gateway is TrafficDirector Open Mesh.  
`SECURE_WEB_GATEWAY` | The type of the customer managed gateway is SecureWebGateway (SWG).  
  
## IpVersion

The types of IP version for the gateway. Possible values are: * IPV4 * IPV6

Enums  
---  
`IP_VERSION_UNSPECIFIED` | The type when IP version is not specified. Defaults to IPV4.  
`IPV4` | The type for IP version 4.  
`IPV6` | The type for IP version 6.  
  
## RoutingMode

The routing mode of the Gateway, to determine how the Gateway routes traffic. Today, this field only applies to Gateways of type SECURE_WEB_GATEWAY. Possible values are: * EXPLICIT_ROUTING_MODE * NEXT_HOP_ROUTING_MODE

Enums  
---  
`EXPLICIT_ROUTING_MODE` | The routing mode is explicit; clients are configured to send traffic through the gateway. This is the default routing mode.  
`NEXT_HOP_ROUTING_MODE` | The routing mode is next-hop. Clients are unaware of the gateway, and a route (advanced route or other route type) can be configured to direct traffic from client to gateway. The gateway then acts as a next-hop to the destination.  
  
## Methods  
  
---  
  
### `[create](https://docs.cloud.google.com/service-mesh/v1.28/docs/reference/network-services/rest/v1/projects.locations.gateways/create)`

|  Creates a new Gateway in a given project and location.  
  
### `[delete](https://docs.cloud.google.com/service-mesh/v1.28/docs/reference/network-services/rest/v1/projects.locations.gateways/delete)`

|  Deletes a single Gateway.  
  
### `[get](https://docs.cloud.google.com/service-mesh/v1.28/docs/reference/network-services/rest/v1/projects.locations.gateways/get)`

|  Gets details of a single Gateway.  
  
### `[list](https://docs.cloud.google.com/service-mesh/v1.28/docs/reference/network-services/rest/v1/projects.locations.gateways/list)`

|  Lists Gateways in a given project and location.  
  
### `[patch](https://docs.cloud.google.com/service-mesh/v1.28/docs/reference/network-services/rest/v1/projects.locations.gateways/patch)`

|  Updates the parameters of a single Gateway.  
  
### `[setIamPolicy](https://docs.cloud.google.com/service-mesh/v1.28/docs/reference/network-services/rest/v1/projects.locations.gateways/setIamPolicy)`

|  Sets the access control policy on the specified resource.  
  
### `[testIamPermissions](https://docs.cloud.google.com/service-mesh/v1.28/docs/reference/network-services/rest/v1/projects.locations.gateways/testIamPermissions)`

|  Returns permissions that a caller has on the specified resource.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-04-28 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-04-28 UTC."],[],[]] 
