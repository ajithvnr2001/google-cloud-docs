---
url: https://docs.cloud.google.com/java/docs/reference/google-cloud-sql/latest/com.google.cloud.sql.v1.SqlInstancesServiceGrpc.SqlInstancesServiceFutureStub
title: Class SqlInstancesServiceGrpc.SqlInstancesServiceFutureStub (0.5.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T20:25:39.058818+00:00
---

# Class SqlInstancesServiceGrpc.SqlInstancesServiceFutureStub (0.5.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-cloud-sql/latest/com.google.cloud.sql.v1.SqlInstancesServiceGrpc.SqlInstancesServiceFutureStub

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Class SqlInstancesServiceGrpc.SqlInstancesServiceFutureStub (0.5.0) Stay organized with collections  Save and categorize content based on your preferences. 

0.5.0 (latest)  0.1.0 
    
    
    public static final class SqlInstancesServiceGrpc.SqlInstancesServiceFutureStub extends AbstractFutureStub<SqlInstancesServiceGrpc.SqlInstancesServiceFutureStub>

A stub to allow clients to do ListenableFuture-style rpc calls to service SqlInstancesService.

## Inheritance

[java.lang.Object](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html) > io.grpc.stub.AbstractStub > io.grpc.stub.AbstractFutureStub > SqlInstancesServiceGrpc.SqlInstancesServiceFutureStub

## Inherited Members

io.grpc.stub.AbstractFutureStub.<T>newStub(io.grpc.stub.AbstractStub.StubFactory<T>,io.grpc.Channel)

io.grpc.stub.AbstractFutureStub.<T>newStub(io.grpc.stub.AbstractStub.StubFactory<T>,io.grpc.Channel,io.grpc.CallOptions)

io.grpc.stub.AbstractStub.<T>withOption(io.grpc.CallOptions.Key<T>,T)

io.grpc.stub.AbstractStub.build(io.grpc.Channel,io.grpc.CallOptions)

io.grpc.stub.AbstractStub.getCallOptions()

io.grpc.stub.AbstractStub.getChannel()

io.grpc.stub.AbstractStub.withCallCredentials(io.grpc.CallCredentials)

io.grpc.stub.AbstractStub.withChannel(io.grpc.Channel)

io.grpc.stub.AbstractStub.withCompression(java.lang.String)

io.grpc.stub.AbstractStub.withDeadline(io.grpc.Deadline)

io.grpc.stub.AbstractStub.withDeadlineAfter(java.time.Duration)

io.grpc.stub.AbstractStub.withDeadlineAfter(long,java.util.concurrent.TimeUnit)

io.grpc.stub.AbstractStub.withExecutor(java.util.concurrent.Executor)

io.grpc.stub.AbstractStub.withInterceptors(io.grpc.ClientInterceptor...)

io.grpc.stub.AbstractStub.withMaxInboundMessageSize(int)

io.grpc.stub.AbstractStub.withMaxOutboundMessageSize(int)

io.grpc.stub.AbstractStub.withOnReadyThreshold(int)

io.grpc.stub.AbstractStub.withWaitForReady()

[Object.clone()](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html#clone--)

[Object.equals(Object)](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html#equals-java.lang.Object-)

[Object.finalize()](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html#finalize--)

[Object.getClass()](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html#getClass--)

[Object.hashCode()](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html#hashCode--)

[Object.notify()](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html#notify--)

[Object.notifyAll()](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html#notifyAll--)

[Object.toString()](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html#toString--)

[Object.wait()](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html#wait--)

[Object.wait(long)](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html#wait-long-)

[Object.wait(long,int)](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html#wait-long-int-)

## Methods 

### acquireSsrsLease(SqlInstancesAcquireSsrsLeaseRequest request)
    
    
    public ListenableFuture<SqlInstancesAcquireSsrsLeaseResponse> acquireSsrsLease(SqlInstancesAcquireSsrsLeaseRequest request)

Acquire a lease for the setup of SQL Server Reporting Services (SSRS).

**Parameter**  
---  
**Name** | **Description**  
`request` | `[SqlInstancesAcquireSsrsLeaseRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-sql/latest/com.google.cloud.sql.v1.SqlInstancesAcquireSsrsLeaseRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`com.google.common.util.concurrent.ListenableFuture<[SqlInstancesAcquireSsrsLeaseResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-sql/latest/com.google.cloud.sql.v1.SqlInstancesAcquireSsrsLeaseResponse)>` |   
  
### addEntraIdCertificate(SqlInstancesAddEntraIdCertificateRequest request)
    
    
    public ListenableFuture<Operation> addEntraIdCertificate(SqlInstancesAddEntraIdCertificateRequest request)

Adds a new Entra ID certificate for the specified instance. If an Entra ID certificate was previously added but never used in a certificate rotation, this operation replaces that version.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[SqlInstancesAddEntraIdCertificateRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-sql/latest/com.google.cloud.sql.v1.SqlInstancesAddEntraIdCertificateRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`com.google.common.util.concurrent.ListenableFuture<[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-sql/latest/com.google.cloud.sql.v1.Operation)>` |   
  
### addServerCa(SqlInstancesAddServerCaRequest request)
    
    
    public ListenableFuture<Operation> addServerCa(SqlInstancesAddServerCaRequest request)

Adds a new trusted Certificate Authority (CA) version for the specified instance. Required to prepare for a certificate rotation. If a CA version was previously added but never used in a certificate rotation, this operation replaces that version. There cannot be more than one CA version waiting to be rotated in. For instances that have enabled Certificate Authority Service (CAS) based server CA, use AddServerCertificate to add a new server certificate.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[SqlInstancesAddServerCaRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-sql/latest/com.google.cloud.sql.v1.SqlInstancesAddServerCaRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`com.google.common.util.concurrent.ListenableFuture<[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-sql/latest/com.google.cloud.sql.v1.Operation)>` |   
  
### addServerCertificate(SqlInstancesAddServerCertificateRequest request)
    
    
    public ListenableFuture<Operation> addServerCertificate(SqlInstancesAddServerCertificateRequest request)

Add a new trusted server certificate version for the specified instance using Certificate Authority Service (CAS) server CA. Required to prepare for a certificate rotation. If a server certificate version was previously added but never used in a certificate rotation, this operation replaces that version. There cannot be more than one certificate version waiting to be rotated in. For instances not using CAS server CA, use AddServerCa instead.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[SqlInstancesAddServerCertificateRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-sql/latest/com.google.cloud.sql.v1.SqlInstancesAddServerCertificateRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`com.google.common.util.concurrent.ListenableFuture<[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-sql/latest/com.google.cloud.sql.v1.Operation)>` |   
  
### build(Channel channel, CallOptions callOptions)
    
    
    protected SqlInstancesServiceGrpc.SqlInstancesServiceFutureStub build(Channel channel, CallOptions callOptions)

**Parameters**  
---  
**Name** | **Description**  
`channel` | `io.grpc.Channel`  
  
`callOptions` | `io.grpc.CallOptions`  
  
**Returns**  
---  
**Type** | **Description**  
`[SqlInstancesServiceGrpc.SqlInstancesServiceFutureStub](https://docs.cloud.google.com/java/docs/reference/google-cloud-sql/latest/com.google.cloud.sql.v1.SqlInstancesServiceGrpc.SqlInstancesServiceFutureStub)` |   
**Overrides**

io.grpc.stub.AbstractStub.build(io.grpc.Channel,io.grpc.CallOptions)

### clone(SqlInstancesCloneRequest request)
    
    
    public ListenableFuture<Operation> clone(SqlInstancesCloneRequest request)

Creates a Cloud SQL instance as a clone of the source instance. Using this operation might cause your instance to restart.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[SqlInstancesCloneRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-sql/latest/com.google.cloud.sql.v1.SqlInstancesCloneRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`com.google.common.util.concurrent.ListenableFuture<[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-sql/latest/com.google.cloud.sql.v1.Operation)>` |   
  
### createEphemeral(SqlInstancesCreateEphemeralCertRequest request)
    
    
    public ListenableFuture<SslCert> createEphemeral(SqlInstancesCreateEphemeralCertRequest request)

Generates a short-lived X509 certificate containing the provided public key and signed by a private key specific to the target instance. Users may use the certificate to authenticate as themselves when connecting to the database.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[SqlInstancesCreateEphemeralCertRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-sql/latest/com.google.cloud.sql.v1.SqlInstancesCreateEphemeralCertRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`com.google.common.util.concurrent.ListenableFuture<[SslCert](https://docs.cloud.google.com/java/docs/reference/google-cloud-sql/latest/com.google.cloud.sql.v1.SslCert)>` |   
  
### delete(SqlInstancesDeleteRequest request)
    
    
    public ListenableFuture<Operation> delete(SqlInstancesDeleteRequest request)

Deletes a Cloud SQL instance.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[SqlInstancesDeleteRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-sql/latest/com.google.cloud.sql.v1.SqlInstancesDeleteRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`com.google.common.util.concurrent.ListenableFuture<[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-sql/latest/com.google.cloud.sql.v1.Operation)>` |   
  
### demote(SqlInstancesDemoteRequest request)
    
    
    public ListenableFuture<Operation> demote(SqlInstancesDemoteRequest request)

Demotes an existing standalone instance to be a Cloud SQL read replica for an external database server.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[SqlInstancesDemoteRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-sql/latest/com.google.cloud.sql.v1.SqlInstancesDemoteRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`com.google.common.util.concurrent.ListenableFuture<[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-sql/latest/com.google.cloud.sql.v1.Operation)>` |   
  
### demoteMaster(SqlInstancesDemoteMasterRequest request)
    
    
    public ListenableFuture<Operation> demoteMaster(SqlInstancesDemoteMasterRequest request)

Demotes the stand-alone instance to be a Cloud SQL read replica for an external database server.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[SqlInstancesDemoteMasterRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-sql/latest/com.google.cloud.sql.v1.SqlInstancesDemoteMasterRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`com.google.common.util.concurrent.ListenableFuture<[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-sql/latest/com.google.cloud.sql.v1.Operation)>` |   
  
### executeSql(SqlInstancesExecuteSqlRequest request)
    
    
    public ListenableFuture<SqlInstancesExecuteSqlResponse> executeSql(SqlInstancesExecuteSqlRequest request)

Execute SQL statements.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[SqlInstancesExecuteSqlRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-sql/latest/com.google.cloud.sql.v1.SqlInstancesExecuteSqlRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`com.google.common.util.concurrent.ListenableFuture<[SqlInstancesExecuteSqlResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-sql/latest/com.google.cloud.sql.v1.SqlInstancesExecuteSqlResponse)>` |   
  
### export(SqlInstancesExportRequest request)
    
    
    public ListenableFuture<Operation> export(SqlInstancesExportRequest request)

Exports data from a Cloud SQL instance to a Cloud Storage bucket as a SQL dump or CSV file.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[SqlInstancesExportRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-sql/latest/com.google.cloud.sql.v1.SqlInstancesExportRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`com.google.common.util.concurrent.ListenableFuture<[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-sql/latest/com.google.cloud.sql.v1.Operation)>` |   
  
### failover(SqlInstancesFailoverRequest request)
    
    
    public ListenableFuture<Operation> failover(SqlInstancesFailoverRequest request)

Initiates a manual failover of a high availability (HA) primary instance to a standby instance, which becomes the primary instance. Users are then rerouted to the new primary. For more information, see the [Overview of high availability](https://cloud.google.com/sql/docs/mysql/high-availability) page in the Cloud SQL documentation. If using Legacy HA (MySQL only), this causes the instance to failover to its failover replica instance.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[SqlInstancesFailoverRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-sql/latest/com.google.cloud.sql.v1.SqlInstancesFailoverRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`com.google.common.util.concurrent.ListenableFuture<[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-sql/latest/com.google.cloud.sql.v1.Operation)>` |   
  
### get(SqlInstancesGetRequest request)
    
    
    public ListenableFuture<DatabaseInstance> get(SqlInstancesGetRequest request)

Retrieves a resource containing information about a Cloud SQL instance.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[SqlInstancesGetRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-sql/latest/com.google.cloud.sql.v1.SqlInstancesGetRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`com.google.common.util.concurrent.ListenableFuture<[DatabaseInstance](https://docs.cloud.google.com/java/docs/reference/google-cloud-sql/latest/com.google.cloud.sql.v1.DatabaseInstance)>` |   
  
### getDiskShrinkConfig(SqlInstancesGetDiskShrinkConfigRequest request)
    
    
    public ListenableFuture<SqlInstancesGetDiskShrinkConfigResponse> getDiskShrinkConfig(SqlInstancesGetDiskShrinkConfigRequest request)

Get Disk Shrink Config for a given instance.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[SqlInstancesGetDiskShrinkConfigRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-sql/latest/com.google.cloud.sql.v1.SqlInstancesGetDiskShrinkConfigRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`com.google.common.util.concurrent.ListenableFuture<[SqlInstancesGetDiskShrinkConfigResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-sql/latest/com.google.cloud.sql.v1.SqlInstancesGetDiskShrinkConfigResponse)>` |   
  
### getLatestRecoveryTime(SqlInstancesGetLatestRecoveryTimeRequest request)
    
    
    public ListenableFuture<SqlInstancesGetLatestRecoveryTimeResponse> getLatestRecoveryTime(SqlInstancesGetLatestRecoveryTimeRequest request)

Get Latest Recovery Time for a given instance.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[SqlInstancesGetLatestRecoveryTimeRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-sql/latest/com.google.cloud.sql.v1.SqlInstancesGetLatestRecoveryTimeRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`com.google.common.util.concurrent.ListenableFuture<[SqlInstancesGetLatestRecoveryTimeResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-sql/latest/com.google.cloud.sql.v1.SqlInstancesGetLatestRecoveryTimeResponse)>` |   
  
### import_(SqlInstancesImportRequest request)
    
    
    public ListenableFuture<Operation> import_(SqlInstancesImportRequest request)

Imports data into a Cloud SQL instance from a SQL dump or CSV file in Cloud Storage.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[SqlInstancesImportRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-sql/latest/com.google.cloud.sql.v1.SqlInstancesImportRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`com.google.common.util.concurrent.ListenableFuture<[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-sql/latest/com.google.cloud.sql.v1.Operation)>` |   
  
### insert(SqlInstancesInsertRequest request)
    
    
    public ListenableFuture<Operation> insert(SqlInstancesInsertRequest request)

Creates a new Cloud SQL instance.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[SqlInstancesInsertRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-sql/latest/com.google.cloud.sql.v1.SqlInstancesInsertRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`com.google.common.util.concurrent.ListenableFuture<[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-sql/latest/com.google.cloud.sql.v1.Operation)>` |   
  
### list(SqlInstancesListRequest request)
    
    
    public ListenableFuture<InstancesListResponse> list(SqlInstancesListRequest request)

Lists instances under a given project.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[SqlInstancesListRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-sql/latest/com.google.cloud.sql.v1.SqlInstancesListRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`com.google.common.util.concurrent.ListenableFuture<[InstancesListResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-sql/latest/com.google.cloud.sql.v1.InstancesListResponse)>` |   
  
### listEntraIdCertificates(SqlInstancesListEntraIdCertificatesRequest request)
    
    
    public ListenableFuture<InstancesListEntraIdCertificatesResponse> listEntraIdCertificates(SqlInstancesListEntraIdCertificatesRequest request)

Lists all versions of EntraID certificates for the specified instance. There can be up to three sets of certificates listed: the certificate that is currently in use, a future that has been added but not yet used to sign a certificate, and a certificate that has been rotated out.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[SqlInstancesListEntraIdCertificatesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-sql/latest/com.google.cloud.sql.v1.SqlInstancesListEntraIdCertificatesRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`com.google.common.util.concurrent.ListenableFuture<[InstancesListEntraIdCertificatesResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-sql/latest/com.google.cloud.sql.v1.InstancesListEntraIdCertificatesResponse)>` |   
  
### listServerCas(SqlInstancesListServerCasRequest request)
    
    
    public ListenableFuture<InstancesListServerCasResponse> listServerCas(SqlInstancesListServerCasRequest request)

Lists all of the trusted Certificate Authorities (CAs) for the specified instance. There can be up to three CAs listed: the CA that was used to sign the certificate that is currently in use, a CA that has been added but not yet used to sign a certificate, and a CA used to sign a certificate that has previously rotated out.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[SqlInstancesListServerCasRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-sql/latest/com.google.cloud.sql.v1.SqlInstancesListServerCasRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`com.google.common.util.concurrent.ListenableFuture<[InstancesListServerCasResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-sql/latest/com.google.cloud.sql.v1.InstancesListServerCasResponse)>` |   
  
### listServerCertificates(SqlInstancesListServerCertificatesRequest request)
    
    
    public ListenableFuture<InstancesListServerCertificatesResponse> listServerCertificates(SqlInstancesListServerCertificatesRequest request)

Lists all versions of server certificates and certificate authorities (CAs) for the specified instance. There can be up to three sets of certs listed: the certificate that is currently in use, a future that has been added but not yet used to sign a certificate, and a certificate that has been rotated out. For instances not using Certificate Authority Service (CAS) server CA, use ListServerCas instead.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[SqlInstancesListServerCertificatesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-sql/latest/com.google.cloud.sql.v1.SqlInstancesListServerCertificatesRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`com.google.common.util.concurrent.ListenableFuture<[InstancesListServerCertificatesResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-sql/latest/com.google.cloud.sql.v1.InstancesListServerCertificatesResponse)>` |   
  
### patch(SqlInstancesPatchRequest request)
    
    
    public ListenableFuture<Operation> patch(SqlInstancesPatchRequest request)

Partially updates settings of a Cloud SQL instance by merging the request with the current configuration. This method supports patch semantics.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[SqlInstancesPatchRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-sql/latest/com.google.cloud.sql.v1.SqlInstancesPatchRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`com.google.common.util.concurrent.ListenableFuture<[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-sql/latest/com.google.cloud.sql.v1.Operation)>` |   
  
### performDiskShrink(SqlInstancesPerformDiskShrinkRequest request)
    
    
    public ListenableFuture<Operation> performDiskShrink(SqlInstancesPerformDiskShrinkRequest request)

Perform Disk Shrink on primary instance.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[SqlInstancesPerformDiskShrinkRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-sql/latest/com.google.cloud.sql.v1.SqlInstancesPerformDiskShrinkRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`com.google.common.util.concurrent.ListenableFuture<[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-sql/latest/com.google.cloud.sql.v1.Operation)>` |   
  
### pointInTimeRestore(SqlInstancesPointInTimeRestoreRequest request)
    
    
    public ListenableFuture<Operation> pointInTimeRestore(SqlInstancesPointInTimeRestoreRequest request)

Point in time restore for an instance managed by Google Cloud Backup and Disaster Recovery.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[SqlInstancesPointInTimeRestoreRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-sql/latest/com.google.cloud.sql.v1.SqlInstancesPointInTimeRestoreRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`com.google.common.util.concurrent.ListenableFuture<[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-sql/latest/com.google.cloud.sql.v1.Operation)>` |   
  
### preCheckMajorVersionUpgrade(SqlInstancesPreCheckMajorVersionUpgradeRequest request)
    
    
    public ListenableFuture<Operation> preCheckMajorVersionUpgrade(SqlInstancesPreCheckMajorVersionUpgradeRequest request)

Execute MVU Pre-checks

**Parameter**  
---  
**Name** | **Description**  
`request` | `[SqlInstancesPreCheckMajorVersionUpgradeRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-sql/latest/com.google.cloud.sql.v1.SqlInstancesPreCheckMajorVersionUpgradeRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`com.google.common.util.concurrent.ListenableFuture<[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-sql/latest/com.google.cloud.sql.v1.Operation)>` |   
  
### promoteReplica(SqlInstancesPromoteReplicaRequest request)
    
    
    public ListenableFuture<Operation> promoteReplica(SqlInstancesPromoteReplicaRequest request)

Promotes the read replica instance to be an independent Cloud SQL primary instance. Using this operation might cause your instance to restart.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[SqlInstancesPromoteReplicaRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-sql/latest/com.google.cloud.sql.v1.SqlInstancesPromoteReplicaRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`com.google.common.util.concurrent.ListenableFuture<[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-sql/latest/com.google.cloud.sql.v1.Operation)>` |   
  
### reencrypt(SqlInstancesReencryptRequest request)
    
    
    public ListenableFuture<Operation> reencrypt(SqlInstancesReencryptRequest request)

Reencrypt CMEK instance with latest key version.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[SqlInstancesReencryptRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-sql/latest/com.google.cloud.sql.v1.SqlInstancesReencryptRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`com.google.common.util.concurrent.ListenableFuture<[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-sql/latest/com.google.cloud.sql.v1.Operation)>` |   
  
### releaseSsrsLease(SqlInstancesReleaseSsrsLeaseRequest request)
    
    
    public ListenableFuture<SqlInstancesReleaseSsrsLeaseResponse> releaseSsrsLease(SqlInstancesReleaseSsrsLeaseRequest request)

Release a lease for the setup of SQL Server Reporting Services (SSRS).

**Parameter**  
---  
**Name** | **Description**  
`request` | `[SqlInstancesReleaseSsrsLeaseRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-sql/latest/com.google.cloud.sql.v1.SqlInstancesReleaseSsrsLeaseRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`com.google.common.util.concurrent.ListenableFuture<[SqlInstancesReleaseSsrsLeaseResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-sql/latest/com.google.cloud.sql.v1.SqlInstancesReleaseSsrsLeaseResponse)>` |   
  
### rescheduleMaintenance(SqlInstancesRescheduleMaintenanceRequest request)
    
    
    public ListenableFuture<Operation> rescheduleMaintenance(SqlInstancesRescheduleMaintenanceRequest request)

Reschedules the maintenance on the given instance.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[SqlInstancesRescheduleMaintenanceRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-sql/latest/com.google.cloud.sql.v1.SqlInstancesRescheduleMaintenanceRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`com.google.common.util.concurrent.ListenableFuture<[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-sql/latest/com.google.cloud.sql.v1.Operation)>` |   
  
### resetReplicaSize(SqlInstancesResetReplicaSizeRequest request)
    
    
    public ListenableFuture<Operation> resetReplicaSize(SqlInstancesResetReplicaSizeRequest request)

Reset Replica Size to primary instance disk size.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[SqlInstancesResetReplicaSizeRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-sql/latest/com.google.cloud.sql.v1.SqlInstancesResetReplicaSizeRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`com.google.common.util.concurrent.ListenableFuture<[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-sql/latest/com.google.cloud.sql.v1.Operation)>` |   
  
### resetSslConfig(SqlInstancesResetSslConfigRequest request)
    
    
    public ListenableFuture<Operation> resetSslConfig(SqlInstancesResetSslConfigRequest request)

Deletes all client certificates and generates a new server SSL certificate for the instance.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[SqlInstancesResetSslConfigRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-sql/latest/com.google.cloud.sql.v1.SqlInstancesResetSslConfigRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`com.google.common.util.concurrent.ListenableFuture<[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-sql/latest/com.google.cloud.sql.v1.Operation)>` |   
  
### restart(SqlInstancesRestartRequest request)
    
    
    public ListenableFuture<Operation> restart(SqlInstancesRestartRequest request)

Restarts a Cloud SQL instance.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[SqlInstancesRestartRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-sql/latest/com.google.cloud.sql.v1.SqlInstancesRestartRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`com.google.common.util.concurrent.ListenableFuture<[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-sql/latest/com.google.cloud.sql.v1.Operation)>` |   
  
### restoreBackup(SqlInstancesRestoreBackupRequest request)
    
    
    public ListenableFuture<Operation> restoreBackup(SqlInstancesRestoreBackupRequest request)

Restores a backup of a Cloud SQL instance. Using this operation might cause your instance to restart.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[SqlInstancesRestoreBackupRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-sql/latest/com.google.cloud.sql.v1.SqlInstancesRestoreBackupRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`com.google.common.util.concurrent.ListenableFuture<[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-sql/latest/com.google.cloud.sql.v1.Operation)>` |   
  
### rotateEntraIdCertificate(SqlInstancesRotateEntraIdCertificateRequest request)
    
    
    public ListenableFuture<Operation> rotateEntraIdCertificate(SqlInstancesRotateEntraIdCertificateRequest request)

Rotates the server certificate version to one previously added with the addEntraIdCertificate method.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[SqlInstancesRotateEntraIdCertificateRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-sql/latest/com.google.cloud.sql.v1.SqlInstancesRotateEntraIdCertificateRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`com.google.common.util.concurrent.ListenableFuture<[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-sql/latest/com.google.cloud.sql.v1.Operation)>` |   
  
### rotateServerCa(SqlInstancesRotateServerCaRequest request)
    
    
    public ListenableFuture<Operation> rotateServerCa(SqlInstancesRotateServerCaRequest request)

Rotates the server certificate to one signed by the Certificate Authority (CA) version previously added with the addServerCA method. For instances that have enabled Certificate Authority Service (CAS) based server CA, use RotateServerCertificate to rotate the server certificate.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[SqlInstancesRotateServerCaRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-sql/latest/com.google.cloud.sql.v1.SqlInstancesRotateServerCaRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`com.google.common.util.concurrent.ListenableFuture<[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-sql/latest/com.google.cloud.sql.v1.Operation)>` |   
  
### rotateServerCertificate(SqlInstancesRotateServerCertificateRequest request)
    
    
    public ListenableFuture<Operation> rotateServerCertificate(SqlInstancesRotateServerCertificateRequest request)

Rotates the server certificate version to one previously added with the addServerCertificate method. For instances not using Certificate Authority Service (CAS) server CA, use RotateServerCa instead.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[SqlInstancesRotateServerCertificateRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-sql/latest/com.google.cloud.sql.v1.SqlInstancesRotateServerCertificateRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`com.google.common.util.concurrent.ListenableFuture<[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-sql/latest/com.google.cloud.sql.v1.Operation)>` |   
  
### startExternalSync(SqlInstancesStartExternalSyncRequest request)
    
    
    public ListenableFuture<Operation> startExternalSync(SqlInstancesStartExternalSyncRequest request)

Start External primary instance migration.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[SqlInstancesStartExternalSyncRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-sql/latest/com.google.cloud.sql.v1.SqlInstancesStartExternalSyncRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`com.google.common.util.concurrent.ListenableFuture<[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-sql/latest/com.google.cloud.sql.v1.Operation)>` |   
  
### startReplica(SqlInstancesStartReplicaRequest request)
    
    
    public ListenableFuture<Operation> startReplica(SqlInstancesStartReplicaRequest request)

Starts the replication in the read replica instance.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[SqlInstancesStartReplicaRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-sql/latest/com.google.cloud.sql.v1.SqlInstancesStartReplicaRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`com.google.common.util.concurrent.ListenableFuture<[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-sql/latest/com.google.cloud.sql.v1.Operation)>` |   
  
### stopReplica(SqlInstancesStopReplicaRequest request)
    
    
    public ListenableFuture<Operation> stopReplica(SqlInstancesStopReplicaRequest request)

Stops the replication in the read replica instance.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[SqlInstancesStopReplicaRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-sql/latest/com.google.cloud.sql.v1.SqlInstancesStopReplicaRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`com.google.common.util.concurrent.ListenableFuture<[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-sql/latest/com.google.cloud.sql.v1.Operation)>` |   
  
### switchover(SqlInstancesSwitchoverRequest request)
    
    
    public ListenableFuture<Operation> switchover(SqlInstancesSwitchoverRequest request)

Switches over from the primary instance to the DR replica instance.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[SqlInstancesSwitchoverRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-sql/latest/com.google.cloud.sql.v1.SqlInstancesSwitchoverRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`com.google.common.util.concurrent.ListenableFuture<[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-sql/latest/com.google.cloud.sql.v1.Operation)>` |   
  
### truncateLog(SqlInstancesTruncateLogRequest request)
    
    
    public ListenableFuture<Operation> truncateLog(SqlInstancesTruncateLogRequest request)

Truncate MySQL general and slow query log tables MySQL only.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[SqlInstancesTruncateLogRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-sql/latest/com.google.cloud.sql.v1.SqlInstancesTruncateLogRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`com.google.common.util.concurrent.ListenableFuture<[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-sql/latest/com.google.cloud.sql.v1.Operation)>` |   
  
### update(SqlInstancesUpdateRequest request)
    
    
    public ListenableFuture<Operation> update(SqlInstancesUpdateRequest request)

Updates settings of a Cloud SQL instance. Using this operation might cause your instance to restart.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[SqlInstancesUpdateRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-sql/latest/com.google.cloud.sql.v1.SqlInstancesUpdateRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`com.google.common.util.concurrent.ListenableFuture<[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-sql/latest/com.google.cloud.sql.v1.Operation)>` |   
  
### verifyExternalSyncSettings(SqlInstancesVerifyExternalSyncSettingsRequest request)
    
    
    public ListenableFuture<SqlInstancesVerifyExternalSyncSettingsResponse> verifyExternalSyncSettings(SqlInstancesVerifyExternalSyncSettingsRequest request)

Verify External primary instance external sync settings.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[SqlInstancesVerifyExternalSyncSettingsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-sql/latest/com.google.cloud.sql.v1.SqlInstancesVerifyExternalSyncSettingsRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`com.google.common.util.concurrent.ListenableFuture<[SqlInstancesVerifyExternalSyncSettingsResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-sql/latest/com.google.cloud.sql.v1.SqlInstancesVerifyExternalSyncSettingsResponse)>` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-06 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-06 UTC."],[],[]] 
