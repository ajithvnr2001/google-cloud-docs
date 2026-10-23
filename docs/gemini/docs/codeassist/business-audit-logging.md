---
url: https://docs.cloud.google.com/gemini/docs/codeassist/business-audit-logging/
title: Business AI Code audit logging \u00a0|\u00a0 Gemini for Google Cloud \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T13:03:50.880510+00:00
---

# Business AI Code audit logging  |  Gemini for Google Cloud  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/gemini/docs/codeassist/business-audit-logging/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini for Google Cloud ](https://docs.cloud.google.com/gemini/docs)
  * [ Guides ](https://docs.cloud.google.com/gemini/docs/overview)



Send feedback 

#  Business AI Code audit logging Stay organized with collections  Save and categorize content based on your preferences. 

This document lists the audited methods for Business AI Code. Google Cloud services generate audit logs that record administrative and access activities within your Google Cloud resources. For more information about Cloud Audit Logs, see the following: 

  * [Types of audit logs](https://docs.cloud.google.com/logging/docs/audit#types)
  * [Audit log entry structure](https://docs.cloud.google.com/logging/docs/audit#audit_log_entry_structure)
  * [Storing and routing audit logs](https://docs.cloud.google.com/logging/docs/audit#storing_and_routing_audit_logs)
  * [Cloud Logging pricing summary](https://docs.cloud.google.com/stackdriver/pricing#logs-pricing-summary)
  * [Enable Data Access audit logs](https://docs.cloud.google.com/logging/docs/audit/configure-data-access)



## Service name

To view the Business AI Code audit logs, do the following:

  1. In the Google Cloud console, go to the Logs Explorer page:

[Go to Logs Explorer](https://console.cloud.google.com/logs/query)

  2. Copy and paste the following query into the **Query** field of the Logs Explorer, and then click **Run query**.
         
         protoPayload.serviceName="businessaicode.googleapis.com"
           




## Methods by permission type

Each IAM permission has a `type` property, whose value is an enum that can be one of four values: `ADMIN_READ`, `ADMIN_WRITE`, `DATA_READ`, or `DATA_WRITE`. When you call a method, Business AI Code generates an audit log whose category is dependent on the `type` property of the permission required to perform the method. Methods that require an IAM permission with the `type` property value of `DATA_READ`, `DATA_WRITE`, or `ADMIN_READ` generate [Data Access](https://docs.cloud.google.com/logging/docs/audit#data-access) audit logs. Methods that require an IAM permission with the `type` property value of `ADMIN_WRITE` generate [Admin Activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity) audit logs.

API methods in the following list that are marked with (LRO) are long-running operations (LROs). These methods usually generate two audit log entries: one when the operation starts and another when it ends. For more information see [Audit logs for long-running operations](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro). Permission type | Methods  
---|---  
`DATA_READ` | `google.cloud.businessaicode.v1alpha.ManagementService.FetchConfig`  
`google.cloud.businessaicode.v1alpha.PredictionService.FetchQuotaStatus`  
`google.cloud.businessaicode.v1alpha.PredictionService.GenerateContent`  
`google.cloud.businessaicode.v1alpha.PredictionService.QueryConfig`  
`google.cloud.businessaicode.v1alpha.PredictionService.StreamGenerateContent`  
`google.cloud.businessaicode.v1beta.ManagementService.FetchConfig`  
`google.cloud.businessaicode.v1beta.PredictionService.FetchQuotaStatus`  
`google.cloud.businessaicode.v1beta.PredictionService.GenerateContent`  
`google.cloud.businessaicode.v1beta.PredictionService.QueryConfig`  
`google.cloud.businessaicode.v1beta.PredictionService.StreamGenerateContent`  
`google.cloud.businessaicode.v1main.PredictionService.QueryConfig`  
`DATA_WRITE` | `google.cloud.businessaicode.v1alpha.ManagementService.SelfAssignLicense`  
`google.cloud.businessaicode.v1alpha.PredictionService.SendTelemetry`  
`google.cloud.businessaicode.v1alpha.TelemetryService.SendTelemetry`  
`google.cloud.businessaicode.v1beta.ManagementService.SelfAssignLicense`  
`google.cloud.businessaicode.v1beta.PredictionService.SendTelemetry`  
`google.cloud.businessaicode.v1beta.TelemetryService.SendTelemetry`  
`google.cloud.businessaicode.v1main.PredictionService.SendTelemetry`  
  
## API interface audit logs

For information about how and which permissions are evaluated for each method, see the Identity and Access Management documentation for Business AI Code.

### `google.cloud.businessaicode.v1alpha.ManagementService`

The following audit logs are associated with methods belonging to `google.cloud.businessaicode.v1alpha.ManagementService`.

#### `FetchConfig`

  * **Method** : `google.cloud.businessaicode.v1alpha.ManagementService.FetchConfig`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `businessaicode.locations.queryConfiguration - DATA_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.businessaicode.v1alpha.ManagementService.FetchConfig" `  




#### `SelfAssignLicense`

  * **Method** : `google.cloud.businessaicode.v1alpha.ManagementService.SelfAssignLicense`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `businessaicode.locations.selfAssignLicense - DATA_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.businessaicode.v1alpha.ManagementService.SelfAssignLicense" `  




### `google.cloud.businessaicode.v1alpha.PredictionService`

The following audit logs are associated with methods belonging to `google.cloud.businessaicode.v1alpha.PredictionService`.

#### `FetchQuotaStatus`

  * **Method** : `google.cloud.businessaicode.v1alpha.PredictionService.FetchQuotaStatus`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `businessaicode.locations.fetchQuotaStatus - DATA_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.businessaicode.v1alpha.PredictionService.FetchQuotaStatus" `  




#### `GenerateContent`

  * **Method** : `google.cloud.businessaicode.v1alpha.PredictionService.GenerateContent`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `businessaicode.locations.generateContent - DATA_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.businessaicode.v1alpha.PredictionService.GenerateContent" `  




#### `QueryConfig`

  * **Method** : `google.cloud.businessaicode.v1alpha.PredictionService.QueryConfig`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `businessaicode.locations.queryConfiguration - DATA_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.businessaicode.v1alpha.PredictionService.QueryConfig" `  




#### `SendTelemetry`

  * **Method** : `google.cloud.businessaicode.v1alpha.PredictionService.SendTelemetry`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `businessaicode.locations.sendTelemetry - DATA_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.businessaicode.v1alpha.PredictionService.SendTelemetry" `  




#### `StreamGenerateContent`

  * **Method** : `google.cloud.businessaicode.v1alpha.PredictionService.StreamGenerateContent`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `businessaicode.locations.generateContent - DATA_READ`
  * **Method is a long-running or streaming operation** : [**Streaming RPC**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#streaming)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.businessaicode.v1alpha.PredictionService.StreamGenerateContent" `  




### `google.cloud.businessaicode.v1alpha.TelemetryService`

The following audit logs are associated with methods belonging to `google.cloud.businessaicode.v1alpha.TelemetryService`.

#### `SendTelemetry`

  * **Method** : `google.cloud.businessaicode.v1alpha.TelemetryService.SendTelemetry`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `businessaicode.locations.sendTelemetry - DATA_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.businessaicode.v1alpha.TelemetryService.SendTelemetry" `  




### `google.cloud.businessaicode.v1beta.ManagementService`

The following audit logs are associated with methods belonging to `google.cloud.businessaicode.v1beta.ManagementService`.

#### `FetchConfig`

  * **Method** : `google.cloud.businessaicode.v1beta.ManagementService.FetchConfig`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `businessaicode.locations.queryConfiguration - DATA_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.businessaicode.v1beta.ManagementService.FetchConfig" `  




#### `SelfAssignLicense`

  * **Method** : `google.cloud.businessaicode.v1beta.ManagementService.SelfAssignLicense`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `businessaicode.locations.selfAssignLicense - DATA_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.businessaicode.v1beta.ManagementService.SelfAssignLicense" `  




### `google.cloud.businessaicode.v1beta.PredictionService`

The following audit logs are associated with methods belonging to `google.cloud.businessaicode.v1beta.PredictionService`.

#### `FetchQuotaStatus`

  * **Method** : `google.cloud.businessaicode.v1beta.PredictionService.FetchQuotaStatus`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `businessaicode.locations.fetchQuotaStatus - DATA_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.businessaicode.v1beta.PredictionService.FetchQuotaStatus" `  




#### `GenerateContent`

  * **Method** : `google.cloud.businessaicode.v1beta.PredictionService.GenerateContent`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `businessaicode.locations.generateContent - DATA_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.businessaicode.v1beta.PredictionService.GenerateContent" `  




#### `QueryConfig`

  * **Method** : `google.cloud.businessaicode.v1beta.PredictionService.QueryConfig`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `businessaicode.locations.queryConfiguration - DATA_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.businessaicode.v1beta.PredictionService.QueryConfig" `  




#### `SendTelemetry`

  * **Method** : `google.cloud.businessaicode.v1beta.PredictionService.SendTelemetry`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `businessaicode.locations.sendTelemetry - DATA_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.businessaicode.v1beta.PredictionService.SendTelemetry" `  




#### `StreamGenerateContent`

  * **Method** : `google.cloud.businessaicode.v1beta.PredictionService.StreamGenerateContent`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `businessaicode.locations.generateContent - DATA_READ`
  * **Method is a long-running or streaming operation** : [**Streaming RPC**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#streaming)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.businessaicode.v1beta.PredictionService.StreamGenerateContent" `  




### `google.cloud.businessaicode.v1beta.TelemetryService`

The following audit logs are associated with methods belonging to `google.cloud.businessaicode.v1beta.TelemetryService`.

#### `SendTelemetry`

  * **Method** : `google.cloud.businessaicode.v1beta.TelemetryService.SendTelemetry`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `businessaicode.locations.sendTelemetry - DATA_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.businessaicode.v1beta.TelemetryService.SendTelemetry" `  




### `google.cloud.businessaicode.v1main.PredictionService`

The following audit logs are associated with methods belonging to `google.cloud.businessaicode.v1main.PredictionService`.

#### `QueryConfig`

  * **Method** : `google.cloud.businessaicode.v1main.PredictionService.QueryConfig`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `businessaicode.locations.queryConfiguration - DATA_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.businessaicode.v1main.PredictionService.QueryConfig" `  




#### `SendTelemetry`

  * **Method** : `google.cloud.businessaicode.v1main.PredictionService.SendTelemetry`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `businessaicode.locations.sendTelemetry - DATA_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.businessaicode.v1main.PredictionService.SendTelemetry" `  




## Methods that don't produce audit logs

A method might not produce audit logs for one or more of the following reasons: 

  * It is a high volume method involving significant log generation and storage costs.
  * It has low auditing value.
  * Another audit or platform log already provides method coverage.



The following methods don't produce audit logs:

  * `google.cloud.businessaicode.v1alpha.ManagementService.FetchLicenses`
  * `google.cloud.businessaicode.v1beta.ManagementService.FetchLicenses`



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
