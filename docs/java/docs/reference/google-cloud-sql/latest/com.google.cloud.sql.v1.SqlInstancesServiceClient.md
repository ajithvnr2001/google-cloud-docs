---
url: https://docs.cloud.google.com/java/docs/reference/google-cloud-sql/latest/com.google.cloud.sql.v1.SqlInstancesServiceClient
title: Class SqlInstancesServiceClient (0.5.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T17:56:20.320634+00:00
---

# Class SqlInstancesServiceClient (0.5.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-cloud-sql/latest/com.google.cloud.sql.v1.SqlInstancesServiceClient

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Class SqlInstancesServiceClient (0.5.0) Stay organized with collections  Save and categorize content based on your preferences. 

0.5.0 (latest)  0.1.0 

[GitHub Repository](https://github.com/googleapis/google-cloud-java/tree/main/java-sql/google-cloud-sql/src/main/java/com/google/cloud/sql/v1/SqlInstancesServiceClient.java)| [Product Reference](https://cloud.google.com/sql/)  
---|---  
  
This class provides the ability to make remote calls to the backing service through method calls that map to API methods. Sample code to get started:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (SqlInstancesServiceClient sqlInstancesServiceClient = SqlInstancesServiceClient.create()) {
       SqlInstancesAddServerCaRequest request =
           SqlInstancesAddServerCaRequest.newBuilder()
               .setInstance("instance555127957")
               .setProject("project-309310695")
               .build();
       Operation response = sqlInstancesServiceClient.addServerCa(request);
     }
     

Note: close() needs to be called on the SqlInstancesServiceClient object to clean up resources such as threads. In the example above, try-with-resources is used, which automatically calls close().

Methods Method | Description | Method Variants  
---|---|---  
AddServerCa |  Adds a new trusted Certificate Authority (CA) version for the specified instance. Required to prepare for a certificate rotation. If a CA version was previously added but never used in a certificate rotation, this operation replaces that version. There cannot be more than one CA version waiting to be rotated in. For instances that have enabled Certificate Authority Service (CAS) based server CA, use AddServerCertificate to add a new server certificate. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * addServerCa(SqlInstancesAddServerCaRequest request) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * addServerCaCallable() 

  
AddServerCertificate |  Add a new trusted server certificate version for the specified instance using Certificate Authority Service (CAS) server CA. Required to prepare for a certificate rotation. If a server certificate version was previously added but never used in a certificate rotation, this operation replaces that version. There cannot be more than one certificate version waiting to be rotated in. For instances not using CAS server CA, use AddServerCa instead. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * addServerCertificate(SqlInstancesAddServerCertificateRequest request) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * addServerCertificateCallable() 

  
AddEntraIdCertificate |  Adds a new Entra ID certificate for the specified instance. If an Entra ID certificate was previously added but never used in a certificate rotation, this operation replaces that version. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * addEntraIdCertificate(SqlInstancesAddEntraIdCertificateRequest request) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * addEntraIdCertificateCallable() 

  
Clone |  Creates a Cloud SQL instance as a clone of the source instance. Using this operation might cause your instance to restart. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * clone(SqlInstancesCloneRequest request) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * cloneCallable() 

  
Delete |  Deletes a Cloud SQL instance. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * delete(SqlInstancesDeleteRequest request) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * deleteCallable() 

  
DemoteMaster |  Demotes the stand-alone instance to be a Cloud SQL read replica for an external database server. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * demoteMaster(SqlInstancesDemoteMasterRequest request) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * demoteMasterCallable() 

  
Demote |  Demotes an existing standalone instance to be a Cloud SQL read replica for an external database server. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * demote(SqlInstancesDemoteRequest request) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * demoteCallable() 

  
Export |  Exports data from a Cloud SQL instance to a Cloud Storage bucket as a SQL dump or CSV file. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * export(SqlInstancesExportRequest request) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * exportCallable() 

  
Failover |  Initiates a manual failover of a high availability (HA) primary instance to a standby instance, which becomes the primary instance. Users are then rerouted to the new primary. For more information, see the [Overview of high availability](https://cloud.google.com/sql/docs/mysql/high-availability) page in the Cloud SQL documentation. If using Legacy HA (MySQL only), this causes the instance to failover to its failover replica instance. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * failover(SqlInstancesFailoverRequest request) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * failoverCallable() 

  
Reencrypt |  Reencrypt CMEK instance with latest key version. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * reencrypt(SqlInstancesReencryptRequest request) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * reencryptCallable() 

  
Get |  Retrieves a resource containing information about a Cloud SQL instance. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * get(SqlInstancesGetRequest request) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * getCallable() 

  
Import |  Imports data into a Cloud SQL instance from a SQL dump or CSV file in Cloud Storage. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * import_(SqlInstancesImportRequest request) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * import_Callable() 

  
Insert |  Creates a new Cloud SQL instance. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * insert(SqlInstancesInsertRequest request) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * insertCallable() 

  
List |  Lists instances under a given project. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * list(SqlInstancesListRequest request) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * listCallable() 

  
ListServerCas |  Lists all of the trusted Certificate Authorities (CAs) for the specified instance. There can be up to three CAs listed: the CA that was used to sign the certificate that is currently in use, a CA that has been added but not yet used to sign a certificate, and a CA used to sign a certificate that has previously rotated out. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * listServerCas(SqlInstancesListServerCasRequest request) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * listServerCasCallable() 

  
ListServerCertificates |  Lists all versions of server certificates and certificate authorities (CAs) for the specified instance. There can be up to three sets of certs listed: the certificate that is currently in use, a future that has been added but not yet used to sign a certificate, and a certificate that has been rotated out. For instances not using Certificate Authority Service (CAS) server CA, use ListServerCas instead. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * listServerCertificates(SqlInstancesListServerCertificatesRequest request) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * listServerCertificatesCallable() 

  
ListEntraIdCertificates |  Lists all versions of EntraID certificates for the specified instance. There can be up to three sets of certificates listed: the certificate that is currently in use, a future that has been added but not yet used to sign a certificate, and a certificate that has been rotated out. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * listEntraIdCertificates(SqlInstancesListEntraIdCertificatesRequest request) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * listEntraIdCertificatesCallable() 

  
Patch |  Partially updates settings of a Cloud SQL instance by merging the request with the current configuration. This method supports patch semantics. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * patch(SqlInstancesPatchRequest request) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * patchCallable() 

  
PromoteReplica |  Promotes the read replica instance to be an independent Cloud SQL primary instance. Using this operation might cause your instance to restart. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * promoteReplica(SqlInstancesPromoteReplicaRequest request) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * promoteReplicaCallable() 

  
Switchover |  Switches over from the primary instance to the DR replica instance. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * switchover(SqlInstancesSwitchoverRequest request) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * switchoverCallable() 

  
ResetSslConfig |  Deletes all client certificates and generates a new server SSL certificate for the instance. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * resetSslConfig(SqlInstancesResetSslConfigRequest request) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * resetSslConfigCallable() 

  
Restart |  Restarts a Cloud SQL instance. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * restart(SqlInstancesRestartRequest request) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * restartCallable() 

  
RestoreBackup |  Restores a backup of a Cloud SQL instance. Using this operation might cause your instance to restart. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * restoreBackup(SqlInstancesRestoreBackupRequest request) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * restoreBackupCallable() 

  
RotateServerCa |  Rotates the server certificate to one signed by the Certificate Authority (CA) version previously added with the addServerCA method. For instances that have enabled Certificate Authority Service (CAS) based server CA, use RotateServerCertificate to rotate the server certificate. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * rotateServerCa(SqlInstancesRotateServerCaRequest request) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * rotateServerCaCallable() 

  
RotateServerCertificate |  Rotates the server certificate version to one previously added with the addServerCertificate method. For instances not using Certificate Authority Service (CAS) server CA, use RotateServerCa instead. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * rotateServerCertificate(SqlInstancesRotateServerCertificateRequest request) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * rotateServerCertificateCallable() 

  
RotateEntraIdCertificate |  Rotates the server certificate version to one previously added with the addEntraIdCertificate method. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * rotateEntraIdCertificate(SqlInstancesRotateEntraIdCertificateRequest request) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * rotateEntraIdCertificateCallable() 

  
StartReplica |  Starts the replication in the read replica instance. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * startReplica(SqlInstancesStartReplicaRequest request) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * startReplicaCallable() 

  
StopReplica |  Stops the replication in the read replica instance. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * stopReplica(SqlInstancesStopReplicaRequest request) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * stopReplicaCallable() 

  
TruncateLog |  Truncate MySQL general and slow query log tables MySQL only. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * truncateLog(SqlInstancesTruncateLogRequest request) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * truncateLogCallable() 

  
Update |  Updates settings of a Cloud SQL instance. Using this operation might cause your instance to restart. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * update(SqlInstancesUpdateRequest request) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * updateCallable() 

  
CreateEphemeral |  Generates a short-lived X509 certificate containing the provided public key and signed by a private key specific to the target instance. Users may use the certificate to authenticate as themselves when connecting to the database. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * createEphemeral(SqlInstancesCreateEphemeralCertRequest request) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * createEphemeralCallable() 

  
RescheduleMaintenance |  Reschedules the maintenance on the given instance. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * rescheduleMaintenance(SqlInstancesRescheduleMaintenanceRequest request) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * rescheduleMaintenanceCallable() 

  
VerifyExternalSyncSettings |  Verify External primary instance external sync settings. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * verifyExternalSyncSettings(SqlInstancesVerifyExternalSyncSettingsRequest request) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * verifyExternalSyncSettingsCallable() 

  
StartExternalSync |  Start External primary instance migration. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * startExternalSync(SqlInstancesStartExternalSyncRequest request) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * startExternalSyncCallable() 

  
PerformDiskShrink |  Perform Disk Shrink on primary instance. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * performDiskShrink(SqlInstancesPerformDiskShrinkRequest request) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * performDiskShrinkCallable() 

  
GetDiskShrinkConfig |  Get Disk Shrink Config for a given instance. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * getDiskShrinkConfig(SqlInstancesGetDiskShrinkConfigRequest request) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * getDiskShrinkConfigCallable() 

  
ResetReplicaSize |  Reset Replica Size to primary instance disk size. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * resetReplicaSize(SqlInstancesResetReplicaSizeRequest request) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * resetReplicaSizeCallable() 

  
GetLatestRecoveryTime |  Get Latest Recovery Time for a given instance. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * getLatestRecoveryTime(SqlInstancesGetLatestRecoveryTimeRequest request) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * getLatestRecoveryTimeCallable() 

  
ExecuteSql |  Execute SQL statements. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * executeSql(SqlInstancesExecuteSqlRequest request) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * executeSqlCallable() 

  
AcquireSsrsLease |  Acquire a lease for the setup of SQL Server Reporting Services (SSRS). |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * acquireSsrsLease(SqlInstancesAcquireSsrsLeaseRequest request) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * acquireSsrsLeaseCallable() 

  
ReleaseSsrsLease |  Release a lease for the setup of SQL Server Reporting Services (SSRS). |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * releaseSsrsLease(SqlInstancesReleaseSsrsLeaseRequest request) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * releaseSsrsLeaseCallable() 

  
PreCheckMajorVersionUpgrade |  Execute MVU Pre-checks |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * preCheckMajorVersionUpgrade(SqlInstancesPreCheckMajorVersionUpgradeRequest request) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * preCheckMajorVersionUpgradeCallable() 

  
PointInTimeRestore |  Point in time restore for an instance managed by Google Cloud Backup and Disaster Recovery. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * pointInTimeRestore(SqlInstancesPointInTimeRestoreRequest request) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * pointInTimeRestoreCallable() 

  
  
See the individual methods for example code.

Many parameters require resource names to be formatted in a particular way. To assist with these names, this class includes a format method for each type of name, and additionally a parse method to extract the individual identifiers contained within names that are returned.

This class can be customized by passing in a custom instance of SqlInstancesServiceSettings to create(). For example:

To customize credentials:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     SqlInstancesServiceSettings sqlInstancesServiceSettings =
         SqlInstancesServiceSettings.newBuilder()
             .setCredentialsProvider(FixedCredentialsProvider.create(myCredentials))
             .build();
     SqlInstancesServiceClient sqlInstancesServiceClient =
         SqlInstancesServiceClient.create(sqlInstancesServiceSettings);
     

To customize the endpoint:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     SqlInstancesServiceSettings sqlInstancesServiceSettings =
         SqlInstancesServiceSettings.newBuilder().setEndpoint(myEndpoint).build();
     SqlInstancesServiceClient sqlInstancesServiceClient =
         SqlInstancesServiceClient.create(sqlInstancesServiceSettings);
     

To use REST (HTTP1.1/JSON) transport (instead of gRPC) for sending and receiving requests over the wire:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     SqlInstancesServiceSettings sqlInstancesServiceSettings =
         SqlInstancesServiceSettings.newHttpJsonBuilder().build();
     SqlInstancesServiceClient sqlInstancesServiceClient =
         SqlInstancesServiceClient.create(sqlInstancesServiceSettings);
     

Please refer to the GitHub repository's samples for more quickstart code snippets.

## Inheritance

[java.lang.Object](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html) > SqlInstancesServiceClient

## Static Methods 

### create()
    
    
    public static final SqlInstancesServiceClient create()

Constructs an instance of SqlInstancesServiceClient with default settings.

**Returns**  
---  
**Type** | **Description**  
`[SqlInstancesServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-sql/latest/com.google.cloud.sql.v1.SqlInstancesServiceClient)` |   
**Exceptions**  
---  
**Type** | **Description**  
`[IOException](https://docs.oracle.com/javase/8/docs/api/java/io/IOException.html)` |   
  
### create(SqlInstancesServiceSettings settings)
    
    
    public static final SqlInstancesServiceClient create(SqlInstancesServiceSettings settings)

Constructs an instance of SqlInstancesServiceClient, using the given settings. The channels are created based on the settings passed in, or defaults for any settings that are not set.

**Parameter**  
---  
**Name** | **Description**  
`settings` | `[SqlInstancesServiceSettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-sql/latest/com.google.cloud.sql.v1.SqlInstancesServiceSettings)`  
  
**Returns**  
---  
**Type** | **Description**  
`[SqlInstancesServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-sql/latest/com.google.cloud.sql.v1.SqlInstancesServiceClient)` |   
**Exceptions**  
---  
**Type** | **Description**  
`[IOException](https://docs.oracle.com/javase/8/docs/api/java/io/IOException.html)` |   
  
### create(SqlInstancesServiceStub stub)
    
    
    public static final SqlInstancesServiceClient create(SqlInstancesServiceStub stub)

Constructs an instance of SqlInstancesServiceClient, using the given stub for making calls. This is for advanced usage - prefer using create(SqlInstancesServiceSettings).

**Parameter**  
---  
**Name** | **Description**  
`stub` | `[SqlInstancesServiceStub](https://docs.cloud.google.com/java/docs/reference/google-cloud-sql/latest/com.google.cloud.sql.v1.stub.SqlInstancesServiceStub)`  
  
**Returns**  
---  
**Type** | **Description**  
`[SqlInstancesServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-sql/latest/com.google.cloud.sql.v1.SqlInstancesServiceClient)` |   
  
## Constructors 

### SqlInstancesServiceClient(SqlInstancesServiceSettings settings)
    
    
    protected SqlInstancesServiceClient(SqlInstancesServiceSettings settings)

Constructs an instance of SqlInstancesServiceClient, using the given settings. This is protected so that it is easy to make a subclass, but otherwise, the static factory methods should be preferred.

**Parameter**  
---  
**Name** | **Description**  
`settings` | `[SqlInstancesServiceSettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-sql/latest/com.google.cloud.sql.v1.SqlInstancesServiceSettings)`  
  
  
### SqlInstancesServiceClient(SqlInstancesServiceStub stub)
    
    
    protected SqlInstancesServiceClient(SqlInstancesServiceStub stub)

**Parameter**  
---  
**Name** | **Description**  
`stub` | `[SqlInstancesServiceStub](https://docs.cloud.google.com/java/docs/reference/google-cloud-sql/latest/com.google.cloud.sql.v1.stub.SqlInstancesServiceStub)`  
  
  
## Methods 

### acquireSsrsLease(SqlInstancesAcquireSsrsLeaseRequest request)
    
    
    public final SqlInstancesAcquireSsrsLeaseResponse acquireSsrsLease(SqlInstancesAcquireSsrsLeaseRequest request)

Acquire a lease for the setup of SQL Server Reporting Services (SSRS).

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (SqlInstancesServiceClient sqlInstancesServiceClient = SqlInstancesServiceClient.create()) {
       SqlInstancesAcquireSsrsLeaseRequest request =
           SqlInstancesAcquireSsrsLeaseRequest.newBuilder()
               .setInstance("instance555127957")
               .setProject("project-309310695")
               .setBody(InstancesAcquireSsrsLeaseRequest.newBuilder().build())
               .build();
       SqlInstancesAcquireSsrsLeaseResponse response =
           sqlInstancesServiceClient.acquireSsrsLease(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[SqlInstancesAcquireSsrsLeaseRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-sql/latest/com.google.cloud.sql.v1.SqlInstancesAcquireSsrsLeaseRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[SqlInstancesAcquireSsrsLeaseResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-sql/latest/com.google.cloud.sql.v1.SqlInstancesAcquireSsrsLeaseResponse)` |   
  
### acquireSsrsLeaseCallable()
    
    
    public final UnaryCallable<SqlInstancesAcquireSsrsLeaseRequest,SqlInstancesAcquireSsrsLeaseResponse> acquireSsrsLeaseCallable()

Acquire a lease for the setup of SQL Server Reporting Services (SSRS).

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (SqlInstancesServiceClient sqlInstancesServiceClient = SqlInstancesServiceClient.create()) {
       SqlInstancesAcquireSsrsLeaseRequest request =
           SqlInstancesAcquireSsrsLeaseRequest.newBuilder()
               .setInstance("instance555127957")
               .setProject("project-309310695")
               .setBody(InstancesAcquireSsrsLeaseRequest.newBuilder().build())
               .build();
       ApiFuture<SqlInstancesAcquireSsrsLeaseResponse> future =
           sqlInstancesServiceClient.acquireSsrsLeaseCallable().futureCall(request);
       // Do something.
       SqlInstancesAcquireSsrsLeaseResponse response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[SqlInstancesAcquireSsrsLeaseRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-sql/latest/com.google.cloud.sql.v1.SqlInstancesAcquireSsrsLeaseRequest),[SqlInstancesAcquireSsrsLeaseResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-sql/latest/com.google.cloud.sql.v1.SqlInstancesAcquireSsrsLeaseResponse)>` |   
  
### addEntraIdCertificate(SqlInstancesAddEntraIdCertificateRequest request)
    
    
    public final Operation addEntraIdCertificate(SqlInstancesAddEntraIdCertificateRequest request)

Adds a new Entra ID certificate for the specified instance. If an Entra ID certificate was previously added but never used in a certificate rotation, this operation replaces that version.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (SqlInstancesServiceClient sqlInstancesServiceClient = SqlInstancesServiceClient.create()) {
       SqlInstancesAddEntraIdCertificateRequest request =
           SqlInstancesAddEntraIdCertificateRequest.newBuilder()
               .setInstance("instance555127957")
               .setProject("project-309310695")
               .build();
       Operation response = sqlInstancesServiceClient.addEntraIdCertificate(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[SqlInstancesAddEntraIdCertificateRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-sql/latest/com.google.cloud.sql.v1.SqlInstancesAddEntraIdCertificateRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-sql/latest/com.google.cloud.sql.v1.Operation)` |   
  
### addEntraIdCertificateCallable()
    
    
    public final UnaryCallable<SqlInstancesAddEntraIdCertificateRequest,Operation> addEntraIdCertificateCallable()

Adds a new Entra ID certificate for the specified instance. If an Entra ID certificate was previously added but never used in a certificate rotation, this operation replaces that version.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (SqlInstancesServiceClient sqlInstancesServiceClient = SqlInstancesServiceClient.create()) {
       SqlInstancesAddEntraIdCertificateRequest request =
           SqlInstancesAddEntraIdCertificateRequest.newBuilder()
               .setInstance("instance555127957")
               .setProject("project-309310695")
               .build();
       ApiFuture<Operation> future =
           sqlInstancesServiceClient.addEntraIdCertificateCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[SqlInstancesAddEntraIdCertificateRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-sql/latest/com.google.cloud.sql.v1.SqlInstancesAddEntraIdCertificateRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-sql/latest/com.google.cloud.sql.v1.Operation)>` |   
  
### addServerCa(SqlInstancesAddServerCaRequest request)
    
    
    public final Operation addServerCa(SqlInstancesAddServerCaRequest request)

Adds a new trusted Certificate Authority (CA) version for the specified instance. Required to prepare for a certificate rotation. If a CA version was previously added but never used in a certificate rotation, this operation replaces that version. There cannot be more than one CA version waiting to be rotated in. For instances that have enabled Certificate Authority Service (CAS) based server CA, use AddServerCertificate to add a new server certificate.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (SqlInstancesServiceClient sqlInstancesServiceClient = SqlInstancesServiceClient.create()) {
       SqlInstancesAddServerCaRequest request =
           SqlInstancesAddServerCaRequest.newBuilder()
               .setInstance("instance555127957")
               .setProject("project-309310695")
               .build();
       Operation response = sqlInstancesServiceClient.addServerCa(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[SqlInstancesAddServerCaRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-sql/latest/com.google.cloud.sql.v1.SqlInstancesAddServerCaRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-sql/latest/com.google.cloud.sql.v1.Operation)` |   
  
### addServerCaCallable()
    
    
    public final UnaryCallable<SqlInstancesAddServerCaRequest,Operation> addServerCaCallable()

Adds a new trusted Certificate Authority (CA) version for the specified instance. Required to prepare for a certificate rotation. If a CA version was previously added but never used in a certificate rotation, this operation replaces that version. There cannot be more than one CA version waiting to be rotated in. For instances that have enabled Certificate Authority Service (CAS) based server CA, use AddServerCertificate to add a new server certificate.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (SqlInstancesServiceClient sqlInstancesServiceClient = SqlInstancesServiceClient.create()) {
       SqlInstancesAddServerCaRequest request =
           SqlInstancesAddServerCaRequest.newBuilder()
               .setInstance("instance555127957")
               .setProject("project-309310695")
               .build();
       ApiFuture<Operation> future =
           sqlInstancesServiceClient.addServerCaCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[SqlInstancesAddServerCaRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-sql/latest/com.google.cloud.sql.v1.SqlInstancesAddServerCaRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-sql/latest/com.google.cloud.sql.v1.Operation)>` |   
  
### addServerCertificate(SqlInstancesAddServerCertificateRequest request)
    
    
    public final Operation addServerCertificate(SqlInstancesAddServerCertificateRequest request)

Add a new trusted server certificate version for the specified instance using Certificate Authority Service (CAS) server CA. Required to prepare for a certificate rotation. If a server certificate version was previously added but never used in a certificate rotation, this operation replaces that version. There cannot be more than one certificate version waiting to be rotated in. For instances not using CAS server CA, use AddServerCa instead.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (SqlInstancesServiceClient sqlInstancesServiceClient = SqlInstancesServiceClient.create()) {
       SqlInstancesAddServerCertificateRequest request =
           SqlInstancesAddServerCertificateRequest.newBuilder()
               .setInstance("instance555127957")
               .setProject("project-309310695")
               .build();
       Operation response = sqlInstancesServiceClient.addServerCertificate(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[SqlInstancesAddServerCertificateRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-sql/latest/com.google.cloud.sql.v1.SqlInstancesAddServerCertificateRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-sql/latest/com.google.cloud.sql.v1.Operation)` |   
  
### addServerCertificateCallable()
    
    
    public final UnaryCallable<SqlInstancesAddServerCertificateRequest,Operation> addServerCertificateCallable()

Add a new trusted server certificate version for the specified instance using Certificate Authority Service (CAS) server CA. Required to prepare for a certificate rotation. If a server certificate version was previously added but never used in a certificate rotation, this operation replaces that version. There cannot be more than one certificate version waiting to be rotated in. For instances not using CAS server CA, use AddServerCa instead.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (SqlInstancesServiceClient sqlInstancesServiceClient = SqlInstancesServiceClient.create()) {
       SqlInstancesAddServerCertificateRequest request =
           SqlInstancesAddServerCertificateRequest.newBuilder()
               .setInstance("instance555127957")
               .setProject("project-309310695")
               .build();
       ApiFuture<Operation> future =
           sqlInstancesServiceClient.addServerCertificateCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[SqlInstancesAddServerCertificateRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-sql/latest/com.google.cloud.sql.v1.SqlInstancesAddServerCertificateRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-sql/latest/com.google.cloud.sql.v1.Operation)>` |   
  
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
  
### clone(SqlInstancesCloneRequest request)
    
    
    public final Operation clone(SqlInstancesCloneRequest request)

Creates a Cloud SQL instance as a clone of the source instance. Using this operation might cause your instance to restart.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (SqlInstancesServiceClient sqlInstancesServiceClient = SqlInstancesServiceClient.create()) {
       SqlInstancesCloneRequest request =
           SqlInstancesCloneRequest.newBuilder()
               .setInstance("instance555127957")
               .setProject("project-309310695")
               .setBody(InstancesCloneRequest.newBuilder().build())
               .build();
       Operation response = sqlInstancesServiceClient.clone(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[SqlInstancesCloneRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-sql/latest/com.google.cloud.sql.v1.SqlInstancesCloneRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-sql/latest/com.google.cloud.sql.v1.Operation)` |   
  
### cloneCallable()
    
    
    public final UnaryCallable<SqlInstancesCloneRequest,Operation> cloneCallable()

Creates a Cloud SQL instance as a clone of the source instance. Using this operation might cause your instance to restart.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (SqlInstancesServiceClient sqlInstancesServiceClient = SqlInstancesServiceClient.create()) {
       SqlInstancesCloneRequest request =
           SqlInstancesCloneRequest.newBuilder()
               .setInstance("instance555127957")
               .setProject("project-309310695")
               .setBody(InstancesCloneRequest.newBuilder().build())
               .build();
       ApiFuture<Operation> future = sqlInstancesServiceClient.cloneCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[SqlInstancesCloneRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-sql/latest/com.google.cloud.sql.v1.SqlInstancesCloneRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-sql/latest/com.google.cloud.sql.v1.Operation)>` |   
  
### close()
    
    
    public final void close()

### createEphemeral(SqlInstancesCreateEphemeralCertRequest request)
    
    
    public final SslCert createEphemeral(SqlInstancesCreateEphemeralCertRequest request)

Generates a short-lived X509 certificate containing the provided public key and signed by a private key specific to the target instance. Users may use the certificate to authenticate as themselves when connecting to the database.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (SqlInstancesServiceClient sqlInstancesServiceClient = SqlInstancesServiceClient.create()) {
       SqlInstancesCreateEphemeralCertRequest request =
           SqlInstancesCreateEphemeralCertRequest.newBuilder()
               .setInstance("instance555127957")
               .setProject("project-309310695")
               .setBody(SslCertsCreateEphemeralRequest.newBuilder().build())
               .build();
       SslCert response = sqlInstancesServiceClient.createEphemeral(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[SqlInstancesCreateEphemeralCertRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-sql/latest/com.google.cloud.sql.v1.SqlInstancesCreateEphemeralCertRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[SslCert](https://docs.cloud.google.com/java/docs/reference/google-cloud-sql/latest/com.google.cloud.sql.v1.SslCert)` |   
  
### createEphemeralCallable()
    
    
    public final UnaryCallable<SqlInstancesCreateEphemeralCertRequest,SslCert> createEphemeralCallable()

Generates a short-lived X509 certificate containing the provided public key and signed by a private key specific to the target instance. Users may use the certificate to authenticate as themselves when connecting to the database.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (SqlInstancesServiceClient sqlInstancesServiceClient = SqlInstancesServiceClient.create()) {
       SqlInstancesCreateEphemeralCertRequest request =
           SqlInstancesCreateEphemeralCertRequest.newBuilder()
               .setInstance("instance555127957")
               .setProject("project-309310695")
               .setBody(SslCertsCreateEphemeralRequest.newBuilder().build())
               .build();
       ApiFuture<SslCert> future =
           sqlInstancesServiceClient.createEphemeralCallable().futureCall(request);
       // Do something.
       SslCert response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[SqlInstancesCreateEphemeralCertRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-sql/latest/com.google.cloud.sql.v1.SqlInstancesCreateEphemeralCertRequest),[SslCert](https://docs.cloud.google.com/java/docs/reference/google-cloud-sql/latest/com.google.cloud.sql.v1.SslCert)>` |   
  
### delete(SqlInstancesDeleteRequest request)
    
    
    public final Operation delete(SqlInstancesDeleteRequest request)

Deletes a Cloud SQL instance.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (SqlInstancesServiceClient sqlInstancesServiceClient = SqlInstancesServiceClient.create()) {
       SqlInstancesDeleteRequest request =
           SqlInstancesDeleteRequest.newBuilder()
               .setInstance("instance555127957")
               .setProject("project-309310695")
               .setEnableFinalBackup(true)
               .setFinalBackupDescription("finalBackupDescription-293551612")
               .build();
       Operation response = sqlInstancesServiceClient.delete(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[SqlInstancesDeleteRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-sql/latest/com.google.cloud.sql.v1.SqlInstancesDeleteRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-sql/latest/com.google.cloud.sql.v1.Operation)` |   
  
### deleteCallable()
    
    
    public final UnaryCallable<SqlInstancesDeleteRequest,Operation> deleteCallable()

Deletes a Cloud SQL instance.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (SqlInstancesServiceClient sqlInstancesServiceClient = SqlInstancesServiceClient.create()) {
       SqlInstancesDeleteRequest request =
           SqlInstancesDeleteRequest.newBuilder()
               .setInstance("instance555127957")
               .setProject("project-309310695")
               .setEnableFinalBackup(true)
               .setFinalBackupDescription("finalBackupDescription-293551612")
               .build();
       ApiFuture<Operation> future = sqlInstancesServiceClient.deleteCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[SqlInstancesDeleteRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-sql/latest/com.google.cloud.sql.v1.SqlInstancesDeleteRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-sql/latest/com.google.cloud.sql.v1.Operation)>` |   
  
### demote(SqlInstancesDemoteRequest request)
    
    
    public final Operation demote(SqlInstancesDemoteRequest request)

Demotes an existing standalone instance to be a Cloud SQL read replica for an external database server.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (SqlInstancesServiceClient sqlInstancesServiceClient = SqlInstancesServiceClient.create()) {
       SqlInstancesDemoteRequest request =
           SqlInstancesDemoteRequest.newBuilder()
               .setInstance("instance555127957")
               .setProject("project-309310695")
               .setBody(InstancesDemoteRequest.newBuilder().build())
               .build();
       Operation response = sqlInstancesServiceClient.demote(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[SqlInstancesDemoteRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-sql/latest/com.google.cloud.sql.v1.SqlInstancesDemoteRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-sql/latest/com.google.cloud.sql.v1.Operation)` |   
  
### demoteCallable()
    
    
    public final UnaryCallable<SqlInstancesDemoteRequest,Operation> demoteCallable()

Demotes an existing standalone instance to be a Cloud SQL read replica for an external database server.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (SqlInstancesServiceClient sqlInstancesServiceClient = SqlInstancesServiceClient.create()) {
       SqlInstancesDemoteRequest request =
           SqlInstancesDemoteRequest.newBuilder()
               .setInstance("instance555127957")
               .setProject("project-309310695")
               .setBody(InstancesDemoteRequest.newBuilder().build())
               .build();
       ApiFuture<Operation> future = sqlInstancesServiceClient.demoteCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[SqlInstancesDemoteRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-sql/latest/com.google.cloud.sql.v1.SqlInstancesDemoteRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-sql/latest/com.google.cloud.sql.v1.Operation)>` |   
  
### demoteMaster(SqlInstancesDemoteMasterRequest request)
    
    
    public final Operation demoteMaster(SqlInstancesDemoteMasterRequest request)

Demotes the stand-alone instance to be a Cloud SQL read replica for an external database server.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (SqlInstancesServiceClient sqlInstancesServiceClient = SqlInstancesServiceClient.create()) {
       SqlInstancesDemoteMasterRequest request =
           SqlInstancesDemoteMasterRequest.newBuilder()
               .setInstance("instance555127957")
               .setProject("project-309310695")
               .setBody(InstancesDemoteMasterRequest.newBuilder().build())
               .build();
       Operation response = sqlInstancesServiceClient.demoteMaster(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[SqlInstancesDemoteMasterRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-sql/latest/com.google.cloud.sql.v1.SqlInstancesDemoteMasterRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-sql/latest/com.google.cloud.sql.v1.Operation)` |   
  
### demoteMasterCallable()
    
    
    public final UnaryCallable<SqlInstancesDemoteMasterRequest,Operation> demoteMasterCallable()

Demotes the stand-alone instance to be a Cloud SQL read replica for an external database server.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (SqlInstancesServiceClient sqlInstancesServiceClient = SqlInstancesServiceClient.create()) {
       SqlInstancesDemoteMasterRequest request =
           SqlInstancesDemoteMasterRequest.newBuilder()
               .setInstance("instance555127957")
               .setProject("project-309310695")
               .setBody(InstancesDemoteMasterRequest.newBuilder().build())
               .build();
       ApiFuture<Operation> future =
           sqlInstancesServiceClient.demoteMasterCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[SqlInstancesDemoteMasterRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-sql/latest/com.google.cloud.sql.v1.SqlInstancesDemoteMasterRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-sql/latest/com.google.cloud.sql.v1.Operation)>` |   
  
### executeSql(SqlInstancesExecuteSqlRequest request)
    
    
    public final SqlInstancesExecuteSqlResponse executeSql(SqlInstancesExecuteSqlRequest request)

Execute SQL statements.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (SqlInstancesServiceClient sqlInstancesServiceClient = SqlInstancesServiceClient.create()) {
       SqlInstancesExecuteSqlRequest request =
           SqlInstancesExecuteSqlRequest.newBuilder()
               .setInstance("instance555127957")
               .setProject("project-309310695")
               .setBody(ExecuteSqlPayload.newBuilder().build())
               .build();
       SqlInstancesExecuteSqlResponse response = sqlInstancesServiceClient.executeSql(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[SqlInstancesExecuteSqlRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-sql/latest/com.google.cloud.sql.v1.SqlInstancesExecuteSqlRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[SqlInstancesExecuteSqlResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-sql/latest/com.google.cloud.sql.v1.SqlInstancesExecuteSqlResponse)` |   
  
### executeSqlCallable()
    
    
    public final UnaryCallable<SqlInstancesExecuteSqlRequest,SqlInstancesExecuteSqlResponse> executeSqlCallable()

Execute SQL statements.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (SqlInstancesServiceClient sqlInstancesServiceClient = SqlInstancesServiceClient.create()) {
       SqlInstancesExecuteSqlRequest request =
           SqlInstancesExecuteSqlRequest.newBuilder()
               .setInstance("instance555127957")
               .setProject("project-309310695")
               .setBody(ExecuteSqlPayload.newBuilder().build())
               .build();
       ApiFuture<SqlInstancesExecuteSqlResponse> future =
           sqlInstancesServiceClient.executeSqlCallable().futureCall(request);
       // Do something.
       SqlInstancesExecuteSqlResponse response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[SqlInstancesExecuteSqlRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-sql/latest/com.google.cloud.sql.v1.SqlInstancesExecuteSqlRequest),[SqlInstancesExecuteSqlResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-sql/latest/com.google.cloud.sql.v1.SqlInstancesExecuteSqlResponse)>` |   
  
### export(SqlInstancesExportRequest request)
    
    
    public final Operation export(SqlInstancesExportRequest request)

Exports data from a Cloud SQL instance to a Cloud Storage bucket as a SQL dump or CSV file.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (SqlInstancesServiceClient sqlInstancesServiceClient = SqlInstancesServiceClient.create()) {
       SqlInstancesExportRequest request =
           SqlInstancesExportRequest.newBuilder()
               .setInstance("instance555127957")
               .setProject("project-309310695")
               .setBody(InstancesExportRequest.newBuilder().build())
               .build();
       Operation response = sqlInstancesServiceClient.export(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[SqlInstancesExportRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-sql/latest/com.google.cloud.sql.v1.SqlInstancesExportRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-sql/latest/com.google.cloud.sql.v1.Operation)` |   
  
### exportCallable()
    
    
    public final UnaryCallable<SqlInstancesExportRequest,Operation> exportCallable()

Exports data from a Cloud SQL instance to a Cloud Storage bucket as a SQL dump or CSV file.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (SqlInstancesServiceClient sqlInstancesServiceClient = SqlInstancesServiceClient.create()) {
       SqlInstancesExportRequest request =
           SqlInstancesExportRequest.newBuilder()
               .setInstance("instance555127957")
               .setProject("project-309310695")
               .setBody(InstancesExportRequest.newBuilder().build())
               .build();
       ApiFuture<Operation> future = sqlInstancesServiceClient.exportCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[SqlInstancesExportRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-sql/latest/com.google.cloud.sql.v1.SqlInstancesExportRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-sql/latest/com.google.cloud.sql.v1.Operation)>` |   
  
### failover(SqlInstancesFailoverRequest request)
    
    
    public final Operation failover(SqlInstancesFailoverRequest request)

Initiates a manual failover of a high availability (HA) primary instance to a standby instance, which becomes the primary instance. Users are then rerouted to the new primary. For more information, see the [Overview of high availability](https://cloud.google.com/sql/docs/mysql/high-availability) page in the Cloud SQL documentation. If using Legacy HA (MySQL only), this causes the instance to failover to its failover replica instance.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (SqlInstancesServiceClient sqlInstancesServiceClient = SqlInstancesServiceClient.create()) {
       SqlInstancesFailoverRequest request =
           SqlInstancesFailoverRequest.newBuilder()
               .setInstance("instance555127957")
               .setProject("project-309310695")
               .setBody(InstancesFailoverRequest.newBuilder().build())
               .build();
       Operation response = sqlInstancesServiceClient.failover(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[SqlInstancesFailoverRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-sql/latest/com.google.cloud.sql.v1.SqlInstancesFailoverRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-sql/latest/com.google.cloud.sql.v1.Operation)` |   
  
### failoverCallable()
    
    
    public final UnaryCallable<SqlInstancesFailoverRequest,Operation> failoverCallable()

Initiates a manual failover of a high availability (HA) primary instance to a standby instance, which becomes the primary instance. Users are then rerouted to the new primary. For more information, see the [Overview of high availability](https://cloud.google.com/sql/docs/mysql/high-availability) page in the Cloud SQL documentation. If using Legacy HA (MySQL only), this causes the instance to failover to its failover replica instance.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (SqlInstancesServiceClient sqlInstancesServiceClient = SqlInstancesServiceClient.create()) {
       SqlInstancesFailoverRequest request =
           SqlInstancesFailoverRequest.newBuilder()
               .setInstance("instance555127957")
               .setProject("project-309310695")
               .setBody(InstancesFailoverRequest.newBuilder().build())
               .build();
       ApiFuture<Operation> future =
           sqlInstancesServiceClient.failoverCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[SqlInstancesFailoverRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-sql/latest/com.google.cloud.sql.v1.SqlInstancesFailoverRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-sql/latest/com.google.cloud.sql.v1.Operation)>` |   
  
### get(SqlInstancesGetRequest request)
    
    
    public final DatabaseInstance get(SqlInstancesGetRequest request)

Retrieves a resource containing information about a Cloud SQL instance.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (SqlInstancesServiceClient sqlInstancesServiceClient = SqlInstancesServiceClient.create()) {
       SqlInstancesGetRequest request =
           SqlInstancesGetRequest.newBuilder()
               .setInstance("instance555127957")
               .setProject("project-309310695")
               .build();
       DatabaseInstance response = sqlInstancesServiceClient.get(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[SqlInstancesGetRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-sql/latest/com.google.cloud.sql.v1.SqlInstancesGetRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[DatabaseInstance](https://docs.cloud.google.com/java/docs/reference/google-cloud-sql/latest/com.google.cloud.sql.v1.DatabaseInstance)` |   
  
### getCallable()
    
    
    public final UnaryCallable<SqlInstancesGetRequest,DatabaseInstance> getCallable()

Retrieves a resource containing information about a Cloud SQL instance.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (SqlInstancesServiceClient sqlInstancesServiceClient = SqlInstancesServiceClient.create()) {
       SqlInstancesGetRequest request =
           SqlInstancesGetRequest.newBuilder()
               .setInstance("instance555127957")
               .setProject("project-309310695")
               .build();
       ApiFuture<DatabaseInstance> future =
           sqlInstancesServiceClient.getCallable().futureCall(request);
       // Do something.
       DatabaseInstance response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[SqlInstancesGetRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-sql/latest/com.google.cloud.sql.v1.SqlInstancesGetRequest),[DatabaseInstance](https://docs.cloud.google.com/java/docs/reference/google-cloud-sql/latest/com.google.cloud.sql.v1.DatabaseInstance)>` |   
  
### getDiskShrinkConfig(SqlInstancesGetDiskShrinkConfigRequest request)
    
    
    public final SqlInstancesGetDiskShrinkConfigResponse getDiskShrinkConfig(SqlInstancesGetDiskShrinkConfigRequest request)

Get Disk Shrink Config for a given instance.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (SqlInstancesServiceClient sqlInstancesServiceClient = SqlInstancesServiceClient.create()) {
       SqlInstancesGetDiskShrinkConfigRequest request =
           SqlInstancesGetDiskShrinkConfigRequest.newBuilder()
               .setInstance("instance555127957")
               .setProject("project-309310695")
               .build();
       SqlInstancesGetDiskShrinkConfigResponse response =
           sqlInstancesServiceClient.getDiskShrinkConfig(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[SqlInstancesGetDiskShrinkConfigRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-sql/latest/com.google.cloud.sql.v1.SqlInstancesGetDiskShrinkConfigRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[SqlInstancesGetDiskShrinkConfigResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-sql/latest/com.google.cloud.sql.v1.SqlInstancesGetDiskShrinkConfigResponse)` |   
  
### getDiskShrinkConfigCallable()
    
    
    public final UnaryCallable<SqlInstancesGetDiskShrinkConfigRequest,SqlInstancesGetDiskShrinkConfigResponse> getDiskShrinkConfigCallable()

Get Disk Shrink Config for a given instance.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (SqlInstancesServiceClient sqlInstancesServiceClient = SqlInstancesServiceClient.create()) {
       SqlInstancesGetDiskShrinkConfigRequest request =
           SqlInstancesGetDiskShrinkConfigRequest.newBuilder()
               .setInstance("instance555127957")
               .setProject("project-309310695")
               .build();
       ApiFuture<SqlInstancesGetDiskShrinkConfigResponse> future =
           sqlInstancesServiceClient.getDiskShrinkConfigCallable().futureCall(request);
       // Do something.
       SqlInstancesGetDiskShrinkConfigResponse response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[SqlInstancesGetDiskShrinkConfigRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-sql/latest/com.google.cloud.sql.v1.SqlInstancesGetDiskShrinkConfigRequest),[SqlInstancesGetDiskShrinkConfigResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-sql/latest/com.google.cloud.sql.v1.SqlInstancesGetDiskShrinkConfigResponse)>` |   
  
### getLatestRecoveryTime(SqlInstancesGetLatestRecoveryTimeRequest request)
    
    
    public final SqlInstancesGetLatestRecoveryTimeResponse getLatestRecoveryTime(SqlInstancesGetLatestRecoveryTimeRequest request)

Get Latest Recovery Time for a given instance.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (SqlInstancesServiceClient sqlInstancesServiceClient = SqlInstancesServiceClient.create()) {
       SqlInstancesGetLatestRecoveryTimeRequest request =
           SqlInstancesGetLatestRecoveryTimeRequest.newBuilder()
               .setInstance("instance555127957")
               .setProject("project-309310695")
               .setSourceInstanceDeletionTime(Timestamp.newBuilder().build())
               .build();
       SqlInstancesGetLatestRecoveryTimeResponse response =
           sqlInstancesServiceClient.getLatestRecoveryTime(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[SqlInstancesGetLatestRecoveryTimeRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-sql/latest/com.google.cloud.sql.v1.SqlInstancesGetLatestRecoveryTimeRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[SqlInstancesGetLatestRecoveryTimeResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-sql/latest/com.google.cloud.sql.v1.SqlInstancesGetLatestRecoveryTimeResponse)` |   
  
### getLatestRecoveryTimeCallable()
    
    
    public final UnaryCallable<SqlInstancesGetLatestRecoveryTimeRequest,SqlInstancesGetLatestRecoveryTimeResponse> getLatestRecoveryTimeCallable()

Get Latest Recovery Time for a given instance.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (SqlInstancesServiceClient sqlInstancesServiceClient = SqlInstancesServiceClient.create()) {
       SqlInstancesGetLatestRecoveryTimeRequest request =
           SqlInstancesGetLatestRecoveryTimeRequest.newBuilder()
               .setInstance("instance555127957")
               .setProject("project-309310695")
               .setSourceInstanceDeletionTime(Timestamp.newBuilder().build())
               .build();
       ApiFuture<SqlInstancesGetLatestRecoveryTimeResponse> future =
           sqlInstancesServiceClient.getLatestRecoveryTimeCallable().futureCall(request);
       // Do something.
       SqlInstancesGetLatestRecoveryTimeResponse response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[SqlInstancesGetLatestRecoveryTimeRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-sql/latest/com.google.cloud.sql.v1.SqlInstancesGetLatestRecoveryTimeRequest),[SqlInstancesGetLatestRecoveryTimeResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-sql/latest/com.google.cloud.sql.v1.SqlInstancesGetLatestRecoveryTimeResponse)>` |   
  
### getSettings()
    
    
    public final @Nullable SqlInstancesServiceSettings getSettings()

**Returns**  
---  
**Type** | **Description**  
`@org.jspecify.annotations.Nullable com.google.cloud.sql.v1.SqlInstancesServiceSettings` |   
  
### getStub()
    
    
    public SqlInstancesServiceStub getStub()

**Returns**  
---  
**Type** | **Description**  
`[SqlInstancesServiceStub](https://docs.cloud.google.com/java/docs/reference/google-cloud-sql/latest/com.google.cloud.sql.v1.stub.SqlInstancesServiceStub)` |   
  
### import_(SqlInstancesImportRequest request)
    
    
    public final Operation import_(SqlInstancesImportRequest request)

Imports data into a Cloud SQL instance from a SQL dump or CSV file in Cloud Storage.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (SqlInstancesServiceClient sqlInstancesServiceClient = SqlInstancesServiceClient.create()) {
       SqlInstancesImportRequest request =
           SqlInstancesImportRequest.newBuilder()
               .setInstance("instance555127957")
               .setProject("project-309310695")
               .setBody(InstancesImportRequest.newBuilder().build())
               .build();
       Operation response = sqlInstancesServiceClient.import_(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[SqlInstancesImportRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-sql/latest/com.google.cloud.sql.v1.SqlInstancesImportRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-sql/latest/com.google.cloud.sql.v1.Operation)` |   
  
### import_Callable()
    
    
    public final UnaryCallable<SqlInstancesImportRequest,Operation> import_Callable()

Imports data into a Cloud SQL instance from a SQL dump or CSV file in Cloud Storage.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (SqlInstancesServiceClient sqlInstancesServiceClient = SqlInstancesServiceClient.create()) {
       SqlInstancesImportRequest request =
           SqlInstancesImportRequest.newBuilder()
               .setInstance("instance555127957")
               .setProject("project-309310695")
               .setBody(InstancesImportRequest.newBuilder().build())
               .build();
       ApiFuture<Operation> future = sqlInstancesServiceClient.importCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[SqlInstancesImportRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-sql/latest/com.google.cloud.sql.v1.SqlInstancesImportRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-sql/latest/com.google.cloud.sql.v1.Operation)>` |   
  
### insert(SqlInstancesInsertRequest request)
    
    
    public final Operation insert(SqlInstancesInsertRequest request)

Creates a new Cloud SQL instance.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (SqlInstancesServiceClient sqlInstancesServiceClient = SqlInstancesServiceClient.create()) {
       SqlInstancesInsertRequest request =
           SqlInstancesInsertRequest.newBuilder()
               .setProject("project-309310695")
               .setBody(DatabaseInstance.newBuilder().build())
               .build();
       Operation response = sqlInstancesServiceClient.insert(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[SqlInstancesInsertRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-sql/latest/com.google.cloud.sql.v1.SqlInstancesInsertRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-sql/latest/com.google.cloud.sql.v1.Operation)` |   
  
### insertCallable()
    
    
    public final UnaryCallable<SqlInstancesInsertRequest,Operation> insertCallable()

Creates a new Cloud SQL instance.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (SqlInstancesServiceClient sqlInstancesServiceClient = SqlInstancesServiceClient.create()) {
       SqlInstancesInsertRequest request =
           SqlInstancesInsertRequest.newBuilder()
               .setProject("project-309310695")
               .setBody(DatabaseInstance.newBuilder().build())
               .build();
       ApiFuture<Operation> future = sqlInstancesServiceClient.insertCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[SqlInstancesInsertRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-sql/latest/com.google.cloud.sql.v1.SqlInstancesInsertRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-sql/latest/com.google.cloud.sql.v1.Operation)>` |   
  
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
  
### list(SqlInstancesListRequest request)
    
    
    public final InstancesListResponse list(SqlInstancesListRequest request)

Lists instances under a given project.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (SqlInstancesServiceClient sqlInstancesServiceClient = SqlInstancesServiceClient.create()) {
       SqlInstancesListRequest request =
           SqlInstancesListRequest.newBuilder()
               .setFilter("filter-1274492040")
               .setMaxResults(1128457243)
               .setPageToken("pageToken873572522")
               .setProject("project-309310695")
               .build();
       InstancesListResponse response = sqlInstancesServiceClient.list(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[SqlInstancesListRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-sql/latest/com.google.cloud.sql.v1.SqlInstancesListRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[InstancesListResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-sql/latest/com.google.cloud.sql.v1.InstancesListResponse)` |   
  
### listCallable()
    
    
    public final UnaryCallable<SqlInstancesListRequest,InstancesListResponse> listCallable()

Lists instances under a given project.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (SqlInstancesServiceClient sqlInstancesServiceClient = SqlInstancesServiceClient.create()) {
       SqlInstancesListRequest request =
           SqlInstancesListRequest.newBuilder()
               .setFilter("filter-1274492040")
               .setMaxResults(1128457243)
               .setPageToken("pageToken873572522")
               .setProject("project-309310695")
               .build();
       ApiFuture<InstancesListResponse> future =
           sqlInstancesServiceClient.listCallable().futureCall(request);
       // Do something.
       InstancesListResponse response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[SqlInstancesListRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-sql/latest/com.google.cloud.sql.v1.SqlInstancesListRequest),[InstancesListResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-sql/latest/com.google.cloud.sql.v1.InstancesListResponse)>` |   
  
### listEntraIdCertificates(SqlInstancesListEntraIdCertificatesRequest request)
    
    
    public final InstancesListEntraIdCertificatesResponse listEntraIdCertificates(SqlInstancesListEntraIdCertificatesRequest request)

Lists all versions of EntraID certificates for the specified instance. There can be up to three sets of certificates listed: the certificate that is currently in use, a future that has been added but not yet used to sign a certificate, and a certificate that has been rotated out.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (SqlInstancesServiceClient sqlInstancesServiceClient = SqlInstancesServiceClient.create()) {
       SqlInstancesListEntraIdCertificatesRequest request =
           SqlInstancesListEntraIdCertificatesRequest.newBuilder()
               .setInstance("instance555127957")
               .setProject("project-309310695")
               .build();
       InstancesListEntraIdCertificatesResponse response =
           sqlInstancesServiceClient.listEntraIdCertificates(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[SqlInstancesListEntraIdCertificatesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-sql/latest/com.google.cloud.sql.v1.SqlInstancesListEntraIdCertificatesRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[InstancesListEntraIdCertificatesResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-sql/latest/com.google.cloud.sql.v1.InstancesListEntraIdCertificatesResponse)` |   
  
### listEntraIdCertificatesCallable()
    
    
    public final UnaryCallable<SqlInstancesListEntraIdCertificatesRequest,InstancesListEntraIdCertificatesResponse> listEntraIdCertificatesCallable()

Lists all versions of EntraID certificates for the specified instance. There can be up to three sets of certificates listed: the certificate that is currently in use, a future that has been added but not yet used to sign a certificate, and a certificate that has been rotated out.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (SqlInstancesServiceClient sqlInstancesServiceClient = SqlInstancesServiceClient.create()) {
       SqlInstancesListEntraIdCertificatesRequest request =
           SqlInstancesListEntraIdCertificatesRequest.newBuilder()
               .setInstance("instance555127957")
               .setProject("project-309310695")
               .build();
       ApiFuture<InstancesListEntraIdCertificatesResponse> future =
           sqlInstancesServiceClient.listEntraIdCertificatesCallable().futureCall(request);
       // Do something.
       InstancesListEntraIdCertificatesResponse response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[SqlInstancesListEntraIdCertificatesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-sql/latest/com.google.cloud.sql.v1.SqlInstancesListEntraIdCertificatesRequest),[InstancesListEntraIdCertificatesResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-sql/latest/com.google.cloud.sql.v1.InstancesListEntraIdCertificatesResponse)>` |   
  
### listServerCas(SqlInstancesListServerCasRequest request)
    
    
    public final InstancesListServerCasResponse listServerCas(SqlInstancesListServerCasRequest request)

Lists all of the trusted Certificate Authorities (CAs) for the specified instance. There can be up to three CAs listed: the CA that was used to sign the certificate that is currently in use, a CA that has been added but not yet used to sign a certificate, and a CA used to sign a certificate that has previously rotated out.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (SqlInstancesServiceClient sqlInstancesServiceClient = SqlInstancesServiceClient.create()) {
       SqlInstancesListServerCasRequest request =
           SqlInstancesListServerCasRequest.newBuilder()
               .setInstance("instance555127957")
               .setProject("project-309310695")
               .build();
       InstancesListServerCasResponse response = sqlInstancesServiceClient.listServerCas(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[SqlInstancesListServerCasRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-sql/latest/com.google.cloud.sql.v1.SqlInstancesListServerCasRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[InstancesListServerCasResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-sql/latest/com.google.cloud.sql.v1.InstancesListServerCasResponse)` |   
  
### listServerCasCallable()
    
    
    public final UnaryCallable<SqlInstancesListServerCasRequest,InstancesListServerCasResponse> listServerCasCallable()

Lists all of the trusted Certificate Authorities (CAs) for the specified instance. There can be up to three CAs listed: the CA that was used to sign the certificate that is currently in use, a CA that has been added but not yet used to sign a certificate, and a CA used to sign a certificate that has previously rotated out.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (SqlInstancesServiceClient sqlInstancesServiceClient = SqlInstancesServiceClient.create()) {
       SqlInstancesListServerCasRequest request =
           SqlInstancesListServerCasRequest.newBuilder()
               .setInstance("instance555127957")
               .setProject("project-309310695")
               .build();
       ApiFuture<InstancesListServerCasResponse> future =
           sqlInstancesServiceClient.listServerCasCallable().futureCall(request);
       // Do something.
       InstancesListServerCasResponse response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[SqlInstancesListServerCasRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-sql/latest/com.google.cloud.sql.v1.SqlInstancesListServerCasRequest),[InstancesListServerCasResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-sql/latest/com.google.cloud.sql.v1.InstancesListServerCasResponse)>` |   
  
### listServerCertificates(SqlInstancesListServerCertificatesRequest request)
    
    
    public final InstancesListServerCertificatesResponse listServerCertificates(SqlInstancesListServerCertificatesRequest request)

Lists all versions of server certificates and certificate authorities (CAs) for the specified instance. There can be up to three sets of certs listed: the certificate that is currently in use, a future that has been added but not yet used to sign a certificate, and a certificate that has been rotated out. For instances not using Certificate Authority Service (CAS) server CA, use ListServerCas instead.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (SqlInstancesServiceClient sqlInstancesServiceClient = SqlInstancesServiceClient.create()) {
       SqlInstancesListServerCertificatesRequest request =
           SqlInstancesListServerCertificatesRequest.newBuilder()
               .setInstance("instance555127957")
               .setProject("project-309310695")
               .build();
       InstancesListServerCertificatesResponse response =
           sqlInstancesServiceClient.listServerCertificates(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[SqlInstancesListServerCertificatesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-sql/latest/com.google.cloud.sql.v1.SqlInstancesListServerCertificatesRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[InstancesListServerCertificatesResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-sql/latest/com.google.cloud.sql.v1.InstancesListServerCertificatesResponse)` |   
  
### listServerCertificatesCallable()
    
    
    public final UnaryCallable<SqlInstancesListServerCertificatesRequest,InstancesListServerCertificatesResponse> listServerCertificatesCallable()

Lists all versions of server certificates and certificate authorities (CAs) for the specified instance. There can be up to three sets of certs listed: the certificate that is currently in use, a future that has been added but not yet used to sign a certificate, and a certificate that has been rotated out. For instances not using Certificate Authority Service (CAS) server CA, use ListServerCas instead.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (SqlInstancesServiceClient sqlInstancesServiceClient = SqlInstancesServiceClient.create()) {
       SqlInstancesListServerCertificatesRequest request =
           SqlInstancesListServerCertificatesRequest.newBuilder()
               .setInstance("instance555127957")
               .setProject("project-309310695")
               .build();
       ApiFuture<InstancesListServerCertificatesResponse> future =
           sqlInstancesServiceClient.listServerCertificatesCallable().futureCall(request);
       // Do something.
       InstancesListServerCertificatesResponse response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[SqlInstancesListServerCertificatesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-sql/latest/com.google.cloud.sql.v1.SqlInstancesListServerCertificatesRequest),[InstancesListServerCertificatesResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-sql/latest/com.google.cloud.sql.v1.InstancesListServerCertificatesResponse)>` |   
  
### patch(SqlInstancesPatchRequest request)
    
    
    public final Operation patch(SqlInstancesPatchRequest request)

Partially updates settings of a Cloud SQL instance by merging the request with the current configuration. This method supports patch semantics.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (SqlInstancesServiceClient sqlInstancesServiceClient = SqlInstancesServiceClient.create()) {
       SqlInstancesPatchRequest request =
           SqlInstancesPatchRequest.newBuilder()
               .setInstance("instance555127957")
               .setProject("project-309310695")
               .setReconcilePscNetworking(true)
               .setReconcilePscNetworkingForce(true)
               .setBody(DatabaseInstance.newBuilder().build())
               .build();
       Operation response = sqlInstancesServiceClient.patch(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[SqlInstancesPatchRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-sql/latest/com.google.cloud.sql.v1.SqlInstancesPatchRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-sql/latest/com.google.cloud.sql.v1.Operation)` |   
  
### patchCallable()
    
    
    public final UnaryCallable<SqlInstancesPatchRequest,Operation> patchCallable()

Partially updates settings of a Cloud SQL instance by merging the request with the current configuration. This method supports patch semantics.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (SqlInstancesServiceClient sqlInstancesServiceClient = SqlInstancesServiceClient.create()) {
       SqlInstancesPatchRequest request =
           SqlInstancesPatchRequest.newBuilder()
               .setInstance("instance555127957")
               .setProject("project-309310695")
               .setReconcilePscNetworking(true)
               .setReconcilePscNetworkingForce(true)
               .setBody(DatabaseInstance.newBuilder().build())
               .build();
       ApiFuture<Operation> future = sqlInstancesServiceClient.patchCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[SqlInstancesPatchRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-sql/latest/com.google.cloud.sql.v1.SqlInstancesPatchRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-sql/latest/com.google.cloud.sql.v1.Operation)>` |   
  
### performDiskShrink(SqlInstancesPerformDiskShrinkRequest request)
    
    
    public final Operation performDiskShrink(SqlInstancesPerformDiskShrinkRequest request)

Perform Disk Shrink on primary instance.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (SqlInstancesServiceClient sqlInstancesServiceClient = SqlInstancesServiceClient.create()) {
       SqlInstancesPerformDiskShrinkRequest request =
           SqlInstancesPerformDiskShrinkRequest.newBuilder()
               .setInstance("instance555127957")
               .setProject("project-309310695")
               .setBody(PerformDiskShrinkContext.newBuilder().build())
               .build();
       Operation response = sqlInstancesServiceClient.performDiskShrink(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[SqlInstancesPerformDiskShrinkRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-sql/latest/com.google.cloud.sql.v1.SqlInstancesPerformDiskShrinkRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-sql/latest/com.google.cloud.sql.v1.Operation)` |   
  
### performDiskShrinkCallable()
    
    
    public final UnaryCallable<SqlInstancesPerformDiskShrinkRequest,Operation> performDiskShrinkCallable()

Perform Disk Shrink on primary instance.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (SqlInstancesServiceClient sqlInstancesServiceClient = SqlInstancesServiceClient.create()) {
       SqlInstancesPerformDiskShrinkRequest request =
           SqlInstancesPerformDiskShrinkRequest.newBuilder()
               .setInstance("instance555127957")
               .setProject("project-309310695")
               .setBody(PerformDiskShrinkContext.newBuilder().build())
               .build();
       ApiFuture<Operation> future =
           sqlInstancesServiceClient.performDiskShrinkCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[SqlInstancesPerformDiskShrinkRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-sql/latest/com.google.cloud.sql.v1.SqlInstancesPerformDiskShrinkRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-sql/latest/com.google.cloud.sql.v1.Operation)>` |   
  
### pointInTimeRestore(SqlInstancesPointInTimeRestoreRequest request)
    
    
    public final Operation pointInTimeRestore(SqlInstancesPointInTimeRestoreRequest request)

Point in time restore for an instance managed by Google Cloud Backup and Disaster Recovery.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (SqlInstancesServiceClient sqlInstancesServiceClient = SqlInstancesServiceClient.create()) {
       SqlInstancesPointInTimeRestoreRequest request =
           SqlInstancesPointInTimeRestoreRequest.newBuilder()
               .setParent("parent-995424086")
               .setContext(PointInTimeRestoreContext.newBuilder().build())
               .build();
       Operation response = sqlInstancesServiceClient.pointInTimeRestore(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[SqlInstancesPointInTimeRestoreRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-sql/latest/com.google.cloud.sql.v1.SqlInstancesPointInTimeRestoreRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-sql/latest/com.google.cloud.sql.v1.Operation)` |   
  
### pointInTimeRestoreCallable()
    
    
    public final UnaryCallable<SqlInstancesPointInTimeRestoreRequest,Operation> pointInTimeRestoreCallable()

Point in time restore for an instance managed by Google Cloud Backup and Disaster Recovery.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (SqlInstancesServiceClient sqlInstancesServiceClient = SqlInstancesServiceClient.create()) {
       SqlInstancesPointInTimeRestoreRequest request =
           SqlInstancesPointInTimeRestoreRequest.newBuilder()
               .setParent("parent-995424086")
               .setContext(PointInTimeRestoreContext.newBuilder().build())
               .build();
       ApiFuture<Operation> future =
           sqlInstancesServiceClient.pointInTimeRestoreCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[SqlInstancesPointInTimeRestoreRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-sql/latest/com.google.cloud.sql.v1.SqlInstancesPointInTimeRestoreRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-sql/latest/com.google.cloud.sql.v1.Operation)>` |   
  
### preCheckMajorVersionUpgrade(SqlInstancesPreCheckMajorVersionUpgradeRequest request)
    
    
    public final Operation preCheckMajorVersionUpgrade(SqlInstancesPreCheckMajorVersionUpgradeRequest request)

Execute MVU Pre-checks

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (SqlInstancesServiceClient sqlInstancesServiceClient = SqlInstancesServiceClient.create()) {
       SqlInstancesPreCheckMajorVersionUpgradeRequest request =
           SqlInstancesPreCheckMajorVersionUpgradeRequest.newBuilder()
               .setInstance("instance555127957")
               .setProject("project-309310695")
               .setBody(InstancesPreCheckMajorVersionUpgradeRequest.newBuilder().build())
               .build();
       Operation response = sqlInstancesServiceClient.preCheckMajorVersionUpgrade(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[SqlInstancesPreCheckMajorVersionUpgradeRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-sql/latest/com.google.cloud.sql.v1.SqlInstancesPreCheckMajorVersionUpgradeRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-sql/latest/com.google.cloud.sql.v1.Operation)` |   
  
### preCheckMajorVersionUpgradeCallable()
    
    
    public final UnaryCallable<SqlInstancesPreCheckMajorVersionUpgradeRequest,Operation> preCheckMajorVersionUpgradeCallable()

Execute MVU Pre-checks

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (SqlInstancesServiceClient sqlInstancesServiceClient = SqlInstancesServiceClient.create()) {
       SqlInstancesPreCheckMajorVersionUpgradeRequest request =
           SqlInstancesPreCheckMajorVersionUpgradeRequest.newBuilder()
               .setInstance("instance555127957")
               .setProject("project-309310695")
               .setBody(InstancesPreCheckMajorVersionUpgradeRequest.newBuilder().build())
               .build();
       ApiFuture<Operation> future =
           sqlInstancesServiceClient.preCheckMajorVersionUpgradeCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[SqlInstancesPreCheckMajorVersionUpgradeRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-sql/latest/com.google.cloud.sql.v1.SqlInstancesPreCheckMajorVersionUpgradeRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-sql/latest/com.google.cloud.sql.v1.Operation)>` |   
  
### promoteReplica(SqlInstancesPromoteReplicaRequest request)
    
    
    public final Operation promoteReplica(SqlInstancesPromoteReplicaRequest request)

Promotes the read replica instance to be an independent Cloud SQL primary instance. Using this operation might cause your instance to restart.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (SqlInstancesServiceClient sqlInstancesServiceClient = SqlInstancesServiceClient.create()) {
       SqlInstancesPromoteReplicaRequest request =
           SqlInstancesPromoteReplicaRequest.newBuilder()
               .setInstance("instance555127957")
               .setProject("project-309310695")
               .setFailover(true)
               .build();
       Operation response = sqlInstancesServiceClient.promoteReplica(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[SqlInstancesPromoteReplicaRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-sql/latest/com.google.cloud.sql.v1.SqlInstancesPromoteReplicaRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-sql/latest/com.google.cloud.sql.v1.Operation)` |   
  
### promoteReplicaCallable()
    
    
    public final UnaryCallable<SqlInstancesPromoteReplicaRequest,Operation> promoteReplicaCallable()

Promotes the read replica instance to be an independent Cloud SQL primary instance. Using this operation might cause your instance to restart.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (SqlInstancesServiceClient sqlInstancesServiceClient = SqlInstancesServiceClient.create()) {
       SqlInstancesPromoteReplicaRequest request =
           SqlInstancesPromoteReplicaRequest.newBuilder()
               .setInstance("instance555127957")
               .setProject("project-309310695")
               .setFailover(true)
               .build();
       ApiFuture<Operation> future =
           sqlInstancesServiceClient.promoteReplicaCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[SqlInstancesPromoteReplicaRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-sql/latest/com.google.cloud.sql.v1.SqlInstancesPromoteReplicaRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-sql/latest/com.google.cloud.sql.v1.Operation)>` |   
  
### reencrypt(SqlInstancesReencryptRequest request)
    
    
    public final Operation reencrypt(SqlInstancesReencryptRequest request)

Reencrypt CMEK instance with latest key version.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (SqlInstancesServiceClient sqlInstancesServiceClient = SqlInstancesServiceClient.create()) {
       SqlInstancesReencryptRequest request =
           SqlInstancesReencryptRequest.newBuilder()
               .setInstance("instance555127957")
               .setProject("project-309310695")
               .setBody(InstancesReencryptRequest.newBuilder().build())
               .build();
       Operation response = sqlInstancesServiceClient.reencrypt(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[SqlInstancesReencryptRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-sql/latest/com.google.cloud.sql.v1.SqlInstancesReencryptRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-sql/latest/com.google.cloud.sql.v1.Operation)` |   
  
### reencryptCallable()
    
    
    public final UnaryCallable<SqlInstancesReencryptRequest,Operation> reencryptCallable()

Reencrypt CMEK instance with latest key version.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (SqlInstancesServiceClient sqlInstancesServiceClient = SqlInstancesServiceClient.create()) {
       SqlInstancesReencryptRequest request =
           SqlInstancesReencryptRequest.newBuilder()
               .setInstance("instance555127957")
               .setProject("project-309310695")
               .setBody(InstancesReencryptRequest.newBuilder().build())
               .build();
       ApiFuture<Operation> future =
           sqlInstancesServiceClient.reencryptCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[SqlInstancesReencryptRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-sql/latest/com.google.cloud.sql.v1.SqlInstancesReencryptRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-sql/latest/com.google.cloud.sql.v1.Operation)>` |   
  
### releaseSsrsLease(SqlInstancesReleaseSsrsLeaseRequest request)
    
    
    public final SqlInstancesReleaseSsrsLeaseResponse releaseSsrsLease(SqlInstancesReleaseSsrsLeaseRequest request)

Release a lease for the setup of SQL Server Reporting Services (SSRS).

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (SqlInstancesServiceClient sqlInstancesServiceClient = SqlInstancesServiceClient.create()) {
       SqlInstancesReleaseSsrsLeaseRequest request =
           SqlInstancesReleaseSsrsLeaseRequest.newBuilder()
               .setInstance("instance555127957")
               .setProject("project-309310695")
               .build();
       SqlInstancesReleaseSsrsLeaseResponse response =
           sqlInstancesServiceClient.releaseSsrsLease(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[SqlInstancesReleaseSsrsLeaseRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-sql/latest/com.google.cloud.sql.v1.SqlInstancesReleaseSsrsLeaseRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[SqlInstancesReleaseSsrsLeaseResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-sql/latest/com.google.cloud.sql.v1.SqlInstancesReleaseSsrsLeaseResponse)` |   
  
### releaseSsrsLeaseCallable()
    
    
    public final UnaryCallable<SqlInstancesReleaseSsrsLeaseRequest,SqlInstancesReleaseSsrsLeaseResponse> releaseSsrsLeaseCallable()

Release a lease for the setup of SQL Server Reporting Services (SSRS).

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (SqlInstancesServiceClient sqlInstancesServiceClient = SqlInstancesServiceClient.create()) {
       SqlInstancesReleaseSsrsLeaseRequest request =
           SqlInstancesReleaseSsrsLeaseRequest.newBuilder()
               .setInstance("instance555127957")
               .setProject("project-309310695")
               .build();
       ApiFuture<SqlInstancesReleaseSsrsLeaseResponse> future =
           sqlInstancesServiceClient.releaseSsrsLeaseCallable().futureCall(request);
       // Do something.
       SqlInstancesReleaseSsrsLeaseResponse response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[SqlInstancesReleaseSsrsLeaseRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-sql/latest/com.google.cloud.sql.v1.SqlInstancesReleaseSsrsLeaseRequest),[SqlInstancesReleaseSsrsLeaseResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-sql/latest/com.google.cloud.sql.v1.SqlInstancesReleaseSsrsLeaseResponse)>` |   
  
### rescheduleMaintenance(SqlInstancesRescheduleMaintenanceRequest request)
    
    
    public final Operation rescheduleMaintenance(SqlInstancesRescheduleMaintenanceRequest request)

Reschedules the maintenance on the given instance.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (SqlInstancesServiceClient sqlInstancesServiceClient = SqlInstancesServiceClient.create()) {
       SqlInstancesRescheduleMaintenanceRequest request =
           SqlInstancesRescheduleMaintenanceRequest.newBuilder()
               .setInstance("instance555127957")
               .setProject("project-309310695")
               .setBody(SqlInstancesRescheduleMaintenanceRequestBody.newBuilder().build())
               .build();
       Operation response = sqlInstancesServiceClient.rescheduleMaintenance(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[SqlInstancesRescheduleMaintenanceRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-sql/latest/com.google.cloud.sql.v1.SqlInstancesRescheduleMaintenanceRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-sql/latest/com.google.cloud.sql.v1.Operation)` |   
  
### rescheduleMaintenanceCallable()
    
    
    public final UnaryCallable<SqlInstancesRescheduleMaintenanceRequest,Operation> rescheduleMaintenanceCallable()

Reschedules the maintenance on the given instance.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (SqlInstancesServiceClient sqlInstancesServiceClient = SqlInstancesServiceClient.create()) {
       SqlInstancesRescheduleMaintenanceRequest request =
           SqlInstancesRescheduleMaintenanceRequest.newBuilder()
               .setInstance("instance555127957")
               .setProject("project-309310695")
               .setBody(SqlInstancesRescheduleMaintenanceRequestBody.newBuilder().build())
               .build();
       ApiFuture<Operation> future =
           sqlInstancesServiceClient.rescheduleMaintenanceCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[SqlInstancesRescheduleMaintenanceRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-sql/latest/com.google.cloud.sql.v1.SqlInstancesRescheduleMaintenanceRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-sql/latest/com.google.cloud.sql.v1.Operation)>` |   
  
### resetReplicaSize(SqlInstancesResetReplicaSizeRequest request)
    
    
    public final Operation resetReplicaSize(SqlInstancesResetReplicaSizeRequest request)

Reset Replica Size to primary instance disk size.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (SqlInstancesServiceClient sqlInstancesServiceClient = SqlInstancesServiceClient.create()) {
       SqlInstancesResetReplicaSizeRequest request =
           SqlInstancesResetReplicaSizeRequest.newBuilder()
               .setInstance("instance555127957")
               .setProject("project-309310695")
               .build();
       Operation response = sqlInstancesServiceClient.resetReplicaSize(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[SqlInstancesResetReplicaSizeRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-sql/latest/com.google.cloud.sql.v1.SqlInstancesResetReplicaSizeRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-sql/latest/com.google.cloud.sql.v1.Operation)` |   
  
### resetReplicaSizeCallable()
    
    
    public final UnaryCallable<SqlInstancesResetReplicaSizeRequest,Operation> resetReplicaSizeCallable()

Reset Replica Size to primary instance disk size.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (SqlInstancesServiceClient sqlInstancesServiceClient = SqlInstancesServiceClient.create()) {
       SqlInstancesResetReplicaSizeRequest request =
           SqlInstancesResetReplicaSizeRequest.newBuilder()
               .setInstance("instance555127957")
               .setProject("project-309310695")
               .build();
       ApiFuture<Operation> future =
           sqlInstancesServiceClient.resetReplicaSizeCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[SqlInstancesResetReplicaSizeRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-sql/latest/com.google.cloud.sql.v1.SqlInstancesResetReplicaSizeRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-sql/latest/com.google.cloud.sql.v1.Operation)>` |   
  
### resetSslConfig(SqlInstancesResetSslConfigRequest request)
    
    
    public final Operation resetSslConfig(SqlInstancesResetSslConfigRequest request)

Deletes all client certificates and generates a new server SSL certificate for the instance.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (SqlInstancesServiceClient sqlInstancesServiceClient = SqlInstancesServiceClient.create()) {
       SqlInstancesResetSslConfigRequest request =
           SqlInstancesResetSslConfigRequest.newBuilder()
               .setInstance("instance555127957")
               .setProject("project-309310695")
               .build();
       Operation response = sqlInstancesServiceClient.resetSslConfig(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[SqlInstancesResetSslConfigRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-sql/latest/com.google.cloud.sql.v1.SqlInstancesResetSslConfigRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-sql/latest/com.google.cloud.sql.v1.Operation)` |   
  
### resetSslConfigCallable()
    
    
    public final UnaryCallable<SqlInstancesResetSslConfigRequest,Operation> resetSslConfigCallable()

Deletes all client certificates and generates a new server SSL certificate for the instance.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (SqlInstancesServiceClient sqlInstancesServiceClient = SqlInstancesServiceClient.create()) {
       SqlInstancesResetSslConfigRequest request =
           SqlInstancesResetSslConfigRequest.newBuilder()
               .setInstance("instance555127957")
               .setProject("project-309310695")
               .build();
       ApiFuture<Operation> future =
           sqlInstancesServiceClient.resetSslConfigCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[SqlInstancesResetSslConfigRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-sql/latest/com.google.cloud.sql.v1.SqlInstancesResetSslConfigRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-sql/latest/com.google.cloud.sql.v1.Operation)>` |   
  
### restart(SqlInstancesRestartRequest request)
    
    
    public final Operation restart(SqlInstancesRestartRequest request)

Restarts a Cloud SQL instance.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (SqlInstancesServiceClient sqlInstancesServiceClient = SqlInstancesServiceClient.create()) {
       SqlInstancesRestartRequest request =
           SqlInstancesRestartRequest.newBuilder()
               .setInstance("instance555127957")
               .setProject("project-309310695")
               .build();
       Operation response = sqlInstancesServiceClient.restart(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[SqlInstancesRestartRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-sql/latest/com.google.cloud.sql.v1.SqlInstancesRestartRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-sql/latest/com.google.cloud.sql.v1.Operation)` |   
  
### restartCallable()
    
    
    public final UnaryCallable<SqlInstancesRestartRequest,Operation> restartCallable()

Restarts a Cloud SQL instance.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (SqlInstancesServiceClient sqlInstancesServiceClient = SqlInstancesServiceClient.create()) {
       SqlInstancesRestartRequest request =
           SqlInstancesRestartRequest.newBuilder()
               .setInstance("instance555127957")
               .setProject("project-309310695")
               .build();
       ApiFuture<Operation> future = sqlInstancesServiceClient.restartCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[SqlInstancesRestartRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-sql/latest/com.google.cloud.sql.v1.SqlInstancesRestartRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-sql/latest/com.google.cloud.sql.v1.Operation)>` |   
  
### restoreBackup(SqlInstancesRestoreBackupRequest request)
    
    
    public final Operation restoreBackup(SqlInstancesRestoreBackupRequest request)

Restores a backup of a Cloud SQL instance. Using this operation might cause your instance to restart.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (SqlInstancesServiceClient sqlInstancesServiceClient = SqlInstancesServiceClient.create()) {
       SqlInstancesRestoreBackupRequest request =
           SqlInstancesRestoreBackupRequest.newBuilder()
               .setInstance("instance555127957")
               .setProject("project-309310695")
               .setBody(InstancesRestoreBackupRequest.newBuilder().build())
               .build();
       Operation response = sqlInstancesServiceClient.restoreBackup(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[SqlInstancesRestoreBackupRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-sql/latest/com.google.cloud.sql.v1.SqlInstancesRestoreBackupRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-sql/latest/com.google.cloud.sql.v1.Operation)` |   
  
### restoreBackupCallable()
    
    
    public final UnaryCallable<SqlInstancesRestoreBackupRequest,Operation> restoreBackupCallable()

Restores a backup of a Cloud SQL instance. Using this operation might cause your instance to restart.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (SqlInstancesServiceClient sqlInstancesServiceClient = SqlInstancesServiceClient.create()) {
       SqlInstancesRestoreBackupRequest request =
           SqlInstancesRestoreBackupRequest.newBuilder()
               .setInstance("instance555127957")
               .setProject("project-309310695")
               .setBody(InstancesRestoreBackupRequest.newBuilder().build())
               .build();
       ApiFuture<Operation> future =
           sqlInstancesServiceClient.restoreBackupCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[SqlInstancesRestoreBackupRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-sql/latest/com.google.cloud.sql.v1.SqlInstancesRestoreBackupRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-sql/latest/com.google.cloud.sql.v1.Operation)>` |   
  
### rotateEntraIdCertificate(SqlInstancesRotateEntraIdCertificateRequest request)
    
    
    public final Operation rotateEntraIdCertificate(SqlInstancesRotateEntraIdCertificateRequest request)

Rotates the server certificate version to one previously added with the addEntraIdCertificate method.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (SqlInstancesServiceClient sqlInstancesServiceClient = SqlInstancesServiceClient.create()) {
       SqlInstancesRotateEntraIdCertificateRequest request =
           SqlInstancesRotateEntraIdCertificateRequest.newBuilder()
               .setInstance("instance555127957")
               .setProject("project-309310695")
               .setBody(InstancesRotateEntraIdCertificateRequest.newBuilder().build())
               .build();
       Operation response = sqlInstancesServiceClient.rotateEntraIdCertificate(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[SqlInstancesRotateEntraIdCertificateRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-sql/latest/com.google.cloud.sql.v1.SqlInstancesRotateEntraIdCertificateRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-sql/latest/com.google.cloud.sql.v1.Operation)` |   
  
### rotateEntraIdCertificateCallable()
    
    
    public final UnaryCallable<SqlInstancesRotateEntraIdCertificateRequest,Operation> rotateEntraIdCertificateCallable()

Rotates the server certificate version to one previously added with the addEntraIdCertificate method.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (SqlInstancesServiceClient sqlInstancesServiceClient = SqlInstancesServiceClient.create()) {
       SqlInstancesRotateEntraIdCertificateRequest request =
           SqlInstancesRotateEntraIdCertificateRequest.newBuilder()
               .setInstance("instance555127957")
               .setProject("project-309310695")
               .setBody(InstancesRotateEntraIdCertificateRequest.newBuilder().build())
               .build();
       ApiFuture<Operation> future =
           sqlInstancesServiceClient.rotateEntraIdCertificateCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[SqlInstancesRotateEntraIdCertificateRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-sql/latest/com.google.cloud.sql.v1.SqlInstancesRotateEntraIdCertificateRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-sql/latest/com.google.cloud.sql.v1.Operation)>` |   
  
### rotateServerCa(SqlInstancesRotateServerCaRequest request)
    
    
    public final Operation rotateServerCa(SqlInstancesRotateServerCaRequest request)

Rotates the server certificate to one signed by the Certificate Authority (CA) version previously added with the addServerCA method. For instances that have enabled Certificate Authority Service (CAS) based server CA, use RotateServerCertificate to rotate the server certificate.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (SqlInstancesServiceClient sqlInstancesServiceClient = SqlInstancesServiceClient.create()) {
       SqlInstancesRotateServerCaRequest request =
           SqlInstancesRotateServerCaRequest.newBuilder()
               .setInstance("instance555127957")
               .setProject("project-309310695")
               .setBody(InstancesRotateServerCaRequest.newBuilder().build())
               .build();
       Operation response = sqlInstancesServiceClient.rotateServerCa(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[SqlInstancesRotateServerCaRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-sql/latest/com.google.cloud.sql.v1.SqlInstancesRotateServerCaRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-sql/latest/com.google.cloud.sql.v1.Operation)` |   
  
### rotateServerCaCallable()
    
    
    public final UnaryCallable<SqlInstancesRotateServerCaRequest,Operation> rotateServerCaCallable()

Rotates the server certificate to one signed by the Certificate Authority (CA) version previously added with the addServerCA method. For instances that have enabled Certificate Authority Service (CAS) based server CA, use RotateServerCertificate to rotate the server certificate.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (SqlInstancesServiceClient sqlInstancesServiceClient = SqlInstancesServiceClient.create()) {
       SqlInstancesRotateServerCaRequest request =
           SqlInstancesRotateServerCaRequest.newBuilder()
               .setInstance("instance555127957")
               .setProject("project-309310695")
               .setBody(InstancesRotateServerCaRequest.newBuilder().build())
               .build();
       ApiFuture<Operation> future =
           sqlInstancesServiceClient.rotateServerCaCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[SqlInstancesRotateServerCaRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-sql/latest/com.google.cloud.sql.v1.SqlInstancesRotateServerCaRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-sql/latest/com.google.cloud.sql.v1.Operation)>` |   
  
### rotateServerCertificate(SqlInstancesRotateServerCertificateRequest request)
    
    
    public final Operation rotateServerCertificate(SqlInstancesRotateServerCertificateRequest request)

Rotates the server certificate version to one previously added with the addServerCertificate method. For instances not using Certificate Authority Service (CAS) server CA, use RotateServerCa instead.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (SqlInstancesServiceClient sqlInstancesServiceClient = SqlInstancesServiceClient.create()) {
       SqlInstancesRotateServerCertificateRequest request =
           SqlInstancesRotateServerCertificateRequest.newBuilder()
               .setInstance("instance555127957")
               .setProject("project-309310695")
               .setBody(InstancesRotateServerCertificateRequest.newBuilder().build())
               .build();
       Operation response = sqlInstancesServiceClient.rotateServerCertificate(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[SqlInstancesRotateServerCertificateRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-sql/latest/com.google.cloud.sql.v1.SqlInstancesRotateServerCertificateRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-sql/latest/com.google.cloud.sql.v1.Operation)` |   
  
### rotateServerCertificateCallable()
    
    
    public final UnaryCallable<SqlInstancesRotateServerCertificateRequest,Operation> rotateServerCertificateCallable()

Rotates the server certificate version to one previously added with the addServerCertificate method. For instances not using Certificate Authority Service (CAS) server CA, use RotateServerCa instead.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (SqlInstancesServiceClient sqlInstancesServiceClient = SqlInstancesServiceClient.create()) {
       SqlInstancesRotateServerCertificateRequest request =
           SqlInstancesRotateServerCertificateRequest.newBuilder()
               .setInstance("instance555127957")
               .setProject("project-309310695")
               .setBody(InstancesRotateServerCertificateRequest.newBuilder().build())
               .build();
       ApiFuture<Operation> future =
           sqlInstancesServiceClient.rotateServerCertificateCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[SqlInstancesRotateServerCertificateRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-sql/latest/com.google.cloud.sql.v1.SqlInstancesRotateServerCertificateRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-sql/latest/com.google.cloud.sql.v1.Operation)>` |   
  
### shutdown()
    
    
    public void shutdown()

### shutdownNow()
    
    
    public void shutdownNow()

### startExternalSync(SqlInstancesStartExternalSyncRequest request)
    
    
    public final Operation startExternalSync(SqlInstancesStartExternalSyncRequest request)

Start External primary instance migration.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (SqlInstancesServiceClient sqlInstancesServiceClient = SqlInstancesServiceClient.create()) {
       SqlInstancesStartExternalSyncRequest request =
           SqlInstancesStartExternalSyncRequest.newBuilder()
               .setInstance("instance555127957")
               .setProject("project-309310695")
               .setSkipVerification(true)
               .setSyncParallelLevel(ExternalSyncParallelLevel.forNumber(0))
               .setReplicaOverwriteEnabled(true)
               .build();
       Operation response = sqlInstancesServiceClient.startExternalSync(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[SqlInstancesStartExternalSyncRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-sql/latest/com.google.cloud.sql.v1.SqlInstancesStartExternalSyncRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-sql/latest/com.google.cloud.sql.v1.Operation)` |   
  
### startExternalSyncCallable()
    
    
    public final UnaryCallable<SqlInstancesStartExternalSyncRequest,Operation> startExternalSyncCallable()

Start External primary instance migration.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (SqlInstancesServiceClient sqlInstancesServiceClient = SqlInstancesServiceClient.create()) {
       SqlInstancesStartExternalSyncRequest request =
           SqlInstancesStartExternalSyncRequest.newBuilder()
               .setInstance("instance555127957")
               .setProject("project-309310695")
               .setSkipVerification(true)
               .setSyncParallelLevel(ExternalSyncParallelLevel.forNumber(0))
               .setReplicaOverwriteEnabled(true)
               .build();
       ApiFuture<Operation> future =
           sqlInstancesServiceClient.startExternalSyncCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[SqlInstancesStartExternalSyncRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-sql/latest/com.google.cloud.sql.v1.SqlInstancesStartExternalSyncRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-sql/latest/com.google.cloud.sql.v1.Operation)>` |   
  
### startReplica(SqlInstancesStartReplicaRequest request)
    
    
    public final Operation startReplica(SqlInstancesStartReplicaRequest request)

Starts the replication in the read replica instance.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (SqlInstancesServiceClient sqlInstancesServiceClient = SqlInstancesServiceClient.create()) {
       SqlInstancesStartReplicaRequest request =
           SqlInstancesStartReplicaRequest.newBuilder()
               .setInstance("instance555127957")
               .setProject("project-309310695")
               .build();
       Operation response = sqlInstancesServiceClient.startReplica(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[SqlInstancesStartReplicaRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-sql/latest/com.google.cloud.sql.v1.SqlInstancesStartReplicaRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-sql/latest/com.google.cloud.sql.v1.Operation)` |   
  
### startReplicaCallable()
    
    
    public final UnaryCallable<SqlInstancesStartReplicaRequest,Operation> startReplicaCallable()

Starts the replication in the read replica instance.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (SqlInstancesServiceClient sqlInstancesServiceClient = SqlInstancesServiceClient.create()) {
       SqlInstancesStartReplicaRequest request =
           SqlInstancesStartReplicaRequest.newBuilder()
               .setInstance("instance555127957")
               .setProject("project-309310695")
               .build();
       ApiFuture<Operation> future =
           sqlInstancesServiceClient.startReplicaCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[SqlInstancesStartReplicaRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-sql/latest/com.google.cloud.sql.v1.SqlInstancesStartReplicaRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-sql/latest/com.google.cloud.sql.v1.Operation)>` |   
  
### stopReplica(SqlInstancesStopReplicaRequest request)
    
    
    public final Operation stopReplica(SqlInstancesStopReplicaRequest request)

Stops the replication in the read replica instance.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (SqlInstancesServiceClient sqlInstancesServiceClient = SqlInstancesServiceClient.create()) {
       SqlInstancesStopReplicaRequest request =
           SqlInstancesStopReplicaRequest.newBuilder()
               .setInstance("instance555127957")
               .setProject("project-309310695")
               .build();
       Operation response = sqlInstancesServiceClient.stopReplica(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[SqlInstancesStopReplicaRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-sql/latest/com.google.cloud.sql.v1.SqlInstancesStopReplicaRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-sql/latest/com.google.cloud.sql.v1.Operation)` |   
  
### stopReplicaCallable()
    
    
    public final UnaryCallable<SqlInstancesStopReplicaRequest,Operation> stopReplicaCallable()

Stops the replication in the read replica instance.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (SqlInstancesServiceClient sqlInstancesServiceClient = SqlInstancesServiceClient.create()) {
       SqlInstancesStopReplicaRequest request =
           SqlInstancesStopReplicaRequest.newBuilder()
               .setInstance("instance555127957")
               .setProject("project-309310695")
               .build();
       ApiFuture<Operation> future =
           sqlInstancesServiceClient.stopReplicaCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[SqlInstancesStopReplicaRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-sql/latest/com.google.cloud.sql.v1.SqlInstancesStopReplicaRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-sql/latest/com.google.cloud.sql.v1.Operation)>` |   
  
### switchover(SqlInstancesSwitchoverRequest request)
    
    
    public final Operation switchover(SqlInstancesSwitchoverRequest request)

Switches over from the primary instance to the DR replica instance.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (SqlInstancesServiceClient sqlInstancesServiceClient = SqlInstancesServiceClient.create()) {
       SqlInstancesSwitchoverRequest request =
           SqlInstancesSwitchoverRequest.newBuilder()
               .setInstance("instance555127957")
               .setProject("project-309310695")
               .setDbTimeout(Duration.newBuilder().build())
               .build();
       Operation response = sqlInstancesServiceClient.switchover(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[SqlInstancesSwitchoverRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-sql/latest/com.google.cloud.sql.v1.SqlInstancesSwitchoverRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-sql/latest/com.google.cloud.sql.v1.Operation)` |   
  
### switchoverCallable()
    
    
    public final UnaryCallable<SqlInstancesSwitchoverRequest,Operation> switchoverCallable()

Switches over from the primary instance to the DR replica instance.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (SqlInstancesServiceClient sqlInstancesServiceClient = SqlInstancesServiceClient.create()) {
       SqlInstancesSwitchoverRequest request =
           SqlInstancesSwitchoverRequest.newBuilder()
               .setInstance("instance555127957")
               .setProject("project-309310695")
               .setDbTimeout(Duration.newBuilder().build())
               .build();
       ApiFuture<Operation> future =
           sqlInstancesServiceClient.switchoverCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[SqlInstancesSwitchoverRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-sql/latest/com.google.cloud.sql.v1.SqlInstancesSwitchoverRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-sql/latest/com.google.cloud.sql.v1.Operation)>` |   
  
### truncateLog(SqlInstancesTruncateLogRequest request)
    
    
    public final Operation truncateLog(SqlInstancesTruncateLogRequest request)

Truncate MySQL general and slow query log tables MySQL only.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (SqlInstancesServiceClient sqlInstancesServiceClient = SqlInstancesServiceClient.create()) {
       SqlInstancesTruncateLogRequest request =
           SqlInstancesTruncateLogRequest.newBuilder()
               .setInstance("instance555127957")
               .setProject("project-309310695")
               .setBody(InstancesTruncateLogRequest.newBuilder().build())
               .build();
       Operation response = sqlInstancesServiceClient.truncateLog(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[SqlInstancesTruncateLogRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-sql/latest/com.google.cloud.sql.v1.SqlInstancesTruncateLogRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-sql/latest/com.google.cloud.sql.v1.Operation)` |   
  
### truncateLogCallable()
    
    
    public final UnaryCallable<SqlInstancesTruncateLogRequest,Operation> truncateLogCallable()

Truncate MySQL general and slow query log tables MySQL only.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (SqlInstancesServiceClient sqlInstancesServiceClient = SqlInstancesServiceClient.create()) {
       SqlInstancesTruncateLogRequest request =
           SqlInstancesTruncateLogRequest.newBuilder()
               .setInstance("instance555127957")
               .setProject("project-309310695")
               .setBody(InstancesTruncateLogRequest.newBuilder().build())
               .build();
       ApiFuture<Operation> future =
           sqlInstancesServiceClient.truncateLogCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[SqlInstancesTruncateLogRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-sql/latest/com.google.cloud.sql.v1.SqlInstancesTruncateLogRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-sql/latest/com.google.cloud.sql.v1.Operation)>` |   
  
### update(SqlInstancesUpdateRequest request)
    
    
    public final Operation update(SqlInstancesUpdateRequest request)

Updates settings of a Cloud SQL instance. Using this operation might cause your instance to restart.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (SqlInstancesServiceClient sqlInstancesServiceClient = SqlInstancesServiceClient.create()) {
       SqlInstancesUpdateRequest request =
           SqlInstancesUpdateRequest.newBuilder()
               .setInstance("instance555127957")
               .setProject("project-309310695")
               .setBody(DatabaseInstance.newBuilder().build())
               .build();
       Operation response = sqlInstancesServiceClient.update(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[SqlInstancesUpdateRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-sql/latest/com.google.cloud.sql.v1.SqlInstancesUpdateRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-sql/latest/com.google.cloud.sql.v1.Operation)` |   
  
### updateCallable()
    
    
    public final UnaryCallable<SqlInstancesUpdateRequest,Operation> updateCallable()

Updates settings of a Cloud SQL instance. Using this operation might cause your instance to restart.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (SqlInstancesServiceClient sqlInstancesServiceClient = SqlInstancesServiceClient.create()) {
       SqlInstancesUpdateRequest request =
           SqlInstancesUpdateRequest.newBuilder()
               .setInstance("instance555127957")
               .setProject("project-309310695")
               .setBody(DatabaseInstance.newBuilder().build())
               .build();
       ApiFuture<Operation> future = sqlInstancesServiceClient.updateCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[SqlInstancesUpdateRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-sql/latest/com.google.cloud.sql.v1.SqlInstancesUpdateRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-sql/latest/com.google.cloud.sql.v1.Operation)>` |   
  
### verifyExternalSyncSettings(SqlInstancesVerifyExternalSyncSettingsRequest request)
    
    
    public final SqlInstancesVerifyExternalSyncSettingsResponse verifyExternalSyncSettings(SqlInstancesVerifyExternalSyncSettingsRequest request)

Verify External primary instance external sync settings.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (SqlInstancesServiceClient sqlInstancesServiceClient = SqlInstancesServiceClient.create()) {
       SqlInstancesVerifyExternalSyncSettingsRequest request =
           SqlInstancesVerifyExternalSyncSettingsRequest.newBuilder()
               .setInstance("instance555127957")
               .setProject("project-309310695")
               .setVerifyConnectionOnly(true)
               .setVerifyReplicationOnly(true)
               .setSyncParallelLevel(ExternalSyncParallelLevel.forNumber(0))
               .addAllSelectedObjects(new ArrayList<ExternalSyncSelectedObject>())
               .build();
       SqlInstancesVerifyExternalSyncSettingsResponse response =
           sqlInstancesServiceClient.verifyExternalSyncSettings(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[SqlInstancesVerifyExternalSyncSettingsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-sql/latest/com.google.cloud.sql.v1.SqlInstancesVerifyExternalSyncSettingsRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[SqlInstancesVerifyExternalSyncSettingsResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-sql/latest/com.google.cloud.sql.v1.SqlInstancesVerifyExternalSyncSettingsResponse)` |   
  
### verifyExternalSyncSettingsCallable()
    
    
    public final UnaryCallable<SqlInstancesVerifyExternalSyncSettingsRequest,SqlInstancesVerifyExternalSyncSettingsResponse> verifyExternalSyncSettingsCallable()

Verify External primary instance external sync settings.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (SqlInstancesServiceClient sqlInstancesServiceClient = SqlInstancesServiceClient.create()) {
       SqlInstancesVerifyExternalSyncSettingsRequest request =
           SqlInstancesVerifyExternalSyncSettingsRequest.newBuilder()
               .setInstance("instance555127957")
               .setProject("project-309310695")
               .setVerifyConnectionOnly(true)
               .setVerifyReplicationOnly(true)
               .setSyncParallelLevel(ExternalSyncParallelLevel.forNumber(0))
               .addAllSelectedObjects(new ArrayList<ExternalSyncSelectedObject>())
               .build();
       ApiFuture<SqlInstancesVerifyExternalSyncSettingsResponse> future =
           sqlInstancesServiceClient.verifyExternalSyncSettingsCallable().futureCall(request);
       // Do something.
       SqlInstancesVerifyExternalSyncSettingsResponse response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[SqlInstancesVerifyExternalSyncSettingsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-sql/latest/com.google.cloud.sql.v1.SqlInstancesVerifyExternalSyncSettingsRequest),[SqlInstancesVerifyExternalSyncSettingsResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-sql/latest/com.google.cloud.sql.v1.SqlInstancesVerifyExternalSyncSettingsResponse)>` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-06 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-06 UTC."],[],[]] 
