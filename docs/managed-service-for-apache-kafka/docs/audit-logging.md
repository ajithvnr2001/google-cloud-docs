---
url: https://docs.cloud.google.com/managed-service-for-apache-kafka/docs/audit-logging/
title: Managed Service for Apache Kafka audit logging \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:45:10.739916+00:00
---

# Managed Service for Apache Kafka audit logging  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/managed-service-for-apache-kafka/docs/audit-logging/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Managed Service for Apache Kafka ](https://docs.cloud.google.com/managed-service-for-apache-kafka/docs)
  * [ Guides ](https://docs.cloud.google.com/managed-service-for-apache-kafka/docs/overview)



Send feedback 

#  Managed Service for Apache Kafka audit logging Stay organized with collections  Save and categorize content based on your preferences. 

This document lists the audited methods for Google Cloud Managed Service for Apache Kafka. Google Cloud services generate audit logs that record administrative and access activities within your Google Cloud resources. For more information about Cloud Audit Logs, see the following: 

  * [Types of audit logs](https://docs.cloud.google.com/logging/docs/audit#types)
  * [Audit log entry structure](https://docs.cloud.google.com/logging/docs/audit#audit_log_entry_structure)
  * [Storing and routing audit logs](https://docs.cloud.google.com/logging/docs/audit#storing_and_routing_audit_logs)
  * [Cloud Logging pricing summary](https://docs.cloud.google.com/stackdriver/pricing#logs-pricing-summary)
  * [Enable Data Access audit logs](https://docs.cloud.google.com/logging/docs/audit/configure-data-access)



## Service name

To view the Google Cloud Managed Service for Apache Kafka audit logs, do the following:

  1. In the Google Cloud console, go to the Logs Explorer page:

[Go to Logs Explorer](https://console.cloud.google.com/logs/query)

  2. Copy and paste the following query into the **Query** field of the Logs Explorer, and then click **Run query**.
         
         protoPayload.serviceName="managedkafka.googleapis.com"
           




## Methods by permission type

Each IAM permission has a `type` property, whose value is an enum that can be one of four values: `ADMIN_READ`, `ADMIN_WRITE`, `DATA_READ`, or `DATA_WRITE`. When you call a method, Google Cloud Managed Service for Apache Kafka generates an audit log whose category is dependent on the `type` property of the permission required to perform the method. Methods that require an IAM permission with the `type` property value of `DATA_READ`, `DATA_WRITE`, or `ADMIN_READ` generate [Data Access](https://docs.cloud.google.com/logging/docs/audit#data-access) audit logs. Methods that require an IAM permission with the `type` property value of `ADMIN_WRITE` generate [Admin Activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity) audit logs.

API methods in the following list that are marked with (LRO) are long-running operations (LROs). These methods usually generate two audit log entries: one when the operation starts and another when it ends. For more information see [Audit logs for long-running operations](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro). Permission type | Methods  
---|---  
`ADMIN_READ` | `google.cloud.managedkafka.schemaregistry.v1.ManagedSchemaRegistry.CheckCompatibility`  
`google.cloud.managedkafka.schemaregistry.v1.ManagedSchemaRegistry.GetContext`  
`google.cloud.managedkafka.schemaregistry.v1.ManagedSchemaRegistry.GetRawSchema`  
`google.cloud.managedkafka.schemaregistry.v1.ManagedSchemaRegistry.GetRawSchemaVersion`  
`google.cloud.managedkafka.schemaregistry.v1.ManagedSchemaRegistry.GetSchema`  
`google.cloud.managedkafka.schemaregistry.v1.ManagedSchemaRegistry.GetSchemaConfig`  
`google.cloud.managedkafka.schemaregistry.v1.ManagedSchemaRegistry.GetSchemaMode`  
`google.cloud.managedkafka.schemaregistry.v1.ManagedSchemaRegistry.GetSchemaRegistry`  
`google.cloud.managedkafka.schemaregistry.v1.ManagedSchemaRegistry.GetVersion`  
`google.cloud.managedkafka.schemaregistry.v1.ManagedSchemaRegistry.ListContexts`  
`google.cloud.managedkafka.schemaregistry.v1.ManagedSchemaRegistry.ListReferencedSchemas`  
`google.cloud.managedkafka.schemaregistry.v1.ManagedSchemaRegistry.ListSchemaRegistries`  
`google.cloud.managedkafka.schemaregistry.v1.ManagedSchemaRegistry.ListSchemaTypes`  
`google.cloud.managedkafka.schemaregistry.v1.ManagedSchemaRegistry.ListSchemaVersions`  
`google.cloud.managedkafka.schemaregistry.v1.ManagedSchemaRegistry.ListSubjects`  
`google.cloud.managedkafka.schemaregistry.v1.ManagedSchemaRegistry.ListSubjectsBySchemaId`  
`google.cloud.managedkafka.schemaregistry.v1.ManagedSchemaRegistry.ListVersions`  
`google.cloud.managedkafka.schemaregistry.v1.ManagedSchemaRegistry.LookupVersion`  
`google.cloud.managedkafka.v1.ManagedKafka.GetAcl`  
`google.cloud.managedkafka.v1.ManagedKafka.GetCluster`  
`google.cloud.managedkafka.v1.ManagedKafka.GetConsumerGroup`  
`google.cloud.managedkafka.v1.ManagedKafka.GetTopic`  
`google.cloud.managedkafka.v1.ManagedKafka.ListAcls`  
`google.cloud.managedkafka.v1.ManagedKafka.ListClusters`  
`google.cloud.managedkafka.v1.ManagedKafka.ListConsumerGroups`  
`google.cloud.managedkafka.v1.ManagedKafka.ListTopics`  
`google.cloud.managedkafka.v1.ManagedKafkaConnect.GetConnectCluster`  
`google.cloud.managedkafka.v1.ManagedKafkaConnect.GetConnector`  
`google.cloud.managedkafka.v1.ManagedKafkaConnect.ListConnectClusters`  
`google.cloud.managedkafka.v1.ManagedKafkaConnect.ListConnectors`  
`google.longrunning.Operations.GetOperation`  
`google.longrunning.Operations.ListOperations`  
`ADMIN_WRITE` | `google.cloud.managedkafka.schemaregistry.v1.ManagedSchemaRegistry.CreateSchemaRegistry`  
`google.cloud.managedkafka.schemaregistry.v1.ManagedSchemaRegistry.CreateVersion`  
`google.cloud.managedkafka.schemaregistry.v1.ManagedSchemaRegistry.DeleteSchemaConfig`  
`google.cloud.managedkafka.schemaregistry.v1.ManagedSchemaRegistry.DeleteSchemaMode`  
`google.cloud.managedkafka.schemaregistry.v1.ManagedSchemaRegistry.DeleteSchemaRegistry`  
`google.cloud.managedkafka.schemaregistry.v1.ManagedSchemaRegistry.DeleteSubject`  
`google.cloud.managedkafka.schemaregistry.v1.ManagedSchemaRegistry.DeleteVersion`  
`google.cloud.managedkafka.schemaregistry.v1.ManagedSchemaRegistry.UpdateSchemaConfig`  
`google.cloud.managedkafka.schemaregistry.v1.ManagedSchemaRegistry.UpdateSchemaMode`  
`google.cloud.managedkafka.v1.ManagedKafka.AddAclEntry`  
`google.cloud.managedkafka.v1.ManagedKafka.CreateAcl`  
`google.cloud.managedkafka.v1.ManagedKafka.CreateCluster` (LRO)  
`google.cloud.managedkafka.v1.ManagedKafka.CreateTopic`  
`google.cloud.managedkafka.v1.ManagedKafka.DeleteAcl`  
`google.cloud.managedkafka.v1.ManagedKafka.DeleteCluster` (LRO)  
`google.cloud.managedkafka.v1.ManagedKafka.DeleteConsumerGroup`  
`google.cloud.managedkafka.v1.ManagedKafka.DeleteTopic`  
`google.cloud.managedkafka.v1.ManagedKafka.RemoveAclEntry`  
`google.cloud.managedkafka.v1.ManagedKafka.UpdateAcl`  
`google.cloud.managedkafka.v1.ManagedKafka.UpdateCluster` (LRO)  
`google.cloud.managedkafka.v1.ManagedKafka.UpdateConsumerGroup`  
`google.cloud.managedkafka.v1.ManagedKafka.UpdateTopic`  
`google.cloud.managedkafka.v1.ManagedKafkaConnect.CreateConnectCluster` (LRO)  
`google.cloud.managedkafka.v1.ManagedKafkaConnect.CreateConnector`  
`google.cloud.managedkafka.v1.ManagedKafkaConnect.DeleteConnectCluster` (LRO)  
`google.cloud.managedkafka.v1.ManagedKafkaConnect.DeleteConnector`  
`google.cloud.managedkafka.v1.ManagedKafkaConnect.PauseConnector`  
`google.cloud.managedkafka.v1.ManagedKafkaConnect.RestartConnector`  
`google.cloud.managedkafka.v1.ManagedKafkaConnect.ResumeConnector`  
`google.cloud.managedkafka.v1.ManagedKafkaConnect.StopConnector`  
`google.cloud.managedkafka.v1.ManagedKafkaConnect.UpdateConnectCluster` (LRO)  
`google.cloud.managedkafka.v1.ManagedKafkaConnect.UpdateConnector`  
`google.longrunning.Operations.CancelOperation`  
`google.longrunning.Operations.DeleteOperation`  
`DATA_WRITE` | `google.cloud.managedkafka.v1.Auth.AuthenticateConnection`  
  
## API interface audit logs

For information about how and which permissions are evaluated for each method, see the Identity and Access Management documentation for Google Cloud Managed Service for Apache Kafka.

### `google.cloud.managedkafka.schemaregistry.v1.ManagedSchemaRegistry`

The following audit logs are associated with methods belonging to `google.cloud.managedkafka.schemaregistry.v1.ManagedSchemaRegistry`.

#### `CheckCompatibility`

  * **Method** : `google.cloud.managedkafka.schemaregistry.v1.ManagedSchemaRegistry.CheckCompatibility`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `managedkafka.versions.checkCompatibility - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.managedkafka.schemaregistry.v1.ManagedSchemaRegistry.CheckCompatibility" `  




#### `CreateSchemaRegistry`

  * **Method** : `google.cloud.managedkafka.schemaregistry.v1.ManagedSchemaRegistry.CreateSchemaRegistry`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `managedkafka.schemaRegistries.create - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.managedkafka.schemaregistry.v1.ManagedSchemaRegistry.CreateSchemaRegistry" `  




#### `CreateVersion`

  * **Method** : `google.cloud.managedkafka.schemaregistry.v1.ManagedSchemaRegistry.CreateVersion`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `managedkafka.versions.create - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.managedkafka.schemaregistry.v1.ManagedSchemaRegistry.CreateVersion" `  




#### `DeleteSchemaConfig`

  * **Method** : `google.cloud.managedkafka.schemaregistry.v1.ManagedSchemaRegistry.DeleteSchemaConfig`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `managedkafka.config.delete - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.managedkafka.schemaregistry.v1.ManagedSchemaRegistry.DeleteSchemaConfig" `  




#### `DeleteSchemaMode`

  * **Method** : `google.cloud.managedkafka.schemaregistry.v1.ManagedSchemaRegistry.DeleteSchemaMode`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `managedkafka.mode.delete - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.managedkafka.schemaregistry.v1.ManagedSchemaRegistry.DeleteSchemaMode" `  




#### `DeleteSchemaRegistry`

  * **Method** : `google.cloud.managedkafka.schemaregistry.v1.ManagedSchemaRegistry.DeleteSchemaRegistry`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `managedkafka.schemaRegistries.delete - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.managedkafka.schemaregistry.v1.ManagedSchemaRegistry.DeleteSchemaRegistry" `  




#### `DeleteSubject`

  * **Method** : `google.cloud.managedkafka.schemaregistry.v1.ManagedSchemaRegistry.DeleteSubject`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `managedkafka.subjects.delete - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.managedkafka.schemaregistry.v1.ManagedSchemaRegistry.DeleteSubject" `  




#### `DeleteVersion`

  * **Method** : `google.cloud.managedkafka.schemaregistry.v1.ManagedSchemaRegistry.DeleteVersion`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `managedkafka.versions.delete - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.managedkafka.schemaregistry.v1.ManagedSchemaRegistry.DeleteVersion" `  




#### `GetContext`

  * **Method** : `google.cloud.managedkafka.schemaregistry.v1.ManagedSchemaRegistry.GetContext`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `managedkafka.contexts.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.managedkafka.schemaregistry.v1.ManagedSchemaRegistry.GetContext" `  




#### `GetRawSchema`

  * **Method** : `google.cloud.managedkafka.schemaregistry.v1.ManagedSchemaRegistry.GetRawSchema`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `managedkafka.schemas.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.managedkafka.schemaregistry.v1.ManagedSchemaRegistry.GetRawSchema" `  




#### `GetRawSchemaVersion`

  * **Method** : `google.cloud.managedkafka.schemaregistry.v1.ManagedSchemaRegistry.GetRawSchemaVersion`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `managedkafka.versions.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.managedkafka.schemaregistry.v1.ManagedSchemaRegistry.GetRawSchemaVersion" `  




#### `GetSchema`

  * **Method** : `google.cloud.managedkafka.schemaregistry.v1.ManagedSchemaRegistry.GetSchema`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `managedkafka.schemas.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.managedkafka.schemaregistry.v1.ManagedSchemaRegistry.GetSchema" `  




#### `GetSchemaConfig`

  * **Method** : `google.cloud.managedkafka.schemaregistry.v1.ManagedSchemaRegistry.GetSchemaConfig`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `managedkafka.config.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.managedkafka.schemaregistry.v1.ManagedSchemaRegistry.GetSchemaConfig" `  




#### `GetSchemaMode`

  * **Method** : `google.cloud.managedkafka.schemaregistry.v1.ManagedSchemaRegistry.GetSchemaMode`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `managedkafka.mode.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.managedkafka.schemaregistry.v1.ManagedSchemaRegistry.GetSchemaMode" `  




#### `GetSchemaRegistry`

  * **Method** : `google.cloud.managedkafka.schemaregistry.v1.ManagedSchemaRegistry.GetSchemaRegistry`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `managedkafka.schemaRegistries.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.managedkafka.schemaregistry.v1.ManagedSchemaRegistry.GetSchemaRegistry" `  




#### `GetVersion`

  * **Method** : `google.cloud.managedkafka.schemaregistry.v1.ManagedSchemaRegistry.GetVersion`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `managedkafka.versions.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.managedkafka.schemaregistry.v1.ManagedSchemaRegistry.GetVersion" `  




#### `ListContexts`

  * **Method** : `google.cloud.managedkafka.schemaregistry.v1.ManagedSchemaRegistry.ListContexts`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `managedkafka.contexts.list - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.managedkafka.schemaregistry.v1.ManagedSchemaRegistry.ListContexts" `  




#### `ListReferencedSchemas`

  * **Method** : `google.cloud.managedkafka.schemaregistry.v1.ManagedSchemaRegistry.ListReferencedSchemas`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `managedkafka.versions.referencedby - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.managedkafka.schemaregistry.v1.ManagedSchemaRegistry.ListReferencedSchemas" `  




#### `ListSchemaRegistries`

  * **Method** : `google.cloud.managedkafka.schemaregistry.v1.ManagedSchemaRegistry.ListSchemaRegistries`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `managedkafka.schemaRegistries.list - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.managedkafka.schemaregistry.v1.ManagedSchemaRegistry.ListSchemaRegistries" `  




#### `ListSchemaTypes`

  * **Method** : `google.cloud.managedkafka.schemaregistry.v1.ManagedSchemaRegistry.ListSchemaTypes`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `managedkafka.schemas.listTypes - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.managedkafka.schemaregistry.v1.ManagedSchemaRegistry.ListSchemaTypes" `  




#### `ListSchemaVersions`

  * **Method** : `google.cloud.managedkafka.schemaregistry.v1.ManagedSchemaRegistry.ListSchemaVersions`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `managedkafka.schemas.listVersions - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.managedkafka.schemaregistry.v1.ManagedSchemaRegistry.ListSchemaVersions" `  




#### `ListSubjects`

  * **Method** : `google.cloud.managedkafka.schemaregistry.v1.ManagedSchemaRegistry.ListSubjects`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `managedkafka.subjects.list - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.managedkafka.schemaregistry.v1.ManagedSchemaRegistry.ListSubjects" `  




#### `ListSubjectsBySchemaId`

  * **Method** : `google.cloud.managedkafka.schemaregistry.v1.ManagedSchemaRegistry.ListSubjectsBySchemaId`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `managedkafka.schemas.listSubjects - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.managedkafka.schemaregistry.v1.ManagedSchemaRegistry.ListSubjectsBySchemaId" `  




#### `ListVersions`

  * **Method** : `google.cloud.managedkafka.schemaregistry.v1.ManagedSchemaRegistry.ListVersions`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `managedkafka.versions.list - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.managedkafka.schemaregistry.v1.ManagedSchemaRegistry.ListVersions" `  




#### `LookupVersion`

  * **Method** : `google.cloud.managedkafka.schemaregistry.v1.ManagedSchemaRegistry.LookupVersion`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `managedkafka.subjects.lookup - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.managedkafka.schemaregistry.v1.ManagedSchemaRegistry.LookupVersion" `  




#### `UpdateSchemaConfig`

  * **Method** : `google.cloud.managedkafka.schemaregistry.v1.ManagedSchemaRegistry.UpdateSchemaConfig`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `managedkafka.config.update - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.managedkafka.schemaregistry.v1.ManagedSchemaRegistry.UpdateSchemaConfig" `  




#### `UpdateSchemaMode`

  * **Method** : `google.cloud.managedkafka.schemaregistry.v1.ManagedSchemaRegistry.UpdateSchemaMode`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `managedkafka.mode.update - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.managedkafka.schemaregistry.v1.ManagedSchemaRegistry.UpdateSchemaMode" `  




### `google.cloud.managedkafka.v1.Auth`

The following audit logs are associated with methods belonging to `google.cloud.managedkafka.v1.Auth`.

#### `AuthenticateConnection`

  * **Method** : `google.cloud.managedkafka.v1.Auth.AuthenticateConnection`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `managedkafka.clusters.connect - DATA_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.managedkafka.v1.Auth.AuthenticateConnection" `  




### `google.cloud.managedkafka.v1.ManagedKafka`

The following audit logs are associated with methods belonging to `google.cloud.managedkafka.v1.ManagedKafka`.

#### `AddAclEntry`

  * **Method** : `google.cloud.managedkafka.v1.ManagedKafka.AddAclEntry`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `managedkafka.acls.updateEntries - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.managedkafka.v1.ManagedKafka.AddAclEntry" `  




#### `CreateAcl`

  * **Method** : `google.cloud.managedkafka.v1.ManagedKafka.CreateAcl`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `managedkafka.acls.create - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.managedkafka.v1.ManagedKafka.CreateAcl" `  




#### `CreateCluster`

  * **Method** : `google.cloud.managedkafka.v1.ManagedKafka.CreateCluster`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `managedkafka.clusters.create - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.managedkafka.v1.ManagedKafka.CreateCluster" `  




#### `CreateTopic`

  * **Method** : `google.cloud.managedkafka.v1.ManagedKafka.CreateTopic`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `managedkafka.topics.create - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.managedkafka.v1.ManagedKafka.CreateTopic" `  




#### `DeleteAcl`

  * **Method** : `google.cloud.managedkafka.v1.ManagedKafka.DeleteAcl`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `managedkafka.acls.delete - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.managedkafka.v1.ManagedKafka.DeleteAcl" `  




#### `DeleteCluster`

  * **Method** : `google.cloud.managedkafka.v1.ManagedKafka.DeleteCluster`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `managedkafka.clusters.delete - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.managedkafka.v1.ManagedKafka.DeleteCluster" `  




#### `DeleteConsumerGroup`

  * **Method** : `google.cloud.managedkafka.v1.ManagedKafka.DeleteConsumerGroup`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `managedkafka.consumerGroups.delete - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.managedkafka.v1.ManagedKafka.DeleteConsumerGroup" `  




#### `DeleteTopic`

  * **Method** : `google.cloud.managedkafka.v1.ManagedKafka.DeleteTopic`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `managedkafka.topics.delete - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.managedkafka.v1.ManagedKafka.DeleteTopic" `  




#### `GetAcl`

  * **Method** : `google.cloud.managedkafka.v1.ManagedKafka.GetAcl`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `managedkafka.acls.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.managedkafka.v1.ManagedKafka.GetAcl" `  




#### `GetCluster`

  * **Method** : `google.cloud.managedkafka.v1.ManagedKafka.GetCluster`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `managedkafka.clusters.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.managedkafka.v1.ManagedKafka.GetCluster" `  




#### `GetConsumerGroup`

  * **Method** : `google.cloud.managedkafka.v1.ManagedKafka.GetConsumerGroup`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `managedkafka.consumerGroups.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.managedkafka.v1.ManagedKafka.GetConsumerGroup" `  




#### `GetTopic`

  * **Method** : `google.cloud.managedkafka.v1.ManagedKafka.GetTopic`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `managedkafka.topics.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.managedkafka.v1.ManagedKafka.GetTopic" `  




#### `ListAcls`

  * **Method** : `google.cloud.managedkafka.v1.ManagedKafka.ListAcls`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `managedkafka.acls.list - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.managedkafka.v1.ManagedKafka.ListAcls" `  




#### `ListClusters`

  * **Method** : `google.cloud.managedkafka.v1.ManagedKafka.ListClusters`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `managedkafka.clusters.list - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.managedkafka.v1.ManagedKafka.ListClusters" `  




#### `ListConsumerGroups`

  * **Method** : `google.cloud.managedkafka.v1.ManagedKafka.ListConsumerGroups`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `managedkafka.consumerGroups.list - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.managedkafka.v1.ManagedKafka.ListConsumerGroups" `  




#### `ListTopics`

  * **Method** : `google.cloud.managedkafka.v1.ManagedKafka.ListTopics`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `managedkafka.topics.list - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.managedkafka.v1.ManagedKafka.ListTopics" `  




#### `RemoveAclEntry`

  * **Method** : `google.cloud.managedkafka.v1.ManagedKafka.RemoveAclEntry`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `managedkafka.acls.updateEntries - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.managedkafka.v1.ManagedKafka.RemoveAclEntry" `  




#### `UpdateAcl`

  * **Method** : `google.cloud.managedkafka.v1.ManagedKafka.UpdateAcl`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `managedkafka.acls.update - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.managedkafka.v1.ManagedKafka.UpdateAcl" `  




#### `UpdateCluster`

  * **Method** : `google.cloud.managedkafka.v1.ManagedKafka.UpdateCluster`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `managedkafka.clusters.update - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.managedkafka.v1.ManagedKafka.UpdateCluster" `  




#### `UpdateConsumerGroup`

  * **Method** : `google.cloud.managedkafka.v1.ManagedKafka.UpdateConsumerGroup`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `managedkafka.consumerGroups.update - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.managedkafka.v1.ManagedKafka.UpdateConsumerGroup" `  




#### `UpdateTopic`

  * **Method** : `google.cloud.managedkafka.v1.ManagedKafka.UpdateTopic`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `managedkafka.topics.update - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.managedkafka.v1.ManagedKafka.UpdateTopic" `  




### `google.cloud.managedkafka.v1.ManagedKafkaConnect`

The following audit logs are associated with methods belonging to `google.cloud.managedkafka.v1.ManagedKafkaConnect`.

#### `CreateConnectCluster`

  * **Method** : `google.cloud.managedkafka.v1.ManagedKafkaConnect.CreateConnectCluster`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `managedkafka.connectClusters.create - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.managedkafka.v1.ManagedKafkaConnect.CreateConnectCluster" `  




#### `CreateConnector`

  * **Method** : `google.cloud.managedkafka.v1.ManagedKafkaConnect.CreateConnector`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `managedkafka.connectors.create - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.managedkafka.v1.ManagedKafkaConnect.CreateConnector" `  




#### `DeleteConnectCluster`

  * **Method** : `google.cloud.managedkafka.v1.ManagedKafkaConnect.DeleteConnectCluster`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `managedkafka.connectClusters.delete - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.managedkafka.v1.ManagedKafkaConnect.DeleteConnectCluster" `  




#### `DeleteConnector`

  * **Method** : `google.cloud.managedkafka.v1.ManagedKafkaConnect.DeleteConnector`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `managedkafka.connectors.delete - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.managedkafka.v1.ManagedKafkaConnect.DeleteConnector" `  




#### `GetConnectCluster`

  * **Method** : `google.cloud.managedkafka.v1.ManagedKafkaConnect.GetConnectCluster`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `managedkafka.connectClusters.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.managedkafka.v1.ManagedKafkaConnect.GetConnectCluster" `  




#### `GetConnector`

  * **Method** : `google.cloud.managedkafka.v1.ManagedKafkaConnect.GetConnector`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `managedkafka.connectors.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.managedkafka.v1.ManagedKafkaConnect.GetConnector" `  




#### `ListConnectClusters`

  * **Method** : `google.cloud.managedkafka.v1.ManagedKafkaConnect.ListConnectClusters`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `managedkafka.connectClusters.list - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.managedkafka.v1.ManagedKafkaConnect.ListConnectClusters" `  




#### `ListConnectors`

  * **Method** : `google.cloud.managedkafka.v1.ManagedKafkaConnect.ListConnectors`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `managedkafka.connectors.list - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.managedkafka.v1.ManagedKafkaConnect.ListConnectors" `  




#### `PauseConnector`

  * **Method** : `google.cloud.managedkafka.v1.ManagedKafkaConnect.PauseConnector`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `managedkafka.connectors.pause - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.managedkafka.v1.ManagedKafkaConnect.PauseConnector" `  




#### `RestartConnector`

  * **Method** : `google.cloud.managedkafka.v1.ManagedKafkaConnect.RestartConnector`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `managedkafka.connectors.restart - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.managedkafka.v1.ManagedKafkaConnect.RestartConnector" `  




#### `ResumeConnector`

  * **Method** : `google.cloud.managedkafka.v1.ManagedKafkaConnect.ResumeConnector`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `managedkafka.connectors.resume - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.managedkafka.v1.ManagedKafkaConnect.ResumeConnector" `  




#### `StopConnector`

  * **Method** : `google.cloud.managedkafka.v1.ManagedKafkaConnect.StopConnector`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `managedkafka.connectors.stop - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.managedkafka.v1.ManagedKafkaConnect.StopConnector" `  




#### `UpdateConnectCluster`

  * **Method** : `google.cloud.managedkafka.v1.ManagedKafkaConnect.UpdateConnectCluster`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `managedkafka.connectClusters.update - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.managedkafka.v1.ManagedKafkaConnect.UpdateConnectCluster" `  




#### `UpdateConnector`

  * **Method** : `google.cloud.managedkafka.v1.ManagedKafkaConnect.UpdateConnector`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `managedkafka.connectors.update - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.managedkafka.v1.ManagedKafkaConnect.UpdateConnector" `  




### `google.longrunning.Operations`

The following audit logs are associated with methods belonging to `google.longrunning.Operations`.

#### `CancelOperation`

  * **Method** : `google.longrunning.Operations.CancelOperation`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `managedkafka.operations.cancel - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.longrunning.Operations.CancelOperation" `  




#### `DeleteOperation`

  * **Method** : `google.longrunning.Operations.DeleteOperation`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `managedkafka.operations.delete - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.longrunning.Operations.DeleteOperation" `  




#### `GetOperation`

  * **Method** : `google.longrunning.Operations.GetOperation`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `managedkafka.operations.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.longrunning.Operations.GetOperation" `  




#### `ListOperations`

  * **Method** : `google.longrunning.Operations.ListOperations`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `managedkafka.operations.list - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.longrunning.Operations.ListOperations" `  




_Apache Kafka® is a registered trademark of The Apache Software Foundation or its affiliates in the United States and/or other countries._

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
