---
url: https://docs.cloud.google.com/java/docs/reference/google-cloud-spanner-jdbc/latest/com.google.cloud.spanner.DatabaseAdminClient
title: Interface DatabaseAdminClient (2.46.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T15:04:03.614842+00:00
---

# Interface DatabaseAdminClient (2.46.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-cloud-spanner-jdbc/latest/com.google.cloud.spanner.DatabaseAdminClient

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Interface DatabaseAdminClient (2.46.0) Stay organized with collections  Save and categorize content based on your preferences. 

2.46.0 (latest)  2.42.0  2.41.0  2.40.0  2.38.0  2.35.4  2.34.0  2.33.2  2.32.3  2.31.2  2.30.4  2.28.0  2.27.1  2.26.1  2.25.1  2.24.1  2.23.0  2.22.1  2.21.0  2.20.2  2.19.3  2.18.1  2.17.0  2.16.1  2.15.5  2.14.6  2.13.4  2.11.4  2.10.0  2.9.16  2.8.0  2.7.12  2.6.4  2.5.11 
    
    
    public interface DatabaseAdminClient

## Methods 

### cancelOperation(String arg0)
    
    
    public abstract void cancelOperation(String arg0)

**Parameter**  
---  
**Name** | **Description**  
`arg0` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
  
  
### copyBackup(BackupId arg0, Backup arg1)
    
    
    public default OperationFuture<Backup,CopyBackupMetadata> copyBackup(BackupId arg0, Backup arg1)

**Parameters**  
---  
**Name** | **Description**  
`arg0` | `[BackupId](https://docs.cloud.google.com/java/docs/reference/google-cloud-spanner-jdbc/latest/com.google.cloud.spanner.BackupId)`  
  
`arg1` | `[Backup](https://docs.cloud.google.com/java/docs/reference/google-cloud-spanner-jdbc/latest/com.google.cloud.spanner.Backup)`  
  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Backup](https://docs.cloud.google.com/java/docs/reference/google-cloud-spanner-jdbc/latest/com.google.cloud.spanner.Backup),com.google.spanner.admin.database.v1.CopyBackupMetadata>` |   
  
### copyBackup(String arg0, String arg1, String arg2, Timestamp arg3)
    
    
    public default OperationFuture<Backup,CopyBackupMetadata> copyBackup(String arg0, String arg1, String arg2, Timestamp arg3)

**Parameters**  
---  
**Name** | **Description**  
`arg0` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
  
`arg1` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
  
`arg2` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
  
`arg3` | `com.google.cloud.Timestamp`  
  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Backup](https://docs.cloud.google.com/java/docs/reference/google-cloud-spanner-jdbc/latest/com.google.cloud.spanner.Backup),com.google.spanner.admin.database.v1.CopyBackupMetadata>` |   
  
### createBackup(Backup arg0)
    
    
    public abstract OperationFuture<Backup,CreateBackupMetadata> createBackup(Backup arg0)

**Parameter**  
---  
**Name** | **Description**  
`arg0` | `[Backup](https://docs.cloud.google.com/java/docs/reference/google-cloud-spanner-jdbc/latest/com.google.cloud.spanner.Backup)`  
  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Backup](https://docs.cloud.google.com/java/docs/reference/google-cloud-spanner-jdbc/latest/com.google.cloud.spanner.Backup),com.google.spanner.admin.database.v1.CreateBackupMetadata>` |   
**Exceptions**  
---  
**Type** | **Description**  
`[SpannerException](https://docs.cloud.google.com/java/docs/reference/google-cloud-spanner-jdbc/latest/com.google.cloud.spanner.SpannerException)` |   
  
### createBackup(String arg0, String arg1, String arg2, Timestamp arg3)
    
    
    public abstract OperationFuture<Backup,CreateBackupMetadata> createBackup(String arg0, String arg1, String arg2, Timestamp arg3)

**Parameters**  
---  
**Name** | **Description**  
`arg0` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
  
`arg1` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
  
`arg2` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
  
`arg3` | `com.google.cloud.Timestamp`  
  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Backup](https://docs.cloud.google.com/java/docs/reference/google-cloud-spanner-jdbc/latest/com.google.cloud.spanner.Backup),com.google.spanner.admin.database.v1.CreateBackupMetadata>` |   
**Exceptions**  
---  
**Type** | **Description**  
`[SpannerException](https://docs.cloud.google.com/java/docs/reference/google-cloud-spanner-jdbc/latest/com.google.cloud.spanner.SpannerException)` |   
  
### createDatabase(Database arg0, Iterable<String> arg1)
    
    
    public abstract OperationFuture<Database,CreateDatabaseMetadata> createDatabase(Database arg0, Iterable<String> arg1)

**Parameters**  
---  
**Name** | **Description**  
`arg0` | `[Database](https://docs.cloud.google.com/java/docs/reference/google-cloud-spanner-jdbc/latest/com.google.cloud.spanner.Database)`  
  
`arg1` | `[Iterable](https://docs.oracle.com/javase/8/docs/api/java/lang/Iterable.html)<[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)>`  
  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Database](https://docs.cloud.google.com/java/docs/reference/google-cloud-spanner-jdbc/latest/com.google.cloud.spanner.Database),com.google.spanner.admin.database.v1.CreateDatabaseMetadata>` |   
**Exceptions**  
---  
**Type** | **Description**  
`[SpannerException](https://docs.cloud.google.com/java/docs/reference/google-cloud-spanner-jdbc/latest/com.google.cloud.spanner.SpannerException)` |   
  
### createDatabase(String arg0, String arg1, Dialect arg2, Iterable<String> arg3)
    
    
    public default OperationFuture<Database,CreateDatabaseMetadata> createDatabase(String arg0, String arg1, Dialect arg2, Iterable<String> arg3)

**Parameters**  
---  
**Name** | **Description**  
`arg0` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
  
`arg1` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
  
`arg2` | `[Dialect](https://docs.cloud.google.com/java/docs/reference/google-cloud-spanner-jdbc/latest/com.google.cloud.spanner.Dialect)`  
  
`arg3` | `[Iterable](https://docs.oracle.com/javase/8/docs/api/java/lang/Iterable.html)<[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)>`  
  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Database](https://docs.cloud.google.com/java/docs/reference/google-cloud-spanner-jdbc/latest/com.google.cloud.spanner.Database),com.google.spanner.admin.database.v1.CreateDatabaseMetadata>` |   
**Exceptions**  
---  
**Type** | **Description**  
`[SpannerException](https://docs.cloud.google.com/java/docs/reference/google-cloud-spanner-jdbc/latest/com.google.cloud.spanner.SpannerException)` |   
  
### createDatabase(String arg0, String arg1, Iterable<String> arg2)
    
    
    public abstract OperationFuture<Database,CreateDatabaseMetadata> createDatabase(String arg0, String arg1, Iterable<String> arg2)

**Parameters**  
---  
**Name** | **Description**  
`arg0` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
  
`arg1` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
  
`arg2` | `[Iterable](https://docs.oracle.com/javase/8/docs/api/java/lang/Iterable.html)<[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)>`  
  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Database](https://docs.cloud.google.com/java/docs/reference/google-cloud-spanner-jdbc/latest/com.google.cloud.spanner.Database),com.google.spanner.admin.database.v1.CreateDatabaseMetadata>` |   
**Exceptions**  
---  
**Type** | **Description**  
`[SpannerException](https://docs.cloud.google.com/java/docs/reference/google-cloud-spanner-jdbc/latest/com.google.cloud.spanner.SpannerException)` |   
  
### deleteBackup(String arg0, String arg1)
    
    
    public abstract void deleteBackup(String arg0, String arg1)

**Parameters**  
---  
**Name** | **Description**  
`arg0` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
  
`arg1` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
  
  
### dropDatabase(String arg0, String arg1)
    
    
    public abstract void dropDatabase(String arg0, String arg1)

**Parameters**  
---  
**Name** | **Description**  
`arg0` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
  
`arg1` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
  
**Exceptions**  
---  
**Type** | **Description**  
`[SpannerException](https://docs.cloud.google.com/java/docs/reference/google-cloud-spanner-jdbc/latest/com.google.cloud.spanner.SpannerException)` |   
  
### getBackup(String arg0, String arg1)
    
    
    public abstract Backup getBackup(String arg0, String arg1)

**Parameters**  
---  
**Name** | **Description**  
`arg0` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
  
`arg1` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Backup](https://docs.cloud.google.com/java/docs/reference/google-cloud-spanner-jdbc/latest/com.google.cloud.spanner.Backup)` |   
**Exceptions**  
---  
**Type** | **Description**  
`[SpannerException](https://docs.cloud.google.com/java/docs/reference/google-cloud-spanner-jdbc/latest/com.google.cloud.spanner.SpannerException)` |   
  
### getBackupIAMPolicy(String arg0, String arg1)
    
    
    public abstract Policy getBackupIAMPolicy(String arg0, String arg1)

**Parameters**  
---  
**Name** | **Description**  
`arg0` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
  
`arg1` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`com.google.cloud.Policy` |   
  
### getDatabase(String arg0, String arg1)
    
    
    public abstract Database getDatabase(String arg0, String arg1)

**Parameters**  
---  
**Name** | **Description**  
`arg0` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
  
`arg1` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Database](https://docs.cloud.google.com/java/docs/reference/google-cloud-spanner-jdbc/latest/com.google.cloud.spanner.Database)` |   
**Exceptions**  
---  
**Type** | **Description**  
`[SpannerException](https://docs.cloud.google.com/java/docs/reference/google-cloud-spanner-jdbc/latest/com.google.cloud.spanner.SpannerException)` |   
  
### getDatabaseDdl(String arg0, String arg1)
    
    
    public abstract List<String> getDatabaseDdl(String arg0, String arg1)

**Parameters**  
---  
**Name** | **Description**  
`arg0` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
  
`arg1` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)>` |   
  
### getDatabaseDdlResponse(String arg0, String arg1)
    
    
    public abstract GetDatabaseDdlResponse getDatabaseDdlResponse(String arg0, String arg1)

**Parameters**  
---  
**Name** | **Description**  
`arg0` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
  
`arg1` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`com.google.spanner.admin.database.v1.GetDatabaseDdlResponse` |   
  
### getDatabaseIAMPolicy(String arg0, String arg1, int arg2)
    
    
    public abstract Policy getDatabaseIAMPolicy(String arg0, String arg1, int arg2)

**Parameters**  
---  
**Name** | **Description**  
`arg0` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
  
`arg1` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
  
`arg2` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`com.google.cloud.Policy` |   
  
### getOperation(String arg0)
    
    
    public abstract Operation getOperation(String arg0)

**Parameter**  
---  
**Name** | **Description**  
`arg0` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)` |   
  
