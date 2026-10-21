---
url: https://docs.cloud.google.com/managed-microsoft-ad/reference/rest/v1beta1/projects.locations.global.peerings
title: REST Resource: projects.locations.global.peerings \u00a0|\u00a0 Managed Microsoft AD \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T13:30:23.892096+00:00
---

# REST Resource: projects.locations.global.peerings  |  Managed Microsoft AD  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/managed-microsoft-ad/reference/rest/v1beta1/projects.locations.global.peerings

  * [ Home ](https://docs.cloud.google.com/)
  * [ Managed Microsoft AD ](https://docs.cloud.google.com/managed-microsoft-ad)
  * [ Reference ](https://docs.cloud.google.com/managed-microsoft-ad/reference/rest)



Send feedback 

#  REST Resource: projects.locations.global.peerings Stay organized with collections  Save and categorize content based on your preferences. 

  * Resource: Peering
    * JSON representation
  * State
  * Methods



## Resource: Peering

Represents a Managed Microsoft Identities Peering.

JSON representation  
---  
      
    
    {
      "name": string,
      "labels": {
        string: string,
        ...
      },
      "authorizedNetwork": string,
      "domainResource": string,
      "createTime": string,
      "updateTime": string,
      "state": enum ([State](https://docs.cloud.google.com/managed-microsoft-ad/reference/rest/v1beta1/projects.locations.global.peerings#State)),
      "statusMessage": string
    }  
  
Fields  
---  
`name` |  `string` Output only. Unique name of the peering in this scope including projects and location using the form: `projects/{projectId}/locations/global/peerings/{peeringId}`.  
`labels` |  `map (key: string, value: string)` Optional. Resource labels to represent user provided metadata.An object containing a list of `"key": value` pairs. Example: `{ "name": "wrench", "mass": "1.3kg", "count": "3" }`.  
`authorizedNetwork` |  `string` Required. The full names of the Google Compute Engine [networks](https://docs.cloud.google.com/compute/docs/networks-and-firewalls#networks) to which the instance is connected. Caller needs to make sure that CIDR subnets do not overlap between networks, else peering creation will fail.  
`domainResource` |  `string` Required. Full domain resource path for the Managed AD Domain involved in peering. The resource path should be in the form: `projects/{projectId}/locations/global/domains/{domainName}`  
`createTime` |  `string (`[Timestamp](https://developers.google.com/protocol-buffers/docs/reference/google.protobuf#google.protobuf.Timestamp)` format)` Output only. The time the instance was created.A timestamp in RFC3339 UTC "Zulu" format, with nanosecond resolution and up to nine fractional digits. Examples: `"2014-10-02T15:01:23Z"` and `"2014-10-02T15:01:23.045123456Z"`.  
`updateTime` |  `string (`[Timestamp](https://developers.google.com/protocol-buffers/docs/reference/google.protobuf#google.protobuf.Timestamp)` format)` Output only. Last update time.A timestamp in RFC3339 UTC "Zulu" format, with nanosecond resolution and up to nine fractional digits. Examples: `"2014-10-02T15:01:23Z"` and `"2014-10-02T15:01:23.045123456Z"`.  
`state` |  `enum (`[State](https://docs.cloud.google.com/managed-microsoft-ad/reference/rest/v1beta1/projects.locations.global.peerings#State)`)` Output only. The current state of this Peering.  
`statusMessage` |  `string` Output only. Additional information about the current status of this peering, if available.  
  
## State

Represents the different states of a Peering.

Enums  
---  
`STATE_UNSPECIFIED` | Not set.  
`CREATING` | Peering is being created.  
`CONNECTED` | Peering is connected.  
`DISCONNECTED` | Peering is disconnected.  
`DELETING` | Peering is being deleted.  
  
## Methods  
  
---  
  
### `[create](https://docs.cloud.google.com/managed-microsoft-ad/reference/rest/v1beta1/projects.locations.global.peerings/create)`

|  Creates a Peering for Managed AD instance.  
  
### `[delete](https://docs.cloud.google.com/managed-microsoft-ad/reference/rest/v1beta1/projects.locations.global.peerings/delete)`

|  Deletes identified Peering.  
  
### `[get](https://docs.cloud.google.com/managed-microsoft-ad/reference/rest/v1beta1/projects.locations.global.peerings/get)`

|  Gets details of a single Peering.  
  
### `[getIamPolicy](https://docs.cloud.google.com/managed-microsoft-ad/reference/rest/v1beta1/projects.locations.global.peerings/getIamPolicy)`

|  Gets the access control policy for a resource.  
  
### `[list](https://docs.cloud.google.com/managed-microsoft-ad/reference/rest/v1beta1/projects.locations.global.peerings/list)`

|  Lists Peerings in a given project.  
  
### `[patch](https://docs.cloud.google.com/managed-microsoft-ad/reference/rest/v1beta1/projects.locations.global.peerings/patch)`

|  Updates the labels for specified Peering.  
  
### `[setIamPolicy](https://docs.cloud.google.com/managed-microsoft-ad/reference/rest/v1beta1/projects.locations.global.peerings/setIamPolicy)`

|  Sets the access control policy on the specified resource.  
  
### `[testIamPermissions](https://docs.cloud.google.com/managed-microsoft-ad/reference/rest/v1beta1/projects.locations.global.peerings/testIamPermissions)`

|  Returns permissions that a caller has on the specified resource.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-05-14 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-05-14 UTC."],[],[]] 
