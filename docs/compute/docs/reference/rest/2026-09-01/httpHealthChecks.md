---
url: https://docs.cloud.google.com/compute/docs/reference/rest/2026-09-01/httpHealthChecks/
title: REST Resource: httpHealthChecks \u00a0|\u00a0 Compute Engine \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:05:31.855893+00:00
---

# REST Resource: httpHealthChecks  |  Compute Engine  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/compute/docs/reference/rest/2026-09-01/httpHealthChecks/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ Compute Engine ](https://docs.cloud.google.com/compute/docs)
  * [ APIs & Reference ](https://docs.cloud.google.com/compute/docs/apis)



Send feedback 

#  REST Resource: httpHealthChecks Stay organized with collections  Save and categorize content based on your preferences. 

  * Resource: HttpHealthCheck
    * JSON representation
  * Methods



## Resource: HttpHealthCheck

Represents a legacy HTTP Health Check resource.

Legacy HTTP health checks are now only required by target pool-based network load balancers. For all other load balancers, including backend service-based network load balancers, and for managed instance group auto-healing, you must use modern (non-legacy) health checks.

For more information, see [Health checks overview](https://docs.cloud.google.com/load-balancing/docs/health-check-concepts).

JSON representation  
---  
      
    
    {
      "kind": string,
      "id": string,
      "creationTimestamp": string,
      "name": string,
      "description": string,
      "host": string,
      "requestPath": string,
      "port": integer,
      "checkIntervalSec": integer,
      "timeoutSec": integer,
      "unhealthyThreshold": integer,
      "healthyThreshold": integer,
      "selfLink": string
    }  
  
Fields  
---  
`kind` |  `string` Output only. Type of the resource. Always `compute#httpHealthCheck` for HTTP health checks.  
`id` |  `string ([uint64](https://developers.google.com/discovery/v1/type-format) format)` Output only. The unique identifier for the resource. This identifier is defined by the server.  
`creationTimestamp` |  `string` Output only. Creation timestamp in [RFC3339](https://www.ietf.org/rfc/rfc3339.txt) text format.  
`name` |  `string` Name of the resource. Provided by the client when the resource is created. The name must be 1-63 characters long, and comply with [RFC1035](https://www.ietf.org/rfc/rfc1035.txt). Specifically, the name must be 1-63 characters long and match the regular expression `[a-z]([-a-z0-9]*[a-z0-9])?` which means the first character must be a lowercase letter, and all following characters must be a dash, lowercase letter, or digit, except the last character, which cannot be a dash.  
`description` |  `string` An optional description of this resource. Provide this property when you create the resource.  
`host` |  `string` The value of the host header in the HTTP health check request. If left empty (default value), the public IP on behalf of which this health check is performed will be used.  
`requestPath` |  `string` The request path of the HTTP health check request. The default value is `/`. This field does not support query parameters. Must comply with [RFC3986](https://www.ietf.org/rfc/rfc3986.txt).  
`port` |  `integer` The TCP port number for the HTTP health check request. The default value is `80`.  
`checkIntervalSec` |  `integer` How often (in seconds) to send a health check. The default value is `5` seconds.  
`timeoutSec` |  `integer` How long (in seconds) to wait before claiming failure. The default value is `5` seconds. It is invalid for `timeoutSec` to have greater value than `checkIntervalSec`.  
`unhealthyThreshold` |  `integer` A so-far healthy instance will be marked unhealthy after this many consecutive failures. The default value is `2`.  
`healthyThreshold` |  `integer` A so-far unhealthy instance will be marked healthy after this many consecutive successes. The default value is `2`.  
`selfLink` |  `string` Output only. Server-defined URL for the resource.  
  
## Methods  
  
---  
  
### `[delete](https://docs.cloud.google.com/compute/docs/reference/rest/2026-09-01/httpHealthChecks/delete)`

|  Deletes the specified HttpHealthCheck resource.  
  
### `[get](https://docs.cloud.google.com/compute/docs/reference/rest/2026-09-01/httpHealthChecks/get)`

|  Returns the specified HttpHealthCheck resource.  
  
### `[insert](https://docs.cloud.google.com/compute/docs/reference/rest/2026-09-01/httpHealthChecks/insert)`

|  Creates a HttpHealthCheck resource in the specified project using the data included in the request.  
  
### `[list](https://docs.cloud.google.com/compute/docs/reference/rest/2026-09-01/httpHealthChecks/list)`

|  Retrieves the list of HttpHealthCheck resources available to the specified project.  
  
### `[patch](https://docs.cloud.google.com/compute/docs/reference/rest/2026-09-01/httpHealthChecks/patch)`

|  Updates a HttpHealthCheck resource in the specified project using the data included in the request.  
  
### `[testIamPermissions](https://docs.cloud.google.com/compute/docs/reference/rest/2026-09-01/httpHealthChecks/testIamPermissions)`

|  Returns permissions that a caller has on the specified resource.  
  
### `[update](https://docs.cloud.google.com/compute/docs/reference/rest/2026-09-01/httpHealthChecks/update)`

|  Updates a HttpHealthCheck resource in the specified project using the data included in the request.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-01 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-01 UTC."],[],[]] 
