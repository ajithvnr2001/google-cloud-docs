---
url: https://docs.cloud.google.com/security-command-center/docs/audit-logging-security-center-management/
title: Security Center Management API audit logging \u00a0|\u00a0 Security Command Center \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:51:58.526911+00:00
---

# Security Center Management API audit logging  |  Security Command Center  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/security-command-center/docs/audit-logging-security-center-management/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Security Command Center ](https://docs.cloud.google.com/security-command-center/docs)
  * [ Guides ](https://docs.cloud.google.com/security-command-center/docs/security-command-center-overview)



Send feedback 

#  Security Center Management API audit logging Stay organized with collections  Save and categorize content based on your preferences. 

Standard-legacy, Standard, Premium, and Enterprise (Deprecated) [service tiers](https://docs.cloud.google.com/security-command-center/docs/service-tiers) The Security Command Center Enterprise service tier will shut down on May 21, 2027. If your organization uses the Enterprise service tier, then the organization will automatically move to the Premium service tier on or after May 21, 2027. Contact your account representative or a [Google Cloud sales specialist](https://cloud.google.com/contact) if you have questions. 

This document describes audit logging for Security Center Management API. Google Cloud services generate audit logs that record administrative and access activities within your Google Cloud resources. For more information about Cloud Audit Logs, see the following: 

  * [Types of audit logs](https://docs.cloud.google.com/logging/docs/audit#types)
  * [Audit log entry structure](https://docs.cloud.google.com/logging/docs/audit#audit_log_entry_structure)
  * [Storing and routing audit logs](https://docs.cloud.google.com/logging/docs/audit#storing_and_routing_audit_logs)
  * [Cloud Logging pricing summary](https://docs.cloud.google.com/stackdriver/pricing#logs-pricing-summary)
  * [Enable Data Access audit logs](https://docs.cloud.google.com/logging/docs/audit/configure-data-access)



## Service name

Security Center Management API audit logs use the service name `securitycentermanagement.googleapis.com`. Filter for this service: 
    
    
        protoPayload.serviceName="securitycentermanagement.googleapis.com"
      

## Methods by permission type

Each IAM permission has a `type` property, whose value is an enum that can be one of four values: `ADMIN_READ`, `ADMIN_WRITE`, `DATA_READ`, or `DATA_WRITE`. When you call a method, Security Center Management API generates an audit log whose category is dependent on the `type` property of the permission required to perform the method. Methods that require an IAM permission with the `type` property value of `DATA_READ`, `DATA_WRITE`, or `ADMIN_READ` generate [Data Access](https://docs.cloud.google.com/logging/docs/audit#data-access) audit logs. Methods that require an IAM permission with the `type` property value of `ADMIN_WRITE` generate [Admin Activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity) audit logs.

Permission type | Methods  
---|---  
`ADMIN_READ` | `google.cloud.securitycentermanagement.v1.SecurityCenterManagement.GetEffectiveEventThreatDetectionCustomModule`  
`google.cloud.securitycentermanagement.v1.SecurityCenterManagement.GetEffectiveSecurityHealthAnalyticsCustomModule`  
`google.cloud.securitycentermanagement.v1.SecurityCenterManagement.GetEventThreatDetectionCustomModule`  
`google.cloud.securitycentermanagement.v1.SecurityCenterManagement.GetSecurityCenterService`  
`google.cloud.securitycentermanagement.v1.SecurityCenterManagement.GetSecurityHealthAnalyticsCustomModule`  
`google.cloud.securitycentermanagement.v1.SecurityCenterManagement.ListDescendantEventThreatDetectionCustomModules`  
`google.cloud.securitycentermanagement.v1.SecurityCenterManagement.ListDescendantSecurityHealthAnalyticsCustomModules`  
`google.cloud.securitycentermanagement.v1.SecurityCenterManagement.ListEffectiveEventThreatDetectionCustomModules`  
`google.cloud.securitycentermanagement.v1.SecurityCenterManagement.ListEffectiveSecurityHealthAnalyticsCustomModules`  
`google.cloud.securitycentermanagement.v1.SecurityCenterManagement.ListEventThreatDetectionCustomModules`  
`google.cloud.securitycentermanagement.v1.SecurityCenterManagement.ListSecurityCenterServices`  
`google.cloud.securitycentermanagement.v1.SecurityCenterManagement.ListSecurityHealthAnalyticsCustomModules`  
`google.cloud.securitycentermanagement.v1.SecurityCenterManagement.SimulateSecurityHealthAnalyticsCustomModule`  
`google.cloud.securitycentermanagement.v1.SecurityCenterManagement.ValidateEventThreatDetectionCustomModule`  
`ADMIN_WRITE` | `google.cloud.securitycentermanagement.v1.SecurityCenterManagement.CreateEventThreatDetectionCustomModule`  
`google.cloud.securitycentermanagement.v1.SecurityCenterManagement.CreateSecurityHealthAnalyticsCustomModule`  
`google.cloud.securitycentermanagement.v1.SecurityCenterManagement.DeleteEventThreatDetectionCustomModule`  
`google.cloud.securitycentermanagement.v1.SecurityCenterManagement.DeleteSecurityHealthAnalyticsCustomModule`  
`google.cloud.securitycentermanagement.v1.SecurityCenterManagement.UpdateEventThreatDetectionCustomModule`  
`google.cloud.securitycentermanagement.v1.SecurityCenterManagement.UpdateSecurityCenterService`  
`google.cloud.securitycentermanagement.v1.SecurityCenterManagement.UpdateSecurityHealthAnalyticsCustomModule`  
  
## API interface audit logs

For information about how and which permissions are evaluated for each method, see the [Identity and Access Management documentation](https://docs.cloud.google.com/security-command-center/docs/access-control) for Security Center Management API.

### `google.cloud.securitycentermanagement.v1.SecurityCenterManagement`

The following audit logs are associated with methods belonging to `google.cloud.securitycentermanagement.v1.SecurityCenterManagement`.

#### `CreateEventThreatDetectionCustomModule`

  * **Method** : `google.cloud.securitycentermanagement.v1.SecurityCenterManagement.CreateEventThreatDetectionCustomModule`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `securitycentermanagement.eventThreatDetectionCustomModules.create - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.securitycentermanagement.v1.SecurityCenterManagement.CreateEventThreatDetectionCustomModule" `  




#### `CreateSecurityHealthAnalyticsCustomModule`

  * **Method** : `google.cloud.securitycentermanagement.v1.SecurityCenterManagement.CreateSecurityHealthAnalyticsCustomModule`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `securitycentermanagement.securityHealthAnalyticsCustomModules.create - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.securitycentermanagement.v1.SecurityCenterManagement.CreateSecurityHealthAnalyticsCustomModule" `  




#### `DeleteEventThreatDetectionCustomModule`

  * **Method** : `google.cloud.securitycentermanagement.v1.SecurityCenterManagement.DeleteEventThreatDetectionCustomModule`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `securitycentermanagement.eventThreatDetectionCustomModules.delete - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.securitycentermanagement.v1.SecurityCenterManagement.DeleteEventThreatDetectionCustomModule" `  




#### `DeleteSecurityHealthAnalyticsCustomModule`

  * **Method** : `google.cloud.securitycentermanagement.v1.SecurityCenterManagement.DeleteSecurityHealthAnalyticsCustomModule`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `securitycentermanagement.securityHealthAnalyticsCustomModules.delete - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.securitycentermanagement.v1.SecurityCenterManagement.DeleteSecurityHealthAnalyticsCustomModule" `  




#### `GetEffectiveEventThreatDetectionCustomModule`

  * **Method** : `google.cloud.securitycentermanagement.v1.SecurityCenterManagement.GetEffectiveEventThreatDetectionCustomModule`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `securitycentermanagement.effectiveEventThreatDetectionCustomModules.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.securitycentermanagement.v1.SecurityCenterManagement.GetEffectiveEventThreatDetectionCustomModule" `  




#### `GetEffectiveSecurityHealthAnalyticsCustomModule`

  * **Method** : `google.cloud.securitycentermanagement.v1.SecurityCenterManagement.GetEffectiveSecurityHealthAnalyticsCustomModule`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `securitycentermanagement.effectiveSecurityHealthAnalyticsCustomModules.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.securitycentermanagement.v1.SecurityCenterManagement.GetEffectiveSecurityHealthAnalyticsCustomModule" `  




#### `GetEventThreatDetectionCustomModule`

  * **Method** : `google.cloud.securitycentermanagement.v1.SecurityCenterManagement.GetEventThreatDetectionCustomModule`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `securitycentermanagement.eventThreatDetectionCustomModules.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.securitycentermanagement.v1.SecurityCenterManagement.GetEventThreatDetectionCustomModule" `  




#### `GetSecurityCenterService`

  * **Method** : `google.cloud.securitycentermanagement.v1.SecurityCenterManagement.GetSecurityCenterService`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `securitycentermanagement.securityCenterServices.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.securitycentermanagement.v1.SecurityCenterManagement.GetSecurityCenterService" `  




#### `GetSecurityHealthAnalyticsCustomModule`

  * **Method** : `google.cloud.securitycentermanagement.v1.SecurityCenterManagement.GetSecurityHealthAnalyticsCustomModule`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `securitycentermanagement.securityHealthAnalyticsCustomModules.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.securitycentermanagement.v1.SecurityCenterManagement.GetSecurityHealthAnalyticsCustomModule" `  




#### `ListDescendantEventThreatDetectionCustomModules`

  * **Method** : `google.cloud.securitycentermanagement.v1.SecurityCenterManagement.ListDescendantEventThreatDetectionCustomModules`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `securitycentermanagement.eventThreatDetectionCustomModules.list - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.securitycentermanagement.v1.SecurityCenterManagement.ListDescendantEventThreatDetectionCustomModules" `  




#### `ListDescendantSecurityHealthAnalyticsCustomModules`

  * **Method** : `google.cloud.securitycentermanagement.v1.SecurityCenterManagement.ListDescendantSecurityHealthAnalyticsCustomModules`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `securitycentermanagement.securityHealthAnalyticsCustomModules.list - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.securitycentermanagement.v1.SecurityCenterManagement.ListDescendantSecurityHealthAnalyticsCustomModules" `  




#### `ListEffectiveEventThreatDetectionCustomModules`

  * **Method** : `google.cloud.securitycentermanagement.v1.SecurityCenterManagement.ListEffectiveEventThreatDetectionCustomModules`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `securitycentermanagement.effectiveEventThreatDetectionCustomModules.list - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.securitycentermanagement.v1.SecurityCenterManagement.ListEffectiveEventThreatDetectionCustomModules" `  




#### `ListEffectiveSecurityHealthAnalyticsCustomModules`

  * **Method** : `google.cloud.securitycentermanagement.v1.SecurityCenterManagement.ListEffectiveSecurityHealthAnalyticsCustomModules`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `securitycentermanagement.effectiveSecurityHealthAnalyticsCustomModules.list - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.securitycentermanagement.v1.SecurityCenterManagement.ListEffectiveSecurityHealthAnalyticsCustomModules" `  




#### `ListEventThreatDetectionCustomModules`

  * **Method** : `google.cloud.securitycentermanagement.v1.SecurityCenterManagement.ListEventThreatDetectionCustomModules`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `securitycentermanagement.eventThreatDetectionCustomModules.list - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.securitycentermanagement.v1.SecurityCenterManagement.ListEventThreatDetectionCustomModules" `  




#### `ListSecurityCenterServices`

  * **Method** : `google.cloud.securitycentermanagement.v1.SecurityCenterManagement.ListSecurityCenterServices`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `securitycentermanagement.securityCenterServices.list - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.securitycentermanagement.v1.SecurityCenterManagement.ListSecurityCenterServices" `  




#### `ListSecurityHealthAnalyticsCustomModules`

  * **Method** : `google.cloud.securitycentermanagement.v1.SecurityCenterManagement.ListSecurityHealthAnalyticsCustomModules`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `securitycentermanagement.securityHealthAnalyticsCustomModules.list - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.securitycentermanagement.v1.SecurityCenterManagement.ListSecurityHealthAnalyticsCustomModules" `  




#### `SimulateSecurityHealthAnalyticsCustomModule`

  * **Method** : `google.cloud.securitycentermanagement.v1.SecurityCenterManagement.SimulateSecurityHealthAnalyticsCustomModule`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `securitycentermanagement.securityHealthAnalyticsCustomModules.simulate - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.securitycentermanagement.v1.SecurityCenterManagement.SimulateSecurityHealthAnalyticsCustomModule" `  




#### `UpdateEventThreatDetectionCustomModule`

  * **Method** : `google.cloud.securitycentermanagement.v1.SecurityCenterManagement.UpdateEventThreatDetectionCustomModule`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `securitycentermanagement.eventThreatDetectionCustomModules.update - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.securitycentermanagement.v1.SecurityCenterManagement.UpdateEventThreatDetectionCustomModule" `  




#### `UpdateSecurityCenterService`

  * **Method** : `google.cloud.securitycentermanagement.v1.SecurityCenterManagement.UpdateSecurityCenterService`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `securitycentermanagement.securityCenterServices.update - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.securitycentermanagement.v1.SecurityCenterManagement.UpdateSecurityCenterService" `  




#### `UpdateSecurityHealthAnalyticsCustomModule`

  * **Method** : `google.cloud.securitycentermanagement.v1.SecurityCenterManagement.UpdateSecurityHealthAnalyticsCustomModule`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `securitycentermanagement.securityHealthAnalyticsCustomModules.update - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.securitycentermanagement.v1.SecurityCenterManagement.UpdateSecurityHealthAnalyticsCustomModule" `  




#### `ValidateEventThreatDetectionCustomModule`

  * **Method** : `google.cloud.securitycentermanagement.v1.SecurityCenterManagement.ValidateEventThreatDetectionCustomModule`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `securitycentermanagement.eventThreatDetectionCustomModules.validate - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.securitycentermanagement.v1.SecurityCenterManagement.ValidateEventThreatDetectionCustomModule" `  




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
