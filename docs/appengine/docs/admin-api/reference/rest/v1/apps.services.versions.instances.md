---
url: https://docs.cloud.google.com/appengine/docs/admin-api/reference/rest/v1/apps.services.versions.instances
title: REST Resource: apps.services.versions.instances \u00a0|\u00a0 App Engine Admin API \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T09:03:57.898563+00:00
---

# REST Resource: apps.services.versions.instances  |  App Engine Admin API  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/appengine/docs/admin-api/reference/rest/v1/apps.services.versions.instances

  * [ Home ](https://docs.cloud.google.com/)
  * [ App Engine ](https://docs.cloud.google.com/appengine)
  * [ Admin API ](https://docs.cloud.google.com/appengine/docs/admin-api)
  * [ Reference ](https://docs.cloud.google.com/appengine/docs/admin-api/apis)



Send feedback 

#  REST Resource: apps.services.versions.instances Stay organized with collections  Save and categorize content based on your preferences. 

  * Resource: Instance
    * JSON representation
  * Availability
  * LivenessState
  * Methods



## Resource: Instance

An Instance resource is the computing unit that App Engine uses to automatically scale an application.

JSON representation  
---  
      
    
    {
      "name": string,
      "id": string,
      "appEngineRelease": string,
      "availability": enum ([Availability](https://docs.cloud.google.com/appengine/docs/admin-api/reference/rest/v1/apps.services.versions.instances#Availability)),
      "vmName": string,
      "vmZoneName": string,
      "vmId": string,
      "startTime": string,
      "requests": integer,
      "errors": integer,
      "qps": number,
      "averageLatency": integer,
      "memoryUsage": string,
      "vmStatus": string,
      "vmDebugEnabled": boolean,
      "vmIp": string,
      "vmLiveness": enum ([LivenessState](https://docs.cloud.google.com/appengine/docs/admin-api/reference/rest/v1/apps.services.versions.instances#LivenessState))
    }  
  
Fields  
---  
`name` |  `string` Output only. Full path to the Instance resource in the API. Example: `apps/myapp/services/default/versions/v1/instances/instance-1`.  
`id` |  `string` Output only. Relative name of the instance within the version. Example: `instance-1`.  
`appEngineRelease` |  `string` Output only. App Engine release this instance is running on.  
`availability` |  `enum (`[Availability](https://docs.cloud.google.com/appengine/docs/admin-api/reference/rest/v1/apps.services.versions.instances#Availability)`)` Output only. Availability of the instance.  
`vmName` |  `string` Output only. Name of the virtual machine where this instance lives. Only applicable for instances in App Engine flexible environment.  
`vmZoneName` |  `string` Output only. Zone where the virtual machine is located. Only applicable for instances in App Engine flexible environment.  
`vmId` |  `string` Output only. Virtual machine ID of this instance. Only applicable for instances in App Engine flexible environment.  
`startTime` |  `string (`[Timestamp](https://developers.google.com/protocol-buffers/docs/reference/google.protobuf#google.protobuf.Timestamp)` format)` Output only. Time that this instance was started.A timestamp in RFC3339 UTC "Zulu" format, with nanosecond resolution and up to nine fractional digits. Examples: `"2014-10-02T15:01:23Z"` and `"2014-10-02T15:01:23.045123456Z"`.Note: This field is used in responses only. Any value specified here in a request is ignored.  
`requests` |  `integer` Output only. Number of requests since this instance was started.  
`errors` |  `integer` Output only. Number of errors since this instance was started.  
`qps` |  `number` Output only. Average queries per second (QPS) over the last minute.  
`averageLatency` |  `integer` Output only. Average latency (ms) over the last minute.  
`memoryUsage` |  `string ([int64](https://developers.google.com/discovery/v1/type-format) format)` Output only. Total memory in use (bytes).  
`vmStatus` |  `string` Output only. Status of the virtual machine where this instance lives. Only applicable for instances in App Engine flexible environment.  
`vmDebugEnabled` |  `boolean` Output only. Whether this instance is in debug mode. Only applicable for instances in App Engine flexible environment.  
`vmIp` |  `string` Output only. The IP address of this instance. Only applicable for instances in App Engine flexible environment.  
`vmLiveness` |  `enum (`[LivenessState](https://docs.cloud.google.com/appengine/docs/admin-api/reference/rest/v1/apps.services.versions.instances#LivenessState)`)` Output only. The liveness health check of this instance. Only applicable for instances in App Engine flexible environment.  
  
## Availability

Availability of the instance.

Enums  
---  
`UNSPECIFIED` |   
`RESIDENT` |   
`DYNAMIC` |   
  
## LivenessState

Liveness health check status for Flex instances.

Enums  
---  
`LIVENESS_STATE_UNSPECIFIED` | There is no liveness health check for the instance. Only applicable for instances in App Engine standard environment.  
`UNKNOWN` | The health checking system is aware of the instance but its health is not known at the moment.  
`HEALTHY` | The instance is reachable i.e. a connection to the application health checking endpoint can be established, and conforms to the requirements defined by the health check.  
`UNHEALTHY` | The instance is reachable, but does not conform to the requirements defined by the health check.  
`DRAINING` | The instance is being drained. The existing connections to the instance have time to complete, but the new ones are being refused.  
`TIMEOUT` | The instance is unreachable i.e. a connection to the application health checking endpoint cannot be established, or the server does not respond within the specified timeout.  
  
## Methods  
  
---  
  
### `[debug](https://docs.cloud.google.com/appengine/docs/admin-api/reference/rest/v1/apps.services.versions.instances/debug)`

|  Enables debugging on a VM instance.  
  
### `[delete](https://docs.cloud.google.com/appengine/docs/admin-api/reference/rest/v1/apps.services.versions.instances/delete)`

|  Stops a running instance.  
  
### `[get](https://docs.cloud.google.com/appengine/docs/admin-api/reference/rest/v1/apps.services.versions.instances/get)`

|  Gets instance information.  
  
### `[list](https://docs.cloud.google.com/appengine/docs/admin-api/reference/rest/v1/apps.services.versions.instances/list)`

|  Lists the instances of a version.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-06-16 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-06-16 UTC."],[],[]] 
