---
url: https://docs.cloud.google.com/compute/docs/reference/rest/v1/targetHttpProxies/
title: REST Resource: targetHttpProxies \u00a0|\u00a0 Compute Engine \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:37:02.791032+00:00
---

# REST Resource: targetHttpProxies  |  Compute Engine  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/compute/docs/reference/rest/v1/targetHttpProxies/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ Compute Engine ](https://docs.cloud.google.com/compute/docs)
  * [ APIs & Reference ](https://docs.cloud.google.com/compute/docs/apis)



Send feedback 

#  REST Resource: targetHttpProxies Stay organized with collections  Save and categorize content based on your preferences. 

  * Resource: TargetHttpProxy
    * JSON representation
  * Methods



## Resource: TargetHttpProxy

Represents a Target HTTP Proxy resource.

Google Compute Engine has two Target HTTP Proxy resources:

  * [Global](https://docs.cloud.google.com/compute/docs/reference/rest/v1/targetHttpProxies)
  * [Regional](https://docs.cloud.google.com/compute/docs/reference/rest/v1/regionTargetHttpProxies)



A target HTTP proxy is a component of Google Cloud HTTP load balancers.

  * targetHttpProxies are used by global external Application Load Balancers, classic Application Load Balancers, cross-region internal Application Load Balancers, and Traffic Director.
  * regionTargetHttpProxies are used by regional internal Application Load Balancers and regional external Application Load Balancers.



Forwarding rules reference a target HTTP proxy, and the target proxy then references a URL map. For more information, read [Using Target Proxies](https://docs.cloud.google.com/load-balancing/docs/target-proxies) and [ Forwarding rule concepts](https://docs.cloud.google.com/load-balancing/docs/forwarding-rule-concepts).

JSON representation  
---  
      
    
    {
      "kind": string,
      "id": string,
      "creationTimestamp": string,
      "name": string,
      "description": string,
      "selfLink": string,
      "urlMap": string,
      "region": string,
      "proxyBind": boolean,
      "fingerprint": string,
      "httpKeepAliveTimeoutSec": integer
    }  
  
Fields  
---  
`kind` |  `string` Output only. Type of resource. Always `compute#targetHttpProxy` for target HTTP proxies.  
`id` |  `string ([uint64](https://developers.google.com/discovery/v1/type-format) format)` Output only. The unique identifier for the resource. This identifier is defined by the server.  
`creationTimestamp` |  `string` Output only. Creation timestamp in [RFC3339](https://www.ietf.org/rfc/rfc3339.txt) text format.  
`name` |  `string` Name of the resource. Provided by the client when the resource is created. The name must be 1-63 characters long, and comply with [RFC1035](https://www.ietf.org/rfc/rfc1035.txt). Specifically, the name must be 1-63 characters long and match the regular expression `[a-z]([-a-z0-9]*[a-z0-9])?` which means the first character must be a lowercase letter, and all following characters must be a dash, lowercase letter, or digit, except the last character, which cannot be a dash.  
`description` |  `string` An optional description of this resource. Provide this property when you create the resource.  
`selfLink` |  `string` Output only. Server-defined URL for the resource.  
`urlMap` |  `string` URL to the UrlMap resource that defines the mapping from URL to the BackendService.  
`region` |  `string` Output only. URL of the region where the regional Target HTTP Proxy resides. This field is not applicable to global Target HTTP Proxies.  
`proxyBind` |  `boolean` This field only applies when the forwarding rule that references this target proxy has a `loadBalancingScheme` set to `INTERNAL_SELF_MANAGED`.When this field is set to `true`, Envoy proxies set up inbound traffic interception and bind to the IP address and port specified in the forwarding rule. This is generally useful when using Traffic Director to configure Envoy as a gateway or middle proxy (in other words, not a sidecar proxy). The Envoy proxy listens for inbound requests and handles requests when it receives them.The default is `false`.  
`fingerprint` |  `string ([bytes](https://developers.google.com/discovery/v1/type-format) format)` Fingerprint of this resource. A hash of the contents stored in this object. This field is used in optimistic locking. This field will be ignored when inserting a `TargetHttpProxy`. An up-to-date fingerprint must be provided in order to patch/update the TargetHttpProxy; otherwise, the request will fail with error `412 conditionNotMet`. To see the latest fingerprint, make a `get()` request to retrieve the TargetHttpProxy.A base64-encoded string.  
`httpKeepAliveTimeoutSec` |  `integer` Specifies how long to keep a connection open, after completing a response, while there is no matching traffic (in seconds). If an HTTP keep-alive is not specified, a default value (610 seconds) will be used.For global external Application Load Balancers, the minimum allowed value is 5 seconds and the maximum allowed value is 1200 seconds.For classic Application Load Balancers, this option is not supported.  
  
## Methods  
  
---  
  
### `[aggregatedList](https://docs.cloud.google.com/compute/docs/reference/rest/v1/targetHttpProxies/aggregatedList)`

|  Retrieves the list of all TargetHttpProxy resources, regional and global, available to the specified project.  
  
### `[delete](https://docs.cloud.google.com/compute/docs/reference/rest/v1/targetHttpProxies/delete)`

|  Deletes the specified TargetHttpProxy resource.  
  
### `[get](https://docs.cloud.google.com/compute/docs/reference/rest/v1/targetHttpProxies/get)`

|  Returns the specified TargetHttpProxy resource.  
  
### `[insert](https://docs.cloud.google.com/compute/docs/reference/rest/v1/targetHttpProxies/insert)`

|  Creates a TargetHttpProxy resource in the specified project using the data included in the request.  
  
### `[list](https://docs.cloud.google.com/compute/docs/reference/rest/v1/targetHttpProxies/list)`

|  Retrieves the list of TargetHttpProxy resources available to the specified project.  
  
### `[patch](https://docs.cloud.google.com/compute/docs/reference/rest/v1/targetHttpProxies/patch)`

|  Patches the specified TargetHttpProxy resource with the data included in the request.  
  
### `[setUrlMap](https://docs.cloud.google.com/compute/docs/reference/rest/v1/targetHttpProxies/setUrlMap)`

|  Changes the URL map for TargetHttpProxy.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-05-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-05-13 UTC."],[],[]] 
