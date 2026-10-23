---
url: https://docs.cloud.google.com/threat-intelligence/audit-logging/
title: Google Threat Intelligence Alerts audit logging \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T09:40:24.535245+00:00
---

# Google Threat Intelligence Alerts audit logging  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/threat-intelligence/audit-logging/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Threat Intelligence ](https://docs.cloud.google.com/threat-intelligence)
  * [ Guides ](https://docs.cloud.google.com/threat-intelligence/guides/concepts)



Send feedback 

#  Google Threat Intelligence Alerts audit logging Stay organized with collections  Save and categorize content based on your preferences. 

This document lists the audited methods for Threat Intelligence Service. Google Cloud services generate audit logs that record administrative and access activities within your Google Cloud resources. For more information about Cloud Audit Logs, see the following: 

  * [Types of audit logs](https://docs.cloud.google.com/logging/docs/audit#types)
  * [Audit log entry structure](https://docs.cloud.google.com/logging/docs/audit#audit_log_entry_structure)
  * [Storing and routing audit logs](https://docs.cloud.google.com/logging/docs/audit#storing_and_routing_audit_logs)
  * [Cloud Logging pricing summary](https://docs.cloud.google.com/stackdriver/pricing#logs-pricing-summary)
  * [Enable Data Access audit logs](https://docs.cloud.google.com/logging/docs/audit/configure-data-access)



## Service name

To view the Threat Intelligence Service audit logs, do the following:

  1. In the Google Cloud console, go to the Logs Explorer page:

[Go to Logs Explorer](https://console.cloud.google.com/logs/query)

  2. Copy and paste the following query into the **Query** field of the Logs Explorer, and then click **Run query**.
         
         protoPayload.serviceName="threatintelligence.googleapis.com"
           




## Methods by permission type

Each IAM permission has a `type` property, whose value is an enum that can be one of four values: `ADMIN_READ`, `ADMIN_WRITE`, `DATA_READ`, or `DATA_WRITE`. When you call a method, Threat Intelligence Service generates an audit log whose category is dependent on the `type` property of the permission required to perform the method. Methods that require an IAM permission with the `type` property value of `DATA_READ`, `DATA_WRITE`, or `ADMIN_READ` generate [Data Access](https://docs.cloud.google.com/logging/docs/audit#data-access) audit logs. Methods that require an IAM permission with the `type` property value of `ADMIN_WRITE` generate [Admin Activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity) audit logs.

API methods in the following list that are marked with (LRO) are long-running operations (LROs). These methods usually generate two audit log entries: one when the operation starts and another when it ends. For more information see [Audit logs for long-running operations](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro). Permission type | Methods  
---|---  
`DATA_READ` | `google.cloud.threatintelligence.v1beta.AlertService.EnumerateAlertFacets`  
`google.cloud.threatintelligence.v1beta.AlertService.GetAlert`  
`google.cloud.threatintelligence.v1beta.AlertService.GetAlertDocument`  
`google.cloud.threatintelligence.v1beta.AlertService.ListAlerts`  
`google.cloud.threatintelligence.v1beta.ConfigurationService.GetConfiguration`  
`google.cloud.threatintelligence.v1beta.ConfigurationService.ListConfigurationRevisions`  
`google.cloud.threatintelligence.v1beta.ConfigurationService.ListConfigurations`  
`google.cloud.threatintelligence.v1beta.FindingService.GetFinding`  
`google.cloud.threatintelligence.v1beta.FindingService.ListFindings`  
`google.cloud.threatintelligence.v1beta.FindingService.SearchFindings`  
`DATA_WRITE` | `google.cloud.threatintelligence.v1beta.AlertService.MarkAlertAsBenign`  
`google.cloud.threatintelligence.v1beta.AlertService.MarkAlertAsDuplicate`  
`google.cloud.threatintelligence.v1beta.AlertService.MarkAlertAsEscalated`  
`google.cloud.threatintelligence.v1beta.AlertService.MarkAlertAsFalsePositive`  
`google.cloud.threatintelligence.v1beta.AlertService.MarkAlertAsNotActionable`  
`google.cloud.threatintelligence.v1beta.AlertService.MarkAlertAsRead`  
`google.cloud.threatintelligence.v1beta.AlertService.MarkAlertAsResolved`  
`google.cloud.threatintelligence.v1beta.AlertService.MarkAlertAsTrackedExternally`  
`google.cloud.threatintelligence.v1beta.AlertService.MarkAlertAsTriaged`  
`google.cloud.threatintelligence.v1beta.ConfigurationService.GenerateOrgProfileConfiguration`  
`google.cloud.threatintelligence.v1beta.ConfigurationService.UpsertConfiguration`  
  
## API interface audit logs

For information about how and which permissions are evaluated for each method, see the Identity and Access Management documentation for Threat Intelligence Service.

### `google.cloud.threatintelligence.v1beta.AlertService`

The following audit logs are associated with methods belonging to `google.cloud.threatintelligence.v1beta.AlertService`.

#### `EnumerateAlertFacets`

  * **Method** : `google.cloud.threatintelligence.v1beta.AlertService.EnumerateAlertFacets`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `threatintelligence.alerts.list - DATA_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.threatintelligence.v1beta.AlertService.EnumerateAlertFacets" `  




#### `GetAlert`

  * **Method** : `google.cloud.threatintelligence.v1beta.AlertService.GetAlert`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `threatintelligence.alerts.get - DATA_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.threatintelligence.v1beta.AlertService.GetAlert" `  




#### `GetAlertDocument`

  * **Method** : `google.cloud.threatintelligence.v1beta.AlertService.GetAlertDocument`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `threatintelligence.alertdocuments.get - DATA_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.threatintelligence.v1beta.AlertService.GetAlertDocument" `  




#### `ListAlerts`

  * **Method** : `google.cloud.threatintelligence.v1beta.AlertService.ListAlerts`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `threatintelligence.alerts.list - DATA_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.threatintelligence.v1beta.AlertService.ListAlerts" `  




#### `MarkAlertAsBenign`

  * **Method** : `google.cloud.threatintelligence.v1beta.AlertService.MarkAlertAsBenign`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `threatintelligence.alerts.update - DATA_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.threatintelligence.v1beta.AlertService.MarkAlertAsBenign" `  




#### `MarkAlertAsDuplicate`

  * **Method** : `google.cloud.threatintelligence.v1beta.AlertService.MarkAlertAsDuplicate`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `threatintelligence.alerts.update - DATA_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.threatintelligence.v1beta.AlertService.MarkAlertAsDuplicate" `  




#### `MarkAlertAsEscalated`

  * **Method** : `google.cloud.threatintelligence.v1beta.AlertService.MarkAlertAsEscalated`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `threatintelligence.alerts.update - DATA_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.threatintelligence.v1beta.AlertService.MarkAlertAsEscalated" `  




#### `MarkAlertAsFalsePositive`

  * **Method** : `google.cloud.threatintelligence.v1beta.AlertService.MarkAlertAsFalsePositive`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `threatintelligence.alerts.update - DATA_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.threatintelligence.v1beta.AlertService.MarkAlertAsFalsePositive" `  




#### `MarkAlertAsNotActionable`

  * **Method** : `google.cloud.threatintelligence.v1beta.AlertService.MarkAlertAsNotActionable`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `threatintelligence.alerts.update - DATA_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.threatintelligence.v1beta.AlertService.MarkAlertAsNotActionable" `  




#### `MarkAlertAsRead`

  * **Method** : `google.cloud.threatintelligence.v1beta.AlertService.MarkAlertAsRead`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `threatintelligence.alerts.update - DATA_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.threatintelligence.v1beta.AlertService.MarkAlertAsRead" `  




#### `MarkAlertAsResolved`

  * **Method** : `google.cloud.threatintelligence.v1beta.AlertService.MarkAlertAsResolved`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `threatintelligence.alerts.update - DATA_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.threatintelligence.v1beta.AlertService.MarkAlertAsResolved" `  




#### `MarkAlertAsTrackedExternally`

  * **Method** : `google.cloud.threatintelligence.v1beta.AlertService.MarkAlertAsTrackedExternally`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `threatintelligence.alerts.update - DATA_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.threatintelligence.v1beta.AlertService.MarkAlertAsTrackedExternally" `  




#### `MarkAlertAsTriaged`

  * **Method** : `google.cloud.threatintelligence.v1beta.AlertService.MarkAlertAsTriaged`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `threatintelligence.alerts.update - DATA_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.threatintelligence.v1beta.AlertService.MarkAlertAsTriaged" `  




### `google.cloud.threatintelligence.v1beta.ConfigurationService`

The following audit logs are associated with methods belonging to `google.cloud.threatintelligence.v1beta.ConfigurationService`.

#### `GenerateOrgProfileConfiguration`

  * **Method** : `google.cloud.threatintelligence.v1beta.ConfigurationService.GenerateOrgProfileConfiguration`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `threatintelligence.configurations.create - DATA_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.threatintelligence.v1beta.ConfigurationService.GenerateOrgProfileConfiguration" `  




#### `GetConfiguration`

  * **Method** : `google.cloud.threatintelligence.v1beta.ConfigurationService.GetConfiguration`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `threatintelligence.configurations.get - DATA_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.threatintelligence.v1beta.ConfigurationService.GetConfiguration" `  




#### `ListConfigurationRevisions`

  * **Method** : `google.cloud.threatintelligence.v1beta.ConfigurationService.ListConfigurationRevisions`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `threatintelligence.configurations.listRevisions - DATA_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.threatintelligence.v1beta.ConfigurationService.ListConfigurationRevisions" `  




#### `ListConfigurations`

  * **Method** : `google.cloud.threatintelligence.v1beta.ConfigurationService.ListConfigurations`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `threatintelligence.configurations.list - DATA_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.threatintelligence.v1beta.ConfigurationService.ListConfigurations" `  




#### `UpsertConfiguration`

  * **Method** : `google.cloud.threatintelligence.v1beta.ConfigurationService.UpsertConfiguration`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `threatintelligence.configurations.update - DATA_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.threatintelligence.v1beta.ConfigurationService.UpsertConfiguration" `  




### `google.cloud.threatintelligence.v1beta.FindingService`

The following audit logs are associated with methods belonging to `google.cloud.threatintelligence.v1beta.FindingService`.

#### `GetFinding`

  * **Method** : `google.cloud.threatintelligence.v1beta.FindingService.GetFinding`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `threatintelligence.findings.get - DATA_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.threatintelligence.v1beta.FindingService.GetFinding" `  




#### `ListFindings`

  * **Method** : `google.cloud.threatintelligence.v1beta.FindingService.ListFindings`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `threatintelligence.findings.list - DATA_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.threatintelligence.v1beta.FindingService.ListFindings" `  




#### `SearchFindings`

  * **Method** : `google.cloud.threatintelligence.v1beta.FindingService.SearchFindings`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `threatintelligence.findings.list - DATA_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.threatintelligence.v1beta.FindingService.SearchFindings" `  




## Methods that don't produce audit logs

A method might not produce audit logs for one or more of the following reasons: 

  * It is a high volume method involving significant log generation and storage costs.
  * It has low auditing value.
  * Another audit or platform log already provides method coverage.



The following methods don't produce audit logs:

  * `google.longrunning.Operations.CancelOperation`
  * `google.longrunning.Operations.DeleteOperation`
  * `google.longrunning.Operations.GetOperation`
  * `google.longrunning.Operations.ListOperations`
  * `google.longrunning.Operations.WaitOperation`



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
