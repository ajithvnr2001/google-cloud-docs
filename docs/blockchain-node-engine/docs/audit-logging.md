---
url: https://docs.cloud.google.com/blockchain-node-engine/docs/audit-logging/
title: Blockchain Node Engine audit logging \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:09:20.387421+00:00
---

# Blockchain Node Engine audit logging  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/blockchain-node-engine/docs/audit-logging/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ Blockchain Node Engine ](https://docs.cloud.google.com/blockchain-node-engine/docs)
  * [ Guides ](https://docs.cloud.google.com/blockchain-node-engine/docs/overview)



Send feedback 

#  Blockchain Node Engine audit logging Stay organized with collections  Save and categorize content based on your preferences. 

This document lists the audited methods for Blockchain Node Engine. Google Cloud services generate audit logs that record administrative and access activities within your Google Cloud resources. For more information about Cloud Audit Logs, see the following: 

  * [Types of audit logs](https://docs.cloud.google.com/logging/docs/audit#types)
  * [Audit log entry structure](https://docs.cloud.google.com/logging/docs/audit#audit_log_entry_structure)
  * [Storing and routing audit logs](https://docs.cloud.google.com/logging/docs/audit#storing_and_routing_audit_logs)
  * [Cloud Logging pricing summary](https://docs.cloud.google.com/stackdriver/pricing#logs-pricing-summary)
  * [Enable Data Access audit logs](https://docs.cloud.google.com/logging/docs/audit/configure-data-access)



## Service name

To view the Blockchain Node Engine audit logs, do the following:

  1. In the Google Cloud console, go to the Logs Explorer page:

[Go to Logs Explorer](https://console.cloud.google.com/logs/query)

  2. Copy and paste the following query into the **Query** field of the Logs Explorer, and then click **Run query**.
         
         protoPayload.serviceName="blockchainnodeengine.googleapis.com"
           




## Methods by permission type

Each IAM permission has a `type` property, whose value is an enum that can be one of four values: `ADMIN_READ`, `ADMIN_WRITE`, `DATA_READ`, or `DATA_WRITE`. When you call a method, Blockchain Node Engine generates an audit log whose category is dependent on the `type` property of the permission required to perform the method. Methods that require an IAM permission with the `type` property value of `DATA_READ`, `DATA_WRITE`, or `ADMIN_READ` generate [Data Access](https://docs.cloud.google.com/logging/docs/audit#data-access) audit logs. Methods that require an IAM permission with the `type` property value of `ADMIN_WRITE` generate [Admin Activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity) audit logs.

API methods in the following list that are marked with (LRO) are long-running operations (LROs). These methods usually generate two audit log entries: one when the operation starts and another when it ends. For more information see [Audit logs for long-running operations](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro). Permission type | Methods  
---|---  
`ADMIN_READ` | `google.cloud.blockchainnodeengine.v1.BlockchainNodeEngine.GetBlockchainNode`  
`google.cloud.blockchainnodeengine.v1.BlockchainNodeEngine.ListBlockchainNodes`  
`google.cloud.blockchainnodeengine.v1alpha1.BlockchainNodeEngine.GetBlockchainNode`  
`google.cloud.blockchainnodeengine.v1alpha1.BlockchainNodeEngine.ListBlockchainNodes`  
`google.longrunning.Operations.GetOperation`  
`google.longrunning.Operations.ListOperations`  
`ADMIN_WRITE` | `google.cloud.blockchainnodeengine.v1.BlockchainNodeEngine.CreateBlockchainNode` (LRO)  
`google.cloud.blockchainnodeengine.v1.BlockchainNodeEngine.DeleteBlockchainNode` (LRO)  
`google.cloud.blockchainnodeengine.v1.BlockchainNodeEngine.UpdateBlockchainNode`  
`google.cloud.blockchainnodeengine.v1alpha1.BlockchainNodeEngine.CreateBlockchainNode` (LRO)  
`google.cloud.blockchainnodeengine.v1alpha1.BlockchainNodeEngine.DeleteBlockchainNode` (LRO)  
`google.cloud.blockchainnodeengine.v1alpha1.BlockchainNodeEngine.UpdateBlockchainNode`  
`google.longrunning.Operations.CancelOperation`  
`google.longrunning.Operations.DeleteOperation`  
  
## API interface audit logs

For information about how and which permissions are evaluated for each method, see the Identity and Access Management documentation for Blockchain Node Engine.

### `google.cloud.blockchainnodeengine.v1.BlockchainNodeEngine`

The following audit logs are associated with methods belonging to `google.cloud.blockchainnodeengine.v1.BlockchainNodeEngine`.

#### `CreateBlockchainNode`

  * **Method** : `google.cloud.blockchainnodeengine.v1.BlockchainNodeEngine.CreateBlockchainNode`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `blockchainnodeengine.blockchainNodes.create - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.blockchainnodeengine.v1.BlockchainNodeEngine.CreateBlockchainNode" `  




#### `DeleteBlockchainNode`

  * **Method** : `google.cloud.blockchainnodeengine.v1.BlockchainNodeEngine.DeleteBlockchainNode`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `blockchainnodeengine.blockchainNodes.delete - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.blockchainnodeengine.v1.BlockchainNodeEngine.DeleteBlockchainNode" `  




#### `GetBlockchainNode`

  * **Method** : `google.cloud.blockchainnodeengine.v1.BlockchainNodeEngine.GetBlockchainNode`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `blockchainnodeengine.blockchainNodes.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.blockchainnodeengine.v1.BlockchainNodeEngine.GetBlockchainNode" `  




#### `ListBlockchainNodes`

  * **Method** : `google.cloud.blockchainnodeengine.v1.BlockchainNodeEngine.ListBlockchainNodes`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `blockchainnodeengine.blockchainNodes.list - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.blockchainnodeengine.v1.BlockchainNodeEngine.ListBlockchainNodes" `  




#### `UpdateBlockchainNode`

  * **Method** : `google.cloud.blockchainnodeengine.v1.BlockchainNodeEngine.UpdateBlockchainNode`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `blockchainnodeengine.blockchainNodes.update - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.blockchainnodeengine.v1.BlockchainNodeEngine.UpdateBlockchainNode" `  




### `google.cloud.blockchainnodeengine.v1alpha1.BlockchainNodeEngine`

The following audit logs are associated with methods belonging to `google.cloud.blockchainnodeengine.v1alpha1.BlockchainNodeEngine`.

#### `CreateBlockchainNode`

  * **Method** : `google.cloud.blockchainnodeengine.v1alpha1.BlockchainNodeEngine.CreateBlockchainNode`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `blockchainnodeengine.blockchainNodes.create - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.blockchainnodeengine.v1alpha1.BlockchainNodeEngine.CreateBlockchainNode" `  




#### `DeleteBlockchainNode`

  * **Method** : `google.cloud.blockchainnodeengine.v1alpha1.BlockchainNodeEngine.DeleteBlockchainNode`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `blockchainnodeengine.blockchainNodes.delete - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.blockchainnodeengine.v1alpha1.BlockchainNodeEngine.DeleteBlockchainNode" `  




#### `GetBlockchainNode`

  * **Method** : `google.cloud.blockchainnodeengine.v1alpha1.BlockchainNodeEngine.GetBlockchainNode`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `blockchainnodeengine.blockchainNodes.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.blockchainnodeengine.v1alpha1.BlockchainNodeEngine.GetBlockchainNode" `  




#### `ListBlockchainNodes`

  * **Method** : `google.cloud.blockchainnodeengine.v1alpha1.BlockchainNodeEngine.ListBlockchainNodes`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `blockchainnodeengine.blockchainNodes.list - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.blockchainnodeengine.v1alpha1.BlockchainNodeEngine.ListBlockchainNodes" `  




#### `UpdateBlockchainNode`

  * **Method** : `google.cloud.blockchainnodeengine.v1alpha1.BlockchainNodeEngine.UpdateBlockchainNode`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `blockchainnodeengine.blockchainNodes.update - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.blockchainnodeengine.v1alpha1.BlockchainNodeEngine.UpdateBlockchainNode" `  




### `google.longrunning.Operations`

The following audit logs are associated with methods belonging to `google.longrunning.Operations`.

#### `CancelOperation`

  * **Method** : `google.longrunning.Operations.CancelOperation`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `blockchainnodeengine.operations.cancel - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.longrunning.Operations.CancelOperation" `  




#### `DeleteOperation`

  * **Method** : `google.longrunning.Operations.DeleteOperation`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `blockchainnodeengine.operations.delete - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.longrunning.Operations.DeleteOperation" `  




#### `GetOperation`

  * **Method** : `google.longrunning.Operations.GetOperation`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `blockchainnodeengine.operations.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.longrunning.Operations.GetOperation" `  




#### `ListOperations`

  * **Method** : `google.longrunning.Operations.ListOperations`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `blockchainnodeengine.operations.list - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.longrunning.Operations.ListOperations" `  




## Methods that don't produce audit logs

A method might not produce audit logs for one or more of the following reasons: 

  * It is a high volume method involving significant log generation and storage costs.
  * It has low auditing value.
  * Another audit or platform log already provides method coverage.



The following methods don't produce audit logs:

  * `google.cloud.location.Locations.GetLocation`
  * `google.cloud.location.Locations.ListLocations`
  * `google.longrunning.Operations.WaitOperation`



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
