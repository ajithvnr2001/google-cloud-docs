---
url: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Memorystore.V1Beta/latest/Google.Cloud.Memorystore.V1Beta.Memorystore.MemorystoreBase
title: Memorystore v1beta API - Class Memorystore.MemorystoreBase (1.0.0-beta07) \u00a0|\u00a0 .NET client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T15:05:46.541454+00:00
---

# Memorystore v1beta API - Class Memorystore.MemorystoreBase (1.0.0-beta07)  |  .NET client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Memorystore.V1Beta/latest/Google.Cloud.Memorystore.V1Beta.Memorystore.MemorystoreBase

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ .NET ](https://docs.cloud.google.com/dotnet/docs)
  * [ Client libraries ](https://docs.cloud.google.com/dotnet/docs/reference)



Send feedback 

#  Memorystore v1beta API - Class Memorystore.MemorystoreBase (1.0.0-beta07) Stay organized with collections  Save and categorize content based on your preferences. 

1.0.0-beta07 (latest)  1.0.0-beta06 
    
    
    [BindServiceMethod(typeof(Memorystore), "BindService")]
    public abstract class Memorystore.MemorystoreBase

Reference documentation and code samples for the Memorystore v1beta API class Memorystore.MemorystoreBase.

Base class for server-side implementations of Memorystore

## Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object) > Memorystore.MemorystoreBase

## Inherited Members

[object.GetHashCode()](https://learn.microsoft.com/dotnet/api/system.object.gethashcode)

[object.GetType()](https://learn.microsoft.com/dotnet/api/system.object.gettype)

[object.MemberwiseClone()](https://learn.microsoft.com/dotnet/api/system.object.memberwiseclone)

[object.ToString()](https://learn.microsoft.com/dotnet/api/system.object.tostring)

## Namespace

[Google.Cloud.Memorystore.V1Beta](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Memorystore.V1Beta/latest/Google.Cloud.Memorystore.V1Beta)

## Assembly

Google.Cloud.Memorystore.V1Beta.dll

## Methods 

### AddAuthToken(AddAuthTokenRequest, ServerCallContext)
    
    
    public virtual Task<Operation> AddAuthToken(AddAuthTokenRequest request, ServerCallContext context)

Adds a token for a user of a token based auth enabled instance.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[AddAuthTokenRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Memorystore.V1Beta/latest/Google.Cloud.Memorystore.V1Beta.AddAuthTokenRequest)`  
The request received from the client.  
`context` | `[ServerCallContext](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.ServerCallContext.html)`  
The context of the server-side call handler being invoked.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation.html)` | The response to send back to the client (wrapped by a task).  
  
### AddTokenAuthUser(AddTokenAuthUserRequest, ServerCallContext)
    
    
    public virtual Task<Operation> AddTokenAuthUser(AddTokenAuthUserRequest request, ServerCallContext context)

Adds a token auth user for a token based auth enabled instance.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[AddTokenAuthUserRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Memorystore.V1Beta/latest/Google.Cloud.Memorystore.V1Beta.AddTokenAuthUserRequest)`  
The request received from the client.  
`context` | `[ServerCallContext](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.ServerCallContext.html)`  
The context of the server-side call handler being invoked.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation.html)` | The response to send back to the client (wrapped by a task).  
  
### BackupInstance(BackupInstanceRequest, ServerCallContext)
    
    
    public virtual Task<Operation> BackupInstance(BackupInstanceRequest request, ServerCallContext context)

Backup Instance. If this is the first time a backup is being created, a backup collection will be created at the backend, and this backup belongs to this collection. Both collection and backup will have a resource name. Backup will be executed for each shard. A replica (primary if nonHA) will be selected to perform the execution. Backup call will be rejected if there is an ongoing backup or update operation. Be aware that during preview, if the instance's internal software version is too old, critical update will be performed before actual backup. Once the internal software version is updated to the minimum version required by the backup feature, subsequent backups will not require critical update. After preview, there will be no critical update needed for backup.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[BackupInstanceRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Memorystore.V1Beta/latest/Google.Cloud.Memorystore.V1Beta.BackupInstanceRequest)`  
The request received from the client.  
`context` | `[ServerCallContext](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.ServerCallContext.html)`  
The context of the server-side call handler being invoked.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation.html)` | The response to send back to the client (wrapped by a task).  
  
### CreateAclPolicy(CreateAclPolicyRequest, ServerCallContext)
    
    
    public virtual Task<AclPolicy> CreateAclPolicy(CreateAclPolicyRequest request, ServerCallContext context)

Creates an ACL policy. The creation is executed synchronously and the policy is available for use immediately after the RPC returns.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[CreateAclPolicyRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Memorystore.V1Beta/latest/Google.Cloud.Memorystore.V1Beta.CreateAclPolicyRequest)`  
The request received from the client.  
`context` | `[ServerCallContext](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.ServerCallContext.html)`  
The context of the server-side call handler being invoked.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[AclPolicy](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Memorystore.V1Beta/latest/Google.Cloud.Memorystore.V1Beta.AclPolicy)` | The response to send back to the client (wrapped by a task).  
  
### CreateInstance(CreateInstanceRequest, ServerCallContext)
    
    
    public virtual Task<Operation> CreateInstance(CreateInstanceRequest request, ServerCallContext context)

Creates a new Instance in a given project and location.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[CreateInstanceRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Memorystore.V1Beta/latest/Google.Cloud.Memorystore.V1Beta.CreateInstanceRequest)`  
The request received from the client.  
`context` | `[ServerCallContext](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.ServerCallContext.html)`  
The context of the server-side call handler being invoked.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation.html)` | The response to send back to the client (wrapped by a task).  
  
### DeleteAclPolicy(DeleteAclPolicyRequest, ServerCallContext)
    
    
    public virtual Task<Operation> DeleteAclPolicy(DeleteAclPolicyRequest request, ServerCallContext context)

Deletes a specific ACL policy. This action will delete the ACL policy and all the rules associated with it. An ACL policy cannot be deleted if it is attached to an instance.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[DeleteAclPolicyRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Memorystore.V1Beta/latest/Google.Cloud.Memorystore.V1Beta.DeleteAclPolicyRequest)`  
The request received from the client.  
`context` | `[ServerCallContext](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.ServerCallContext.html)`  
The context of the server-side call handler being invoked.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation.html)` | The response to send back to the client (wrapped by a task).  
  
### DeleteAuthToken(DeleteAuthTokenRequest, ServerCallContext)
    
    
    public virtual Task<Operation> DeleteAuthToken(DeleteAuthTokenRequest request, ServerCallContext context)

Deletes a token for a user of a token based auth enabled instance.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[DeleteAuthTokenRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Memorystore.V1Beta/latest/Google.Cloud.Memorystore.V1Beta.DeleteAuthTokenRequest)`  
The request received from the client.  
`context` | `[ServerCallContext](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.ServerCallContext.html)`  
The context of the server-side call handler being invoked.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation.html)` | The response to send back to the client (wrapped by a task).  
  
### DeleteBackup(DeleteBackupRequest, ServerCallContext)
    
    
    public virtual Task<Operation> DeleteBackup(DeleteBackupRequest request, ServerCallContext context)

Deletes a specific backup.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[DeleteBackupRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Memorystore.V1Beta/latest/Google.Cloud.Memorystore.V1Beta.DeleteBackupRequest)`  
The request received from the client.  
`context` | `[ServerCallContext](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.ServerCallContext.html)`  
The context of the server-side call handler being invoked.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation.html)` | The response to send back to the client (wrapped by a task).  
  
### DeleteInstance(DeleteInstanceRequest, ServerCallContext)
    
    
    public virtual Task<Operation> DeleteInstance(DeleteInstanceRequest request, ServerCallContext context)

Deletes a single Instance.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[DeleteInstanceRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Memorystore.V1Beta/latest/Google.Cloud.Memorystore.V1Beta.DeleteInstanceRequest)`  
The request received from the client.  
`context` | `[ServerCallContext](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.ServerCallContext.html)`  
The context of the server-side call handler being invoked.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation.html)` | The response to send back to the client (wrapped by a task).  
  
### DeleteTokenAuthUser(DeleteTokenAuthUserRequest, ServerCallContext)
    
    
    public virtual Task<Operation> DeleteTokenAuthUser(DeleteTokenAuthUserRequest request, ServerCallContext context)

Deletes a token auth user for a token based auth enabled instance.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[DeleteTokenAuthUserRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Memorystore.V1Beta/latest/Google.Cloud.Memorystore.V1Beta.DeleteTokenAuthUserRequest)`  
The request received from the client.  
`context` | `[ServerCallContext](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.ServerCallContext.html)`  
The context of the server-side call handler being invoked.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation.html)` | The response to send back to the client (wrapped by a task).  
  
### ExportBackup(ExportBackupRequest, ServerCallContext)
    
    
    public virtual Task<Operation> ExportBackup(ExportBackupRequest request, ServerCallContext context)

Exports a specific backup to a customer target Cloud Storage URI.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ExportBackupRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Memorystore.V1Beta/latest/Google.Cloud.Memorystore.V1Beta.ExportBackupRequest)`  
The request received from the client.  
`context` | `[ServerCallContext](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.ServerCallContext.html)`  
The context of the server-side call handler being invoked.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation.html)` | The response to send back to the client (wrapped by a task).  
  
### FinishMigration(FinishMigrationRequest, ServerCallContext)
    
    
    public virtual Task<Operation> FinishMigration(FinishMigrationRequest request, ServerCallContext context)

Finalizes the migration process.

After the successful completion of this operation, the target instance will:

  1. Stop replicating from the source instance.
  2. Allow both reads and writes.



**Parameters**  
---  
**Name** | **Description**  
`request` | `[FinishMigrationRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Memorystore.V1Beta/latest/Google.Cloud.Memorystore.V1Beta.FinishMigrationRequest)`  
The request received from the client.  
`context` | `[ServerCallContext](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.ServerCallContext.html)`  
The context of the server-side call handler being invoked.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation.html)` | The response to send back to the client (wrapped by a task).  
  
