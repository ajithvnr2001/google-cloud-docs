---
url: https://docs.cloud.google.com/nodejs/docs/reference/alloydb/latest/alloydb/protos.google.cloud.alloydb.v1alpha.alloydbadmin-class
title: Class protos.google.cloud.alloydb.v1alpha.AlloyDBAdmin (3.3.1) \u00a0|\u00a0 Node.js client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T17:54:17.044355+00:00
---

# Class protos.google.cloud.alloydb.v1alpha.AlloyDBAdmin (3.3.1)  |  Node.js client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/nodejs/docs/reference/alloydb/latest/alloydb/protos.google.cloud.alloydb.v1alpha.alloydbadmin-class

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Node.js ](https://docs.cloud.google.com/nodejs/docs)
  * [ Client libraries ](https://docs.cloud.google.com/nodejs/docs/reference)



Send feedback 

#  Class protos.google.cloud.alloydb.v1alpha.AlloyDBAdmin (3.3.1) Stay organized with collections  Save and categorize content based on your preferences. 

3.3.1 (latest)  2.7.0  2.6.0  2.5.0  2.4.0  2.3.0  1.10.1  1.9.0  1.6.0  1.4.1  1.3.0  1.2.0  0.1.1 

Represents an AlloyDBAdmin

## Inheritance

$protobuf.rpc.Service > protos.google.cloud.alloydb.v1alpha.AlloyDBAdmin

## Package

[@google-cloud/alloydb](https://docs.cloud.google.com/nodejs/docs/reference/alloydb/latest/overview.html)

## Constructors 

### (constructor)(rpcImpl, requestDelimited, responseDelimited)
    
    
    constructor(rpcImpl: $protobuf.RPCImpl, requestDelimited?: boolean, responseDelimited?: boolean);

Constructs a new AlloyDBAdmin service.

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

### batchCreateInstances(request, callback)
    
    
    public batchCreateInstances(request: google.cloud.alloydb.v1alpha.IBatchCreateInstancesRequest, callback: google.cloud.alloydb.v1alpha.AlloyDBAdmin.BatchCreateInstancesCallback): void;

Calls BatchCreateInstances.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IBatchCreateInstancesRequest](https://docs.cloud.google.com/nodejs/docs/reference/alloydb/latest/alloydb/protos.google.cloud.alloydb.v1alpha.ibatchcreateinstancesrequest)`   
BatchCreateInstancesRequest message or plain object  
`callback` |  `[BatchCreateInstancesCallback](https://docs.cloud.google.com/nodejs/docs/reference/alloydb/latest/overview.html)`   
Node-style callback called with the error, if any, and Operation  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### batchCreateInstances(request)
    
    
    public batchCreateInstances(request: google.cloud.alloydb.v1alpha.IBatchCreateInstancesRequest): Promise<google.longrunning.Operation>;

Calls BatchCreateInstances.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IBatchCreateInstancesRequest](https://docs.cloud.google.com/nodejs/docs/reference/alloydb/latest/alloydb/protos.google.cloud.alloydb.v1alpha.ibatchcreateinstancesrequest)`   
BatchCreateInstancesRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.longrunning.Operation](https://docs.cloud.google.com/nodejs/docs/reference/alloydb/latest/alloydb/protos.google.longrunning.operation)>` | Promise  
  
### create(rpcImpl, requestDelimited, responseDelimited)
    
    
    public static create(rpcImpl: $protobuf.RPCImpl, requestDelimited?: boolean, responseDelimited?: boolean): AlloyDBAdmin;

Creates new AlloyDBAdmin service using the specified rpc implementation.

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
`[AlloyDBAdmin](https://docs.cloud.google.com/nodejs/docs/reference/alloydb/latest/alloydb/protos.google.cloud.alloydb.v1alpha.alloydbadmin-class)` | RPC service. Useful where requests and/or responses are streamed.  
  
### createBackup(request, callback)
    
    
    public createBackup(request: google.cloud.alloydb.v1alpha.ICreateBackupRequest, callback: google.cloud.alloydb.v1alpha.AlloyDBAdmin.CreateBackupCallback): void;

Calls CreateBackup.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[ICreateBackupRequest](https://docs.cloud.google.com/nodejs/docs/reference/alloydb/latest/alloydb/protos.google.cloud.alloydb.v1alpha.icreatebackuprequest)`   
CreateBackupRequest message or plain object  
`callback` |  `[CreateBackupCallback](https://docs.cloud.google.com/nodejs/docs/reference/alloydb/latest/overview.html)`   
Node-style callback called with the error, if any, and Operation  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### createBackup(request)
    
    
    public createBackup(request: google.cloud.alloydb.v1alpha.ICreateBackupRequest): Promise<google.longrunning.Operation>;

Calls CreateBackup.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[ICreateBackupRequest](https://docs.cloud.google.com/nodejs/docs/reference/alloydb/latest/alloydb/protos.google.cloud.alloydb.v1alpha.icreatebackuprequest)`   
CreateBackupRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.longrunning.Operation](https://docs.cloud.google.com/nodejs/docs/reference/alloydb/latest/alloydb/protos.google.longrunning.operation)>` | Promise  
  
### createCluster(request, callback)
    
    
    public createCluster(request: google.cloud.alloydb.v1alpha.ICreateClusterRequest, callback: google.cloud.alloydb.v1alpha.AlloyDBAdmin.CreateClusterCallback): void;

Calls CreateCluster.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[ICreateClusterRequest](https://docs.cloud.google.com/nodejs/docs/reference/alloydb/latest/alloydb/protos.google.cloud.alloydb.v1alpha.icreateclusterrequest)`   
CreateClusterRequest message or plain object  
`callback` |  `[CreateClusterCallback](https://docs.cloud.google.com/nodejs/docs/reference/alloydb/latest/overview.html)`   
Node-style callback called with the error, if any, and Operation  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### createCluster(request)
    
    
    public createCluster(request: google.cloud.alloydb.v1alpha.ICreateClusterRequest): Promise<google.longrunning.Operation>;

Calls CreateCluster.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[ICreateClusterRequest](https://docs.cloud.google.com/nodejs/docs/reference/alloydb/latest/alloydb/protos.google.cloud.alloydb.v1alpha.icreateclusterrequest)`   
CreateClusterRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.longrunning.Operation](https://docs.cloud.google.com/nodejs/docs/reference/alloydb/latest/alloydb/protos.google.longrunning.operation)>` | Promise  
  
### createDatabase(request, callback)
    
    
    public createDatabase(request: google.cloud.alloydb.v1alpha.ICreateDatabaseRequest, callback: google.cloud.alloydb.v1alpha.AlloyDBAdmin.CreateDatabaseCallback): void;

Calls CreateDatabase.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[ICreateDatabaseRequest](https://docs.cloud.google.com/nodejs/docs/reference/alloydb/latest/alloydb/protos.google.cloud.alloydb.v1alpha.icreatedatabaserequest)`   
CreateDatabaseRequest message or plain object  
`callback` |  `[CreateDatabaseCallback](https://docs.cloud.google.com/nodejs/docs/reference/alloydb/latest/overview.html)`   
Node-style callback called with the error, if any, and Database  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### createDatabase(request)
    
    
    public createDatabase(request: google.cloud.alloydb.v1alpha.ICreateDatabaseRequest): Promise<google.cloud.alloydb.v1alpha.Database>;

Calls CreateDatabase.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[ICreateDatabaseRequest](https://docs.cloud.google.com/nodejs/docs/reference/alloydb/latest/alloydb/protos.google.cloud.alloydb.v1alpha.icreatedatabaserequest)`   
CreateDatabaseRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.alloydb.v1alpha.Database](https://docs.cloud.google.com/nodejs/docs/reference/alloydb/latest/alloydb/protos.google.cloud.alloydb.v1alpha.database)>` | Promise  
  
### createInstance(request, callback)
    
    
    public createInstance(request: google.cloud.alloydb.v1alpha.ICreateInstanceRequest, callback: google.cloud.alloydb.v1alpha.AlloyDBAdmin.CreateInstanceCallback): void;

Calls CreateInstance.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[ICreateInstanceRequest](https://docs.cloud.google.com/nodejs/docs/reference/alloydb/latest/alloydb/protos.google.cloud.alloydb.v1alpha.icreateinstancerequest)`   
CreateInstanceRequest message or plain object  
`callback` |  `[CreateInstanceCallback](https://docs.cloud.google.com/nodejs/docs/reference/alloydb/latest/overview.html)`   
Node-style callback called with the error, if any, and Operation  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### createInstance(request)
    
    
    public createInstance(request: google.cloud.alloydb.v1alpha.ICreateInstanceRequest): Promise<google.longrunning.Operation>;

Calls CreateInstance.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[ICreateInstanceRequest](https://docs.cloud.google.com/nodejs/docs/reference/alloydb/latest/alloydb/protos.google.cloud.alloydb.v1alpha.icreateinstancerequest)`   
CreateInstanceRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.longrunning.Operation](https://docs.cloud.google.com/nodejs/docs/reference/alloydb/latest/alloydb/protos.google.longrunning.operation)>` | Promise  
  
### createSecondaryCluster(request, callback)
    
    
    public createSecondaryCluster(request: google.cloud.alloydb.v1alpha.ICreateSecondaryClusterRequest, callback: google.cloud.alloydb.v1alpha.AlloyDBAdmin.CreateSecondaryClusterCallback): void;

Calls CreateSecondaryCluster.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[ICreateSecondaryClusterRequest](https://docs.cloud.google.com/nodejs/docs/reference/alloydb/latest/alloydb/protos.google.cloud.alloydb.v1alpha.icreatesecondaryclusterrequest)`   
CreateSecondaryClusterRequest message or plain object  
`callback` |  `[CreateSecondaryClusterCallback](https://docs.cloud.google.com/nodejs/docs/reference/alloydb/latest/overview.html)`   
Node-style callback called with the error, if any, and Operation  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### createSecondaryCluster(request)
    
    
    public createSecondaryCluster(request: google.cloud.alloydb.v1alpha.ICreateSecondaryClusterRequest): Promise<google.longrunning.Operation>;

Calls CreateSecondaryCluster.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[ICreateSecondaryClusterRequest](https://docs.cloud.google.com/nodejs/docs/reference/alloydb/latest/alloydb/protos.google.cloud.alloydb.v1alpha.icreatesecondaryclusterrequest)`   
CreateSecondaryClusterRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.longrunning.Operation](https://docs.cloud.google.com/nodejs/docs/reference/alloydb/latest/alloydb/protos.google.longrunning.operation)>` | Promise  
  
### createSecondaryInstance(request, callback)
    
    
    public createSecondaryInstance(request: google.cloud.alloydb.v1alpha.ICreateSecondaryInstanceRequest, callback: google.cloud.alloydb.v1alpha.AlloyDBAdmin.CreateSecondaryInstanceCallback): void;

Calls CreateSecondaryInstance.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[ICreateSecondaryInstanceRequest](https://docs.cloud.google.com/nodejs/docs/reference/alloydb/latest/alloydb/protos.google.cloud.alloydb.v1alpha.icreatesecondaryinstancerequest)`   
CreateSecondaryInstanceRequest message or plain object  
`callback` |  `[CreateSecondaryInstanceCallback](https://docs.cloud.google.com/nodejs/docs/reference/alloydb/latest/overview.html)`   
Node-style callback called with the error, if any, and Operation  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### createSecondaryInstance(request)
    
    
    public createSecondaryInstance(request: google.cloud.alloydb.v1alpha.ICreateSecondaryInstanceRequest): Promise<google.longrunning.Operation>;

Calls CreateSecondaryInstance.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[ICreateSecondaryInstanceRequest](https://docs.cloud.google.com/nodejs/docs/reference/alloydb/latest/alloydb/protos.google.cloud.alloydb.v1alpha.icreatesecondaryinstancerequest)`   
CreateSecondaryInstanceRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.longrunning.Operation](https://docs.cloud.google.com/nodejs/docs/reference/alloydb/latest/alloydb/protos.google.longrunning.operation)>` | Promise  
  
### createUser(request, callback)
    
    
    public createUser(request: google.cloud.alloydb.v1alpha.ICreateUserRequest, callback: google.cloud.alloydb.v1alpha.AlloyDBAdmin.CreateUserCallback): void;

Calls CreateUser.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[ICreateUserRequest](https://docs.cloud.google.com/nodejs/docs/reference/alloydb/latest/alloydb/protos.google.cloud.alloydb.v1alpha.icreateuserrequest)`   
CreateUserRequest message or plain object  
`callback` |  `[CreateUserCallback](https://docs.cloud.google.com/nodejs/docs/reference/alloydb/latest/overview.html)`   
Node-style callback called with the error, if any, and User  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### createUser(request)
    
    
    public createUser(request: google.cloud.alloydb.v1alpha.ICreateUserRequest): Promise<google.cloud.alloydb.v1alpha.User>;

Calls CreateUser.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[ICreateUserRequest](https://docs.cloud.google.com/nodejs/docs/reference/alloydb/latest/alloydb/protos.google.cloud.alloydb.v1alpha.icreateuserrequest)`   
CreateUserRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.alloydb.v1alpha.User](https://docs.cloud.google.com/nodejs/docs/reference/alloydb/latest/alloydb/protos.google.cloud.alloydb.v1alpha.user-class)>` | Promise  
  
### deleteBackup(request, callback)
    
    
    public deleteBackup(request: google.cloud.alloydb.v1alpha.IDeleteBackupRequest, callback: google.cloud.alloydb.v1alpha.AlloyDBAdmin.DeleteBackupCallback): void;

Calls DeleteBackup.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IDeleteBackupRequest](https://docs.cloud.google.com/nodejs/docs/reference/alloydb/latest/alloydb/protos.google.cloud.alloydb.v1alpha.ideletebackuprequest)`   
DeleteBackupRequest message or plain object  
`callback` |  `[DeleteBackupCallback](https://docs.cloud.google.com/nodejs/docs/reference/alloydb/latest/overview.html)`   
Node-style callback called with the error, if any, and Operation  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### deleteBackup(request)
    
    
    public deleteBackup(request: google.cloud.alloydb.v1alpha.IDeleteBackupRequest): Promise<google.longrunning.Operation>;

Calls DeleteBackup.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IDeleteBackupRequest](https://docs.cloud.google.com/nodejs/docs/reference/alloydb/latest/alloydb/protos.google.cloud.alloydb.v1alpha.ideletebackuprequest)`   
DeleteBackupRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.longrunning.Operation](https://docs.cloud.google.com/nodejs/docs/reference/alloydb/latest/alloydb/protos.google.longrunning.operation)>` | Promise  
  
### deleteCluster(request, callback)
    
    
    public deleteCluster(request: google.cloud.alloydb.v1alpha.IDeleteClusterRequest, callback: google.cloud.alloydb.v1alpha.AlloyDBAdmin.DeleteClusterCallback): void;

Calls DeleteCluster.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IDeleteClusterRequest](https://docs.cloud.google.com/nodejs/docs/reference/alloydb/latest/alloydb/protos.google.cloud.alloydb.v1alpha.ideleteclusterrequest)`   
DeleteClusterRequest message or plain object  
`callback` |  `[DeleteClusterCallback](https://docs.cloud.google.com/nodejs/docs/reference/alloydb/latest/overview.html)`   
Node-style callback called with the error, if any, and Operation  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### deleteCluster(request)
    
    
    public deleteCluster(request: google.cloud.alloydb.v1alpha.IDeleteClusterRequest): Promise<google.longrunning.Operation>;

Calls DeleteCluster.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IDeleteClusterRequest](https://docs.cloud.google.com/nodejs/docs/reference/alloydb/latest/alloydb/protos.google.cloud.alloydb.v1alpha.ideleteclusterrequest)`   
DeleteClusterRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.longrunning.Operation](https://docs.cloud.google.com/nodejs/docs/reference/alloydb/latest/alloydb/protos.google.longrunning.operation)>` | Promise  
  
### deleteInstance(request, callback)
    
    
    public deleteInstance(request: google.cloud.alloydb.v1alpha.IDeleteInstanceRequest, callback: google.cloud.alloydb.v1alpha.AlloyDBAdmin.DeleteInstanceCallback): void;

Calls DeleteInstance.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IDeleteInstanceRequest](https://docs.cloud.google.com/nodejs/docs/reference/alloydb/latest/alloydb/protos.google.cloud.alloydb.v1alpha.ideleteinstancerequest)`   
DeleteInstanceRequest message or plain object  
`callback` |  `[DeleteInstanceCallback](https://docs.cloud.google.com/nodejs/docs/reference/alloydb/latest/overview.html)`   
Node-style callback called with the error, if any, and Operation  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### deleteInstance(request)
    
    
    public deleteInstance(request: google.cloud.alloydb.v1alpha.IDeleteInstanceRequest): Promise<google.longrunning.Operation>;

Calls DeleteInstance.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IDeleteInstanceRequest](https://docs.cloud.google.com/nodejs/docs/reference/alloydb/latest/alloydb/protos.google.cloud.alloydb.v1alpha.ideleteinstancerequest)`   
DeleteInstanceRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.longrunning.Operation](https://docs.cloud.google.com/nodejs/docs/reference/alloydb/latest/alloydb/protos.google.longrunning.operation)>` | Promise  
  
### deleteUser(request, callback)
    
    
    public deleteUser(request: google.cloud.alloydb.v1alpha.IDeleteUserRequest, callback: google.cloud.alloydb.v1alpha.AlloyDBAdmin.DeleteUserCallback): void;

Calls DeleteUser.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IDeleteUserRequest](https://docs.cloud.google.com/nodejs/docs/reference/alloydb/latest/alloydb/protos.google.cloud.alloydb.v1alpha.ideleteuserrequest)`   
DeleteUserRequest message or plain object  
`callback` |  `[DeleteUserCallback](https://docs.cloud.google.com/nodejs/docs/reference/alloydb/latest/overview.html)`   
Node-style callback called with the error, if any, and Empty  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### deleteUser(request)
    
    
    public deleteUser(request: google.cloud.alloydb.v1alpha.IDeleteUserRequest): Promise<google.protobuf.Empty>;

Calls DeleteUser.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IDeleteUserRequest](https://docs.cloud.google.com/nodejs/docs/reference/alloydb/latest/alloydb/protos.google.cloud.alloydb.v1alpha.ideleteuserrequest)`   
DeleteUserRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.protobuf.Empty](https://docs.cloud.google.com/nodejs/docs/reference/alloydb/latest/alloydb/protos.google.protobuf.empty)>` | Promise  
  
### executeSql(request, callback)
    
    
    public executeSql(request: google.cloud.alloydb.v1alpha.IExecuteSqlRequest, callback: google.cloud.alloydb.v1alpha.AlloyDBAdmin.ExecuteSqlCallback): void;

Calls ExecuteSql.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IExecuteSqlRequest](https://docs.cloud.google.com/nodejs/docs/reference/alloydb/latest/alloydb/protos.google.cloud.alloydb.v1alpha.iexecutesqlrequest)`   
ExecuteSqlRequest message or plain object  
`callback` |  `[ExecuteSqlCallback](https://docs.cloud.google.com/nodejs/docs/reference/alloydb/latest/overview.html)`   
Node-style callback called with the error, if any, and ExecuteSqlResponse  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### executeSql(request)
    
    
    public executeSql(request: google.cloud.alloydb.v1alpha.IExecuteSqlRequest): Promise<google.cloud.alloydb.v1alpha.ExecuteSqlResponse>;

Calls ExecuteSql.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IExecuteSqlRequest](https://docs.cloud.google.com/nodejs/docs/reference/alloydb/latest/alloydb/protos.google.cloud.alloydb.v1alpha.iexecutesqlrequest)`   
ExecuteSqlRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.alloydb.v1alpha.ExecuteSqlResponse](https://docs.cloud.google.com/nodejs/docs/reference/alloydb/latest/alloydb/protos.google.cloud.alloydb.v1alpha.executesqlresponse)>` | Promise  
  
### exportCluster(request, callback)
    
    
    public exportCluster(request: google.cloud.alloydb.v1alpha.IExportClusterRequest, callback: google.cloud.alloydb.v1alpha.AlloyDBAdmin.ExportClusterCallback): void;

Calls ExportCluster.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IExportClusterRequest](https://docs.cloud.google.com/nodejs/docs/reference/alloydb/latest/alloydb/protos.google.cloud.alloydb.v1alpha.iexportclusterrequest)`   
ExportClusterRequest message or plain object  
`callback` |  `[ExportClusterCallback](https://docs.cloud.google.com/nodejs/docs/reference/alloydb/latest/overview.html)`   
Node-style callback called with the error, if any, and Operation  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### exportCluster(request)
    
    
    public exportCluster(request: google.cloud.alloydb.v1alpha.IExportClusterRequest): Promise<google.longrunning.Operation>;

Calls ExportCluster.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IExportClusterRequest](https://docs.cloud.google.com/nodejs/docs/reference/alloydb/latest/alloydb/protos.google.cloud.alloydb.v1alpha.iexportclusterrequest)`   
ExportClusterRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.longrunning.Operation](https://docs.cloud.google.com/nodejs/docs/reference/alloydb/latest/alloydb/protos.google.longrunning.operation)>` | Promise  
  
### failoverInstance(request, callback)
    
    
    public failoverInstance(request: google.cloud.alloydb.v1alpha.IFailoverInstanceRequest, callback: google.cloud.alloydb.v1alpha.AlloyDBAdmin.FailoverInstanceCallback): void;

Calls FailoverInstance.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IFailoverInstanceRequest](https://docs.cloud.google.com/nodejs/docs/reference/alloydb/latest/alloydb/protos.google.cloud.alloydb.v1alpha.ifailoverinstancerequest)`   
FailoverInstanceRequest message or plain object  
`callback` |  `[FailoverInstanceCallback](https://docs.cloud.google.com/nodejs/docs/reference/alloydb/latest/overview.html)`   
Node-style callback called with the error, if any, and Operation  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### failoverInstance(request)
    
    
    public failoverInstance(request: google.cloud.alloydb.v1alpha.IFailoverInstanceRequest): Promise<google.longrunning.Operation>;

Calls FailoverInstance.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IFailoverInstanceRequest](https://docs.cloud.google.com/nodejs/docs/reference/alloydb/latest/alloydb/protos.google.cloud.alloydb.v1alpha.ifailoverinstancerequest)`   
FailoverInstanceRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.longrunning.Operation](https://docs.cloud.google.com/nodejs/docs/reference/alloydb/latest/alloydb/protos.google.longrunning.operation)>` | Promise  
  
### generateClientCertificate(request, callback)
    
    
    public generateClientCertificate(request: google.cloud.alloydb.v1alpha.IGenerateClientCertificateRequest, callback: google.cloud.alloydb.v1alpha.AlloyDBAdmin.GenerateClientCertificateCallback): void;

Calls GenerateClientCertificate.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IGenerateClientCertificateRequest](https://docs.cloud.google.com/nodejs/docs/reference/alloydb/latest/alloydb/protos.google.cloud.alloydb.v1alpha.igenerateclientcertificaterequest)`   
GenerateClientCertificateRequest message or plain object  
`callback` |  `[GenerateClientCertificateCallback](https://docs.cloud.google.com/nodejs/docs/reference/alloydb/latest/overview.html)`   
Node-style callback called with the error, if any, and GenerateClientCertificateResponse  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### generateClientCertificate(request)
    
    
    public generateClientCertificate(request: google.cloud.alloydb.v1alpha.IGenerateClientCertificateRequest): Promise<google.cloud.alloydb.v1alpha.GenerateClientCertificateResponse>;

Calls GenerateClientCertificate.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IGenerateClientCertificateRequest](https://docs.cloud.google.com/nodejs/docs/reference/alloydb/latest/alloydb/protos.google.cloud.alloydb.v1alpha.igenerateclientcertificaterequest)`   
GenerateClientCertificateRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.alloydb.v1alpha.GenerateClientCertificateResponse](https://docs.cloud.google.com/nodejs/docs/reference/alloydb/latest/alloydb/protos.google.cloud.alloydb.v1alpha.generateclientcertificateresponse)>` | Promise  
  
### getBackup(request, callback)
    
    
    public getBackup(request: google.cloud.alloydb.v1alpha.IGetBackupRequest, callback: google.cloud.alloydb.v1alpha.AlloyDBAdmin.GetBackupCallback): void;

Calls GetBackup.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IGetBackupRequest](https://docs.cloud.google.com/nodejs/docs/reference/alloydb/latest/alloydb/protos.google.cloud.alloydb.v1alpha.igetbackuprequest)`   
GetBackupRequest message or plain object  
`callback` |  `[GetBackupCallback](https://docs.cloud.google.com/nodejs/docs/reference/alloydb/latest/overview.html)`   
Node-style callback called with the error, if any, and Backup  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### getBackup(request)
    
    
    public getBackup(request: google.cloud.alloydb.v1alpha.IGetBackupRequest): Promise<google.cloud.alloydb.v1alpha.Backup>;

Calls GetBackup.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IGetBackupRequest](https://docs.cloud.google.com/nodejs/docs/reference/alloydb/latest/alloydb/protos.google.cloud.alloydb.v1alpha.igetbackuprequest)`   
GetBackupRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.alloydb.v1alpha.Backup](https://docs.cloud.google.com/nodejs/docs/reference/alloydb/latest/alloydb/protos.google.cloud.alloydb.v1alpha.backup-class)>` | Promise  
  
### getCluster(request, callback)
    
    
    public getCluster(request: google.cloud.alloydb.v1alpha.IGetClusterRequest, callback: google.cloud.alloydb.v1alpha.AlloyDBAdmin.GetClusterCallback): void;

Calls GetCluster.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IGetClusterRequest](https://docs.cloud.google.com/nodejs/docs/reference/alloydb/latest/alloydb/protos.google.cloud.alloydb.v1alpha.igetclusterrequest)`   
GetClusterRequest message or plain object  
`callback` |  `[GetClusterCallback](https://docs.cloud.google.com/nodejs/docs/reference/alloydb/latest/overview.html)`   
Node-style callback called with the error, if any, and Cluster  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### getCluster(request)
    
    
    public getCluster(request: google.cloud.alloydb.v1alpha.IGetClusterRequest): Promise<google.cloud.alloydb.v1alpha.Cluster>;

Calls GetCluster.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IGetClusterRequest](https://docs.cloud.google.com/nodejs/docs/reference/alloydb/latest/alloydb/protos.google.cloud.alloydb.v1alpha.igetclusterrequest)`   
GetClusterRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.alloydb.v1alpha.Cluster](https://docs.cloud.google.com/nodejs/docs/reference/alloydb/latest/alloydb/protos.google.cloud.alloydb.v1alpha.cluster-class)>` | Promise  
  
### getConnectionInfo(request, callback)
    
    
    public getConnectionInfo(request: google.cloud.alloydb.v1alpha.IGetConnectionInfoRequest, callback: google.cloud.alloydb.v1alpha.AlloyDBAdmin.GetConnectionInfoCallback): void;

Calls GetConnectionInfo.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IGetConnectionInfoRequest](https://docs.cloud.google.com/nodejs/docs/reference/alloydb/latest/alloydb/protos.google.cloud.alloydb.v1alpha.igetconnectioninforequest)`   
GetConnectionInfoRequest message or plain object  
`callback` |  `[GetConnectionInfoCallback](https://docs.cloud.google.com/nodejs/docs/reference/alloydb/latest/overview.html)`   
Node-style callback called with the error, if any, and ConnectionInfo  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### getConnectionInfo(request)
    
    
    public getConnectionInfo(request: google.cloud.alloydb.v1alpha.IGetConnectionInfoRequest): Promise<google.cloud.alloydb.v1alpha.ConnectionInfo>;

Calls GetConnectionInfo.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IGetConnectionInfoRequest](https://docs.cloud.google.com/nodejs/docs/reference/alloydb/latest/alloydb/protos.google.cloud.alloydb.v1alpha.igetconnectioninforequest)`   
GetConnectionInfoRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.alloydb.v1alpha.ConnectionInfo](https://docs.cloud.google.com/nodejs/docs/reference/alloydb/latest/alloydb/protos.google.cloud.alloydb.v1alpha.connectioninfo)>` | Promise  
  
### getInstance(request, callback)
    
    
    public getInstance(request: google.cloud.alloydb.v1alpha.IGetInstanceRequest, callback: google.cloud.alloydb.v1alpha.AlloyDBAdmin.GetInstanceCallback): void;

Calls GetInstance.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IGetInstanceRequest](https://docs.cloud.google.com/nodejs/docs/reference/alloydb/latest/alloydb/protos.google.cloud.alloydb.v1alpha.igetinstancerequest)`   
GetInstanceRequest message or plain object  
`callback` |  `[GetInstanceCallback](https://docs.cloud.google.com/nodejs/docs/reference/alloydb/latest/overview.html)`   
Node-style callback called with the error, if any, and Instance  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### getInstance(request)
    
    
    public getInstance(request: google.cloud.alloydb.v1alpha.IGetInstanceRequest): Promise<google.cloud.alloydb.v1alpha.Instance>;

Calls GetInstance.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IGetInstanceRequest](https://docs.cloud.google.com/nodejs/docs/reference/alloydb/latest/alloydb/protos.google.cloud.alloydb.v1alpha.igetinstancerequest)`   
GetInstanceRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.alloydb.v1alpha.Instance](https://docs.cloud.google.com/nodejs/docs/reference/alloydb/latest/alloydb/protos.google.cloud.alloydb.v1alpha.instance-class)>` | Promise  
  
### getUser(request, callback)
    
    
    public getUser(request: google.cloud.alloydb.v1alpha.IGetUserRequest, callback: google.cloud.alloydb.v1alpha.AlloyDBAdmin.GetUserCallback): void;

Calls GetUser.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IGetUserRequest](https://docs.cloud.google.com/nodejs/docs/reference/alloydb/latest/alloydb/protos.google.cloud.alloydb.v1alpha.igetuserrequest)`   
GetUserRequest message or plain object  
`callback` |  `[GetUserCallback](https://docs.cloud.google.com/nodejs/docs/reference/alloydb/latest/overview.html)`   
Node-style callback called with the error, if any, and User  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### getUser(request)
    
    
    public getUser(request: google.cloud.alloydb.v1alpha.IGetUserRequest): Promise<google.cloud.alloydb.v1alpha.User>;

Calls GetUser.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IGetUserRequest](https://docs.cloud.google.com/nodejs/docs/reference/alloydb/latest/alloydb/protos.google.cloud.alloydb.v1alpha.igetuserrequest)`   
GetUserRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.alloydb.v1alpha.User](https://docs.cloud.google.com/nodejs/docs/reference/alloydb/latest/alloydb/protos.google.cloud.alloydb.v1alpha.user-class)>` | Promise  
  
### importCluster(request, callback)
    
    
    public importCluster(request: google.cloud.alloydb.v1alpha.IImportClusterRequest, callback: google.cloud.alloydb.v1alpha.AlloyDBAdmin.ImportClusterCallback): void;

Calls ImportCluster.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IImportClusterRequest](https://docs.cloud.google.com/nodejs/docs/reference/alloydb/latest/alloydb/protos.google.cloud.alloydb.v1alpha.iimportclusterrequest)`   
ImportClusterRequest message or plain object  
`callback` |  `[ImportClusterCallback](https://docs.cloud.google.com/nodejs/docs/reference/alloydb/latest/overview.html)`   
Node-style callback called with the error, if any, and Operation  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### importCluster(request)
    
    
    public importCluster(request: google.cloud.alloydb.v1alpha.IImportClusterRequest): Promise<google.longrunning.Operation>;

Calls ImportCluster.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IImportClusterRequest](https://docs.cloud.google.com/nodejs/docs/reference/alloydb/latest/alloydb/protos.google.cloud.alloydb.v1alpha.iimportclusterrequest)`   
ImportClusterRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.longrunning.Operation](https://docs.cloud.google.com/nodejs/docs/reference/alloydb/latest/alloydb/protos.google.longrunning.operation)>` | Promise  
  
### injectFault(request, callback)
    
    
    public injectFault(request: google.cloud.alloydb.v1alpha.IInjectFaultRequest, callback: google.cloud.alloydb.v1alpha.AlloyDBAdmin.InjectFaultCallback): void;

Calls InjectFault.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IInjectFaultRequest](https://docs.cloud.google.com/nodejs/docs/reference/alloydb/latest/alloydb/protos.google.cloud.alloydb.v1alpha.iinjectfaultrequest)`   
InjectFaultRequest message or plain object  
`callback` |  `[InjectFaultCallback](https://docs.cloud.google.com/nodejs/docs/reference/alloydb/latest/overview.html)`   
Node-style callback called with the error, if any, and Operation  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### injectFault(request)
    
    
    public injectFault(request: google.cloud.alloydb.v1alpha.IInjectFaultRequest): Promise<google.longrunning.Operation>;

Calls InjectFault.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IInjectFaultRequest](https://docs.cloud.google.com/nodejs/docs/reference/alloydb/latest/alloydb/protos.google.cloud.alloydb.v1alpha.iinjectfaultrequest)`   
InjectFaultRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.longrunning.Operation](https://docs.cloud.google.com/nodejs/docs/reference/alloydb/latest/alloydb/protos.google.longrunning.operation)>` | Promise  
  
### listBackups(request, callback)
    
    
    public listBackups(request: google.cloud.alloydb.v1alpha.IListBackupsRequest, callback: google.cloud.alloydb.v1alpha.AlloyDBAdmin.ListBackupsCallback): void;

Calls ListBackups.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListBackupsRequest](https://docs.cloud.google.com/nodejs/docs/reference/alloydb/latest/alloydb/protos.google.cloud.alloydb.v1alpha.ilistbackupsrequest)`   
ListBackupsRequest message or plain object  
`callback` |  `[ListBackupsCallback](https://docs.cloud.google.com/nodejs/docs/reference/alloydb/latest/overview.html)`   
Node-style callback called with the error, if any, and ListBackupsResponse  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### listBackups(request)
    
    
    public listBackups(request: google.cloud.alloydb.v1alpha.IListBackupsRequest): Promise<google.cloud.alloydb.v1alpha.ListBackupsResponse>;

Calls ListBackups.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IListBackupsRequest](https://docs.cloud.google.com/nodejs/docs/reference/alloydb/latest/alloydb/protos.google.cloud.alloydb.v1alpha.ilistbackupsrequest)`   
ListBackupsRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.alloydb.v1alpha.ListBackupsResponse](https://docs.cloud.google.com/nodejs/docs/reference/alloydb/latest/alloydb/protos.google.cloud.alloydb.v1alpha.listbackupsresponse)>` | Promise  
  
### listClusters(request, callback)
    
    
    public listClusters(request: google.cloud.alloydb.v1alpha.IListClustersRequest, callback: google.cloud.alloydb.v1alpha.AlloyDBAdmin.ListClustersCallback): void;

Calls ListClusters.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListClustersRequest](https://docs.cloud.google.com/nodejs/docs/reference/alloydb/latest/alloydb/protos.google.cloud.alloydb.v1alpha.ilistclustersrequest)`   
ListClustersRequest message or plain object  
`callback` |  `[ListClustersCallback](https://docs.cloud.google.com/nodejs/docs/reference/alloydb/latest/overview.html)`   
Node-style callback called with the error, if any, and ListClustersResponse  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### listClusters(request)
    
    
    public listClusters(request: google.cloud.alloydb.v1alpha.IListClustersRequest): Promise<google.cloud.alloydb.v1alpha.ListClustersResponse>;

Calls ListClusters.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IListClustersRequest](https://docs.cloud.google.com/nodejs/docs/reference/alloydb/latest/alloydb/protos.google.cloud.alloydb.v1alpha.ilistclustersrequest)`   
ListClustersRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.alloydb.v1alpha.ListClustersResponse](https://docs.cloud.google.com/nodejs/docs/reference/alloydb/latest/alloydb/protos.google.cloud.alloydb.v1alpha.listclustersresponse)>` | Promise  
  
### listDatabases(request, callback)
    
    
    public listDatabases(request: google.cloud.alloydb.v1alpha.IListDatabasesRequest, callback: google.cloud.alloydb.v1alpha.AlloyDBAdmin.ListDatabasesCallback): void;

Calls ListDatabases.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListDatabasesRequest](https://docs.cloud.google.com/nodejs/docs/reference/alloydb/latest/alloydb/protos.google.cloud.alloydb.v1alpha.ilistdatabasesrequest)`   
ListDatabasesRequest message or plain object  
`callback` |  `[ListDatabasesCallback](https://docs.cloud.google.com/nodejs/docs/reference/alloydb/latest/overview.html)`   
Node-style callback called with the error, if any, and ListDatabasesResponse  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### listDatabases(request)
    
    
    public listDatabases(request: google.cloud.alloydb.v1alpha.IListDatabasesRequest): Promise<google.cloud.alloydb.v1alpha.ListDatabasesResponse>;

Calls ListDatabases.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IListDatabasesRequest](https://docs.cloud.google.com/nodejs/docs/reference/alloydb/latest/alloydb/protos.google.cloud.alloydb.v1alpha.ilistdatabasesrequest)`   
ListDatabasesRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.alloydb.v1alpha.ListDatabasesResponse](https://docs.cloud.google.com/nodejs/docs/reference/alloydb/latest/alloydb/protos.google.cloud.alloydb.v1alpha.listdatabasesresponse)>` | Promise  
  
### listInstances(request, callback)
    
    
    public listInstances(request: google.cloud.alloydb.v1alpha.IListInstancesRequest, callback: google.cloud.alloydb.v1alpha.AlloyDBAdmin.ListInstancesCallback): void;

Calls ListInstances.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListInstancesRequest](https://docs.cloud.google.com/nodejs/docs/reference/alloydb/latest/alloydb/protos.google.cloud.alloydb.v1alpha.ilistinstancesrequest)`   
ListInstancesRequest message or plain object  
`callback` |  `[ListInstancesCallback](https://docs.cloud.google.com/nodejs/docs/reference/alloydb/latest/overview.html)`   
Node-style callback called with the error, if any, and ListInstancesResponse  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### listInstances(request)
    
    
    public listInstances(request: google.cloud.alloydb.v1alpha.IListInstancesRequest): Promise<google.cloud.alloydb.v1alpha.ListInstancesResponse>;

Calls ListInstances.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IListInstancesRequest](https://docs.cloud.google.com/nodejs/docs/reference/alloydb/latest/alloydb/protos.google.cloud.alloydb.v1alpha.ilistinstancesrequest)`   
ListInstancesRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.alloydb.v1alpha.ListInstancesResponse](https://docs.cloud.google.com/nodejs/docs/reference/alloydb/latest/alloydb/protos.google.cloud.alloydb.v1alpha.listinstancesresponse)>` | Promise  
  
### listSupportedDatabaseFlags(request, callback)
    
    
    public listSupportedDatabaseFlags(request: google.cloud.alloydb.v1alpha.IListSupportedDatabaseFlagsRequest, callback: google.cloud.alloydb.v1alpha.AlloyDBAdmin.ListSupportedDatabaseFlagsCallback): void;

Calls ListSupportedDatabaseFlags.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListSupportedDatabaseFlagsRequest](https://docs.cloud.google.com/nodejs/docs/reference/alloydb/latest/alloydb/protos.google.cloud.alloydb.v1alpha.ilistsupporteddatabaseflagsrequest)`   
ListSupportedDatabaseFlagsRequest message or plain object  
`callback` |  `[ListSupportedDatabaseFlagsCallback](https://docs.cloud.google.com/nodejs/docs/reference/alloydb/latest/overview.html)`   
Node-style callback called with the error, if any, and ListSupportedDatabaseFlagsResponse  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### listSupportedDatabaseFlags(request)
    
    
    public listSupportedDatabaseFlags(request: google.cloud.alloydb.v1alpha.IListSupportedDatabaseFlagsRequest): Promise<google.cloud.alloydb.v1alpha.ListSupportedDatabaseFlagsResponse>;

Calls ListSupportedDatabaseFlags.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IListSupportedDatabaseFlagsRequest](https://docs.cloud.google.com/nodejs/docs/reference/alloydb/latest/alloydb/protos.google.cloud.alloydb.v1alpha.ilistsupporteddatabaseflagsrequest)`   
ListSupportedDatabaseFlagsRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.alloydb.v1alpha.ListSupportedDatabaseFlagsResponse](https://docs.cloud.google.com/nodejs/docs/reference/alloydb/latest/alloydb/protos.google.cloud.alloydb.v1alpha.listsupporteddatabaseflagsresponse)>` | Promise  
  
### listUsers(request, callback)
    
    
    public listUsers(request: google.cloud.alloydb.v1alpha.IListUsersRequest, callback: google.cloud.alloydb.v1alpha.AlloyDBAdmin.ListUsersCallback): void;

Calls ListUsers.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListUsersRequest](https://docs.cloud.google.com/nodejs/docs/reference/alloydb/latest/alloydb/protos.google.cloud.alloydb.v1alpha.ilistusersrequest)`   
ListUsersRequest message or plain object  
`callback` |  `[ListUsersCallback](https://docs.cloud.google.com/nodejs/docs/reference/alloydb/latest/overview.html)`   
Node-style callback called with the error, if any, and ListUsersResponse  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### listUsers(request)
    
    
    public listUsers(request: google.cloud.alloydb.v1alpha.IListUsersRequest): Promise<google.cloud.alloydb.v1alpha.ListUsersResponse>;

Calls ListUsers.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IListUsersRequest](https://docs.cloud.google.com/nodejs/docs/reference/alloydb/latest/alloydb/protos.google.cloud.alloydb.v1alpha.ilistusersrequest)`   
ListUsersRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.alloydb.v1alpha.ListUsersResponse](https://docs.cloud.google.com/nodejs/docs/reference/alloydb/latest/alloydb/protos.google.cloud.alloydb.v1alpha.listusersresponse)>` | Promise  
  
### promoteCluster(request, callback)
    
    
    public promoteCluster(request: google.cloud.alloydb.v1alpha.IPromoteClusterRequest, callback: google.cloud.alloydb.v1alpha.AlloyDBAdmin.PromoteClusterCallback): void;

Calls PromoteCluster.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IPromoteClusterRequest](https://docs.cloud.google.com/nodejs/docs/reference/alloydb/latest/alloydb/protos.google.cloud.alloydb.v1alpha.ipromoteclusterrequest)`   
PromoteClusterRequest message or plain object  
`callback` |  `[PromoteClusterCallback](https://docs.cloud.google.com/nodejs/docs/reference/alloydb/latest/overview.html)`   
Node-style callback called with the error, if any, and Operation  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### promoteCluster(request)
    
    
    public promoteCluster(request: google.cloud.alloydb.v1alpha.IPromoteClusterRequest): Promise<google.longrunning.Operation>;

Calls PromoteCluster.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IPromoteClusterRequest](https://docs.cloud.google.com/nodejs/docs/reference/alloydb/latest/alloydb/protos.google.cloud.alloydb.v1alpha.ipromoteclusterrequest)`   
PromoteClusterRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.longrunning.Operation](https://docs.cloud.google.com/nodejs/docs/reference/alloydb/latest/alloydb/protos.google.longrunning.operation)>` | Promise  
  
### restartInstance(request, callback)
    
    
    public restartInstance(request: google.cloud.alloydb.v1alpha.IRestartInstanceRequest, callback: google.cloud.alloydb.v1alpha.AlloyDBAdmin.RestartInstanceCallback): void;

Calls RestartInstance.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IRestartInstanceRequest](https://docs.cloud.google.com/nodejs/docs/reference/alloydb/latest/alloydb/protos.google.cloud.alloydb.v1alpha.irestartinstancerequest)`   
RestartInstanceRequest message or plain object  
`callback` |  `[RestartInstanceCallback](https://docs.cloud.google.com/nodejs/docs/reference/alloydb/latest/overview.html)`   
Node-style callback called with the error, if any, and Operation  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### restartInstance(request)
    
    
    public restartInstance(request: google.cloud.alloydb.v1alpha.IRestartInstanceRequest): Promise<google.longrunning.Operation>;

Calls RestartInstance.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IRestartInstanceRequest](https://docs.cloud.google.com/nodejs/docs/reference/alloydb/latest/alloydb/protos.google.cloud.alloydb.v1alpha.irestartinstancerequest)`   
RestartInstanceRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.longrunning.Operation](https://docs.cloud.google.com/nodejs/docs/reference/alloydb/latest/alloydb/protos.google.longrunning.operation)>` | Promise  
  
### restoreCluster(request, callback)
    
    
    public restoreCluster(request: google.cloud.alloydb.v1alpha.IRestoreClusterRequest, callback: google.cloud.alloydb.v1alpha.AlloyDBAdmin.RestoreClusterCallback): void;

Calls RestoreCluster.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IRestoreClusterRequest](https://docs.cloud.google.com/nodejs/docs/reference/alloydb/latest/alloydb/protos.google.cloud.alloydb.v1alpha.irestoreclusterrequest)`   
RestoreClusterRequest message or plain object  
`callback` |  `[RestoreClusterCallback](https://docs.cloud.google.com/nodejs/docs/reference/alloydb/latest/overview.html)`   
Node-style callback called with the error, if any, and Operation  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### restoreCluster(request)
    
    
    public restoreCluster(request: google.cloud.alloydb.v1alpha.IRestoreClusterRequest): Promise<google.longrunning.Operation>;

Calls RestoreCluster.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IRestoreClusterRequest](https://docs.cloud.google.com/nodejs/docs/reference/alloydb/latest/alloydb/protos.google.cloud.alloydb.v1alpha.irestoreclusterrequest)`   
RestoreClusterRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.longrunning.Operation](https://docs.cloud.google.com/nodejs/docs/reference/alloydb/latest/alloydb/protos.google.longrunning.operation)>` | Promise  
  
### switchoverCluster(request, callback)
    
    
    public switchoverCluster(request: google.cloud.alloydb.v1alpha.ISwitchoverClusterRequest, callback: google.cloud.alloydb.v1alpha.AlloyDBAdmin.SwitchoverClusterCallback): void;

Calls SwitchoverCluster.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[ISwitchoverClusterRequest](https://docs.cloud.google.com/nodejs/docs/reference/alloydb/latest/alloydb/protos.google.cloud.alloydb.v1alpha.iswitchoverclusterrequest)`   
SwitchoverClusterRequest message or plain object  
`callback` |  `[SwitchoverClusterCallback](https://docs.cloud.google.com/nodejs/docs/reference/alloydb/latest/overview.html)`   
Node-style callback called with the error, if any, and Operation  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### switchoverCluster(request)
    
    
    public switchoverCluster(request: google.cloud.alloydb.v1alpha.ISwitchoverClusterRequest): Promise<google.longrunning.Operation>;

Calls SwitchoverCluster.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[ISwitchoverClusterRequest](https://docs.cloud.google.com/nodejs/docs/reference/alloydb/latest/alloydb/protos.google.cloud.alloydb.v1alpha.iswitchoverclusterrequest)`   
SwitchoverClusterRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.longrunning.Operation](https://docs.cloud.google.com/nodejs/docs/reference/alloydb/latest/alloydb/protos.google.longrunning.operation)>` | Promise  
  
### updateBackup(request, callback)
    
    
    public updateBackup(request: google.cloud.alloydb.v1alpha.IUpdateBackupRequest, callback: google.cloud.alloydb.v1alpha.AlloyDBAdmin.UpdateBackupCallback): void;

Calls UpdateBackup.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IUpdateBackupRequest](https://docs.cloud.google.com/nodejs/docs/reference/alloydb/latest/alloydb/protos.google.cloud.alloydb.v1alpha.iupdatebackuprequest)`   
UpdateBackupRequest message or plain object  
`callback` |  `[UpdateBackupCallback](https://docs.cloud.google.com/nodejs/docs/reference/alloydb/latest/overview.html)`   
Node-style callback called with the error, if any, and Operation  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### updateBackup(request)
    
    
    public updateBackup(request: google.cloud.alloydb.v1alpha.IUpdateBackupRequest): Promise<google.longrunning.Operation>;

Calls UpdateBackup.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IUpdateBackupRequest](https://docs.cloud.google.com/nodejs/docs/reference/alloydb/latest/alloydb/protos.google.cloud.alloydb.v1alpha.iupdatebackuprequest)`   
UpdateBackupRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.longrunning.Operation](https://docs.cloud.google.com/nodejs/docs/reference/alloydb/latest/alloydb/protos.google.longrunning.operation)>` | Promise  
  
### updateCluster(request, callback)
    
    
    public updateCluster(request: google.cloud.alloydb.v1alpha.IUpdateClusterRequest, callback: google.cloud.alloydb.v1alpha.AlloyDBAdmin.UpdateClusterCallback): void;

Calls UpdateCluster.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IUpdateClusterRequest](https://docs.cloud.google.com/nodejs/docs/reference/alloydb/latest/alloydb/protos.google.cloud.alloydb.v1alpha.iupdateclusterrequest)`   
UpdateClusterRequest message or plain object  
`callback` |  `[UpdateClusterCallback](https://docs.cloud.google.com/nodejs/docs/reference/alloydb/latest/overview.html)`   
Node-style callback called with the error, if any, and Operation  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### updateCluster(request)
    
    
    public updateCluster(request: google.cloud.alloydb.v1alpha.IUpdateClusterRequest): Promise<google.longrunning.Operation>;

Calls UpdateCluster.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IUpdateClusterRequest](https://docs.cloud.google.com/nodejs/docs/reference/alloydb/latest/alloydb/protos.google.cloud.alloydb.v1alpha.iupdateclusterrequest)`   
UpdateClusterRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.longrunning.Operation](https://docs.cloud.google.com/nodejs/docs/reference/alloydb/latest/alloydb/protos.google.longrunning.operation)>` | Promise  
  
### updateInstance(request, callback)
    
    
    public updateInstance(request: google.cloud.alloydb.v1alpha.IUpdateInstanceRequest, callback: google.cloud.alloydb.v1alpha.AlloyDBAdmin.UpdateInstanceCallback): void;

Calls UpdateInstance.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IUpdateInstanceRequest](https://docs.cloud.google.com/nodejs/docs/reference/alloydb/latest/alloydb/protos.google.cloud.alloydb.v1alpha.iupdateinstancerequest)`   
UpdateInstanceRequest message or plain object  
`callback` |  `[UpdateInstanceCallback](https://docs.cloud.google.com/nodejs/docs/reference/alloydb/latest/overview.html)`   
Node-style callback called with the error, if any, and Operation  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### updateInstance(request)
    
    
    public updateInstance(request: google.cloud.alloydb.v1alpha.IUpdateInstanceRequest): Promise<google.longrunning.Operation>;

Calls UpdateInstance.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IUpdateInstanceRequest](https://docs.cloud.google.com/nodejs/docs/reference/alloydb/latest/alloydb/protos.google.cloud.alloydb.v1alpha.iupdateinstancerequest)`   
UpdateInstanceRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.longrunning.Operation](https://docs.cloud.google.com/nodejs/docs/reference/alloydb/latest/alloydb/protos.google.longrunning.operation)>` | Promise  
  
### updateUser(request, callback)
    
    
    public updateUser(request: google.cloud.alloydb.v1alpha.IUpdateUserRequest, callback: google.cloud.alloydb.v1alpha.AlloyDBAdmin.UpdateUserCallback): void;

Calls UpdateUser.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IUpdateUserRequest](https://docs.cloud.google.com/nodejs/docs/reference/alloydb/latest/alloydb/protos.google.cloud.alloydb.v1alpha.iupdateuserrequest)`   
UpdateUserRequest message or plain object  
`callback` |  `[UpdateUserCallback](https://docs.cloud.google.com/nodejs/docs/reference/alloydb/latest/overview.html)`   
Node-style callback called with the error, if any, and User  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### updateUser(request)
    
    
    public updateUser(request: google.cloud.alloydb.v1alpha.IUpdateUserRequest): Promise<google.cloud.alloydb.v1alpha.User>;

Calls UpdateUser.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IUpdateUserRequest](https://docs.cloud.google.com/nodejs/docs/reference/alloydb/latest/alloydb/protos.google.cloud.alloydb.v1alpha.iupdateuserrequest)`   
UpdateUserRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.alloydb.v1alpha.User](https://docs.cloud.google.com/nodejs/docs/reference/alloydb/latest/alloydb/protos.google.cloud.alloydb.v1alpha.user-class)>` | Promise  
  
### upgradeCluster(request, callback)
    
    
    public upgradeCluster(request: google.cloud.alloydb.v1alpha.IUpgradeClusterRequest, callback: google.cloud.alloydb.v1alpha.AlloyDBAdmin.UpgradeClusterCallback): void;

Calls UpgradeCluster.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IUpgradeClusterRequest](https://docs.cloud.google.com/nodejs/docs/reference/alloydb/latest/alloydb/protos.google.cloud.alloydb.v1alpha.iupgradeclusterrequest)`   
UpgradeClusterRequest message or plain object  
`callback` |  `[UpgradeClusterCallback](https://docs.cloud.google.com/nodejs/docs/reference/alloydb/latest/overview.html)`   
Node-style callback called with the error, if any, and Operation  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### upgradeCluster(request)
    
    
    public upgradeCluster(request: google.cloud.alloydb.v1alpha.IUpgradeClusterRequest): Promise<google.longrunning.Operation>;

Calls UpgradeCluster.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IUpgradeClusterRequest](https://docs.cloud.google.com/nodejs/docs/reference/alloydb/latest/alloydb/protos.google.cloud.alloydb.v1alpha.iupgradeclusterrequest)`   
UpgradeClusterRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.longrunning.Operation](https://docs.cloud.google.com/nodejs/docs/reference/alloydb/latest/alloydb/protos.google.longrunning.operation)>` | Promise  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-02 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-02 UTC."],[],[]] 
