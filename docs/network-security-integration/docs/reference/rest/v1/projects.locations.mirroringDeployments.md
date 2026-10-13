---
url: https://docs.cloud.google.com/network-security-integration/docs/reference/rest/v1/projects.locations.mirroringDeployments
title: REST Resource: projects.locations.mirroringDeployments \u00a0|\u00a0 Network Security Integration \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T17:36:32.414859+00:00
---

# REST Resource: projects.locations.mirroringDeployments  |  Network Security Integration  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/network-security-integration/docs/reference/rest/v1/projects.locations.mirroringDeployments

  * [ Home ](https://docs.cloud.google.com/)
  * [ Network Security Integration ](https://docs.cloud.google.com/network-security-integration)
  * [ Reference ](https://docs.cloud.google.com/network-security-integration/docs/apis)



Send feedback 

#  REST Resource: projects.locations.mirroringDeployments Stay organized with collections  Save and categorize content based on your preferences. 

## Resource: MirroringDeployment

A deployment represents a zonal mirroring backend ready to accept GENEVE-encapsulated replica traffic, e.g. a zonal instance group fronted by an internal passthrough load balancer. Deployments are always part of a global deployment group which represents a global mirroring service.

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
      "forwardingRule": string,
      "mirroringDeploymentGroup": string,
      "state": enum (State),
      "reconciling": boolean,
      "description": string
    }  
  
Fields  
---  
`name` |  `string` Immutable. Identifier. The resource name of this deployment, for example: `projects/123456789/locations/us-central1-a/mirroringDeployments/my-dep`. See <https://google.aip.dev/122> for more details.  
`createTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Output only. The timestamp when the resource was created. See <https://google.aip.dev/148#timestamps>.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`updateTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Output only. The timestamp when the resource was most recently updated. See <https://google.aip.dev/148#timestamps>.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`labels` |  `map (key: string, value: string)` Optional. Labels are key/value pairs that help to organize and filter resources.An object containing a list of `"key": value` pairs. Example: `{ "name": "wrench", "mass": "1.3kg", "count": "3" }`.  
`forwardingRule` |  `string` Required. Immutable. The regional forwarding rule that fronts the mirroring collectors, for example: `projects/123456789/regions/us-central1/forwardingRules/my-rule`. See <https://google.aip.dev/124>.  
`mirroringDeploymentGroup` |  `string` Required. Immutable. The deployment group that this deployment is a part of, for example: `projects/123456789/locations/global/mirroringDeploymentGroups/my-dg`. See <https://google.aip.dev/124>.  
`state` |  `enum (`State`)` Output only. The current state of the deployment. See <https://google.aip.dev/216>.  
`reconciling` |  `boolean` Output only. The current state of the resource does not match the user's intended state, and the system is working to reconcile them. This part of the normal operation (e.g. linking a new association to the parent group). See <https://google.aip.dev/128>.  
`description` |  `string` Optional. User-provided description of the deployment. Used as additional context for the deployment.  
  
## Methods  
  
---  
  
### `[create](https://docs.cloud.google.com/network-security-integration/docs/reference/rest/v1/projects.locations.mirroringDeployments/create)`

|  Creates a deployment in a given project and location.  
  
### `[delete](https://docs.cloud.google.com/network-security-integration/docs/reference/rest/v1/projects.locations.mirroringDeployments/delete)`

|  Deletes a deployment.  
  
### `[get](https://docs.cloud.google.com/network-security-integration/docs/reference/rest/v1/projects.locations.mirroringDeployments/get)`

|  Gets a specific deployment.  
  
### `[list](https://docs.cloud.google.com/network-security-integration/docs/reference/rest/v1/projects.locations.mirroringDeployments/list)`

|  Lists deployments in a given project and location.  
  
### `[patch](https://docs.cloud.google.com/network-security-integration/docs/reference/rest/v1/projects.locations.mirroringDeployments/patch)`

|  Updates a deployment.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-12-23 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-12-23 UTC."],[],[]] 
