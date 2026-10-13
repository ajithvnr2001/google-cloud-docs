---
url: https://docs.cloud.google.com/network-security-integration/docs/reference/rest/v1/projects.locations.interceptEndpointGroups
title: REST Resource: projects.locations.interceptEndpointGroups \u00a0|\u00a0 Network Security Integration \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T17:36:30.917564+00:00
---

# REST Resource: projects.locations.interceptEndpointGroups  |  Network Security Integration  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/network-security-integration/docs/reference/rest/v1/projects.locations.interceptEndpointGroups

  * [ Home ](https://docs.cloud.google.com/)
  * [ Network Security Integration ](https://docs.cloud.google.com/network-security-integration)
  * [ Reference ](https://docs.cloud.google.com/network-security-integration/docs/apis)



Send feedback 

#  REST Resource: projects.locations.interceptEndpointGroups Stay organized with collections  Save and categorize content based on your preferences. 

## Resource: InterceptEndpointGroup

An endpoint group is a consumer frontend for a deployment group (backend). In order to configure intercept for a network, consumers must create: - An association between their network and the endpoint group. - A security profile that points to the endpoint group. - A firewall rule that references the security profile (group).

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
      "interceptDeploymentGroup": string,
      "connectedDeploymentGroup": {
        object ([ConnectedDeploymentGroup](https://docs.cloud.google.com/network-security-integration/docs/reference/rest/v1/projects.locations.interceptEndpointGroups#ConnectedDeploymentGroup))
      },
      "state": enum ([State](https://docs.cloud.google.com/network-security-integration/docs/reference/rest/v1/projects.locations.interceptEndpointGroups#State)),
      "reconciling": boolean,
      "associations": [
        {
          object ([AssociationDetails](https://docs.cloud.google.com/network-security-integration/docs/reference/rest/v1/projects.locations.interceptEndpointGroups#AssociationDetails))
        }
      ],
      "description": string
    }  
  
Fields  
---  
`name` |  `string` Immutable. Identifier. The resource name of this endpoint group, for example: `projects/123456789/locations/global/interceptEndpointGroups/my-eg`. See <https://google.aip.dev/122> for more details.  
`createTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Output only. The timestamp when the resource was created. See <https://google.aip.dev/148#timestamps>.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`updateTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Output only. The timestamp when the resource was most recently updated. See <https://google.aip.dev/148#timestamps>.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`labels` |  `map (key: string, value: string)` Optional. Labels are key/value pairs that help to organize and filter resources.An object containing a list of `"key": value` pairs. Example: `{ "name": "wrench", "mass": "1.3kg", "count": "3" }`.  
`interceptDeploymentGroup` |  `string` Required. Immutable. The deployment group that this endpoint group is connected to, for example: `projects/123456789/locations/global/interceptDeploymentGroups/my-dg`. See <https://google.aip.dev/124>.  
`connectedDeploymentGroup` |  `object (`[ConnectedDeploymentGroup](https://docs.cloud.google.com/network-security-integration/docs/reference/rest/v1/projects.locations.interceptEndpointGroups#ConnectedDeploymentGroup)`)` Output only. Details about the connected deployment group to this endpoint group.  
`state` |  `enum (`[State](https://docs.cloud.google.com/network-security-integration/docs/reference/rest/v1/projects.locations.interceptEndpointGroups#State)`)` Output only. The current state of the endpoint group. See <https://google.aip.dev/216>.  
`reconciling` |  `boolean` Output only. The current state of the resource does not match the user's intended state, and the system is working to reconcile them. This is part of the normal operation (e.g. adding a new association to the group). See <https://google.aip.dev/128>.  
`associations[]` |  `object (`[AssociationDetails](https://docs.cloud.google.com/network-security-integration/docs/reference/rest/v1/projects.locations.interceptEndpointGroups#AssociationDetails)`)` Output only. List of associations to this endpoint group.  
`description` |  `string` Optional. User-provided description of the endpoint group. Used as additional context for the endpoint group.  
  
## ConnectedDeploymentGroup

The endpoint group's view of a connected deployment group.

JSON representation  
---  
      
    
    {
      "name": string,
      "locations": [
        {
          object ([InterceptLocation](https://docs.cloud.google.com/network-security-integration/docs/reference/rest/v1/InterceptLocation))
        }
      ]
    }  
  
Fields  
---  
`name` |  `string` Output only. The connected deployment group's resource name, for example: `projects/123456789/locations/global/interceptDeploymentGroups/my-dg`. See <https://google.aip.dev/124>.  
`locations[]` |  `object (`[InterceptLocation](https://docs.cloud.google.com/network-security-integration/docs/reference/rest/v1/InterceptLocation)`)` Output only. The list of locations where the deployment group is present.  
  
## State

Endpoint group state.

Enums  
---  
`STATE_UNSPECIFIED` | State not set (this is not a valid state).  
`ACTIVE` | The endpoint group is ready and in sync with the target deployment group.  
`CLOSED` | The deployment group backing this endpoint group has been force-deleted. This endpoint group cannot be used and interception is effectively disabled.  
`CREATING` | The endpoint group is being created.  
`DELETING` | The endpoint group is being deleted.  
`OUT_OF_SYNC` | The endpoint group is out of sync with the backing deployment group. In most cases, this is a result of a transient issue within the system (e.g. an inaccessible location) and the system is expected to recover automatically. See the associations field for details per network and location.  
`DELETE_FAILED` | An attempt to delete the endpoint group has failed. This is a terminal state and the endpoint group is not expected to recover. The only permitted operation is to retry deleting the endpoint group.  
  
## AssociationDetails

The endpoint group's view of a connected association.

JSON representation  
---  
      
    
    {
      "name": string,
      "network": string,
      "state": enum (State)
    }  
  
Fields  
---  
`name` |  `string` Output only. The connected association's resource name, for example: `projects/123456789/locations/global/interceptEndpointGroupAssociations/my-ega`. See <https://google.aip.dev/124>.  
`network` |  `string` Output only. The associated network, for example: projects/123456789/global/networks/my-network. See <https://google.aip.dev/124>.  
`state` |  `enum (`State`)` Output only. Most recent known state of the association.  
  
## Methods  
  
---  
  
### `[create](https://docs.cloud.google.com/network-security-integration/docs/reference/rest/v1/projects.locations.interceptEndpointGroups/create)`

|  Creates an endpoint group in a given project and location.  
  
### `[delete](https://docs.cloud.google.com/network-security-integration/docs/reference/rest/v1/projects.locations.interceptEndpointGroups/delete)`

|  Deletes an endpoint group.  
  
### `[get](https://docs.cloud.google.com/network-security-integration/docs/reference/rest/v1/projects.locations.interceptEndpointGroups/get)`

|  Gets a specific endpoint group.  
  
### `[list](https://docs.cloud.google.com/network-security-integration/docs/reference/rest/v1/projects.locations.interceptEndpointGroups/list)`

|  Lists endpoint groups in a given project and location.  
  
### `[patch](https://docs.cloud.google.com/network-security-integration/docs/reference/rest/v1/projects.locations.interceptEndpointGroups/patch)`

|  Updates an endpoint group.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-12-23 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-12-23 UTC."],[],[]] 
