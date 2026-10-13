---
url: https://docs.cloud.google.com/security-command-center/docs/audit-logging-security-posture/
title: Security posture audit logging \u00a0|\u00a0 Security Command Center \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T18:14:18.879417+00:00
---

# Security posture audit logging  |  Security Command Center  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/security-command-center/docs/audit-logging-security-posture/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Security Command Center ](https://docs.cloud.google.com/security-command-center/docs)
  * [ Guides ](https://docs.cloud.google.com/security-command-center/docs/security-command-center-overview)



Send feedback 

#  Security posture audit logging Stay organized with collections  Save and categorize content based on your preferences. 

Premium and Enterprise (Deprecated) [service tiers](https://docs.cloud.google.com/security-command-center/docs/service-tiers) (requires [organization-level activation](https://docs.cloud.google.com/security-command-center/docs/activate-scc-overview#overview_of_organization-level_activation)) The Security Command Center Enterprise service tier will shut down on May 21, 2027. If your organization uses the Enterprise service tier, then the organization will automatically move to the Premium service tier on or after May 21, 2027. Contact your account representative or a [Google Cloud sales specialist](https://cloud.google.com/contact) if you have questions. 

This document lists the audited methods for Security posture. Google Cloud services generate audit logs that record administrative and access activities within your Google Cloud resources. For more information about Cloud Audit Logs, see the following: 

  * [Types of audit logs](https://docs.cloud.google.com/logging/docs/audit#types)
  * [Audit log entry structure](https://docs.cloud.google.com/logging/docs/audit#audit_log_entry_structure)
  * [Storing and routing audit logs](https://docs.cloud.google.com/logging/docs/audit#storing_and_routing_audit_logs)
  * [Cloud Logging pricing summary](https://docs.cloud.google.com/stackdriver/pricing#logs-pricing-summary)
  * [Enable Data Access audit logs](https://docs.cloud.google.com/logging/docs/audit/configure-data-access)



## Service name

To view the Security posture audit logs, do the following:

  1. In the Google Cloud console, go to the Logs Explorer page:

[Go to Logs Explorer](https://console.cloud.google.com/logs/query)

  2. Copy and paste the following query into the **Query** field of the Logs Explorer, and then click **Run query**.
         
         protoPayload.serviceName="securityposture.googleapis.com"
           




## Methods by permission type

Each IAM permission has a `type` property, whose value is an enum that can be one of four values: `ADMIN_READ`, `ADMIN_WRITE`, `DATA_READ`, or `DATA_WRITE`. When you call a method, Security posture generates an audit log whose category is dependent on the `type` property of the permission required to perform the method. Methods that require an IAM permission with the `type` property value of `DATA_READ`, `DATA_WRITE`, or `ADMIN_READ` generate [Data Access](https://docs.cloud.google.com/logging/docs/audit#data-access) audit logs. Methods that require an IAM permission with the `type` property value of `ADMIN_WRITE` generate [Admin Activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity) audit logs.

API methods in the following list that are marked with (LRO) are long-running operations (LROs). These methods usually generate two audit log entries: one when the operation starts and another when it ends. For more information see [Audit logs for long-running operations](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro). Permission type | Methods  
---|---  
`DATA_READ` | `google.cloud.securityposture.v1.SecurityPosture.GetPosture`  
`google.cloud.securityposture.v1.SecurityPosture.GetPostureDeployment`  
`google.cloud.securityposture.v1.SecurityPosture.GetPostureTemplate`  
`google.cloud.securityposture.v1.SecurityPosture.GetReport`  
`google.cloud.securityposture.v1.SecurityPosture.ListPostureDeployments`  
`google.cloud.securityposture.v1.SecurityPosture.ListPostureRevisions`  
`google.cloud.securityposture.v1.SecurityPosture.ListPostureTemplates`  
`google.cloud.securityposture.v1.SecurityPosture.ListPostures`  
`google.cloud.securityposture.v1.SecurityPosture.ListReports`  
`DATA_WRITE` | `google.cloud.securityposture.v1.SecurityPosture.CreatePosture` (LRO)  
`google.cloud.securityposture.v1.SecurityPosture.CreatePostureDeployment` (LRO)  
`google.cloud.securityposture.v1.SecurityPosture.DeletePosture` (LRO)  
`google.cloud.securityposture.v1.SecurityPosture.DeletePostureDeployment` (LRO)  
`google.cloud.securityposture.v1.SecurityPosture.ExtractPosture` (LRO)  
`google.cloud.securityposture.v1.SecurityPosture.UpdatePosture` (LRO)  
`google.cloud.securityposture.v1.SecurityPosture.UpdatePostureDeployment` (LRO)  
  
## API interface audit logs

For information about how and which permissions are evaluated for each method, see the [Identity and Access Management documentation](https://docs.cloud.google.com/security-command-center/docs/access-control) for Security posture.

### `google.cloud.securityposture.v1.SecurityPosture`

The following audit logs are associated with methods belonging to `google.cloud.securityposture.v1.SecurityPosture`.

#### `CreatePosture`

  * **Method** : `google.cloud.securityposture.v1.SecurityPosture.CreatePosture`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `securityposture.postures.create - DATA_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.securityposture.v1.SecurityPosture.CreatePosture" `  




#### `CreatePostureDeployment`

  * **Method** : `google.cloud.securityposture.v1.SecurityPosture.CreatePostureDeployment`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `securityposture.postureDeployments.create - DATA_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.securityposture.v1.SecurityPosture.CreatePostureDeployment" `  




#### `DeletePosture`

  * **Method** : `google.cloud.securityposture.v1.SecurityPosture.DeletePosture`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `securityposture.postures.delete - DATA_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.securityposture.v1.SecurityPosture.DeletePosture" `  




#### `DeletePostureDeployment`

  * **Method** : `google.cloud.securityposture.v1.SecurityPosture.DeletePostureDeployment`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `securityposture.postureDeployments.delete - DATA_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.securityposture.v1.SecurityPosture.DeletePostureDeployment" `  




#### `ExtractPosture`

  * **Method** : `google.cloud.securityposture.v1.SecurityPosture.ExtractPosture`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `securityposture.postures.extract - DATA_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.securityposture.v1.SecurityPosture.ExtractPosture" `  




#### `GetPosture`

  * **Method** : `google.cloud.securityposture.v1.SecurityPosture.GetPosture`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `securityposture.postures.get - DATA_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.securityposture.v1.SecurityPosture.GetPosture" `  




#### `GetPostureDeployment`

  * **Method** : `google.cloud.securityposture.v1.SecurityPosture.GetPostureDeployment`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `securityposture.postureDeployments.get - DATA_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.securityposture.v1.SecurityPosture.GetPostureDeployment" `  




#### `GetPostureTemplate`

  * **Method** : `google.cloud.securityposture.v1.SecurityPosture.GetPostureTemplate`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `securityposture.postureTemplates.get - DATA_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.securityposture.v1.SecurityPosture.GetPostureTemplate" `  




#### `GetReport`

  * **Method** : `google.cloud.securityposture.v1.SecurityPosture.GetReport`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `securityposture.reports.get - DATA_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.securityposture.v1.SecurityPosture.GetReport" `  




#### `ListPostureDeployments`

  * **Method** : `google.cloud.securityposture.v1.SecurityPosture.ListPostureDeployments`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `securityposture.postureDeployments.list - DATA_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.securityposture.v1.SecurityPosture.ListPostureDeployments" `  




#### `ListPostureRevisions`

  * **Method** : `google.cloud.securityposture.v1.SecurityPosture.ListPostureRevisions`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `securityposture.postures.get - DATA_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.securityposture.v1.SecurityPosture.ListPostureRevisions" `  




#### `ListPostureTemplates`

  * **Method** : `google.cloud.securityposture.v1.SecurityPosture.ListPostureTemplates`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `securityposture.postureTemplates.list - DATA_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.securityposture.v1.SecurityPosture.ListPostureTemplates" `  




#### `ListPostures`

  * **Method** : `google.cloud.securityposture.v1.SecurityPosture.ListPostures`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `securityposture.postures.list - DATA_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.securityposture.v1.SecurityPosture.ListPostures" `  




#### `ListReports`

  * **Method** : `google.cloud.securityposture.v1.SecurityPosture.ListReports`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `securityposture.reports.list - DATA_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.securityposture.v1.SecurityPosture.ListReports" `  




#### `UpdatePosture`

  * **Method** : `google.cloud.securityposture.v1.SecurityPosture.UpdatePosture`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `securityposture.postures.update - DATA_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.securityposture.v1.SecurityPosture.UpdatePosture" `  




#### `UpdatePostureDeployment`

  * **Method** : `google.cloud.securityposture.v1.SecurityPosture.UpdatePostureDeployment`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `securityposture.postureDeployments.update - DATA_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.securityposture.v1.SecurityPosture.UpdatePostureDeployment" `  




## Methods that don't produce audit logs

A method might not produce audit logs for one or more of the following reasons: 

  * It is a high volume method involving significant log generation and storage costs.
  * It has low auditing value.
  * Another audit or platform log already provides method coverage.



The following methods don't produce audit logs:

  * `google.cloud.location.Locations.GetLocation`
  * `google.cloud.location.Locations.ListLocations`
  * `google.cloud.securityposture.v1.SecurityPosture.CreateIaCValidationReport`
  * `google.longrunning.Operations.CancelOperation`
  * `google.longrunning.Operations.DeleteOperation`
  * `google.longrunning.Operations.GetOperation`
  * `google.longrunning.Operations.ListOperations`
  * `google.longrunning.Operations.WaitOperation`



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
