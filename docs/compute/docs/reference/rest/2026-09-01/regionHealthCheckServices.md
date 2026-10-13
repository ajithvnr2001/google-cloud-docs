---
url: https://docs.cloud.google.com/compute/docs/reference/rest/2026-09-01/regionHealthCheckServices/
title: REST Resource: regionHealthCheckServices \u00a0|\u00a0 Compute Engine \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T19:07:12.087789+00:00
---

# REST Resource: regionHealthCheckServices  |  Compute Engine  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/compute/docs/reference/rest/2026-09-01/regionHealthCheckServices/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ Compute Engine ](https://docs.cloud.google.com/compute/docs)
  * [ APIs & Reference ](https://docs.cloud.google.com/compute/docs/apis)



Send feedback 

#  REST Resource: regionHealthCheckServices Stay organized with collections  Save and categorize content based on your preferences. 

  * Resource: HealthCheckService
    * JSON representation
  * Methods



## Resource: HealthCheckService

Represents a Health-Check as a Service resource.

JSON representation  
---  
      
    
    {
      "kind": string,
      "id": string,
      "creationTimestamp": string,
      "selfLink": string,
      "name": string,
      "description": string,
      "region": string,
      "healthStatusAggregationPolicy": enum,
      "healthChecks": [
        string
      ],
      "networkEndpointGroups": [
        string
      ],
      "notificationEndpoints": [
        string
      ],
      "fingerprint": string
    }  
  
Fields  
---  
`kind` |  `string` Output only. Type of the resource. Always `compute#healthCheckService`for health check services.  
`id` |  `string ([uint64](https://developers.google.com/discovery/v1/type-format) format)` Output only. The unique identifier for the resource. This identifier is defined by the server.  
`creationTimestamp` |  `string` Output only. Creation timestamp in [RFC3339](https://www.ietf.org/rfc/rfc3339.txt) text format.  
`selfLink` |  `string` Output only. Server-defined URL for the resource.  
`name` |  `string` Name of the resource. The name must be 1-63 characters long, and comply with [RFC1035](https://www.ietf.org/rfc/rfc1035.txt). Specifically, the name must be 1-63 characters long and match the regular expression `[a-z]([-a-z0-9]*[a-z0-9])?` which means the first character must be a lowercase letter, and all following characters must be a dash, lowercase letter, or digit, except the last character, which cannot be a dash.  
`description` |  `string` An optional description of this resource. Provide this property when you create the resource.  
`region` |  `string` Output only. URL of the region where the health check service resides. This field is not applicable to global health check services. You must specify this field as part of the HTTP request URL. It is not settable as a field in the request body.  
`healthStatusAggregationPolicy` |  `enum` Optional. Policy for how the results from multiple health checks for the same endpoint are aggregated. Defaults to NO_AGGREGATION if unspecified. 

  * `NO_AGGREGATION`. An `EndpointHealth` message is returned for each <endpoint, health check> pair in the health check service.
  * `AND`. If any health check of an endpoint reports `UNHEALTHY`, then `UNHEALTHY` is the `HealthState` of the endpoint. If all health checks report `HEALTHY`, the `HealthState` of the endpoint is `HEALTHY`. 

. This is only allowed with regional `HealthCheckService`.   
`healthChecks[]` |  `string` A list of URLs to the `HealthCheck` resources. Must have at least one `HealthCheck`, and not more than 10 for regional `HealthCheckService`, and not more than 1 for global `HealthCheckService`. `HealthCheck` resources must have `portSpecification`=`USE_SERVING_PORT` or `portSpecification`=`USE_FIXED_PORT`. For regional `HealthCheckService`, the `HealthCheck` must be regional and in the same region. For global `HealthCheckService`, `HealthCheck` must be global. Mix of regional and global `HealthChecks` is not supported. Multiple regional `HealthChecks` must belong to the same region. Regional `HealthChecks` must belong to the same region as zones of `NetworkEndpointGroups`. For global `HealthCheckService` using global `INTERNET_IP_PORT` `NetworkEndpointGroups`, the global `HealthChecks` must specify `sourceRegions`, and `HealthChecks` that specify `sourceRegions` can only be used with global `INTERNET_IP_PORT` `NetworkEndpointGroups`.  
`networkEndpointGroups[]` |  `string` A list of URLs to the `NetworkEndpointGroup` resources. Must not have more than 100. For regional `HealthCheckService`, `NEG`s must be in zones in the region of the `HealthCheckService`. For global `HealthCheckServices`, the `NetworkEndpointGroups` must be global `INTERNET_IP_PORT`.  
`notificationEndpoints[]` |  `string` A list of URLs to the `NotificationEndpoint` resources. Must not have more than 10. A list of endpoints for receiving notifications of change in health status. For regional `HealthCheckService`, `NotificationEndpoint` must be regional and in the same region. For global `HealthCheckService`, `NotificationEndpoint` must be global.  
`fingerprint` |  `string ([bytes](https://developers.google.com/discovery/v1/type-format) format)` Fingerprint of this resource. A hash of the contents stored in this object. This field is used in optimistic locking. This field will be ignored when inserting a `HealthCheckService`. An up-to-date fingerprint must be provided in order to patch/update the HealthCheckService; Otherwise, the request will fail with error `412 conditionNotMet`. To see the latest fingerprint, make a `get()` request to retrieve the HealthCheckService.A base64-encoded string.  
  
## Methods  
  
---  
  
### `[aggregatedList](https://docs.cloud.google.com/compute/docs/reference/rest/2026-09-01/regionHealthCheckServices/aggregatedList)`

|  Retrieves the list of all `HealthCheckService` resources, regional and global, available to the specified project.  
  
### `[delete](https://docs.cloud.google.com/compute/docs/reference/rest/2026-09-01/regionHealthCheckServices/delete)`

|  Deletes the specified regional HealthCheckService.  
  
### `[get](https://docs.cloud.google.com/compute/docs/reference/rest/2026-09-01/regionHealthCheckServices/get)`

|  Returns the specified regional `HealthCheckService` resource.  
  
### `[insert](https://docs.cloud.google.com/compute/docs/reference/rest/2026-09-01/regionHealthCheckServices/insert)`

|  Creates a regional `HealthCheckService` resource in the specified project and region using the data included in the request.  
  
### `[list](https://docs.cloud.google.com/compute/docs/reference/rest/2026-09-01/regionHealthCheckServices/list)`

|  Lists all the `HealthCheckService` resources that have been configured for the specified project in the given region.  
  
### `[patch](https://docs.cloud.google.com/compute/docs/reference/rest/2026-09-01/regionHealthCheckServices/patch)`

|  Updates the specified regional `HealthCheckService` resource with the data included in the request.  
  
### `[testIamPermissions](https://docs.cloud.google.com/compute/docs/reference/rest/2026-09-01/regionHealthCheckServices/testIamPermissions)`

|  Returns permissions that a caller has on the specified resource.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-01 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-01 UTC."],[],[]] 
