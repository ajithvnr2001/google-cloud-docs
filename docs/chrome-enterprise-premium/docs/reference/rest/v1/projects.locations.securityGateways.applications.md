---
url: https://docs.cloud.google.com/chrome-enterprise-premium/docs/reference/rest/v1/projects.locations.securityGateways.applications
title: REST Resource: projects.locations.securityGateways.applications \u00a0|\u00a0 Chrome Enterprise Premium \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T17:36:12.383456+00:00
---

# REST Resource: projects.locations.securityGateways.applications  |  Chrome Enterprise Premium  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chrome-enterprise-premium/docs/reference/rest/v1/projects.locations.securityGateways.applications

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Chrome Enterprise Premium ](https://docs.cloud.google.com/chrome-enterprise-premium/docs)
  * [ Reference ](https://docs.cloud.google.com/chrome-enterprise-premium/docs/reference)



Send feedback 

#  REST Resource: projects.locations.securityGateways.applications Stay organized with collections  Save and categorize content based on your preferences. 

  * Resource: Application
    * JSON representation
  * EndpointMatcher
    * JSON representation
  * Upstream
    * JSON representation
  * Network
    * JSON representation
  * External
    * JSON representation
  * Endpoint
    * JSON representation
  * EgressPolicy
    * JSON representation
  * Schema
  * Methods



## Resource: Application

The information about an application resource.

JSON representation  
---  
      
    
    {
      "name": string,
      "endpointMatchers": [
        {
          object ([EndpointMatcher](https://docs.cloud.google.com/chrome-enterprise-premium/docs/reference/rest/v1/projects.locations.securityGateways.applications#EndpointMatcher))
        }
      ],
      "createTime": string,
      "updateTime": string,
      "displayName": string,
      "upstreams": [
        {
          object ([Upstream](https://docs.cloud.google.com/chrome-enterprise-premium/docs/reference/rest/v1/projects.locations.securityGateways.applications#Upstream))
        }
      ],
      "schema": enum ([Schema](https://docs.cloud.google.com/chrome-enterprise-premium/docs/reference/rest/v1/projects.locations.securityGateways.applications#Schema))
    }  
  
Fields  
---  
`name` |  `string` Identifier. Name of the resource.  
`endpointMatchers[]` |  `object (`[EndpointMatcher](https://docs.cloud.google.com/chrome-enterprise-premium/docs/reference/rest/v1/projects.locations.securityGateways.applications#EndpointMatcher)`)` Optional. An array of conditions to match the application's network endpoint. Each element in the array is an EndpointMatcher object, which defines a specific combination of a hostname pattern and one or more ports. The application is considered matched if at least one of the EndpointMatcher conditions in this array is met (the conditions are combined using OR logic). Each EndpointMatcher must contain a hostname pattern, such as "example.com", and one or more port numbers specified as a string, such as "443".Hostname and port number examples: "*.example.com", "443" "example.com" and "22" "example.com" and "22,33"  
`createTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Output only. Timestamp when the resource was created.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`updateTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Output only. Timestamp when the resource was last modified.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`displayName` |  `string` Optional. An arbitrary user-provided name for the application resource. Cannot exceed 64 characters.  
`upstreams[]` |  `object (`[Upstream](https://docs.cloud.google.com/chrome-enterprise-premium/docs/reference/rest/v1/projects.locations.securityGateways.applications#Upstream)`)` Optional. Which upstream resources to forward traffic to.  
`schema` |  `enum (`[Schema](https://docs.cloud.google.com/chrome-enterprise-premium/docs/reference/rest/v1/projects.locations.securityGateways.applications#Schema)`)` Optional. Type of the external application.  
  
## EndpointMatcher

EndpointMatcher contains the information of the endpoint that will match the application.

JSON representation  
---  
      
    
    {
      "hostname": string,
      "ports": [
        integer
      ]
    }  
  
Fields  
---  
`hostname` |  `string` Required. Hostname of the application.  
`ports[]` |  `integer` Required. The ports of the application.  
  
## Upstream

Which upstream resource to forward traffic to.

JSON representation  
---  
      
    
    {
      "proxyProtocol": {
        object ([ProxyProtocolConfig](https://docs.cloud.google.com/chrome-enterprise-premium/docs/reference/rest/v1/ProxyProtocolConfig))
      },
      "egressPolicy": {
        object ([EgressPolicy](https://docs.cloud.google.com/chrome-enterprise-premium/docs/reference/rest/v1/projects.locations.securityGateways.applications#EgressPolicy))
      },
    
      // Union field target can be only one of the following:
      "network": {
        object ([Network](https://docs.cloud.google.com/chrome-enterprise-premium/docs/reference/rest/v1/projects.locations.securityGateways.applications#Network))
      },
      "external": {
        object ([External](https://docs.cloud.google.com/chrome-enterprise-premium/docs/reference/rest/v1/projects.locations.securityGateways.applications#External))
      }
      // End of list of possible types for union field target.
    }  
  
Fields  
---  
`proxyProtocol` |  `object (`[ProxyProtocolConfig](https://docs.cloud.google.com/chrome-enterprise-premium/docs/reference/rest/v1/ProxyProtocolConfig)`)` Optional. Enables proxy protocol configuration for the upstream.  
`egressPolicy` |  `object (`[EgressPolicy](https://docs.cloud.google.com/chrome-enterprise-premium/docs/reference/rest/v1/projects.locations.securityGateways.applications#EgressPolicy)`)` Optional. Routing policy information.  
Union field `target`. The target of the upstream resource. `target` can be only one of the following:  
`network` |  `object (`[Network](https://docs.cloud.google.com/chrome-enterprise-premium/docs/reference/rest/v1/projects.locations.securityGateways.applications#Network)`)` Network to forward traffic to.  
`external` |  `object (`[External](https://docs.cloud.google.com/chrome-enterprise-premium/docs/reference/rest/v1/projects.locations.securityGateways.applications#External)`)` List of the external endpoints to forward traffic to.  
  
## Network

Network to forward traffic to.

JSON representation  
---  
      
    
    {
      "name": string
    }  
  
Fields  
---  
`name` |  `string` Required. Network name is of the format: `projects/{project}/global/networks/{network}  
  
## External

Endpoints to forward traffic to.

JSON representation  
---  
      
    
    {
      "endpoints": [
        {
          object ([Endpoint](https://docs.cloud.google.com/chrome-enterprise-premium/docs/reference/rest/v1/projects.locations.securityGateways.applications#Endpoint))
        }
      ]
    }  
  
Fields  
---  
`endpoints[]` |  `object (`[Endpoint](https://docs.cloud.google.com/chrome-enterprise-premium/docs/reference/rest/v1/projects.locations.securityGateways.applications#Endpoint)`)` Required. List of the endpoints to forward traffic to.  
  
## Endpoint

Internet Gateway endpoint to forward traffic to.

JSON representation  
---  
      
    
    {
      "hostname": string,
      "port": integer
    }  
  
Fields  
---  
`hostname` |  `string` Required. Hostname of the endpoint.  
`port` |  `integer` Required. Port of the endpoint.  
  
## EgressPolicy

Routing policy information.

JSON representation  
---  
      
    
    {
      "regions": [
        string
      ]
    }  
  
Fields  
---  
`regions[]` |  `string` Required. List of the regions where the application sends traffic.  
  
## Schema

Defines the type of external application.

Enums  
---  
`SCHEMA_UNSPECIFIED` | Default value. This value is unused.  
`PROXY_GATEWAY` | Proxy which routes traffic to actual applications, like Netscaler Gateway.  
`API_GATEWAY` | Service Discovery API endpoint when Service Discovery is enabled in Gateway.  
  
## Methods  
  
---  
  
### `[create](https://docs.cloud.google.com/chrome-enterprise-premium/docs/reference/rest/v1/projects.locations.securityGateways.applications/create)`

|  Creates a new Application in a given project and location.  
  
### `[delete](https://docs.cloud.google.com/chrome-enterprise-premium/docs/reference/rest/v1/projects.locations.securityGateways.applications/delete)`

|  Deletes a single application.  
  
### `[get](https://docs.cloud.google.com/chrome-enterprise-premium/docs/reference/rest/v1/projects.locations.securityGateways.applications/get)`

|  Gets details of a single Application.  
  
### `[getIamPolicy](https://docs.cloud.google.com/chrome-enterprise-premium/docs/reference/rest/v1/projects.locations.securityGateways.applications/getIamPolicy)`

|  Gets the access control policy for a resource.  
  
### `[list](https://docs.cloud.google.com/chrome-enterprise-premium/docs/reference/rest/v1/projects.locations.securityGateways.applications/list)`

|  Lists Applications in a given project and location.  
  
### `[patch](https://docs.cloud.google.com/chrome-enterprise-premium/docs/reference/rest/v1/projects.locations.securityGateways.applications/patch)`

|  Updates the parameters of a single Application.  
  
### `[setIamPolicy](https://docs.cloud.google.com/chrome-enterprise-premium/docs/reference/rest/v1/projects.locations.securityGateways.applications/setIamPolicy)`

|  Sets the access control policy on the specified resource.  
  
### `[testIamPermissions](https://docs.cloud.google.com/chrome-enterprise-premium/docs/reference/rest/v1/projects.locations.securityGateways.applications/testIamPermissions)`

|  Returns permissions that a caller has on the specified resource.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-03-02 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-03-02 UTC."],[],[]] 
