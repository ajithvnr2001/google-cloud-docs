---
url: https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/dataform/protos.google.cloud.dataform.v1.dataform-class
title: Class protos.google.cloud.dataform.v1.Dataform (3.4.0) \u00a0|\u00a0 Node.js client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:43:40.425481+00:00
---

# Class protos.google.cloud.dataform.v1.Dataform (3.4.0)  |  Node.js client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/dataform/protos.google.cloud.dataform.v1.dataform-class

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Node.js ](https://docs.cloud.google.com/nodejs/docs)
  * [ Client libraries ](https://docs.cloud.google.com/nodejs/docs/reference)



Send feedback 

#  Class protos.google.cloud.dataform.v1.Dataform (3.4.0) Stay organized with collections  Save and categorize content based on your preferences. 

3.4.0 (latest)  3.3.1  2.5.0  2.4.0  2.1.0  1.4.0  1.0.2  0.4.2  0.2.0  0.1.0 

Represents a Dataform

## Inheritance

$protobuf.rpc.Service > protos.google.cloud.dataform.v1.Dataform

## Package

[@google-cloud/dataform](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/overview.html)

## Constructors 

### (constructor)(rpcImpl, requestDelimited, responseDelimited)
    
    
    constructor(rpcImpl: $protobuf.RPCImpl, requestDelimited?: boolean, responseDelimited?: boolean);

Constructs a new Dataform service.

**Parameters**  
---  
**Name** | **Description**  
`rpcImpl` |  `$protobuf.RPCImpl`   
RPC implementation  
`requestDelimited` |  `boolean`   
Whether requests are length-delimited  
`responseDelimited` |  `boolean`   
Whether responses are length-delimited  
  
## Methods 

### cancelWorkflowInvocation(request, callback)
    
    
    public cancelWorkflowInvocation(request: google.cloud.dataform.v1.ICancelWorkflowInvocationRequest, callback: google.cloud.dataform.v1.Dataform.CancelWorkflowInvocationCallback): void;

Calls CancelWorkflowInvocation.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[ICancelWorkflowInvocationRequest](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/dataform/protos.google.cloud.dataform.v1.icancelworkflowinvocationrequest)`   
CancelWorkflowInvocationRequest message or plain object  
`callback` |  `[CancelWorkflowInvocationCallback](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/overview.html)`   
Node-style callback called with the error, if any, and CancelWorkflowInvocationResponse  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### cancelWorkflowInvocation(request)
    
    
    public cancelWorkflowInvocation(request: google.cloud.dataform.v1.ICancelWorkflowInvocationRequest): Promise<google.cloud.dataform.v1.CancelWorkflowInvocationResponse>;

Calls CancelWorkflowInvocation.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[ICancelWorkflowInvocationRequest](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/dataform/protos.google.cloud.dataform.v1.icancelworkflowinvocationrequest)`   
CancelWorkflowInvocationRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.dataform.v1.CancelWorkflowInvocationResponse](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/dataform/protos.google.cloud.dataform.v1.cancelworkflowinvocationresponse)>` | Promise  
  
### commitRepositoryChanges(request, callback)
    
    
    public commitRepositoryChanges(request: google.cloud.dataform.v1.ICommitRepositoryChangesRequest, callback: google.cloud.dataform.v1.Dataform.CommitRepositoryChangesCallback): void;

Calls CommitRepositoryChanges.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[ICommitRepositoryChangesRequest](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/dataform/protos.google.cloud.dataform.v1.icommitrepositorychangesrequest)`   
CommitRepositoryChangesRequest message or plain object  
`callback` |  `[CommitRepositoryChangesCallback](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/overview.html)`   
Node-style callback called with the error, if any, and CommitRepositoryChangesResponse  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### commitRepositoryChanges(request)
    
    
    public commitRepositoryChanges(request: google.cloud.dataform.v1.ICommitRepositoryChangesRequest): Promise<google.cloud.dataform.v1.CommitRepositoryChangesResponse>;

Calls CommitRepositoryChanges.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[ICommitRepositoryChangesRequest](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/dataform/protos.google.cloud.dataform.v1.icommitrepositorychangesrequest)`   
CommitRepositoryChangesRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.dataform.v1.CommitRepositoryChangesResponse](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/dataform/protos.google.cloud.dataform.v1.commitrepositorychangesresponse)>` | Promise  
  
### commitWorkspaceChanges(request, callback)
    
    
    public commitWorkspaceChanges(request: google.cloud.dataform.v1.ICommitWorkspaceChangesRequest, callback: google.cloud.dataform.v1.Dataform.CommitWorkspaceChangesCallback): void;

Calls CommitWorkspaceChanges.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[ICommitWorkspaceChangesRequest](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/dataform/protos.google.cloud.dataform.v1.icommitworkspacechangesrequest)`   
CommitWorkspaceChangesRequest message or plain object  
`callback` |  `[CommitWorkspaceChangesCallback](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/overview.html)`   
Node-style callback called with the error, if any, and CommitWorkspaceChangesResponse  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### commitWorkspaceChanges(request)
    
    
    public commitWorkspaceChanges(request: google.cloud.dataform.v1.ICommitWorkspaceChangesRequest): Promise<google.cloud.dataform.v1.CommitWorkspaceChangesResponse>;

Calls CommitWorkspaceChanges.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[ICommitWorkspaceChangesRequest](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/dataform/protos.google.cloud.dataform.v1.icommitworkspacechangesrequest)`   
CommitWorkspaceChangesRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.dataform.v1.CommitWorkspaceChangesResponse](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/dataform/protos.google.cloud.dataform.v1.commitworkspacechangesresponse)>` | Promise  
  
### computeRepositoryAccessTokenStatus(request, callback)
    
    
    public computeRepositoryAccessTokenStatus(request: google.cloud.dataform.v1.IComputeRepositoryAccessTokenStatusRequest, callback: google.cloud.dataform.v1.Dataform.ComputeRepositoryAccessTokenStatusCallback): void;

Calls ComputeRepositoryAccessTokenStatus.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IComputeRepositoryAccessTokenStatusRequest](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/dataform/protos.google.cloud.dataform.v1.icomputerepositoryaccesstokenstatusrequest)`   
ComputeRepositoryAccessTokenStatusRequest message or plain object  
`callback` |  `[ComputeRepositoryAccessTokenStatusCallback](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/overview.html)`   
Node-style callback called with the error, if any, and ComputeRepositoryAccessTokenStatusResponse  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### computeRepositoryAccessTokenStatus(request)
    
    
    public computeRepositoryAccessTokenStatus(request: google.cloud.dataform.v1.IComputeRepositoryAccessTokenStatusRequest): Promise<google.cloud.dataform.v1.ComputeRepositoryAccessTokenStatusResponse>;

Calls ComputeRepositoryAccessTokenStatus.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IComputeRepositoryAccessTokenStatusRequest](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/dataform/protos.google.cloud.dataform.v1.icomputerepositoryaccesstokenstatusrequest)`   
ComputeRepositoryAccessTokenStatusRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.dataform.v1.ComputeRepositoryAccessTokenStatusResponse](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/dataform/protos.google.cloud.dataform.v1.computerepositoryaccesstokenstatusresponse-class)>` | Promise  
  
### create(rpcImpl, requestDelimited, responseDelimited)
    
    
    public static create(rpcImpl: $protobuf.RPCImpl, requestDelimited?: boolean, responseDelimited?: boolean): Dataform;

Creates new Dataform service using the specified rpc implementation.

**Parameters**  
---  
**Name** | **Description**  
`rpcImpl` |  `$protobuf.RPCImpl`   
RPC implementation  
`requestDelimited` |  `boolean`   
Whether requests are length-delimited  
`responseDelimited` |  `boolean`   
Whether responses are length-delimited  
**Returns**  
---  
**Type** | **Description**  
`[Dataform](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/dataform/protos.google.cloud.dataform.v1.dataform-class)` | RPC service. Useful where requests and/or responses are streamed.  
  
### createCompilationResult(request, callback)
    
    
    public createCompilationResult(request: google.cloud.dataform.v1.ICreateCompilationResultRequest, callback: google.cloud.dataform.v1.Dataform.CreateCompilationResultCallback): void;

Calls CreateCompilationResult.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[ICreateCompilationResultRequest](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/dataform/protos.google.cloud.dataform.v1.icreatecompilationresultrequest)`   
CreateCompilationResultRequest message or plain object  
`callback` |  `[CreateCompilationResultCallback](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/overview.html)`   
Node-style callback called with the error, if any, and CompilationResult  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### createCompilationResult(request)
    
    
    public createCompilationResult(request: google.cloud.dataform.v1.ICreateCompilationResultRequest): Promise<google.cloud.dataform.v1.CompilationResult>;

Calls CreateCompilationResult.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[ICreateCompilationResultRequest](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/dataform/protos.google.cloud.dataform.v1.icreatecompilationresultrequest)`   
CreateCompilationResultRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.dataform.v1.CompilationResult](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/dataform/protos.google.cloud.dataform.v1.compilationresult-class)>` | Promise  
  
### createFolder(request, callback)
    
    
    public createFolder(request: google.cloud.dataform.v1.ICreateFolderRequest, callback: google.cloud.dataform.v1.Dataform.CreateFolderCallback): void;

Calls CreateFolder.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[ICreateFolderRequest](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/dataform/protos.google.cloud.dataform.v1.icreatefolderrequest)`   
CreateFolderRequest message or plain object  
`callback` |  `[CreateFolderCallback](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/overview.html)`   
Node-style callback called with the error, if any, and Folder  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### createFolder(request)
    
    
    public createFolder(request: google.cloud.dataform.v1.ICreateFolderRequest): Promise<google.cloud.dataform.v1.Folder>;

Calls CreateFolder.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[ICreateFolderRequest](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/dataform/protos.google.cloud.dataform.v1.icreatefolderrequest)`   
CreateFolderRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.dataform.v1.Folder](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/dataform/protos.google.cloud.dataform.v1.folder)>` | Promise  
  
### createReleaseConfig(request, callback)
    
    
    public createReleaseConfig(request: google.cloud.dataform.v1.ICreateReleaseConfigRequest, callback: google.cloud.dataform.v1.Dataform.CreateReleaseConfigCallback): void;

