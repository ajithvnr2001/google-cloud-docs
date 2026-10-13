---
url: https://docs.cloud.google.com/java/docs/reference/google-cloud-redis-cluster/latest/com.google.cloud.redis.cluster.v1beta1.CloudRedisClusterGrpc.CloudRedisClusterBlockingStub
title: Class CloudRedisClusterGrpc.CloudRedisClusterBlockingStub (0.71.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T16:52:40.439367+00:00
---

# Class CloudRedisClusterGrpc.CloudRedisClusterBlockingStub (0.71.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-cloud-redis-cluster/latest/com.google.cloud.redis.cluster.v1beta1.CloudRedisClusterGrpc.CloudRedisClusterBlockingStub

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Class CloudRedisClusterGrpc.CloudRedisClusterBlockingStub (0.71.0) Stay organized with collections  Save and categorize content based on your preferences. 

0.71.0 (latest)  0.67.0  0.66.0  0.65.0  0.63.0  0.60.0  0.59.0  0.57.0  0.55.0  0.54.0  0.52.0  0.50.0  0.48.0  0.47.0  0.46.0  0.45.0  0.44.0  0.42.0  0.40.0  0.39.0  0.36.0  0.35.0  0.34.0  0.32.0  0.31.0  0.30.0  0.29.0  0.28.0  0.27.0  0.26.0  0.25.0  0.24.0  0.23.0  0.21.0  0.20.0  0.19.0  0.18.0  0.17.0  0.16.0  0.15.0  0.14.0  0.13.0  0.12.0  0.11.0  0.9.0  0.8.0  0.7.0  0.6.0  0.5.0  0.4.0  0.3.0  0.2.0  0.1.0 
    
    
    public static final class CloudRedisClusterGrpc.CloudRedisClusterBlockingStub extends AbstractBlockingStub<CloudRedisClusterGrpc.CloudRedisClusterBlockingStub>

A stub to allow clients to do limited synchronous rpc calls to service CloudRedisCluster.

Configures and manages Cloud Memorystore for Redis clusters Google Cloud Memorystore for Redis Cluster The `redis.googleapis.com` service implements the Google Cloud Memorystore for Redis API and defines the following resource model for managing Redis clusters:

  * The service works with a collection of cloud projects, named: `/projects/*`
  * Each project has a collection of available locations, named: `/locations/*`
  * Each location has a collection of Redis clusters, named: `/clusters/*`
  * As such, Redis clusters are resources of the form: `/projects/{project_id}/locations/{location_id}/clusters/{instance_id}` Note that location_id must be a GCP `region`; for example:
  * `projects/redpepper-1290/locations/us-central1/clusters/my-redis`



## Inheritance

[java.lang.Object](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html) > io.grpc.stub.AbstractStub > io.grpc.stub.AbstractBlockingStub > CloudRedisClusterGrpc.CloudRedisClusterBlockingStub

## Inherited Members

io.grpc.stub.AbstractBlockingStub.<T>newStub(io.grpc.stub.AbstractStub.StubFactory<T>,io.grpc.Channel)

io.grpc.stub.AbstractBlockingStub.<T>newStub(io.grpc.stub.AbstractStub.StubFactory<T>,io.grpc.Channel,io.grpc.CallOptions)

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

### backupCluster(BackupClusterRequest request)
    
    
    public Operation backupCluster(BackupClusterRequest request)

Backup Redis Cluster. If this is the first time a backup is being created, a backup collection will be created at the backend, and this backup belongs to this collection. Both collection and backup will have a resource name. Backup will be executed for each shard. A replica (primary if nonHA) will be selected to perform the execution. Backup call will be rejected if there is an ongoing backup or update operation. Be aware that during preview, if the cluster's internal software version is too old, critical update will be performed before actual backup. Once the internal software version is updated to the minimum version required by the backup feature, subsequent backups will not require critical update. After preview, there will be no critical update needed for backup.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[BackupClusterRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-redis-cluster/latest/com.google.cloud.redis.cluster.v1beta1.BackupClusterRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)` |   
  
### build(Channel channel, CallOptions callOptions)
    
    
    protected CloudRedisClusterGrpc.CloudRedisClusterBlockingStub build(Channel channel, CallOptions callOptions)

**Parameters**  
---  
**Name** | **Description**  
`channel` | `io.grpc.Channel`  
  
`callOptions` | `io.grpc.CallOptions`  
  
**Returns**  
---  
**Type** | **Description**  
`[CloudRedisClusterGrpc.CloudRedisClusterBlockingStub](https://docs.cloud.google.com/java/docs/reference/google-cloud-redis-cluster/latest/com.google.cloud.redis.cluster.v1beta1.CloudRedisClusterGrpc.CloudRedisClusterBlockingStub)` |   
**Overrides**

io.grpc.stub.AbstractStub.build(io.grpc.Channel,io.grpc.CallOptions)

### createCluster(CreateClusterRequest request)
    
    
    public Operation createCluster(CreateClusterRequest request)

Creates a Redis cluster based on the specified properties. The creation is executed asynchronously and callers may check the returned operation to track its progress. Once the operation is completed the Redis cluster will be fully functional. The completed longrunning.Operation will contain the new cluster object in the response field. The returned operation is automatically deleted after a few hours, so there is no need to call DeleteOperation.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[CreateClusterRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-redis-cluster/latest/com.google.cloud.redis.cluster.v1beta1.CreateClusterRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)` |   
  
### deleteBackup(DeleteBackupRequest request)
    
    
    public Operation deleteBackup(DeleteBackupRequest request)

Deletes a specific backup.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[DeleteBackupRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-redis-cluster/latest/com.google.cloud.redis.cluster.v1beta1.DeleteBackupRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)` |   
  
### deleteCluster(DeleteClusterRequest request)
    
    
    public Operation deleteCluster(DeleteClusterRequest request)

Deletes a specific Redis cluster. Cluster stops serving and data is deleted.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[DeleteClusterRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-redis-cluster/latest/com.google.cloud.redis.cluster.v1beta1.DeleteClusterRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)` |   
  
### exportBackup(ExportBackupRequest request)
    
    
    public Operation exportBackup(ExportBackupRequest request)

Exports a specific backup to a customer target Cloud Storage URI.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[ExportBackupRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-redis-cluster/latest/com.google.cloud.redis.cluster.v1beta1.ExportBackupRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)` |   
  
### getBackup(GetBackupRequest request)
    
    
    public Backup getBackup(GetBackupRequest request)

Gets the details of a specific backup.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[GetBackupRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-redis-cluster/latest/com.google.cloud.redis.cluster.v1beta1.GetBackupRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Backup](https://docs.cloud.google.com/java/docs/reference/google-cloud-redis-cluster/latest/com.google.cloud.redis.cluster.v1beta1.Backup)` |   
  
### getBackupCollection(GetBackupCollectionRequest request)
    
    
    public BackupCollection getBackupCollection(GetBackupCollectionRequest request)

Get a backup collection.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[GetBackupCollectionRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-redis-cluster/latest/com.google.cloud.redis.cluster.v1beta1.GetBackupCollectionRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`[BackupCollection](https://docs.cloud.google.com/java/docs/reference/google-cloud-redis-cluster/latest/com.google.cloud.redis.cluster.v1beta1.BackupCollection)` |   
  
### getCluster(GetClusterRequest request)
    
    
    public Cluster getCluster(GetClusterRequest request)

Gets the details of a specific Redis cluster.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[GetClusterRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-redis-cluster/latest/com.google.cloud.redis.cluster.v1beta1.GetClusterRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Cluster](https://docs.cloud.google.com/java/docs/reference/google-cloud-redis-cluster/latest/com.google.cloud.redis.cluster.v1beta1.Cluster)` |   
  
### getClusterCertificateAuthority(GetClusterCertificateAuthorityRequest request)
    
    
    public CertificateAuthority getClusterCertificateAuthority(GetClusterCertificateAuthorityRequest request)

Gets the details of certificate authority information for Redis cluster.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[GetClusterCertificateAuthorityRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-redis-cluster/latest/com.google.cloud.redis.cluster.v1beta1.GetClusterCertificateAuthorityRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`[CertificateAuthority](https://docs.cloud.google.com/java/docs/reference/google-cloud-redis-cluster/latest/com.google.cloud.redis.cluster.v1beta1.CertificateAuthority)` |   
  
### getSharedRegionalCertificateAuthority(GetSharedRegionalCertificateAuthorityRequest request)
    
    
    public SharedRegionalCertificateAuthority getSharedRegionalCertificateAuthority(GetSharedRegionalCertificateAuthorityRequest request)

Gets the details of regional certificate authority information for Redis cluster.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[GetSharedRegionalCertificateAuthorityRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-redis-cluster/latest/com.google.cloud.redis.cluster.v1beta1.GetSharedRegionalCertificateAuthorityRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`[SharedRegionalCertificateAuthority](https://docs.cloud.google.com/java/docs/reference/google-cloud-redis-cluster/latest/com.google.cloud.redis.cluster.v1beta1.SharedRegionalCertificateAuthority)` |   
  
### listBackupCollections(ListBackupCollectionsRequest request)
    
    
    public ListBackupCollectionsResponse listBackupCollections(ListBackupCollectionsRequest request)

Lists all backup collections owned by a consumer project in either the specified location (region) or all locations. If `location_id` is specified as `-` (wildcard), then all regions available to the project are queried, and the results are aggregated.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[ListBackupCollectionsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-redis-cluster/latest/com.google.cloud.redis.cluster.v1beta1.ListBackupCollectionsRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`[ListBackupCollectionsResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-redis-cluster/latest/com.google.cloud.redis.cluster.v1beta1.ListBackupCollectionsResponse)` |   
  
### listBackups(ListBackupsRequest request)
    
    
    public ListBackupsResponse listBackups(ListBackupsRequest request)

Lists all backups owned by a backup collection.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[ListBackupsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-redis-cluster/latest/com.google.cloud.redis.cluster.v1beta1.ListBackupsRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`[ListBackupsResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-redis-cluster/latest/com.google.cloud.redis.cluster.v1beta1.ListBackupsResponse)` |   
  
### listClusters(ListClustersRequest request)
    
    
    public ListClustersResponse listClusters(ListClustersRequest request)

Lists all Redis clusters owned by a project in either the specified location (region) or all locations. The location should have the following format:

  * `projects/{project_id}/locations/{location_id}` If `location_id` is specified as `-` (wildcard), then all regions available to the project are queried, and the results are aggregated.



**Parameter**  
---  
**Name** | **Description**  
`request` | `[ListClustersRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-redis-cluster/latest/com.google.cloud.redis.cluster.v1beta1.ListClustersRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`[ListClustersResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-redis-cluster/latest/com.google.cloud.redis.cluster.v1beta1.ListClustersResponse)` |   
  
### rescheduleClusterMaintenance(RescheduleClusterMaintenanceRequest request)
    
    
    public Operation rescheduleClusterMaintenance(RescheduleClusterMaintenanceRequest request)

Reschedules upcoming maintenance event.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[RescheduleClusterMaintenanceRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-redis-cluster/latest/com.google.cloud.redis.cluster.v1beta1.RescheduleClusterMaintenanceRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)` |   
  
### updateCluster(UpdateClusterRequest request)
    
    
    public Operation updateCluster(UpdateClusterRequest request)

Updates the metadata and configuration of a specific Redis cluster. Completed longrunning.Operation will contain the new cluster object in the response field. The returned operation is automatically deleted after a few hours, so there is no need to call DeleteOperation.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[UpdateClusterRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-redis-cluster/latest/com.google.cloud.redis.cluster.v1beta1.UpdateClusterRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-06 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-06 UTC."],[],[]] 
