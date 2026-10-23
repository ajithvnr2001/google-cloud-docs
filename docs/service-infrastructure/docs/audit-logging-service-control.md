---
url: https://docs.cloud.google.com/service-infrastructure/docs/audit-logging-service-control/
title: Service Control audit logging \u00a0|\u00a0 Service Infrastructure \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:53:24.236242+00:00
---

# Service Control audit logging  |  Service Infrastructure  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/service-infrastructure/docs/audit-logging-service-control/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Service Infrastructure ](https://docs.cloud.google.com/service-infrastructure/docs)
  * [ Guides ](https://docs.cloud.google.com/service-infrastructure/docs/how-to)



Send feedback 

#  Service Control audit logging Stay organized with collections  Save and categorize content based on your preferences. 

This document lists the audited methods for Service Control. Google Cloud services generate audit logs that record administrative and access activities within your Google Cloud resources. For more information about Cloud Audit Logs, see the following: 

  * [Types of audit logs](https://docs.cloud.google.com/logging/docs/audit#types)
  * [Audit log entry structure](https://docs.cloud.google.com/logging/docs/audit#audit_log_entry_structure)
  * [Storing and routing audit logs](https://docs.cloud.google.com/logging/docs/audit#storing_and_routing_audit_logs)
  * [Cloud Logging pricing summary](https://docs.cloud.google.com/stackdriver/pricing#logs-pricing-summary)
  * [Enable Data Access audit logs](https://docs.cloud.google.com/logging/docs/audit/configure-data-access)



## Service name

To view the Service Control audit logs, do the following:

  1. In the Google Cloud console, go to the Logs Explorer page:

[Go to Logs Explorer](https://console.cloud.google.com/logs/query)

  2. Copy and paste the following query into the **Query** field of the Logs Explorer, and then click **Run query**.
         
         protoPayload.serviceName="servicecontrol.googleapis.com"
           




## Methods by permission type

Each IAM permission has a `type` property, whose value is an enum that can be one of four values: `ADMIN_READ`, `ADMIN_WRITE`, `DATA_READ`, or `DATA_WRITE`. When you call a method, Service Control generates an audit log whose category is dependent on the `type` property of the permission required to perform the method. Methods that require an IAM permission with the `type` property value of `DATA_READ`, `DATA_WRITE`, or `ADMIN_READ` generate [Data Access](https://docs.cloud.google.com/logging/docs/audit#data-access) audit logs. Methods that require an IAM permission with the `type` property value of `ADMIN_WRITE` generate [Admin Activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity) audit logs.

API methods in the following list that are marked with (LRO) are long-running operations (LROs). These methods usually generate two audit log entries: one when the operation starts and another when it ends. For more information see [Audit logs for long-running operations](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro). Permission type | Methods  
---|---  
`OTHER` | `google.api.servicecontrol.v1.QuotaController.AllocateQuota`: To enable this log, enable `DATA_WRITE` under the service `servicemanagement.googleapis.com`.  
`google.api.servicecontrol.v1.ServiceController.Check`: To enable this log, enable `DATA_WRITE` under the service `servicemanagement.googleapis.com`.  
`google.api.servicecontrol.v1.ServiceController.Report`: To enable this log, enable `DATA_WRITE` under the service `servicemanagement.googleapis.com`.  
`google.api.servicecontrol.v2.ServiceController.Check`: To enable this log, enable `DATA_WRITE` under the service `servicemanagement.googleapis.com`.  
`google.api.servicecontrol.v2.ServiceController.Report`: To enable this log, enable `DATA_WRITE` under the service `servicemanagement.googleapis.com`.  
  
## API interface audit logs

For information about how and which permissions are evaluated for each method, see the Identity and Access Management documentation for Service Control.

### `google.api.servicecontrol.v1.QuotaController`

The following audit logs are associated with methods belonging to `google.api.servicecontrol.v1.QuotaController`.

#### `AllocateQuota`

  * **Method** : `google.api.servicecontrol.v1.QuotaController.AllocateQuota`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `servicemanagement.services.quota - DATA_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.api.servicecontrol.v1.QuotaController.AllocateQuota" `  




### `google.api.servicecontrol.v1.ServiceController`

The following audit logs are associated with methods belonging to `google.api.servicecontrol.v1.ServiceController`.

#### `Check`

  * **Method** : `google.api.servicecontrol.v1.ServiceController.Check`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `servicemanagement.services.check - DATA_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.api.servicecontrol.v1.ServiceController.Check" `  




#### `Report`

  * **Method** : `google.api.servicecontrol.v1.ServiceController.Report`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `servicemanagement.services.report - DATA_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.api.servicecontrol.v1.ServiceController.Report" `  




### `google.api.servicecontrol.v2.ServiceController`

The following audit logs are associated with methods belonging to `google.api.servicecontrol.v2.ServiceController`.

#### `Check`

  * **Method** : `google.api.servicecontrol.v2.ServiceController.Check`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `servicemanagement.services.check - DATA_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.api.servicecontrol.v2.ServiceController.Check" `  




#### `Report`

  * **Method** : `google.api.servicecontrol.v2.ServiceController.Report`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `servicemanagement.services.report - DATA_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.api.servicecontrol.v2.ServiceController.Report" `  




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
