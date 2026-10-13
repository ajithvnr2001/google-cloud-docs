---
url: https://docs.cloud.google.com/security-command-center/docs/reference/securityposture/rest/v1/organizations.locations.postureDeployments
title: REST Resource: organizations.locations.postureDeployments \u00a0|\u00a0 Security Command Center \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T19:16:55.632563+00:00
---

# REST Resource: organizations.locations.postureDeployments  |  Security Command Center  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/security-command-center/docs/reference/securityposture/rest/v1/organizations.locations.postureDeployments

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Security Command Center ](https://docs.cloud.google.com/security-command-center/docs)
  * [ Reference ](https://docs.cloud.google.com/security-command-center/docs/vulnerability-findings-index)



Send feedback 

#  REST Resource: organizations.locations.postureDeployments Stay organized with collections  Save and categorize content based on your preferences. 

  * Resource: PostureDeployment
    * JSON representation
  * State
  * Methods



## Resource: PostureDeployment

Details for a `[Posture](https://docs.cloud.google.com/security-command-center/docs/reference/securityposture/rest/v1/organizations.locations.postures#Posture)` deployment on an organization, folder, or project.

You can deploy at most one posture to each organization, folder, or project. The parent resource for a posture deployment is always the organization, even if the deployment applies to a folder or project.

JSON representation  
---  
      
    
    {
      "name": string,
      "targetResource": string,
      "state": enum ([State](https://docs.cloud.google.com/security-command-center/docs/reference/securityposture/rest/v1/organizations.locations.postureDeployments#State)),
      "postureId": string,
      "postureRevisionId": string,
      "createTime": string,
      "updateTime": string,
      "description": string,
      "etag": string,
      "annotations": {
        string: string,
        ...
      },
      "reconciling": boolean,
      "desiredPostureId": string,
      "desiredPostureRevisionId": string,
      "failureMessage": string,
      "categories": [
        enum ([Category](https://docs.cloud.google.com/security-command-center/docs/reference/securityposture/rest/v1/Category))
      ]
    }  
  
Fields  
---  
`name` |  `string` Required. Identifier. The name of the posture deployment, in the format `organizations/{organization}/locations/global/postureDeployments/{deployment_id}`.  
`targetResource` |  `string` Required. The organization, folder, or project where the posture is deployed. Uses one of the following formats:

  * `organizations/{organization_number}`
  * `folders/{folder_number}`
  * `projects/{project_number}`

  
`state` |  `enum (`[State](https://docs.cloud.google.com/security-command-center/docs/reference/securityposture/rest/v1/organizations.locations.postureDeployments#State)`)` Output only. The state of the posture deployment.  
`postureId` |  `string` Required. The posture used in the deployment, in the format `organizations/{organization}/locations/global/postures/{postureId}`.  
`postureRevisionId` |  `string` Required. The revision ID of the posture used in the deployment.  
`createTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Output only. The time at which the posture deployment was created.Uses RFC 3339, where generated output will always be Z-normalized and uses 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`updateTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Output only. The time at which the posture deployment was last updated.Uses RFC 3339, where generated output will always be Z-normalized and uses 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`description` |  `string` Optional. A description of the posture deployment.  
`etag` |  `string` Optional. An opaque identifier for the current version of the posture deployment.To prevent concurrent updates from overwriting each other, always provide the `etag` when you update a posture deployment. You can also provide the `etag` when you delete a posture deployment, to help ensure that you're deleting the intended posture deployment.  
`annotations` |  `map (key: string, value: string)` Optional. The user-specified annotations for the posture deployment.For details about the values you can use in an annotation, see [AIP-148: Standard fields](https://google.aip.dev/148#annotations).An object containing a list of `"key": value` pairs. Example: `{ "name": "wrench", "mass": "1.3kg", "count": "3" }`.  
`reconciling` |  `boolean` Output only. Whether the posture deployment is in the process of being updated.  
`desiredPostureId` |  `string` Output only. The posture ID that was specified for the deployment. Present only if the posture deployment is in a failed state.  
`desiredPostureRevisionId` |  `string` Output only. The revision ID of the posture that was specified for the deployment. Present only if the deployment is in a failed state.  
`failureMessage` |  `string` Output only. A description of why the posture deployment failed. Present only if the deployment is in a failed state.  
`categories[]` |  `enum (`[Category](https://docs.cloud.google.com/security-command-center/docs/reference/securityposture/rest/v1/Category)`)` Output only. The categories that the posture deployment belongs to, as determined by the Security Posture API.  
  
## State

The state of a `[PostureDeployment](https://docs.cloud.google.com/security-command-center/docs/reference/securityposture/rest/v1/organizations.locations.postureDeployments#PostureDeployment)`.

Enums  
---  
`STATE_UNSPECIFIED` | Default value. This value is unused.  
`CREATING` | The posture deployment is being created.  
`DELETING` | The posture deployment is being deleted.  
`UPDATING` | The posture deployment is being updated.  
`ACTIVE` | The posture deployment is active and in use.  
`CREATE_FAILED` | The posture deployment could not be created.  
`UPDATE_FAILED` | The posture deployment could not be updated.  
`DELETE_FAILED` | The posture deployment could not be deleted.  
  
## Methods  
  
---  
  
### `[create](https://docs.cloud.google.com/security-command-center/docs/reference/securityposture/rest/v1/organizations.locations.postureDeployments/create)`

|  Creates a new `[PostureDeployment](https://docs.cloud.google.com/security-command-center/docs/reference/securityposture/rest/v1/organizations.locations.postureDeployments#PostureDeployment)` in a given project and location.  
  
### `[delete](https://docs.cloud.google.com/security-command-center/docs/reference/securityposture/rest/v1/organizations.locations.postureDeployments/delete)`

|  Deletes a `[PostureDeployment](https://docs.cloud.google.com/security-command-center/docs/reference/securityposture/rest/v1/organizations.locations.postureDeployments#PostureDeployment)`.  
  
### `[get](https://docs.cloud.google.com/security-command-center/docs/reference/securityposture/rest/v1/organizations.locations.postureDeployments/get)`

|  Gets details for a `[PostureDeployment](https://docs.cloud.google.com/security-command-center/docs/reference/securityposture/rest/v1/organizations.locations.postureDeployments#PostureDeployment)`.  
  
### `[list](https://docs.cloud.google.com/security-command-center/docs/reference/securityposture/rest/v1/organizations.locations.postureDeployments/list)`

|  Lists every `[PostureDeployment](https://docs.cloud.google.com/security-command-center/docs/reference/securityposture/rest/v1/organizations.locations.postureDeployments#PostureDeployment)` in a project and location.  
  
### `[patch](https://docs.cloud.google.com/security-command-center/docs/reference/securityposture/rest/v1/organizations.locations.postureDeployments/patch)`

|  Updates an existing `[PostureDeployment](https://docs.cloud.google.com/security-command-center/docs/reference/securityposture/rest/v1/organizations.locations.postureDeployments#PostureDeployment)`.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-08-14 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-08-14 UTC."],[],[]] 
