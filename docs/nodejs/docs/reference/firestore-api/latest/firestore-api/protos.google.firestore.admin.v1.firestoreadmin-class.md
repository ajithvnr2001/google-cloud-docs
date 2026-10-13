---
url: https://docs.cloud.google.com/nodejs/docs/reference/firestore-api/latest/firestore-api/protos.google.firestore.admin.v1.firestoreadmin-class
title: Class protos.google.firestore.admin.v1.FirestoreAdmin (0.2.0) \u00a0|\u00a0 Node.js client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T17:44:25.577728+00:00
---

# Class protos.google.firestore.admin.v1.FirestoreAdmin (0.2.0)  |  Node.js client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/nodejs/docs/reference/firestore-api/latest/firestore-api/protos.google.firestore.admin.v1.firestoreadmin-class

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Node.js ](https://docs.cloud.google.com/nodejs/docs)
  * [ Client libraries ](https://docs.cloud.google.com/nodejs/docs/reference)



Send feedback 

#  Class protos.google.firestore.admin.v1.FirestoreAdmin (0.2.0) Stay organized with collections  Save and categorize content based on your preferences. 

Represents a FirestoreAdmin

## Inheritance

$protobuf.rpc.Service > protos.google.firestore.admin.v1.FirestoreAdmin

## Package

[@google-cloud/firestore-api](https://docs.cloud.google.com/nodejs/docs/reference/firestore-api/latest/overview.html)

## Constructors 

### (constructor)(rpcImpl, requestDelimited, responseDelimited)
    
    
    constructor(rpcImpl: $protobuf.RPCImpl, requestDelimited?: boolean, responseDelimited?: boolean);

Constructs a new FirestoreAdmin service.

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

### bulkDeleteDocuments(request, callback)
    
    
    public bulkDeleteDocuments(request: google.firestore.admin.v1.IBulkDeleteDocumentsRequest, callback: google.firestore.admin.v1.FirestoreAdmin.BulkDeleteDocumentsCallback): void;

Calls BulkDeleteDocuments.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IBulkDeleteDocumentsRequest](https://docs.cloud.google.com/nodejs/docs/reference/firestore-api/latest/firestore-api/protos.google.firestore.admin.v1.ibulkdeletedocumentsrequest)`   
BulkDeleteDocumentsRequest message or plain object  
`callback` |  `[BulkDeleteDocumentsCallback](https://docs.cloud.google.com/nodejs/docs/reference/firestore-api/latest/overview.html)`   
Node-style callback called with the error, if any, and Operation  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### bulkDeleteDocuments(request)
    
    
    public bulkDeleteDocuments(request: google.firestore.admin.v1.IBulkDeleteDocumentsRequest): Promise<google.longrunning.Operation>;

Calls BulkDeleteDocuments.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IBulkDeleteDocumentsRequest](https://docs.cloud.google.com/nodejs/docs/reference/firestore-api/latest/firestore-api/protos.google.firestore.admin.v1.ibulkdeletedocumentsrequest)`   
BulkDeleteDocumentsRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.longrunning.Operation](https://docs.cloud.google.com/nodejs/docs/reference/firestore-api/latest/firestore-api/protos.google.longrunning.operation)>` | Promise  
  
### cloneDatabase(request, callback)
    
    
    public cloneDatabase(request: google.firestore.admin.v1.ICloneDatabaseRequest, callback: google.firestore.admin.v1.FirestoreAdmin.CloneDatabaseCallback): void;

Calls CloneDatabase.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[ICloneDatabaseRequest](https://docs.cloud.google.com/nodejs/docs/reference/firestore-api/latest/firestore-api/protos.google.firestore.admin.v1.iclonedatabaserequest)`   
CloneDatabaseRequest message or plain object  
`callback` |  `[CloneDatabaseCallback](https://docs.cloud.google.com/nodejs/docs/reference/firestore-api/latest/overview.html)`   
Node-style callback called with the error, if any, and Operation  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### cloneDatabase(request)
    
    
    public cloneDatabase(request: google.firestore.admin.v1.ICloneDatabaseRequest): Promise<google.longrunning.Operation>;

Calls CloneDatabase.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[ICloneDatabaseRequest](https://docs.cloud.google.com/nodejs/docs/reference/firestore-api/latest/firestore-api/protos.google.firestore.admin.v1.iclonedatabaserequest)`   
CloneDatabaseRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.longrunning.Operation](https://docs.cloud.google.com/nodejs/docs/reference/firestore-api/latest/firestore-api/protos.google.longrunning.operation)>` | Promise  
  
### create(rpcImpl, requestDelimited, responseDelimited)
    
    
    public static create(rpcImpl: $protobuf.RPCImpl, requestDelimited?: boolean, responseDelimited?: boolean): FirestoreAdmin;

Creates new FirestoreAdmin service using the specified rpc implementation.

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
`[FirestoreAdmin](https://docs.cloud.google.com/nodejs/docs/reference/firestore-api/latest/firestore-api/protos.google.firestore.admin.v1.firestoreadmin-class)` | RPC service. Useful where requests and/or responses are streamed.  
  
### createBackupSchedule(request, callback)
    
    
    public createBackupSchedule(request: google.firestore.admin.v1.ICreateBackupScheduleRequest, callback: google.firestore.admin.v1.FirestoreAdmin.CreateBackupScheduleCallback): void;

Calls CreateBackupSchedule.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[ICreateBackupScheduleRequest](https://docs.cloud.google.com/nodejs/docs/reference/firestore-api/latest/firestore-api/protos.google.firestore.admin.v1.icreatebackupschedulerequest)`   
CreateBackupScheduleRequest message or plain object  
`callback` |  `[CreateBackupScheduleCallback](https://docs.cloud.google.com/nodejs/docs/reference/firestore-api/latest/overview.html)`   
Node-style callback called with the error, if any, and BackupSchedule  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### createBackupSchedule(request)
    
    
    public createBackupSchedule(request: google.firestore.admin.v1.ICreateBackupScheduleRequest): Promise<google.firestore.admin.v1.BackupSchedule>;

Calls CreateBackupSchedule.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[ICreateBackupScheduleRequest](https://docs.cloud.google.com/nodejs/docs/reference/firestore-api/latest/firestore-api/protos.google.firestore.admin.v1.icreatebackupschedulerequest)`   
CreateBackupScheduleRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.firestore.admin.v1.BackupSchedule](https://docs.cloud.google.com/nodejs/docs/reference/firestore-api/latest/firestore-api/protos.google.firestore.admin.v1.backupschedule)>` | Promise  
  
### createDatabase(request, callback)
    
    
    public createDatabase(request: google.firestore.admin.v1.ICreateDatabaseRequest, callback: google.firestore.admin.v1.FirestoreAdmin.CreateDatabaseCallback): void;

Calls CreateDatabase.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[ICreateDatabaseRequest](https://docs.cloud.google.com/nodejs/docs/reference/firestore-api/latest/firestore-api/protos.google.firestore.admin.v1.icreatedatabaserequest)`   
CreateDatabaseRequest message or plain object  
`callback` |  `[CreateDatabaseCallback](https://docs.cloud.google.com/nodejs/docs/reference/firestore-api/latest/overview.html)`   
Node-style callback called with the error, if any, and Operation  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### createDatabase(request)
    
    
    public createDatabase(request: google.firestore.admin.v1.ICreateDatabaseRequest): Promise<google.longrunning.Operation>;

Calls CreateDatabase.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[ICreateDatabaseRequest](https://docs.cloud.google.com/nodejs/docs/reference/firestore-api/latest/firestore-api/protos.google.firestore.admin.v1.icreatedatabaserequest)`   
CreateDatabaseRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.longrunning.Operation](https://docs.cloud.google.com/nodejs/docs/reference/firestore-api/latest/firestore-api/protos.google.longrunning.operation)>` | Promise  
  
### createIndex(request, callback)
    
    
    public createIndex(request: google.firestore.admin.v1.ICreateIndexRequest, callback: google.firestore.admin.v1.FirestoreAdmin.CreateIndexCallback): void;

Calls CreateIndex.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[ICreateIndexRequest](https://docs.cloud.google.com/nodejs/docs/reference/firestore-api/latest/firestore-api/protos.google.firestore.admin.v1.icreateindexrequest)`   
CreateIndexRequest message or plain object  
`callback` |  `[CreateIndexCallback](https://docs.cloud.google.com/nodejs/docs/reference/firestore-api/latest/overview.html)`   
Node-style callback called with the error, if any, and Operation  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### createIndex(request)
    
    
    public createIndex(request: google.firestore.admin.v1.ICreateIndexRequest): Promise<google.longrunning.Operation>;

Calls CreateIndex.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[ICreateIndexRequest](https://docs.cloud.google.com/nodejs/docs/reference/firestore-api/latest/firestore-api/protos.google.firestore.admin.v1.icreateindexrequest)`   
CreateIndexRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.longrunning.Operation](https://docs.cloud.google.com/nodejs/docs/reference/firestore-api/latest/firestore-api/protos.google.longrunning.operation)>` | Promise  
  
### createUserCreds(request, callback)
    
    
    public createUserCreds(request: google.firestore.admin.v1.ICreateUserCredsRequest, callback: google.firestore.admin.v1.FirestoreAdmin.CreateUserCredsCallback): void;

Calls CreateUserCreds.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[ICreateUserCredsRequest](https://docs.cloud.google.com/nodejs/docs/reference/firestore-api/latest/firestore-api/protos.google.firestore.admin.v1.icreateusercredsrequest)`   
CreateUserCredsRequest message or plain object  
`callback` |  `[CreateUserCredsCallback](https://docs.cloud.google.com/nodejs/docs/reference/firestore-api/latest/overview.html)`   
Node-style callback called with the error, if any, and UserCreds  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### createUserCreds(request)
    
    
    public createUserCreds(request: google.firestore.admin.v1.ICreateUserCredsRequest): Promise<google.firestore.admin.v1.UserCreds>;

Calls CreateUserCreds.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[ICreateUserCredsRequest](https://docs.cloud.google.com/nodejs/docs/reference/firestore-api/latest/firestore-api/protos.google.firestore.admin.v1.icreateusercredsrequest)`   
CreateUserCredsRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.firestore.admin.v1.UserCreds](https://docs.cloud.google.com/nodejs/docs/reference/firestore-api/latest/firestore-api/protos.google.firestore.admin.v1.usercreds-class)>` | Promise  
  
### deleteBackup(request, callback)
    
    
    public deleteBackup(request: google.firestore.admin.v1.IDeleteBackupRequest, callback: google.firestore.admin.v1.FirestoreAdmin.DeleteBackupCallback): void;

Calls DeleteBackup.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IDeleteBackupRequest](https://docs.cloud.google.com/nodejs/docs/reference/firestore-api/latest/firestore-api/protos.google.firestore.admin.v1.ideletebackuprequest)`   
DeleteBackupRequest message or plain object  
`callback` |  `[DeleteBackupCallback](https://docs.cloud.google.com/nodejs/docs/reference/firestore-api/latest/overview.html)`   
Node-style callback called with the error, if any, and Empty  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### deleteBackup(request)
    
    
    public deleteBackup(request: google.firestore.admin.v1.IDeleteBackupRequest): Promise<google.protobuf.Empty>;

Calls DeleteBackup.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IDeleteBackupRequest](https://docs.cloud.google.com/nodejs/docs/reference/firestore-api/latest/firestore-api/protos.google.firestore.admin.v1.ideletebackuprequest)`   
DeleteBackupRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.protobuf.Empty](https://docs.cloud.google.com/nodejs/docs/reference/firestore-api/latest/firestore-api/protos.google.protobuf.empty)>` | Promise  
  
### deleteBackupSchedule(request, callback)
    
    
    public deleteBackupSchedule(request: google.firestore.admin.v1.IDeleteBackupScheduleRequest, callback: google.firestore.admin.v1.FirestoreAdmin.DeleteBackupScheduleCallback): void;

Calls DeleteBackupSchedule.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IDeleteBackupScheduleRequest](https://docs.cloud.google.com/nodejs/docs/reference/firestore-api/latest/firestore-api/protos.google.firestore.admin.v1.ideletebackupschedulerequest)`   
DeleteBackupScheduleRequest message or plain object  
`callback` |  `[DeleteBackupScheduleCallback](https://docs.cloud.google.com/nodejs/docs/reference/firestore-api/latest/overview.html)`   
Node-style callback called with the error, if any, and Empty  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### deleteBackupSchedule(request)
    
    
    public deleteBackupSchedule(request: google.firestore.admin.v1.IDeleteBackupScheduleRequest): Promise<google.protobuf.Empty>;

Calls DeleteBackupSchedule.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IDeleteBackupScheduleRequest](https://docs.cloud.google.com/nodejs/docs/reference/firestore-api/latest/firestore-api/protos.google.firestore.admin.v1.ideletebackupschedulerequest)`   
DeleteBackupScheduleRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.protobuf.Empty](https://docs.cloud.google.com/nodejs/docs/reference/firestore-api/latest/firestore-api/protos.google.protobuf.empty)>` | Promise  
  
### deleteDatabase(request, callback)
    
    
    public deleteDatabase(request: google.firestore.admin.v1.IDeleteDatabaseRequest, callback: google.firestore.admin.v1.FirestoreAdmin.DeleteDatabaseCallback): void;

Calls DeleteDatabase.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IDeleteDatabaseRequest](https://docs.cloud.google.com/nodejs/docs/reference/firestore-api/latest/firestore-api/protos.google.firestore.admin.v1.ideletedatabaserequest)`   
DeleteDatabaseRequest message or plain object  
`callback` |  `[DeleteDatabaseCallback](https://docs.cloud.google.com/nodejs/docs/reference/firestore-api/latest/overview.html)`   
Node-style callback called with the error, if any, and Operation  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### deleteDatabase(request)
    
    
    public deleteDatabase(request: google.firestore.admin.v1.IDeleteDatabaseRequest): Promise<google.longrunning.Operation>;

Calls DeleteDatabase.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IDeleteDatabaseRequest](https://docs.cloud.google.com/nodejs/docs/reference/firestore-api/latest/firestore-api/protos.google.firestore.admin.v1.ideletedatabaserequest)`   
DeleteDatabaseRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.longrunning.Operation](https://docs.cloud.google.com/nodejs/docs/reference/firestore-api/latest/firestore-api/protos.google.longrunning.operation)>` | Promise  
  
### deleteIndex(request, callback)
    
    
    public deleteIndex(request: google.firestore.admin.v1.IDeleteIndexRequest, callback: google.firestore.admin.v1.FirestoreAdmin.DeleteIndexCallback): void;

Calls DeleteIndex.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IDeleteIndexRequest](https://docs.cloud.google.com/nodejs/docs/reference/firestore-api/latest/firestore-api/protos.google.firestore.admin.v1.ideleteindexrequest)`   
DeleteIndexRequest message or plain object  
`callback` |  `[DeleteIndexCallback](https://docs.cloud.google.com/nodejs/docs/reference/firestore-api/latest/overview.html)`   
Node-style callback called with the error, if any, and Empty  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### deleteIndex(request)
    
    
    public deleteIndex(request: google.firestore.admin.v1.IDeleteIndexRequest): Promise<google.protobuf.Empty>;

Calls DeleteIndex.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IDeleteIndexRequest](https://docs.cloud.google.com/nodejs/docs/reference/firestore-api/latest/firestore-api/protos.google.firestore.admin.v1.ideleteindexrequest)`   
DeleteIndexRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.protobuf.Empty](https://docs.cloud.google.com/nodejs/docs/reference/firestore-api/latest/firestore-api/protos.google.protobuf.empty)>` | Promise  
  
### deleteUserCreds(request, callback)
    
    
    public deleteUserCreds(request: google.firestore.admin.v1.IDeleteUserCredsRequest, callback: google.firestore.admin.v1.FirestoreAdmin.DeleteUserCredsCallback): void;

Calls DeleteUserCreds.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IDeleteUserCredsRequest](https://docs.cloud.google.com/nodejs/docs/reference/firestore-api/latest/firestore-api/protos.google.firestore.admin.v1.ideleteusercredsrequest)`   
DeleteUserCredsRequest message or plain object  
`callback` |  `[DeleteUserCredsCallback](https://docs.cloud.google.com/nodejs/docs/reference/firestore-api/latest/overview.html)`   
Node-style callback called with the error, if any, and Empty  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### deleteUserCreds(request)
    
    
    public deleteUserCreds(request: google.firestore.admin.v1.IDeleteUserCredsRequest): Promise<google.protobuf.Empty>;

Calls DeleteUserCreds.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IDeleteUserCredsRequest](https://docs.cloud.google.com/nodejs/docs/reference/firestore-api/latest/firestore-api/protos.google.firestore.admin.v1.ideleteusercredsrequest)`   
DeleteUserCredsRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.protobuf.Empty](https://docs.cloud.google.com/nodejs/docs/reference/firestore-api/latest/firestore-api/protos.google.protobuf.empty)>` | Promise  
  
### disableUserCreds(request, callback)
    
    
    public disableUserCreds(request: google.firestore.admin.v1.IDisableUserCredsRequest, callback: google.firestore.admin.v1.FirestoreAdmin.DisableUserCredsCallback): void;

Calls DisableUserCreds.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IDisableUserCredsRequest](https://docs.cloud.google.com/nodejs/docs/reference/firestore-api/latest/firestore-api/protos.google.firestore.admin.v1.idisableusercredsrequest)`   
DisableUserCredsRequest message or plain object  
`callback` |  `[DisableUserCredsCallback](https://docs.cloud.google.com/nodejs/docs/reference/firestore-api/latest/overview.html)`   
Node-style callback called with the error, if any, and UserCreds  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### disableUserCreds(request)
    
    
    public disableUserCreds(request: google.firestore.admin.v1.IDisableUserCredsRequest): Promise<google.firestore.admin.v1.UserCreds>;

Calls DisableUserCreds.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IDisableUserCredsRequest](https://docs.cloud.google.com/nodejs/docs/reference/firestore-api/latest/firestore-api/protos.google.firestore.admin.v1.idisableusercredsrequest)`   
DisableUserCredsRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.firestore.admin.v1.UserCreds](https://docs.cloud.google.com/nodejs/docs/reference/firestore-api/latest/firestore-api/protos.google.firestore.admin.v1.usercreds-class)>` | Promise  
  
### enableUserCreds(request, callback)
    
    
    public enableUserCreds(request: google.firestore.admin.v1.IEnableUserCredsRequest, callback: google.firestore.admin.v1.FirestoreAdmin.EnableUserCredsCallback): void;

Calls EnableUserCreds.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IEnableUserCredsRequest](https://docs.cloud.google.com/nodejs/docs/reference/firestore-api/latest/firestore-api/protos.google.firestore.admin.v1.ienableusercredsrequest)`   
EnableUserCredsRequest message or plain object  
`callback` |  `[EnableUserCredsCallback](https://docs.cloud.google.com/nodejs/docs/reference/firestore-api/latest/overview.html)`   
Node-style callback called with the error, if any, and UserCreds  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### enableUserCreds(request)
    
    
    public enableUserCreds(request: google.firestore.admin.v1.IEnableUserCredsRequest): Promise<google.firestore.admin.v1.UserCreds>;

Calls EnableUserCreds.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IEnableUserCredsRequest](https://docs.cloud.google.com/nodejs/docs/reference/firestore-api/latest/firestore-api/protos.google.firestore.admin.v1.ienableusercredsrequest)`   
EnableUserCredsRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.firestore.admin.v1.UserCreds](https://docs.cloud.google.com/nodejs/docs/reference/firestore-api/latest/firestore-api/protos.google.firestore.admin.v1.usercreds-class)>` | Promise  
  
### exportDocuments(request, callback)
    
    
    public exportDocuments(request: google.firestore.admin.v1.IExportDocumentsRequest, callback: google.firestore.admin.v1.FirestoreAdmin.ExportDocumentsCallback): void;

Calls ExportDocuments.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IExportDocumentsRequest](https://docs.cloud.google.com/nodejs/docs/reference/firestore-api/latest/firestore-api/protos.google.firestore.admin.v1.iexportdocumentsrequest)`   
ExportDocumentsRequest message or plain object  
`callback` |  `[ExportDocumentsCallback](https://docs.cloud.google.com/nodejs/docs/reference/firestore-api/latest/overview.html)`   
Node-style callback called with the error, if any, and Operation  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### exportDocuments(request)
    
    
    public exportDocuments(request: google.firestore.admin.v1.IExportDocumentsRequest): Promise<google.longrunning.Operation>;

Calls ExportDocuments.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IExportDocumentsRequest](https://docs.cloud.google.com/nodejs/docs/reference/firestore-api/latest/firestore-api/protos.google.firestore.admin.v1.iexportdocumentsrequest)`   
ExportDocumentsRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.longrunning.Operation](https://docs.cloud.google.com/nodejs/docs/reference/firestore-api/latest/firestore-api/protos.google.longrunning.operation)>` | Promise  
  
### getBackup(request, callback)
    
    
    public getBackup(request: google.firestore.admin.v1.IGetBackupRequest, callback: google.firestore.admin.v1.FirestoreAdmin.GetBackupCallback): void;

Calls GetBackup.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IGetBackupRequest](https://docs.cloud.google.com/nodejs/docs/reference/firestore-api/latest/firestore-api/protos.google.firestore.admin.v1.igetbackuprequest)`   
GetBackupRequest message or plain object  
`callback` |  `[GetBackupCallback](https://docs.cloud.google.com/nodejs/docs/reference/firestore-api/latest/overview.html)`   
Node-style callback called with the error, if any, and Backup  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### getBackup(request)
    
    
    public getBackup(request: google.firestore.admin.v1.IGetBackupRequest): Promise<google.firestore.admin.v1.Backup>;

Calls GetBackup.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IGetBackupRequest](https://docs.cloud.google.com/nodejs/docs/reference/firestore-api/latest/firestore-api/protos.google.firestore.admin.v1.igetbackuprequest)`   
GetBackupRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.firestore.admin.v1.Backup](https://docs.cloud.google.com/nodejs/docs/reference/firestore-api/latest/firestore-api/protos.google.firestore.admin.v1.backup-class)>` | Promise  
  
### getBackupSchedule(request, callback)
    
    
    public getBackupSchedule(request: google.firestore.admin.v1.IGetBackupScheduleRequest, callback: google.firestore.admin.v1.FirestoreAdmin.GetBackupScheduleCallback): void;

Calls GetBackupSchedule.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IGetBackupScheduleRequest](https://docs.cloud.google.com/nodejs/docs/reference/firestore-api/latest/firestore-api/protos.google.firestore.admin.v1.igetbackupschedulerequest)`   
GetBackupScheduleRequest message or plain object  
`callback` |  `[GetBackupScheduleCallback](https://docs.cloud.google.com/nodejs/docs/reference/firestore-api/latest/overview.html)`   
Node-style callback called with the error, if any, and BackupSchedule  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### getBackupSchedule(request)
    
    
    public getBackupSchedule(request: google.firestore.admin.v1.IGetBackupScheduleRequest): Promise<google.firestore.admin.v1.BackupSchedule>;

Calls GetBackupSchedule.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IGetBackupScheduleRequest](https://docs.cloud.google.com/nodejs/docs/reference/firestore-api/latest/firestore-api/protos.google.firestore.admin.v1.igetbackupschedulerequest)`   
GetBackupScheduleRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.firestore.admin.v1.BackupSchedule](https://docs.cloud.google.com/nodejs/docs/reference/firestore-api/latest/firestore-api/protos.google.firestore.admin.v1.backupschedule)>` | Promise  
  
### getDatabase(request, callback)
    
    
    public getDatabase(request: google.firestore.admin.v1.IGetDatabaseRequest, callback: google.firestore.admin.v1.FirestoreAdmin.GetDatabaseCallback): void;

Calls GetDatabase.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IGetDatabaseRequest](https://docs.cloud.google.com/nodejs/docs/reference/firestore-api/latest/firestore-api/protos.google.firestore.admin.v1.igetdatabaserequest)`   
GetDatabaseRequest message or plain object  
`callback` |  `[GetDatabaseCallback](https://docs.cloud.google.com/nodejs/docs/reference/firestore-api/latest/overview.html)`   
Node-style callback called with the error, if any, and Database  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### getDatabase(request)
    
    
    public getDatabase(request: google.firestore.admin.v1.IGetDatabaseRequest): Promise<google.firestore.admin.v1.Database>;

Calls GetDatabase.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IGetDatabaseRequest](https://docs.cloud.google.com/nodejs/docs/reference/firestore-api/latest/firestore-api/protos.google.firestore.admin.v1.igetdatabaserequest)`   
GetDatabaseRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.firestore.admin.v1.Database](https://docs.cloud.google.com/nodejs/docs/reference/firestore-api/latest/firestore-api/protos.google.firestore.admin.v1.database-class)>` | Promise  
  
### getField(request, callback)
    
    
    public getField(request: google.firestore.admin.v1.IGetFieldRequest, callback: google.firestore.admin.v1.FirestoreAdmin.GetFieldCallback): void;

Calls GetField.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IGetFieldRequest](https://docs.cloud.google.com/nodejs/docs/reference/firestore-api/latest/firestore-api/protos.google.firestore.admin.v1.igetfieldrequest)`   
GetFieldRequest message or plain object  
`callback` |  `[GetFieldCallback](https://docs.cloud.google.com/nodejs/docs/reference/firestore-api/latest/overview.html)`   
Node-style callback called with the error, if any, and Field  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### getField(request)
    
    
    public getField(request: google.firestore.admin.v1.IGetFieldRequest): Promise<google.firestore.admin.v1.Field>;

Calls GetField.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IGetFieldRequest](https://docs.cloud.google.com/nodejs/docs/reference/firestore-api/latest/firestore-api/protos.google.firestore.admin.v1.igetfieldrequest)`   
GetFieldRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.firestore.admin.v1.Field](https://docs.cloud.google.com/nodejs/docs/reference/firestore-api/latest/firestore-api/protos.google.firestore.admin.v1.field-class)>` | Promise  
  
### getIndex(request, callback)
    
    
    public getIndex(request: google.firestore.admin.v1.IGetIndexRequest, callback: google.firestore.admin.v1.FirestoreAdmin.GetIndexCallback): void;

Calls GetIndex.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IGetIndexRequest](https://docs.cloud.google.com/nodejs/docs/reference/firestore-api/latest/firestore-api/protos.google.firestore.admin.v1.igetindexrequest)`   
GetIndexRequest message or plain object  
`callback` |  `[GetIndexCallback](https://docs.cloud.google.com/nodejs/docs/reference/firestore-api/latest/overview.html)`   
Node-style callback called with the error, if any, and Index  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### getIndex(request)
    
    
    public getIndex(request: google.firestore.admin.v1.IGetIndexRequest): Promise<google.firestore.admin.v1.Index>;

Calls GetIndex.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IGetIndexRequest](https://docs.cloud.google.com/nodejs/docs/reference/firestore-api/latest/firestore-api/protos.google.firestore.admin.v1.igetindexrequest)`   
GetIndexRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.firestore.admin.v1.Index](https://docs.cloud.google.com/nodejs/docs/reference/firestore-api/latest/firestore-api/protos.google.firestore.admin.v1.index-class)>` | Promise  
  
### getUserCreds(request, callback)
    
    
    public getUserCreds(request: google.firestore.admin.v1.IGetUserCredsRequest, callback: google.firestore.admin.v1.FirestoreAdmin.GetUserCredsCallback): void;

Calls GetUserCreds.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IGetUserCredsRequest](https://docs.cloud.google.com/nodejs/docs/reference/firestore-api/latest/firestore-api/protos.google.firestore.admin.v1.igetusercredsrequest)`   
GetUserCredsRequest message or plain object  
`callback` |  `[GetUserCredsCallback](https://docs.cloud.google.com/nodejs/docs/reference/firestore-api/latest/overview.html)`   
Node-style callback called with the error, if any, and UserCreds  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### getUserCreds(request)
    
    
    public getUserCreds(request: google.firestore.admin.v1.IGetUserCredsRequest): Promise<google.firestore.admin.v1.UserCreds>;

Calls GetUserCreds.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IGetUserCredsRequest](https://docs.cloud.google.com/nodejs/docs/reference/firestore-api/latest/firestore-api/protos.google.firestore.admin.v1.igetusercredsrequest)`   
GetUserCredsRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.firestore.admin.v1.UserCreds](https://docs.cloud.google.com/nodejs/docs/reference/firestore-api/latest/firestore-api/protos.google.firestore.admin.v1.usercreds-class)>` | Promise  
  
### importDocuments(request, callback)
    
    
    public importDocuments(request: google.firestore.admin.v1.IImportDocumentsRequest, callback: google.firestore.admin.v1.FirestoreAdmin.ImportDocumentsCallback): void;

Calls ImportDocuments.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IImportDocumentsRequest](https://docs.cloud.google.com/nodejs/docs/reference/firestore-api/latest/firestore-api/protos.google.firestore.admin.v1.iimportdocumentsrequest)`   
ImportDocumentsRequest message or plain object  
`callback` |  `[ImportDocumentsCallback](https://docs.cloud.google.com/nodejs/docs/reference/firestore-api/latest/overview.html)`   
Node-style callback called with the error, if any, and Operation  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### importDocuments(request)
    
    
    public importDocuments(request: google.firestore.admin.v1.IImportDocumentsRequest): Promise<google.longrunning.Operation>;

Calls ImportDocuments.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IImportDocumentsRequest](https://docs.cloud.google.com/nodejs/docs/reference/firestore-api/latest/firestore-api/protos.google.firestore.admin.v1.iimportdocumentsrequest)`   
ImportDocumentsRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.longrunning.Operation](https://docs.cloud.google.com/nodejs/docs/reference/firestore-api/latest/firestore-api/protos.google.longrunning.operation)>` | Promise  
  
### listBackups(request, callback)
    
    
    public listBackups(request: google.firestore.admin.v1.IListBackupsRequest, callback: google.firestore.admin.v1.FirestoreAdmin.ListBackupsCallback): void;

Calls ListBackups.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListBackupsRequest](https://docs.cloud.google.com/nodejs/docs/reference/firestore-api/latest/firestore-api/protos.google.firestore.admin.v1.ilistbackupsrequest)`   
ListBackupsRequest message or plain object  
`callback` |  `[ListBackupsCallback](https://docs.cloud.google.com/nodejs/docs/reference/firestore-api/latest/overview.html)`   
Node-style callback called with the error, if any, and ListBackupsResponse  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### listBackups(request)
    
    
    public listBackups(request: google.firestore.admin.v1.IListBackupsRequest): Promise<google.firestore.admin.v1.ListBackupsResponse>;

Calls ListBackups.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IListBackupsRequest](https://docs.cloud.google.com/nodejs/docs/reference/firestore-api/latest/firestore-api/protos.google.firestore.admin.v1.ilistbackupsrequest)`   
ListBackupsRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.firestore.admin.v1.ListBackupsResponse](https://docs.cloud.google.com/nodejs/docs/reference/firestore-api/latest/firestore-api/protos.google.firestore.admin.v1.listbackupsresponse)>` | Promise  
  
### listBackupSchedules(request, callback)
    
    
    public listBackupSchedules(request: google.firestore.admin.v1.IListBackupSchedulesRequest, callback: google.firestore.admin.v1.FirestoreAdmin.ListBackupSchedulesCallback): void;

Calls ListBackupSchedules.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListBackupSchedulesRequest](https://docs.cloud.google.com/nodejs/docs/reference/firestore-api/latest/firestore-api/protos.google.firestore.admin.v1.ilistbackupschedulesrequest)`   
ListBackupSchedulesRequest message or plain object  
`callback` |  `[ListBackupSchedulesCallback](https://docs.cloud.google.com/nodejs/docs/reference/firestore-api/latest/overview.html)`   
Node-style callback called with the error, if any, and ListBackupSchedulesResponse  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### listBackupSchedules(request)
    
    
    public listBackupSchedules(request: google.firestore.admin.v1.IListBackupSchedulesRequest): Promise<google.firestore.admin.v1.ListBackupSchedulesResponse>;

Calls ListBackupSchedules.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IListBackupSchedulesRequest](https://docs.cloud.google.com/nodejs/docs/reference/firestore-api/latest/firestore-api/protos.google.firestore.admin.v1.ilistbackupschedulesrequest)`   
ListBackupSchedulesRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.firestore.admin.v1.ListBackupSchedulesResponse](https://docs.cloud.google.com/nodejs/docs/reference/firestore-api/latest/firestore-api/protos.google.firestore.admin.v1.listbackupschedulesresponse)>` | Promise  
  
### listDatabases(request, callback)
    
    
    public listDatabases(request: google.firestore.admin.v1.IListDatabasesRequest, callback: google.firestore.admin.v1.FirestoreAdmin.ListDatabasesCallback): void;

Calls ListDatabases.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListDatabasesRequest](https://docs.cloud.google.com/nodejs/docs/reference/firestore-api/latest/firestore-api/protos.google.firestore.admin.v1.ilistdatabasesrequest)`   
ListDatabasesRequest message or plain object  
`callback` |  `[ListDatabasesCallback](https://docs.cloud.google.com/nodejs/docs/reference/firestore-api/latest/overview.html)`   
Node-style callback called with the error, if any, and ListDatabasesResponse  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### listDatabases(request)
    
    
    public listDatabases(request: google.firestore.admin.v1.IListDatabasesRequest): Promise<google.firestore.admin.v1.ListDatabasesResponse>;

Calls ListDatabases.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IListDatabasesRequest](https://docs.cloud.google.com/nodejs/docs/reference/firestore-api/latest/firestore-api/protos.google.firestore.admin.v1.ilistdatabasesrequest)`   
ListDatabasesRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.firestore.admin.v1.ListDatabasesResponse](https://docs.cloud.google.com/nodejs/docs/reference/firestore-api/latest/firestore-api/protos.google.firestore.admin.v1.listdatabasesresponse)>` | Promise  
  
### listFields(request, callback)
    
    
    public listFields(request: google.firestore.admin.v1.IListFieldsRequest, callback: google.firestore.admin.v1.FirestoreAdmin.ListFieldsCallback): void;

Calls ListFields.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListFieldsRequest](https://docs.cloud.google.com/nodejs/docs/reference/firestore-api/latest/firestore-api/protos.google.firestore.admin.v1.ilistfieldsrequest)`   
ListFieldsRequest message or plain object  
`callback` |  `[ListFieldsCallback](https://docs.cloud.google.com/nodejs/docs/reference/firestore-api/latest/overview.html)`   
Node-style callback called with the error, if any, and ListFieldsResponse  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### listFields(request)
    
    
    public listFields(request: google.firestore.admin.v1.IListFieldsRequest): Promise<google.firestore.admin.v1.ListFieldsResponse>;

Calls ListFields.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IListFieldsRequest](https://docs.cloud.google.com/nodejs/docs/reference/firestore-api/latest/firestore-api/protos.google.firestore.admin.v1.ilistfieldsrequest)`   
ListFieldsRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.firestore.admin.v1.ListFieldsResponse](https://docs.cloud.google.com/nodejs/docs/reference/firestore-api/latest/firestore-api/protos.google.firestore.admin.v1.listfieldsresponse)>` | Promise  
  
### listIndexes(request, callback)
    
    
    public listIndexes(request: google.firestore.admin.v1.IListIndexesRequest, callback: google.firestore.admin.v1.FirestoreAdmin.ListIndexesCallback): void;

Calls ListIndexes.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListIndexesRequest](https://docs.cloud.google.com/nodejs/docs/reference/firestore-api/latest/firestore-api/protos.google.firestore.admin.v1.ilistindexesrequest)`   
ListIndexesRequest message or plain object  
`callback` |  `[ListIndexesCallback](https://docs.cloud.google.com/nodejs/docs/reference/firestore-api/latest/overview.html)`   
Node-style callback called with the error, if any, and ListIndexesResponse  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### listIndexes(request)
    
    
    public listIndexes(request: google.firestore.admin.v1.IListIndexesRequest): Promise<google.firestore.admin.v1.ListIndexesResponse>;

Calls ListIndexes.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IListIndexesRequest](https://docs.cloud.google.com/nodejs/docs/reference/firestore-api/latest/firestore-api/protos.google.firestore.admin.v1.ilistindexesrequest)`   
ListIndexesRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.firestore.admin.v1.ListIndexesResponse](https://docs.cloud.google.com/nodejs/docs/reference/firestore-api/latest/firestore-api/protos.google.firestore.admin.v1.listindexesresponse)>` | Promise  
  
### listUserCreds(request, callback)
    
    
    public listUserCreds(request: google.firestore.admin.v1.IListUserCredsRequest, callback: google.firestore.admin.v1.FirestoreAdmin.ListUserCredsCallback): void;

Calls ListUserCreds.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListUserCredsRequest](https://docs.cloud.google.com/nodejs/docs/reference/firestore-api/latest/firestore-api/protos.google.firestore.admin.v1.ilistusercredsrequest)`   
ListUserCredsRequest message or plain object  
`callback` |  `[ListUserCredsCallback](https://docs.cloud.google.com/nodejs/docs/reference/firestore-api/latest/overview.html)`   
Node-style callback called with the error, if any, and ListUserCredsResponse  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### listUserCreds(request)
    
    
    public listUserCreds(request: google.firestore.admin.v1.IListUserCredsRequest): Promise<google.firestore.admin.v1.ListUserCredsResponse>;

Calls ListUserCreds.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IListUserCredsRequest](https://docs.cloud.google.com/nodejs/docs/reference/firestore-api/latest/firestore-api/protos.google.firestore.admin.v1.ilistusercredsrequest)`   
ListUserCredsRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.firestore.admin.v1.ListUserCredsResponse](https://docs.cloud.google.com/nodejs/docs/reference/firestore-api/latest/firestore-api/protos.google.firestore.admin.v1.listusercredsresponse)>` | Promise  
  
### resetUserPassword(request, callback)
    
    
    public resetUserPassword(request: google.firestore.admin.v1.IResetUserPasswordRequest, callback: google.firestore.admin.v1.FirestoreAdmin.ResetUserPasswordCallback): void;

Calls ResetUserPassword.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IResetUserPasswordRequest](https://docs.cloud.google.com/nodejs/docs/reference/firestore-api/latest/firestore-api/protos.google.firestore.admin.v1.iresetuserpasswordrequest)`   
ResetUserPasswordRequest message or plain object  
`callback` |  `[ResetUserPasswordCallback](https://docs.cloud.google.com/nodejs/docs/reference/firestore-api/latest/overview.html)`   
Node-style callback called with the error, if any, and UserCreds  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### resetUserPassword(request)
    
    
    public resetUserPassword(request: google.firestore.admin.v1.IResetUserPasswordRequest): Promise<google.firestore.admin.v1.UserCreds>;

Calls ResetUserPassword.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IResetUserPasswordRequest](https://docs.cloud.google.com/nodejs/docs/reference/firestore-api/latest/firestore-api/protos.google.firestore.admin.v1.iresetuserpasswordrequest)`   
ResetUserPasswordRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.firestore.admin.v1.UserCreds](https://docs.cloud.google.com/nodejs/docs/reference/firestore-api/latest/firestore-api/protos.google.firestore.admin.v1.usercreds-class)>` | Promise  
  
### restoreDatabase(request, callback)
    
    
    public restoreDatabase(request: google.firestore.admin.v1.IRestoreDatabaseRequest, callback: google.firestore.admin.v1.FirestoreAdmin.RestoreDatabaseCallback): void;

Calls RestoreDatabase.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IRestoreDatabaseRequest](https://docs.cloud.google.com/nodejs/docs/reference/firestore-api/latest/firestore-api/protos.google.firestore.admin.v1.irestoredatabaserequest)`   
RestoreDatabaseRequest message or plain object  
`callback` |  `[RestoreDatabaseCallback](https://docs.cloud.google.com/nodejs/docs/reference/firestore-api/latest/overview.html)`   
Node-style callback called with the error, if any, and Operation  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### restoreDatabase(request)
    
    
    public restoreDatabase(request: google.firestore.admin.v1.IRestoreDatabaseRequest): Promise<google.longrunning.Operation>;

Calls RestoreDatabase.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IRestoreDatabaseRequest](https://docs.cloud.google.com/nodejs/docs/reference/firestore-api/latest/firestore-api/protos.google.firestore.admin.v1.irestoredatabaserequest)`   
RestoreDatabaseRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.longrunning.Operation](https://docs.cloud.google.com/nodejs/docs/reference/firestore-api/latest/firestore-api/protos.google.longrunning.operation)>` | Promise  
  
### updateBackupSchedule(request, callback)
    
    
    public updateBackupSchedule(request: google.firestore.admin.v1.IUpdateBackupScheduleRequest, callback: google.firestore.admin.v1.FirestoreAdmin.UpdateBackupScheduleCallback): void;

Calls UpdateBackupSchedule.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IUpdateBackupScheduleRequest](https://docs.cloud.google.com/nodejs/docs/reference/firestore-api/latest/firestore-api/protos.google.firestore.admin.v1.iupdatebackupschedulerequest)`   
UpdateBackupScheduleRequest message or plain object  
`callback` |  `[UpdateBackupScheduleCallback](https://docs.cloud.google.com/nodejs/docs/reference/firestore-api/latest/overview.html)`   
Node-style callback called with the error, if any, and BackupSchedule  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### updateBackupSchedule(request)
    
    
    public updateBackupSchedule(request: google.firestore.admin.v1.IUpdateBackupScheduleRequest): Promise<google.firestore.admin.v1.BackupSchedule>;

Calls UpdateBackupSchedule.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IUpdateBackupScheduleRequest](https://docs.cloud.google.com/nodejs/docs/reference/firestore-api/latest/firestore-api/protos.google.firestore.admin.v1.iupdatebackupschedulerequest)`   
UpdateBackupScheduleRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.firestore.admin.v1.BackupSchedule](https://docs.cloud.google.com/nodejs/docs/reference/firestore-api/latest/firestore-api/protos.google.firestore.admin.v1.backupschedule)>` | Promise  
  
### updateDatabase(request, callback)
    
    
    public updateDatabase(request: google.firestore.admin.v1.IUpdateDatabaseRequest, callback: google.firestore.admin.v1.FirestoreAdmin.UpdateDatabaseCallback): void;

Calls UpdateDatabase.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IUpdateDatabaseRequest](https://docs.cloud.google.com/nodejs/docs/reference/firestore-api/latest/firestore-api/protos.google.firestore.admin.v1.iupdatedatabaserequest)`   
UpdateDatabaseRequest message or plain object  
`callback` |  `[UpdateDatabaseCallback](https://docs.cloud.google.com/nodejs/docs/reference/firestore-api/latest/overview.html)`   
Node-style callback called with the error, if any, and Operation  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### updateDatabase(request)
    
    
    public updateDatabase(request: google.firestore.admin.v1.IUpdateDatabaseRequest): Promise<google.longrunning.Operation>;

Calls UpdateDatabase.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IUpdateDatabaseRequest](https://docs.cloud.google.com/nodejs/docs/reference/firestore-api/latest/firestore-api/protos.google.firestore.admin.v1.iupdatedatabaserequest)`   
UpdateDatabaseRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.longrunning.Operation](https://docs.cloud.google.com/nodejs/docs/reference/firestore-api/latest/firestore-api/protos.google.longrunning.operation)>` | Promise  
  
### updateField(request, callback)
    
    
    public updateField(request: google.firestore.admin.v1.IUpdateFieldRequest, callback: google.firestore.admin.v1.FirestoreAdmin.UpdateFieldCallback): void;

Calls UpdateField.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IUpdateFieldRequest](https://docs.cloud.google.com/nodejs/docs/reference/firestore-api/latest/firestore-api/protos.google.firestore.admin.v1.iupdatefieldrequest)`   
UpdateFieldRequest message or plain object  
`callback` |  `[UpdateFieldCallback](https://docs.cloud.google.com/nodejs/docs/reference/firestore-api/latest/overview.html)`   
Node-style callback called with the error, if any, and Operation  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### updateField(request)
    
    
    public updateField(request: google.firestore.admin.v1.IUpdateFieldRequest): Promise<google.longrunning.Operation>;

Calls UpdateField.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IUpdateFieldRequest](https://docs.cloud.google.com/nodejs/docs/reference/firestore-api/latest/firestore-api/protos.google.firestore.admin.v1.iupdatefieldrequest)`   
UpdateFieldRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.longrunning.Operation](https://docs.cloud.google.com/nodejs/docs/reference/firestore-api/latest/firestore-api/protos.google.longrunning.operation)>` | Promise  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-07-31 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-07-31 UTC."],[],[]] 
