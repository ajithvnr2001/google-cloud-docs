---
url: https://docs.cloud.google.com/error-reporting/docs/audit-logging/
title: Error Reporting audit logging \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-20T20:44:46.660137+00:00
---

# Error Reporting audit logging  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/error-reporting/docs/audit-logging/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Observability ](https://docs.cloud.google.com/docs/observability)
  * [ Error Reporting ](https://docs.cloud.google.com/error-reporting/docs)
  * [ Guides ](https://docs.cloud.google.com/error-reporting/docs/grouping-errors)



Send feedback 

#  Error Reporting audit logging Stay organized with collections  Save and categorize content based on your preferences. 

This document lists the audited methods for Error Reporting. Google Cloud services generate audit logs that record administrative and access activities within your Google Cloud resources. For more information about Cloud Audit Logs, see the following: 

  * [Types of audit logs](https://docs.cloud.google.com/logging/docs/audit#types)
  * [Audit log entry structure](https://docs.cloud.google.com/logging/docs/audit#audit_log_entry_structure)
  * [Storing and routing audit logs](https://docs.cloud.google.com/logging/docs/audit#storing_and_routing_audit_logs)
  * [Cloud Logging pricing summary](https://docs.cloud.google.com/stackdriver/pricing#logs-pricing-summary)
  * [Enable Data Access audit logs](https://docs.cloud.google.com/logging/docs/audit/configure-data-access)



## Service name

To view the Error Reporting audit logs, do the following:

  1. In the Google Cloud console, go to the Logs Explorer page:

[Go to Logs Explorer](https://console.cloud.google.com/logs/query)

  2. Copy and paste the following query into the **Query** field of the Logs Explorer, and then click **Run query**.
         
         protoPayload.serviceName="clouderrorreporting.googleapis.com"
           




## Methods by permission type

Each IAM permission has a `type` property, whose value is an enum that can be one of four values: `ADMIN_READ`, `ADMIN_WRITE`, `DATA_READ`, or `DATA_WRITE`. When you call a method, Error Reporting generates an audit log whose category is dependent on the `type` property of the permission required to perform the method. Methods that require an IAM permission with the `type` property value of `DATA_READ`, `DATA_WRITE`, or `ADMIN_READ` generate [Data Access](https://docs.cloud.google.com/logging/docs/audit#data-access) audit logs. Methods that require an IAM permission with the `type` property value of `ADMIN_WRITE` generate [Admin Activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity) audit logs.

API methods in the following list that are marked with (LRO) are long-running operations (LROs). These methods usually generate two audit log entries: one when the operation starts and another when it ends. For more information see [Audit logs for long-running operations](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro). Permission type | Methods  
---|---  
`ADMIN_READ` | `google.devtools.clouderrorreporting.v1beta1.ErrorGroupService.GetGroup`  
`ADMIN_WRITE` | `google.devtools.clouderrorreporting.v1beta1.ErrorGroupService.UpdateGroup`  
`google.devtools.clouderrorreporting.v1beta1.ErrorStatsService.DeleteEvents`  
`DATA_READ` | `google.devtools.clouderrorreporting.v1beta1.ErrorStatsService.ListEvents`  
`google.devtools.clouderrorreporting.v1beta1.ErrorStatsService.ListGroupStats`  
  
## API interface audit logs

For information about how and which permissions are evaluated for each method, see the Identity and Access Management documentation for Error Reporting.

### `google.devtools.clouderrorreporting.v1beta1.ErrorGroupService`

The following audit logs are associated with methods belonging to `google.devtools.clouderrorreporting.v1beta1.ErrorGroupService`.

#### `GetGroup`

  * **Method** : `google.devtools.clouderrorreporting.v1beta1.ErrorGroupService.GetGroup`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `errorreporting.groupMetadata.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.devtools.clouderrorreporting.v1beta1.ErrorGroupService.GetGroup" `  




#### `UpdateGroup`

  * **Method** : `google.devtools.clouderrorreporting.v1beta1.ErrorGroupService.UpdateGroup`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `errorreporting.groupMetadata.update - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.devtools.clouderrorreporting.v1beta1.ErrorGroupService.UpdateGroup" `  




### `google.devtools.clouderrorreporting.v1beta1.ErrorStatsService`

The following audit logs are associated with methods belonging to `google.devtools.clouderrorreporting.v1beta1.ErrorStatsService`.

#### `DeleteEvents`

  * **Method** : `google.devtools.clouderrorreporting.v1beta1.ErrorStatsService.DeleteEvents`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `errorreporting.errorEvents.delete - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.devtools.clouderrorreporting.v1beta1.ErrorStatsService.DeleteEvents" `  




#### `ListEvents`

  * **Method** : `google.devtools.clouderrorreporting.v1beta1.ErrorStatsService.ListEvents`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `errorreporting.errorEvents.list - DATA_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.devtools.clouderrorreporting.v1beta1.ErrorStatsService.ListEvents" `  




#### `ListGroupStats`

  * **Method** : `google.devtools.clouderrorreporting.v1beta1.ErrorStatsService.ListGroupStats`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `errorreporting.groups.list - DATA_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.devtools.clouderrorreporting.v1beta1.ErrorStatsService.ListGroupStats" `  




## Methods that don't produce audit logs

A method might not produce audit logs for one or more of the following reasons: 

  * It is a high volume method involving significant log generation and storage costs.
  * It has low auditing value.
  * Another audit or platform log already provides method coverage.



The following methods don't produce audit logs:

  * `google.devtools.clouderrorreporting.v1beta1.ReportErrorsService.ReportErrorEvent`



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
