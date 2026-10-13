---
url: https://docs.cloud.google.com/java/docs/reference/google-cloud-filestore/latest/com.google.cloud.filestore.v1.CloudFilestoreManagerGrpc.AsyncService
title: Interface CloudFilestoreManagerGrpc.AsyncService (1.100.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T17:56:56.318203+00:00
---

# Interface CloudFilestoreManagerGrpc.AsyncService (1.100.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-cloud-filestore/latest/com.google.cloud.filestore.v1.CloudFilestoreManagerGrpc.AsyncService

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Interface CloudFilestoreManagerGrpc.AsyncService (1.100.0) Stay organized with collections  Save and categorize content based on your preferences. 

1.100.0 (latest)  1.96.0  1.95.0  1.94.0  1.92.0  1.89.0  1.88.0  1.86.0  1.84.0  1.83.0  1.82.0  1.81.0  1.79.0  1.77.0  1.76.0  1.75.0  1.74.0  1.73.0  1.71.0  1.69.0  1.68.0  1.65.0  1.64.0  1.63.0  1.61.0  1.60.0  1.59.0  1.58.0  1.57.0  1.56.0  1.55.0  1.54.0  1.53.0  1.52.0  1.50.0  1.49.0  1.48.0  1.47.0  1.46.0  1.45.0  1.44.0  1.43.0  1.42.0  1.41.0  1.40.0  1.38.0  1.37.0  1.36.0  1.35.0  1.34.0  1.33.0  1.32.0  1.31.0  1.30.0  1.29.0  1.28.0  1.25.0  1.24.0  1.23.0  1.22.0  1.21.0  1.20.0  1.19.0  1.18.0  1.17.0  1.16.0  1.15.0  1.14.0  1.13.0  1.12.0  1.10.0  1.9.0  1.8.0  1.7.0  1.6.0  1.5.0  1.2.0 
    
    
    public static interface CloudFilestoreManagerGrpc.AsyncService

Configures and manages Filestore resources. Filestore Manager v1. The `file.googleapis.com` service implements the Filestore API and defines the following resource model for managing instances:

  * The service works with a collection of cloud projects, named: `/projects/*`
  * Each project has a collection of available locations, named: `/locations/*`
  * Each location has a collection of instances and backups, named: `/instances/*` and `/backups/*` respectively.
  * As such, Filestore instances are resources of the form: `/projects/{project_number}/locations/{location_id}/instances/{instance_id}` and backups are resources of the form: `/projects/{project_number}/locations/{location_id}/backup/{backup_id}` Note that location_id must be a Google Cloud `zone` for instances, but a Google Cloud `region` for backups; for example:
  * `projects/12345/locations/us-central1-c/instances/my-filestore`
  * `projects/12345/locations/us-central1/backups/my-backup`



## Methods 

### createBackup(CreateBackupRequest request, StreamObserver<Operation> responseObserver)
    
    
    public default void createBackup(CreateBackupRequest request, StreamObserver<Operation> responseObserver)

Creates a backup.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[CreateBackupRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-filestore/latest/com.google.cloud.filestore.v1.CreateBackupRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>`  
  
  
### createInstance(CreateInstanceRequest request, StreamObserver<Operation> responseObserver)
    
    
    public default void createInstance(CreateInstanceRequest request, StreamObserver<Operation> responseObserver)

Creates an instance. When creating from a backup, the capacity of the new instance needs to be equal to or larger than the capacity of the backup (and also equal to or larger than the minimum capacity of the tier).

**Parameters**  
---  
**Name** | **Description**  
`request` | `[CreateInstanceRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-filestore/latest/com.google.cloud.filestore.v1.CreateInstanceRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>`  
  
  
### createSnapshot(CreateSnapshotRequest request, StreamObserver<Operation> responseObserver)
    
    
    public default void createSnapshot(CreateSnapshotRequest request, StreamObserver<Operation> responseObserver)

Creates a snapshot.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[CreateSnapshotRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-filestore/latest/com.google.cloud.filestore.v1.CreateSnapshotRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>`  
  
  
### deleteBackup(DeleteBackupRequest request, StreamObserver<Operation> responseObserver)
    
    
    public default void deleteBackup(DeleteBackupRequest request, StreamObserver<Operation> responseObserver)

Deletes a backup.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[DeleteBackupRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-filestore/latest/com.google.cloud.filestore.v1.DeleteBackupRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>`  
  
  
### deleteInstance(DeleteInstanceRequest request, StreamObserver<Operation> responseObserver)
    
    
    public default void deleteInstance(DeleteInstanceRequest request, StreamObserver<Operation> responseObserver)

Deletes an instance.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[DeleteInstanceRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-filestore/latest/com.google.cloud.filestore.v1.DeleteInstanceRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>`  
  
  
### deleteSnapshot(DeleteSnapshotRequest request, StreamObserver<Operation> responseObserver)
    
    
    public default void deleteSnapshot(DeleteSnapshotRequest request, StreamObserver<Operation> responseObserver)

Deletes a snapshot.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[DeleteSnapshotRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-filestore/latest/com.google.cloud.filestore.v1.DeleteSnapshotRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>`  
  
  
### getBackup(GetBackupRequest request, StreamObserver<Backup> responseObserver)
    
    
    public default void getBackup(GetBackupRequest request, StreamObserver<Backup> responseObserver)

Gets the details of a specific backup.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetBackupRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-filestore/latest/com.google.cloud.filestore.v1.GetBackupRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[Backup](https://docs.cloud.google.com/java/docs/reference/google-cloud-filestore/latest/com.google.cloud.filestore.v1.Backup)>`  
  
  
### getInstance(GetInstanceRequest request, StreamObserver<Instance> responseObserver)
    
    
    public default void getInstance(GetInstanceRequest request, StreamObserver<Instance> responseObserver)

Gets the details of a specific instance.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetInstanceRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-filestore/latest/com.google.cloud.filestore.v1.GetInstanceRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[Instance](https://docs.cloud.google.com/java/docs/reference/google-cloud-filestore/latest/com.google.cloud.filestore.v1.Instance)>`  
  
  
### getSnapshot(GetSnapshotRequest request, StreamObserver<Snapshot> responseObserver)
    
    
    public default void getSnapshot(GetSnapshotRequest request, StreamObserver<Snapshot> responseObserver)

Gets the details of a specific snapshot.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetSnapshotRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-filestore/latest/com.google.cloud.filestore.v1.GetSnapshotRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[Snapshot](https://docs.cloud.google.com/java/docs/reference/google-cloud-filestore/latest/com.google.cloud.filestore.v1.Snapshot)>`  
  
  
### listBackups(ListBackupsRequest request, StreamObserver<ListBackupsResponse> responseObserver)
    
    
    public default void listBackups(ListBackupsRequest request, StreamObserver<ListBackupsResponse> responseObserver)

Lists all backups in a project for either a specified location or for all locations.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ListBackupsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-filestore/latest/com.google.cloud.filestore.v1.ListBackupsRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[ListBackupsResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-filestore/latest/com.google.cloud.filestore.v1.ListBackupsResponse)>`  
  
  
### listInstances(ListInstancesRequest request, StreamObserver<ListInstancesResponse> responseObserver)
    
    
    public default void listInstances(ListInstancesRequest request, StreamObserver<ListInstancesResponse> responseObserver)

Lists all instances in a project for either a specified location or for all locations.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ListInstancesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-filestore/latest/com.google.cloud.filestore.v1.ListInstancesRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[ListInstancesResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-filestore/latest/com.google.cloud.filestore.v1.ListInstancesResponse)>`  
  
  
### listSnapshots(ListSnapshotsRequest request, StreamObserver<ListSnapshotsResponse> responseObserver)
    
    
    public default void listSnapshots(ListSnapshotsRequest request, StreamObserver<ListSnapshotsResponse> responseObserver)

Lists all snapshots in a project for either a specified location or for all locations.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ListSnapshotsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-filestore/latest/com.google.cloud.filestore.v1.ListSnapshotsRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[ListSnapshotsResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-filestore/latest/com.google.cloud.filestore.v1.ListSnapshotsResponse)>`  
  
  
### promoteReplica(PromoteReplicaRequest request, StreamObserver<Operation> responseObserver)
    
    
    public default void promoteReplica(PromoteReplicaRequest request, StreamObserver<Operation> responseObserver)

Promote the standby instance (replica).

**Parameters**  
---  
**Name** | **Description**  
`request` | `[PromoteReplicaRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-filestore/latest/com.google.cloud.filestore.v1.PromoteReplicaRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>`  
  
  
### restoreInstance(RestoreInstanceRequest request, StreamObserver<Operation> responseObserver)
    
    
    public default void restoreInstance(RestoreInstanceRequest request, StreamObserver<Operation> responseObserver)

Restores an existing instance's file share from a backup. The capacity of the instance needs to be equal to or larger than the capacity of the backup (and also equal to or larger than the minimum capacity of the tier).

**Parameters**  
---  
**Name** | **Description**  
`request` | `[RestoreInstanceRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-filestore/latest/com.google.cloud.filestore.v1.RestoreInstanceRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>`  
  
  
### revertInstance(RevertInstanceRequest request, StreamObserver<Operation> responseObserver)
    
    
    public default void revertInstance(RevertInstanceRequest request, StreamObserver<Operation> responseObserver)

Revert an existing instance's file system to a specified snapshot.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[RevertInstanceRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-filestore/latest/com.google.cloud.filestore.v1.RevertInstanceRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>`  
  
  
### updateBackup(UpdateBackupRequest request, StreamObserver<Operation> responseObserver)
    
    
    public default void updateBackup(UpdateBackupRequest request, StreamObserver<Operation> responseObserver)

Updates the settings of a specific backup.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[UpdateBackupRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-filestore/latest/com.google.cloud.filestore.v1.UpdateBackupRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>`  
  
  
### updateInstance(UpdateInstanceRequest request, StreamObserver<Operation> responseObserver)
    
    
    public default void updateInstance(UpdateInstanceRequest request, StreamObserver<Operation> responseObserver)

Updates the settings of a specific instance.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[UpdateInstanceRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-filestore/latest/com.google.cloud.filestore.v1.UpdateInstanceRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>`  
  
  
### updateSnapshot(UpdateSnapshotRequest request, StreamObserver<Operation> responseObserver)
    
    
    public default void updateSnapshot(UpdateSnapshotRequest request, StreamObserver<Operation> responseObserver)

Updates the settings of a specific snapshot.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[UpdateSnapshotRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-filestore/latest/com.google.cloud.filestore.v1.UpdateSnapshotRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>`  
  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-07 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-07 UTC."],[],[]] 