### listBackupOperations(String arg0, Options.ListOption[] arg1)
    
    
    public abstract Page<Operation> listBackupOperations(String arg0, Options.ListOption[] arg1)

**Parameters**  
---  
**Name** | **Description**  
`arg0` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
  
`arg1` | `[ListOption](https://docs.cloud.google.com/java/docs/reference/google-cloud-spanner-jdbc/latest/com.google.cloud.spanner.Options.ListOption)[]`  
  
**Returns**  
---  
**Type** | **Description**  
`[Page](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.paging.Page.html)<[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### listBackups(String arg0, Options.ListOption[] arg1)
    
    
    public abstract Page<Backup> listBackups(String arg0, Options.ListOption[] arg1)

**Parameters**  
---  
**Name** | **Description**  
`arg0` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
  
`arg1` | `[ListOption](https://docs.cloud.google.com/java/docs/reference/google-cloud-spanner-jdbc/latest/com.google.cloud.spanner.Options.ListOption)[]`  
  
**Returns**  
---  
**Type** | **Description**  
`[Page](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.paging.Page.html)<[Backup](https://docs.cloud.google.com/java/docs/reference/google-cloud-spanner-jdbc/latest/com.google.cloud.spanner.Backup)>` |   
  
### listDatabaseOperations(String arg0, Options.ListOption[] arg1)
    
    
    public abstract Page<Operation> listDatabaseOperations(String arg0, Options.ListOption[] arg1)

**Parameters**  
---  
**Name** | **Description**  
`arg0` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
  
`arg1` | `[ListOption](https://docs.cloud.google.com/java/docs/reference/google-cloud-spanner-jdbc/latest/com.google.cloud.spanner.Options.ListOption)[]`  
  
**Returns**  
---  
**Type** | **Description**  
`[Page](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.paging.Page.html)<[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### listDatabaseRoles(String arg0, String arg1, Options.ListOption[] arg2)
    
    
    public abstract Page<DatabaseRole> listDatabaseRoles(String arg0, String arg1, Options.ListOption[] arg2)

**Parameters**  
---  
**Name** | **Description**  
`arg0` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
  
`arg1` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
  
`arg2` | `[ListOption](https://docs.cloud.google.com/java/docs/reference/google-cloud-spanner-jdbc/latest/com.google.cloud.spanner.Options.ListOption)[]`  
  
**Returns**  
---  
**Type** | **Description**  
`[Page](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.paging.Page.html)<[DatabaseRole](https://docs.cloud.google.com/java/docs/reference/google-cloud-spanner-jdbc/latest/com.google.cloud.spanner.DatabaseRole)>` |   
  
### listDatabases(String arg0, Options.ListOption[] arg1)
    
    
    public abstract Page<Database> listDatabases(String arg0, Options.ListOption[] arg1)

**Parameters**  
---  
**Name** | **Description**  
`arg0` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
  
`arg1` | `[ListOption](https://docs.cloud.google.com/java/docs/reference/google-cloud-spanner-jdbc/latest/com.google.cloud.spanner.Options.ListOption)[]`  
  
**Returns**  
---  
**Type** | **Description**  
`[Page](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.paging.Page.html)<[Database](https://docs.cloud.google.com/java/docs/reference/google-cloud-spanner-jdbc/latest/com.google.cloud.spanner.Database)>` |   
  
### newBackupBuilder(BackupId arg0)
    
    
    public abstract Backup.Builder newBackupBuilder(BackupId arg0)

**Parameter**  
---  
**Name** | **Description**  
`arg0` | `[BackupId](https://docs.cloud.google.com/java/docs/reference/google-cloud-spanner-jdbc/latest/com.google.cloud.spanner.BackupId)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-spanner-jdbc/latest/com.google.cloud.spanner.Backup.Builder)` |   
  
### newDatabaseBuilder(DatabaseId arg0)
    
    
    public abstract Database.Builder newDatabaseBuilder(DatabaseId arg0)

**Parameter**  
---  
**Name** | **Description**  
`arg0` | `[DatabaseId](https://docs.cloud.google.com/java/docs/reference/google-cloud-spanner-jdbc/latest/com.google.cloud.spanner.DatabaseId)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-spanner-jdbc/latest/com.google.cloud.spanner.Database.Builder)` |   
  
### newRestoreBuilder(BackupId arg0, DatabaseId arg1)
    
    
    public abstract Restore.Builder newRestoreBuilder(BackupId arg0, DatabaseId arg1)

**Parameters**  
---  
**Name** | **Description**  
`arg0` | `[BackupId](https://docs.cloud.google.com/java/docs/reference/google-cloud-spanner-jdbc/latest/com.google.cloud.spanner.BackupId)`  
  
`arg1` | `[DatabaseId](https://docs.cloud.google.com/java/docs/reference/google-cloud-spanner-jdbc/latest/com.google.cloud.spanner.DatabaseId)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-spanner-jdbc/latest/com.google.cloud.spanner.Restore.Builder)` |   
  
### restoreDatabase(Restore arg0)
    
    
    public abstract OperationFuture<Database,RestoreDatabaseMetadata> restoreDatabase(Restore arg0)

**Parameter**  
---  
**Name** | **Description**  
`arg0` | `[Restore](https://docs.cloud.google.com/java/docs/reference/google-cloud-spanner-jdbc/latest/com.google.cloud.spanner.Restore)`  
  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Database](https://docs.cloud.google.com/java/docs/reference/google-cloud-spanner-jdbc/latest/com.google.cloud.spanner.Database),com.google.spanner.admin.database.v1.RestoreDatabaseMetadata>` |   
**Exceptions**  
---  
**Type** | **Description**  
`[SpannerException](https://docs.cloud.google.com/java/docs/reference/google-cloud-spanner-jdbc/latest/com.google.cloud.spanner.SpannerException)` |   
  
### restoreDatabase(String arg0, String arg1, String arg2, String arg3)
    
    
    public abstract OperationFuture<Database,RestoreDatabaseMetadata> restoreDatabase(String arg0, String arg1, String arg2, String arg3)

**Parameters**  
---  
**Name** | **Description**  
`arg0` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
  
`arg1` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
  
`arg2` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
  
`arg3` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Database](https://docs.cloud.google.com/java/docs/reference/google-cloud-spanner-jdbc/latest/com.google.cloud.spanner.Database),com.google.spanner.admin.database.v1.RestoreDatabaseMetadata>` |   
**Exceptions**  
---  
**Type** | **Description**  
`[SpannerException](https://docs.cloud.google.com/java/docs/reference/google-cloud-spanner-jdbc/latest/com.google.cloud.spanner.SpannerException)` |   
  
### setBackupIAMPolicy(String arg0, String arg1, Policy arg2)
    
    
    public abstract Policy setBackupIAMPolicy(String arg0, String arg1, Policy arg2)

**Parameters**  
---  
**Name** | **Description**  
`arg0` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
  
`arg1` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
  
`arg2` | `com.google.cloud.Policy`  
  
**Returns**  
---  
**Type** | **Description**  
`com.google.cloud.Policy` |   
  
### setDatabaseIAMPolicy(String arg0, String arg1, Policy arg2)
    
    
    public abstract Policy setDatabaseIAMPolicy(String arg0, String arg1, Policy arg2)

**Parameters**  
---  
**Name** | **Description**  
`arg0` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
  
`arg1` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
  
`arg2` | `com.google.cloud.Policy`  
  
**Returns**  
---  
**Type** | **Description**  
`com.google.cloud.Policy` |   
  
### testBackupIAMPermissions(String arg0, String arg1, Iterable<String> arg2)
    
    
    public abstract Iterable<String> testBackupIAMPermissions(String arg0, String arg1, Iterable<String> arg2)

**Parameters**  
---  
**Name** | **Description**  
`arg0` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
  
`arg1` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
  
`arg2` | `[Iterable](https://docs.oracle.com/javase/8/docs/api/java/lang/Iterable.html)<[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)>`  
  
**Returns**  
---  
**Type** | **Description**  
`[Iterable](https://docs.oracle.com/javase/8/docs/api/java/lang/Iterable.html)<[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)>` |   
  
### testDatabaseIAMPermissions(String arg0, String arg1, Iterable<String> arg2)
    
    
    public abstract Iterable<String> testDatabaseIAMPermissions(String arg0, String arg1, Iterable<String> arg2)

**Parameters**  
---  
**Name** | **Description**  
`arg0` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
  
`arg1` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
  
`arg2` | `[Iterable](https://docs.oracle.com/javase/8/docs/api/java/lang/Iterable.html)<[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)>`  
  
**Returns**  
---  
**Type** | **Description**  
`[Iterable](https://docs.oracle.com/javase/8/docs/api/java/lang/Iterable.html)<[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)>` |   
  
### updateBackup(String arg0, String arg1, Timestamp arg2)
    
    
    public abstract Backup updateBackup(String arg0, String arg1, Timestamp arg2)

**Parameters**  
---  
**Name** | **Description**  
`arg0` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
  
`arg1` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
  
`arg2` | `com.google.cloud.Timestamp`  
  
**Returns**  
---  
**Type** | **Description**  
`[Backup](https://docs.cloud.google.com/java/docs/reference/google-cloud-spanner-jdbc/latest/com.google.cloud.spanner.Backup)` |   
  
### updateDatabase(Database arg0, DatabaseInfo.DatabaseField[] arg1)
    
    
    public abstract OperationFuture<Database,UpdateDatabaseMetadata> updateDatabase(Database arg0, DatabaseInfo.DatabaseField[] arg1)

**Parameters**  
---  
**Name** | **Description**  
`arg0` | `[Database](https://docs.cloud.google.com/java/docs/reference/google-cloud-spanner-jdbc/latest/com.google.cloud.spanner.Database)`  
  
`arg1` | `[DatabaseField](https://docs.cloud.google.com/java/docs/reference/google-cloud-spanner-jdbc/latest/com.google.cloud.spanner.DatabaseInfo.DatabaseField)[]`  
  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Database](https://docs.cloud.google.com/java/docs/reference/google-cloud-spanner-jdbc/latest/com.google.cloud.spanner.Database),com.google.spanner.admin.database.v1.UpdateDatabaseMetadata>` |   
**Exceptions**  
---  
**Type** | **Description**  
`[SpannerException](https://docs.cloud.google.com/java/docs/reference/google-cloud-spanner-jdbc/latest/com.google.cloud.spanner.SpannerException)` |   
  
### updateDatabaseDdl(Database arg0, Iterable<String> arg1, String arg2)
    
    
    public abstract OperationFuture<Void,UpdateDatabaseDdlMetadata> updateDatabaseDdl(Database arg0, Iterable<String> arg1, String arg2)

**Parameters**  
---  
**Name** | **Description**  
`arg0` | `[Database](https://docs.cloud.google.com/java/docs/reference/google-cloud-spanner-jdbc/latest/com.google.cloud.spanner.Database)`  
  
`arg1` | `[Iterable](https://docs.oracle.com/javase/8/docs/api/java/lang/Iterable.html)<[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)>`  
  
`arg2` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Void](https://docs.oracle.com/javase/8/docs/api/java/lang/Void.html),com.google.spanner.admin.database.v1.UpdateDatabaseDdlMetadata>` |   
**Exceptions**  
---  
**Type** | **Description**  
`[SpannerException](https://docs.cloud.google.com/java/docs/reference/google-cloud-spanner-jdbc/latest/com.google.cloud.spanner.SpannerException)` |   
  
### updateDatabaseDdl(String arg0, String arg1, Iterable<String> arg2, String arg3)
    
    
    public abstract OperationFuture<Void,UpdateDatabaseDdlMetadata> updateDatabaseDdl(String arg0, String arg1, Iterable<String> arg2, String arg3)

**Parameters**  
---  
**Name** | **Description**  
`arg0` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
  
`arg1` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
  
`arg2` | `[Iterable](https://docs.oracle.com/javase/8/docs/api/java/lang/Iterable.html)<[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)>`  
  
`arg3` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Void](https://docs.oracle.com/javase/8/docs/api/java/lang/Void.html),com.google.spanner.admin.database.v1.UpdateDatabaseDdlMetadata>` |   
**Exceptions**  
---  
**Type** | **Description**  
`[SpannerException](https://docs.cloud.google.com/java/docs/reference/google-cloud-spanner-jdbc/latest/com.google.cloud.spanner.SpannerException)` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-06 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-06 UTC."],[],[]] 
