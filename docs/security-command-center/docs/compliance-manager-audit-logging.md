---
url: https://docs.cloud.google.com/security-command-center/docs/compliance-manager-audit-logging/
title: Compliance Manager audit logging \u00a0|\u00a0 Security Command Center \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T18:14:19.627737+00:00
---

# Compliance Manager audit logging  |  Security Command Center  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/security-command-center/docs/compliance-manager-audit-logging/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Security Command Center ](https://docs.cloud.google.com/security-command-center/docs)
  * [ Guides ](https://docs.cloud.google.com/security-command-center/docs/security-command-center-overview)



Send feedback 

#  Compliance Manager audit logging Stay organized with collections  Save and categorize content based on your preferences. 

Standard, Premium, and Enterprise (Deprecated) [service tiers](https://docs.cloud.google.com/security-command-center/docs/service-tiers) The Security Command Center Enterprise service tier will shut down on May 21, 2027. If your organization uses the Enterprise service tier, then the organization will automatically move to the Premium service tier on or after May 21, 2027. Contact your account representative or a [Google Cloud sales specialist](https://cloud.google.com/contact) if you have questions. 

This document lists the audited methods for Compliance Manager. Google Cloud services generate audit logs that record administrative and access activities within your Google Cloud resources. For more information about Cloud Audit Logs, see the following: 

  * [Types of audit logs](https://docs.cloud.google.com/logging/docs/audit#types)
  * [Audit log entry structure](https://docs.cloud.google.com/logging/docs/audit#audit_log_entry_structure)
  * [Storing and routing audit logs](https://docs.cloud.google.com/logging/docs/audit#storing_and_routing_audit_logs)
  * [Cloud Logging pricing summary](https://docs.cloud.google.com/stackdriver/pricing#logs-pricing-summary)
  * [Enable Data Access audit logs](https://docs.cloud.google.com/logging/docs/audit/configure-data-access)



## Service name

To view the Compliance Manager audit logs, do the following:

  1. In the Google Cloud console, go to the Logs Explorer page:

[Go to Logs Explorer](https://console.cloud.google.com/logs/query)

  2. Copy and paste the following query into the **Query** field of the Logs Explorer, and then click **Run query**.
         
         protoPayload.serviceName="cloudsecuritycompliance.googleapis.com"
           




## Methods by permission type

Each IAM permission has a `type` property, whose value is an enum that can be one of four values: `ADMIN_READ`, `ADMIN_WRITE`, `DATA_READ`, or `DATA_WRITE`. When you call a method, Compliance Manager generates an audit log whose category is dependent on the `type` property of the permission required to perform the method. Methods that require an IAM permission with the `type` property value of `DATA_READ`, `DATA_WRITE`, or `ADMIN_READ` generate [Data Access](https://docs.cloud.google.com/logging/docs/audit#data-access) audit logs. Methods that require an IAM permission with the `type` property value of `ADMIN_WRITE` generate [Admin Activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity) audit logs.

API methods in the following list that are marked with (LRO) are long-running operations (LROs). These methods usually generate two audit log entries: one when the operation starts and another when it ends. For more information see [Audit logs for long-running operations](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro). Permission type | Methods  
---|---  
`ADMIN_READ` | `google.cloud.cloudsecuritycompliance.v1.Audit.GetOperation`  
`google.cloud.cloudsecuritycompliance.v1.Deployment.GetCloudControlDeployment`  
`google.cloud.cloudsecuritycompliance.v1.Deployment.GetFrameworkDeployment`  
`google.cloud.cloudsecuritycompliance.v1.Deployment.ListCloudControlDeployments`  
`google.cloud.cloudsecuritycompliance.v1.Deployment.ListFrameworkDeployments`  
`google.longrunning.Operations.GetOperation`  
`google.longrunning.Operations.ListOperations`  
`ADMIN_WRITE` | `google.cloud.cloudsecuritycompliance.v1.CmEnrollmentService.UpdateCmEnrollment`  
`google.cloud.cloudsecuritycompliance.v1.Config.CreateCloudControl`  
`google.cloud.cloudsecuritycompliance.v1.Config.CreateFramework`  
`google.cloud.cloudsecuritycompliance.v1.Config.DeleteCloudControl`  
`google.cloud.cloudsecuritycompliance.v1.Config.DeleteFramework`  
`google.cloud.cloudsecuritycompliance.v1.Config.UpdateCloudControl`  
`google.cloud.cloudsecuritycompliance.v1.Config.UpdateFramework`  
`google.cloud.cloudsecuritycompliance.v1.Deployment.CreateFrameworkDeployment` (LRO)  
`google.cloud.cloudsecuritycompliance.v1.Deployment.DeleteFrameworkDeployment` (LRO)  
`google.longrunning.Operations.CancelOperation`  
`google.longrunning.Operations.DeleteOperation`  
`DATA_READ` | `google.cloud.cloudsecuritycompliance.v1.Audit.GetFrameworkAudit`  
`google.cloud.cloudsecuritycompliance.v1.Audit.ListFrameworkAudits`  
`google.cloud.cloudsecuritycompliance.v1.CmEnrollmentService.CalculateEffectiveCmEnrollment`  
`google.cloud.cloudsecuritycompliance.v1.Config.GetCloudControl`  
`google.cloud.cloudsecuritycompliance.v1.Config.GetFramework`  
`google.cloud.cloudsecuritycompliance.v1.Config.ListCloudControls`  
`google.cloud.cloudsecuritycompliance.v1.Config.ListFrameworks`  
`google.cloud.cloudsecuritycompliance.v1.Monitoring.AggregateFrameworkComplianceReport`  
`google.cloud.cloudsecuritycompliance.v1.Monitoring.FetchFrameworkComplianceReport`  
`google.cloud.cloudsecuritycompliance.v1.Monitoring.ListControlComplianceSummaries`  
`google.cloud.cloudsecuritycompliance.v1.Monitoring.ListFindingSummaries`  
`google.cloud.cloudsecuritycompliance.v1.Monitoring.ListFrameworkComplianceSummaries`  
`DATA_WRITE` | `google.cloud.cloudsecuritycompliance.v1.Audit.CreateFrameworkAudit` (LRO)  
`google.cloud.cloudsecuritycompliance.v1.Audit.GenerateFrameworkAuditScopeReport`  
  
## API interface audit logs

For information about how and which permissions are evaluated for each method, see the Identity and Access Management documentation for Compliance Manager.

### `google.cloud.cloudsecuritycompliance.v1.Audit`

The following audit logs are associated with methods belonging to `google.cloud.cloudsecuritycompliance.v1.Audit`.

#### `CreateFrameworkAudit`

  * **Method** : `google.cloud.cloudsecuritycompliance.v1.Audit.CreateFrameworkAudit`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `cloudsecuritycompliance.frameworkAudits.create - DATA_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.cloudsecuritycompliance.v1.Audit.CreateFrameworkAudit" `  




#### `GenerateFrameworkAuditScopeReport`

  * **Method** : `google.cloud.cloudsecuritycompliance.v1.Audit.GenerateFrameworkAuditScopeReport`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `cloudsecuritycompliance.auditScopeReports.generate - DATA_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.cloudsecuritycompliance.v1.Audit.GenerateFrameworkAuditScopeReport" `  




#### `GetFrameworkAudit`

  * **Method** : `google.cloud.cloudsecuritycompliance.v1.Audit.GetFrameworkAudit`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `cloudsecuritycompliance.frameworkAudits.get - DATA_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.cloudsecuritycompliance.v1.Audit.GetFrameworkAudit" `  




#### `GetOperation`

  * **Method** : `google.cloud.cloudsecuritycompliance.v1.Audit.GetOperation`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `cloudsecuritycompliance.operations.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.cloudsecuritycompliance.v1.Audit.GetOperation" `  




#### `ListFrameworkAudits`

  * **Method** : `google.cloud.cloudsecuritycompliance.v1.Audit.ListFrameworkAudits`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `cloudsecuritycompliance.frameworkAudits.list - DATA_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.cloudsecuritycompliance.v1.Audit.ListFrameworkAudits" `  




### `google.cloud.cloudsecuritycompliance.v1.CmEnrollmentService`

The following audit logs are associated with methods belonging to `google.cloud.cloudsecuritycompliance.v1.CmEnrollmentService`.

#### `CalculateEffectiveCmEnrollment`

  * **Method** : `google.cloud.cloudsecuritycompliance.v1.CmEnrollmentService.CalculateEffectiveCmEnrollment`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `cloudsecuritycompliance.cmEnrollments.get - DATA_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.cloudsecuritycompliance.v1.CmEnrollmentService.CalculateEffectiveCmEnrollment" `  




#### `UpdateCmEnrollment`

  * **Method** : `google.cloud.cloudsecuritycompliance.v1.CmEnrollmentService.UpdateCmEnrollment`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `cloudsecuritycompliance.cmEnrollments.update - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.cloudsecuritycompliance.v1.CmEnrollmentService.UpdateCmEnrollment" `  




### `google.cloud.cloudsecuritycompliance.v1.Config`

The following audit logs are associated with methods belonging to `google.cloud.cloudsecuritycompliance.v1.Config`.

#### `CreateCloudControl`

  * **Method** : `google.cloud.cloudsecuritycompliance.v1.Config.CreateCloudControl`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `cloudsecuritycompliance.cloudControls.create - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.cloudsecuritycompliance.v1.Config.CreateCloudControl" `  




#### `CreateFramework`

  * **Method** : `google.cloud.cloudsecuritycompliance.v1.Config.CreateFramework`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `cloudsecuritycompliance.frameworks.create - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.cloudsecuritycompliance.v1.Config.CreateFramework" `  




#### `DeleteCloudControl`

  * **Method** : `google.cloud.cloudsecuritycompliance.v1.Config.DeleteCloudControl`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `cloudsecuritycompliance.cloudControls.delete - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.cloudsecuritycompliance.v1.Config.DeleteCloudControl" `  




#### `DeleteFramework`

  * **Method** : `google.cloud.cloudsecuritycompliance.v1.Config.DeleteFramework`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `cloudsecuritycompliance.frameworks.delete - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.cloudsecuritycompliance.v1.Config.DeleteFramework" `  




#### `GetCloudControl`

  * **Method** : `google.cloud.cloudsecuritycompliance.v1.Config.GetCloudControl`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `cloudsecuritycompliance.cloudControls.get - DATA_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.cloudsecuritycompliance.v1.Config.GetCloudControl" `  




#### `GetFramework`

  * **Method** : `google.cloud.cloudsecuritycompliance.v1.Config.GetFramework`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `cloudsecuritycompliance.frameworks.get - DATA_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.cloudsecuritycompliance.v1.Config.GetFramework" `  




#### `ListCloudControls`

  * **Method** : `google.cloud.cloudsecuritycompliance.v1.Config.ListCloudControls`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `cloudsecuritycompliance.cloudControls.list - DATA_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.cloudsecuritycompliance.v1.Config.ListCloudControls" `  




#### `ListFrameworks`

  * **Method** : `google.cloud.cloudsecuritycompliance.v1.Config.ListFrameworks`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `cloudsecuritycompliance.frameworks.list - DATA_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.cloudsecuritycompliance.v1.Config.ListFrameworks" `  




#### `UpdateCloudControl`

  * **Method** : `google.cloud.cloudsecuritycompliance.v1.Config.UpdateCloudControl`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `cloudsecuritycompliance.cloudControls.update - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.cloudsecuritycompliance.v1.Config.UpdateCloudControl" `  




#### `UpdateFramework`

  * **Method** : `google.cloud.cloudsecuritycompliance.v1.Config.UpdateFramework`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `cloudsecuritycompliance.frameworks.update - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.cloudsecuritycompliance.v1.Config.UpdateFramework" `  




### `google.cloud.cloudsecuritycompliance.v1.Deployment`

The following audit logs are associated with methods belonging to `google.cloud.cloudsecuritycompliance.v1.Deployment`.

#### `CreateFrameworkDeployment`

  * **Method** : `google.cloud.cloudsecuritycompliance.v1.Deployment.CreateFrameworkDeployment`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `cloudsecuritycompliance.frameworkDeployments.create - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.cloudsecuritycompliance.v1.Deployment.CreateFrameworkDeployment" `  




#### `DeleteFrameworkDeployment`

  * **Method** : `google.cloud.cloudsecuritycompliance.v1.Deployment.DeleteFrameworkDeployment`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `cloudsecuritycompliance.frameworkDeployments.delete - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.cloudsecuritycompliance.v1.Deployment.DeleteFrameworkDeployment" `  




#### `GetCloudControlDeployment`

  * **Method** : `google.cloud.cloudsecuritycompliance.v1.Deployment.GetCloudControlDeployment`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `cloudsecuritycompliance.cloudControlDeployments.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.cloudsecuritycompliance.v1.Deployment.GetCloudControlDeployment" `  




#### `GetFrameworkDeployment`

  * **Method** : `google.cloud.cloudsecuritycompliance.v1.Deployment.GetFrameworkDeployment`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `cloudsecuritycompliance.frameworkDeployments.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.cloudsecuritycompliance.v1.Deployment.GetFrameworkDeployment" `  




#### `ListCloudControlDeployments`

  * **Method** : `google.cloud.cloudsecuritycompliance.v1.Deployment.ListCloudControlDeployments`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `cloudsecuritycompliance.cloudControlDeployments.list - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.cloudsecuritycompliance.v1.Deployment.ListCloudControlDeployments" `  




#### `ListFrameworkDeployments`

  * **Method** : `google.cloud.cloudsecuritycompliance.v1.Deployment.ListFrameworkDeployments`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `cloudsecuritycompliance.frameworkDeployments.list - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.cloudsecuritycompliance.v1.Deployment.ListFrameworkDeployments" `  




### `google.cloud.cloudsecuritycompliance.v1.Monitoring`

The following audit logs are associated with methods belonging to `google.cloud.cloudsecuritycompliance.v1.Monitoring`.

#### `AggregateFrameworkComplianceReport`

  * **Method** : `google.cloud.cloudsecuritycompliance.v1.Monitoring.AggregateFrameworkComplianceReport`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `cloudsecuritycompliance.frameworkComplianceReports.aggregate - DATA_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.cloudsecuritycompliance.v1.Monitoring.AggregateFrameworkComplianceReport" `  




#### `FetchFrameworkComplianceReport`

  * **Method** : `google.cloud.cloudsecuritycompliance.v1.Monitoring.FetchFrameworkComplianceReport`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `cloudsecuritycompliance.frameworkComplianceReports.get - DATA_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.cloudsecuritycompliance.v1.Monitoring.FetchFrameworkComplianceReport" `  




#### `ListControlComplianceSummaries`

  * **Method** : `google.cloud.cloudsecuritycompliance.v1.Monitoring.ListControlComplianceSummaries`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `cloudsecuritycompliance.controlComplianceSummaries.list - DATA_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.cloudsecuritycompliance.v1.Monitoring.ListControlComplianceSummaries" `  




#### `ListFindingSummaries`

  * **Method** : `google.cloud.cloudsecuritycompliance.v1.Monitoring.ListFindingSummaries`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `cloudsecuritycompliance.findingSummaries.list - DATA_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.cloudsecuritycompliance.v1.Monitoring.ListFindingSummaries" `  




#### `ListFrameworkComplianceSummaries`

  * **Method** : `google.cloud.cloudsecuritycompliance.v1.Monitoring.ListFrameworkComplianceSummaries`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `cloudsecuritycompliance.frameworkComplianceSummaries.list - DATA_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.cloudsecuritycompliance.v1.Monitoring.ListFrameworkComplianceSummaries" `  




### `google.longrunning.Operations`

The following audit logs are associated with methods belonging to `google.longrunning.Operations`.

#### `CancelOperation`

  * **Method** : `google.longrunning.Operations.CancelOperation`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `cloudsecuritycompliance.operations.cancel - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.longrunning.Operations.CancelOperation" `  




#### `DeleteOperation`

  * **Method** : `google.longrunning.Operations.DeleteOperation`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `cloudsecuritycompliance.operations.delete - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.longrunning.Operations.DeleteOperation" `  




#### `GetOperation`

  * **Method** : `google.longrunning.Operations.GetOperation`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `cloudsecuritycompliance.operations.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.longrunning.Operations.GetOperation" `  




#### `ListOperations`

  * **Method** : `google.longrunning.Operations.ListOperations`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `cloudsecuritycompliance.operations.list - ADMIN_READ`
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



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
