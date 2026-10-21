---
url: https://docs.cloud.google.com/deploy/docs/api/reference/rest/v1/projects.locations.customTargetTypes
title: REST Resource: projects.locations.customTargetTypes \u00a0|\u00a0 Cloud Deploy \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T09:14:55.955716+00:00
---

# REST Resource: projects.locations.customTargetTypes  |  Cloud Deploy  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/deploy/docs/api/reference/rest/v1/projects.locations.customTargetTypes

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Cloud Deploy ](https://docs.cloud.google.com/deploy/docs)
  * [ Reference ](https://docs.cloud.google.com/deploy/docs/api)



Send feedback 

#  REST Resource: projects.locations.customTargetTypes Stay organized with collections  Save and categorize content based on your preferences. 

  * Resource: CustomTargetType
    * JSON representation
    * CustomTargetSkaffoldActions
      * JSON representation
    * SkaffoldModules
      * JSON representation
    * SkaffoldGitSource
      * JSON representation
    * SkaffoldGCSSource
      * JSON representation
    * SkaffoldGCBRepoSource
      * JSON representation
    * CustomTargetTasks
      * JSON representation
  * Methods



## Resource: CustomTargetType

A `CustomTargetType` resource in the Cloud Deploy API.

A `CustomTargetType` defines a type of custom target that can be referenced in a `Target` in order to facilitate deploying to other systems besides the supported runtimes.

JSON representation  
---  
      
    
    {
      "name": string,
      "customTargetTypeId": string,
      "uid": string,
      "description": string,
      "annotations": {
        string: string,
        ...
      },
      "labels": {
        string: string,
        ...
      },
      "createTime": string,
      "updateTime": string,
      "etag": string,
    
      // Union field definition can be only one of the following:
      "customActions": {
        object ([CustomTargetSkaffoldActions](https://docs.cloud.google.com/deploy/docs/api/reference/rest/v1/projects.locations.customTargetTypes#CustomTargetType.CustomTargetSkaffoldActions))
      },
      "tasks": {
        object ([CustomTargetTasks](https://docs.cloud.google.com/deploy/docs/api/reference/rest/v1/projects.locations.customTargetTypes#CustomTargetType.CustomTargetTasks))
      }
      // End of list of possible types for union field definition.
    }  
  
Fields  
---  
`name` |  `string` Identifier. Name of the `CustomTargetType`. Format is `projects/{project}/locations/{location}/customTargetTypes/{customTargetType}`. The `customTargetType` component must match `[a-z]([a-z0-9-]{0,61}[a-z0-9])?`  
`customTargetTypeId` |  `string` Output only. Resource id of the `CustomTargetType`.  
`uid` |  `string` Output only. Unique identifier of the `CustomTargetType`.  
`description` |  `string` Optional. Description of the `CustomTargetType`. Max length is 255 characters.  
`annotations` |  `map (key: string, value: string)` Optional. User annotations. These attributes can only be set and used by the user, and not by Cloud Deploy. See <https://google.aip.dev/128#annotations> for more details such as format and size limitations.An object containing a list of `"key": value` pairs. Example: `{ "name": "wrench", "mass": "1.3kg", "count": "3" }`.  
`labels` |  `map (key: string, value: string)` Optional. Labels are attributes that can be set and used by both the user and by Cloud Deploy. Labels must meet the following constraints:

  * Keys and values can contain only lowercase letters, numeric characters, underscores, and dashes.
  * All characters must use UTF-8 encoding, and international characters are allowed.
  * Keys must start with a lowercase letter or international character.
  * Each resource is limited to a maximum of 64 labels.

Both keys and values are additionally constrained to be <= 128 bytes.An object containing a list of `"key": value` pairs. Example: `{ "name": "wrench", "mass": "1.3kg", "count": "3" }`.  
`createTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Output only. Time at which the `CustomTargetType` was created.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`updateTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Output only. Most recent time at which the `CustomTargetType` was updated.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`etag` |  `string` Optional. This checksum is computed by the server based on the value of other fields, and may be sent on update and delete requests to ensure the client has an up-to-date value before proceeding.  
Union field `definition`. Defines the `CustomTargetType` renderer and deployer. `definition` can be only one of the following:  
`customActions` |  `object (`[CustomTargetSkaffoldActions](https://docs.cloud.google.com/deploy/docs/api/reference/rest/v1/projects.locations.customTargetTypes#CustomTargetType.CustomTargetSkaffoldActions)`)` Optional. Configures render and deploy for the `CustomTargetType` using Skaffold custom actions.  
`tasks` |  `object (`[CustomTargetTasks](https://docs.cloud.google.com/deploy/docs/api/reference/rest/v1/projects.locations.customTargetTypes#CustomTargetType.CustomTargetTasks)`)` Optional. Configures render and deploy for the `CustomTargetType` using tasks.  
  
### CustomTargetSkaffoldActions

CustomTargetSkaffoldActions represents the `CustomTargetType` configuration using Skaffold custom actions.

JSON representation  
---  
      
    
    {
      "renderAction": string,
      "deployAction": string,
      "includeSkaffoldModules": [
        {
          object ([SkaffoldModules](https://docs.cloud.google.com/deploy/docs/api/reference/rest/v1/projects.locations.customTargetTypes#CustomTargetType.SkaffoldModules))
        }
      ]
    }  
  
Fields  
---  
`renderAction` |  `string` Optional. The Skaffold custom action responsible for render operations. If not provided then Cloud Deploy will perform the render operations via `skaffold render`.  
`deployAction` |  `string` Required. The Skaffold custom action responsible for deploy operations.  
`includeSkaffoldModules[]` |  `object (`[SkaffoldModules](https://docs.cloud.google.com/deploy/docs/api/reference/rest/v1/projects.locations.customTargetTypes#CustomTargetType.SkaffoldModules)`)` Optional. List of Skaffold modules Cloud Deploy will include in the Skaffold Config as required before performing diagnose.  
  
### SkaffoldModules

Skaffold Config modules and their remote source.

JSON representation  
---  
      
    
    {
      "configs": [
        string
      ],
    
      // Union field source can be only one of the following:
      "git": {
        object ([SkaffoldGitSource](https://docs.cloud.google.com/deploy/docs/api/reference/rest/v1/projects.locations.customTargetTypes#CustomTargetType.SkaffoldGitSource))
      },
      "googleCloudStorage": {
        object ([SkaffoldGCSSource](https://docs.cloud.google.com/deploy/docs/api/reference/rest/v1/projects.locations.customTargetTypes#CustomTargetType.SkaffoldGCSSource))
      },
      "googleCloudBuildRepo": {
        object ([SkaffoldGCBRepoSource](https://docs.cloud.google.com/deploy/docs/api/reference/rest/v1/projects.locations.customTargetTypes#CustomTargetType.SkaffoldGCBRepoSource))
      }
      // End of list of possible types for union field source.
    }  
  
Fields  
---  
`configs[]` |  `string` Optional. The Skaffold Config modules to use from the specified source.  
Union field `source`. The source that contains the Skaffold Config modules. `source` can be only one of the following:  
`git` |  `object (`[SkaffoldGitSource](https://docs.cloud.google.com/deploy/docs/api/reference/rest/v1/projects.locations.customTargetTypes#CustomTargetType.SkaffoldGitSource)`)` Optional. Remote git repository containing the Skaffold Config modules.  
`googleCloudStorage` |  `object (`[SkaffoldGCSSource](https://docs.cloud.google.com/deploy/docs/api/reference/rest/v1/projects.locations.customTargetTypes#CustomTargetType.SkaffoldGCSSource)`)` Optional. Cloud Storage bucket containing the Skaffold Config modules.  
`googleCloudBuildRepo` |  `object (`[SkaffoldGCBRepoSource](https://docs.cloud.google.com/deploy/docs/api/reference/rest/v1/projects.locations.customTargetTypes#CustomTargetType.SkaffoldGCBRepoSource)`)` Optional. Cloud Build V2 repository containing the Skaffold Config modules.  
  
### SkaffoldGitSource

Git repository containing Skaffold Config modules.

JSON representation  
---  
      
    
    {
      "repo": string,
      "path": string,
      "ref": string
    }  
  
Fields  
---  
`repo` |  `string` Required. Git repository the package should be cloned from.  
`path` |  `string` Optional. Relative path from the repository root to the Skaffold file.  
`ref` |  `string` Optional. Git branch or tag to use when cloning the repository.  
  
### SkaffoldGCSSource

Cloud Storage bucket containing Skaffold Config modules.

JSON representation  
---  
      
    
    {
      "source": string,
      "path": string
    }  
  
Fields  
---  
`source` |  `string` Required. Cloud Storage source paths to copy recursively. For example, providing "gs://my-bucket/dir/configs/*" will result in Skaffold copying all files within the "dir/configs" directory in the bucket "my-bucket".  
`path` |  `string` Optional. Relative path from the source to the Skaffold file.  
  
### SkaffoldGCBRepoSource

Cloud Build V2 Repository containing Skaffold Configs.

JSON representation  
---  
      
    
    {
      "repository": string,
      "path": string,
      "ref": string
    }  
  
Fields  
---  
`repository` |  `string` Required. Name of the Cloud Build V2 Repository. Format is projects/{project}/locations/{location}/connections/{connection}/repositories/{repository}.  
`path` |  `string` Optional. Relative path from the repository root to the Skaffold Config file.  
`ref` |  `string` Optional. Branch or tag to use when cloning the repository.  
  
### CustomTargetTasks

CustomTargetTasks represents the `CustomTargetType` configuration using tasks.

JSON representation  
---  
      
    
    {
      "render": {
        object ([Task](https://docs.cloud.google.com/deploy/docs/api/reference/rest/v1/Task))
      },
      "deploy": {
        object ([Task](https://docs.cloud.google.com/deploy/docs/api/reference/rest/v1/Task))
      }
    }  
  
Fields  
---  
`render` |  `object (`[Task](https://docs.cloud.google.com/deploy/docs/api/reference/rest/v1/Task)`)` Optional. The task responsible for render operations. If not provided then Cloud Deploy will perform its default rendering operation.  
`deploy` |  `object (`[Task](https://docs.cloud.google.com/deploy/docs/api/reference/rest/v1/Task)`)` Required. The task responsible for deploy operations.  
  
## Methods  
  
---  
  
### `[create](https://docs.cloud.google.com/deploy/docs/api/reference/rest/v1/projects.locations.customTargetTypes/create)`

|  Creates a new CustomTargetType in a given project and location.  
  
### `[delete](https://docs.cloud.google.com/deploy/docs/api/reference/rest/v1/projects.locations.customTargetTypes/delete)`

|  Deletes a single CustomTargetType.  
  
### `[get](https://docs.cloud.google.com/deploy/docs/api/reference/rest/v1/projects.locations.customTargetTypes/get)`

|  Gets details of a single CustomTargetType.  
  
### `[getIamPolicy](https://docs.cloud.google.com/deploy/docs/api/reference/rest/v1/projects.locations.customTargetTypes/getIamPolicy)`

|  Gets the access control policy for a resource.  
  
### `[list](https://docs.cloud.google.com/deploy/docs/api/reference/rest/v1/projects.locations.customTargetTypes/list)`

|  Lists CustomTargetTypes in a given project and location.  
  
### `[patch](https://docs.cloud.google.com/deploy/docs/api/reference/rest/v1/projects.locations.customTargetTypes/patch)`

|  Updates a single CustomTargetType.  
  
### `[setIamPolicy](https://docs.cloud.google.com/deploy/docs/api/reference/rest/v1/projects.locations.customTargetTypes/setIamPolicy)`

|  Sets the access control policy on the specified resource.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-06-02 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-06-02 UTC."],[],[]] 
