---
url: https://docs.cloud.google.com/nodejs/docs/reference/memorystore/latest/memorystore/protos.google.cloud.memorystore.v1.memorystore-class
title: Class protos.google.cloud.memorystore.v1.Memorystore (0.10.1) \u00a0|\u00a0 Node.js client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T16:02:05.756515+00:00
---

# Class protos.google.cloud.memorystore.v1.Memorystore (0.10.1)  |  Node.js client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/nodejs/docs/reference/memorystore/latest/memorystore/protos.google.cloud.memorystore.v1.memorystore-class

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Node.js ](https://docs.cloud.google.com/nodejs/docs)
  * [ Client libraries ](https://docs.cloud.google.com/nodejs/docs/reference)



Send feedback 

#  Class protos.google.cloud.memorystore.v1.Memorystore (0.10.1) Stay organized with collections  Save and categorize content based on your preferences. 

0.10.1 (latest)  0.8.0  0.7.0  0.4.0  0.1.0 

Represents a Memorystore

## Inheritance

$protobuf.rpc.Service > protos.google.cloud.memorystore.v1.Memorystore

## Package

[@google-cloud/memorystore](https://docs.cloud.google.com/nodejs/docs/reference/memorystore/latest/overview.html)

## Constructors 

### (constructor)(rpcImpl, requestDelimited, responseDelimited)
    
    
    constructor(rpcImpl: $protobuf.RPCImpl, requestDelimited?: boolean, responseDelimited?: boolean);

Constructs a new Memorystore service.

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

### addAuthToken(request, callback)
    
    
    public addAuthToken(request: google.cloud.memorystore.v1.IAddAuthTokenRequest, callback: google.cloud.memorystore.v1.Memorystore.AddAuthTokenCallback): void;

Calls AddAuthToken.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IAddAuthTokenRequest](https://docs.cloud.google.com/nodejs/docs/reference/memorystore/latest/memorystore/protos.google.cloud.memorystore.v1.iaddauthtokenrequest)`   
AddAuthTokenRequest message or plain object  
`callback` |  `[AddAuthTokenCallback](https://docs.cloud.google.com/nodejs/docs/reference/memorystore/latest/overview.html)`   
Node-style callback called with the error, if any, and Operation  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### addAuthToken(request)
    
    
    public addAuthToken(request: google.cloud.memorystore.v1.IAddAuthTokenRequest): Promise<google.longrunning.Operation>;

Calls AddAuthToken.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IAddAuthTokenRequest](https://docs.cloud.google.com/nodejs/docs/reference/memorystore/latest/memorystore/protos.google.cloud.memorystore.v1.iaddauthtokenrequest)`   
AddAuthTokenRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.longrunning.Operation](https://docs.cloud.google.com/nodejs/docs/reference/memorystore/latest/memorystore/protos.google.longrunning.operation)>` | Promise  
  
### addTokenAuthUser(request, callback)
    
    
    public addTokenAuthUser(request: google.cloud.memorystore.v1.IAddTokenAuthUserRequest, callback: google.cloud.memorystore.v1.Memorystore.AddTokenAuthUserCallback): void;

Calls AddTokenAuthUser.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IAddTokenAuthUserRequest](https://docs.cloud.google.com/nodejs/docs/reference/memorystore/latest/memorystore/protos.google.cloud.memorystore.v1.iaddtokenauthuserrequest)`   
AddTokenAuthUserRequest message or plain object  
`callback` |  `[AddTokenAuthUserCallback](https://docs.cloud.google.com/nodejs/docs/reference/memorystore/latest/overview.html)`   
Node-style callback called with the error, if any, and Operation  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### addTokenAuthUser(request)
    
    
    public addTokenAuthUser(request: google.cloud.memorystore.v1.IAddTokenAuthUserRequest): Promise<google.longrunning.Operation>;

Calls AddTokenAuthUser.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IAddTokenAuthUserRequest](https://docs.cloud.google.com/nodejs/docs/reference/memorystore/latest/memorystore/protos.google.cloud.memorystore.v1.iaddtokenauthuserrequest)`   
AddTokenAuthUserRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.longrunning.Operation](https://docs.cloud.google.com/nodejs/docs/reference/memorystore/latest/memorystore/protos.google.longrunning.operation)>` | Promise  
  
### backupInstance(request, callback)
    
    
    public backupInstance(request: google.cloud.memorystore.v1.IBackupInstanceRequest, callback: google.cloud.memorystore.v1.Memorystore.BackupInstanceCallback): void;

Calls BackupInstance.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IBackupInstanceRequest](https://docs.cloud.google.com/nodejs/docs/reference/memorystore/latest/memorystore/protos.google.cloud.memorystore.v1.ibackupinstancerequest)`   
BackupInstanceRequest message or plain object  
`callback` |  `[BackupInstanceCallback](https://docs.cloud.google.com/nodejs/docs/reference/memorystore/latest/overview.html)`   
Node-style callback called with the error, if any, and Operation  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### backupInstance(request)
    
    
    public backupInstance(request: google.cloud.memorystore.v1.IBackupInstanceRequest): Promise<google.longrunning.Operation>;

Calls BackupInstance.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IBackupInstanceRequest](https://docs.cloud.google.com/nodejs/docs/reference/memorystore/latest/memorystore/protos.google.cloud.memorystore.v1.ibackupinstancerequest)`   
BackupInstanceRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.longrunning.Operation](https://docs.cloud.google.com/nodejs/docs/reference/memorystore/latest/memorystore/protos.google.longrunning.operation)>` | Promise  
  
### create(rpcImpl, requestDelimited, responseDelimited)
    
    
    public static create(rpcImpl: $protobuf.RPCImpl, requestDelimited?: boolean, responseDelimited?: boolean): Memorystore;

Creates new Memorystore service using the specified rpc implementation.

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
`[Memorystore](https://docs.cloud.google.com/nodejs/docs/reference/memorystore/latest/memorystore/protos.google.cloud.memorystore.v1.memorystore-class)` | RPC service. Useful where requests and/or responses are streamed.  
  
### createInstance(request, callback)
    
    
    public createInstance(request: google.cloud.memorystore.v1.ICreateInstanceRequest, callback: google.cloud.memorystore.v1.Memorystore.CreateInstanceCallback): void;

Calls CreateInstance.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[ICreateInstanceRequest](https://docs.cloud.google.com/nodejs/docs/reference/memorystore/latest/memorystore/protos.google.cloud.memorystore.v1.icreateinstancerequest)`   
CreateInstanceRequest message or plain object  
`callback` |  `[CreateInstanceCallback](https://docs.cloud.google.com/nodejs/docs/reference/memorystore/latest/overview.html)`   
Node-style callback called with the error, if any, and Operation  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### createInstance(request)
    
    
    public createInstance(request: google.cloud.memorystore.v1.ICreateInstanceRequest): Promise<google.longrunning.Operation>;

Calls CreateInstance.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[ICreateInstanceRequest](https://docs.cloud.google.com/nodejs/docs/reference/memorystore/latest/memorystore/protos.google.cloud.memorystore.v1.icreateinstancerequest)`   
CreateInstanceRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.longrunning.Operation](https://docs.cloud.google.com/nodejs/docs/reference/memorystore/latest/memorystore/protos.google.longrunning.operation)>` | Promise  
  
### deleteAuthToken(request, callback)
    
    
    public deleteAuthToken(request: google.cloud.memorystore.v1.IDeleteAuthTokenRequest, callback: google.cloud.memorystore.v1.Memorystore.DeleteAuthTokenCallback): void;

Calls DeleteAuthToken.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IDeleteAuthTokenRequest](https://docs.cloud.google.com/nodejs/docs/reference/memorystore/latest/memorystore/protos.google.cloud.memorystore.v1.ideleteauthtokenrequest)`   
DeleteAuthTokenRequest message or plain object  
`callback` |  `[DeleteAuthTokenCallback](https://docs.cloud.google.com/nodejs/docs/reference/memorystore/latest/overview.html)`   
Node-style callback called with the error, if any, and Operation  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### deleteAuthToken(request)
    
    
    public deleteAuthToken(request: google.cloud.memorystore.v1.IDeleteAuthTokenRequest): Promise<google.longrunning.Operation>;

Calls DeleteAuthToken.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IDeleteAuthTokenRequest](https://docs.cloud.google.com/nodejs/docs/reference/memorystore/latest/memorystore/protos.google.cloud.memorystore.v1.ideleteauthtokenrequest)`   
DeleteAuthTokenRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.longrunning.Operation](https://docs.cloud.google.com/nodejs/docs/reference/memorystore/latest/memorystore/protos.google.longrunning.operation)>` | Promise  
  
### deleteBackup(request, callback)
    
    
    public deleteBackup(request: google.cloud.memorystore.v1.IDeleteBackupRequest, callback: google.cloud.memorystore.v1.Memorystore.DeleteBackupCallback): void;

Calls DeleteBackup.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IDeleteBackupRequest](https://docs.cloud.google.com/nodejs/docs/reference/memorystore/latest/memorystore/protos.google.cloud.memorystore.v1.ideletebackuprequest)`   
DeleteBackupRequest message or plain object  
`callback` |  `[DeleteBackupCallback](https://docs.cloud.google.com/nodejs/docs/reference/memorystore/latest/overview.html)`   
Node-style callback called with the error, if any, and Operation  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### deleteBackup(request)
    
    
    public deleteBackup(request: google.cloud.memorystore.v1.IDeleteBackupRequest): Promise<google.longrunning.Operation>;

Calls DeleteBackup.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IDeleteBackupRequest](https://docs.cloud.google.com/nodejs/docs/reference/memorystore/latest/memorystore/protos.google.cloud.memorystore.v1.ideletebackuprequest)`   
DeleteBackupRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.longrunning.Operation](https://docs.cloud.google.com/nodejs/docs/reference/memorystore/latest/memorystore/protos.google.longrunning.operation)>` | Promise  
  
### deleteInstance(request, callback)
    
    
    public deleteInstance(request: google.cloud.memorystore.v1.IDeleteInstanceRequest, callback: google.cloud.memorystore.v1.Memorystore.DeleteInstanceCallback): void;

Calls DeleteInstance.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IDeleteInstanceRequest](https://docs.cloud.google.com/nodejs/docs/reference/memorystore/latest/memorystore/protos.google.cloud.memorystore.v1.ideleteinstancerequest)`   
DeleteInstanceRequest message or plain object  
`callback` |  `[DeleteInstanceCallback](https://docs.cloud.google.com/nodejs/docs/reference/memorystore/latest/overview.html)`   
Node-style callback called with the error, if any, and Operation  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### deleteInstance(request)
    
    
    public deleteInstance(request: google.cloud.memorystore.v1.IDeleteInstanceRequest): Promise<google.longrunning.Operation>;

Calls DeleteInstance.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IDeleteInstanceRequest](https://docs.cloud.google.com/nodejs/docs/reference/memorystore/latest/memorystore/protos.google.cloud.memorystore.v1.ideleteinstancerequest)`   
DeleteInstanceRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.longrunning.Operation](https://docs.cloud.google.com/nodejs/docs/reference/memorystore/latest/memorystore/protos.google.longrunning.operation)>` | Promise  
  
### deleteTokenAuthUser(request, callback)
    
    
    public deleteTokenAuthUser(request: google.cloud.memorystore.v1.IDeleteTokenAuthUserRequest, callback: google.cloud.memorystore.v1.Memorystore.DeleteTokenAuthUserCallback): void;

Calls DeleteTokenAuthUser.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IDeleteTokenAuthUserRequest](https://docs.cloud.google.com/nodejs/docs/reference/memorystore/latest/memorystore/protos.google.cloud.memorystore.v1.ideletetokenauthuserrequest)`   
DeleteTokenAuthUserRequest message or plain object  
`callback` |  `[DeleteTokenAuthUserCallback](https://docs.cloud.google.com/nodejs/docs/reference/memorystore/latest/overview.html)`   
Node-style callback called with the error, if any, and Operation  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### deleteTokenAuthUser(request)
    
    
    public deleteTokenAuthUser(request: google.cloud.memorystore.v1.IDeleteTokenAuthUserRequest): Promise<google.longrunning.Operation>;

Calls DeleteTokenAuthUser.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IDeleteTokenAuthUserRequest](https://docs.cloud.google.com/nodejs/docs/reference/memorystore/latest/memorystore/protos.google.cloud.memorystore.v1.ideletetokenauthuserrequest)`   
DeleteTokenAuthUserRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.longrunning.Operation](https://docs.cloud.google.com/nodejs/docs/reference/memorystore/latest/memorystore/protos.google.longrunning.operation)>` | Promise  
  
### exportBackup(request, callback)
    
    
    public exportBackup(request: google.cloud.memorystore.v1.IExportBackupRequest, callback: google.cloud.memorystore.v1.Memorystore.ExportBackupCallback): void;

Calls ExportBackup.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IExportBackupRequest](https://docs.cloud.google.com/nodejs/docs/reference/memorystore/latest/memorystore/protos.google.cloud.memorystore.v1.iexportbackuprequest)`   
ExportBackupRequest message or plain object  
`callback` |  `[ExportBackupCallback](https://docs.cloud.google.com/nodejs/docs/reference/memorystore/latest/overview.html)`   
Node-style callback called with the error, if any, and Operation  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### exportBackup(request)
    
    
    public exportBackup(request: google.cloud.memorystore.v1.IExportBackupRequest): Promise<google.longrunning.Operation>;

Calls ExportBackup.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IExportBackupRequest](https://docs.cloud.google.com/nodejs/docs/reference/memorystore/latest/memorystore/protos.google.cloud.memorystore.v1.iexportbackuprequest)`   
ExportBackupRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.longrunning.Operation](https://docs.cloud.google.com/nodejs/docs/reference/memorystore/latest/memorystore/protos.google.longrunning.operation)>` | Promise  
  
### finishMigration(request, callback)
    
    
    public finishMigration(request: google.cloud.memorystore.v1.IFinishMigrationRequest, callback: google.cloud.memorystore.v1.Memorystore.FinishMigrationCallback): void;

Calls FinishMigration.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IFinishMigrationRequest](https://docs.cloud.google.com/nodejs/docs/reference/memorystore/latest/memorystore/protos.google.cloud.memorystore.v1.ifinishmigrationrequest)`   
FinishMigrationRequest message or plain object  
`callback` |  `[FinishMigrationCallback](https://docs.cloud.google.com/nodejs/docs/reference/memorystore/latest/overview.html)`   
Node-style callback called with the error, if any, and Operation  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### finishMigration(request)
    
    
    public finishMigration(request: google.cloud.memorystore.v1.IFinishMigrationRequest): Promise<google.longrunning.Operation>;

Calls FinishMigration.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IFinishMigrationRequest](https://docs.cloud.google.com/nodejs/docs/reference/memorystore/latest/memorystore/protos.google.cloud.memorystore.v1.ifinishmigrationrequest)`   
FinishMigrationRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.longrunning.Operation](https://docs.cloud.google.com/nodejs/docs/reference/memorystore/latest/memorystore/protos.google.longrunning.operation)>` | Promise  
  
### getAuthToken(request, callback)
    
    
    public getAuthToken(request: google.cloud.memorystore.v1.IGetAuthTokenRequest, callback: google.cloud.memorystore.v1.Memorystore.GetAuthTokenCallback): void;

Calls GetAuthToken.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IGetAuthTokenRequest](https://docs.cloud.google.com/nodejs/docs/reference/memorystore/latest/memorystore/protos.google.cloud.memorystore.v1.igetauthtokenrequest)`   
GetAuthTokenRequest message or plain object  
`callback` |  `[GetAuthTokenCallback](https://docs.cloud.google.com/nodejs/docs/reference/memorystore/latest/overview.html)`   
Node-style callback called with the error, if any, and AuthToken  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### getAuthToken(request)
    
    
    public getAuthToken(request: google.cloud.memorystore.v1.IGetAuthTokenRequest): Promise<google.cloud.memorystore.v1.AuthToken>;

Calls GetAuthToken.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IGetAuthTokenRequest](https://docs.cloud.google.com/nodejs/docs/reference/memorystore/latest/memorystore/protos.google.cloud.memorystore.v1.igetauthtokenrequest)`   
GetAuthTokenRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.memorystore.v1.AuthToken](https://docs.cloud.google.com/nodejs/docs/reference/memorystore/latest/memorystore/protos.google.cloud.memorystore.v1.authtoken-class)>` | Promise  
  
### getBackup(request, callback)
    
    
    public getBackup(request: google.cloud.memorystore.v1.IGetBackupRequest, callback: google.cloud.memorystore.v1.Memorystore.GetBackupCallback): void;

Calls GetBackup.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IGetBackupRequest](https://docs.cloud.google.com/nodejs/docs/reference/memorystore/latest/memorystore/protos.google.cloud.memorystore.v1.igetbackuprequest)`   
GetBackupRequest message or plain object  
`callback` |  `[GetBackupCallback](https://docs.cloud.google.com/nodejs/docs/reference/memorystore/latest/overview.html)`   
Node-style callback called with the error, if any, and Backup  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### getBackup(request)
    
    
    public getBackup(request: google.cloud.memorystore.v1.IGetBackupRequest): Promise<google.cloud.memorystore.v1.Backup>;

Calls GetBackup.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IGetBackupRequest](https://docs.cloud.google.com/nodejs/docs/reference/memorystore/latest/memorystore/protos.google.cloud.memorystore.v1.igetbackuprequest)`   
GetBackupRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.memorystore.v1.Backup](https://docs.cloud.google.com/nodejs/docs/reference/memorystore/latest/memorystore/protos.google.cloud.memorystore.v1.backup-class)>` | Promise  
  
### getBackupCollection(request, callback)
    
    
    public getBackupCollection(request: google.cloud.memorystore.v1.IGetBackupCollectionRequest, callback: google.cloud.memorystore.v1.Memorystore.GetBackupCollectionCallback): void;

Calls GetBackupCollection.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IGetBackupCollectionRequest](https://docs.cloud.google.com/nodejs/docs/reference/memorystore/latest/memorystore/protos.google.cloud.memorystore.v1.igetbackupcollectionrequest)`   
GetBackupCollectionRequest message or plain object  
`callback` |  `[GetBackupCollectionCallback](https://docs.cloud.google.com/nodejs/docs/reference/memorystore/latest/overview.html)`   
Node-style callback called with the error, if any, and BackupCollection  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### getBackupCollection(request)
    
    
    public getBackupCollection(request: google.cloud.memorystore.v1.IGetBackupCollectionRequest): Promise<google.cloud.memorystore.v1.BackupCollection>;

Calls GetBackupCollection.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IGetBackupCollectionRequest](https://docs.cloud.google.com/nodejs/docs/reference/memorystore/latest/memorystore/protos.google.cloud.memorystore.v1.igetbackupcollectionrequest)`   
GetBackupCollectionRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.memorystore.v1.BackupCollection](https://docs.cloud.google.com/nodejs/docs/reference/memorystore/latest/memorystore/protos.google.cloud.memorystore.v1.backupcollection)>` | Promise  
  
### getCertificateAuthority(request, callback)
    
    
    public getCertificateAuthority(request: google.cloud.memorystore.v1.IGetCertificateAuthorityRequest, callback: google.cloud.memorystore.v1.Memorystore.GetCertificateAuthorityCallback): void;

Calls GetCertificateAuthority.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IGetCertificateAuthorityRequest](https://docs.cloud.google.com/nodejs/docs/reference/memorystore/latest/memorystore/protos.google.cloud.memorystore.v1.igetcertificateauthorityrequest)`   
GetCertificateAuthorityRequest message or plain object  
`callback` |  `[GetCertificateAuthorityCallback](https://docs.cloud.google.com/nodejs/docs/reference/memorystore/latest/overview.html)`   
Node-style callback called with the error, if any, and CertificateAuthority  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### getCertificateAuthority(request)
    
    
    public getCertificateAuthority(request: google.cloud.memorystore.v1.IGetCertificateAuthorityRequest): Promise<google.cloud.memorystore.v1.CertificateAuthority>;

Calls GetCertificateAuthority.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IGetCertificateAuthorityRequest](https://docs.cloud.google.com/nodejs/docs/reference/memorystore/latest/memorystore/protos.google.cloud.memorystore.v1.igetcertificateauthorityrequest)`   
GetCertificateAuthorityRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.memorystore.v1.CertificateAuthority](https://docs.cloud.google.com/nodejs/docs/reference/memorystore/latest/memorystore/protos.google.cloud.memorystore.v1.certificateauthority-class)>` | Promise  
  
### getInstance(request, callback)
    
    
    public getInstance(request: google.cloud.memorystore.v1.IGetInstanceRequest, callback: google.cloud.memorystore.v1.Memorystore.GetInstanceCallback): void;

Calls GetInstance.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IGetInstanceRequest](https://docs.cloud.google.com/nodejs/docs/reference/memorystore/latest/memorystore/protos.google.cloud.memorystore.v1.igetinstancerequest)`   
GetInstanceRequest message or plain object  
`callback` |  `[GetInstanceCallback](https://docs.cloud.google.com/nodejs/docs/reference/memorystore/latest/overview.html)`   
Node-style callback called with the error, if any, and Instance  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### getInstance(request)
    
    
    public getInstance(request: google.cloud.memorystore.v1.IGetInstanceRequest): Promise<google.cloud.memorystore.v1.Instance>;

Calls GetInstance.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IGetInstanceRequest](https://docs.cloud.google.com/nodejs/docs/reference/memorystore/latest/memorystore/protos.google.cloud.memorystore.v1.igetinstancerequest)`   
GetInstanceRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.memorystore.v1.Instance](https://docs.cloud.google.com/nodejs/docs/reference/memorystore/latest/memorystore/protos.google.cloud.memorystore.v1.instance-class)>` | Promise  
  
### getSharedRegionalCertificateAuthority(request, callback)
    
    
    public getSharedRegionalCertificateAuthority(request: google.cloud.memorystore.v1.IGetSharedRegionalCertificateAuthorityRequest, callback: google.cloud.memorystore.v1.Memorystore.GetSharedRegionalCertificateAuthorityCallback): void;

Calls GetSharedRegionalCertificateAuthority.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IGetSharedRegionalCertificateAuthorityRequest](https://docs.cloud.google.com/nodejs/docs/reference/memorystore/latest/memorystore/protos.google.cloud.memorystore.v1.igetsharedregionalcertificateauthorityrequest)`   
GetSharedRegionalCertificateAuthorityRequest message or plain object  
`callback` |  `[GetSharedRegionalCertificateAuthorityCallback](https://docs.cloud.google.com/nodejs/docs/reference/memorystore/latest/overview.html)`   
Node-style callback called with the error, if any, and SharedRegionalCertificateAuthority  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### getSharedRegionalCertificateAuthority(request)
    
    
    public getSharedRegionalCertificateAuthority(request: google.cloud.memorystore.v1.IGetSharedRegionalCertificateAuthorityRequest): Promise<google.cloud.memorystore.v1.SharedRegionalCertificateAuthority>;

Calls GetSharedRegionalCertificateAuthority.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IGetSharedRegionalCertificateAuthorityRequest](https://docs.cloud.google.com/nodejs/docs/reference/memorystore/latest/memorystore/protos.google.cloud.memorystore.v1.igetsharedregionalcertificateauthorityrequest)`   
GetSharedRegionalCertificateAuthorityRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.memorystore.v1.SharedRegionalCertificateAuthority](https://docs.cloud.google.com/nodejs/docs/reference/memorystore/latest/memorystore/protos.google.cloud.memorystore.v1.sharedregionalcertificateauthority-class)>` | Promise  
  
### getTokenAuthUser(request, callback)
    
    
    public getTokenAuthUser(request: google.cloud.memorystore.v1.IGetTokenAuthUserRequest, callback: google.cloud.memorystore.v1.Memorystore.GetTokenAuthUserCallback): void;

Calls GetTokenAuthUser.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IGetTokenAuthUserRequest](https://docs.cloud.google.com/nodejs/docs/reference/memorystore/latest/memorystore/protos.google.cloud.memorystore.v1.igettokenauthuserrequest)`   
GetTokenAuthUserRequest message or plain object  
`callback` |  `[GetTokenAuthUserCallback](https://docs.cloud.google.com/nodejs/docs/reference/memorystore/latest/overview.html)`   
Node-style callback called with the error, if any, and TokenAuthUser  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### getTokenAuthUser(request)
    
    
    public getTokenAuthUser(request: google.cloud.memorystore.v1.IGetTokenAuthUserRequest): Promise<google.cloud.memorystore.v1.TokenAuthUser>;

Calls GetTokenAuthUser.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IGetTokenAuthUserRequest](https://docs.cloud.google.com/nodejs/docs/reference/memorystore/latest/memorystore/protos.google.cloud.memorystore.v1.igettokenauthuserrequest)`   
GetTokenAuthUserRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.memorystore.v1.TokenAuthUser](https://docs.cloud.google.com/nodejs/docs/reference/memorystore/latest/memorystore/protos.google.cloud.memorystore.v1.tokenauthuser-class)>` | Promise  
  
### listAuthTokens(request, callback)
    
    
    public listAuthTokens(request: google.cloud.memorystore.v1.IListAuthTokensRequest, callback: google.cloud.memorystore.v1.Memorystore.ListAuthTokensCallback): void;

Calls ListAuthTokens.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListAuthTokensRequest](https://docs.cloud.google.com/nodejs/docs/reference/memorystore/latest/memorystore/protos.google.cloud.memorystore.v1.ilistauthtokensrequest)`   
ListAuthTokensRequest message or plain object  
`callback` |  `[ListAuthTokensCallback](https://docs.cloud.google.com/nodejs/docs/reference/memorystore/latest/overview.html)`   
Node-style callback called with the error, if any, and ListAuthTokensResponse  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### listAuthTokens(request)
    
    
    public listAuthTokens(request: google.cloud.memorystore.v1.IListAuthTokensRequest): Promise<google.cloud.memorystore.v1.ListAuthTokensResponse>;

Calls ListAuthTokens.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IListAuthTokensRequest](https://docs.cloud.google.com/nodejs/docs/reference/memorystore/latest/memorystore/protos.google.cloud.memorystore.v1.ilistauthtokensrequest)`   
ListAuthTokensRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.memorystore.v1.ListAuthTokensResponse](https://docs.cloud.google.com/nodejs/docs/reference/memorystore/latest/memorystore/protos.google.cloud.memorystore.v1.listauthtokensresponse)>` | Promise  
  
### listBackupCollections(request, callback)
    
    
    public listBackupCollections(request: google.cloud.memorystore.v1.IListBackupCollectionsRequest, callback: google.cloud.memorystore.v1.Memorystore.ListBackupCollectionsCallback): void;

Calls ListBackupCollections.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListBackupCollectionsRequest](https://docs.cloud.google.com/nodejs/docs/reference/memorystore/latest/memorystore/protos.google.cloud.memorystore.v1.ilistbackupcollectionsrequest)`   
ListBackupCollectionsRequest message or plain object  
`callback` |  `[ListBackupCollectionsCallback](https://docs.cloud.google.com/nodejs/docs/reference/memorystore/latest/overview.html)`   
Node-style callback called with the error, if any, and ListBackupCollectionsResponse  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### listBackupCollections(request)
    
    
    public listBackupCollections(request: google.cloud.memorystore.v1.IListBackupCollectionsRequest): Promise<google.cloud.memorystore.v1.ListBackupCollectionsResponse>;

Calls ListBackupCollections.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IListBackupCollectionsRequest](https://docs.cloud.google.com/nodejs/docs/reference/memorystore/latest/memorystore/protos.google.cloud.memorystore.v1.ilistbackupcollectionsrequest)`   
ListBackupCollectionsRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.memorystore.v1.ListBackupCollectionsResponse](https://docs.cloud.google.com/nodejs/docs/reference/memorystore/latest/memorystore/protos.google.cloud.memorystore.v1.listbackupcollectionsresponse)>` | Promise  
  
### listBackups(request, callback)
    
    
    public listBackups(request: google.cloud.memorystore.v1.IListBackupsRequest, callback: google.cloud.memorystore.v1.Memorystore.ListBackupsCallback): void;

Calls ListBackups.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListBackupsRequest](https://docs.cloud.google.com/nodejs/docs/reference/memorystore/latest/memorystore/protos.google.cloud.memorystore.v1.ilistbackupsrequest)`   
ListBackupsRequest message or plain object  
`callback` |  `[ListBackupsCallback](https://docs.cloud.google.com/nodejs/docs/reference/memorystore/latest/overview.html)`   
Node-style callback called with the error, if any, and ListBackupsResponse  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### listBackups(request)
    
    
    public listBackups(request: google.cloud.memorystore.v1.IListBackupsRequest): Promise<google.cloud.memorystore.v1.ListBackupsResponse>;

Calls ListBackups.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IListBackupsRequest](https://docs.cloud.google.com/nodejs/docs/reference/memorystore/latest/memorystore/protos.google.cloud.memorystore.v1.ilistbackupsrequest)`   
ListBackupsRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.memorystore.v1.ListBackupsResponse](https://docs.cloud.google.com/nodejs/docs/reference/memorystore/latest/memorystore/protos.google.cloud.memorystore.v1.listbackupsresponse)>` | Promise  
  
### listInstances(request, callback)
    
    
    public listInstances(request: google.cloud.memorystore.v1.IListInstancesRequest, callback: google.cloud.memorystore.v1.Memorystore.ListInstancesCallback): void;

Calls ListInstances.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListInstancesRequest](https://docs.cloud.google.com/nodejs/docs/reference/memorystore/latest/memorystore/protos.google.cloud.memorystore.v1.ilistinstancesrequest)`   
ListInstancesRequest message or plain object  
`callback` |  `[ListInstancesCallback](https://docs.cloud.google.com/nodejs/docs/reference/memorystore/latest/overview.html)`   
Node-style callback called with the error, if any, and ListInstancesResponse  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### listInstances(request)
    
    
    public listInstances(request: google.cloud.memorystore.v1.IListInstancesRequest): Promise<google.cloud.memorystore.v1.ListInstancesResponse>;

Calls ListInstances.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IListInstancesRequest](https://docs.cloud.google.com/nodejs/docs/reference/memorystore/latest/memorystore/protos.google.cloud.memorystore.v1.ilistinstancesrequest)`   
ListInstancesRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.memorystore.v1.ListInstancesResponse](https://docs.cloud.google.com/nodejs/docs/reference/memorystore/latest/memorystore/protos.google.cloud.memorystore.v1.listinstancesresponse)>` | Promise  
  
### listTokenAuthUsers(request, callback)
    
    
    public listTokenAuthUsers(request: google.cloud.memorystore.v1.IListTokenAuthUsersRequest, callback: google.cloud.memorystore.v1.Memorystore.ListTokenAuthUsersCallback): void;

Calls ListTokenAuthUsers.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListTokenAuthUsersRequest](https://docs.cloud.google.com/nodejs/docs/reference/memorystore/latest/memorystore/protos.google.cloud.memorystore.v1.ilisttokenauthusersrequest)`   
ListTokenAuthUsersRequest message or plain object  
`callback` |  `[ListTokenAuthUsersCallback](https://docs.cloud.google.com/nodejs/docs/reference/memorystore/latest/overview.html)`   
Node-style callback called with the error, if any, and ListTokenAuthUsersResponse  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### listTokenAuthUsers(request)
    
    
    public listTokenAuthUsers(request: google.cloud.memorystore.v1.IListTokenAuthUsersRequest): Promise<google.cloud.memorystore.v1.ListTokenAuthUsersResponse>;

Calls ListTokenAuthUsers.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IListTokenAuthUsersRequest](https://docs.cloud.google.com/nodejs/docs/reference/memorystore/latest/memorystore/protos.google.cloud.memorystore.v1.ilisttokenauthusersrequest)`   
ListTokenAuthUsersRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.memorystore.v1.ListTokenAuthUsersResponse](https://docs.cloud.google.com/nodejs/docs/reference/memorystore/latest/memorystore/protos.google.cloud.memorystore.v1.listtokenauthusersresponse)>` | Promise  
  
### rescheduleMaintenance(request, callback)
    
    
    public rescheduleMaintenance(request: google.cloud.memorystore.v1.IRescheduleMaintenanceRequest, callback: google.cloud.memorystore.v1.Memorystore.RescheduleMaintenanceCallback): void;

Calls RescheduleMaintenance.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IRescheduleMaintenanceRequest](https://docs.cloud.google.com/nodejs/docs/reference/memorystore/latest/memorystore/protos.google.cloud.memorystore.v1.ireschedulemaintenancerequest)`   
RescheduleMaintenanceRequest message or plain object  
`callback` |  `[RescheduleMaintenanceCallback](https://docs.cloud.google.com/nodejs/docs/reference/memorystore/latest/overview.html)`   
Node-style callback called with the error, if any, and Operation  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### rescheduleMaintenance(request)
    
    
    public rescheduleMaintenance(request: google.cloud.memorystore.v1.IRescheduleMaintenanceRequest): Promise<google.longrunning.Operation>;

Calls RescheduleMaintenance.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IRescheduleMaintenanceRequest](https://docs.cloud.google.com/nodejs/docs/reference/memorystore/latest/memorystore/protos.google.cloud.memorystore.v1.ireschedulemaintenancerequest)`   
RescheduleMaintenanceRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.longrunning.Operation](https://docs.cloud.google.com/nodejs/docs/reference/memorystore/latest/memorystore/protos.google.longrunning.operation)>` | Promise  
  
### startMigration(request, callback)
    
    
    public startMigration(request: google.cloud.memorystore.v1.IStartMigrationRequest, callback: google.cloud.memorystore.v1.Memorystore.StartMigrationCallback): void;

Calls StartMigration.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IStartMigrationRequest](https://docs.cloud.google.com/nodejs/docs/reference/memorystore/latest/memorystore/protos.google.cloud.memorystore.v1.istartmigrationrequest)`   
StartMigrationRequest message or plain object  
`callback` |  `[StartMigrationCallback](https://docs.cloud.google.com/nodejs/docs/reference/memorystore/latest/overview.html)`   
Node-style callback called with the error, if any, and Operation  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### startMigration(request)
    
    
    public startMigration(request: google.cloud.memorystore.v1.IStartMigrationRequest): Promise<google.longrunning.Operation>;

Calls StartMigration.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IStartMigrationRequest](https://docs.cloud.google.com/nodejs/docs/reference/memorystore/latest/memorystore/protos.google.cloud.memorystore.v1.istartmigrationrequest)`   
StartMigrationRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.longrunning.Operation](https://docs.cloud.google.com/nodejs/docs/reference/memorystore/latest/memorystore/protos.google.longrunning.operation)>` | Promise  
  
### updateInstance(request, callback)
    
    
    public updateInstance(request: google.cloud.memorystore.v1.IUpdateInstanceRequest, callback: google.cloud.memorystore.v1.Memorystore.UpdateInstanceCallback): void;

Calls UpdateInstance.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IUpdateInstanceRequest](https://docs.cloud.google.com/nodejs/docs/reference/memorystore/latest/memorystore/protos.google.cloud.memorystore.v1.iupdateinstancerequest)`   
UpdateInstanceRequest message or plain object  
`callback` |  `[UpdateInstanceCallback](https://docs.cloud.google.com/nodejs/docs/reference/memorystore/latest/overview.html)`   
Node-style callback called with the error, if any, and Operation  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### updateInstance(request)
    
    
    public updateInstance(request: google.cloud.memorystore.v1.IUpdateInstanceRequest): Promise<google.longrunning.Operation>;

Calls UpdateInstance.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IUpdateInstanceRequest](https://docs.cloud.google.com/nodejs/docs/reference/memorystore/latest/memorystore/protos.google.cloud.memorystore.v1.iupdateinstancerequest)`   
UpdateInstanceRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.longrunning.Operation](https://docs.cloud.google.com/nodejs/docs/reference/memorystore/latest/memorystore/protos.google.longrunning.operation)>` | Promise  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-02 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-02 UTC."],[],[]] 
