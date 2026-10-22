---
url: https://docs.cloud.google.com/managed-microsoft-ad/docs/audit-logging/
title: Managed Microsoft AD audit logging \u00a0|\u00a0 Managed Service for Microsoft Active Directory \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T15:31:09.073682+00:00
---

# Managed Microsoft AD audit logging  |  Managed Service for Microsoft Active Directory  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/managed-microsoft-ad/docs/audit-logging/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Access and resource management ](https://docs.cloud.google.com/docs/access-resources)
  * [ Managed Microsoft AD ](https://docs.cloud.google.com/managed-microsoft-ad/docs)
  * [ Guides ](https://docs.cloud.google.com/managed-microsoft-ad/docs/overview)



Send feedback 

#  Managed Microsoft AD audit logging Stay organized with collections  Save and categorize content based on your preferences. 

This document describes audit logging for Managed Service for Microsoft Active Directory. Google Cloud services generate audit logs that record administrative and access activities within your Google Cloud resources. For more information about Cloud Audit Logs, see the following: 

  * [Types of audit logs](https://docs.cloud.google.com/logging/docs/audit#types)
  * [Audit log entry structure](https://docs.cloud.google.com/logging/docs/audit#audit_log_entry_structure)
  * [Storing and routing audit logs](https://docs.cloud.google.com/logging/docs/audit#storing_and_routing_audit_logs)
  * [Cloud Logging pricing summary](https://docs.cloud.google.com/stackdriver/pricing#logs-pricing-summary)
  * [Enable Data Access audit logs](https://docs.cloud.google.com/logging/docs/audit/configure-data-access)



## Service name

Managed Service for Microsoft Active Directory audit logs use the service name `managedidentities.googleapis.com`. Filter for this service: 
    
    
        protoPayload.serviceName="managedidentities.googleapis.com"
      

## Methods by permission type

Each IAM permission has a `type` property, whose value is an enum that can be one of four values: `ADMIN_READ`, `ADMIN_WRITE`, `DATA_READ`, or `DATA_WRITE`. When you call a method, Managed Service for Microsoft Active Directory generates an audit log whose category is dependent on the `type` property of the permission required to perform the method. Methods that require an IAM permission with the `type` property value of `DATA_READ`, `DATA_WRITE`, or `ADMIN_READ` generate [Data Access](https://docs.cloud.google.com/logging/docs/audit#data-access) audit logs. Methods that require an IAM permission with the `type` property value of `ADMIN_WRITE` generate [Admin Activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity) audit logs.

API methods in the following list that are marked with (LRO) are long-running operations (LROs). These methods usually generate two audit log entries: one when the operation starts and another when it ends. For more information see [Audit logs for long-running operations](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro). Permission type | Methods  
---|---  
`ADMIN_READ` | `google.cloud.managedidentities.v1.ManagedIdentitiesService.CheckMigrationPermission`  
`google.cloud.managedidentities.v1.ManagedIdentitiesService.GetDomain`  
`google.cloud.managedidentities.v1.ManagedIdentitiesService.GetLDAPSSettings`  
`google.cloud.managedidentities.v1.ManagedIdentitiesService.GetPeering`  
`google.cloud.managedidentities.v1.ManagedIdentitiesService.GetSqlIntegration`  
`google.cloud.managedidentities.v1.ManagedIdentitiesService.ListDomains`  
`google.cloud.managedidentities.v1.ManagedIdentitiesService.ListPeerings`  
`google.cloud.managedidentities.v1.ManagedIdentitiesService.ListSqlIntegrations`  
`google.cloud.managedidentities.v1.ManagedIdentitiesService.ValidateTrust` (LRO)  
`google.cloud.managedidentities.v1alpha1.ManagedIdentitiesService.CheckMigrationPermission`  
`google.cloud.managedidentities.v1alpha1.ManagedIdentitiesService.GetDomain`  
`google.cloud.managedidentities.v1alpha1.ManagedIdentitiesService.GetLDAPSSettings`  
`google.cloud.managedidentities.v1alpha1.ManagedIdentitiesService.GetPeering`  
`google.cloud.managedidentities.v1alpha1.ManagedIdentitiesService.GetSQLIntegration`  
`google.cloud.managedidentities.v1alpha1.ManagedIdentitiesService.ListDomains`  
`google.cloud.managedidentities.v1alpha1.ManagedIdentitiesService.ListPeerings`  
`google.cloud.managedidentities.v1alpha1.ManagedIdentitiesService.ListSQLIntegrations`  
`google.cloud.managedidentities.v1alpha1.ManagedIdentitiesService.ValidateTrust`  
`google.cloud.managedidentities.v1beta1.ManagedIdentitiesService.CheckMigrationPermission`  
`google.cloud.managedidentities.v1beta1.ManagedIdentitiesService.GetDomain`  
`google.cloud.managedidentities.v1beta1.ManagedIdentitiesService.GetLDAPSSettings`  
`google.cloud.managedidentities.v1beta1.ManagedIdentitiesService.GetPeering`  
`google.cloud.managedidentities.v1beta1.ManagedIdentitiesService.GetSqlIntegration`  
`google.cloud.managedidentities.v1beta1.ManagedIdentitiesService.ListDomains`  
`google.cloud.managedidentities.v1beta1.ManagedIdentitiesService.ListPeerings`  
`google.cloud.managedidentities.v1beta1.ManagedIdentitiesService.ListSqlIntegrations`  
`google.cloud.managedidentities.v1beta1.ManagedIdentitiesService.ValidateTrust`  
`google.cloud.managedidentities.v1internal1.ManagedIdentitiesService.GetInternalIntegratedNetwork`  
`GetIamPolicy`  
`google.longrunning.Operations.GetOperation`  
`google.longrunning.Operations.ListOperations`  
`ADMIN_WRITE` | `google.cloud.managedidentities.v1.ManagedIdentitiesService.AttachTrust` (LRO)  
`google.cloud.managedidentities.v1.ManagedIdentitiesService.CreateBackup` (LRO)  
`google.cloud.managedidentities.v1.ManagedIdentitiesService.CreateMicrosoftAdDomain` (LRO)  
`google.cloud.managedidentities.v1.ManagedIdentitiesService.CreatePeering` (LRO)  
`google.cloud.managedidentities.v1.ManagedIdentitiesService.DeleteBackup` (LRO)  
`google.cloud.managedidentities.v1.ManagedIdentitiesService.DeleteDomain` (LRO)  
`google.cloud.managedidentities.v1.ManagedIdentitiesService.DeletePeering` (LRO)  
`google.cloud.managedidentities.v1.ManagedIdentitiesService.DetachTrust` (LRO)  
`google.cloud.managedidentities.v1.ManagedIdentitiesService.DisableMigration`  
`google.cloud.managedidentities.v1.ManagedIdentitiesService.DomainJoinMachine`  
`google.cloud.managedidentities.v1.ManagedIdentitiesService.EnableMigration`  
`google.cloud.managedidentities.v1.ManagedIdentitiesService.ExtendSchema` (LRO)  
`google.cloud.managedidentities.v1.ManagedIdentitiesService.ReconfigureTrust` (LRO)  
`google.cloud.managedidentities.v1.ManagedIdentitiesService.ResetAdminPassword`  
`google.cloud.managedidentities.v1.ManagedIdentitiesService.RestoreDomain`  
`google.cloud.managedidentities.v1.ManagedIdentitiesService.UpdateBackup` (LRO)  
`google.cloud.managedidentities.v1.ManagedIdentitiesService.UpdateDomain` (LRO)  
`google.cloud.managedidentities.v1.ManagedIdentitiesService.UpdateLDAPSSettings` (LRO)  
`google.cloud.managedidentities.v1.ManagedIdentitiesService.UpdatePeering` (LRO)  
`google.cloud.managedidentities.v1alpha1.ManagedIdentitiesService.AttachTrust`  
`google.cloud.managedidentities.v1alpha1.ManagedIdentitiesService.CreateBackup` (LRO)  
`google.cloud.managedidentities.v1alpha1.ManagedIdentitiesService.CreateMicrosoftAdDomain` (LRO)  
`google.cloud.managedidentities.v1alpha1.ManagedIdentitiesService.CreatePeering`  
`google.cloud.managedidentities.v1alpha1.ManagedIdentitiesService.DeleteBackup`  
`google.cloud.managedidentities.v1alpha1.ManagedIdentitiesService.DeleteDomain` (LRO)  
`google.cloud.managedidentities.v1alpha1.ManagedIdentitiesService.DeletePeering`  
`google.cloud.managedidentities.v1alpha1.ManagedIdentitiesService.DetachTrust`  
`google.cloud.managedidentities.v1alpha1.ManagedIdentitiesService.DisableMigration`  
`google.cloud.managedidentities.v1alpha1.ManagedIdentitiesService.DomainJoinMachine`  
`google.cloud.managedidentities.v1alpha1.ManagedIdentitiesService.EnableMigration`  
`google.cloud.managedidentities.v1alpha1.ManagedIdentitiesService.ExtendSchema`  
`google.cloud.managedidentities.v1alpha1.ManagedIdentitiesService.ReconfigureTrust`  
`google.cloud.managedidentities.v1alpha1.ManagedIdentitiesService.ResetAdminPassword`  
`google.cloud.managedidentities.v1alpha1.ManagedIdentitiesService.RestoreDomain` (LRO)  
`google.cloud.managedidentities.v1alpha1.ManagedIdentitiesService.UpdateBackup`  
`google.cloud.managedidentities.v1alpha1.ManagedIdentitiesService.UpdateDomain` (LRO)  
`google.cloud.managedidentities.v1alpha1.ManagedIdentitiesService.UpdateLDAPSSettings`  
`google.cloud.managedidentities.v1alpha1.ManagedIdentitiesService.UpdatePeering`  
`google.cloud.managedidentities.v1beta1.ManagedIdentitiesService.AttachTrust` (LRO)  
`google.cloud.managedidentities.v1beta1.ManagedIdentitiesService.CreateBackup`  
`google.cloud.managedidentities.v1beta1.ManagedIdentitiesService.CreateMicrosoftAdDomain` (LRO)  
`google.cloud.managedidentities.v1beta1.ManagedIdentitiesService.CreatePeering` (LRO)  
`google.cloud.managedidentities.v1beta1.ManagedIdentitiesService.DeleteBackup`  
`google.cloud.managedidentities.v1beta1.ManagedIdentitiesService.DeleteDomain` (LRO)  
`google.cloud.managedidentities.v1beta1.ManagedIdentitiesService.DeletePeering` (LRO)  
`google.cloud.managedidentities.v1beta1.ManagedIdentitiesService.DetachTrust` (LRO)  
`google.cloud.managedidentities.v1beta1.ManagedIdentitiesService.DisableMigration`  
`google.cloud.managedidentities.v1beta1.ManagedIdentitiesService.DomainJoinMachine`  
`google.cloud.managedidentities.v1beta1.ManagedIdentitiesService.EnableMigration`  
`google.cloud.managedidentities.v1beta1.ManagedIdentitiesService.ExtendSchema`  
`google.cloud.managedidentities.v1beta1.ManagedIdentitiesService.ReconfigureTrust`  
`google.cloud.managedidentities.v1beta1.ManagedIdentitiesService.ResetAdminPassword`  
`google.cloud.managedidentities.v1beta1.ManagedIdentitiesService.RestoreDomain`  
`google.cloud.managedidentities.v1beta1.ManagedIdentitiesService.UpdateBackup`  
`google.cloud.managedidentities.v1beta1.ManagedIdentitiesService.UpdateDomain` (LRO)  
`google.cloud.managedidentities.v1beta1.ManagedIdentitiesService.UpdateLDAPSSettings` (LRO)  
`google.cloud.managedidentities.v1beta1.ManagedIdentitiesService.UpdatePeering`  
`google.cloud.managedidentities.v1internal1.ManagedIdentitiesService.CreateInternalIntegratedNetwork` (LRO)  
`google.cloud.managedidentities.v1internal1.ManagedIdentitiesService.CreateInternalSQLIntegration` (LRO)  
`google.cloud.managedidentities.v1internal1.ManagedIdentitiesService.DeleteInternalIntegratedNetwork` (LRO)  
`google.cloud.managedidentities.v1internal1.ManagedIdentitiesService.DeleteInternalSQLIntegration` (LRO)  
`google.cloud.managedidentities.v1internal1.ManagedIdentitiesService.ResetInternalSQLPassword`  
`SetIamPolicy`  
`google.longrunning.Operations.CancelOperation`  
`google.longrunning.Operations.DeleteOperation`  
  
## API interface audit logs

For information about how and which permissions are evaluated for each method, see the Identity and Access Management documentation for Managed Service for Microsoft Active Directory.

### `google.cloud.managedidentities.v1.ManagedIdentitiesService`

The following audit logs are associated with methods belonging to `google.cloud.managedidentities.v1.ManagedIdentitiesService`.

#### `AttachTrust`

  * **Method** : `google.cloud.managedidentities.v1.ManagedIdentitiesService.AttachTrust`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `managedidentities.domains.attachTrust - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.managedidentities.v1.ManagedIdentitiesService.AttachTrust" `  




#### `CheckMigrationPermission`

  * **Method** : `google.cloud.managedidentities.v1.ManagedIdentitiesService.CheckMigrationPermission`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `managedidentities.domains.checkMigrationPermission - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.managedidentities.v1.ManagedIdentitiesService.CheckMigrationPermission" `  




#### `CreateBackup`

  * **Method** : `google.cloud.managedidentities.v1.ManagedIdentitiesService.CreateBackup`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `managedidentities.backups.create - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.managedidentities.v1.ManagedIdentitiesService.CreateBackup" `  




#### `CreateMicrosoftAdDomain`

  * **Method** : `google.cloud.managedidentities.v1.ManagedIdentitiesService.CreateMicrosoftAdDomain`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `managedidentities.domains.create - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.managedidentities.v1.ManagedIdentitiesService.CreateMicrosoftAdDomain" `  




#### `CreatePeering`

  * **Method** : `google.cloud.managedidentities.v1.ManagedIdentitiesService.CreatePeering`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `managedidentities.peerings.create - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.managedidentities.v1.ManagedIdentitiesService.CreatePeering" `  




#### `DeleteBackup`

  * **Method** : `google.cloud.managedidentities.v1.ManagedIdentitiesService.DeleteBackup`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `managedidentities.backups.delete - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.managedidentities.v1.ManagedIdentitiesService.DeleteBackup" `  




#### `DeleteDomain`

  * **Method** : `google.cloud.managedidentities.v1.ManagedIdentitiesService.DeleteDomain`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `managedidentities.domains.delete - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.managedidentities.v1.ManagedIdentitiesService.DeleteDomain" `  




#### `DeletePeering`

  * **Method** : `google.cloud.managedidentities.v1.ManagedIdentitiesService.DeletePeering`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `managedidentities.peerings.delete - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.managedidentities.v1.ManagedIdentitiesService.DeletePeering" `  




#### `DetachTrust`

  * **Method** : `google.cloud.managedidentities.v1.ManagedIdentitiesService.DetachTrust`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `managedidentities.domains.detachTrust - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.managedidentities.v1.ManagedIdentitiesService.DetachTrust" `  




#### `DisableMigration`

  * **Method** : `google.cloud.managedidentities.v1.ManagedIdentitiesService.DisableMigration`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `managedidentities.domains.disableMigration - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.managedidentities.v1.ManagedIdentitiesService.DisableMigration" `  




#### `DomainJoinMachine`

  * **Method** : `google.cloud.managedidentities.v1.ManagedIdentitiesService.DomainJoinMachine`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `managedidentities.domains.domainJoinMachine - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.managedidentities.v1.ManagedIdentitiesService.DomainJoinMachine" `  




#### `EnableMigration`

  * **Method** : `google.cloud.managedidentities.v1.ManagedIdentitiesService.EnableMigration`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `managedidentities.domains.enableMigration - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.managedidentities.v1.ManagedIdentitiesService.EnableMigration" `  




#### `ExtendSchema`

  * **Method** : `google.cloud.managedidentities.v1.ManagedIdentitiesService.ExtendSchema`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `managedidentities.domains.extendSchema - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.managedidentities.v1.ManagedIdentitiesService.ExtendSchema" `  




#### `GetDomain`

  * **Method** : `google.cloud.managedidentities.v1.ManagedIdentitiesService.GetDomain`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `managedidentities.domains.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.managedidentities.v1.ManagedIdentitiesService.GetDomain" `  




#### `GetLDAPSSettings`

  * **Method** : `google.cloud.managedidentities.v1.ManagedIdentitiesService.GetLDAPSSettings`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `managedidentities.domains.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.managedidentities.v1.ManagedIdentitiesService.GetLDAPSSettings" `  




#### `GetPeering`

  * **Method** : `google.cloud.managedidentities.v1.ManagedIdentitiesService.GetPeering`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `managedidentities.peerings.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.managedidentities.v1.ManagedIdentitiesService.GetPeering" `  




#### `GetSqlIntegration`

  * **Method** : `google.cloud.managedidentities.v1.ManagedIdentitiesService.GetSqlIntegration`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `managedidentities.sqlintegrations.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.managedidentities.v1.ManagedIdentitiesService.GetSqlIntegration" `  




#### `ListDomains`

  * **Method** : `google.cloud.managedidentities.v1.ManagedIdentitiesService.ListDomains`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `managedidentities.domains.list - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.managedidentities.v1.ManagedIdentitiesService.ListDomains" `  




#### `ListPeerings`

  * **Method** : `google.cloud.managedidentities.v1.ManagedIdentitiesService.ListPeerings`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `managedidentities.peerings.list - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.managedidentities.v1.ManagedIdentitiesService.ListPeerings" `  




#### `ListSqlIntegrations`

  * **Method** : `google.cloud.managedidentities.v1.ManagedIdentitiesService.ListSqlIntegrations`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `managedidentities.sqlintegrations.list - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.managedidentities.v1.ManagedIdentitiesService.ListSqlIntegrations" `  




#### `ReconfigureTrust`

  * **Method** : `google.cloud.managedidentities.v1.ManagedIdentitiesService.ReconfigureTrust`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `managedidentities.domains.reconfigureTrust - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.managedidentities.v1.ManagedIdentitiesService.ReconfigureTrust" `  




#### `ResetAdminPassword`

  * **Method** : `google.cloud.managedidentities.v1.ManagedIdentitiesService.ResetAdminPassword`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `managedidentities.domains.resetpassword - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.managedidentities.v1.ManagedIdentitiesService.ResetAdminPassword" `  




#### `RestoreDomain`

  * **Method** : `google.cloud.managedidentities.v1.ManagedIdentitiesService.RestoreDomain`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `managedidentities.domains.restore - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.managedidentities.v1.ManagedIdentitiesService.RestoreDomain" `  




#### `UpdateBackup`

  * **Method** : `google.cloud.managedidentities.v1.ManagedIdentitiesService.UpdateBackup`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `managedidentities.backups.update - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.managedidentities.v1.ManagedIdentitiesService.UpdateBackup" `  




#### `UpdateDomain`

  * **Method** : `google.cloud.managedidentities.v1.ManagedIdentitiesService.UpdateDomain`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `managedidentities.domains.update - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.managedidentities.v1.ManagedIdentitiesService.UpdateDomain" `  




#### `UpdateLDAPSSettings`

  * **Method** : `google.cloud.managedidentities.v1.ManagedIdentitiesService.UpdateLDAPSSettings`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `managedidentities.domains.updateLDAPSSettings - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.managedidentities.v1.ManagedIdentitiesService.UpdateLDAPSSettings" `  




#### `UpdatePeering`

  * **Method** : `google.cloud.managedidentities.v1.ManagedIdentitiesService.UpdatePeering`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `managedidentities.peerings.update - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.managedidentities.v1.ManagedIdentitiesService.UpdatePeering" `  




#### `ValidateTrust`

  * **Method** : `google.cloud.managedidentities.v1.ManagedIdentitiesService.ValidateTrust`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `managedidentities.domains.validateTrust - ADMIN_READ`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.managedidentities.v1.ManagedIdentitiesService.ValidateTrust" `  




### `google.cloud.managedidentities.v1alpha1.ManagedIdentitiesService`

The following audit logs are associated with methods belonging to `google.cloud.managedidentities.v1alpha1.ManagedIdentitiesService`.

#### `AttachTrust`

  * **Method** : `google.cloud.managedidentities.v1alpha1.ManagedIdentitiesService.AttachTrust`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `managedidentities.domains.attachTrust - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.managedidentities.v1alpha1.ManagedIdentitiesService.AttachTrust" `  




#### `CheckMigrationPermission`

  * **Method** : `google.cloud.managedidentities.v1alpha1.ManagedIdentitiesService.CheckMigrationPermission`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `managedidentities.domains.checkMigrationPermission - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.managedidentities.v1alpha1.ManagedIdentitiesService.CheckMigrationPermission" `  




#### `CreateBackup`

  * **Method** : `google.cloud.managedidentities.v1alpha1.ManagedIdentitiesService.CreateBackup`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `managedidentities.backups.create - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.managedidentities.v1alpha1.ManagedIdentitiesService.CreateBackup" `  




#### `CreateMicrosoftAdDomain`

  * **Method** : `google.cloud.managedidentities.v1alpha1.ManagedIdentitiesService.CreateMicrosoftAdDomain`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `managedidentities.domains.create - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.managedidentities.v1alpha1.ManagedIdentitiesService.CreateMicrosoftAdDomain" `  




#### `CreatePeering`

  * **Method** : `google.cloud.managedidentities.v1alpha1.ManagedIdentitiesService.CreatePeering`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `managedidentities.peerings.create - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.managedidentities.v1alpha1.ManagedIdentitiesService.CreatePeering" `  




#### `DeleteBackup`

  * **Method** : `google.cloud.managedidentities.v1alpha1.ManagedIdentitiesService.DeleteBackup`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `managedidentities.backups.delete - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.managedidentities.v1alpha1.ManagedIdentitiesService.DeleteBackup" `  




#### `DeleteDomain`

  * **Method** : `google.cloud.managedidentities.v1alpha1.ManagedIdentitiesService.DeleteDomain`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `managedidentities.domains.delete - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.managedidentities.v1alpha1.ManagedIdentitiesService.DeleteDomain" `  




#### `DeletePeering`

  * **Method** : `google.cloud.managedidentities.v1alpha1.ManagedIdentitiesService.DeletePeering`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `managedidentities.peerings.delete - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.managedidentities.v1alpha1.ManagedIdentitiesService.DeletePeering" `  




#### `DetachTrust`

  * **Method** : `google.cloud.managedidentities.v1alpha1.ManagedIdentitiesService.DetachTrust`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `managedidentities.domains.detachTrust - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.managedidentities.v1alpha1.ManagedIdentitiesService.DetachTrust" `  




#### `DisableMigration`

  * **Method** : `google.cloud.managedidentities.v1alpha1.ManagedIdentitiesService.DisableMigration`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `managedidentities.domains.disableMigration - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.managedidentities.v1alpha1.ManagedIdentitiesService.DisableMigration" `  




#### `DomainJoinMachine`

  * **Method** : `google.cloud.managedidentities.v1alpha1.ManagedIdentitiesService.DomainJoinMachine`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `managedidentities.domains.domainJoinMachine - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.managedidentities.v1alpha1.ManagedIdentitiesService.DomainJoinMachine" `  




#### `EnableMigration`

  * **Method** : `google.cloud.managedidentities.v1alpha1.ManagedIdentitiesService.EnableMigration`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `managedidentities.domains.enableMigration - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.managedidentities.v1alpha1.ManagedIdentitiesService.EnableMigration" `  




#### `ExtendSchema`

  * **Method** : `google.cloud.managedidentities.v1alpha1.ManagedIdentitiesService.ExtendSchema`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `managedidentities.domains.extendSchema - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.managedidentities.v1alpha1.ManagedIdentitiesService.ExtendSchema" `  




#### `GetDomain`

  * **Method** : `google.cloud.managedidentities.v1alpha1.ManagedIdentitiesService.GetDomain`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `managedidentities.domains.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.managedidentities.v1alpha1.ManagedIdentitiesService.GetDomain" `  




#### `GetLDAPSSettings`

  * **Method** : `google.cloud.managedidentities.v1alpha1.ManagedIdentitiesService.GetLDAPSSettings`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `managedidentities.domains.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.managedidentities.v1alpha1.ManagedIdentitiesService.GetLDAPSSettings" `  




#### `GetPeering`

  * **Method** : `google.cloud.managedidentities.v1alpha1.ManagedIdentitiesService.GetPeering`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `managedidentities.peerings.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.managedidentities.v1alpha1.ManagedIdentitiesService.GetPeering" `  




#### `GetSQLIntegration`

  * **Method** : `google.cloud.managedidentities.v1alpha1.ManagedIdentitiesService.GetSQLIntegration`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `managedidentities.sqlintegrations.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.managedidentities.v1alpha1.ManagedIdentitiesService.GetSQLIntegration" `  




#### `ListDomains`

  * **Method** : `google.cloud.managedidentities.v1alpha1.ManagedIdentitiesService.ListDomains`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `managedidentities.domains.list - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.managedidentities.v1alpha1.ManagedIdentitiesService.ListDomains" `  




#### `ListPeerings`

  * **Method** : `google.cloud.managedidentities.v1alpha1.ManagedIdentitiesService.ListPeerings`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `managedidentities.peerings.list - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.managedidentities.v1alpha1.ManagedIdentitiesService.ListPeerings" `  




#### `ListSQLIntegrations`

  * **Method** : `google.cloud.managedidentities.v1alpha1.ManagedIdentitiesService.ListSQLIntegrations`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `managedidentities.sqlintegrations.list - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.managedidentities.v1alpha1.ManagedIdentitiesService.ListSQLIntegrations" `  




#### `ReconfigureTrust`

  * **Method** : `google.cloud.managedidentities.v1alpha1.ManagedIdentitiesService.ReconfigureTrust`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `managedidentities.domains.reconfigureTrust - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.managedidentities.v1alpha1.ManagedIdentitiesService.ReconfigureTrust" `  




#### `ResetAdminPassword`

  * **Method** : `google.cloud.managedidentities.v1alpha1.ManagedIdentitiesService.ResetAdminPassword`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `managedidentities.domains.resetpassword - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.managedidentities.v1alpha1.ManagedIdentitiesService.ResetAdminPassword" `  




#### `RestoreDomain`

  * **Method** : `google.cloud.managedidentities.v1alpha1.ManagedIdentitiesService.RestoreDomain`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `managedidentities.domains.restore - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.managedidentities.v1alpha1.ManagedIdentitiesService.RestoreDomain" `  




#### `UpdateBackup`

  * **Method** : `google.cloud.managedidentities.v1alpha1.ManagedIdentitiesService.UpdateBackup`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `managedidentities.backups.update - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.managedidentities.v1alpha1.ManagedIdentitiesService.UpdateBackup" `  




#### `UpdateDomain`

  * **Method** : `google.cloud.managedidentities.v1alpha1.ManagedIdentitiesService.UpdateDomain`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `managedidentities.domains.update - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.managedidentities.v1alpha1.ManagedIdentitiesService.UpdateDomain" `  




#### `UpdateLDAPSSettings`

  * **Method** : `google.cloud.managedidentities.v1alpha1.ManagedIdentitiesService.UpdateLDAPSSettings`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `managedidentities.domains.updateLDAPSSettings - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.managedidentities.v1alpha1.ManagedIdentitiesService.UpdateLDAPSSettings" `  




#### `UpdatePeering`

  * **Method** : `google.cloud.managedidentities.v1alpha1.ManagedIdentitiesService.UpdatePeering`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `managedidentities.peerings.update - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.managedidentities.v1alpha1.ManagedIdentitiesService.UpdatePeering" `  




#### `ValidateTrust`

  * **Method** : `google.cloud.managedidentities.v1alpha1.ManagedIdentitiesService.ValidateTrust`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `managedidentities.domains.validateTrust - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.managedidentities.v1alpha1.ManagedIdentitiesService.ValidateTrust" `  




### `google.cloud.managedidentities.v1beta1.ManagedIdentitiesService`

The following audit logs are associated with methods belonging to `google.cloud.managedidentities.v1beta1.ManagedIdentitiesService`.

#### `AttachTrust`

  * **Method** : `google.cloud.managedidentities.v1beta1.ManagedIdentitiesService.AttachTrust`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `managedidentities.domains.attachTrust - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.managedidentities.v1beta1.ManagedIdentitiesService.AttachTrust" `  




#### `CheckMigrationPermission`

  * **Method** : `google.cloud.managedidentities.v1beta1.ManagedIdentitiesService.CheckMigrationPermission`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `managedidentities.domains.checkMigrationPermission - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.managedidentities.v1beta1.ManagedIdentitiesService.CheckMigrationPermission" `  




#### `CreateBackup`

  * **Method** : `google.cloud.managedidentities.v1beta1.ManagedIdentitiesService.CreateBackup`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `managedidentities.backups.create - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.managedidentities.v1beta1.ManagedIdentitiesService.CreateBackup" `  




#### `CreateMicrosoftAdDomain`

  * **Method** : `google.cloud.managedidentities.v1beta1.ManagedIdentitiesService.CreateMicrosoftAdDomain`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `managedidentities.domains.create - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.managedidentities.v1beta1.ManagedIdentitiesService.CreateMicrosoftAdDomain" `  




#### `CreatePeering`

  * **Method** : `google.cloud.managedidentities.v1beta1.ManagedIdentitiesService.CreatePeering`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `managedidentities.peerings.create - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.managedidentities.v1beta1.ManagedIdentitiesService.CreatePeering" `  




#### `DeleteBackup`

  * **Method** : `google.cloud.managedidentities.v1beta1.ManagedIdentitiesService.DeleteBackup`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `managedidentities.backups.delete - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.managedidentities.v1beta1.ManagedIdentitiesService.DeleteBackup" `  




#### `DeleteDomain`

  * **Method** : `google.cloud.managedidentities.v1beta1.ManagedIdentitiesService.DeleteDomain`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `managedidentities.domains.delete - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.managedidentities.v1beta1.ManagedIdentitiesService.DeleteDomain" `  




#### `DeletePeering`

  * **Method** : `google.cloud.managedidentities.v1beta1.ManagedIdentitiesService.DeletePeering`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `managedidentities.peerings.delete - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.managedidentities.v1beta1.ManagedIdentitiesService.DeletePeering" `  




#### `DetachTrust`

  * **Method** : `google.cloud.managedidentities.v1beta1.ManagedIdentitiesService.DetachTrust`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `managedidentities.domains.detachTrust - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.managedidentities.v1beta1.ManagedIdentitiesService.DetachTrust" `  




#### `DisableMigration`

  * **Method** : `google.cloud.managedidentities.v1beta1.ManagedIdentitiesService.DisableMigration`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `managedidentities.domains.disableMigration - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.managedidentities.v1beta1.ManagedIdentitiesService.DisableMigration" `  




#### `DomainJoinMachine`

  * **Method** : `google.cloud.managedidentities.v1beta1.ManagedIdentitiesService.DomainJoinMachine`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `managedidentities.domains.domainJoinMachine - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.managedidentities.v1beta1.ManagedIdentitiesService.DomainJoinMachine" `  




#### `EnableMigration`

  * **Method** : `google.cloud.managedidentities.v1beta1.ManagedIdentitiesService.EnableMigration`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `managedidentities.domains.enableMigration - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.managedidentities.v1beta1.ManagedIdentitiesService.EnableMigration" `  




#### `ExtendSchema`

  * **Method** : `google.cloud.managedidentities.v1beta1.ManagedIdentitiesService.ExtendSchema`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `managedidentities.domains.extendSchema - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.managedidentities.v1beta1.ManagedIdentitiesService.ExtendSchema" `  




#### `GetDomain`

  * **Method** : `google.cloud.managedidentities.v1beta1.ManagedIdentitiesService.GetDomain`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `managedidentities.domains.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.managedidentities.v1beta1.ManagedIdentitiesService.GetDomain" `  




#### `GetLDAPSSettings`

  * **Method** : `google.cloud.managedidentities.v1beta1.ManagedIdentitiesService.GetLDAPSSettings`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `managedidentities.domains.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.managedidentities.v1beta1.ManagedIdentitiesService.GetLDAPSSettings" `  




#### `GetPeering`

  * **Method** : `google.cloud.managedidentities.v1beta1.ManagedIdentitiesService.GetPeering`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `managedidentities.peerings.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.managedidentities.v1beta1.ManagedIdentitiesService.GetPeering" `  




#### `GetSqlIntegration`

  * **Method** : `google.cloud.managedidentities.v1beta1.ManagedIdentitiesService.GetSqlIntegration`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `managedidentities.sqlintegrations.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.managedidentities.v1beta1.ManagedIdentitiesService.GetSqlIntegration" `  




#### `ListDomains`

  * **Method** : `google.cloud.managedidentities.v1beta1.ManagedIdentitiesService.ListDomains`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `managedidentities.domains.list - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.managedidentities.v1beta1.ManagedIdentitiesService.ListDomains" `  




#### `ListPeerings`

  * **Method** : `google.cloud.managedidentities.v1beta1.ManagedIdentitiesService.ListPeerings`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `managedidentities.peerings.list - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.managedidentities.v1beta1.ManagedIdentitiesService.ListPeerings" `  




#### `ListSqlIntegrations`

  * **Method** : `google.cloud.managedidentities.v1beta1.ManagedIdentitiesService.ListSqlIntegrations`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `managedidentities.sqlintegrations.list - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.managedidentities.v1beta1.ManagedIdentitiesService.ListSqlIntegrations" `  




#### `ReconfigureTrust`

  * **Method** : `google.cloud.managedidentities.v1beta1.ManagedIdentitiesService.ReconfigureTrust`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `managedidentities.domains.reconfigureTrust - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.managedidentities.v1beta1.ManagedIdentitiesService.ReconfigureTrust" `  




#### `ResetAdminPassword`

  * **Method** : `google.cloud.managedidentities.v1beta1.ManagedIdentitiesService.ResetAdminPassword`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `managedidentities.domains.resetpassword - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.managedidentities.v1beta1.ManagedIdentitiesService.ResetAdminPassword" `  




#### `RestoreDomain`

  * **Method** : `google.cloud.managedidentities.v1beta1.ManagedIdentitiesService.RestoreDomain`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `managedidentities.domains.restore - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.managedidentities.v1beta1.ManagedIdentitiesService.RestoreDomain" `  




#### `UpdateBackup`

  * **Method** : `google.cloud.managedidentities.v1beta1.ManagedIdentitiesService.UpdateBackup`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `managedidentities.backups.update - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.managedidentities.v1beta1.ManagedIdentitiesService.UpdateBackup" `  




#### `UpdateDomain`

  * **Method** : `google.cloud.managedidentities.v1beta1.ManagedIdentitiesService.UpdateDomain`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `managedidentities.domains.update - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.managedidentities.v1beta1.ManagedIdentitiesService.UpdateDomain" `  




#### `UpdateLDAPSSettings`

  * **Method** : `google.cloud.managedidentities.v1beta1.ManagedIdentitiesService.UpdateLDAPSSettings`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `managedidentities.domains.updateLDAPSSettings - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.managedidentities.v1beta1.ManagedIdentitiesService.UpdateLDAPSSettings" `  




#### `UpdatePeering`

  * **Method** : `google.cloud.managedidentities.v1beta1.ManagedIdentitiesService.UpdatePeering`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `managedidentities.peerings.update - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.managedidentities.v1beta1.ManagedIdentitiesService.UpdatePeering" `  




#### `ValidateTrust`

  * **Method** : `google.cloud.managedidentities.v1beta1.ManagedIdentitiesService.ValidateTrust`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `managedidentities.domains.validateTrust - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.managedidentities.v1beta1.ManagedIdentitiesService.ValidateTrust" `  




### `google.cloud.managedidentities.v1internal1.ManagedIdentitiesService`

The following audit logs are associated with methods belonging to `google.cloud.managedidentities.v1internal1.ManagedIdentitiesService`.

#### `CreateInternalIntegratedNetwork`

  * **Method** : `google.cloud.managedidentities.v1internal1.ManagedIdentitiesService.CreateInternalIntegratedNetwork`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `managedidentities.integratednetworks.create - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.managedidentities.v1internal1.ManagedIdentitiesService.CreateInternalIntegratedNetwork" `  




#### `CreateInternalSQLIntegration`

  * **Method** : `google.cloud.managedidentities.v1internal1.ManagedIdentitiesService.CreateInternalSQLIntegration`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `managedidentities.sqlintegrations.create - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.managedidentities.v1internal1.ManagedIdentitiesService.CreateInternalSQLIntegration" `  




#### `DeleteInternalIntegratedNetwork`

  * **Method** : `google.cloud.managedidentities.v1internal1.ManagedIdentitiesService.DeleteInternalIntegratedNetwork`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `managedidentities.integratednetworks.delete - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.managedidentities.v1internal1.ManagedIdentitiesService.DeleteInternalIntegratedNetwork" `  




#### `DeleteInternalSQLIntegration`

  * **Method** : `google.cloud.managedidentities.v1internal1.ManagedIdentitiesService.DeleteInternalSQLIntegration`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `managedidentities.sqlintegrations.delete - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.managedidentities.v1internal1.ManagedIdentitiesService.DeleteInternalSQLIntegration" `  




#### `GetInternalIntegratedNetwork`

  * **Method** : `google.cloud.managedidentities.v1internal1.ManagedIdentitiesService.GetInternalIntegratedNetwork`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `managedidentities.integratednetworks.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.managedidentities.v1internal1.ManagedIdentitiesService.GetInternalIntegratedNetwork" `  




#### `ResetInternalSQLPassword`

  * **Method** : `google.cloud.managedidentities.v1internal1.ManagedIdentitiesService.ResetInternalSQLPassword`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `managedidentities.sqlintegrations.resetsqlpassword - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.managedidentities.v1internal1.ManagedIdentitiesService.ResetInternalSQLPassword" `  




### `google.iam.v1.IAMPolicy`

The following audit logs are associated with methods belonging to `google.iam.v1.IAMPolicy`.

#### `GetIamPolicy`

  * **Method** : `GetIamPolicy`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `managedidentities.domains.getIamPolicy - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="GetIamPolicy" `  




#### `SetIamPolicy`

  * **Method** : `SetIamPolicy`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `managedidentities.domains.setIamPolicy - ADMIN_WRITE`
    * `managedidentities.peerings.setIamPolicy - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="SetIamPolicy" `  




### `google.longrunning.Operations`

The following audit logs are associated with methods belonging to `google.longrunning.Operations`.

#### `CancelOperation`

  * **Method** : `google.longrunning.Operations.CancelOperation`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `managedidentities.operations.cancel - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.longrunning.Operations.CancelOperation" `  




#### `DeleteOperation`

  * **Method** : `google.longrunning.Operations.DeleteOperation`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `managedidentities.operations.delete - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.longrunning.Operations.DeleteOperation" `  




#### `GetOperation`

  * **Method** : `google.longrunning.Operations.GetOperation`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `managedidentities.operations.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.longrunning.Operations.GetOperation" `  




#### `ListOperations`

  * **Method** : `google.longrunning.Operations.ListOperations`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `managedidentities.operations.list - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.longrunning.Operations.ListOperations" `  




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
