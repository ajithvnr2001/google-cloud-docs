---
url: https://docs.cloud.google.com/dataform/reference/rest/
title: Dataform API \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T00:41:59.051931+00:00
---

# Dataform API  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dataform/reference/rest/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Dataform ](https://docs.cloud.google.com/dataform)
  * [ Reference ](https://docs.cloud.google.com/dataform/docs/authentication)



Send feedback 

#  Dataform API Stay organized with collections  Save and categorize content based on your preferences. 

Service to develop, version control, and operationalize SQL pipelines in BigQuery.

  * REST Resource: v1.projects.locations
  * REST Resource: v1.projects.locations.folders
  * REST Resource: v1.projects.locations.operations
  * REST Resource: v1.projects.locations.repositories
  * REST Resource: v1.projects.locations.repositories.compilationResults
  * REST Resource: v1.projects.locations.repositories.releaseConfigs
  * REST Resource: v1.projects.locations.repositories.workflowConfigs
  * REST Resource: v1.projects.locations.repositories.workflowInvocations
  * REST Resource: v1.projects.locations.repositories.workspaces
  * REST Resource: v1.projects.locations.teamFolders
  * REST Resource: v1beta1.projects.locations
  * REST Resource: v1beta1.projects.locations.folders
  * REST Resource: v1beta1.projects.locations.operations
  * REST Resource: v1beta1.projects.locations.repositories
  * REST Resource: v1beta1.projects.locations.repositories.compilationResults
  * REST Resource: v1beta1.projects.locations.repositories.releaseConfigs
  * REST Resource: v1beta1.projects.locations.repositories.workflowConfigs
  * REST Resource: v1beta1.projects.locations.repositories.workflowInvocations
  * REST Resource: v1beta1.projects.locations.repositories.workspaces
  * REST Resource: v1beta1.projects.locations.teamFolders



## Service: dataform.googleapis.com

To call this service, we recommend that you use the Google-provided [client libraries](https://cloud.google.com/apis/docs/client-libraries-explained). If your application needs to use your own libraries to call this service, use the following information when you make the API requests.

### Discovery document

A [Discovery Document](https://developers.google.com/discovery/v1/reference/apis) is a machine-readable specification for describing and consuming REST APIs. It is used to build client libraries, IDE plugins, and other tools that interact with Google APIs. One service may provide multiple discovery documents. This service provides the following discovery documents:

  * <https://dataform.googleapis.com/$discovery/rest?version=v1>
  * <https://dataform.googleapis.com/$discovery/rest?version=v1beta1>



### Service endpoint

A [service endpoint](https://cloud.google.com/apis/design/glossary#api_service_endpoint) is a base URL that specifies the network address of an API service. One service might have multiple service endpoints. This service has the following service endpoint and all URIs below are relative to this service endpoint:

  * `https://dataform.googleapis.com`



### Regional service endpoint

A regional service endpoint is a base URL that specifies the network address of an API service in a single region. A service that is available in multiple regions might have multiple regional endpoints. Select a location to see its regional service endpoint for this service. 

global africa-south1 asia-east1 asia-east2 asia-northeast1 asia-northeast2 asia-northeast3 asia-south1 asia-south2 asia-southeast1 asia-southeast2 australia-southeast1 australia-southeast2 europe-central2 europe-north1 europe-southwest1 europe-west1 europe-west10 europe-west12 europe-west2 europe-west3 europe-west4 europe-west6 europe-west8 europe-west9 me-central1 me-central2 me-west1 northamerica-northeast1 northamerica-northeast2 southamerica-east1 southamerica-west1 us-central1 us-east1 us-east4 us-east5 us-south1 us-west1 us-west2 us-west3 us-west4

  

* `https://dataform.googleapis.com`

## REST Resource: [v1.projects.locations](https://docs.cloud.google.com/dataform/reference/rest/v1/projects.locations)

Methods  
---  
`[get](https://docs.cloud.google.com/dataform/reference/rest/v1/projects.locations/get)` |  `GET /v1/{name=projects/*/locations/*}`   
Gets information about a location.  
`[getConfig](https://docs.cloud.google.com/dataform/reference/rest/v1/projects.locations/getConfig)` |  `GET /v1/{name=projects/*/locations/*/config}`   
Get default config for a given project and location.  
`[list](https://docs.cloud.google.com/dataform/reference/rest/v1/projects.locations/list)` |  `GET /v1/{name=projects/*}/locations`   
Lists information about the supported locations for this service.  
`[queryUserRootContents](https://docs.cloud.google.com/dataform/reference/rest/v1/projects.locations/queryUserRootContents)` |  `GET /v1/{location=projects/*/locations/*}:queryUserRootContents`   
Returns the contents of a caller's root folder in a given location.  
`[updateConfig](https://docs.cloud.google.com/dataform/reference/rest/v1/projects.locations/updateConfig)` |  `PATCH /v1/{config.name=projects/*/locations/*/config}`   
Update default config for a given project and location.  
  
## REST Resource: [v1.projects.locations.folders](https://docs.cloud.google.com/dataform/reference/rest/v1/projects.locations.folders)

Methods  
---  
`[create](https://docs.cloud.google.com/dataform/reference/rest/v1/projects.locations.folders/create)` |  `POST /v1/{parent=projects/*/locations/*}/folders`   
Creates a new Folder in a given project and location.  
`[delete](https://docs.cloud.google.com/dataform/reference/rest/v1/projects.locations.folders/delete)` |  `DELETE /v1/{name=projects/*/locations/*/folders/*}`   
Deletes a single Folder.  
`[deleteTree](https://docs.cloud.google.com/dataform/reference/rest/v1/projects.locations.folders/deleteTree)` |  `POST /v1/{name=projects/*/locations/*/folders/*}:deleteTree`   
Deletes a Folder with its contents (Folders, Repositories, Workspaces, ReleaseConfigs, and WorkflowConfigs).  
`[get](https://docs.cloud.google.com/dataform/reference/rest/v1/projects.locations.folders/get)` |  `GET /v1/{name=projects/*/locations/*/folders/*}`   
Fetches a single Folder.  
`[getIamPolicy](https://docs.cloud.google.com/dataform/reference/rest/v1/projects.locations.folders/getIamPolicy)` |  `GET /v1/{resource=projects/*/locations/*/folders/*}:getIamPolicy`   
Gets the access control policy for a resource.  
`[move](https://docs.cloud.google.com/dataform/reference/rest/v1/projects.locations.folders/move)` |  `POST /v1/{name=projects/*/locations/*/folders/*}:move`   
Moves a Folder to a new Folder, TeamFolder, or the root location.  
`[patch](https://docs.cloud.google.com/dataform/reference/rest/v1/projects.locations.folders/patch)` |  `PATCH /v1/{folder.name=projects/*/locations/*/folders/*}`   
Updates a single Folder.  
`[queryFolderContents](https://docs.cloud.google.com/dataform/reference/rest/v1/projects.locations.folders/queryFolderContents)` |  `GET /v1/{folder=projects/*/locations/*/folders/*}:queryFolderContents`   
Returns the contents of a given Folder.  
`[setIamPolicy](https://docs.cloud.google.com/dataform/reference/rest/v1/projects.locations.folders/setIamPolicy)` |  `POST /v1/{resource=projects/*/locations/*/folders/*}:setIamPolicy`   
Sets the access control policy on the specified resource.  
`[testIamPermissions](https://docs.cloud.google.com/dataform/reference/rest/v1/projects.locations.folders/testIamPermissions)` |  `POST /v1/{resource=projects/*/locations/*/folders/*}:testIamPermissions`   
Returns permissions that a caller has on the specified resource.  
  
## REST Resource: [v1.projects.locations.operations](https://docs.cloud.google.com/dataform/reference/rest/v1/projects.locations.operations)

Methods  
---  
`[cancel](https://docs.cloud.google.com/dataform/reference/rest/v1/projects.locations.operations/cancel)` |  `POST /v1/{name=projects/*/locations/*/operations/*}:cancel`   
Starts asynchronous cancellation on a long-running operation.  
`[delete](https://docs.cloud.google.com/dataform/reference/rest/v1/projects.locations.operations/delete)` |  `DELETE /v1/{name=projects/*/locations/*/operations/*}`   
Deletes a long-running operation.  
`[get](https://docs.cloud.google.com/dataform/reference/rest/v1/projects.locations.operations/get)` |  `GET /v1/{name=projects/*/locations/*/operations/*}`   
Gets the latest state of a long-running operation.  
`[list](https://docs.cloud.google.com/dataform/reference/rest/v1/projects.locations.operations/list)` |  `GET /v1/{name=projects/*/locations/*}/operations`   
Lists operations that match the specified filter in the request.  
  
## REST Resource: [v1.projects.locations.repositories](https://docs.cloud.google.com/dataform/reference/rest/v1/projects.locations.repositories)

Methods  
---  
`[commit](https://docs.cloud.google.com/dataform/reference/rest/v1/projects.locations.repositories/commit)` |  `POST /v1/{name=projects/*/locations/*/repositories/*}:commit`   
Applies a Git commit to a Repository.  
`[computeAccessTokenStatus](https://docs.cloud.google.com/dataform/reference/rest/v1/projects.locations.repositories/computeAccessTokenStatus)` |  `GET /v1/{name=projects/*/locations/*/repositories/*}:computeAccessTokenStatus`   
Computes a Repository's Git access token status.  
`[create](https://docs.cloud.google.com/dataform/reference/rest/v1/projects.locations.repositories/create)` |  `POST /v1/{parent=projects/*/locations/*}/repositories`   
Creates a new Repository in a given project and location.  
`[delete](https://docs.cloud.google.com/dataform/reference/rest/v1/projects.locations.repositories/delete)` |  `DELETE /v1/{name=projects/*/locations/*/repositories/*}`   
Deletes a single Repository.  
`[fetchHistory](https://docs.cloud.google.com/dataform/reference/rest/v1/projects.locations.repositories/fetchHistory)` |  `GET /v1/{name=projects/*/locations/*/repositories/*}:fetchHistory`   
Fetches a Repository's history of commits.  
`[fetchRemoteBranches](https://docs.cloud.google.com/dataform/reference/rest/v1/projects.locations.repositories/fetchRemoteBranches)` |  `GET /v1/{name=projects/*/locations/*/repositories/*}:fetchRemoteBranches`   
Fetches a Repository's remote branches.  
`[get](https://docs.cloud.google.com/dataform/reference/rest/v1/projects.locations.repositories/get)` |  `GET /v1/{name=projects/*/locations/*/repositories/*}`   
Fetches a single Repository.  
`[getIamPolicy](https://docs.cloud.google.com/dataform/reference/rest/v1/projects.locations.repositories/getIamPolicy)` |  `GET /v1/{resource=projects/*/locations/*/repositories/*}:getIamPolicy`   
Gets the access control policy for a resource.  
`[list](https://docs.cloud.google.com/dataform/reference/rest/v1/projects.locations.repositories/list)` |  `GET /v1/{parent=projects/*/locations/*}/repositories`   
Lists Repositories in a given project and location.  
`[move](https://docs.cloud.google.com/dataform/reference/rest/v1/projects.locations.repositories/move)` |  `POST /v1/{name=projects/*/locations/*/repositories/*}:move`   
Moves a Repository to a new location.  
`[patch](https://docs.cloud.google.com/dataform/reference/rest/v1/projects.locations.repositories/patch)` |  `PATCH /v1/{repository.name=projects/*/locations/*/repositories/*}`   
Updates a single Repository.  
`[queryDirectoryContents](https://docs.cloud.google.com/dataform/reference/rest/v1/projects.locations.repositories/queryDirectoryContents)` |  `GET /v1/{name=projects/*/locations/*/repositories/*}:queryDirectoryContents`   
Returns the contents of a given Repository directory.  
`[readFile](https://docs.cloud.google.com/dataform/reference/rest/v1/projects.locations.repositories/readFile)` |  `GET /v1/{name=projects/*/locations/*/repositories/*}:readFile`   
Returns the contents of a file (inside a Repository).  
`[setIamPolicy](https://docs.cloud.google.com/dataform/reference/rest/v1/projects.locations.repositories/setIamPolicy)` |  `POST /v1/{resource=projects/*/locations/*/repositories/*}:setIamPolicy`   
Sets the access control policy on the specified resource.  
`[testIamPermissions](https://docs.cloud.google.com/dataform/reference/rest/v1/projects.locations.repositories/testIamPermissions)` |  `POST /v1/{resource=projects/*/locations/*/repositories/*}:testIamPermissions`   
Returns permissions that a caller has on the specified resource.  
  
## REST Resource: [v1.projects.locations.repositories.compilationResults](https://docs.cloud.google.com/dataform/reference/rest/v1/projects.locations.repositories.compilationResults)

Methods  
---  
`[create](https://docs.cloud.google.com/dataform/reference/rest/v1/projects.locations.repositories.compilationResults/create)` |  `POST /v1/{parent=projects/*/locations/*/repositories/*}/compilationResults`   
Creates a new CompilationResult in a given project and location.  
`[get](https://docs.cloud.google.com/dataform/reference/rest/v1/projects.locations.repositories.compilationResults/get)` |  `GET /v1/{name=projects/*/locations/*/repositories/*/compilationResults/*}`   
Fetches a single CompilationResult.  
`[list](https://docs.cloud.google.com/dataform/reference/rest/v1/projects.locations.repositories.compilationResults/list)` |  `GET /v1/{parent=projects/*/locations/*/repositories/*}/compilationResults`   
Lists CompilationResults in a given Repository.  
`[query](https://docs.cloud.google.com/dataform/reference/rest/v1/projects.locations.repositories.compilationResults/query)` |  `GET /v1/{name=projects/*/locations/*/repositories/*/compilationResults/*}:query`   
Returns CompilationResultActions in a given CompilationResult.  
  
## REST Resource: [v1.projects.locations.repositories.releaseConfigs](https://docs.cloud.google.com/dataform/reference/rest/v1/projects.locations.repositories.releaseConfigs)

Methods  
---  
`[create](https://docs.cloud.google.com/dataform/reference/rest/v1/projects.locations.repositories.releaseConfigs/create)` |  `POST /v1/{parent=projects/*/locations/*/repositories/*}/releaseConfigs`   
Creates a new ReleaseConfig in a given Repository.  
`[delete](https://docs.cloud.google.com/dataform/reference/rest/v1/projects.locations.repositories.releaseConfigs/delete)` |  `DELETE /v1/{name=projects/*/locations/*/repositories/*/releaseConfigs/*}`   
Deletes a single ReleaseConfig.  
`[get](https://docs.cloud.google.com/dataform/reference/rest/v1/projects.locations.repositories.releaseConfigs/get)` |  `GET /v1/{name=projects/*/locations/*/repositories/*/releaseConfigs/*}`   
Fetches a single ReleaseConfig.  
`[list](https://docs.cloud.google.com/dataform/reference/rest/v1/projects.locations.repositories.releaseConfigs/list)` |  `GET /v1/{parent=projects/*/locations/*/repositories/*}/releaseConfigs`   
Lists ReleaseConfigs in a given Repository.  
`[patch](https://docs.cloud.google.com/dataform/reference/rest/v1/projects.locations.repositories.releaseConfigs/patch)` |  `PATCH /v1/{releaseConfig.name=projects/*/locations/*/repositories/*/releaseConfigs/*}`   
Updates a single ReleaseConfig.  
  
## REST Resource: [v1.projects.locations.repositories.workflowConfigs](https://docs.cloud.google.com/dataform/reference/rest/v1/projects.locations.repositories.workflowConfigs)

Methods  
---  
`[create](https://docs.cloud.google.com/dataform/reference/rest/v1/projects.locations.repositories.workflowConfigs/create)` |  `POST /v1/{parent=projects/*/locations/*/repositories/*}/workflowConfigs`   
Creates a new WorkflowConfig in a given Repository.  
`[delete](https://docs.cloud.google.com/dataform/reference/rest/v1/projects.locations.repositories.workflowConfigs/delete)` |  `DELETE /v1/{name=projects/*/locations/*/repositories/*/workflowConfigs/*}`   
Deletes a single WorkflowConfig.  
`[get](https://docs.cloud.google.com/dataform/reference/rest/v1/projects.locations.repositories.workflowConfigs/get)` |  `GET /v1/{name=projects/*/locations/*/repositories/*/workflowConfigs/*}`   
Fetches a single WorkflowConfig.  
`[list](https://docs.cloud.google.com/dataform/reference/rest/v1/projects.locations.repositories.workflowConfigs/list)` |  `GET /v1/{parent=projects/*/locations/*/repositories/*}/workflowConfigs`   
Lists WorkflowConfigs in a given Repository.  
`[patch](https://docs.cloud.google.com/dataform/reference/rest/v1/projects.locations.repositories.workflowConfigs/patch)` |  `PATCH /v1/{workflowConfig.name=projects/*/locations/*/repositories/*/workflowConfigs/*}`   
Updates a single WorkflowConfig.  
  
## REST Resource: [v1.projects.locations.repositories.workflowInvocations](https://docs.cloud.google.com/dataform/reference/rest/v1/projects.locations.repositories.workflowInvocations)

Methods  
---  
`[cancel](https://docs.cloud.google.com/dataform/reference/rest/v1/projects.locations.repositories.workflowInvocations/cancel)` |  `POST /v1/{name=projects/*/locations/*/repositories/*/workflowInvocations/*}:cancel`   
Requests cancellation of a running WorkflowInvocation.  
`[create](https://docs.cloud.google.com/dataform/reference/rest/v1/projects.locations.repositories.workflowInvocations/create)` |  `POST /v1/{parent=projects/*/locations/*/repositories/*}/workflowInvocations`   
Creates a new WorkflowInvocation in a given Repository.  
`[delete](https://docs.cloud.google.com/dataform/reference/rest/v1/projects.locations.repositories.workflowInvocations/delete)` |  `DELETE /v1/{name=projects/*/locations/*/repositories/*/workflowInvocations/*}`   
Deletes a single WorkflowInvocation.  
`[get](https://docs.cloud.google.com/dataform/reference/rest/v1/projects.locations.repositories.workflowInvocations/get)` |  `GET /v1/{name=projects/*/locations/*/repositories/*/workflowInvocations/*}`   
Fetches a single WorkflowInvocation.  
`[list](https://docs.cloud.google.com/dataform/reference/rest/v1/projects.locations.repositories.workflowInvocations/list)` |  `GET /v1/{parent=projects/*/locations/*/repositories/*}/workflowInvocations`   
Lists WorkflowInvocations in a given Repository.  
`[query](https://docs.cloud.google.com/dataform/reference/rest/v1/projects.locations.repositories.workflowInvocations/query)` |  `GET /v1/{name=projects/*/locations/*/repositories/*/workflowInvocations/*}:query`   
Returns WorkflowInvocationActions in a given WorkflowInvocation.  
  
## REST Resource: [v1.projects.locations.repositories.workspaces](https://docs.cloud.google.com/dataform/reference/rest/v1/projects.locations.repositories.workspaces)

Methods  
---  
`[commit](https://docs.cloud.google.com/dataform/reference/rest/v1/projects.locations.repositories.workspaces/commit)` |  `POST /v1/{name=projects/*/locations/*/repositories/*/workspaces/*}:commit`   
Applies a Git commit for uncommitted files in a Workspace.  
`[create](https://docs.cloud.google.com/dataform/reference/rest/v1/projects.locations.repositories.workspaces/create)` |  `POST /v1/{parent=projects/*/locations/*/repositories/*}/workspaces`   
Creates a new Workspace in a given Repository.  
`[delete](https://docs.cloud.google.com/dataform/reference/rest/v1/projects.locations.repositories.workspaces/delete)` |  `DELETE /v1/{name=projects/*/locations/*/repositories/*/workspaces/*}`   
Deletes a single Workspace.  
`[fetchFileDiff](https://docs.cloud.google.com/dataform/reference/rest/v1/projects.locations.repositories.workspaces/fetchFileDiff)` |  `GET /v1/{workspace=projects/*/locations/*/repositories/*/workspaces/*}:fetchFileDiff`   
Fetches Git diff for an uncommitted file in a Workspace.  
`[fetchFileGitStatuses](https://docs.cloud.google.com/dataform/reference/rest/v1/projects.locations.repositories.workspaces/fetchFileGitStatuses)` |  `GET /v1/{name=projects/*/locations/*/repositories/*/workspaces/*}:fetchFileGitStatuses`   
Fetches Git statuses for the files in a Workspace.  
`[fetchGitAheadBehind](https://docs.cloud.google.com/dataform/reference/rest/v1/projects.locations.repositories.workspaces/fetchGitAheadBehind)` |  `GET /v1/{name=projects/*/locations/*/repositories/*/workspaces/*}:fetchGitAheadBehind`   
Fetches Git ahead/behind against a remote branch.  
`[get](https://docs.cloud.google.com/dataform/reference/rest/v1/projects.locations.repositories.workspaces/get)` |  `GET /v1/{name=projects/*/locations/*/repositories/*/workspaces/*}`   
Fetches a single Workspace.  
`[getIamPolicy](https://docs.cloud.google.com/dataform/reference/rest/v1/projects.locations.repositories.workspaces/getIamPolicy)` |  `GET /v1/{resource=projects/*/locations/*/repositories/*/workspaces/*}:getIamPolicy`   
Gets the access control policy for a resource.  
`[installNpmPackages](https://docs.cloud.google.com/dataform/reference/rest/v1/projects.locations.repositories.workspaces/installNpmPackages)` |  `POST /v1/{workspace=projects/*/locations/*/repositories/*/workspaces/*}:installNpmPackages`   
Installs dependency NPM packages (inside a Workspace).  
`[list](https://docs.cloud.google.com/dataform/reference/rest/v1/projects.locations.repositories.workspaces/list)` |  `GET /v1/{parent=projects/*/locations/*/repositories/*}/workspaces`   
Lists Workspaces in a given Repository.  
`[makeDirectory](https://docs.cloud.google.com/dataform/reference/rest/v1/projects.locations.repositories.workspaces/makeDirectory)` |  `POST /v1/{workspace=projects/*/locations/*/repositories/*/workspaces/*}:makeDirectory`   
Creates a directory inside a Workspace.  
`[moveDirectory](https://docs.cloud.google.com/dataform/reference/rest/v1/projects.locations.repositories.workspaces/moveDirectory)` |  `POST /v1/{workspace=projects/*/locations/*/repositories/*/workspaces/*}:moveDirectory`   
Moves a directory (inside a Workspace), and all of its contents, to a new location.  
`[moveFile](https://docs.cloud.google.com/dataform/reference/rest/v1/projects.locations.repositories.workspaces/moveFile)` |  `POST /v1/{workspace=projects/*/locations/*/repositories/*/workspaces/*}:moveFile`   
Moves a file (inside a Workspace) to a new location.  
`[pull](https://docs.cloud.google.com/dataform/reference/rest/v1/projects.locations.repositories.workspaces/pull)` |  `POST /v1/{name=projects/*/locations/*/repositories/*/workspaces/*}:pull`   
Pulls Git commits from the Repository's remote into a Workspace.  
`[push](https://docs.cloud.google.com/dataform/reference/rest/v1/projects.locations.repositories.workspaces/push)` |  `POST /v1/{name=projects/*/locations/*/repositories/*/workspaces/*}:push`   
Pushes Git commits from a Workspace to the Repository's remote.  
`[queryDirectoryContents](https://docs.cloud.google.com/dataform/reference/rest/v1/projects.locations.repositories.workspaces/queryDirectoryContents)` |  `GET /v1/{workspace=projects/*/locations/*/repositories/*/workspaces/*}:queryDirectoryContents`   
Returns the contents of a given Workspace directory.  
`[readFile](https://docs.cloud.google.com/dataform/reference/rest/v1/projects.locations.repositories.workspaces/readFile)` |  `GET /v1/{workspace=projects/*/locations/*/repositories/*/workspaces/*}:readFile`   
Returns the contents of a file (inside a Workspace).  
`[removeDirectory](https://docs.cloud.google.com/dataform/reference/rest/v1/projects.locations.repositories.workspaces/removeDirectory)` |  `POST /v1/{workspace=projects/*/locations/*/repositories/*/workspaces/*}:removeDirectory`   
Deletes a directory (inside a Workspace) and all of its contents.  
`[removeFile](https://docs.cloud.google.com/dataform/reference/rest/v1/projects.locations.repositories.workspaces/removeFile)` |  `POST /v1/{workspace=projects/*/locations/*/repositories/*/workspaces/*}:removeFile`   
Deletes a file (inside a Workspace).  
`[reset](https://docs.cloud.google.com/dataform/reference/rest/v1/projects.locations.repositories.workspaces/reset)` |  `POST /v1/{name=projects/*/locations/*/repositories/*/workspaces/*}:reset`   
Performs a Git reset for uncommitted files in a Workspace.  
`[searchFiles](https://docs.cloud.google.com/dataform/reference/rest/v1/projects.locations.repositories.workspaces/searchFiles)` |  `GET /v1/{workspace=projects/*/locations/*/repositories/*/workspaces/*}:searchFiles`   
Finds the contents of a given Workspace directory by filter.  
`[setIamPolicy](https://docs.cloud.google.com/dataform/reference/rest/v1/projects.locations.repositories.workspaces/setIamPolicy)` |  `POST /v1/{resource=projects/*/locations/*/repositories/*/workspaces/*}:setIamPolicy`   
Sets the access control policy on the specified resource.  
`[testIamPermissions](https://docs.cloud.google.com/dataform/reference/rest/v1/projects.locations.repositories.workspaces/testIamPermissions)` |  `POST /v1/{resource=projects/*/locations/*/repositories/*/workspaces/*}:testIamPermissions`   
Returns permissions that a caller has on the specified resource.  
`[writeFile](https://docs.cloud.google.com/dataform/reference/rest/v1/projects.locations.repositories.workspaces/writeFile)` |  `POST /v1/{workspace=projects/*/locations/*/repositories/*/workspaces/*}:writeFile`   
Writes to a file (inside a Workspace).  
  
## REST Resource: [v1.projects.locations.teamFolders](https://docs.cloud.google.com/dataform/reference/rest/v1/projects.locations.teamFolders)

Methods  
---  
`[create](https://docs.cloud.google.com/dataform/reference/rest/v1/projects.locations.teamFolders/create)` |  `POST /v1/{parent=projects/*/locations/*}/teamFolders`   
Creates a new TeamFolder in a given project and location.  
`[delete](https://docs.cloud.google.com/dataform/reference/rest/v1/projects.locations.teamFolders/delete)` |  `DELETE /v1/{name=projects/*/locations/*/teamFolders/*}`   
Deletes a single TeamFolder.  
`[deleteTree](https://docs.cloud.google.com/dataform/reference/rest/v1/projects.locations.teamFolders/deleteTree)` |  `POST /v1/{name=projects/*/locations/*/teamFolders/*}:deleteTree`   
Deletes a TeamFolder with its contents (Folders, Repositories, Workspaces, ReleaseConfigs, and WorkflowConfigs).  
`[get](https://docs.cloud.google.com/dataform/reference/rest/v1/projects.locations.teamFolders/get)` |  `GET /v1/{name=projects/*/locations/*/teamFolders/*}`   
Fetches a single TeamFolder.  
`[getIamPolicy](https://docs.cloud.google.com/dataform/reference/rest/v1/projects.locations.teamFolders/getIamPolicy)` |  `GET /v1/{resource=projects/*/locations/*/teamFolders/*}:getIamPolicy`   
Gets the access control policy for a resource.  
`[patch](https://docs.cloud.google.com/dataform/reference/rest/v1/projects.locations.teamFolders/patch)` |  `PATCH /v1/{teamFolder.name=projects/*/locations/*/teamFolders/*}`   
Updates a single TeamFolder.  
`[queryContents](https://docs.cloud.google.com/dataform/reference/rest/v1/projects.locations.teamFolders/queryContents)` |  `GET /v1/{teamFolder=projects/*/locations/*/teamFolders/*}:queryContents`   
Returns the contents of a given TeamFolder.  
`[search](https://docs.cloud.google.com/dataform/reference/rest/v1/projects.locations.teamFolders/search)` |  `GET /v1/{location=projects/*/locations/*}/teamFolders:search`   
Returns all TeamFolders in a given location that the caller has access to and match the provided filter.  
`[setIamPolicy](https://docs.cloud.google.com/dataform/reference/rest/v1/projects.locations.teamFolders/setIamPolicy)` |  `POST /v1/{resource=projects/*/locations/*/teamFolders/*}:setIamPolicy`   
Sets the access control policy on the specified resource.  
`[testIamPermissions](https://docs.cloud.google.com/dataform/reference/rest/v1/projects.locations.teamFolders/testIamPermissions)` |  `POST /v1/{resource=projects/*/locations/*/teamFolders/*}:testIamPermissions`   
Returns permissions that a caller has on the specified resource.  
  
## REST Resource: [v1beta1.projects.locations](https://docs.cloud.google.com/dataform/reference/rest/v1beta1/projects.locations)

Methods  
---  
`[get](https://docs.cloud.google.com/dataform/reference/rest/v1beta1/projects.locations/get)` |  `GET /v1beta1/{name=projects/*/locations/*}`   
Gets information about a location.  
`[getConfig](https://docs.cloud.google.com/dataform/reference/rest/v1beta1/projects.locations/getConfig)` |  `GET /v1beta1/{name=projects/*/locations/*/config}`   
Get default config for a given project and location.  
`[list](https://docs.cloud.google.com/dataform/reference/rest/v1beta1/projects.locations/list)` |  `GET /v1beta1/{name=projects/*}/locations`   
Lists information about the supported locations for this service.  
`[queryUserRootContents](https://docs.cloud.google.com/dataform/reference/rest/v1beta1/projects.locations/queryUserRootContents)` |  `GET /v1beta1/{location=projects/*/locations/*}:queryUserRootContents`   
Returns the contents of a caller's root folder in a given location.  
`[updateConfig](https://docs.cloud.google.com/dataform/reference/rest/v1beta1/projects.locations/updateConfig)` |  `PATCH /v1beta1/{config.name=projects/*/locations/*/config}`   
Update default config for a given project and location.  
  
## REST Resource: [v1beta1.projects.locations.folders](https://docs.cloud.google.com/dataform/reference/rest/v1beta1/projects.locations.folders)

Methods  
---  
`[create](https://docs.cloud.google.com/dataform/reference/rest/v1beta1/projects.locations.folders/create)` |  `POST /v1beta1/{parent=projects/*/locations/*}/folders`   
Creates a new Folder in a given project and location.  
`[delete](https://docs.cloud.google.com/dataform/reference/rest/v1beta1/projects.locations.folders/delete)` |  `DELETE /v1beta1/{name=projects/*/locations/*/folders/*}`   
Deletes a single Folder.  
`[deleteTree](https://docs.cloud.google.com/dataform/reference/rest/v1beta1/projects.locations.folders/deleteTree)` |  `POST /v1beta1/{name=projects/*/locations/*/folders/*}:deleteTree`   
Deletes a Folder with its contents (Folders, Repositories, Workspaces, ReleaseConfigs, and WorkflowConfigs).  
`[get](https://docs.cloud.google.com/dataform/reference/rest/v1beta1/projects.locations.folders/get)` |  `GET /v1beta1/{name=projects/*/locations/*/folders/*}`   
Fetches a single Folder.  
`[getIamPolicy](https://docs.cloud.google.com/dataform/reference/rest/v1beta1/projects.locations.folders/getIamPolicy)` |  `GET /v1beta1/{resource=projects/*/locations/*/folders/*}:getIamPolicy`   
Gets the access control policy for a resource.  
`[move](https://docs.cloud.google.com/dataform/reference/rest/v1beta1/projects.locations.folders/move)` |  `POST /v1beta1/{name=projects/*/locations/*/folders/*}:move`   
Moves a Folder to a new Folder, TeamFolder, or the root location.  
`[patch](https://docs.cloud.google.com/dataform/reference/rest/v1beta1/projects.locations.folders/patch)` |  `PATCH /v1beta1/{folder.name=projects/*/locations/*/folders/*}`   
Updates a single Folder.  
`[queryFolderContents](https://docs.cloud.google.com/dataform/reference/rest/v1beta1/projects.locations.folders/queryFolderContents)` |  `GET /v1beta1/{folder=projects/*/locations/*/folders/*}:queryFolderContents`   
Returns the contents of a given Folder.  
`[setIamPolicy](https://docs.cloud.google.com/dataform/reference/rest/v1beta1/projects.locations.folders/setIamPolicy)` |  `POST /v1beta1/{resource=projects/*/locations/*/folders/*}:setIamPolicy`   
Sets the access control policy on the specified resource.  
`[testIamPermissions](https://docs.cloud.google.com/dataform/reference/rest/v1beta1/projects.locations.folders/testIamPermissions)` |  `POST /v1beta1/{resource=projects/*/locations/*/folders/*}:testIamPermissions`   
Returns permissions that a caller has on the specified resource.  
  
## REST Resource: [v1beta1.projects.locations.operations](https://docs.cloud.google.com/dataform/reference/rest/v1beta1/projects.locations.operations)

Methods  
---  
`[cancel](https://docs.cloud.google.com/dataform/reference/rest/v1beta1/projects.locations.operations/cancel)` |  `POST /v1beta1/{name=projects/*/locations/*/operations/*}:cancel`   
Starts asynchronous cancellation on a long-running operation.  
`[delete](https://docs.cloud.google.com/dataform/reference/rest/v1beta1/projects.locations.operations/delete)` |  `DELETE /v1beta1/{name=projects/*/locations/*/operations/*}`   
Deletes a long-running operation.  
`[get](https://docs.cloud.google.com/dataform/reference/rest/v1beta1/projects.locations.operations/get)` |  `GET /v1beta1/{name=projects/*/locations/*/operations/*}`   
Gets the latest state of a long-running operation.  
`[list](https://docs.cloud.google.com/dataform/reference/rest/v1beta1/projects.locations.operations/list)` |  `GET /v1beta1/{name=projects/*/locations/*}/operations`   
Lists operations that match the specified filter in the request.  
  
## REST Resource: [v1beta1.projects.locations.repositories](https://docs.cloud.google.com/dataform/reference/rest/v1beta1/projects.locations.repositories)

Methods  
---  
`[commit](https://docs.cloud.google.com/dataform/reference/rest/v1beta1/projects.locations.repositories/commit)` |  `POST /v1beta1/{name=projects/*/locations/*/repositories/*}:commit`   
Applies a Git commit to a Repository.  
`[computeAccessTokenStatus](https://docs.cloud.google.com/dataform/reference/rest/v1beta1/projects.locations.repositories/computeAccessTokenStatus)` |  `GET /v1beta1/{name=projects/*/locations/*/repositories/*}:computeAccessTokenStatus`   
Computes a Repository's Git access token status.  
`[create](https://docs.cloud.google.com/dataform/reference/rest/v1beta1/projects.locations.repositories/create)` |  `POST /v1beta1/{parent=projects/*/locations/*}/repositories`   
Creates a new Repository in a given project and location.  
`[delete](https://docs.cloud.google.com/dataform/reference/rest/v1beta1/projects.locations.repositories/delete)` |  `DELETE /v1beta1/{name=projects/*/locations/*/repositories/*}`   
Deletes a single Repository.  
`[deleteLongRunning](https://docs.cloud.google.com/dataform/reference/rest/v1beta1/projects.locations.repositories/deleteLongRunning)` |  `POST /v1beta1/{name=projects/*/locations/*/repositories/*}:deleteLongRunning`   
Deletes a single repository asynchronously.  
`[fetchHistory](https://docs.cloud.google.com/dataform/reference/rest/v1beta1/projects.locations.repositories/fetchHistory)` |  `GET /v1beta1/{name=projects/*/locations/*/repositories/*}:fetchHistory`   
Fetches a Repository's history of commits.  
`[fetchRemoteBranches](https://docs.cloud.google.com/dataform/reference/rest/v1beta1/projects.locations.repositories/fetchRemoteBranches)` |  `GET /v1beta1/{name=projects/*/locations/*/repositories/*}:fetchRemoteBranches`   
Fetches a Repository's remote branches.  
`[get](https://docs.cloud.google.com/dataform/reference/rest/v1beta1/projects.locations.repositories/get)` |  `GET /v1beta1/{name=projects/*/locations/*/repositories/*}`   
Fetches a single Repository.  
`[getIamPolicy](https://docs.cloud.google.com/dataform/reference/rest/v1beta1/projects.locations.repositories/getIamPolicy)` |  `GET /v1beta1/{resource=projects/*/locations/*/repositories/*}:getIamPolicy`   
Gets the access control policy for a resource.  
`[list](https://docs.cloud.google.com/dataform/reference/rest/v1beta1/projects.locations.repositories/list)` |  `GET /v1beta1/{parent=projects/*/locations/*}/repositories`   
Lists Repositories in a given project and location.  
`[move](https://docs.cloud.google.com/dataform/reference/rest/v1beta1/projects.locations.repositories/move)` |  `POST /v1beta1/{name=projects/*/locations/*/repositories/*}:move`   
Moves a Repository to a new location.  
`[patch](https://docs.cloud.google.com/dataform/reference/rest/v1beta1/projects.locations.repositories/patch)` |  `PATCH /v1beta1/{repository.name=projects/*/locations/*/repositories/*}`   
Updates a single Repository.  
`[queryDirectoryContents](https://docs.cloud.google.com/dataform/reference/rest/v1beta1/projects.locations.repositories/queryDirectoryContents)` |  `GET /v1beta1/{name=projects/*/locations/*/repositories/*}:queryDirectoryContents`   
Returns the contents of a given Repository directory.  
`[readFile](https://docs.cloud.google.com/dataform/reference/rest/v1beta1/projects.locations.repositories/readFile)` |  `GET /v1beta1/{name=projects/*/locations/*/repositories/*}:readFile`   
Returns the contents of a file (inside a Repository).  
`[setIamPolicy](https://docs.cloud.google.com/dataform/reference/rest/v1beta1/projects.locations.repositories/setIamPolicy)` |  `POST /v1beta1/{resource=projects/*/locations/*/repositories/*}:setIamPolicy`   
Sets the access control policy on the specified resource.  
`[testIamPermissions](https://docs.cloud.google.com/dataform/reference/rest/v1beta1/projects.locations.repositories/testIamPermissions)` |  `POST /v1beta1/{resource=projects/*/locations/*/repositories/*}:testIamPermissions`   
Returns permissions that a caller has on the specified resource.  
  
## REST Resource: [v1beta1.projects.locations.repositories.compilationResults](https://docs.cloud.google.com/dataform/reference/rest/v1beta1/projects.locations.repositories.compilationResults)

Methods  
---  
`[create](https://docs.cloud.google.com/dataform/reference/rest/v1beta1/projects.locations.repositories.compilationResults/create)` |  `POST /v1beta1/{parent=projects/*/locations/*/repositories/*}/compilationResults`   
Creates a new CompilationResult in a given project and location.  
`[get](https://docs.cloud.google.com/dataform/reference/rest/v1beta1/projects.locations.repositories.compilationResults/get)` |  `GET /v1beta1/{name=projects/*/locations/*/repositories/*/compilationResults/*}`   
Fetches a single CompilationResult.  
`[list](https://docs.cloud.google.com/dataform/reference/rest/v1beta1/projects.locations.repositories.compilationResults/list)` |  `GET /v1beta1/{parent=projects/*/locations/*/repositories/*}/compilationResults`   
Lists CompilationResults in a given Repository.  
`[query](https://docs.cloud.google.com/dataform/reference/rest/v1beta1/projects.locations.repositories.compilationResults/query)` |  `GET /v1beta1/{name=projects/*/locations/*/repositories/*/compilationResults/*}:query`   
Returns CompilationResultActions in a given CompilationResult.  
  
## REST Resource: [v1beta1.projects.locations.repositories.releaseConfigs](https://docs.cloud.google.com/dataform/reference/rest/v1beta1/projects.locations.repositories.releaseConfigs)

Methods  
---  
`[create](https://docs.cloud.google.com/dataform/reference/rest/v1beta1/projects.locations.repositories.releaseConfigs/create)` |  `POST /v1beta1/{parent=projects/*/locations/*/repositories/*}/releaseConfigs`   
Creates a new ReleaseConfig in a given Repository.  
`[delete](https://docs.cloud.google.com/dataform/reference/rest/v1beta1/projects.locations.repositories.releaseConfigs/delete)` |  `DELETE /v1beta1/{name=projects/*/locations/*/repositories/*/releaseConfigs/*}`   
Deletes a single ReleaseConfig.  
`[get](https://docs.cloud.google.com/dataform/reference/rest/v1beta1/projects.locations.repositories.releaseConfigs/get)` |  `GET /v1beta1/{name=projects/*/locations/*/repositories/*/releaseConfigs/*}`   
Fetches a single ReleaseConfig.  
`[list](https://docs.cloud.google.com/dataform/reference/rest/v1beta1/projects.locations.repositories.releaseConfigs/list)` |  `GET /v1beta1/{parent=projects/*/locations/*/repositories/*}/releaseConfigs`   
Lists ReleaseConfigs in a given Repository.  
`[patch](https://docs.cloud.google.com/dataform/reference/rest/v1beta1/projects.locations.repositories.releaseConfigs/patch)` |  `PATCH /v1beta1/{releaseConfig.name=projects/*/locations/*/repositories/*/releaseConfigs/*}`   
Updates a single ReleaseConfig.  
  
## REST Resource: [v1beta1.projects.locations.repositories.workflowConfigs](https://docs.cloud.google.com/dataform/reference/rest/v1beta1/projects.locations.repositories.workflowConfigs)

Methods  
---  
`[create](https://docs.cloud.google.com/dataform/reference/rest/v1beta1/projects.locations.repositories.workflowConfigs/create)` |  `POST /v1beta1/{parent=projects/*/locations/*/repositories/*}/workflowConfigs`   
Creates a new WorkflowConfig in a given Repository.  
`[delete](https://docs.cloud.google.com/dataform/reference/rest/v1beta1/projects.locations.repositories.workflowConfigs/delete)` |  `DELETE /v1beta1/{name=projects/*/locations/*/repositories/*/workflowConfigs/*}`   
Deletes a single WorkflowConfig.  
`[get](https://docs.cloud.google.com/dataform/reference/rest/v1beta1/projects.locations.repositories.workflowConfigs/get)` |  `GET /v1beta1/{name=projects/*/locations/*/repositories/*/workflowConfigs/*}`   
Fetches a single WorkflowConfig.  
`[list](https://docs.cloud.google.com/dataform/reference/rest/v1beta1/projects.locations.repositories.workflowConfigs/list)` |  `GET /v1beta1/{parent=projects/*/locations/*/repositories/*}/workflowConfigs`   
Lists WorkflowConfigs in a given Repository.  
`[patch](https://docs.cloud.google.com/dataform/reference/rest/v1beta1/projects.locations.repositories.workflowConfigs/patch)` |  `PATCH /v1beta1/{workflowConfig.name=projects/*/locations/*/repositories/*/workflowConfigs/*}`   
Updates a single WorkflowConfig.  
  
## REST Resource: [v1beta1.projects.locations.repositories.workflowInvocations](https://docs.cloud.google.com/dataform/reference/rest/v1beta1/projects.locations.repositories.workflowInvocations)

Methods  
---  
`[cancel](https://docs.cloud.google.com/dataform/reference/rest/v1beta1/projects.locations.repositories.workflowInvocations/cancel)` |  `POST /v1beta1/{name=projects/*/locations/*/repositories/*/workflowInvocations/*}:cancel`   
Requests cancellation of a running WorkflowInvocation.  
`[create](https://docs.cloud.google.com/dataform/reference/rest/v1beta1/projects.locations.repositories.workflowInvocations/create)` |  `POST /v1beta1/{parent=projects/*/locations/*/repositories/*}/workflowInvocations`   
Creates a new WorkflowInvocation in a given Repository.  
`[delete](https://docs.cloud.google.com/dataform/reference/rest/v1beta1/projects.locations.repositories.workflowInvocations/delete)` |  `DELETE /v1beta1/{name=projects/*/locations/*/repositories/*/workflowInvocations/*}`   
Deletes a single WorkflowInvocation.  
`[get](https://docs.cloud.google.com/dataform/reference/rest/v1beta1/projects.locations.repositories.workflowInvocations/get)` |  `GET /v1beta1/{name=projects/*/locations/*/repositories/*/workflowInvocations/*}`   
Fetches a single WorkflowInvocation.  
`[list](https://docs.cloud.google.com/dataform/reference/rest/v1beta1/projects.locations.repositories.workflowInvocations/list)` |  `GET /v1beta1/{parent=projects/*/locations/*/repositories/*}/workflowInvocations`   
Lists WorkflowInvocations in a given Repository.  
`[query](https://docs.cloud.google.com/dataform/reference/rest/v1beta1/projects.locations.repositories.workflowInvocations/query)` |  `GET /v1beta1/{name=projects/*/locations/*/repositories/*/workflowInvocations/*}:query`   
Returns WorkflowInvocationActions in a given WorkflowInvocation.  
  
## REST Resource: [v1beta1.projects.locations.repositories.workspaces](https://docs.cloud.google.com/dataform/reference/rest/v1beta1/projects.locations.repositories.workspaces)

Methods  
---  
`[checkout](https://docs.cloud.google.com/dataform/reference/rest/v1beta1/projects.locations.repositories.workspaces/checkout)` |  `POST /v1beta1/{name=projects/*/locations/*/repositories/*/workspaces/*}:checkout`   
Checkout a branch in a workspace.  
`[commit](https://docs.cloud.google.com/dataform/reference/rest/v1beta1/projects.locations.repositories.workspaces/commit)` |  `POST /v1beta1/{name=projects/*/locations/*/repositories/*/workspaces/*}:commit`   
Applies a Git commit for uncommitted files in a Workspace.  
`[create](https://docs.cloud.google.com/dataform/reference/rest/v1beta1/projects.locations.repositories.workspaces/create)` |  `POST /v1beta1/{parent=projects/*/locations/*/repositories/*}/workspaces`   
Creates a new Workspace in a given Repository.  
`[delete](https://docs.cloud.google.com/dataform/reference/rest/v1beta1/projects.locations.repositories.workspaces/delete)` |  `DELETE /v1beta1/{name=projects/*/locations/*/repositories/*/workspaces/*}`   
Deletes a single Workspace.  
`[deleteBranch](https://docs.cloud.google.com/dataform/reference/rest/v1beta1/projects.locations.repositories.workspaces/deleteBranch)` |  `POST /v1beta1/{name=projects/*/locations/*/repositories/*/workspaces/*}:deleteBranch`   
Deletes a branch in a workspace.  
`[fetchBranches](https://docs.cloud.google.com/dataform/reference/rest/v1beta1/projects.locations.repositories.workspaces/fetchBranches)` |  `GET /v1beta1/{name=projects/*/locations/*/repositories/*/workspaces/*}:fetchBranches`   
Fetches branches in a workspace.  
`[fetchCurrentBranch](https://docs.cloud.google.com/dataform/reference/rest/v1beta1/projects.locations.repositories.workspaces/fetchCurrentBranch)` |  `GET /v1beta1/{name=projects/*/locations/*/repositories/*/workspaces/*}:fetchCurrentBranch`   
Fetches the current branch of a workspace.  
`[fetchFileDiff](https://docs.cloud.google.com/dataform/reference/rest/v1beta1/projects.locations.repositories.workspaces/fetchFileDiff)` |  `GET /v1beta1/{workspace=projects/*/locations/*/repositories/*/workspaces/*}:fetchFileDiff`   
Fetches Git diff for an uncommitted file in a Workspace.  
`[fetchFileGitStatuses](https://docs.cloud.google.com/dataform/reference/rest/v1beta1/projects.locations.repositories.workspaces/fetchFileGitStatuses)` |  `GET /v1beta1/{name=projects/*/locations/*/repositories/*/workspaces/*}:fetchFileGitStatuses`   
Fetches Git statuses for the files in a Workspace.  
`[fetchGitAheadBehind](https://docs.cloud.google.com/dataform/reference/rest/v1beta1/projects.locations.repositories.workspaces/fetchGitAheadBehind)` |  `GET /v1beta1/{name=projects/*/locations/*/repositories/*/workspaces/*}:fetchGitAheadBehind`   
Fetches Git ahead/behind against a remote branch.  
`[get](https://docs.cloud.google.com/dataform/reference/rest/v1beta1/projects.locations.repositories.workspaces/get)` |  `GET /v1beta1/{name=projects/*/locations/*/repositories/*/workspaces/*}`   
Fetches a single Workspace.  
`[getIamPolicy](https://docs.cloud.google.com/dataform/reference/rest/v1beta1/projects.locations.repositories.workspaces/getIamPolicy)` |  `GET /v1beta1/{resource=projects/*/locations/*/repositories/*/workspaces/*}:getIamPolicy`   
Gets the access control policy for a resource.  
`[installNpmPackages](https://docs.cloud.google.com/dataform/reference/rest/v1beta1/projects.locations.repositories.workspaces/installNpmPackages)` |  `POST /v1beta1/{workspace=projects/*/locations/*/repositories/*/workspaces/*}:installNpmPackages`   
Installs dependency NPM packages (inside a Workspace).  
`[list](https://docs.cloud.google.com/dataform/reference/rest/v1beta1/projects.locations.repositories.workspaces/list)` |  `GET /v1beta1/{parent=projects/*/locations/*/repositories/*}/workspaces`   
Lists Workspaces in a given Repository.  
`[makeDirectory](https://docs.cloud.google.com/dataform/reference/rest/v1beta1/projects.locations.repositories.workspaces/makeDirectory)` |  `POST /v1beta1/{workspace=projects/*/locations/*/repositories/*/workspaces/*}:makeDirectory`   
Creates a directory inside a Workspace.  
`[moveDirectory](https://docs.cloud.google.com/dataform/reference/rest/v1beta1/projects.locations.repositories.workspaces/moveDirectory)` |  `POST /v1beta1/{workspace=projects/*/locations/*/repositories/*/workspaces/*}:moveDirectory`   
Moves a directory (inside a Workspace), and all of its contents, to a new location.  
`[moveFile](https://docs.cloud.google.com/dataform/reference/rest/v1beta1/projects.locations.repositories.workspaces/moveFile)` |  `POST /v1beta1/{workspace=projects/*/locations/*/repositories/*/workspaces/*}:moveFile`   
Moves a file (inside a Workspace) to a new location.  
`[pull](https://docs.cloud.google.com/dataform/reference/rest/v1beta1/projects.locations.repositories.workspaces/pull)` |  `POST /v1beta1/{name=projects/*/locations/*/repositories/*/workspaces/*}:pull`   
Pulls Git commits from the Repository's remote into a Workspace.  
`[push](https://docs.cloud.google.com/dataform/reference/rest/v1beta1/projects.locations.repositories.workspaces/push)` |  `POST /v1beta1/{name=projects/*/locations/*/repositories/*/workspaces/*}:push`   
Pushes Git commits from a Workspace to the Repository's remote.  
`[queryDirectoryContents](https://docs.cloud.google.com/dataform/reference/rest/v1beta1/projects.locations.repositories.workspaces/queryDirectoryContents)` |  `GET /v1beta1/{workspace=projects/*/locations/*/repositories/*/workspaces/*}:queryDirectoryContents`   
Returns the contents of a given Workspace directory.  
`[readFile](https://docs.cloud.google.com/dataform/reference/rest/v1beta1/projects.locations.repositories.workspaces/readFile)` |  `GET /v1beta1/{workspace=projects/*/locations/*/repositories/*/workspaces/*}:readFile`   
Returns the contents of a file (inside a Workspace).  
`[removeDirectory](https://docs.cloud.google.com/dataform/reference/rest/v1beta1/projects.locations.repositories.workspaces/removeDirectory)` |  `POST /v1beta1/{workspace=projects/*/locations/*/repositories/*/workspaces/*}:removeDirectory`   
Deletes a directory (inside a Workspace) and all of its contents.  
`[removeFile](https://docs.cloud.google.com/dataform/reference/rest/v1beta1/projects.locations.repositories.workspaces/removeFile)` |  `POST /v1beta1/{workspace=projects/*/locations/*/repositories/*/workspaces/*}:removeFile`   
Deletes a file (inside a Workspace).  
`[reset](https://docs.cloud.google.com/dataform/reference/rest/v1beta1/projects.locations.repositories.workspaces/reset)` |  `POST /v1beta1/{name=projects/*/locations/*/repositories/*/workspaces/*}:reset`   
Performs a Git reset for uncommitted files in a Workspace.  
`[searchFiles](https://docs.cloud.google.com/dataform/reference/rest/v1beta1/projects.locations.repositories.workspaces/searchFiles)` |  `GET /v1beta1/{workspace=projects/*/locations/*/repositories/*/workspaces/*}:searchFiles`   
Finds the contents of a given Workspace directory by filter.  
`[setIamPolicy](https://docs.cloud.google.com/dataform/reference/rest/v1beta1/projects.locations.repositories.workspaces/setIamPolicy)` |  `POST /v1beta1/{resource=projects/*/locations/*/repositories/*/workspaces/*}:setIamPolicy`   
Sets the access control policy on the specified resource.  
`[syncWorkspaceRefs](https://docs.cloud.google.com/dataform/reference/rest/v1beta1/projects.locations.repositories.workspaces/syncWorkspaceRefs)` |  `POST /v1beta1/{name=projects/*/locations/*/repositories/*/workspaces/*}:syncWorkspaceRefs`   
Syncs the refs of a workspace.  
`[testIamPermissions](https://docs.cloud.google.com/dataform/reference/rest/v1beta1/projects.locations.repositories.workspaces/testIamPermissions)` |  `POST /v1beta1/{resource=projects/*/locations/*/repositories/*/workspaces/*}:testIamPermissions`   
Returns permissions that a caller has on the specified resource.  
`[writeFile](https://docs.cloud.google.com/dataform/reference/rest/v1beta1/projects.locations.repositories.workspaces/writeFile)` |  `POST /v1beta1/{workspace=projects/*/locations/*/repositories/*/workspaces/*}:writeFile`   
Writes to a file (inside a Workspace).  
  
## REST Resource: [v1beta1.projects.locations.teamFolders](https://docs.cloud.google.com/dataform/reference/rest/v1beta1/projects.locations.teamFolders)

Methods  
---  
`[create](https://docs.cloud.google.com/dataform/reference/rest/v1beta1/projects.locations.teamFolders/create)` |  `POST /v1beta1/{parent=projects/*/locations/*}/teamFolders`   
Creates a new TeamFolder in a given project and location.  
`[delete](https://docs.cloud.google.com/dataform/reference/rest/v1beta1/projects.locations.teamFolders/delete)` |  `DELETE /v1beta1/{name=projects/*/locations/*/teamFolders/*}`   
Deletes a single TeamFolder.  
`[deleteTree](https://docs.cloud.google.com/dataform/reference/rest/v1beta1/projects.locations.teamFolders/deleteTree)` |  `POST /v1beta1/{name=projects/*/locations/*/teamFolders/*}:deleteTree`   
Deletes a TeamFolder with its contents (Folders, Repositories, Workspaces, ReleaseConfigs, and WorkflowConfigs).  
`[get](https://docs.cloud.google.com/dataform/reference/rest/v1beta1/projects.locations.teamFolders/get)` |  `GET /v1beta1/{name=projects/*/locations/*/teamFolders/*}`   
Fetches a single TeamFolder.  
`[getIamPolicy](https://docs.cloud.google.com/dataform/reference/rest/v1beta1/projects.locations.teamFolders/getIamPolicy)` |  `GET /v1beta1/{resource=projects/*/locations/*/teamFolders/*}:getIamPolicy`   
Gets the access control policy for a resource.  
`[patch](https://docs.cloud.google.com/dataform/reference/rest/v1beta1/projects.locations.teamFolders/patch)` |  `PATCH /v1beta1/{teamFolder.name=projects/*/locations/*/teamFolders/*}`   
Updates a single TeamFolder.  
`[queryContents](https://docs.cloud.google.com/dataform/reference/rest/v1beta1/projects.locations.teamFolders/queryContents)` |  `GET /v1beta1/{teamFolder=projects/*/locations/*/teamFolders/*}:queryContents`   
Returns the contents of a given TeamFolder.  
`[search](https://docs.cloud.google.com/dataform/reference/rest/v1beta1/projects.locations.teamFolders/search)` |  `GET /v1beta1/{location=projects/*/locations/*}/teamFolders:search`   
Returns all TeamFolders in a given location that the caller has access to and match the provided filter.  
`[setIamPolicy](https://docs.cloud.google.com/dataform/reference/rest/v1beta1/projects.locations.teamFolders/setIamPolicy)` |  `POST /v1beta1/{resource=projects/*/locations/*/teamFolders/*}:setIamPolicy`   
Sets the access control policy on the specified resource.  
`[testIamPermissions](https://docs.cloud.google.com/dataform/reference/rest/v1beta1/projects.locations.teamFolders/testIamPermissions)` |  `POST /v1beta1/{resource=projects/*/locations/*/teamFolders/*}:testIamPermissions`   
Returns permissions that a caller has on the specified resource.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-08-17 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-08-17 UTC."],[],[]] 
