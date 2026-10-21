---
url: https://docs.cloud.google.com/dataform/reference/rest/v1beta1/projects.locations.repositories.compilationResults
title: REST Resource: projects.locations.repositories.compilationResults \u00a0|\u00a0 Dataform \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T00:42:20.251438+00:00
---

# REST Resource: projects.locations.repositories.compilationResults  |  Dataform  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dataform/reference/rest/v1beta1/projects.locations.repositories.compilationResults

  * [ Home ](https://docs.cloud.google.com/)
  * [ Dataform ](https://docs.cloud.google.com/dataform)
  * [ Reference ](https://docs.cloud.google.com/dataform/docs/authentication)



Send feedback 

#  REST Resource: projects.locations.repositories.compilationResults Stay organized with collections  Save and categorize content based on your preferences. 

  * Resource: CompilationResult
    * JSON representation
  * CompilationError
    * JSON representation
  * GcsRepositorySnapshotMetadata
    * JSON representation
  * Methods



## Resource: CompilationResult

Represents the result of compiling a Dataform project.

JSON representation  
---  
      
    
    {
      "name": string,
      "codeCompilationConfig": {
        object ([CodeCompilationConfig](https://docs.cloud.google.com/dataform/reference/rest/v1beta1/CodeCompilationConfig))
      },
      "resolvedGitCommitSha": string,
      "dataformCoreVersion": string,
      "compilationErrors": [
        {
          object ([CompilationError](https://docs.cloud.google.com/dataform/reference/rest/v1beta1/projects.locations.repositories.compilationResults#CompilationError))
        }
      ],
      "dataEncryptionState": {
        object ([DataEncryptionState](https://docs.cloud.google.com/dataform/reference/rest/v1beta1/DataEncryptionState))
      },
      "createTime": string,
      "privateResourceMetadata": {
        object ([PrivateResourceMetadata](https://docs.cloud.google.com/dataform/reference/rest/v1beta1/PrivateResourceMetadata))
      },
      "gcsRepositorySnapshotMetadata": {
        object ([GcsRepositorySnapshotMetadata](https://docs.cloud.google.com/dataform/reference/rest/v1beta1/projects.locations.repositories.compilationResults#GcsRepositorySnapshotMetadata))
      },
    
      // Union field source can be only one of the following:
      "gitCommitish": string,
      "workspace": string,
      "releaseConfig": string
      // End of list of possible types for union field source.
      "internalMetadata": string
    }  
  
Fields  
---  
`name` |  `string` Output only. The compilation result's name.  
`codeCompilationConfig` |  `object (`[CodeCompilationConfig](https://docs.cloud.google.com/dataform/reference/rest/v1beta1/CodeCompilationConfig)`)` Immutable. If set, fields of `codeCompilationConfig` override the default compilation settings that are specified in dataform.json.  
`resolvedGitCommitSha` |  `string` Output only. The fully resolved Git commit SHA of the code that was compiled. Not set for compilation results whose source is a workspace.  
`dataformCoreVersion` |  `string` Output only. The version of `@dataform/core` that was used for compilation.  
`compilationErrors[]` |  `object (`[CompilationError](https://docs.cloud.google.com/dataform/reference/rest/v1beta1/projects.locations.repositories.compilationResults#CompilationError)`)` Output only. Errors encountered during project compilation.  
`dataEncryptionState` |  `object (`[DataEncryptionState](https://docs.cloud.google.com/dataform/reference/rest/v1beta1/DataEncryptionState)`)` Output only. Only set if the repository has a KMS Key.  
`createTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Output only. The timestamp of when the compilation result was created.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`privateResourceMetadata` |  `object (`[PrivateResourceMetadata](https://docs.cloud.google.com/dataform/reference/rest/v1beta1/PrivateResourceMetadata)`)` Output only. Metadata indicating whether this resource is user-scoped. `CompilationResult` resource is `userScoped` only if it is sourced from a workspace.  
`gcsRepositorySnapshotMetadata` |  `object (`[GcsRepositorySnapshotMetadata](https://docs.cloud.google.com/dataform/reference/rest/v1beta1/projects.locations.repositories.compilationResults#GcsRepositorySnapshotMetadata)`)` Output only. Metadata about the repository snapshot used by scheduled notebooks.  
Union field `source`. The source of the compilation result. `source` can be only one of the following:  
`gitCommitish` |  `string` Immutable. Git commit/tag/branch name at which the repository should be compiled. Must exist in the remote repository. Examples: - a commit SHA: `12ade345` \- a tag: `tag1` \- a branch name: `branch1`  
`workspace` |  `string` Immutable. The name of the workspace to compile. Must be in the format `projects/*/locations/*/repositories/*/workspaces/*`.  
`releaseConfig` |  `string` Immutable. The name of the release config to compile. Must be in the format `projects/*/locations/*/repositories/*/releaseConfigs/*`.  
`internalMetadata` |  `string` Output only. All the metadata information that is used internally to serve the resource. For example: timestamps, flags, status fields, etc. The format of this field is a JSON string.  
  
## CompilationError

An error encountered when attempting to compile a Dataform project.

JSON representation  
---  
      
    
    {
      "message": string,
      "stack": string,
      "path": string,
      "actionTarget": {
        object ([Target](https://docs.cloud.google.com/dataform/reference/rest/v1beta1/Target))
      }
    }  
  
Fields  
---  
`message` |  `string` Output only. The error's top level message.  
`stack` |  `string` Output only. The error's full stack trace.  
`path` |  `string` Output only. The path of the file where this error occurred, if available, relative to the project root.  
`actionTarget` |  `object (`[Target](https://docs.cloud.google.com/dataform/reference/rest/v1beta1/Target)`)` Output only. The identifier of the action where this error occurred, if available.  
  
## GcsRepositorySnapshotMetadata

Metadata about a repository snapshot stored in Google Cloud Storage.

JSON representation  
---  
      
    
    {
      "repositorySnapshotUri": string,
      "crc32cChecksum": string,
      "generation": string
    }  
  
Fields  
---  
`repositorySnapshotUri` |  `string` Output only. The Google Cloud Storage URI of the repository snapshot.  
`crc32cChecksum` |  `string` Output only. The crc32c checksum of the repository snapshot, big-endian base64 encoded.  
`generation` |  `string ([int64](https://developers.google.com/discovery/v1/type-format) format)` Output only. The generation number of the Cloud Storage object. See <https://cloud.google.com/storage/docs/metadata#generation-number>.  
  
## Methods  
  
---  
  
### `[create](https://docs.cloud.google.com/dataform/reference/rest/v1beta1/projects.locations.repositories.compilationResults/create)`

|  Creates a new CompilationResult in a given project and location.  
  
### `[get](https://docs.cloud.google.com/dataform/reference/rest/v1beta1/projects.locations.repositories.compilationResults/get)`

|  Fetches a single CompilationResult.  
  
### `[list](https://docs.cloud.google.com/dataform/reference/rest/v1beta1/projects.locations.repositories.compilationResults/list)`

|  Lists CompilationResults in a given Repository.  
  
### `[query](https://docs.cloud.google.com/dataform/reference/rest/v1beta1/projects.locations.repositories.compilationResults/query)`

|  Returns CompilationResultActions in a given CompilationResult.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-08-17 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-08-17 UTC."],[],[]] 
