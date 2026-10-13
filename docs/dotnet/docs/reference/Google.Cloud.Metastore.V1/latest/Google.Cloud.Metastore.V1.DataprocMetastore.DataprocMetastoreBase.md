---
url: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Metastore.V1/latest/Google.Cloud.Metastore.V1.DataprocMetastore.DataprocMetastoreBase
title: Dataproc Metastore v1 API - Class DataprocMetastore.DataprocMetastoreBase (2.10.0) \u00a0|\u00a0 .NET client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T19:35:51.337898+00:00
---

# Dataproc Metastore v1 API - Class DataprocMetastore.DataprocMetastoreBase (2.10.0)  |  .NET client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Metastore.V1/latest/Google.Cloud.Metastore.V1.DataprocMetastore.DataprocMetastoreBase

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ .NET ](https://docs.cloud.google.com/dotnet/docs)
  * [ Client libraries ](https://docs.cloud.google.com/dotnet/docs/reference)



Send feedback 

#  Dataproc Metastore v1 API - Class DataprocMetastore.DataprocMetastoreBase (2.10.0) Stay organized with collections  Save and categorize content based on your preferences. 

Version latestkeyboard_arrow_down

  * [ 2.10.0 (latest) ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Metastore.V1/latest/Google.Cloud.Metastore.V1.DataprocMetastore.DataprocMetastoreBase)
  * [ 2.9.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Metastore.V1/2.9.0/Google.Cloud.Metastore.V1.DataprocMetastore.DataprocMetastoreBase)
  * [ 2.8.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Metastore.V1/2.8.0/Google.Cloud.Metastore.V1.DataprocMetastore.DataprocMetastoreBase)
  * [ 2.7.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Metastore.V1/2.7.0/Google.Cloud.Metastore.V1.DataprocMetastore.DataprocMetastoreBase)
  * [ 2.6.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Metastore.V1/2.6.0/Google.Cloud.Metastore.V1.DataprocMetastore.DataprocMetastoreBase)
  * [ 2.5.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Metastore.V1/2.5.0/Google.Cloud.Metastore.V1.DataprocMetastore.DataprocMetastoreBase)
  * [ 2.4.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Metastore.V1/2.4.0/Google.Cloud.Metastore.V1.DataprocMetastore.DataprocMetastoreBase)
  * [ 2.3.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Metastore.V1/2.3.0/Google.Cloud.Metastore.V1.DataprocMetastore.DataprocMetastoreBase)
  * [ 2.2.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Metastore.V1/2.2.0/Google.Cloud.Metastore.V1.DataprocMetastore.DataprocMetastoreBase)
  * [ 2.1.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Metastore.V1/2.1.0/Google.Cloud.Metastore.V1.DataprocMetastore.DataprocMetastoreBase)
  * [ 2.0.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Metastore.V1/2.0.0/Google.Cloud.Metastore.V1.DataprocMetastore.DataprocMetastoreBase)
  * [ 1.1.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Metastore.V1/1.1.0/Google.Cloud.Metastore.V1.DataprocMetastore.DataprocMetastoreBase)
  * [ 1.0.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Metastore.V1/1.0.0/Google.Cloud.Metastore.V1.DataprocMetastore.DataprocMetastoreBase)


    
    
    [BindServiceMethod(typeof(DataprocMetastore), "BindService")]
    public abstract class DataprocMetastore.DataprocMetastoreBase

Reference documentation and code samples for the Dataproc Metastore v1 API class DataprocMetastore.DataprocMetastoreBase.

Base class for server-side implementations of DataprocMetastore

## Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object) > DataprocMetastore.DataprocMetastoreBase

## Inherited Members

[object.GetHashCode()](https://learn.microsoft.com/dotnet/api/system.object.gethashcode)

[object.GetType()](https://learn.microsoft.com/dotnet/api/system.object.gettype)

[object.MemberwiseClone()](https://learn.microsoft.com/dotnet/api/system.object.memberwiseclone)

[object.ToString()](https://learn.microsoft.com/dotnet/api/system.object.tostring)

## Namespace

[Google.Cloud.Metastore.V1](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Metastore.V1/latest/Google.Cloud.Metastore.V1)

## Assembly

Google.Cloud.Metastore.V1.dll

## Methods 

### AlterMetadataResourceLocation(AlterMetadataResourceLocationRequest, ServerCallContext)
    
    
    public virtual Task<Operation> AlterMetadataResourceLocation(AlterMetadataResourceLocationRequest request, ServerCallContext context)

Alter metadata resource location. The metadata resource can be a database, table, or partition. This functionality only updates the parent directory for the respective metadata resource and does not transfer any existing data to the new location.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[AlterMetadataResourceLocationRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Metastore.V1/latest/Google.Cloud.Metastore.V1.AlterMetadataResourceLocationRequest)`  
The request received from the client.  
`context` | `[ServerCallContext](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.ServerCallContext.html)`  
The context of the server-side call handler being invoked.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation.html)` | The response to send back to the client (wrapped by a task).  
  
### CreateBackup(CreateBackupRequest, ServerCallContext)
    
    
    public virtual Task<Operation> CreateBackup(CreateBackupRequest request, ServerCallContext context)

Creates a new backup in a given project and location.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[CreateBackupRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Metastore.V1/latest/Google.Cloud.Metastore.V1.CreateBackupRequest)`  
The request received from the client.  
`context` | `[ServerCallContext](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.ServerCallContext.html)`  
The context of the server-side call handler being invoked.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation.html)` | The response to send back to the client (wrapped by a task).  
  
### CreateMetadataImport(CreateMetadataImportRequest, ServerCallContext)
    
    
    public virtual Task<Operation> CreateMetadataImport(CreateMetadataImportRequest request, ServerCallContext context)

Creates a new MetadataImport in a given project and location.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[CreateMetadataImportRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Metastore.V1/latest/Google.Cloud.Metastore.V1.CreateMetadataImportRequest)`  
The request received from the client.  
`context` | `[ServerCallContext](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.ServerCallContext.html)`  
The context of the server-side call handler being invoked.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation.html)` | The response to send back to the client (wrapped by a task).  
  
### CreateService(CreateServiceRequest, ServerCallContext)
    
    
    public virtual Task<Operation> CreateService(CreateServiceRequest request, ServerCallContext context)

Creates a metastore service in a project and location.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[CreateServiceRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Metastore.V1/latest/Google.Cloud.Metastore.V1.CreateServiceRequest)`  
The request received from the client.  
`context` | `[ServerCallContext](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.ServerCallContext.html)`  
The context of the server-side call handler being invoked.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation.html)` | The response to send back to the client (wrapped by a task).  
  
### DeleteBackup(DeleteBackupRequest, ServerCallContext)
    
    
    public virtual Task<Operation> DeleteBackup(DeleteBackupRequest request, ServerCallContext context)

Deletes a single backup.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[DeleteBackupRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Metastore.V1/latest/Google.Cloud.Metastore.V1.DeleteBackupRequest)`  
The request received from the client.  
`context` | `[ServerCallContext](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.ServerCallContext.html)`  
The context of the server-side call handler being invoked.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation.html)` | The response to send back to the client (wrapped by a task).  
  
### DeleteService(DeleteServiceRequest, ServerCallContext)
    
    
    public virtual Task<Operation> DeleteService(DeleteServiceRequest request, ServerCallContext context)

Deletes a single service.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[DeleteServiceRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Metastore.V1/latest/Google.Cloud.Metastore.V1.DeleteServiceRequest)`  
The request received from the client.  
`context` | `[ServerCallContext](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.ServerCallContext.html)`  
The context of the server-side call handler being invoked.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation.html)` | The response to send back to the client (wrapped by a task).  
  
### ExportMetadata(ExportMetadataRequest, ServerCallContext)
    
    
    public virtual Task<Operation> ExportMetadata(ExportMetadataRequest request, ServerCallContext context)

Exports metadata from a service.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ExportMetadataRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Metastore.V1/latest/Google.Cloud.Metastore.V1.ExportMetadataRequest)`  
The request received from the client.  
`context` | `[ServerCallContext](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.ServerCallContext.html)`  
The context of the server-side call handler being invoked.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation.html)` | The response to send back to the client (wrapped by a task).  
  
### GetBackup(GetBackupRequest, ServerCallContext)
    
    
    public virtual Task<Backup> GetBackup(GetBackupRequest request, ServerCallContext context)

Gets details of a single backup.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetBackupRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Metastore.V1/latest/Google.Cloud.Metastore.V1.GetBackupRequest)`  
The request received from the client.  
`context` | `[ServerCallContext](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.ServerCallContext.html)`  
The context of the server-side call handler being invoked.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Backup](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Metastore.V1/latest/Google.Cloud.Metastore.V1.Backup)` | The response to send back to the client (wrapped by a task).  
  
### GetMetadataImport(GetMetadataImportRequest, ServerCallContext)
    
    
    public virtual Task<MetadataImport> GetMetadataImport(GetMetadataImportRequest request, ServerCallContext context)

Gets details of a single import.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetMetadataImportRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Metastore.V1/latest/Google.Cloud.Metastore.V1.GetMetadataImportRequest)`  
The request received from the client.  
`context` | `[ServerCallContext](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.ServerCallContext.html)`  
The context of the server-side call handler being invoked.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[MetadataImport](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Metastore.V1/latest/Google.Cloud.Metastore.V1.MetadataImport)` | The response to send back to the client (wrapped by a task).  
  
### GetService(GetServiceRequest, ServerCallContext)
    
    
    public virtual Task<Service> GetService(GetServiceRequest request, ServerCallContext context)

Gets the details of a single service.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetServiceRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Metastore.V1/latest/Google.Cloud.Metastore.V1.GetServiceRequest)`  
The request received from the client.  
`context` | `[ServerCallContext](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.ServerCallContext.html)`  
The context of the server-side call handler being invoked.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Service](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Metastore.V1/latest/Google.Cloud.Metastore.V1.Service)` | The response to send back to the client (wrapped by a task).  
  
### ListBackups(ListBackupsRequest, ServerCallContext)
    
    
    public virtual Task<ListBackupsResponse> ListBackups(ListBackupsRequest request, ServerCallContext context)

Lists backups in a service.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ListBackupsRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Metastore.V1/latest/Google.Cloud.Metastore.V1.ListBackupsRequest)`  
The request received from the client.  
`context` | `[ServerCallContext](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.ServerCallContext.html)`  
The context of the server-side call handler being invoked.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[ListBackupsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Metastore.V1/latest/Google.Cloud.Metastore.V1.ListBackupsResponse)` | The response to send back to the client (wrapped by a task).  
  
### ListMetadataImports(ListMetadataImportsRequest, ServerCallContext)
    
    
    public virtual Task<ListMetadataImportsResponse> ListMetadataImports(ListMetadataImportsRequest request, ServerCallContext context)

Lists imports in a service.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ListMetadataImportsRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Metastore.V1/latest/Google.Cloud.Metastore.V1.ListMetadataImportsRequest)`  
The request received from the client.  
`context` | `[ServerCallContext](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.ServerCallContext.html)`  
The context of the server-side call handler being invoked.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[ListMetadataImportsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Metastore.V1/latest/Google.Cloud.Metastore.V1.ListMetadataImportsResponse)` | The response to send back to the client (wrapped by a task).  
  
