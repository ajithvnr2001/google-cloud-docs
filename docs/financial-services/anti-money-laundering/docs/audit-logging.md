---
url: https://docs.cloud.google.com/financial-services/anti-money-laundering/docs/audit-logging/
title: Use AML AI audit logs \u00a0|\u00a0 Anti Money Laundering AI \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T08:51:55.411520+00:00
---

# Use AML AI audit logs  |  Anti Money Laundering AI  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/financial-services/anti-money-laundering/docs/audit-logging/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Industry solutions ](https://docs.cloud.google.com/docs/industry)
  * [ Anti Money Laundering AI ](https://docs.cloud.google.com/financial-services/anti-money-laundering/docs)
  * [ Guides ](https://docs.cloud.google.com/financial-services/anti-money-laundering/docs/concepts/overview)



Send feedback 

#  Use AML AI audit logs Stay organized with collections  Save and categorize content based on your preferences. 

This document lists the audited methods for Financial Services. Google Cloud services generate audit logs that record administrative and access activities within your Google Cloud resources. For more information about Cloud Audit Logs, see the following: 

  * [Types of audit logs](https://docs.cloud.google.com/logging/docs/audit#types)
  * [Audit log entry structure](https://docs.cloud.google.com/logging/docs/audit#audit_log_entry_structure)
  * [Storing and routing audit logs](https://docs.cloud.google.com/logging/docs/audit#storing_and_routing_audit_logs)
  * [Cloud Logging pricing summary](https://docs.cloud.google.com/stackdriver/pricing#logs-pricing-summary)
  * [Enable Data Access audit logs](https://docs.cloud.google.com/logging/docs/audit/configure-data-access)



## Service name

To view the Financial Services audit logs, do the following:

  1. In the Google Cloud console, go to the Logs Explorer page:

[Go to Logs Explorer](https://console.cloud.google.com/logs/query)

  2. Copy and paste the following query into the **Query** field of the Logs Explorer, and then click **Run query**.
         
         protoPayload.serviceName="financialservices.googleapis.com"
           




## Methods by permission type

Each IAM permission has a `type` property, whose value is an enum that can be one of four values: `ADMIN_READ`, `ADMIN_WRITE`, `DATA_READ`, or `DATA_WRITE`. When you call a method, Financial Services generates an audit log whose category is dependent on the `type` property of the permission required to perform the method. Methods that require an IAM permission with the `type` property value of `DATA_READ`, `DATA_WRITE`, or `ADMIN_READ` generate [Data Access](https://docs.cloud.google.com/logging/docs/audit#data-access) audit logs. Methods that require an IAM permission with the `type` property value of `ADMIN_WRITE` generate [Admin Activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity) audit logs.

API methods in the following list that are marked with (LRO) are long-running operations (LROs). These methods usually generate two audit log entries: one when the operation starts and another when it ends. For more information see [Audit logs for long-running operations](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro). Permission type | Methods  
---|---  
`ADMIN_READ` | `google.longrunning.Operations.GetOperation`  
`google.longrunning.Operations.ListOperations`  
`ADMIN_WRITE` | `google.longrunning.Operations.CancelOperation`  
`google.longrunning.Operations.DeleteOperation`  
`DATA_READ` | `google.cloud.financialservices.v1.AML.ExportBacktestResultMetadata` (LRO)  
`google.cloud.financialservices.v1.AML.ExportEngineConfigMetadata` (LRO)  
`google.cloud.financialservices.v1.AML.ExportModelMetadata` (LRO)  
`google.cloud.financialservices.v1.AML.ExportPredictionResultMetadata` (LRO)  
`google.cloud.financialservices.v1.AML.ExportRegisteredParties` (LRO)  
`google.cloud.financialservices.v1.AML.GetBacktestResult`  
`google.cloud.financialservices.v1.AML.GetDataset`  
`google.cloud.financialservices.v1.AML.GetEngineConfig`  
`google.cloud.financialservices.v1.AML.GetEngineVersion`  
`google.cloud.financialservices.v1.AML.GetInstance`  
`google.cloud.financialservices.v1.AML.GetModel`  
`google.cloud.financialservices.v1.AML.GetPredictionResult`  
`google.cloud.financialservices.v1.AML.ListBacktestResults`  
`google.cloud.financialservices.v1.AML.ListDatasets`  
`google.cloud.financialservices.v1.AML.ListEngineConfigs`  
`google.cloud.financialservices.v1.AML.ListEngineVersions`  
`google.cloud.financialservices.v1.AML.ListInstances`  
`google.cloud.financialservices.v1.AML.ListModels`  
`google.cloud.financialservices.v1.AML.ListPredictionResults`  
`google.cloud.financialservices.v1alpha.AML.ExportBacktestResultMetadata` (LRO)  
`google.cloud.financialservices.v1alpha.AML.ExportEngineConfigMetadata` (LRO)  
`google.cloud.financialservices.v1alpha.AML.ExportModelMetadata` (LRO)  
`google.cloud.financialservices.v1alpha.AML.ExportPredictionResultMetadata` (LRO)  
`google.cloud.financialservices.v1alpha.AML.ExportRegisteredParties` (LRO)  
`google.cloud.financialservices.v1alpha.AML.GetBacktestResult`  
`google.cloud.financialservices.v1alpha.AML.GetDataset`  
`google.cloud.financialservices.v1alpha.AML.GetEngineConfig`  
`google.cloud.financialservices.v1alpha.AML.GetEngineVersion`  
`google.cloud.financialservices.v1alpha.AML.GetInstance`  
`google.cloud.financialservices.v1alpha.AML.GetModel`  
`google.cloud.financialservices.v1alpha.AML.GetPredictionResult`  
`google.cloud.financialservices.v1alpha.AML.ListBacktestResults`  
`google.cloud.financialservices.v1alpha.AML.ListDatasets`  
`google.cloud.financialservices.v1alpha.AML.ListEngineConfigs`  
`google.cloud.financialservices.v1alpha.AML.ListEngineVersions`  
`google.cloud.financialservices.v1alpha.AML.ListInstances`  
`google.cloud.financialservices.v1alpha.AML.ListModels`  
`google.cloud.financialservices.v1alpha.AML.ListPredictionResults`  
`DATA_WRITE` | `google.cloud.financialservices.v1.AML.CreateBacktestResult` (LRO)  
`google.cloud.financialservices.v1.AML.CreateDataset` (LRO)  
`google.cloud.financialservices.v1.AML.CreateEngineConfig` (LRO)  
`google.cloud.financialservices.v1.AML.CreateInstance` (LRO)  
`google.cloud.financialservices.v1.AML.CreateModel` (LRO)  
`google.cloud.financialservices.v1.AML.CreatePredictionResult` (LRO)  
`google.cloud.financialservices.v1.AML.DeleteBacktestResult` (LRO)  
`google.cloud.financialservices.v1.AML.DeleteDataset` (LRO)  
`google.cloud.financialservices.v1.AML.DeleteEngineConfig` (LRO)  
`google.cloud.financialservices.v1.AML.DeleteInstance` (LRO)  
`google.cloud.financialservices.v1.AML.DeleteModel` (LRO)  
`google.cloud.financialservices.v1.AML.DeletePredictionResult` (LRO)  
`google.cloud.financialservices.v1.AML.ImportRegisteredParties` (LRO)  
`google.cloud.financialservices.v1.AML.UpdateDataset` (LRO)  
`google.cloud.financialservices.v1.AML.UpdateInstance` (LRO)  
`google.cloud.financialservices.v1alpha.AML.CreateBacktestResult` (LRO)  
`google.cloud.financialservices.v1alpha.AML.CreateDataset` (LRO)  
`google.cloud.financialservices.v1alpha.AML.CreateEngineConfig` (LRO)  
`google.cloud.financialservices.v1alpha.AML.CreateInstance` (LRO)  
`google.cloud.financialservices.v1alpha.AML.CreateModel` (LRO)  
`google.cloud.financialservices.v1alpha.AML.CreatePredictionResult` (LRO)  
`google.cloud.financialservices.v1alpha.AML.DeleteBacktestResult` (LRO)  
`google.cloud.financialservices.v1alpha.AML.DeleteDataset` (LRO)  
`google.cloud.financialservices.v1alpha.AML.DeleteEngineConfig` (LRO)  
`google.cloud.financialservices.v1alpha.AML.DeleteInstance` (LRO)  
`google.cloud.financialservices.v1alpha.AML.DeleteModel` (LRO)  
`google.cloud.financialservices.v1alpha.AML.DeletePredictionResult` (LRO)  
`google.cloud.financialservices.v1alpha.AML.ImportRegisteredParties` (LRO)  
`google.cloud.financialservices.v1alpha.AML.UpdateBacktestResult` (LRO)  
`google.cloud.financialservices.v1alpha.AML.UpdateDataset` (LRO)  
`google.cloud.financialservices.v1alpha.AML.UpdateEngineConfig` (LRO)  
`google.cloud.financialservices.v1alpha.AML.UpdateInstance` (LRO)  
`google.cloud.financialservices.v1alpha.AML.UpdateModel` (LRO)  
`google.cloud.financialservices.v1alpha.AML.UpdatePredictionResult` (LRO)  
  
## API interface audit logs

For information about how and which permissions are evaluated for each method, see the Identity and Access Management documentation for Financial Services.

### `google.cloud.financialservices.v1.AML`

The following audit logs are associated with methods belonging to `google.cloud.financialservices.v1.AML`.

#### `CreateBacktestResult`

  * **Method** : `google.cloud.financialservices.v1.AML.CreateBacktestResult`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `financialservices.v1backtests.create - DATA_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.financialservices.v1.AML.CreateBacktestResult" `  




#### `CreateDataset`

  * **Method** : `google.cloud.financialservices.v1.AML.CreateDataset`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `financialservices.v1datasets.create - DATA_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.financialservices.v1.AML.CreateDataset" `  




#### `CreateEngineConfig`

  * **Method** : `google.cloud.financialservices.v1.AML.CreateEngineConfig`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `financialservices.v1engineconfigs.create - DATA_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.financialservices.v1.AML.CreateEngineConfig" `  




#### `CreateInstance`

  * **Method** : `google.cloud.financialservices.v1.AML.CreateInstance`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `financialservices.v1instances.create - DATA_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.financialservices.v1.AML.CreateInstance" `  




#### `CreateModel`

  * **Method** : `google.cloud.financialservices.v1.AML.CreateModel`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `financialservices.v1models.create - DATA_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.financialservices.v1.AML.CreateModel" `  




#### `CreatePredictionResult`

  * **Method** : `google.cloud.financialservices.v1.AML.CreatePredictionResult`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `financialservices.v1predictions.create - DATA_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.financialservices.v1.AML.CreatePredictionResult" `  




#### `DeleteBacktestResult`

  * **Method** : `google.cloud.financialservices.v1.AML.DeleteBacktestResult`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `financialservices.v1backtests.delete - DATA_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.financialservices.v1.AML.DeleteBacktestResult" `  




#### `DeleteDataset`

  * **Method** : `google.cloud.financialservices.v1.AML.DeleteDataset`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `financialservices.v1datasets.delete - DATA_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.financialservices.v1.AML.DeleteDataset" `  




#### `DeleteEngineConfig`

  * **Method** : `google.cloud.financialservices.v1.AML.DeleteEngineConfig`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `financialservices.v1engineconfigs.delete - DATA_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.financialservices.v1.AML.DeleteEngineConfig" `  




#### `DeleteInstance`

  * **Method** : `google.cloud.financialservices.v1.AML.DeleteInstance`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `financialservices.v1instances.delete - DATA_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.financialservices.v1.AML.DeleteInstance" `  




#### `DeleteModel`

  * **Method** : `google.cloud.financialservices.v1.AML.DeleteModel`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `financialservices.v1models.delete - DATA_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.financialservices.v1.AML.DeleteModel" `  




#### `DeletePredictionResult`

  * **Method** : `google.cloud.financialservices.v1.AML.DeletePredictionResult`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `financialservices.v1predictions.delete - DATA_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.financialservices.v1.AML.DeletePredictionResult" `  




#### `ExportBacktestResultMetadata`

  * **Method** : `google.cloud.financialservices.v1.AML.ExportBacktestResultMetadata`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `financialservices.v1backtests.exportMetadata - DATA_READ`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.financialservices.v1.AML.ExportBacktestResultMetadata" `  




#### `ExportEngineConfigMetadata`

  * **Method** : `google.cloud.financialservices.v1.AML.ExportEngineConfigMetadata`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `financialservices.v1engineconfigs.exportMetadata - DATA_READ`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.financialservices.v1.AML.ExportEngineConfigMetadata" `  




#### `ExportModelMetadata`

  * **Method** : `google.cloud.financialservices.v1.AML.ExportModelMetadata`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `financialservices.v1models.exportMetadata - DATA_READ`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.financialservices.v1.AML.ExportModelMetadata" `  




#### `ExportPredictionResultMetadata`

  * **Method** : `google.cloud.financialservices.v1.AML.ExportPredictionResultMetadata`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `financialservices.v1predictions.exportMetadata - DATA_READ`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.financialservices.v1.AML.ExportPredictionResultMetadata" `  




#### `ExportRegisteredParties`

  * **Method** : `google.cloud.financialservices.v1.AML.ExportRegisteredParties`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `financialservices.v1instances.exportRegisteredParties - DATA_READ`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.financialservices.v1.AML.ExportRegisteredParties" `  




#### `GetBacktestResult`

  * **Method** : `google.cloud.financialservices.v1.AML.GetBacktestResult`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `financialservices.v1backtests.get - DATA_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.financialservices.v1.AML.GetBacktestResult" `  




#### `GetDataset`

  * **Method** : `google.cloud.financialservices.v1.AML.GetDataset`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `financialservices.v1datasets.get - DATA_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.financialservices.v1.AML.GetDataset" `  




#### `GetEngineConfig`

  * **Method** : `google.cloud.financialservices.v1.AML.GetEngineConfig`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `financialservices.v1engineconfigs.get - DATA_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.financialservices.v1.AML.GetEngineConfig" `  




#### `GetEngineVersion`

  * **Method** : `google.cloud.financialservices.v1.AML.GetEngineVersion`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `financialservices.v1engineversions.get - DATA_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.financialservices.v1.AML.GetEngineVersion" `  




#### `GetInstance`

  * **Method** : `google.cloud.financialservices.v1.AML.GetInstance`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `financialservices.v1instances.get - DATA_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.financialservices.v1.AML.GetInstance" `  




#### `GetModel`

  * **Method** : `google.cloud.financialservices.v1.AML.GetModel`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `financialservices.v1models.get - DATA_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.financialservices.v1.AML.GetModel" `  




#### `GetPredictionResult`

  * **Method** : `google.cloud.financialservices.v1.AML.GetPredictionResult`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `financialservices.v1predictions.get - DATA_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.financialservices.v1.AML.GetPredictionResult" `  




#### `ImportRegisteredParties`

  * **Method** : `google.cloud.financialservices.v1.AML.ImportRegisteredParties`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `financialservices.v1instances.importRegisteredParties - DATA_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.financialservices.v1.AML.ImportRegisteredParties" `  




#### `ListBacktestResults`

  * **Method** : `google.cloud.financialservices.v1.AML.ListBacktestResults`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `financialservices.v1backtests.list - DATA_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.financialservices.v1.AML.ListBacktestResults" `  




#### `ListDatasets`

  * **Method** : `google.cloud.financialservices.v1.AML.ListDatasets`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `financialservices.v1datasets.list - DATA_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.financialservices.v1.AML.ListDatasets" `  




#### `ListEngineConfigs`

  * **Method** : `google.cloud.financialservices.v1.AML.ListEngineConfigs`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `financialservices.v1engineconfigs.list - DATA_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.financialservices.v1.AML.ListEngineConfigs" `  




#### `ListEngineVersions`

  * **Method** : `google.cloud.financialservices.v1.AML.ListEngineVersions`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `financialservices.v1engineversions.list - DATA_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.financialservices.v1.AML.ListEngineVersions" `  




#### `ListInstances`

  * **Method** : `google.cloud.financialservices.v1.AML.ListInstances`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `financialservices.v1instances.list - DATA_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.financialservices.v1.AML.ListInstances" `  




#### `ListModels`

  * **Method** : `google.cloud.financialservices.v1.AML.ListModels`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `financialservices.v1models.list - DATA_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.financialservices.v1.AML.ListModels" `  




#### `ListPredictionResults`

  * **Method** : `google.cloud.financialservices.v1.AML.ListPredictionResults`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `financialservices.v1predictions.list - DATA_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.financialservices.v1.AML.ListPredictionResults" `  




#### `UpdateDataset`

  * **Method** : `google.cloud.financialservices.v1.AML.UpdateDataset`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `financialservices.v1datasets.update - DATA_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.financialservices.v1.AML.UpdateDataset" `  




#### `UpdateInstance`

  * **Method** : `google.cloud.financialservices.v1.AML.UpdateInstance`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `financialservices.v1instances.update - DATA_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.financialservices.v1.AML.UpdateInstance" `  




### `google.cloud.financialservices.v1alpha.AML`

The following audit logs are associated with methods belonging to `google.cloud.financialservices.v1alpha.AML`.

#### `CreateBacktestResult`

  * **Method** : `google.cloud.financialservices.v1alpha.AML.CreateBacktestResult`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `financialservices.v1backtests.create - DATA_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.financialservices.v1alpha.AML.CreateBacktestResult" `  




#### `CreateDataset`

  * **Method** : `google.cloud.financialservices.v1alpha.AML.CreateDataset`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `financialservices.v1datasets.create - DATA_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.financialservices.v1alpha.AML.CreateDataset" `  




#### `CreateEngineConfig`

  * **Method** : `google.cloud.financialservices.v1alpha.AML.CreateEngineConfig`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `financialservices.v1engineconfigs.create - DATA_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.financialservices.v1alpha.AML.CreateEngineConfig" `  




#### `CreateInstance`

  * **Method** : `google.cloud.financialservices.v1alpha.AML.CreateInstance`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `financialservices.v1instances.create - DATA_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.financialservices.v1alpha.AML.CreateInstance" `  




#### `CreateModel`

  * **Method** : `google.cloud.financialservices.v1alpha.AML.CreateModel`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `financialservices.v1models.create - DATA_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.financialservices.v1alpha.AML.CreateModel" `  




#### `CreatePredictionResult`

  * **Method** : `google.cloud.financialservices.v1alpha.AML.CreatePredictionResult`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `financialservices.v1predictions.create - DATA_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.financialservices.v1alpha.AML.CreatePredictionResult" `  




#### `DeleteBacktestResult`

  * **Method** : `google.cloud.financialservices.v1alpha.AML.DeleteBacktestResult`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `financialservices.v1backtests.delete - DATA_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.financialservices.v1alpha.AML.DeleteBacktestResult" `  




#### `DeleteDataset`

  * **Method** : `google.cloud.financialservices.v1alpha.AML.DeleteDataset`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `financialservices.v1datasets.delete - DATA_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.financialservices.v1alpha.AML.DeleteDataset" `  




#### `DeleteEngineConfig`

  * **Method** : `google.cloud.financialservices.v1alpha.AML.DeleteEngineConfig`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `financialservices.v1engineconfigs.delete - DATA_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.financialservices.v1alpha.AML.DeleteEngineConfig" `  




#### `DeleteInstance`

  * **Method** : `google.cloud.financialservices.v1alpha.AML.DeleteInstance`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `financialservices.v1instances.delete - DATA_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.financialservices.v1alpha.AML.DeleteInstance" `  




#### `DeleteModel`

  * **Method** : `google.cloud.financialservices.v1alpha.AML.DeleteModel`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `financialservices.v1models.delete - DATA_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.financialservices.v1alpha.AML.DeleteModel" `  




#### `DeletePredictionResult`

  * **Method** : `google.cloud.financialservices.v1alpha.AML.DeletePredictionResult`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `financialservices.v1predictions.delete - DATA_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.financialservices.v1alpha.AML.DeletePredictionResult" `  




#### `ExportBacktestResultMetadata`

  * **Method** : `google.cloud.financialservices.v1alpha.AML.ExportBacktestResultMetadata`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `financialservices.v1backtests.exportMetadata - DATA_READ`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.financialservices.v1alpha.AML.ExportBacktestResultMetadata" `  




#### `ExportEngineConfigMetadata`

  * **Method** : `google.cloud.financialservices.v1alpha.AML.ExportEngineConfigMetadata`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `financialservices.v1engineconfigs.exportMetadata - DATA_READ`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.financialservices.v1alpha.AML.ExportEngineConfigMetadata" `  




#### `ExportModelMetadata`

  * **Method** : `google.cloud.financialservices.v1alpha.AML.ExportModelMetadata`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `financialservices.v1models.exportMetadata - DATA_READ`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.financialservices.v1alpha.AML.ExportModelMetadata" `  




#### `ExportPredictionResultMetadata`

  * **Method** : `google.cloud.financialservices.v1alpha.AML.ExportPredictionResultMetadata`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `financialservices.v1predictions.exportMetadata - DATA_READ`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.financialservices.v1alpha.AML.ExportPredictionResultMetadata" `  




#### `ExportRegisteredParties`

  * **Method** : `google.cloud.financialservices.v1alpha.AML.ExportRegisteredParties`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `financialservices.v1instances.exportRegisteredParties - DATA_READ`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.financialservices.v1alpha.AML.ExportRegisteredParties" `  




#### `GetBacktestResult`

  * **Method** : `google.cloud.financialservices.v1alpha.AML.GetBacktestResult`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `financialservices.v1backtests.get - DATA_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.financialservices.v1alpha.AML.GetBacktestResult" `  




#### `GetDataset`

  * **Method** : `google.cloud.financialservices.v1alpha.AML.GetDataset`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `financialservices.v1datasets.get - DATA_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.financialservices.v1alpha.AML.GetDataset" `  




#### `GetEngineConfig`

  * **Method** : `google.cloud.financialservices.v1alpha.AML.GetEngineConfig`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `financialservices.v1engineconfigs.get - DATA_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.financialservices.v1alpha.AML.GetEngineConfig" `  




#### `GetEngineVersion`

  * **Method** : `google.cloud.financialservices.v1alpha.AML.GetEngineVersion`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `financialservices.v1engineversions.get - DATA_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.financialservices.v1alpha.AML.GetEngineVersion" `  




#### `GetInstance`

  * **Method** : `google.cloud.financialservices.v1alpha.AML.GetInstance`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `financialservices.v1instances.get - DATA_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.financialservices.v1alpha.AML.GetInstance" `  




#### `GetModel`

  * **Method** : `google.cloud.financialservices.v1alpha.AML.GetModel`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `financialservices.v1models.get - DATA_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.financialservices.v1alpha.AML.GetModel" `  




#### `GetPredictionResult`

  * **Method** : `google.cloud.financialservices.v1alpha.AML.GetPredictionResult`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `financialservices.v1predictions.get - DATA_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.financialservices.v1alpha.AML.GetPredictionResult" `  




#### `ImportRegisteredParties`

  * **Method** : `google.cloud.financialservices.v1alpha.AML.ImportRegisteredParties`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `financialservices.v1instances.importRegisteredParties - DATA_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.financialservices.v1alpha.AML.ImportRegisteredParties" `  




#### `ListBacktestResults`

  * **Method** : `google.cloud.financialservices.v1alpha.AML.ListBacktestResults`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `financialservices.v1backtests.list - DATA_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.financialservices.v1alpha.AML.ListBacktestResults" `  




#### `ListDatasets`

  * **Method** : `google.cloud.financialservices.v1alpha.AML.ListDatasets`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `financialservices.v1datasets.list - DATA_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.financialservices.v1alpha.AML.ListDatasets" `  




#### `ListEngineConfigs`

  * **Method** : `google.cloud.financialservices.v1alpha.AML.ListEngineConfigs`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `financialservices.v1engineconfigs.list - DATA_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.financialservices.v1alpha.AML.ListEngineConfigs" `  




#### `ListEngineVersions`

  * **Method** : `google.cloud.financialservices.v1alpha.AML.ListEngineVersions`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `financialservices.v1engineversions.list - DATA_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.financialservices.v1alpha.AML.ListEngineVersions" `  




#### `ListInstances`

  * **Method** : `google.cloud.financialservices.v1alpha.AML.ListInstances`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `financialservices.v1instances.list - DATA_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.financialservices.v1alpha.AML.ListInstances" `  




#### `ListModels`

  * **Method** : `google.cloud.financialservices.v1alpha.AML.ListModels`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `financialservices.v1models.list - DATA_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.financialservices.v1alpha.AML.ListModels" `  




#### `ListPredictionResults`

  * **Method** : `google.cloud.financialservices.v1alpha.AML.ListPredictionResults`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `financialservices.v1predictions.list - DATA_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.financialservices.v1alpha.AML.ListPredictionResults" `  




#### `UpdateBacktestResult`

  * **Method** : `google.cloud.financialservices.v1alpha.AML.UpdateBacktestResult`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `financialservices.v1backtests.update - DATA_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.financialservices.v1alpha.AML.UpdateBacktestResult" `  




#### `UpdateDataset`

  * **Method** : `google.cloud.financialservices.v1alpha.AML.UpdateDataset`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `financialservices.v1datasets.update - DATA_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.financialservices.v1alpha.AML.UpdateDataset" `  




#### `UpdateEngineConfig`

  * **Method** : `google.cloud.financialservices.v1alpha.AML.UpdateEngineConfig`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `financialservices.v1engineconfigs.update - DATA_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.financialservices.v1alpha.AML.UpdateEngineConfig" `  




#### `UpdateInstance`

  * **Method** : `google.cloud.financialservices.v1alpha.AML.UpdateInstance`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `financialservices.v1instances.update - DATA_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.financialservices.v1alpha.AML.UpdateInstance" `  




#### `UpdateModel`

  * **Method** : `google.cloud.financialservices.v1alpha.AML.UpdateModel`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `financialservices.v1models.update - DATA_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.financialservices.v1alpha.AML.UpdateModel" `  




#### `UpdatePredictionResult`

  * **Method** : `google.cloud.financialservices.v1alpha.AML.UpdatePredictionResult`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `financialservices.v1predictions.update - DATA_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.financialservices.v1alpha.AML.UpdatePredictionResult" `  




### `google.longrunning.Operations`

The following audit logs are associated with methods belonging to `google.longrunning.Operations`.

#### `CancelOperation`

  * **Method** : `google.longrunning.Operations.CancelOperation`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `financialservices.operations.cancel - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.longrunning.Operations.CancelOperation" `  




#### `DeleteOperation`

  * **Method** : `google.longrunning.Operations.DeleteOperation`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `financialservices.operations.delete - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.longrunning.Operations.DeleteOperation" `  




#### `GetOperation`

  * **Method** : `google.longrunning.Operations.GetOperation`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `financialservices.operations.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.longrunning.Operations.GetOperation" `  




#### `ListOperations`

  * **Method** : `google.longrunning.Operations.ListOperations`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `financialservices.operations.list - ADMIN_READ`
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

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
