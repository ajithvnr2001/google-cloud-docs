---
url: https://docs.cloud.google.com/capacity-planner/docs/audit-logging/
title: Capacity Planner audit logging \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T18:38:57.635740+00:00
---

# Capacity Planner audit logging  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/capacity-planner/docs/audit-logging/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ Compute Engine ](https://docs.cloud.google.com/compute/docs)
  * [ Capacity Planner ](https://docs.cloud.google.com/capacity-planner/docs)
  * [ Guides ](https://docs.cloud.google.com/capacity-planner/docs/overview)



Send feedback 

#  Capacity Planner audit logging Stay organized with collections  Save and categorize content based on your preferences. 

**Preview**

This product is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA products are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

This document lists the audited methods for Capacity Planner. Google Cloud services generate audit logs that record administrative and access activities within your Google Cloud resources. For more information about Cloud Audit Logs, see the following: 

  * [Types of audit logs](https://docs.cloud.google.com/logging/docs/audit#types)
  * [Audit log entry structure](https://docs.cloud.google.com/logging/docs/audit#audit_log_entry_structure)
  * [Storing and routing audit logs](https://docs.cloud.google.com/logging/docs/audit#storing_and_routing_audit_logs)
  * [Cloud Logging pricing summary](https://docs.cloud.google.com/stackdriver/pricing#logs-pricing-summary)
  * [Enable Data Access audit logs](https://docs.cloud.google.com/logging/docs/audit/configure-data-access)



## Service name

To view the Capacity Planner audit logs, do the following:

  1. In the Google Cloud console, go to the Logs Explorer page:

[Go to Logs Explorer](https://console.cloud.google.com/logs/query)

  2. Copy and paste the following query into the **Query** field of the Logs Explorer, and then click **Run query**.
         
         protoPayload.serviceName="capacityplanner.googleapis.com"
           




## Methods by permission type

Each IAM permission has a `type` property, whose value is an enum that can be one of four values: `ADMIN_READ`, `ADMIN_WRITE`, `DATA_READ`, or `DATA_WRITE`. When you call a method, Capacity Planner generates an audit log whose category is dependent on the `type` property of the permission required to perform the method. Methods that require an IAM permission with the `type` property value of `DATA_READ`, `DATA_WRITE`, or `ADMIN_READ` generate [Data Access](https://docs.cloud.google.com/logging/docs/audit#data-access) audit logs. Methods that require an IAM permission with the `type` property value of `ADMIN_WRITE` generate [Admin Activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity) audit logs.

API methods in the following list that are marked with (LRO) are long-running operations (LROs). These methods usually generate two audit log entries: one when the operation starts and another when it ends. For more information see [Audit logs for long-running operations](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro). Permission type | Methods  
---|---  
`ADMIN_READ` | `google.cloud.capacityplanner.v1alpha.UsageService.ExportForecasts`  
`google.cloud.capacityplanner.v1alpha.UsageService.ExportMachineShapeUsage`  
`google.cloud.capacityplanner.v1alpha.UsageService.ExportReservationsUsage`  
`google.cloud.capacityplanner.v1alpha.UsageService.ExportUsageHistories`  
`google.cloud.capacityplanner.v1alpha.UsageService.QueryForecasts`  
`google.cloud.capacityplanner.v1alpha.UsageService.QueryReservations`  
`google.cloud.capacityplanner.v1alpha.UsageService.QueryUsageHistories`  
`google.cloud.capacityplanner.v1beta.UsageService.ExportForecasts`  
`google.cloud.capacityplanner.v1beta.UsageService.ExportReservationsUsage`  
`google.cloud.capacityplanner.v1beta.UsageService.ExportUsageHistories`  
`google.cloud.capacityplanner.v1beta.UsageService.QueryForecasts`  
`google.cloud.capacityplanner.v1beta.UsageService.QueryReservations`  
`google.cloud.capacityplanner.v1beta.UsageService.QueryUsageHistories`  
`google.cloud.capacityplanner.v1main.UsageService.QueryForecasts`  
`google.cloud.capacityplanner.v1main.UsageService.QueryMachineShapeUsage`  
`google.cloud.capacityplanner.v1main.UsageService.QueryReservations`  
`google.cloud.capacityplanner.v1main.UsageService.QueryUsageHistories`  
`google.cloud.capacityplanner.v1main.UsageService.SummarizeUsage`  
`DATA_READ` | `google.cloud.capacityplanner.v1alpha.CapacityPlanningService.CheckRelatedResources`  
`google.cloud.capacityplanner.v1alpha.CapacityPlanningService.GetCapacityPlan`  
`google.cloud.capacityplanner.v1alpha.CapacityPlanningService.ListCapacityPlans`  
`google.cloud.capacityplanner.v1alpha.CapacityPlanningService.QueryCapacityPlanInsights`  
`google.cloud.capacityplanner.v1alpha.CapacityPlanningService.QueryCapacityPlans`  
`google.cloud.capacityplanner.v1alpha.CapacityPlanningService.QueryDemandPlanMetadata`  
`google.longrunning.Operations.GetOperation`  
`DATA_WRITE` | `google.cloud.capacityplanner.v1alpha.CapacityPlanningService.CreateCapacityPlan`  
  
## API interface audit logs

For information about how and which permissions are evaluated for each method, see the Identity and Access Management documentation for Capacity Planner.

### `google.cloud.capacityplanner.v1alpha.CapacityPlanningService`

The following audit logs are associated with methods belonging to `google.cloud.capacityplanner.v1alpha.CapacityPlanningService`.

#### `CheckRelatedResources`

  * **Method** : `google.cloud.capacityplanner.v1alpha.CapacityPlanningService.CheckRelatedResources`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `capacityplanner.capacityPlans.get - DATA_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.capacityplanner.v1alpha.CapacityPlanningService.CheckRelatedResources" `  




#### `CreateCapacityPlan`

  * **Method** : `google.cloud.capacityplanner.v1alpha.CapacityPlanningService.CreateCapacityPlan`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `capacityplanner.capacityPlans.create - DATA_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.capacityplanner.v1alpha.CapacityPlanningService.CreateCapacityPlan" `  




#### `GetCapacityPlan`

  * **Method** : `google.cloud.capacityplanner.v1alpha.CapacityPlanningService.GetCapacityPlan`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `capacityplanner.capacityPlans.get - DATA_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.capacityplanner.v1alpha.CapacityPlanningService.GetCapacityPlan" `  




#### `ListCapacityPlans`

  * **Method** : `google.cloud.capacityplanner.v1alpha.CapacityPlanningService.ListCapacityPlans`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `capacityplanner.capacityPlans.list - DATA_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.capacityplanner.v1alpha.CapacityPlanningService.ListCapacityPlans" `  




#### `QueryCapacityPlanInsights`

  * **Method** : `google.cloud.capacityplanner.v1alpha.CapacityPlanningService.QueryCapacityPlanInsights`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `capacityplanner.capacityPlans.list - DATA_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.capacityplanner.v1alpha.CapacityPlanningService.QueryCapacityPlanInsights" `  




#### `QueryCapacityPlans`

  * **Method** : `google.cloud.capacityplanner.v1alpha.CapacityPlanningService.QueryCapacityPlans`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `capacityplanner.capacityPlans.list - DATA_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.capacityplanner.v1alpha.CapacityPlanningService.QueryCapacityPlans" `  




#### `QueryDemandPlanMetadata`

  * **Method** : `google.cloud.capacityplanner.v1alpha.CapacityPlanningService.QueryDemandPlanMetadata`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `capacityplanner.capacityPlans.list - DATA_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.capacityplanner.v1alpha.CapacityPlanningService.QueryDemandPlanMetadata" `  




### `google.cloud.capacityplanner.v1alpha.UsageService`

The following audit logs are associated with methods belonging to `google.cloud.capacityplanner.v1alpha.UsageService`.

#### `ExportForecasts`

  * **Method** : `google.cloud.capacityplanner.v1alpha.UsageService.ExportForecasts`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `capacityplanner.forecasts.list - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.capacityplanner.v1alpha.UsageService.ExportForecasts" `  




#### `ExportMachineShapeUsage`

  * **Method** : `google.cloud.capacityplanner.v1alpha.UsageService.ExportMachineShapeUsage`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `capacityplanner.forecasts.list - ADMIN_READ`
    * `capacityplanner.usageHistories.list - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.capacityplanner.v1alpha.UsageService.ExportMachineShapeUsage" `  




#### `ExportReservationsUsage`

  * **Method** : `google.cloud.capacityplanner.v1alpha.UsageService.ExportReservationsUsage`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `capacityplanner.usageHistories.list - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.capacityplanner.v1alpha.UsageService.ExportReservationsUsage" `  




#### `ExportUsageHistories`

  * **Method** : `google.cloud.capacityplanner.v1alpha.UsageService.ExportUsageHistories`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `capacityplanner.usageHistories.list - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.capacityplanner.v1alpha.UsageService.ExportUsageHistories" `  




#### `QueryForecasts`

  * **Method** : `google.cloud.capacityplanner.v1alpha.UsageService.QueryForecasts`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `capacityplanner.forecasts.list - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.capacityplanner.v1alpha.UsageService.QueryForecasts" `  




#### `QueryReservations`

  * **Method** : `google.cloud.capacityplanner.v1alpha.UsageService.QueryReservations`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `capacityplanner.usageHistories.list - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.capacityplanner.v1alpha.UsageService.QueryReservations" `  




#### `QueryUsageHistories`

  * **Method** : `google.cloud.capacityplanner.v1alpha.UsageService.QueryUsageHistories`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `capacityplanner.usageHistories.list - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.capacityplanner.v1alpha.UsageService.QueryUsageHistories" `  




### `google.cloud.capacityplanner.v1beta.UsageService`

The following audit logs are associated with methods belonging to `google.cloud.capacityplanner.v1beta.UsageService`.

#### `ExportForecasts`

  * **Method** : `google.cloud.capacityplanner.v1beta.UsageService.ExportForecasts`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `capacityplanner.forecasts.list - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.capacityplanner.v1beta.UsageService.ExportForecasts" `  




#### `ExportReservationsUsage`

  * **Method** : `google.cloud.capacityplanner.v1beta.UsageService.ExportReservationsUsage`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `capacityplanner.usageHistories.list - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.capacityplanner.v1beta.UsageService.ExportReservationsUsage" `  




#### `ExportUsageHistories`

  * **Method** : `google.cloud.capacityplanner.v1beta.UsageService.ExportUsageHistories`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `capacityplanner.usageHistories.list - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.capacityplanner.v1beta.UsageService.ExportUsageHistories" `  




#### `QueryForecasts`

  * **Method** : `google.cloud.capacityplanner.v1beta.UsageService.QueryForecasts`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `capacityplanner.forecasts.list - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.capacityplanner.v1beta.UsageService.QueryForecasts" `  




#### `QueryReservations`

  * **Method** : `google.cloud.capacityplanner.v1beta.UsageService.QueryReservations`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `capacityplanner.usageHistories.list - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.capacityplanner.v1beta.UsageService.QueryReservations" `  




#### `QueryUsageHistories`

  * **Method** : `google.cloud.capacityplanner.v1beta.UsageService.QueryUsageHistories`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `capacityplanner.usageHistories.list - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.capacityplanner.v1beta.UsageService.QueryUsageHistories" `  




### `google.cloud.capacityplanner.v1main.UsageService`

The following audit logs are associated with methods belonging to `google.cloud.capacityplanner.v1main.UsageService`.

#### `QueryForecasts`

  * **Method** : `google.cloud.capacityplanner.v1main.UsageService.QueryForecasts`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `capacityplanner.forecasts.list - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.capacityplanner.v1main.UsageService.QueryForecasts" `  




#### `QueryMachineShapeUsage`

  * **Method** : `google.cloud.capacityplanner.v1main.UsageService.QueryMachineShapeUsage`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `capacityplanner.forecasts.list - ADMIN_READ`
    * `capacityplanner.usageHistories.list - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.capacityplanner.v1main.UsageService.QueryMachineShapeUsage" `  




#### `QueryReservations`

  * **Method** : `google.cloud.capacityplanner.v1main.UsageService.QueryReservations`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `capacityplanner.usageHistories.list - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.capacityplanner.v1main.UsageService.QueryReservations" `  




#### `QueryUsageHistories`

  * **Method** : `google.cloud.capacityplanner.v1main.UsageService.QueryUsageHistories`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `capacityplanner.usageHistories.list - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.capacityplanner.v1main.UsageService.QueryUsageHistories" `  




#### `SummarizeUsage`

  * **Method** : `google.cloud.capacityplanner.v1main.UsageService.SummarizeUsage`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `capacityplanner.usageHistories.summarize - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.capacityplanner.v1main.UsageService.SummarizeUsage" `  




### `google.longrunning.Operations`

The following audit logs are associated with methods belonging to `google.longrunning.Operations`.

#### `GetOperation`

  * **Method** : `google.longrunning.Operations.GetOperation`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `capacityplanner.operations.get - DATA_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.longrunning.Operations.GetOperation" `  




## Methods that don't produce audit logs

A method might not produce audit logs for one or more of the following reasons: 

  * It is a high volume method involving significant log generation and storage costs.
  * It has low auditing value.
  * Another audit or platform log already provides method coverage.



The following methods don't produce audit logs:

  * `google.longrunning.Operations.CancelOperation`
  * `google.longrunning.Operations.DeleteOperation`
  * `google.longrunning.Operations.ListOperations`
  * `google.longrunning.Operations.WaitOperation`



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
