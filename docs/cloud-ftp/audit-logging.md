---
url: https://docs.cloud.google.com/cloud-ftp/audit-logging/
title: Cloud FTP audit logging \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:03:01.399927+00:00
---

# Cloud FTP audit logging  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/cloud-ftp/audit-logging/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Storage ](https://docs.cloud.google.com/docs/storage)
  * [ Cloud FTP ](https://docs.cloud.google.com/cloud-ftp)
  * [ Guides ](https://docs.cloud.google.com/cloud-ftp/overview)



Send feedback 

#  Cloud FTP audit logging Stay organized with collections  Save and categorize content based on your preferences. 

This document lists the audited methods for Cloud FTP. Google Cloud services generate audit logs that record administrative and access activities within your Google Cloud resources. For more information about Cloud Audit Logs, see the following: 

  * [Types of audit logs](https://docs.cloud.google.com/logging/docs/audit#types)
  * [Audit log entry structure](https://docs.cloud.google.com/logging/docs/audit#audit_log_entry_structure)
  * [Storing and routing audit logs](https://docs.cloud.google.com/logging/docs/audit#storing_and_routing_audit_logs)
  * [Cloud Logging pricing summary](https://docs.cloud.google.com/stackdriver/pricing#logs-pricing-summary)
  * [Enable Data Access audit logs](https://docs.cloud.google.com/logging/docs/audit/configure-data-access)



## Service name

To view the Cloud FTP audit logs, do the following:

  1. In the Google Cloud console, go to the Logs Explorer page:

[Go to Logs Explorer](https://console.cloud.google.com/logs/query)

  2. Copy and paste the following query into the **Query** field of the Logs Explorer, and then click **Run query**.
         
         protoPayload.serviceName="ftp.googleapis.com"
           




## Methods by permission type

Each IAM permission has a `type` property, whose value is an enum that can be one of four values: `ADMIN_READ`, `ADMIN_WRITE`, `DATA_READ`, or `DATA_WRITE`. When you call a method, Cloud FTP generates an audit log whose category is dependent on the `type` property of the permission required to perform the method. Methods that require an IAM permission with the `type` property value of `DATA_READ`, `DATA_WRITE`, or `ADMIN_READ` generate [Data Access](https://docs.cloud.google.com/logging/docs/audit#data-access) audit logs. Methods that require an IAM permission with the `type` property value of `ADMIN_WRITE` generate [Admin Activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity) audit logs.

API methods in the following list that are marked with (LRO) are long-running operations (LROs). These methods usually generate two audit log entries: one when the operation starts and another when it ends. For more information see [Audit logs for long-running operations](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro). Permission type | Methods  
---|---  
`ADMIN_READ` | `google.cloud.ftp.v1.CloudFtp.GetServer`  
`google.cloud.ftp.v1.CloudFtp.GetUser`  
`google.cloud.ftp.v1.CloudFtp.ListServers`  
`google.cloud.ftp.v1.CloudFtp.ListUsers`  
`google.cloud.ftp.v1alpha.CloudFtp.GetServer`  
`google.cloud.ftp.v1alpha.CloudFtp.GetUser`  
`google.cloud.ftp.v1alpha.CloudFtp.ListServers`  
`google.cloud.ftp.v1alpha.CloudFtp.ListUsers`  
`ADMIN_WRITE` | `google.cloud.ftp.v1.CloudFtp.CreateServer` (LRO)  
`google.cloud.ftp.v1.CloudFtp.CreateUser` (LRO)  
`google.cloud.ftp.v1.CloudFtp.DeleteServer` (LRO)  
`google.cloud.ftp.v1.CloudFtp.DeleteUser` (LRO)  
`google.cloud.ftp.v1.CloudFtp.StartServer` (LRO)  
`google.cloud.ftp.v1.CloudFtp.StopServer` (LRO)  
`google.cloud.ftp.v1.CloudFtp.UpdateServer` (LRO)  
`google.cloud.ftp.v1.CloudFtp.UpdateUser` (LRO)  
`google.cloud.ftp.v1alpha.CloudFtp.CreateServer` (LRO)  
`google.cloud.ftp.v1alpha.CloudFtp.CreateUser` (LRO)  
`google.cloud.ftp.v1alpha.CloudFtp.DeleteServer` (LRO)  
`google.cloud.ftp.v1alpha.CloudFtp.DeleteUser` (LRO)  
`google.cloud.ftp.v1alpha.CloudFtp.StartServer` (LRO)  
`google.cloud.ftp.v1alpha.CloudFtp.StopServer` (LRO)  
`google.cloud.ftp.v1alpha.CloudFtp.UpdateServer` (LRO)  
`google.cloud.ftp.v1alpha.CloudFtp.UpdateUser` (LRO)  
  
## API interface audit logs

For information about how and which permissions are evaluated for each method, see the Identity and Access Management documentation for Cloud FTP.

### `google.cloud.ftp.v1.CloudFtp`

The following audit logs are associated with methods belonging to `google.cloud.ftp.v1.CloudFtp`.

#### `CreateServer`

  * **Method** : `google.cloud.ftp.v1.CloudFtp.CreateServer`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `ftp.servers.create - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.ftp.v1.CloudFtp.CreateServer" `  




#### `CreateUser`

  * **Method** : `google.cloud.ftp.v1.CloudFtp.CreateUser`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `ftp.users.create - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.ftp.v1.CloudFtp.CreateUser" `  




#### `DeleteServer`

  * **Method** : `google.cloud.ftp.v1.CloudFtp.DeleteServer`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `ftp.servers.delete - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.ftp.v1.CloudFtp.DeleteServer" `  




#### `DeleteUser`

  * **Method** : `google.cloud.ftp.v1.CloudFtp.DeleteUser`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `ftp.users.delete - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.ftp.v1.CloudFtp.DeleteUser" `  




#### `GetServer`

  * **Method** : `google.cloud.ftp.v1.CloudFtp.GetServer`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `ftp.servers.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.ftp.v1.CloudFtp.GetServer" `  




#### `GetUser`

  * **Method** : `google.cloud.ftp.v1.CloudFtp.GetUser`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `ftp.users.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.ftp.v1.CloudFtp.GetUser" `  




#### `ListServers`

  * **Method** : `google.cloud.ftp.v1.CloudFtp.ListServers`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `ftp.servers.list - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.ftp.v1.CloudFtp.ListServers" `  




#### `ListUsers`

  * **Method** : `google.cloud.ftp.v1.CloudFtp.ListUsers`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `ftp.users.list - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.ftp.v1.CloudFtp.ListUsers" `  




#### `StartServer`

  * **Method** : `google.cloud.ftp.v1.CloudFtp.StartServer`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `ftp.servers.start - ADMIN_WRITE`
    * `ftp.servers.update - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.ftp.v1.CloudFtp.StartServer" `  




#### `StopServer`

  * **Method** : `google.cloud.ftp.v1.CloudFtp.StopServer`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `ftp.servers.stop - ADMIN_WRITE`
    * `ftp.servers.update - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.ftp.v1.CloudFtp.StopServer" `  




#### `UpdateServer`

  * **Method** : `google.cloud.ftp.v1.CloudFtp.UpdateServer`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `ftp.servers.update - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.ftp.v1.CloudFtp.UpdateServer" `  




#### `UpdateUser`

  * **Method** : `google.cloud.ftp.v1.CloudFtp.UpdateUser`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `ftp.users.update - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.ftp.v1.CloudFtp.UpdateUser" `  




### `google.cloud.ftp.v1alpha.CloudFtp`

The following audit logs are associated with methods belonging to `google.cloud.ftp.v1alpha.CloudFtp`.

#### `CreateServer`

  * **Method** : `google.cloud.ftp.v1alpha.CloudFtp.CreateServer`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `ftp.servers.create - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.ftp.v1alpha.CloudFtp.CreateServer" `  




#### `CreateUser`

  * **Method** : `google.cloud.ftp.v1alpha.CloudFtp.CreateUser`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `ftp.users.create - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.ftp.v1alpha.CloudFtp.CreateUser" `  




#### `DeleteServer`

  * **Method** : `google.cloud.ftp.v1alpha.CloudFtp.DeleteServer`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `ftp.servers.delete - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.ftp.v1alpha.CloudFtp.DeleteServer" `  




#### `DeleteUser`

  * **Method** : `google.cloud.ftp.v1alpha.CloudFtp.DeleteUser`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `ftp.users.delete - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.ftp.v1alpha.CloudFtp.DeleteUser" `  




#### `GetServer`

  * **Method** : `google.cloud.ftp.v1alpha.CloudFtp.GetServer`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `ftp.servers.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.ftp.v1alpha.CloudFtp.GetServer" `  




#### `GetUser`

  * **Method** : `google.cloud.ftp.v1alpha.CloudFtp.GetUser`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `ftp.users.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.ftp.v1alpha.CloudFtp.GetUser" `  




#### `ListServers`

  * **Method** : `google.cloud.ftp.v1alpha.CloudFtp.ListServers`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `ftp.servers.list - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.ftp.v1alpha.CloudFtp.ListServers" `  




#### `ListUsers`

  * **Method** : `google.cloud.ftp.v1alpha.CloudFtp.ListUsers`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `ftp.users.list - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.ftp.v1alpha.CloudFtp.ListUsers" `  




#### `StartServer`

  * **Method** : `google.cloud.ftp.v1alpha.CloudFtp.StartServer`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `ftp.servers.start - ADMIN_WRITE`
    * `ftp.servers.update - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.ftp.v1alpha.CloudFtp.StartServer" `  




#### `StopServer`

  * **Method** : `google.cloud.ftp.v1alpha.CloudFtp.StopServer`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `ftp.servers.stop - ADMIN_WRITE`
    * `ftp.servers.update - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.ftp.v1alpha.CloudFtp.StopServer" `  




#### `UpdateServer`

  * **Method** : `google.cloud.ftp.v1alpha.CloudFtp.UpdateServer`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `ftp.servers.update - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.ftp.v1alpha.CloudFtp.UpdateServer" `  




#### `UpdateUser`

  * **Method** : `google.cloud.ftp.v1alpha.CloudFtp.UpdateUser`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `ftp.users.update - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.ftp.v1alpha.CloudFtp.UpdateUser" `  




## Methods that don't produce audit logs

A method might not produce audit logs for one or more of the following reasons: 

  * It is a high volume method involving significant log generation and storage costs.
  * It has low auditing value.
  * Another audit or platform log already provides method coverage.



The following methods don't produce audit logs:

  * `google.cloud.location.Locations.GetLocation`
  * `google.cloud.location.Locations.ListLocations`



## Audit logs for SFTP file transfers

To generate logs for SFTP file transfers, use [Cloud Audit Logs with Cloud Storage](https://docs.cloud.google.com/storage/docs/audit-logging). These logs capture the underlying Cloud Storage API operations that are performed during file transfers, such as creating Cloud Storage objects.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
