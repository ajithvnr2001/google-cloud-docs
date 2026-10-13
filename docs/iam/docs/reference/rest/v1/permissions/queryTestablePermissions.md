---
url: https://docs.cloud.google.com/iam/docs/reference/rest/v1/permissions/queryTestablePermissions/
title: Method: permissions.queryTestablePermissions \u00a0|\u00a0 Identity and Access Management (IAM) \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:53:53.804471+00:00
---

# Method: permissions.queryTestablePermissions  |  Identity and Access Management (IAM)  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/iam/docs/reference/rest/v1/permissions/queryTestablePermissions/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ IAM ](https://docs.cloud.google.com/iam/docs)
  * [ Reference ](https://docs.cloud.google.com/iam/docs/apis)



Send feedback 

#  Method: permissions.queryTestablePermissions Stay organized with collections  Save and categorize content based on your preferences. 

  * HTTP request
  * Request body
    * JSON representation
  * Response body
    * JSON representation
  * Authorization scopes
  * Permission
    * JSON representation
  * PermissionLaunchStage
  * CustomRolesSupportLevel
  * Examples
  * Try it!



Lists every permission that you can test on a resource. A permission is testable if you can check whether a principal has that permission on the resource.

### HTTP request

`POST https://iam.googleapis.com/v1/permissions:queryTestablePermissions`

The URL uses [gRPC Transcoding](https://google.aip.dev/127) syntax.

### Request body

The request body contains data with the following structure:

JSON representation  
---  
      
    
    {
      "fullResourceName": string,
      "pageSize": integer,
      "pageToken": string
    }  
  
Fields  
---  
`fullResourceName` |  `string` Required. The full resource name to query from the list of testable permissions.The name follows the Google Cloud Platform resource format. For example, a Cloud Platform project with id `my-project` will be named `//cloudresourcemanager.googleapis.com/projects/my-project`.  
`pageSize` |  `integer` Optional limit on the number of permissions to include in the response.The default is 100, and the maximum is 1,000.  
`pageToken` |  `string` Optional pagination token returned in an earlier QueryTestablePermissionsRequest.  
  
### Response body

The response containing permissions which can be tested on a resource.

If successful, the response body contains data with the following structure:

JSON representation  
---  
      
    
    {
      "permissions": [
        {
          object ([Permission](https://docs.cloud.google.com/iam/docs/reference/rest/v1/permissions/queryTestablePermissions#Permission))
        }
      ],
      "nextPageToken": string
    }  
  
Fields  
---  
`permissions[]` |  `object (`[Permission](https://docs.cloud.google.com/iam/docs/reference/rest/v1/permissions/queryTestablePermissions#Permission)`)` The Permissions testable on the requested resource.  
`nextPageToken` |  `string` To retrieve the next page of results, set `QueryTestableRolesRequest.page_token` to this value.  
  
### Authorization scopes

Requires one of the following OAuth scopes:

  * `https://www.googleapis.com/auth/iam`
  * ` https://www.googleapis.com/auth/cloud-platform`



For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).

## Permission

A permission which can be included by a role.

JSON representation  
---  
      
    
    {
      "name": string,
      "title": string,
      "description": string,
      "onlyInPredefinedRoles": boolean,
      "stage": enum ([PermissionLaunchStage](https://docs.cloud.google.com/iam/docs/reference/rest/v1/permissions/queryTestablePermissions#PermissionLaunchStage)),
      "customRolesSupportLevel": enum ([CustomRolesSupportLevel](https://docs.cloud.google.com/iam/docs/reference/rest/v1/permissions/queryTestablePermissions#CustomRolesSupportLevel)),
      "apiDisabled": boolean,
      "primaryPermission": string
    }  
  
Fields  
---  
`name` |  `string` The name of this Permission.  
`title` |  `string` The title of this Permission.  
`description` |  `string` A brief description of what this Permission is used for.  
`onlyInPredefinedRoles  
**(deprecated)**` |  `boolean` This item is deprecated!  
`stage` |  `enum (`[PermissionLaunchStage](https://docs.cloud.google.com/iam/docs/reference/rest/v1/permissions/queryTestablePermissions#PermissionLaunchStage)`)` The current launch stage of the permission.  
`customRolesSupportLevel` |  `enum (`[CustomRolesSupportLevel](https://docs.cloud.google.com/iam/docs/reference/rest/v1/permissions/queryTestablePermissions#CustomRolesSupportLevel)`)` The current custom role support level.  
`apiDisabled` |  `boolean` The service API associated with the permission is not enabled.  
`primaryPermission` |  `string` The preferred name for this permission. If present, then this permission is an alias of, and equivalent to, the listed primaryPermission.  
  
## PermissionLaunchStage

A stage representing a permission's lifecycle phase.

Enums  
---  
`ALPHA` | The permission is currently in an alpha phase.  
`BETA` | The permission is currently in a beta phase.  
`GA` | The permission is generally available.  
`DEPRECATED` | The permission is being deprecated.  
  
## CustomRolesSupportLevel

The state of the permission with regards to custom roles.

Enums  
---  
`SUPPORTED` | Default state. Permission is fully supported for custom role use.  
`TESTING` | Permission is being tested to check custom role compatibility.  
`NOT_SUPPORTED` | Permission is not supported for custom role use.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-05-21 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-05-21 UTC."],[],[]] 
