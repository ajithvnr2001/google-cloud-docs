---
url: https://docs.cloud.google.com/dataform/reference/rest/v1beta1/projects.locations.repositories
title: REST Resource: projects.locations.repositories \u00a0|\u00a0 Dataform \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T00:42:17.239912+00:00
---

# REST Resource: projects.locations.repositories  |  Dataform  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dataform/reference/rest/v1beta1/projects.locations.repositories

  * [ Home ](https://docs.cloud.google.com/)
  * [ Dataform ](https://docs.cloud.google.com/dataform)
  * [ Reference ](https://docs.cloud.google.com/dataform/docs/authentication)



Send feedback 

#  REST Resource: projects.locations.repositories Stay organized with collections  Save and categorize content based on your preferences. 

  * Resource: Repository
    * JSON representation
  * GitRemoteSettings
    * JSON representation
  * SshAuthenticationConfig
    * JSON representation
  * TokenStatus
  * WorkspaceCompilationOverrides
    * JSON representation
  * EndUserAuthConfig
    * JSON representation
  * Methods



## Resource: Repository

Represents a Dataform Git repository.

JSON representation  
---  
      
    
    {
      "name": string,
      "createTime": string,
      "displayName": string,
      "gitRemoteSettings": {
        object ([GitRemoteSettings](https://docs.cloud.google.com/dataform/reference/rest/v1beta1/projects.locations.repositories#GitRemoteSettings))
      },
      "npmrcEnvironmentVariablesSecretVersion": string,
      "workspaceCompilationOverrides": {
        object ([WorkspaceCompilationOverrides](https://docs.cloud.google.com/dataform/reference/rest/v1beta1/projects.locations.repositories#WorkspaceCompilationOverrides))
      },
      "labels": {
        string: string,
        ...
      },
      "setAuthenticatedUserAdmin": boolean,
      "serviceAccount": string,
      "kmsKeyName": string,
      "dataEncryptionState": {
        object ([DataEncryptionState](https://docs.cloud.google.com/dataform/reference/rest/v1beta1/DataEncryptionState))
      },
      "endUserAuthConfig": {
        object ([EndUserAuthConfig](https://docs.cloud.google.com/dataform/reference/rest/v1beta1/projects.locations.repositories#EndUserAuthConfig))
      },
      "containingFolder": string,
      "teamFolderName": string,
      "strictActAsChecks": boolean,
      "internalMetadata": string
    }  
  
Fields  
---  
`name` |  `string` Identifier. The repository's name.  
`createTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Output only. The timestamp of when the repository was created.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`displayName` |  `string` Optional. The repository's user-friendly name.  
`gitRemoteSettings` |  `object (`[GitRemoteSettings](https://docs.cloud.google.com/dataform/reference/rest/v1beta1/projects.locations.repositories#GitRemoteSettings)`)` Optional. If set, configures this repository to be linked to a Git remote.  
`npmrcEnvironmentVariablesSecretVersion` |  `string` Optional. The name of the Secret Manager secret version to be used to interpolate variables into the .npmrc file for package installation operations. Must be in the format `projects/*/secrets/*/versions/*`. The file itself must be in a JSON format.  
`workspaceCompilationOverrides` |  `object (`[WorkspaceCompilationOverrides](https://docs.cloud.google.com/dataform/reference/rest/v1beta1/projects.locations.repositories#WorkspaceCompilationOverrides)`)` Optional. If set, fields of `workspaceCompilationOverrides` override the default compilation settings that are specified in dataform.json when creating workspace-scoped compilation results. See documentation for `WorkspaceCompilationOverrides` for more information.  
`labels` |  `map (key: string, value: string)` Optional. Repository user labels.An object containing a list of `"key": value` pairs. Example: `{ "name": "wrench", "mass": "1.3kg", "count": "3" }`.  
`setAuthenticatedUserAdmin` |  `boolean` Optional. Input only. If set to true, the authenticated user will be granted the roles/dataform.admin role on the created repository. To modify access to the created repository later apply setIamPolicy from <https://cloud.google.com/dataform/reference/rest#rest-resource:-v1beta1.projects.locations.repositories>  
`serviceAccount` |  `string` Optional. The service account to run workflow invocations under.  
`kmsKeyName` |  `string` Optional. The reference to a KMS encryption key. If provided, it will be used to encrypt user data in the repository and all child resources. It is not possible to add or update the encryption key after the repository is created. Example: `projects/{kms_project}/locations/{location}/keyRings/{key_location}/cryptoKeys/{key}`  
`dataEncryptionState` |  `object (`[DataEncryptionState](https://docs.cloud.google.com/dataform/reference/rest/v1beta1/DataEncryptionState)`)` Output only. A data encryption state of a Git repository if this Repository is protected by a KMS key.  
`endUserAuthConfig` |  `object (`[EndUserAuthConfig](https://docs.cloud.google.com/dataform/reference/rest/v1beta1/projects.locations.repositories#EndUserAuthConfig)`)` Optional. Includes configuration options for end user authentication.  
`containingFolder` |  `string` Optional. The name of the containing folder of the repository. The field is immutable and it can be modified via a repositories.move operation. Format: `projects/*/locations/*/folders/*`. or `projects/*/locations/*/teamFolders/*`.  
`teamFolderName` |  `string` Output only. The resource name of the TeamFolder that this Repository is associated with. This should take the format: projects/{project}/locations/{location}/teamFolders/{teamFolder}. If this is not set, the Repository is not associated with a TeamFolder.  
`strictActAsChecks` |  `boolean` Optional. If set to True, any user modification that could lead to code execution within a workflow configuration requires the user to have "act-as" permission on the effective service account. See <https://cloud.google.com/dataform/docs/strict-act-as-mode>  
`internalMetadata` |  `string` Output only. All the metadata information that is used internally to serve the resource. For example: timestamps, flags, status fields, etc. The format of this field is a JSON string.  
  
## GitRemoteSettings

Controls Git remote configuration for a repository.

JSON representation  
---  
      
    
    {
      "url": string,
      "defaultBranch": string,
      "effectiveDefaultBranch": string,
      "authenticationTokenSecretVersion": string,
      "sshAuthenticationConfig": {
        object ([SshAuthenticationConfig](https://docs.cloud.google.com/dataform/reference/rest/v1beta1/projects.locations.repositories#SshAuthenticationConfig))
      },
      "tokenStatus": enum ([TokenStatus](https://docs.cloud.google.com/dataform/reference/rest/v1beta1/projects.locations.repositories#TokenStatus)),
      "gitRepositoryLink": string
    }  
  
Fields  
---  
`url` |  `string` Required. The Git remote's URL.  
`defaultBranch` |  `string` Optional. The Git remote's default branch name. If not set, `main` will be used.  
`effectiveDefaultBranch` |  `string` Output only. The Git remote's effective default branch name. This is the default branch name of the Git remote if it is set, otherwise it is `main`.  
`authenticationTokenSecretVersion` |  `string` Optional. The name of the Secret Manager secret version to use as an authentication token for Git operations. Must be in the format `projects/*/secrets/*/versions/*`.  
`sshAuthenticationConfig` |  `object (`[SshAuthenticationConfig](https://docs.cloud.google.com/dataform/reference/rest/v1beta1/projects.locations.repositories#SshAuthenticationConfig)`)` Optional. Authentication fields for remote uris using SSH protocol.  
`tokenStatus  
**(deprecated)**` |  `enum (`[TokenStatus](https://docs.cloud.google.com/dataform/reference/rest/v1beta1/projects.locations.repositories#TokenStatus)`)` This item is deprecated!Output only. Deprecated: The field does not contain any token status information. Instead use <https://cloud.google.com/dataform/reference/rest/v1beta1/projects.locations.repositories/computeAccessTokenStatus>  
`gitRepositoryLink` |  `string` Optional. Resource name for the `GitRepositoryLink` used for machine credentials. Must be in the format `projects/*/locations/*/connections/*/gitRepositoryLinks/*`  
  
## SshAuthenticationConfig

Configures fields for performing SSH authentication.

JSON representation  
---  
      
    
    {
      "userPrivateKeySecretVersion": string,
      "hostPublicKey": string
    }  
  
Fields  
---  
`userPrivateKeySecretVersion` |  `string` Required. The name of the Secret Manager secret version to use as a ssh private key for Git operations. Must be in the format `projects/*/secrets/*/versions/*`.  
`hostPublicKey` |  `string` Required. Content of a public SSH key to verify an identity of a remote Git host.  
  
## TokenStatus

The status of the authentication token.

Enums  
---  
`TOKEN_STATUS_UNSPECIFIED` | Default value. This value is unused.  
`NOT_FOUND` | The token could not be found in Secret Manager (or the Dataform Service Account did not have permission to access it).  
`INVALID` | The token could not be used to authenticate against the Git remote.  
`VALID` | The token was used successfully to authenticate against the Git remote.  
  
## WorkspaceCompilationOverrides

Configures workspace compilation overrides for a repository. Primarily used by the UI (`console.cloud.google.com`). `schemaSuffix` and `tablePrefix` can have a special expression - `${workspaceName}`, which refers to the workspace name from which the compilation results will be created. API callers are expected to resolve the expression in these overrides and provide them explicitly in `codeCompilationConfig` (<https://cloud.google.com/dataform/reference/rest/v1beta1/projects.locations.repositories.compilationResults#codecompilationconfig>) when creating workspace-scoped compilation results.

JSON representation  
---  
      
    
    {
      "defaultDatabase": string,
      "schemaSuffix": string,
      "tablePrefix": string
    }  
  
Fields  
---  
`defaultDatabase` |  `string` Optional. The default database (Google Cloud project ID).  
`schemaSuffix` |  `string` Optional. The suffix that should be appended to all schema (BigQuery dataset ID) names.  
`tablePrefix` |  `string` Optional. The prefix that should be prepended to all table names.  
  
## EndUserAuthConfig

Includes configuration options for repository end user authentication.

JSON representation  
---  
      
    
    {
      "oauthConfig": {
        object ([OAuthConfig](https://docs.cloud.google.com/dataform/reference/rest/v1beta1/OAuthConfig))
      }
    }  
  
Fields  
---  
`oauthConfig` |  `object (`[OAuthConfig](https://docs.cloud.google.com/dataform/reference/rest/v1beta1/OAuthConfig)`)` Optional. OAuth configuration for repository end user authentication.  
  
## Methods  
  
---  
  
### `[commit](https://docs.cloud.google.com/dataform/reference/rest/v1beta1/projects.locations.repositories/commit)`

|  Applies a Git commit to a Repository.  
  
### `[computeAccessTokenStatus](https://docs.cloud.google.com/dataform/reference/rest/v1beta1/projects.locations.repositories/computeAccessTokenStatus)`

|  Computes a Repository's Git access token status.  
  
### `[create](https://docs.cloud.google.com/dataform/reference/rest/v1beta1/projects.locations.repositories/create)`

|  Creates a new Repository in a given project and location.  
  
### `[delete](https://docs.cloud.google.com/dataform/reference/rest/v1beta1/projects.locations.repositories/delete)`

|  Deletes a single Repository.  
  
### `[deleteLongRunning](https://docs.cloud.google.com/dataform/reference/rest/v1beta1/projects.locations.repositories/deleteLongRunning)`

|  Deletes a single repository asynchronously.  
  
### `[fetchHistory](https://docs.cloud.google.com/dataform/reference/rest/v1beta1/projects.locations.repositories/fetchHistory)`

|  Fetches a Repository's history of commits.  
  
### `[fetchRemoteBranches](https://docs.cloud.google.com/dataform/reference/rest/v1beta1/projects.locations.repositories/fetchRemoteBranches)`

|  Fetches a Repository's remote branches.  
  
### `[get](https://docs.cloud.google.com/dataform/reference/rest/v1beta1/projects.locations.repositories/get)`

|  Fetches a single Repository.  
  
### `[getIamPolicy](https://docs.cloud.google.com/dataform/reference/rest/v1beta1/projects.locations.repositories/getIamPolicy)`

|  Gets the access control policy for a resource.  
  
### `[list](https://docs.cloud.google.com/dataform/reference/rest/v1beta1/projects.locations.repositories/list)`

|  Lists Repositories in a given project and location.  
  
### `[move](https://docs.cloud.google.com/dataform/reference/rest/v1beta1/projects.locations.repositories/move)`

|  Moves a Repository to a new location.  
  
### `[patch](https://docs.cloud.google.com/dataform/reference/rest/v1beta1/projects.locations.repositories/patch)`

|  Updates a single Repository.  
  
### `[queryDirectoryContents](https://docs.cloud.google.com/dataform/reference/rest/v1beta1/projects.locations.repositories/queryDirectoryContents)`

|  Returns the contents of a given Repository directory.  
  
### `[readFile](https://docs.cloud.google.com/dataform/reference/rest/v1beta1/projects.locations.repositories/readFile)`

|  Returns the contents of a file (inside a Repository).  
  
### `[setIamPolicy](https://docs.cloud.google.com/dataform/reference/rest/v1beta1/projects.locations.repositories/setIamPolicy)`

|  Sets the access control policy on the specified resource.  
  
### `[testIamPermissions](https://docs.cloud.google.com/dataform/reference/rest/v1beta1/projects.locations.repositories/testIamPermissions)`

|  Returns permissions that a caller has on the specified resource.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-09-25 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-09-25 UTC."],[],[]] 
