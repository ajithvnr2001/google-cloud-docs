---
url: https://docs.cloud.google.com/sql/docs/postgres/audit-logging/
title: Cloud SQL for PostgreSQL audit logging \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T04:31:01.168708+00:00
---

# Cloud SQL for PostgreSQL audit logging  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sql/docs/postgres/audit-logging/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Cloud SQL ](https://docs.cloud.google.com/sql/docs)
  * [ PostgreSQL ](https://docs.cloud.google.com/sql/docs/postgres)
  * [ Guides ](https://docs.cloud.google.com/sql/docs/postgres/features)



Send feedback 

#  Cloud SQL for PostgreSQL audit logging Stay organized with collections  Save and categorize content based on your preferences. 

[MySQL](https://docs.cloud.google.com/sql/docs/mysql/audit-logging "View this page for the MySQL database engine") | PostgreSQL | [SQL Server](https://docs.cloud.google.com/sql/docs/sqlserver/audit-logging "View this page for the SQL Server database engine")

This document lists the audited methods for Cloud SQL. Google Cloud services generate audit logs that record administrative and access activities within your Google Cloud resources. For more information about Cloud Audit Logs, see the following: 

  * [Types of audit logs](https://docs.cloud.google.com/logging/docs/audit#types)
  * [Audit log entry structure](https://docs.cloud.google.com/logging/docs/audit#audit_log_entry_structure)
  * [Storing and routing audit logs](https://docs.cloud.google.com/logging/docs/audit#storing_and_routing_audit_logs)
  * [Cloud Logging pricing summary](https://docs.cloud.google.com/stackdriver/pricing#logs-pricing-summary)
  * [Enable Data Access audit logs](https://docs.cloud.google.com/logging/docs/audit/configure-data-access)



## Service name

To view the Cloud SQL audit logs, do the following:

  1. In the Google Cloud console, go to the Logs Explorer page:

[Go to Logs Explorer](https://console.cloud.google.com/logs/query)

  2. Copy and paste the following query into the **Query** field of the Logs Explorer, and then click **Run query**.
         
         protoPayload.serviceName="cloudsql.googleapis.com"
           




## Methods by permission type

Each IAM permission has a `type` property, whose value is an enum that can be one of four values: `ADMIN_READ`, `ADMIN_WRITE`, `DATA_READ`, or `DATA_WRITE`. When you call a method, Cloud SQL generates an audit log whose category is dependent on the `type` property of the permission required to perform the method. Methods that require an IAM permission with the `type` property value of `DATA_READ`, `DATA_WRITE`, or `ADMIN_READ` generate [Data Access](https://docs.cloud.google.com/logging/docs/audit#data-access) audit logs. Methods that require an IAM permission with the `type` property value of `ADMIN_WRITE` generate [Admin Activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity) audit logs.

API methods in the following list that are marked with (LRO) are long-running operations (LROs). These methods usually generate two audit log entries: one when the operation starts and another when it ends. For more information see [Audit logs for long-running operations](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro). Permission type | Methods  
---|---  
`ADMIN_READ` | `cloudsql.backupRuns.get`  
`cloudsql.backupRuns.list`  
`cloudsql.backups.list`  
`cloudsql.instances.get` (LRO)  
`cloudsql.instances.list`  
`cloudsql.instances.listServerCas`  
`cloudsql.operations.get`  
`cloudsql.operations.list`  
`cloudsql.sslCerts.get`  
`cloudsql.sslCerts.list`  
`ADMIN_WRITE` | `cloudsql.backupRuns.create` (LRO)  
`cloudsql.backupRuns.delete` (LRO)  
`cloudsql.backups.create` (LRO)  
`cloudsql.backups.delete` (LRO)  
`cloudsql.backups.update` (LRO)  
`cloudsql.instances.addServerCa` (LRO)  
`cloudsql.instances.clone` (LRO)  
`cloudsql.instances.connect`  
`cloudsql.instances.create` (LRO)  
`cloudsql.instances.delete` (LRO)  
`cloudsql.instances.demoteMaster` (LRO)  
`cloudsql.instances.failover` (LRO)  
`cloudsql.instances.migrate` (LRO)  
`cloudsql.instances.promoteReplica` (LRO)  
`cloudsql.instances.reencrypt` (LRO)  
`cloudsql.instances.resetSslConfig` (LRO)  
`cloudsql.instances.restart` (LRO)  
`cloudsql.instances.restoreBackup` (LRO)  
`cloudsql.instances.rotateServerCa` (LRO)  
`cloudsql.instances.startReplica` (LRO)  
`cloudsql.instances.stopReplica` (LRO)  
`cloudsql.instances.truncateLog` (LRO)  
`cloudsql.instances.update` (LRO)  
`cloudsql.sslCerts.create` (LRO)  
`cloudsql.sslCerts.delete` (LRO)  
`DATA_READ` | `cloudsql.databases.get`  
`cloudsql.databases.list`  
`cloudsql.instances.export` (LRO)  
`cloudsql.users.get`  
`cloudsql.users.list`  
`DATA_WRITE` | `cloudsql.databases.create` (LRO)  
`cloudsql.databases.delete` (LRO)  
`cloudsql.databases.update` (LRO)  
`cloudsql.instances.executeSql` (LRO)  
`cloudsql.instances.import` (LRO)  
`cloudsql.instances.login`  
`cloudsql.users.create` (LRO)  
`cloudsql.users.delete` (LRO)  
`cloudsql.users.update` (LRO)  
  
## API interface audit logs

For information about how and which permissions are evaluated for each method, see the Identity and Access Management documentation for Cloud SQL.

### `cloudsql.backupRuns`

The following audit logs are associated with methods belonging to `cloudsql.backupRuns`.

#### `create`

  * **Method** : `cloudsql.backupRuns.create`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `cloudsql.backupRuns.create - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="cloudsql.backupRuns.create" `  




#### `delete`

  * **Method** : `cloudsql.backupRuns.delete`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `cloudsql.backupRuns.delete - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="cloudsql.backupRuns.delete" `  




#### `get`

  * **Method** : `cloudsql.backupRuns.get`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `cloudsql.backupRuns.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="cloudsql.backupRuns.get" `  




#### `list`

  * **Method** : `cloudsql.backupRuns.list`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `cloudsql.backupRuns.list - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="cloudsql.backupRuns.list" `  




### `cloudsql.backups`

The following audit logs are associated with methods belonging to `cloudsql.backups`.

#### `create`

  * **Method** : `cloudsql.backups.create`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `cloudsql.backupRuns.create - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="cloudsql.backups.create" `  




#### `delete`

  * **Method** : `cloudsql.backups.delete`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `cloudsql.backupRuns.delete - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="cloudsql.backups.delete" `  




#### `list`

  * **Method** : `cloudsql.backups.list`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `cloudsql.backupRuns.list - ADMIN_READ`
    * `cloudsql.instances.list - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="cloudsql.backups.list" `  




#### `update`

  * **Method** : `cloudsql.backups.update`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `cloudsql.backupRuns.update - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="cloudsql.backups.update" `  




### `cloudsql.databases`

The following audit logs are associated with methods belonging to `cloudsql.databases`.

#### `create`

  * **Method** : `cloudsql.databases.create`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `cloudsql.databases.create - DATA_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="cloudsql.databases.create" `  




#### `delete`

  * **Method** : `cloudsql.databases.delete`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `cloudsql.databases.delete - DATA_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="cloudsql.databases.delete" `  




#### `get`

  * **Method** : `cloudsql.databases.get`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `cloudsql.databases.get - DATA_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="cloudsql.databases.get" `  




#### `list`

  * **Method** : `cloudsql.databases.list`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `cloudsql.databases.list - DATA_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="cloudsql.databases.list" `  




#### `update`

  * **Method** : `cloudsql.databases.update`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `cloudsql.databases.update - DATA_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="cloudsql.databases.update" `  




### `cloudsql.instances`

The following audit logs are associated with methods belonging to `cloudsql.instances`.

#### `addServerCa`

  * **Method** : `cloudsql.instances.addServerCa`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `cloudsql.instances.addServerCa - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="cloudsql.instances.addServerCa" `  




#### `clone`

  * **Method** : `cloudsql.instances.clone`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `cloudsql.instances.clone - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="cloudsql.instances.clone" `  




#### `connect`

  * **Method** : `cloudsql.instances.connect`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `cloudsql.instances.connect - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="cloudsql.instances.connect" `  




#### `create`

  * **Method** : `cloudsql.instances.create`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `cloudsql.instances.create - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="cloudsql.instances.create" `  




#### `delete`

  * **Method** : `cloudsql.instances.delete`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `cloudsql.instances.delete - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="cloudsql.instances.delete" `  




#### `demoteMaster`

  * **Method** : `cloudsql.instances.demoteMaster`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `cloudsql.instances.demoteMaster - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="cloudsql.instances.demoteMaster" `  




#### `executeSql`

  * **Method** : `cloudsql.instances.executeSql`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `cloudsql.instances.executeSql - DATA_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="cloudsql.instances.executeSql" `  




#### `export`

  * **Method** : `cloudsql.instances.export`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `cloudsql.instances.export - DATA_READ`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="cloudsql.instances.export" `  




#### `failover`

  * **Method** : `cloudsql.instances.failover`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `cloudsql.instances.failover - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="cloudsql.instances.failover" `  




#### `get`

  * **Method** : `cloudsql.instances.get`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `cloudsql.instances.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="cloudsql.instances.get" `  




#### `import`

  * **Method** : `cloudsql.instances.import`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `cloudsql.instances.import - DATA_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="cloudsql.instances.import" `  




#### `list`

  * **Method** : `cloudsql.instances.list`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `cloudsql.instances.list - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="cloudsql.instances.list" `  




#### `listServerCas`

  * **Method** : `cloudsql.instances.listServerCas`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `cloudsql.instances.listServerCas - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="cloudsql.instances.listServerCas" `  




#### `login`

  * **Method** : `cloudsql.instances.login`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `cloudsql.instances.login - DATA_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="cloudsql.instances.login" `  




#### `migrate`

  * **Method** : `cloudsql.instances.migrate`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `cloudsql.instances.migrate - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="cloudsql.instances.migrate" `  




#### `promoteReplica`

  * **Method** : `cloudsql.instances.promoteReplica`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `cloudsql.instances.promoteReplica - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="cloudsql.instances.promoteReplica" `  




#### `query`

  * **Method** : `cloudsql.instances.query`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="cloudsql.instances.query" `  




#### `reencrypt`

  * **Method** : `cloudsql.instances.reencrypt`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `cloudsql.instances.reencrypt - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="cloudsql.instances.reencrypt" `  




#### `resetSslConfig`

  * **Method** : `cloudsql.instances.resetSslConfig`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `cloudsql.instances.resetSslConfig - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="cloudsql.instances.resetSslConfig" `  




#### `restart`

  * **Method** : `cloudsql.instances.restart`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `cloudsql.instances.restart - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="cloudsql.instances.restart" `  




#### `restoreBackup`

  * **Method** : `cloudsql.instances.restoreBackup`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `cloudsql.instances.restoreBackup - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="cloudsql.instances.restoreBackup" `  




#### `rotateServerCa`

  * **Method** : `cloudsql.instances.rotateServerCa`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `cloudsql.instances.rotateServerCa - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="cloudsql.instances.rotateServerCa" `  




#### `startReplica`

  * **Method** : `cloudsql.instances.startReplica`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `cloudsql.instances.startReplica - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="cloudsql.instances.startReplica" `  




#### `stopReplica`

  * **Method** : `cloudsql.instances.stopReplica`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `cloudsql.instances.stopReplica - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="cloudsql.instances.stopReplica" `  




#### `truncateLog`

  * **Method** : `cloudsql.instances.truncateLog`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `cloudsql.instances.truncateLog - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="cloudsql.instances.truncateLog" `  




#### `update`

  * **Method** : `cloudsql.instances.update`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `cloudsql.instances.update - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="cloudsql.instances.update" `  




### `cloudsql.operations`

The following audit logs are associated with methods belonging to `cloudsql.operations`.

#### `get`

  * **Method** : `cloudsql.operations.get`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `cloudsql.instances.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="cloudsql.operations.get" `  




#### `list`

  * **Method** : `cloudsql.operations.list`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `cloudsql.instances.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="cloudsql.operations.list" `  




### `cloudsql.sslCerts`

The following audit logs are associated with methods belonging to `cloudsql.sslCerts`.

#### `create`

  * **Method** : `cloudsql.sslCerts.create`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `cloudsql.sslCerts.create - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="cloudsql.sslCerts.create" `  




#### `delete`

  * **Method** : `cloudsql.sslCerts.delete`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `cloudsql.sslCerts.delete - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="cloudsql.sslCerts.delete" `  




#### `get`

  * **Method** : `cloudsql.sslCerts.get`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `cloudsql.sslCerts.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="cloudsql.sslCerts.get" `  




#### `list`

  * **Method** : `cloudsql.sslCerts.list`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `cloudsql.sslCerts.list - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="cloudsql.sslCerts.list" `  




### `cloudsql.users`

The following audit logs are associated with methods belonging to `cloudsql.users`.

#### `create`

  * **Method** : `cloudsql.users.create`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `cloudsql.users.create - DATA_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="cloudsql.users.create" `  




#### `delete`

  * **Method** : `cloudsql.users.delete`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `cloudsql.users.delete - DATA_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="cloudsql.users.delete" `  




#### `get`

  * **Method** : `cloudsql.users.get`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `cloudsql.users.get - DATA_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="cloudsql.users.get" `  




#### `list`

  * **Method** : `cloudsql.users.list`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `cloudsql.users.list - DATA_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="cloudsql.users.list" `  




#### `update`

  * **Method** : `cloudsql.users.update`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `cloudsql.users.update - DATA_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="cloudsql.users.update" `  




## System events

System Event audit logs are generated by GCP systems, not direct user action. For more information, see [System Event audit logs](https://docs.cloud.google.com/logging/docs/audit#system-event).

Method Name | Filter For This Event | Notes  
---|---|---  
cloudsql.instances.autoFailover |  ` protoPayload.methodName="cloudsql.instances.autoFailover" ` |   
cloudsql.instances.automatedBackup |  ` protoPayload.methodName="cloudsql.instances.automatedBackup" ` |   
cloudsql.instances.automaticStorageIncrease |  ` protoPayload.methodName="cloudsql.instances.automaticStorageIncrease" ` |   
cloudsql.instances.readPoolAutoScale |  ` protoPayload.methodName="cloudsql.instances.readPoolAutoScale" ` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
