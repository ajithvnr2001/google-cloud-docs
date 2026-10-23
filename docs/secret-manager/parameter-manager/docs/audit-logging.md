---
url: https://docs.cloud.google.com/secret-manager/parameter-manager/docs/audit-logging/
title: Parameter Manager audit logging \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T09:57:43.606930+00:00
---

# Parameter Manager audit logging  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/secret-manager/parameter-manager/docs/audit-logging/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Secret Manager ](https://docs.cloud.google.com/secret-manager/docs)
  * [ Parameter Manager ](https://docs.cloud.google.com/secret-manager/parameter-manager/docs/overview)



Send feedback 

#  Parameter Manager audit logging Stay organized with collections  Save and categorize content based on your preferences. 

This document describes audit logging for Parameter Manager. Google Cloud services generate audit logs that record administrative and access activities within your Google Cloud resources. For more information about Cloud Audit Logs, see the following: 

  * [Types of audit logs](https://docs.cloud.google.com/logging/docs/audit#types)
  * [Audit log entry structure](https://docs.cloud.google.com/logging/docs/audit#audit_log_entry_structure)
  * [Storing and routing audit logs](https://docs.cloud.google.com/logging/docs/audit#storing_and_routing_audit_logs)
  * [Cloud Logging pricing summary](https://docs.cloud.google.com/stackdriver/pricing#logs-pricing-summary)
  * [Enable Data Access audit logs](https://docs.cloud.google.com/logging/docs/audit/configure-data-access)



## Service name

Parameter Manager audit logs use the service name `parametermanager.googleapis.com`. Filter for this service: 
    
    
        protoPayload.serviceName="parametermanager.googleapis.com"
      

## Methods by permission type

Each IAM permission has a `type` property, whose value is an enum that can be one of four values: `ADMIN_READ`, `ADMIN_WRITE`, `DATA_READ`, or `DATA_WRITE`. When you call a method, Parameter Manager generates an audit log whose category is dependent on the `type` property of the permission required to perform the method. Methods that require an IAM permission with the `type` property value of `DATA_READ`, `DATA_WRITE`, or `ADMIN_READ` generate [Data Access](https://docs.cloud.google.com/logging/docs/audit#data-access) audit logs. Methods that require an IAM permission with the `type` property value of `ADMIN_WRITE` generate [Admin Activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity) audit logs.

API methods in the following list that are marked with (LRO) are long-running operations (LROs). These methods usually generate two audit log entries: one when the operation starts and another when it ends. For more information see [Audit logs for long-running operations](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro). Permission type | Methods  
---|---  
`ADMIN_READ` | `google.cloud.parametermanager.v1.ParameterManager.GetParameter`  
`google.cloud.parametermanager.v1.ParameterManager.ListParameters`  
`ADMIN_WRITE` | `google.cloud.parametermanager.v1.ParameterManager.CreateParameter`  
`google.cloud.parametermanager.v1.ParameterManager.CreateParameterVersion`  
`google.cloud.parametermanager.v1.ParameterManager.DeleteParameter`  
`google.cloud.parametermanager.v1.ParameterManager.DeleteParameterVersion`  
`google.cloud.parametermanager.v1.ParameterManager.UpdateParameter`  
`google.cloud.parametermanager.v1.ParameterManager.UpdateParameterVersion`  
`DATA_READ` | `google.cloud.parametermanager.v1.ParameterManager.GetParameterVersion`  
`google.cloud.parametermanager.v1.ParameterManager.ListParameterVersions`  
`google.cloud.parametermanager.v1.ParameterManager.RenderParameterVersion`  
  
## API interface audit logs

For information about how and which permissions are evaluated for each method, see the Identity and Access Management documentation for Parameter Manager.

### `google.cloud.parametermanager.v1.ParameterManager`

The following audit logs are associated with methods belonging to `google.cloud.parametermanager.v1.ParameterManager`.

#### `CreateParameter`

  * **Method** : `google.cloud.parametermanager.v1.ParameterManager.CreateParameter`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `parametermanager.parameters.create - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.parametermanager.v1.ParameterManager.CreateParameter" `  




#### `CreateParameterVersion`

  * **Method** : `google.cloud.parametermanager.v1.ParameterManager.CreateParameterVersion`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `parametermanager.parameterVersions.create - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.parametermanager.v1.ParameterManager.CreateParameterVersion" `  




#### `DeleteParameter`

  * **Method** : `google.cloud.parametermanager.v1.ParameterManager.DeleteParameter`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `parametermanager.parameters.delete - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.parametermanager.v1.ParameterManager.DeleteParameter" `  




#### `DeleteParameterVersion`

  * **Method** : `google.cloud.parametermanager.v1.ParameterManager.DeleteParameterVersion`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `parametermanager.parameterVersions.delete - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.parametermanager.v1.ParameterManager.DeleteParameterVersion" `  




#### `GetParameter`

  * **Method** : `google.cloud.parametermanager.v1.ParameterManager.GetParameter`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `parametermanager.parameters.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.parametermanager.v1.ParameterManager.GetParameter" `  




#### `GetParameterVersion`

  * **Method** : `google.cloud.parametermanager.v1.ParameterManager.GetParameterVersion`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `parametermanager.parameterVersions.get - DATA_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.parametermanager.v1.ParameterManager.GetParameterVersion" `  




#### `ListParameterVersions`

  * **Method** : `google.cloud.parametermanager.v1.ParameterManager.ListParameterVersions`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `parametermanager.parameterVersions.list - DATA_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.parametermanager.v1.ParameterManager.ListParameterVersions" `  




#### `ListParameters`

  * **Method** : `google.cloud.parametermanager.v1.ParameterManager.ListParameters`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `parametermanager.parameters.list - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.parametermanager.v1.ParameterManager.ListParameters" `  




#### `RenderParameterVersion`

  * **Method** : `google.cloud.parametermanager.v1.ParameterManager.RenderParameterVersion`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `parametermanager.parameterVersions.render - DATA_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.parametermanager.v1.ParameterManager.RenderParameterVersion" `  




#### `UpdateParameter`

  * **Method** : `google.cloud.parametermanager.v1.ParameterManager.UpdateParameter`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `parametermanager.parameters.update - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.parametermanager.v1.ParameterManager.UpdateParameter" `  




#### `UpdateParameterVersion`

  * **Method** : `google.cloud.parametermanager.v1.ParameterManager.UpdateParameterVersion`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `parametermanager.parameterVersions.update - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.parametermanager.v1.ParameterManager.UpdateParameterVersion" `  




## Methods that don't produce audit logs

A method might not produce audit logs for one or more of the following reasons: 

  * It is a high volume method involving significant log generation and storage costs.
  * It has low auditing value.
  * Another audit or platform log already provides method coverage.



The following methods don't produce audit logs:

  * `google.cloud.location.Locations.GetLocation`
  * `google.cloud.location.Locations.ListLocations`



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
