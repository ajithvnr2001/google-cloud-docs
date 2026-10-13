---
url: https://docs.cloud.google.com/security-command-center/docs/audit-logging/
title: Security Command Center audit logging \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T18:14:19.156118+00:00
---

# Security Command Center audit logging  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/security-command-center/docs/audit-logging/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Security Command Center ](https://docs.cloud.google.com/security-command-center/docs)
  * [ Guides ](https://docs.cloud.google.com/security-command-center/docs/security-command-center-overview)



Send feedback 

#  Security Command Center audit logging Stay organized with collections  Save and categorize content based on your preferences. 

Standard-legacy, Standard, Premium, and Enterprise (Deprecated) [service tiers](https://docs.cloud.google.com/security-command-center/docs/service-tiers) The Security Command Center Enterprise service tier will shut down on May 21, 2027. If your organization uses the Enterprise service tier, then the organization will automatically move to the Premium service tier on or after May 21, 2027. Contact your account representative or a [Google Cloud sales specialist](https://cloud.google.com/contact) if you have questions. 

This document lists the audited methods for Security Command Center. Google Cloud services generate audit logs that record administrative and access activities within your Google Cloud resources. For more information about Cloud Audit Logs, see the following: 

  * [Types of audit logs](https://docs.cloud.google.com/logging/docs/audit#types)
  * [Audit log entry structure](https://docs.cloud.google.com/logging/docs/audit#audit_log_entry_structure)
  * [Storing and routing audit logs](https://docs.cloud.google.com/logging/docs/audit#storing_and_routing_audit_logs)
  * [Cloud Logging pricing summary](https://docs.cloud.google.com/stackdriver/pricing#logs-pricing-summary)
  * [Enable Data Access audit logs](https://docs.cloud.google.com/logging/docs/audit/configure-data-access)



## Notes

Depending on the level at which Security Command Center is activated—project level or organization level—certain operations in the following sections might or might not appear in the audit logs.

## Service name

To view the Security Command Center audit logs, do the following:

  1. In the Google Cloud console, go to the Logs Explorer page:

[Go to Logs Explorer](https://console.cloud.google.com/logs/query)

  2. Copy and paste the following query into the **Query** field of the Logs Explorer, and then click **Run query**.
         
         protoPayload.serviceName="securitycenter.googleapis.com"
           




## Methods by permission type

Each IAM permission has a `type` property, whose value is an enum that can be one of four values: `ADMIN_READ`, `ADMIN_WRITE`, `DATA_READ`, or `DATA_WRITE`. When you call a method, Security Command Center generates an audit log whose category is dependent on the `type` property of the permission required to perform the method. Methods that require an IAM permission with the `type` property value of `DATA_READ`, `DATA_WRITE`, or `ADMIN_READ` generate [Data Access](https://docs.cloud.google.com/logging/docs/audit#data-access) audit logs. Methods that require an IAM permission with the `type` property value of `ADMIN_WRITE` generate [Admin Activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity) audit logs.

API methods in the following list that are marked with (LRO) are long-running operations (LROs). These methods usually generate two audit log entries: one when the operation starts and another when it ends. For more information see [Audit logs for long-running operations](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro). Permission type | Methods  
---|---  
`ADMIN_READ` | `google.cloud.securitycenter.settings.v1beta2.Settings.CalculateContainerThreatDetectionSettings`  
`google.cloud.securitycenter.settings.v1beta2.Settings.CalculateEventThreatDetectionSettings`  
`google.cloud.securitycenter.settings.v1beta2.Settings.CalculateRapidVulnerabilityDetectionSettings`  
`google.cloud.securitycenter.settings.v1beta2.Settings.CalculateSecurityHealthAnalyticsSettings`  
`google.cloud.securitycenter.settings.v1beta2.Settings.CalculateVirtualMachineThreatDetectionSettings`  
`google.cloud.securitycenter.settings.v1beta2.Settings.CalculateWebSecurityScannerSettings`  
`google.cloud.securitycenter.settings.v1beta2.Settings.GetContainerThreatDetectionSettings`  
`google.cloud.securitycenter.settings.v1beta2.Settings.GetEventThreatDetectionSettings`  
`google.cloud.securitycenter.settings.v1beta2.Settings.GetRapidVulnerabilityDetectionSettings`  
`google.cloud.securitycenter.settings.v1beta2.Settings.GetSecurityCenterSettings`  
`google.cloud.securitycenter.settings.v1beta2.Settings.GetSecurityHealthAnalyticsSettings`  
`google.cloud.securitycenter.settings.v1beta2.Settings.GetSubscription`  
`google.cloud.securitycenter.settings.v1beta2.Settings.GetVirtualMachineThreatDetectionSettings`  
`google.cloud.securitycenter.settings.v1beta2.Settings.GetWebSecurityScannerSettings`  
`google.cloud.securitycenter.v1.SecurityCenter.GetBigQueryExport`  
`google.cloud.securitycenter.v1.SecurityCenter.GetEffectiveEventThreatDetectionCustomModule`  
`google.cloud.securitycenter.v1.SecurityCenter.GetEffectiveSecurityHealthAnalyticsCustomModule`  
`google.cloud.securitycenter.v1.SecurityCenter.GetEventThreatDetectionCustomModule`  
`google.cloud.securitycenter.v1.SecurityCenter.GetIamPolicy`  
`google.cloud.securitycenter.v1.SecurityCenter.GetMuteConfig`  
`google.cloud.securitycenter.v1.SecurityCenter.GetOrganizationSettings`  
`google.cloud.securitycenter.v1.SecurityCenter.GetResourceValueConfig`  
`google.cloud.securitycenter.v1.SecurityCenter.GetSecurityHealthAnalyticsCustomModule`  
`google.cloud.securitycenter.v1.SecurityCenter.GetValuedResource`  
`google.cloud.securitycenter.v1.SecurityCenter.ListBigQueryExports`  
`google.cloud.securitycenter.v1.SecurityCenter.ListDescendantEventThreatDetectionCustomModules`  
`google.cloud.securitycenter.v1.SecurityCenter.ListDescendantSecurityHealthAnalyticsCustomModules`  
`google.cloud.securitycenter.v1.SecurityCenter.ListEffectiveEventThreatDetectionCustomModules`  
`google.cloud.securitycenter.v1.SecurityCenter.ListEffectiveSecurityHealthAnalyticsCustomModules`  
`google.cloud.securitycenter.v1.SecurityCenter.ListEventThreatDetectionCustomModules`  
`google.cloud.securitycenter.v1.SecurityCenter.ListMuteConfigs`  
`google.cloud.securitycenter.v1.SecurityCenter.ListResourceValueConfigs`  
`google.cloud.securitycenter.v1.SecurityCenter.ListSecurityHealthAnalyticsCustomModules`  
`google.cloud.securitycenter.v1.SecurityCenter.SimulateSecurityHealthAnalyticsCustomModule`  
`google.cloud.securitycenter.v1.SecurityCenter.ValidateEventThreatDetectionCustomModule`  
`google.cloud.securitycenter.v1beta1.SecurityCenter.GetIamPolicy`  
`google.cloud.securitycenter.v1beta1.SecurityCenter.GetOrganizationSettings`  
`google.cloud.securitycenter.v1p1beta1.SecurityCenter.GetIamPolicy`  
`google.cloud.securitycenter.v1p1beta1.SecurityCenter.GetOrganizationSettings`  
`google.cloud.securitycenter.v2.SecurityCenter.GetBigQueryExport`  
`google.cloud.securitycenter.v2.SecurityCenter.GetIamPolicy`  
`google.cloud.securitycenter.v2.SecurityCenter.GetMuteConfig`  
`google.cloud.securitycenter.v2.SecurityCenter.GetResourceValueConfig`  
`google.cloud.securitycenter.v2.SecurityCenter.GetValuedResource`  
`google.cloud.securitycenter.v2.SecurityCenter.ListBigQueryExports`  
`google.cloud.securitycenter.v2.SecurityCenter.ListMuteConfigs`  
`google.cloud.securitycenter.v2.SecurityCenter.ListResourceValueConfigs`  
`ADMIN_WRITE` | `google.cloud.securitycenter.settings.v1beta2.Settings.UpdateContainerThreatDetectionSettings`  
`google.cloud.securitycenter.settings.v1beta2.Settings.UpdateEventThreatDetectionSettings`  
`google.cloud.securitycenter.settings.v1beta2.Settings.UpdateRapidVulnerabilityDetectionSettings`  
`google.cloud.securitycenter.settings.v1beta2.Settings.UpdateSecurityHealthAnalyticsSettings`  
`google.cloud.securitycenter.settings.v1beta2.Settings.UpdateVirtualMachineThreatDetectionSettings`  
`google.cloud.securitycenter.settings.v1beta2.Settings.UpdateWebSecurityScannerSettings`  
`google.cloud.securitycenter.v1.SecurityCenter.BatchCreateResourceValueConfigs`  
`google.cloud.securitycenter.v1.SecurityCenter.CreateBigQueryExport`  
`google.cloud.securitycenter.v1.SecurityCenter.CreateEventThreatDetectionCustomModule`  
`google.cloud.securitycenter.v1.SecurityCenter.CreateMuteConfig`  
`google.cloud.securitycenter.v1.SecurityCenter.CreateSecurityHealthAnalyticsCustomModule`  
`google.cloud.securitycenter.v1.SecurityCenter.DeleteBigQueryExport`  
`google.cloud.securitycenter.v1.SecurityCenter.DeleteEventThreatDetectionCustomModule`  
`google.cloud.securitycenter.v1.SecurityCenter.DeleteMuteConfig`  
`google.cloud.securitycenter.v1.SecurityCenter.DeleteResourceValueConfig`  
`google.cloud.securitycenter.v1.SecurityCenter.DeleteSecurityHealthAnalyticsCustomModule`  
`google.cloud.securitycenter.v1.SecurityCenter.SetIamPolicy`  
`google.cloud.securitycenter.v1.SecurityCenter.UpdateBigQueryExport`  
`google.cloud.securitycenter.v1.SecurityCenter.UpdateEventThreatDetectionCustomModule`  
`google.cloud.securitycenter.v1.SecurityCenter.UpdateMuteConfig`  
`google.cloud.securitycenter.v1.SecurityCenter.UpdateOrganizationSettings`  
`google.cloud.securitycenter.v1.SecurityCenter.UpdateResourceValueConfig`  
`google.cloud.securitycenter.v1.SecurityCenter.UpdateSecurityHealthAnalyticsCustomModule`  
`google.cloud.securitycenter.v1beta1.SecurityCenter.SetIamPolicy`  
`google.cloud.securitycenter.v1beta1.SecurityCenter.UpdateOrganizationSettings`  
`google.cloud.securitycenter.v1p1beta1.SecurityCenter.SetIamPolicy`  
`google.cloud.securitycenter.v1p1beta1.SecurityCenter.UpdateOrganizationSettings`  
`google.cloud.securitycenter.v2.SecurityCenter.BatchCreateResourceValueConfigs`  
`google.cloud.securitycenter.v2.SecurityCenter.CreateBigQueryExport`  
`google.cloud.securitycenter.v2.SecurityCenter.CreateMuteConfig`  
`google.cloud.securitycenter.v2.SecurityCenter.DeleteBigQueryExport`  
`google.cloud.securitycenter.v2.SecurityCenter.DeleteMuteConfig`  
`google.cloud.securitycenter.v2.SecurityCenter.DeleteResourceValueConfig`  
`google.cloud.securitycenter.v2.SecurityCenter.SetIamPolicy`  
`google.cloud.securitycenter.v2.SecurityCenter.UpdateBigQueryExport`  
`google.cloud.securitycenter.v2.SecurityCenter.UpdateMuteConfig`  
`google.cloud.securitycenter.v2.SecurityCenter.UpdateResourceValueConfig`  
`DATA_READ` | `google.cloud.securitycenter.v1.SecurityCenter.GetNotificationConfig`  
`google.cloud.securitycenter.v1.SecurityCenter.GetSimulation`  
`google.cloud.securitycenter.v1.SecurityCenter.GetSource`  
`google.cloud.securitycenter.v1.SecurityCenter.GroupAssets`  
`google.cloud.securitycenter.v1.SecurityCenter.GroupFindings`  
`google.cloud.securitycenter.v1.SecurityCenter.ListAssets`  
`google.cloud.securitycenter.v1.SecurityCenter.ListAttackPaths`  
`google.cloud.securitycenter.v1.SecurityCenter.ListFindings`  
`google.cloud.securitycenter.v1.SecurityCenter.ListNotificationConfigs`  
`google.cloud.securitycenter.v1.SecurityCenter.ListSources`  
`google.cloud.securitycenter.v1.SecurityCenter.ListValuedResources`  
`google.cloud.securitycenter.v1beta1.SecurityCenter.GetSource`  
`google.cloud.securitycenter.v1beta1.SecurityCenter.GroupFindings`  
`google.cloud.securitycenter.v1beta1.SecurityCenter.ListAssets`  
`google.cloud.securitycenter.v1beta1.SecurityCenter.ListFindings`  
`google.cloud.securitycenter.v1beta1.SecurityCenter.ListSources`  
`google.cloud.securitycenter.v1p1beta1.SecurityCenter.GetNotificationConfig`  
`google.cloud.securitycenter.v1p1beta1.SecurityCenter.GetSource`  
`google.cloud.securitycenter.v1p1beta1.SecurityCenter.GroupAssets`  
`google.cloud.securitycenter.v1p1beta1.SecurityCenter.GroupFindings`  
`google.cloud.securitycenter.v1p1beta1.SecurityCenter.ListAssets`  
`google.cloud.securitycenter.v1p1beta1.SecurityCenter.ListFindings`  
`google.cloud.securitycenter.v1p1beta1.SecurityCenter.ListNotificationConfigs`  
`google.cloud.securitycenter.v1p1beta1.SecurityCenter.ListSources`  
`google.cloud.securitycenter.v2.SecurityCenter.GetNotificationConfig`  
`google.cloud.securitycenter.v2.SecurityCenter.GetSimulation`  
`google.cloud.securitycenter.v2.SecurityCenter.GetSource`  
`google.cloud.securitycenter.v2.SecurityCenter.GroupFindings`  
`google.cloud.securitycenter.v2.SecurityCenter.ListAttackPaths`  
`google.cloud.securitycenter.v2.SecurityCenter.ListFindings`  
`google.cloud.securitycenter.v2.SecurityCenter.ListNotificationConfigs`  
`google.cloud.securitycenter.v2.SecurityCenter.ListSources`  
`google.cloud.securitycenter.v2.SecurityCenter.ListValuedResources`  
`DATA_WRITE` | `google.cloud.securitycenter.v1.SecurityCenter.BulkMuteFindings` (LRO)  
`google.cloud.securitycenter.v1.SecurityCenter.CreateFinding`  
`google.cloud.securitycenter.v1.SecurityCenter.CreateNotificationConfig`  
`google.cloud.securitycenter.v1.SecurityCenter.CreateSource`  
`google.cloud.securitycenter.v1.SecurityCenter.DeleteNotificationConfig`  
`google.cloud.securitycenter.v1.SecurityCenter.SetFindingState`  
`google.cloud.securitycenter.v1.SecurityCenter.SetMute`  
`google.cloud.securitycenter.v1.SecurityCenter.UpdateExternalSystem`  
`google.cloud.securitycenter.v1.SecurityCenter.UpdateFinding`  
`google.cloud.securitycenter.v1.SecurityCenter.UpdateNotificationConfig`  
`google.cloud.securitycenter.v1.SecurityCenter.UpdateSecurityMarks`  
`google.cloud.securitycenter.v1.SecurityCenter.UpdateSource`  
`google.cloud.securitycenter.v1beta1.SecurityCenter.CreateFinding`  
`google.cloud.securitycenter.v1beta1.SecurityCenter.CreateSource`  
`google.cloud.securitycenter.v1beta1.SecurityCenter.SetFindingState`  
`google.cloud.securitycenter.v1beta1.SecurityCenter.UpdateFinding`  
`google.cloud.securitycenter.v1beta1.SecurityCenter.UpdateSecurityMarks`  
`google.cloud.securitycenter.v1beta1.SecurityCenter.UpdateSource`  
`google.cloud.securitycenter.v1p1beta1.SecurityCenter.CreateFinding`  
`google.cloud.securitycenter.v1p1beta1.SecurityCenter.CreateNotificationConfig`  
`google.cloud.securitycenter.v1p1beta1.SecurityCenter.CreateSource`  
`google.cloud.securitycenter.v1p1beta1.SecurityCenter.DeleteNotificationConfig`  
`google.cloud.securitycenter.v1p1beta1.SecurityCenter.SetFindingState`  
`google.cloud.securitycenter.v1p1beta1.SecurityCenter.UpdateFinding`  
`google.cloud.securitycenter.v1p1beta1.SecurityCenter.UpdateNotificationConfig`  
`google.cloud.securitycenter.v1p1beta1.SecurityCenter.UpdateSecurityMarks`  
`google.cloud.securitycenter.v1p1beta1.SecurityCenter.UpdateSource`  
`google.cloud.securitycenter.v2.SecurityCenter.BulkMuteFindings` (LRO)  
`google.cloud.securitycenter.v2.SecurityCenter.CreateFinding`  
`google.cloud.securitycenter.v2.SecurityCenter.CreateNotificationConfig`  
`google.cloud.securitycenter.v2.SecurityCenter.CreateSource`  
`google.cloud.securitycenter.v2.SecurityCenter.DeleteNotificationConfig`  
`google.cloud.securitycenter.v2.SecurityCenter.ExportFindings` (LRO)  
`google.cloud.securitycenter.v2.SecurityCenter.SetFindingState`  
`google.cloud.securitycenter.v2.SecurityCenter.SetMute`  
`google.cloud.securitycenter.v2.SecurityCenter.UpdateExternalSystem`  
`google.cloud.securitycenter.v2.SecurityCenter.UpdateFinding`  
`google.cloud.securitycenter.v2.SecurityCenter.UpdateNotificationConfig`  
`google.cloud.securitycenter.v2.SecurityCenter.UpdateSecurityMarks`  
`google.cloud.securitycenter.v2.SecurityCenter.UpdateSource`  
  
## API interface audit logs

For information about how and which permissions are evaluated for each method, see the [Identity and Access Management documentation](https://docs.cloud.google.com/security-command-center/docs/access-control) for Security Command Center.

### `google.cloud.securitycenter.settings.v1beta2.Settings`

The following audit logs are associated with methods belonging to `google.cloud.securitycenter.settings.v1beta2.Settings`.

#### `CalculateContainerThreatDetectionSettings`

  * **Method** : `google.cloud.securitycenter.settings.v1beta2.Settings.CalculateContainerThreatDetectionSettings`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `securitycenter.containerthreatdetectionsettings.calculate - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.securitycenter.settings.v1beta2.Settings.CalculateContainerThreatDetectionSettings" `  




#### `CalculateEventThreatDetectionSettings`

  * **Method** : `google.cloud.securitycenter.settings.v1beta2.Settings.CalculateEventThreatDetectionSettings`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `securitycenter.eventthreatdetectionsettings.calculate - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.securitycenter.settings.v1beta2.Settings.CalculateEventThreatDetectionSettings" `  




#### `CalculateRapidVulnerabilityDetectionSettings`

  * **Method** : `google.cloud.securitycenter.settings.v1beta2.Settings.CalculateRapidVulnerabilityDetectionSettings`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `securitycenter.rapidvulnerabilitydetectionsettings.calculate - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.securitycenter.settings.v1beta2.Settings.CalculateRapidVulnerabilityDetectionSettings" `  




#### `CalculateSecurityHealthAnalyticsSettings`

  * **Method** : `google.cloud.securitycenter.settings.v1beta2.Settings.CalculateSecurityHealthAnalyticsSettings`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `securitycenter.securityhealthanalyticssettings.calculate - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.securitycenter.settings.v1beta2.Settings.CalculateSecurityHealthAnalyticsSettings" `  




#### `CalculateVirtualMachineThreatDetectionSettings`

  * **Method** : `google.cloud.securitycenter.settings.v1beta2.Settings.CalculateVirtualMachineThreatDetectionSettings`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `securitycenter.virtualmachinethreatdetectionsettings.calculate - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.securitycenter.settings.v1beta2.Settings.CalculateVirtualMachineThreatDetectionSettings" `  




#### `CalculateWebSecurityScannerSettings`

  * **Method** : `google.cloud.securitycenter.settings.v1beta2.Settings.CalculateWebSecurityScannerSettings`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `securitycenter.websecurityscannersettings.calculate - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.securitycenter.settings.v1beta2.Settings.CalculateWebSecurityScannerSettings" `  




#### `GetContainerThreatDetectionSettings`

  * **Method** : `google.cloud.securitycenter.settings.v1beta2.Settings.GetContainerThreatDetectionSettings`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `securitycenter.containerthreatdetectionsettings.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.securitycenter.settings.v1beta2.Settings.GetContainerThreatDetectionSettings" `  




#### `GetEventThreatDetectionSettings`

  * **Method** : `google.cloud.securitycenter.settings.v1beta2.Settings.GetEventThreatDetectionSettings`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `securitycenter.eventthreatdetectionsettings.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.securitycenter.settings.v1beta2.Settings.GetEventThreatDetectionSettings" `  




#### `GetRapidVulnerabilityDetectionSettings`

  * **Method** : `google.cloud.securitycenter.settings.v1beta2.Settings.GetRapidVulnerabilityDetectionSettings`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `securitycenter.rapidvulnerabilitydetectionsettings.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.securitycenter.settings.v1beta2.Settings.GetRapidVulnerabilityDetectionSettings" `  




#### `GetSecurityCenterSettings`

  * **Method** : `google.cloud.securitycenter.settings.v1beta2.Settings.GetSecurityCenterSettings`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `securitycenter.securitycentersettings.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.securitycenter.settings.v1beta2.Settings.GetSecurityCenterSettings" `  




#### `GetSecurityHealthAnalyticsSettings`

  * **Method** : `google.cloud.securitycenter.settings.v1beta2.Settings.GetSecurityHealthAnalyticsSettings`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `securitycenter.securityhealthanalyticssettings.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.securitycenter.settings.v1beta2.Settings.GetSecurityHealthAnalyticsSettings" `  




#### `GetSubscription`

  * **Method** : `google.cloud.securitycenter.settings.v1beta2.Settings.GetSubscription`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `securitycenter.subscription.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.securitycenter.settings.v1beta2.Settings.GetSubscription" `  




#### `GetVirtualMachineThreatDetectionSettings`

  * **Method** : `google.cloud.securitycenter.settings.v1beta2.Settings.GetVirtualMachineThreatDetectionSettings`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `securitycenter.virtualmachinethreatdetectionsettings.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.securitycenter.settings.v1beta2.Settings.GetVirtualMachineThreatDetectionSettings" `  




#### `GetWebSecurityScannerSettings`

  * **Method** : `google.cloud.securitycenter.settings.v1beta2.Settings.GetWebSecurityScannerSettings`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `securitycenter.websecurityscannersettings.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.securitycenter.settings.v1beta2.Settings.GetWebSecurityScannerSettings" `  




#### `UpdateContainerThreatDetectionSettings`

  * **Method** : `google.cloud.securitycenter.settings.v1beta2.Settings.UpdateContainerThreatDetectionSettings`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `securitycenter.containerthreatdetectionsettings.update - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.securitycenter.settings.v1beta2.Settings.UpdateContainerThreatDetectionSettings" `  




#### `UpdateEventThreatDetectionSettings`

  * **Method** : `google.cloud.securitycenter.settings.v1beta2.Settings.UpdateEventThreatDetectionSettings`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `securitycenter.eventthreatdetectionsettings.update - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.securitycenter.settings.v1beta2.Settings.UpdateEventThreatDetectionSettings" `  




#### `UpdateRapidVulnerabilityDetectionSettings`

  * **Method** : `google.cloud.securitycenter.settings.v1beta2.Settings.UpdateRapidVulnerabilityDetectionSettings`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `securitycenter.rapidvulnerabilitydetectionsettings.update - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.securitycenter.settings.v1beta2.Settings.UpdateRapidVulnerabilityDetectionSettings" `  




#### `UpdateSecurityHealthAnalyticsSettings`

  * **Method** : `google.cloud.securitycenter.settings.v1beta2.Settings.UpdateSecurityHealthAnalyticsSettings`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `securitycenter.securityhealthanalyticssettings.update - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.securitycenter.settings.v1beta2.Settings.UpdateSecurityHealthAnalyticsSettings" `  




#### `UpdateVirtualMachineThreatDetectionSettings`

  * **Method** : `google.cloud.securitycenter.settings.v1beta2.Settings.UpdateVirtualMachineThreatDetectionSettings`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `securitycenter.virtualmachinethreatdetectionsettings.update - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.securitycenter.settings.v1beta2.Settings.UpdateVirtualMachineThreatDetectionSettings" `  




#### `UpdateWebSecurityScannerSettings`

  * **Method** : `google.cloud.securitycenter.settings.v1beta2.Settings.UpdateWebSecurityScannerSettings`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `securitycenter.websecurityscannersettings.update - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.securitycenter.settings.v1beta2.Settings.UpdateWebSecurityScannerSettings" `  




### `google.cloud.securitycenter.v1.SecurityCenter`

The following audit logs are associated with methods belonging to `google.cloud.securitycenter.v1.SecurityCenter`.

#### `BatchCreateResourceValueConfigs`

  * **Method** : `google.cloud.securitycenter.v1.SecurityCenter.BatchCreateResourceValueConfigs`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `securitycenter.resourcevalueconfigs.create - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.securitycenter.v1.SecurityCenter.BatchCreateResourceValueConfigs" `  




#### `BulkMuteFindings`

  * **Method** : `google.cloud.securitycenter.v1.SecurityCenter.BulkMuteFindings`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `securitycenter.findings.bulkMuteUpdate - DATA_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.securitycenter.v1.SecurityCenter.BulkMuteFindings" `  




#### `CreateBigQueryExport`

  * **Method** : `google.cloud.securitycenter.v1.SecurityCenter.CreateBigQueryExport`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `securitycenter.bigQueryExports.create - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.securitycenter.v1.SecurityCenter.CreateBigQueryExport" `  




#### `CreateEventThreatDetectionCustomModule`

  * **Method** : `google.cloud.securitycenter.v1.SecurityCenter.CreateEventThreatDetectionCustomModule`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `securitycenter.eventthreatdetectioncustommodules.create - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.securitycenter.v1.SecurityCenter.CreateEventThreatDetectionCustomModule" `  




#### `CreateFinding`

  * **Method** : `google.cloud.securitycenter.v1.SecurityCenter.CreateFinding`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `securitycenter.findings.update - DATA_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.securitycenter.v1.SecurityCenter.CreateFinding" `  




#### `CreateMuteConfig`

  * **Method** : `google.cloud.securitycenter.v1.SecurityCenter.CreateMuteConfig`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `securitycenter.muteconfigs.create - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.securitycenter.v1.SecurityCenter.CreateMuteConfig" `  




#### `CreateNotificationConfig`

  * **Method** : `google.cloud.securitycenter.v1.SecurityCenter.CreateNotificationConfig`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `securitycenter.notificationconfig.create - DATA_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.securitycenter.v1.SecurityCenter.CreateNotificationConfig" `  




#### `CreateSecurityHealthAnalyticsCustomModule`

  * **Method** : `google.cloud.securitycenter.v1.SecurityCenter.CreateSecurityHealthAnalyticsCustomModule`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `securitycenter.securityhealthanalyticscustommodules.create - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.securitycenter.v1.SecurityCenter.CreateSecurityHealthAnalyticsCustomModule" `  




#### `CreateSource`

  * **Method** : `google.cloud.securitycenter.v1.SecurityCenter.CreateSource`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `securitycenter.sources.update - DATA_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.securitycenter.v1.SecurityCenter.CreateSource" `  




#### `DeleteBigQueryExport`

  * **Method** : `google.cloud.securitycenter.v1.SecurityCenter.DeleteBigQueryExport`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `securitycenter.bigQueryExports.delete - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.securitycenter.v1.SecurityCenter.DeleteBigQueryExport" `  




#### `DeleteEventThreatDetectionCustomModule`

  * **Method** : `google.cloud.securitycenter.v1.SecurityCenter.DeleteEventThreatDetectionCustomModule`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `securitycenter.eventthreatdetectioncustommodules.delete - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.securitycenter.v1.SecurityCenter.DeleteEventThreatDetectionCustomModule" `  




#### `DeleteMuteConfig`

  * **Method** : `google.cloud.securitycenter.v1.SecurityCenter.DeleteMuteConfig`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `securitycenter.muteconfigs.delete - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.securitycenter.v1.SecurityCenter.DeleteMuteConfig" `  




#### `DeleteNotificationConfig`

  * **Method** : `google.cloud.securitycenter.v1.SecurityCenter.DeleteNotificationConfig`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `securitycenter.notificationconfig.delete - DATA_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.securitycenter.v1.SecurityCenter.DeleteNotificationConfig" `  




#### `DeleteResourceValueConfig`

  * **Method** : `google.cloud.securitycenter.v1.SecurityCenter.DeleteResourceValueConfig`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `securitycenter.resourcevalueconfigs.delete - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.securitycenter.v1.SecurityCenter.DeleteResourceValueConfig" `  




#### `DeleteSecurityHealthAnalyticsCustomModule`

  * **Method** : `google.cloud.securitycenter.v1.SecurityCenter.DeleteSecurityHealthAnalyticsCustomModule`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `securitycenter.securityhealthanalyticscustommodules.delete - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.securitycenter.v1.SecurityCenter.DeleteSecurityHealthAnalyticsCustomModule" `  




#### `GetBigQueryExport`

  * **Method** : `google.cloud.securitycenter.v1.SecurityCenter.GetBigQueryExport`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `securitycenter.bigQueryExports.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.securitycenter.v1.SecurityCenter.GetBigQueryExport" `  




#### `GetEffectiveEventThreatDetectionCustomModule`

  * **Method** : `google.cloud.securitycenter.v1.SecurityCenter.GetEffectiveEventThreatDetectionCustomModule`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `securitycenter.effectiveeventthreatdetectioncustommodules.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.securitycenter.v1.SecurityCenter.GetEffectiveEventThreatDetectionCustomModule" `  




#### `GetEffectiveSecurityHealthAnalyticsCustomModule`

  * **Method** : `google.cloud.securitycenter.v1.SecurityCenter.GetEffectiveSecurityHealthAnalyticsCustomModule`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `securitycenter.effectivesecurityhealthanalyticscustommodules.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.securitycenter.v1.SecurityCenter.GetEffectiveSecurityHealthAnalyticsCustomModule" `  




#### `GetEventThreatDetectionCustomModule`

  * **Method** : `google.cloud.securitycenter.v1.SecurityCenter.GetEventThreatDetectionCustomModule`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `securitycenter.eventthreatdetectioncustommodules.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.securitycenter.v1.SecurityCenter.GetEventThreatDetectionCustomModule" `  




#### `GetIamPolicy`

  * **Method** : `google.cloud.securitycenter.v1.SecurityCenter.GetIamPolicy`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `securitycenter.sources.getIamPolicy - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.securitycenter.v1.SecurityCenter.GetIamPolicy" `  




#### `GetMuteConfig`

  * **Method** : `google.cloud.securitycenter.v1.SecurityCenter.GetMuteConfig`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `securitycenter.muteconfigs.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.securitycenter.v1.SecurityCenter.GetMuteConfig" `  




#### `GetNotificationConfig`

  * **Method** : `google.cloud.securitycenter.v1.SecurityCenter.GetNotificationConfig`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `securitycenter.notificationconfig.get - DATA_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.securitycenter.v1.SecurityCenter.GetNotificationConfig" `  




#### `GetOrganizationSettings`

  * **Method** : `google.cloud.securitycenter.v1.SecurityCenter.GetOrganizationSettings`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `securitycenter.organizationsettings.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.securitycenter.v1.SecurityCenter.GetOrganizationSettings" `  




#### `GetResourceValueConfig`

  * **Method** : `google.cloud.securitycenter.v1.SecurityCenter.GetResourceValueConfig`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `securitycenter.resourcevalueconfigs.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.securitycenter.v1.SecurityCenter.GetResourceValueConfig" `  




#### `GetSecurityHealthAnalyticsCustomModule`

  * **Method** : `google.cloud.securitycenter.v1.SecurityCenter.GetSecurityHealthAnalyticsCustomModule`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `securitycenter.securityhealthanalyticscustommodules.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.securitycenter.v1.SecurityCenter.GetSecurityHealthAnalyticsCustomModule" `  




#### `GetSimulation`

  * **Method** : `google.cloud.securitycenter.v1.SecurityCenter.GetSimulation`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `securitycenter.simulations.get - DATA_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.securitycenter.v1.SecurityCenter.GetSimulation" `  




#### `GetSource`

  * **Method** : `google.cloud.securitycenter.v1.SecurityCenter.GetSource`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `securitycenter.sources.get - DATA_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.securitycenter.v1.SecurityCenter.GetSource" `  




#### `GetValuedResource`

  * **Method** : `google.cloud.securitycenter.v1.SecurityCenter.GetValuedResource`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `securitycenter.valuedresources.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.securitycenter.v1.SecurityCenter.GetValuedResource" `  




#### `GroupAssets`

  * **Method** : `google.cloud.securitycenter.v1.SecurityCenter.GroupAssets`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `securitycenter.assets.group - DATA_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.securitycenter.v1.SecurityCenter.GroupAssets" `  




#### `GroupFindings`

  * **Method** : `google.cloud.securitycenter.v1.SecurityCenter.GroupFindings`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `securitycenter.findings.group - DATA_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.securitycenter.v1.SecurityCenter.GroupFindings" `  




#### `ListAssets`

  * **Method** : `google.cloud.securitycenter.v1.SecurityCenter.ListAssets`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `securitycenter.assets.list - DATA_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.securitycenter.v1.SecurityCenter.ListAssets" `  




#### `ListAttackPaths`

  * **Method** : `google.cloud.securitycenter.v1.SecurityCenter.ListAttackPaths`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `securitycenter.attackpaths.list - DATA_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.securitycenter.v1.SecurityCenter.ListAttackPaths" `  




#### `ListBigQueryExports`

  * **Method** : `google.cloud.securitycenter.v1.SecurityCenter.ListBigQueryExports`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `securitycenter.bigQueryExports.list - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.securitycenter.v1.SecurityCenter.ListBigQueryExports" `  




#### `ListDescendantEventThreatDetectionCustomModules`

  * **Method** : `google.cloud.securitycenter.v1.SecurityCenter.ListDescendantEventThreatDetectionCustomModules`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `securitycenter.eventthreatdetectioncustommodules.list - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.securitycenter.v1.SecurityCenter.ListDescendantEventThreatDetectionCustomModules" `  




#### `ListDescendantSecurityHealthAnalyticsCustomModules`

  * **Method** : `google.cloud.securitycenter.v1.SecurityCenter.ListDescendantSecurityHealthAnalyticsCustomModules`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `securitycenter.securityhealthanalyticscustommodules.list - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.securitycenter.v1.SecurityCenter.ListDescendantSecurityHealthAnalyticsCustomModules" `  




#### `ListEffectiveEventThreatDetectionCustomModules`

  * **Method** : `google.cloud.securitycenter.v1.SecurityCenter.ListEffectiveEventThreatDetectionCustomModules`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `securitycenter.effectiveeventthreatdetectioncustommodules.list - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.securitycenter.v1.SecurityCenter.ListEffectiveEventThreatDetectionCustomModules" `  




#### `ListEffectiveSecurityHealthAnalyticsCustomModules`

  * **Method** : `google.cloud.securitycenter.v1.SecurityCenter.ListEffectiveSecurityHealthAnalyticsCustomModules`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `securitycenter.effectivesecurityhealthanalyticscustommodules.list - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.securitycenter.v1.SecurityCenter.ListEffectiveSecurityHealthAnalyticsCustomModules" `  




#### `ListEventThreatDetectionCustomModules`

  * **Method** : `google.cloud.securitycenter.v1.SecurityCenter.ListEventThreatDetectionCustomModules`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `securitycenter.eventthreatdetectioncustommodules.list - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.securitycenter.v1.SecurityCenter.ListEventThreatDetectionCustomModules" `  




#### `ListFindings`

  * **Method** : `google.cloud.securitycenter.v1.SecurityCenter.ListFindings`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `securitycenter.findings.list - DATA_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.securitycenter.v1.SecurityCenter.ListFindings" `  




#### `ListMuteConfigs`

  * **Method** : `google.cloud.securitycenter.v1.SecurityCenter.ListMuteConfigs`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `securitycenter.muteconfigs.list - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.securitycenter.v1.SecurityCenter.ListMuteConfigs" `  




#### `ListNotificationConfigs`

  * **Method** : `google.cloud.securitycenter.v1.SecurityCenter.ListNotificationConfigs`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `securitycenter.notificationconfig.list - DATA_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.securitycenter.v1.SecurityCenter.ListNotificationConfigs" `  




#### `ListResourceValueConfigs`

  * **Method** : `google.cloud.securitycenter.v1.SecurityCenter.ListResourceValueConfigs`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `securitycenter.resourcevalueconfigs.list - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.securitycenter.v1.SecurityCenter.ListResourceValueConfigs" `  




#### `ListSecurityHealthAnalyticsCustomModules`

  * **Method** : `google.cloud.securitycenter.v1.SecurityCenter.ListSecurityHealthAnalyticsCustomModules`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `securitycenter.securityhealthanalyticscustommodules.list - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.securitycenter.v1.SecurityCenter.ListSecurityHealthAnalyticsCustomModules" `  




#### `ListSources`

  * **Method** : `google.cloud.securitycenter.v1.SecurityCenter.ListSources`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `securitycenter.sources.list - DATA_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.securitycenter.v1.SecurityCenter.ListSources" `  




#### `ListValuedResources`

  * **Method** : `google.cloud.securitycenter.v1.SecurityCenter.ListValuedResources`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `securitycenter.valuedresources.list - DATA_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.securitycenter.v1.SecurityCenter.ListValuedResources" `  




#### `SetFindingState`

  * **Method** : `google.cloud.securitycenter.v1.SecurityCenter.SetFindingState`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `securitycenter.findings.setState - DATA_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.securitycenter.v1.SecurityCenter.SetFindingState" `  




#### `SetIamPolicy`

  * **Method** : `google.cloud.securitycenter.v1.SecurityCenter.SetIamPolicy`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `securitycenter.sources.setIamPolicy - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.securitycenter.v1.SecurityCenter.SetIamPolicy" `  




#### `SetMute`

  * **Method** : `google.cloud.securitycenter.v1.SecurityCenter.SetMute`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `securitycenter.findings.setMute - DATA_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.securitycenter.v1.SecurityCenter.SetMute" `  




#### `SimulateSecurityHealthAnalyticsCustomModule`

  * **Method** : `google.cloud.securitycenter.v1.SecurityCenter.SimulateSecurityHealthAnalyticsCustomModule`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `securitycenter.securityhealthanalyticscustommodules.simulate - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.securitycenter.v1.SecurityCenter.SimulateSecurityHealthAnalyticsCustomModule" `  




#### `UpdateBigQueryExport`

  * **Method** : `google.cloud.securitycenter.v1.SecurityCenter.UpdateBigQueryExport`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `securitycenter.bigQueryExports.update - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.securitycenter.v1.SecurityCenter.UpdateBigQueryExport" `  




#### `UpdateEventThreatDetectionCustomModule`

  * **Method** : `google.cloud.securitycenter.v1.SecurityCenter.UpdateEventThreatDetectionCustomModule`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `securitycenter.eventthreatdetectioncustommodules.update - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.securitycenter.v1.SecurityCenter.UpdateEventThreatDetectionCustomModule" `  




#### `UpdateExternalSystem`

  * **Method** : `google.cloud.securitycenter.v1.SecurityCenter.UpdateExternalSystem`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `securitycenter.findingexternalsystems.update - DATA_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.securitycenter.v1.SecurityCenter.UpdateExternalSystem" `  




#### `UpdateFinding`

  * **Method** : `google.cloud.securitycenter.v1.SecurityCenter.UpdateFinding`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `securitycenter.findings.update - DATA_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.securitycenter.v1.SecurityCenter.UpdateFinding" `  




#### `UpdateMuteConfig`

  * **Method** : `google.cloud.securitycenter.v1.SecurityCenter.UpdateMuteConfig`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `securitycenter.muteconfigs.update - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.securitycenter.v1.SecurityCenter.UpdateMuteConfig" `  




#### `UpdateNotificationConfig`

  * **Method** : `google.cloud.securitycenter.v1.SecurityCenter.UpdateNotificationConfig`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `securitycenter.notificationconfig.update - DATA_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.securitycenter.v1.SecurityCenter.UpdateNotificationConfig" `  




#### `UpdateOrganizationSettings`

  * **Method** : `google.cloud.securitycenter.v1.SecurityCenter.UpdateOrganizationSettings`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `securitycenter.organizationsettings.update - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.securitycenter.v1.SecurityCenter.UpdateOrganizationSettings" `  




#### `UpdateResourceValueConfig`

  * **Method** : `google.cloud.securitycenter.v1.SecurityCenter.UpdateResourceValueConfig`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `securitycenter.resourcevalueconfigs.update - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.securitycenter.v1.SecurityCenter.UpdateResourceValueConfig" `  




#### `UpdateSecurityHealthAnalyticsCustomModule`

  * **Method** : `google.cloud.securitycenter.v1.SecurityCenter.UpdateSecurityHealthAnalyticsCustomModule`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `securitycenter.securityhealthanalyticscustommodules.update - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.securitycenter.v1.SecurityCenter.UpdateSecurityHealthAnalyticsCustomModule" `  




#### `UpdateSecurityMarks`

  * **Method** : `google.cloud.securitycenter.v1.SecurityCenter.UpdateSecurityMarks`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `securitycenter.findingsecuritymarks.update - DATA_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.securitycenter.v1.SecurityCenter.UpdateSecurityMarks" `  




#### `UpdateSource`

  * **Method** : `google.cloud.securitycenter.v1.SecurityCenter.UpdateSource`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `securitycenter.sources.update - DATA_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.securitycenter.v1.SecurityCenter.UpdateSource" `  




#### `ValidateEventThreatDetectionCustomModule`

  * **Method** : `google.cloud.securitycenter.v1.SecurityCenter.ValidateEventThreatDetectionCustomModule`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `securitycenter.eventthreatdetectioncustommodules.validate - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.securitycenter.v1.SecurityCenter.ValidateEventThreatDetectionCustomModule" `  




### `google.cloud.securitycenter.v1beta1.SecurityCenter`

The following audit logs are associated with methods belonging to `google.cloud.securitycenter.v1beta1.SecurityCenter`.

#### `CreateFinding`

  * **Method** : `google.cloud.securitycenter.v1beta1.SecurityCenter.CreateFinding`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `securitycenter.findings.update - DATA_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.securitycenter.v1beta1.SecurityCenter.CreateFinding" `  




#### `CreateSource`

  * **Method** : `google.cloud.securitycenter.v1beta1.SecurityCenter.CreateSource`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `securitycenter.sources.update - DATA_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.securitycenter.v1beta1.SecurityCenter.CreateSource" `  




#### `GetIamPolicy`

  * **Method** : `google.cloud.securitycenter.v1beta1.SecurityCenter.GetIamPolicy`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `securitycenter.sources.getIamPolicy - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.securitycenter.v1beta1.SecurityCenter.GetIamPolicy" `  




#### `GetOrganizationSettings`

  * **Method** : `google.cloud.securitycenter.v1beta1.SecurityCenter.GetOrganizationSettings`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `securitycenter.organizationsettings.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.securitycenter.v1beta1.SecurityCenter.GetOrganizationSettings" `  




#### `GetSource`

  * **Method** : `google.cloud.securitycenter.v1beta1.SecurityCenter.GetSource`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `securitycenter.sources.get - DATA_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.securitycenter.v1beta1.SecurityCenter.GetSource" `  




#### `GroupFindings`

  * **Method** : `google.cloud.securitycenter.v1beta1.SecurityCenter.GroupFindings`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `securitycenter.findings.group - DATA_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.securitycenter.v1beta1.SecurityCenter.GroupFindings" `  




#### `ListAssets`

  * **Method** : `google.cloud.securitycenter.v1beta1.SecurityCenter.ListAssets`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `securitycenter.assets.list - DATA_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.securitycenter.v1beta1.SecurityCenter.ListAssets" `  




#### `ListFindings`

  * **Method** : `google.cloud.securitycenter.v1beta1.SecurityCenter.ListFindings`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `securitycenter.findings.list - DATA_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.securitycenter.v1beta1.SecurityCenter.ListFindings" `  




#### `ListSources`

  * **Method** : `google.cloud.securitycenter.v1beta1.SecurityCenter.ListSources`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `securitycenter.sources.list - DATA_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.securitycenter.v1beta1.SecurityCenter.ListSources" `  




#### `SetFindingState`

  * **Method** : `google.cloud.securitycenter.v1beta1.SecurityCenter.SetFindingState`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `securitycenter.findings.setState - DATA_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.securitycenter.v1beta1.SecurityCenter.SetFindingState" `  




#### `SetIamPolicy`

  * **Method** : `google.cloud.securitycenter.v1beta1.SecurityCenter.SetIamPolicy`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `securitycenter.sources.setIamPolicy - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.securitycenter.v1beta1.SecurityCenter.SetIamPolicy" `  




#### `UpdateFinding`

  * **Method** : `google.cloud.securitycenter.v1beta1.SecurityCenter.UpdateFinding`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `securitycenter.findings.update - DATA_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.securitycenter.v1beta1.SecurityCenter.UpdateFinding" `  




#### `UpdateOrganizationSettings`

  * **Method** : `google.cloud.securitycenter.v1beta1.SecurityCenter.UpdateOrganizationSettings`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `securitycenter.organizationsettings.update - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.securitycenter.v1beta1.SecurityCenter.UpdateOrganizationSettings" `  




#### `UpdateSecurityMarks`

  * **Method** : `google.cloud.securitycenter.v1beta1.SecurityCenter.UpdateSecurityMarks`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `securitycenter.findingsecuritymarks.update - DATA_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.securitycenter.v1beta1.SecurityCenter.UpdateSecurityMarks" `  




#### `UpdateSource`

  * **Method** : `google.cloud.securitycenter.v1beta1.SecurityCenter.UpdateSource`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `securitycenter.sources.update - DATA_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.securitycenter.v1beta1.SecurityCenter.UpdateSource" `  




### `google.cloud.securitycenter.v1p1beta1.SecurityCenter`

The following audit logs are associated with methods belonging to `google.cloud.securitycenter.v1p1beta1.SecurityCenter`.

#### `CreateFinding`

  * **Method** : `google.cloud.securitycenter.v1p1beta1.SecurityCenter.CreateFinding`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `securitycenter.findings.update - DATA_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.securitycenter.v1p1beta1.SecurityCenter.CreateFinding" `  




#### `CreateNotificationConfig`

  * **Method** : `google.cloud.securitycenter.v1p1beta1.SecurityCenter.CreateNotificationConfig`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `securitycenter.notificationconfig.create - DATA_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.securitycenter.v1p1beta1.SecurityCenter.CreateNotificationConfig" `  




#### `CreateSource`

  * **Method** : `google.cloud.securitycenter.v1p1beta1.SecurityCenter.CreateSource`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `securitycenter.sources.update - DATA_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.securitycenter.v1p1beta1.SecurityCenter.CreateSource" `  




#### `DeleteNotificationConfig`

  * **Method** : `google.cloud.securitycenter.v1p1beta1.SecurityCenter.DeleteNotificationConfig`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `securitycenter.notificationconfig.delete - DATA_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.securitycenter.v1p1beta1.SecurityCenter.DeleteNotificationConfig" `  




#### `GetIamPolicy`

  * **Method** : `google.cloud.securitycenter.v1p1beta1.SecurityCenter.GetIamPolicy`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `securitycenter.sources.getIamPolicy - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.securitycenter.v1p1beta1.SecurityCenter.GetIamPolicy" `  




#### `GetNotificationConfig`

  * **Method** : `google.cloud.securitycenter.v1p1beta1.SecurityCenter.GetNotificationConfig`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `securitycenter.notificationconfig.get - DATA_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.securitycenter.v1p1beta1.SecurityCenter.GetNotificationConfig" `  




#### `GetOrganizationSettings`

  * **Method** : `google.cloud.securitycenter.v1p1beta1.SecurityCenter.GetOrganizationSettings`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `securitycenter.organizationsettings.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.securitycenter.v1p1beta1.SecurityCenter.GetOrganizationSettings" `  




#### `GetSource`

  * **Method** : `google.cloud.securitycenter.v1p1beta1.SecurityCenter.GetSource`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `securitycenter.sources.get - DATA_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.securitycenter.v1p1beta1.SecurityCenter.GetSource" `  




#### `GroupAssets`

  * **Method** : `google.cloud.securitycenter.v1p1beta1.SecurityCenter.GroupAssets`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `securitycenter.assets.group - DATA_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.securitycenter.v1p1beta1.SecurityCenter.GroupAssets" `  




#### `GroupFindings`

  * **Method** : `google.cloud.securitycenter.v1p1beta1.SecurityCenter.GroupFindings`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `securitycenter.findings.group - DATA_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.securitycenter.v1p1beta1.SecurityCenter.GroupFindings" `  




#### `ListAssets`

  * **Method** : `google.cloud.securitycenter.v1p1beta1.SecurityCenter.ListAssets`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `securitycenter.assets.list - DATA_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.securitycenter.v1p1beta1.SecurityCenter.ListAssets" `  




#### `ListFindings`

  * **Method** : `google.cloud.securitycenter.v1p1beta1.SecurityCenter.ListFindings`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `securitycenter.findings.list - DATA_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.securitycenter.v1p1beta1.SecurityCenter.ListFindings" `  




#### `ListNotificationConfigs`

  * **Method** : `google.cloud.securitycenter.v1p1beta1.SecurityCenter.ListNotificationConfigs`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `securitycenter.notificationconfig.list - DATA_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.securitycenter.v1p1beta1.SecurityCenter.ListNotificationConfigs" `  




#### `ListSources`

  * **Method** : `google.cloud.securitycenter.v1p1beta1.SecurityCenter.ListSources`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `securitycenter.sources.list - DATA_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.securitycenter.v1p1beta1.SecurityCenter.ListSources" `  




#### `SetFindingState`

  * **Method** : `google.cloud.securitycenter.v1p1beta1.SecurityCenter.SetFindingState`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `securitycenter.findings.setState - DATA_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.securitycenter.v1p1beta1.SecurityCenter.SetFindingState" `  




#### `SetIamPolicy`

  * **Method** : `google.cloud.securitycenter.v1p1beta1.SecurityCenter.SetIamPolicy`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `securitycenter.sources.setIamPolicy - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.securitycenter.v1p1beta1.SecurityCenter.SetIamPolicy" `  




#### `UpdateFinding`

  * **Method** : `google.cloud.securitycenter.v1p1beta1.SecurityCenter.UpdateFinding`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `securitycenter.findings.update - DATA_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.securitycenter.v1p1beta1.SecurityCenter.UpdateFinding" `  




#### `UpdateNotificationConfig`

  * **Method** : `google.cloud.securitycenter.v1p1beta1.SecurityCenter.UpdateNotificationConfig`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `securitycenter.notificationconfig.update - DATA_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.securitycenter.v1p1beta1.SecurityCenter.UpdateNotificationConfig" `  




#### `UpdateOrganizationSettings`

  * **Method** : `google.cloud.securitycenter.v1p1beta1.SecurityCenter.UpdateOrganizationSettings`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `securitycenter.organizationsettings.update - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.securitycenter.v1p1beta1.SecurityCenter.UpdateOrganizationSettings" `  




#### `UpdateSecurityMarks`

  * **Method** : `google.cloud.securitycenter.v1p1beta1.SecurityCenter.UpdateSecurityMarks`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `securitycenter.assetsecuritymarks.update - DATA_WRITE`
    * `securitycenter.findingsecuritymarks.update - DATA_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.securitycenter.v1p1beta1.SecurityCenter.UpdateSecurityMarks" `  




#### `UpdateSource`

  * **Method** : `google.cloud.securitycenter.v1p1beta1.SecurityCenter.UpdateSource`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `securitycenter.sources.update - DATA_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.securitycenter.v1p1beta1.SecurityCenter.UpdateSource" `  




### `google.cloud.securitycenter.v2.SecurityCenter`

The following audit logs are associated with methods belonging to `google.cloud.securitycenter.v2.SecurityCenter`.

#### `BatchCreateResourceValueConfigs`

  * **Method** : `google.cloud.securitycenter.v2.SecurityCenter.BatchCreateResourceValueConfigs`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `securitycenter.resourcevalueconfigs.create - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.securitycenter.v2.SecurityCenter.BatchCreateResourceValueConfigs" `  




#### `BulkMuteFindings`

  * **Method** : `google.cloud.securitycenter.v2.SecurityCenter.BulkMuteFindings`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `securitycenter.findings.bulkMuteUpdate - DATA_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.securitycenter.v2.SecurityCenter.BulkMuteFindings" `  




#### `CreateBigQueryExport`

  * **Method** : `google.cloud.securitycenter.v2.SecurityCenter.CreateBigQueryExport`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `securitycenter.bigQueryExports.create - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.securitycenter.v2.SecurityCenter.CreateBigQueryExport" `  




#### `CreateFinding`

  * **Method** : `google.cloud.securitycenter.v2.SecurityCenter.CreateFinding`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `securitycenter.findings.update - DATA_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.securitycenter.v2.SecurityCenter.CreateFinding" `  




#### `CreateMuteConfig`

  * **Method** : `google.cloud.securitycenter.v2.SecurityCenter.CreateMuteConfig`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `securitycenter.muteconfigs.create - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.securitycenter.v2.SecurityCenter.CreateMuteConfig" `  




#### `CreateNotificationConfig`

  * **Method** : `google.cloud.securitycenter.v2.SecurityCenter.CreateNotificationConfig`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `securitycenter.notificationconfig.create - DATA_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.securitycenter.v2.SecurityCenter.CreateNotificationConfig" `  




#### `CreateSource`

  * **Method** : `google.cloud.securitycenter.v2.SecurityCenter.CreateSource`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `securitycenter.sources.update - DATA_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.securitycenter.v2.SecurityCenter.CreateSource" `  




#### `DeleteBigQueryExport`

  * **Method** : `google.cloud.securitycenter.v2.SecurityCenter.DeleteBigQueryExport`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `securitycenter.bigQueryExports.delete - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.securitycenter.v2.SecurityCenter.DeleteBigQueryExport" `  




#### `DeleteMuteConfig`

  * **Method** : `google.cloud.securitycenter.v2.SecurityCenter.DeleteMuteConfig`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `securitycenter.muteconfigs.delete - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.securitycenter.v2.SecurityCenter.DeleteMuteConfig" `  




#### `DeleteNotificationConfig`

  * **Method** : `google.cloud.securitycenter.v2.SecurityCenter.DeleteNotificationConfig`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `securitycenter.notificationconfig.delete - DATA_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.securitycenter.v2.SecurityCenter.DeleteNotificationConfig" `  




#### `DeleteResourceValueConfig`

  * **Method** : `google.cloud.securitycenter.v2.SecurityCenter.DeleteResourceValueConfig`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `securitycenter.resourcevalueconfigs.delete - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.securitycenter.v2.SecurityCenter.DeleteResourceValueConfig" `  




#### `ExportFindings`

  * **Method** : `google.cloud.securitycenter.v2.SecurityCenter.ExportFindings`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `securitycenter.findings.export - DATA_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.securitycenter.v2.SecurityCenter.ExportFindings" `  




#### `GetBigQueryExport`

  * **Method** : `google.cloud.securitycenter.v2.SecurityCenter.GetBigQueryExport`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `securitycenter.bigQueryExports.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.securitycenter.v2.SecurityCenter.GetBigQueryExport" `  




#### `GetIamPolicy`

  * **Method** : `google.cloud.securitycenter.v2.SecurityCenter.GetIamPolicy`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `securitycenter.sources.getIamPolicy - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.securitycenter.v2.SecurityCenter.GetIamPolicy" `  




#### `GetMuteConfig`

  * **Method** : `google.cloud.securitycenter.v2.SecurityCenter.GetMuteConfig`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `securitycenter.muteconfigs.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.securitycenter.v2.SecurityCenter.GetMuteConfig" `  




#### `GetNotificationConfig`

  * **Method** : `google.cloud.securitycenter.v2.SecurityCenter.GetNotificationConfig`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `securitycenter.notificationconfig.get - DATA_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.securitycenter.v2.SecurityCenter.GetNotificationConfig" `  




#### `GetResourceValueConfig`

  * **Method** : `google.cloud.securitycenter.v2.SecurityCenter.GetResourceValueConfig`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `securitycenter.resourcevalueconfigs.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.securitycenter.v2.SecurityCenter.GetResourceValueConfig" `  




#### `GetSimulation`

  * **Method** : `google.cloud.securitycenter.v2.SecurityCenter.GetSimulation`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `securitycenter.simulations.get - DATA_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.securitycenter.v2.SecurityCenter.GetSimulation" `  




#### `GetSource`

  * **Method** : `google.cloud.securitycenter.v2.SecurityCenter.GetSource`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `securitycenter.sources.get - DATA_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.securitycenter.v2.SecurityCenter.GetSource" `  




#### `GetValuedResource`

  * **Method** : `google.cloud.securitycenter.v2.SecurityCenter.GetValuedResource`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `securitycenter.valuedresources.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.securitycenter.v2.SecurityCenter.GetValuedResource" `  




#### `GroupFindings`

  * **Method** : `google.cloud.securitycenter.v2.SecurityCenter.GroupFindings`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `securitycenter.findings.group - DATA_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.securitycenter.v2.SecurityCenter.GroupFindings" `  




#### `ListAttackPaths`

  * **Method** : `google.cloud.securitycenter.v2.SecurityCenter.ListAttackPaths`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `securitycenter.attackpaths.list - DATA_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.securitycenter.v2.SecurityCenter.ListAttackPaths" `  




#### `ListBigQueryExports`

  * **Method** : `google.cloud.securitycenter.v2.SecurityCenter.ListBigQueryExports`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `securitycenter.bigQueryExports.list - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.securitycenter.v2.SecurityCenter.ListBigQueryExports" `  




#### `ListFindings`

  * **Method** : `google.cloud.securitycenter.v2.SecurityCenter.ListFindings`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `securitycenter.findings.list - DATA_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.securitycenter.v2.SecurityCenter.ListFindings" `  




#### `ListMuteConfigs`

  * **Method** : `google.cloud.securitycenter.v2.SecurityCenter.ListMuteConfigs`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `securitycenter.muteconfigs.list - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.securitycenter.v2.SecurityCenter.ListMuteConfigs" `  




#### `ListNotificationConfigs`

  * **Method** : `google.cloud.securitycenter.v2.SecurityCenter.ListNotificationConfigs`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `securitycenter.notificationconfig.list - DATA_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.securitycenter.v2.SecurityCenter.ListNotificationConfigs" `  




#### `ListResourceValueConfigs`

  * **Method** : `google.cloud.securitycenter.v2.SecurityCenter.ListResourceValueConfigs`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `securitycenter.resourcevalueconfigs.list - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.securitycenter.v2.SecurityCenter.ListResourceValueConfigs" `  




#### `ListSources`

  * **Method** : `google.cloud.securitycenter.v2.SecurityCenter.ListSources`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `securitycenter.sources.list - DATA_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.securitycenter.v2.SecurityCenter.ListSources" `  




#### `ListValuedResources`

  * **Method** : `google.cloud.securitycenter.v2.SecurityCenter.ListValuedResources`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `securitycenter.valuedresources.list - DATA_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.securitycenter.v2.SecurityCenter.ListValuedResources" `  




#### `SetFindingState`

  * **Method** : `google.cloud.securitycenter.v2.SecurityCenter.SetFindingState`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `securitycenter.findings.setState - DATA_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.securitycenter.v2.SecurityCenter.SetFindingState" `  




#### `SetIamPolicy`

  * **Method** : `google.cloud.securitycenter.v2.SecurityCenter.SetIamPolicy`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `securitycenter.sources.setIamPolicy - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.securitycenter.v2.SecurityCenter.SetIamPolicy" `  




#### `SetMute`

  * **Method** : `google.cloud.securitycenter.v2.SecurityCenter.SetMute`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `securitycenter.findings.setMute - DATA_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.securitycenter.v2.SecurityCenter.SetMute" `  




#### `UpdateBigQueryExport`

  * **Method** : `google.cloud.securitycenter.v2.SecurityCenter.UpdateBigQueryExport`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `securitycenter.bigQueryExports.update - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.securitycenter.v2.SecurityCenter.UpdateBigQueryExport" `  




#### `UpdateExternalSystem`

  * **Method** : `google.cloud.securitycenter.v2.SecurityCenter.UpdateExternalSystem`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `securitycenter.findingexternalsystems.update - DATA_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.securitycenter.v2.SecurityCenter.UpdateExternalSystem" `  




#### `UpdateFinding`

  * **Method** : `google.cloud.securitycenter.v2.SecurityCenter.UpdateFinding`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `securitycenter.findings.update - DATA_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.securitycenter.v2.SecurityCenter.UpdateFinding" `  




#### `UpdateMuteConfig`

  * **Method** : `google.cloud.securitycenter.v2.SecurityCenter.UpdateMuteConfig`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `securitycenter.muteconfigs.update - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.securitycenter.v2.SecurityCenter.UpdateMuteConfig" `  




#### `UpdateNotificationConfig`

  * **Method** : `google.cloud.securitycenter.v2.SecurityCenter.UpdateNotificationConfig`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `securitycenter.notificationconfig.update - DATA_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.securitycenter.v2.SecurityCenter.UpdateNotificationConfig" `  




#### `UpdateResourceValueConfig`

  * **Method** : `google.cloud.securitycenter.v2.SecurityCenter.UpdateResourceValueConfig`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `securitycenter.resourcevalueconfigs.update - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.securitycenter.v2.SecurityCenter.UpdateResourceValueConfig" `  




#### `UpdateSecurityMarks`

  * **Method** : `google.cloud.securitycenter.v2.SecurityCenter.UpdateSecurityMarks`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `securitycenter.findingsecuritymarks.update - DATA_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.securitycenter.v2.SecurityCenter.UpdateSecurityMarks" `  




#### `UpdateSource`

  * **Method** : `google.cloud.securitycenter.v2.SecurityCenter.UpdateSource`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `securitycenter.sources.update - DATA_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.securitycenter.v2.SecurityCenter.UpdateSource" `  




## System events

System Event audit logs are generated by GCP systems, not direct user action. For more information, see [System Event audit logs](https://docs.cloud.google.com/logging/docs/audit#system-event).

Method Name | Filter For This Event | Notes  
---|---|---  
DiskVulnerabilityScanStatus |  ` protoPayload.methodName="DiskVulnerabilityScanStatus" ` |   
VmThreatDetectionScanStarted |  ` protoPayload.methodName="VmThreatDetectionScanStarted" ` |   
google.cloud.securitycenter.v2.SecurityCenter.ReasoningEngineVulnerabilityFindingPublished |  ` protoPayload.methodName="google.cloud.securitycenter.v2.SecurityCenter.ReasoningEngineVulnerabilityFindingPublished" ` |   
  
## Methods that don't produce audit logs

A method might not produce audit logs for one or more of the following reasons: 

  * It is a high volume method involving significant log generation and storage costs.
  * It has low auditing value.
  * Another audit or platform log already provides method coverage.



The following methods don't produce audit logs:

  * `google.cloud.securitycenter.v1.SecurityCenter.RunAssetDiscovery`
  * `google.cloud.securitycenter.v1.SecurityCenter.TestIamPermissions`
  * `google.cloud.securitycenter.v1beta1.SecurityCenter.RunAssetDiscovery`
  * `google.cloud.securitycenter.v1beta1.SecurityCenter.TestIamPermissions`
  * `google.cloud.securitycenter.v1p1beta1.SecurityCenter.RunAssetDiscovery`
  * `google.cloud.securitycenter.v1p1beta1.SecurityCenter.TestIamPermissions`
  * `google.cloud.securitycenter.v2.SecurityCenter.TestIamPermissions`
  * `google.longrunning.Operations.CancelOperation`
  * `google.longrunning.Operations.DeleteOperation`
  * `google.longrunning.Operations.GetOperation`
  * `google.longrunning.Operations.ListOperations`
  * `google.longrunning.Operations.WaitOperation`



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
