---
url: https://docs.cloud.google.com/deployment-manager/docs/audit-logging/
title: Cloud Deployment Manager audit logging \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T00:21:06.053782+00:00
---

# Cloud Deployment Manager audit logging  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/deployment-manager/docs/audit-logging/

Cloud Deployment Manager reached end of support on **March 31, 2026**.   
If you currently use Deployment Manager, please migrate to Infrastructure Manager or an alternative deployment technology.  
  
For more information on the deprecation and shutdown, see [Deployment Manager deprecation](https://docs.cloud.google.com/deployment-manager/docs/deprecations). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Infrastructure as code ](https://docs.cloud.google.com/docs/iac)
  * [ Cloud Deployment Manager ](https://docs.cloud.google.com/deployment-manager/docs)
  * [ Guides ](https://docs.cloud.google.com/deployment-manager/docs/manage-cloud-resources-deployment)



Send feedback 

#  Cloud Deployment Manager audit logging Stay organized with collections  Save and categorize content based on your preferences. 

This document describes audit logging for Cloud Deployment Manager. Google Cloud services generate audit logs that record administrative and access activities within your Google Cloud resources. For more information about Cloud Audit Logs, see the following: 

  * [Types of audit logs](https://docs.cloud.google.com/logging/docs/audit#types)
  * [Audit log entry structure](https://docs.cloud.google.com/logging/docs/audit#audit_log_entry_structure)
  * [Storing and routing audit logs](https://docs.cloud.google.com/logging/docs/audit#storing_and_routing_audit_logs)
  * [Cloud Logging pricing summary](https://docs.cloud.google.com/stackdriver/pricing#logs-pricing-summary)
  * [Enable Data Access audit logs](https://docs.cloud.google.com/logging/docs/audit/configure-data-access)



## Service name

Cloud Deployment Manager audit logs use the service name `deploymentmanager.googleapis.com`. Filter for this service: 
    
    
        protoPayload.serviceName="deploymentmanager.googleapis.com"
      

## Methods by permission type

Each IAM permission has a `type` property, whose value is an enum that can be one of four values: `ADMIN_READ`, `ADMIN_WRITE`, `DATA_READ`, or `DATA_WRITE`. When you call a method, Cloud Deployment Manager generates an audit log whose category is dependent on the `type` property of the permission required to perform the method. Methods that require an IAM permission with the `type` property value of `DATA_READ`, `DATA_WRITE`, or `ADMIN_READ` generate [Data Access](https://docs.cloud.google.com/logging/docs/audit#data-access) audit logs. Methods that require an IAM permission with the `type` property value of `ADMIN_WRITE` generate [Admin Activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity) audit logs.

API methods in the following list that are marked with (LRO) are long-running operations (LROs). These methods usually generate two audit log entries: one when the operation starts and another when it ends. For more information see [Audit logs for long-running operations](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro). Permission type | Methods  
---|---  
`ADMIN_READ` | `v2.deploymentmanager.deployments.get`  
`v2.deploymentmanager.deployments.getIamPolicy`  
`v2.deploymentmanager.deployments.list`  
`v2.deploymentmanager.manifests.get`  
`v2.deploymentmanager.manifests.list`  
`v2.deploymentmanager.operations.get`  
`v2.deploymentmanager.operations.list`  
`v2.deploymentmanager.resources.get`  
`v2.deploymentmanager.resources.list`  
`v2.deploymentmanager.types.list`  
`v2beta.deploymentmanager.deployments.get`  
`v2beta.deploymentmanager.deployments.list`  
`v2beta.deploymentmanager.manifests.get`  
`v2beta.deploymentmanager.manifests.list`  
`v2beta.deploymentmanager.operations.get`  
`v2beta.deploymentmanager.resources.list`  
`ADMIN_WRITE` | `alpha.deploymentmanager.deployments.insert` (LRO)  
`v2.deploymentmanager.deployments.cancelPreview` (LRO)  
`v2.deploymentmanager.deployments.delete` (LRO)  
`v2.deploymentmanager.deployments.insert` (LRO)  
`v2.deploymentmanager.deployments.patch` (LRO)  
`v2.deploymentmanager.deployments.setIamPolicy`  
`v2.deploymentmanager.deployments.stop` (LRO)  
`v2.deploymentmanager.deployments.update` (LRO)  
`v2beta.deploymentmanager.deployments.cancelPreview` (LRO)  
`v2beta.deploymentmanager.deployments.delete` (LRO)  
`v2beta.deploymentmanager.deployments.insert` (LRO)  
`v2beta.deploymentmanager.deployments.patch` (LRO)  
`v2beta.deploymentmanager.deployments.stop` (LRO)  
`v2beta.deploymentmanager.deployments.update` (LRO)  
  
## API interface audit logs

For information about how and which permissions are evaluated for each method, see the Identity and Access Management documentation for Cloud Deployment Manager.

### `alpha.deploymentmanager.deployments`

The following audit logs are associated with methods belonging to `alpha.deploymentmanager.deployments`.

#### `insert`

  * **Method** : `alpha.deploymentmanager.deployments.insert`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `deploymentmanager.deployments.create - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="alpha.deploymentmanager.deployments.insert" `  




### `v2.deploymentmanager.deployments`

The following audit logs are associated with methods belonging to `v2.deploymentmanager.deployments`.

#### `cancelPreview`

  * **Method** : `v2.deploymentmanager.deployments.cancelPreview`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `deploymentmanager.deployments.cancelPreview - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="v2.deploymentmanager.deployments.cancelPreview" `  




#### `delete`

  * **Method** : `v2.deploymentmanager.deployments.delete`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `deploymentmanager.deployments.delete - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="v2.deploymentmanager.deployments.delete" `  




#### `get`

  * **Method** : `v2.deploymentmanager.deployments.get`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `deploymentmanager.deployments.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="v2.deploymentmanager.deployments.get" `  




#### `getIamPolicy`

  * **Method** : `v2.deploymentmanager.deployments.getIamPolicy`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `deploymentmanager.deployments.getIamPolicy - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="v2.deploymentmanager.deployments.getIamPolicy" `  




#### `insert`

  * **Method** : `v2.deploymentmanager.deployments.insert`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `deploymentmanager.deployments.create - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="v2.deploymentmanager.deployments.insert" `  




#### `list`

  * **Method** : `v2.deploymentmanager.deployments.list`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `deploymentmanager.deployments.list - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="v2.deploymentmanager.deployments.list" `  




#### `patch`

  * **Method** : `v2.deploymentmanager.deployments.patch`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `deploymentmanager.deployments.update - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="v2.deploymentmanager.deployments.patch" `  




#### `setIamPolicy`

  * **Method** : `v2.deploymentmanager.deployments.setIamPolicy`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `deploymentmanager.deployments.setIamPolicy - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="v2.deploymentmanager.deployments.setIamPolicy" `  




#### `stop`

  * **Method** : `v2.deploymentmanager.deployments.stop`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `deploymentmanager.deployments.stop - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="v2.deploymentmanager.deployments.stop" `  




#### `update`

  * **Method** : `v2.deploymentmanager.deployments.update`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `deploymentmanager.deployments.update - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="v2.deploymentmanager.deployments.update" `  




### `v2.deploymentmanager.manifests`

The following audit logs are associated with methods belonging to `v2.deploymentmanager.manifests`.

#### `get`

  * **Method** : `v2.deploymentmanager.manifests.get`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `deploymentmanager.manifests.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="v2.deploymentmanager.manifests.get" `  




#### `list`

  * **Method** : `v2.deploymentmanager.manifests.list`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `deploymentmanager.manifests.list - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="v2.deploymentmanager.manifests.list" `  




### `v2.deploymentmanager.operations`

The following audit logs are associated with methods belonging to `v2.deploymentmanager.operations`.

#### `get`

  * **Method** : `v2.deploymentmanager.operations.get`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `deploymentmanager.operations.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="v2.deploymentmanager.operations.get" `  




#### `list`

  * **Method** : `v2.deploymentmanager.operations.list`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `deploymentmanager.operations.list - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="v2.deploymentmanager.operations.list" `  




### `v2.deploymentmanager.resources`

The following audit logs are associated with methods belonging to `v2.deploymentmanager.resources`.

#### `get`

  * **Method** : `v2.deploymentmanager.resources.get`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `deploymentmanager.resources.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="v2.deploymentmanager.resources.get" `  




#### `list`

  * **Method** : `v2.deploymentmanager.resources.list`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `deploymentmanager.resources.list - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="v2.deploymentmanager.resources.list" `  




### `v2.deploymentmanager.types`

The following audit logs are associated with methods belonging to `v2.deploymentmanager.types`.

#### `list`

  * **Method** : `v2.deploymentmanager.types.list`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `deploymentmanager.types.list - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="v2.deploymentmanager.types.list" `  




### `v2beta.deploymentmanager.deployments`

The following audit logs are associated with methods belonging to `v2beta.deploymentmanager.deployments`.

#### `cancelPreview`

  * **Method** : `v2beta.deploymentmanager.deployments.cancelPreview`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `deploymentmanager.deployments.cancelPreview - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="v2beta.deploymentmanager.deployments.cancelPreview" `  




#### `delete`

  * **Method** : `v2beta.deploymentmanager.deployments.delete`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `deploymentmanager.deployments.delete - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="v2beta.deploymentmanager.deployments.delete" `  




#### `get`

  * **Method** : `v2beta.deploymentmanager.deployments.get`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `deploymentmanager.deployments.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="v2beta.deploymentmanager.deployments.get" `  




#### `insert`

  * **Method** : `v2beta.deploymentmanager.deployments.insert`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `deploymentmanager.deployments.create - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="v2beta.deploymentmanager.deployments.insert" `  




#### `list`

  * **Method** : `v2beta.deploymentmanager.deployments.list`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `deploymentmanager.deployments.list - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="v2beta.deploymentmanager.deployments.list" `  




#### `patch`

  * **Method** : `v2beta.deploymentmanager.deployments.patch`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `deploymentmanager.deployments.get - ADMIN_READ`
    * `deploymentmanager.deployments.update - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="v2beta.deploymentmanager.deployments.patch" `  




#### `stop`

  * **Method** : `v2beta.deploymentmanager.deployments.stop`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `deploymentmanager.deployments.stop - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="v2beta.deploymentmanager.deployments.stop" `  




#### `update`

  * **Method** : `v2beta.deploymentmanager.deployments.update`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `deploymentmanager.deployments.update - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="v2beta.deploymentmanager.deployments.update" `  




### `v2beta.deploymentmanager.manifests`

The following audit logs are associated with methods belonging to `v2beta.deploymentmanager.manifests`.

#### `get`

  * **Method** : `v2beta.deploymentmanager.manifests.get`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `deploymentmanager.manifests.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="v2beta.deploymentmanager.manifests.get" `  




#### `list`

  * **Method** : `v2beta.deploymentmanager.manifests.list`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `deploymentmanager.manifests.list - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="v2beta.deploymentmanager.manifests.list" `  




### `v2beta.deploymentmanager.operations`

The following audit logs are associated with methods belonging to `v2beta.deploymentmanager.operations`.

#### `get`

  * **Method** : `v2beta.deploymentmanager.operations.get`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `deploymentmanager.operations.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="v2beta.deploymentmanager.operations.get" `  




### `v2beta.deploymentmanager.resources`

The following audit logs are associated with methods belonging to `v2beta.deploymentmanager.resources`.

#### `list`

  * **Method** : `v2beta.deploymentmanager.resources.list`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `deploymentmanager.resources.list - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="v2beta.deploymentmanager.resources.list" `  




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