### GetAclPolicy(GetAclPolicyRequest, ServerCallContext)
    
    
    public virtual Task<AclPolicy> GetAclPolicy(GetAclPolicyRequest request, ServerCallContext context)

Gets the details of a specific Memorystore ACL policy.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetAclPolicyRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Memorystore.V1Beta/latest/Google.Cloud.Memorystore.V1Beta.GetAclPolicyRequest)`  
The request received from the client.  
`context` | `[ServerCallContext](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.ServerCallContext.html)`  
The context of the server-side call handler being invoked.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[AclPolicy](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Memorystore.V1Beta/latest/Google.Cloud.Memorystore.V1Beta.AclPolicy)` | The response to send back to the client (wrapped by a task).  
  
### GetAclPolicyRevision(GetAclPolicyRevisionRequest, ServerCallContext)
    
    
    public virtual Task<AclPolicyRevision> GetAclPolicyRevision(GetAclPolicyRevisionRequest request, ServerCallContext context)

Gets details of a specific ACL policy revision.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetAclPolicyRevisionRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Memorystore.V1Beta/latest/Google.Cloud.Memorystore.V1Beta.GetAclPolicyRevisionRequest)`  
The request received from the client.  
`context` | `[ServerCallContext](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.ServerCallContext.html)`  
The context of the server-side call handler being invoked.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[AclPolicyRevision](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Memorystore.V1Beta/latest/Google.Cloud.Memorystore.V1Beta.AclPolicyRevision)` | The response to send back to the client (wrapped by a task).  
  
