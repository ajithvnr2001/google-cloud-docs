---
url: https://docs.cloud.google.com/compute/docs/instances/windows/lima-audit-logging/
title: Compute Engine audit logging \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T08:21:47.902174+00:00
---

# Compute Engine audit logging  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/compute/docs/instances/windows/lima-audit-logging/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ Compute Engine ](https://docs.cloud.google.com/compute/docs)
  * [ Guides ](https://docs.cloud.google.com/compute/docs/overview)



Send feedback 

#  Compute Engine audit logging Stay organized with collections  Save and categorize content based on your preferences. 

This document describes audit logging for License Manager. Google Cloud services generate audit logs that record administrative and access activities within your Google Cloud resources. For more information about Cloud Audit Logs, see the following: 

  * [Types of audit logs](https://docs.cloud.google.com/logging/docs/audit#types)
  * [Audit log entry structure](https://docs.cloud.google.com/logging/docs/audit#audit_log_entry_structure)
  * [Storing and routing audit logs](https://docs.cloud.google.com/logging/docs/audit#storing_and_routing_audit_logs)
  * [Cloud Logging pricing summary](https://docs.cloud.google.com/stackdriver/pricing#logs-pricing-summary)
  * [Enable Data Access audit logs](https://docs.cloud.google.com/logging/docs/audit/configure-data-access)



## Service name

License Manager audit logs use the service name `licensemanager.googleapis.com`. Filter for this service: 
    
    
        protoPayload.serviceName="licensemanager.googleapis.com"
      

## Methods by permission type

Each IAM permission has a `type` property, whose value is an enum that can be one of four values: `ADMIN_READ`, `ADMIN_WRITE`, `DATA_READ`, or `DATA_WRITE`. When you call a method, License Manager generates an audit log whose category is dependent on the `type` property of the permission required to perform the method. Methods that require an IAM permission with the `type` property value of `DATA_READ`, `DATA_WRITE`, or `ADMIN_READ` generate [Data Access](https://docs.cloud.google.com/logging/docs/audit#data-access) audit logs. Methods that require an IAM permission with the `type` property value of `ADMIN_WRITE` generate [Admin Activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity) audit logs.

API methods in the following list that are marked with (LRO) are long-running operations (LROs). These methods usually generate two audit log entries: one when the operation starts and another when it ends. For more information see [Audit logs for long-running operations](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro). Permission type | Methods  
---|---  
`DATA_READ` | `google.cloud.licensemanager.v1.LicenseManager.AggregateUsage`  
`google.cloud.licensemanager.v1.LicenseManager.GetConfiguration`  
`google.cloud.licensemanager.v1.LicenseManager.GetInstance`  
`google.cloud.licensemanager.v1.LicenseManager.GetProduct`  
`google.cloud.licensemanager.v1.LicenseManager.ListConfigurations`  
`google.cloud.licensemanager.v1.LicenseManager.ListInstances`  
`google.cloud.licensemanager.v1.LicenseManager.ListProducts`  
`google.cloud.licensemanager.v1.LicenseManager.QueryConfigurationLicenseUsage`  
`google.cloud.licensemanager.v1alpha.LicenseManager.AggregateUsage`  
`google.cloud.licensemanager.v1alpha.LicenseManager.GetConfiguration`  
`google.cloud.licensemanager.v1alpha.LicenseManager.GetInstance`  
`google.cloud.licensemanager.v1alpha.LicenseManager.GetProduct`  
`google.cloud.licensemanager.v1alpha.LicenseManager.ListConfigurations`  
`google.cloud.licensemanager.v1alpha.LicenseManager.ListInstances`  
`google.cloud.licensemanager.v1alpha.LicenseManager.ListProducts`  
`google.cloud.licensemanager.v1alpha.LicenseManager.QueryConfigurationLicenseUsage`  
`DATA_WRITE` | `google.cloud.licensemanager.v1.LicenseManager.CreateConfiguration` (LRO)  
`google.cloud.licensemanager.v1.LicenseManager.DeactivateConfiguration` (LRO)  
`google.cloud.licensemanager.v1.LicenseManager.DeleteConfiguration` (LRO)  
`google.cloud.licensemanager.v1.LicenseManager.ReactivateConfiguration` (LRO)  
`google.cloud.licensemanager.v1.LicenseManager.UpdateConfiguration` (LRO)  
`google.cloud.licensemanager.v1alpha.LicenseManager.CreateConfiguration` (LRO)  
`google.cloud.licensemanager.v1alpha.LicenseManager.DeactivateConfiguration` (LRO)  
`google.cloud.licensemanager.v1alpha.LicenseManager.DeleteConfiguration` (LRO)  
`google.cloud.licensemanager.v1alpha.LicenseManager.ReactivateConfiguration` (LRO)  
`google.cloud.licensemanager.v1alpha.LicenseManager.UpdateConfiguration` (LRO)  
  
## API interface audit logs

For information about how and which permissions are evaluated for each method, see the Identity and Access Management documentation for License Manager.

### `google.cloud.licensemanager.v1.LicenseManager`

The following audit logs are associated with methods belonging to `google.cloud.licensemanager.v1.LicenseManager`.

#### `AggregateUsage`

  * **Method** : `google.cloud.licensemanager.v1.LicenseManager.AggregateUsage`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `licensemanager.configurations.aggregateUsage - DATA_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.licensemanager.v1.LicenseManager.AggregateUsage" `  




#### `CreateConfiguration`

  * **Method** : `google.cloud.licensemanager.v1.LicenseManager.CreateConfiguration`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `licensemanager.configurations.create - DATA_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.licensemanager.v1.LicenseManager.CreateConfiguration" `  




#### `DeactivateConfiguration`

  * **Method** : `google.cloud.licensemanager.v1.LicenseManager.DeactivateConfiguration`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `licensemanager.configurations.update - DATA_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.licensemanager.v1.LicenseManager.DeactivateConfiguration" `  




#### `DeleteConfiguration`

  * **Method** : `google.cloud.licensemanager.v1.LicenseManager.DeleteConfiguration`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `licensemanager.configurations.delete - DATA_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.licensemanager.v1.LicenseManager.DeleteConfiguration" `  




#### `GetConfiguration`

  * **Method** : `google.cloud.licensemanager.v1.LicenseManager.GetConfiguration`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `licensemanager.configurations.get - DATA_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.licensemanager.v1.LicenseManager.GetConfiguration" `  




#### `GetInstance`

  * **Method** : `google.cloud.licensemanager.v1.LicenseManager.GetInstance`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `licensemanager.instances.get - DATA_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.licensemanager.v1.LicenseManager.GetInstance" `  




#### `GetProduct`

  * **Method** : `google.cloud.licensemanager.v1.LicenseManager.GetProduct`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `licensemanager.products.get - DATA_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.licensemanager.v1.LicenseManager.GetProduct" `  




#### `ListConfigurations`

  * **Method** : `google.cloud.licensemanager.v1.LicenseManager.ListConfigurations`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `licensemanager.configurations.list - DATA_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.licensemanager.v1.LicenseManager.ListConfigurations" `  




#### `ListInstances`

  * **Method** : `google.cloud.licensemanager.v1.LicenseManager.ListInstances`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `licensemanager.instances.list - DATA_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.licensemanager.v1.LicenseManager.ListInstances" `  




#### `ListProducts`

  * **Method** : `google.cloud.licensemanager.v1.LicenseManager.ListProducts`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `licensemanager.products.list - DATA_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.licensemanager.v1.LicenseManager.ListProducts" `  




#### `QueryConfigurationLicenseUsage`

  * **Method** : `google.cloud.licensemanager.v1.LicenseManager.QueryConfigurationLicenseUsage`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `licensemanager.configurations.queryLicenseUsage - DATA_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.licensemanager.v1.LicenseManager.QueryConfigurationLicenseUsage" `  




#### `ReactivateConfiguration`

  * **Method** : `google.cloud.licensemanager.v1.LicenseManager.ReactivateConfiguration`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `licensemanager.configurations.update - DATA_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.licensemanager.v1.LicenseManager.ReactivateConfiguration" `  




#### `UpdateConfiguration`

  * **Method** : `google.cloud.licensemanager.v1.LicenseManager.UpdateConfiguration`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `licensemanager.configurations.update - DATA_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.licensemanager.v1.LicenseManager.UpdateConfiguration" `  




### `google.cloud.licensemanager.v1alpha.LicenseManager`

The following audit logs are associated with methods belonging to `google.cloud.licensemanager.v1alpha.LicenseManager`.

#### `AggregateUsage`

  * **Method** : `google.cloud.licensemanager.v1alpha.LicenseManager.AggregateUsage`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `licensemanager.configurations.aggregateUsage - DATA_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.licensemanager.v1alpha.LicenseManager.AggregateUsage" `  




#### `CreateConfiguration`

  * **Method** : `google.cloud.licensemanager.v1alpha.LicenseManager.CreateConfiguration`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `licensemanager.configurations.create - DATA_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.licensemanager.v1alpha.LicenseManager.CreateConfiguration" `  




#### `DeactivateConfiguration`

  * **Method** : `google.cloud.licensemanager.v1alpha.LicenseManager.DeactivateConfiguration`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `licensemanager.configurations.update - DATA_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.licensemanager.v1alpha.LicenseManager.DeactivateConfiguration" `  




#### `DeleteConfiguration`

  * **Method** : `google.cloud.licensemanager.v1alpha.LicenseManager.DeleteConfiguration`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `licensemanager.configurations.delete - DATA_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.licensemanager.v1alpha.LicenseManager.DeleteConfiguration" `  




#### `GetConfiguration`

  * **Method** : `google.cloud.licensemanager.v1alpha.LicenseManager.GetConfiguration`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `licensemanager.configurations.get - DATA_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.licensemanager.v1alpha.LicenseManager.GetConfiguration" `  




#### `GetInstance`

  * **Method** : `google.cloud.licensemanager.v1alpha.LicenseManager.GetInstance`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `licensemanager.instances.get - DATA_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.licensemanager.v1alpha.LicenseManager.GetInstance" `  




#### `GetProduct`

  * **Method** : `google.cloud.licensemanager.v1alpha.LicenseManager.GetProduct`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `licensemanager.products.get - DATA_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.licensemanager.v1alpha.LicenseManager.GetProduct" `  




#### `ListConfigurations`

  * **Method** : `google.cloud.licensemanager.v1alpha.LicenseManager.ListConfigurations`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `licensemanager.configurations.list - DATA_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.licensemanager.v1alpha.LicenseManager.ListConfigurations" `  




#### `ListInstances`

  * **Method** : `google.cloud.licensemanager.v1alpha.LicenseManager.ListInstances`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `licensemanager.instances.list - DATA_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.licensemanager.v1alpha.LicenseManager.ListInstances" `  




#### `ListProducts`

  * **Method** : `google.cloud.licensemanager.v1alpha.LicenseManager.ListProducts`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `licensemanager.products.list - DATA_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.licensemanager.v1alpha.LicenseManager.ListProducts" `  




#### `QueryConfigurationLicenseUsage`

  * **Method** : `google.cloud.licensemanager.v1alpha.LicenseManager.QueryConfigurationLicenseUsage`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `licensemanager.configurations.queryLicenseUsage - DATA_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.licensemanager.v1alpha.LicenseManager.QueryConfigurationLicenseUsage" `  




#### `ReactivateConfiguration`

  * **Method** : `google.cloud.licensemanager.v1alpha.LicenseManager.ReactivateConfiguration`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `licensemanager.configurations.update - DATA_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.licensemanager.v1alpha.LicenseManager.ReactivateConfiguration" `  




#### `UpdateConfiguration`

  * **Method** : `google.cloud.licensemanager.v1alpha.LicenseManager.UpdateConfiguration`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `licensemanager.configurations.update - DATA_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.licensemanager.v1alpha.LicenseManager.UpdateConfiguration" `  




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
