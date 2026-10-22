---
url: https://docs.cloud.google.com/device-streaming/docs/audit-logging/
title: Device Streaming API audit logging \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T05:40:03.714446+00:00
---

# Device Streaming API audit logging  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/device-streaming/docs/audit-logging/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Device Streaming ](https://docs.cloud.google.com/device-streaming/docs)
  * [ Guides ](https://docs.cloud.google.com/device-streaming/docs/audit-logging)



Send feedback 

#  Device Streaming API audit logging Stay organized with collections  Save and categorize content based on your preferences. 

This document describes audit logging for Device Streaming. Google Cloud services generate audit logs that record administrative and access activities within your Google Cloud resources. For more information about Cloud Audit Logs, see the following: 

  * [Types of audit logs](https://docs.cloud.google.com/logging/docs/audit#types)
  * [Audit log entry structure](https://docs.cloud.google.com/logging/docs/audit#audit_log_entry_structure)
  * [Storing and routing audit logs](https://docs.cloud.google.com/logging/docs/audit#storing_and_routing_audit_logs)
  * [Cloud Logging pricing summary](https://docs.cloud.google.com/stackdriver/pricing#logs-pricing-summary)
  * [Enable Data Access audit logs](https://docs.cloud.google.com/logging/docs/audit/configure-data-access)



## Service name

Device Streaming audit logs use the service name `devicestreaming.googleapis.com`. Filter for this service: 
    
    
        protoPayload.serviceName="devicestreaming.googleapis.com"
      

## Methods by permission type

Each IAM permission has a `type` property, whose value is an enum that can be one of four values: `ADMIN_READ`, `ADMIN_WRITE`, `DATA_READ`, or `DATA_WRITE`. When you call a method, Device Streaming generates an audit log whose category is dependent on the `type` property of the permission required to perform the method. Methods that require an IAM permission with the `type` property value of `DATA_READ`, `DATA_WRITE`, or `ADMIN_READ` generate [Data Access](https://docs.cloud.google.com/logging/docs/audit#data-access) audit logs. Methods that require an IAM permission with the `type` property value of `ADMIN_WRITE` generate [Admin Activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity) audit logs.

Permission type | Methods  
---|---  
`ADMIN_READ` | `google.cloud.devicestreaming.v1.DirectAccessService.GetDeviceSession`  
`google.cloud.devicestreaming.v1.DirectAccessService.ListDeviceSessions`  
`ADMIN_WRITE` | `google.cloud.devicestreaming.v1.DirectAccessService.CancelDeviceSession`  
`google.cloud.devicestreaming.v1.DirectAccessService.CreateDeviceSession`  
`google.cloud.devicestreaming.v1.DirectAccessService.UpdateDeviceSession`  
`DATA_WRITE` | `google.cloud.devicestreaming.v1.DirectAccessService.AdbConnect`  
  
## API interface audit logs

For information about how and which permissions are evaluated for each method, see the Identity and Access Management documentation for Device Streaming.

### `google.cloud.devicestreaming.v1.DirectAccessService`

The following audit logs are associated with methods belonging to `google.cloud.devicestreaming.v1.DirectAccessService`.

#### `AdbConnect`

  * **Method** : `google.cloud.devicestreaming.v1.DirectAccessService.AdbConnect`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `devicestreaming.deviceSessions.use - DATA_WRITE`
  * **Method is a long-running or streaming operation** : [**Streaming RPC**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#streaming)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.devicestreaming.v1.DirectAccessService.AdbConnect" `  




#### `CancelDeviceSession`

  * **Method** : `google.cloud.devicestreaming.v1.DirectAccessService.CancelDeviceSession`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `devicestreaming.deviceSessions.cancel - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.devicestreaming.v1.DirectAccessService.CancelDeviceSession" `  




#### `CreateDeviceSession`

  * **Method** : `google.cloud.devicestreaming.v1.DirectAccessService.CreateDeviceSession`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `devicestreaming.deviceSessions.create - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.devicestreaming.v1.DirectAccessService.CreateDeviceSession" `  




#### `GetDeviceSession`

  * **Method** : `google.cloud.devicestreaming.v1.DirectAccessService.GetDeviceSession`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `devicestreaming.deviceSessions.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.devicestreaming.v1.DirectAccessService.GetDeviceSession" `  




#### `ListDeviceSessions`

  * **Method** : `google.cloud.devicestreaming.v1.DirectAccessService.ListDeviceSessions`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `devicestreaming.deviceSessions.list - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.devicestreaming.v1.DirectAccessService.ListDeviceSessions" `  




#### `UpdateDeviceSession`

  * **Method** : `google.cloud.devicestreaming.v1.DirectAccessService.UpdateDeviceSession`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `devicestreaming.deviceSessions.update - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.devicestreaming.v1.DirectAccessService.UpdateDeviceSession" `  




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