Calls CreateReleaseConfig.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[ICreateReleaseConfigRequest](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/dataform/protos.google.cloud.dataform.v1.icreatereleaseconfigrequest)`   
CreateReleaseConfigRequest message or plain object  
`callback` |  `[CreateReleaseConfigCallback](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/overview.html)`   
Node-style callback called with the error, if any, and ReleaseConfig  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### createReleaseConfig(request)
    
    
    public createReleaseConfig(request: google.cloud.dataform.v1.ICreateReleaseConfigRequest): Promise<google.cloud.dataform.v1.ReleaseConfig>;

Calls CreateReleaseConfig.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[ICreateReleaseConfigRequest](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/dataform/protos.google.cloud.dataform.v1.icreatereleaseconfigrequest)`   
CreateReleaseConfigRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.dataform.v1.ReleaseConfig](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/dataform/protos.google.cloud.dataform.v1.releaseconfig-class)>` | Promise  
  
### createRepository(request, callback)
    
    
    public createRepository(request: google.cloud.dataform.v1.ICreateRepositoryRequest, callback: google.cloud.dataform.v1.Dataform.CreateRepositoryCallback): void;

Calls CreateRepository.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[ICreateRepositoryRequest](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/dataform/protos.google.cloud.dataform.v1.icreaterepositoryrequest)`   
CreateRepositoryRequest message or plain object  
`callback` |  `[CreateRepositoryCallback](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/overview.html)`   
Node-style callback called with the error, if any, and Repository  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### createRepository(request)
    
    
    public createRepository(request: google.cloud.dataform.v1.ICreateRepositoryRequest): Promise<google.cloud.dataform.v1.Repository>;

Calls CreateRepository.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[ICreateRepositoryRequest](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/dataform/protos.google.cloud.dataform.v1.icreaterepositoryrequest)`   
CreateRepositoryRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.dataform.v1.Repository](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/dataform/protos.google.cloud.dataform.v1.repository-class)>` | Promise  
  
### createTeamFolder(request, callback)
    
    
    public createTeamFolder(request: google.cloud.dataform.v1.ICreateTeamFolderRequest, callback: google.cloud.dataform.v1.Dataform.CreateTeamFolderCallback): void;

Calls CreateTeamFolder.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[ICreateTeamFolderRequest](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/dataform/protos.google.cloud.dataform.v1.icreateteamfolderrequest)`   
CreateTeamFolderRequest message or plain object  
`callback` |  `[CreateTeamFolderCallback](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/overview.html)`   
Node-style callback called with the error, if any, and TeamFolder  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### createTeamFolder(request)
    
    
    public createTeamFolder(request: google.cloud.dataform.v1.ICreateTeamFolderRequest): Promise<google.cloud.dataform.v1.TeamFolder>;

Calls CreateTeamFolder.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[ICreateTeamFolderRequest](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/dataform/protos.google.cloud.dataform.v1.icreateteamfolderrequest)`   
CreateTeamFolderRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.dataform.v1.TeamFolder](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/dataform/protos.google.cloud.dataform.v1.teamfolder)>` | Promise  
  
### createWorkflowConfig(request, callback)
    
    
    public createWorkflowConfig(request: google.cloud.dataform.v1.ICreateWorkflowConfigRequest, callback: google.cloud.dataform.v1.Dataform.CreateWorkflowConfigCallback): void;

Calls CreateWorkflowConfig.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[ICreateWorkflowConfigRequest](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/dataform/protos.google.cloud.dataform.v1.icreateworkflowconfigrequest)`   
CreateWorkflowConfigRequest message or plain object  
`callback` |  `[CreateWorkflowConfigCallback](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/overview.html)`   
Node-style callback called with the error, if any, and WorkflowConfig  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### createWorkflowConfig(request)
    
    
    public createWorkflowConfig(request: google.cloud.dataform.v1.ICreateWorkflowConfigRequest): Promise<google.cloud.dataform.v1.WorkflowConfig>;

Calls CreateWorkflowConfig.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[ICreateWorkflowConfigRequest](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/dataform/protos.google.cloud.dataform.v1.icreateworkflowconfigrequest)`   
CreateWorkflowConfigRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.dataform.v1.WorkflowConfig](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/dataform/protos.google.cloud.dataform.v1.workflowconfig-class)>` | Promise  
  
### createWorkflowInvocation(request, callback)
    
    
    public createWorkflowInvocation(request: google.cloud.dataform.v1.ICreateWorkflowInvocationRequest, callback: google.cloud.dataform.v1.Dataform.CreateWorkflowInvocationCallback): void;

Calls CreateWorkflowInvocation.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[ICreateWorkflowInvocationRequest](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/dataform/protos.google.cloud.dataform.v1.icreateworkflowinvocationrequest)`   
CreateWorkflowInvocationRequest message or plain object  
`callback` |  `[CreateWorkflowInvocationCallback](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/overview.html)`   
Node-style callback called with the error, if any, and WorkflowInvocation  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### createWorkflowInvocation(request)
    
    
    public createWorkflowInvocation(request: google.cloud.dataform.v1.ICreateWorkflowInvocationRequest): Promise<google.cloud.dataform.v1.WorkflowInvocation>;

Calls CreateWorkflowInvocation.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[ICreateWorkflowInvocationRequest](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/dataform/protos.google.cloud.dataform.v1.icreateworkflowinvocationrequest)`   
CreateWorkflowInvocationRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.dataform.v1.WorkflowInvocation](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/dataform/protos.google.cloud.dataform.v1.workflowinvocation-class)>` | Promise  
  
### createWorkspace(request, callback)
    
    
    public createWorkspace(request: google.cloud.dataform.v1.ICreateWorkspaceRequest, callback: google.cloud.dataform.v1.Dataform.CreateWorkspaceCallback): void;

Calls CreateWorkspace.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[ICreateWorkspaceRequest](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/dataform/protos.google.cloud.dataform.v1.icreateworkspacerequest)`   
CreateWorkspaceRequest message or plain object  
`callback` |  `[CreateWorkspaceCallback](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/overview.html)`   
Node-style callback called with the error, if any, and Workspace  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### createWorkspace(request)
    
    
    public createWorkspace(request: google.cloud.dataform.v1.ICreateWorkspaceRequest): Promise<google.cloud.dataform.v1.Workspace>;

Calls CreateWorkspace.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[ICreateWorkspaceRequest](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/dataform/protos.google.cloud.dataform.v1.icreateworkspacerequest)`   
CreateWorkspaceRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.dataform.v1.Workspace](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/dataform/protos.google.cloud.dataform.v1.workspace)>` | Promise  
  
### deleteFolder(request, callback)
    
    
    public deleteFolder(request: google.cloud.dataform.v1.IDeleteFolderRequest, callback: google.cloud.dataform.v1.Dataform.DeleteFolderCallback): void;

Calls DeleteFolder.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IDeleteFolderRequest](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/dataform/protos.google.cloud.dataform.v1.ideletefolderrequest)`   
DeleteFolderRequest message or plain object  
`callback` |  `[DeleteFolderCallback](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/overview.html)`   
Node-style callback called with the error, if any, and Empty  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### deleteFolder(request)
    
    
    public deleteFolder(request: google.cloud.dataform.v1.IDeleteFolderRequest): Promise<google.protobuf.Empty>;

Calls DeleteFolder.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IDeleteFolderRequest](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/dataform/protos.google.cloud.dataform.v1.ideletefolderrequest)`   
DeleteFolderRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.protobuf.Empty](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/dataform/protos.google.protobuf.empty)>` | Promise  
  
### deleteFolderTree(request, callback)
    
    
    public deleteFolderTree(request: google.cloud.dataform.v1.IDeleteFolderTreeRequest, callback: google.cloud.dataform.v1.Dataform.DeleteFolderTreeCallback): void;

Calls DeleteFolderTree.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IDeleteFolderTreeRequest](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/dataform/protos.google.cloud.dataform.v1.ideletefoldertreerequest)`   
DeleteFolderTreeRequest message or plain object  
`callback` |  `[DeleteFolderTreeCallback](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/overview.html)`   
Node-style callback called with the error, if any, and Operation  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### deleteFolderTree(request)
    
    
    public deleteFolderTree(request: google.cloud.dataform.v1.IDeleteFolderTreeRequest): Promise<google.longrunning.Operation>;

Calls DeleteFolderTree.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IDeleteFolderTreeRequest](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/dataform/protos.google.cloud.dataform.v1.ideletefoldertreerequest)`   
DeleteFolderTreeRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.longrunning.Operation](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/dataform/protos.google.longrunning.operation)>` | Promise  
  
### deleteReleaseConfig(request, callback)
    
    
    public deleteReleaseConfig(request: google.cloud.dataform.v1.IDeleteReleaseConfigRequest, callback: google.cloud.dataform.v1.Dataform.DeleteReleaseConfigCallback): void;

Calls DeleteReleaseConfig.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IDeleteReleaseConfigRequest](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/dataform/protos.google.cloud.dataform.v1.ideletereleaseconfigrequest)`   
DeleteReleaseConfigRequest message or plain object  
`callback` |  `[DeleteReleaseConfigCallback](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/overview.html)`   
Node-style callback called with the error, if any, and Empty  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### deleteReleaseConfig(request)
    
    
    public deleteReleaseConfig(request: google.cloud.dataform.v1.IDeleteReleaseConfigRequest): Promise<google.protobuf.Empty>;

Calls DeleteReleaseConfig.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IDeleteReleaseConfigRequest](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/dataform/protos.google.cloud.dataform.v1.ideletereleaseconfigrequest)`   
DeleteReleaseConfigRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.protobuf.Empty](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/dataform/protos.google.protobuf.empty)>` | Promise  
  
### deleteRepository(request, callback)
    
    
    public deleteRepository(request: google.cloud.dataform.v1.IDeleteRepositoryRequest, callback: google.cloud.dataform.v1.Dataform.DeleteRepositoryCallback): void;

Calls DeleteRepository.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IDeleteRepositoryRequest](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/dataform/protos.google.cloud.dataform.v1.ideleterepositoryrequest)`   
DeleteRepositoryRequest message or plain object  
`callback` |  `[DeleteRepositoryCallback](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/overview.html)`   
Node-style callback called with the error, if any, and Empty  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### deleteRepository(request)
    
    
    public deleteRepository(request: google.cloud.dataform.v1.IDeleteRepositoryRequest): Promise<google.protobuf.Empty>;

Calls DeleteRepository.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IDeleteRepositoryRequest](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/dataform/protos.google.cloud.dataform.v1.ideleterepositoryrequest)`   
DeleteRepositoryRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.protobuf.Empty](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/dataform/protos.google.protobuf.empty)>` | Promise  
  
### deleteTeamFolder(request, callback)
    
    
    public deleteTeamFolder(request: google.cloud.dataform.v1.IDeleteTeamFolderRequest, callback: google.cloud.dataform.v1.Dataform.DeleteTeamFolderCallback): void;

