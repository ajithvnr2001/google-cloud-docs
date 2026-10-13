---
url: https://docs.cloud.google.com/java/docs/reference/google-cloud-dataform/latest/com.google.cloud.dataform.v1.DataformGrpc.AsyncService
title: Interface DataformGrpc.AsyncService (0.98.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:51:50.467407+00:00
---

# Interface DataformGrpc.AsyncService (0.98.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-cloud-dataform/latest/com.google.cloud.dataform.v1.DataformGrpc.AsyncService

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Interface DataformGrpc.AsyncService (0.98.0) Stay organized with collections  Save and categorize content based on your preferences. 

0.98.0 (latest)  0.94.0  0.93.0  0.92.0  0.90.0  0.87.0  0.86.0  0.84.0  0.82.0  0.81.0  0.80.0  0.79.0  0.77.0  0.75.0  0.74.0  0.73.0  0.72.0  0.71.0  0.69.0  0.67.0  0.66.0  0.63.0  0.62.0  0.61.0  0.59.0  0.58.0  0.57.0  0.56.0  0.55.0  0.54.0  0.53.0  0.52.0  0.51.0  0.50.0  0.48.0  0.47.0  0.46.0  0.45.0  0.44.0  0.43.0  0.42.0  0.41.0  0.40.0  0.39.0  0.38.0  0.36.0  0.35.0  0.34.0  0.33.0  0.32.0  0.31.0  0.30.0  0.29.0  0.28.0  0.27.0  0.26.0  0.23.0  0.22.0  0.21.0  0.20.0  0.19.0  0.18.0  0.17.0  0.16.0  0.15.0  0.14.0  0.13.0  0.12.0  0.11.0  0.10.0  0.8.0  0.7.0  0.6.0  0.5.0  0.4.0  0.3.0  0.2.4 
    
    
    public static interface DataformGrpc.AsyncService

Dataform is a service to develop, create, document, test, and update curated tables in BigQuery.

## Methods 

### cancelWorkflowInvocation(CancelWorkflowInvocationRequest request, StreamObserver<CancelWorkflowInvocationResponse> responseObserver)
    
    
    public default void cancelWorkflowInvocation(CancelWorkflowInvocationRequest request, StreamObserver<CancelWorkflowInvocationResponse> responseObserver)

Requests cancellation of a running WorkflowInvocation.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[CancelWorkflowInvocationRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataform/latest/com.google.cloud.dataform.v1.CancelWorkflowInvocationRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[CancelWorkflowInvocationResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataform/latest/com.google.cloud.dataform.v1.CancelWorkflowInvocationResponse)>`  
  
  
### commitRepositoryChanges(CommitRepositoryChangesRequest request, StreamObserver<CommitRepositoryChangesResponse> responseObserver)
    
    
    public default void commitRepositoryChanges(CommitRepositoryChangesRequest request, StreamObserver<CommitRepositoryChangesResponse> responseObserver)

Applies a Git commit to a Repository. The Repository must not have a value for `git_remote_settings.url`.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[CommitRepositoryChangesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataform/latest/com.google.cloud.dataform.v1.CommitRepositoryChangesRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[CommitRepositoryChangesResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataform/latest/com.google.cloud.dataform.v1.CommitRepositoryChangesResponse)>`  
  
  
### commitWorkspaceChanges(CommitWorkspaceChangesRequest request, StreamObserver<CommitWorkspaceChangesResponse> responseObserver)
    
    
    public default void commitWorkspaceChanges(CommitWorkspaceChangesRequest request, StreamObserver<CommitWorkspaceChangesResponse> responseObserver)

Applies a Git commit for uncommitted files in a Workspace.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[CommitWorkspaceChangesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataform/latest/com.google.cloud.dataform.v1.CommitWorkspaceChangesRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[CommitWorkspaceChangesResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataform/latest/com.google.cloud.dataform.v1.CommitWorkspaceChangesResponse)>`  
  
  
### computeRepositoryAccessTokenStatus(ComputeRepositoryAccessTokenStatusRequest request, StreamObserver<ComputeRepositoryAccessTokenStatusResponse> responseObserver)
    
    
    public default void computeRepositoryAccessTokenStatus(ComputeRepositoryAccessTokenStatusRequest request, StreamObserver<ComputeRepositoryAccessTokenStatusResponse> responseObserver)

Computes a Repository's Git access token status.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ComputeRepositoryAccessTokenStatusRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataform/latest/com.google.cloud.dataform.v1.ComputeRepositoryAccessTokenStatusRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[ComputeRepositoryAccessTokenStatusResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataform/latest/com.google.cloud.dataform.v1.ComputeRepositoryAccessTokenStatusResponse)>`  
  
  
### createCompilationResult(CreateCompilationResultRequest request, StreamObserver<CompilationResult> responseObserver)
    
    
    public default void createCompilationResult(CreateCompilationResultRequest request, StreamObserver<CompilationResult> responseObserver)

Creates a new CompilationResult in a given project and location.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[CreateCompilationResultRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataform/latest/com.google.cloud.dataform.v1.CreateCompilationResultRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[CompilationResult](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataform/latest/com.google.cloud.dataform.v1.CompilationResult)>`  
  
  
### createFolder(CreateFolderRequest request, StreamObserver<Folder> responseObserver)
    
    
    public default void createFolder(CreateFolderRequest request, StreamObserver<Folder> responseObserver)

Creates a new Folder in a given project and location.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[CreateFolderRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataform/latest/com.google.cloud.dataform.v1.CreateFolderRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[Folder](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataform/latest/com.google.cloud.dataform.v1.Folder)>`  
  
  
### createReleaseConfig(CreateReleaseConfigRequest request, StreamObserver<ReleaseConfig> responseObserver)
    
    
    public default void createReleaseConfig(CreateReleaseConfigRequest request, StreamObserver<ReleaseConfig> responseObserver)

Creates a new ReleaseConfig in a given Repository.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[CreateReleaseConfigRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataform/latest/com.google.cloud.dataform.v1.CreateReleaseConfigRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[ReleaseConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataform/latest/com.google.cloud.dataform.v1.ReleaseConfig)>`  
  
  
### createRepository(CreateRepositoryRequest request, StreamObserver<Repository> responseObserver)
    
    
    public default void createRepository(CreateRepositoryRequest request, StreamObserver<Repository> responseObserver)

Creates a new Repository in a given project and location.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[CreateRepositoryRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataform/latest/com.google.cloud.dataform.v1.CreateRepositoryRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[Repository](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataform/latest/com.google.cloud.dataform.v1.Repository)>`  
  
  
### createTeamFolder(CreateTeamFolderRequest request, StreamObserver<TeamFolder> responseObserver)
    
    
    public default void createTeamFolder(CreateTeamFolderRequest request, StreamObserver<TeamFolder> responseObserver)

Creates a new TeamFolder in a given project and location.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[CreateTeamFolderRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataform/latest/com.google.cloud.dataform.v1.CreateTeamFolderRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[TeamFolder](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataform/latest/com.google.cloud.dataform.v1.TeamFolder)>`  
  
  
### createWorkflowConfig(CreateWorkflowConfigRequest request, StreamObserver<WorkflowConfig> responseObserver)
    
    
    public default void createWorkflowConfig(CreateWorkflowConfigRequest request, StreamObserver<WorkflowConfig> responseObserver)

Creates a new WorkflowConfig in a given Repository.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[CreateWorkflowConfigRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataform/latest/com.google.cloud.dataform.v1.CreateWorkflowConfigRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[WorkflowConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataform/latest/com.google.cloud.dataform.v1.WorkflowConfig)>`  
  
  
### createWorkflowInvocation(CreateWorkflowInvocationRequest request, StreamObserver<WorkflowInvocation> responseObserver)
    
    
    public default void createWorkflowInvocation(CreateWorkflowInvocationRequest request, StreamObserver<WorkflowInvocation> responseObserver)

Creates a new WorkflowInvocation in a given Repository.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[CreateWorkflowInvocationRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataform/latest/com.google.cloud.dataform.v1.CreateWorkflowInvocationRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[WorkflowInvocation](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataform/latest/com.google.cloud.dataform.v1.WorkflowInvocation)>`  
  
  
### createWorkspace(CreateWorkspaceRequest request, StreamObserver<Workspace> responseObserver)
    
    
    public default void createWorkspace(CreateWorkspaceRequest request, StreamObserver<Workspace> responseObserver)

Creates a new Workspace in a given Repository.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[CreateWorkspaceRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataform/latest/com.google.cloud.dataform.v1.CreateWorkspaceRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[Workspace](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataform/latest/com.google.cloud.dataform.v1.Workspace)>`  
  
  
### deleteFolder(DeleteFolderRequest request, StreamObserver<Empty> responseObserver)
    
    
    public default void deleteFolder(DeleteFolderRequest request, StreamObserver<Empty> responseObserver)

Deletes a single Folder.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[DeleteFolderRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataform/latest/com.google.cloud.dataform.v1.DeleteFolderRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html)>`  
  
  
### deleteFolderTree(DeleteFolderTreeRequest request, StreamObserver<Operation> responseObserver)
    
    
    public default void deleteFolderTree(DeleteFolderTreeRequest request, StreamObserver<Operation> responseObserver)

Deletes a Folder with its contents (Folders, Repositories, Workspaces, ReleaseConfigs, and WorkflowConfigs).

**Parameters**  
---  
**Name** | **Description**  
`request` | `[DeleteFolderTreeRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataform/latest/com.google.cloud.dataform.v1.DeleteFolderTreeRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>`  
  
  
### deleteReleaseConfig(DeleteReleaseConfigRequest request, StreamObserver<Empty> responseObserver)
    
    
    public default void deleteReleaseConfig(DeleteReleaseConfigRequest request, StreamObserver<Empty> responseObserver)

Deletes a single ReleaseConfig.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[DeleteReleaseConfigRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataform/latest/com.google.cloud.dataform.v1.DeleteReleaseConfigRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html)>`  
  
  
### deleteRepository(DeleteRepositoryRequest request, StreamObserver<Empty> responseObserver)
    
    
    public default void deleteRepository(DeleteRepositoryRequest request, StreamObserver<Empty> responseObserver)

Deletes a single Repository.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[DeleteRepositoryRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataform/latest/com.google.cloud.dataform.v1.DeleteRepositoryRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html)>`  
  
  
### deleteTeamFolder(DeleteTeamFolderRequest request, StreamObserver<Empty> responseObserver)
    
    
    public default void deleteTeamFolder(DeleteTeamFolderRequest request, StreamObserver<Empty> responseObserver)

Deletes a single TeamFolder.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[DeleteTeamFolderRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataform/latest/com.google.cloud.dataform.v1.DeleteTeamFolderRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html)>`  
  
  
### deleteTeamFolderTree(DeleteTeamFolderTreeRequest request, StreamObserver<Operation> responseObserver)
    
    
    public default void deleteTeamFolderTree(DeleteTeamFolderTreeRequest request, StreamObserver<Operation> responseObserver)

Deletes a TeamFolder with its contents (Folders, Repositories, Workspaces, ReleaseConfigs, and WorkflowConfigs).

**Parameters**  
---  
**Name** | **Description**  
`request` | `[DeleteTeamFolderTreeRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataform/latest/com.google.cloud.dataform.v1.DeleteTeamFolderTreeRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>`  
  
  
### deleteWorkflowConfig(DeleteWorkflowConfigRequest request, StreamObserver<Empty> responseObserver)
    
    
    public default void deleteWorkflowConfig(DeleteWorkflowConfigRequest request, StreamObserver<Empty> responseObserver)

Deletes a single WorkflowConfig.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[DeleteWorkflowConfigRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataform/latest/com.google.cloud.dataform.v1.DeleteWorkflowConfigRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html)>`  
  
  
### deleteWorkflowInvocation(DeleteWorkflowInvocationRequest request, StreamObserver<Empty> responseObserver)
    
    
    public default void deleteWorkflowInvocation(DeleteWorkflowInvocationRequest request, StreamObserver<Empty> responseObserver)

Deletes a single WorkflowInvocation.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[DeleteWorkflowInvocationRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataform/latest/com.google.cloud.dataform.v1.DeleteWorkflowInvocationRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html)>`  
  
  
### deleteWorkspace(DeleteWorkspaceRequest request, StreamObserver<Empty> responseObserver)
    
    
    public default void deleteWorkspace(DeleteWorkspaceRequest request, StreamObserver<Empty> responseObserver)

Deletes a single Workspace.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[DeleteWorkspaceRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataform/latest/com.google.cloud.dataform.v1.DeleteWorkspaceRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html)>`  
  
  
### fetchFileDiff(FetchFileDiffRequest request, StreamObserver<FetchFileDiffResponse> responseObserver)
    
    
    public default void fetchFileDiff(FetchFileDiffRequest request, StreamObserver<FetchFileDiffResponse> responseObserver)

Fetches Git diff for an uncommitted file in a Workspace.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[FetchFileDiffRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataform/latest/com.google.cloud.dataform.v1.FetchFileDiffRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[FetchFileDiffResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataform/latest/com.google.cloud.dataform.v1.FetchFileDiffResponse)>`  
  
  
### fetchFileGitStatuses(FetchFileGitStatusesRequest request, StreamObserver<FetchFileGitStatusesResponse> responseObserver)
    
    
    public default void fetchFileGitStatuses(FetchFileGitStatusesRequest request, StreamObserver<FetchFileGitStatusesResponse> responseObserver)

Fetches Git statuses for the files in a Workspace.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[FetchFileGitStatusesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataform/latest/com.google.cloud.dataform.v1.FetchFileGitStatusesRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[FetchFileGitStatusesResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataform/latest/com.google.cloud.dataform.v1.FetchFileGitStatusesResponse)>`  
  
  
### fetchGitAheadBehind(FetchGitAheadBehindRequest request, StreamObserver<FetchGitAheadBehindResponse> responseObserver)
    
    
    public default void fetchGitAheadBehind(FetchGitAheadBehindRequest request, StreamObserver<FetchGitAheadBehindResponse> responseObserver)

Fetches Git ahead/behind against a remote branch.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[FetchGitAheadBehindRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataform/latest/com.google.cloud.dataform.v1.FetchGitAheadBehindRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[FetchGitAheadBehindResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataform/latest/com.google.cloud.dataform.v1.FetchGitAheadBehindResponse)>`  
  
  
### fetchRemoteBranches(FetchRemoteBranchesRequest request, StreamObserver<FetchRemoteBranchesResponse> responseObserver)
    
    
    public default void fetchRemoteBranches(FetchRemoteBranchesRequest request, StreamObserver<FetchRemoteBranchesResponse> responseObserver)

Fetches a Repository's remote branches.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[FetchRemoteBranchesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataform/latest/com.google.cloud.dataform.v1.FetchRemoteBranchesRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[FetchRemoteBranchesResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataform/latest/com.google.cloud.dataform.v1.FetchRemoteBranchesResponse)>`  
  
  
### fetchRepositoryHistory(FetchRepositoryHistoryRequest request, StreamObserver<FetchRepositoryHistoryResponse> responseObserver)
    
    
    public default void fetchRepositoryHistory(FetchRepositoryHistoryRequest request, StreamObserver<FetchRepositoryHistoryResponse> responseObserver)

Fetches a Repository's history of commits. The Repository must not have a value for `git_remote_settings.url`.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[FetchRepositoryHistoryRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataform/latest/com.google.cloud.dataform.v1.FetchRepositoryHistoryRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[FetchRepositoryHistoryResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataform/latest/com.google.cloud.dataform.v1.FetchRepositoryHistoryResponse)>`  
  
  
### getCompilationResult(GetCompilationResultRequest request, StreamObserver<CompilationResult> responseObserver)
    
    
    public default void getCompilationResult(GetCompilationResultRequest request, StreamObserver<CompilationResult> responseObserver)

Fetches a single CompilationResult.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetCompilationResultRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataform/latest/com.google.cloud.dataform.v1.GetCompilationResultRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[CompilationResult](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataform/latest/com.google.cloud.dataform.v1.CompilationResult)>`  
  
  
### getConfig(GetConfigRequest request, StreamObserver<Config> responseObserver)
    
    
    public default void getConfig(GetConfigRequest request, StreamObserver<Config> responseObserver)

Get default config for a given project and location.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetConfigRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataform/latest/com.google.cloud.dataform.v1.GetConfigRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[Config](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataform/latest/com.google.cloud.dataform.v1.Config)>`  
  
  
### getFolder(GetFolderRequest request, StreamObserver<Folder> responseObserver)
    
    
    public default void getFolder(GetFolderRequest request, StreamObserver<Folder> responseObserver)

Fetches a single Folder.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetFolderRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataform/latest/com.google.cloud.dataform.v1.GetFolderRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[Folder](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataform/latest/com.google.cloud.dataform.v1.Folder)>`  
  
  
### getIamPolicy(GetIamPolicyRequest request, StreamObserver<Policy> responseObserver)
    
    
    public default void getIamPolicy(GetIamPolicyRequest request, StreamObserver<Policy> responseObserver)

Gets the access control policy for a resource. Returns an empty policy if the resource exists and does not have a policy set.

**Parameters**  
---  
**Name** | **Description**  
`request` | `com.google.iam.v1.GetIamPolicyRequest`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<com.google.iam.v1.Policy>`  
  
  
### getReleaseConfig(GetReleaseConfigRequest request, StreamObserver<ReleaseConfig> responseObserver)
    
    
    public default void getReleaseConfig(GetReleaseConfigRequest request, StreamObserver<ReleaseConfig> responseObserver)

Fetches a single ReleaseConfig.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetReleaseConfigRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataform/latest/com.google.cloud.dataform.v1.GetReleaseConfigRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[ReleaseConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataform/latest/com.google.cloud.dataform.v1.ReleaseConfig)>`  
  
  
### getRepository(GetRepositoryRequest request, StreamObserver<Repository> responseObserver)
    
    
    public default void getRepository(GetRepositoryRequest request, StreamObserver<Repository> responseObserver)

Fetches a single Repository.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetRepositoryRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataform/latest/com.google.cloud.dataform.v1.GetRepositoryRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[Repository](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataform/latest/com.google.cloud.dataform.v1.Repository)>`  
  
  
### getTeamFolder(GetTeamFolderRequest request, StreamObserver<TeamFolder> responseObserver)
    
    
    public default void getTeamFolder(GetTeamFolderRequest request, StreamObserver<TeamFolder> responseObserver)

Fetches a single TeamFolder.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetTeamFolderRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataform/latest/com.google.cloud.dataform.v1.GetTeamFolderRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[TeamFolder](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataform/latest/com.google.cloud.dataform.v1.TeamFolder)>`  
  
  
### getWorkflowConfig(GetWorkflowConfigRequest request, StreamObserver<WorkflowConfig> responseObserver)
    
    
    public default void getWorkflowConfig(GetWorkflowConfigRequest request, StreamObserver<WorkflowConfig> responseObserver)

Fetches a single WorkflowConfig.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetWorkflowConfigRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataform/latest/com.google.cloud.dataform.v1.GetWorkflowConfigRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[WorkflowConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataform/latest/com.google.cloud.dataform.v1.WorkflowConfig)>`  
  
  
### getWorkflowInvocation(GetWorkflowInvocationRequest request, StreamObserver<WorkflowInvocation> responseObserver)
    
    
    public default void getWorkflowInvocation(GetWorkflowInvocationRequest request, StreamObserver<WorkflowInvocation> responseObserver)

Fetches a single WorkflowInvocation.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetWorkflowInvocationRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataform/latest/com.google.cloud.dataform.v1.GetWorkflowInvocationRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[WorkflowInvocation](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataform/latest/com.google.cloud.dataform.v1.WorkflowInvocation)>`  
  
  
### getWorkspace(GetWorkspaceRequest request, StreamObserver<Workspace> responseObserver)
    
    
    public default void getWorkspace(GetWorkspaceRequest request, StreamObserver<Workspace> responseObserver)

Fetches a single Workspace.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetWorkspaceRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataform/latest/com.google.cloud.dataform.v1.GetWorkspaceRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[Workspace](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataform/latest/com.google.cloud.dataform.v1.Workspace)>`  
  
  
### installNpmPackages(InstallNpmPackagesRequest request, StreamObserver<InstallNpmPackagesResponse> responseObserver)
    
    
    public default void installNpmPackages(InstallNpmPackagesRequest request, StreamObserver<InstallNpmPackagesResponse> responseObserver)

Installs dependency NPM packages (inside a Workspace).

**Parameters**  
---  
**Name** | **Description**  
`request` | `[InstallNpmPackagesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataform/latest/com.google.cloud.dataform.v1.InstallNpmPackagesRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[InstallNpmPackagesResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataform/latest/com.google.cloud.dataform.v1.InstallNpmPackagesResponse)>`  
  
  
### listCompilationResults(ListCompilationResultsRequest request, StreamObserver<ListCompilationResultsResponse> responseObserver)
    
    
    public default void listCompilationResults(ListCompilationResultsRequest request, StreamObserver<ListCompilationResultsResponse> responseObserver)

Lists CompilationResults in a given Repository.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ListCompilationResultsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataform/latest/com.google.cloud.dataform.v1.ListCompilationResultsRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[ListCompilationResultsResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataform/latest/com.google.cloud.dataform.v1.ListCompilationResultsResponse)>`  
  
  
### listReleaseConfigs(ListReleaseConfigsRequest request, StreamObserver<ListReleaseConfigsResponse> responseObserver)
    
    
    public default void listReleaseConfigs(ListReleaseConfigsRequest request, StreamObserver<ListReleaseConfigsResponse> responseObserver)

Lists ReleaseConfigs in a given Repository.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ListReleaseConfigsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataform/latest/com.google.cloud.dataform.v1.ListReleaseConfigsRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[ListReleaseConfigsResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataform/latest/com.google.cloud.dataform.v1.ListReleaseConfigsResponse)>`  
  
  
### listRepositories(ListRepositoriesRequest request, StreamObserver<ListRepositoriesResponse> responseObserver)
    
    
    public default void listRepositories(ListRepositoriesRequest request, StreamObserver<ListRepositoriesResponse> responseObserver)

Lists Repositories in a given project and location. **Note:** _This method can return repositories not shown in the[Dataform UI](https://console.cloud.google.com/bigquery/dataform)_.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ListRepositoriesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataform/latest/com.google.cloud.dataform.v1.ListRepositoriesRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[ListRepositoriesResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataform/latest/com.google.cloud.dataform.v1.ListRepositoriesResponse)>`  
  
  
### listWorkflowConfigs(ListWorkflowConfigsRequest request, StreamObserver<ListWorkflowConfigsResponse> responseObserver)
    
    
    public default void listWorkflowConfigs(ListWorkflowConfigsRequest request, StreamObserver<ListWorkflowConfigsResponse> responseObserver)

Lists WorkflowConfigs in a given Repository.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ListWorkflowConfigsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataform/latest/com.google.cloud.dataform.v1.ListWorkflowConfigsRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[ListWorkflowConfigsResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataform/latest/com.google.cloud.dataform.v1.ListWorkflowConfigsResponse)>`  
  
  
### listWorkflowInvocations(ListWorkflowInvocationsRequest request, StreamObserver<ListWorkflowInvocationsResponse> responseObserver)
    
    
    public default void listWorkflowInvocations(ListWorkflowInvocationsRequest request, StreamObserver<ListWorkflowInvocationsResponse> responseObserver)

Lists WorkflowInvocations in a given Repository.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ListWorkflowInvocationsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataform/latest/com.google.cloud.dataform.v1.ListWorkflowInvocationsRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[ListWorkflowInvocationsResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataform/latest/com.google.cloud.dataform.v1.ListWorkflowInvocationsResponse)>`  
  
  
### listWorkspaces(ListWorkspacesRequest request, StreamObserver<ListWorkspacesResponse> responseObserver)
    
    
    public default void listWorkspaces(ListWorkspacesRequest request, StreamObserver<ListWorkspacesResponse> responseObserver)

Lists Workspaces in a given Repository.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ListWorkspacesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataform/latest/com.google.cloud.dataform.v1.ListWorkspacesRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[ListWorkspacesResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataform/latest/com.google.cloud.dataform.v1.ListWorkspacesResponse)>`  
  
  
### makeDirectory(MakeDirectoryRequest request, StreamObserver<MakeDirectoryResponse> responseObserver)
    
    
    public default void makeDirectory(MakeDirectoryRequest request, StreamObserver<MakeDirectoryResponse> responseObserver)

Creates a directory inside a Workspace.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[MakeDirectoryRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataform/latest/com.google.cloud.dataform.v1.MakeDirectoryRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[MakeDirectoryResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataform/latest/com.google.cloud.dataform.v1.MakeDirectoryResponse)>`  
  
  
### moveDirectory(MoveDirectoryRequest request, StreamObserver<MoveDirectoryResponse> responseObserver)
    
    
    public default void moveDirectory(MoveDirectoryRequest request, StreamObserver<MoveDirectoryResponse> responseObserver)

Moves a directory (inside a Workspace), and all of its contents, to a new location.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[MoveDirectoryRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataform/latest/com.google.cloud.dataform.v1.MoveDirectoryRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[MoveDirectoryResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataform/latest/com.google.cloud.dataform.v1.MoveDirectoryResponse)>`  
  
  
### moveFile(MoveFileRequest request, StreamObserver<MoveFileResponse> responseObserver)
    
    
    public default void moveFile(MoveFileRequest request, StreamObserver<MoveFileResponse> responseObserver)

Moves a file (inside a Workspace) to a new location.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[MoveFileRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataform/latest/com.google.cloud.dataform.v1.MoveFileRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[MoveFileResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataform/latest/com.google.cloud.dataform.v1.MoveFileResponse)>`  
  
  
### moveFolder(MoveFolderRequest request, StreamObserver<Operation> responseObserver)
    
    
    public default void moveFolder(MoveFolderRequest request, StreamObserver<Operation> responseObserver)

Moves a Folder to a new Folder, TeamFolder, or the root location.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[MoveFolderRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataform/latest/com.google.cloud.dataform.v1.MoveFolderRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>`  
  
  
### moveRepository(MoveRepositoryRequest request, StreamObserver<Operation> responseObserver)
    
    
    public default void moveRepository(MoveRepositoryRequest request, StreamObserver<Operation> responseObserver)

Moves a Repository to a new location.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[MoveRepositoryRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataform/latest/com.google.cloud.dataform.v1.MoveRepositoryRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>`  
  
  
### pullGitCommits(PullGitCommitsRequest request, StreamObserver<PullGitCommitsResponse> responseObserver)
    
    
    public default void pullGitCommits(PullGitCommitsRequest request, StreamObserver<PullGitCommitsResponse> responseObserver)

Pulls Git commits from the Repository's remote into a Workspace.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[PullGitCommitsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataform/latest/com.google.cloud.dataform.v1.PullGitCommitsRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[PullGitCommitsResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataform/latest/com.google.cloud.dataform.v1.PullGitCommitsResponse)>`  
  
  
### pushGitCommits(PushGitCommitsRequest request, StreamObserver<PushGitCommitsResponse> responseObserver)
    
    
    public default void pushGitCommits(PushGitCommitsRequest request, StreamObserver<PushGitCommitsResponse> responseObserver)

Pushes Git commits from a Workspace to the Repository's remote.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[PushGitCommitsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataform/latest/com.google.cloud.dataform.v1.PushGitCommitsRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[PushGitCommitsResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataform/latest/com.google.cloud.dataform.v1.PushGitCommitsResponse)>`  
  
  
### queryCompilationResultActions(QueryCompilationResultActionsRequest request, StreamObserver<QueryCompilationResultActionsResponse> responseObserver)
    
    
    public default void queryCompilationResultActions(QueryCompilationResultActionsRequest request, StreamObserver<QueryCompilationResultActionsResponse> responseObserver)

Returns CompilationResultActions in a given CompilationResult.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[QueryCompilationResultActionsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataform/latest/com.google.cloud.dataform.v1.QueryCompilationResultActionsRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[QueryCompilationResultActionsResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataform/latest/com.google.cloud.dataform.v1.QueryCompilationResultActionsResponse)>`  
  
  
### queryDirectoryContents(QueryDirectoryContentsRequest request, StreamObserver<QueryDirectoryContentsResponse> responseObserver)
    
    
    public default void queryDirectoryContents(QueryDirectoryContentsRequest request, StreamObserver<QueryDirectoryContentsResponse> responseObserver)

Returns the contents of a given Workspace directory.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[QueryDirectoryContentsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataform/latest/com.google.cloud.dataform.v1.QueryDirectoryContentsRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[QueryDirectoryContentsResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataform/latest/com.google.cloud.dataform.v1.QueryDirectoryContentsResponse)>`  
  
  
### queryFolderContents(QueryFolderContentsRequest request, StreamObserver<QueryFolderContentsResponse> responseObserver)
    
    
    public default void queryFolderContents(QueryFolderContentsRequest request, StreamObserver<QueryFolderContentsResponse> responseObserver)

Returns the contents of a given Folder.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[QueryFolderContentsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataform/latest/com.google.cloud.dataform.v1.QueryFolderContentsRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[QueryFolderContentsResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataform/latest/com.google.cloud.dataform.v1.QueryFolderContentsResponse)>`  
  
  
### queryRepositoryDirectoryContents(QueryRepositoryDirectoryContentsRequest request, StreamObserver<QueryRepositoryDirectoryContentsResponse> responseObserver)
    
    
    public default void queryRepositoryDirectoryContents(QueryRepositoryDirectoryContentsRequest request, StreamObserver<QueryRepositoryDirectoryContentsResponse> responseObserver)

Returns the contents of a given Repository directory. The Repository must not have a value for `git_remote_settings.url`.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[QueryRepositoryDirectoryContentsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataform/latest/com.google.cloud.dataform.v1.QueryRepositoryDirectoryContentsRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[QueryRepositoryDirectoryContentsResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataform/latest/com.google.cloud.dataform.v1.QueryRepositoryDirectoryContentsResponse)>`  
  
  
### queryTeamFolderContents(QueryTeamFolderContentsRequest request, StreamObserver<QueryTeamFolderContentsResponse> responseObserver)
    
    
    public default void queryTeamFolderContents(QueryTeamFolderContentsRequest request, StreamObserver<QueryTeamFolderContentsResponse> responseObserver)

Returns the contents of a given TeamFolder.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[QueryTeamFolderContentsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataform/latest/com.google.cloud.dataform.v1.QueryTeamFolderContentsRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[QueryTeamFolderContentsResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataform/latest/com.google.cloud.dataform.v1.QueryTeamFolderContentsResponse)>`  
  
  
### queryUserRootContents(QueryUserRootContentsRequest request, StreamObserver<QueryUserRootContentsResponse> responseObserver)
    
    
    public default void queryUserRootContents(QueryUserRootContentsRequest request, StreamObserver<QueryUserRootContentsResponse> responseObserver)

Returns the contents of a caller's root folder in a given location. The root folder contains all resources that are created by the user and not contained in any other folder.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[QueryUserRootContentsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataform/latest/com.google.cloud.dataform.v1.QueryUserRootContentsRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[QueryUserRootContentsResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataform/latest/com.google.cloud.dataform.v1.QueryUserRootContentsResponse)>`  
  
  
### queryWorkflowInvocationActions(QueryWorkflowInvocationActionsRequest request, StreamObserver<QueryWorkflowInvocationActionsResponse> responseObserver)
    
    
    public default void queryWorkflowInvocationActions(QueryWorkflowInvocationActionsRequest request, StreamObserver<QueryWorkflowInvocationActionsResponse> responseObserver)

Returns WorkflowInvocationActions in a given WorkflowInvocation.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[QueryWorkflowInvocationActionsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataform/latest/com.google.cloud.dataform.v1.QueryWorkflowInvocationActionsRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[QueryWorkflowInvocationActionsResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataform/latest/com.google.cloud.dataform.v1.QueryWorkflowInvocationActionsResponse)>`  
  
  
### readFile(ReadFileRequest request, StreamObserver<ReadFileResponse> responseObserver)
    
    
    public default void readFile(ReadFileRequest request, StreamObserver<ReadFileResponse> responseObserver)

Returns the contents of a file (inside a Workspace).

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ReadFileRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataform/latest/com.google.cloud.dataform.v1.ReadFileRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[ReadFileResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataform/latest/com.google.cloud.dataform.v1.ReadFileResponse)>`  
  
  
### readRepositoryFile(ReadRepositoryFileRequest request, StreamObserver<ReadRepositoryFileResponse> responseObserver)
    
    
    public default void readRepositoryFile(ReadRepositoryFileRequest request, StreamObserver<ReadRepositoryFileResponse> responseObserver)

Returns the contents of a file (inside a Repository). The Repository must not have a value for `git_remote_settings.url`.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ReadRepositoryFileRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataform/latest/com.google.cloud.dataform.v1.ReadRepositoryFileRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[ReadRepositoryFileResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataform/latest/com.google.cloud.dataform.v1.ReadRepositoryFileResponse)>`  
  
  
### removeDirectory(RemoveDirectoryRequest request, StreamObserver<RemoveDirectoryResponse> responseObserver)
    
    
    public default void removeDirectory(RemoveDirectoryRequest request, StreamObserver<RemoveDirectoryResponse> responseObserver)

Deletes a directory (inside a Workspace) and all of its contents.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[RemoveDirectoryRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataform/latest/com.google.cloud.dataform.v1.RemoveDirectoryRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[RemoveDirectoryResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataform/latest/com.google.cloud.dataform.v1.RemoveDirectoryResponse)>`  
  
  
### removeFile(RemoveFileRequest request, StreamObserver<RemoveFileResponse> responseObserver)
    
    
    public default void removeFile(RemoveFileRequest request, StreamObserver<RemoveFileResponse> responseObserver)

Deletes a file (inside a Workspace).

**Parameters**  
---  
**Name** | **Description**  
`request` | `[RemoveFileRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataform/latest/com.google.cloud.dataform.v1.RemoveFileRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[RemoveFileResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataform/latest/com.google.cloud.dataform.v1.RemoveFileResponse)>`  
  
  
### resetWorkspaceChanges(ResetWorkspaceChangesRequest request, StreamObserver<ResetWorkspaceChangesResponse> responseObserver)
    
    
    public default void resetWorkspaceChanges(ResetWorkspaceChangesRequest request, StreamObserver<ResetWorkspaceChangesResponse> responseObserver)

Performs a Git reset for uncommitted files in a Workspace.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ResetWorkspaceChangesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataform/latest/com.google.cloud.dataform.v1.ResetWorkspaceChangesRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[ResetWorkspaceChangesResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataform/latest/com.google.cloud.dataform.v1.ResetWorkspaceChangesResponse)>`  
  
  
### searchFiles(SearchFilesRequest request, StreamObserver<SearchFilesResponse> responseObserver)
    
    
    public default void searchFiles(SearchFilesRequest request, StreamObserver<SearchFilesResponse> responseObserver)

Finds the contents of a given Workspace directory by filter.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[SearchFilesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataform/latest/com.google.cloud.dataform.v1.SearchFilesRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[SearchFilesResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataform/latest/com.google.cloud.dataform.v1.SearchFilesResponse)>`  
  
  
### searchTeamFolders(SearchTeamFoldersRequest request, StreamObserver<SearchTeamFoldersResponse> responseObserver)
    
    
    public default void searchTeamFolders(SearchTeamFoldersRequest request, StreamObserver<SearchTeamFoldersResponse> responseObserver)

Returns all TeamFolders in a given location that the caller has access to and match the provided filter.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[SearchTeamFoldersRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataform/latest/com.google.cloud.dataform.v1.SearchTeamFoldersRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[SearchTeamFoldersResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataform/latest/com.google.cloud.dataform.v1.SearchTeamFoldersResponse)>`  
  
  
### setIamPolicy(SetIamPolicyRequest request, StreamObserver<Policy> responseObserver)
    
    
    public default void setIamPolicy(SetIamPolicyRequest request, StreamObserver<Policy> responseObserver)

Sets the access control policy on the specified resource. Replaces any existing policy. Can return `NOT_FOUND`, `INVALID_ARGUMENT`, and `PERMISSION_DENIED` errors.

**Parameters**  
---  
**Name** | **Description**  
`request` | `com.google.iam.v1.SetIamPolicyRequest`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<com.google.iam.v1.Policy>`  
  
  
### testIamPermissions(TestIamPermissionsRequest request, StreamObserver<TestIamPermissionsResponse> responseObserver)
    
    
    public default void testIamPermissions(TestIamPermissionsRequest request, StreamObserver<TestIamPermissionsResponse> responseObserver)

Returns permissions that a caller has on the specified resource. If the resource does not exist, this will return an empty set of permissions, not a `NOT_FOUND` error. Note: This operation is designed to be used for building permission-aware UIs and command-line tools, not for authorization checking. This operation may "fail open" without warning.

**Parameters**  
---  
**Name** | **Description**  
`request` | `com.google.iam.v1.TestIamPermissionsRequest`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<com.google.iam.v1.TestIamPermissionsResponse>`  
  
  
### updateConfig(UpdateConfigRequest request, StreamObserver<Config> responseObserver)
    
    
    public default void updateConfig(UpdateConfigRequest request, StreamObserver<Config> responseObserver)

Update default config for a given project and location. **Note:** _This method does not fully implement[AIP/134](https://google.aip.dev/134). The wildcard entry (\_) is treated as a bad request, and when the `field_mask` is omitted, the request is treated as a full update on all modifiable fields.*

**Parameters**  
---  
**Name** | **Description**  
`request` | `[UpdateConfigRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataform/latest/com.google.cloud.dataform.v1.UpdateConfigRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[Config](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataform/latest/com.google.cloud.dataform.v1.Config)>`  
  
  
### updateFolder(UpdateFolderRequest request, StreamObserver<Folder> responseObserver)
    
    
    public default void updateFolder(UpdateFolderRequest request, StreamObserver<Folder> responseObserver)

Updates a single Folder.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[UpdateFolderRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataform/latest/com.google.cloud.dataform.v1.UpdateFolderRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[Folder](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataform/latest/com.google.cloud.dataform.v1.Folder)>`  
  
  
### updateReleaseConfig(UpdateReleaseConfigRequest request, StreamObserver<ReleaseConfig> responseObserver)
    
    
    public default void updateReleaseConfig(UpdateReleaseConfigRequest request, StreamObserver<ReleaseConfig> responseObserver)

Updates a single ReleaseConfig. **Note:** _This method does not fully implement[AIP/134](https://google.aip.dev/134). The wildcard entry (\_) is treated as a bad request, and when the `field_mask` is omitted, the request is treated as a full update on all modifiable fields.*

**Parameters**  
---  
**Name** | **Description**  
`request` | `[UpdateReleaseConfigRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataform/latest/com.google.cloud.dataform.v1.UpdateReleaseConfigRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[ReleaseConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataform/latest/com.google.cloud.dataform.v1.ReleaseConfig)>`  
  
  
### updateRepository(UpdateRepositoryRequest request, StreamObserver<Repository> responseObserver)
    
    
    public default void updateRepository(UpdateRepositoryRequest request, StreamObserver<Repository> responseObserver)

Updates a single Repository. **Note:** _This method does not fully implement[AIP/134](https://google.aip.dev/134). The wildcard entry (\_) is treated as a bad request, and when the `field_mask` is omitted, the request is treated as a full update on all modifiable fields.*

**Parameters**  
---  
**Name** | **Description**  
`request` | `[UpdateRepositoryRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataform/latest/com.google.cloud.dataform.v1.UpdateRepositoryRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[Repository](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataform/latest/com.google.cloud.dataform.v1.Repository)>`  
  
  
### updateTeamFolder(UpdateTeamFolderRequest request, StreamObserver<TeamFolder> responseObserver)
    
    
    public default void updateTeamFolder(UpdateTeamFolderRequest request, StreamObserver<TeamFolder> responseObserver)

Updates a single TeamFolder.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[UpdateTeamFolderRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataform/latest/com.google.cloud.dataform.v1.UpdateTeamFolderRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[TeamFolder](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataform/latest/com.google.cloud.dataform.v1.TeamFolder)>`  
  
  
### updateWorkflowConfig(UpdateWorkflowConfigRequest request, StreamObserver<WorkflowConfig> responseObserver)
    
    
    public default void updateWorkflowConfig(UpdateWorkflowConfigRequest request, StreamObserver<WorkflowConfig> responseObserver)

Updates a single WorkflowConfig. **Note:** _This method does not fully implement[AIP/134](https://google.aip.dev/134). The wildcard entry (\_) is treated as a bad request, and when the `field_mask` is omitted, the request is treated as a full update on all modifiable fields.*

**Parameters**  
---  
**Name** | **Description**  
`request` | `[UpdateWorkflowConfigRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataform/latest/com.google.cloud.dataform.v1.UpdateWorkflowConfigRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[WorkflowConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataform/latest/com.google.cloud.dataform.v1.WorkflowConfig)>`  
  
  
### writeFile(WriteFileRequest request, StreamObserver<WriteFileResponse> responseObserver)
    
    
    public default void writeFile(WriteFileRequest request, StreamObserver<WriteFileResponse> responseObserver)

Writes to a file (inside a Workspace).

**Parameters**  
---  
**Name** | **Description**  
`request` | `[WriteFileRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataform/latest/com.google.cloud.dataform.v1.WriteFileRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[WriteFileResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataform/latest/com.google.cloud.dataform.v1.WriteFileResponse)>`  
  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-06 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-06 UTC."],[],[]] 
