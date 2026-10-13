---
url: https://docs.cloud.google.com/application-design-center/docs/reference/rest/v1/projects.locations.spaces
title: REST Resource: projects.locations.spaces \u00a0|\u00a0 Application Design Center \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T19:30:05.985649+00:00
---

# REST Resource: projects.locations.spaces  |  Application Design Center  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/application-design-center/docs/reference/rest/v1/projects.locations.spaces

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Application Design Center ](https://docs.cloud.google.com/application-design-center/docs)
  * [ Reference ](https://docs.cloud.google.com/application-design-center/docs/apis)



Send feedback 

#  REST Resource: projects.locations.spaces Stay organized with collections  Save and categorize content based on your preferences. 

  * Resource: Space
    * JSON representation
  * Methods



## Resource: Space

Space is a top level resource for managing teams building applications through Application Design Center.

JSON representation  
---  
      
    
    {
      "name": string,
      "displayName": string,
      "description": string,
      "createTime": string,
      "updateTime": string,
      "gcsBucket": string,
      "tags": {
        string: string,
        ...
      },
      "enableGcpSharedTemplates": boolean
    }  
  
Fields  
---  
`name` |  `string` Identifier. The space name.  
`displayName` |  `string` Optional. Display name for the space.  
`description` |  `string` Optional. Description for the space.  
`createTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Output only. Space creation timestamp.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`updateTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Output only. Space update timestampUses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`gcsBucket` |  `string` Optional. An existing Google Cloud Storage bucket that you want to use instead of creating a new bucket during Application Design Center setup. If not provided, a default bucket is created during setup. The bucket must exist in the same project as the space. If the bucket name does not exist in the same project as the space, the request fails with an INVALID_ARGUMENT error. If you do not have access to the bucket, the request fails with a PERMISSION_DENIED error. Format: {$bucket_name} For example, if the Cloud Storage bucket URI is gs:\/\/{$bucket_name}, the format is {$bucket_name}.  
`tags` |  `map (key: string, value: string)` Optional. Input only. Immutable. Tags are key/values bound to space resource. Example:
    
    
      "123/environment": "production"
      "123/costCenter": "marketing"
    

For more information on tag creation and management, see <https://cloud.google.com/resource-manager/docs/tags/tags-overview>.An object containing a list of `"key": value` pairs. Example: `{ "name": "wrench", "mass": "1.3kg", "count": "3" }`.  
`enableGcpSharedTemplates` |  `boolean` Optional. Flag to enable Google opinionated shared templates.  
  
## Methods  
  
---  
  
### `[create](https://docs.cloud.google.com/application-design-center/docs/reference/rest/v1/projects.locations.spaces/create)`

|  Creates a space.  
  
### `[delete](https://docs.cloud.google.com/application-design-center/docs/reference/rest/v1/projects.locations.spaces/delete)`

|  Deletes a space.  
  
### `[generateTerraformPlanAssessmentReport](https://docs.cloud.google.com/application-design-center/docs/reference/rest/v1/projects.locations.spaces/generateTerraformPlanAssessmentReport)`

|  Generate a Terraform plan assessment report for a given Terraform plan.  
  
### `[get](https://docs.cloud.google.com/application-design-center/docs/reference/rest/v1/projects.locations.spaces/get)`

|  Gets details about a space.  
  
### `[getIamPolicy](https://docs.cloud.google.com/application-design-center/docs/reference/rest/v1/projects.locations.spaces/getIamPolicy)`

|  Gets the access control policy for a resource.  
  
### `[list](https://docs.cloud.google.com/application-design-center/docs/reference/rest/v1/projects.locations.spaces/list)`

|  Lists spaces in a given project and location.  
  
### `[patch](https://docs.cloud.google.com/application-design-center/docs/reference/rest/v1/projects.locations.spaces/patch)`

|  Updates a space.  
  
### `[registerAppHubApplicationResources](https://docs.cloud.google.com/application-design-center/docs/reference/rest/v1/projects.locations.spaces/registerAppHubApplicationResources)`

|  Register deployed resources from terraform state file with App Hub without needing a space.  
  
### `[setIamPolicy](https://docs.cloud.google.com/application-design-center/docs/reference/rest/v1/projects.locations.spaces/setIamPolicy)`

|  Sets the access control policy on the specified resource.  
  
### `[testIamPermissions](https://docs.cloud.google.com/application-design-center/docs/reference/rest/v1/projects.locations.spaces/testIamPermissions)`

|  Returns permissions that a caller has on the specified resource.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-06-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-06-03 UTC."],[],[]] 
