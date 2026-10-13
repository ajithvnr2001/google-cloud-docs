---
url: https://docs.cloud.google.com/network-security-integration/docs/reference/rest/v1/projects.locations.interceptDeployments
title: REST Resource: projects.locations.interceptDeployments \u00a0|\u00a0 Network Security Integration \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T16:24:18.402914+00:00
---

# REST Resource: projects.locations.interceptDeployments  |  Network Security Integration  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/network-security-integration/docs/reference/rest/v1/projects.locations.interceptDeployments

  * [ Home ](https://docs.cloud.google.com/)
  * [ Network Security Integration ](https://docs.cloud.google.com/network-security-integration)
  * [ Reference ](https://docs.cloud.google.com/network-security-integration/docs/apis)



Send feedback 

#  REST Resource: projects.locations.interceptDeployments Stay organized with collections  Save and categorize content based on your preferences. 

## Resource: InterceptDeployment

A deployment represents a zonal intercept backend ready to accept GENEVE-encapsulated traffic, e.g. a zonal instance group fronted by an internal passthrough load balancer. Deployments are always part of a global deployment group which represents a global intercept service.

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
      "interceptDeploymentGroup": string,
      "state": enum ([State](https://docs.cloud.google.com/network-security-integration/docs/reference/rest/v1/State)),
      "reconciling": boolean,
      "description": string
    }  
  
Fields  
---  
`name` |  `string` Immutable. Identifier. The resource name of this deployment, for example: `projects/123456789/locations/us-central1-a/interceptDeployments/my-dep`. See <https://google.aip.dev/122> for more details.  
`createTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Output only. The timestamp when the resource was created. See <https://google.aip.dev/148#timestamps>.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`updateTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Output only. The timestamp when the resource was most recently updated. See <https://google.aip.dev/148#timestamps>.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`labels` |  `map (key: string, value: string)` Optional. Labels are key/value pairs that help to organize and filter resources.An object containing a list of `"key": value` pairs. Example: `{ "name": "wrench", "mass": "1.3kg", "count": "3" }`.  
`forwardingRule` |  `string` Required. Immutable. The regional forwarding rule that fronts the interceptors, for example: `projects/123456789/regions/us-central1/forwardingRules/my-rule`. See <https://google.aip.dev/124>.  
`interceptDeploymentGroup` |  `string` Required. Immutable. The deployment group that this deployment is a part of, for example: `projects/123456789/locations/global/interceptDeploymentGroups/my-dg`. See <https://google.aip.dev/124>.  
`state` |  `enum (`[State](https://docs.cloud.google.com/network-security-integration/docs/reference/rest/v1/State)`)` Output only. The current state of the deployment. See <https://google.aip.dev/216>.  
`reconciling` |  `boolean` Output only. The current state of the resource does not match the user's intended state, and the system is working to reconcile them. This part of the normal operation (e.g. linking a new association to the parent group). See <https://google.aip.dev/128>.  
`description` |  `string` Optional. User-provided description of the deployment. Used as additional context for the deployment.  
  
## Methods  
  
---  
  
### `[create](https://docs.cloud.google.com/network-security-integration/docs/reference/rest/v1/projects.locations.interceptDeployments/create)`

|  Creates a deployment in a given project and location.  
  
### `[delete](https://docs.cloud.google.com/network-security-integration/docs/reference/rest/v1/projects.locations.interceptDeployments/delete)`

|  Deletes a deployment.  
  
### `[get](https://docs.cloud.google.com/network-security-integration/docs/reference/rest/v1/projects.locations.interceptDeployments/get)`

|  Gets a specific deployment.  
  
### `[list](https://docs.cloud.google.com/network-security-integration/docs/reference/rest/v1/projects.locations.interceptDeployments/list)`

|  Lists deployments in a given project and location.  
  
### `[patch](https://docs.cloud.google.com/network-security-integration/docs/reference/rest/v1/projects.locations.interceptDeployments/patch)`

|  Updates a deployment.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-12-23 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-12-23 UTC."],[],[]] 
