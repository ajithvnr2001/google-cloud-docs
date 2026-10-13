---
url: https://docs.cloud.google.com/service-mesh/v1.22/docs/reference/network-security/rest/v1beta1/organizations.locations.addressGroups
title: REST Resource: organizations.locations.addressGroups \u00a0|\u00a0 Cloud Service Mesh v1.22 \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T16:48:41.868543+00:00
---

# REST Resource: organizations.locations.addressGroups  |  Cloud Service Mesh v1.22  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/service-mesh/v1.22/docs/reference/network-security/rest/v1beta1/organizations.locations.addressGroups

You are viewing archived v1.22 Service Mesh documentation.

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
  * [ Cloud Service Mesh ](https://docs.cloud.google.com/service-mesh/docs)
  * [ v1.22 ](https://docs.cloud.google.com/service-mesh/v1.22/docs)



Send feedback 

#  REST Resource: organizations.locations.addressGroups Stay organized with collections  Save and categorize content based on your preferences. 

  * Resource: AddressGroup
    * JSON representation
    * Type
    * Purpose
  * Methods



## Resource: AddressGroup

AddressGroup is a resource that specifies how a collection of IP/DNS used in Firewall Policy.

JSON representation  
---  
      
    
    {
      "name": string,
      "description": string,
      "createTime": string,
      "updateTime": string,
      "labels": {
        string: string,
        ...
      },
      "type": enum ([Type](https://docs.cloud.google.com/service-mesh/v1.22/docs/reference/network-security/rest/v1beta1/organizations.locations.addressGroups#AddressGroup.Type)),
      "items": [
        string
      ],
      "capacity": integer,
      "selfLink": string,
      "purpose": [
        enum ([Purpose](https://docs.cloud.google.com/service-mesh/v1.22/docs/reference/network-security/rest/v1beta1/organizations.locations.addressGroups#AddressGroup.Purpose))
      ]
    }  
  
Fields  
---  
`name` |  `string` Required. Name of the AddressGroup resource. It matches pattern `projects/*/locations/{location}/addressGroups/<addressGroup>`.  
`description` |  `string` Optional. Free-text description of the resource.  
`createTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Output only. The timestamp when the resource was created.A timestamp in RFC3339 UTC "Zulu" format, with nanosecond resolution and up to nine fractional digits. Examples: `"2014-10-02T15:01:23Z"` and `"2014-10-02T15:01:23.045123456Z"`.  
`updateTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Output only. The timestamp when the resource was updated.A timestamp in RFC3339 UTC "Zulu" format, with nanosecond resolution and up to nine fractional digits. Examples: `"2014-10-02T15:01:23Z"` and `"2014-10-02T15:01:23.045123456Z"`.  
`labels` |  `map (key: string, value: string)` Optional. Set of label tags associated with the AddressGroup resource.An object containing a list of `"key": value` pairs. Example: `{ "name": "wrench", "mass": "1.3kg", "count": "3" }`.  
`type` |  `enum (`[Type](https://docs.cloud.google.com/service-mesh/v1.22/docs/reference/network-security/rest/v1beta1/organizations.locations.addressGroups#AddressGroup.Type)`)` Required. The type of the Address Group. Possible values are "IPv4" or "IPV6".  
`items[]` |  `string` Optional. List of items.  
`capacity` |  `integer` Required. Capacity of the Address Group  
`selfLink` |  `string` Output only. Server-defined fully-qualified URL for this resource.  
`purpose[]` |  `enum (`[Purpose](https://docs.cloud.google.com/service-mesh/v1.22/docs/reference/network-security/rest/v1beta1/organizations.locations.addressGroups#AddressGroup.Purpose)`)` Optional. List of supported purposes of the Address Group.  
  
### Type

Possible type of the Address Group.

Enums  
---  
`TYPE_UNSPECIFIED` | Default value.  
`IPV4` | IP v4 ranges.  
`IPV6` | IP v6 ranges.  
  
### Purpose

Purpose of the Address Group.

Enums  
---  
`PURPOSE_UNSPECIFIED` | Default value. Should never happen.  
`DEFAULT` | Address Group is distributed to VMC, and is usable in Firewall Policies and other systems that rely on VMC.  
`CLOUD_ARMOR` | Address Group is usable in Cloud Armor.  
  
## Methods  
  
---  
  
### `[addItems](https://docs.cloud.google.com/service-mesh/v1.22/docs/reference/network-security/rest/v1beta1/organizations.locations.addressGroups/addItems)`

|  Adds items to an address group.  
  
### `[cloneItems](https://docs.cloud.google.com/service-mesh/v1.22/docs/reference/network-security/rest/v1beta1/organizations.locations.addressGroups/cloneItems)`

|  Clones items from one address group to another.  
  
### `[create](https://docs.cloud.google.com/service-mesh/v1.22/docs/reference/network-security/rest/v1beta1/organizations.locations.addressGroups/create)`

|  Creates a new address group in a given project and location.  
  
### `[delete](https://docs.cloud.google.com/service-mesh/v1.22/docs/reference/network-security/rest/v1beta1/organizations.locations.addressGroups/delete)`

|  Deletes an address group.  
  
### `[get](https://docs.cloud.google.com/service-mesh/v1.22/docs/reference/network-security/rest/v1beta1/organizations.locations.addressGroups/get)`

|  Gets details of a single address group.  
  
### `[list](https://docs.cloud.google.com/service-mesh/v1.22/docs/reference/network-security/rest/v1beta1/organizations.locations.addressGroups/list)`

|  Lists address groups in a given project and location.  
  
### `[listReferences](https://docs.cloud.google.com/service-mesh/v1.22/docs/reference/network-security/rest/v1beta1/organizations.locations.addressGroups/listReferences)`

|  Lists references of an address group.  
  
### `[patch](https://docs.cloud.google.com/service-mesh/v1.22/docs/reference/network-security/rest/v1beta1/organizations.locations.addressGroups/patch)`

|  Updates parameters of an address group.  
  
### `[removeItems](https://docs.cloud.google.com/service-mesh/v1.22/docs/reference/network-security/rest/v1beta1/organizations.locations.addressGroups/removeItems)`

|  Removes items from an address group.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-06-18 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-06-18 UTC."],[],[]] 
