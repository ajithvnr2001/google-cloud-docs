---
url: https://docs.cloud.google.com/vmware-engine/docs/public/reference/rest/v1/projects.locations.privateClouds.loggingServers
title: REST Resource: projects.locations.privateClouds.loggingServers \u00a0|\u00a0 Google Cloud VMware Engine \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T07:51:16.574411+00:00
---

# REST Resource: projects.locations.privateClouds.loggingServers  |  Google Cloud VMware Engine  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/vmware-engine/docs/public/reference/rest/v1/projects.locations.privateClouds.loggingServers

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ VMware Engine ](https://docs.cloud.google.com/vmware-engine/docs)
  * [ Reference ](https://docs.cloud.google.com/vmware-engine/docs/public/reference/rest)



Send feedback 

#  REST Resource: projects.locations.privateClouds.loggingServers Stay organized with collections  Save and categorize content based on your preferences. 

  * Resource: LoggingServer
    * JSON representation
  * Protocol
  * SourceType
  * Methods



## Resource: LoggingServer

Logging server to receive vCenter or ESXi logs.

JSON representation  
---  
      
    
    {
      "name": string,
      "createTime": string,
      "updateTime": string,
      "hostname": string,
      "port": integer,
      "protocol": enum ([Protocol](https://docs.cloud.google.com/vmware-engine/docs/public/reference/rest/v1/projects.locations.privateClouds.loggingServers#Protocol)),
      "sourceType": enum ([SourceType](https://docs.cloud.google.com/vmware-engine/docs/public/reference/rest/v1/projects.locations.privateClouds.loggingServers#SourceType)),
      "uid": string
    }  
  
Fields  
---  
`name` |  `string` Output only. The resource name of this logging server. Resource names are schemeless URIs that follow the conventions in <https://cloud.google.com/apis/design/resource_names>. For example: `projects/my-project/locations/us-central1-a/privateClouds/my-cloud/loggingServers/my-logging-server`  
`createTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Output only. Creation time of this resource.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`updateTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Output only. Last update time of this resource.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`hostname` |  `string` Required. Fully-qualified domain name (FQDN) or IP Address of the logging server.  
`port` |  `integer` Required. Port number at which the logging server receives logs.  
`protocol` |  `enum (`[Protocol](https://docs.cloud.google.com/vmware-engine/docs/public/reference/rest/v1/projects.locations.privateClouds.loggingServers#Protocol)`)` Required. Protocol used by vCenter to send logs to a logging server.  
`sourceType` |  `enum (`[SourceType](https://docs.cloud.google.com/vmware-engine/docs/public/reference/rest/v1/projects.locations.privateClouds.loggingServers#SourceType)`)` Required. The type of component that produces logs that will be forwarded to this logging server.  
`uid` |  `string` Output only. System-generated unique identifier for the resource.  
  
## Protocol

Defines possible protocols used to send logs to a logging server.

Enums  
---  
`PROTOCOL_UNSPECIFIED` | Unspecified communications protocol. This is the default value.  
`UDP` | UDP  
`TCP` | TCP  
`TLS` | TLS  
`SSL` | SSL  
`RELP` | RELP  
  
## SourceType

Defines possible types of component that produces logs.

Enums  
---  
`SOURCE_TYPE_UNSPECIFIED` | The default value. This value should never be used.  
`ESXI` | Logs produced by ESXI hosts  
`VCSA` | Logs produced by vCenter server  
  
## Methods  
  
---  
  
### `[create](https://docs.cloud.google.com/vmware-engine/docs/public/reference/rest/v1/projects.locations.privateClouds.loggingServers/create)`

|  Create a new logging server for a given private cloud.  
  
### `[delete](https://docs.cloud.google.com/vmware-engine/docs/public/reference/rest/v1/projects.locations.privateClouds.loggingServers/delete)`

|  Deletes a single logging server.  
  
### `[get](https://docs.cloud.google.com/vmware-engine/docs/public/reference/rest/v1/projects.locations.privateClouds.loggingServers/get)`

|  Gets details of a logging server.  
  
### `[list](https://docs.cloud.google.com/vmware-engine/docs/public/reference/rest/v1/projects.locations.privateClouds.loggingServers/list)`

|  Lists logging servers configured for a given private cloud.  
  
### `[patch](https://docs.cloud.google.com/vmware-engine/docs/public/reference/rest/v1/projects.locations.privateClouds.loggingServers/patch)`

|  Updates the parameters of a single logging server.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-02-11 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-02-11 UTC."],[],[]] 
