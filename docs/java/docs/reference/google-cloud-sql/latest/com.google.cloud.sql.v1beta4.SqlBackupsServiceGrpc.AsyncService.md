---
url: https://docs.cloud.google.com/java/docs/reference/google-cloud-sql/latest/com.google.cloud.sql.v1beta4.SqlBackupsServiceGrpc.AsyncService
title: Interface SqlBackupsServiceGrpc.AsyncService (0.5.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:18:52.025809+00:00
---

# Interface SqlBackupsServiceGrpc.AsyncService (0.5.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-cloud-sql/latest/com.google.cloud.sql.v1beta4.SqlBackupsServiceGrpc.AsyncService

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Interface SqlBackupsServiceGrpc.AsyncService (0.5.0) Stay organized with collections  Save and categorize content based on your preferences. 

0.5.0 (latest)  0.1.0 
    
    
    public static interface SqlBackupsServiceGrpc.AsyncService

## Methods 

### createBackup(CreateBackupRequest request, StreamObserver<Operation> responseObserver)
    
    
    public default void createBackup(CreateBackupRequest request, StreamObserver<Operation> responseObserver)

Creates a backup for a Cloud SQL instance. This API can be used only to create on-demand backups.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[CreateBackupRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-sql/latest/com.google.cloud.sql.v1beta4.CreateBackupRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-sql/latest/com.google.cloud.sql.v1beta4.Operation)>`  
  
  
### deleteBackup(DeleteBackupRequest request, StreamObserver<Operation> responseObserver)
    
    
    public default void deleteBackup(DeleteBackupRequest request, StreamObserver<Operation> responseObserver)

Deletes the backup.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[DeleteBackupRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-sql/latest/com.google.cloud.sql.v1beta4.DeleteBackupRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-sql/latest/com.google.cloud.sql.v1beta4.Operation)>`  
  
  
### getBackup(GetBackupRequest request, StreamObserver<Backup> responseObserver)
    
    
    public default void getBackup(GetBackupRequest request, StreamObserver<Backup> responseObserver)

Retrieves a resource containing information about a backup.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetBackupRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-sql/latest/com.google.cloud.sql.v1beta4.GetBackupRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[Backup](https://docs.cloud.google.com/java/docs/reference/google-cloud-sql/latest/com.google.cloud.sql.v1beta4.Backup)>`  
  
  
### listBackups(ListBackupsRequest request, StreamObserver<ListBackupsResponse> responseObserver)
    
    
    public default void listBackups(ListBackupsRequest request, StreamObserver<ListBackupsResponse> responseObserver)

Lists all backups associated with the project.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ListBackupsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-sql/latest/com.google.cloud.sql.v1beta4.ListBackupsRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[ListBackupsResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-sql/latest/com.google.cloud.sql.v1beta4.ListBackupsResponse)>`  
  
  
### updateBackup(UpdateBackupRequest request, StreamObserver<Operation> responseObserver)
    
    
    public default void updateBackup(UpdateBackupRequest request, StreamObserver<Operation> responseObserver)

Updates the retention period and the description of the backup. You can use this API to update final backups only.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[UpdateBackupRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-sql/latest/com.google.cloud.sql.v1beta4.UpdateBackupRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-sql/latest/com.google.cloud.sql.v1beta4.Operation)>`  
  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-06 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-06 UTC."],[],[]] 