Calls DeleteTeamFolder.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IDeleteTeamFolderRequest](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/dataform/protos.google.cloud.dataform.v1.ideleteteamfolderrequest)`   
DeleteTeamFolderRequest message or plain object  
`callback` |  `[DeleteTeamFolderCallback](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/overview.html)`   
Node-style callback called with the error, if any, and Empty  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### deleteTeamFolder(request)
    
    
    public deleteTeamFolder(request: google.cloud.dataform.v1.IDeleteTeamFolderRequest): Promise<google.protobuf.Empty>;

Calls DeleteTeamFolder.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IDeleteTeamFolderRequest](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/dataform/protos.google.cloud.dataform.v1.ideleteteamfolderrequest)`   
DeleteTeamFolderRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.protobuf.Empty](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/dataform/protos.google.protobuf.empty)>` | Promise  
  
### deleteTeamFolderTree(request, callback)
    
    
    public deleteTeamFolderTree(request: google.cloud.dataform.v1.IDeleteTeamFolderTreeRequest, callback: google.cloud.dataform.v1.Dataform.DeleteTeamFolderTreeCallback): void;

Calls DeleteTeamFolderTree.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IDeleteTeamFolderTreeRequest](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/dataform/protos.google.cloud.dataform.v1.ideleteteamfoldertreerequest)`   
DeleteTeamFolderTreeRequest message or plain object  
`callback` |  `[DeleteTeamFolderTreeCallback](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/overview.html)`   
Node-style callback called with the error, if any, and Operation  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### deleteTeamFolderTree(request)
    
    
    public deleteTeamFolderTree(request: google.cloud.dataform.v1.IDeleteTeamFolderTreeRequest): Promise<google.longrunning.Operation>;

Calls DeleteTeamFolderTree.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IDeleteTeamFolderTreeRequest](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/dataform/protos.google.cloud.dataform.v1.ideleteteamfoldertreerequest)`   
DeleteTeamFolderTreeRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.longrunning.Operation](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/dataform/protos.google.longrunning.operation)>` | Promise  
  
### deleteWorkflowConfig(request, callback)
    
    
    public deleteWorkflowConfig(request: google.cloud.dataform.v1.IDeleteWorkflowConfigRequest, callback: google.cloud.dataform.v1.Dataform.DeleteWorkflowConfigCallback): void;

Calls DeleteWorkflowConfig.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IDeleteWorkflowConfigRequest](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/dataform/protos.google.cloud.dataform.v1.ideleteworkflowconfigrequest)`   
DeleteWorkflowConfigRequest message or plain object  
`callback` |  `[DeleteWorkflowConfigCallback](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/overview.html)`   
Node-style callback called with the error, if any, and Empty  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### deleteWorkflowConfig(request)
    
    
    public deleteWorkflowConfig(request: google.cloud.dataform.v1.IDeleteWorkflowConfigRequest): Promise<google.protobuf.Empty>;

Calls DeleteWorkflowConfig.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IDeleteWorkflowConfigRequest](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/dataform/protos.google.cloud.dataform.v1.ideleteworkflowconfigrequest)`   
DeleteWorkflowConfigRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.protobuf.Empty](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/dataform/protos.google.protobuf.empty)>` | Promise  
  
### deleteWorkflowInvocation(request, callback)
    
    
    public deleteWorkflowInvocation(request: google.cloud.dataform.v1.IDeleteWorkflowInvocationRequest, callback: google.cloud.dataform.v1.Dataform.DeleteWorkflowInvocationCallback): void;

Calls DeleteWorkflowInvocation.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IDeleteWorkflowInvocationRequest](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/dataform/protos.google.cloud.dataform.v1.ideleteworkflowinvocationrequest)`   
DeleteWorkflowInvocationRequest message or plain object  
`callback` |  `[DeleteWorkflowInvocationCallback](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/overview.html)`   
Node-style callback called with the error, if any, and Empty  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### deleteWorkflowInvocation(request)
    
    
    public deleteWorkflowInvocation(request: google.cloud.dataform.v1.IDeleteWorkflowInvocationRequest): Promise<google.protobuf.Empty>;

Calls DeleteWorkflowInvocation.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IDeleteWorkflowInvocationRequest](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/dataform/protos.google.cloud.dataform.v1.ideleteworkflowinvocationrequest)`   
DeleteWorkflowInvocationRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.protobuf.Empty](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/dataform/protos.google.protobuf.empty)>` | Promise  
  
### deleteWorkspace(request, callback)
    
    
    public deleteWorkspace(request: google.cloud.dataform.v1.IDeleteWorkspaceRequest, callback: google.cloud.dataform.v1.Dataform.DeleteWorkspaceCallback): void;

Calls DeleteWorkspace.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IDeleteWorkspaceRequest](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/dataform/protos.google.cloud.dataform.v1.ideleteworkspacerequest)`   
DeleteWorkspaceRequest message or plain object  
`callback` |  `[DeleteWorkspaceCallback](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/overview.html)`   
Node-style callback called with the error, if any, and Empty  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### deleteWorkspace(request)
    
    
    public deleteWorkspace(request: google.cloud.dataform.v1.IDeleteWorkspaceRequest): Promise<google.protobuf.Empty>;

Calls DeleteWorkspace.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IDeleteWorkspaceRequest](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/dataform/protos.google.cloud.dataform.v1.ideleteworkspacerequest)`   
DeleteWorkspaceRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.protobuf.Empty](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/dataform/protos.google.protobuf.empty)>` | Promise  
  
### fetchFileDiff(request, callback)
    
    
    public fetchFileDiff(request: google.cloud.dataform.v1.IFetchFileDiffRequest, callback: google.cloud.dataform.v1.Dataform.FetchFileDiffCallback): void;

Calls FetchFileDiff.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IFetchFileDiffRequest](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/dataform/protos.google.cloud.dataform.v1.ifetchfilediffrequest)`   
FetchFileDiffRequest message or plain object  
`callback` |  `[FetchFileDiffCallback](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/overview.html)`   
Node-style callback called with the error, if any, and FetchFileDiffResponse  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### fetchFileDiff(request)
    
    
    public fetchFileDiff(request: google.cloud.dataform.v1.IFetchFileDiffRequest): Promise<google.cloud.dataform.v1.FetchFileDiffResponse>;

Calls FetchFileDiff.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IFetchFileDiffRequest](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/dataform/protos.google.cloud.dataform.v1.ifetchfilediffrequest)`   
FetchFileDiffRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.dataform.v1.FetchFileDiffResponse](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/dataform/protos.google.cloud.dataform.v1.fetchfilediffresponse)>` | Promise  
  
### fetchFileGitStatuses(request, callback)
    
    
    public fetchFileGitStatuses(request: google.cloud.dataform.v1.IFetchFileGitStatusesRequest, callback: google.cloud.dataform.v1.Dataform.FetchFileGitStatusesCallback): void;

Calls FetchFileGitStatuses.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IFetchFileGitStatusesRequest](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/dataform/protos.google.cloud.dataform.v1.ifetchfilegitstatusesrequest)`   
FetchFileGitStatusesRequest message or plain object  
`callback` |  `[FetchFileGitStatusesCallback](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/overview.html)`   
Node-style callback called with the error, if any, and FetchFileGitStatusesResponse  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### fetchFileGitStatuses(request)
    
    
    public fetchFileGitStatuses(request: google.cloud.dataform.v1.IFetchFileGitStatusesRequest): Promise<google.cloud.dataform.v1.FetchFileGitStatusesResponse>;

Calls FetchFileGitStatuses.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IFetchFileGitStatusesRequest](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/dataform/protos.google.cloud.dataform.v1.ifetchfilegitstatusesrequest)`   
FetchFileGitStatusesRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.dataform.v1.FetchFileGitStatusesResponse](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/dataform/protos.google.cloud.dataform.v1.fetchfilegitstatusesresponse-class)>` | Promise  
  
### fetchGitAheadBehind(request, callback)
    
    
    public fetchGitAheadBehind(request: google.cloud.dataform.v1.IFetchGitAheadBehindRequest, callback: google.cloud.dataform.v1.Dataform.FetchGitAheadBehindCallback): void;

Calls FetchGitAheadBehind.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IFetchGitAheadBehindRequest](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/dataform/protos.google.cloud.dataform.v1.ifetchgitaheadbehindrequest)`   
FetchGitAheadBehindRequest message or plain object  
`callback` |  `[FetchGitAheadBehindCallback](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/overview.html)`   
Node-style callback called with the error, if any, and FetchGitAheadBehindResponse  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### fetchGitAheadBehind(request)
    
    
    public fetchGitAheadBehind(request: google.cloud.dataform.v1.IFetchGitAheadBehindRequest): Promise<google.cloud.dataform.v1.FetchGitAheadBehindResponse>;

Calls FetchGitAheadBehind.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IFetchGitAheadBehindRequest](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/dataform/protos.google.cloud.dataform.v1.ifetchgitaheadbehindrequest)`   
FetchGitAheadBehindRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.dataform.v1.FetchGitAheadBehindResponse](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/dataform/protos.google.cloud.dataform.v1.fetchgitaheadbehindresponse)>` | Promise  
  
### fetchRemoteBranches(request, callback)
    
    
    public fetchRemoteBranches(request: google.cloud.dataform.v1.IFetchRemoteBranchesRequest, callback: google.cloud.dataform.v1.Dataform.FetchRemoteBranchesCallback): void;

Calls FetchRemoteBranches.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IFetchRemoteBranchesRequest](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/dataform/protos.google.cloud.dataform.v1.ifetchremotebranchesrequest)`   
FetchRemoteBranchesRequest message or plain object  
`callback` |  `[FetchRemoteBranchesCallback](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/overview.html)`   
Node-style callback called with the error, if any, and FetchRemoteBranchesResponse  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### fetchRemoteBranches(request)
    
    
    public fetchRemoteBranches(request: google.cloud.dataform.v1.IFetchRemoteBranchesRequest): Promise<google.cloud.dataform.v1.FetchRemoteBranchesResponse>;

Calls FetchRemoteBranches.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IFetchRemoteBranchesRequest](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/dataform/protos.google.cloud.dataform.v1.ifetchremotebranchesrequest)`   
FetchRemoteBranchesRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.dataform.v1.FetchRemoteBranchesResponse](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/dataform/protos.google.cloud.dataform.v1.fetchremotebranchesresponse)>` | Promise  
  
### fetchRepositoryHistory(request, callback)
    
    
    public fetchRepositoryHistory(request: google.cloud.dataform.v1.IFetchRepositoryHistoryRequest, callback: google.cloud.dataform.v1.Dataform.FetchRepositoryHistoryCallback): void;

Calls FetchRepositoryHistory.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IFetchRepositoryHistoryRequest](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/dataform/protos.google.cloud.dataform.v1.ifetchrepositoryhistoryrequest)`   
FetchRepositoryHistoryRequest message or plain object  
`callback` |  `[FetchRepositoryHistoryCallback](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/overview.html)`   
Node-style callback called with the error, if any, and FetchRepositoryHistoryResponse  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### fetchRepositoryHistory(request)
    
    
    public fetchRepositoryHistory(request: google.cloud.dataform.v1.IFetchRepositoryHistoryRequest): Promise<google.cloud.dataform.v1.FetchRepositoryHistoryResponse>;

