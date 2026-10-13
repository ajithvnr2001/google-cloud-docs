---
url: https://docs.cloud.google.com/iam/docs/reference/rest/v1/organizations.roles
title: REST Resource: organizations.roles \u00a0|\u00a0 Identity and Access Management (IAM) \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:53:52.284287+00:00
---

# REST Resource: organizations.roles  |  Identity and Access Management (IAM)  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/iam/docs/reference/rest/v1/organizations.roles

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ IAM ](https://docs.cloud.google.com/iam/docs)
  * [ Reference ](https://docs.cloud.google.com/iam/docs/apis)



Send feedback 

#  REST Resource: organizations.roles Stay organized with collections  Save and categorize content based on your preferences. 

  * Resource: Role
    * JSON representation
    * RoleLaunchStage
  * Methods



## Resource: Role

A role in the Identity and Access Management API.

JSON representation  
---  
      
    
    {
      "name": string,
      "title": string,
      "description": string,
      "includedPermissions": [
        string
      ],
      "stage": enum ([RoleLaunchStage](https://docs.cloud.google.com/iam/docs/reference/rest/v1/organizations.roles#Role.RoleLaunchStage)),
      "etag": string,
      "deleted": boolean
    }  
  
Fields  
---  
`name` |  `string` The name of the role.When `Role` is used in `roles.create`, the role name must not be set.When `Role` is used in output and other input such as `roles.patch`, the role name is the complete path. For example, `roles/logging.viewer` for predefined roles, `organizations/{ORGANIZATION_ID}/roles/myRole` for organization-level custom roles, and `projects/{PROJECT_ID}/roles/myRole` for project-level custom roles.  
`title` |  `string` Optional. A human-readable title for the role. Typically this is limited to 100 UTF-8 bytes.  
`description` |  `string` Optional. A human-readable description for the role.  
`includedPermissions[]` |  `string` The names of the permissions this role grants when bound in an IAM policy.  
`stage` |  `enum (`[RoleLaunchStage](https://docs.cloud.google.com/iam/docs/reference/rest/v1/organizations.roles#Role.RoleLaunchStage)`)` The current launch stage of the role. If the `ALPHA` launch stage has been selected for a role, the `stage` field will not be included in the returned definition for the role.  
`etag` |  `string ([bytes](https://developers.google.com/discovery/v1/type-format) format)` Used to perform a consistent read-modify-write.A base64-encoded string.  
`deleted` |  `boolean` The current deleted state of the role. This field is read only. It will be ignored in calls to roles.create and roles.patch.  
  
### RoleLaunchStage

A stage representing a role's lifecycle phase.

Enums  
---  
`ALPHA` | The user has indicated this role is currently in an Alpha phase. If this launch stage is selected, the `stage` field will not be included when requesting the definition for a given role.  
`BETA` | The user has indicated this role is currently in a Beta phase.  
`GA` | The user has indicated this role is generally available.  
`DEPRECATED` | The user has indicated this role is being deprecated.  
`DISABLED` | This role is disabled and will not contribute permissions to any principals it is granted to in policies.  
`EAP` | The user has indicated this role is currently in an EAP phase.  
  
## Methods  
  
---  
  
### `[create](https://docs.cloud.google.com/iam/docs/reference/rest/v1/organizations.roles/create)`

|  Creates a new custom `[Role](https://docs.cloud.google.com/iam/docs/reference/rest/v1/organizations.roles#Role)`.  
  
### `[delete](https://docs.cloud.google.com/iam/docs/reference/rest/v1/organizations.roles/delete)`

|  Deletes a custom `[Role](https://docs.cloud.google.com/iam/docs/reference/rest/v1/organizations.roles#Role)`.  
  
### `[get](https://docs.cloud.google.com/iam/docs/reference/rest/v1/organizations.roles/get)`

|  Gets the definition of a `[Role](https://docs.cloud.google.com/iam/docs/reference/rest/v1/organizations.roles#Role)`.  
  
### `[list](https://docs.cloud.google.com/iam/docs/reference/rest/v1/organizations.roles/list)`

|  Lists every predefined `[Role](https://docs.cloud.google.com/iam/docs/reference/rest/v1/organizations.roles#Role)` that IAM supports, or every custom role that is defined for an organization or project.  
  
### `[patch](https://docs.cloud.google.com/iam/docs/reference/rest/v1/organizations.roles/patch)`

|  Updates the definition of a custom `[Role](https://docs.cloud.google.com/iam/docs/reference/rest/v1/organizations.roles#Role)`.  
  
### `[undelete](https://docs.cloud.google.com/iam/docs/reference/rest/v1/organizations.roles/undelete)`

|  Undeletes a custom `[Role](https://docs.cloud.google.com/iam/docs/reference/rest/v1/organizations.roles#Role)`.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-05-21 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-05-21 UTC."],[],[]] 
