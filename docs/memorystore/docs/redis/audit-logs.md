---
url: https://docs.cloud.google.com/memorystore/docs/redis/audit-logs/
title: Memorystore for Redis audit logging \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T11:33:58.399661+00:00
---

# Memorystore for Redis audit logging  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/memorystore/docs/redis/audit-logs/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Memorystore ](https://docs.cloud.google.com/memorystore/docs)
  * [ Memorystore for Redis ](https://docs.cloud.google.com/memorystore/docs/redis)
  * [ Guides ](https://docs.cloud.google.com/memorystore/docs/redis/redis-overview)



Send feedback 

#  Memorystore for Redis audit logging Stay organized with collections  Save and categorize content based on your preferences. 

This document describes audit logging for Memorystore for Redis. Google Cloud services generate audit logs that record administrative and access activities within your Google Cloud resources. For more information about Cloud Audit Logs, see the following: 

  * [Types of audit logs](https://docs.cloud.google.com/logging/docs/audit#types)
  * [Audit log entry structure](https://docs.cloud.google.com/logging/docs/audit#audit_log_entry_structure)
  * [Storing and routing audit logs](https://docs.cloud.google.com/logging/docs/audit#storing_and_routing_audit_logs)
  * [Cloud Logging pricing summary](https://docs.cloud.google.com/stackdriver/pricing#logs-pricing-summary)
  * [Enable Data Access audit logs](https://docs.cloud.google.com/logging/docs/audit/configure-data-access)



## Service name

Memorystore for Redis audit logs use the service name `redis.googleapis.com`. Filter for this service: 
    
    
        protoPayload.serviceName="redis.googleapis.com"
      

## Methods by permission type

Each IAM permission has a `type` property, whose value is an enum that can be one of four values: `ADMIN_READ`, `ADMIN_WRITE`, `DATA_READ`, or `DATA_WRITE`. When you call a method, Memorystore for Redis generates an audit log whose category is dependent on the `type` property of the permission required to perform the method. Methods that require an IAM permission with the `type` property value of `DATA_READ`, `DATA_WRITE`, or `ADMIN_READ` generate [Data Access](https://docs.cloud.google.com/logging/docs/audit#data-access) audit logs. Methods that require an IAM permission with the `type` property value of `ADMIN_WRITE` generate [Admin Activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity) audit logs.

API methods in the following list that are marked with (LRO) are long-running operations (LROs). These methods usually generate two audit log entries: one when the operation starts and another when it ends. For more information see [Audit logs for long-running operations](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro). Permission type | Methods  
---|---  
`ADMIN_READ` | `google.cloud.redis.cluster.v1.CloudRedisCluster.ExportBackup` (LRO)  
`google.cloud.redis.cluster.v1.CloudRedisCluster.GetBackup`  
`google.cloud.redis.cluster.v1.CloudRedisCluster.GetBackupCollection`  
`google.cloud.redis.cluster.v1.CloudRedisCluster.GetCluster`  
`google.cloud.redis.cluster.v1.CloudRedisCluster.GetClusterCertificateAuthority`  
`google.cloud.redis.cluster.v1.CloudRedisCluster.ListBackupCollections`  
`google.cloud.redis.cluster.v1.CloudRedisCluster.ListBackups`  
`google.cloud.redis.cluster.v1.CloudRedisCluster.ListClusters`  
`google.cloud.redis.cluster.v1alpha1.CloudRedisCluster.ExportBackup`  
`google.cloud.redis.cluster.v1alpha1.CloudRedisCluster.GetBackup`  
`google.cloud.redis.cluster.v1alpha1.CloudRedisCluster.GetBackupCollection`  
`google.cloud.redis.cluster.v1alpha1.CloudRedisCluster.GetCluster`  
`google.cloud.redis.cluster.v1alpha1.CloudRedisCluster.GetClusterCertificateAuthority`  
`google.cloud.redis.cluster.v1alpha1.CloudRedisCluster.ListBackupCollections`  
`google.cloud.redis.cluster.v1alpha1.CloudRedisCluster.ListBackups`  
`google.cloud.redis.cluster.v1alpha1.CloudRedisCluster.ListClusters`  
`google.cloud.redis.cluster.v1beta1.CloudRedisCluster.ExportBackup` (LRO)  
`google.cloud.redis.cluster.v1beta1.CloudRedisCluster.GetBackup`  
`google.cloud.redis.cluster.v1beta1.CloudRedisCluster.GetBackupCollection`  
`google.cloud.redis.cluster.v1beta1.CloudRedisCluster.GetCluster`  
`google.cloud.redis.cluster.v1beta1.CloudRedisCluster.GetClusterCertificateAuthority`  
`google.cloud.redis.cluster.v1beta1.CloudRedisCluster.ListBackupCollections`  
`google.cloud.redis.cluster.v1beta1.CloudRedisCluster.ListBackups`  
`google.cloud.redis.cluster.v1beta1.CloudRedisCluster.ListClusters`  
`google.cloud.redis.v1.CloudRedis.GetInstance`  
`google.cloud.redis.v1.CloudRedis.GetInstanceAuthString`  
`google.cloud.redis.v1.CloudRedis.ListInstances`  
`google.cloud.redis.v1alpha1.CloudRedis.GetInstance`  
`google.cloud.redis.v1alpha1.CloudRedis.GetInstanceAuthString`  
`google.cloud.redis.v1alpha1.CloudRedis.ListInstances`  
`google.cloud.redis.v1beta1.CloudRedis.GetInstance`  
`google.cloud.redis.v1beta1.CloudRedis.GetInstanceAuthString`  
`google.cloud.redis.v1beta1.CloudRedis.ListInstances`  
`google.longrunning.Operations.GetOperation`  
`google.longrunning.Operations.ListOperations`  
`ADMIN_WRITE` | `google.cloud.redis.cluster.v1.CloudRedisCluster.BackupCluster` (LRO)  
`google.cloud.redis.cluster.v1.CloudRedisCluster.CreateCluster` (LRO)  
`google.cloud.redis.cluster.v1.CloudRedisCluster.DeleteBackup` (LRO)  
`google.cloud.redis.cluster.v1.CloudRedisCluster.DeleteCluster` (LRO)  
`google.cloud.redis.cluster.v1.CloudRedisCluster.RescheduleClusterMaintenance`  
`google.cloud.redis.cluster.v1.CloudRedisCluster.UpdateCluster` (LRO)  
`google.cloud.redis.cluster.v1alpha1.CloudRedisCluster.BackupCluster` (LRO)  
`google.cloud.redis.cluster.v1alpha1.CloudRedisCluster.CreateCluster` (LRO)  
`google.cloud.redis.cluster.v1alpha1.CloudRedisCluster.DeleteBackup` (LRO)  
`google.cloud.redis.cluster.v1alpha1.CloudRedisCluster.DeleteCluster` (LRO)  
`google.cloud.redis.cluster.v1alpha1.CloudRedisCluster.RescheduleClusterMaintenance`  
`google.cloud.redis.cluster.v1alpha1.CloudRedisCluster.UpdateCluster` (LRO)  
`google.cloud.redis.cluster.v1beta1.CloudRedisCluster.BackupCluster` (LRO)  
`google.cloud.redis.cluster.v1beta1.CloudRedisCluster.CreateCluster` (LRO)  
`google.cloud.redis.cluster.v1beta1.CloudRedisCluster.DeleteBackup` (LRO)  
`google.cloud.redis.cluster.v1beta1.CloudRedisCluster.DeleteCluster` (LRO)  
`google.cloud.redis.cluster.v1beta1.CloudRedisCluster.RescheduleClusterMaintenance`  
`google.cloud.redis.cluster.v1beta1.CloudRedisCluster.UpdateCluster` (LRO)  
`google.cloud.redis.v1.CloudRedis.CreateInstance` (LRO)  
`google.cloud.redis.v1.CloudRedis.DeleteInstance` (LRO)  
`google.cloud.redis.v1.CloudRedis.ExportInstance` (LRO)  
`google.cloud.redis.v1.CloudRedis.FailoverInstance` (LRO)  
`google.cloud.redis.v1.CloudRedis.ImportInstance` (LRO)  
`google.cloud.redis.v1.CloudRedis.RescheduleMaintenance` (LRO)  
`google.cloud.redis.v1.CloudRedis.UpdateInstance` (LRO)  
`google.cloud.redis.v1.CloudRedis.UpgradeInstance` (LRO)  
`google.cloud.redis.v1alpha1.CloudRedis.CreateInstance` (LRO)  
`google.cloud.redis.v1alpha1.CloudRedis.DeleteInstance` (LRO)  
`google.cloud.redis.v1alpha1.CloudRedis.ExportInstance` (LRO)  
`google.cloud.redis.v1alpha1.CloudRedis.FailoverInstance` (LRO)  
`google.cloud.redis.v1alpha1.CloudRedis.ImportInstance` (LRO)  
`google.cloud.redis.v1alpha1.CloudRedis.RescheduleMaintenance`  
`google.cloud.redis.v1alpha1.CloudRedis.UpdateInstance` (LRO)  
`google.cloud.redis.v1alpha1.CloudRedis.UpgradeInstance` (LRO)  
`google.cloud.redis.v1beta1.CloudRedis.CreateInstance` (LRO)  
`google.cloud.redis.v1beta1.CloudRedis.DeleteInstance` (LRO)  
`google.cloud.redis.v1beta1.CloudRedis.ExportInstance` (LRO)  
`google.cloud.redis.v1beta1.CloudRedis.FailoverInstance` (LRO)  
`google.cloud.redis.v1beta1.CloudRedis.ImportInstance` (LRO)  
`google.cloud.redis.v1beta1.CloudRedis.RescheduleMaintenance`  
`google.cloud.redis.v1beta1.CloudRedis.UpdateInstance` (LRO)  
`google.cloud.redis.v1beta1.CloudRedis.UpgradeInstance` (LRO)  
`google.longrunning.Operations.CancelOperation`  
`google.longrunning.Operations.DeleteOperation`  
  
## API interface audit logs

For information about how and which permissions are evaluated for each method, see the Identity and Access Management documentation for Memorystore for Redis.

### `google.cloud.redis.cluster.v1.CloudRedisCluster`

The following audit logs are associated with methods belonging to `google.cloud.redis.cluster.v1.CloudRedisCluster`.

#### `BackupCluster`

  * **Method** : `google.cloud.redis.cluster.v1.CloudRedisCluster.BackupCluster`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `redis.clusters.backup - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.redis.cluster.v1.CloudRedisCluster.BackupCluster" `  




#### `CreateCluster`

  * **Method** : `google.cloud.redis.cluster.v1.CloudRedisCluster.CreateCluster`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `redis.clusters.create - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.redis.cluster.v1.CloudRedisCluster.CreateCluster" `  




#### `DeleteBackup`

  * **Method** : `google.cloud.redis.cluster.v1.CloudRedisCluster.DeleteBackup`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `redis.backups.delete - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.redis.cluster.v1.CloudRedisCluster.DeleteBackup" `  




#### `DeleteCluster`

  * **Method** : `google.cloud.redis.cluster.v1.CloudRedisCluster.DeleteCluster`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `redis.clusters.delete - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.redis.cluster.v1.CloudRedisCluster.DeleteCluster" `  




#### `ExportBackup`

  * **Method** : `google.cloud.redis.cluster.v1.CloudRedisCluster.ExportBackup`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `redis.backups.export - ADMIN_READ`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.redis.cluster.v1.CloudRedisCluster.ExportBackup" `  




#### `GetBackup`

  * **Method** : `google.cloud.redis.cluster.v1.CloudRedisCluster.GetBackup`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `redis.backups.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.redis.cluster.v1.CloudRedisCluster.GetBackup" `  




#### `GetBackupCollection`

  * **Method** : `google.cloud.redis.cluster.v1.CloudRedisCluster.GetBackupCollection`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `redis.backupCollections.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.redis.cluster.v1.CloudRedisCluster.GetBackupCollection" `  




#### `GetCluster`

  * **Method** : `google.cloud.redis.cluster.v1.CloudRedisCluster.GetCluster`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `redis.clusters.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.redis.cluster.v1.CloudRedisCluster.GetCluster" `  




#### `GetClusterCertificateAuthority`

  * **Method** : `google.cloud.redis.cluster.v1.CloudRedisCluster.GetClusterCertificateAuthority`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `redis.clusters.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.redis.cluster.v1.CloudRedisCluster.GetClusterCertificateAuthority" `  




#### `ListBackupCollections`

  * **Method** : `google.cloud.redis.cluster.v1.CloudRedisCluster.ListBackupCollections`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `redis.backupCollections.list - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.redis.cluster.v1.CloudRedisCluster.ListBackupCollections" `  




#### `ListBackups`

  * **Method** : `google.cloud.redis.cluster.v1.CloudRedisCluster.ListBackups`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `redis.backups.list - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.redis.cluster.v1.CloudRedisCluster.ListBackups" `  




#### `ListClusters`

  * **Method** : `google.cloud.redis.cluster.v1.CloudRedisCluster.ListClusters`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `redis.clusters.list - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.redis.cluster.v1.CloudRedisCluster.ListClusters" `  




#### `RescheduleClusterMaintenance`

  * **Method** : `google.cloud.redis.cluster.v1.CloudRedisCluster.RescheduleClusterMaintenance`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `redis.clusters.rescheduleMaintenance - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.redis.cluster.v1.CloudRedisCluster.RescheduleClusterMaintenance" `  




#### `UpdateCluster`

  * **Method** : `google.cloud.redis.cluster.v1.CloudRedisCluster.UpdateCluster`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `redis.clusters.update - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.redis.cluster.v1.CloudRedisCluster.UpdateCluster" `  




### `google.cloud.redis.cluster.v1alpha1.CloudRedisCluster`

The following audit logs are associated with methods belonging to `google.cloud.redis.cluster.v1alpha1.CloudRedisCluster`.

#### `BackupCluster`

  * **Method** : `google.cloud.redis.cluster.v1alpha1.CloudRedisCluster.BackupCluster`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `redis.clusters.backup - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.redis.cluster.v1alpha1.CloudRedisCluster.BackupCluster" `  




#### `CreateCluster`

  * **Method** : `google.cloud.redis.cluster.v1alpha1.CloudRedisCluster.CreateCluster`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `redis.clusters.create - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.redis.cluster.v1alpha1.CloudRedisCluster.CreateCluster" `  




#### `DeleteBackup`

  * **Method** : `google.cloud.redis.cluster.v1alpha1.CloudRedisCluster.DeleteBackup`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `redis.backups.delete - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.redis.cluster.v1alpha1.CloudRedisCluster.DeleteBackup" `  




#### `DeleteCluster`

  * **Method** : `google.cloud.redis.cluster.v1alpha1.CloudRedisCluster.DeleteCluster`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `redis.clusters.delete - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.redis.cluster.v1alpha1.CloudRedisCluster.DeleteCluster" `  




#### `ExportBackup`

  * **Method** : `google.cloud.redis.cluster.v1alpha1.CloudRedisCluster.ExportBackup`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `redis.backups.export - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.redis.cluster.v1alpha1.CloudRedisCluster.ExportBackup" `  




#### `GetBackup`

  * **Method** : `google.cloud.redis.cluster.v1alpha1.CloudRedisCluster.GetBackup`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `redis.backups.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.redis.cluster.v1alpha1.CloudRedisCluster.GetBackup" `  




#### `GetBackupCollection`

  * **Method** : `google.cloud.redis.cluster.v1alpha1.CloudRedisCluster.GetBackupCollection`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `redis.backupCollections.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.redis.cluster.v1alpha1.CloudRedisCluster.GetBackupCollection" `  




#### `GetCluster`

  * **Method** : `google.cloud.redis.cluster.v1alpha1.CloudRedisCluster.GetCluster`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `redis.clusters.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.redis.cluster.v1alpha1.CloudRedisCluster.GetCluster" `  




#### `GetClusterCertificateAuthority`

  * **Method** : `google.cloud.redis.cluster.v1alpha1.CloudRedisCluster.GetClusterCertificateAuthority`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `redis.clusters.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.redis.cluster.v1alpha1.CloudRedisCluster.GetClusterCertificateAuthority" `  




#### `ListBackupCollections`

  * **Method** : `google.cloud.redis.cluster.v1alpha1.CloudRedisCluster.ListBackupCollections`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `redis.backupCollections.list - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.redis.cluster.v1alpha1.CloudRedisCluster.ListBackupCollections" `  




#### `ListBackups`

  * **Method** : `google.cloud.redis.cluster.v1alpha1.CloudRedisCluster.ListBackups`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `redis.backups.list - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.redis.cluster.v1alpha1.CloudRedisCluster.ListBackups" `  




#### `ListClusters`

  * **Method** : `google.cloud.redis.cluster.v1alpha1.CloudRedisCluster.ListClusters`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `redis.clusters.list - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.redis.cluster.v1alpha1.CloudRedisCluster.ListClusters" `  




#### `RescheduleClusterMaintenance`

  * **Method** : `google.cloud.redis.cluster.v1alpha1.CloudRedisCluster.RescheduleClusterMaintenance`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `redis.clusters.rescheduleMaintenance - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.redis.cluster.v1alpha1.CloudRedisCluster.RescheduleClusterMaintenance" `  




#### `UpdateCluster`

  * **Method** : `google.cloud.redis.cluster.v1alpha1.CloudRedisCluster.UpdateCluster`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `redis.clusters.update - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.redis.cluster.v1alpha1.CloudRedisCluster.UpdateCluster" `  




### `google.cloud.redis.cluster.v1beta1.CloudRedisCluster`

The following audit logs are associated with methods belonging to `google.cloud.redis.cluster.v1beta1.CloudRedisCluster`.

#### `BackupCluster`

  * **Method** : `google.cloud.redis.cluster.v1beta1.CloudRedisCluster.BackupCluster`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `redis.clusters.backup - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.redis.cluster.v1beta1.CloudRedisCluster.BackupCluster" `  




#### `CreateCluster`

  * **Method** : `google.cloud.redis.cluster.v1beta1.CloudRedisCluster.CreateCluster`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `redis.clusters.create - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.redis.cluster.v1beta1.CloudRedisCluster.CreateCluster" `  




#### `DeleteBackup`

  * **Method** : `google.cloud.redis.cluster.v1beta1.CloudRedisCluster.DeleteBackup`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `redis.backups.delete - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.redis.cluster.v1beta1.CloudRedisCluster.DeleteBackup" `  




#### `DeleteCluster`

  * **Method** : `google.cloud.redis.cluster.v1beta1.CloudRedisCluster.DeleteCluster`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `redis.clusters.delete - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.redis.cluster.v1beta1.CloudRedisCluster.DeleteCluster" `  




#### `ExportBackup`

  * **Method** : `google.cloud.redis.cluster.v1beta1.CloudRedisCluster.ExportBackup`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `redis.backups.export - ADMIN_READ`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.redis.cluster.v1beta1.CloudRedisCluster.ExportBackup" `  




#### `GetBackup`

  * **Method** : `google.cloud.redis.cluster.v1beta1.CloudRedisCluster.GetBackup`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `redis.backups.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.redis.cluster.v1beta1.CloudRedisCluster.GetBackup" `  




#### `GetBackupCollection`

  * **Method** : `google.cloud.redis.cluster.v1beta1.CloudRedisCluster.GetBackupCollection`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `redis.backupCollections.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.redis.cluster.v1beta1.CloudRedisCluster.GetBackupCollection" `  




#### `GetCluster`

  * **Method** : `google.cloud.redis.cluster.v1beta1.CloudRedisCluster.GetCluster`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `redis.clusters.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.redis.cluster.v1beta1.CloudRedisCluster.GetCluster" `  




#### `GetClusterCertificateAuthority`

  * **Method** : `google.cloud.redis.cluster.v1beta1.CloudRedisCluster.GetClusterCertificateAuthority`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `redis.clusters.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.redis.cluster.v1beta1.CloudRedisCluster.GetClusterCertificateAuthority" `  




#### `ListBackupCollections`

  * **Method** : `google.cloud.redis.cluster.v1beta1.CloudRedisCluster.ListBackupCollections`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `redis.backupCollections.list - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.redis.cluster.v1beta1.CloudRedisCluster.ListBackupCollections" `  




#### `ListBackups`

  * **Method** : `google.cloud.redis.cluster.v1beta1.CloudRedisCluster.ListBackups`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `redis.backups.list - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.redis.cluster.v1beta1.CloudRedisCluster.ListBackups" `  




#### `ListClusters`

  * **Method** : `google.cloud.redis.cluster.v1beta1.CloudRedisCluster.ListClusters`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `redis.clusters.list - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.redis.cluster.v1beta1.CloudRedisCluster.ListClusters" `  




#### `RescheduleClusterMaintenance`

  * **Method** : `google.cloud.redis.cluster.v1beta1.CloudRedisCluster.RescheduleClusterMaintenance`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `redis.clusters.rescheduleMaintenance - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.redis.cluster.v1beta1.CloudRedisCluster.RescheduleClusterMaintenance" `  




#### `UpdateCluster`

  * **Method** : `google.cloud.redis.cluster.v1beta1.CloudRedisCluster.UpdateCluster`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `redis.clusters.update - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.redis.cluster.v1beta1.CloudRedisCluster.UpdateCluster" `  




### `google.cloud.redis.v1.CloudRedis`

The following audit logs are associated with methods belonging to `google.cloud.redis.v1.CloudRedis`.

#### `CreateInstance`

  * **Method** : `google.cloud.redis.v1.CloudRedis.CreateInstance`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `redis.instances.create - ADMIN_WRITE`
    * `redis.instances.updateAuth - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.redis.v1.CloudRedis.CreateInstance" `  




#### `DeleteInstance`

  * **Method** : `google.cloud.redis.v1.CloudRedis.DeleteInstance`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `redis.instances.delete - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.redis.v1.CloudRedis.DeleteInstance" `  




#### `ExportInstance`

  * **Method** : `google.cloud.redis.v1.CloudRedis.ExportInstance`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `redis.instances.export - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.redis.v1.CloudRedis.ExportInstance" `  




#### `FailoverInstance`

  * **Method** : `google.cloud.redis.v1.CloudRedis.FailoverInstance`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `redis.instances.failover - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.redis.v1.CloudRedis.FailoverInstance" `  




#### `GetInstance`

  * **Method** : `google.cloud.redis.v1.CloudRedis.GetInstance`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `redis.instances.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.redis.v1.CloudRedis.GetInstance" `  




#### `GetInstanceAuthString`

  * **Method** : `google.cloud.redis.v1.CloudRedis.GetInstanceAuthString`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `redis.instances.getAuthString - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.redis.v1.CloudRedis.GetInstanceAuthString" `  




#### `ImportInstance`

  * **Method** : `google.cloud.redis.v1.CloudRedis.ImportInstance`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `redis.instances.import - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.redis.v1.CloudRedis.ImportInstance" `  




#### `ListInstances`

  * **Method** : `google.cloud.redis.v1.CloudRedis.ListInstances`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `redis.instances.list - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.redis.v1.CloudRedis.ListInstances" `  




#### `RescheduleMaintenance`

  * **Method** : `google.cloud.redis.v1.CloudRedis.RescheduleMaintenance`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `redis.instances.rescheduleMaintenance - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.redis.v1.CloudRedis.RescheduleMaintenance" `  




#### `UpdateInstance`

  * **Method** : `google.cloud.redis.v1.CloudRedis.UpdateInstance`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `redis.instances.update - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.redis.v1.CloudRedis.UpdateInstance" `  




#### `UpgradeInstance`

  * **Method** : `google.cloud.redis.v1.CloudRedis.UpgradeInstance`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `redis.instances.upgrade - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.redis.v1.CloudRedis.UpgradeInstance" `  




### `google.cloud.redis.v1alpha1.CloudRedis`

The following audit logs are associated with methods belonging to `google.cloud.redis.v1alpha1.CloudRedis`.

#### `CreateInstance`

  * **Method** : `google.cloud.redis.v1alpha1.CloudRedis.CreateInstance`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `redis.instances.create - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.redis.v1alpha1.CloudRedis.CreateInstance" `  




#### `DeleteInstance`

  * **Method** : `google.cloud.redis.v1alpha1.CloudRedis.DeleteInstance`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `redis.instances.delete - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.redis.v1alpha1.CloudRedis.DeleteInstance" `  




#### `ExportInstance`

  * **Method** : `google.cloud.redis.v1alpha1.CloudRedis.ExportInstance`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `redis.instances.export - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.redis.v1alpha1.CloudRedis.ExportInstance" `  




#### `FailoverInstance`

  * **Method** : `google.cloud.redis.v1alpha1.CloudRedis.FailoverInstance`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `redis.instances.failover - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.redis.v1alpha1.CloudRedis.FailoverInstance" `  




#### `GetInstance`

  * **Method** : `google.cloud.redis.v1alpha1.CloudRedis.GetInstance`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `redis.instances.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.redis.v1alpha1.CloudRedis.GetInstance" `  




#### `GetInstanceAuthString`

  * **Method** : `google.cloud.redis.v1alpha1.CloudRedis.GetInstanceAuthString`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `redis.instances.getAuthString - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.redis.v1alpha1.CloudRedis.GetInstanceAuthString" `  




#### `ImportInstance`

  * **Method** : `google.cloud.redis.v1alpha1.CloudRedis.ImportInstance`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `redis.instances.import - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.redis.v1alpha1.CloudRedis.ImportInstance" `  




#### `ListInstances`

  * **Method** : `google.cloud.redis.v1alpha1.CloudRedis.ListInstances`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `redis.instances.list - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.redis.v1alpha1.CloudRedis.ListInstances" `  




#### `RescheduleMaintenance`

  * **Method** : `google.cloud.redis.v1alpha1.CloudRedis.RescheduleMaintenance`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `redis.instances.rescheduleMaintenance - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.redis.v1alpha1.CloudRedis.RescheduleMaintenance" `  




#### `UpdateInstance`

  * **Method** : `google.cloud.redis.v1alpha1.CloudRedis.UpdateInstance`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `redis.instances.update - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.redis.v1alpha1.CloudRedis.UpdateInstance" `  




#### `UpgradeInstance`

  * **Method** : `google.cloud.redis.v1alpha1.CloudRedis.UpgradeInstance`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `redis.instances.upgrade - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.redis.v1alpha1.CloudRedis.UpgradeInstance" `  




### `google.cloud.redis.v1beta1.CloudRedis`

The following audit logs are associated with methods belonging to `google.cloud.redis.v1beta1.CloudRedis`.

#### `CreateInstance`

  * **Method** : `google.cloud.redis.v1beta1.CloudRedis.CreateInstance`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `redis.instances.create - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.redis.v1beta1.CloudRedis.CreateInstance" `  




#### `DeleteInstance`

  * **Method** : `google.cloud.redis.v1beta1.CloudRedis.DeleteInstance`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `redis.instances.delete - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.redis.v1beta1.CloudRedis.DeleteInstance" `  




#### `ExportInstance`

  * **Method** : `google.cloud.redis.v1beta1.CloudRedis.ExportInstance`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `redis.instances.export - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.redis.v1beta1.CloudRedis.ExportInstance" `  




#### `FailoverInstance`

  * **Method** : `google.cloud.redis.v1beta1.CloudRedis.FailoverInstance`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `redis.instances.failover - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.redis.v1beta1.CloudRedis.FailoverInstance" `  




#### `GetInstance`

  * **Method** : `google.cloud.redis.v1beta1.CloudRedis.GetInstance`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `redis.instances.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.redis.v1beta1.CloudRedis.GetInstance" `  




#### `GetInstanceAuthString`

  * **Method** : `google.cloud.redis.v1beta1.CloudRedis.GetInstanceAuthString`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `redis.instances.getAuthString - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.redis.v1beta1.CloudRedis.GetInstanceAuthString" `  




#### `ImportInstance`

  * **Method** : `google.cloud.redis.v1beta1.CloudRedis.ImportInstance`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `redis.instances.import - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.redis.v1beta1.CloudRedis.ImportInstance" `  




#### `ListInstances`

  * **Method** : `google.cloud.redis.v1beta1.CloudRedis.ListInstances`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `redis.instances.list - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.redis.v1beta1.CloudRedis.ListInstances" `  




#### `RescheduleMaintenance`

  * **Method** : `google.cloud.redis.v1beta1.CloudRedis.RescheduleMaintenance`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `redis.instances.rescheduleMaintenance - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.redis.v1beta1.CloudRedis.RescheduleMaintenance" `  




#### `UpdateInstance`

  * **Method** : `google.cloud.redis.v1beta1.CloudRedis.UpdateInstance`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `redis.instances.update - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.redis.v1beta1.CloudRedis.UpdateInstance" `  




#### `UpgradeInstance`

  * **Method** : `google.cloud.redis.v1beta1.CloudRedis.UpgradeInstance`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `redis.instances.upgrade - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.redis.v1beta1.CloudRedis.UpgradeInstance" `  




### `google.longrunning.Operations`

The following audit logs are associated with methods belonging to `google.longrunning.Operations`.

#### `CancelOperation`

  * **Method** : `google.longrunning.Operations.CancelOperation`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `redis.operations.cancel - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.longrunning.Operations.CancelOperation" `  




#### `DeleteOperation`

  * **Method** : `google.longrunning.Operations.DeleteOperation`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `redis.operations.delete - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.longrunning.Operations.DeleteOperation" `  




#### `GetOperation`

  * **Method** : `google.longrunning.Operations.GetOperation`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `redis.operations.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.longrunning.Operations.GetOperation" `  




#### `ListOperations`

  * **Method** : `google.longrunning.Operations.ListOperations`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `redis.operations.list - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.longrunning.Operations.ListOperations" `  




## Methods that don't produce audit logs

A method might not produce audit logs for one or more of the following reasons: 

  * It is a high volume method involving significant log generation and storage costs.
  * It has low auditing value.
  * Another audit or platform log already provides method coverage.



The following methods don't produce audit logs:

  * `google.cloud.location.Locations.GetLocation`
  * `google.cloud.location.Locations.ListLocations`
  * `google.longrunning.Operations.WaitOperation`



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