Calls FetchRepositoryHistory.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IFetchRepositoryHistoryRequest](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/dataform/protos.google.cloud.dataform.v1.ifetchrepositoryhistoryrequest)`   
FetchRepositoryHistoryRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.dataform.v1.FetchRepositoryHistoryResponse](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/dataform/protos.google.cloud.dataform.v1.fetchrepositoryhistoryresponse)>` | Promise  
  
### getCompilationResult(request, callback)
    
    
    public getCompilationResult(request: google.cloud.dataform.v1.IGetCompilationResultRequest, callback: google.cloud.dataform.v1.Dataform.GetCompilationResultCallback): void;

Calls GetCompilationResult.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IGetCompilationResultRequest](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/dataform/protos.google.cloud.dataform.v1.igetcompilationresultrequest)`   
GetCompilationResultRequest message or plain object  
`callback` |  `[GetCompilationResultCallback](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/overview.html)`   
Node-style callback called with the error, if any, and CompilationResult  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### getCompilationResult(request)
    
    
    public getCompilationResult(request: google.cloud.dataform.v1.IGetCompilationResultRequest): Promise<google.cloud.dataform.v1.CompilationResult>;

Calls GetCompilationResult.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IGetCompilationResultRequest](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/dataform/protos.google.cloud.dataform.v1.igetcompilationresultrequest)`   
GetCompilationResultRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.dataform.v1.CompilationResult](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/dataform/protos.google.cloud.dataform.v1.compilationresult-class)>` | Promise  
  
### getConfig(request, callback)
    
    
    public getConfig(request: google.cloud.dataform.v1.IGetConfigRequest, callback: google.cloud.dataform.v1.Dataform.GetConfigCallback): void;

Calls GetConfig.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IGetConfigRequest](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/dataform/protos.google.cloud.dataform.v1.igetconfigrequest)`   
GetConfigRequest message or plain object  
`callback` |  `[GetConfigCallback](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/overview.html)`   
Node-style callback called with the error, if any, and Config  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### getConfig(request)
    
    
    public getConfig(request: google.cloud.dataform.v1.IGetConfigRequest): Promise<google.cloud.dataform.v1.Config>;

Calls GetConfig.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IGetConfigRequest](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/dataform/protos.google.cloud.dataform.v1.igetconfigrequest)`   
GetConfigRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.dataform.v1.Config](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/dataform/protos.google.cloud.dataform.v1.config)>` | Promise  
  
### getFolder(request, callback)
    
    
    public getFolder(request: google.cloud.dataform.v1.IGetFolderRequest, callback: google.cloud.dataform.v1.Dataform.GetFolderCallback): void;

Calls GetFolder.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IGetFolderRequest](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/dataform/protos.google.cloud.dataform.v1.igetfolderrequest)`   
GetFolderRequest message or plain object  
`callback` |  `[GetFolderCallback](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/overview.html)`   
Node-style callback called with the error, if any, and Folder  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### getFolder(request)
    
    
    public getFolder(request: google.cloud.dataform.v1.IGetFolderRequest): Promise<google.cloud.dataform.v1.Folder>;

Calls GetFolder.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IGetFolderRequest](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/dataform/protos.google.cloud.dataform.v1.igetfolderrequest)`   
GetFolderRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.dataform.v1.Folder](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/dataform/protos.google.cloud.dataform.v1.folder)>` | Promise  
  
### getIamPolicy(request, callback)
    
    
    public getIamPolicy(request: google.iam.v1.IGetIamPolicyRequest, callback: google.cloud.dataform.v1.Dataform.GetIamPolicyCallback): void;

Calls GetIamPolicy.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IGetIamPolicyRequest](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/dataform/protos.google.iam.v1.igetiampolicyrequest)`   
GetIamPolicyRequest message or plain object  
`callback` |  `[GetIamPolicyCallback](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/overview.html)`   
Node-style callback called with the error, if any, and Policy  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### getIamPolicy(request)
    
    
    public getIamPolicy(request: google.iam.v1.IGetIamPolicyRequest): Promise<google.iam.v1.Policy>;

Calls GetIamPolicy.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IGetIamPolicyRequest](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/dataform/protos.google.iam.v1.igetiampolicyrequest)`   
GetIamPolicyRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.iam.v1.Policy](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/dataform/protos.google.iam.v1.policy)>` | Promise  
  
### getReleaseConfig(request, callback)
    
    
    public getReleaseConfig(request: google.cloud.dataform.v1.IGetReleaseConfigRequest, callback: google.cloud.dataform.v1.Dataform.GetReleaseConfigCallback): void;

Calls GetReleaseConfig.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IGetReleaseConfigRequest](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/dataform/protos.google.cloud.dataform.v1.igetreleaseconfigrequest)`   
GetReleaseConfigRequest message or plain object  
`callback` |  `[GetReleaseConfigCallback](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/overview.html)`   
Node-style callback called with the error, if any, and ReleaseConfig  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### getReleaseConfig(request)
    
    
    public getReleaseConfig(request: google.cloud.dataform.v1.IGetReleaseConfigRequest): Promise<google.cloud.dataform.v1.ReleaseConfig>;

Calls GetReleaseConfig.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IGetReleaseConfigRequest](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/dataform/protos.google.cloud.dataform.v1.igetreleaseconfigrequest)`   
GetReleaseConfigRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.dataform.v1.ReleaseConfig](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/dataform/protos.google.cloud.dataform.v1.releaseconfig-class)>` | Promise  
  
### getRepository(request, callback)
    
    
    public getRepository(request: google.cloud.dataform.v1.IGetRepositoryRequest, callback: google.cloud.dataform.v1.Dataform.GetRepositoryCallback): void;

Calls GetRepository.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IGetRepositoryRequest](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/dataform/protos.google.cloud.dataform.v1.igetrepositoryrequest)`   
GetRepositoryRequest message or plain object  
`callback` |  `[GetRepositoryCallback](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/overview.html)`   
Node-style callback called with the error, if any, and Repository  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### getRepository(request)
    
    
    public getRepository(request: google.cloud.dataform.v1.IGetRepositoryRequest): Promise<google.cloud.dataform.v1.Repository>;

Calls GetRepository.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IGetRepositoryRequest](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/dataform/protos.google.cloud.dataform.v1.igetrepositoryrequest)`   
GetRepositoryRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.dataform.v1.Repository](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/dataform/protos.google.cloud.dataform.v1.repository-class)>` | Promise  
  
### getTeamFolder(request, callback)
    
    
    public getTeamFolder(request: google.cloud.dataform.v1.IGetTeamFolderRequest, callback: google.cloud.dataform.v1.Dataform.GetTeamFolderCallback): void;

Calls GetTeamFolder.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IGetTeamFolderRequest](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/dataform/protos.google.cloud.dataform.v1.igetteamfolderrequest)`   
GetTeamFolderRequest message or plain object  
`callback` |  `[GetTeamFolderCallback](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/overview.html)`   
Node-style callback called with the error, if any, and TeamFolder  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### getTeamFolder(request)
    
    
    public getTeamFolder(request: google.cloud.dataform.v1.IGetTeamFolderRequest): Promise<google.cloud.dataform.v1.TeamFolder>;

Calls GetTeamFolder.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IGetTeamFolderRequest](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/dataform/protos.google.cloud.dataform.v1.igetteamfolderrequest)`   
GetTeamFolderRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.dataform.v1.TeamFolder](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/dataform/protos.google.cloud.dataform.v1.teamfolder)>` | Promise  
  
### getWorkflowConfig(request, callback)
    
    
    public getWorkflowConfig(request: google.cloud.dataform.v1.IGetWorkflowConfigRequest, callback: google.cloud.dataform.v1.Dataform.GetWorkflowConfigCallback): void;

Calls GetWorkflowConfig.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IGetWorkflowConfigRequest](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/dataform/protos.google.cloud.dataform.v1.igetworkflowconfigrequest)`   
GetWorkflowConfigRequest message or plain object  
`callback` |  `[GetWorkflowConfigCallback](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/overview.html)`   
Node-style callback called with the error, if any, and WorkflowConfig  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### getWorkflowConfig(request)
    
    
    public getWorkflowConfig(request: google.cloud.dataform.v1.IGetWorkflowConfigRequest): Promise<google.cloud.dataform.v1.WorkflowConfig>;

Calls GetWorkflowConfig.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IGetWorkflowConfigRequest](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/dataform/protos.google.cloud.dataform.v1.igetworkflowconfigrequest)`   
GetWorkflowConfigRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.dataform.v1.WorkflowConfig](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/dataform/protos.google.cloud.dataform.v1.workflowconfig-class)>` | Promise  
  
### getWorkflowInvocation(request, callback)
    
    
    public getWorkflowInvocation(request: google.cloud.dataform.v1.IGetWorkflowInvocationRequest, callback: google.cloud.dataform.v1.Dataform.GetWorkflowInvocationCallback): void;

Calls GetWorkflowInvocation.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IGetWorkflowInvocationRequest](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/dataform/protos.google.cloud.dataform.v1.igetworkflowinvocationrequest)`   
GetWorkflowInvocationRequest message or plain object  
`callback` |  `[GetWorkflowInvocationCallback](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/overview.html)`   
Node-style callback called with the error, if any, and WorkflowInvocation  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### getWorkflowInvocation(request)
    
    
    public getWorkflowInvocation(request: google.cloud.dataform.v1.IGetWorkflowInvocationRequest): Promise<google.cloud.dataform.v1.WorkflowInvocation>;

Calls GetWorkflowInvocation.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IGetWorkflowInvocationRequest](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/dataform/protos.google.cloud.dataform.v1.igetworkflowinvocationrequest)`   
GetWorkflowInvocationRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.dataform.v1.WorkflowInvocation](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/dataform/protos.google.cloud.dataform.v1.workflowinvocation-class)>` | Promise  
  
### getWorkspace(request, callback)
    
    
    public getWorkspace(request: google.cloud.dataform.v1.IGetWorkspaceRequest, callback: google.cloud.dataform.v1.Dataform.GetWorkspaceCallback): void;

Calls GetWorkspace.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IGetWorkspaceRequest](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/dataform/protos.google.cloud.dataform.v1.igetworkspacerequest)`   
GetWorkspaceRequest message or plain object  
`callback` |  `[GetWorkspaceCallback](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/overview.html)`   
Node-style callback called with the error, if any, and Workspace  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### getWorkspace(request)
    
    
    public getWorkspace(request: google.cloud.dataform.v1.IGetWorkspaceRequest): Promise<google.cloud.dataform.v1.Workspace>;

