---
url: https://docs.cloud.google.com/network-intelligence-center/docs/connectivity-tests/how-to/audit-logging/
title: Connectivity Tests audit logging \u00a0|\u00a0 Network Intelligence Center - Connectivity Tests \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T12:35:34.928139+00:00
---

# Connectivity Tests audit logging  |  Network Intelligence Center - Connectivity Tests  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/network-intelligence-center/docs/connectivity-tests/how-to/audit-logging/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Networking ](https://docs.cloud.google.com/docs/networking)
  * [ Network Intelligence Center ](https://docs.cloud.google.com/network-intelligence-center/docs)
  * [ Connectivity Tests ](https://docs.cloud.google.com/network-intelligence-center/docs/connectivity-tests)
  * [ Guides ](https://docs.cloud.google.com/network-intelligence-center/docs/connectivity-tests/how-to/running-connectivity-tests)



Send feedback 

#  Connectivity Tests audit logging Stay organized with collections  Save and categorize content based on your preferences. 

This document describes audit logging for Connectivity Tests. Google Cloud services generate audit logs that record administrative and access activities within your Google Cloud resources. For more information about Cloud Audit Logs, see the following: 

  * [Types of audit logs](https://docs.cloud.google.com/logging/docs/audit#types)
  * [Audit log entry structure](https://docs.cloud.google.com/logging/docs/audit#audit_log_entry_structure)
  * [Storing and routing audit logs](https://docs.cloud.google.com/logging/docs/audit#storing_and_routing_audit_logs)
  * [Cloud Logging pricing summary](https://docs.cloud.google.com/stackdriver/pricing#logs-pricing-summary)
  * [Enable Data Access audit logs](https://docs.cloud.google.com/logging/docs/audit/configure-data-access)



## Service name

Connectivity Tests audit logs use the service name `networkmanagement.googleapis.com`. Filter for this service: 
    
    
        protoPayload.serviceName="networkmanagement.googleapis.com"
      

## Methods by permission type

Each IAM permission has a `type` property, whose value is an enum that can be one of four values: `ADMIN_READ`, `ADMIN_WRITE`, `DATA_READ`, or `DATA_WRITE`. When you call a method, Connectivity Tests generates an audit log whose category is dependent on the `type` property of the permission required to perform the method. Methods that require an IAM permission with the `type` property value of `DATA_READ`, `DATA_WRITE`, or `ADMIN_READ` generate [Data Access](https://docs.cloud.google.com/logging/docs/audit#data-access) audit logs. Methods that require an IAM permission with the `type` property value of `ADMIN_WRITE` generate [Admin Activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity) audit logs.

API methods in the following list that are marked with (LRO) are long-running operations (LROs). These methods usually generate two audit log entries: one when the operation starts and another when it ends. For more information see [Audit logs for long-running operations](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro). Permission type | Methods  
---|---  
`ADMIN_READ` | `google.cloud.networkmanagement.v1.ReachabilityService.GetConnectivityTest`  
`google.cloud.networkmanagement.v1.ReachabilityService.ListConnectivityTests`  
`google.cloud.networkmanagement.v1.VpcFlowLogsService.GetVpcFlowLogsConfig`  
`google.cloud.networkmanagement.v1.VpcFlowLogsService.ListVpcFlowLogsConfigs`  
`google.cloud.networkmanagement.v1beta1.ReachabilityService.GetConnectivityTest`  
`google.cloud.networkmanagement.v1beta1.ReachabilityService.ListConnectivityTests`  
`google.cloud.networkmanagement.v1beta1.VpcFlowLogsService.GetVpcFlowLogsConfig`  
`google.cloud.networkmanagement.v1beta1.VpcFlowLogsService.ListVpcFlowLogsConfigs`  
`GetIamPolicy`  
`google.longrunning.Operations.GetOperation`  
`google.longrunning.Operations.ListOperations`  
`ADMIN_WRITE` | `google.cloud.networkmanagement.v1.ReachabilityService.CreateConnectivityTest` (LRO)  
`google.cloud.networkmanagement.v1.ReachabilityService.DeleteConnectivityTest` (LRO)  
`google.cloud.networkmanagement.v1.ReachabilityService.RerunConnectivityTest` (LRO)  
`google.cloud.networkmanagement.v1.ReachabilityService.UpdateConnectivityTest` (LRO)  
`google.cloud.networkmanagement.v1.VpcFlowLogsService.CreateVpcFlowLogsConfig` (LRO)  
`google.cloud.networkmanagement.v1.VpcFlowLogsService.DeleteVpcFlowLogsConfig` (LRO)  
`google.cloud.networkmanagement.v1.VpcFlowLogsService.UpdateVpcFlowLogsConfig` (LRO)  
`google.cloud.networkmanagement.v1beta1.ReachabilityService.CreateConnectivityTest` (LRO)  
`google.cloud.networkmanagement.v1beta1.ReachabilityService.DeleteConnectivityTest` (LRO)  
`google.cloud.networkmanagement.v1beta1.ReachabilityService.RerunConnectivityTest` (LRO)  
`google.cloud.networkmanagement.v1beta1.ReachabilityService.UpdateConnectivityTest` (LRO)  
`google.cloud.networkmanagement.v1beta1.VpcFlowLogsService.CreateVpcFlowLogsConfig` (LRO)  
`google.cloud.networkmanagement.v1beta1.VpcFlowLogsService.DeleteVpcFlowLogsConfig` (LRO)  
`google.cloud.networkmanagement.v1beta1.VpcFlowLogsService.UpdateVpcFlowLogsConfig` (LRO)  
`SetIamPolicy`  
`google.longrunning.Operations.CancelOperation`  
`google.longrunning.Operations.DeleteOperation`  
  
## API interface audit logs

For information about how and which permissions are evaluated for each method, see the Identity and Access Management documentation for Connectivity Tests.

### `google.cloud.networkmanagement.v1.ReachabilityService`

The following audit logs are associated with methods belonging to `google.cloud.networkmanagement.v1.ReachabilityService`.

#### `CreateConnectivityTest`

  * **Method** : `google.cloud.networkmanagement.v1.ReachabilityService.CreateConnectivityTest`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `networkmanagement.connectivitytests.create - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.networkmanagement.v1.ReachabilityService.CreateConnectivityTest" `  




#### `DeleteConnectivityTest`

  * **Method** : `google.cloud.networkmanagement.v1.ReachabilityService.DeleteConnectivityTest`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `networkmanagement.connectivitytests.delete - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.networkmanagement.v1.ReachabilityService.DeleteConnectivityTest" `  




#### `GetConnectivityTest`

  * **Method** : `google.cloud.networkmanagement.v1.ReachabilityService.GetConnectivityTest`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `networkmanagement.connectivitytests.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.networkmanagement.v1.ReachabilityService.GetConnectivityTest" `  




#### `ListConnectivityTests`

  * **Method** : `google.cloud.networkmanagement.v1.ReachabilityService.ListConnectivityTests`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `networkmanagement.connectivitytests.list - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.networkmanagement.v1.ReachabilityService.ListConnectivityTests" `  




#### `RerunConnectivityTest`

  * **Method** : `google.cloud.networkmanagement.v1.ReachabilityService.RerunConnectivityTest`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `networkmanagement.connectivitytests.rerun - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.networkmanagement.v1.ReachabilityService.RerunConnectivityTest" `  




#### `UpdateConnectivityTest`

  * **Method** : `google.cloud.networkmanagement.v1.ReachabilityService.UpdateConnectivityTest`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `networkmanagement.connectivitytests.update - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.networkmanagement.v1.ReachabilityService.UpdateConnectivityTest" `  




### `google.cloud.networkmanagement.v1.VpcFlowLogsService`

The following audit logs are associated with methods belonging to `google.cloud.networkmanagement.v1.VpcFlowLogsService`.

#### `CreateVpcFlowLogsConfig`

  * **Method** : `google.cloud.networkmanagement.v1.VpcFlowLogsService.CreateVpcFlowLogsConfig`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `networkmanagement.vpcflowlogsconfigs.create - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.networkmanagement.v1.VpcFlowLogsService.CreateVpcFlowLogsConfig" `  




#### `DeleteVpcFlowLogsConfig`

  * **Method** : `google.cloud.networkmanagement.v1.VpcFlowLogsService.DeleteVpcFlowLogsConfig`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `networkmanagement.vpcflowlogsconfigs.delete - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.networkmanagement.v1.VpcFlowLogsService.DeleteVpcFlowLogsConfig" `  




#### `GetVpcFlowLogsConfig`

  * **Method** : `google.cloud.networkmanagement.v1.VpcFlowLogsService.GetVpcFlowLogsConfig`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `networkmanagement.vpcflowlogsconfigs.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.networkmanagement.v1.VpcFlowLogsService.GetVpcFlowLogsConfig" `  




#### `ListVpcFlowLogsConfigs`

  * **Method** : `google.cloud.networkmanagement.v1.VpcFlowLogsService.ListVpcFlowLogsConfigs`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `networkmanagement.vpcflowlogsconfigs.list - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.networkmanagement.v1.VpcFlowLogsService.ListVpcFlowLogsConfigs" `  




#### `UpdateVpcFlowLogsConfig`

  * **Method** : `google.cloud.networkmanagement.v1.VpcFlowLogsService.UpdateVpcFlowLogsConfig`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `networkmanagement.vpcflowlogsconfigs.update - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.networkmanagement.v1.VpcFlowLogsService.UpdateVpcFlowLogsConfig" `  




### `google.cloud.networkmanagement.v1beta1.ReachabilityService`

The following audit logs are associated with methods belonging to `google.cloud.networkmanagement.v1beta1.ReachabilityService`.

#### `CreateConnectivityTest`

  * **Method** : `google.cloud.networkmanagement.v1beta1.ReachabilityService.CreateConnectivityTest`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `networkmanagement.connectivitytests.create - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.networkmanagement.v1beta1.ReachabilityService.CreateConnectivityTest" `  




#### `DeleteConnectivityTest`

  * **Method** : `google.cloud.networkmanagement.v1beta1.ReachabilityService.DeleteConnectivityTest`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `networkmanagement.connectivitytests.delete - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.networkmanagement.v1beta1.ReachabilityService.DeleteConnectivityTest" `  




#### `GetConnectivityTest`

  * **Method** : `google.cloud.networkmanagement.v1beta1.ReachabilityService.GetConnectivityTest`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `networkmanagement.connectivitytests.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.networkmanagement.v1beta1.ReachabilityService.GetConnectivityTest" `  




#### `ListConnectivityTests`

  * **Method** : `google.cloud.networkmanagement.v1beta1.ReachabilityService.ListConnectivityTests`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `networkmanagement.connectivitytests.list - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.networkmanagement.v1beta1.ReachabilityService.ListConnectivityTests" `  




#### `RerunConnectivityTest`

  * **Method** : `google.cloud.networkmanagement.v1beta1.ReachabilityService.RerunConnectivityTest`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `networkmanagement.connectivitytests.rerun - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.networkmanagement.v1beta1.ReachabilityService.RerunConnectivityTest" `  




#### `UpdateConnectivityTest`

  * **Method** : `google.cloud.networkmanagement.v1beta1.ReachabilityService.UpdateConnectivityTest`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `networkmanagement.connectivitytests.update - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.networkmanagement.v1beta1.ReachabilityService.UpdateConnectivityTest" `  




### `google.cloud.networkmanagement.v1beta1.VpcFlowLogsService`

The following audit logs are associated with methods belonging to `google.cloud.networkmanagement.v1beta1.VpcFlowLogsService`.

#### `CreateVpcFlowLogsConfig`

  * **Method** : `google.cloud.networkmanagement.v1beta1.VpcFlowLogsService.CreateVpcFlowLogsConfig`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `networkmanagement.vpcflowlogsconfigs.create - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.networkmanagement.v1beta1.VpcFlowLogsService.CreateVpcFlowLogsConfig" `  




#### `DeleteVpcFlowLogsConfig`

  * **Method** : `google.cloud.networkmanagement.v1beta1.VpcFlowLogsService.DeleteVpcFlowLogsConfig`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `networkmanagement.vpcflowlogsconfigs.delete - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.networkmanagement.v1beta1.VpcFlowLogsService.DeleteVpcFlowLogsConfig" `  




#### `GetVpcFlowLogsConfig`

  * **Method** : `google.cloud.networkmanagement.v1beta1.VpcFlowLogsService.GetVpcFlowLogsConfig`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `networkmanagement.vpcflowlogsconfigs.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.networkmanagement.v1beta1.VpcFlowLogsService.GetVpcFlowLogsConfig" `  




#### `ListVpcFlowLogsConfigs`

  * **Method** : `google.cloud.networkmanagement.v1beta1.VpcFlowLogsService.ListVpcFlowLogsConfigs`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `networkmanagement.vpcflowlogsconfigs.list - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.networkmanagement.v1beta1.VpcFlowLogsService.ListVpcFlowLogsConfigs" `  




#### `UpdateVpcFlowLogsConfig`

  * **Method** : `google.cloud.networkmanagement.v1beta1.VpcFlowLogsService.UpdateVpcFlowLogsConfig`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `networkmanagement.vpcflowlogsconfigs.update - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.networkmanagement.v1beta1.VpcFlowLogsService.UpdateVpcFlowLogsConfig" `  




### `google.iam.v1.IAMPolicy`

The following audit logs are associated with methods belonging to `google.iam.v1.IAMPolicy`.

#### `GetIamPolicy`

  * **Method** : `GetIamPolicy`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `networkmanagement.connectivitytests.getIamPolicy - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="GetIamPolicy" `  




#### `SetIamPolicy`

  * **Method** : `SetIamPolicy`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `networkmanagement.connectivitytests.setIamPolicy - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="SetIamPolicy" `  




### `google.longrunning.Operations`

The following audit logs are associated with methods belonging to `google.longrunning.Operations`.

#### `CancelOperation`

  * **Method** : `google.longrunning.Operations.CancelOperation`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `networkmanagement.operations.cancel - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.longrunning.Operations.CancelOperation" `  




#### `DeleteOperation`

  * **Method** : `google.longrunning.Operations.DeleteOperation`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `networkmanagement.operations.delete - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.longrunning.Operations.DeleteOperation" `  




#### `GetOperation`

  * **Method** : `google.longrunning.Operations.GetOperation`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `networkmanagement.operations.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.longrunning.Operations.GetOperation" `  




#### `ListOperations`

  * **Method** : `google.longrunning.Operations.ListOperations`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `networkmanagement.operations.list - ADMIN_READ`
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

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
