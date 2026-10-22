---
url: https://docs.cloud.google.com/compute/vm-manager/docs/audit-logging/
title: VM Manager audit logging \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:08:46.463612+00:00
---

# VM Manager audit logging  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/compute/vm-manager/docs/audit-logging/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ Compute Engine ](https://docs.cloud.google.com/compute/docs)
  * [ VM Manager ](https://docs.cloud.google.com/compute/vm-manager/docs)
  * [ Guides ](https://docs.cloud.google.com/compute/vm-manager/docs/overview)



Send feedback 

#  VM Manager audit logging Stay organized with collections  Save and categorize content based on your preferences. 

This document describes audit logging for VM Manager. Google Cloud services generate audit logs that record administrative and access activities within your Google Cloud resources. For more information about Cloud Audit Logs, see the following: 

  * [Types of audit logs](https://docs.cloud.google.com/logging/docs/audit#types)
  * [Audit log entry structure](https://docs.cloud.google.com/logging/docs/audit#audit_log_entry_structure)
  * [Storing and routing audit logs](https://docs.cloud.google.com/logging/docs/audit#storing_and_routing_audit_logs)
  * [Cloud Logging pricing summary](https://docs.cloud.google.com/stackdriver/pricing#logs-pricing-summary)
  * [Enable Data Access audit logs](https://docs.cloud.google.com/logging/docs/audit/configure-data-access)



## Service name

VM Manager audit logs use the service name `osconfig.googleapis.com`. Filter for this service: 
    
    
        protoPayload.serviceName="osconfig.googleapis.com"
      

## Methods by permission type

Each IAM permission has a `type` property, whose value is an enum that can be one of four values: `ADMIN_READ`, `ADMIN_WRITE`, `DATA_READ`, or `DATA_WRITE`. When you call a method, VM Manager generates an audit log whose category is dependent on the `type` property of the permission required to perform the method. Methods that require an IAM permission with the `type` property value of `DATA_READ`, `DATA_WRITE`, or `ADMIN_READ` generate [Data Access](https://docs.cloud.google.com/logging/docs/audit#data-access) audit logs. Methods that require an IAM permission with the `type` property value of `ADMIN_WRITE` generate [Admin Activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity) audit logs.

API methods in the following list that are marked with (LRO) are long-running operations (LROs). These methods usually generate two audit log entries: one when the operation starts and another when it ends. For more information see [Audit logs for long-running operations](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro). Permission type | Methods  
---|---  
`ADMIN_READ` | `google.cloud.osconfig.v1.OsConfigGlobalService.GetProjectFeatureSettings`  
`ADMIN_WRITE` | `google.cloud.osconfig.v1.OsConfigGlobalService.UpdateProjectFeatureSettings`  
`DATA_READ` | `google.cloud.osconfig.v1.OsConfigService.GetPatchDeployment`  
`google.cloud.osconfig.v1.OsConfigService.GetPatchJob`  
`google.cloud.osconfig.v1.OsConfigService.ListPatchDeployments`  
`google.cloud.osconfig.v1.OsConfigService.ListPatchJobInstanceDetails`  
`google.cloud.osconfig.v1.OsConfigService.ListPatchJobs`  
`google.cloud.osconfig.v1.OsConfigZonalService.GetInventory`  
`google.cloud.osconfig.v1.OsConfigZonalService.GetOSPolicyAssignment`  
`google.cloud.osconfig.v1.OsConfigZonalService.GetOSPolicyAssignmentReport`  
`google.cloud.osconfig.v1.OsConfigZonalService.GetVulnerabilityReport`  
`google.cloud.osconfig.v1.OsConfigZonalService.ListInventories`  
`google.cloud.osconfig.v1.OsConfigZonalService.ListOSPolicyAssignmentReports`  
`google.cloud.osconfig.v1.OsConfigZonalService.ListOSPolicyAssignmentRevisions`  
`google.cloud.osconfig.v1.OsConfigZonalService.ListOSPolicyAssignments`  
`google.cloud.osconfig.v1.OsConfigZonalService.ListVulnerabilityReports`  
`google.cloud.osconfig.v1alpha.OsConfigZonalService.GetInstanceOSPoliciesCompliance`  
`google.cloud.osconfig.v1alpha.OsConfigZonalService.GetInventory`  
`google.cloud.osconfig.v1alpha.OsConfigZonalService.GetOSPolicyAssignment`  
`google.cloud.osconfig.v1alpha.OsConfigZonalService.GetOSPolicyAssignmentReport`  
`google.cloud.osconfig.v1alpha.OsConfigZonalService.GetVulnerabilityReport`  
`google.cloud.osconfig.v1alpha.OsConfigZonalService.ListInstanceOSPoliciesCompliances`  
`google.cloud.osconfig.v1alpha.OsConfigZonalService.ListInventories`  
`google.cloud.osconfig.v1alpha.OsConfigZonalService.ListOSPolicyAssignmentReports`  
`google.cloud.osconfig.v1alpha.OsConfigZonalService.ListOSPolicyAssignmentRevisions`  
`google.cloud.osconfig.v1alpha.OsConfigZonalService.ListOSPolicyAssignments`  
`google.cloud.osconfig.v1alpha.OsConfigZonalService.ListVulnerabilityReports`  
`google.cloud.osconfig.v1beta.OsConfigService.GetGuestPolicy`  
`google.cloud.osconfig.v1beta.OsConfigService.GetPatchDeployment`  
`google.cloud.osconfig.v1beta.OsConfigService.GetPatchJob`  
`google.cloud.osconfig.v1beta.OsConfigService.ListGuestPolicies`  
`google.cloud.osconfig.v1beta.OsConfigService.ListPatchDeployments`  
`google.cloud.osconfig.v1beta.OsConfigService.ListPatchJobInstanceDetails`  
`google.cloud.osconfig.v1beta.OsConfigService.ListPatchJobs`  
`google.cloud.osconfig.v2.PolicyOrchestratorService.GetPolicyOrchestrator`  
`google.cloud.osconfig.v2.PolicyOrchestratorService.GetPolicyOrchestratorForFolder`  
`google.cloud.osconfig.v2.PolicyOrchestratorService.GetPolicyOrchestratorForOrganization`  
`google.cloud.osconfig.v2.PolicyOrchestratorService.ListPolicyOrchestrators`  
`google.cloud.osconfig.v2.PolicyOrchestratorService.ListPolicyOrchestratorsForFolder`  
`google.cloud.osconfig.v2.PolicyOrchestratorService.ListPolicyOrchestratorsForOrganization`  
`google.cloud.osconfig.v2beta.PolicyOrchestratorService.GetPolicyOrchestrator`  
`google.cloud.osconfig.v2beta.PolicyOrchestratorService.GetPolicyOrchestratorForFolder`  
`google.cloud.osconfig.v2beta.PolicyOrchestratorService.GetPolicyOrchestratorForOrganization`  
`google.cloud.osconfig.v2beta.PolicyOrchestratorService.ListPolicyOrchestrators`  
`google.cloud.osconfig.v2beta.PolicyOrchestratorService.ListPolicyOrchestratorsForFolder`  
`google.cloud.osconfig.v2beta.PolicyOrchestratorService.ListPolicyOrchestratorsForOrganization`  
`google.longrunning.Operations.GetOperation`  
`google.longrunning.Operations.ListOperations`  
`DATA_WRITE` | `google.cloud.osconfig.v1.OsConfigService.CancelPatchJob`  
`google.cloud.osconfig.v1.OsConfigService.CreatePatchDeployment`  
`google.cloud.osconfig.v1.OsConfigService.DeletePatchDeployment`  
`google.cloud.osconfig.v1.OsConfigService.ExecutePatchJob`  
`google.cloud.osconfig.v1.OsConfigService.PausePatchDeployment`  
`google.cloud.osconfig.v1.OsConfigService.ResumePatchDeployment`  
`google.cloud.osconfig.v1.OsConfigService.UpdatePatchDeployment`  
`google.cloud.osconfig.v1.OsConfigZonalService.CreateOSPolicyAssignment` (LRO)  
`google.cloud.osconfig.v1.OsConfigZonalService.DeleteOSPolicyAssignment` (LRO)  
`google.cloud.osconfig.v1.OsConfigZonalService.UpdateOSPolicyAssignment` (LRO)  
`google.cloud.osconfig.v1alpha.OsConfigZonalService.CreateOSPolicyAssignment` (LRO)  
`google.cloud.osconfig.v1alpha.OsConfigZonalService.DeleteOSPolicyAssignment` (LRO)  
`google.cloud.osconfig.v1alpha.OsConfigZonalService.UpdateOSPolicyAssignment` (LRO)  
`google.cloud.osconfig.v1beta.OsConfigService.CancelPatchJob`  
`google.cloud.osconfig.v1beta.OsConfigService.CreateGuestPolicy`  
`google.cloud.osconfig.v1beta.OsConfigService.CreatePatchDeployment`  
`google.cloud.osconfig.v1beta.OsConfigService.DeleteGuestPolicy`  
`google.cloud.osconfig.v1beta.OsConfigService.DeletePatchDeployment`  
`google.cloud.osconfig.v1beta.OsConfigService.ExecutePatchJob`  
`google.cloud.osconfig.v1beta.OsConfigService.PausePatchDeployment`  
`google.cloud.osconfig.v1beta.OsConfigService.ResumePatchDeployment`  
`google.cloud.osconfig.v1beta.OsConfigService.UpdateGuestPolicy`  
`google.cloud.osconfig.v1beta.OsConfigService.UpdatePatchDeployment`  
`google.cloud.osconfig.v2.PolicyOrchestratorService.CreatePolicyOrchestrator` (LRO)  
`google.cloud.osconfig.v2.PolicyOrchestratorService.CreatePolicyOrchestratorForFolder` (LRO)  
`google.cloud.osconfig.v2.PolicyOrchestratorService.CreatePolicyOrchestratorForOrganization` (LRO)  
`google.cloud.osconfig.v2.PolicyOrchestratorService.DeletePolicyOrchestrator` (LRO)  
`google.cloud.osconfig.v2.PolicyOrchestratorService.DeletePolicyOrchestratorForFolder` (LRO)  
`google.cloud.osconfig.v2.PolicyOrchestratorService.DeletePolicyOrchestratorForOrganization` (LRO)  
`google.cloud.osconfig.v2.PolicyOrchestratorService.UpdatePolicyOrchestrator` (LRO)  
`google.cloud.osconfig.v2.PolicyOrchestratorService.UpdatePolicyOrchestratorForFolder` (LRO)  
`google.cloud.osconfig.v2.PolicyOrchestratorService.UpdatePolicyOrchestratorForOrganization` (LRO)  
`google.cloud.osconfig.v2beta.PolicyOrchestratorService.CreatePolicyOrchestrator` (LRO)  
`google.cloud.osconfig.v2beta.PolicyOrchestratorService.CreatePolicyOrchestratorForFolder` (LRO)  
`google.cloud.osconfig.v2beta.PolicyOrchestratorService.CreatePolicyOrchestratorForOrganization` (LRO)  
`google.cloud.osconfig.v2beta.PolicyOrchestratorService.DeletePolicyOrchestrator` (LRO)  
`google.cloud.osconfig.v2beta.PolicyOrchestratorService.DeletePolicyOrchestratorForFolder` (LRO)  
`google.cloud.osconfig.v2beta.PolicyOrchestratorService.DeletePolicyOrchestratorForOrganization` (LRO)  
`google.cloud.osconfig.v2beta.PolicyOrchestratorService.UpdatePolicyOrchestrator` (LRO)  
`google.cloud.osconfig.v2beta.PolicyOrchestratorService.UpdatePolicyOrchestratorForFolder` (LRO)  
`google.cloud.osconfig.v2beta.PolicyOrchestratorService.UpdatePolicyOrchestratorForOrganization` (LRO)  
`google.longrunning.OsConfigOperationsService.CancelOperation`  
`google.longrunning.Operations.DeleteOperation`  
  
## API interface audit logs

For information about how and which permissions are evaluated for each method, see the Identity and Access Management documentation for VM Manager.

### `google.cloud.osconfig.v1.OsConfigGlobalService`

The following audit logs are associated with methods belonging to `google.cloud.osconfig.v1.OsConfigGlobalService`.

#### `GetProjectFeatureSettings`

  * **Method** : `google.cloud.osconfig.v1.OsConfigGlobalService.GetProjectFeatureSettings`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `osconfig.projectFeatureSettings.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.osconfig.v1.OsConfigGlobalService.GetProjectFeatureSettings" `  




#### `UpdateProjectFeatureSettings`

  * **Method** : `google.cloud.osconfig.v1.OsConfigGlobalService.UpdateProjectFeatureSettings`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `osconfig.projectFeatureSettings.update - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.osconfig.v1.OsConfigGlobalService.UpdateProjectFeatureSettings" `  




### `google.cloud.osconfig.v1.OsConfigService`

The following audit logs are associated with methods belonging to `google.cloud.osconfig.v1.OsConfigService`.

#### `CancelPatchJob`

  * **Method** : `google.cloud.osconfig.v1.OsConfigService.CancelPatchJob`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `osconfig.patchJobs.exec - DATA_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.osconfig.v1.OsConfigService.CancelPatchJob" `  




#### `CreatePatchDeployment`

  * **Method** : `google.cloud.osconfig.v1.OsConfigService.CreatePatchDeployment`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `osconfig.patchDeployments.create - DATA_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.osconfig.v1.OsConfigService.CreatePatchDeployment" `  




#### `DeletePatchDeployment`

  * **Method** : `google.cloud.osconfig.v1.OsConfigService.DeletePatchDeployment`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `osconfig.patchDeployments.delete - DATA_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.osconfig.v1.OsConfigService.DeletePatchDeployment" `  




#### `ExecutePatchJob`

  * **Method** : `google.cloud.osconfig.v1.OsConfigService.ExecutePatchJob`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `osconfig.patchJobs.exec - DATA_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.osconfig.v1.OsConfigService.ExecutePatchJob" `  




#### `GetPatchDeployment`

  * **Method** : `google.cloud.osconfig.v1.OsConfigService.GetPatchDeployment`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `osconfig.patchDeployments.get - DATA_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.osconfig.v1.OsConfigService.GetPatchDeployment" `  




#### `GetPatchJob`

  * **Method** : `google.cloud.osconfig.v1.OsConfigService.GetPatchJob`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `osconfig.patchJobs.get - DATA_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.osconfig.v1.OsConfigService.GetPatchJob" `  




#### `ListPatchDeployments`

  * **Method** : `google.cloud.osconfig.v1.OsConfigService.ListPatchDeployments`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `osconfig.patchDeployments.list - DATA_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.osconfig.v1.OsConfigService.ListPatchDeployments" `  




#### `ListPatchJobInstanceDetails`

  * **Method** : `google.cloud.osconfig.v1.OsConfigService.ListPatchJobInstanceDetails`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `osconfig.patchJobs.get - DATA_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.osconfig.v1.OsConfigService.ListPatchJobInstanceDetails" `  




#### `ListPatchJobs`

  * **Method** : `google.cloud.osconfig.v1.OsConfigService.ListPatchJobs`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `osconfig.patchJobs.list - DATA_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.osconfig.v1.OsConfigService.ListPatchJobs" `  




#### `PausePatchDeployment`

  * **Method** : `google.cloud.osconfig.v1.OsConfigService.PausePatchDeployment`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `osconfig.patchDeployments.pause - DATA_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.osconfig.v1.OsConfigService.PausePatchDeployment" `  




#### `ResumePatchDeployment`

  * **Method** : `google.cloud.osconfig.v1.OsConfigService.ResumePatchDeployment`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `osconfig.patchDeployments.resume - DATA_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.osconfig.v1.OsConfigService.ResumePatchDeployment" `  




#### `UpdatePatchDeployment`

  * **Method** : `google.cloud.osconfig.v1.OsConfigService.UpdatePatchDeployment`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `osconfig.patchDeployments.update - DATA_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.osconfig.v1.OsConfigService.UpdatePatchDeployment" `  




### `google.cloud.osconfig.v1.OsConfigZonalService`

The following audit logs are associated with methods belonging to `google.cloud.osconfig.v1.OsConfigZonalService`.

#### `CreateOSPolicyAssignment`

  * **Method** : `google.cloud.osconfig.v1.OsConfigZonalService.CreateOSPolicyAssignment`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `osconfig.osPolicyAssignments.create - DATA_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.osconfig.v1.OsConfigZonalService.CreateOSPolicyAssignment" `  




#### `DeleteOSPolicyAssignment`

  * **Method** : `google.cloud.osconfig.v1.OsConfigZonalService.DeleteOSPolicyAssignment`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `osconfig.osPolicyAssignments.delete - DATA_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.osconfig.v1.OsConfigZonalService.DeleteOSPolicyAssignment" `  




#### `GetInventory`

  * **Method** : `google.cloud.osconfig.v1.OsConfigZonalService.GetInventory`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `osconfig.inventories.get - DATA_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.osconfig.v1.OsConfigZonalService.GetInventory" `  




#### `GetOSPolicyAssignment`

  * **Method** : `google.cloud.osconfig.v1.OsConfigZonalService.GetOSPolicyAssignment`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `osconfig.osPolicyAssignments.get - DATA_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.osconfig.v1.OsConfigZonalService.GetOSPolicyAssignment" `  




#### `GetOSPolicyAssignmentReport`

  * **Method** : `google.cloud.osconfig.v1.OsConfigZonalService.GetOSPolicyAssignmentReport`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `osconfig.osPolicyAssignmentReports.get - DATA_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.osconfig.v1.OsConfigZonalService.GetOSPolicyAssignmentReport" `  




#### `GetVulnerabilityReport`

  * **Method** : `google.cloud.osconfig.v1.OsConfigZonalService.GetVulnerabilityReport`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `osconfig.vulnerabilityReports.get - DATA_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.osconfig.v1.OsConfigZonalService.GetVulnerabilityReport" `  




#### `ListInventories`

  * **Method** : `google.cloud.osconfig.v1.OsConfigZonalService.ListInventories`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `osconfig.inventories.list - DATA_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.osconfig.v1.OsConfigZonalService.ListInventories" `  




#### `ListOSPolicyAssignmentReports`

  * **Method** : `google.cloud.osconfig.v1.OsConfigZonalService.ListOSPolicyAssignmentReports`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `osconfig.osPolicyAssignmentReports.list - DATA_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.osconfig.v1.OsConfigZonalService.ListOSPolicyAssignmentReports" `  




#### `ListOSPolicyAssignmentRevisions`

  * **Method** : `google.cloud.osconfig.v1.OsConfigZonalService.ListOSPolicyAssignmentRevisions`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `osconfig.osPolicyAssignments.get - DATA_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.osconfig.v1.OsConfigZonalService.ListOSPolicyAssignmentRevisions" `  




#### `ListOSPolicyAssignments`

  * **Method** : `google.cloud.osconfig.v1.OsConfigZonalService.ListOSPolicyAssignments`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `osconfig.osPolicyAssignments.list - DATA_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.osconfig.v1.OsConfigZonalService.ListOSPolicyAssignments" `  




#### `ListVulnerabilityReports`

  * **Method** : `google.cloud.osconfig.v1.OsConfigZonalService.ListVulnerabilityReports`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `osconfig.vulnerabilityReports.list - DATA_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.osconfig.v1.OsConfigZonalService.ListVulnerabilityReports" `  




#### `UpdateOSPolicyAssignment`

  * **Method** : `google.cloud.osconfig.v1.OsConfigZonalService.UpdateOSPolicyAssignment`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `osconfig.osPolicyAssignments.update - DATA_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.osconfig.v1.OsConfigZonalService.UpdateOSPolicyAssignment" `  




### `google.cloud.osconfig.v1alpha.OsConfigZonalService`

The following audit logs are associated with methods belonging to `google.cloud.osconfig.v1alpha.OsConfigZonalService`.

#### `CreateOSPolicyAssignment`

  * **Method** : `google.cloud.osconfig.v1alpha.OsConfigZonalService.CreateOSPolicyAssignment`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `osconfig.osPolicyAssignments.create - DATA_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.osconfig.v1alpha.OsConfigZonalService.CreateOSPolicyAssignment" `  




#### `DeleteOSPolicyAssignment`

  * **Method** : `google.cloud.osconfig.v1alpha.OsConfigZonalService.DeleteOSPolicyAssignment`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `osconfig.osPolicyAssignments.delete - DATA_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.osconfig.v1alpha.OsConfigZonalService.DeleteOSPolicyAssignment" `  




#### `GetInstanceOSPoliciesCompliance`

  * **Method** : `google.cloud.osconfig.v1alpha.OsConfigZonalService.GetInstanceOSPoliciesCompliance`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `osconfig.instanceOSPoliciesCompliances.get - DATA_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.osconfig.v1alpha.OsConfigZonalService.GetInstanceOSPoliciesCompliance" `  




#### `GetInventory`

  * **Method** : `google.cloud.osconfig.v1alpha.OsConfigZonalService.GetInventory`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `osconfig.inventories.get - DATA_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.osconfig.v1alpha.OsConfigZonalService.GetInventory" `  




#### `GetOSPolicyAssignment`

  * **Method** : `google.cloud.osconfig.v1alpha.OsConfigZonalService.GetOSPolicyAssignment`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `osconfig.osPolicyAssignments.get - DATA_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.osconfig.v1alpha.OsConfigZonalService.GetOSPolicyAssignment" `  




#### `GetOSPolicyAssignmentReport`

  * **Method** : `google.cloud.osconfig.v1alpha.OsConfigZonalService.GetOSPolicyAssignmentReport`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `osconfig.osPolicyAssignmentReports.get - DATA_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.osconfig.v1alpha.OsConfigZonalService.GetOSPolicyAssignmentReport" `  




#### `GetVulnerabilityReport`

  * **Method** : `google.cloud.osconfig.v1alpha.OsConfigZonalService.GetVulnerabilityReport`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `osconfig.vulnerabilityReports.get - DATA_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.osconfig.v1alpha.OsConfigZonalService.GetVulnerabilityReport" `  




#### `ListInstanceOSPoliciesCompliances`

  * **Method** : `google.cloud.osconfig.v1alpha.OsConfigZonalService.ListInstanceOSPoliciesCompliances`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `osconfig.instanceOSPoliciesCompliances.list - DATA_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.osconfig.v1alpha.OsConfigZonalService.ListInstanceOSPoliciesCompliances" `  




#### `ListInventories`

  * **Method** : `google.cloud.osconfig.v1alpha.OsConfigZonalService.ListInventories`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `osconfig.inventories.list - DATA_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.osconfig.v1alpha.OsConfigZonalService.ListInventories" `  




#### `ListOSPolicyAssignmentReports`

  * **Method** : `google.cloud.osconfig.v1alpha.OsConfigZonalService.ListOSPolicyAssignmentReports`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `osconfig.osPolicyAssignmentReports.list - DATA_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.osconfig.v1alpha.OsConfigZonalService.ListOSPolicyAssignmentReports" `  




#### `ListOSPolicyAssignmentRevisions`

  * **Method** : `google.cloud.osconfig.v1alpha.OsConfigZonalService.ListOSPolicyAssignmentRevisions`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `osconfig.osPolicyAssignments.get - DATA_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.osconfig.v1alpha.OsConfigZonalService.ListOSPolicyAssignmentRevisions" `  




#### `ListOSPolicyAssignments`

  * **Method** : `google.cloud.osconfig.v1alpha.OsConfigZonalService.ListOSPolicyAssignments`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `osconfig.osPolicyAssignments.list - DATA_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.osconfig.v1alpha.OsConfigZonalService.ListOSPolicyAssignments" `  




#### `ListVulnerabilityReports`

  * **Method** : `google.cloud.osconfig.v1alpha.OsConfigZonalService.ListVulnerabilityReports`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `osconfig.vulnerabilityReports.list - DATA_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.osconfig.v1alpha.OsConfigZonalService.ListVulnerabilityReports" `  




#### `UpdateOSPolicyAssignment`

  * **Method** : `google.cloud.osconfig.v1alpha.OsConfigZonalService.UpdateOSPolicyAssignment`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `osconfig.osPolicyAssignments.update - DATA_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.osconfig.v1alpha.OsConfigZonalService.UpdateOSPolicyAssignment" `  




### `google.cloud.osconfig.v1beta.OsConfigService`

The following audit logs are associated with methods belonging to `google.cloud.osconfig.v1beta.OsConfigService`.

#### `CancelPatchJob`

  * **Method** : `google.cloud.osconfig.v1beta.OsConfigService.CancelPatchJob`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `osconfig.patchJobs.exec - DATA_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.osconfig.v1beta.OsConfigService.CancelPatchJob" `  




#### `CreateGuestPolicy`

  * **Method** : `google.cloud.osconfig.v1beta.OsConfigService.CreateGuestPolicy`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `osconfig.guestPolicies.create - DATA_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.osconfig.v1beta.OsConfigService.CreateGuestPolicy" `  




#### `CreatePatchDeployment`

  * **Method** : `google.cloud.osconfig.v1beta.OsConfigService.CreatePatchDeployment`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `osconfig.patchDeployments.create - DATA_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.osconfig.v1beta.OsConfigService.CreatePatchDeployment" `  




#### `DeleteGuestPolicy`

  * **Method** : `google.cloud.osconfig.v1beta.OsConfigService.DeleteGuestPolicy`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `osconfig.guestPolicies.delete - DATA_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.osconfig.v1beta.OsConfigService.DeleteGuestPolicy" `  




#### `DeletePatchDeployment`

  * **Method** : `google.cloud.osconfig.v1beta.OsConfigService.DeletePatchDeployment`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `osconfig.patchDeployments.delete - DATA_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.osconfig.v1beta.OsConfigService.DeletePatchDeployment" `  




#### `ExecutePatchJob`

  * **Method** : `google.cloud.osconfig.v1beta.OsConfigService.ExecutePatchJob`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `osconfig.patchJobs.exec - DATA_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.osconfig.v1beta.OsConfigService.ExecutePatchJob" `  




#### `GetGuestPolicy`

  * **Method** : `google.cloud.osconfig.v1beta.OsConfigService.GetGuestPolicy`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `osconfig.guestPolicies.get - DATA_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.osconfig.v1beta.OsConfigService.GetGuestPolicy" `  




#### `GetPatchDeployment`

  * **Method** : `google.cloud.osconfig.v1beta.OsConfigService.GetPatchDeployment`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `osconfig.patchDeployments.get - DATA_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.osconfig.v1beta.OsConfigService.GetPatchDeployment" `  




#### `GetPatchJob`

  * **Method** : `google.cloud.osconfig.v1beta.OsConfigService.GetPatchJob`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `osconfig.patchJobs.get - DATA_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.osconfig.v1beta.OsConfigService.GetPatchJob" `  




#### `ListGuestPolicies`

  * **Method** : `google.cloud.osconfig.v1beta.OsConfigService.ListGuestPolicies`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `osconfig.guestPolicies.list - DATA_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.osconfig.v1beta.OsConfigService.ListGuestPolicies" `  




#### `ListPatchDeployments`

  * **Method** : `google.cloud.osconfig.v1beta.OsConfigService.ListPatchDeployments`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `osconfig.patchDeployments.list - DATA_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.osconfig.v1beta.OsConfigService.ListPatchDeployments" `  




#### `ListPatchJobInstanceDetails`

  * **Method** : `google.cloud.osconfig.v1beta.OsConfigService.ListPatchJobInstanceDetails`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `osconfig.patchJobs.get - DATA_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.osconfig.v1beta.OsConfigService.ListPatchJobInstanceDetails" `  




#### `ListPatchJobs`

  * **Method** : `google.cloud.osconfig.v1beta.OsConfigService.ListPatchJobs`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `osconfig.patchJobs.list - DATA_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.osconfig.v1beta.OsConfigService.ListPatchJobs" `  




#### `PausePatchDeployment`

  * **Method** : `google.cloud.osconfig.v1beta.OsConfigService.PausePatchDeployment`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `osconfig.patchDeployments.pause - DATA_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.osconfig.v1beta.OsConfigService.PausePatchDeployment" `  




#### `ResumePatchDeployment`

  * **Method** : `google.cloud.osconfig.v1beta.OsConfigService.ResumePatchDeployment`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `osconfig.patchDeployments.resume - DATA_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.osconfig.v1beta.OsConfigService.ResumePatchDeployment" `  




#### `UpdateGuestPolicy`

  * **Method** : `google.cloud.osconfig.v1beta.OsConfigService.UpdateGuestPolicy`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `osconfig.guestPolicies.update - DATA_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.osconfig.v1beta.OsConfigService.UpdateGuestPolicy" `  




#### `UpdatePatchDeployment`

  * **Method** : `google.cloud.osconfig.v1beta.OsConfigService.UpdatePatchDeployment`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `osconfig.patchDeployments.update - DATA_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.osconfig.v1beta.OsConfigService.UpdatePatchDeployment" `  




### `google.cloud.osconfig.v2.PolicyOrchestratorService`

The following audit logs are associated with methods belonging to `google.cloud.osconfig.v2.PolicyOrchestratorService`.

#### `CreatePolicyOrchestrator`

  * **Method** : `google.cloud.osconfig.v2.PolicyOrchestratorService.CreatePolicyOrchestrator`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `osconfig.policyOrchestrators.create - DATA_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.osconfig.v2.PolicyOrchestratorService.CreatePolicyOrchestrator" `  




#### `CreatePolicyOrchestratorForFolder`

  * **Method** : `google.cloud.osconfig.v2.PolicyOrchestratorService.CreatePolicyOrchestratorForFolder`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `osconfig.policyOrchestrators.create - DATA_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.osconfig.v2.PolicyOrchestratorService.CreatePolicyOrchestratorForFolder" `  




#### `CreatePolicyOrchestratorForOrganization`

  * **Method** : `google.cloud.osconfig.v2.PolicyOrchestratorService.CreatePolicyOrchestratorForOrganization`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `osconfig.policyOrchestrators.create - DATA_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.osconfig.v2.PolicyOrchestratorService.CreatePolicyOrchestratorForOrganization" `  




#### `DeletePolicyOrchestrator`

  * **Method** : `google.cloud.osconfig.v2.PolicyOrchestratorService.DeletePolicyOrchestrator`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `osconfig.policyOrchestrators.delete - DATA_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.osconfig.v2.PolicyOrchestratorService.DeletePolicyOrchestrator" `  




#### `DeletePolicyOrchestratorForFolder`

  * **Method** : `google.cloud.osconfig.v2.PolicyOrchestratorService.DeletePolicyOrchestratorForFolder`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `osconfig.policyOrchestrators.delete - DATA_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.osconfig.v2.PolicyOrchestratorService.DeletePolicyOrchestratorForFolder" `  




#### `DeletePolicyOrchestratorForOrganization`

  * **Method** : `google.cloud.osconfig.v2.PolicyOrchestratorService.DeletePolicyOrchestratorForOrganization`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `osconfig.policyOrchestrators.delete - DATA_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.osconfig.v2.PolicyOrchestratorService.DeletePolicyOrchestratorForOrganization" `  




#### `GetPolicyOrchestrator`

  * **Method** : `google.cloud.osconfig.v2.PolicyOrchestratorService.GetPolicyOrchestrator`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `osconfig.policyOrchestrators.get - DATA_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.osconfig.v2.PolicyOrchestratorService.GetPolicyOrchestrator" `  




#### `GetPolicyOrchestratorForFolder`

  * **Method** : `google.cloud.osconfig.v2.PolicyOrchestratorService.GetPolicyOrchestratorForFolder`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `osconfig.policyOrchestrators.get - DATA_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.osconfig.v2.PolicyOrchestratorService.GetPolicyOrchestratorForFolder" `  




#### `GetPolicyOrchestratorForOrganization`

  * **Method** : `google.cloud.osconfig.v2.PolicyOrchestratorService.GetPolicyOrchestratorForOrganization`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `osconfig.policyOrchestrators.get - DATA_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.osconfig.v2.PolicyOrchestratorService.GetPolicyOrchestratorForOrganization" `  




#### `ListPolicyOrchestrators`

  * **Method** : `google.cloud.osconfig.v2.PolicyOrchestratorService.ListPolicyOrchestrators`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `osconfig.policyOrchestrators.list - DATA_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.osconfig.v2.PolicyOrchestratorService.ListPolicyOrchestrators" `  




#### `ListPolicyOrchestratorsForFolder`

  * **Method** : `google.cloud.osconfig.v2.PolicyOrchestratorService.ListPolicyOrchestratorsForFolder`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `osconfig.policyOrchestrators.list - DATA_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.osconfig.v2.PolicyOrchestratorService.ListPolicyOrchestratorsForFolder" `  




#### `ListPolicyOrchestratorsForOrganization`

  * **Method** : `google.cloud.osconfig.v2.PolicyOrchestratorService.ListPolicyOrchestratorsForOrganization`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `osconfig.policyOrchestrators.list - DATA_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.osconfig.v2.PolicyOrchestratorService.ListPolicyOrchestratorsForOrganization" `  




#### `UpdatePolicyOrchestrator`

  * **Method** : `google.cloud.osconfig.v2.PolicyOrchestratorService.UpdatePolicyOrchestrator`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `osconfig.policyOrchestrators.update - DATA_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.osconfig.v2.PolicyOrchestratorService.UpdatePolicyOrchestrator" `  




#### `UpdatePolicyOrchestratorForFolder`

  * **Method** : `google.cloud.osconfig.v2.PolicyOrchestratorService.UpdatePolicyOrchestratorForFolder`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `osconfig.policyOrchestrators.update - DATA_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.osconfig.v2.PolicyOrchestratorService.UpdatePolicyOrchestratorForFolder" `  




#### `UpdatePolicyOrchestratorForOrganization`

  * **Method** : `google.cloud.osconfig.v2.PolicyOrchestratorService.UpdatePolicyOrchestratorForOrganization`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `osconfig.policyOrchestrators.update - DATA_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.osconfig.v2.PolicyOrchestratorService.UpdatePolicyOrchestratorForOrganization" `  




### `google.cloud.osconfig.v2beta.PolicyOrchestratorService`

The following audit logs are associated with methods belonging to `google.cloud.osconfig.v2beta.PolicyOrchestratorService`.

#### `CreatePolicyOrchestrator`

  * **Method** : `google.cloud.osconfig.v2beta.PolicyOrchestratorService.CreatePolicyOrchestrator`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `osconfig.policyOrchestrators.create - DATA_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.osconfig.v2beta.PolicyOrchestratorService.CreatePolicyOrchestrator" `  




#### `CreatePolicyOrchestratorForFolder`

  * **Method** : `google.cloud.osconfig.v2beta.PolicyOrchestratorService.CreatePolicyOrchestratorForFolder`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `osconfig.policyOrchestrators.create - DATA_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.osconfig.v2beta.PolicyOrchestratorService.CreatePolicyOrchestratorForFolder" `  




#### `CreatePolicyOrchestratorForOrganization`

  * **Method** : `google.cloud.osconfig.v2beta.PolicyOrchestratorService.CreatePolicyOrchestratorForOrganization`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `osconfig.policyOrchestrators.create - DATA_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.osconfig.v2beta.PolicyOrchestratorService.CreatePolicyOrchestratorForOrganization" `  




#### `DeletePolicyOrchestrator`

  * **Method** : `google.cloud.osconfig.v2beta.PolicyOrchestratorService.DeletePolicyOrchestrator`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `osconfig.policyOrchestrators.delete - DATA_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.osconfig.v2beta.PolicyOrchestratorService.DeletePolicyOrchestrator" `  




#### `DeletePolicyOrchestratorForFolder`

  * **Method** : `google.cloud.osconfig.v2beta.PolicyOrchestratorService.DeletePolicyOrchestratorForFolder`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `osconfig.policyOrchestrators.delete - DATA_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.osconfig.v2beta.PolicyOrchestratorService.DeletePolicyOrchestratorForFolder" `  




#### `DeletePolicyOrchestratorForOrganization`

  * **Method** : `google.cloud.osconfig.v2beta.PolicyOrchestratorService.DeletePolicyOrchestratorForOrganization`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `osconfig.policyOrchestrators.delete - DATA_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.osconfig.v2beta.PolicyOrchestratorService.DeletePolicyOrchestratorForOrganization" `  




#### `GetPolicyOrchestrator`

  * **Method** : `google.cloud.osconfig.v2beta.PolicyOrchestratorService.GetPolicyOrchestrator`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `osconfig.policyOrchestrators.get - DATA_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.osconfig.v2beta.PolicyOrchestratorService.GetPolicyOrchestrator" `  




#### `GetPolicyOrchestratorForFolder`

  * **Method** : `google.cloud.osconfig.v2beta.PolicyOrchestratorService.GetPolicyOrchestratorForFolder`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `osconfig.policyOrchestrators.get - DATA_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.osconfig.v2beta.PolicyOrchestratorService.GetPolicyOrchestratorForFolder" `  




#### `GetPolicyOrchestratorForOrganization`

  * **Method** : `google.cloud.osconfig.v2beta.PolicyOrchestratorService.GetPolicyOrchestratorForOrganization`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `osconfig.policyOrchestrators.get - DATA_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.osconfig.v2beta.PolicyOrchestratorService.GetPolicyOrchestratorForOrganization" `  




#### `ListPolicyOrchestrators`

  * **Method** : `google.cloud.osconfig.v2beta.PolicyOrchestratorService.ListPolicyOrchestrators`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `osconfig.policyOrchestrators.list - DATA_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.osconfig.v2beta.PolicyOrchestratorService.ListPolicyOrchestrators" `  




#### `ListPolicyOrchestratorsForFolder`

  * **Method** : `google.cloud.osconfig.v2beta.PolicyOrchestratorService.ListPolicyOrchestratorsForFolder`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `osconfig.policyOrchestrators.list - DATA_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.osconfig.v2beta.PolicyOrchestratorService.ListPolicyOrchestratorsForFolder" `  




#### `ListPolicyOrchestratorsForOrganization`

  * **Method** : `google.cloud.osconfig.v2beta.PolicyOrchestratorService.ListPolicyOrchestratorsForOrganization`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `osconfig.policyOrchestrators.list - DATA_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.osconfig.v2beta.PolicyOrchestratorService.ListPolicyOrchestratorsForOrganization" `  




#### `UpdatePolicyOrchestrator`

  * **Method** : `google.cloud.osconfig.v2beta.PolicyOrchestratorService.UpdatePolicyOrchestrator`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `osconfig.policyOrchestrators.update - DATA_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.osconfig.v2beta.PolicyOrchestratorService.UpdatePolicyOrchestrator" `  




#### `UpdatePolicyOrchestratorForFolder`

  * **Method** : `google.cloud.osconfig.v2beta.PolicyOrchestratorService.UpdatePolicyOrchestratorForFolder`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `osconfig.policyOrchestrators.update - DATA_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.osconfig.v2beta.PolicyOrchestratorService.UpdatePolicyOrchestratorForFolder" `  




#### `UpdatePolicyOrchestratorForOrganization`

  * **Method** : `google.cloud.osconfig.v2beta.PolicyOrchestratorService.UpdatePolicyOrchestratorForOrganization`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `osconfig.policyOrchestrators.update - DATA_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.osconfig.v2beta.PolicyOrchestratorService.UpdatePolicyOrchestratorForOrganization" `  




### `google.longrunning.Operations`

The following audit logs are associated with methods belonging to `google.longrunning.Operations`.

#### `CancelOperation`

  * **Method** : `google.longrunning.OsConfigOperationsService.CancelOperation`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `osconfig.osPolicyAssignments.update - DATA_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.longrunning.OsConfigOperationsService.CancelOperation" `  




#### `DeleteOperation`

  * **Method** : `google.longrunning.Operations.DeleteOperation`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `osconfig.operations.delete - DATA_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.longrunning.Operations.DeleteOperation" `  




#### `GetOperation`

  * **Method** : `google.longrunning.Operations.GetOperation`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `osconfig.instanceTasks.check - DATA_READ`
    * `osconfig.osPolicyAssignments.get - DATA_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.longrunning.Operations.GetOperation" `  




#### `ListOperations`

  * **Method** : `google.longrunning.Operations.ListOperations`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `osconfig.operations.list - DATA_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.longrunning.Operations.ListOperations" `  




## Methods that don't produce audit logs

A method might not produce audit logs for one or more of the following reasons: 

  * It is a high volume method involving significant log generation and storage costs.
  * It has low auditing value.
  * Another audit or platform log already provides method coverage.



The following methods don't produce audit logs:

  * `google.cloud.osconfig.agentendpoint.v1.AgentEndpointService.ReceiveTaskNotification`
  * `google.cloud.osconfig.agentendpoint.v1.AgentEndpointService.RegisterAgent`
  * `google.cloud.osconfig.agentendpoint.v1.AgentEndpointService.ReportInventory`
  * `google.cloud.osconfig.agentendpoint.v1.AgentEndpointService.ReportTaskComplete`
  * `google.cloud.osconfig.agentendpoint.v1.AgentEndpointService.ReportTaskProgress`
  * `google.cloud.osconfig.agentendpoint.v1.AgentEndpointService.StartNextTask`
  * `google.cloud.osconfig.agentendpoint.v1beta.AgentEndpointService.LookupEffectiveGuestPolicy`
  * `google.cloud.osconfig.agentendpoint.v1beta.AgentEndpointService.ReceiveTaskNotification`
  * `google.cloud.osconfig.agentendpoint.v1beta.AgentEndpointService.RegisterAgent`
  * `google.cloud.osconfig.agentendpoint.v1beta.AgentEndpointService.ReportTaskComplete`
  * `google.cloud.osconfig.agentendpoint.v1beta.AgentEndpointService.ReportTaskProgress`
  * `google.cloud.osconfig.agentendpoint.v1beta.AgentEndpointService.StartNextTask`



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