### ListServices(ListServicesRequest, ServerCallContext)
    
    
    public virtual Task<ListServicesResponse> ListServices(ListServicesRequest request, ServerCallContext context)

Lists services in a project and location.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ListServicesRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Metastore.V1/latest/Google.Cloud.Metastore.V1.ListServicesRequest)`  
The request received from the client.  
`context` | `[ServerCallContext](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.ServerCallContext.html)`  
The context of the server-side call handler being invoked.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[ListServicesResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Metastore.V1/latest/Google.Cloud.Metastore.V1.ListServicesResponse)` | The response to send back to the client (wrapped by a task).  
  
### MoveTableToDatabase(MoveTableToDatabaseRequest, ServerCallContext)
    
    
    public virtual Task<Operation> MoveTableToDatabase(MoveTableToDatabaseRequest request, ServerCallContext context)

Move a table to another database.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[MoveTableToDatabaseRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Metastore.V1/latest/Google.Cloud.Metastore.V1.MoveTableToDatabaseRequest)`  
The request received from the client.  
`context` | `[ServerCallContext](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.ServerCallContext.html)`  
The context of the server-side call handler being invoked.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation.html)` | The response to send back to the client (wrapped by a task).  
  
### QueryMetadata(QueryMetadataRequest, ServerCallContext)
    
    
    public virtual Task<Operation> QueryMetadata(QueryMetadataRequest request, ServerCallContext context)