Calls GetWorkspace.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IGetWorkspaceRequest](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/dataform/protos.google.cloud.dataform.v1.igetworkspacerequest)`   
GetWorkspaceRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.dataform.v1.Workspace](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/dataform/protos.google.cloud.dataform.v1.workspace)>` | Promise  
  
### installNpmPackages(request, callback)
    
    
    public installNpmPackages(request: google.cloud.dataform.v1.IInstallNpmPackagesRequest, callback: google.cloud.dataform.v1.Dataform.InstallNpmPackagesCallback): void;

Calls InstallNpmPackages.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IInstallNpmPackagesRequest](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/dataform/protos.google.cloud.dataform.v1.iinstallnpmpackagesrequest)`   
InstallNpmPackagesRequest message or plain object  
`callback` |  `[InstallNpmPackagesCallback](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/overview.html)`   
Node-style callback called with the error, if any, and InstallNpmPackagesResponse  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### installNpmPackages(request)
    
    
    public installNpmPackages(request: google.cloud.dataform.v1.IInstallNpmPackagesRequest): Promise<google.cloud.dataform.v1.InstallNpmPackagesResponse>;

Calls InstallNpmPackages.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IInstallNpmPackagesRequest](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/dataform/protos.google.cloud.dataform.v1.iinstallnpmpackagesrequest)`   
InstallNpmPackagesRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.dataform.v1.InstallNpmPackagesResponse](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/dataform/protos.google.cloud.dataform.v1.installnpmpackagesresponse)>` | Promise  
  
### listCompilationResults(request, callback)
    
    
    public listCompilationResults(request: google.cloud.dataform.v1.IListCompilationResultsRequest, callback: google.cloud.dataform.v1.Dataform.ListCompilationResultsCallback): void;

Calls ListCompilationResults.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListCompilationResultsRequest](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/dataform/protos.google.cloud.dataform.v1.ilistcompilationresultsrequest)`   
ListCompilationResultsRequest message or plain object  
`callback` |  `[ListCompilationResultsCallback](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/overview.html)`   
Node-style callback called with the error, if any, and ListCompilationResultsResponse  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### listCompilationResults(request)
    
    
    public listCompilationResults(request: google.cloud.dataform.v1.IListCompilationResultsRequest): Promise<google.cloud.dataform.v1.ListCompilationResultsResponse>;

Calls ListCompilationResults.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IListCompilationResultsRequest](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/dataform/protos.google.cloud.dataform.v1.ilistcompilationresultsrequest)`   
ListCompilationResultsRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.dataform.v1.ListCompilationResultsResponse](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/dataform/protos.google.cloud.dataform.v1.listcompilationresultsresponse)>` | Promise  
  
### listReleaseConfigs(request, callback)
    
    
    public listReleaseConfigs(request: google.cloud.dataform.v1.IListReleaseConfigsRequest, callback: google.cloud.dataform.v1.Dataform.ListReleaseConfigsCallback): void;

Calls ListReleaseConfigs.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListReleaseConfigsRequest](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/dataform/protos.google.cloud.dataform.v1.ilistreleaseconfigsrequest)`   
ListReleaseConfigsRequest message or plain object  
`callback` |  `[ListReleaseConfigsCallback](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/overview.html)`   
Node-style callback called with the error, if any, and ListReleaseConfigsResponse  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### listReleaseConfigs(request)
    
    
    public listReleaseConfigs(request: google.cloud.dataform.v1.IListReleaseConfigsRequest): Promise<google.cloud.dataform.v1.ListReleaseConfigsResponse>;

Calls ListReleaseConfigs.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IListReleaseConfigsRequest](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/dataform/protos.google.cloud.dataform.v1.ilistreleaseconfigsrequest)`   
ListReleaseConfigsRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.dataform.v1.ListReleaseConfigsResponse](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/dataform/protos.google.cloud.dataform.v1.listreleaseconfigsresponse)>` | Promise  
  
### listRepositories(request, callback)
    
    
    public listRepositories(request: google.cloud.dataform.v1.IListRepositoriesRequest, callback: google.cloud.dataform.v1.Dataform.ListRepositoriesCallback): void;

Calls ListRepositories.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListRepositoriesRequest](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/dataform/protos.google.cloud.dataform.v1.ilistrepositoriesrequest)`   
ListRepositoriesRequest message or plain object  
`callback` |  `[ListRepositoriesCallback](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/overview.html)`   
Node-style callback called with the error, if any, and ListRepositoriesResponse  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### listRepositories(request)
    
    
    public listRepositories(request: google.cloud.dataform.v1.IListRepositoriesRequest): Promise<google.cloud.dataform.v1.ListRepositoriesResponse>;

Calls ListRepositories.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IListRepositoriesRequest](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/dataform/protos.google.cloud.dataform.v1.ilistrepositoriesrequest)`   
ListRepositoriesRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.dataform.v1.ListRepositoriesResponse](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/dataform/protos.google.cloud.dataform.v1.listrepositoriesresponse)>` | Promise  
  
### listWorkflowConfigs(request, callback)
    
    
    public listWorkflowConfigs(request: google.cloud.dataform.v1.IListWorkflowConfigsRequest, callback: google.cloud.dataform.v1.Dataform.ListWorkflowConfigsCallback): void;

Calls ListWorkflowConfigs.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListWorkflowConfigsRequest](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/dataform/protos.google.cloud.dataform.v1.ilistworkflowconfigsrequest)`   
ListWorkflowConfigsRequest message or plain object  
`callback` |  `[ListWorkflowConfigsCallback](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/overview.html)`   
Node-style callback called with the error, if any, and ListWorkflowConfigsResponse  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### listWorkflowConfigs(request)
    
    
    public listWorkflowConfigs(request: google.cloud.dataform.v1.IListWorkflowConfigsRequest): Promise<google.cloud.dataform.v1.ListWorkflowConfigsResponse>;

Calls ListWorkflowConfigs.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IListWorkflowConfigsRequest](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/dataform/protos.google.cloud.dataform.v1.ilistworkflowconfigsrequest)`   
ListWorkflowConfigsRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.dataform.v1.ListWorkflowConfigsResponse](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/dataform/protos.google.cloud.dataform.v1.listworkflowconfigsresponse)>` | Promise  
  
### listWorkflowInvocations(request, callback)
    
    
    public listWorkflowInvocations(request: google.cloud.dataform.v1.IListWorkflowInvocationsRequest, callback: google.cloud.dataform.v1.Dataform.ListWorkflowInvocationsCallback): void;

Calls ListWorkflowInvocations.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListWorkflowInvocationsRequest](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/dataform/protos.google.cloud.dataform.v1.ilistworkflowinvocationsrequest)`   
ListWorkflowInvocationsRequest message or plain object  
`callback` |  `[ListWorkflowInvocationsCallback](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/overview.html)`   
Node-style callback called with the error, if any, and ListWorkflowInvocationsResponse  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### listWorkflowInvocations(request)
    
    
    public listWorkflowInvocations(request: google.cloud.dataform.v1.IListWorkflowInvocationsRequest): Promise<google.cloud.dataform.v1.ListWorkflowInvocationsResponse>;

Calls ListWorkflowInvocations.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IListWorkflowInvocationsRequest](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/dataform/protos.google.cloud.dataform.v1.ilistworkflowinvocationsrequest)`   
ListWorkflowInvocationsRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.dataform.v1.ListWorkflowInvocationsResponse](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/dataform/protos.google.cloud.dataform.v1.listworkflowinvocationsresponse)>` | Promise  
  
### listWorkspaces(request, callback)
    
    
    public listWorkspaces(request: google.cloud.dataform.v1.IListWorkspacesRequest, callback: google.cloud.dataform.v1.Dataform.ListWorkspacesCallback): void;

Calls ListWorkspaces.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListWorkspacesRequest](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/dataform/protos.google.cloud.dataform.v1.ilistworkspacesrequest)`   
ListWorkspacesRequest message or plain object  
`callback` |  `[ListWorkspacesCallback](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/overview.html)`   
Node-style callback called with the error, if any, and ListWorkspacesResponse  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### listWorkspaces(request)
    
    
    public listWorkspaces(request: google.cloud.dataform.v1.IListWorkspacesRequest): Promise<google.cloud.dataform.v1.ListWorkspacesResponse>;

Calls ListWorkspaces.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IListWorkspacesRequest](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/dataform/protos.google.cloud.dataform.v1.ilistworkspacesrequest)`   
ListWorkspacesRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.dataform.v1.ListWorkspacesResponse](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/dataform/protos.google.cloud.dataform.v1.listworkspacesresponse)>` | Promise  
  
### makeDirectory(request, callback)
    
    
    public makeDirectory(request: google.cloud.dataform.v1.IMakeDirectoryRequest, callback: google.cloud.dataform.v1.Dataform.MakeDirectoryCallback): void;

Calls MakeDirectory.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IMakeDirectoryRequest](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/dataform/protos.google.cloud.dataform.v1.imakedirectoryrequest)`   
MakeDirectoryRequest message or plain object  
`callback` |  `[MakeDirectoryCallback](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/overview.html)`   
Node-style callback called with the error, if any, and MakeDirectoryResponse  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### makeDirectory(request)
    
    
    public makeDirectory(request: google.cloud.dataform.v1.IMakeDirectoryRequest): Promise<google.cloud.dataform.v1.MakeDirectoryResponse>;

Calls MakeDirectory.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IMakeDirectoryRequest](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/dataform/protos.google.cloud.dataform.v1.imakedirectoryrequest)`   
MakeDirectoryRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.dataform.v1.MakeDirectoryResponse](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/dataform/protos.google.cloud.dataform.v1.makedirectoryresponse)>` | Promise  
  
### moveDirectory(request, callback)
    
    
    public moveDirectory(request: google.cloud.dataform.v1.IMoveDirectoryRequest, callback: google.cloud.dataform.v1.Dataform.MoveDirectoryCallback): void;

