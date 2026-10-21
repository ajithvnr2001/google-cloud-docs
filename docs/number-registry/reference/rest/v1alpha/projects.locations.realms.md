---
url: https://docs.cloud.google.com/number-registry/reference/rest/v1alpha/projects.locations.realms
title: REST Resource: projects.locations.realms \u00a0|\u00a0 Cloud Number Registry \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T12:34:13.050391+00:00
---

# REST Resource: projects.locations.realms  |  Cloud Number Registry  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/number-registry/reference/rest/v1alpha/projects.locations.realms

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Networking ](https://docs.cloud.google.com/docs/networking)
  * [ Cloud Number Registry ](https://docs.cloud.google.com/number-registry)
  * [ Reference ](https://docs.cloud.google.com/number-registry/apis)



Send feedback 

#  REST Resource: projects.locations.realms Stay organized with collections  Save and categorize content based on your preferences. 

  * Resource: Realm
    * JSON representation
  * TrafficType
  * ManagementType
  * IpVersion
  * RealmAggregatedData
    * JSON representation
  * Methods



## Resource: Realm

A Realm represents a distinct network domain or security zone. It groups Ranges that share the same traffic and management characteristics. All the ranges in a Realm are routable to each other, meaning that they cannot overlap.

JSON representation  
---  
      
    
    {
      "name": string,
      "trafficType": enum ([TrafficType](https://docs.cloud.google.com/number-registry/reference/rest/v1alpha/projects.locations.realms#TrafficType)),
      "managementType": enum ([ManagementType](https://docs.cloud.google.com/number-registry/reference/rest/v1alpha/projects.locations.realms#ManagementType)),
      "registryBook": string,
      "discoveryMetadata": {
        object ([DiscoveryMetadata](https://docs.cloud.google.com/number-registry/reference/rest/v1alpha/DiscoveryMetadata))
      },
      "createTime": string,
      "updateTime": string,
      "labels": {
        string: string,
        ...
      },
      "ipVersion": enum ([IpVersion](https://docs.cloud.google.com/number-registry/reference/rest/v1alpha/projects.locations.realms#IpVersion)),
      "aggregatedData": {
        object ([RealmAggregatedData](https://docs.cloud.google.com/number-registry/reference/rest/v1alpha/projects.locations.realms#RealmAggregatedData))
      }
    }  
  
Fields  
---  
`name` |  `string` Required. Identifier. The resource name of the Realm.  
`trafficType` |  `enum (`[TrafficType](https://docs.cloud.google.com/number-registry/reference/rest/v1alpha/projects.locations.realms#TrafficType)`)` Required. Traffic type of the Realm.  
`managementType` |  `enum (`[ManagementType](https://docs.cloud.google.com/number-registry/reference/rest/v1alpha/projects.locations.realms#ManagementType)`)` Required. Management type of the Realm.  
`registryBook` |  `string` Required. Name of the RegistryBook that claims the Realm.  
`discoveryMetadata` |  `object (`[DiscoveryMetadata](https://docs.cloud.google.com/number-registry/reference/rest/v1alpha/DiscoveryMetadata)`)` Output only. Discovery metadata of the Realm.  
`createTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Output only. The time at which the Realm was created.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`updateTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Output only. The time at which the Realm was last updated.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`labels` |  `map (key: string, value: string)` Optional. User-defined labels.An object containing a list of `"key": value` pairs. Example: `{ "name": "wrench", "mass": "1.3kg", "count": "3" }`.  
`ipVersion` |  `enum (`[IpVersion](https://docs.cloud.google.com/number-registry/reference/rest/v1alpha/projects.locations.realms#IpVersion)`)` Optional. IP version of the Realm.  
`aggregatedData` |  `object (`[RealmAggregatedData](https://docs.cloud.google.com/number-registry/reference/rest/v1alpha/projects.locations.realms#RealmAggregatedData)`)` Output only. Aggregated data for the Realm. Populated only when the view is AGGREGATE.  
  
## TrafficType

Traffic type of the Realm.

Enums  
---  
`TRAFFIC_TYPE_UNSPECIFIED` | Unspecified traffic type.  
`UNSET` | Unset traffic type.  
`INTERNET` | Internet traffic.  
`PRIVATE` | Private traffic.  
`LINKLOCAL` | Linklocal traffic.  
  
## ManagementType

Management type of the Realm.

Enums  
---  
`MANAGEMENT_TYPE_UNSPECIFIED` | Unspecified management type.  
`CNR` | Managed by Cloud Number Registry.  
`USER` | Managed by User.  
  
## IpVersion

IP version of the Realm.

Enums  
---  
`IP_VERSION_UNSPECIFIED` | Unspecified IP version.  
`IPV4` | IPv4 IP version.  
`IPV6` | IPv6 IP version.  
  
## RealmAggregatedData

Aggregated data for the Realm.

JSON representation  
---  
      
    
    {
      "discoveredRangesCount": integer,
      "customRangesCount": integer
    }  
  
Fields  
---  
`discoveredRangesCount` |  `integer` Output only. Number of DiscoveredRanges in the Realm.  
`customRangesCount` |  `integer` Output only. Number of CustomRanges in the Realm.  
  
## Methods  
  
---  
  
### `[create](https://docs.cloud.google.com/number-registry/reference/rest/v1alpha/projects.locations.realms/create)`

|  Creates a new Realm in a given project and location.  
  
### `[delete](https://docs.cloud.google.com/number-registry/reference/rest/v1alpha/projects.locations.realms/delete)`

|  Deletes a single Realm.  
  
### `[get](https://docs.cloud.google.com/number-registry/reference/rest/v1alpha/projects.locations.realms/get)`

|  Gets details of a single Realm.  
  
### `[list](https://docs.cloud.google.com/number-registry/reference/rest/v1alpha/projects.locations.realms/list)`

|  Lists Realms in a given project and location.  
  
### `[patch](https://docs.cloud.google.com/number-registry/reference/rest/v1alpha/projects.locations.realms/patch)`

|  Updates the parameters of a single Realm.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-06-02 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-06-02 UTC."],[],[]] 
