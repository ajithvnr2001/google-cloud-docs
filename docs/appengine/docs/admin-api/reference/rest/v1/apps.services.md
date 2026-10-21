---
url: https://docs.cloud.google.com/appengine/docs/admin-api/reference/rest/v1/apps.services
title: REST Resource: apps.services \u00a0|\u00a0 App Engine Admin API \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T09:03:57.003128+00:00
---

# REST Resource: apps.services  |  App Engine Admin API  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/appengine/docs/admin-api/reference/rest/v1/apps.services

  * [ Home ](https://docs.cloud.google.com/)
  * [ App Engine ](https://docs.cloud.google.com/appengine)
  * [ Admin API ](https://docs.cloud.google.com/appengine/docs/admin-api)
  * [ Reference ](https://docs.cloud.google.com/appengine/docs/admin-api/apis)



Send feedback 

#  REST Resource: apps.services Stay organized with collections  Save and categorize content based on your preferences. 

  * Resource: Service
    * JSON representation
  * TrafficSplit
    * JSON representation
  * ShardBy
  * NetworkSettings
    * JSON representation
  * IngressTrafficAllowed
  * Methods



## Resource: Service

A Service resource is a logical component of an application that can share state and communicate in a secure fashion with other services. For example, an application that handles customer requests might include separate services to handle tasks such as backend data analysis or API requests from mobile devices. Each service has a collection of versions that define a specific set of code used to implement the functionality of that service.

JSON representation  
---  
      
    
    {
      "name": string,
      "id": string,
      "split": {
        object ([TrafficSplit](https://docs.cloud.google.com/appengine/docs/admin-api/reference/rest/v1/apps.services#TrafficSplit))
      },
      "labels": {
        string: string,
        ...
      },
      "networkSettings": {
        object ([NetworkSettings](https://docs.cloud.google.com/appengine/docs/admin-api/reference/rest/v1/apps.services#NetworkSettings))
      }
    }  
  
Fields  
---  
`name` |  `string` Full path to the Service resource in the API. Example: `apps/myapp/services/default`.Note: This field is used in responses only. Any value specified here in a request is ignored.  
`id` |  `string` Relative name of the service within the application. Example: `default`.Note: This field is used in responses only. Any value specified here in a request is ignored.  
`split` |  `object (`[TrafficSplit](https://docs.cloud.google.com/appengine/docs/admin-api/reference/rest/v1/apps.services#TrafficSplit)`)` Mapping that defines fractional HTTP traffic diversion to different versions within the service.  
`labels` |  `map (key: string, value: string)` A set of labels to apply to this service. Labels are key/value pairs that describe the service and all resources that belong to it (e.g., versions). The labels can be used to search and group resources, and are propagated to the usage and billing reports, enabling fine-grain analysis of costs. An example of using labels is to tag resources belonging to different environments (e.g., "env=prod", "env=qa").Label keys and values can be no longer than 63 characters and can only contain lowercase letters, numeric characters, underscores, dashes, and international characters. Label keys must start with a lowercase letter or an international character. Each service can have at most 32 labels.An object containing a list of `"key": value` pairs. Example: `{ "name": "wrench", "mass": "1.3kg", "count": "3" }`.  
`networkSettings` |  `object (`[NetworkSettings](https://docs.cloud.google.com/appengine/docs/admin-api/reference/rest/v1/apps.services#NetworkSettings)`)` Ingress settings for this service. Will apply to all versions.  
  
## TrafficSplit

Traffic routing configuration for versions within a single service. Traffic splits define how traffic directed to the service is assigned to versions.

JSON representation  
---  
      
    
    {
      "shardBy": enum ([ShardBy](https://docs.cloud.google.com/appengine/docs/admin-api/reference/rest/v1/apps.services#ShardBy)),
      "allocations": {
        string: number,
        ...
      }
    }  
  
Fields  
---  
`shardBy` |  `enum (`[ShardBy](https://docs.cloud.google.com/appengine/docs/admin-api/reference/rest/v1/apps.services#ShardBy)`)` Mechanism used to determine which version a request is sent to. The traffic selection algorithm will be stable for either type until allocations are changed.  
`allocations` |  `map (key: string, value: number)` Mapping from version IDs within the service to fractional (0.000, 1] allocations of traffic for that version. Each version can be specified only once, but some versions in the service may not have any traffic allocation. Services that have traffic allocated cannot be deleted until either the service is deleted or their traffic allocation is removed. Allocations must sum to 1. Up to two decimal place precision is supported for IP-based splits and up to three decimal places is supported for cookie-based splits.An object containing a list of `"key": value` pairs. Example: `{ "name": "wrench", "mass": "1.3kg", "count": "3" }`.  
  
## ShardBy

Available sharding mechanisms.

Enums  
---  
`UNSPECIFIED` | Diversion method unspecified.  
`COOKIE` | Diversion based on a specially named cookie, "GOOGAPPUID." The cookie must be set by the application itself or no diversion will occur.  
`IP` | Diversion based on applying the modulus operation to a fingerprint of the IP address.  
`RANDOM` | Diversion based on weighted random assignment. An incoming request is randomly routed to a version in the traffic split, with probability proportional to the version's traffic share.  
  
## NetworkSettings

A NetworkSettings resource is a container for ingress settings for a version or service.

JSON representation  
---  
      
    
    {
      "ingressTrafficAllowed": enum ([IngressTrafficAllowed](https://docs.cloud.google.com/appengine/docs/admin-api/reference/rest/v1/apps.services#IngressTrafficAllowed))
    }  
  
Fields  
---  
`ingressTrafficAllowed` |  `enum (`[IngressTrafficAllowed](https://docs.cloud.google.com/appengine/docs/admin-api/reference/rest/v1/apps.services#IngressTrafficAllowed)`)` The ingress settings for version or service.  
  
## IngressTrafficAllowed

If unspecified, INGRESS_TRAFFIC_ALLOWED_ALL will be used.

Enums  
---  
`INGRESS_TRAFFIC_ALLOWED_UNSPECIFIED` | Unspecified  
`INGRESS_TRAFFIC_ALLOWED_ALL` | Allow HTTP traffic from public and private sources.  
`INGRESS_TRAFFIC_ALLOWED_INTERNAL_ONLY` | Allow HTTP traffic from only private VPC sources.  
`INGRESS_TRAFFIC_ALLOWED_INTERNAL_AND_LB` | Allow HTTP traffic from private VPC sources and through load balancers.  
  
## Methods  
  
---  
  
### `[delete](https://docs.cloud.google.com/appengine/docs/admin-api/reference/rest/v1/apps.services/delete)`

|  Deletes the specified service and all enclosed versions.  
  
### `[get](https://docs.cloud.google.com/appengine/docs/admin-api/reference/rest/v1/apps.services/get)`

|  Gets the current configuration of the specified service.  
  
### `[list](https://docs.cloud.google.com/appengine/docs/admin-api/reference/rest/v1/apps.services/list)`

|  Lists all the services in the application.  
  
### `[patch](https://docs.cloud.google.com/appengine/docs/admin-api/reference/rest/v1/apps.services/patch)`

|  Updates the configuration of the specified service.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-06-16 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-06-16 UTC."],[],[]] 
