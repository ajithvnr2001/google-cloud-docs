---
url: https://docs.cloud.google.com/bigtable/docs/audit-logging/
title: Cloud Bigtable API audit logging \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T00:29:12.728641+00:00
---

# Cloud Bigtable API audit logging  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/bigtable/docs/audit-logging/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Bigtable ](https://docs.cloud.google.com/bigtable/docs)
  * [ Guides ](https://docs.cloud.google.com/bigtable/docs/overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

#  Cloud Bigtable API audit logging

This document lists the audited methods for Cloud Bigtable API. Google Cloud services generate audit logs that record administrative and access activities within your Google Cloud resources. For more information about Cloud Audit Logs, see the following: 

  * [Types of audit logs](https://docs.cloud.google.com/logging/docs/audit#types)
  * [Audit log entry structure](https://docs.cloud.google.com/logging/docs/audit#audit_log_entry_structure)
  * [Storing and routing audit logs](https://docs.cloud.google.com/logging/docs/audit#storing_and_routing_audit_logs)
  * [Cloud Logging pricing summary](https://docs.cloud.google.com/stackdriver/pricing#logs-pricing-summary)
  * [Enable Data Access audit logs](https://docs.cloud.google.com/logging/docs/audit/configure-data-access)



## Notes

When a log entry exceeds the [size limit](https://docs.cloud.google.com/logging/docs/audit#quotas), Cloud Logging splits that entry and distributes the data across several entries. To learn how to identify and reassemble split audit logs, see [Split audit log entries](https://docs.cloud.google.com/logging/docs/audit/split-logs).

## Service name

To view the Cloud Bigtable API audit logs, do the following:

  1. In the Google Cloud console, go to the Logs Explorer page:

[Go to Logs Explorer](https://console.cloud.google.com/logs/query)

  2. Copy and paste the following query into the **Query** field of the Logs Explorer, and then click **Run query**.
         
         protoPayload.serviceName="bigtable.googleapis.com"
           




## Methods by permission type

For details about which fields are logged for Data Access audit logging, see [Audit log fields](https://docs.cloud.google.com/bigtable/docs/audit-log-fields). Before you enable Data Access audit logging, read [Managing Costs](https://docs.cloud.google.com/bigtable/docs/audit-log-estimate-costs).

Each IAM permission has a `type` property, whose value is an enum that can be one of four values: `ADMIN_READ`, `ADMIN_WRITE`, `DATA_READ`, or `DATA_WRITE`. When you call a method, Cloud Bigtable API generates an audit log whose category is dependent on the `type` property of the permission required to perform the method. Methods that require an IAM permission with the `type` property value of `DATA_READ`, `DATA_WRITE`, or `ADMIN_READ` generate [Data Access](https://docs.cloud.google.com/logging/docs/audit#data-access) audit logs. Methods that require an IAM permission with the `type` property value of `ADMIN_WRITE` generate [Admin Activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity) audit logs.

API methods in the following list that are marked with (LRO) are long-running operations (LROs). These methods usually generate two audit log entries: one when the operation starts and another when it ends. For more information see [Audit logs for long-running operations](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro). Permission type | Methods  
---|---  
`ADMIN_READ` | `google.bigtable.v2.Bigtable.PingAndWarm`  
`DATA_READ` | `google.bigtable.v2.Bigtable.ExecuteQuery`  
`google.bigtable.v2.Bigtable.GenerateInitialChangeStreamPartitions`  
`google.bigtable.v2.Bigtable.PrepareQuery`  
`google.bigtable.v2.Bigtable.ReadChangeStream`  
`google.bigtable.v2.Bigtable.ReadModifyWriteRow`  
`google.bigtable.v2.Bigtable.ReadRows`  
`google.bigtable.v2.Bigtable.SampleRowKeys`  
`DATA_WRITE` | `google.bigtable.v2.Bigtable.CheckAndMutateRow`  
`google.bigtable.v2.Bigtable.MutateRow`  
`google.bigtable.v2.Bigtable.MutateRows`  
`google.bigtable.v2.Bigtable.ReadModifyWriteRow`  
  
## API interface audit logs

For information about how and which permissions are evaluated for each method, see the Identity and Access Management documentation for Cloud Bigtable API.

### `google.bigtable.v2.Bigtable`

The following audit logs are associated with methods belonging to `google.bigtable.v2.Bigtable`.

#### `CheckAndMutateRow`

  * **Method** : `google.bigtable.v2.Bigtable.CheckAndMutateRow`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `bigtable.tables.mutateRows - DATA_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.bigtable.v2.Bigtable.CheckAndMutateRow" `  




#### `ExecuteQuery`

  * **Method** : `google.bigtable.v2.Bigtable.ExecuteQuery`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `bigtable.instances.executeQuery - DATA_READ`
    * `bigtable.tables.readRows - DATA_READ`
  * **Method is a long-running or streaming operation** : [**Streaming RPC**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#streaming)   

  * **Filter for this method** : ` protoPayload.methodName="google.bigtable.v2.Bigtable.ExecuteQuery" `  




#### `GenerateInitialChangeStreamPartitions`

  * **Method** : `google.bigtable.v2.Bigtable.GenerateInitialChangeStreamPartitions`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `bigtable.tables.readRows - DATA_READ`
  * **Method is a long-running or streaming operation** : [**Streaming RPC**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#streaming)   

  * **Filter for this method** : ` protoPayload.methodName="google.bigtable.v2.Bigtable.GenerateInitialChangeStreamPartitions" `  




#### `MutateRow`

  * **Method** : `google.bigtable.v2.Bigtable.MutateRow`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `bigtable.tables.mutateRows - DATA_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.bigtable.v2.Bigtable.MutateRow" `  




#### `MutateRows`

  * **Method** : `google.bigtable.v2.Bigtable.MutateRows`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `bigtable.tables.mutateRows - DATA_WRITE`
  * **Method is a long-running or streaming operation** : [**Streaming RPC**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#streaming)   

  * **Filter for this method** : ` protoPayload.methodName="google.bigtable.v2.Bigtable.MutateRows" `  




#### `PingAndWarm`

  * **Method** : `google.bigtable.v2.Bigtable.PingAndWarm`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `bigtable.instances.ping - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.bigtable.v2.Bigtable.PingAndWarm" `  




#### `PrepareQuery`

  * **Method** : `google.bigtable.v2.Bigtable.PrepareQuery`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `bigtable.instances.executeQuery - DATA_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.bigtable.v2.Bigtable.PrepareQuery" `  




#### `ReadChangeStream`

  * **Method** : `google.bigtable.v2.Bigtable.ReadChangeStream`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `bigtable.tables.readRows - DATA_READ`
  * **Method is a long-running or streaming operation** : [**Streaming RPC**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#streaming)   

  * **Filter for this method** : ` protoPayload.methodName="google.bigtable.v2.Bigtable.ReadChangeStream" `  




#### `ReadModifyWriteRow`

  * **Method** : `google.bigtable.v2.Bigtable.ReadModifyWriteRow`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `bigtable.tables.mutateRows - DATA_WRITE`
    * `bigtable.tables.readRows - DATA_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.bigtable.v2.Bigtable.ReadModifyWriteRow" `  




#### `ReadRows`

  * **Method** : `google.bigtable.v2.Bigtable.ReadRows`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `bigtable.tables.readRows - DATA_READ`
  * **Method is a long-running or streaming operation** : [**Streaming RPC**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#streaming)   

  * **Filter for this method** : ` protoPayload.methodName="google.bigtable.v2.Bigtable.ReadRows" `  




#### `SampleRowKeys`

  * **Method** : `google.bigtable.v2.Bigtable.SampleRowKeys`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `bigtable.tables.sampleRowKeys - DATA_READ`
  * **Method is a long-running or streaming operation** : [**Streaming RPC**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#streaming)   

  * **Filter for this method** : ` protoPayload.methodName="google.bigtable.v2.Bigtable.SampleRowKeys" `  




## Methods that don't produce audit logs

A method might not produce audit logs for one or more of the following reasons: 

  * It is a high volume method involving significant log generation and storage costs.
  * It has low auditing value.
  * Another audit or platform log already provides method coverage.



The following methods don't produce audit logs:

  * `grpc.lookup.v1.RouteLookupService.RouteLookup`



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