### GetAuthToken(GetAuthTokenRequest, ServerCallContext)
    
    
    public virtual Task<AuthToken> GetAuthToken(GetAuthTokenRequest request, ServerCallContext context)

Gets a token based auth enabled instance's auth token for a given user.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetAuthTokenRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Memorystore.V1Beta/latest/Google.Cloud.Memorystore.V1Beta.GetAuthTokenRequest)`  
The request received from the client.  
`context` | `[ServerCallContext](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.ServerCallContext.html)`  
The context of the server-side call handler being invoked.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[AuthToken](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Memorystore.V1Beta/latest/Google.Cloud.Memorystore.V1Beta.AuthToken)` | The response to send back to the client (wrapped by a task).  
  
### GetBackup(GetBackupRequest, ServerCallContext)
    
    
    public virtual Task<Backup> GetBackup(GetBackupRequest request, ServerCallContext context)

Gets the details of a specific backup.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetBackupRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Memorystore.V1Beta/latest/Google.Cloud.Memorystore.V1Beta.GetBackupRequest)`  
The request received from the client.  
`context` | `[ServerCallContext](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.ServerCallContext.html)`  
The context of the server-side call handler being invoked.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Backup](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Memorystore.V1Beta/latest/Google.Cloud.Memorystore.V1Beta.Backup)` | The response to send back to the client (wrapped by a task).  
  
### GetBackupCollection(GetBackupCollectionRequest, ServerCallContext)
    
    
    public virtual Task<BackupCollection> GetBackupCollection(GetBackupCollectionRequest request, ServerCallContext context)

Get a backup collection.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetBackupCollectionRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Memorystore.V1Beta/latest/Google.Cloud.Memorystore.V1Beta.GetBackupCollectionRequest)`  
The request received from the client.  
`context` | `[ServerCallContext](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.ServerCallContext.html)`  
The context of the server-side call handler being invoked.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[BackupCollection](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Memorystore.V1Beta/latest/Google.Cloud.Memorystore.V1Beta.BackupCollection)` | The response to send back to the client (wrapped by a task).  
  
### GetCertificateAuthority(GetCertificateAuthorityRequest, ServerCallContext)
    
    
    public virtual Task<CertificateAuthority> GetCertificateAuthority(GetCertificateAuthorityRequest request, ServerCallContext context)

Gets details about the certificate authority for an Instance.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetCertificateAuthorityRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Memorystore.V1Beta/latest/Google.Cloud.Memorystore.V1Beta.GetCertificateAuthorityRequest)`  
The request received from the client.  
`context` | `[ServerCallContext](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.ServerCallContext.html)`  
The context of the server-side call handler being invoked.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[CertificateAuthority](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Memorystore.V1Beta/latest/Google.Cloud.Memorystore.V1Beta.CertificateAuthority)` | The response to send back to the client (wrapped by a task).  
  
### GetInstance(GetInstanceRequest, ServerCallContext)
    
    
    public virtual Task<Instance> GetInstance(GetInstanceRequest request, ServerCallContext context)

Gets details of a single Instance.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetInstanceRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Memorystore.V1Beta/latest/Google.Cloud.Memorystore.V1Beta.GetInstanceRequest)`  
The request received from the client.  
`context` | `[ServerCallContext](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.ServerCallContext.html)`  
The context of the server-side call handler being invoked.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Instance](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Memorystore.V1Beta/latest/Google.Cloud.Memorystore.V1Beta.Instance)` | The response to send back to the client (wrapped by a task).  
  
### GetSharedRegionalCertificateAuthority(GetSharedRegionalCertificateAuthorityRequest, ServerCallContext)
    
    
    public virtual Task<SharedRegionalCertificateAuthority> GetSharedRegionalCertificateAuthority(GetSharedRegionalCertificateAuthorityRequest request, ServerCallContext context)

Gets the details of shared regional certificate authority information for Memorystore instance.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetSharedRegionalCertificateAuthorityRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Memorystore.V1Beta/latest/Google.Cloud.Memorystore.V1Beta.GetSharedRegionalCertificateAuthorityRequest)`  
The request received from the client.  
`context` | `[ServerCallContext](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.ServerCallContext.html)`  
The context of the server-side call handler being invoked.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[SharedRegionalCertificateAuthority](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Memorystore.V1Beta/latest/Google.Cloud.Memorystore.V1Beta.SharedRegionalCertificateAuthority)` | The response to send back to the client (wrapped by a task).  
  
### GetTokenAuthUser(GetTokenAuthUserRequest, ServerCallContext)
    
    
    public virtual Task<TokenAuthUser> GetTokenAuthUser(GetTokenAuthUserRequest request, ServerCallContext context)

Gets a specific token auth user for a token based auth enabled instance.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetTokenAuthUserRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Memorystore.V1Beta/latest/Google.Cloud.Memorystore.V1Beta.GetTokenAuthUserRequest)`  
The request received from the client.  
`context` | `[ServerCallContext](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.ServerCallContext.html)`  
The context of the server-side call handler being invoked.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[TokenAuthUser](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Memorystore.V1Beta/latest/Google.Cloud.Memorystore.V1Beta.TokenAuthUser)` | The response to send back to the client (wrapped by a task).  
  
### ListAclPolicies(ListAclPoliciesRequest, ServerCallContext)
    
    
    public virtual Task<ListAclPoliciesResponse> ListAclPolicies(ListAclPoliciesRequest request, ServerCallContext context)

Lists all ACL policies owned by a project in either the specified location (region) or all locations.

The location should have the following format:

  * `projects/{project_id}/locations/{location_id}`



If `location_id` is specified as `-` (wildcard), then all regions available to the project are queried, and the results are aggregated.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ListAclPoliciesRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Memorystore.V1Beta/latest/Google.Cloud.Memorystore.V1Beta.ListAclPoliciesRequest)`  
The request received from the client.  
`context` | `[ServerCallContext](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.ServerCallContext.html)`  
The context of the server-side call handler being invoked.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[ListAclPoliciesResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Memorystore.V1Beta/latest/Google.Cloud.Memorystore.V1Beta.ListAclPoliciesResponse)` | The response to send back to the client (wrapped by a task).  
  
### ListAclPolicyRevisions(ListAclPolicyRevisionsRequest, ServerCallContext)
    
    
    public virtual Task<ListAclPolicyRevisionsResponse> ListAclPolicyRevisions(ListAclPolicyRevisionsRequest request, ServerCallContext context)

Lists all ACL policy revisions in a given ACL policy.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ListAclPolicyRevisionsRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Memorystore.V1Beta/latest/Google.Cloud.Memorystore.V1Beta.ListAclPolicyRevisionsRequest)`  
The request received from the client.  
`context` | `[ServerCallContext](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.ServerCallContext.html)`  
The context of the server-side call handler being invoked.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[ListAclPolicyRevisionsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Memorystore.V1Beta/latest/Google.Cloud.Memorystore.V1Beta.ListAclPolicyRevisionsResponse)` | The response to send back to the client (wrapped by a task).  
  
### ListAuthTokens(ListAuthTokensRequest, ServerCallContext)
    
    
    public virtual Task<ListAuthTokensResponse> ListAuthTokens(ListAuthTokensRequest request, ServerCallContext context)

Lists all the auth tokens for a specific token auth user.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ListAuthTokensRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Memorystore.V1Beta/latest/Google.Cloud.Memorystore.V1Beta.ListAuthTokensRequest)`  
The request received from the client.  
`context` | `[ServerCallContext](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.ServerCallContext.html)`  
The context of the server-side call handler being invoked.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[ListAuthTokensResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Memorystore.V1Beta/latest/Google.Cloud.Memorystore.V1Beta.ListAuthTokensResponse)` | The response to send back to the client (wrapped by a task).  
  
### ListBackupCollections(ListBackupCollectionsRequest, ServerCallContext)
    
    
    public virtual Task<ListBackupCollectionsResponse> ListBackupCollections(ListBackupCollectionsRequest request, ServerCallContext context)

Lists all backup collections owned by a consumer project in either the specified location (region) or all locations.

If `location_id` is specified as `-` (wildcard), then all regions available to the project are queried, and the results are aggregated.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ListBackupCollectionsRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Memorystore.V1Beta/latest/Google.Cloud.Memorystore.V1Beta.ListBackupCollectionsRequest)`  
The request received from the client.  
`context` | `[ServerCallContext](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.ServerCallContext.html)`  
The context of the server-side call handler being invoked.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[ListBackupCollectionsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Memorystore.V1Beta/latest/Google.Cloud.Memorystore.V1Beta.ListBackupCollectionsResponse)` | The response to send back to the client (wrapped by a task).  
  
### ListBackups(ListBackupsRequest, ServerCallContext)
    
    
    public virtual Task<ListBackupsResponse> ListBackups(ListBackupsRequest request, ServerCallContext context)

Lists all backups owned by a backup collection.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ListBackupsRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Memorystore.V1Beta/latest/Google.Cloud.Memorystore.V1Beta.ListBackupsRequest)`  
The request received from the client.  
`context` | `[ServerCallContext](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.ServerCallContext.html)`  
The context of the server-side call handler being invoked.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[ListBackupsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Memorystore.V1Beta/latest/Google.Cloud.Memorystore.V1Beta.ListBackupsResponse)` | The response to send back to the client (wrapped by a task).  
  
### ListInstances(ListInstancesRequest, ServerCallContext)
    
    
    public virtual Task<ListInstancesResponse> ListInstances(ListInstancesRequest request, ServerCallContext context)

Lists Instances in a given project and location.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ListInstancesRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Memorystore.V1Beta/latest/Google.Cloud.Memorystore.V1Beta.ListInstancesRequest)`  
The request received from the client.  
`context` | `[ServerCallContext](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.ServerCallContext.html)`  
The context of the server-side call handler being invoked.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[ListInstancesResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Memorystore.V1Beta/latest/Google.Cloud.Memorystore.V1Beta.ListInstancesResponse)` | The response to send back to the client (wrapped by a task).  
  
### ListTokenAuthUsers(ListTokenAuthUsersRequest, ServerCallContext)
    
    
    public virtual Task<ListTokenAuthUsersResponse> ListTokenAuthUsers(ListTokenAuthUsersRequest request, ServerCallContext context)

Lists all the token auth users for a token based auth enabled instance.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ListTokenAuthUsersRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Memorystore.V1Beta/latest/Google.Cloud.Memorystore.V1Beta.ListTokenAuthUsersRequest)`  
The request received from the client.  
`context` | `[ServerCallContext](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.ServerCallContext.html)`  
The context of the server-side call handler being invoked.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[ListTokenAuthUsersResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Memorystore.V1Beta/latest/Google.Cloud.Memorystore.V1Beta.ListTokenAuthUsersResponse)` | The response to send back to the client (wrapped by a task).  
  
### RescheduleMaintenance(RescheduleMaintenanceRequest, ServerCallContext)
    
    
    public virtual Task<Operation> RescheduleMaintenance(RescheduleMaintenanceRequest request, ServerCallContext context)

Reschedules upcoming maintenance event.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[RescheduleMaintenanceRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Memorystore.V1Beta/latest/Google.Cloud.Memorystore.V1Beta.RescheduleMaintenanceRequest)`  
The request received from the client.  
`context` | `[ServerCallContext](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.ServerCallContext.html)`  
The context of the server-side call handler being invoked.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation.html)` | The response to send back to the client (wrapped by a task).  
  
### StartMigration(StartMigrationRequest, ServerCallContext)
    
    
    public virtual Task<Operation> StartMigration(StartMigrationRequest request, ServerCallContext context)

Initiates the migration of a source instance to the target Memorystore instance.

After the successful completion of this operation, the target instance will:

  1. Set up replication with the source instance and replicate any writes to the source instance.
  2. Only allow reads.



**Parameters**  
---  
**Name** | **Description**  
`request` | `[StartMigrationRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Memorystore.V1Beta/latest/Google.Cloud.Memorystore.V1Beta.StartMigrationRequest)`  
The request received from the client.  
`context` | `[ServerCallContext](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.ServerCallContext.html)`  
The context of the server-side call handler being invoked.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation.html)` | The response to send back to the client (wrapped by a task).  
  