Calls MoveDirectory.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IMoveDirectoryRequest](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/dataform/protos.google.cloud.dataform.v1.imovedirectoryrequest)`   
MoveDirectoryRequest message or plain object  
`callback` |  `[MoveDirectoryCallback](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/overview.html)`   
Node-style callback called with the error, if any, and MoveDirectoryResponse  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### moveDirectory(request)
    
    
    public moveDirectory(request: google.cloud.dataform.v1.IMoveDirectoryRequest): Promise<google.cloud.dataform.v1.MoveDirectoryResponse>;

Calls MoveDirectory.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IMoveDirectoryRequest](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/dataform/protos.google.cloud.dataform.v1.imovedirectoryrequest)`   
MoveDirectoryRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.dataform.v1.MoveDirectoryResponse](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/dataform/protos.google.cloud.dataform.v1.movedirectoryresponse)>` | Promise  
  
### moveFile(request, callback)
    
    
    public moveFile(request: google.cloud.dataform.v1.IMoveFileRequest, callback: google.cloud.dataform.v1.Dataform.MoveFileCallback): void;

Calls MoveFile.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IMoveFileRequest](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/dataform/protos.google.cloud.dataform.v1.imovefilerequest)`   
MoveFileRequest message or plain object  
`callback` |  `[MoveFileCallback](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/overview.html)`   
Node-style callback called with the error, if any, and MoveFileResponse  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### moveFile(request)
    
    
    public moveFile(request: google.cloud.dataform.v1.IMoveFileRequest): Promise<google.cloud.dataform.v1.MoveFileResponse>;

Calls MoveFile.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IMoveFileRequest](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/dataform/protos.google.cloud.dataform.v1.imovefilerequest)`   
MoveFileRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.dataform.v1.MoveFileResponse](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/dataform/protos.google.cloud.dataform.v1.movefileresponse)>` | Promise  
  
### moveFolder(request, callback)
    
    
    public moveFolder(request: google.cloud.dataform.v1.IMoveFolderRequest, callback: google.cloud.dataform.v1.Dataform.MoveFolderCallback): void;

Calls MoveFolder.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IMoveFolderRequest](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/dataform/protos.google.cloud.dataform.v1.imovefolderrequest)`   
MoveFolderRequest message or plain object  
`callback` |  `[MoveFolderCallback](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/overview.html)`   
Node-style callback called with the error, if any, and Operation  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### moveFolder(request)
    
    
    public moveFolder(request: google.cloud.dataform.v1.IMoveFolderRequest): Promise<google.longrunning.Operation>;

Calls MoveFolder.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IMoveFolderRequest](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/dataform/protos.google.cloud.dataform.v1.imovefolderrequest)`   
MoveFolderRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.longrunning.Operation](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/dataform/protos.google.longrunning.operation)>` | Promise  
  
### moveRepository(request, callback)
    
    
    public moveRepository(request: google.cloud.dataform.v1.IMoveRepositoryRequest, callback: google.cloud.dataform.v1.Dataform.MoveRepositoryCallback): void;

Calls MoveRepository.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IMoveRepositoryRequest](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/dataform/protos.google.cloud.dataform.v1.imoverepositoryrequest)`   
MoveRepositoryRequest message or plain object  
`callback` |  `[MoveRepositoryCallback](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/overview.html)`   
Node-style callback called with the error, if any, and Operation  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### moveRepository(request)
    
    
    public moveRepository(request: google.cloud.dataform.v1.IMoveRepositoryRequest): Promise<google.longrunning.Operation>;

Calls MoveRepository.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IMoveRepositoryRequest](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/dataform/protos.google.cloud.dataform.v1.imoverepositoryrequest)`   
MoveRepositoryRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.longrunning.Operation](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/dataform/protos.google.longrunning.operation)>` | Promise  
  
### pullGitCommits(request, callback)
    
    
    public pullGitCommits(request: google.cloud.dataform.v1.IPullGitCommitsRequest, callback: google.cloud.dataform.v1.Dataform.PullGitCommitsCallback): void;

Calls PullGitCommits.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IPullGitCommitsRequest](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/dataform/protos.google.cloud.dataform.v1.ipullgitcommitsrequest)`   
PullGitCommitsRequest message or plain object  
`callback` |  `[PullGitCommitsCallback](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/overview.html)`   
Node-style callback called with the error, if any, and PullGitCommitsResponse  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### pullGitCommits(request)
    
    
    public pullGitCommits(request: google.cloud.dataform.v1.IPullGitCommitsRequest): Promise<google.cloud.dataform.v1.PullGitCommitsResponse>;

Calls PullGitCommits.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IPullGitCommitsRequest](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/dataform/protos.google.cloud.dataform.v1.ipullgitcommitsrequest)`   
PullGitCommitsRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.dataform.v1.PullGitCommitsResponse](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/dataform/protos.google.cloud.dataform.v1.pullgitcommitsresponse)>` | Promise  
  
### pushGitCommits(request, callback)
    
    
    public pushGitCommits(request: google.cloud.dataform.v1.IPushGitCommitsRequest, callback: google.cloud.dataform.v1.Dataform.PushGitCommitsCallback): void;

Calls PushGitCommits.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IPushGitCommitsRequest](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/dataform/protos.google.cloud.dataform.v1.ipushgitcommitsrequest)`   
PushGitCommitsRequest message or plain object  
`callback` |  `[PushGitCommitsCallback](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/overview.html)`   
Node-style callback called with the error, if any, and PushGitCommitsResponse  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### pushGitCommits(request)
    
    
    public pushGitCommits(request: google.cloud.dataform.v1.IPushGitCommitsRequest): Promise<google.cloud.dataform.v1.PushGitCommitsResponse>;

Calls PushGitCommits.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IPushGitCommitsRequest](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/dataform/protos.google.cloud.dataform.v1.ipushgitcommitsrequest)`   
PushGitCommitsRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.dataform.v1.PushGitCommitsResponse](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/dataform/protos.google.cloud.dataform.v1.pushgitcommitsresponse)>` | Promise  
  
### queryCompilationResultActions(request, callback)
    
    
    public queryCompilationResultActions(request: google.cloud.dataform.v1.IQueryCompilationResultActionsRequest, callback: google.cloud.dataform.v1.Dataform.QueryCompilationResultActionsCallback): void;

Calls QueryCompilationResultActions.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IQueryCompilationResultActionsRequest](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/dataform/protos.google.cloud.dataform.v1.iquerycompilationresultactionsrequest)`   
QueryCompilationResultActionsRequest message or plain object  
`callback` |  `[QueryCompilationResultActionsCallback](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/overview.html)`   
Node-style callback called with the error, if any, and QueryCompilationResultActionsResponse  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### queryCompilationResultActions(request)
    
    
    public queryCompilationResultActions(request: google.cloud.dataform.v1.IQueryCompilationResultActionsRequest): Promise<google.cloud.dataform.v1.QueryCompilationResultActionsResponse>;

Calls QueryCompilationResultActions.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IQueryCompilationResultActionsRequest](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/dataform/protos.google.cloud.dataform.v1.iquerycompilationresultactionsrequest)`   
QueryCompilationResultActionsRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.dataform.v1.QueryCompilationResultActionsResponse](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/dataform/protos.google.cloud.dataform.v1.querycompilationresultactionsresponse)>` | Promise  
  
### queryDirectoryContents(request, callback)
    
    
    public queryDirectoryContents(request: google.cloud.dataform.v1.IQueryDirectoryContentsRequest, callback: google.cloud.dataform.v1.Dataform.QueryDirectoryContentsCallback): void;

Calls QueryDirectoryContents.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IQueryDirectoryContentsRequest](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/dataform/protos.google.cloud.dataform.v1.iquerydirectorycontentsrequest)`   
QueryDirectoryContentsRequest message or plain object  
`callback` |  `[QueryDirectoryContentsCallback](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/overview.html)`   
Node-style callback called with the error, if any, and QueryDirectoryContentsResponse  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### queryDirectoryContents(request)
    
    
    public queryDirectoryContents(request: google.cloud.dataform.v1.IQueryDirectoryContentsRequest): Promise<google.cloud.dataform.v1.QueryDirectoryContentsResponse>;

Calls QueryDirectoryContents.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IQueryDirectoryContentsRequest](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/dataform/protos.google.cloud.dataform.v1.iquerydirectorycontentsrequest)`   
QueryDirectoryContentsRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.dataform.v1.QueryDirectoryContentsResponse](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/dataform/protos.google.cloud.dataform.v1.querydirectorycontentsresponse)>` | Promise  
  
### queryFolderContents(request, callback)
    
    
    public queryFolderContents(request: google.cloud.dataform.v1.IQueryFolderContentsRequest, callback: google.cloud.dataform.v1.Dataform.QueryFolderContentsCallback): void;

Calls QueryFolderContents.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IQueryFolderContentsRequest](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/dataform/protos.google.cloud.dataform.v1.iqueryfoldercontentsrequest)`   
QueryFolderContentsRequest message or plain object  
`callback` |  `[QueryFolderContentsCallback](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/overview.html)`   
Node-style callback called with the error, if any, and QueryFolderContentsResponse  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### queryFolderContents(request)
    
    
    public queryFolderContents(request: google.cloud.dataform.v1.IQueryFolderContentsRequest): Promise<google.cloud.dataform.v1.QueryFolderContentsResponse>;

Calls QueryFolderContents.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IQueryFolderContentsRequest](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/dataform/protos.google.cloud.dataform.v1.iqueryfoldercontentsrequest)`   
QueryFolderContentsRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.dataform.v1.QueryFolderContentsResponse](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/dataform/protos.google.cloud.dataform.v1.queryfoldercontentsresponse-class)>` | Promise  
  
### queryRepositoryDirectoryContents(request, callback)
    
    
    public queryRepositoryDirectoryContents(request: google.cloud.dataform.v1.IQueryRepositoryDirectoryContentsRequest, callback: google.cloud.dataform.v1.Dataform.QueryRepositoryDirectoryContentsCallback): void;

Calls QueryRepositoryDirectoryContents.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IQueryRepositoryDirectoryContentsRequest](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/dataform/protos.google.cloud.dataform.v1.iqueryrepositorydirectorycontentsrequest)`   
QueryRepositoryDirectoryContentsRequest message or plain object  
`callback` |  `[QueryRepositoryDirectoryContentsCallback](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/overview.html)`   
Node-style callback called with the error, if any, and QueryRepositoryDirectoryContentsResponse  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### queryRepositoryDirectoryContents(request)
    
    
    public queryRepositoryDirectoryContents(request: google.cloud.dataform.v1.IQueryRepositoryDirectoryContentsRequest): Promise<google.cloud.dataform.v1.QueryRepositoryDirectoryContentsResponse>;

Calls QueryRepositoryDirectoryContents.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IQueryRepositoryDirectoryContentsRequest](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/dataform/protos.google.cloud.dataform.v1.iqueryrepositorydirectorycontentsrequest)`   
QueryRepositoryDirectoryContentsRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.dataform.v1.QueryRepositoryDirectoryContentsResponse](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/dataform/protos.google.cloud.dataform.v1.queryrepositorydirectorycontentsresponse)>` | Promise  
  
