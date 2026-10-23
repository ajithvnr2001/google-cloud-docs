---
url: https://docs.cloud.google.com/run/docs/audit-logging/
title: Cloud Run audit logging \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T09:58:20.020183+00:00
---

# Cloud Run audit logging  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/run/docs/audit-logging/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ Cloud Run ](https://docs.cloud.google.com/run/docs)
  * [ Guides ](https://docs.cloud.google.com/run/docs/overview/what-is-cloud-run)



Send feedback 

#  Cloud Run audit logging Stay organized with collections  Save and categorize content based on your preferences. 

This document describes audit logging for Cloud Run. Google Cloud services generate audit logs that record administrative and access activities within your Google Cloud resources. For more information about Cloud Audit Logs, see the following: 

  * [Types of audit logs](https://docs.cloud.google.com/logging/docs/audit#types)
  * [Audit log entry structure](https://docs.cloud.google.com/logging/docs/audit#audit_log_entry_structure)
  * [Storing and routing audit logs](https://docs.cloud.google.com/logging/docs/audit#storing_and_routing_audit_logs)
  * [Cloud Logging pricing summary](https://docs.cloud.google.com/stackdriver/pricing#logs-pricing-summary)
  * [Enable Data Access audit logs](https://docs.cloud.google.com/logging/docs/audit/configure-data-access)



## Service name

Cloud Run audit logs use the service name `run.googleapis.com`. Filter for this service: 
    
    
        protoPayload.serviceName="run.googleapis.com"
      

## Methods by permission type

Each IAM permission has a `type` property, whose value is an enum that can be one of four values: `ADMIN_READ`, `ADMIN_WRITE`, `DATA_READ`, or `DATA_WRITE`. When you call a method, Cloud Run generates an audit log whose category is dependent on the `type` property of the permission required to perform the method. Methods that require an IAM permission with the `type` property value of `DATA_READ`, `DATA_WRITE`, or `ADMIN_READ` generate [Data Access](https://docs.cloud.google.com/logging/docs/audit#data-access) audit logs. Methods that require an IAM permission with the `type` property value of `ADMIN_WRITE` generate [Admin Activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity) audit logs.

API methods in the following list that are marked with (LRO) are long-running operations (LROs). These methods usually generate two audit log entries: one when the operation starts and another when it ends. For more information see [Audit logs for long-running operations](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro). Permission type | Methods  
---|---  
`ADMIN_READ` | `google.cloud.location.Locations.ListLocations`  
`google.cloud.run.v1.AuthorizedDomains.ListAuthorizedDomains`  
`google.cloud.run.v1.Configurations.GetConfiguration`  
`google.cloud.run.v1.Configurations.ListConfigurations`  
`google.cloud.run.v1.DomainMappings.GetDomainMapping`  
`google.cloud.run.v1.DomainMappings.ListDomainMappings`  
`google.cloud.run.v1.Executions.GetExecution`  
`google.cloud.run.v1.Executions.ListExecutions`  
`google.cloud.run.v1.Jobs.GetIamPolicy`  
`google.cloud.run.v1.Jobs.GetJob`  
`google.cloud.run.v1.Jobs.ListJobs`  
`google.cloud.run.v1.Revisions.GetRevision`  
`google.cloud.run.v1.Revisions.ListRevisions`  
`google.cloud.run.v1.Routes.GetRoute`  
`google.cloud.run.v1.Routes.ListRoutes`  
`google.cloud.run.v1.Services.GetIamPolicy`  
`google.cloud.run.v1.Services.GetService`  
`google.cloud.run.v1.Services.ListServices`  
`google.cloud.run.v1.Tasks.GetTask`  
`google.cloud.run.v1.Tasks.ListTasks`  
`google.cloud.run.v2.Executions.GetExecution`  
`google.cloud.run.v2.Executions.ListExecutions`  
`google.cloud.run.v2.ExportServices.ExportImageMetadata`  
`google.cloud.run.v2.ExportServices.ExportProjectMetadata`  
`google.cloud.run.v2.ExportServices.ExportResourceMetadata`  
`google.cloud.run.v2.Jobs.GetIamPolicy`  
`google.cloud.run.v2.Jobs.GetJob`  
`google.cloud.run.v2.Jobs.ListJobs`  
`google.cloud.run.v2.Revisions.GetRevision`  
`google.cloud.run.v2.Revisions.ListRevisions`  
`google.cloud.run.v2.Services.GetIamPolicy`  
`google.cloud.run.v2.Services.GetService`  
`google.cloud.run.v2.Services.ListServices`  
`google.cloud.run.v2.Tasks.GetTask`  
`google.cloud.run.v2.Tasks.ListTasks`  
`google.cloud.run.v2.WorkerPools.GetWorkerPool`  
`google.cloud.run.v2.WorkerPools.ListWorkerPools`  
`google.longrunning.Operations.GetOperation`  
`google.longrunning.Operations.ListOperations`  
`google.longrunning.Operations.WaitOperation`  
`ADMIN_WRITE` | `google.cloud.run.v1.DomainMappings.CreateDomainMapping`  
`google.cloud.run.v1.DomainMappings.DeleteDomainMapping`  
`google.cloud.run.v1.Executions.CancelExecution`  
`google.cloud.run.v1.Executions.DeleteExecution`  
`google.cloud.run.v1.Jobs.CreateJob`  
`google.cloud.run.v1.Jobs.DeleteJob`  
`google.cloud.run.v1.Jobs.ReplaceJob`  
`google.cloud.run.v1.Jobs.SetIamPolicy`  
`google.cloud.run.v1.Revisions.DeleteRevision`  
`google.cloud.run.v1.Services.CreateService`  
`google.cloud.run.v1.Services.DeleteService`  
`google.cloud.run.v1.Services.ReplaceService`  
`google.cloud.run.v1.Services.SetIamPolicy`  
`google.cloud.run.v2.Builds.SubmitBuild`  
`google.cloud.run.v2.Executions.CancelExecution`  
`google.cloud.run.v2.Executions.DeleteExecution`  
`google.cloud.run.v2.Jobs.CreateJob`  
`google.cloud.run.v2.Jobs.DeleteJob`  
`google.cloud.run.v2.Jobs.SetIamPolicy`  
`google.cloud.run.v2.Jobs.UpdateJob`  
`google.cloud.run.v2.Revisions.DeleteRevision`  
`google.cloud.run.v2.Services.CreateService`  
`google.cloud.run.v2.Services.DeleteService`  
`google.cloud.run.v2.Services.SetIamPolicy`  
`google.cloud.run.v2.Services.UpdateService`  
`google.cloud.run.v2.WorkerPools.CreateWorkerPool`  
`google.cloud.run.v2.WorkerPools.DeleteWorkerPool`  
`google.cloud.run.v2.WorkerPools.UpdateWorkerPool`  
`google.longrunning.Operations.DeleteOperation`  
`DATA_READ` | `google.cloud.run.v2.ExportServices.ExportImage`  
`google.cloud.run.v2.ExportServices.ExportStatus`  
`DATA_WRITE` | `google.cloud.run.v1.Jobs.RunJob`  
`google.cloud.run.v2.Jobs.RunJob`  
  
## API interface audit logs

For information about how and which permissions are evaluated for each method, see the Identity and Access Management documentation for Cloud Run.

### `google.cloud.location.Locations`

The following audit logs are associated with methods belonging to `google.cloud.location.Locations`.

#### `ListLocations`

  * **Method** : `google.cloud.location.Locations.ListLocations`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `run.locations.list - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.location.Locations.ListLocations" `  




### `google.cloud.run.v1.AuthorizedDomains`

The following audit logs are associated with methods belonging to `google.cloud.run.v1.AuthorizedDomains`.

#### `ListAuthorizedDomains`

  * **Method** : `google.cloud.run.v1.AuthorizedDomains.ListAuthorizedDomains`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `run.authorizeddomains.list - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.run.v1.AuthorizedDomains.ListAuthorizedDomains" `  




### `google.cloud.run.v1.Configurations`

The following audit logs are associated with methods belonging to `google.cloud.run.v1.Configurations`.

#### `GetConfiguration`

  * **Method** : `google.cloud.run.v1.Configurations.GetConfiguration`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `run.configurations.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.run.v1.Configurations.GetConfiguration" `  




#### `ListConfigurations`

  * **Method** : `google.cloud.run.v1.Configurations.ListConfigurations`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `run.configurations.list - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.run.v1.Configurations.ListConfigurations" `  




### `google.cloud.run.v1.DomainMappings`

The following audit logs are associated with methods belonging to `google.cloud.run.v1.DomainMappings`.

#### `CreateDomainMapping`

  * **Method** : `google.cloud.run.v1.DomainMappings.CreateDomainMapping`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `run.domainmappings.create - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.run.v1.DomainMappings.CreateDomainMapping" `  




#### `DeleteDomainMapping`

  * **Method** : `google.cloud.run.v1.DomainMappings.DeleteDomainMapping`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `run.domainmappings.delete - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.run.v1.DomainMappings.DeleteDomainMapping" `  




#### `GetDomainMapping`

  * **Method** : `google.cloud.run.v1.DomainMappings.GetDomainMapping`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `run.domainmappings.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.run.v1.DomainMappings.GetDomainMapping" `  




#### `ListDomainMappings`

  * **Method** : `google.cloud.run.v1.DomainMappings.ListDomainMappings`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `run.domainmappings.list - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.run.v1.DomainMappings.ListDomainMappings" `  




### `google.cloud.run.v1.Executions`

The following audit logs are associated with methods belonging to `google.cloud.run.v1.Executions`.

#### `CancelExecution`

  * **Method** : `google.cloud.run.v1.Executions.CancelExecution`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `run.executions.cancel - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.run.v1.Executions.CancelExecution" `  




#### `DeleteExecution`

  * **Method** : `google.cloud.run.v1.Executions.DeleteExecution`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `run.executions.delete - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.run.v1.Executions.DeleteExecution" `  




#### `GetExecution`

  * **Method** : `google.cloud.run.v1.Executions.GetExecution`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `run.executions.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.run.v1.Executions.GetExecution" `  




#### `ListExecutions`

  * **Method** : `google.cloud.run.v1.Executions.ListExecutions`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `run.executions.list - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.run.v1.Executions.ListExecutions" `  




### `google.cloud.run.v1.Jobs`

The following audit logs are associated with methods belonging to `google.cloud.run.v1.Jobs`.

#### `CreateJob`

  * **Method** : `google.cloud.run.v1.Jobs.CreateJob`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `run.jobs.create - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.run.v1.Jobs.CreateJob" `  




#### `DeleteJob`

  * **Method** : `google.cloud.run.v1.Jobs.DeleteJob`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `run.jobs.delete - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.run.v1.Jobs.DeleteJob" `  




#### `GetIamPolicy`

  * **Method** : `google.cloud.run.v1.Jobs.GetIamPolicy`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `run.jobs.getIamPolicy - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.run.v1.Jobs.GetIamPolicy" `  




#### `GetJob`

  * **Method** : `google.cloud.run.v1.Jobs.GetJob`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `run.jobs.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.run.v1.Jobs.GetJob" `  




#### `ListJobs`

  * **Method** : `google.cloud.run.v1.Jobs.ListJobs`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `run.jobs.list - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.run.v1.Jobs.ListJobs" `  




#### `ReplaceJob`

  * **Method** : `google.cloud.run.v1.Jobs.ReplaceJob`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `run.jobs.update - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.run.v1.Jobs.ReplaceJob" `  




#### `RunJob`

  * **Method** : `google.cloud.run.v1.Jobs.RunJob`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `run.jobs.run - DATA_WRITE`
    * `run.jobs.runWithOverrides - DATA_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.run.v1.Jobs.RunJob" `  




#### `SetIamPolicy`

  * **Method** : `google.cloud.run.v1.Jobs.SetIamPolicy`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `run.jobs.setIamPolicy - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.run.v1.Jobs.SetIamPolicy" `  




### `google.cloud.run.v1.Revisions`

The following audit logs are associated with methods belonging to `google.cloud.run.v1.Revisions`.

#### `DeleteRevision`

  * **Method** : `google.cloud.run.v1.Revisions.DeleteRevision`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `run.revisions.delete - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.run.v1.Revisions.DeleteRevision" `  




#### `GetRevision`

  * **Method** : `google.cloud.run.v1.Revisions.GetRevision`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `run.revisions.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.run.v1.Revisions.GetRevision" `  




#### `ListRevisions`

  * **Method** : `google.cloud.run.v1.Revisions.ListRevisions`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `run.revisions.list - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.run.v1.Revisions.ListRevisions" `  




### `google.cloud.run.v1.Routes`

The following audit logs are associated with methods belonging to `google.cloud.run.v1.Routes`.

#### `GetRoute`

  * **Method** : `google.cloud.run.v1.Routes.GetRoute`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `run.routes.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.run.v1.Routes.GetRoute" `  




#### `ListRoutes`

  * **Method** : `google.cloud.run.v1.Routes.ListRoutes`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `run.routes.list - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.run.v1.Routes.ListRoutes" `  




### `google.cloud.run.v1.Services`

The following audit logs are associated with methods belonging to `google.cloud.run.v1.Services`.

#### `CreateService`

  * **Method** : `google.cloud.run.v1.Services.CreateService`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `run.services.create - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.run.v1.Services.CreateService" `  




#### `DeleteService`

  * **Method** : `google.cloud.run.v1.Services.DeleteService`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `run.operations.get - ADMIN_READ`
    * `run.services.delete - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.run.v1.Services.DeleteService" `  




#### `GetIamPolicy`

  * **Method** : `google.cloud.run.v1.Services.GetIamPolicy`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `run.services.getIamPolicy - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.run.v1.Services.GetIamPolicy" `  




#### `GetService`

  * **Method** : `google.cloud.run.v1.Services.GetService`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `run.services.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.run.v1.Services.GetService" `  




#### `ListServices`

  * **Method** : `google.cloud.run.v1.Services.ListServices`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `run.services.list - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.run.v1.Services.ListServices" `  




#### `ReplaceService`

  * **Method** : `google.cloud.run.v1.Services.ReplaceService`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `run.operations.get - ADMIN_READ`
    * `run.services.update - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.run.v1.Services.ReplaceService" `  




#### `SetIamPolicy`

  * **Method** : `google.cloud.run.v1.Services.SetIamPolicy`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `run.services.setIamPolicy - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.run.v1.Services.SetIamPolicy" `  




### `google.cloud.run.v1.Tasks`

The following audit logs are associated with methods belonging to `google.cloud.run.v1.Tasks`.

#### `GetTask`

  * **Method** : `google.cloud.run.v1.Tasks.GetTask`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `run.tasks.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.run.v1.Tasks.GetTask" `  




#### `ListTasks`

  * **Method** : `google.cloud.run.v1.Tasks.ListTasks`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `run.tasks.list - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.run.v1.Tasks.ListTasks" `  




### `google.cloud.run.v2.Builds`

The following audit logs are associated with methods belonging to `google.cloud.run.v2.Builds`.

#### `SubmitBuild`

  * **Method** : `google.cloud.run.v2.Builds.SubmitBuild`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `cloudbuild.builds.create - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.run.v2.Builds.SubmitBuild" `  




### `google.cloud.run.v2.Executions`

The following audit logs are associated with methods belonging to `google.cloud.run.v2.Executions`.

#### `CancelExecution`

  * **Method** : `google.cloud.run.v2.Executions.CancelExecution`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `run.executions.cancel - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.run.v2.Executions.CancelExecution" `  




#### `DeleteExecution`

  * **Method** : `google.cloud.run.v2.Executions.DeleteExecution`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `run.executions.delete - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.run.v2.Executions.DeleteExecution" `  




#### `GetExecution`

  * **Method** : `google.cloud.run.v2.Executions.GetExecution`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `run.executions.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.run.v2.Executions.GetExecution" `  




#### `ListExecutions`

  * **Method** : `google.cloud.run.v2.Executions.ListExecutions`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `run.executions.list - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.run.v2.Executions.ListExecutions" `  




### `google.cloud.run.v2.ExportServices`

The following audit logs are associated with methods belonging to `google.cloud.run.v2.ExportServices`.

#### `ExportImage`

  * **Method** : `google.cloud.run.v2.ExportServices.ExportImage`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `run.locations.exportImage - DATA_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.run.v2.ExportServices.ExportImage" `  




#### `ExportImageMetadata`

  * **Method** : `google.cloud.run.v2.ExportServices.ExportImageMetadata`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `run.locations.exportMetadata - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.run.v2.ExportServices.ExportImageMetadata" `  




#### `ExportProjectMetadata`

  * **Method** : `google.cloud.run.v2.ExportServices.ExportProjectMetadata`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `run.locations.exportMetadata - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.run.v2.ExportServices.ExportProjectMetadata" `  




#### `ExportResourceMetadata`

  * **Method** : `google.cloud.run.v2.ExportServices.ExportResourceMetadata`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `run.locations.exportMetadata - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.run.v2.ExportServices.ExportResourceMetadata" `  




#### `ExportStatus`

  * **Method** : `google.cloud.run.v2.ExportServices.ExportStatus`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `run.locations.exportImage - DATA_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.run.v2.ExportServices.ExportStatus" `  




### `google.cloud.run.v2.Jobs`

The following audit logs are associated with methods belonging to `google.cloud.run.v2.Jobs`.

#### `CreateJob`

  * **Method** : `google.cloud.run.v2.Jobs.CreateJob`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `run.jobs.create - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.run.v2.Jobs.CreateJob" `  




#### `DeleteJob`

  * **Method** : `google.cloud.run.v2.Jobs.DeleteJob`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `run.jobs.delete - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.run.v2.Jobs.DeleteJob" `  




#### `GetIamPolicy`

  * **Method** : `google.cloud.run.v2.Jobs.GetIamPolicy`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `run.jobs.getIamPolicy - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.run.v2.Jobs.GetIamPolicy" `  




#### `GetJob`

  * **Method** : `google.cloud.run.v2.Jobs.GetJob`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `run.jobs.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.run.v2.Jobs.GetJob" `  




#### `ListJobs`

  * **Method** : `google.cloud.run.v2.Jobs.ListJobs`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `run.jobs.list - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.run.v2.Jobs.ListJobs" `  




#### `RunJob`

  * **Method** : `google.cloud.run.v2.Jobs.RunJob`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `run.jobs.run - DATA_WRITE`
    * `run.jobs.runWithOverrides - DATA_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.run.v2.Jobs.RunJob" `  




#### `SetIamPolicy`

  * **Method** : `google.cloud.run.v2.Jobs.SetIamPolicy`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `run.jobs.setIamPolicy - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.run.v2.Jobs.SetIamPolicy" `  




#### `UpdateJob`

  * **Method** : `google.cloud.run.v2.Jobs.UpdateJob`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `run.jobs.update - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.run.v2.Jobs.UpdateJob" `  




### `google.cloud.run.v2.Revisions`

The following audit logs are associated with methods belonging to `google.cloud.run.v2.Revisions`.

#### `DeleteRevision`

  * **Method** : `google.cloud.run.v2.Revisions.DeleteRevision`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `run.revisions.delete - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.run.v2.Revisions.DeleteRevision" `  




#### `GetRevision`

  * **Method** : `google.cloud.run.v2.Revisions.GetRevision`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `run.revisions.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.run.v2.Revisions.GetRevision" `  




#### `ListRevisions`

  * **Method** : `google.cloud.run.v2.Revisions.ListRevisions`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `run.revisions.list - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.run.v2.Revisions.ListRevisions" `  




### `google.cloud.run.v2.Services`

The following audit logs are associated with methods belonging to `google.cloud.run.v2.Services`.

#### `CreateService`

  * **Method** : `google.cloud.run.v2.Services.CreateService`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `run.services.create - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.run.v2.Services.CreateService" `  




#### `DeleteService`

  * **Method** : `google.cloud.run.v2.Services.DeleteService`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `run.services.delete - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.run.v2.Services.DeleteService" `  




#### `GetIamPolicy`

  * **Method** : `google.cloud.run.v2.Services.GetIamPolicy`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `run.services.getIamPolicy - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.run.v2.Services.GetIamPolicy" `  




#### `GetService`

  * **Method** : `google.cloud.run.v2.Services.GetService`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `run.services.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.run.v2.Services.GetService" `  




#### `ListServices`

  * **Method** : `google.cloud.run.v2.Services.ListServices`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `run.services.list - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.run.v2.Services.ListServices" `  




#### `SetIamPolicy`

  * **Method** : `google.cloud.run.v2.Services.SetIamPolicy`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `run.services.setIamPolicy - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.run.v2.Services.SetIamPolicy" `  




#### `UpdateService`

  * **Method** : `google.cloud.run.v2.Services.UpdateService`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `run.services.update - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.run.v2.Services.UpdateService" `  




### `google.cloud.run.v2.Tasks`

The following audit logs are associated with methods belonging to `google.cloud.run.v2.Tasks`.

#### `GetTask`

  * **Method** : `google.cloud.run.v2.Tasks.GetTask`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `run.tasks.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.run.v2.Tasks.GetTask" `  




#### `ListTasks`

  * **Method** : `google.cloud.run.v2.Tasks.ListTasks`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `run.tasks.list - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.run.v2.Tasks.ListTasks" `  




### `google.cloud.run.v2.WorkerPools`

The following audit logs are associated with methods belonging to `google.cloud.run.v2.WorkerPools`.

#### `CreateWorkerPool`

  * **Method** : `google.cloud.run.v2.WorkerPools.CreateWorkerPool`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `run.workerpools.create - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.run.v2.WorkerPools.CreateWorkerPool" `  




#### `DeleteWorkerPool`

  * **Method** : `google.cloud.run.v2.WorkerPools.DeleteWorkerPool`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `run.workerpools.delete - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.run.v2.WorkerPools.DeleteWorkerPool" `  




#### `GetWorkerPool`

  * **Method** : `google.cloud.run.v2.WorkerPools.GetWorkerPool`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `run.workerpools.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.run.v2.WorkerPools.GetWorkerPool" `  




#### `ListWorkerPools`

  * **Method** : `google.cloud.run.v2.WorkerPools.ListWorkerPools`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `run.workerpools.list - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.run.v2.WorkerPools.ListWorkerPools" `  




#### `UpdateWorkerPool`

  * **Method** : `google.cloud.run.v2.WorkerPools.UpdateWorkerPool`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `run.workerpools.update - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.run.v2.WorkerPools.UpdateWorkerPool" `  




### `google.longrunning.Operations`

The following audit logs are associated with methods belonging to `google.longrunning.Operations`.

#### `DeleteOperation`

  * **Method** : `google.longrunning.Operations.DeleteOperation`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `run.operations.delete - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.longrunning.Operations.DeleteOperation" `  




#### `GetOperation`

  * **Method** : `google.longrunning.Operations.GetOperation`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `run.operations.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.longrunning.Operations.GetOperation" `  




#### `ListOperations`

  * **Method** : `google.longrunning.Operations.ListOperations`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `run.operations.list - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.longrunning.Operations.ListOperations" `  




#### `WaitOperation`

  * **Method** : `google.longrunning.Operations.WaitOperation`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `run.operations.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.longrunning.Operations.WaitOperation" `  




## System events

System Event audit logs are generated by GCP systems, not direct user action. For more information, see [System Event audit logs](https://docs.cloud.google.com/logging/docs/audit#system-event).

Method Name | Filter For This Event | Notes  
---|---|---  
/DomainMappings.CreateDomainMapping |  ` protoPayload.methodName="/DomainMappings.CreateDomainMapping" ` |   
/DomainMappings.DeleteDomainMapping |  ` protoPayload.methodName="/DomainMappings.DeleteDomainMapping" ` |   
/Executions.CancelExecution |  ` protoPayload.methodName="/Executions.CancelExecution" ` |   
/Executions.DeleteExecution |  ` protoPayload.methodName="/Executions.DeleteExecution" ` |   
/InternalServices.CreateInternalService |  ` protoPayload.methodName="/InternalServices.CreateInternalService" ` |   
/InternalServices.DeleteInternalService |  ` protoPayload.methodName="/InternalServices.DeleteInternalService" ` |   
/InternalServices.ReplaceInternalService |  ` protoPayload.methodName="/InternalServices.ReplaceInternalService" ` |   
/Jobs.CreateJob |  ` protoPayload.methodName="/Jobs.CreateJob" ` |   
/Jobs.DeleteJob |  ` protoPayload.methodName="/Jobs.DeleteJob" ` |   
/Jobs.ReplaceJob |  ` protoPayload.methodName="/Jobs.ReplaceJob" ` |   
/Jobs.RunJob |  ` protoPayload.methodName="/Jobs.RunJob" ` |   
/Jobs.UpdateJob |  ` protoPayload.methodName="/Jobs.UpdateJob" ` |   
/ProjectConfigs.DeleteProjectConfig |  ` protoPayload.methodName="/ProjectConfigs.DeleteProjectConfig" ` |   
/Revisions.DeleteRevision |  ` protoPayload.methodName="/Revisions.DeleteRevision" ` |   
/Services.CreateService |  ` protoPayload.methodName="/Services.CreateService" ` |   
/Services.DeleteService |  ` protoPayload.methodName="/Services.DeleteService" ` |   
/Services.ReplaceService |  ` protoPayload.methodName="/Services.ReplaceService" ` |   
/Services.UpdateService |  ` protoPayload.methodName="/Services.UpdateService" ` |   
/WorkerPools.CreateWorkerPool |  ` protoPayload.methodName="/WorkerPools.CreateWorkerPool" ` |   
/WorkerPools.DeleteWorkerPool |  ` protoPayload.methodName="/WorkerPools.DeleteWorkerPool" ` |   
/WorkerPools.UpdateWorkerPool |  ` protoPayload.methodName="/WorkerPools.UpdateWorkerPool" ` |   
  
## Methods that don't produce audit logs

A method might not produce audit logs for one or more of the following reasons: 

  * It is a high volume method involving significant log generation and storage costs.
  * It has low auditing value.
  * Another audit or platform log already provides method coverage.



The following methods don't produce audit logs:

  * `google.cloud.run.v1.Jobs.TestIamPermissions`
  * `google.cloud.run.v1.Services.TestIamPermissions`
  * `google.cloud.run.v2.Jobs.TestIamPermissions`
  * `google.cloud.run.v2.Services.TestIamPermissions`
  * `google.cloud.run.v2.WorkerPools.TestIamPermissions`



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