### UpdateAclPolicy(UpdateAclPolicyRequest, ServerCallContext)
    
    
    public virtual Task<Operation> UpdateAclPolicy(UpdateAclPolicyRequest request, ServerCallContext context)

Updates the ACL policy.

The operation will apply the updated ACL policy to all the linked instances. The operation will return success if it successfully applied the policy to all the instances. If the operation completed with a failure, the service will continue to apply the policy via reconciliation for the failed instances even after operation completion to ensure eventual consistency.

Completed longrunning.Operation will contain the new ACL policy object in the response field.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[UpdateAclPolicyRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Memorystore.V1Beta/latest/Google.Cloud.Memorystore.V1Beta.UpdateAclPolicyRequest)`  
The request received from the client.  
`context` | `[ServerCallContext](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.ServerCallContext.html)`  
The context of the server-side call handler being invoked.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation.html)` | The response to send back to the client (wrapped by a task).  
  
### UpdateInstance(UpdateInstanceRequest, ServerCallContext)
    
    
    public virtual Task<Operation> UpdateInstance(UpdateInstanceRequest request, ServerCallContext context)

Updates the parameters of a single Instance.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[UpdateInstanceRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Memorystore.V1Beta/latest/Google.Cloud.Memorystore.V1Beta.UpdateInstanceRequest)`  
The request received from the client.  
`context` | `[ServerCallContext](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.ServerCallContext.html)`  
The context of the server-side call handler being invoked.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation.html)` | The response to send back to the client (wrapped by a task).  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