### queryTeamFolderContents(request, callback)
    
    
    public queryTeamFolderContents(request: google.cloud.dataform.v1.IQueryTeamFolderContentsRequest, callback: google.cloud.dataform.v1.Dataform.QueryTeamFolderContentsCallback): void;

Calls QueryTeamFolderContents.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IQueryTeamFolderContentsRequest](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/dataform/protos.google.cloud.dataform.v1.iqueryteamfoldercontentsrequest)`   
QueryTeamFolderContentsRequest message or plain object  
`callback` |  `[QueryTeamFolderContentsCallback](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/overview.html)`   
Node-style callback called with the error, if any, and QueryTeamFolderContentsResponse  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### queryTeamFolderContents(request)
    
    
    public queryTeamFolderContents(request: google.cloud.dataform.v1.IQueryTeamFolderContentsRequest): Promise<google.cloud.dataform.v1.QueryTeamFolderContentsResponse>;

Calls QueryTeamFolderContents.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IQueryTeamFolderContentsRequest](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/dataform/protos.google.cloud.dataform.v1.iqueryteamfoldercontentsrequest)`   
QueryTeamFolderContentsRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.dataform.v1.QueryTeamFolderContentsResponse](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/dataform/protos.google.cloud.dataform.v1.queryteamfoldercontentsresponse-class)>` | Promise  
  
### queryUserRootContents(request, callback)
    
    
    public queryUserRootContents(request: google.cloud.dataform.v1.IQueryUserRootContentsRequest, callback: google.cloud.dataform.v1.Dataform.QueryUserRootContentsCallback): void;

Calls QueryUserRootContents.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IQueryUserRootContentsRequest](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/dataform/protos.google.cloud.dataform.v1.iqueryuserrootcontentsrequest)`   
QueryUserRootContentsRequest message or plain object  
`callback` |  `[QueryUserRootContentsCallback](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/overview.html)`   
Node-style callback called with the error, if any, and QueryUserRootContentsResponse  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### queryUserRootContents(request)
    
    
    public queryUserRootContents(request: google.cloud.dataform.v1.IQueryUserRootContentsRequest): Promise<google.cloud.dataform.v1.QueryUserRootContentsResponse>;

Calls QueryUserRootContents.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IQueryUserRootContentsRequest](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/dataform/protos.google.cloud.dataform.v1.iqueryuserrootcontentsrequest)`   
QueryUserRootContentsRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.dataform.v1.QueryUserRootContentsResponse](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/dataform/protos.google.cloud.dataform.v1.queryuserrootcontentsresponse-class)>` | Promise  
  
### queryWorkflowInvocationActions(request, callback)
    
    
    public queryWorkflowInvocationActions(request: google.cloud.dataform.v1.IQueryWorkflowInvocationActionsRequest, callback: google.cloud.dataform.v1.Dataform.QueryWorkflowInvocationActionsCallback): void;

Calls QueryWorkflowInvocationActions.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IQueryWorkflowInvocationActionsRequest](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/dataform/protos.google.cloud.dataform.v1.iqueryworkflowinvocationactionsrequest)`   
QueryWorkflowInvocationActionsRequest message or plain object  
`callback` |  `[QueryWorkflowInvocationActionsCallback](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/overview.html)`   
Node-style callback called with the error, if any, and QueryWorkflowInvocationActionsResponse  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### queryWorkflowInvocationActions(request)
    
    
    public queryWorkflowInvocationActions(request: google.cloud.dataform.v1.IQueryWorkflowInvocationActionsRequest): Promise<google.cloud.dataform.v1.QueryWorkflowInvocationActionsResponse>;

Calls QueryWorkflowInvocationActions.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IQueryWorkflowInvocationActionsRequest](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/dataform/protos.google.cloud.dataform.v1.iqueryworkflowinvocationactionsrequest)`   
QueryWorkflowInvocationActionsRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.dataform.v1.QueryWorkflowInvocationActionsResponse](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/dataform/protos.google.cloud.dataform.v1.queryworkflowinvocationactionsresponse)>` | Promise  
  
### readFile(request, callback)
    
    
    public readFile(request: google.cloud.dataform.v1.IReadFileRequest, callback: google.cloud.dataform.v1.Dataform.ReadFileCallback): void;

Calls ReadFile.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IReadFileRequest](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/dataform/protos.google.cloud.dataform.v1.ireadfilerequest)`   
ReadFileRequest message or plain object  
`callback` |  `[ReadFileCallback](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/overview.html)`   
Node-style callback called with the error, if any, and ReadFileResponse  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### readFile(request)
    
    
    public readFile(request: google.cloud.dataform.v1.IReadFileRequest): Promise<google.cloud.dataform.v1.ReadFileResponse>;

Calls ReadFile.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IReadFileRequest](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/dataform/protos.google.cloud.dataform.v1.ireadfilerequest)`   
ReadFileRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.dataform.v1.ReadFileResponse](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/dataform/protos.google.cloud.dataform.v1.readfileresponse)>` | Promise  
  
### readRepositoryFile(request, callback)
    
    
    public readRepositoryFile(request: google.cloud.dataform.v1.IReadRepositoryFileRequest, callback: google.cloud.dataform.v1.Dataform.ReadRepositoryFileCallback): void;

Calls ReadRepositoryFile.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IReadRepositoryFileRequest](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/dataform/protos.google.cloud.dataform.v1.ireadrepositoryfilerequest)`   
ReadRepositoryFileRequest message or plain object  
`callback` |  `[ReadRepositoryFileCallback](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/overview.html)`   
Node-style callback called with the error, if any, and ReadRepositoryFileResponse  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### readRepositoryFile(request)
    
    
    public readRepositoryFile(request: google.cloud.dataform.v1.IReadRepositoryFileRequest): Promise<google.cloud.dataform.v1.ReadRepositoryFileResponse>;

Calls ReadRepositoryFile.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IReadRepositoryFileRequest](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/dataform/protos.google.cloud.dataform.v1.ireadrepositoryfilerequest)`   
ReadRepositoryFileRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.dataform.v1.ReadRepositoryFileResponse](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/dataform/protos.google.cloud.dataform.v1.readrepositoryfileresponse)>` | Promise  
  
### removeDirectory(request, callback)
    
    
    public removeDirectory(request: google.cloud.dataform.v1.IRemoveDirectoryRequest, callback: google.cloud.dataform.v1.Dataform.RemoveDirectoryCallback): void;

Calls RemoveDirectory.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IRemoveDirectoryRequest](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/dataform/protos.google.cloud.dataform.v1.iremovedirectoryrequest)`   
RemoveDirectoryRequest message or plain object  
`callback` |  `[RemoveDirectoryCallback](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/overview.html)`   
Node-style callback called with the error, if any, and RemoveDirectoryResponse  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### removeDirectory(request)
    
    
    public removeDirectory(request: google.cloud.dataform.v1.IRemoveDirectoryRequest): Promise<google.cloud.dataform.v1.RemoveDirectoryResponse>;

Calls RemoveDirectory.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IRemoveDirectoryRequest](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/dataform/protos.google.cloud.dataform.v1.iremovedirectoryrequest)`   
RemoveDirectoryRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.dataform.v1.RemoveDirectoryResponse](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/dataform/protos.google.cloud.dataform.v1.removedirectoryresponse)>` | Promise  
  
### removeFile(request, callback)
    
    
    public removeFile(request: google.cloud.dataform.v1.IRemoveFileRequest, callback: google.cloud.dataform.v1.Dataform.RemoveFileCallback): void;

Calls RemoveFile.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IRemoveFileRequest](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/dataform/protos.google.cloud.dataform.v1.iremovefilerequest)`   
RemoveFileRequest message or plain object  
`callback` |  `[RemoveFileCallback](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/overview.html)`   
Node-style callback called with the error, if any, and RemoveFileResponse  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### removeFile(request)
    
    
    public removeFile(request: google.cloud.dataform.v1.IRemoveFileRequest): Promise<google.cloud.dataform.v1.RemoveFileResponse>;

Calls RemoveFile.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IRemoveFileRequest](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/dataform/protos.google.cloud.dataform.v1.iremovefilerequest)`   
RemoveFileRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.dataform.v1.RemoveFileResponse](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/dataform/protos.google.cloud.dataform.v1.removefileresponse)>` | Promise  
  
### resetWorkspaceChanges(request, callback)
    
    
    public resetWorkspaceChanges(request: google.cloud.dataform.v1.IResetWorkspaceChangesRequest, callback: google.cloud.dataform.v1.Dataform.ResetWorkspaceChangesCallback): void;

Calls ResetWorkspaceChanges.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IResetWorkspaceChangesRequest](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/dataform/protos.google.cloud.dataform.v1.iresetworkspacechangesrequest)`   
ResetWorkspaceChangesRequest message or plain object  
`callback` |  `[ResetWorkspaceChangesCallback](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/overview.html)`   
Node-style callback called with the error, if any, and ResetWorkspaceChangesResponse  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### resetWorkspaceChanges(request)
    
    
    public resetWorkspaceChanges(request: google.cloud.dataform.v1.IResetWorkspaceChangesRequest): Promise<google.cloud.dataform.v1.ResetWorkspaceChangesResponse>;

Calls ResetWorkspaceChanges.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IResetWorkspaceChangesRequest](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/dataform/protos.google.cloud.dataform.v1.iresetworkspacechangesrequest)`   
ResetWorkspaceChangesRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.dataform.v1.ResetWorkspaceChangesResponse](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/dataform/protos.google.cloud.dataform.v1.resetworkspacechangesresponse)>` | Promise  
  
### searchFiles(request, callback)
    
    
    public searchFiles(request: google.cloud.dataform.v1.ISearchFilesRequest, callback: google.cloud.dataform.v1.Dataform.SearchFilesCallback): void;

Calls SearchFiles.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[ISearchFilesRequest](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/dataform/protos.google.cloud.dataform.v1.isearchfilesrequest)`   
SearchFilesRequest message or plain object  
`callback` |  `[SearchFilesCallback](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/overview.html)`   
Node-style callback called with the error, if any, and SearchFilesResponse  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### searchFiles(request)
    
    
    public searchFiles(request: google.cloud.dataform.v1.ISearchFilesRequest): Promise<google.cloud.dataform.v1.SearchFilesResponse>;

Calls SearchFiles.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[ISearchFilesRequest](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/dataform/protos.google.cloud.dataform.v1.isearchfilesrequest)`   
SearchFilesRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.dataform.v1.SearchFilesResponse](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/dataform/protos.google.cloud.dataform.v1.searchfilesresponse)>` | Promise  
  
### searchTeamFolders(request, callback)
    
    
    public searchTeamFolders(request: google.cloud.dataform.v1.ISearchTeamFoldersRequest, callback: google.cloud.dataform.v1.Dataform.SearchTeamFoldersCallback): void;

Calls SearchTeamFolders.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[ISearchTeamFoldersRequest](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/dataform/protos.google.cloud.dataform.v1.isearchteamfoldersrequest)`   
SearchTeamFoldersRequest message or plain object  
`callback` |  `[SearchTeamFoldersCallback](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/overview.html)`   
Node-style callback called with the error, if any, and SearchTeamFoldersResponse  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### searchTeamFolders(request)
    
    
    public searchTeamFolders(request: google.cloud.dataform.v1.ISearchTeamFoldersRequest): Promise<google.cloud.dataform.v1.SearchTeamFoldersResponse>;