Query DPMS metadata.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[QueryMetadataRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Metastore.V1/latest/Google.Cloud.Metastore.V1.QueryMetadataRequest)`  
The request received from the client.  
`context` | `[ServerCallContext](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.ServerCallContext.html)`  
The context of the server-side call handler being invoked.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation.html)` | The response to send back to the client (wrapped by a task).  
  
### RestoreService(RestoreServiceRequest, ServerCallContext)
    
    
    public virtual Task<Operation> RestoreService(RestoreServiceRequest request, ServerCallContext context)

Restores a service from a backup.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[RestoreServiceRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Metastore.V1/latest/Google.Cloud.Metastore.V1.RestoreServiceRequest)`  
The request received from the client.  
`context` | `[ServerCallContext](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.ServerCallContext.html)`  
The context of the server-side call handler being invoked.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation.html)` | The response to send back to the client (wrapped by a task).  
  
### UpdateMetadataImport(UpdateMetadataImportRequest, ServerCallContext)
    
    
    public virtual Task<Operation> UpdateMetadataImport(UpdateMetadataImportRequest request, ServerCallContext context)

Updates a single import. Only the description field of MetadataImport is supported to be updated.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[UpdateMetadataImportRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Metastore.V1/latest/Google.Cloud.Metastore.V1.UpdateMetadataImportRequest)`  
The request received from the client.  
`context` | `[ServerCallContext](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.ServerCallContext.html)`  
The context of the server-side call handler being invoked.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation.html)` | The response to send back to the client (wrapped by a task).  
  
### UpdateService(UpdateServiceRequest, ServerCallContext)
    
    
    public virtual Task<Operation> UpdateService(UpdateServiceRequest request, ServerCallContext context)

Updates the parameters of a single service.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[UpdateServiceRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Metastore.V1/latest/Google.Cloud.Metastore.V1.UpdateServiceRequest)`  
The request received from the client.  
`context` | `[ServerCallContext](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.ServerCallContext.html)`  
The context of the server-side call handler being invoked.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation.html)` | The response to send back to the client (wrapped by a task).  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-03-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-03-09 UTC."],[],[]] 
