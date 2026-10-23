---
url: https://docs.cloud.google.com/profiler/docs/audit-logging/
title: Cloud Profiler Audit Logging \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:20:26.715026+00:00
---

# Cloud Profiler Audit Logging  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/profiler/docs/audit-logging/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Observability ](https://docs.cloud.google.com/docs/observability)
  * [ Cloud Profiler ](https://docs.cloud.google.com/profiler/docs)
  * [ Guides ](https://docs.cloud.google.com/profiler/docs/measure-app-performance)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Cloud Profiler Audit Logging

This document describes audit logging for Cloud Profiler. Google Cloud services generate audit logs that record administrative and access activities within your Google Cloud resources. For more information about Cloud Audit Logs, see the following: 

  * [Types of audit logs](https://docs.cloud.google.com/logging/docs/audit#types)
  * [Audit log entry structure](https://docs.cloud.google.com/logging/docs/audit#audit_log_entry_structure)
  * [Storing and routing audit logs](https://docs.cloud.google.com/logging/docs/audit#storing_and_routing_audit_logs)
  * [Cloud Logging pricing summary](https://docs.cloud.google.com/stackdriver/pricing#logs-pricing-summary)
  * [Enable Data Access audit logs](https://docs.cloud.google.com/logging/docs/audit/configure-data-access)



## Service name

Cloud Profiler audit logs use the service name `cloudprofiler.googleapis.com`. Filter for this service: 
    
    
        protoPayload.serviceName="cloudprofiler.googleapis.com"
      

## Methods by permission type

Each IAM permission has a `type` property, whose value is an enum that can be one of four values: `ADMIN_READ`, `ADMIN_WRITE`, `DATA_READ`, or `DATA_WRITE`. When you call a method, Cloud Profiler generates an audit log whose category is dependent on the `type` property of the permission required to perform the method. Methods that require an IAM permission with the `type` property value of `DATA_READ`, `DATA_WRITE`, or `ADMIN_READ` generate [Data Access](https://docs.cloud.google.com/logging/docs/audit#data-access) audit logs. Methods that require an IAM permission with the `type` property value of `ADMIN_WRITE` generate [Admin Activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity) audit logs.

API methods in the following list that are marked with (LRO) are long-running operations (LROs). These methods usually generate two audit log entries: one when the operation starts and another when it ends. For more information see [Audit logs for long-running operations](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro). Permission type | Methods  
---|---  
`DATA_READ` | `google.devtools.cloudprofiler.v2.ExportService.ListProfiles`  
`DATA_WRITE` | `google.devtools.cloudprofiler.v2.ProfilerService.CreateOfflineProfile`  
`google.devtools.cloudprofiler.v2.ProfilerService.CreateProfile`  
`google.devtools.cloudprofiler.v2.ProfilerService.UpdateProfile`  
  
## API interface audit logs

For information about how and which permissions are evaluated for each method, see the Identity and Access Management documentation for Cloud Profiler.

### `google.devtools.cloudprofiler.v2.ExportService`

The following audit logs are associated with methods belonging to `google.devtools.cloudprofiler.v2.ExportService`.

#### `ListProfiles`

  * **Method** : `google.devtools.cloudprofiler.v2.ExportService.ListProfiles`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `cloudprofiler.profiles.list - DATA_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.devtools.cloudprofiler.v2.ExportService.ListProfiles" `  




### `google.devtools.cloudprofiler.v2.ProfilerService`

The following audit logs are associated with methods belonging to `google.devtools.cloudprofiler.v2.ProfilerService`.

#### `CreateOfflineProfile`

  * **Method** : `google.devtools.cloudprofiler.v2.ProfilerService.CreateOfflineProfile`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `cloudprofiler.profiles.create - DATA_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.devtools.cloudprofiler.v2.ProfilerService.CreateOfflineProfile" `  




#### `CreateProfile`

  * **Method** : `google.devtools.cloudprofiler.v2.ProfilerService.CreateProfile`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `cloudprofiler.profiles.create - DATA_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.devtools.cloudprofiler.v2.ProfilerService.CreateProfile" `  




#### `UpdateProfile`

  * **Method** : `google.devtools.cloudprofiler.v2.ProfilerService.UpdateProfile`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `cloudprofiler.profiles.update - DATA_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.devtools.cloudprofiler.v2.ProfilerService.UpdateProfile" `  




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
