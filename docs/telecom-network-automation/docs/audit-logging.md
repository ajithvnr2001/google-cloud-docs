---
url: https://docs.cloud.google.com/telecom-network-automation/docs/audit-logging/
title: Telco Automation API audit logging \u00a0|\u00a0 Telecom Network Automation \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T08:36:48.507691+00:00
---

# Telco Automation API audit logging  |  Telecom Network Automation  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/telecom-network-automation/docs/audit-logging/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Industry solutions ](https://docs.cloud.google.com/docs/industry)
  * [ Telecom Network Automation ](https://docs.cloud.google.com/telecom-network-automation/docs)
  * [ Guides ](https://docs.cloud.google.com/telecom-network-automation/docs/overview)



Send feedback 

#  Telco Automation API audit logging Stay organized with collections  Save and categorize content based on your preferences. 

This document describes audit logging for Telco Automation API. Google Cloud services generate audit logs that record administrative and access activities within your Google Cloud resources. For more information about Cloud Audit Logs, see the following: 

  * [Types of audit logs](https://docs.cloud.google.com/logging/docs/audit#types)
  * [Audit log entry structure](https://docs.cloud.google.com/logging/docs/audit#audit_log_entry_structure)
  * [Storing and routing audit logs](https://docs.cloud.google.com/logging/docs/audit#storing_and_routing_audit_logs)
  * [Cloud Logging pricing summary](https://docs.cloud.google.com/stackdriver/pricing#logs-pricing-summary)
  * [Enable Data Access audit logs](https://docs.cloud.google.com/logging/docs/audit/configure-data-access)



## Service name

Telco Automation API audit logs use the service name `telcoautomation.googleapis.com`. Filter for this service: 
    
    
        protoPayload.serviceName="telcoautomation.googleapis.com"
      

## Methods by permission type

Each IAM permission has a `type` property, whose value is an enum that can be one of four values: `ADMIN_READ`, `ADMIN_WRITE`, `DATA_READ`, or `DATA_WRITE`. When you call a method, Telco Automation API generates an audit log whose category is dependent on the `type` property of the permission required to perform the method. Methods that require an IAM permission with the `type` property value of `DATA_READ`, `DATA_WRITE`, or `ADMIN_READ` generate [Data Access](https://docs.cloud.google.com/logging/docs/audit#data-access) audit logs. Methods that require an IAM permission with the `type` property value of `ADMIN_WRITE` generate [Admin Activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity) audit logs.

Permission type | Methods  
---|---  
`ADMIN_READ` | `google.cloud.telcoautomation.v1.TelcoAutomation.GetBlueprint`  
`google.cloud.telcoautomation.v1.TelcoAutomation.GetDeployment`  
`google.cloud.telcoautomation.v1.TelcoAutomation.ListBlueprintRevisions`  
`google.cloud.telcoautomation.v1alpha1.TelcoAutomation.ComputeDeploymentStatus`  
`google.cloud.telcoautomation.v1alpha1.TelcoAutomation.GetBlueprint`  
`google.cloud.telcoautomation.v1alpha1.TelcoAutomation.GetDeployment`  
`google.cloud.telcoautomation.v1alpha1.TelcoAutomation.GetEdgeSlm`  
`google.cloud.telcoautomation.v1alpha1.TelcoAutomation.ListBlueprints`  
`google.cloud.telcoautomation.v1alpha1.TelcoAutomation.ListDeployments`  
`google.cloud.telcoautomation.v1alpha1.TelcoAutomation.ListOrchestrationClusters`  
`google.cloud.telcoautomation.v1alpha1.TelcoAutomation.SearchBlueprintRevisions`  
`google.cloud.telcoautomation.v1alpha1.TelcoAutomation.SearchDeploymentRevisions`  
`ADMIN_WRITE` | `google.cloud.telcoautomation.v1.TelcoAutomation.ApproveBlueprint`  
`google.cloud.telcoautomation.v1.TelcoAutomation.CreateBlueprint`  
`google.cloud.telcoautomation.v1.TelcoAutomation.CreateDeployment`  
`google.cloud.telcoautomation.v1.TelcoAutomation.ProposeBlueprint`  
`google.cloud.telcoautomation.v1.TelcoAutomation.UpdateDeployment`  
`google.cloud.telcoautomation.v1alpha1.TelcoAutomation.ApplyDeployment`  
`google.cloud.telcoautomation.v1alpha1.TelcoAutomation.ApproveBlueprint`  
`google.cloud.telcoautomation.v1alpha1.TelcoAutomation.CreateBlueprint`  
`google.cloud.telcoautomation.v1alpha1.TelcoAutomation.CreateDeployment`  
`google.cloud.telcoautomation.v1alpha1.TelcoAutomation.CreateOrchestrationCluster`  
`google.cloud.telcoautomation.v1alpha1.TelcoAutomation.DeleteBlueprint`  
`google.cloud.telcoautomation.v1alpha1.TelcoAutomation.DeleteOrchestrationCluster`  
`google.cloud.telcoautomation.v1alpha1.TelcoAutomation.DiscardBlueprintChanges`  
`google.cloud.telcoautomation.v1alpha1.TelcoAutomation.ProposeBlueprint`  
`google.cloud.telcoautomation.v1alpha1.TelcoAutomation.RejectBlueprint`  
`google.cloud.telcoautomation.v1alpha1.TelcoAutomation.RemoveDeployment`  
`google.cloud.telcoautomation.v1alpha1.TelcoAutomation.UpdateBlueprint`  
`DATA_READ` | `google.cloud.telcoautomation.v1alpha1.TelcoAutomation.ListPublicBlueprints`  
  
## API interface audit logs

For information about how and which permissions are evaluated for each method, see the Identity and Access Management documentation for Telco Automation API.

### `google.cloud.telcoautomation.v1.TelcoAutomation`

The following audit logs are associated with methods belonging to `google.cloud.telcoautomation.v1.TelcoAutomation`.

#### `ApproveBlueprint`

  * **Method** : `google.cloud.telcoautomation.v1.TelcoAutomation.ApproveBlueprint`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `telcoautomation.blueprints.approve - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.telcoautomation.v1.TelcoAutomation.ApproveBlueprint" `  




#### `CreateBlueprint`

  * **Method** : `google.cloud.telcoautomation.v1.TelcoAutomation.CreateBlueprint`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `telcoautomation.blueprints.create - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.telcoautomation.v1.TelcoAutomation.CreateBlueprint" `  




#### `CreateDeployment`

  * **Method** : `google.cloud.telcoautomation.v1.TelcoAutomation.CreateDeployment`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `telcoautomation.deployments.create - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.telcoautomation.v1.TelcoAutomation.CreateDeployment" `  




#### `GetBlueprint`

  * **Method** : `google.cloud.telcoautomation.v1.TelcoAutomation.GetBlueprint`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `telcoautomation.blueprints.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.telcoautomation.v1.TelcoAutomation.GetBlueprint" `  




#### `GetDeployment`

  * **Method** : `google.cloud.telcoautomation.v1.TelcoAutomation.GetDeployment`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `telcoautomation.deployments.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.telcoautomation.v1.TelcoAutomation.GetDeployment" `  




#### `ListBlueprintRevisions`

  * **Method** : `google.cloud.telcoautomation.v1.TelcoAutomation.ListBlueprintRevisions`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `telcoautomation.blueprints.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.telcoautomation.v1.TelcoAutomation.ListBlueprintRevisions" `  




#### `ProposeBlueprint`

  * **Method** : `google.cloud.telcoautomation.v1.TelcoAutomation.ProposeBlueprint`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `telcoautomation.blueprints.propose - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.telcoautomation.v1.TelcoAutomation.ProposeBlueprint" `  




#### `UpdateDeployment`

  * **Method** : `google.cloud.telcoautomation.v1.TelcoAutomation.UpdateDeployment`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `telcoautomation.deployments.update - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.telcoautomation.v1.TelcoAutomation.UpdateDeployment" `  




### `google.cloud.telcoautomation.v1alpha1.TelcoAutomation`

The following audit logs are associated with methods belonging to `google.cloud.telcoautomation.v1alpha1.TelcoAutomation`.

#### `ApplyDeployment`

  * **Method** : `google.cloud.telcoautomation.v1alpha1.TelcoAutomation.ApplyDeployment`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `telcoautomation.deployments.apply - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.telcoautomation.v1alpha1.TelcoAutomation.ApplyDeployment" `  




#### `ApproveBlueprint`

  * **Method** : `google.cloud.telcoautomation.v1alpha1.TelcoAutomation.ApproveBlueprint`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `telcoautomation.blueprints.approve - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.telcoautomation.v1alpha1.TelcoAutomation.ApproveBlueprint" `  




#### `ComputeDeploymentStatus`

  * **Method** : `google.cloud.telcoautomation.v1alpha1.TelcoAutomation.ComputeDeploymentStatus`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `telcoautomation.deployments.computeStatus - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.telcoautomation.v1alpha1.TelcoAutomation.ComputeDeploymentStatus" `  




#### `CreateBlueprint`

  * **Method** : `google.cloud.telcoautomation.v1alpha1.TelcoAutomation.CreateBlueprint`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `telcoautomation.blueprints.create - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.telcoautomation.v1alpha1.TelcoAutomation.CreateBlueprint" `  




#### `CreateDeployment`

  * **Method** : `google.cloud.telcoautomation.v1alpha1.TelcoAutomation.CreateDeployment`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `telcoautomation.deployments.create - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.telcoautomation.v1alpha1.TelcoAutomation.CreateDeployment" `  




#### `CreateOrchestrationCluster`

  * **Method** : `google.cloud.telcoautomation.v1alpha1.TelcoAutomation.CreateOrchestrationCluster`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `telcoautomation.orchestrationClusters.create - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.telcoautomation.v1alpha1.TelcoAutomation.CreateOrchestrationCluster" `  




#### `DeleteBlueprint`

  * **Method** : `google.cloud.telcoautomation.v1alpha1.TelcoAutomation.DeleteBlueprint`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `telcoautomation.blueprints.delete - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.telcoautomation.v1alpha1.TelcoAutomation.DeleteBlueprint" `  




#### `DeleteOrchestrationCluster`

  * **Method** : `google.cloud.telcoautomation.v1alpha1.TelcoAutomation.DeleteOrchestrationCluster`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `telcoautomation.orchestrationClusters.delete - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.telcoautomation.v1alpha1.TelcoAutomation.DeleteOrchestrationCluster" `  




#### `DiscardBlueprintChanges`

  * **Method** : `google.cloud.telcoautomation.v1alpha1.TelcoAutomation.DiscardBlueprintChanges`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `telcoautomation.blueprints.update - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.telcoautomation.v1alpha1.TelcoAutomation.DiscardBlueprintChanges" `  




#### `GetBlueprint`

  * **Method** : `google.cloud.telcoautomation.v1alpha1.TelcoAutomation.GetBlueprint`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `telcoautomation.blueprints.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.telcoautomation.v1alpha1.TelcoAutomation.GetBlueprint" `  




#### `GetDeployment`

  * **Method** : `google.cloud.telcoautomation.v1alpha1.TelcoAutomation.GetDeployment`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `telcoautomation.deployments.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.telcoautomation.v1alpha1.TelcoAutomation.GetDeployment" `  




#### `GetEdgeSlm`

  * **Method** : `google.cloud.telcoautomation.v1alpha1.TelcoAutomation.GetEdgeSlm`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `telcoautomation.edgeSlms.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.telcoautomation.v1alpha1.TelcoAutomation.GetEdgeSlm" `  




#### `ListBlueprints`

  * **Method** : `google.cloud.telcoautomation.v1alpha1.TelcoAutomation.ListBlueprints`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `telcoautomation.blueprints.list - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.telcoautomation.v1alpha1.TelcoAutomation.ListBlueprints" `  




#### `ListDeployments`

  * **Method** : `google.cloud.telcoautomation.v1alpha1.TelcoAutomation.ListDeployments`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `telcoautomation.deployments.list - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.telcoautomation.v1alpha1.TelcoAutomation.ListDeployments" `  




#### `ListOrchestrationClusters`

  * **Method** : `google.cloud.telcoautomation.v1alpha1.TelcoAutomation.ListOrchestrationClusters`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `telcoautomation.orchestrationClusters.list - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.telcoautomation.v1alpha1.TelcoAutomation.ListOrchestrationClusters" `  




#### `ListPublicBlueprints`

  * **Method** : `google.cloud.telcoautomation.v1alpha1.TelcoAutomation.ListPublicBlueprints`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `telcoautomation.publicBlueprints.list - DATA_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.telcoautomation.v1alpha1.TelcoAutomation.ListPublicBlueprints" `  




#### `ProposeBlueprint`

  * **Method** : `google.cloud.telcoautomation.v1alpha1.TelcoAutomation.ProposeBlueprint`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `telcoautomation.blueprints.propose - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.telcoautomation.v1alpha1.TelcoAutomation.ProposeBlueprint" `  




#### `RejectBlueprint`

  * **Method** : `google.cloud.telcoautomation.v1alpha1.TelcoAutomation.RejectBlueprint`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `telcoautomation.blueprints.approve - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.telcoautomation.v1alpha1.TelcoAutomation.RejectBlueprint" `  




#### `RemoveDeployment`

  * **Method** : `google.cloud.telcoautomation.v1alpha1.TelcoAutomation.RemoveDeployment`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `telcoautomation.deployments.delete - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.telcoautomation.v1alpha1.TelcoAutomation.RemoveDeployment" `  




#### `SearchBlueprintRevisions`

  * **Method** : `google.cloud.telcoautomation.v1alpha1.TelcoAutomation.SearchBlueprintRevisions`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `telcoautomation.blueprints.list - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.telcoautomation.v1alpha1.TelcoAutomation.SearchBlueprintRevisions" `  




#### `SearchDeploymentRevisions`

  * **Method** : `google.cloud.telcoautomation.v1alpha1.TelcoAutomation.SearchDeploymentRevisions`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `telcoautomation.deployments.list - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.telcoautomation.v1alpha1.TelcoAutomation.SearchDeploymentRevisions" `  




#### `UpdateBlueprint`

  * **Method** : `google.cloud.telcoautomation.v1alpha1.TelcoAutomation.UpdateBlueprint`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `telcoautomation.blueprints.update - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.telcoautomation.v1alpha1.TelcoAutomation.UpdateBlueprint" `  




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
