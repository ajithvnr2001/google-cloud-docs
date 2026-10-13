---
url: https://docs.cloud.google.com/network-security-integration/docs/reference/rest/v1/projects.locations.interceptEndpointGroupAssociations
title: REST Resource: projects.locations.interceptEndpointGroupAssociations \u00a0|\u00a0 Network Security Integration \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T17:36:30.146838+00:00
---

# REST Resource: projects.locations.interceptEndpointGroupAssociations  |  Network Security Integration  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/network-security-integration/docs/reference/rest/v1/projects.locations.interceptEndpointGroupAssociations

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Networking ](https://docs.cloud.google.com/docs/networking)
  * [ Network Security Integration ](https://docs.cloud.google.com/network-security-integration/docs)
  * [ Reference ](https://docs.cloud.google.com/network-security-integration/docs/apis)



Send feedback 

#  REST Resource: projects.locations.interceptEndpointGroupAssociations Stay organized with collections  Save and categorize content based on your preferences. 

## Resource: InterceptEndpointGroupAssociation

An endpoint group association represents a link between a network and an endpoint group in the organization.

Creating an association creates the networking infrastructure linking the network to the endpoint group, but does not enable intercept by itself. To enable intercept, the user must also create a network firewall policy containing intercept rules and associate it with the network.

JSON representation  
---  
      
    
    {
      "name": string,
      "createTime": string,
      "updateTime": string,
      "labels": {
        string: string,
        ...
      },
      "interceptEndpointGroup": string,
      "network": string,
      "locationsDetails": [
        {
          object ([LocationDetails](https://docs.cloud.google.com/network-security-integration/docs/reference/rest/v1/projects.locations.interceptEndpointGroupAssociations#LocationDetails))
        }
      ],
      "state": enum (State),
      "reconciling": boolean,
      "locations": [
        {
          object ([InterceptLocation](https://docs.cloud.google.com/network-security-integration/docs/reference/rest/v1/InterceptLocation))
        }
      ],
      "networkCookie": integer
    }  
  
Fields  
---  
`name` |  `string` Immutable. Identifier. The resource name of this endpoint group association, for example: `projects/123456789/locations/global/interceptEndpointGroupAssociations/my-eg-association`. See <https://google.aip.dev/122> for more details.  
`createTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Output only. The timestamp when the resource was created. See <https://google.aip.dev/148#timestamps>.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`updateTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Output only. The timestamp when the resource was most recently updated. See <https://google.aip.dev/148#timestamps>.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`labels` |  `map (key: string, value: string)` Optional. Labels are key/value pairs that help to organize and filter resources.An object containing a list of `"key": value` pairs. Example: `{ "name": "wrench", "mass": "1.3kg", "count": "3" }`.  
`interceptEndpointGroup` |  `string` Required. Immutable. The endpoint group that this association is connected to, for example: `projects/123456789/locations/global/interceptEndpointGroups/my-eg`. See <https://google.aip.dev/124>.  
`network` |  `string` Required. Immutable. The VPC network that is associated. for example: `projects/123456789/global/networks/my-network`. See <https://google.aip.dev/124>.  
`locationsDetails[]  
**(deprecated)**` |  `object (`[LocationDetails](https://docs.cloud.google.com/network-security-integration/docs/reference/rest/v1/projects.locations.interceptEndpointGroupAssociations#LocationDetails)`)` This item is deprecated!Output only. The list of locations where the association is present. This information is retrieved from the linked endpoint group, and not configured as part of the association itself.  
`state` |  `enum (`State`)` Output only. Current state of the endpoint group association.  
`reconciling` |  `boolean` Output only. The current state of the resource does not match the user's intended state, and the system is working to reconcile them. This part of the normal operation (e.g. adding a new location to the target deployment group). See <https://google.aip.dev/128>.  
`locations[]` |  `object (`[InterceptLocation](https://docs.cloud.google.com/network-security-integration/docs/reference/rest/v1/InterceptLocation)`)` Output only. The list of locations where the association is configured. This information is retrieved from the linked endpoint group.  
`networkCookie` |  `integer ([uint32](https://developers.google.com/discovery/v1/type-format) format)` Output only. Identifier used by the data-path. See the NSI GENEVE format for more details: <https://docs.cloud.google.com/network-security-integration/docs/understand-geneve#network_id>  
  
## LocationDetails

Contains details about the state of an association in a specific cloud location.

JSON representation  
---  
      
    
    {
      "location": string,
      "state": enum ([State](https://docs.cloud.google.com/network-security-integration/docs/reference/rest/v1/projects.locations.interceptEndpointGroupAssociations#State))
    }  
  
Fields  
---  
`location` |  `string` Output only. The cloud location, e.g. "us-central1-a" or "asia-south1".  
`state` |  `enum (`[State](https://docs.cloud.google.com/network-security-integration/docs/reference/rest/v1/projects.locations.interceptEndpointGroupAssociations#State)`)` Output only. The current state of the association in this location.  
  
## State

The state of association.

Enums  
---  
`STATE_UNSPECIFIED` | Not set.  
`ACTIVE` | The association is ready and in sync with the linked endpoint group.  
`OUT_OF_SYNC` | The association is out of sync with the linked endpoint group. In most cases, this is a result of a transient issue within the system (e.g. an inaccessible location) and the system is expected to recover automatically.  
  
## Methods  
  
---  
  
### `[create](https://docs.cloud.google.com/network-security-integration/docs/reference/rest/v1/projects.locations.interceptEndpointGroupAssociations/create)`

|  Creates an association in a given project and location.  
  
### `[delete](https://docs.cloud.google.com/network-security-integration/docs/reference/rest/v1/projects.locations.interceptEndpointGroupAssociations/delete)`

|  Deletes an association.  
  
### `[get](https://docs.cloud.google.com/network-security-integration/docs/reference/rest/v1/projects.locations.interceptEndpointGroupAssociations/get)`

|  Gets a specific association.  
  
### `[list](https://docs.cloud.google.com/network-security-integration/docs/reference/rest/v1/projects.locations.interceptEndpointGroupAssociations/list)`

|  Lists associations in a given project and location.  
  
### `[patch](https://docs.cloud.google.com/network-security-integration/docs/reference/rest/v1/projects.locations.interceptEndpointGroupAssociations/patch)`

|  Updates an association.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-08-10 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-08-10 UTC."],[],[]] 
