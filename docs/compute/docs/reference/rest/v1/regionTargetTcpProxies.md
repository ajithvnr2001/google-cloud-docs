---
url: https://docs.cloud.google.com/compute/docs/reference/rest/v1/regionTargetTcpProxies/
title: REST Resource: regionTargetTcpProxies \u00a0|\u00a0 Compute Engine \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:49:32.375871+00:00
---

# REST Resource: regionTargetTcpProxies  |  Compute Engine  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/compute/docs/reference/rest/v1/regionTargetTcpProxies/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ Compute Engine ](https://docs.cloud.google.com/compute/docs)
  * [ APIs & Reference ](https://docs.cloud.google.com/compute/docs/apis)



Send feedback 

#  REST Resource: regionTargetTcpProxies Stay organized with collections  Save and categorize content based on your preferences. 

  * Resource: TargetTcpProxy
    * JSON representation
  * Methods



## Resource: TargetTcpProxy

Represents a Target TCP Proxy resource.

A target TCP proxy is a component of a Proxy Network Load Balancer. The forwarding rule references the target TCP proxy, and the target proxy then references a backend service. For more information, read [Proxy Network Load Balancer overview](https://docs.cloud.google.com/load-balancing/docs/proxy-network-load-balancer).

JSON representation  
---  
      
    
    {
      "kind": string,
      "id": string,
      "creationTimestamp": string,
      "name": string,
      "description": string,
      "selfLink": string,
      "service": string,
      "proxyHeader": enum,
      "proxyBind": boolean,
      "region": string,
      "loadBalancingScheme": enum
    }  
  
Fields  
---  
`kind` |  `string` Output only. Type of the resource. Always `compute#targetTcpProxy` for target TCP proxies.  
`id` |  `string ([uint64](https://developers.google.com/discovery/v1/type-format) format)` Output only. The unique identifier for the resource. This identifier is defined by the server.  
`creationTimestamp` |  `string` Output only. Creation timestamp in [RFC3339](https://www.ietf.org/rfc/rfc3339.txt) text format.  
`name` |  `string` Name of the resource. Provided by the client when the resource is created. The name must be 1-63 characters long, and comply with [RFC1035](https://www.ietf.org/rfc/rfc1035.txt). Specifically, the name must be 1-63 characters long and match the regular expression `[a-z]([-a-z0-9]*[a-z0-9])?` which means the first character must be a lowercase letter, and all following characters must be a dash, lowercase letter, or digit, except the last character, which cannot be a dash.  
`description` |  `string` An optional description of this resource. Provide this property when you create the resource.  
`selfLink` |  `string` Output only. Server-defined URL for the resource.  
`service` |  `string` URL to the BackendService resource.  
`proxyHeader` |  `enum` Specifies the type of proxy header to append before sending data to the backend, either `NONE` or `PROXY_V1`. The default is `NONE`.  
`proxyBind` |  `boolean` This field only applies when the forwarding rule that references this target proxy has a `loadBalancingScheme` set to `INTERNAL_SELF_MANAGED`.When this field is set to `true`, Envoy proxies set up inbound traffic interception and bind to the IP address and port specified in the forwarding rule. This is generally useful when using Traffic Director to configure Envoy as a gateway or middle proxy (in other words, not a sidecar proxy). The Envoy proxy listens for inbound requests and handles requests when it receives them.The default is `false`.  
`region` |  `string` Output only. URL of the region where the regional TCP proxy resides. This field is not applicable to global TCP proxy.  
`loadBalancingScheme` |  `enum` Specifies the type of load balancing scheme used by this target proxy.  
  
## Methods  
  
---  
  
### `[delete](https://docs.cloud.google.com/compute/docs/reference/rest/v1/regionTargetTcpProxies/delete)`

|  Deletes the specified TargetTcpProxy resource.  
  
### `[get](https://docs.cloud.google.com/compute/docs/reference/rest/v1/regionTargetTcpProxies/get)`

|  Returns the specified TargetTcpProxy resource.  
  
### `[insert](https://docs.cloud.google.com/compute/docs/reference/rest/v1/regionTargetTcpProxies/insert)`

|  Creates a TargetTcpProxy resource in the specified project and region using the data included in the request.  
  
### `[list](https://docs.cloud.google.com/compute/docs/reference/rest/v1/regionTargetTcpProxies/list)`

|  Retrieves a list of `TargetTcpProxy` resources available to the specified project in a given region.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-07-17 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-07-17 UTC."],[],[]] 
