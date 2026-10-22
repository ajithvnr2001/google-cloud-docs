---
url: https://docs.cloud.google.com/composer/docs/composer-3/audit-logging/
title: Managed Service for Apache Airflow audit logging \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:17:53.091930+00:00
---

# Managed Service for Apache Airflow audit logging  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/composer/docs/composer-3/audit-logging/

To more strongly embrace the success and growing customer preference for OSS solutions, Cloud Composer is evolving to become **Managed Service for Apache Airflow**. This name change provides improved customer understanding of our portfolio while reinforcing our commitment to being the most open cloud ecosystem. 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Managed Service for Apache Airflow ](https://docs.cloud.google.com/composer/docs)
  * [ Gen 3 Guides ](https://docs.cloud.google.com/composer/docs/composer-3/composer-overview)



Send feedback 

#  Managed Service for Apache Airflow audit logging Stay organized with collections  Save and categorize content based on your preferences. 

**Managed Airflow (Gen 3)** | [Managed Airflow (Gen 2)](https://docs.cloud.google.com/composer/docs/composer-2/audit-logging "View this page for Managed Airflow \(Gen 2\)") | [Managed Airflow (Legacy Gen 1)](https://docs.cloud.google.com/composer/docs/composer-1/audit-logging "View this page for Managed Airflow \(Legacy Gen 1\)")

This document describes audit logging for Managed Service for Apache Airflow. Google Cloud services generate audit logs that record administrative and access activities within your Google Cloud resources. For more information about Cloud Audit Logs, see the following: 

  * [Types of audit logs](https://docs.cloud.google.com/logging/docs/audit#types)
  * [Audit log entry structure](https://docs.cloud.google.com/logging/docs/audit#audit_log_entry_structure)
  * [Storing and routing audit logs](https://docs.cloud.google.com/logging/docs/audit#storing_and_routing_audit_logs)
  * [Cloud Logging pricing summary](https://docs.cloud.google.com/stackdriver/pricing#logs-pricing-summary)
  * [Enable Data Access audit logs](https://docs.cloud.google.com/logging/docs/audit/configure-data-access)



## Service name

Managed Service for Apache Airflow audit logs use the service name `composer.googleapis.com`. Filter for this service: 
    
    
        protoPayload.serviceName="composer.googleapis.com"
      

## Methods by permission type

Each IAM permission has a `type` property, whose value is an enum that can be one of four values: `ADMIN_READ`, `ADMIN_WRITE`, `DATA_READ`, or `DATA_WRITE`. When you call a method, Managed Service for Apache Airflow generates an audit log whose category is dependent on the `type` property of the permission required to perform the method. Methods that require an IAM permission with the `type` property value of `DATA_READ`, `DATA_WRITE`, or `ADMIN_READ` generate [Data Access](https://docs.cloud.google.com/logging/docs/audit#data-access) audit logs. Methods that require an IAM permission with the `type` property value of `ADMIN_WRITE` generate [Admin Activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity) audit logs.

API methods in the following list that are marked with (LRO) are long-running operations (LROs). These methods usually generate two audit log entries: one when the operation starts and another when it ends. For more information see [Audit logs for long-running operations](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro). Permission type | Methods  
---|---  
`ADMIN_READ` | `google.cloud.orchestration.airflow.service.v1.Environments.FetchDatabaseProperties`  
`google.cloud.orchestration.airflow.service.v1.Environments.GetEnvironment`  
`google.cloud.orchestration.airflow.service.v1.Environments.GetUserWorkloadsConfigMap`  
`google.cloud.orchestration.airflow.service.v1.Environments.GetUserWorkloadsSecret`  
`google.cloud.orchestration.airflow.service.v1.Environments.ListEnvironments`  
`google.cloud.orchestration.airflow.service.v1.Environments.ListUserWorkloadsConfigMaps`  
`google.cloud.orchestration.airflow.service.v1.Environments.ListUserWorkloadsSecrets`  
`google.cloud.orchestration.airflow.service.v1.Environments.ListWorkloads`  
`google.cloud.orchestration.airflow.service.v1.ImageVersions.ListImageVersions`  
`google.cloud.orchestration.airflow.service.v1beta1.Environments.FetchDatabaseProperties`  
`google.cloud.orchestration.airflow.service.v1beta1.Environments.GetEnvironment`  
`google.cloud.orchestration.airflow.service.v1beta1.Environments.GetUserWorkloadsConfigMap`  
`google.cloud.orchestration.airflow.service.v1beta1.Environments.GetUserWorkloadsSecret`  
`google.cloud.orchestration.airflow.service.v1beta1.Environments.ListEnvironments`  
`google.cloud.orchestration.airflow.service.v1beta1.Environments.ListUserWorkloadsConfigMaps`  
`google.cloud.orchestration.airflow.service.v1beta1.Environments.ListUserWorkloadsSecrets`  
`google.cloud.orchestration.airflow.service.v1beta1.Environments.ListWorkloads`  
`google.cloud.orchestration.airflow.service.v1beta1.ImageVersions.ListImageVersions`  
`ADMIN_WRITE` | `google.cloud.orchestration.airflow.service.v1.Environments.CheckUpgrade` (LRO)  
`google.cloud.orchestration.airflow.service.v1.Environments.CreateEnvironment` (LRO)  
`google.cloud.orchestration.airflow.service.v1.Environments.CreateUserWorkloadsConfigMap`  
`google.cloud.orchestration.airflow.service.v1.Environments.CreateUserWorkloadsSecret`  
`google.cloud.orchestration.airflow.service.v1.Environments.DatabaseFailover` (LRO)  
`google.cloud.orchestration.airflow.service.v1.Environments.DeleteEnvironment` (LRO)  
`google.cloud.orchestration.airflow.service.v1.Environments.DeleteUserWorkloadsConfigMap`  
`google.cloud.orchestration.airflow.service.v1.Environments.DeleteUserWorkloadsSecret`  
`google.cloud.orchestration.airflow.service.v1.Environments.ExecuteAirflowCommand`  
`google.cloud.orchestration.airflow.service.v1.Environments.LoadSnapshot` (LRO)  
`google.cloud.orchestration.airflow.service.v1.Environments.PollAirflowCommand`  
`google.cloud.orchestration.airflow.service.v1.Environments.SaveSnapshot` (LRO)  
`google.cloud.orchestration.airflow.service.v1.Environments.StopAirflowCommand`  
`google.cloud.orchestration.airflow.service.v1.Environments.UpdateEnvironment` (LRO)  
`google.cloud.orchestration.airflow.service.v1.Environments.UpdateUserWorkloadsConfigMap`  
`google.cloud.orchestration.airflow.service.v1.Environments.UpdateUserWorkloadsSecret`  
`google.cloud.orchestration.airflow.service.v1beta1.Environments.CheckUpgrade` (LRO)  
`google.cloud.orchestration.airflow.service.v1beta1.Environments.CreateEnvironment` (LRO)  
`google.cloud.orchestration.airflow.service.v1beta1.Environments.CreateUserWorkloadsConfigMap`  
`google.cloud.orchestration.airflow.service.v1beta1.Environments.CreateUserWorkloadsSecret`  
`google.cloud.orchestration.airflow.service.v1beta1.Environments.DatabaseFailover` (LRO)  
`google.cloud.orchestration.airflow.service.v1beta1.Environments.DeleteEnvironment` (LRO)  
`google.cloud.orchestration.airflow.service.v1beta1.Environments.DeleteUserWorkloadsConfigMap`  
`google.cloud.orchestration.airflow.service.v1beta1.Environments.DeleteUserWorkloadsSecret`  
`google.cloud.orchestration.airflow.service.v1beta1.Environments.ExecuteAirflowCommand`  
`google.cloud.orchestration.airflow.service.v1beta1.Environments.LoadSnapshot` (LRO)  
`google.cloud.orchestration.airflow.service.v1beta1.Environments.PollAirflowCommand`  
`google.cloud.orchestration.airflow.service.v1beta1.Environments.RestartWebServer` (LRO)  
`google.cloud.orchestration.airflow.service.v1beta1.Environments.SaveSnapshot` (LRO)  
`google.cloud.orchestration.airflow.service.v1beta1.Environments.StopAirflowCommand`  
`google.cloud.orchestration.airflow.service.v1beta1.Environments.UpdateEnvironment` (LRO)  
`google.cloud.orchestration.airflow.service.v1beta1.Environments.UpdateUserWorkloadsConfigMap`  
`google.cloud.orchestration.airflow.service.v1beta1.Environments.UpdateUserWorkloadsSecret`  
`google.longrunning.Operations.DeleteOperation`  
  
## API interface audit logs

For information about how and which permissions are evaluated for each method, see the Identity and Access Management documentation for Managed Service for Apache Airflow.

### `google.cloud.orchestration.airflow.service.v1.Environments`

The following audit logs are associated with methods belonging to `google.cloud.orchestration.airflow.service.v1.Environments`.

#### `CheckUpgrade`

  * **Method** : `google.cloud.orchestration.airflow.service.v1.Environments.CheckUpgrade`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `composer.environments.update - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.orchestration.airflow.service.v1.Environments.CheckUpgrade" `  




#### `CreateEnvironment`

  * **Method** : `google.cloud.orchestration.airflow.service.v1.Environments.CreateEnvironment`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `composer.environments.create - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.orchestration.airflow.service.v1.Environments.CreateEnvironment" `  




#### `CreateUserWorkloadsConfigMap`

  * **Method** : `google.cloud.orchestration.airflow.service.v1.Environments.CreateUserWorkloadsConfigMap`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `composer.userworkloadsconfigmaps.create - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.orchestration.airflow.service.v1.Environments.CreateUserWorkloadsConfigMap" `  




#### `CreateUserWorkloadsSecret`

  * **Method** : `google.cloud.orchestration.airflow.service.v1.Environments.CreateUserWorkloadsSecret`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `composer.userworkloadssecrets.create - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.orchestration.airflow.service.v1.Environments.CreateUserWorkloadsSecret" `  




#### `DatabaseFailover`

  * **Method** : `google.cloud.orchestration.airflow.service.v1.Environments.DatabaseFailover`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `composer.environments.update - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.orchestration.airflow.service.v1.Environments.DatabaseFailover" `  




#### `DeleteEnvironment`

  * **Method** : `google.cloud.orchestration.airflow.service.v1.Environments.DeleteEnvironment`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `composer.environments.delete - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.orchestration.airflow.service.v1.Environments.DeleteEnvironment" `  




#### `DeleteUserWorkloadsConfigMap`

  * **Method** : `google.cloud.orchestration.airflow.service.v1.Environments.DeleteUserWorkloadsConfigMap`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `composer.userworkloadsconfigmaps.delete - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.orchestration.airflow.service.v1.Environments.DeleteUserWorkloadsConfigMap" `  




#### `DeleteUserWorkloadsSecret`

  * **Method** : `google.cloud.orchestration.airflow.service.v1.Environments.DeleteUserWorkloadsSecret`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `composer.userworkloadssecrets.delete - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.orchestration.airflow.service.v1.Environments.DeleteUserWorkloadsSecret" `  




#### `ExecuteAirflowCommand`

  * **Method** : `google.cloud.orchestration.airflow.service.v1.Environments.ExecuteAirflowCommand`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `composer.environments.executeAirflowCommand - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.orchestration.airflow.service.v1.Environments.ExecuteAirflowCommand" `  




#### `FetchDatabaseProperties`

  * **Method** : `google.cloud.orchestration.airflow.service.v1.Environments.FetchDatabaseProperties`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `composer.environments.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.orchestration.airflow.service.v1.Environments.FetchDatabaseProperties" `  




#### `GetEnvironment`

  * **Method** : `google.cloud.orchestration.airflow.service.v1.Environments.GetEnvironment`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `composer.environments.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.orchestration.airflow.service.v1.Environments.GetEnvironment" `  




#### `GetUserWorkloadsConfigMap`

  * **Method** : `google.cloud.orchestration.airflow.service.v1.Environments.GetUserWorkloadsConfigMap`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `composer.userworkloadsconfigmaps.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.orchestration.airflow.service.v1.Environments.GetUserWorkloadsConfigMap" `  




#### `GetUserWorkloadsSecret`

  * **Method** : `google.cloud.orchestration.airflow.service.v1.Environments.GetUserWorkloadsSecret`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `composer.userworkloadssecrets.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.orchestration.airflow.service.v1.Environments.GetUserWorkloadsSecret" `  




#### `ListEnvironments`

  * **Method** : `google.cloud.orchestration.airflow.service.v1.Environments.ListEnvironments`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `composer.environments.list - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.orchestration.airflow.service.v1.Environments.ListEnvironments" `  




#### `ListUserWorkloadsConfigMaps`

  * **Method** : `google.cloud.orchestration.airflow.service.v1.Environments.ListUserWorkloadsConfigMaps`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `composer.userworkloadsconfigmaps.list - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.orchestration.airflow.service.v1.Environments.ListUserWorkloadsConfigMaps" `  




#### `ListUserWorkloadsSecrets`

  * **Method** : `google.cloud.orchestration.airflow.service.v1.Environments.ListUserWorkloadsSecrets`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `composer.userworkloadssecrets.list - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.orchestration.airflow.service.v1.Environments.ListUserWorkloadsSecrets" `  




#### `ListWorkloads`

  * **Method** : `google.cloud.orchestration.airflow.service.v1.Environments.ListWorkloads`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `composer.environments.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.orchestration.airflow.service.v1.Environments.ListWorkloads" `  




#### `LoadSnapshot`

  * **Method** : `google.cloud.orchestration.airflow.service.v1.Environments.LoadSnapshot`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `composer.environments.update - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.orchestration.airflow.service.v1.Environments.LoadSnapshot" `  




#### `PollAirflowCommand`

  * **Method** : `google.cloud.orchestration.airflow.service.v1.Environments.PollAirflowCommand`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `composer.environments.executeAirflowCommand - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.orchestration.airflow.service.v1.Environments.PollAirflowCommand" `  




#### `SaveSnapshot`

  * **Method** : `google.cloud.orchestration.airflow.service.v1.Environments.SaveSnapshot`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `composer.environments.update - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.orchestration.airflow.service.v1.Environments.SaveSnapshot" `  




#### `StopAirflowCommand`

  * **Method** : `google.cloud.orchestration.airflow.service.v1.Environments.StopAirflowCommand`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `composer.environments.executeAirflowCommand - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.orchestration.airflow.service.v1.Environments.StopAirflowCommand" `  




#### `UpdateEnvironment`

  * **Method** : `google.cloud.orchestration.airflow.service.v1.Environments.UpdateEnvironment`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `composer.environments.update - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.orchestration.airflow.service.v1.Environments.UpdateEnvironment" `  




#### `UpdateUserWorkloadsConfigMap`

  * **Method** : `google.cloud.orchestration.airflow.service.v1.Environments.UpdateUserWorkloadsConfigMap`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `composer.userworkloadsconfigmaps.update - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.orchestration.airflow.service.v1.Environments.UpdateUserWorkloadsConfigMap" `  




#### `UpdateUserWorkloadsSecret`

  * **Method** : `google.cloud.orchestration.airflow.service.v1.Environments.UpdateUserWorkloadsSecret`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `composer.userworkloadssecrets.update - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.orchestration.airflow.service.v1.Environments.UpdateUserWorkloadsSecret" `  




### `google.cloud.orchestration.airflow.service.v1.ImageVersions`

The following audit logs are associated with methods belonging to `google.cloud.orchestration.airflow.service.v1.ImageVersions`.

#### `ListImageVersions`

  * **Method** : `google.cloud.orchestration.airflow.service.v1.ImageVersions.ListImageVersions`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `composer.imageversions.list - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.orchestration.airflow.service.v1.ImageVersions.ListImageVersions" `  




### `google.cloud.orchestration.airflow.service.v1beta1.Environments`

The following audit logs are associated with methods belonging to `google.cloud.orchestration.airflow.service.v1beta1.Environments`.

#### `CheckUpgrade`

  * **Method** : `google.cloud.orchestration.airflow.service.v1beta1.Environments.CheckUpgrade`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `composer.environments.update - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.orchestration.airflow.service.v1beta1.Environments.CheckUpgrade" `  




#### `CreateEnvironment`

  * **Method** : `google.cloud.orchestration.airflow.service.v1beta1.Environments.CreateEnvironment`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `composer.environments.create - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.orchestration.airflow.service.v1beta1.Environments.CreateEnvironment" `  




#### `CreateUserWorkloadsConfigMap`

  * **Method** : `google.cloud.orchestration.airflow.service.v1beta1.Environments.CreateUserWorkloadsConfigMap`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `composer.userworkloadsconfigmaps.create - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.orchestration.airflow.service.v1beta1.Environments.CreateUserWorkloadsConfigMap" `  




#### `CreateUserWorkloadsSecret`

  * **Method** : `google.cloud.orchestration.airflow.service.v1beta1.Environments.CreateUserWorkloadsSecret`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `composer.userworkloadssecrets.create - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.orchestration.airflow.service.v1beta1.Environments.CreateUserWorkloadsSecret" `  




#### `DatabaseFailover`

  * **Method** : `google.cloud.orchestration.airflow.service.v1beta1.Environments.DatabaseFailover`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `composer.environments.update - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.orchestration.airflow.service.v1beta1.Environments.DatabaseFailover" `  




#### `DeleteEnvironment`

  * **Method** : `google.cloud.orchestration.airflow.service.v1beta1.Environments.DeleteEnvironment`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `composer.environments.delete - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.orchestration.airflow.service.v1beta1.Environments.DeleteEnvironment" `  




#### `DeleteUserWorkloadsConfigMap`

  * **Method** : `google.cloud.orchestration.airflow.service.v1beta1.Environments.DeleteUserWorkloadsConfigMap`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `composer.userworkloadsconfigmaps.delete - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.orchestration.airflow.service.v1beta1.Environments.DeleteUserWorkloadsConfigMap" `  




#### `DeleteUserWorkloadsSecret`

  * **Method** : `google.cloud.orchestration.airflow.service.v1beta1.Environments.DeleteUserWorkloadsSecret`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `composer.userworkloadssecrets.delete - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.orchestration.airflow.service.v1beta1.Environments.DeleteUserWorkloadsSecret" `  




#### `ExecuteAirflowCommand`

  * **Method** : `google.cloud.orchestration.airflow.service.v1beta1.Environments.ExecuteAirflowCommand`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `composer.environments.executeAirflowCommand - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.orchestration.airflow.service.v1beta1.Environments.ExecuteAirflowCommand" `  




#### `FetchDatabaseProperties`

  * **Method** : `google.cloud.orchestration.airflow.service.v1beta1.Environments.FetchDatabaseProperties`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `composer.environments.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.orchestration.airflow.service.v1beta1.Environments.FetchDatabaseProperties" `  




#### `GetEnvironment`

  * **Method** : `google.cloud.orchestration.airflow.service.v1beta1.Environments.GetEnvironment`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `composer.environments.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.orchestration.airflow.service.v1beta1.Environments.GetEnvironment" `  




#### `GetUserWorkloadsConfigMap`

  * **Method** : `google.cloud.orchestration.airflow.service.v1beta1.Environments.GetUserWorkloadsConfigMap`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `composer.userworkloadsconfigmaps.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.orchestration.airflow.service.v1beta1.Environments.GetUserWorkloadsConfigMap" `  




#### `GetUserWorkloadsSecret`

  * **Method** : `google.cloud.orchestration.airflow.service.v1beta1.Environments.GetUserWorkloadsSecret`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `composer.userworkloadssecrets.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.orchestration.airflow.service.v1beta1.Environments.GetUserWorkloadsSecret" `  




#### `ListEnvironments`

  * **Method** : `google.cloud.orchestration.airflow.service.v1beta1.Environments.ListEnvironments`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `composer.environments.list - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.orchestration.airflow.service.v1beta1.Environments.ListEnvironments" `  




#### `ListUserWorkloadsConfigMaps`

  * **Method** : `google.cloud.orchestration.airflow.service.v1beta1.Environments.ListUserWorkloadsConfigMaps`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `composer.userworkloadsconfigmaps.list - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.orchestration.airflow.service.v1beta1.Environments.ListUserWorkloadsConfigMaps" `  




#### `ListUserWorkloadsSecrets`

  * **Method** : `google.cloud.orchestration.airflow.service.v1beta1.Environments.ListUserWorkloadsSecrets`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `composer.userworkloadssecrets.list - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.orchestration.airflow.service.v1beta1.Environments.ListUserWorkloadsSecrets" `  




#### `ListWorkloads`

  * **Method** : `google.cloud.orchestration.airflow.service.v1beta1.Environments.ListWorkloads`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `composer.environments.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.orchestration.airflow.service.v1beta1.Environments.ListWorkloads" `  




#### `LoadSnapshot`

  * **Method** : `google.cloud.orchestration.airflow.service.v1beta1.Environments.LoadSnapshot`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `composer.environments.update - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.orchestration.airflow.service.v1beta1.Environments.LoadSnapshot" `  




#### `PollAirflowCommand`

  * **Method** : `google.cloud.orchestration.airflow.service.v1beta1.Environments.PollAirflowCommand`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `composer.environments.executeAirflowCommand - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.orchestration.airflow.service.v1beta1.Environments.PollAirflowCommand" `  




#### `RestartWebServer`

  * **Method** : `google.cloud.orchestration.airflow.service.v1beta1.Environments.RestartWebServer`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `composer.environments.update - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.orchestration.airflow.service.v1beta1.Environments.RestartWebServer" `  




#### `SaveSnapshot`

  * **Method** : `google.cloud.orchestration.airflow.service.v1beta1.Environments.SaveSnapshot`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `composer.environments.update - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.orchestration.airflow.service.v1beta1.Environments.SaveSnapshot" `  




#### `StopAirflowCommand`

  * **Method** : `google.cloud.orchestration.airflow.service.v1beta1.Environments.StopAirflowCommand`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `composer.environments.executeAirflowCommand - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.orchestration.airflow.service.v1beta1.Environments.StopAirflowCommand" `  




#### `UpdateEnvironment`

  * **Method** : `google.cloud.orchestration.airflow.service.v1beta1.Environments.UpdateEnvironment`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `composer.environments.update - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.orchestration.airflow.service.v1beta1.Environments.UpdateEnvironment" `  




#### `UpdateUserWorkloadsConfigMap`

  * **Method** : `google.cloud.orchestration.airflow.service.v1beta1.Environments.UpdateUserWorkloadsConfigMap`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `composer.userworkloadsconfigmaps.update - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.orchestration.airflow.service.v1beta1.Environments.UpdateUserWorkloadsConfigMap" `  




#### `UpdateUserWorkloadsSecret`

  * **Method** : `google.cloud.orchestration.airflow.service.v1beta1.Environments.UpdateUserWorkloadsSecret`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `composer.userworkloadssecrets.update - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.orchestration.airflow.service.v1beta1.Environments.UpdateUserWorkloadsSecret" `  




### `google.cloud.orchestration.airflow.service.v1beta1.ImageVersions`

The following audit logs are associated with methods belonging to `google.cloud.orchestration.airflow.service.v1beta1.ImageVersions`.

#### `ListImageVersions`

  * **Method** : `google.cloud.orchestration.airflow.service.v1beta1.ImageVersions.ListImageVersions`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `composer.imageversions.list - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.orchestration.airflow.service.v1beta1.ImageVersions.ListImageVersions" `  




### `google.longrunning.Operations`

The following audit logs are associated with methods belonging to `google.longrunning.Operations`.

#### `DeleteOperation`

  * **Method** : `google.longrunning.Operations.DeleteOperation`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `composer.operations.delete - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.longrunning.Operations.DeleteOperation" `  




## Methods that don't produce audit logs

A method might not produce audit logs for one or more of the following reasons: 

  * It is a high volume method involving significant log generation and storage costs.
  * It has low auditing value.
  * Another audit or platform log already provides method coverage.



The following methods don't produce audit logs:

  * `google.longrunning.Operations.GetOperation`
  * `google.longrunning.Operations.ListOperations`



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