Calls SearchTeamFolders.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[ISearchTeamFoldersRequest](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/dataform/protos.google.cloud.dataform.v1.isearchteamfoldersrequest)`   
SearchTeamFoldersRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.dataform.v1.SearchTeamFoldersResponse](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/dataform/protos.google.cloud.dataform.v1.searchteamfoldersresponse-class)>` | Promise  
  
### setIamPolicy(request, callback)
    
    
    public setIamPolicy(request: google.iam.v1.ISetIamPolicyRequest, callback: google.cloud.dataform.v1.Dataform.SetIamPolicyCallback): void;

Calls SetIamPolicy.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[ISetIamPolicyRequest](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/dataform/protos.google.iam.v1.isetiampolicyrequest)`   
SetIamPolicyRequest message or plain object  
`callback` |  `[SetIamPolicyCallback](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/overview.html)`   
Node-style callback called with the error, if any, and Policy  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### setIamPolicy(request)
    
    
    public setIamPolicy(request: google.iam.v1.ISetIamPolicyRequest): Promise<google.iam.v1.Policy>;

Calls SetIamPolicy.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[ISetIamPolicyRequest](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/dataform/protos.google.iam.v1.isetiampolicyrequest)`   
SetIamPolicyRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.iam.v1.Policy](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/dataform/protos.google.iam.v1.policy)>` | Promise  
  
### testIamPermissions(request, callback)
    
    
    public testIamPermissions(request: google.iam.v1.ITestIamPermissionsRequest, callback: google.cloud.dataform.v1.Dataform.TestIamPermissionsCallback): void;

Calls TestIamPermissions.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[ITestIamPermissionsRequest](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/dataform/protos.google.iam.v1.itestiampermissionsrequest)`   
TestIamPermissionsRequest message or plain object  
`callback` |  `[TestIamPermissionsCallback](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/overview.html)`   
Node-style callback called with the error, if any, and TestIamPermissionsResponse  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### testIamPermissions(request)
    
    
    public testIamPermissions(request: google.iam.v1.ITestIamPermissionsRequest): Promise<google.iam.v1.TestIamPermissionsResponse>;

Calls TestIamPermissions.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[ITestIamPermissionsRequest](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/dataform/protos.google.iam.v1.itestiampermissionsrequest)`   
TestIamPermissionsRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.iam.v1.TestIamPermissionsResponse](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/dataform/protos.google.iam.v1.testiampermissionsresponse)>` | Promise  
  
### updateConfig(request, callback)
    
    
    public updateConfig(request: google.cloud.dataform.v1.IUpdateConfigRequest, callback: google.cloud.dataform.v1.Dataform.UpdateConfigCallback): void;

Calls UpdateConfig.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IUpdateConfigRequest](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/dataform/protos.google.cloud.dataform.v1.iupdateconfigrequest)`   
UpdateConfigRequest message or plain object  
`callback` |  `[UpdateConfigCallback](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/overview.html)`   
Node-style callback called with the error, if any, and Config  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### updateConfig(request)
    
    
    public updateConfig(request: google.cloud.dataform.v1.IUpdateConfigRequest): Promise<google.cloud.dataform.v1.Config>;

Calls UpdateConfig.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IUpdateConfigRequest](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/dataform/protos.google.cloud.dataform.v1.iupdateconfigrequest)`   
UpdateConfigRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.dataform.v1.Config](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/dataform/protos.google.cloud.dataform.v1.config)>` | Promise  
  
### updateFolder(request, callback)
    
    
    public updateFolder(request: google.cloud.dataform.v1.IUpdateFolderRequest, callback: google.cloud.dataform.v1.Dataform.UpdateFolderCallback): void;

Calls UpdateFolder.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IUpdateFolderRequest](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/dataform/protos.google.cloud.dataform.v1.iupdatefolderrequest)`   
UpdateFolderRequest message or plain object  
`callback` |  `[UpdateFolderCallback](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/overview.html)`   
Node-style callback called with the error, if any, and Folder  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### updateFolder(request)
    
    
    public updateFolder(request: google.cloud.dataform.v1.IUpdateFolderRequest): Promise<google.cloud.dataform.v1.Folder>;

Calls UpdateFolder.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IUpdateFolderRequest](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/dataform/protos.google.cloud.dataform.v1.iupdatefolderrequest)`   
UpdateFolderRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.dataform.v1.Folder](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/dataform/protos.google.cloud.dataform.v1.folder)>` | Promise  
  
### updateReleaseConfig(request, callback)
    
    
    public updateReleaseConfig(request: google.cloud.dataform.v1.IUpdateReleaseConfigRequest, callback: google.cloud.dataform.v1.Dataform.UpdateReleaseConfigCallback): void;

Calls UpdateReleaseConfig.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IUpdateReleaseConfigRequest](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/dataform/protos.google.cloud.dataform.v1.iupdatereleaseconfigrequest)`   
UpdateReleaseConfigRequest message or plain object  
`callback` |  `[UpdateReleaseConfigCallback](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/overview.html)`   
Node-style callback called with the error, if any, and ReleaseConfig  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### updateReleaseConfig(request)
    
    
    public updateReleaseConfig(request: google.cloud.dataform.v1.IUpdateReleaseConfigRequest): Promise<google.cloud.dataform.v1.ReleaseConfig>;

Calls UpdateReleaseConfig.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IUpdateReleaseConfigRequest](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/dataform/protos.google.cloud.dataform.v1.iupdatereleaseconfigrequest)`   
UpdateReleaseConfigRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.dataform.v1.ReleaseConfig](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/dataform/protos.google.cloud.dataform.v1.releaseconfig-class)>` | Promise  
  
### updateRepository(request, callback)
    
    
    public updateRepository(request: google.cloud.dataform.v1.IUpdateRepositoryRequest, callback: google.cloud.dataform.v1.Dataform.UpdateRepositoryCallback): void;

Calls UpdateRepository.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IUpdateRepositoryRequest](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/dataform/protos.google.cloud.dataform.v1.iupdaterepositoryrequest)`   
UpdateRepositoryRequest message or plain object  
`callback` |  `[UpdateRepositoryCallback](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/overview.html)`   
Node-style callback called with the error, if any, and Repository  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### updateRepository(request)
    
    
    public updateRepository(request: google.cloud.dataform.v1.IUpdateRepositoryRequest): Promise<google.cloud.dataform.v1.Repository>;

Calls UpdateRepository.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IUpdateRepositoryRequest](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/dataform/protos.google.cloud.dataform.v1.iupdaterepositoryrequest)`   
UpdateRepositoryRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.dataform.v1.Repository](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/dataform/protos.google.cloud.dataform.v1.repository-class)>` | Promise  
  
### updateTeamFolder(request, callback)
    
    
    public updateTeamFolder(request: google.cloud.dataform.v1.IUpdateTeamFolderRequest, callback: google.cloud.dataform.v1.Dataform.UpdateTeamFolderCallback): void;

Calls UpdateTeamFolder.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IUpdateTeamFolderRequest](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/dataform/protos.google.cloud.dataform.v1.iupdateteamfolderrequest)`   
UpdateTeamFolderRequest message or plain object  
`callback` |  `[UpdateTeamFolderCallback](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/overview.html)`   
Node-style callback called with the error, if any, and TeamFolder  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### updateTeamFolder(request)
    
    
    public updateTeamFolder(request: google.cloud.dataform.v1.IUpdateTeamFolderRequest): Promise<google.cloud.dataform.v1.TeamFolder>;

Calls UpdateTeamFolder.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IUpdateTeamFolderRequest](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/dataform/protos.google.cloud.dataform.v1.iupdateteamfolderrequest)`   
UpdateTeamFolderRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.dataform.v1.TeamFolder](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/dataform/protos.google.cloud.dataform.v1.teamfolder)>` | Promise  
  
### updateWorkflowConfig(request, callback)
    
    
    public updateWorkflowConfig(request: google.cloud.dataform.v1.IUpdateWorkflowConfigRequest, callback: google.cloud.dataform.v1.Dataform.UpdateWorkflowConfigCallback): void;

Calls UpdateWorkflowConfig.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IUpdateWorkflowConfigRequest](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/dataform/protos.google.cloud.dataform.v1.iupdateworkflowconfigrequest)`   
UpdateWorkflowConfigRequest message or plain object  
`callback` |  `[UpdateWorkflowConfigCallback](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/overview.html)`   
Node-style callback called with the error, if any, and WorkflowConfig  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### updateWorkflowConfig(request)
    
    
    public updateWorkflowConfig(request: google.cloud.dataform.v1.IUpdateWorkflowConfigRequest): Promise<google.cloud.dataform.v1.WorkflowConfig>;

Calls UpdateWorkflowConfig.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IUpdateWorkflowConfigRequest](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/dataform/protos.google.cloud.dataform.v1.iupdateworkflowconfigrequest)`   
UpdateWorkflowConfigRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.dataform.v1.WorkflowConfig](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/dataform/protos.google.cloud.dataform.v1.workflowconfig-class)>` | Promise  
  
### writeFile(request, callback)
    
    
    public writeFile(request: google.cloud.dataform.v1.IWriteFileRequest, callback: google.cloud.dataform.v1.Dataform.WriteFileCallback): void;

Calls WriteFile.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IWriteFileRequest](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/dataform/protos.google.cloud.dataform.v1.iwritefilerequest)`   
WriteFileRequest message or plain object  
`callback` |  `[WriteFileCallback](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/overview.html)`   
Node-style callback called with the error, if any, and WriteFileResponse  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### writeFile(request)
    
    
    public writeFile(request: google.cloud.dataform.v1.IWriteFileRequest): Promise<google.cloud.dataform.v1.WriteFileResponse>;

Calls WriteFile.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IWriteFileRequest](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/dataform/protos.google.cloud.dataform.v1.iwritefilerequest)`   
WriteFileRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.dataform.v1.WriteFileResponse](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/dataform/protos.google.cloud.dataform.v1.writefileresponse)>` | Promise  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-03 UTC."],[],[]] 
