---
url: https://docs.cloud.google.com/java/docs/reference/google-cloud-dataform/latest/com.google.cloud.dataform.v1beta1.DataformClient
title: Class DataformClient (0.98.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T15:03:28.207516+00:00
---

# Class DataformClient (0.98.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-cloud-dataform/latest/com.google.cloud.dataform.v1beta1.DataformClient

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Class DataformClient (0.98.0) Stay organized with collections  Save and categorize content based on your preferences. 

0.98.0 (latest)  0.94.0  0.93.0  0.92.0  0.90.0  0.87.0  0.86.0  0.84.0  0.82.0  0.81.0  0.80.0  0.79.0  0.77.0  0.75.0  0.74.0  0.73.0  0.72.0  0.71.0  0.69.0  0.67.0  0.66.0  0.63.0  0.62.0  0.61.0  0.59.0  0.58.0  0.57.0  0.56.0  0.55.0  0.54.0  0.53.0  0.52.0  0.51.0  0.50.0  0.48.0  0.47.0  0.46.0  0.45.0  0.44.0  0.43.0  0.42.0  0.41.0  0.40.0  0.39.0  0.38.0  0.36.0  0.35.0  0.34.0  0.33.0  0.32.0  0.31.0  0.30.0  0.29.0  0.28.0  0.27.0  0.26.0  0.23.0  0.22.0  0.21.0  0.20.0  0.19.0  0.18.0  0.17.0  0.16.0  0.15.0  0.14.0  0.13.0  0.12.0  0.11.0  0.10.0  0.8.0  0.7.0  0.6.0  0.5.0  0.4.0  0.3.0  0.2.4 

**Beta**

This library is covered by the [Pre-GA Offerings Terms](https://docs.cloud.google.com/terms/service-terms#1) of the Terms of Service. Pre-GA libraries might have limited support, and changes to pre-GA libraries might not be compatible with other pre-GA versions. For more information, see the [launch stage descriptions](https://docs.cloud.google.com/products#product-launch-stages). 

[GitHub Repository](https://github.com/googleapis/google-cloud-java/tree/main/java-dataform/google-cloud-dataform/src/main/java/com/google/cloud/dataform/v1beta1/DataformClient.java)| [Product Reference](https://cloud.google.com/dataform/docs)  
---|---  
  
Service Description: Dataform is a service to develop, create, document, test, and update curated tables in BigQuery.

This class provides the ability to make remote calls to the backing service through method calls that map to API methods. Sample code to get started:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DataformClient dataformClient = DataformClient.create()) {
       TeamFolderName name = TeamFolderName.of("[PROJECT]", "[LOCATION]", "[TEAM_FOLDER]");
       TeamFolder response = dataformClient.getTeamFolder(name);
     }
     

Note: close() needs to be called on the DataformClient object to clean up resources such as threads. In the example above, try-with-resources is used, which automatically calls close().

Methods Method | Description | Method Variants  
---|---|---  
GetTeamFolder |  Fetches a single TeamFolder. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * getTeamFolder(GetTeamFolderRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * getTeamFolder(TeamFolderName name) 
  * getTeamFolder(String name) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * getTeamFolderCallable() 

  
CreateTeamFolder |  Creates a new TeamFolder in a given project and location. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * createTeamFolder(CreateTeamFolderRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * createTeamFolder(LocationName parent, TeamFolder teamFolder) 
  * createTeamFolder(String parent, TeamFolder teamFolder) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * createTeamFolderCallable() 

  
UpdateTeamFolder |  Updates a single TeamFolder. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * updateTeamFolder(UpdateTeamFolderRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * updateTeamFolder(TeamFolder teamFolder, FieldMask updateMask) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * updateTeamFolderCallable() 

  
DeleteTeamFolder |  Deletes a single TeamFolder. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * deleteTeamFolder(DeleteTeamFolderRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * deleteTeamFolder(TeamFolderName name) 
  * deleteTeamFolder(String name) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * deleteTeamFolderCallable() 

  
DeleteTeamFolderTree |  Deletes a TeamFolder with its contents (Folders, Repositories, Workspaces, ReleaseConfigs, and WorkflowConfigs). |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * deleteTeamFolderTreeAsync(DeleteTeamFolderTreeRequest request) 

Methods that return long-running operations have "Async" method variants that return `OperationFuture`, which is used to track polling of the service.

  * deleteTeamFolderTreeAsync(TeamFolderName name, boolean force) 
  * deleteTeamFolderTreeAsync(String name, boolean force) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * deleteTeamFolderTreeOperationCallable() 
  * deleteTeamFolderTreeCallable() 

  
QueryTeamFolderContents |  Returns the contents of a given TeamFolder. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * queryTeamFolderContents(QueryTeamFolderContentsRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * queryTeamFolderContents(TeamFolderName teamFolder) 
  * queryTeamFolderContents(String teamFolder) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * queryTeamFolderContentsPagedCallable() 
  * queryTeamFolderContentsCallable() 

  
SearchTeamFolders |  Returns all TeamFolders in a given location that the caller has access to and match the provided filter. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * searchTeamFolders(SearchTeamFoldersRequest request) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * searchTeamFoldersPagedCallable() 
  * searchTeamFoldersCallable() 

  
GetFolder |  Fetches a single Folder. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * getFolder(GetFolderRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * getFolder(FolderName name) 
  * getFolder(String name) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * getFolderCallable() 

  
CreateFolder |  Creates a new Folder in a given project and location. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * createFolder(CreateFolderRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * createFolder(LocationName parent, Folder folder) 
  * createFolder(String parent, Folder folder) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * createFolderCallable() 

  
UpdateFolder |  Updates a single Folder. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * updateFolder(UpdateFolderRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * updateFolder(Folder folder, FieldMask updateMask) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * updateFolderCallable() 

  
DeleteFolder |  Deletes a single Folder. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * deleteFolder(DeleteFolderRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * deleteFolder(FolderName name) 
  * deleteFolder(String name) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * deleteFolderCallable() 

  
DeleteFolderTree |  Deletes a Folder with its contents (Folders, Repositories, Workspaces, ReleaseConfigs, and WorkflowConfigs). |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * deleteFolderTreeAsync(DeleteFolderTreeRequest request) 

Methods that return long-running operations have "Async" method variants that return `OperationFuture`, which is used to track polling of the service.

  * deleteFolderTreeAsync(FolderName name, boolean force) 
  * deleteFolderTreeAsync(String name, boolean force) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * deleteFolderTreeOperationCallable() 
  * deleteFolderTreeCallable() 

  
QueryFolderContents |  Returns the contents of a given Folder. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * queryFolderContents(QueryFolderContentsRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * queryFolderContents(FolderName folder) 
  * queryFolderContents(String folder) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * queryFolderContentsPagedCallable() 
  * queryFolderContentsCallable() 

  
QueryUserRootContents |  Returns the contents of a caller's root folder in a given location. The root folder contains all resources that are created by the user and not contained in any other folder. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * queryUserRootContents(QueryUserRootContentsRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * queryUserRootContents(LocationName location) 
  * queryUserRootContents(String location) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * queryUserRootContentsPagedCallable() 
  * queryUserRootContentsCallable() 

  
MoveFolder |  Moves a Folder to a new Folder, TeamFolder, or the root location. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * moveFolderAsync(MoveFolderRequest request) 

Methods that return long-running operations have "Async" method variants that return `OperationFuture`, which is used to track polling of the service.

  * moveFolderAsync(FolderName name, String destinationContainingFolder) 
  * moveFolderAsync(String name, String destinationContainingFolder) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * moveFolderOperationCallable() 
  * moveFolderCallable() 

  
ListRepositories |  Lists Repositories in a given project and location.  **Note:** *This method can return repositories not shown in the [Dataform UI](https://console.cloud.google.com/bigquery/dataform)*. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * listRepositories(ListRepositoriesRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * listRepositories(LocationName parent) 
  * listRepositories(String parent) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * listRepositoriesPagedCallable() 
  * listRepositoriesCallable() 

  
GetRepository |  Fetches a single Repository. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * getRepository(GetRepositoryRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * getRepository(RepositoryName name) 
  * getRepository(String name) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * getRepositoryCallable() 

  
CreateRepository |  Creates a new Repository in a given project and location. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * createRepository(CreateRepositoryRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * createRepository(LocationName parent, Repository repository, String repositoryId) 
  * createRepository(String parent, Repository repository, String repositoryId) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * createRepositoryCallable() 

  
UpdateRepository |  Updates a single Repository.  **Note:** *This method does not fully implement [AIP/134](https://google.aip.dev/134). The wildcard entry (\\*) is treated as a bad request, and when the `field_mask` is omitted, the request is treated as a full update on all modifiable fields.* |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * updateRepository(UpdateRepositoryRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * updateRepository(Repository repository, FieldMask updateMask) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * updateRepositoryCallable() 

  
DeleteRepository |  Deletes a single Repository. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * deleteRepository(DeleteRepositoryRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * deleteRepository(RepositoryName name) 
  * deleteRepository(String name) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * deleteRepositoryCallable() 

  
DeleteRepositoryLongRunning |  Deletes a single repository asynchronously. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * deleteRepositoryLongRunningAsync(DeleteRepositoryLongRunningRequest request) 

Methods that return long-running operations have "Async" method variants that return `OperationFuture`, which is used to track polling of the service.

  * deleteRepositoryLongRunningAsync(RepositoryName name, boolean force) 
  * deleteRepositoryLongRunningAsync(String name, boolean force) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * deleteRepositoryLongRunningOperationCallable() 
  * deleteRepositoryLongRunningCallable() 

  
MoveRepository |  Moves a Repository to a new location. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * moveRepositoryAsync(MoveRepositoryRequest request) 

Methods that return long-running operations have "Async" method variants that return `OperationFuture`, which is used to track polling of the service.

  * moveRepositoryAsync(RepositoryName name, String destinationContainingFolder) 
  * moveRepositoryAsync(String name, String destinationContainingFolder) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * moveRepositoryOperationCallable() 
  * moveRepositoryCallable() 

  
CommitRepositoryChanges |  Applies a Git commit to a Repository. The Repository must not have a value for `git_remote_settings.url`. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * commitRepositoryChanges(CommitRepositoryChangesRequest request) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * commitRepositoryChangesCallable() 

  
ReadRepositoryFile |  Returns the contents of a file (inside a Repository). The Repository must not have a value for `git_remote_settings.url`. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * readRepositoryFile(ReadRepositoryFileRequest request) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * readRepositoryFileCallable() 

  
QueryRepositoryDirectoryContents |  Returns the contents of a given Repository directory. The Repository must not have a value for `git_remote_settings.url`. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * queryRepositoryDirectoryContents(QueryRepositoryDirectoryContentsRequest request) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * queryRepositoryDirectoryContentsPagedCallable() 
  * queryRepositoryDirectoryContentsCallable() 

  
FetchRepositoryHistory |  Fetches a Repository's history of commits. The Repository must not have a value for `git_remote_settings.url`. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * fetchRepositoryHistory(FetchRepositoryHistoryRequest request) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * fetchRepositoryHistoryPagedCallable() 
  * fetchRepositoryHistoryCallable() 

  
ComputeRepositoryAccessTokenStatus |  Computes a Repository's Git access token status. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * computeRepositoryAccessTokenStatus(ComputeRepositoryAccessTokenStatusRequest request) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * computeRepositoryAccessTokenStatusCallable() 

  
FetchRemoteBranches |  Fetches a Repository's remote branches. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * fetchRemoteBranches(FetchRemoteBranchesRequest request) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * fetchRemoteBranchesCallable() 

  
ListWorkspaces |  Lists Workspaces in a given Repository. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * listWorkspaces(ListWorkspacesRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * listWorkspaces(RepositoryName parent) 
  * listWorkspaces(String parent) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * listWorkspacesPagedCallable() 
  * listWorkspacesCallable() 

  
GetWorkspace |  Fetches a single Workspace. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * getWorkspace(GetWorkspaceRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * getWorkspace(WorkspaceName name) 
  * getWorkspace(String name) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * getWorkspaceCallable() 

  
CreateWorkspace |  Creates a new Workspace in a given Repository. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * createWorkspace(CreateWorkspaceRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * createWorkspace(RepositoryName parent, Workspace workspace, String workspaceId) 
  * createWorkspace(String parent, Workspace workspace, String workspaceId) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * createWorkspaceCallable() 

  
DeleteWorkspace |  Deletes a single Workspace. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * deleteWorkspace(DeleteWorkspaceRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * deleteWorkspace(WorkspaceName name) 
  * deleteWorkspace(String name) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * deleteWorkspaceCallable() 

  
InstallNpmPackages |  Installs dependency NPM packages (inside a Workspace). |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * installNpmPackages(InstallNpmPackagesRequest request) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * installNpmPackagesCallable() 

  
PullGitCommits |  Pulls Git commits from the Repository's remote into a Workspace. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * pullGitCommits(PullGitCommitsRequest request) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * pullGitCommitsCallable() 

  
SyncWorkspaceRefs |  Syncs the refs of a Workspace. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * syncWorkspaceRefs(SyncWorkspaceRefsRequest request) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * syncWorkspaceRefsCallable() 

  
FetchWorkspaceBranches |  Fetches branches in a Workspace. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * fetchWorkspaceBranches(FetchWorkspaceBranchesRequest request) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * fetchWorkspaceBranchesPagedCallable() 
  * fetchWorkspaceBranchesCallable() 

  
DeleteBranch |  Deletes a branch in a Workspace. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * deleteBranch(DeleteBranchRequest request) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * deleteBranchCallable() 

  
CheckoutWorkspaceBranch |  Checkout a branch in a Workspace. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * checkoutWorkspaceBranch(CheckoutWorkspaceBranchRequest request) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * checkoutWorkspaceBranchCallable() 

  
FetchCurrentWorkspaceBranch |  Fetches the current branch of a Workspace. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * fetchCurrentWorkspaceBranch(FetchCurrentWorkspaceBranchRequest request) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * fetchCurrentWorkspaceBranchCallable() 

  
PushGitCommits |  Pushes Git commits from a Workspace to the Repository's remote. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * pushGitCommits(PushGitCommitsRequest request) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * pushGitCommitsCallable() 

  
FetchFileGitStatuses |  Fetches Git statuses for the files in a Workspace. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * fetchFileGitStatuses(FetchFileGitStatusesRequest request) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * fetchFileGitStatusesCallable() 

  
FetchGitAheadBehind |  Fetches Git ahead/behind against a remote branch. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * fetchGitAheadBehind(FetchGitAheadBehindRequest request) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * fetchGitAheadBehindCallable() 

  
CommitWorkspaceChanges |  Applies a Git commit for uncommitted files in a Workspace. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * commitWorkspaceChanges(CommitWorkspaceChangesRequest request) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * commitWorkspaceChangesCallable() 

  
ResetWorkspaceChanges |  Performs a Git reset for uncommitted files in a Workspace. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * resetWorkspaceChanges(ResetWorkspaceChangesRequest request) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * resetWorkspaceChangesCallable() 

  
FetchFileDiff |  Fetches Git diff for an uncommitted file in a Workspace. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * fetchFileDiff(FetchFileDiffRequest request) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * fetchFileDiffCallable() 

  
QueryDirectoryContents |  Returns the contents of a given Workspace directory. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * queryDirectoryContents(QueryDirectoryContentsRequest request) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * queryDirectoryContentsPagedCallable() 
  * queryDirectoryContentsCallable() 

  
SearchFiles |  Finds the contents of a given Workspace directory by filter. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * searchFiles(SearchFilesRequest request) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * searchFilesPagedCallable() 
  * searchFilesCallable() 

  
MakeDirectory |  Creates a directory inside a Workspace. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * makeDirectory(MakeDirectoryRequest request) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * makeDirectoryCallable() 

  
RemoveDirectory |  Deletes a directory (inside a Workspace) and all of its contents. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * removeDirectory(RemoveDirectoryRequest request) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * removeDirectoryCallable() 

  
MoveDirectory |  Moves a directory (inside a Workspace), and all of its contents, to a new location. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * moveDirectory(MoveDirectoryRequest request) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * moveDirectoryCallable() 

  
ReadFile |  Returns the contents of a file (inside a Workspace). |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * readFile(ReadFileRequest request) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * readFileCallable() 

  
RemoveFile |  Deletes a file (inside a Workspace). |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * removeFile(RemoveFileRequest request) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * removeFileCallable() 

  
MoveFile |  Moves a file (inside a Workspace) to a new location. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * moveFile(MoveFileRequest request) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * moveFileCallable() 

  
WriteFile |  Writes to a file (inside a Workspace). |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * writeFile(WriteFileRequest request) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * writeFileCallable() 

  
ListReleaseConfigs |  Lists ReleaseConfigs in a given Repository. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * listReleaseConfigs(ListReleaseConfigsRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * listReleaseConfigs(RepositoryName parent) 
  * listReleaseConfigs(String parent) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * listReleaseConfigsPagedCallable() 
  * listReleaseConfigsCallable() 

  
GetReleaseConfig |  Fetches a single ReleaseConfig. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * getReleaseConfig(GetReleaseConfigRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * getReleaseConfig(ReleaseConfigName name) 
  * getReleaseConfig(String name) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * getReleaseConfigCallable() 

  
CreateReleaseConfig |  Creates a new ReleaseConfig in a given Repository. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * createReleaseConfig(CreateReleaseConfigRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * createReleaseConfig(RepositoryName parent, ReleaseConfig releaseConfig, String releaseConfigId) 
  * createReleaseConfig(String parent, ReleaseConfig releaseConfig, String releaseConfigId) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * createReleaseConfigCallable() 

  
UpdateReleaseConfig |  Updates a single ReleaseConfig.  **Note:** *This method does not fully implement [AIP/134](https://google.aip.dev/134). The wildcard entry (\\*) is treated as a bad request, and when the `field_mask` is omitted, the request is treated as a full update on all modifiable fields.* |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * updateReleaseConfig(UpdateReleaseConfigRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * updateReleaseConfig(ReleaseConfig releaseConfig, FieldMask updateMask) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * updateReleaseConfigCallable() 

  
DeleteReleaseConfig |  Deletes a single ReleaseConfig. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * deleteReleaseConfig(DeleteReleaseConfigRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * deleteReleaseConfig(ReleaseConfigName name) 
  * deleteReleaseConfig(String name) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * deleteReleaseConfigCallable() 

  
ListCompilationResults |  Lists CompilationResults in a given Repository. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * listCompilationResults(ListCompilationResultsRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * listCompilationResults(RepositoryName parent) 
  * listCompilationResults(String parent) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * listCompilationResultsPagedCallable() 
  * listCompilationResultsCallable() 

  
GetCompilationResult |  Fetches a single CompilationResult. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * getCompilationResult(GetCompilationResultRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * getCompilationResult(CompilationResultName name) 
  * getCompilationResult(String name) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * getCompilationResultCallable() 

  
CreateCompilationResult |  Creates a new CompilationResult in a given project and location. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * createCompilationResult(CreateCompilationResultRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * createCompilationResult(RepositoryName parent, CompilationResult compilationResult) 
  * createCompilationResult(String parent, CompilationResult compilationResult) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * createCompilationResultCallable() 

  
QueryCompilationResultActions |  Returns CompilationResultActions in a given CompilationResult. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * queryCompilationResultActions(QueryCompilationResultActionsRequest request) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * queryCompilationResultActionsPagedCallable() 
  * queryCompilationResultActionsCallable() 

  
ListWorkflowConfigs |  Lists WorkflowConfigs in a given Repository. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * listWorkflowConfigs(ListWorkflowConfigsRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * listWorkflowConfigs(RepositoryName parent) 
  * listWorkflowConfigs(String parent) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * listWorkflowConfigsPagedCallable() 
  * listWorkflowConfigsCallable() 

  
GetWorkflowConfig |  Fetches a single WorkflowConfig. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * getWorkflowConfig(GetWorkflowConfigRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * getWorkflowConfig(WorkflowConfigName name) 
  * getWorkflowConfig(String name) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * getWorkflowConfigCallable() 

  
CreateWorkflowConfig |  Creates a new WorkflowConfig in a given Repository. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * createWorkflowConfig(CreateWorkflowConfigRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * createWorkflowConfig(RepositoryName parent, WorkflowConfig workflowConfig, String workflowConfigId) 
  * createWorkflowConfig(String parent, WorkflowConfig workflowConfig, String workflowConfigId) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * createWorkflowConfigCallable() 

  
UpdateWorkflowConfig |  Updates a single WorkflowConfig.  **Note:** *This method does not fully implement [AIP/134](https://google.aip.dev/134). The wildcard entry (\\*) is treated as a bad request, and when the `field_mask` is omitted, the request is treated as a full update on all modifiable fields.* |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * updateWorkflowConfig(UpdateWorkflowConfigRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * updateWorkflowConfig(WorkflowConfig workflowConfig, FieldMask updateMask) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * updateWorkflowConfigCallable() 

  
DeleteWorkflowConfig |  Deletes a single WorkflowConfig. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * deleteWorkflowConfig(DeleteWorkflowConfigRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * deleteWorkflowConfig(WorkflowConfigName name) 
  * deleteWorkflowConfig(String name) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * deleteWorkflowConfigCallable() 

  
ListWorkflowInvocations |  Lists WorkflowInvocations in a given Repository. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * listWorkflowInvocations(ListWorkflowInvocationsRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * listWorkflowInvocations(RepositoryName parent) 
  * listWorkflowInvocations(String parent) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * listWorkflowInvocationsPagedCallable() 
  * listWorkflowInvocationsCallable() 

  
GetWorkflowInvocation |  Fetches a single WorkflowInvocation. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * getWorkflowInvocation(GetWorkflowInvocationRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * getWorkflowInvocation(WorkflowInvocationName name) 
  * getWorkflowInvocation(String name) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * getWorkflowInvocationCallable() 

  
CreateWorkflowInvocation |  Creates a new WorkflowInvocation in a given Repository. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * createWorkflowInvocation(CreateWorkflowInvocationRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * createWorkflowInvocation(RepositoryName parent, WorkflowInvocation workflowInvocation) 
  * createWorkflowInvocation(String parent, WorkflowInvocation workflowInvocation) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * createWorkflowInvocationCallable() 

  
DeleteWorkflowInvocation |  Deletes a single WorkflowInvocation. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * deleteWorkflowInvocation(DeleteWorkflowInvocationRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * deleteWorkflowInvocation(WorkflowInvocationName name) 
  * deleteWorkflowInvocation(String name) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * deleteWorkflowInvocationCallable() 

  
CancelWorkflowInvocation |  Requests cancellation of a running WorkflowInvocation. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * cancelWorkflowInvocation(CancelWorkflowInvocationRequest request) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * cancelWorkflowInvocationCallable() 

  
QueryWorkflowInvocationActions |  Returns WorkflowInvocationActions in a given WorkflowInvocation. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * queryWorkflowInvocationActions(QueryWorkflowInvocationActionsRequest request) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * queryWorkflowInvocationActionsPagedCallable() 
  * queryWorkflowInvocationActionsCallable() 

  
GetConfig |  Get default config for a given project and location. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * getConfig(GetConfigRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * getConfig(ConfigName name) 
  * getConfig(String name) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * getConfigCallable() 

  
UpdateConfig |  Update default config for a given project and location.  **Note:** *This method does not fully implement [AIP/134](https://google.aip.dev/134). The wildcard entry (\\*) is treated as a bad request, and when the `field_mask` is omitted, the request is treated as a full update on all modifiable fields.* |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * updateConfig(UpdateConfigRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * updateConfig(Config config, FieldMask updateMask) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * updateConfigCallable() 

  
GetIamPolicy |  Gets the access control policy for a resource. Returns an empty policy if the resource exists and does not have a policy set. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * getIamPolicy(GetIamPolicyRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * getIamPolicy(ResourceName resource) 
  * getIamPolicy(String resource) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * getIamPolicyCallable() 

  
SetIamPolicy |  Sets the access control policy on the specified resource. Replaces any existing policy.  Can return `NOT_FOUND`, `INVALID_ARGUMENT`, and `PERMISSION_DENIED` errors. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * setIamPolicy(SetIamPolicyRequest request) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * setIamPolicyCallable() 

  
TestIamPermissions |  Returns permissions that a caller has on the specified resource. If the resource does not exist, this will return an empty set of permissions, not a `NOT_FOUND` error.  Note: This operation is designed to be used for building permission-aware UIs and command-line tools, not for authorization checking. This operation may "fail open" without warning. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * testIamPermissions(TestIamPermissionsRequest request) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * testIamPermissionsCallable() 

  
ListLocations |  Lists information about the supported locations for this service.  This method lists locations based on the resource scope provided inthe ListLocationsRequest.name field: ***Global locations**: If `name` is empty, the method lists thepublic locations available to all projects. * **Project-specificlocations**: If `name` follows the format`projects/{project}`, the method lists locations visible to thatspecific project. This includes public, private, or otherproject-specific locations enabled for the project.  For gRPC and client library implementations, the resource name ispassed as the `name` field. For direct service calls, the resourcename isincorporated into the request path based on the specific serviceimplementation and version. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * listLocations(ListLocationsRequest request) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * listLocationsPagedCallable() 
  * listLocationsCallable() 

  
GetLocation |  Gets information about a location. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * getLocation(GetLocationRequest request) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * getLocationCallable() 

  
  
See the individual methods for example code.

Many parameters require resource names to be formatted in a particular way. To assist with these names, this class includes a format method for each type of name, and additionally a parse method to extract the individual identifiers contained within names that are returned.

This class can be customized by passing in a custom instance of DataformSettings to create(). For example:

To customize credentials:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     DataformSettings dataformSettings =
         DataformSettings.newBuilder()
             .setCredentialsProvider(FixedCredentialsProvider.create(myCredentials))
             .build();
     DataformClient dataformClient = DataformClient.create(dataformSettings);
     

To customize the endpoint:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     DataformSettings dataformSettings =
         DataformSettings.newBuilder().setEndpoint(myEndpoint).build();
     DataformClient dataformClient = DataformClient.create(dataformSettings);
     

To use REST (HTTP1.1/JSON) transport (instead of gRPC) for sending and receiving requests over the wire:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     DataformSettings dataformSettings = DataformSettings.newHttpJsonBuilder().build();
     DataformClient dataformClient = DataformClient.create(dataformSettings);
     

Please refer to the GitHub repository's samples for more quickstart code snippets.

## Inheritance

[java.lang.Object](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html) > DataformClient

## Static Methods 

### create()
    
    
    public static final DataformClient create()

Constructs an instance of DataformClient with default settings.

**Returns**  
---  
**Type** | **Description**  
`[DataformClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataform/latest/com.google.cloud.dataform.v1beta1.DataformClient)` |   
**Exceptions**  
---  
**Type** | **Description**  
`[IOException](https://docs.oracle.com/javase/8/docs/api/java/io/IOException.html)` |   
  
### create(DataformSettings settings)
    
    
    public static final DataformClient create(DataformSettings settings)

Constructs an instance of DataformClient, using the given settings. The channels are created based on the settings passed in, or defaults for any settings that are not set.

**Parameter**  
---  
**Name** | **Description**  
`settings` | `[DataformSettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataform/latest/com.google.cloud.dataform.v1beta1.DataformSettings)`  
  
**Returns**  
---  
**Type** | **Description**  
`[DataformClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataform/latest/com.google.cloud.dataform.v1beta1.DataformClient)` |   
**Exceptions**  
---  
**Type** | **Description**  
`[IOException](https://docs.oracle.com/javase/8/docs/api/java/io/IOException.html)` |   
  
### create(DataformStub stub)
    
    
    public static final DataformClient create(DataformStub stub)

Constructs an instance of DataformClient, using the given stub for making calls. This is for advanced usage - prefer using create(DataformSettings).

**Parameter**  
---  
**Name** | **Description**  
`stub` | `[DataformStub](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataform/latest/com.google.cloud.dataform.v1beta1.stub.DataformStub)`  
  
**Returns**  
---  
**Type** | **Description**  
`[DataformClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataform/latest/com.google.cloud.dataform.v1beta1.DataformClient)` |   
  
## Constructors 

### DataformClient(DataformSettings settings)
    
    
    protected DataformClient(DataformSettings settings)

Constructs an instance of DataformClient, using the given settings. This is protected so that it is easy to make a subclass, but otherwise, the static factory methods should be preferred.

**Parameter**  
---  
**Name** | **Description**  
`settings` | `[DataformSettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataform/latest/com.google.cloud.dataform.v1beta1.DataformSettings)`  
  
  
### DataformClient(DataformStub stub)
    
    
    protected DataformClient(DataformStub stub)

**Parameter**  
---  
**Name** | **Description**  
`stub` | `[DataformStub](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataform/latest/com.google.cloud.dataform.v1beta1.stub.DataformStub)`  
  
  
## Methods 

### awaitTermination(long duration, TimeUnit unit)
    
    
    public boolean awaitTermination(long duration, TimeUnit unit)

**Parameters**  
---  
**Name** | **Description**  
`duration` | `[long](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
`unit` | `[TimeUnit](https://docs.oracle.com/javase/8/docs/api/java/util/concurrent/TimeUnit.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` |   
**Exceptions**  
---  
**Type** | **Description**  
`[InterruptedException](https://docs.oracle.com/javase/8/docs/api/java/lang/InterruptedException.html)` |   
  
### cancelWorkflowInvocation(CancelWorkflowInvocationRequest request)
    
    
    public final CancelWorkflowInvocationResponse cancelWorkflowInvocation(CancelWorkflowInvocationRequest request)

Requests cancellation of a running WorkflowInvocation.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DataformClient dataformClient = DataformClient.create()) {
       CancelWorkflowInvocationRequest request =
           CancelWorkflowInvocationRequest.newBuilder()
               .setName(
                   WorkflowInvocationName.of(
                           "[PROJECT]", "[LOCATION]", "[REPOSITORY]", "[WORKFLOW_INVOCATION]")
                       .toString())
               .build();
       CancelWorkflowInvocationResponse response = dataformClient.cancelWorkflowInvocation(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[CancelWorkflowInvocationRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataform/latest/com.google.cloud.dataform.v1beta1.CancelWorkflowInvocationRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[CancelWorkflowInvocationResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataform/latest/com.google.cloud.dataform.v1beta1.CancelWorkflowInvocationResponse)` |   
  
### cancelWorkflowInvocationCallable()
    
    
    public final UnaryCallable<CancelWorkflowInvocationRequest,CancelWorkflowInvocationResponse> cancelWorkflowInvocationCallable()

Requests cancellation of a running WorkflowInvocation.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DataformClient dataformClient = DataformClient.create()) {
       CancelWorkflowInvocationRequest request =
           CancelWorkflowInvocationRequest.newBuilder()
               .setName(
                   WorkflowInvocationName.of(
                           "[PROJECT]", "[LOCATION]", "[REPOSITORY]", "[WORKFLOW_INVOCATION]")
                       .toString())
               .build();
       ApiFuture<CancelWorkflowInvocationResponse> future =
           dataformClient.cancelWorkflowInvocationCallable().futureCall(request);
       // Do something.
       CancelWorkflowInvocationResponse response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[CancelWorkflowInvocationRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataform/latest/com.google.cloud.dataform.v1beta1.CancelWorkflowInvocationRequest),[CancelWorkflowInvocationResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataform/latest/com.google.cloud.dataform.v1beta1.CancelWorkflowInvocationResponse)>` |   
  
### checkoutWorkspaceBranch(CheckoutWorkspaceBranchRequest request)
    
    
    public final void checkoutWorkspaceBranch(CheckoutWorkspaceBranchRequest request)

Checkout a branch in a Workspace.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DataformClient dataformClient = DataformClient.create()) {
       CheckoutWorkspaceBranchRequest request =
           CheckoutWorkspaceBranchRequest.newBuilder()
               .setName(
                   WorkspaceName.of("[PROJECT]", "[LOCATION]", "[REPOSITORY]", "[WORKSPACE]")
                       .toString())
               .setBranch("branch-1381030494")
               .setCreateIfNotExists(true)
               .setSourceBranch("sourceBranch838777245")
               .build();
       dataformClient.checkoutWorkspaceBranch(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[CheckoutWorkspaceBranchRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataform/latest/com.google.cloud.dataform.v1beta1.CheckoutWorkspaceBranchRequest)`  
The request object containing all of the parameters for the API call.  
  
### checkoutWorkspaceBranchCallable()
    
    
    public final UnaryCallable<CheckoutWorkspaceBranchRequest,Empty> checkoutWorkspaceBranchCallable()

Checkout a branch in a Workspace.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DataformClient dataformClient = DataformClient.create()) {
       CheckoutWorkspaceBranchRequest request =
           CheckoutWorkspaceBranchRequest.newBuilder()
               .setName(
                   WorkspaceName.of("[PROJECT]", "[LOCATION]", "[REPOSITORY]", "[WORKSPACE]")
                       .toString())
               .setBranch("branch-1381030494")
               .setCreateIfNotExists(true)
               .setSourceBranch("sourceBranch838777245")
               .build();
       ApiFuture<Empty> future =
           dataformClient.checkoutWorkspaceBranchCallable().futureCall(request);
       // Do something.
       future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[CheckoutWorkspaceBranchRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataform/latest/com.google.cloud.dataform.v1beta1.CheckoutWorkspaceBranchRequest),[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html)>` |   
  
### close()
    
    
    public final void close()

### commitRepositoryChanges(CommitRepositoryChangesRequest request)
    
    
    public final CommitRepositoryChangesResponse commitRepositoryChanges(CommitRepositoryChangesRequest request)

Applies a Git commit to a Repository. The Repository must not have a value for `git_remote_settings.url`.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DataformClient dataformClient = DataformClient.create()) {
       CommitRepositoryChangesRequest request =
           CommitRepositoryChangesRequest.newBuilder()
               .setName(RepositoryName.of("[PROJECT]", "[LOCATION]", "[REPOSITORY]").toString())
               .setCommitMetadata(CommitMetadata.newBuilder().build())
               .setRequiredHeadCommitSha("requiredHeadCommitSha-393901930")
               .putAllFileOperations(
                   new HashMap<String, CommitRepositoryChangesRequest.FileOperation>())
               .build();
       CommitRepositoryChangesResponse response = dataformClient.commitRepositoryChanges(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[CommitRepositoryChangesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataform/latest/com.google.cloud.dataform.v1beta1.CommitRepositoryChangesRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[CommitRepositoryChangesResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataform/latest/com.google.cloud.dataform.v1beta1.CommitRepositoryChangesResponse)` |   
  
### commitRepositoryChangesCallable()
    
    
    public final UnaryCallable<CommitRepositoryChangesRequest,CommitRepositoryChangesResponse> commitRepositoryChangesCallable()

Applies a Git commit to a Repository. The Repository must not have a value for `git_remote_settings.url`.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DataformClient dataformClient = DataformClient.create()) {
       CommitRepositoryChangesRequest request =
           CommitRepositoryChangesRequest.newBuilder()
               .setName(RepositoryName.of("[PROJECT]", "[LOCATION]", "[REPOSITORY]").toString())
               .setCommitMetadata(CommitMetadata.newBuilder().build())
               .setRequiredHeadCommitSha("requiredHeadCommitSha-393901930")
               .putAllFileOperations(
                   new HashMap<String, CommitRepositoryChangesRequest.FileOperation>())
               .build();
       ApiFuture<CommitRepositoryChangesResponse> future =
           dataformClient.commitRepositoryChangesCallable().futureCall(request);
       // Do something.
       CommitRepositoryChangesResponse response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[CommitRepositoryChangesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataform/latest/com.google.cloud.dataform.v1beta1.CommitRepositoryChangesRequest),[CommitRepositoryChangesResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataform/latest/com.google.cloud.dataform.v1beta1.CommitRepositoryChangesResponse)>` |   
  
### commitWorkspaceChanges(CommitWorkspaceChangesRequest request)
    
    
    public final CommitWorkspaceChangesResponse commitWorkspaceChanges(CommitWorkspaceChangesRequest request)

Applies a Git commit for uncommitted files in a Workspace.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DataformClient dataformClient = DataformClient.create()) {
       CommitWorkspaceChangesRequest request =
           CommitWorkspaceChangesRequest.newBuilder()
               .setName(
                   WorkspaceName.of("[PROJECT]", "[LOCATION]", "[REPOSITORY]", "[WORKSPACE]")
                       .toString())
               .setAuthor(CommitAuthor.newBuilder().build())
               .setCommitMessage("commitMessage2039804624")
               .addAllPaths(new ArrayList<String>())
               .build();
       CommitWorkspaceChangesResponse response = dataformClient.commitWorkspaceChanges(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[CommitWorkspaceChangesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataform/latest/com.google.cloud.dataform.v1beta1.CommitWorkspaceChangesRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[CommitWorkspaceChangesResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataform/latest/com.google.cloud.dataform.v1beta1.CommitWorkspaceChangesResponse)` |   
  
### commitWorkspaceChangesCallable()
    
    
    public final UnaryCallable<CommitWorkspaceChangesRequest,CommitWorkspaceChangesResponse> commitWorkspaceChangesCallable()

Applies a Git commit for uncommitted files in a Workspace.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DataformClient dataformClient = DataformClient.create()) {
       CommitWorkspaceChangesRequest request =
           CommitWorkspaceChangesRequest.newBuilder()
               .setName(
                   WorkspaceName.of("[PROJECT]", "[LOCATION]", "[REPOSITORY]", "[WORKSPACE]")
                       .toString())
               .setAuthor(CommitAuthor.newBuilder().build())
               .setCommitMessage("commitMessage2039804624")
               .addAllPaths(new ArrayList<String>())
               .build();
       ApiFuture<CommitWorkspaceChangesResponse> future =
           dataformClient.commitWorkspaceChangesCallable().futureCall(request);
       // Do something.
       CommitWorkspaceChangesResponse response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[CommitWorkspaceChangesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataform/latest/com.google.cloud.dataform.v1beta1.CommitWorkspaceChangesRequest),[CommitWorkspaceChangesResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataform/latest/com.google.cloud.dataform.v1beta1.CommitWorkspaceChangesResponse)>` |   
  
### computeRepositoryAccessTokenStatus(ComputeRepositoryAccessTokenStatusRequest request)
    
    
    public final ComputeRepositoryAccessTokenStatusResponse computeRepositoryAccessTokenStatus(ComputeRepositoryAccessTokenStatusRequest request)

Computes a Repository's Git access token status.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DataformClient dataformClient = DataformClient.create()) {
       ComputeRepositoryAccessTokenStatusRequest request =
           ComputeRepositoryAccessTokenStatusRequest.newBuilder()
               .setName(RepositoryName.of("[PROJECT]", "[LOCATION]", "[REPOSITORY]").toString())
               .build();
       ComputeRepositoryAccessTokenStatusResponse response =
           dataformClient.computeRepositoryAccessTokenStatus(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[ComputeRepositoryAccessTokenStatusRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataform/latest/com.google.cloud.dataform.v1beta1.ComputeRepositoryAccessTokenStatusRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[ComputeRepositoryAccessTokenStatusResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataform/latest/com.google.cloud.dataform.v1beta1.ComputeRepositoryAccessTokenStatusResponse)` |   
  
### computeRepositoryAccessTokenStatusCallable()
    
    
    public final UnaryCallable<ComputeRepositoryAccessTokenStatusRequest,ComputeRepositoryAccessTokenStatusResponse> computeRepositoryAccessTokenStatusCallable()

Computes a Repository's Git access token status.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DataformClient dataformClient = DataformClient.create()) {
       ComputeRepositoryAccessTokenStatusRequest request =
           ComputeRepositoryAccessTokenStatusRequest.newBuilder()
               .setName(RepositoryName.of("[PROJECT]", "[LOCATION]", "[REPOSITORY]").toString())
               .build();
       ApiFuture<ComputeRepositoryAccessTokenStatusResponse> future =
           dataformClient.computeRepositoryAccessTokenStatusCallable().futureCall(request);
       // Do something.
       ComputeRepositoryAccessTokenStatusResponse response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ComputeRepositoryAccessTokenStatusRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataform/latest/com.google.cloud.dataform.v1beta1.ComputeRepositoryAccessTokenStatusRequest),[ComputeRepositoryAccessTokenStatusResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataform/latest/com.google.cloud.dataform.v1beta1.ComputeRepositoryAccessTokenStatusResponse)>` |   
  
### createCompilationResult(@Nullable RepositoryName parent, CompilationResult compilationResult)
    
    
    public final CompilationResult createCompilationResult(@Nullable RepositoryName parent, CompilationResult compilationResult)

Creates a new CompilationResult in a given project and location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DataformClient dataformClient = DataformClient.create()) {
       RepositoryName parent = RepositoryName.of("[PROJECT]", "[LOCATION]", "[REPOSITORY]");
       CompilationResult compilationResult = CompilationResult.newBuilder().build();
       CompilationResult response =
           dataformClient.createCompilationResult(parent, compilationResult);
     }
     

**Parameters**  
---  
**Name** | **Description**  
`parent` | `@org.jspecify.annotations.Nullable com.google.cloud.dataform.v1beta1.RepositoryName`  
Required. The repository in which to create the compilation result. Must be in the format `projects/*/locations/*/repositories/*`.  
`compilationResult` | `[CompilationResult](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataform/latest/com.google.cloud.dataform.v1beta1.CompilationResult)`  
Required. The compilation result to create.  
**Returns**  
---  
**Type** | **Description**  
`[CompilationResult](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataform/latest/com.google.cloud.dataform.v1beta1.CompilationResult)` |   
  
### createCompilationResult(CreateCompilationResultRequest request)
    
    
    public final CompilationResult createCompilationResult(CreateCompilationResultRequest request)

Creates a new CompilationResult in a given project and location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DataformClient dataformClient = DataformClient.create()) {
       CreateCompilationResultRequest request =
           CreateCompilationResultRequest.newBuilder()
               .setParent(RepositoryName.of("[PROJECT]", "[LOCATION]", "[REPOSITORY]").toString())
               .setCompilationResult(CompilationResult.newBuilder().build())
               .build();
       CompilationResult response = dataformClient.createCompilationResult(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[CreateCompilationResultRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataform/latest/com.google.cloud.dataform.v1beta1.CreateCompilationResultRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[CompilationResult](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataform/latest/com.google.cloud.dataform.v1beta1.CompilationResult)` |   
  
### createCompilationResult(String parent, CompilationResult compilationResult)
    
    
    public final CompilationResult createCompilationResult(String parent, CompilationResult compilationResult)

Creates a new CompilationResult in a given project and location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DataformClient dataformClient = DataformClient.create()) {
       String parent = RepositoryName.of("[PROJECT]", "[LOCATION]", "[REPOSITORY]").toString();
       CompilationResult compilationResult = CompilationResult.newBuilder().build();
       CompilationResult response =
           dataformClient.createCompilationResult(parent, compilationResult);
     }
     

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The repository in which to create the compilation result. Must be in the format `projects/*/locations/*/repositories/*`.  
`compilationResult` | `[CompilationResult](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataform/latest/com.google.cloud.dataform.v1beta1.CompilationResult)`  
Required. The compilation result to create.  
**Returns**  
---  
**Type** | **Description**  
`[CompilationResult](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataform/latest/com.google.cloud.dataform.v1beta1.CompilationResult)` |   
  
### createCompilationResultCallable()
    
    
    public final UnaryCallable<CreateCompilationResultRequest,CompilationResult> createCompilationResultCallable()

Creates a new CompilationResult in a given project and location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DataformClient dataformClient = DataformClient.create()) {
       CreateCompilationResultRequest request =
           CreateCompilationResultRequest.newBuilder()
               .setParent(RepositoryName.of("[PROJECT]", "[LOCATION]", "[REPOSITORY]").toString())
               .setCompilationResult(CompilationResult.newBuilder().build())
               .build();
       ApiFuture<CompilationResult> future =
           dataformClient.createCompilationResultCallable().futureCall(request);
       // Do something.
       CompilationResult response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[CreateCompilationResultRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataform/latest/com.google.cloud.dataform.v1beta1.CreateCompilationResultRequest),[CompilationResult](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataform/latest/com.google.cloud.dataform.v1beta1.CompilationResult)>` |   
  
### createFolder(@Nullable LocationName parent, Folder folder)
    
    
    public final Folder createFolder(@Nullable LocationName parent, Folder folder)

Creates a new Folder in a given project and location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DataformClient dataformClient = DataformClient.create()) {
       LocationName parent = LocationName.of("[PROJECT]", "[LOCATION]");
       Folder folder = Folder.newBuilder().build();
       Folder response = dataformClient.createFolder(parent, folder);
     }
     

**Parameters**  
---  
**Name** | **Description**  
`parent` | `@org.jspecify.annotations.Nullable com.google.cloud.dataform.v1beta1.LocationName`  
Required. The location in which to create the Folder. Must be in the format `projects/*/locations/*`.  
`folder` | `[Folder](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataform/latest/com.google.cloud.dataform.v1beta1.Folder)`  
Required. The Folder to create.  
**Returns**  
---  
**Type** | **Description**  
`[Folder](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataform/latest/com.google.cloud.dataform.v1beta1.Folder)` |   
  
### createFolder(CreateFolderRequest request)
    
    
    public final Folder createFolder(CreateFolderRequest request)

Creates a new Folder in a given project and location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DataformClient dataformClient = DataformClient.create()) {
       CreateFolderRequest request =
           CreateFolderRequest.newBuilder()
               .setParent(LocationName.of("[PROJECT]", "[LOCATION]").toString())
               .setFolder(Folder.newBuilder().build())
               .setFolderId("folderId294109737")
               .build();
       Folder response = dataformClient.createFolder(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[CreateFolderRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataform/latest/com.google.cloud.dataform.v1beta1.CreateFolderRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[Folder](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataform/latest/com.google.cloud.dataform.v1beta1.Folder)` |   
  
### createFolder(String parent, Folder folder)
    
    
    public final Folder createFolder(String parent, Folder folder)

Creates a new Folder in a given project and location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DataformClient dataformClient = DataformClient.create()) {
       String parent = LocationName.of("[PROJECT]", "[LOCATION]").toString();
       Folder folder = Folder.newBuilder().build();
       Folder response = dataformClient.createFolder(parent, folder);
     }
     

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The location in which to create the Folder. Must be in the format `projects/*/locations/*`.  
`folder` | `[Folder](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataform/latest/com.google.cloud.dataform.v1beta1.Folder)`  
Required. The Folder to create.  
**Returns**  
---  
**Type** | **Description**  
`[Folder](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataform/latest/com.google.cloud.dataform.v1beta1.Folder)` |   
  
### createFolderCallable()
    
    
    public final UnaryCallable<CreateFolderRequest,Folder> createFolderCallable()

Creates a new Folder in a given project and location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DataformClient dataformClient = DataformClient.create()) {
       CreateFolderRequest request =
           CreateFolderRequest.newBuilder()
               .setParent(LocationName.of("[PROJECT]", "[LOCATION]").toString())
               .setFolder(Folder.newBuilder().build())
               .setFolderId("folderId294109737")
               .build();
       ApiFuture<Folder> future = dataformClient.createFolderCallable().futureCall(request);
       // Do something.
       Folder response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[CreateFolderRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataform/latest/com.google.cloud.dataform.v1beta1.CreateFolderRequest),[Folder](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataform/latest/com.google.cloud.dataform.v1beta1.Folder)>` |   
  
### createReleaseConfig(@Nullable RepositoryName parent, ReleaseConfig releaseConfig, String releaseConfigId)
    
    
    public final ReleaseConfig createReleaseConfig(@Nullable RepositoryName parent, ReleaseConfig releaseConfig, String releaseConfigId)

Creates a new ReleaseConfig in a given Repository.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DataformClient dataformClient = DataformClient.create()) {
       RepositoryName parent = RepositoryName.of("[PROJECT]", "[LOCATION]", "[REPOSITORY]");
       ReleaseConfig releaseConfig = ReleaseConfig.newBuilder().build();
       String releaseConfigId = "releaseConfigId1350457636";
       ReleaseConfig response =
           dataformClient.createReleaseConfig(parent, releaseConfig, releaseConfigId);
     }
     

**Parameters**  
---  
**Name** | **Description**  
`parent` | `@org.jspecify.annotations.Nullable com.google.cloud.dataform.v1beta1.RepositoryName`  
Required. The repository in which to create the release config. Must be in the format `projects/*/locations/*/repositories/*`.  
`releaseConfig` | `[ReleaseConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataform/latest/com.google.cloud.dataform.v1beta1.ReleaseConfig)`  
Required. The release config to create.  
`releaseConfigId` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The ID to use for the release config, which will become the final component of the release config's resource name.  
**Returns**  
---  
**Type** | **Description**  
`[ReleaseConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataform/latest/com.google.cloud.dataform.v1beta1.ReleaseConfig)` |   
  
### createReleaseConfig(CreateReleaseConfigRequest request)
    
    
    public final ReleaseConfig createReleaseConfig(CreateReleaseConfigRequest request)

Creates a new ReleaseConfig in a given Repository.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DataformClient dataformClient = DataformClient.create()) {
       CreateReleaseConfigRequest request =
           CreateReleaseConfigRequest.newBuilder()
               .setParent(RepositoryName.of("[PROJECT]", "[LOCATION]", "[REPOSITORY]").toString())
               .setReleaseConfig(ReleaseConfig.newBuilder().build())
               .setReleaseConfigId("releaseConfigId1350457636")
               .build();
       ReleaseConfig response = dataformClient.createReleaseConfig(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[CreateReleaseConfigRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataform/latest/com.google.cloud.dataform.v1beta1.CreateReleaseConfigRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[ReleaseConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataform/latest/com.google.cloud.dataform.v1beta1.ReleaseConfig)` |   
  
### createReleaseConfig(String parent, ReleaseConfig releaseConfig, String releaseConfigId)
    
    
    public final ReleaseConfig createReleaseConfig(String parent, ReleaseConfig releaseConfig, String releaseConfigId)

Creates a new ReleaseConfig in a given Repository.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DataformClient dataformClient = DataformClient.create()) {
       String parent = RepositoryName.of("[PROJECT]", "[LOCATION]", "[REPOSITORY]").toString();
       ReleaseConfig releaseConfig = ReleaseConfig.newBuilder().build();
       String releaseConfigId = "releaseConfigId1350457636";
       ReleaseConfig response =
           dataformClient.createReleaseConfig(parent, releaseConfig, releaseConfigId);
     }
     

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The repository in which to create the release config. Must be in the format `projects/*/locations/*/repositories/*`.  
`releaseConfig` | `[ReleaseConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataform/latest/com.google.cloud.dataform.v1beta1.ReleaseConfig)`  
Required. The release config to create.  
`releaseConfigId` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The ID to use for the release config, which will become the final component of the release config's resource name.  
**Returns**  
---  
**Type** | **Description**  
`[ReleaseConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataform/latest/com.google.cloud.dataform.v1beta1.ReleaseConfig)` |   
  
### createReleaseConfigCallable()
    
    
    public final UnaryCallable<CreateReleaseConfigRequest,ReleaseConfig> createReleaseConfigCallable()

Creates a new ReleaseConfig in a given Repository.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DataformClient dataformClient = DataformClient.create()) {
       CreateReleaseConfigRequest request =
           CreateReleaseConfigRequest.newBuilder()
               .setParent(RepositoryName.of("[PROJECT]", "[LOCATION]", "[REPOSITORY]").toString())
               .setReleaseConfig(ReleaseConfig.newBuilder().build())
               .setReleaseConfigId("releaseConfigId1350457636")
               .build();
       ApiFuture<ReleaseConfig> future =
           dataformClient.createReleaseConfigCallable().futureCall(request);
       // Do something.
       ReleaseConfig response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[CreateReleaseConfigRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataform/latest/com.google.cloud.dataform.v1beta1.CreateReleaseConfigRequest),[ReleaseConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataform/latest/com.google.cloud.dataform.v1beta1.ReleaseConfig)>` |   
  
### createRepository(@Nullable LocationName parent, Repository repository, String repositoryId)
    
    
    public final Repository createRepository(@Nullable LocationName parent, Repository repository, String repositoryId)

Creates a new Repository in a given project and location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DataformClient dataformClient = DataformClient.create()) {
       LocationName parent = LocationName.of("[PROJECT]", "[LOCATION]");
       Repository repository = Repository.newBuilder().build();
       String repositoryId = "repositoryId2113747461";
       Repository response = dataformClient.createRepository(parent, repository, repositoryId);
     }
     

**Parameters**  
---  
**Name** | **Description**  
`parent` | `@org.jspecify.annotations.Nullable com.google.cloud.dataform.v1beta1.LocationName`  
Required. The location in which to create the repository. Must be in the format `projects/*/locations/*`.  
`repository` | `[Repository](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataform/latest/com.google.cloud.dataform.v1beta1.Repository)`  
Required. The repository to create.  
`repositoryId` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The ID to use for the repository, which will become the final component of the repository's resource name.  
**Returns**  
---  
**Type** | **Description**  
`[Repository](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataform/latest/com.google.cloud.dataform.v1beta1.Repository)` |   
  
### createRepository(CreateRepositoryRequest request)
    
    
    public final Repository createRepository(CreateRepositoryRequest request)

Creates a new Repository in a given project and location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DataformClient dataformClient = DataformClient.create()) {
       CreateRepositoryRequest request =
           CreateRepositoryRequest.newBuilder()
               .setParent(LocationName.of("[PROJECT]", "[LOCATION]").toString())
               .setRepository(Repository.newBuilder().build())
               .setRepositoryId("repositoryId2113747461")
               .build();
       Repository response = dataformClient.createRepository(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[CreateRepositoryRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataform/latest/com.google.cloud.dataform.v1beta1.CreateRepositoryRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[Repository](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataform/latest/com.google.cloud.dataform.v1beta1.Repository)` |   
  
### createRepository(String parent, Repository repository, String repositoryId)
    
    
    public final Repository createRepository(String parent, Repository repository, String repositoryId)

Creates a new Repository in a given project and location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DataformClient dataformClient = DataformClient.create()) {
       String parent = LocationName.of("[PROJECT]", "[LOCATION]").toString();
       Repository repository = Repository.newBuilder().build();
       String repositoryId = "repositoryId2113747461";
       Repository response = dataformClient.createRepository(parent, repository, repositoryId);
     }
     

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The location in which to create the repository. Must be in the format `projects/*/locations/*`.  
`repository` | `[Repository](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataform/latest/com.google.cloud.dataform.v1beta1.Repository)`  
Required. The repository to create.  
`repositoryId` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The ID to use for the repository, which will become the final component of the repository's resource name.  
**Returns**  
---  
**Type** | **Description**  
`[Repository](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataform/latest/com.google.cloud.dataform.v1beta1.Repository)` |   
  
### createRepositoryCallable()
    
    
    public final UnaryCallable<CreateRepositoryRequest,Repository> createRepositoryCallable()

Creates a new Repository in a given project and location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DataformClient dataformClient = DataformClient.create()) {
       CreateRepositoryRequest request =
           CreateRepositoryRequest.newBuilder()
               .setParent(LocationName.of("[PROJECT]", "[LOCATION]").toString())
               .setRepository(Repository.newBuilder().build())
               .setRepositoryId("repositoryId2113747461")
               .build();
       ApiFuture<Repository> future = dataformClient.createRepositoryCallable().futureCall(request);
       // Do something.
       Repository response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[CreateRepositoryRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataform/latest/com.google.cloud.dataform.v1beta1.CreateRepositoryRequest),[Repository](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataform/latest/com.google.cloud.dataform.v1beta1.Repository)>` |   
  
### createTeamFolder(@Nullable LocationName parent, TeamFolder teamFolder)
    
    
    public final TeamFolder createTeamFolder(@Nullable LocationName parent, TeamFolder teamFolder)

Creates a new TeamFolder in a given project and location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DataformClient dataformClient = DataformClient.create()) {
       LocationName parent = LocationName.of("[PROJECT]", "[LOCATION]");
       TeamFolder teamFolder = TeamFolder.newBuilder().build();
       TeamFolder response = dataformClient.createTeamFolder(parent, teamFolder);
     }
     

**Parameters**  
---  
**Name** | **Description**  
`parent` | `@org.jspecify.annotations.Nullable com.google.cloud.dataform.v1beta1.LocationName`  
Required. The location in which to create the TeamFolder. Must be in the format `projects/*/locations/*`.  
`teamFolder` | `[TeamFolder](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataform/latest/com.google.cloud.dataform.v1beta1.TeamFolder)`  
Required. The TeamFolder to create.  
**Returns**  
---  
**Type** | **Description**  
`[TeamFolder](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataform/latest/com.google.cloud.dataform.v1beta1.TeamFolder)` |   
  
### createTeamFolder(CreateTeamFolderRequest request)
    
    
    public final TeamFolder createTeamFolder(CreateTeamFolderRequest request)

Creates a new TeamFolder in a given project and location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DataformClient dataformClient = DataformClient.create()) {
       CreateTeamFolderRequest request =
           CreateTeamFolderRequest.newBuilder()
               .setParent(LocationName.of("[PROJECT]", "[LOCATION]").toString())
               .setTeamFolder(TeamFolder.newBuilder().build())
               .setTeamFolderId("teamFolderId18004902")
               .build();
       TeamFolder response = dataformClient.createTeamFolder(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[CreateTeamFolderRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataform/latest/com.google.cloud.dataform.v1beta1.CreateTeamFolderRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[TeamFolder](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataform/latest/com.google.cloud.dataform.v1beta1.TeamFolder)` |   
  
### createTeamFolder(String parent, TeamFolder teamFolder)
    
    
    public final TeamFolder createTeamFolder(String parent, TeamFolder teamFolder)

Creates a new TeamFolder in a given project and location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DataformClient dataformClient = DataformClient.create()) {
       String parent = LocationName.of("[PROJECT]", "[LOCATION]").toString();
       TeamFolder teamFolder = TeamFolder.newBuilder().build();
       TeamFolder response = dataformClient.createTeamFolder(parent, teamFolder);
     }
     

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The location in which to create the TeamFolder. Must be in the format `projects/*/locations/*`.  
`teamFolder` | `[TeamFolder](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataform/latest/com.google.cloud.dataform.v1beta1.TeamFolder)`  
Required. The TeamFolder to create.  
**Returns**  
---  
**Type** | **Description**  
`[TeamFolder](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataform/latest/com.google.cloud.dataform.v1beta1.TeamFolder)` |   
  
### createTeamFolderCallable()
    
    
    public final UnaryCallable<CreateTeamFolderRequest,TeamFolder> createTeamFolderCallable()

Creates a new TeamFolder in a given project and location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DataformClient dataformClient = DataformClient.create()) {
       CreateTeamFolderRequest request =
           CreateTeamFolderRequest.newBuilder()
               .setParent(LocationName.of("[PROJECT]", "[LOCATION]").toString())
               .setTeamFolder(TeamFolder.newBuilder().build())
               .setTeamFolderId("teamFolderId18004902")
               .build();
       ApiFuture<TeamFolder> future = dataformClient.createTeamFolderCallable().futureCall(request);
       // Do something.
       TeamFolder response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[CreateTeamFolderRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataform/latest/com.google.cloud.dataform.v1beta1.CreateTeamFolderRequest),[TeamFolder](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataform/latest/com.google.cloud.dataform.v1beta1.TeamFolder)>` |   
  
### createWorkflowConfig(@Nullable RepositoryName parent, WorkflowConfig workflowConfig, String workflowConfigId)
    
    
    public final WorkflowConfig createWorkflowConfig(@Nullable RepositoryName parent, WorkflowConfig workflowConfig, String workflowConfigId)

Creates a new WorkflowConfig in a given Repository.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DataformClient dataformClient = DataformClient.create()) {
       RepositoryName parent = RepositoryName.of("[PROJECT]", "[LOCATION]", "[REPOSITORY]");
       WorkflowConfig workflowConfig = WorkflowConfig.newBuilder().build();
       String workflowConfigId = "workflowConfigId-1331048228";
       WorkflowConfig response =
           dataformClient.createWorkflowConfig(parent, workflowConfig, workflowConfigId);
     }
     

**Parameters**  
---  
**Name** | **Description**  
`parent` | `@org.jspecify.annotations.Nullable com.google.cloud.dataform.v1beta1.RepositoryName`  
Required. The repository in which to create the workflow config. Must be in the format `projects/*/locations/*/repositories/*`.  
`workflowConfig` | `[WorkflowConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataform/latest/com.google.cloud.dataform.v1beta1.WorkflowConfig)`  
Required. The workflow config to create.  
`workflowConfigId` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The ID to use for the workflow config, which will become the final component of the workflow config's resource name.  
**Returns**  
---  
**Type** | **Description**  
`[WorkflowConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataform/latest/com.google.cloud.dataform.v1beta1.WorkflowConfig)` |   
  
### createWorkflowConfig(CreateWorkflowConfigRequest request)
    
    
    public final WorkflowConfig createWorkflowConfig(CreateWorkflowConfigRequest request)

Creates a new WorkflowConfig in a given Repository.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DataformClient dataformClient = DataformClient.create()) {
       CreateWorkflowConfigRequest request =
           CreateWorkflowConfigRequest.newBuilder()
               .setParent(RepositoryName.of("[PROJECT]", "[LOCATION]", "[REPOSITORY]").toString())
               .setWorkflowConfig(WorkflowConfig.newBuilder().build())
               .setWorkflowConfigId("workflowConfigId-1331048228")
               .build();
       WorkflowConfig response = dataformClient.createWorkflowConfig(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[CreateWorkflowConfigRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataform/latest/com.google.cloud.dataform.v1beta1.CreateWorkflowConfigRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[WorkflowConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataform/latest/com.google.cloud.dataform.v1beta1.WorkflowConfig)` |   
  
### createWorkflowConfig(String parent, WorkflowConfig workflowConfig, String workflowConfigId)
    
    
    public final WorkflowConfig createWorkflowConfig(String parent, WorkflowConfig workflowConfig, String workflowConfigId)

Creates a new WorkflowConfig in a given Repository.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DataformClient dataformClient = DataformClient.create()) {
       String parent = RepositoryName.of("[PROJECT]", "[LOCATION]", "[REPOSITORY]").toString();
       WorkflowConfig workflowConfig = WorkflowConfig.newBuilder().build();
       String workflowConfigId = "workflowConfigId-1331048228";
       WorkflowConfig response =
           dataformClient.createWorkflowConfig(parent, workflowConfig, workflowConfigId);
     }
     

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The repository in which to create the workflow config. Must be in the format `projects/*/locations/*/repositories/*`.  
`workflowConfig` | `[WorkflowConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataform/latest/com.google.cloud.dataform.v1beta1.WorkflowConfig)`  
Required. The workflow config to create.  
`workflowConfigId` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The ID to use for the workflow config, which will become the final component of the workflow config's resource name.  
**Returns**  
---  
**Type** | **Description**  
`[WorkflowConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataform/latest/com.google.cloud.dataform.v1beta1.WorkflowConfig)` |   
  
### createWorkflowConfigCallable()
    
    
    public final UnaryCallable<CreateWorkflowConfigRequest,WorkflowConfig> createWorkflowConfigCallable()

Creates a new WorkflowConfig in a given Repository.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DataformClient dataformClient = DataformClient.create()) {
       CreateWorkflowConfigRequest request =
           CreateWorkflowConfigRequest.newBuilder()
               .setParent(RepositoryName.of("[PROJECT]", "[LOCATION]", "[REPOSITORY]").toString())
               .setWorkflowConfig(WorkflowConfig.newBuilder().build())
               .setWorkflowConfigId("workflowConfigId-1331048228")
               .build();
       ApiFuture<WorkflowConfig> future =
           dataformClient.createWorkflowConfigCallable().futureCall(request);
       // Do something.
       WorkflowConfig response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[CreateWorkflowConfigRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataform/latest/com.google.cloud.dataform.v1beta1.CreateWorkflowConfigRequest),[WorkflowConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataform/latest/com.google.cloud.dataform.v1beta1.WorkflowConfig)>` |   
  
### createWorkflowInvocation(@Nullable RepositoryName parent, WorkflowInvocation workflowInvocation)
    
    
    public final WorkflowInvocation createWorkflowInvocation(@Nullable RepositoryName parent, WorkflowInvocation workflowInvocation)

Creates a new WorkflowInvocation in a given Repository.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DataformClient dataformClient = DataformClient.create()) {
       RepositoryName parent = RepositoryName.of("[PROJECT]", "[LOCATION]", "[REPOSITORY]");
       WorkflowInvocation workflowInvocation = WorkflowInvocation.newBuilder().build();
       WorkflowInvocation response =
           dataformClient.createWorkflowInvocation(parent, workflowInvocation);
     }
     

**Parameters**  
---  
**Name** | **Description**  
`parent` | `@org.jspecify.annotations.Nullable com.google.cloud.dataform.v1beta1.RepositoryName`  
Required. The repository in which to create the workflow invocation. Must be in the format `projects/*/locations/*/repositories/*`.  
`workflowInvocation` | `[WorkflowInvocation](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataform/latest/com.google.cloud.dataform.v1beta1.WorkflowInvocation)`  
Required. The workflow invocation resource to create.  
**Returns**  
---  
**Type** | **Description**  
`[WorkflowInvocation](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataform/latest/com.google.cloud.dataform.v1beta1.WorkflowInvocation)` |   
  
### createWorkflowInvocation(CreateWorkflowInvocationRequest request)
    
    
    public final WorkflowInvocation createWorkflowInvocation(CreateWorkflowInvocationRequest request)

Creates a new WorkflowInvocation in a given Repository.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DataformClient dataformClient = DataformClient.create()) {
       CreateWorkflowInvocationRequest request =
           CreateWorkflowInvocationRequest.newBuilder()
               .setParent(RepositoryName.of("[PROJECT]", "[LOCATION]", "[REPOSITORY]").toString())
               .setWorkflowInvocation(WorkflowInvocation.newBuilder().build())
               .build();
       WorkflowInvocation response = dataformClient.createWorkflowInvocation(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[CreateWorkflowInvocationRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataform/latest/com.google.cloud.dataform.v1beta1.CreateWorkflowInvocationRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[WorkflowInvocation](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataform/latest/com.google.cloud.dataform.v1beta1.WorkflowInvocation)` |   
  
### createWorkflowInvocation(String parent, WorkflowInvocation workflowInvocation)
    
    
    public final WorkflowInvocation createWorkflowInvocation(String parent, WorkflowInvocation workflowInvocation)

Creates a new WorkflowInvocation in a given Repository.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DataformClient dataformClient = DataformClient.create()) {
       String parent = RepositoryName.of("[PROJECT]", "[LOCATION]", "[REPOSITORY]").toString();
       WorkflowInvocation workflowInvocation = WorkflowInvocation.newBuilder().build();
       WorkflowInvocation response =
           dataformClient.createWorkflowInvocation(parent, workflowInvocation);
     }
     

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The repository in which to create the workflow invocation. Must be in the format `projects/*/locations/*/repositories/*`.  
`workflowInvocation` | `[WorkflowInvocation](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataform/latest/com.google.cloud.dataform.v1beta1.WorkflowInvocation)`  
Required. The workflow invocation resource to create.  
**Returns**  
---  
**Type** | **Description**  
`[WorkflowInvocation](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataform/latest/com.google.cloud.dataform.v1beta1.WorkflowInvocation)` |   
  
### createWorkflowInvocationCallable()
    
    
    public final UnaryCallable<CreateWorkflowInvocationRequest,WorkflowInvocation> createWorkflowInvocationCallable()

Creates a new WorkflowInvocation in a given Repository.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DataformClient dataformClient = DataformClient.create()) {
       CreateWorkflowInvocationRequest request =
           CreateWorkflowInvocationRequest.newBuilder()
               .setParent(RepositoryName.of("[PROJECT]", "[LOCATION]", "[REPOSITORY]").toString())
               .setWorkflowInvocation(WorkflowInvocation.newBuilder().build())
               .build();
       ApiFuture<WorkflowInvocation> future =
           dataformClient.createWorkflowInvocationCallable().futureCall(request);
       // Do something.
       WorkflowInvocation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[CreateWorkflowInvocationRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataform/latest/com.google.cloud.dataform.v1beta1.CreateWorkflowInvocationRequest),[WorkflowInvocation](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataform/latest/com.google.cloud.dataform.v1beta1.WorkflowInvocation)>` |   
  
### createWorkspace(@Nullable RepositoryName parent, Workspace workspace, String workspaceId)
    
    
    public final Workspace createWorkspace(@Nullable RepositoryName parent, Workspace workspace, String workspaceId)

Creates a new Workspace in a given Repository.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DataformClient dataformClient = DataformClient.create()) {
       RepositoryName parent = RepositoryName.of("[PROJECT]", "[LOCATION]", "[REPOSITORY]");
       Workspace workspace = Workspace.newBuilder().build();
       String workspaceId = "workspaceId466560144";
       Workspace response = dataformClient.createWorkspace(parent, workspace, workspaceId);
     }
     

**Parameters**  
---  
**Name** | **Description**  
`parent` | `@org.jspecify.annotations.Nullable com.google.cloud.dataform.v1beta1.RepositoryName`  
Required. The repository in which to create the workspace. Must be in the format `projects/*/locations/*/repositories/*`.  
`workspace` | `[Workspace](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataform/latest/com.google.cloud.dataform.v1beta1.Workspace)`  
Required. The workspace to create.  
`workspaceId` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The ID to use for the workspace, which will become the final component of the workspace's resource name.  
**Returns**  
---  
**Type** | **Description**  
`[Workspace](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataform/latest/com.google.cloud.dataform.v1beta1.Workspace)` |   
  
### createWorkspace(CreateWorkspaceRequest request)
    
    
    public final Workspace createWorkspace(CreateWorkspaceRequest request)

Creates a new Workspace in a given Repository.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DataformClient dataformClient = DataformClient.create()) {
       CreateWorkspaceRequest request =
           CreateWorkspaceRequest.newBuilder()
               .setParent(RepositoryName.of("[PROJECT]", "[LOCATION]", "[REPOSITORY]").toString())
               .setWorkspace(Workspace.newBuilder().build())
               .setWorkspaceId("workspaceId466560144")
               .build();
       Workspace response = dataformClient.createWorkspace(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[CreateWorkspaceRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataform/latest/com.google.cloud.dataform.v1beta1.CreateWorkspaceRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[Workspace](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataform/latest/com.google.cloud.dataform.v1beta1.Workspace)` |   
  
### createWorkspace(String parent, Workspace workspace, String workspaceId)
    
    
    public final Workspace createWorkspace(String parent, Workspace workspace, String workspaceId)

Creates a new Workspace in a given Repository.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DataformClient dataformClient = DataformClient.create()) {
       String parent = RepositoryName.of("[PROJECT]", "[LOCATION]", "[REPOSITORY]").toString();
       Workspace workspace = Workspace.newBuilder().build();
       String workspaceId = "workspaceId466560144";
       Workspace response = dataformClient.createWorkspace(parent, workspace, workspaceId);
     }
     

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The repository in which to create the workspace. Must be in the format `projects/*/locations/*/repositories/*`.  
`workspace` | `[Workspace](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataform/latest/com.google.cloud.dataform.v1beta1.Workspace)`  
Required. The workspace to create.  
`workspaceId` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The ID to use for the workspace, which will become the final component of the workspace's resource name.  
**Returns**  
---  
**Type** | **Description**  
`[Workspace](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataform/latest/com.google.cloud.dataform.v1beta1.Workspace)` |   
  
### createWorkspaceCallable()
    
    
    public final UnaryCallable<CreateWorkspaceRequest,Workspace> createWorkspaceCallable()

Creates a new Workspace in a given Repository.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DataformClient dataformClient = DataformClient.create()) {
       CreateWorkspaceRequest request =
           CreateWorkspaceRequest.newBuilder()
               .setParent(RepositoryName.of("[PROJECT]", "[LOCATION]", "[REPOSITORY]").toString())
               .setWorkspace(Workspace.newBuilder().build())
               .setWorkspaceId("workspaceId466560144")
               .build();
       ApiFuture<Workspace> future = dataformClient.createWorkspaceCallable().futureCall(request);
       // Do something.
       Workspace response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[CreateWorkspaceRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataform/latest/com.google.cloud.dataform.v1beta1.CreateWorkspaceRequest),[Workspace](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataform/latest/com.google.cloud.dataform.v1beta1.Workspace)>` |   
  
### deleteBranch(DeleteBranchRequest request)
    
    
    public final DeleteBranchResponse deleteBranch(DeleteBranchRequest request)

Deletes a branch in a Workspace.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DataformClient dataformClient = DataformClient.create()) {
       DeleteBranchRequest request =
           DeleteBranchRequest.newBuilder()
               .setName(
                   WorkspaceName.of("[PROJECT]", "[LOCATION]", "[REPOSITORY]", "[WORKSPACE]")
                       .toString())
               .setBranch("branch-1381030494")
               .setForce(true)
               .build();
       DeleteBranchResponse response = dataformClient.deleteBranch(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[DeleteBranchRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataform/latest/com.google.cloud.dataform.v1beta1.DeleteBranchRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[DeleteBranchResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataform/latest/com.google.cloud.dataform.v1beta1.DeleteBranchResponse)` |   
  
### deleteBranchCallable()
    
    
    public final UnaryCallable<DeleteBranchRequest,DeleteBranchResponse> deleteBranchCallable()

Deletes a branch in a Workspace.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DataformClient dataformClient = DataformClient.create()) {
       DeleteBranchRequest request =
           DeleteBranchRequest.newBuilder()
               .setName(
                   WorkspaceName.of("[PROJECT]", "[LOCATION]", "[REPOSITORY]", "[WORKSPACE]")
                       .toString())
               .setBranch("branch-1381030494")
               .setForce(true)
               .build();
       ApiFuture<DeleteBranchResponse> future =
           dataformClient.deleteBranchCallable().futureCall(request);
       // Do something.
       DeleteBranchResponse response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[DeleteBranchRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataform/latest/com.google.cloud.dataform.v1beta1.DeleteBranchRequest),[DeleteBranchResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataform/latest/com.google.cloud.dataform.v1beta1.DeleteBranchResponse)>` |   
  
### deleteFolder(@Nullable FolderName name)
    
    
    public final void deleteFolder(@Nullable FolderName name)

Deletes a single Folder.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DataformClient dataformClient = DataformClient.create()) {
       FolderName name = FolderName.of("[PROJECT]", "[LOCATION]", "[FOLDER]");
       dataformClient.deleteFolder(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `@org.jspecify.annotations.Nullable com.google.cloud.dataform.v1beta1.FolderName`  
Required. The Folder's name.  
  
### deleteFolder(DeleteFolderRequest request)
    
    
    public final void deleteFolder(DeleteFolderRequest request)

Deletes a single Folder.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DataformClient dataformClient = DataformClient.create()) {
       DeleteFolderRequest request =
           DeleteFolderRequest.newBuilder()
               .setName(FolderName.of("[PROJECT]", "[LOCATION]", "[FOLDER]").toString())
               .build();
       dataformClient.deleteFolder(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[DeleteFolderRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataform/latest/com.google.cloud.dataform.v1beta1.DeleteFolderRequest)`  
The request object containing all of the parameters for the API call.  
  
### deleteFolder(String name)
    
    
    public final void deleteFolder(String name)

Deletes a single Folder.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DataformClient dataformClient = DataformClient.create()) {
       String name = FolderName.of("[PROJECT]", "[LOCATION]", "[FOLDER]").toString();
       dataformClient.deleteFolder(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The Folder's name.  
  
### deleteFolderCallable()
    
    
    public final UnaryCallable<DeleteFolderRequest,Empty> deleteFolderCallable()

Deletes a single Folder.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DataformClient dataformClient = DataformClient.create()) {
       DeleteFolderRequest request =
           DeleteFolderRequest.newBuilder()
               .setName(FolderName.of("[PROJECT]", "[LOCATION]", "[FOLDER]").toString())
               .build();
       ApiFuture<Empty> future = dataformClient.deleteFolderCallable().futureCall(request);
       // Do something.
       future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[DeleteFolderRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataform/latest/com.google.cloud.dataform.v1beta1.DeleteFolderRequest),[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html)>` |   
  
### deleteFolderTreeAsync(@Nullable FolderName name, boolean force)
    
    
    public final OperationFuture<Empty,DeleteFolderTreeMetadata> deleteFolderTreeAsync(@Nullable FolderName name, boolean force)

Deletes a Folder with its contents (Folders, Repositories, Workspaces, ReleaseConfigs, and WorkflowConfigs).

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DataformClient dataformClient = DataformClient.create()) {
       FolderName name = FolderName.of("[PROJECT]", "[LOCATION]", "[FOLDER]");
       boolean force = true;
       dataformClient.deleteFolderTreeAsync(name, force).get();
     }
     

**Parameters**  
---  
**Name** | **Description**  
`name` | `@org.jspecify.annotations.Nullable com.google.cloud.dataform.v1beta1.FolderName`  
Required. The Folder's name. Format: projects/{project}/locations/{location}/folders/{folder}  
`force` | `[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
Optional. If `false` (default): The operation will fail if any Repository within the folder hierarchy has associated Release Configs or Workflow Configs. If `true`: The operation will attempt to delete everything, including any Release Configs and Workflow Configs linked to Repositories within the folder hierarchy. This permanently removes schedules and resources.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html),[DeleteFolderTreeMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataform/latest/com.google.cloud.dataform.v1beta1.DeleteFolderTreeMetadata)>` |   
  
### deleteFolderTreeAsync(DeleteFolderTreeRequest request)
    
    
    public final OperationFuture<Empty,DeleteFolderTreeMetadata> deleteFolderTreeAsync(DeleteFolderTreeRequest request)

Deletes a Folder with its contents (Folders, Repositories, Workspaces, ReleaseConfigs, and WorkflowConfigs).

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DataformClient dataformClient = DataformClient.create()) {
       DeleteFolderTreeRequest request =
           DeleteFolderTreeRequest.newBuilder()
               .setName(FolderName.of("[PROJECT]", "[LOCATION]", "[FOLDER]").toString())
               .setForce(true)
               .build();
       dataformClient.deleteFolderTreeAsync(request).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[DeleteFolderTreeRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataform/latest/com.google.cloud.dataform.v1beta1.DeleteFolderTreeRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html),[DeleteFolderTreeMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataform/latest/com.google.cloud.dataform.v1beta1.DeleteFolderTreeMetadata)>` |   
  
### deleteFolderTreeAsync(String name, boolean force)
    
    
    public final OperationFuture<Empty,DeleteFolderTreeMetadata> deleteFolderTreeAsync(String name, boolean force)

Deletes a Folder with its contents (Folders, Repositories, Workspaces, ReleaseConfigs, and WorkflowConfigs).

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DataformClient dataformClient = DataformClient.create()) {
       String name = FolderName.of("[PROJECT]", "[LOCATION]", "[FOLDER]").toString();
       boolean force = true;
       dataformClient.deleteFolderTreeAsync(name, force).get();
     }
     

**Parameters**  
---  
**Name** | **Description**  
`name` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The Folder's name. Format: projects/{project}/locations/{location}/folders/{folder}  
`force` | `[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
Optional. If `false` (default): The operation will fail if any Repository within the folder hierarchy has associated Release Configs or Workflow Configs. If `true`: The operation will attempt to delete everything, including any Release Configs and Workflow Configs linked to Repositories within the folder hierarchy. This permanently removes schedules and resources.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html),[DeleteFolderTreeMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataform/latest/com.google.cloud.dataform.v1beta1.DeleteFolderTreeMetadata)>` |   
  
### deleteFolderTreeCallable()
    
    
    public final UnaryCallable<DeleteFolderTreeRequest,Operation> deleteFolderTreeCallable()

Deletes a Folder with its contents (Folders, Repositories, Workspaces, ReleaseConfigs, and WorkflowConfigs).

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DataformClient dataformClient = DataformClient.create()) {
       DeleteFolderTreeRequest request =
           DeleteFolderTreeRequest.newBuilder()
               .setName(FolderName.of("[PROJECT]", "[LOCATION]", "[FOLDER]").toString())
               .setForce(true)
               .build();
       ApiFuture<Operation> future = dataformClient.deleteFolderTreeCallable().futureCall(request);
       // Do something.
       future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[DeleteFolderTreeRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataform/latest/com.google.cloud.dataform.v1beta1.DeleteFolderTreeRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### deleteFolderTreeOperationCallable()
    
    
    public final OperationCallable<DeleteFolderTreeRequest,Empty,DeleteFolderTreeMetadata> deleteFolderTreeOperationCallable()

Deletes a Folder with its contents (Folders, Repositories, Workspaces, ReleaseConfigs, and WorkflowConfigs).

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DataformClient dataformClient = DataformClient.create()) {
       DeleteFolderTreeRequest request =
           DeleteFolderTreeRequest.newBuilder()
               .setName(FolderName.of("[PROJECT]", "[LOCATION]", "[FOLDER]").toString())
               .setForce(true)
               .build();
       OperationFuture<Empty, DeleteFolderTreeMetadata> future =
           dataformClient.deleteFolderTreeOperationCallable().futureCall(request);
       // Do something.
       future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[OperationCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallable.html)<[DeleteFolderTreeRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataform/latest/com.google.cloud.dataform.v1beta1.DeleteFolderTreeRequest),[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html),[DeleteFolderTreeMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataform/latest/com.google.cloud.dataform.v1beta1.DeleteFolderTreeMetadata)>` |   
  
### deleteReleaseConfig(@Nullable ReleaseConfigName name)
    
    
    public final void deleteReleaseConfig(@Nullable ReleaseConfigName name)

Deletes a single ReleaseConfig.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DataformClient dataformClient = DataformClient.create()) {
       ReleaseConfigName name =
           ReleaseConfigName.of("[PROJECT]", "[LOCATION]", "[REPOSITORY]", "[RELEASE_CONFIG]");
       dataformClient.deleteReleaseConfig(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `@org.jspecify.annotations.Nullable com.google.cloud.dataform.v1beta1.ReleaseConfigName`  
Required. The release config's name.  
  
### deleteReleaseConfig(DeleteReleaseConfigRequest request)
    
    
    public final void deleteReleaseConfig(DeleteReleaseConfigRequest request)

Deletes a single ReleaseConfig.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DataformClient dataformClient = DataformClient.create()) {
       DeleteReleaseConfigRequest request =
           DeleteReleaseConfigRequest.newBuilder()
               .setName(
                   ReleaseConfigName.of(
                           "[PROJECT]", "[LOCATION]", "[REPOSITORY]", "[RELEASE_CONFIG]")
                       .toString())
               .build();
       dataformClient.deleteReleaseConfig(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[DeleteReleaseConfigRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataform/latest/com.google.cloud.dataform.v1beta1.DeleteReleaseConfigRequest)`  
The request object containing all of the parameters for the API call.  
  
### deleteReleaseConfig(String name)
    
    
    public final void deleteReleaseConfig(String name)

Deletes a single ReleaseConfig.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DataformClient dataformClient = DataformClient.create()) {
       String name =
           ReleaseConfigName.of("[PROJECT]", "[LOCATION]", "[REPOSITORY]", "[RELEASE_CONFIG]")
               .toString();
       dataformClient.deleteReleaseConfig(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The release config's name.  
  
### deleteReleaseConfigCallable()
    
    
    public final UnaryCallable<DeleteReleaseConfigRequest,Empty> deleteReleaseConfigCallable()

Deletes a single ReleaseConfig.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DataformClient dataformClient = DataformClient.create()) {
       DeleteReleaseConfigRequest request =
           DeleteReleaseConfigRequest.newBuilder()
               .setName(
                   ReleaseConfigName.of(
                           "[PROJECT]", "[LOCATION]", "[REPOSITORY]", "[RELEASE_CONFIG]")
                       .toString())
               .build();
       ApiFuture<Empty> future = dataformClient.deleteReleaseConfigCallable().futureCall(request);
       // Do something.
       future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[DeleteReleaseConfigRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataform/latest/com.google.cloud.dataform.v1beta1.DeleteReleaseConfigRequest),[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html)>` |   
  
### deleteRepository(@Nullable RepositoryName name)
    
    
    public final void deleteRepository(@Nullable RepositoryName name)

Deletes a single Repository.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DataformClient dataformClient = DataformClient.create()) {
       RepositoryName name = RepositoryName.of("[PROJECT]", "[LOCATION]", "[REPOSITORY]");
       dataformClient.deleteRepository(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `@org.jspecify.annotations.Nullable com.google.cloud.dataform.v1beta1.RepositoryName`  
Required. The repository's name.  
  
### deleteRepository(DeleteRepositoryRequest request)
    
    
    public final void deleteRepository(DeleteRepositoryRequest request)

Deletes a single Repository.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DataformClient dataformClient = DataformClient.create()) {
       DeleteRepositoryRequest request =
           DeleteRepositoryRequest.newBuilder()
               .setName(RepositoryName.of("[PROJECT]", "[LOCATION]", "[REPOSITORY]").toString())
               .setForce(true)
               .build();
       dataformClient.deleteRepository(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[DeleteRepositoryRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataform/latest/com.google.cloud.dataform.v1beta1.DeleteRepositoryRequest)`  
The request object containing all of the parameters for the API call.  
  
### deleteRepository(String name)
    
    
    public final void deleteRepository(String name)

Deletes a single Repository.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DataformClient dataformClient = DataformClient.create()) {
       String name = RepositoryName.of("[PROJECT]", "[LOCATION]", "[REPOSITORY]").toString();
       dataformClient.deleteRepository(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The repository's name.  
  
### deleteRepositoryCallable()
    
    
    public final UnaryCallable<DeleteRepositoryRequest,Empty> deleteRepositoryCallable()

Deletes a single Repository.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DataformClient dataformClient = DataformClient.create()) {
       DeleteRepositoryRequest request =
           DeleteRepositoryRequest.newBuilder()
               .setName(RepositoryName.of("[PROJECT]", "[LOCATION]", "[REPOSITORY]").toString())
               .setForce(true)
               .build();
       ApiFuture<Empty> future = dataformClient.deleteRepositoryCallable().futureCall(request);
       // Do something.
       future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[DeleteRepositoryRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataform/latest/com.google.cloud.dataform.v1beta1.DeleteRepositoryRequest),[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html)>` |   
  
### deleteRepositoryLongRunningAsync(@Nullable RepositoryName name, boolean force)
    
    
    public final OperationFuture<DeleteRepositoryLongRunningResponse,DeleteRepositoryLongRunningMetadata> deleteRepositoryLongRunningAsync(@Nullable RepositoryName name, boolean force)

Deletes a single repository asynchronously.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DataformClient dataformClient = DataformClient.create()) {
       RepositoryName name = RepositoryName.of("[PROJECT]", "[LOCATION]", "[REPOSITORY]");
       boolean force = true;
       DeleteRepositoryLongRunningResponse response =
           dataformClient.deleteRepositoryLongRunningAsync(name, force).get();
     }
     

**Parameters**  
---  
**Name** | **Description**  
`name` | `@org.jspecify.annotations.Nullable com.google.cloud.dataform.v1beta1.RepositoryName`  
Required. The repository's name.  
`force` | `[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
Optional. If set to true, child resources of this repository (compilation results and workflow invocations) will also be deleted. Otherwise, the request will only succeed if the repository has no child resources. **Note:** *This flag doesn't support deletion of workspaces, release configs or workflow configs. If any of such resources exists in the repository, the request will fail.*  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[DeleteRepositoryLongRunningResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataform/latest/com.google.cloud.dataform.v1beta1.DeleteRepositoryLongRunningResponse),[DeleteRepositoryLongRunningMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataform/latest/com.google.cloud.dataform.v1beta1.DeleteRepositoryLongRunningMetadata)>` |   
  
### deleteRepositoryLongRunningAsync(DeleteRepositoryLongRunningRequest request)
    
    
    public final OperationFuture<DeleteRepositoryLongRunningResponse,DeleteRepositoryLongRunningMetadata> deleteRepositoryLongRunningAsync(DeleteRepositoryLongRunningRequest request)

Deletes a single repository asynchronously.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DataformClient dataformClient = DataformClient.create()) {
       DeleteRepositoryLongRunningRequest request =
           DeleteRepositoryLongRunningRequest.newBuilder()
               .setName(RepositoryName.of("[PROJECT]", "[LOCATION]", "[REPOSITORY]").toString())
               .setForce(true)
               .build();
       DeleteRepositoryLongRunningResponse response =
           dataformClient.deleteRepositoryLongRunningAsync(request).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[DeleteRepositoryLongRunningRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataform/latest/com.google.cloud.dataform.v1beta1.DeleteRepositoryLongRunningRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[DeleteRepositoryLongRunningResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataform/latest/com.google.cloud.dataform.v1beta1.DeleteRepositoryLongRunningResponse),[DeleteRepositoryLongRunningMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataform/latest/com.google.cloud.dataform.v1beta1.DeleteRepositoryLongRunningMetadata)>` |   
  
### deleteRepositoryLongRunningAsync(String name, boolean force)
    
    
    public final OperationFuture<DeleteRepositoryLongRunningResponse,DeleteRepositoryLongRunningMetadata> deleteRepositoryLongRunningAsync(String name, boolean force)

Deletes a single repository asynchronously.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DataformClient dataformClient = DataformClient.create()) {
       String name = RepositoryName.of("[PROJECT]", "[LOCATION]", "[REPOSITORY]").toString();
       boolean force = true;
       DeleteRepositoryLongRunningResponse response =
           dataformClient.deleteRepositoryLongRunningAsync(name, force).get();
     }
     

**Parameters**  
---  
**Name** | **Description**  
`name` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The repository's name.  
`force` | `[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
Optional. If set to true, child resources of this repository (compilation results and workflow invocations) will also be deleted. Otherwise, the request will only succeed if the repository has no child resources. **Note:** *This flag doesn't support deletion of workspaces, release configs or workflow configs. If any of such resources exists in the repository, the request will fail.*  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[DeleteRepositoryLongRunningResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataform/latest/com.google.cloud.dataform.v1beta1.DeleteRepositoryLongRunningResponse),[DeleteRepositoryLongRunningMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataform/latest/com.google.cloud.dataform.v1beta1.DeleteRepositoryLongRunningMetadata)>` |   
  
### deleteRepositoryLongRunningCallable()
    
    
    public final UnaryCallable<DeleteRepositoryLongRunningRequest,Operation> deleteRepositoryLongRunningCallable()

Deletes a single repository asynchronously.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DataformClient dataformClient = DataformClient.create()) {
       DeleteRepositoryLongRunningRequest request =
           DeleteRepositoryLongRunningRequest.newBuilder()
               .setName(RepositoryName.of("[PROJECT]", "[LOCATION]", "[REPOSITORY]").toString())
               .setForce(true)
               .build();
       ApiFuture<Operation> future =
           dataformClient.deleteRepositoryLongRunningCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[DeleteRepositoryLongRunningRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataform/latest/com.google.cloud.dataform.v1beta1.DeleteRepositoryLongRunningRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### deleteRepositoryLongRunningOperationCallable()
    
    
    public final OperationCallable<DeleteRepositoryLongRunningRequest,DeleteRepositoryLongRunningResponse,DeleteRepositoryLongRunningMetadata> deleteRepositoryLongRunningOperationCallable()

Deletes a single repository asynchronously.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DataformClient dataformClient = DataformClient.create()) {
       DeleteRepositoryLongRunningRequest request =
           DeleteRepositoryLongRunningRequest.newBuilder()
               .setName(RepositoryName.of("[PROJECT]", "[LOCATION]", "[REPOSITORY]").toString())
               .setForce(true)
               .build();
       OperationFuture<DeleteRepositoryLongRunningResponse, DeleteRepositoryLongRunningMetadata>
           future =
               dataformClient.deleteRepositoryLongRunningOperationCallable().futureCall(request);
       // Do something.
       DeleteRepositoryLongRunningResponse response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[OperationCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallable.html)<[DeleteRepositoryLongRunningRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataform/latest/com.google.cloud.dataform.v1beta1.DeleteRepositoryLongRunningRequest),[DeleteRepositoryLongRunningResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataform/latest/com.google.cloud.dataform.v1beta1.DeleteRepositoryLongRunningResponse),[DeleteRepositoryLongRunningMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataform/latest/com.google.cloud.dataform.v1beta1.DeleteRepositoryLongRunningMetadata)>` |   
  
### deleteTeamFolder(@Nullable TeamFolderName name)
    
    
    public final void deleteTeamFolder(@Nullable TeamFolderName name)

Deletes a single TeamFolder.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DataformClient dataformClient = DataformClient.create()) {
       TeamFolderName name = TeamFolderName.of("[PROJECT]", "[LOCATION]", "[TEAM_FOLDER]");
       dataformClient.deleteTeamFolder(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `@org.jspecify.annotations.Nullable com.google.cloud.dataform.v1beta1.TeamFolderName`  
Required. The TeamFolder's name.  
  
### deleteTeamFolder(DeleteTeamFolderRequest request)
    
    
    public final void deleteTeamFolder(DeleteTeamFolderRequest request)

Deletes a single TeamFolder.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DataformClient dataformClient = DataformClient.create()) {
       DeleteTeamFolderRequest request =
           DeleteTeamFolderRequest.newBuilder()
               .setName(TeamFolderName.of("[PROJECT]", "[LOCATION]", "[TEAM_FOLDER]").toString())
               .build();
       dataformClient.deleteTeamFolder(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[DeleteTeamFolderRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataform/latest/com.google.cloud.dataform.v1beta1.DeleteTeamFolderRequest)`  
The request object containing all of the parameters for the API call.  
  
### deleteTeamFolder(String name)
    
    
    public final void deleteTeamFolder(String name)

Deletes a single TeamFolder.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DataformClient dataformClient = DataformClient.create()) {
       String name = TeamFolderName.of("[PROJECT]", "[LOCATION]", "[TEAM_FOLDER]").toString();
       dataformClient.deleteTeamFolder(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The TeamFolder's name.  
  
### deleteTeamFolderCallable()
    
    
    public final UnaryCallable<DeleteTeamFolderRequest,Empty> deleteTeamFolderCallable()

Deletes a single TeamFolder.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DataformClient dataformClient = DataformClient.create()) {
       DeleteTeamFolderRequest request =
           DeleteTeamFolderRequest.newBuilder()
               .setName(TeamFolderName.of("[PROJECT]", "[LOCATION]", "[TEAM_FOLDER]").toString())
               .build();
       ApiFuture<Empty> future = dataformClient.deleteTeamFolderCallable().futureCall(request);
       // Do something.
       future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[DeleteTeamFolderRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataform/latest/com.google.cloud.dataform.v1beta1.DeleteTeamFolderRequest),[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html)>` |   
  
### deleteTeamFolderTreeAsync(@Nullable TeamFolderName name, boolean force)
    
    
    public final OperationFuture<Empty,DeleteFolderTreeMetadata> deleteTeamFolderTreeAsync(@Nullable TeamFolderName name, boolean force)

Deletes a TeamFolder with its contents (Folders, Repositories, Workspaces, ReleaseConfigs, and WorkflowConfigs).

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DataformClient dataformClient = DataformClient.create()) {
       TeamFolderName name = TeamFolderName.of("[PROJECT]", "[LOCATION]", "[TEAM_FOLDER]");
       boolean force = true;
       dataformClient.deleteTeamFolderTreeAsync(name, force).get();
     }
     

**Parameters**  
---  
**Name** | **Description**  
`name` | `@org.jspecify.annotations.Nullable com.google.cloud.dataform.v1beta1.TeamFolderName`  
Required. The TeamFolder's name. Format: projects/{project}/locations/{location}/teamFolders/{team_folder}  
`force` | `[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
Optional. If `false` (default): The operation will fail if any Repository within the folder hierarchy has associated Release Configs or Workflow Configs. If `true`: The operation will attempt to delete everything, including any Release Configs and Workflow Configs linked to Repositories within the folder hierarchy. This permanently removes schedules and resources.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html),[DeleteFolderTreeMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataform/latest/com.google.cloud.dataform.v1beta1.DeleteFolderTreeMetadata)>` |   
  
### deleteTeamFolderTreeAsync(DeleteTeamFolderTreeRequest request)
    
    
    public final OperationFuture<Empty,DeleteFolderTreeMetadata> deleteTeamFolderTreeAsync(DeleteTeamFolderTreeRequest request)

Deletes a TeamFolder with its contents (Folders, Repositories, Workspaces, ReleaseConfigs, and WorkflowConfigs).

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DataformClient dataformClient = DataformClient.create()) {
       DeleteTeamFolderTreeRequest request =
           DeleteTeamFolderTreeRequest.newBuilder()
               .setName(TeamFolderName.of("[PROJECT]", "[LOCATION]", "[TEAM_FOLDER]").toString())
               .setForce(true)
               .build();
       dataformClient.deleteTeamFolderTreeAsync(request).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[DeleteTeamFolderTreeRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataform/latest/com.google.cloud.dataform.v1beta1.DeleteTeamFolderTreeRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html),[DeleteFolderTreeMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataform/latest/com.google.cloud.dataform.v1beta1.DeleteFolderTreeMetadata)>` |   
  
### deleteTeamFolderTreeAsync(String name, boolean force)
    
    
    public final OperationFuture<Empty,DeleteFolderTreeMetadata> deleteTeamFolderTreeAsync(String name, boolean force)

Deletes a TeamFolder with its contents (Folders, Repositories, Workspaces, ReleaseConfigs, and WorkflowConfigs).

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DataformClient dataformClient = DataformClient.create()) {
       String name = TeamFolderName.of("[PROJECT]", "[LOCATION]", "[TEAM_FOLDER]").toString();
       boolean force = true;
       dataformClient.deleteTeamFolderTreeAsync(name, force).get();
     }
     

**Parameters**  
---  
**Name** | **Description**  
`name` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The TeamFolder's name. Format: projects/{project}/locations/{location}/teamFolders/{team_folder}  
`force` | `[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
Optional. If `false` (default): The operation will fail if any Repository within the folder hierarchy has associated Release Configs or Workflow Configs. If `true`: The operation will attempt to delete everything, including any Release Configs and Workflow Configs linked to Repositories within the folder hierarchy. This permanently removes schedules and resources.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html),[DeleteFolderTreeMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataform/latest/com.google.cloud.dataform.v1beta1.DeleteFolderTreeMetadata)>` |   
  
### deleteTeamFolderTreeCallable()
    
    
    public final UnaryCallable<DeleteTeamFolderTreeRequest,Operation> deleteTeamFolderTreeCallable()

Deletes a TeamFolder with its contents (Folders, Repositories, Workspaces, ReleaseConfigs, and WorkflowConfigs).

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DataformClient dataformClient = DataformClient.create()) {
       DeleteTeamFolderTreeRequest request =
           DeleteTeamFolderTreeRequest.newBuilder()
               .setName(TeamFolderName.of("[PROJECT]", "[LOCATION]", "[TEAM_FOLDER]").toString())
               .setForce(true)
               .build();
       ApiFuture<Operation> future =
           dataformClient.deleteTeamFolderTreeCallable().futureCall(request);
       // Do something.
       future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[DeleteTeamFolderTreeRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataform/latest/com.google.cloud.dataform.v1beta1.DeleteTeamFolderTreeRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### deleteTeamFolderTreeOperationCallable()
    
    
    public final OperationCallable<DeleteTeamFolderTreeRequest,Empty,DeleteFolderTreeMetadata> deleteTeamFolderTreeOperationCallable()

Deletes a TeamFolder with its contents (Folders, Repositories, Workspaces, ReleaseConfigs, and WorkflowConfigs).

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DataformClient dataformClient = DataformClient.create()) {
       DeleteTeamFolderTreeRequest request =
           DeleteTeamFolderTreeRequest.newBuilder()
               .setName(TeamFolderName.of("[PROJECT]", "[LOCATION]", "[TEAM_FOLDER]").toString())
               .setForce(true)
               .build();
       OperationFuture<Empty, DeleteFolderTreeMetadata> future =
           dataformClient.deleteTeamFolderTreeOperationCallable().futureCall(request);
       // Do something.
       future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[OperationCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallable.html)<[DeleteTeamFolderTreeRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataform/latest/com.google.cloud.dataform.v1beta1.DeleteTeamFolderTreeRequest),[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html),[DeleteFolderTreeMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataform/latest/com.google.cloud.dataform.v1beta1.DeleteFolderTreeMetadata)>` |   
  
### deleteWorkflowConfig(@Nullable WorkflowConfigName name)
    
    
    public final void deleteWorkflowConfig(@Nullable WorkflowConfigName name)

Deletes a single WorkflowConfig.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DataformClient dataformClient = DataformClient.create()) {
       WorkflowConfigName name =
           WorkflowConfigName.of("[PROJECT]", "[LOCATION]", "[REPOSITORY]", "[WORKFLOW_CONFIG]");
       dataformClient.deleteWorkflowConfig(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `@org.jspecify.annotations.Nullable com.google.cloud.dataform.v1beta1.WorkflowConfigName`  
Required. The workflow config's name.  
  
### deleteWorkflowConfig(DeleteWorkflowConfigRequest request)
    
    
    public final void deleteWorkflowConfig(DeleteWorkflowConfigRequest request)

Deletes a single WorkflowConfig.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DataformClient dataformClient = DataformClient.create()) {
       DeleteWorkflowConfigRequest request =
           DeleteWorkflowConfigRequest.newBuilder()
               .setName(
                   WorkflowConfigName.of(
                           "[PROJECT]", "[LOCATION]", "[REPOSITORY]", "[WORKFLOW_CONFIG]")
                       .toString())
               .build();
       dataformClient.deleteWorkflowConfig(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[DeleteWorkflowConfigRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataform/latest/com.google.cloud.dataform.v1beta1.DeleteWorkflowConfigRequest)`  
The request object containing all of the parameters for the API call.  
  
### deleteWorkflowConfig(String name)
    
    
    public final void deleteWorkflowConfig(String name)

Deletes a single WorkflowConfig.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DataformClient dataformClient = DataformClient.create()) {
       String name =
           WorkflowConfigName.of("[PROJECT]", "[LOCATION]", "[REPOSITORY]", "[WORKFLOW_CONFIG]")
               .toString();
       dataformClient.deleteWorkflowConfig(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The workflow config's name.  
  
### deleteWorkflowConfigCallable()
    
    
    public final UnaryCallable<DeleteWorkflowConfigRequest,Empty> deleteWorkflowConfigCallable()

Deletes a single WorkflowConfig.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DataformClient dataformClient = DataformClient.create()) {
       DeleteWorkflowConfigRequest request =
           DeleteWorkflowConfigRequest.newBuilder()
               .setName(
                   WorkflowConfigName.of(
                           "[PROJECT]", "[LOCATION]", "[REPOSITORY]", "[WORKFLOW_CONFIG]")
                       .toString())
               .build();
       ApiFuture<Empty> future = dataformClient.deleteWorkflowConfigCallable().futureCall(request);
       // Do something.
       future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[DeleteWorkflowConfigRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataform/latest/com.google.cloud.dataform.v1beta1.DeleteWorkflowConfigRequest),[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html)>` |   
  
### deleteWorkflowInvocation(@Nullable WorkflowInvocationName name)
    
    
    public final void deleteWorkflowInvocation(@Nullable WorkflowInvocationName name)

Deletes a single WorkflowInvocation.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DataformClient dataformClient = DataformClient.create()) {
       WorkflowInvocationName name =
           WorkflowInvocationName.of(
               "[PROJECT]", "[LOCATION]", "[REPOSITORY]", "[WORKFLOW_INVOCATION]");
       dataformClient.deleteWorkflowInvocation(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `@org.jspecify.annotations.Nullable com.google.cloud.dataform.v1beta1.WorkflowInvocationName`  
Required. The workflow invocation resource's name.  
  
### deleteWorkflowInvocation(DeleteWorkflowInvocationRequest request)
    
    
    public final void deleteWorkflowInvocation(DeleteWorkflowInvocationRequest request)

Deletes a single WorkflowInvocation.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DataformClient dataformClient = DataformClient.create()) {
       DeleteWorkflowInvocationRequest request =
           DeleteWorkflowInvocationRequest.newBuilder()
               .setName(
                   WorkflowInvocationName.of(
                           "[PROJECT]", "[LOCATION]", "[REPOSITORY]", "[WORKFLOW_INVOCATION]")
                       .toString())
               .build();
       dataformClient.deleteWorkflowInvocation(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[DeleteWorkflowInvocationRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataform/latest/com.google.cloud.dataform.v1beta1.DeleteWorkflowInvocationRequest)`  
The request object containing all of the parameters for the API call.  
  
### deleteWorkflowInvocation(String name)
    
    
    public final void deleteWorkflowInvocation(String name)

Deletes a single WorkflowInvocation.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DataformClient dataformClient = DataformClient.create()) {
       String name =
           WorkflowInvocationName.of(
                   "[PROJECT]", "[LOCATION]", "[REPOSITORY]", "[WORKFLOW_INVOCATION]")
               .toString();
       dataformClient.deleteWorkflowInvocation(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The workflow invocation resource's name.  
  
### deleteWorkflowInvocationCallable()
    
    
    public final UnaryCallable<DeleteWorkflowInvocationRequest,Empty> deleteWorkflowInvocationCallable()

Deletes a single WorkflowInvocation.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DataformClient dataformClient = DataformClient.create()) {
       DeleteWorkflowInvocationRequest request =
           DeleteWorkflowInvocationRequest.newBuilder()
               .setName(
                   WorkflowInvocationName.of(
                           "[PROJECT]", "[LOCATION]", "[REPOSITORY]", "[WORKFLOW_INVOCATION]")
                       .toString())
               .build();
       ApiFuture<Empty> future =
           dataformClient.deleteWorkflowInvocationCallable().futureCall(request);
       // Do something.
       future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[DeleteWorkflowInvocationRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataform/latest/com.google.cloud.dataform.v1beta1.DeleteWorkflowInvocationRequest),[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html)>` |   
  
### deleteWorkspace(@Nullable WorkspaceName name)
    
    
    public final void deleteWorkspace(@Nullable WorkspaceName name)

Deletes a single Workspace.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DataformClient dataformClient = DataformClient.create()) {
       WorkspaceName name =
           WorkspaceName.of("[PROJECT]", "[LOCATION]", "[REPOSITORY]", "[WORKSPACE]");
       dataformClient.deleteWorkspace(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `@org.jspecify.annotations.Nullable com.google.cloud.dataform.v1beta1.WorkspaceName`  
Required. The workspace resource's name.  
  
### deleteWorkspace(DeleteWorkspaceRequest request)
    
    
    public final void deleteWorkspace(DeleteWorkspaceRequest request)

Deletes a single Workspace.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DataformClient dataformClient = DataformClient.create()) {
       DeleteWorkspaceRequest request =
           DeleteWorkspaceRequest.newBuilder()
               .setName(
                   WorkspaceName.of("[PROJECT]", "[LOCATION]", "[REPOSITORY]", "[WORKSPACE]")
                       .toString())
               .build();
       dataformClient.deleteWorkspace(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[DeleteWorkspaceRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataform/latest/com.google.cloud.dataform.v1beta1.DeleteWorkspaceRequest)`  
The request object containing all of the parameters for the API call.  
  
### deleteWorkspace(String name)
    
    
    public final void deleteWorkspace(String name)

Deletes a single Workspace.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DataformClient dataformClient = DataformClient.create()) {
       String name =
           WorkspaceName.of("[PROJECT]", "[LOCATION]", "[REPOSITORY]", "[WORKSPACE]").toString();
       dataformClient.deleteWorkspace(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The workspace resource's name.  
  
### deleteWorkspaceCallable()
    
    
    public final UnaryCallable<DeleteWorkspaceRequest,Empty> deleteWorkspaceCallable()

Deletes a single Workspace.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DataformClient dataformClient = DataformClient.create()) {
       DeleteWorkspaceRequest request =
           DeleteWorkspaceRequest.newBuilder()
               .setName(
                   WorkspaceName.of("[PROJECT]", "[LOCATION]", "[REPOSITORY]", "[WORKSPACE]")
                       .toString())
               .build();
       ApiFuture<Empty> future = dataformClient.deleteWorkspaceCallable().futureCall(request);
       // Do something.
       future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[DeleteWorkspaceRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataform/latest/com.google.cloud.dataform.v1beta1.DeleteWorkspaceRequest),[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html)>` |   
  
### fetchCurrentWorkspaceBranch(FetchCurrentWorkspaceBranchRequest request)
    
    
    public final FetchCurrentWorkspaceBranchResponse fetchCurrentWorkspaceBranch(FetchCurrentWorkspaceBranchRequest request)

Fetches the current branch of a Workspace.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DataformClient dataformClient = DataformClient.create()) {
       FetchCurrentWorkspaceBranchRequest request =
           FetchCurrentWorkspaceBranchRequest.newBuilder()
               .setName(
                   WorkspaceName.of("[PROJECT]", "[LOCATION]", "[REPOSITORY]", "[WORKSPACE]")
                       .toString())
               .build();
       FetchCurrentWorkspaceBranchResponse response =
           dataformClient.fetchCurrentWorkspaceBranch(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[FetchCurrentWorkspaceBranchRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataform/latest/com.google.cloud.dataform.v1beta1.FetchCurrentWorkspaceBranchRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[FetchCurrentWorkspaceBranchResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataform/latest/com.google.cloud.dataform.v1beta1.FetchCurrentWorkspaceBranchResponse)` |   
  
### fetchCurrentWorkspaceBranchCallable()
    
    
    public final UnaryCallable<FetchCurrentWorkspaceBranchRequest,FetchCurrentWorkspaceBranchResponse> fetchCurrentWorkspaceBranchCallable()

Fetches the current branch of a Workspace.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DataformClient dataformClient = DataformClient.create()) {
       FetchCurrentWorkspaceBranchRequest request =
           FetchCurrentWorkspaceBranchRequest.newBuilder()
               .setName(
                   WorkspaceName.of("[PROJECT]", "[LOCATION]", "[REPOSITORY]", "[WORKSPACE]")
                       .toString())
               .build();
       ApiFuture<FetchCurrentWorkspaceBranchResponse> future =
           dataformClient.fetchCurrentWorkspaceBranchCallable().futureCall(request);
       // Do something.
       FetchCurrentWorkspaceBranchResponse response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[FetchCurrentWorkspaceBranchRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataform/latest/com.google.cloud.dataform.v1beta1.FetchCurrentWorkspaceBranchRequest),[FetchCurrentWorkspaceBranchResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataform/latest/com.google.cloud.dataform.v1beta1.FetchCurrentWorkspaceBranchResponse)>` |   
  
### fetchFileDiff(FetchFileDiffRequest request)
    
    
    public final FetchFileDiffResponse fetchFileDiff(FetchFileDiffRequest request)

Fetches Git diff for an uncommitted file in a Workspace.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DataformClient dataformClient = DataformClient.create()) {
       FetchFileDiffRequest request =
           FetchFileDiffRequest.newBuilder()
               .setWorkspace(
                   WorkspaceName.of("[PROJECT]", "[LOCATION]", "[REPOSITORY]", "[WORKSPACE]")
                       .toString())
               .setPath("path3433509")
               .build();
       FetchFileDiffResponse response = dataformClient.fetchFileDiff(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[FetchFileDiffRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataform/latest/com.google.cloud.dataform.v1beta1.FetchFileDiffRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[FetchFileDiffResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataform/latest/com.google.cloud.dataform.v1beta1.FetchFileDiffResponse)` |   
  
### fetchFileDiffCallable()
    
    
    public final UnaryCallable<FetchFileDiffRequest,FetchFileDiffResponse> fetchFileDiffCallable()

Fetches Git diff for an uncommitted file in a Workspace.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DataformClient dataformClient = DataformClient.create()) {
       FetchFileDiffRequest request =
           FetchFileDiffRequest.newBuilder()
               .setWorkspace(
                   WorkspaceName.of("[PROJECT]", "[LOCATION]", "[REPOSITORY]", "[WORKSPACE]")
                       .toString())
               .setPath("path3433509")
               .build();
       ApiFuture<FetchFileDiffResponse> future =
           dataformClient.fetchFileDiffCallable().futureCall(request);
       // Do something.
       FetchFileDiffResponse response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[FetchFileDiffRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataform/latest/com.google.cloud.dataform.v1beta1.FetchFileDiffRequest),[FetchFileDiffResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataform/latest/com.google.cloud.dataform.v1beta1.FetchFileDiffResponse)>` |   
  
### fetchFileGitStatuses(FetchFileGitStatusesRequest request)
    
    
    public final FetchFileGitStatusesResponse fetchFileGitStatuses(FetchFileGitStatusesRequest request)

Fetches Git statuses for the files in a Workspace.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DataformClient dataformClient = DataformClient.create()) {
       FetchFileGitStatusesRequest request =
           FetchFileGitStatusesRequest.newBuilder()
               .setName(
                   WorkspaceName.of("[PROJECT]", "[LOCATION]", "[REPOSITORY]", "[WORKSPACE]")
                       .toString())
               .build();
       FetchFileGitStatusesResponse response = dataformClient.fetchFileGitStatuses(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[FetchFileGitStatusesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataform/latest/com.google.cloud.dataform.v1beta1.FetchFileGitStatusesRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[FetchFileGitStatusesResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataform/latest/com.google.cloud.dataform.v1beta1.FetchFileGitStatusesResponse)` |   
  
### fetchFileGitStatusesCallable()
    
    
    public final UnaryCallable<FetchFileGitStatusesRequest,FetchFileGitStatusesResponse> fetchFileGitStatusesCallable()

Fetches Git statuses for the files in a Workspace.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DataformClient dataformClient = DataformClient.create()) {
       FetchFileGitStatusesRequest request =
           FetchFileGitStatusesRequest.newBuilder()
               .setName(
                   WorkspaceName.of("[PROJECT]", "[LOCATION]", "[REPOSITORY]", "[WORKSPACE]")
                       .toString())
               .build();
       ApiFuture<FetchFileGitStatusesResponse> future =
           dataformClient.fetchFileGitStatusesCallable().futureCall(request);
       // Do something.
       FetchFileGitStatusesResponse response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[FetchFileGitStatusesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataform/latest/com.google.cloud.dataform.v1beta1.FetchFileGitStatusesRequest),[FetchFileGitStatusesResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataform/latest/com.google.cloud.dataform.v1beta1.FetchFileGitStatusesResponse)>` |   
  
### fetchGitAheadBehind(FetchGitAheadBehindRequest request)
    
    
    public final FetchGitAheadBehindResponse fetchGitAheadBehind(FetchGitAheadBehindRequest request)

Fetches Git ahead/behind against a remote branch.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DataformClient dataformClient = DataformClient.create()) {
       FetchGitAheadBehindRequest request =
           FetchGitAheadBehindRequest.newBuilder()
               .setName(
                   WorkspaceName.of("[PROJECT]", "[LOCATION]", "[REPOSITORY]", "[WORKSPACE]")
                       .toString())
               .setRemoteBranch("remoteBranch-533119608")
               .build();
       FetchGitAheadBehindResponse response = dataformClient.fetchGitAheadBehind(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[FetchGitAheadBehindRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataform/latest/com.google.cloud.dataform.v1beta1.FetchGitAheadBehindRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[FetchGitAheadBehindResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataform/latest/com.google.cloud.dataform.v1beta1.FetchGitAheadBehindResponse)` |   
  
### fetchGitAheadBehindCallable()
    
    
    public final UnaryCallable<FetchGitAheadBehindRequest,FetchGitAheadBehindResponse> fetchGitAheadBehindCallable()

Fetches Git ahead/behind against a remote branch.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DataformClient dataformClient = DataformClient.create()) {
       FetchGitAheadBehindRequest request =
           FetchGitAheadBehindRequest.newBuilder()
               .setName(
                   WorkspaceName.of("[PROJECT]", "[LOCATION]", "[REPOSITORY]", "[WORKSPACE]")
                       .toString())
               .setRemoteBranch("remoteBranch-533119608")
               .build();
       ApiFuture<FetchGitAheadBehindResponse> future =
           dataformClient.fetchGitAheadBehindCallable().futureCall(request);
       // Do something.
       FetchGitAheadBehindResponse response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[FetchGitAheadBehindRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataform/latest/com.google.cloud.dataform.v1beta1.FetchGitAheadBehindRequest),[FetchGitAheadBehindResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataform/latest/com.google.cloud.dataform.v1beta1.FetchGitAheadBehindResponse)>` |   
  
### fetchRemoteBranches(FetchRemoteBranchesRequest request)
    
    
    public final FetchRemoteBranchesResponse fetchRemoteBranches(FetchRemoteBranchesRequest request)

Fetches a Repository's remote branches.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DataformClient dataformClient = DataformClient.create()) {
       FetchRemoteBranchesRequest request =
           FetchRemoteBranchesRequest.newBuilder()
               .setName(RepositoryName.of("[PROJECT]", "[LOCATION]", "[REPOSITORY]").toString())
               .build();
       FetchRemoteBranchesResponse response = dataformClient.fetchRemoteBranches(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[FetchRemoteBranchesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataform/latest/com.google.cloud.dataform.v1beta1.FetchRemoteBranchesRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[FetchRemoteBranchesResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataform/latest/com.google.cloud.dataform.v1beta1.FetchRemoteBranchesResponse)` |   
  
### fetchRemoteBranchesCallable()
    
    
    public final UnaryCallable<FetchRemoteBranchesRequest,FetchRemoteBranchesResponse> fetchRemoteBranchesCallable()

Fetches a Repository's remote branches.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DataformClient dataformClient = DataformClient.create()) {
       FetchRemoteBranchesRequest request =
           FetchRemoteBranchesRequest.newBuilder()
               .setName(RepositoryName.of("[PROJECT]", "[LOCATION]", "[REPOSITORY]").toString())
               .build();
       ApiFuture<FetchRemoteBranchesResponse> future =
           dataformClient.fetchRemoteBranchesCallable().futureCall(request);
       // Do something.
       FetchRemoteBranchesResponse response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[FetchRemoteBranchesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataform/latest/com.google.cloud.dataform.v1beta1.FetchRemoteBranchesRequest),[FetchRemoteBranchesResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataform/latest/com.google.cloud.dataform.v1beta1.FetchRemoteBranchesResponse)>` |   
  
### fetchRepositoryHistory(FetchRepositoryHistoryRequest request)
    
    
    public final DataformClient.FetchRepositoryHistoryPagedResponse fetchRepositoryHistory(FetchRepositoryHistoryRequest request)

Fetches a Repository's history of commits. The Repository must not have a value for `git_remote_settings.url`.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DataformClient dataformClient = DataformClient.create()) {
       FetchRepositoryHistoryRequest request =
           FetchRepositoryHistoryRequest.newBuilder()
               .setName(RepositoryName.of("[PROJECT]", "[LOCATION]", "[REPOSITORY]").toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .build();
       for (CommitLogEntry element : dataformClient.fetchRepositoryHistory(request).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[FetchRepositoryHistoryRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataform/latest/com.google.cloud.dataform.v1beta1.FetchRepositoryHistoryRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[DataformClient.FetchRepositoryHistoryPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataform/latest/com.google.cloud.dataform.v1beta1.DataformClient.FetchRepositoryHistoryPagedResponse)` |   
  
### fetchRepositoryHistoryCallable()
    
    
    public final UnaryCallable<FetchRepositoryHistoryRequest,FetchRepositoryHistoryResponse> fetchRepositoryHistoryCallable()

Fetches a Repository's history of commits. The Repository must not have a value for `git_remote_settings.url`.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DataformClient dataformClient = DataformClient.create()) {
       FetchRepositoryHistoryRequest request =
           FetchRepositoryHistoryRequest.newBuilder()
               .setName(RepositoryName.of("[PROJECT]", "[LOCATION]", "[REPOSITORY]").toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .build();
       while (true) {
         FetchRepositoryHistoryResponse response =
             dataformClient.fetchRepositoryHistoryCallable().call(request);
         for (CommitLogEntry element : response.getCommitsList()) {
           // doThingsWith(element);
         }
         String nextPageToken = response.getNextPageToken();
         if (!Strings.isNullOrEmpty(nextPageToken)) {
           request = request.toBuilder().setPageToken(nextPageToken).build();
         } else {
           break;
         }
       }
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[FetchRepositoryHistoryRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataform/latest/com.google.cloud.dataform.v1beta1.FetchRepositoryHistoryRequest),[FetchRepositoryHistoryResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataform/latest/com.google.cloud.dataform.v1beta1.FetchRepositoryHistoryResponse)>` |   
  
### fetchRepositoryHistoryPagedCallable()
    
    
    public final UnaryCallable<FetchRepositoryHistoryRequest,DataformClient.FetchRepositoryHistoryPagedResponse> fetchRepositoryHistoryPagedCallable()

Fetches a Repository's history of commits. The Repository must not have a value for `git_remote_settings.url`.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DataformClient dataformClient = DataformClient.create()) {
       FetchRepositoryHistoryRequest request =
           FetchRepositoryHistoryRequest.newBuilder()
               .setName(RepositoryName.of("[PROJECT]", "[LOCATION]", "[REPOSITORY]").toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .build();
       ApiFuture<CommitLogEntry> future =
           dataformClient.fetchRepositoryHistoryPagedCallable().futureCall(request);
       // Do something.
       for (CommitLogEntry element : future.get().iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[FetchRepositoryHistoryRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataform/latest/com.google.cloud.dataform.v1beta1.FetchRepositoryHistoryRequest),[FetchRepositoryHistoryPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataform/latest/com.google.cloud.dataform.v1beta1.DataformClient.FetchRepositoryHistoryPagedResponse)>` |   
  
### fetchWorkspaceBranches(FetchWorkspaceBranchesRequest request)
    
    
    public final DataformClient.FetchWorkspaceBranchesPagedResponse fetchWorkspaceBranches(FetchWorkspaceBranchesRequest request)

Fetches branches in a Workspace.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DataformClient dataformClient = DataformClient.create()) {
       FetchWorkspaceBranchesRequest request =
           FetchWorkspaceBranchesRequest.newBuilder()
               .setName(
                   WorkspaceName.of("[PROJECT]", "[LOCATION]", "[REPOSITORY]", "[WORKSPACE]")
                       .toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .build();
       for (BranchMetadata element : dataformClient.fetchWorkspaceBranches(request).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[FetchWorkspaceBranchesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataform/latest/com.google.cloud.dataform.v1beta1.FetchWorkspaceBranchesRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[DataformClient.FetchWorkspaceBranchesPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataform/latest/com.google.cloud.dataform.v1beta1.DataformClient.FetchWorkspaceBranchesPagedResponse)` |   
  
### fetchWorkspaceBranchesCallable()
    
    
    public final UnaryCallable<FetchWorkspaceBranchesRequest,FetchWorkspaceBranchesResponse> fetchWorkspaceBranchesCallable()

Fetches branches in a Workspace.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DataformClient dataformClient = DataformClient.create()) {
       FetchWorkspaceBranchesRequest request =
           FetchWorkspaceBranchesRequest.newBuilder()
               .setName(
                   WorkspaceName.of("[PROJECT]", "[LOCATION]", "[REPOSITORY]", "[WORKSPACE]")
                       .toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .build();
       while (true) {
         FetchWorkspaceBranchesResponse response =
             dataformClient.fetchWorkspaceBranchesCallable().call(request);
         for (BranchMetadata element : response.getBranchesList()) {
           // doThingsWith(element);
         }
         String nextPageToken = response.getNextPageToken();
         if (!Strings.isNullOrEmpty(nextPageToken)) {
           request = request.toBuilder().setPageToken(nextPageToken).build();
         } else {
           break;
         }
       }
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[FetchWorkspaceBranchesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataform/latest/com.google.cloud.dataform.v1beta1.FetchWorkspaceBranchesRequest),[FetchWorkspaceBranchesResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataform/latest/com.google.cloud.dataform.v1beta1.FetchWorkspaceBranchesResponse)>` |   
  
### fetchWorkspaceBranchesPagedCallable()
    
    
    public final UnaryCallable<FetchWorkspaceBranchesRequest,DataformClient.FetchWorkspaceBranchesPagedResponse> fetchWorkspaceBranchesPagedCallable()

Fetches branches in a Workspace.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DataformClient dataformClient = DataformClient.create()) {
       FetchWorkspaceBranchesRequest request =
           FetchWorkspaceBranchesRequest.newBuilder()
               .setName(
                   WorkspaceName.of("[PROJECT]", "[LOCATION]", "[REPOSITORY]", "[WORKSPACE]")
                       .toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .build();
       ApiFuture<BranchMetadata> future =
           dataformClient.fetchWorkspaceBranchesPagedCallable().futureCall(request);
       // Do something.
       for (BranchMetadata element : future.get().iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[FetchWorkspaceBranchesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataform/latest/com.google.cloud.dataform.v1beta1.FetchWorkspaceBranchesRequest),[FetchWorkspaceBranchesPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataform/latest/com.google.cloud.dataform.v1beta1.DataformClient.FetchWorkspaceBranchesPagedResponse)>` |   
  
### getCompilationResult(@Nullable CompilationResultName name)
    
    
    public final CompilationResult getCompilationResult(@Nullable CompilationResultName name)

Fetches a single CompilationResult.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DataformClient dataformClient = DataformClient.create()) {
       CompilationResultName name =
           CompilationResultName.of(
               "[PROJECT]", "[LOCATION]", "[REPOSITORY]", "[COMPILATION_RESULT]");
       CompilationResult response = dataformClient.getCompilationResult(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `@org.jspecify.annotations.Nullable com.google.cloud.dataform.v1beta1.CompilationResultName`  
Required. The compilation result's name.  
**Returns**  
---  
**Type** | **Description**  
`[CompilationResult](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataform/latest/com.google.cloud.dataform.v1beta1.CompilationResult)` |   
  
### getCompilationResult(GetCompilationResultRequest request)
    
    
    public final CompilationResult getCompilationResult(GetCompilationResultRequest request)

Fetches a single CompilationResult.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DataformClient dataformClient = DataformClient.create()) {
       GetCompilationResultRequest request =
           GetCompilationResultRequest.newBuilder()
               .setName(
                   CompilationResultName.of(
                           "[PROJECT]", "[LOCATION]", "[REPOSITORY]", "[COMPILATION_RESULT]")
                       .toString())
               .build();
       CompilationResult response = dataformClient.getCompilationResult(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[GetCompilationResultRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataform/latest/com.google.cloud.dataform.v1beta1.GetCompilationResultRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[CompilationResult](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataform/latest/com.google.cloud.dataform.v1beta1.CompilationResult)` |   
  
### getCompilationResult(String name)
    
    
    public final CompilationResult getCompilationResult(String name)

Fetches a single CompilationResult.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DataformClient dataformClient = DataformClient.create()) {
       String name =
           CompilationResultName.of(
                   "[PROJECT]", "[LOCATION]", "[REPOSITORY]", "[COMPILATION_RESULT]")
               .toString();
       CompilationResult response = dataformClient.getCompilationResult(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The compilation result's name.  
**Returns**  
---  
**Type** | **Description**  
`[CompilationResult](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataform/latest/com.google.cloud.dataform.v1beta1.CompilationResult)` |   
  
### getCompilationResultCallable()
    
    
    public final UnaryCallable<GetCompilationResultRequest,CompilationResult> getCompilationResultCallable()

Fetches a single CompilationResult.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DataformClient dataformClient = DataformClient.create()) {
       GetCompilationResultRequest request =
           GetCompilationResultRequest.newBuilder()
               .setName(
                   CompilationResultName.of(
                           "[PROJECT]", "[LOCATION]", "[REPOSITORY]", "[COMPILATION_RESULT]")
                       .toString())
               .build();
       ApiFuture<CompilationResult> future =
           dataformClient.getCompilationResultCallable().futureCall(request);
       // Do something.
       CompilationResult response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[GetCompilationResultRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataform/latest/com.google.cloud.dataform.v1beta1.GetCompilationResultRequest),[CompilationResult](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataform/latest/com.google.cloud.dataform.v1beta1.CompilationResult)>` |   
  
### getConfig(@Nullable ConfigName name)
    
    
    public final Config getConfig(@Nullable ConfigName name)

Get default config for a given project and location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DataformClient dataformClient = DataformClient.create()) {
       ConfigName name = ConfigName.of("[PROJECT]", "[LOCATION]");
       Config response = dataformClient.getConfig(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `@org.jspecify.annotations.Nullable com.google.cloud.dataform.v1beta1.ConfigName`  
Required. The config name.  
**Returns**  
---  
**Type** | **Description**  
`[Config](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataform/latest/com.google.cloud.dataform.v1beta1.Config)` |   
  
### getConfig(GetConfigRequest request)
    
    
    public final Config getConfig(GetConfigRequest request)

Get default config for a given project and location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DataformClient dataformClient = DataformClient.create()) {
       GetConfigRequest request =
           GetConfigRequest.newBuilder()
               .setName(ConfigName.of("[PROJECT]", "[LOCATION]").toString())
               .build();
       Config response = dataformClient.getConfig(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[GetConfigRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataform/latest/com.google.cloud.dataform.v1beta1.GetConfigRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[Config](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataform/latest/com.google.cloud.dataform.v1beta1.Config)` |   
  
### getConfig(String name)
    
    
    public final Config getConfig(String name)

Get default config for a given project and location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DataformClient dataformClient = DataformClient.create()) {
       String name = ConfigName.of("[PROJECT]", "[LOCATION]").toString();
       Config response = dataformClient.getConfig(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The config name.  
**Returns**  
---  
**Type** | **Description**  
`[Config](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataform/latest/com.google.cloud.dataform.v1beta1.Config)` |   
  
### getConfigCallable()
    
    
    public final UnaryCallable<GetConfigRequest,Config> getConfigCallable()

Get default config for a given project and location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DataformClient dataformClient = DataformClient.create()) {
       GetConfigRequest request =
           GetConfigRequest.newBuilder()
               .setName(ConfigName.of("[PROJECT]", "[LOCATION]").toString())
               .build();
       ApiFuture<Config> future = dataformClient.getConfigCallable().futureCall(request);
       // Do something.
       Config response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[GetConfigRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataform/latest/com.google.cloud.dataform.v1beta1.GetConfigRequest),[Config](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataform/latest/com.google.cloud.dataform.v1beta1.Config)>` |   
  
### getFolder(@Nullable FolderName name)
    
    
    public final Folder getFolder(@Nullable FolderName name)

Fetches a single Folder.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DataformClient dataformClient = DataformClient.create()) {
       FolderName name = FolderName.of("[PROJECT]", "[LOCATION]", "[FOLDER]");
       Folder response = dataformClient.getFolder(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `@org.jspecify.annotations.Nullable com.google.cloud.dataform.v1beta1.FolderName`  
Required. The Folder's name.  
**Returns**  
---  
**Type** | **Description**  
`[Folder](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataform/latest/com.google.cloud.dataform.v1beta1.Folder)` |   
  
### getFolder(GetFolderRequest request)
    
    
    public final Folder getFolder(GetFolderRequest request)

Fetches a single Folder.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DataformClient dataformClient = DataformClient.create()) {
       GetFolderRequest request =
           GetFolderRequest.newBuilder()
               .setName(FolderName.of("[PROJECT]", "[LOCATION]", "[FOLDER]").toString())
               .build();
       Folder response = dataformClient.getFolder(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[GetFolderRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataform/latest/com.google.cloud.dataform.v1beta1.GetFolderRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[Folder](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataform/latest/com.google.cloud.dataform.v1beta1.Folder)` |   
  
### getFolder(String name)
    
    
    public final Folder getFolder(String name)

Fetches a single Folder.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DataformClient dataformClient = DataformClient.create()) {
       String name = FolderName.of("[PROJECT]", "[LOCATION]", "[FOLDER]").toString();
       Folder response = dataformClient.getFolder(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The Folder's name.  
**Returns**  
---  
**Type** | **Description**  
`[Folder](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataform/latest/com.google.cloud.dataform.v1beta1.Folder)` |   
  
### getFolderCallable()
    
    
    public final UnaryCallable<GetFolderRequest,Folder> getFolderCallable()

Fetches a single Folder.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DataformClient dataformClient = DataformClient.create()) {
       GetFolderRequest request =
           GetFolderRequest.newBuilder()
               .setName(FolderName.of("[PROJECT]", "[LOCATION]", "[FOLDER]").toString())
               .build();
       ApiFuture<Folder> future = dataformClient.getFolderCallable().futureCall(request);
       // Do something.
       Folder response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[GetFolderRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataform/latest/com.google.cloud.dataform.v1beta1.GetFolderRequest),[Folder](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataform/latest/com.google.cloud.dataform.v1beta1.Folder)>` |   
  
### getHttpJsonOperationsClient()
    
    
    public final OperationsClient getHttpJsonOperationsClient()

**Beta**

This feature is covered by the [Pre-GA Offerings Terms](https://docs.cloud.google.com/terms/service-terms#1) of the Terms of Service. Pre-GA libraries might have limited support, and changes to pre-GA libraries might not be compatible with other pre-GA versions. For more information, see the launch stage descriptions.

Returns the OperationsClient that can be used to query the status of a long-running operation returned by another API method call.

**Returns**  
---  
**Type** | **Description**  
`[OperationsClient](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.httpjson.longrunning.OperationsClient.html)` |   
  
### getIamPolicy(@Nullable ResourceName resource)
    
    
    public final Policy getIamPolicy(@Nullable ResourceName resource)

Gets the access control policy for a resource. Returns an empty policy if the resource exists and does not have a policy set.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DataformClient dataformClient = DataformClient.create()) {
       ResourceName resource = FolderName.of("[PROJECT]", "[LOCATION]", "[FOLDER]");
       Policy response = dataformClient.getIamPolicy(resource);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`resource` | `@org.jspecify.annotations.Nullable com.google.api.resourcenames.ResourceName`  
REQUIRED: The resource for which the policy is being requested. See the operation documentation for the appropriate value for this field.  
**Returns**  
---  
**Type** | **Description**  
`com.google.iam.v1.Policy` |   
  
### getIamPolicy(GetIamPolicyRequest request)
    
    
    public final Policy getIamPolicy(GetIamPolicyRequest request)

Gets the access control policy for a resource. Returns an empty policy if the resource exists and does not have a policy set.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DataformClient dataformClient = DataformClient.create()) {
       GetIamPolicyRequest request =
           GetIamPolicyRequest.newBuilder()
               .setResource(FolderName.of("[PROJECT]", "[LOCATION]", "[FOLDER]").toString())
               .setOptions(GetPolicyOptions.newBuilder().build())
               .build();
       Policy response = dataformClient.getIamPolicy(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `com.google.iam.v1.GetIamPolicyRequest`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`com.google.iam.v1.Policy` |   
  
### getIamPolicy(String resource)
    
    
    public final Policy getIamPolicy(String resource)

Gets the access control policy for a resource. Returns an empty policy if the resource exists and does not have a policy set.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DataformClient dataformClient = DataformClient.create()) {
       String resource =
           CompilationResultName.of(
                   "[PROJECT]", "[LOCATION]", "[REPOSITORY]", "[COMPILATION_RESULT]")
               .toString();
       Policy response = dataformClient.getIamPolicy(resource);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`resource` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
REQUIRED: The resource for which the policy is being requested. See the operation documentation for the appropriate value for this field.  
**Returns**  
---  
**Type** | **Description**  
`com.google.iam.v1.Policy` |   
  
### getIamPolicyCallable()
    
    
    public final UnaryCallable<GetIamPolicyRequest,Policy> getIamPolicyCallable()

Gets the access control policy for a resource. Returns an empty policy if the resource exists and does not have a policy set.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DataformClient dataformClient = DataformClient.create()) {
       GetIamPolicyRequest request =
           GetIamPolicyRequest.newBuilder()
               .setResource(FolderName.of("[PROJECT]", "[LOCATION]", "[FOLDER]").toString())
               .setOptions(GetPolicyOptions.newBuilder().build())
               .build();
       ApiFuture<Policy> future = dataformClient.getIamPolicyCallable().futureCall(request);
       // Do something.
       Policy response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<com.google.iam.v1.GetIamPolicyRequest,com.google.iam.v1.Policy>` |   
  
### getLocation(GetLocationRequest request)
    
    
    public final Location getLocation(GetLocationRequest request)

Gets information about a location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DataformClient dataformClient = DataformClient.create()) {
       GetLocationRequest request = GetLocationRequest.newBuilder().setName("name3373707").build();
       Location response = dataformClient.getLocation(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `com.google.cloud.location.GetLocationRequest`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`com.google.cloud.location.Location` |   
  
### getLocationCallable()
    
    
    public final UnaryCallable<GetLocationRequest,Location> getLocationCallable()

Gets information about a location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DataformClient dataformClient = DataformClient.create()) {
       GetLocationRequest request = GetLocationRequest.newBuilder().setName("name3373707").build();
       ApiFuture<Location> future = dataformClient.getLocationCallable().futureCall(request);
       // Do something.
       Location response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<com.google.cloud.location.GetLocationRequest,com.google.cloud.location.Location>` |   
  
### getOperationsClient()
    
    
    public final OperationsClient getOperationsClient()

Returns the OperationsClient that can be used to query the status of a long-running operation returned by another API method call.

**Returns**  
---  
**Type** | **Description**  
`[OperationsClient](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.OperationsClient.html)` |   
  
### getReleaseConfig(@Nullable ReleaseConfigName name)
    
    
    public final ReleaseConfig getReleaseConfig(@Nullable ReleaseConfigName name)

Fetches a single ReleaseConfig.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DataformClient dataformClient = DataformClient.create()) {
       ReleaseConfigName name =
           ReleaseConfigName.of("[PROJECT]", "[LOCATION]", "[REPOSITORY]", "[RELEASE_CONFIG]");
       ReleaseConfig response = dataformClient.getReleaseConfig(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `@org.jspecify.annotations.Nullable com.google.cloud.dataform.v1beta1.ReleaseConfigName`  
Required. The release config's name.  
**Returns**  
---  
**Type** | **Description**  
`[ReleaseConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataform/latest/com.google.cloud.dataform.v1beta1.ReleaseConfig)` |   
  
### getReleaseConfig(GetReleaseConfigRequest request)
    
    
    public final ReleaseConfig getReleaseConfig(GetReleaseConfigRequest request)

Fetches a single ReleaseConfig.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DataformClient dataformClient = DataformClient.create()) {
       GetReleaseConfigRequest request =
           GetReleaseConfigRequest.newBuilder()
               .setName(
                   ReleaseConfigName.of(
                           "[PROJECT]", "[LOCATION]", "[REPOSITORY]", "[RELEASE_CONFIG]")
                       .toString())
               .build();
       ReleaseConfig response = dataformClient.getReleaseConfig(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[GetReleaseConfigRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataform/latest/com.google.cloud.dataform.v1beta1.GetReleaseConfigRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[ReleaseConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataform/latest/com.google.cloud.dataform.v1beta1.ReleaseConfig)` |   
  
### getReleaseConfig(String name)
    
    
    public final ReleaseConfig getReleaseConfig(String name)

Fetches a single ReleaseConfig.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DataformClient dataformClient = DataformClient.create()) {
       String name =
           ReleaseConfigName.of("[PROJECT]", "[LOCATION]", "[REPOSITORY]", "[RELEASE_CONFIG]")
               .toString();
       ReleaseConfig response = dataformClient.getReleaseConfig(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The release config's name.  
**Returns**  
---  
**Type** | **Description**  
`[ReleaseConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataform/latest/com.google.cloud.dataform.v1beta1.ReleaseConfig)` |   
  
### getReleaseConfigCallable()
    
    
    public final UnaryCallable<GetReleaseConfigRequest,ReleaseConfig> getReleaseConfigCallable()

Fetches a single ReleaseConfig.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DataformClient dataformClient = DataformClient.create()) {
       GetReleaseConfigRequest request =
           GetReleaseConfigRequest.newBuilder()
               .setName(
                   ReleaseConfigName.of(
                           "[PROJECT]", "[LOCATION]", "[REPOSITORY]", "[RELEASE_CONFIG]")
                       .toString())
               .build();
       ApiFuture<ReleaseConfig> future =
           dataformClient.getReleaseConfigCallable().futureCall(request);
       // Do something.
       ReleaseConfig response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[GetReleaseConfigRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataform/latest/com.google.cloud.dataform.v1beta1.GetReleaseConfigRequest),[ReleaseConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataform/latest/com.google.cloud.dataform.v1beta1.ReleaseConfig)>` |   
  
### getRepository(@Nullable RepositoryName name)
    
    
    public final Repository getRepository(@Nullable RepositoryName name)

Fetches a single Repository.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DataformClient dataformClient = DataformClient.create()) {
       RepositoryName name = RepositoryName.of("[PROJECT]", "[LOCATION]", "[REPOSITORY]");
       Repository response = dataformClient.getRepository(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `@org.jspecify.annotations.Nullable com.google.cloud.dataform.v1beta1.RepositoryName`  
Required. The repository's name.  
**Returns**  
---  
**Type** | **Description**  
`[Repository](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataform/latest/com.google.cloud.dataform.v1beta1.Repository)` |   
  
### getRepository(GetRepositoryRequest request)
    
    
    public final Repository getRepository(GetRepositoryRequest request)

Fetches a single Repository.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DataformClient dataformClient = DataformClient.create()) {
       GetRepositoryRequest request =
           GetRepositoryRequest.newBuilder()
               .setName(RepositoryName.of("[PROJECT]", "[LOCATION]", "[REPOSITORY]").toString())
               .build();
       Repository response = dataformClient.getRepository(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[GetRepositoryRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataform/latest/com.google.cloud.dataform.v1beta1.GetRepositoryRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[Repository](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataform/latest/com.google.cloud.dataform.v1beta1.Repository)` |   
  
### getRepository(String name)
    
    
    public final Repository getRepository(String name)

Fetches a single Repository.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DataformClient dataformClient = DataformClient.create()) {
       String name = RepositoryName.of("[PROJECT]", "[LOCATION]", "[REPOSITORY]").toString();
       Repository response = dataformClient.getRepository(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The repository's name.  
**Returns**  
---  
**Type** | **Description**  
`[Repository](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataform/latest/com.google.cloud.dataform.v1beta1.Repository)` |   
  
### getRepositoryCallable()
    
    
    public final UnaryCallable<GetRepositoryRequest,Repository> getRepositoryCallable()

Fetches a single Repository.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DataformClient dataformClient = DataformClient.create()) {
       GetRepositoryRequest request =
           GetRepositoryRequest.newBuilder()
               .setName(RepositoryName.of("[PROJECT]", "[LOCATION]", "[REPOSITORY]").toString())
               .build();
       ApiFuture<Repository> future = dataformClient.getRepositoryCallable().futureCall(request);
       // Do something.
       Repository response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[GetRepositoryRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataform/latest/com.google.cloud.dataform.v1beta1.GetRepositoryRequest),[Repository](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataform/latest/com.google.cloud.dataform.v1beta1.Repository)>` |   
  
### getSettings()
    
    
    public final @Nullable DataformSettings getSettings()

**Returns**  
---  
**Type** | **Description**  
`@org.jspecify.annotations.Nullable com.google.cloud.dataform.v1beta1.DataformSettings` |   
  
### getStub()
    
    
    public DataformStub getStub()

**Returns**  
---  
**Type** | **Description**  
`[DataformStub](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataform/latest/com.google.cloud.dataform.v1beta1.stub.DataformStub)` |   
  
### getTeamFolder(@Nullable TeamFolderName name)
    
    
    public final TeamFolder getTeamFolder(@Nullable TeamFolderName name)

Fetches a single TeamFolder.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DataformClient dataformClient = DataformClient.create()) {
       TeamFolderName name = TeamFolderName.of("[PROJECT]", "[LOCATION]", "[TEAM_FOLDER]");
       TeamFolder response = dataformClient.getTeamFolder(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `@org.jspecify.annotations.Nullable com.google.cloud.dataform.v1beta1.TeamFolderName`  
Required. The TeamFolder's name.  
**Returns**  
---  
**Type** | **Description**  
`[TeamFolder](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataform/latest/com.google.cloud.dataform.v1beta1.TeamFolder)` |   
  
### getTeamFolder(GetTeamFolderRequest request)
    
    
    public final TeamFolder getTeamFolder(GetTeamFolderRequest request)

Fetches a single TeamFolder.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DataformClient dataformClient = DataformClient.create()) {
       GetTeamFolderRequest request =
           GetTeamFolderRequest.newBuilder()
               .setName(TeamFolderName.of("[PROJECT]", "[LOCATION]", "[TEAM_FOLDER]").toString())
               .build();
       TeamFolder response = dataformClient.getTeamFolder(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[GetTeamFolderRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataform/latest/com.google.cloud.dataform.v1beta1.GetTeamFolderRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[TeamFolder](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataform/latest/com.google.cloud.dataform.v1beta1.TeamFolder)` |   
  
### getTeamFolder(String name)
    
    
    public final TeamFolder getTeamFolder(String name)

Fetches a single TeamFolder.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DataformClient dataformClient = DataformClient.create()) {
       String name = TeamFolderName.of("[PROJECT]", "[LOCATION]", "[TEAM_FOLDER]").toString();
       TeamFolder response = dataformClient.getTeamFolder(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The TeamFolder's name.  
**Returns**  
---  
**Type** | **Description**  
`[TeamFolder](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataform/latest/com.google.cloud.dataform.v1beta1.TeamFolder)` |   
  
### getTeamFolderCallable()
    
    
    public final UnaryCallable<GetTeamFolderRequest,TeamFolder> getTeamFolderCallable()

Fetches a single TeamFolder.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DataformClient dataformClient = DataformClient.create()) {
       GetTeamFolderRequest request =
           GetTeamFolderRequest.newBuilder()
               .setName(TeamFolderName.of("[PROJECT]", "[LOCATION]", "[TEAM_FOLDER]").toString())
               .build();
       ApiFuture<TeamFolder> future = dataformClient.getTeamFolderCallable().futureCall(request);
       // Do something.
       TeamFolder response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[GetTeamFolderRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataform/latest/com.google.cloud.dataform.v1beta1.GetTeamFolderRequest),[TeamFolder](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataform/latest/com.google.cloud.dataform.v1beta1.TeamFolder)>` |   
  
### getWorkflowConfig(@Nullable WorkflowConfigName name)
    
    
    public final WorkflowConfig getWorkflowConfig(@Nullable WorkflowConfigName name)

Fetches a single WorkflowConfig.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DataformClient dataformClient = DataformClient.create()) {
       WorkflowConfigName name =
           WorkflowConfigName.of("[PROJECT]", "[LOCATION]", "[REPOSITORY]", "[WORKFLOW_CONFIG]");
       WorkflowConfig response = dataformClient.getWorkflowConfig(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `@org.jspecify.annotations.Nullable com.google.cloud.dataform.v1beta1.WorkflowConfigName`  
Required. The workflow config's name.  
**Returns**  
---  
**Type** | **Description**  
`[WorkflowConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataform/latest/com.google.cloud.dataform.v1beta1.WorkflowConfig)` |   
  
### getWorkflowConfig(GetWorkflowConfigRequest request)
    
    
    public final WorkflowConfig getWorkflowConfig(GetWorkflowConfigRequest request)

Fetches a single WorkflowConfig.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DataformClient dataformClient = DataformClient.create()) {
       GetWorkflowConfigRequest request =
           GetWorkflowConfigRequest.newBuilder()
               .setName(
                   WorkflowConfigName.of(
                           "[PROJECT]", "[LOCATION]", "[REPOSITORY]", "[WORKFLOW_CONFIG]")
                       .toString())
               .build();
       WorkflowConfig response = dataformClient.getWorkflowConfig(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[GetWorkflowConfigRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataform/latest/com.google.cloud.dataform.v1beta1.GetWorkflowConfigRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[WorkflowConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataform/latest/com.google.cloud.dataform.v1beta1.WorkflowConfig)` |   
  
### getWorkflowConfig(String name)
    
    
    public final WorkflowConfig getWorkflowConfig(String name)

Fetches a single WorkflowConfig.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DataformClient dataformClient = DataformClient.create()) {
       String name =
           WorkflowConfigName.of("[PROJECT]", "[LOCATION]", "[REPOSITORY]", "[WORKFLOW_CONFIG]")
               .toString();
       WorkflowConfig response = dataformClient.getWorkflowConfig(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The workflow config's name.  
**Returns**  
---  
**Type** | **Description**  
`[WorkflowConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataform/latest/com.google.cloud.dataform.v1beta1.WorkflowConfig)` |   
  
### getWorkflowConfigCallable()
    
    
    public final UnaryCallable<GetWorkflowConfigRequest,WorkflowConfig> getWorkflowConfigCallable()

Fetches a single WorkflowConfig.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DataformClient dataformClient = DataformClient.create()) {
       GetWorkflowConfigRequest request =
           GetWorkflowConfigRequest.newBuilder()
               .setName(
                   WorkflowConfigName.of(
                           "[PROJECT]", "[LOCATION]", "[REPOSITORY]", "[WORKFLOW_CONFIG]")
                       .toString())
               .build();
       ApiFuture<WorkflowConfig> future =
           dataformClient.getWorkflowConfigCallable().futureCall(request);
       // Do something.
       WorkflowConfig response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[GetWorkflowConfigRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataform/latest/com.google.cloud.dataform.v1beta1.GetWorkflowConfigRequest),[WorkflowConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataform/latest/com.google.cloud.dataform.v1beta1.WorkflowConfig)>` |   
  
### getWorkflowInvocation(@Nullable WorkflowInvocationName name)
    
    
    public final WorkflowInvocation getWorkflowInvocation(@Nullable WorkflowInvocationName name)

Fetches a single WorkflowInvocation.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DataformClient dataformClient = DataformClient.create()) {
       WorkflowInvocationName name =
           WorkflowInvocationName.of(
               "[PROJECT]", "[LOCATION]", "[REPOSITORY]", "[WORKFLOW_INVOCATION]");
       WorkflowInvocation response = dataformClient.getWorkflowInvocation(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `@org.jspecify.annotations.Nullable com.google.cloud.dataform.v1beta1.WorkflowInvocationName`  
Required. The workflow invocation resource's name.  
**Returns**  
---  
**Type** | **Description**  
`[WorkflowInvocation](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataform/latest/com.google.cloud.dataform.v1beta1.WorkflowInvocation)` |   
  
### getWorkflowInvocation(GetWorkflowInvocationRequest request)
    
    
    public final WorkflowInvocation getWorkflowInvocation(GetWorkflowInvocationRequest request)

Fetches a single WorkflowInvocation.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DataformClient dataformClient = DataformClient.create()) {
       GetWorkflowInvocationRequest request =
           GetWorkflowInvocationRequest.newBuilder()
               .setName(
                   WorkflowInvocationName.of(
                           "[PROJECT]", "[LOCATION]", "[REPOSITORY]", "[WORKFLOW_INVOCATION]")
                       .toString())
               .build();
       WorkflowInvocation response = dataformClient.getWorkflowInvocation(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[GetWorkflowInvocationRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataform/latest/com.google.cloud.dataform.v1beta1.GetWorkflowInvocationRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[WorkflowInvocation](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataform/latest/com.google.cloud.dataform.v1beta1.WorkflowInvocation)` |   
  
### getWorkflowInvocation(String name)
    
    
    public final WorkflowInvocation getWorkflowInvocation(String name)

Fetches a single WorkflowInvocation.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DataformClient dataformClient = DataformClient.create()) {
       String name =
           WorkflowInvocationName.of(
                   "[PROJECT]", "[LOCATION]", "[REPOSITORY]", "[WORKFLOW_INVOCATION]")
               .toString();
       WorkflowInvocation response = dataformClient.getWorkflowInvocation(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The workflow invocation resource's name.  
**Returns**  
---  
**Type** | **Description**  
`[WorkflowInvocation](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataform/latest/com.google.cloud.dataform.v1beta1.WorkflowInvocation)` |   
  
### getWorkflowInvocationCallable()
    
    
    public final UnaryCallable<GetWorkflowInvocationRequest,WorkflowInvocation> getWorkflowInvocationCallable()

Fetches a single WorkflowInvocation.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DataformClient dataformClient = DataformClient.create()) {
       GetWorkflowInvocationRequest request =
           GetWorkflowInvocationRequest.newBuilder()
               .setName(
                   WorkflowInvocationName.of(
                           "[PROJECT]", "[LOCATION]", "[REPOSITORY]", "[WORKFLOW_INVOCATION]")
                       .toString())
               .build();
       ApiFuture<WorkflowInvocation> future =
           dataformClient.getWorkflowInvocationCallable().futureCall(request);
       // Do something.
       WorkflowInvocation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[GetWorkflowInvocationRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataform/latest/com.google.cloud.dataform.v1beta1.GetWorkflowInvocationRequest),[WorkflowInvocation](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataform/latest/com.google.cloud.dataform.v1beta1.WorkflowInvocation)>` |   
  
### getWorkspace(@Nullable WorkspaceName name)
    
    
    public final Workspace getWorkspace(@Nullable WorkspaceName name)

Fetches a single Workspace.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DataformClient dataformClient = DataformClient.create()) {
       WorkspaceName name =
           WorkspaceName.of("[PROJECT]", "[LOCATION]", "[REPOSITORY]", "[WORKSPACE]");
       Workspace response = dataformClient.getWorkspace(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `@org.jspecify.annotations.Nullable com.google.cloud.dataform.v1beta1.WorkspaceName`  
Required. The workspace's name.  
**Returns**  
---  
**Type** | **Description**  
`[Workspace](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataform/latest/com.google.cloud.dataform.v1beta1.Workspace)` |   
  
### getWorkspace(GetWorkspaceRequest request)
    
    
    public final Workspace getWorkspace(GetWorkspaceRequest request)

Fetches a single Workspace.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DataformClient dataformClient = DataformClient.create()) {
       GetWorkspaceRequest request =
           GetWorkspaceRequest.newBuilder()
               .setName(
                   WorkspaceName.of("[PROJECT]", "[LOCATION]", "[REPOSITORY]", "[WORKSPACE]")
                       .toString())
               .build();
       Workspace response = dataformClient.getWorkspace(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[GetWorkspaceRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataform/latest/com.google.cloud.dataform.v1beta1.GetWorkspaceRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[Workspace](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataform/latest/com.google.cloud.dataform.v1beta1.Workspace)` |   
  
### getWorkspace(String name)
    
    
    public final Workspace getWorkspace(String name)

Fetches a single Workspace.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DataformClient dataformClient = DataformClient.create()) {
       String name =
           WorkspaceName.of("[PROJECT]", "[LOCATION]", "[REPOSITORY]", "[WORKSPACE]").toString();
       Workspace response = dataformClient.getWorkspace(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The workspace's name.  
**Returns**  
---  
**Type** | **Description**  
`[Workspace](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataform/latest/com.google.cloud.dataform.v1beta1.Workspace)` |   
  
### getWorkspaceCallable()
    
    
    public final UnaryCallable<GetWorkspaceRequest,Workspace> getWorkspaceCallable()

Fetches a single Workspace.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DataformClient dataformClient = DataformClient.create()) {
       GetWorkspaceRequest request =
           GetWorkspaceRequest.newBuilder()
               .setName(
                   WorkspaceName.of("[PROJECT]", "[LOCATION]", "[REPOSITORY]", "[WORKSPACE]")
                       .toString())
               .build();
       ApiFuture<Workspace> future = dataformClient.getWorkspaceCallable().futureCall(request);
       // Do something.
       Workspace response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[GetWorkspaceRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataform/latest/com.google.cloud.dataform.v1beta1.GetWorkspaceRequest),[Workspace](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataform/latest/com.google.cloud.dataform.v1beta1.Workspace)>` |   
  
### installNpmPackages(InstallNpmPackagesRequest request)
    
    
    public final InstallNpmPackagesResponse installNpmPackages(InstallNpmPackagesRequest request)

Installs dependency NPM packages (inside a Workspace).

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DataformClient dataformClient = DataformClient.create()) {
       InstallNpmPackagesRequest request =
           InstallNpmPackagesRequest.newBuilder()
               .setWorkspace(
                   WorkspaceName.of("[PROJECT]", "[LOCATION]", "[REPOSITORY]", "[WORKSPACE]")
                       .toString())
               .setPipelineConfig(PipelineConfig.newBuilder().build())
               .build();
       InstallNpmPackagesResponse response = dataformClient.installNpmPackages(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[InstallNpmPackagesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataform/latest/com.google.cloud.dataform.v1beta1.InstallNpmPackagesRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[InstallNpmPackagesResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataform/latest/com.google.cloud.dataform.v1beta1.InstallNpmPackagesResponse)` |   
  
### installNpmPackagesCallable()
    
    
    public final UnaryCallable<InstallNpmPackagesRequest,InstallNpmPackagesResponse> installNpmPackagesCallable()

Installs dependency NPM packages (inside a Workspace).

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DataformClient dataformClient = DataformClient.create()) {
       InstallNpmPackagesRequest request =
           InstallNpmPackagesRequest.newBuilder()
               .setWorkspace(
                   WorkspaceName.of("[PROJECT]", "[LOCATION]", "[REPOSITORY]", "[WORKSPACE]")
                       .toString())
               .setPipelineConfig(PipelineConfig.newBuilder().build())
               .build();
       ApiFuture<InstallNpmPackagesResponse> future =
           dataformClient.installNpmPackagesCallable().futureCall(request);
       // Do something.
       InstallNpmPackagesResponse response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[InstallNpmPackagesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataform/latest/com.google.cloud.dataform.v1beta1.InstallNpmPackagesRequest),[InstallNpmPackagesResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataform/latest/com.google.cloud.dataform.v1beta1.InstallNpmPackagesResponse)>` |   
  
### isShutdown()
    
    
    public boolean isShutdown()

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` |   
  
### isTerminated()
    
    
    public boolean isTerminated()

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` |   
  
### listCompilationResults(@Nullable RepositoryName parent)
    
    
    public final DataformClient.ListCompilationResultsPagedResponse listCompilationResults(@Nullable RepositoryName parent)

Lists CompilationResults in a given Repository.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DataformClient dataformClient = DataformClient.create()) {
       RepositoryName parent = RepositoryName.of("[PROJECT]", "[LOCATION]", "[REPOSITORY]");
       for (CompilationResult element : dataformClient.listCompilationResults(parent).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`parent` | `@org.jspecify.annotations.Nullable com.google.cloud.dataform.v1beta1.RepositoryName`  
Required. The repository in which to list compilation results. Must be in the format `projects/*/locations/*/repositories/*`.  
**Returns**  
---  
**Type** | **Description**  
`[DataformClient.ListCompilationResultsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataform/latest/com.google.cloud.dataform.v1beta1.DataformClient.ListCompilationResultsPagedResponse)` |   
  
### listCompilationResults(ListCompilationResultsRequest request)
    
    
    public final DataformClient.ListCompilationResultsPagedResponse listCompilationResults(ListCompilationResultsRequest request)

Lists CompilationResults in a given Repository.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DataformClient dataformClient = DataformClient.create()) {
       ListCompilationResultsRequest request =
           ListCompilationResultsRequest.newBuilder()
               .setParent(RepositoryName.of("[PROJECT]", "[LOCATION]", "[REPOSITORY]").toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .setOrderBy("orderBy-1207110587")
               .setFilter("filter-1274492040")
               .build();
       for (CompilationResult element :
           dataformClient.listCompilationResults(request).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[ListCompilationResultsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataform/latest/com.google.cloud.dataform.v1beta1.ListCompilationResultsRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[DataformClient.ListCompilationResultsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataform/latest/com.google.cloud.dataform.v1beta1.DataformClient.ListCompilationResultsPagedResponse)` |   
  
### listCompilationResults(String parent)
    
    
    public final DataformClient.ListCompilationResultsPagedResponse listCompilationResults(String parent)

Lists CompilationResults in a given Repository.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DataformClient dataformClient = DataformClient.create()) {
       String parent = RepositoryName.of("[PROJECT]", "[LOCATION]", "[REPOSITORY]").toString();
       for (CompilationResult element : dataformClient.listCompilationResults(parent).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`parent` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The repository in which to list compilation results. Must be in the format `projects/*/locations/*/repositories/*`.  
**Returns**  
---  
**Type** | **Description**  
`[DataformClient.ListCompilationResultsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataform/latest/com.google.cloud.dataform.v1beta1.DataformClient.ListCompilationResultsPagedResponse)` |   
  
### listCompilationResultsCallable()
    
    
    public final UnaryCallable<ListCompilationResultsRequest,ListCompilationResultsResponse> listCompilationResultsCallable()

Lists CompilationResults in a given Repository.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DataformClient dataformClient = DataformClient.create()) {
       ListCompilationResultsRequest request =
           ListCompilationResultsRequest.newBuilder()
               .setParent(RepositoryName.of("[PROJECT]", "[LOCATION]", "[REPOSITORY]").toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .setOrderBy("orderBy-1207110587")
               .setFilter("filter-1274492040")
               .build();
       while (true) {
         ListCompilationResultsResponse response =
             dataformClient.listCompilationResultsCallable().call(request);
         for (CompilationResult element : response.getCompilationResultsList()) {
           // doThingsWith(element);
         }
         String nextPageToken = response.getNextPageToken();
         if (!Strings.isNullOrEmpty(nextPageToken)) {
           request = request.toBuilder().setPageToken(nextPageToken).build();
         } else {
           break;
         }
       }
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListCompilationResultsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataform/latest/com.google.cloud.dataform.v1beta1.ListCompilationResultsRequest),[ListCompilationResultsResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataform/latest/com.google.cloud.dataform.v1beta1.ListCompilationResultsResponse)>` |   
  
### listCompilationResultsPagedCallable()
    
    
    public final UnaryCallable<ListCompilationResultsRequest,DataformClient.ListCompilationResultsPagedResponse> listCompilationResultsPagedCallable()

Lists CompilationResults in a given Repository.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DataformClient dataformClient = DataformClient.create()) {
       ListCompilationResultsRequest request =
           ListCompilationResultsRequest.newBuilder()
               .setParent(RepositoryName.of("[PROJECT]", "[LOCATION]", "[REPOSITORY]").toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .setOrderBy("orderBy-1207110587")
               .setFilter("filter-1274492040")
               .build();
       ApiFuture<CompilationResult> future =
           dataformClient.listCompilationResultsPagedCallable().futureCall(request);
       // Do something.
       for (CompilationResult element : future.get().iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListCompilationResultsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataform/latest/com.google.cloud.dataform.v1beta1.ListCompilationResultsRequest),[ListCompilationResultsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataform/latest/com.google.cloud.dataform.v1beta1.DataformClient.ListCompilationResultsPagedResponse)>` |   
  
### listLocations(ListLocationsRequest request)
    
    
    public final DataformClient.ListLocationsPagedResponse listLocations(ListLocationsRequest request)

Lists information about the supported locations for this service.

This method lists locations based on the resource scope provided inthe ListLocationsRequest.name field: ***Global locations**: If `name` is empty, the method lists thepublic locations available to all projects. * **Project-specificlocations**: If `name` follows the format`projects/{project}`, the method lists locations visible to thatspecific project. This includes public, private, or otherproject-specific locations enabled for the project.

For gRPC and client library implementations, the resource name ispassed as the `name` field. For direct service calls, the resourcename isincorporated into the request path based on the specific serviceimplementation and version.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DataformClient dataformClient = DataformClient.create()) {
       ListLocationsRequest request =
           ListLocationsRequest.newBuilder()
               .setName("name3373707")
               .setFilter("filter-1274492040")
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .build();
       for (Location element : dataformClient.listLocations(request).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `com.google.cloud.location.ListLocationsRequest`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[DataformClient.ListLocationsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataform/latest/com.google.cloud.dataform.v1beta1.DataformClient.ListLocationsPagedResponse)` |   
  
### listLocationsCallable()
    
    
    public final UnaryCallable<ListLocationsRequest,ListLocationsResponse> listLocationsCallable()

Lists information about the supported locations for this service.

This method lists locations based on the resource scope provided inthe ListLocationsRequest.name field: ***Global locations**: If `name` is empty, the method lists thepublic locations available to all projects. * **Project-specificlocations**: If `name` follows the format`projects/{project}`, the method lists locations visible to thatspecific project. This includes public, private, or otherproject-specific locations enabled for the project.

For gRPC and client library implementations, the resource name ispassed as the `name` field. For direct service calls, the resourcename isincorporated into the request path based on the specific serviceimplementation and version.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DataformClient dataformClient = DataformClient.create()) {
       ListLocationsRequest request =
           ListLocationsRequest.newBuilder()
               .setName("name3373707")
               .setFilter("filter-1274492040")
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .build();
       while (true) {
         ListLocationsResponse response = dataformClient.listLocationsCallable().call(request);
         for (Location element : response.getLocationsList()) {
           // doThingsWith(element);
         }
         String nextPageToken = response.getNextPageToken();
         if (!Strings.isNullOrEmpty(nextPageToken)) {
           request = request.toBuilder().setPageToken(nextPageToken).build();
         } else {
           break;
         }
       }
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<com.google.cloud.location.ListLocationsRequest,com.google.cloud.location.ListLocationsResponse>` |   
  
### listLocationsPagedCallable()
    
    
    public final UnaryCallable<ListLocationsRequest,DataformClient.ListLocationsPagedResponse> listLocationsPagedCallable()

Lists information about the supported locations for this service.

This method lists locations based on the resource scope provided inthe ListLocationsRequest.name field: ***Global locations**: If `name` is empty, the method lists thepublic locations available to all projects. * **Project-specificlocations**: If `name` follows the format`projects/{project}`, the method lists locations visible to thatspecific project. This includes public, private, or otherproject-specific locations enabled for the project.

For gRPC and client library implementations, the resource name ispassed as the `name` field. For direct service calls, the resourcename isincorporated into the request path based on the specific serviceimplementation and version.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DataformClient dataformClient = DataformClient.create()) {
       ListLocationsRequest request =
           ListLocationsRequest.newBuilder()
               .setName("name3373707")
               .setFilter("filter-1274492040")
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .build();
       ApiFuture<Location> future = dataformClient.listLocationsPagedCallable().futureCall(request);
       // Do something.
       for (Location element : future.get().iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<com.google.cloud.location.ListLocationsRequest,[ListLocationsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataform/latest/com.google.cloud.dataform.v1beta1.DataformClient.ListLocationsPagedResponse)>` |   
  
### listReleaseConfigs(@Nullable RepositoryName parent)
    
    
    public final DataformClient.ListReleaseConfigsPagedResponse listReleaseConfigs(@Nullable RepositoryName parent)

Lists ReleaseConfigs in a given Repository.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DataformClient dataformClient = DataformClient.create()) {
       RepositoryName parent = RepositoryName.of("[PROJECT]", "[LOCATION]", "[REPOSITORY]");
       for (ReleaseConfig element : dataformClient.listReleaseConfigs(parent).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`parent` | `@org.jspecify.annotations.Nullable com.google.cloud.dataform.v1beta1.RepositoryName`  
Required. The repository in which to list release configs. Must be in the format `projects/*/locations/*/repositories/*`.  
**Returns**  
---  
**Type** | **Description**  
`[DataformClient.ListReleaseConfigsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataform/latest/com.google.cloud.dataform.v1beta1.DataformClient.ListReleaseConfigsPagedResponse)` |   
  
### listReleaseConfigs(ListReleaseConfigsRequest request)
    
    
    public final DataformClient.ListReleaseConfigsPagedResponse listReleaseConfigs(ListReleaseConfigsRequest request)

Lists ReleaseConfigs in a given Repository.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DataformClient dataformClient = DataformClient.create()) {
       ListReleaseConfigsRequest request =
           ListReleaseConfigsRequest.newBuilder()
               .setParent(RepositoryName.of("[PROJECT]", "[LOCATION]", "[REPOSITORY]").toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .build();
       for (ReleaseConfig element : dataformClient.listReleaseConfigs(request).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[ListReleaseConfigsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataform/latest/com.google.cloud.dataform.v1beta1.ListReleaseConfigsRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[DataformClient.ListReleaseConfigsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataform/latest/com.google.cloud.dataform.v1beta1.DataformClient.ListReleaseConfigsPagedResponse)` |   
  
### listReleaseConfigs(String parent)
    
    
    public final DataformClient.ListReleaseConfigsPagedResponse listReleaseConfigs(String parent)

Lists ReleaseConfigs in a given Repository.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DataformClient dataformClient = DataformClient.create()) {
       String parent = RepositoryName.of("[PROJECT]", "[LOCATION]", "[REPOSITORY]").toString();
       for (ReleaseConfig element : dataformClient.listReleaseConfigs(parent).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`parent` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The repository in which to list release configs. Must be in the format `projects/*/locations/*/repositories/*`.  
**Returns**  
---  
**Type** | **Description**  
`[DataformClient.ListReleaseConfigsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataform/latest/com.google.cloud.dataform.v1beta1.DataformClient.ListReleaseConfigsPagedResponse)` |   
  
### listReleaseConfigsCallable()
    
    
    public final UnaryCallable<ListReleaseConfigsRequest,ListReleaseConfigsResponse> listReleaseConfigsCallable()

Lists ReleaseConfigs in a given Repository.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DataformClient dataformClient = DataformClient.create()) {
       ListReleaseConfigsRequest request =
           ListReleaseConfigsRequest.newBuilder()
               .setParent(RepositoryName.of("[PROJECT]", "[LOCATION]", "[REPOSITORY]").toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .build();
       while (true) {
         ListReleaseConfigsResponse response =
             dataformClient.listReleaseConfigsCallable().call(request);
         for (ReleaseConfig element : response.getReleaseConfigsList()) {
           // doThingsWith(element);
         }
         String nextPageToken = response.getNextPageToken();
         if (!Strings.isNullOrEmpty(nextPageToken)) {
           request = request.toBuilder().setPageToken(nextPageToken).build();
         } else {
           break;
         }
       }
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListReleaseConfigsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataform/latest/com.google.cloud.dataform.v1beta1.ListReleaseConfigsRequest),[ListReleaseConfigsResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataform/latest/com.google.cloud.dataform.v1beta1.ListReleaseConfigsResponse)>` |   
  
### listReleaseConfigsPagedCallable()
    
    
    public final UnaryCallable<ListReleaseConfigsRequest,DataformClient.ListReleaseConfigsPagedResponse> listReleaseConfigsPagedCallable()

Lists ReleaseConfigs in a given Repository.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DataformClient dataformClient = DataformClient.create()) {
       ListReleaseConfigsRequest request =
           ListReleaseConfigsRequest.newBuilder()
               .setParent(RepositoryName.of("[PROJECT]", "[LOCATION]", "[REPOSITORY]").toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .build();
       ApiFuture<ReleaseConfig> future =
           dataformClient.listReleaseConfigsPagedCallable().futureCall(request);
       // Do something.
       for (ReleaseConfig element : future.get().iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListReleaseConfigsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataform/latest/com.google.cloud.dataform.v1beta1.ListReleaseConfigsRequest),[ListReleaseConfigsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataform/latest/com.google.cloud.dataform.v1beta1.DataformClient.ListReleaseConfigsPagedResponse)>` |   
  
### listRepositories(@Nullable LocationName parent)
    
    
    public final DataformClient.ListRepositoriesPagedResponse listRepositories(@Nullable LocationName parent)

Lists Repositories in a given project and location.

**Note:** *This method can return repositories not shown in the [Dataform UI](https://console.cloud.google.com/bigquery/dataform)*.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DataformClient dataformClient = DataformClient.create()) {
       LocationName parent = LocationName.of("[PROJECT]", "[LOCATION]");
       for (Repository element : dataformClient.listRepositories(parent).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`parent` | `@org.jspecify.annotations.Nullable com.google.cloud.dataform.v1beta1.LocationName`  
Required. The location in which to list repositories. Must be in the format `projects/*/locations/*`.  
**Returns**  
---  
**Type** | **Description**  
`[DataformClient.ListRepositoriesPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataform/latest/com.google.cloud.dataform.v1beta1.DataformClient.ListRepositoriesPagedResponse)` |   
  
### listRepositories(ListRepositoriesRequest request)
    
    
    public final DataformClient.ListRepositoriesPagedResponse listRepositories(ListRepositoriesRequest request)

Lists Repositories in a given project and location.

**Note:** *This method can return repositories not shown in the [Dataform UI](https://console.cloud.google.com/bigquery/dataform)*.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DataformClient dataformClient = DataformClient.create()) {
       ListRepositoriesRequest request =
           ListRepositoriesRequest.newBuilder()
               .setParent(LocationName.of("[PROJECT]", "[LOCATION]").toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .setOrderBy("orderBy-1207110587")
               .setFilter("filter-1274492040")
               .build();
       for (Repository element : dataformClient.listRepositories(request).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[ListRepositoriesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataform/latest/com.google.cloud.dataform.v1beta1.ListRepositoriesRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[DataformClient.ListRepositoriesPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataform/latest/com.google.cloud.dataform.v1beta1.DataformClient.ListRepositoriesPagedResponse)` |   
  
### listRepositories(String parent)
    
    
    public final DataformClient.ListRepositoriesPagedResponse listRepositories(String parent)

Lists Repositories in a given project and location.

**Note:** *This method can return repositories not shown in the [Dataform UI](https://console.cloud.google.com/bigquery/dataform)*.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DataformClient dataformClient = DataformClient.create()) {
       String parent = LocationName.of("[PROJECT]", "[LOCATION]").toString();
       for (Repository element : dataformClient.listRepositories(parent).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`parent` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The location in which to list repositories. Must be in the format `projects/*/locations/*`.  
**Returns**  
---  
**Type** | **Description**  
`[DataformClient.ListRepositoriesPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataform/latest/com.google.cloud.dataform.v1beta1.DataformClient.ListRepositoriesPagedResponse)` |   
  
### listRepositoriesCallable()
    
    
    public final UnaryCallable<ListRepositoriesRequest,ListRepositoriesResponse> listRepositoriesCallable()

Lists Repositories in a given project and location.

**Note:** *This method can return repositories not shown in the [Dataform UI](https://console.cloud.google.com/bigquery/dataform)*.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DataformClient dataformClient = DataformClient.create()) {
       ListRepositoriesRequest request =
           ListRepositoriesRequest.newBuilder()
               .setParent(LocationName.of("[PROJECT]", "[LOCATION]").toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .setOrderBy("orderBy-1207110587")
               .setFilter("filter-1274492040")
               .build();
       while (true) {
         ListRepositoriesResponse response = dataformClient.listRepositoriesCallable().call(request);
         for (Repository element : response.getRepositoriesList()) {
           // doThingsWith(element);
         }
         String nextPageToken = response.getNextPageToken();
         if (!Strings.isNullOrEmpty(nextPageToken)) {
           request = request.toBuilder().setPageToken(nextPageToken).build();
         } else {
           break;
         }
       }
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListRepositoriesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataform/latest/com.google.cloud.dataform.v1beta1.ListRepositoriesRequest),[ListRepositoriesResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataform/latest/com.google.cloud.dataform.v1beta1.ListRepositoriesResponse)>` |   
  
### listRepositoriesPagedCallable()
    
    
    public final UnaryCallable<ListRepositoriesRequest,DataformClient.ListRepositoriesPagedResponse> listRepositoriesPagedCallable()

Lists Repositories in a given project and location.

**Note:** *This method can return repositories not shown in the [Dataform UI](https://console.cloud.google.com/bigquery/dataform)*.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DataformClient dataformClient = DataformClient.create()) {
       ListRepositoriesRequest request =
           ListRepositoriesRequest.newBuilder()
               .setParent(LocationName.of("[PROJECT]", "[LOCATION]").toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .setOrderBy("orderBy-1207110587")
               .setFilter("filter-1274492040")
               .build();
       ApiFuture<Repository> future =
           dataformClient.listRepositoriesPagedCallable().futureCall(request);
       // Do something.
       for (Repository element : future.get().iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListRepositoriesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataform/latest/com.google.cloud.dataform.v1beta1.ListRepositoriesRequest),[ListRepositoriesPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataform/latest/com.google.cloud.dataform.v1beta1.DataformClient.ListRepositoriesPagedResponse)>` |   
  
### listWorkflowConfigs(@Nullable RepositoryName parent)
    
    
    public final DataformClient.ListWorkflowConfigsPagedResponse listWorkflowConfigs(@Nullable RepositoryName parent)

Lists WorkflowConfigs in a given Repository.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DataformClient dataformClient = DataformClient.create()) {
       RepositoryName parent = RepositoryName.of("[PROJECT]", "[LOCATION]", "[REPOSITORY]");
       for (WorkflowConfig element : dataformClient.listWorkflowConfigs(parent).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`parent` | `@org.jspecify.annotations.Nullable com.google.cloud.dataform.v1beta1.RepositoryName`  
Required. The repository in which to list workflow configs. Must be in the format `projects/*/locations/*/repositories/*`.  
**Returns**  
---  
**Type** | **Description**  
`[DataformClient.ListWorkflowConfigsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataform/latest/com.google.cloud.dataform.v1beta1.DataformClient.ListWorkflowConfigsPagedResponse)` |   
  
### listWorkflowConfigs(ListWorkflowConfigsRequest request)
    
    
    public final DataformClient.ListWorkflowConfigsPagedResponse listWorkflowConfigs(ListWorkflowConfigsRequest request)

Lists WorkflowConfigs in a given Repository.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DataformClient dataformClient = DataformClient.create()) {
       ListWorkflowConfigsRequest request =
           ListWorkflowConfigsRequest.newBuilder()
               .setParent(RepositoryName.of("[PROJECT]", "[LOCATION]", "[REPOSITORY]").toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .build();
       for (WorkflowConfig element : dataformClient.listWorkflowConfigs(request).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[ListWorkflowConfigsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataform/latest/com.google.cloud.dataform.v1beta1.ListWorkflowConfigsRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[DataformClient.ListWorkflowConfigsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataform/latest/com.google.cloud.dataform.v1beta1.DataformClient.ListWorkflowConfigsPagedResponse)` |   
  
### listWorkflowConfigs(String parent)
    
    
    public final DataformClient.ListWorkflowConfigsPagedResponse listWorkflowConfigs(String parent)

Lists WorkflowConfigs in a given Repository.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DataformClient dataformClient = DataformClient.create()) {
       String parent = RepositoryName.of("[PROJECT]", "[LOCATION]", "[REPOSITORY]").toString();
       for (WorkflowConfig element : dataformClient.listWorkflowConfigs(parent).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`parent` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The repository in which to list workflow configs. Must be in the format `projects/*/locations/*/repositories/*`.  
**Returns**  
---  
**Type** | **Description**  
`[DataformClient.ListWorkflowConfigsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataform/latest/com.google.cloud.dataform.v1beta1.DataformClient.ListWorkflowConfigsPagedResponse)` |   
  
### listWorkflowConfigsCallable()
    
    
    public final UnaryCallable<ListWorkflowConfigsRequest,ListWorkflowConfigsResponse> listWorkflowConfigsCallable()

Lists WorkflowConfigs in a given Repository.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DataformClient dataformClient = DataformClient.create()) {
       ListWorkflowConfigsRequest request =
           ListWorkflowConfigsRequest.newBuilder()
               .setParent(RepositoryName.of("[PROJECT]", "[LOCATION]", "[REPOSITORY]").toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .build();
       while (true) {
         ListWorkflowConfigsResponse response =
             dataformClient.listWorkflowConfigsCallable().call(request);
         for (WorkflowConfig element : response.getWorkflowConfigsList()) {
           // doThingsWith(element);
         }
         String nextPageToken = response.getNextPageToken();
         if (!Strings.isNullOrEmpty(nextPageToken)) {
           request = request.toBuilder().setPageToken(nextPageToken).build();
         } else {
           break;
         }
       }
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListWorkflowConfigsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataform/latest/com.google.cloud.dataform.v1beta1.ListWorkflowConfigsRequest),[ListWorkflowConfigsResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataform/latest/com.google.cloud.dataform.v1beta1.ListWorkflowConfigsResponse)>` |   
  
### listWorkflowConfigsPagedCallable()
    
    
    public final UnaryCallable<ListWorkflowConfigsRequest,DataformClient.ListWorkflowConfigsPagedResponse> listWorkflowConfigsPagedCallable()

Lists WorkflowConfigs in a given Repository.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DataformClient dataformClient = DataformClient.create()) {
       ListWorkflowConfigsRequest request =
           ListWorkflowConfigsRequest.newBuilder()
               .setParent(RepositoryName.of("[PROJECT]", "[LOCATION]", "[REPOSITORY]").toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .build();
       ApiFuture<WorkflowConfig> future =
           dataformClient.listWorkflowConfigsPagedCallable().futureCall(request);
       // Do something.
       for (WorkflowConfig element : future.get().iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListWorkflowConfigsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataform/latest/com.google.cloud.dataform.v1beta1.ListWorkflowConfigsRequest),[ListWorkflowConfigsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataform/latest/com.google.cloud.dataform.v1beta1.DataformClient.ListWorkflowConfigsPagedResponse)>` |   
  
### listWorkflowInvocations(@Nullable RepositoryName parent)
    
    
    public final DataformClient.ListWorkflowInvocationsPagedResponse listWorkflowInvocations(@Nullable RepositoryName parent)

Lists WorkflowInvocations in a given Repository.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DataformClient dataformClient = DataformClient.create()) {
       RepositoryName parent = RepositoryName.of("[PROJECT]", "[LOCATION]", "[REPOSITORY]");
       for (WorkflowInvocation element :
           dataformClient.listWorkflowInvocations(parent).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`parent` | `@org.jspecify.annotations.Nullable com.google.cloud.dataform.v1beta1.RepositoryName`  
Required. The parent resource of the WorkflowInvocation type. Must be in the format `projects/*/locations/*/repositories/*`.  
**Returns**  
---  
**Type** | **Description**  
`[DataformClient.ListWorkflowInvocationsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataform/latest/com.google.cloud.dataform.v1beta1.DataformClient.ListWorkflowInvocationsPagedResponse)` |   
  
### listWorkflowInvocations(ListWorkflowInvocationsRequest request)
    
    
    public final DataformClient.ListWorkflowInvocationsPagedResponse listWorkflowInvocations(ListWorkflowInvocationsRequest request)

Lists WorkflowInvocations in a given Repository.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DataformClient dataformClient = DataformClient.create()) {
       ListWorkflowInvocationsRequest request =
           ListWorkflowInvocationsRequest.newBuilder()
               .setParent(RepositoryName.of("[PROJECT]", "[LOCATION]", "[REPOSITORY]").toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .setOrderBy("orderBy-1207110587")
               .setFilter("filter-1274492040")
               .build();
       for (WorkflowInvocation element :
           dataformClient.listWorkflowInvocations(request).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[ListWorkflowInvocationsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataform/latest/com.google.cloud.dataform.v1beta1.ListWorkflowInvocationsRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[DataformClient.ListWorkflowInvocationsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataform/latest/com.google.cloud.dataform.v1beta1.DataformClient.ListWorkflowInvocationsPagedResponse)` |   
  
### listWorkflowInvocations(String parent)
    
    
    public final DataformClient.ListWorkflowInvocationsPagedResponse listWorkflowInvocations(String parent)

Lists WorkflowInvocations in a given Repository.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DataformClient dataformClient = DataformClient.create()) {
       String parent = RepositoryName.of("[PROJECT]", "[LOCATION]", "[REPOSITORY]").toString();
       for (WorkflowInvocation element :
           dataformClient.listWorkflowInvocations(parent).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`parent` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The parent resource of the WorkflowInvocation type. Must be in the format `projects/*/locations/*/repositories/*`.  
**Returns**  
---  
**Type** | **Description**  
`[DataformClient.ListWorkflowInvocationsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataform/latest/com.google.cloud.dataform.v1beta1.DataformClient.ListWorkflowInvocationsPagedResponse)` |   
  
### listWorkflowInvocationsCallable()
    
    
    public final UnaryCallable<ListWorkflowInvocationsRequest,ListWorkflowInvocationsResponse> listWorkflowInvocationsCallable()

Lists WorkflowInvocations in a given Repository.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DataformClient dataformClient = DataformClient.create()) {
       ListWorkflowInvocationsRequest request =
           ListWorkflowInvocationsRequest.newBuilder()
               .setParent(RepositoryName.of("[PROJECT]", "[LOCATION]", "[REPOSITORY]").toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .setOrderBy("orderBy-1207110587")
               .setFilter("filter-1274492040")
               .build();
       while (true) {
         ListWorkflowInvocationsResponse response =
             dataformClient.listWorkflowInvocationsCallable().call(request);
         for (WorkflowInvocation element : response.getWorkflowInvocationsList()) {
           // doThingsWith(element);
         }
         String nextPageToken = response.getNextPageToken();
         if (!Strings.isNullOrEmpty(nextPageToken)) {
           request = request.toBuilder().setPageToken(nextPageToken).build();
         } else {
           break;
         }
       }
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListWorkflowInvocationsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataform/latest/com.google.cloud.dataform.v1beta1.ListWorkflowInvocationsRequest),[ListWorkflowInvocationsResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataform/latest/com.google.cloud.dataform.v1beta1.ListWorkflowInvocationsResponse)>` |   
  
### listWorkflowInvocationsPagedCallable()
    
    
    public final UnaryCallable<ListWorkflowInvocationsRequest,DataformClient.ListWorkflowInvocationsPagedResponse> listWorkflowInvocationsPagedCallable()

Lists WorkflowInvocations in a given Repository.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DataformClient dataformClient = DataformClient.create()) {
       ListWorkflowInvocationsRequest request =
           ListWorkflowInvocationsRequest.newBuilder()
               .setParent(RepositoryName.of("[PROJECT]", "[LOCATION]", "[REPOSITORY]").toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .setOrderBy("orderBy-1207110587")
               .setFilter("filter-1274492040")
               .build();
       ApiFuture<WorkflowInvocation> future =
           dataformClient.listWorkflowInvocationsPagedCallable().futureCall(request);
       // Do something.
       for (WorkflowInvocation element : future.get().iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListWorkflowInvocationsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataform/latest/com.google.cloud.dataform.v1beta1.ListWorkflowInvocationsRequest),[ListWorkflowInvocationsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataform/latest/com.google.cloud.dataform.v1beta1.DataformClient.ListWorkflowInvocationsPagedResponse)>` |   
  
### listWorkspaces(@Nullable RepositoryName parent)
    
    
    public final DataformClient.ListWorkspacesPagedResponse listWorkspaces(@Nullable RepositoryName parent)

Lists Workspaces in a given Repository.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DataformClient dataformClient = DataformClient.create()) {
       RepositoryName parent = RepositoryName.of("[PROJECT]", "[LOCATION]", "[REPOSITORY]");
       for (Workspace element : dataformClient.listWorkspaces(parent).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`parent` | `@org.jspecify.annotations.Nullable com.google.cloud.dataform.v1beta1.RepositoryName`  
Required. The repository in which to list workspaces. Must be in the format `projects/*/locations/*/repositories/*`.  
**Returns**  
---  
**Type** | **Description**  
`[DataformClient.ListWorkspacesPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataform/latest/com.google.cloud.dataform.v1beta1.DataformClient.ListWorkspacesPagedResponse)` |   
  
### listWorkspaces(ListWorkspacesRequest request)
    
    
    public final DataformClient.ListWorkspacesPagedResponse listWorkspaces(ListWorkspacesRequest request)

Lists Workspaces in a given Repository.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DataformClient dataformClient = DataformClient.create()) {
       ListWorkspacesRequest request =
           ListWorkspacesRequest.newBuilder()
               .setParent(RepositoryName.of("[PROJECT]", "[LOCATION]", "[REPOSITORY]").toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .setOrderBy("orderBy-1207110587")
               .setFilter("filter-1274492040")
               .build();
       for (Workspace element : dataformClient.listWorkspaces(request).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[ListWorkspacesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataform/latest/com.google.cloud.dataform.v1beta1.ListWorkspacesRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[DataformClient.ListWorkspacesPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataform/latest/com.google.cloud.dataform.v1beta1.DataformClient.ListWorkspacesPagedResponse)` |   
  
### listWorkspaces(String parent)
    
    
    public final DataformClient.ListWorkspacesPagedResponse listWorkspaces(String parent)

Lists Workspaces in a given Repository.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DataformClient dataformClient = DataformClient.create()) {
       String parent = RepositoryName.of("[PROJECT]", "[LOCATION]", "[REPOSITORY]").toString();
       for (Workspace element : dataformClient.listWorkspaces(parent).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`parent` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The repository in which to list workspaces. Must be in the format `projects/*/locations/*/repositories/*`.  
**Returns**  
---  
**Type** | **Description**  
`[DataformClient.ListWorkspacesPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataform/latest/com.google.cloud.dataform.v1beta1.DataformClient.ListWorkspacesPagedResponse)` |   
  
### listWorkspacesCallable()
    
    
    public final UnaryCallable<ListWorkspacesRequest,ListWorkspacesResponse> listWorkspacesCallable()

Lists Workspaces in a given Repository.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DataformClient dataformClient = DataformClient.create()) {
       ListWorkspacesRequest request =
           ListWorkspacesRequest.newBuilder()
               .setParent(RepositoryName.of("[PROJECT]", "[LOCATION]", "[REPOSITORY]").toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .setOrderBy("orderBy-1207110587")
               .setFilter("filter-1274492040")
               .build();
       while (true) {
         ListWorkspacesResponse response = dataformClient.listWorkspacesCallable().call(request);
         for (Workspace element : response.getWorkspacesList()) {
           // doThingsWith(element);
         }
         String nextPageToken = response.getNextPageToken();
         if (!Strings.isNullOrEmpty(nextPageToken)) {
           request = request.toBuilder().setPageToken(nextPageToken).build();
         } else {
           break;
         }
       }
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListWorkspacesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataform/latest/com.google.cloud.dataform.v1beta1.ListWorkspacesRequest),[ListWorkspacesResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataform/latest/com.google.cloud.dataform.v1beta1.ListWorkspacesResponse)>` |   
  
### listWorkspacesPagedCallable()
    
    
    public final UnaryCallable<ListWorkspacesRequest,DataformClient.ListWorkspacesPagedResponse> listWorkspacesPagedCallable()

Lists Workspaces in a given Repository.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DataformClient dataformClient = DataformClient.create()) {
       ListWorkspacesRequest request =
           ListWorkspacesRequest.newBuilder()
               .setParent(RepositoryName.of("[PROJECT]", "[LOCATION]", "[REPOSITORY]").toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .setOrderBy("orderBy-1207110587")
               .setFilter("filter-1274492040")
               .build();
       ApiFuture<Workspace> future =
           dataformClient.listWorkspacesPagedCallable().futureCall(request);
       // Do something.
       for (Workspace element : future.get().iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListWorkspacesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataform/latest/com.google.cloud.dataform.v1beta1.ListWorkspacesRequest),[ListWorkspacesPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataform/latest/com.google.cloud.dataform.v1beta1.DataformClient.ListWorkspacesPagedResponse)>` |   
  
### makeDirectory(MakeDirectoryRequest request)
    
    
    public final MakeDirectoryResponse makeDirectory(MakeDirectoryRequest request)

Creates a directory inside a Workspace.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DataformClient dataformClient = DataformClient.create()) {
       MakeDirectoryRequest request =
           MakeDirectoryRequest.newBuilder()
               .setWorkspace(
                   WorkspaceName.of("[PROJECT]", "[LOCATION]", "[REPOSITORY]", "[WORKSPACE]")
                       .toString())
               .setPath("path3433509")
               .build();
       MakeDirectoryResponse response = dataformClient.makeDirectory(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[MakeDirectoryRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataform/latest/com.google.cloud.dataform.v1beta1.MakeDirectoryRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[MakeDirectoryResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataform/latest/com.google.cloud.dataform.v1beta1.MakeDirectoryResponse)` |   
  
### makeDirectoryCallable()
    
    
    public final UnaryCallable<MakeDirectoryRequest,MakeDirectoryResponse> makeDirectoryCallable()

Creates a directory inside a Workspace.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DataformClient dataformClient = DataformClient.create()) {
       MakeDirectoryRequest request =
           MakeDirectoryRequest.newBuilder()
               .setWorkspace(
                   WorkspaceName.of("[PROJECT]", "[LOCATION]", "[REPOSITORY]", "[WORKSPACE]")
                       .toString())
               .setPath("path3433509")
               .build();
       ApiFuture<MakeDirectoryResponse> future =
           dataformClient.makeDirectoryCallable().futureCall(request);
       // Do something.
       MakeDirectoryResponse response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[MakeDirectoryRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataform/latest/com.google.cloud.dataform.v1beta1.MakeDirectoryRequest),[MakeDirectoryResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataform/latest/com.google.cloud.dataform.v1beta1.MakeDirectoryResponse)>` |   
  
### moveDirectory(MoveDirectoryRequest request)
    
    
    public final MoveDirectoryResponse moveDirectory(MoveDirectoryRequest request)

Moves a directory (inside a Workspace), and all of its contents, to a new location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DataformClient dataformClient = DataformClient.create()) {
       MoveDirectoryRequest request =
           MoveDirectoryRequest.newBuilder()
               .setWorkspace(
                   WorkspaceName.of("[PROJECT]", "[LOCATION]", "[REPOSITORY]", "[WORKSPACE]")
                       .toString())
               .setPath("path3433509")
               .setNewPath("newPath1845080549")
               .build();
       MoveDirectoryResponse response = dataformClient.moveDirectory(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[MoveDirectoryRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataform/latest/com.google.cloud.dataform.v1beta1.MoveDirectoryRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[MoveDirectoryResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataform/latest/com.google.cloud.dataform.v1beta1.MoveDirectoryResponse)` |   
  
### moveDirectoryCallable()
    
    
    public final UnaryCallable<MoveDirectoryRequest,MoveDirectoryResponse> moveDirectoryCallable()

Moves a directory (inside a Workspace), and all of its contents, to a new location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DataformClient dataformClient = DataformClient.create()) {
       MoveDirectoryRequest request =
           MoveDirectoryRequest.newBuilder()
               .setWorkspace(
                   WorkspaceName.of("[PROJECT]", "[LOCATION]", "[REPOSITORY]", "[WORKSPACE]")
                       .toString())
               .setPath("path3433509")
               .setNewPath("newPath1845080549")
               .build();
       ApiFuture<MoveDirectoryResponse> future =
           dataformClient.moveDirectoryCallable().futureCall(request);
       // Do something.
       MoveDirectoryResponse response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[MoveDirectoryRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataform/latest/com.google.cloud.dataform.v1beta1.MoveDirectoryRequest),[MoveDirectoryResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataform/latest/com.google.cloud.dataform.v1beta1.MoveDirectoryResponse)>` |   
  
### moveFile(MoveFileRequest request)
    
    
    public final MoveFileResponse moveFile(MoveFileRequest request)

Moves a file (inside a Workspace) to a new location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DataformClient dataformClient = DataformClient.create()) {
       MoveFileRequest request =
           MoveFileRequest.newBuilder()
               .setWorkspace(
                   WorkspaceName.of("[PROJECT]", "[LOCATION]", "[REPOSITORY]", "[WORKSPACE]")
                       .toString())
               .setPath("path3433509")
               .setNewPath("newPath1845080549")
               .build();
       MoveFileResponse response = dataformClient.moveFile(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[MoveFileRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataform/latest/com.google.cloud.dataform.v1beta1.MoveFileRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[MoveFileResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataform/latest/com.google.cloud.dataform.v1beta1.MoveFileResponse)` |   
  
### moveFileCallable()
    
    
    public final UnaryCallable<MoveFileRequest,MoveFileResponse> moveFileCallable()

Moves a file (inside a Workspace) to a new location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DataformClient dataformClient = DataformClient.create()) {
       MoveFileRequest request =
           MoveFileRequest.newBuilder()
               .setWorkspace(
                   WorkspaceName.of("[PROJECT]", "[LOCATION]", "[REPOSITORY]", "[WORKSPACE]")
                       .toString())
               .setPath("path3433509")
               .setNewPath("newPath1845080549")
               .build();
       ApiFuture<MoveFileResponse> future = dataformClient.moveFileCallable().futureCall(request);
       // Do something.
       MoveFileResponse response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[MoveFileRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataform/latest/com.google.cloud.dataform.v1beta1.MoveFileRequest),[MoveFileResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataform/latest/com.google.cloud.dataform.v1beta1.MoveFileResponse)>` |   
  
### moveFolderAsync(@Nullable FolderName name, String destinationContainingFolder)
    
    
    public final OperationFuture<Empty,MoveFolderMetadata> moveFolderAsync(@Nullable FolderName name, String destinationContainingFolder)

Moves a Folder to a new Folder, TeamFolder, or the root location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DataformClient dataformClient = DataformClient.create()) {
       FolderName name = FolderName.of("[PROJECT]", "[LOCATION]", "[FOLDER]");
       String destinationContainingFolder = "destinationContainingFolder870737098";
       dataformClient.moveFolderAsync(name, destinationContainingFolder).get();
     }
     

**Parameters**  
---  
**Name** | **Description**  
`name` | `@org.jspecify.annotations.Nullable com.google.cloud.dataform.v1beta1.FolderName`  
Required. The full resource name of the Folder to move.  
`destinationContainingFolder` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Optional. The name of the Folder, TeamFolder, or root location to move the Folder to. Can be in the format of: "" to move into the root User folder, `projects/*/locations/*/folders/*`, `projects/*/locations/*/teamFolders/*`  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html),[MoveFolderMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataform/latest/com.google.cloud.dataform.v1beta1.MoveFolderMetadata)>` |   
  
### moveFolderAsync(MoveFolderRequest request)
    
    
    public final OperationFuture<Empty,MoveFolderMetadata> moveFolderAsync(MoveFolderRequest request)

Moves a Folder to a new Folder, TeamFolder, or the root location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DataformClient dataformClient = DataformClient.create()) {
       MoveFolderRequest request =
           MoveFolderRequest.newBuilder()
               .setName(FolderName.of("[PROJECT]", "[LOCATION]", "[FOLDER]").toString())
               .setDestinationContainingFolder("destinationContainingFolder870737098")
               .build();
       dataformClient.moveFolderAsync(request).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[MoveFolderRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataform/latest/com.google.cloud.dataform.v1beta1.MoveFolderRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html),[MoveFolderMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataform/latest/com.google.cloud.dataform.v1beta1.MoveFolderMetadata)>` |   
  
### moveFolderAsync(String name, String destinationContainingFolder)
    
    
    public final OperationFuture<Empty,MoveFolderMetadata> moveFolderAsync(String name, String destinationContainingFolder)

Moves a Folder to a new Folder, TeamFolder, or the root location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DataformClient dataformClient = DataformClient.create()) {
       String name = FolderName.of("[PROJECT]", "[LOCATION]", "[FOLDER]").toString();
       String destinationContainingFolder = "destinationContainingFolder870737098";
       dataformClient.moveFolderAsync(name, destinationContainingFolder).get();
     }
     

**Parameters**  
---  
**Name** | **Description**  
`name` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The full resource name of the Folder to move.  
`destinationContainingFolder` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Optional. The name of the Folder, TeamFolder, or root location to move the Folder to. Can be in the format of: "" to move into the root User folder, `projects/*/locations/*/folders/*`, `projects/*/locations/*/teamFolders/*`  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html),[MoveFolderMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataform/latest/com.google.cloud.dataform.v1beta1.MoveFolderMetadata)>` |   
  
### moveFolderCallable()
    
    
    public final UnaryCallable<MoveFolderRequest,Operation> moveFolderCallable()

Moves a Folder to a new Folder, TeamFolder, or the root location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DataformClient dataformClient = DataformClient.create()) {
       MoveFolderRequest request =
           MoveFolderRequest.newBuilder()
               .setName(FolderName.of("[PROJECT]", "[LOCATION]", "[FOLDER]").toString())
               .setDestinationContainingFolder("destinationContainingFolder870737098")
               .build();
       ApiFuture<Operation> future = dataformClient.moveFolderCallable().futureCall(request);
       // Do something.
       future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[MoveFolderRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataform/latest/com.google.cloud.dataform.v1beta1.MoveFolderRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### moveFolderOperationCallable()
    
    
    public final OperationCallable<MoveFolderRequest,Empty,MoveFolderMetadata> moveFolderOperationCallable()

Moves a Folder to a new Folder, TeamFolder, or the root location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DataformClient dataformClient = DataformClient.create()) {
       MoveFolderRequest request =
           MoveFolderRequest.newBuilder()
               .setName(FolderName.of("[PROJECT]", "[LOCATION]", "[FOLDER]").toString())
               .setDestinationContainingFolder("destinationContainingFolder870737098")
               .build();
       OperationFuture<Empty, MoveFolderMetadata> future =
           dataformClient.moveFolderOperationCallable().futureCall(request);
       // Do something.
       future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[OperationCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallable.html)<[MoveFolderRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataform/latest/com.google.cloud.dataform.v1beta1.MoveFolderRequest),[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html),[MoveFolderMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataform/latest/com.google.cloud.dataform.v1beta1.MoveFolderMetadata)>` |   
  
### moveRepositoryAsync(@Nullable RepositoryName name, String destinationContainingFolder)
    
    
    public final OperationFuture<Empty,MoveRepositoryMetadata> moveRepositoryAsync(@Nullable RepositoryName name, String destinationContainingFolder)

Moves a Repository to a new location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DataformClient dataformClient = DataformClient.create()) {
       RepositoryName name = RepositoryName.of("[PROJECT]", "[LOCATION]", "[REPOSITORY]");
       String destinationContainingFolder = "destinationContainingFolder870737098";
       dataformClient.moveRepositoryAsync(name, destinationContainingFolder).get();
     }
     

**Parameters**  
---  
**Name** | **Description**  
`name` | `@org.jspecify.annotations.Nullable com.google.cloud.dataform.v1beta1.RepositoryName`  
Required. The full resource name of the repository to move.  
`destinationContainingFolder` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Optional. The name of the Folder, TeamFolder, or root location to move the repository to. Can be in the format of: "" to move into the root User folder, `projects/*/locations/*/folders/*`, `projects/*/locations/*/teamFolders/*`  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html),[MoveRepositoryMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataform/latest/com.google.cloud.dataform.v1beta1.MoveRepositoryMetadata)>` |   
  
### moveRepositoryAsync(MoveRepositoryRequest request)
    
    
    public final OperationFuture<Empty,MoveRepositoryMetadata> moveRepositoryAsync(MoveRepositoryRequest request)

Moves a Repository to a new location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DataformClient dataformClient = DataformClient.create()) {
       MoveRepositoryRequest request =
           MoveRepositoryRequest.newBuilder()
               .setName(RepositoryName.of("[PROJECT]", "[LOCATION]", "[REPOSITORY]").toString())
               .setDestinationContainingFolder("destinationContainingFolder870737098")
               .build();
       dataformClient.moveRepositoryAsync(request).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[MoveRepositoryRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataform/latest/com.google.cloud.dataform.v1beta1.MoveRepositoryRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html),[MoveRepositoryMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataform/latest/com.google.cloud.dataform.v1beta1.MoveRepositoryMetadata)>` |   
  
### moveRepositoryAsync(String name, String destinationContainingFolder)
    
    
    public final OperationFuture<Empty,MoveRepositoryMetadata> moveRepositoryAsync(String name, String destinationContainingFolder)

Moves a Repository to a new location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DataformClient dataformClient = DataformClient.create()) {
       String name = RepositoryName.of("[PROJECT]", "[LOCATION]", "[REPOSITORY]").toString();
       String destinationContainingFolder = "destinationContainingFolder870737098";
       dataformClient.moveRepositoryAsync(name, destinationContainingFolder).get();
     }
     

**Parameters**  
---  
**Name** | **Description**  
`name` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The full resource name of the repository to move.  
`destinationContainingFolder` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Optional. The name of the Folder, TeamFolder, or root location to move the repository to. Can be in the format of: "" to move into the root User folder, `projects/*/locations/*/folders/*`, `projects/*/locations/*/teamFolders/*`  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html),[MoveRepositoryMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataform/latest/com.google.cloud.dataform.v1beta1.MoveRepositoryMetadata)>` |   
  
### moveRepositoryCallable()
    
    
    public final UnaryCallable<MoveRepositoryRequest,Operation> moveRepositoryCallable()

Moves a Repository to a new location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DataformClient dataformClient = DataformClient.create()) {
       MoveRepositoryRequest request =
           MoveRepositoryRequest.newBuilder()
               .setName(RepositoryName.of("[PROJECT]", "[LOCATION]", "[REPOSITORY]").toString())
               .setDestinationContainingFolder("destinationContainingFolder870737098")
               .build();
       ApiFuture<Operation> future = dataformClient.moveRepositoryCallable().futureCall(request);
       // Do something.
       future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[MoveRepositoryRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataform/latest/com.google.cloud.dataform.v1beta1.MoveRepositoryRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### moveRepositoryOperationCallable()
    
    
    public final OperationCallable<MoveRepositoryRequest,Empty,MoveRepositoryMetadata> moveRepositoryOperationCallable()

Moves a Repository to a new location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DataformClient dataformClient = DataformClient.create()) {
       MoveRepositoryRequest request =
           MoveRepositoryRequest.newBuilder()
               .setName(RepositoryName.of("[PROJECT]", "[LOCATION]", "[REPOSITORY]").toString())
               .setDestinationContainingFolder("destinationContainingFolder870737098")
               .build();
       OperationFuture<Empty, MoveRepositoryMetadata> future =
           dataformClient.moveRepositoryOperationCallable().futureCall(request);
       // Do something.
       future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[OperationCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallable.html)<[MoveRepositoryRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataform/latest/com.google.cloud.dataform.v1beta1.MoveRepositoryRequest),[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html),[MoveRepositoryMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataform/latest/com.google.cloud.dataform.v1beta1.MoveRepositoryMetadata)>` |   
  
### pullGitCommits(PullGitCommitsRequest request)
    
    
    public final PullGitCommitsResponse pullGitCommits(PullGitCommitsRequest request)

Pulls Git commits from the Repository's remote into a Workspace.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DataformClient dataformClient = DataformClient.create()) {
       PullGitCommitsRequest request =
           PullGitCommitsRequest.newBuilder()
               .setName(
                   WorkspaceName.of("[PROJECT]", "[LOCATION]", "[REPOSITORY]", "[WORKSPACE]")
                       .toString())
               .setRemoteBranch("remoteBranch-533119608")
               .setAuthor(CommitAuthor.newBuilder().build())
               .build();
       PullGitCommitsResponse response = dataformClient.pullGitCommits(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[PullGitCommitsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataform/latest/com.google.cloud.dataform.v1beta1.PullGitCommitsRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[PullGitCommitsResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataform/latest/com.google.cloud.dataform.v1beta1.PullGitCommitsResponse)` |   
  
### pullGitCommitsCallable()
    
    
    public final UnaryCallable<PullGitCommitsRequest,PullGitCommitsResponse> pullGitCommitsCallable()

Pulls Git commits from the Repository's remote into a Workspace.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DataformClient dataformClient = DataformClient.create()) {
       PullGitCommitsRequest request =
           PullGitCommitsRequest.newBuilder()
               .setName(
                   WorkspaceName.of("[PROJECT]", "[LOCATION]", "[REPOSITORY]", "[WORKSPACE]")
                       .toString())
               .setRemoteBranch("remoteBranch-533119608")
               .setAuthor(CommitAuthor.newBuilder().build())
               .build();
       ApiFuture<PullGitCommitsResponse> future =
           dataformClient.pullGitCommitsCallable().futureCall(request);
       // Do something.
       PullGitCommitsResponse response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[PullGitCommitsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataform/latest/com.google.cloud.dataform.v1beta1.PullGitCommitsRequest),[PullGitCommitsResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataform/latest/com.google.cloud.dataform.v1beta1.PullGitCommitsResponse)>` |   
  
### pushGitCommits(PushGitCommitsRequest request)
    
    
    public final PushGitCommitsResponse pushGitCommits(PushGitCommitsRequest request)

Pushes Git commits from a Workspace to the Repository's remote.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DataformClient dataformClient = DataformClient.create()) {
       PushGitCommitsRequest request =
           PushGitCommitsRequest.newBuilder()
               .setName(
                   WorkspaceName.of("[PROJECT]", "[LOCATION]", "[REPOSITORY]", "[WORKSPACE]")
                       .toString())
               .setRemoteBranch("remoteBranch-533119608")
               .build();
       PushGitCommitsResponse response = dataformClient.pushGitCommits(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[PushGitCommitsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataform/latest/com.google.cloud.dataform.v1beta1.PushGitCommitsRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[PushGitCommitsResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataform/latest/com.google.cloud.dataform.v1beta1.PushGitCommitsResponse)` |   
  
### pushGitCommitsCallable()
    
    
    public final UnaryCallable<PushGitCommitsRequest,PushGitCommitsResponse> pushGitCommitsCallable()

Pushes Git commits from a Workspace to the Repository's remote.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DataformClient dataformClient = DataformClient.create()) {
       PushGitCommitsRequest request =
           PushGitCommitsRequest.newBuilder()
               .setName(
                   WorkspaceName.of("[PROJECT]", "[LOCATION]", "[REPOSITORY]", "[WORKSPACE]")
                       .toString())
               .setRemoteBranch("remoteBranch-533119608")
               .build();
       ApiFuture<PushGitCommitsResponse> future =
           dataformClient.pushGitCommitsCallable().futureCall(request);
       // Do something.
       PushGitCommitsResponse response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[PushGitCommitsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataform/latest/com.google.cloud.dataform.v1beta1.PushGitCommitsRequest),[PushGitCommitsResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataform/latest/com.google.cloud.dataform.v1beta1.PushGitCommitsResponse)>` |   
  
### queryCompilationResultActions(QueryCompilationResultActionsRequest request)
    
    
    public final DataformClient.QueryCompilationResultActionsPagedResponse queryCompilationResultActions(QueryCompilationResultActionsRequest request)

Returns CompilationResultActions in a given CompilationResult.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DataformClient dataformClient = DataformClient.create()) {
       QueryCompilationResultActionsRequest request =
           QueryCompilationResultActionsRequest.newBuilder()
               .setName(
                   CompilationResultName.of(
                           "[PROJECT]", "[LOCATION]", "[REPOSITORY]", "[COMPILATION_RESULT]")
                       .toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .setFilter("filter-1274492040")
               .build();
       for (CompilationResultAction element :
           dataformClient.queryCompilationResultActions(request).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[QueryCompilationResultActionsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataform/latest/com.google.cloud.dataform.v1beta1.QueryCompilationResultActionsRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[DataformClient.QueryCompilationResultActionsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataform/latest/com.google.cloud.dataform.v1beta1.DataformClient.QueryCompilationResultActionsPagedResponse)` |   
  
### queryCompilationResultActionsCallable()
    
    
    public final UnaryCallable<QueryCompilationResultActionsRequest,QueryCompilationResultActionsResponse> queryCompilationResultActionsCallable()

Returns CompilationResultActions in a given CompilationResult.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DataformClient dataformClient = DataformClient.create()) {
       QueryCompilationResultActionsRequest request =
           QueryCompilationResultActionsRequest.newBuilder()
               .setName(
                   CompilationResultName.of(
                           "[PROJECT]", "[LOCATION]", "[REPOSITORY]", "[COMPILATION_RESULT]")
                       .toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .setFilter("filter-1274492040")
               .build();
       while (true) {
         QueryCompilationResultActionsResponse response =
             dataformClient.queryCompilationResultActionsCallable().call(request);
         for (CompilationResultAction element : response.getCompilationResultActionsList()) {
           // doThingsWith(element);
         }
         String nextPageToken = response.getNextPageToken();
         if (!Strings.isNullOrEmpty(nextPageToken)) {
           request = request.toBuilder().setPageToken(nextPageToken).build();
         } else {
           break;
         }
       }
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[QueryCompilationResultActionsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataform/latest/com.google.cloud.dataform.v1beta1.QueryCompilationResultActionsRequest),[QueryCompilationResultActionsResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataform/latest/com.google.cloud.dataform.v1beta1.QueryCompilationResultActionsResponse)>` |   
  
### queryCompilationResultActionsPagedCallable()
    
    
    public final UnaryCallable<QueryCompilationResultActionsRequest,DataformClient.QueryCompilationResultActionsPagedResponse> queryCompilationResultActionsPagedCallable()

Returns CompilationResultActions in a given CompilationResult.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DataformClient dataformClient = DataformClient.create()) {
       QueryCompilationResultActionsRequest request =
           QueryCompilationResultActionsRequest.newBuilder()
               .setName(
                   CompilationResultName.of(
                           "[PROJECT]", "[LOCATION]", "[REPOSITORY]", "[COMPILATION_RESULT]")
                       .toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .setFilter("filter-1274492040")
               .build();
       ApiFuture<CompilationResultAction> future =
           dataformClient.queryCompilationResultActionsPagedCallable().futureCall(request);
       // Do something.
       for (CompilationResultAction element : future.get().iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[QueryCompilationResultActionsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataform/latest/com.google.cloud.dataform.v1beta1.QueryCompilationResultActionsRequest),[QueryCompilationResultActionsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataform/latest/com.google.cloud.dataform.v1beta1.DataformClient.QueryCompilationResultActionsPagedResponse)>` |   
  
### queryDirectoryContents(QueryDirectoryContentsRequest request)
    
    
    public final DataformClient.QueryDirectoryContentsPagedResponse queryDirectoryContents(QueryDirectoryContentsRequest request)

Returns the contents of a given Workspace directory.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DataformClient dataformClient = DataformClient.create()) {
       QueryDirectoryContentsRequest request =
           QueryDirectoryContentsRequest.newBuilder()
               .setWorkspace(
                   WorkspaceName.of("[PROJECT]", "[LOCATION]", "[REPOSITORY]", "[WORKSPACE]")
                       .toString())
               .setPath("path3433509")
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .setView(DirectoryContentsView.forNumber(0))
               .build();
       for (DirectoryEntry element : dataformClient.queryDirectoryContents(request).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[QueryDirectoryContentsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataform/latest/com.google.cloud.dataform.v1beta1.QueryDirectoryContentsRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[DataformClient.QueryDirectoryContentsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataform/latest/com.google.cloud.dataform.v1beta1.DataformClient.QueryDirectoryContentsPagedResponse)` |   
  
### queryDirectoryContentsCallable()
    
    
    public final UnaryCallable<QueryDirectoryContentsRequest,QueryDirectoryContentsResponse> queryDirectoryContentsCallable()

Returns the contents of a given Workspace directory.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DataformClient dataformClient = DataformClient.create()) {
       QueryDirectoryContentsRequest request =
           QueryDirectoryContentsRequest.newBuilder()
               .setWorkspace(
                   WorkspaceName.of("[PROJECT]", "[LOCATION]", "[REPOSITORY]", "[WORKSPACE]")
                       .toString())
               .setPath("path3433509")
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .setView(DirectoryContentsView.forNumber(0))
               .build();
       while (true) {
         QueryDirectoryContentsResponse response =
             dataformClient.queryDirectoryContentsCallable().call(request);
         for (DirectoryEntry element : response.getDirectoryEntriesList()) {
           // doThingsWith(element);
         }
         String nextPageToken = response.getNextPageToken();
         if (!Strings.isNullOrEmpty(nextPageToken)) {
           request = request.toBuilder().setPageToken(nextPageToken).build();
         } else {
           break;
         }
       }
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[QueryDirectoryContentsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataform/latest/com.google.cloud.dataform.v1beta1.QueryDirectoryContentsRequest),[QueryDirectoryContentsResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataform/latest/com.google.cloud.dataform.v1beta1.QueryDirectoryContentsResponse)>` |   
  
### queryDirectoryContentsPagedCallable()
    
    
    public final UnaryCallable<QueryDirectoryContentsRequest,DataformClient.QueryDirectoryContentsPagedResponse> queryDirectoryContentsPagedCallable()

Returns the contents of a given Workspace directory.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DataformClient dataformClient = DataformClient.create()) {
       QueryDirectoryContentsRequest request =
           QueryDirectoryContentsRequest.newBuilder()
               .setWorkspace(
                   WorkspaceName.of("[PROJECT]", "[LOCATION]", "[REPOSITORY]", "[WORKSPACE]")
                       .toString())
               .setPath("path3433509")
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .setView(DirectoryContentsView.forNumber(0))
               .build();
       ApiFuture<DirectoryEntry> future =
           dataformClient.queryDirectoryContentsPagedCallable().futureCall(request);
       // Do something.
       for (DirectoryEntry element : future.get().iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[QueryDirectoryContentsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataform/latest/com.google.cloud.dataform.v1beta1.QueryDirectoryContentsRequest),[QueryDirectoryContentsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataform/latest/com.google.cloud.dataform.v1beta1.DataformClient.QueryDirectoryContentsPagedResponse)>` |   
  
### queryFolderContents(@Nullable FolderName folder)
    
    
    public final DataformClient.QueryFolderContentsPagedResponse queryFolderContents(@Nullable FolderName folder)

Returns the contents of a given Folder.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DataformClient dataformClient = DataformClient.create()) {
       FolderName folder = FolderName.of("[PROJECT]", "[LOCATION]", "[FOLDER]");
       for (QueryFolderContentsResponse.FolderContentsEntry element :
           dataformClient.queryFolderContents(folder).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`folder` | `@org.jspecify.annotations.Nullable com.google.cloud.dataform.v1beta1.FolderName`  
Required. Resource name of the Folder to list contents for. Format: projects/*/locations/*/folders/*  
**Returns**  
---  
**Type** | **Description**  
`[DataformClient.QueryFolderContentsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataform/latest/com.google.cloud.dataform.v1beta1.DataformClient.QueryFolderContentsPagedResponse)` |   
  
### queryFolderContents(QueryFolderContentsRequest request)
    
    
    public final DataformClient.QueryFolderContentsPagedResponse queryFolderContents(QueryFolderContentsRequest request)

Returns the contents of a given Folder.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DataformClient dataformClient = DataformClient.create()) {
       QueryFolderContentsRequest request =
           QueryFolderContentsRequest.newBuilder()
               .setFolder(FolderName.of("[PROJECT]", "[LOCATION]", "[FOLDER]").toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .setOrderBy("orderBy-1207110587")
               .setFilter("filter-1274492040")
               .build();
       for (QueryFolderContentsResponse.FolderContentsEntry element :
           dataformClient.queryFolderContents(request).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[QueryFolderContentsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataform/latest/com.google.cloud.dataform.v1beta1.QueryFolderContentsRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[DataformClient.QueryFolderContentsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataform/latest/com.google.cloud.dataform.v1beta1.DataformClient.QueryFolderContentsPagedResponse)` |   
  
### queryFolderContents(String folder)
    
    
    public final DataformClient.QueryFolderContentsPagedResponse queryFolderContents(String folder)

Returns the contents of a given Folder.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DataformClient dataformClient = DataformClient.create()) {
       String folder = FolderName.of("[PROJECT]", "[LOCATION]", "[FOLDER]").toString();
       for (QueryFolderContentsResponse.FolderContentsEntry element :
           dataformClient.queryFolderContents(folder).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`folder` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. Resource name of the Folder to list contents for. Format: projects/*/locations/*/folders/*  
**Returns**  
---  
**Type** | **Description**  
`[DataformClient.QueryFolderContentsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataform/latest/com.google.cloud.dataform.v1beta1.DataformClient.QueryFolderContentsPagedResponse)` |   
  
### queryFolderContentsCallable()
    
    
    public final UnaryCallable<QueryFolderContentsRequest,QueryFolderContentsResponse> queryFolderContentsCallable()

Returns the contents of a given Folder.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DataformClient dataformClient = DataformClient.create()) {
       QueryFolderContentsRequest request =
           QueryFolderContentsRequest.newBuilder()
               .setFolder(FolderName.of("[PROJECT]", "[LOCATION]", "[FOLDER]").toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .setOrderBy("orderBy-1207110587")
               .setFilter("filter-1274492040")
               .build();
       while (true) {
         QueryFolderContentsResponse response =
             dataformClient.queryFolderContentsCallable().call(request);
         for (QueryFolderContentsResponse.FolderContentsEntry element : response.getEntriesList()) {
           // doThingsWith(element);
         }
         String nextPageToken = response.getNextPageToken();
         if (!Strings.isNullOrEmpty(nextPageToken)) {
           request = request.toBuilder().setPageToken(nextPageToken).build();
         } else {
           break;
         }
       }
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[QueryFolderContentsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataform/latest/com.google.cloud.dataform.v1beta1.QueryFolderContentsRequest),[QueryFolderContentsResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataform/latest/com.google.cloud.dataform.v1beta1.QueryFolderContentsResponse)>` |   
  
### queryFolderContentsPagedCallable()
    
    
    public final UnaryCallable<QueryFolderContentsRequest,DataformClient.QueryFolderContentsPagedResponse> queryFolderContentsPagedCallable()

Returns the contents of a given Folder.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DataformClient dataformClient = DataformClient.create()) {
       QueryFolderContentsRequest request =
           QueryFolderContentsRequest.newBuilder()
               .setFolder(FolderName.of("[PROJECT]", "[LOCATION]", "[FOLDER]").toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .setOrderBy("orderBy-1207110587")
               .setFilter("filter-1274492040")
               .build();
       ApiFuture<QueryFolderContentsResponse.FolderContentsEntry> future =
           dataformClient.queryFolderContentsPagedCallable().futureCall(request);
       // Do something.
       for (QueryFolderContentsResponse.FolderContentsEntry element : future.get().iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[QueryFolderContentsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataform/latest/com.google.cloud.dataform.v1beta1.QueryFolderContentsRequest),[QueryFolderContentsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataform/latest/com.google.cloud.dataform.v1beta1.DataformClient.QueryFolderContentsPagedResponse)>` |   
  
### queryRepositoryDirectoryContents(QueryRepositoryDirectoryContentsRequest request)
    
    
    public final DataformClient.QueryRepositoryDirectoryContentsPagedResponse queryRepositoryDirectoryContents(QueryRepositoryDirectoryContentsRequest request)

Returns the contents of a given Repository directory. The Repository must not have a value for `git_remote_settings.url`.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DataformClient dataformClient = DataformClient.create()) {
       QueryRepositoryDirectoryContentsRequest request =
           QueryRepositoryDirectoryContentsRequest.newBuilder()
               .setName(RepositoryName.of("[PROJECT]", "[LOCATION]", "[REPOSITORY]").toString())
               .setCommitSha("commitSha-1491174411")
               .setPath("path3433509")
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .build();
       for (DirectoryEntry element :
           dataformClient.queryRepositoryDirectoryContents(request).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[QueryRepositoryDirectoryContentsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataform/latest/com.google.cloud.dataform.v1beta1.QueryRepositoryDirectoryContentsRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[DataformClient.QueryRepositoryDirectoryContentsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataform/latest/com.google.cloud.dataform.v1beta1.DataformClient.QueryRepositoryDirectoryContentsPagedResponse)` |   
  
### queryRepositoryDirectoryContentsCallable()
    
    
    public final UnaryCallable<QueryRepositoryDirectoryContentsRequest,QueryRepositoryDirectoryContentsResponse> queryRepositoryDirectoryContentsCallable()

Returns the contents of a given Repository directory. The Repository must not have a value for `git_remote_settings.url`.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DataformClient dataformClient = DataformClient.create()) {
       QueryRepositoryDirectoryContentsRequest request =
           QueryRepositoryDirectoryContentsRequest.newBuilder()
               .setName(RepositoryName.of("[PROJECT]", "[LOCATION]", "[REPOSITORY]").toString())
               .setCommitSha("commitSha-1491174411")
               .setPath("path3433509")
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .build();
       while (true) {
         QueryRepositoryDirectoryContentsResponse response =
             dataformClient.queryRepositoryDirectoryContentsCallable().call(request);
         for (DirectoryEntry element : response.getDirectoryEntriesList()) {
           // doThingsWith(element);
         }
         String nextPageToken = response.getNextPageToken();
         if (!Strings.isNullOrEmpty(nextPageToken)) {
           request = request.toBuilder().setPageToken(nextPageToken).build();
         } else {
           break;
         }
       }
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[QueryRepositoryDirectoryContentsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataform/latest/com.google.cloud.dataform.v1beta1.QueryRepositoryDirectoryContentsRequest),[QueryRepositoryDirectoryContentsResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataform/latest/com.google.cloud.dataform.v1beta1.QueryRepositoryDirectoryContentsResponse)>` |   
  
### queryRepositoryDirectoryContentsPagedCallable()
    
    
    public final UnaryCallable<QueryRepositoryDirectoryContentsRequest,DataformClient.QueryRepositoryDirectoryContentsPagedResponse> queryRepositoryDirectoryContentsPagedCallable()

Returns the contents of a given Repository directory. The Repository must not have a value for `git_remote_settings.url`.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DataformClient dataformClient = DataformClient.create()) {
       QueryRepositoryDirectoryContentsRequest request =
           QueryRepositoryDirectoryContentsRequest.newBuilder()
               .setName(RepositoryName.of("[PROJECT]", "[LOCATION]", "[REPOSITORY]").toString())
               .setCommitSha("commitSha-1491174411")
               .setPath("path3433509")
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .build();
       ApiFuture<DirectoryEntry> future =
           dataformClient.queryRepositoryDirectoryContentsPagedCallable().futureCall(request);
       // Do something.
       for (DirectoryEntry element : future.get().iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[QueryRepositoryDirectoryContentsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataform/latest/com.google.cloud.dataform.v1beta1.QueryRepositoryDirectoryContentsRequest),[QueryRepositoryDirectoryContentsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataform/latest/com.google.cloud.dataform.v1beta1.DataformClient.QueryRepositoryDirectoryContentsPagedResponse)>` |   
  
### queryTeamFolderContents(@Nullable TeamFolderName teamFolder)
    
    
    public final DataformClient.QueryTeamFolderContentsPagedResponse queryTeamFolderContents(@Nullable TeamFolderName teamFolder)

Returns the contents of a given TeamFolder.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DataformClient dataformClient = DataformClient.create()) {
       TeamFolderName teamFolder = TeamFolderName.of("[PROJECT]", "[LOCATION]", "[TEAM_FOLDER]");
       for (QueryTeamFolderContentsResponse.TeamFolderContentsEntry element :
           dataformClient.queryTeamFolderContents(teamFolder).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`teamFolder` | `@org.jspecify.annotations.Nullable com.google.cloud.dataform.v1beta1.TeamFolderName`  
Required. Resource name of the TeamFolder to list contents for. Format: `projects/*/locations/*/teamFolders/*`.  
**Returns**  
---  
**Type** | **Description**  
`[DataformClient.QueryTeamFolderContentsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataform/latest/com.google.cloud.dataform.v1beta1.DataformClient.QueryTeamFolderContentsPagedResponse)` |   
  
### queryTeamFolderContents(QueryTeamFolderContentsRequest request)
    
    
    public final DataformClient.QueryTeamFolderContentsPagedResponse queryTeamFolderContents(QueryTeamFolderContentsRequest request)

Returns the contents of a given TeamFolder.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DataformClient dataformClient = DataformClient.create()) {
       QueryTeamFolderContentsRequest request =
           QueryTeamFolderContentsRequest.newBuilder()
               .setTeamFolder(
                   TeamFolderName.of("[PROJECT]", "[LOCATION]", "[TEAM_FOLDER]").toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .setOrderBy("orderBy-1207110587")
               .setFilter("filter-1274492040")
               .build();
       for (QueryTeamFolderContentsResponse.TeamFolderContentsEntry element :
           dataformClient.queryTeamFolderContents(request).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[QueryTeamFolderContentsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataform/latest/com.google.cloud.dataform.v1beta1.QueryTeamFolderContentsRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[DataformClient.QueryTeamFolderContentsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataform/latest/com.google.cloud.dataform.v1beta1.DataformClient.QueryTeamFolderContentsPagedResponse)` |   
  
### queryTeamFolderContents(String teamFolder)
    
    
    public final DataformClient.QueryTeamFolderContentsPagedResponse queryTeamFolderContents(String teamFolder)

Returns the contents of a given TeamFolder.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DataformClient dataformClient = DataformClient.create()) {
       String teamFolder = TeamFolderName.of("[PROJECT]", "[LOCATION]", "[TEAM_FOLDER]").toString();
       for (QueryTeamFolderContentsResponse.TeamFolderContentsEntry element :
           dataformClient.queryTeamFolderContents(teamFolder).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`teamFolder` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. Resource name of the TeamFolder to list contents for. Format: `projects/*/locations/*/teamFolders/*`.  
**Returns**  
---  
**Type** | **Description**  
`[DataformClient.QueryTeamFolderContentsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataform/latest/com.google.cloud.dataform.v1beta1.DataformClient.QueryTeamFolderContentsPagedResponse)` |   
  
### queryTeamFolderContentsCallable()
    
    
    public final UnaryCallable<QueryTeamFolderContentsRequest,QueryTeamFolderContentsResponse> queryTeamFolderContentsCallable()

Returns the contents of a given TeamFolder.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DataformClient dataformClient = DataformClient.create()) {
       QueryTeamFolderContentsRequest request =
           QueryTeamFolderContentsRequest.newBuilder()
               .setTeamFolder(
                   TeamFolderName.of("[PROJECT]", "[LOCATION]", "[TEAM_FOLDER]").toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .setOrderBy("orderBy-1207110587")
               .setFilter("filter-1274492040")
               .build();
       while (true) {
         QueryTeamFolderContentsResponse response =
             dataformClient.queryTeamFolderContentsCallable().call(request);
         for (QueryTeamFolderContentsResponse.TeamFolderContentsEntry element :
             response.getEntriesList()) {
           // doThingsWith(element);
         }
         String nextPageToken = response.getNextPageToken();
         if (!Strings.isNullOrEmpty(nextPageToken)) {
           request = request.toBuilder().setPageToken(nextPageToken).build();
         } else {
           break;
         }
       }
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[QueryTeamFolderContentsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataform/latest/com.google.cloud.dataform.v1beta1.QueryTeamFolderContentsRequest),[QueryTeamFolderContentsResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataform/latest/com.google.cloud.dataform.v1beta1.QueryTeamFolderContentsResponse)>` |   
  
### queryTeamFolderContentsPagedCallable()
    
    
    public final UnaryCallable<QueryTeamFolderContentsRequest,DataformClient.QueryTeamFolderContentsPagedResponse> queryTeamFolderContentsPagedCallable()

Returns the contents of a given TeamFolder.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DataformClient dataformClient = DataformClient.create()) {
       QueryTeamFolderContentsRequest request =
           QueryTeamFolderContentsRequest.newBuilder()
               .setTeamFolder(
                   TeamFolderName.of("[PROJECT]", "[LOCATION]", "[TEAM_FOLDER]").toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .setOrderBy("orderBy-1207110587")
               .setFilter("filter-1274492040")
               .build();
       ApiFuture<QueryTeamFolderContentsResponse.TeamFolderContentsEntry> future =
           dataformClient.queryTeamFolderContentsPagedCallable().futureCall(request);
       // Do something.
       for (QueryTeamFolderContentsResponse.TeamFolderContentsEntry element :
           future.get().iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[QueryTeamFolderContentsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataform/latest/com.google.cloud.dataform.v1beta1.QueryTeamFolderContentsRequest),[QueryTeamFolderContentsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataform/latest/com.google.cloud.dataform.v1beta1.DataformClient.QueryTeamFolderContentsPagedResponse)>` |   
  
### queryUserRootContents(@Nullable LocationName location)
    
    
    public final DataformClient.QueryUserRootContentsPagedResponse queryUserRootContents(@Nullable LocationName location)

Returns the contents of a caller's root folder in a given location. The root folder contains all resources that are created by the user and not contained in any other folder.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DataformClient dataformClient = DataformClient.create()) {
       LocationName location = LocationName.of("[PROJECT]", "[LOCATION]");
       for (QueryUserRootContentsResponse.RootContentsEntry element :
           dataformClient.queryUserRootContents(location).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`location` | `@org.jspecify.annotations.Nullable com.google.cloud.dataform.v1beta1.LocationName`  
Required. Location of the user root folder to list contents for. Format: projects/*/locations/*  
**Returns**  
---  
**Type** | **Description**  
`[DataformClient.QueryUserRootContentsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataform/latest/com.google.cloud.dataform.v1beta1.DataformClient.QueryUserRootContentsPagedResponse)` |   
  
### queryUserRootContents(QueryUserRootContentsRequest request)
    
    
    public final DataformClient.QueryUserRootContentsPagedResponse queryUserRootContents(QueryUserRootContentsRequest request)

Returns the contents of a caller's root folder in a given location. The root folder contains all resources that are created by the user and not contained in any other folder.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DataformClient dataformClient = DataformClient.create()) {
       QueryUserRootContentsRequest request =
           QueryUserRootContentsRequest.newBuilder()
               .setLocation(LocationName.of("[PROJECT]", "[LOCATION]").toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .setOrderBy("orderBy-1207110587")
               .setFilter("filter-1274492040")
               .build();
       for (QueryUserRootContentsResponse.RootContentsEntry element :
           dataformClient.queryUserRootContents(request).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[QueryUserRootContentsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataform/latest/com.google.cloud.dataform.v1beta1.QueryUserRootContentsRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[DataformClient.QueryUserRootContentsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataform/latest/com.google.cloud.dataform.v1beta1.DataformClient.QueryUserRootContentsPagedResponse)` |   
  
### queryUserRootContents(String location)
    
    
    public final DataformClient.QueryUserRootContentsPagedResponse queryUserRootContents(String location)

Returns the contents of a caller's root folder in a given location. The root folder contains all resources that are created by the user and not contained in any other folder.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DataformClient dataformClient = DataformClient.create()) {
       String location = LocationName.of("[PROJECT]", "[LOCATION]").toString();
       for (QueryUserRootContentsResponse.RootContentsEntry element :
           dataformClient.queryUserRootContents(location).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`location` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. Location of the user root folder to list contents for. Format: projects/*/locations/*  
**Returns**  
---  
**Type** | **Description**  
`[DataformClient.QueryUserRootContentsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataform/latest/com.google.cloud.dataform.v1beta1.DataformClient.QueryUserRootContentsPagedResponse)` |   
  
### queryUserRootContentsCallable()
    
    
    public final UnaryCallable<QueryUserRootContentsRequest,QueryUserRootContentsResponse> queryUserRootContentsCallable()

Returns the contents of a caller's root folder in a given location. The root folder contains all resources that are created by the user and not contained in any other folder.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DataformClient dataformClient = DataformClient.create()) {
       QueryUserRootContentsRequest request =
           QueryUserRootContentsRequest.newBuilder()
               .setLocation(LocationName.of("[PROJECT]", "[LOCATION]").toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .setOrderBy("orderBy-1207110587")
               .setFilter("filter-1274492040")
               .build();
       while (true) {
         QueryUserRootContentsResponse response =
             dataformClient.queryUserRootContentsCallable().call(request);
         for (QueryUserRootContentsResponse.RootContentsEntry element : response.getEntriesList()) {
           // doThingsWith(element);
         }
         String nextPageToken = response.getNextPageToken();
         if (!Strings.isNullOrEmpty(nextPageToken)) {
           request = request.toBuilder().setPageToken(nextPageToken).build();
         } else {
           break;
         }
       }
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[QueryUserRootContentsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataform/latest/com.google.cloud.dataform.v1beta1.QueryUserRootContentsRequest),[QueryUserRootContentsResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataform/latest/com.google.cloud.dataform.v1beta1.QueryUserRootContentsResponse)>` |   
  
### queryUserRootContentsPagedCallable()
    
    
    public final UnaryCallable<QueryUserRootContentsRequest,DataformClient.QueryUserRootContentsPagedResponse> queryUserRootContentsPagedCallable()

Returns the contents of a caller's root folder in a given location. The root folder contains all resources that are created by the user and not contained in any other folder.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DataformClient dataformClient = DataformClient.create()) {
       QueryUserRootContentsRequest request =
           QueryUserRootContentsRequest.newBuilder()
               .setLocation(LocationName.of("[PROJECT]", "[LOCATION]").toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .setOrderBy("orderBy-1207110587")
               .setFilter("filter-1274492040")
               .build();
       ApiFuture<QueryUserRootContentsResponse.RootContentsEntry> future =
           dataformClient.queryUserRootContentsPagedCallable().futureCall(request);
       // Do something.
       for (QueryUserRootContentsResponse.RootContentsEntry element : future.get().iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[QueryUserRootContentsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataform/latest/com.google.cloud.dataform.v1beta1.QueryUserRootContentsRequest),[QueryUserRootContentsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataform/latest/com.google.cloud.dataform.v1beta1.DataformClient.QueryUserRootContentsPagedResponse)>` |   
  
### queryWorkflowInvocationActions(QueryWorkflowInvocationActionsRequest request)
    
    
    public final DataformClient.QueryWorkflowInvocationActionsPagedResponse queryWorkflowInvocationActions(QueryWorkflowInvocationActionsRequest request)

Returns WorkflowInvocationActions in a given WorkflowInvocation.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DataformClient dataformClient = DataformClient.create()) {
       QueryWorkflowInvocationActionsRequest request =
           QueryWorkflowInvocationActionsRequest.newBuilder()
               .setName(
                   WorkflowInvocationName.of(
                           "[PROJECT]", "[LOCATION]", "[REPOSITORY]", "[WORKFLOW_INVOCATION]")
                       .toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .build();
       for (WorkflowInvocationAction element :
           dataformClient.queryWorkflowInvocationActions(request).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[QueryWorkflowInvocationActionsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataform/latest/com.google.cloud.dataform.v1beta1.QueryWorkflowInvocationActionsRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[DataformClient.QueryWorkflowInvocationActionsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataform/latest/com.google.cloud.dataform.v1beta1.DataformClient.QueryWorkflowInvocationActionsPagedResponse)` |   
  
### queryWorkflowInvocationActionsCallable()
    
    
    public final UnaryCallable<QueryWorkflowInvocationActionsRequest,QueryWorkflowInvocationActionsResponse> queryWorkflowInvocationActionsCallable()

Returns WorkflowInvocationActions in a given WorkflowInvocation.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DataformClient dataformClient = DataformClient.create()) {
       QueryWorkflowInvocationActionsRequest request =
           QueryWorkflowInvocationActionsRequest.newBuilder()
               .setName(
                   WorkflowInvocationName.of(
                           "[PROJECT]", "[LOCATION]", "[REPOSITORY]", "[WORKFLOW_INVOCATION]")
                       .toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .build();
       while (true) {
         QueryWorkflowInvocationActionsResponse response =
             dataformClient.queryWorkflowInvocationActionsCallable().call(request);
         for (WorkflowInvocationAction element : response.getWorkflowInvocationActionsList()) {
           // doThingsWith(element);
         }
         String nextPageToken = response.getNextPageToken();
         if (!Strings.isNullOrEmpty(nextPageToken)) {
           request = request.toBuilder().setPageToken(nextPageToken).build();
         } else {
           break;
         }
       }
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[QueryWorkflowInvocationActionsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataform/latest/com.google.cloud.dataform.v1beta1.QueryWorkflowInvocationActionsRequest),[QueryWorkflowInvocationActionsResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataform/latest/com.google.cloud.dataform.v1beta1.QueryWorkflowInvocationActionsResponse)>` |   
  
### queryWorkflowInvocationActionsPagedCallable()
    
    
    public final UnaryCallable<QueryWorkflowInvocationActionsRequest,DataformClient.QueryWorkflowInvocationActionsPagedResponse> queryWorkflowInvocationActionsPagedCallable()

Returns WorkflowInvocationActions in a given WorkflowInvocation.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DataformClient dataformClient = DataformClient.create()) {
       QueryWorkflowInvocationActionsRequest request =
           QueryWorkflowInvocationActionsRequest.newBuilder()
               .setName(
                   WorkflowInvocationName.of(
                           "[PROJECT]", "[LOCATION]", "[REPOSITORY]", "[WORKFLOW_INVOCATION]")
                       .toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .build();
       ApiFuture<WorkflowInvocationAction> future =
           dataformClient.queryWorkflowInvocationActionsPagedCallable().futureCall(request);
       // Do something.
       for (WorkflowInvocationAction element : future.get().iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[QueryWorkflowInvocationActionsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataform/latest/com.google.cloud.dataform.v1beta1.QueryWorkflowInvocationActionsRequest),[QueryWorkflowInvocationActionsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataform/latest/com.google.cloud.dataform.v1beta1.DataformClient.QueryWorkflowInvocationActionsPagedResponse)>` |   
  
### readFile(ReadFileRequest request)
    
    
    public final ReadFileResponse readFile(ReadFileRequest request)

Returns the contents of a file (inside a Workspace).

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DataformClient dataformClient = DataformClient.create()) {
       ReadFileRequest request =
           ReadFileRequest.newBuilder()
               .setWorkspace(
                   WorkspaceName.of("[PROJECT]", "[LOCATION]", "[REPOSITORY]", "[WORKSPACE]")
                       .toString())
               .setPath("path3433509")
               .setRevision("revision-260786213")
               .build();
       ReadFileResponse response = dataformClient.readFile(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[ReadFileRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataform/latest/com.google.cloud.dataform.v1beta1.ReadFileRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[ReadFileResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataform/latest/com.google.cloud.dataform.v1beta1.ReadFileResponse)` |   
  
### readFileCallable()
    
    
    public final UnaryCallable<ReadFileRequest,ReadFileResponse> readFileCallable()

Returns the contents of a file (inside a Workspace).

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DataformClient dataformClient = DataformClient.create()) {
       ReadFileRequest request =
           ReadFileRequest.newBuilder()
               .setWorkspace(
                   WorkspaceName.of("[PROJECT]", "[LOCATION]", "[REPOSITORY]", "[WORKSPACE]")
                       .toString())
               .setPath("path3433509")
               .setRevision("revision-260786213")
               .build();
       ApiFuture<ReadFileResponse> future = dataformClient.readFileCallable().futureCall(request);
       // Do something.
       ReadFileResponse response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ReadFileRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataform/latest/com.google.cloud.dataform.v1beta1.ReadFileRequest),[ReadFileResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataform/latest/com.google.cloud.dataform.v1beta1.ReadFileResponse)>` |   
  
### readRepositoryFile(ReadRepositoryFileRequest request)
    
    
    public final ReadRepositoryFileResponse readRepositoryFile(ReadRepositoryFileRequest request)

Returns the contents of a file (inside a Repository). The Repository must not have a value for `git_remote_settings.url`.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DataformClient dataformClient = DataformClient.create()) {
       ReadRepositoryFileRequest request =
           ReadRepositoryFileRequest.newBuilder()
               .setName(RepositoryName.of("[PROJECT]", "[LOCATION]", "[REPOSITORY]").toString())
               .setCommitSha("commitSha-1491174411")
               .setPath("path3433509")
               .build();
       ReadRepositoryFileResponse response = dataformClient.readRepositoryFile(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[ReadRepositoryFileRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataform/latest/com.google.cloud.dataform.v1beta1.ReadRepositoryFileRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[ReadRepositoryFileResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataform/latest/com.google.cloud.dataform.v1beta1.ReadRepositoryFileResponse)` |   
  
### readRepositoryFileCallable()
    
    
    public final UnaryCallable<ReadRepositoryFileRequest,ReadRepositoryFileResponse> readRepositoryFileCallable()

Returns the contents of a file (inside a Repository). The Repository must not have a value for `git_remote_settings.url`.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DataformClient dataformClient = DataformClient.create()) {
       ReadRepositoryFileRequest request =
           ReadRepositoryFileRequest.newBuilder()
               .setName(RepositoryName.of("[PROJECT]", "[LOCATION]", "[REPOSITORY]").toString())
               .setCommitSha("commitSha-1491174411")
               .setPath("path3433509")
               .build();
       ApiFuture<ReadRepositoryFileResponse> future =
           dataformClient.readRepositoryFileCallable().futureCall(request);
       // Do something.
       ReadRepositoryFileResponse response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ReadRepositoryFileRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataform/latest/com.google.cloud.dataform.v1beta1.ReadRepositoryFileRequest),[ReadRepositoryFileResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataform/latest/com.google.cloud.dataform.v1beta1.ReadRepositoryFileResponse)>` |   
  
### removeDirectory(RemoveDirectoryRequest request)
    
    
    public final RemoveDirectoryResponse removeDirectory(RemoveDirectoryRequest request)

Deletes a directory (inside a Workspace) and all of its contents.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DataformClient dataformClient = DataformClient.create()) {
       RemoveDirectoryRequest request =
           RemoveDirectoryRequest.newBuilder()
               .setWorkspace(
                   WorkspaceName.of("[PROJECT]", "[LOCATION]", "[REPOSITORY]", "[WORKSPACE]")
                       .toString())
               .setPath("path3433509")
               .build();
       RemoveDirectoryResponse response = dataformClient.removeDirectory(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[RemoveDirectoryRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataform/latest/com.google.cloud.dataform.v1beta1.RemoveDirectoryRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[RemoveDirectoryResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataform/latest/com.google.cloud.dataform.v1beta1.RemoveDirectoryResponse)` |   
  
### removeDirectoryCallable()
    
    
    public final UnaryCallable<RemoveDirectoryRequest,RemoveDirectoryResponse> removeDirectoryCallable()

Deletes a directory (inside a Workspace) and all of its contents.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DataformClient dataformClient = DataformClient.create()) {
       RemoveDirectoryRequest request =
           RemoveDirectoryRequest.newBuilder()
               .setWorkspace(
                   WorkspaceName.of("[PROJECT]", "[LOCATION]", "[REPOSITORY]", "[WORKSPACE]")
                       .toString())
               .setPath("path3433509")
               .build();
       ApiFuture<RemoveDirectoryResponse> future =
           dataformClient.removeDirectoryCallable().futureCall(request);
       // Do something.
       RemoveDirectoryResponse response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[RemoveDirectoryRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataform/latest/com.google.cloud.dataform.v1beta1.RemoveDirectoryRequest),[RemoveDirectoryResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataform/latest/com.google.cloud.dataform.v1beta1.RemoveDirectoryResponse)>` |   
  
### removeFile(RemoveFileRequest request)
    
    
    public final RemoveFileResponse removeFile(RemoveFileRequest request)

Deletes a file (inside a Workspace).

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DataformClient dataformClient = DataformClient.create()) {
       RemoveFileRequest request =
           RemoveFileRequest.newBuilder()
               .setWorkspace(
                   WorkspaceName.of("[PROJECT]", "[LOCATION]", "[REPOSITORY]", "[WORKSPACE]")
                       .toString())
               .setPath("path3433509")
               .build();
       RemoveFileResponse response = dataformClient.removeFile(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[RemoveFileRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataform/latest/com.google.cloud.dataform.v1beta1.RemoveFileRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[RemoveFileResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataform/latest/com.google.cloud.dataform.v1beta1.RemoveFileResponse)` |   
  
### removeFileCallable()
    
    
    public final UnaryCallable<RemoveFileRequest,RemoveFileResponse> removeFileCallable()

Deletes a file (inside a Workspace).

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DataformClient dataformClient = DataformClient.create()) {
       RemoveFileRequest request =
           RemoveFileRequest.newBuilder()
               .setWorkspace(
                   WorkspaceName.of("[PROJECT]", "[LOCATION]", "[REPOSITORY]", "[WORKSPACE]")
                       .toString())
               .setPath("path3433509")
               .build();
       ApiFuture<RemoveFileResponse> future =
           dataformClient.removeFileCallable().futureCall(request);
       // Do something.
       RemoveFileResponse response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[RemoveFileRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataform/latest/com.google.cloud.dataform.v1beta1.RemoveFileRequest),[RemoveFileResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataform/latest/com.google.cloud.dataform.v1beta1.RemoveFileResponse)>` |   
  
### resetWorkspaceChanges(ResetWorkspaceChangesRequest request)
    
    
    public final ResetWorkspaceChangesResponse resetWorkspaceChanges(ResetWorkspaceChangesRequest request)

Performs a Git reset for uncommitted files in a Workspace.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DataformClient dataformClient = DataformClient.create()) {
       ResetWorkspaceChangesRequest request =
           ResetWorkspaceChangesRequest.newBuilder()
               .setName(
                   WorkspaceName.of("[PROJECT]", "[LOCATION]", "[REPOSITORY]", "[WORKSPACE]")
                       .toString())
               .addAllPaths(new ArrayList<String>())
               .setClean(true)
               .build();
       ResetWorkspaceChangesResponse response = dataformClient.resetWorkspaceChanges(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[ResetWorkspaceChangesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataform/latest/com.google.cloud.dataform.v1beta1.ResetWorkspaceChangesRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[ResetWorkspaceChangesResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataform/latest/com.google.cloud.dataform.v1beta1.ResetWorkspaceChangesResponse)` |   
  
### resetWorkspaceChangesCallable()
    
    
    public final UnaryCallable<ResetWorkspaceChangesRequest,ResetWorkspaceChangesResponse> resetWorkspaceChangesCallable()

Performs a Git reset for uncommitted files in a Workspace.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DataformClient dataformClient = DataformClient.create()) {
       ResetWorkspaceChangesRequest request =
           ResetWorkspaceChangesRequest.newBuilder()
               .setName(
                   WorkspaceName.of("[PROJECT]", "[LOCATION]", "[REPOSITORY]", "[WORKSPACE]")
                       .toString())
               .addAllPaths(new ArrayList<String>())
               .setClean(true)
               .build();
       ApiFuture<ResetWorkspaceChangesResponse> future =
           dataformClient.resetWorkspaceChangesCallable().futureCall(request);
       // Do something.
       ResetWorkspaceChangesResponse response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ResetWorkspaceChangesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataform/latest/com.google.cloud.dataform.v1beta1.ResetWorkspaceChangesRequest),[ResetWorkspaceChangesResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataform/latest/com.google.cloud.dataform.v1beta1.ResetWorkspaceChangesResponse)>` |   
  
### searchFiles(SearchFilesRequest request)
    
    
    public final DataformClient.SearchFilesPagedResponse searchFiles(SearchFilesRequest request)

Finds the contents of a given Workspace directory by filter.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DataformClient dataformClient = DataformClient.create()) {
       SearchFilesRequest request =
           SearchFilesRequest.newBuilder()
               .setWorkspace(
                   WorkspaceName.of("[PROJECT]", "[LOCATION]", "[REPOSITORY]", "[WORKSPACE]")
                       .toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .setFilter("filter-1274492040")
               .build();
       for (SearchResult element : dataformClient.searchFiles(request).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[SearchFilesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataform/latest/com.google.cloud.dataform.v1beta1.SearchFilesRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[DataformClient.SearchFilesPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataform/latest/com.google.cloud.dataform.v1beta1.DataformClient.SearchFilesPagedResponse)` |   
  
### searchFilesCallable()
    
    
    public final UnaryCallable<SearchFilesRequest,SearchFilesResponse> searchFilesCallable()

Finds the contents of a given Workspace directory by filter.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DataformClient dataformClient = DataformClient.create()) {
       SearchFilesRequest request =
           SearchFilesRequest.newBuilder()
               .setWorkspace(
                   WorkspaceName.of("[PROJECT]", "[LOCATION]", "[REPOSITORY]", "[WORKSPACE]")
                       .toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .setFilter("filter-1274492040")
               .build();
       while (true) {
         SearchFilesResponse response = dataformClient.searchFilesCallable().call(request);
         for (SearchResult element : response.getSearchResultsList()) {
           // doThingsWith(element);
         }
         String nextPageToken = response.getNextPageToken();
         if (!Strings.isNullOrEmpty(nextPageToken)) {
           request = request.toBuilder().setPageToken(nextPageToken).build();
         } else {
           break;
         }
       }
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[SearchFilesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataform/latest/com.google.cloud.dataform.v1beta1.SearchFilesRequest),[SearchFilesResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataform/latest/com.google.cloud.dataform.v1beta1.SearchFilesResponse)>` |   
  
### searchFilesPagedCallable()
    
    
    public final UnaryCallable<SearchFilesRequest,DataformClient.SearchFilesPagedResponse> searchFilesPagedCallable()

Finds the contents of a given Workspace directory by filter.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DataformClient dataformClient = DataformClient.create()) {
       SearchFilesRequest request =
           SearchFilesRequest.newBuilder()
               .setWorkspace(
                   WorkspaceName.of("[PROJECT]", "[LOCATION]", "[REPOSITORY]", "[WORKSPACE]")
                       .toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .setFilter("filter-1274492040")
               .build();
       ApiFuture<SearchResult> future =
           dataformClient.searchFilesPagedCallable().futureCall(request);
       // Do something.
       for (SearchResult element : future.get().iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[SearchFilesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataform/latest/com.google.cloud.dataform.v1beta1.SearchFilesRequest),[SearchFilesPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataform/latest/com.google.cloud.dataform.v1beta1.DataformClient.SearchFilesPagedResponse)>` |   
  
### searchTeamFolders(SearchTeamFoldersRequest request)
    
    
    public final DataformClient.SearchTeamFoldersPagedResponse searchTeamFolders(SearchTeamFoldersRequest request)

Returns all TeamFolders in a given location that the caller has access to and match the provided filter.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DataformClient dataformClient = DataformClient.create()) {
       SearchTeamFoldersRequest request =
           SearchTeamFoldersRequest.newBuilder()
               .setLocation(LocationName.of("[PROJECT]", "[LOCATION]").toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .setOrderBy("orderBy-1207110587")
               .setFilter("filter-1274492040")
               .build();
       for (SearchTeamFoldersResponse.TeamFolderSearchResult element :
           dataformClient.searchTeamFolders(request).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[SearchTeamFoldersRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataform/latest/com.google.cloud.dataform.v1beta1.SearchTeamFoldersRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[DataformClient.SearchTeamFoldersPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataform/latest/com.google.cloud.dataform.v1beta1.DataformClient.SearchTeamFoldersPagedResponse)` |   
  
### searchTeamFoldersCallable()
    
    
    public final UnaryCallable<SearchTeamFoldersRequest,SearchTeamFoldersResponse> searchTeamFoldersCallable()

Returns all TeamFolders in a given location that the caller has access to and match the provided filter.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DataformClient dataformClient = DataformClient.create()) {
       SearchTeamFoldersRequest request =
           SearchTeamFoldersRequest.newBuilder()
               .setLocation(LocationName.of("[PROJECT]", "[LOCATION]").toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .setOrderBy("orderBy-1207110587")
               .setFilter("filter-1274492040")
               .build();
       while (true) {
         SearchTeamFoldersResponse response =
             dataformClient.searchTeamFoldersCallable().call(request);
         for (SearchTeamFoldersResponse.TeamFolderSearchResult element : response.getResultsList()) {
           // doThingsWith(element);
         }
         String nextPageToken = response.getNextPageToken();
         if (!Strings.isNullOrEmpty(nextPageToken)) {
           request = request.toBuilder().setPageToken(nextPageToken).build();
         } else {
           break;
         }
       }
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[SearchTeamFoldersRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataform/latest/com.google.cloud.dataform.v1beta1.SearchTeamFoldersRequest),[SearchTeamFoldersResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataform/latest/com.google.cloud.dataform.v1beta1.SearchTeamFoldersResponse)>` |   
  
### searchTeamFoldersPagedCallable()
    
    
    public final UnaryCallable<SearchTeamFoldersRequest,DataformClient.SearchTeamFoldersPagedResponse> searchTeamFoldersPagedCallable()

Returns all TeamFolders in a given location that the caller has access to and match the provided filter.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DataformClient dataformClient = DataformClient.create()) {
       SearchTeamFoldersRequest request =
           SearchTeamFoldersRequest.newBuilder()
               .setLocation(LocationName.of("[PROJECT]", "[LOCATION]").toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .setOrderBy("orderBy-1207110587")
               .setFilter("filter-1274492040")
               .build();
       ApiFuture<SearchTeamFoldersResponse.TeamFolderSearchResult> future =
           dataformClient.searchTeamFoldersPagedCallable().futureCall(request);
       // Do something.
       for (SearchTeamFoldersResponse.TeamFolderSearchResult element : future.get().iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[SearchTeamFoldersRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataform/latest/com.google.cloud.dataform.v1beta1.SearchTeamFoldersRequest),[SearchTeamFoldersPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataform/latest/com.google.cloud.dataform.v1beta1.DataformClient.SearchTeamFoldersPagedResponse)>` |   
  
### setIamPolicy(SetIamPolicyRequest request)
    
    
    public final Policy setIamPolicy(SetIamPolicyRequest request)

Sets the access control policy on the specified resource. Replaces any existing policy.

Can return `NOT_FOUND`, `INVALID_ARGUMENT`, and `PERMISSION_DENIED` errors.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DataformClient dataformClient = DataformClient.create()) {
       SetIamPolicyRequest request =
           SetIamPolicyRequest.newBuilder()
               .setResource(FolderName.of("[PROJECT]", "[LOCATION]", "[FOLDER]").toString())
               .setPolicy(Policy.newBuilder().build())
               .setUpdateMask(FieldMask.newBuilder().build())
               .build();
       Policy response = dataformClient.setIamPolicy(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `com.google.iam.v1.SetIamPolicyRequest`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`com.google.iam.v1.Policy` |   
  
### setIamPolicyCallable()
    
    
    public final UnaryCallable<SetIamPolicyRequest,Policy> setIamPolicyCallable()

Sets the access control policy on the specified resource. Replaces any existing policy.

Can return `NOT_FOUND`, `INVALID_ARGUMENT`, and `PERMISSION_DENIED` errors.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DataformClient dataformClient = DataformClient.create()) {
       SetIamPolicyRequest request =
           SetIamPolicyRequest.newBuilder()
               .setResource(FolderName.of("[PROJECT]", "[LOCATION]", "[FOLDER]").toString())
               .setPolicy(Policy.newBuilder().build())
               .setUpdateMask(FieldMask.newBuilder().build())
               .build();
       ApiFuture<Policy> future = dataformClient.setIamPolicyCallable().futureCall(request);
       // Do something.
       Policy response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<com.google.iam.v1.SetIamPolicyRequest,com.google.iam.v1.Policy>` |   
  
### shutdown()
    
    
    public void shutdown()

### shutdownNow()
    
    
    public void shutdownNow()

### syncWorkspaceRefs(SyncWorkspaceRefsRequest request)
    
    
    public final SyncWorkspaceRefsResponse syncWorkspaceRefs(SyncWorkspaceRefsRequest request)

Syncs the refs of a Workspace.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DataformClient dataformClient = DataformClient.create()) {
       SyncWorkspaceRefsRequest request =
           SyncWorkspaceRefsRequest.newBuilder()
               .setName(
                   WorkspaceName.of("[PROJECT]", "[LOCATION]", "[REPOSITORY]", "[WORKSPACE]")
                       .toString())
               .setRemoteBranchName("remoteBranchName2129930291")
               .setDeepen(-1335656811)
               .build();
       SyncWorkspaceRefsResponse response = dataformClient.syncWorkspaceRefs(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[SyncWorkspaceRefsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataform/latest/com.google.cloud.dataform.v1beta1.SyncWorkspaceRefsRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[SyncWorkspaceRefsResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataform/latest/com.google.cloud.dataform.v1beta1.SyncWorkspaceRefsResponse)` |   
  
### syncWorkspaceRefsCallable()
    
    
    public final UnaryCallable<SyncWorkspaceRefsRequest,SyncWorkspaceRefsResponse> syncWorkspaceRefsCallable()

Syncs the refs of a Workspace.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DataformClient dataformClient = DataformClient.create()) {
       SyncWorkspaceRefsRequest request =
           SyncWorkspaceRefsRequest.newBuilder()
               .setName(
                   WorkspaceName.of("[PROJECT]", "[LOCATION]", "[REPOSITORY]", "[WORKSPACE]")
                       .toString())
               .setRemoteBranchName("remoteBranchName2129930291")
               .setDeepen(-1335656811)
               .build();
       ApiFuture<SyncWorkspaceRefsResponse> future =
           dataformClient.syncWorkspaceRefsCallable().futureCall(request);
       // Do something.
       SyncWorkspaceRefsResponse response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[SyncWorkspaceRefsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataform/latest/com.google.cloud.dataform.v1beta1.SyncWorkspaceRefsRequest),[SyncWorkspaceRefsResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataform/latest/com.google.cloud.dataform.v1beta1.SyncWorkspaceRefsResponse)>` |   
  
### testIamPermissions(TestIamPermissionsRequest request)
    
    
    public final TestIamPermissionsResponse testIamPermissions(TestIamPermissionsRequest request)

Returns permissions that a caller has on the specified resource. If the resource does not exist, this will return an empty set of permissions, not a `NOT_FOUND` error.

Note: This operation is designed to be used for building permission-aware UIs and command-line tools, not for authorization checking. This operation may "fail open" without warning.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DataformClient dataformClient = DataformClient.create()) {
       TestIamPermissionsRequest request =
           TestIamPermissionsRequest.newBuilder()
               .setResource(FolderName.of("[PROJECT]", "[LOCATION]", "[FOLDER]").toString())
               .addAllPermissions(new ArrayList<String>())
               .build();
       TestIamPermissionsResponse response = dataformClient.testIamPermissions(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `com.google.iam.v1.TestIamPermissionsRequest`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`com.google.iam.v1.TestIamPermissionsResponse` |   
  
### testIamPermissionsCallable()
    
    
    public final UnaryCallable<TestIamPermissionsRequest,TestIamPermissionsResponse> testIamPermissionsCallable()

Returns permissions that a caller has on the specified resource. If the resource does not exist, this will return an empty set of permissions, not a `NOT_FOUND` error.

Note: This operation is designed to be used for building permission-aware UIs and command-line tools, not for authorization checking. This operation may "fail open" without warning.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DataformClient dataformClient = DataformClient.create()) {
       TestIamPermissionsRequest request =
           TestIamPermissionsRequest.newBuilder()
               .setResource(FolderName.of("[PROJECT]", "[LOCATION]", "[FOLDER]").toString())
               .addAllPermissions(new ArrayList<String>())
               .build();
       ApiFuture<TestIamPermissionsResponse> future =
           dataformClient.testIamPermissionsCallable().futureCall(request);
       // Do something.
       TestIamPermissionsResponse response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<com.google.iam.v1.TestIamPermissionsRequest,com.google.iam.v1.TestIamPermissionsResponse>` |   
  
### updateConfig(Config config, FieldMask updateMask)
    
    
    public final Config updateConfig(Config config, FieldMask updateMask)

Update default config for a given project and location.

**Note:** *This method does not fully implement [AIP/134](https://google.aip.dev/134). The wildcard entry (\\*) is treated as a bad request, and when the `field_mask` is omitted, the request is treated as a full update on all modifiable fields.*

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DataformClient dataformClient = DataformClient.create()) {
       Config config = Config.newBuilder().build();
       FieldMask updateMask = FieldMask.newBuilder().build();
       Config response = dataformClient.updateConfig(config, updateMask);
     }
     

**Parameters**  
---  
**Name** | **Description**  
`config` | `[Config](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataform/latest/com.google.cloud.dataform.v1beta1.Config)`  
Required. The config to update.  
`updateMask` | `[FieldMask](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.FieldMask.html)`  
Optional. Specifies the fields to be updated in the config.  
**Returns**  
---  
**Type** | **Description**  
`[Config](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataform/latest/com.google.cloud.dataform.v1beta1.Config)` |   
  
### updateConfig(UpdateConfigRequest request)
    
    
    public final Config updateConfig(UpdateConfigRequest request)

Update default config for a given project and location.

**Note:** *This method does not fully implement [AIP/134](https://google.aip.dev/134). The wildcard entry (\\*) is treated as a bad request, and when the `field_mask` is omitted, the request is treated as a full update on all modifiable fields.*

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DataformClient dataformClient = DataformClient.create()) {
       UpdateConfigRequest request =
           UpdateConfigRequest.newBuilder()
               .setConfig(Config.newBuilder().build())
               .setUpdateMask(FieldMask.newBuilder().build())
               .build();
       Config response = dataformClient.updateConfig(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[UpdateConfigRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataform/latest/com.google.cloud.dataform.v1beta1.UpdateConfigRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[Config](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataform/latest/com.google.cloud.dataform.v1beta1.Config)` |   
  
### updateConfigCallable()
    
    
    public final UnaryCallable<UpdateConfigRequest,Config> updateConfigCallable()

Update default config for a given project and location.

**Note:** *This method does not fully implement [AIP/134](https://google.aip.dev/134). The wildcard entry (\\*) is treated as a bad request, and when the `field_mask` is omitted, the request is treated as a full update on all modifiable fields.*

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DataformClient dataformClient = DataformClient.create()) {
       UpdateConfigRequest request =
           UpdateConfigRequest.newBuilder()
               .setConfig(Config.newBuilder().build())
               .setUpdateMask(FieldMask.newBuilder().build())
               .build();
       ApiFuture<Config> future = dataformClient.updateConfigCallable().futureCall(request);
       // Do something.
       Config response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[UpdateConfigRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataform/latest/com.google.cloud.dataform.v1beta1.UpdateConfigRequest),[Config](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataform/latest/com.google.cloud.dataform.v1beta1.Config)>` |   
  
### updateFolder(Folder folder, FieldMask updateMask)
    
    
    public final Folder updateFolder(Folder folder, FieldMask updateMask)

Updates a single Folder.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DataformClient dataformClient = DataformClient.create()) {
       Folder folder = Folder.newBuilder().build();
       FieldMask updateMask = FieldMask.newBuilder().build();
       Folder response = dataformClient.updateFolder(folder, updateMask);
     }
     

**Parameters**  
---  
**Name** | **Description**  
`folder` | `[Folder](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataform/latest/com.google.cloud.dataform.v1beta1.Folder)`  
Required. The updated Folder.  
`updateMask` | `[FieldMask](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.FieldMask.html)`  
Optional. Specifies the fields to be updated in the Folder. If left unset, all fields that can be updated, will be updated. A few fields cannot be updated and will be ignored if specified in the update_mask (e.g. parent_name, team_folder_name).  
**Returns**  
---  
**Type** | **Description**  
`[Folder](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataform/latest/com.google.cloud.dataform.v1beta1.Folder)` |   
  
### updateFolder(UpdateFolderRequest request)
    
    
    public final Folder updateFolder(UpdateFolderRequest request)

Updates a single Folder.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DataformClient dataformClient = DataformClient.create()) {
       UpdateFolderRequest request =
           UpdateFolderRequest.newBuilder()
               .setUpdateMask(FieldMask.newBuilder().build())
               .setFolder(Folder.newBuilder().build())
               .build();
       Folder response = dataformClient.updateFolder(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[UpdateFolderRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataform/latest/com.google.cloud.dataform.v1beta1.UpdateFolderRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[Folder](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataform/latest/com.google.cloud.dataform.v1beta1.Folder)` |   
  
### updateFolderCallable()
    
    
    public final UnaryCallable<UpdateFolderRequest,Folder> updateFolderCallable()

Updates a single Folder.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DataformClient dataformClient = DataformClient.create()) {
       UpdateFolderRequest request =
           UpdateFolderRequest.newBuilder()
               .setUpdateMask(FieldMask.newBuilder().build())
               .setFolder(Folder.newBuilder().build())
               .build();
       ApiFuture<Folder> future = dataformClient.updateFolderCallable().futureCall(request);
       // Do something.
       Folder response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[UpdateFolderRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataform/latest/com.google.cloud.dataform.v1beta1.UpdateFolderRequest),[Folder](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataform/latest/com.google.cloud.dataform.v1beta1.Folder)>` |   
  
### updateReleaseConfig(ReleaseConfig releaseConfig, FieldMask updateMask)
    
    
    public final ReleaseConfig updateReleaseConfig(ReleaseConfig releaseConfig, FieldMask updateMask)

Updates a single ReleaseConfig.

**Note:** *This method does not fully implement [AIP/134](https://google.aip.dev/134). The wildcard entry (\\*) is treated as a bad request, and when the `field_mask` is omitted, the request is treated as a full update on all modifiable fields.*

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DataformClient dataformClient = DataformClient.create()) {
       ReleaseConfig releaseConfig = ReleaseConfig.newBuilder().build();
       FieldMask updateMask = FieldMask.newBuilder().build();
       ReleaseConfig response = dataformClient.updateReleaseConfig(releaseConfig, updateMask);
     }
     

**Parameters**  
---  
**Name** | **Description**  
`releaseConfig` | `[ReleaseConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataform/latest/com.google.cloud.dataform.v1beta1.ReleaseConfig)`  
Required. The release config to update.  
`updateMask` | `[FieldMask](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.FieldMask.html)`  
Optional. Specifies the fields to be updated in the release config. If left unset, all fields will be updated.  
**Returns**  
---  
**Type** | **Description**  
`[ReleaseConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataform/latest/com.google.cloud.dataform.v1beta1.ReleaseConfig)` |   
  
### updateReleaseConfig(UpdateReleaseConfigRequest request)
    
    
    public final ReleaseConfig updateReleaseConfig(UpdateReleaseConfigRequest request)

Updates a single ReleaseConfig.

**Note:** *This method does not fully implement [AIP/134](https://google.aip.dev/134). The wildcard entry (\\*) is treated as a bad request, and when the `field_mask` is omitted, the request is treated as a full update on all modifiable fields.*

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DataformClient dataformClient = DataformClient.create()) {
       UpdateReleaseConfigRequest request =
           UpdateReleaseConfigRequest.newBuilder()
               .setUpdateMask(FieldMask.newBuilder().build())
               .setReleaseConfig(ReleaseConfig.newBuilder().build())
               .build();
       ReleaseConfig response = dataformClient.updateReleaseConfig(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[UpdateReleaseConfigRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataform/latest/com.google.cloud.dataform.v1beta1.UpdateReleaseConfigRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[ReleaseConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataform/latest/com.google.cloud.dataform.v1beta1.ReleaseConfig)` |   
  
### updateReleaseConfigCallable()
    
    
    public final UnaryCallable<UpdateReleaseConfigRequest,ReleaseConfig> updateReleaseConfigCallable()

Updates a single ReleaseConfig.

**Note:** *This method does not fully implement [AIP/134](https://google.aip.dev/134). The wildcard entry (\\*) is treated as a bad request, and when the `field_mask` is omitted, the request is treated as a full update on all modifiable fields.*

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DataformClient dataformClient = DataformClient.create()) {
       UpdateReleaseConfigRequest request =
           UpdateReleaseConfigRequest.newBuilder()
               .setUpdateMask(FieldMask.newBuilder().build())
               .setReleaseConfig(ReleaseConfig.newBuilder().build())
               .build();
       ApiFuture<ReleaseConfig> future =
           dataformClient.updateReleaseConfigCallable().futureCall(request);
       // Do something.
       ReleaseConfig response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[UpdateReleaseConfigRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataform/latest/com.google.cloud.dataform.v1beta1.UpdateReleaseConfigRequest),[ReleaseConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataform/latest/com.google.cloud.dataform.v1beta1.ReleaseConfig)>` |   
  
### updateRepository(Repository repository, FieldMask updateMask)
    
    
    public final Repository updateRepository(Repository repository, FieldMask updateMask)

Updates a single Repository.

**Note:** *This method does not fully implement [AIP/134](https://google.aip.dev/134). The wildcard entry (\\*) is treated as a bad request, and when the `field_mask` is omitted, the request is treated as a full update on all modifiable fields.*

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DataformClient dataformClient = DataformClient.create()) {
       Repository repository = Repository.newBuilder().build();
       FieldMask updateMask = FieldMask.newBuilder().build();
       Repository response = dataformClient.updateRepository(repository, updateMask);
     }
     

**Parameters**  
---  
**Name** | **Description**  
`repository` | `[Repository](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataform/latest/com.google.cloud.dataform.v1beta1.Repository)`  
Required. The repository to update.  
`updateMask` | `[FieldMask](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.FieldMask.html)`  
Optional. Specifies the fields to be updated in the repository. If left unset, all fields will be updated.  
**Returns**  
---  
**Type** | **Description**  
`[Repository](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataform/latest/com.google.cloud.dataform.v1beta1.Repository)` |   
  
### updateRepository(UpdateRepositoryRequest request)
    
    
    public final Repository updateRepository(UpdateRepositoryRequest request)

Updates a single Repository.

**Note:** *This method does not fully implement [AIP/134](https://google.aip.dev/134). The wildcard entry (\\*) is treated as a bad request, and when the `field_mask` is omitted, the request is treated as a full update on all modifiable fields.*

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DataformClient dataformClient = DataformClient.create()) {
       UpdateRepositoryRequest request =
           UpdateRepositoryRequest.newBuilder()
               .setUpdateMask(FieldMask.newBuilder().build())
               .setRepository(Repository.newBuilder().build())
               .build();
       Repository response = dataformClient.updateRepository(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[UpdateRepositoryRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataform/latest/com.google.cloud.dataform.v1beta1.UpdateRepositoryRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[Repository](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataform/latest/com.google.cloud.dataform.v1beta1.Repository)` |   
  
### updateRepositoryCallable()
    
    
    public final UnaryCallable<UpdateRepositoryRequest,Repository> updateRepositoryCallable()

Updates a single Repository.

**Note:** *This method does not fully implement [AIP/134](https://google.aip.dev/134). The wildcard entry (\\*) is treated as a bad request, and when the `field_mask` is omitted, the request is treated as a full update on all modifiable fields.*

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DataformClient dataformClient = DataformClient.create()) {
       UpdateRepositoryRequest request =
           UpdateRepositoryRequest.newBuilder()
               .setUpdateMask(FieldMask.newBuilder().build())
               .setRepository(Repository.newBuilder().build())
               .build();
       ApiFuture<Repository> future = dataformClient.updateRepositoryCallable().futureCall(request);
       // Do something.
       Repository response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[UpdateRepositoryRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataform/latest/com.google.cloud.dataform.v1beta1.UpdateRepositoryRequest),[Repository](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataform/latest/com.google.cloud.dataform.v1beta1.Repository)>` |   
  
### updateTeamFolder(TeamFolder teamFolder, FieldMask updateMask)
    
    
    public final TeamFolder updateTeamFolder(TeamFolder teamFolder, FieldMask updateMask)

Updates a single TeamFolder.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DataformClient dataformClient = DataformClient.create()) {
       TeamFolder teamFolder = TeamFolder.newBuilder().build();
       FieldMask updateMask = FieldMask.newBuilder().build();
       TeamFolder response = dataformClient.updateTeamFolder(teamFolder, updateMask);
     }
     

**Parameters**  
---  
**Name** | **Description**  
`teamFolder` | `[TeamFolder](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataform/latest/com.google.cloud.dataform.v1beta1.TeamFolder)`  
Required. The updated TeamFolder.  
`updateMask` | `[FieldMask](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.FieldMask.html)`  
Optional. Specifies the fields to be updated in the Folder. If left unset, all fields will be updated.  
**Returns**  
---  
**Type** | **Description**  
`[TeamFolder](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataform/latest/com.google.cloud.dataform.v1beta1.TeamFolder)` |   
  
### updateTeamFolder(UpdateTeamFolderRequest request)
    
    
    public final TeamFolder updateTeamFolder(UpdateTeamFolderRequest request)

Updates a single TeamFolder.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DataformClient dataformClient = DataformClient.create()) {
       UpdateTeamFolderRequest request =
           UpdateTeamFolderRequest.newBuilder()
               .setUpdateMask(FieldMask.newBuilder().build())
               .setTeamFolder(TeamFolder.newBuilder().build())
               .build();
       TeamFolder response = dataformClient.updateTeamFolder(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[UpdateTeamFolderRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataform/latest/com.google.cloud.dataform.v1beta1.UpdateTeamFolderRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[TeamFolder](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataform/latest/com.google.cloud.dataform.v1beta1.TeamFolder)` |   
  
### updateTeamFolderCallable()
    
    
    public final UnaryCallable<UpdateTeamFolderRequest,TeamFolder> updateTeamFolderCallable()

Updates a single TeamFolder.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DataformClient dataformClient = DataformClient.create()) {
       UpdateTeamFolderRequest request =
           UpdateTeamFolderRequest.newBuilder()
               .setUpdateMask(FieldMask.newBuilder().build())
               .setTeamFolder(TeamFolder.newBuilder().build())
               .build();
       ApiFuture<TeamFolder> future = dataformClient.updateTeamFolderCallable().futureCall(request);
       // Do something.
       TeamFolder response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[UpdateTeamFolderRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataform/latest/com.google.cloud.dataform.v1beta1.UpdateTeamFolderRequest),[TeamFolder](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataform/latest/com.google.cloud.dataform.v1beta1.TeamFolder)>` |   
  
### updateWorkflowConfig(UpdateWorkflowConfigRequest request)
    
    
    public final WorkflowConfig updateWorkflowConfig(UpdateWorkflowConfigRequest request)

Updates a single WorkflowConfig.

**Note:** *This method does not fully implement [AIP/134](https://google.aip.dev/134). The wildcard entry (\\*) is treated as a bad request, and when the `field_mask` is omitted, the request is treated as a full update on all modifiable fields.*

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DataformClient dataformClient = DataformClient.create()) {
       UpdateWorkflowConfigRequest request =
           UpdateWorkflowConfigRequest.newBuilder()
               .setUpdateMask(FieldMask.newBuilder().build())
               .setWorkflowConfig(WorkflowConfig.newBuilder().build())
               .build();
       WorkflowConfig response = dataformClient.updateWorkflowConfig(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[UpdateWorkflowConfigRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataform/latest/com.google.cloud.dataform.v1beta1.UpdateWorkflowConfigRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[WorkflowConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataform/latest/com.google.cloud.dataform.v1beta1.WorkflowConfig)` |   
  
### updateWorkflowConfig(WorkflowConfig workflowConfig, FieldMask updateMask)
    
    
    public final WorkflowConfig updateWorkflowConfig(WorkflowConfig workflowConfig, FieldMask updateMask)

Updates a single WorkflowConfig.

**Note:** *This method does not fully implement [AIP/134](https://google.aip.dev/134). The wildcard entry (\\*) is treated as a bad request, and when the `field_mask` is omitted, the request is treated as a full update on all modifiable fields.*

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DataformClient dataformClient = DataformClient.create()) {
       WorkflowConfig workflowConfig = WorkflowConfig.newBuilder().build();
       FieldMask updateMask = FieldMask.newBuilder().build();
       WorkflowConfig response = dataformClient.updateWorkflowConfig(workflowConfig, updateMask);
     }
     

**Parameters**  
---  
**Name** | **Description**  
`workflowConfig` | `[WorkflowConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataform/latest/com.google.cloud.dataform.v1beta1.WorkflowConfig)`  
Required. The workflow config to update.  
`updateMask` | `[FieldMask](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.FieldMask.html)`  
Optional. Specifies the fields to be updated in the workflow config. If left unset, all fields will be updated.  
**Returns**  
---  
**Type** | **Description**  
`[WorkflowConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataform/latest/com.google.cloud.dataform.v1beta1.WorkflowConfig)` |   
  
### updateWorkflowConfigCallable()
    
    
    public final UnaryCallable<UpdateWorkflowConfigRequest,WorkflowConfig> updateWorkflowConfigCallable()

Updates a single WorkflowConfig.

**Note:** *This method does not fully implement [AIP/134](https://google.aip.dev/134). The wildcard entry (\\*) is treated as a bad request, and when the `field_mask` is omitted, the request is treated as a full update on all modifiable fields.*

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DataformClient dataformClient = DataformClient.create()) {
       UpdateWorkflowConfigRequest request =
           UpdateWorkflowConfigRequest.newBuilder()
               .setUpdateMask(FieldMask.newBuilder().build())
               .setWorkflowConfig(WorkflowConfig.newBuilder().build())
               .build();
       ApiFuture<WorkflowConfig> future =
           dataformClient.updateWorkflowConfigCallable().futureCall(request);
       // Do something.
       WorkflowConfig response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[UpdateWorkflowConfigRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataform/latest/com.google.cloud.dataform.v1beta1.UpdateWorkflowConfigRequest),[WorkflowConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataform/latest/com.google.cloud.dataform.v1beta1.WorkflowConfig)>` |   
  
### writeFile(WriteFileRequest request)
    
    
    public final WriteFileResponse writeFile(WriteFileRequest request)

Writes to a file (inside a Workspace).

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DataformClient dataformClient = DataformClient.create()) {
       WriteFileRequest request =
           WriteFileRequest.newBuilder()
               .setWorkspace(
                   WorkspaceName.of("[PROJECT]", "[LOCATION]", "[REPOSITORY]", "[WORKSPACE]")
                       .toString())
               .setPath("path3433509")
               .setContents(ByteString.EMPTY)
               .build();
       WriteFileResponse response = dataformClient.writeFile(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[WriteFileRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataform/latest/com.google.cloud.dataform.v1beta1.WriteFileRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[WriteFileResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataform/latest/com.google.cloud.dataform.v1beta1.WriteFileResponse)` |   
  
### writeFileCallable()
    
    
    public final UnaryCallable<WriteFileRequest,WriteFileResponse> writeFileCallable()

Writes to a file (inside a Workspace).

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DataformClient dataformClient = DataformClient.create()) {
       WriteFileRequest request =
           WriteFileRequest.newBuilder()
               .setWorkspace(
                   WorkspaceName.of("[PROJECT]", "[LOCATION]", "[REPOSITORY]", "[WORKSPACE]")
                       .toString())
               .setPath("path3433509")
               .setContents(ByteString.EMPTY)
               .build();
       ApiFuture<WriteFileResponse> future = dataformClient.writeFileCallable().futureCall(request);
       // Do something.
       WriteFileResponse response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[WriteFileRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataform/latest/com.google.cloud.dataform.v1beta1.WriteFileRequest),[WriteFileResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataform/latest/com.google.cloud.dataform.v1beta1.WriteFileResponse)>` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-06 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-06 UTC."],[],[]] 
