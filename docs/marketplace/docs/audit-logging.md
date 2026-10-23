---
url: https://docs.cloud.google.com/marketplace/docs/audit-logging/
title: Cloud Commerce Consumer Procurement API audit logging \u00a0|\u00a0 Google Cloud Marketplace \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:46:23.067945+00:00
---

# Cloud Commerce Consumer Procurement API audit logging  |  Google Cloud Marketplace  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/marketplace/docs/audit-logging/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Access and resource management ](https://docs.cloud.google.com/docs/access-resources)
  * [ Google Cloud Marketplace ](https://docs.cloud.google.com/marketplace/docs)
  * [ Guides ](https://docs.cloud.google.com/marketplace/docs/overview)



Send feedback 

#  Cloud Commerce Consumer Procurement API audit logging Stay organized with collections  Save and categorize content based on your preferences. 

This document describes audit logging for Cloud Commerce Consumer Procurement API. Google Cloud services generate audit logs that record administrative and access activities within your Google Cloud resources. For more information about Cloud Audit Logs, see the following: 

  * [Types of audit logs](https://docs.cloud.google.com/logging/docs/audit#types)
  * [Audit log entry structure](https://docs.cloud.google.com/logging/docs/audit#audit_log_entry_structure)
  * [Storing and routing audit logs](https://docs.cloud.google.com/logging/docs/audit#storing_and_routing_audit_logs)
  * [Cloud Logging pricing summary](https://docs.cloud.google.com/stackdriver/pricing#logs-pricing-summary)
  * [Enable Data Access audit logs](https://docs.cloud.google.com/logging/docs/audit/configure-data-access)



## Service name

Cloud Commerce Consumer Procurement API audit logs use the service name `cloudcommerceconsumerprocurement.googleapis.com`. Filter for this service: 
    
    
        protoPayload.serviceName="cloudcommerceconsumerprocurement.googleapis.com"
      

## Methods by permission type

Each IAM permission has a `type` property, whose value is an enum that can be one of four values: `ADMIN_READ`, `ADMIN_WRITE`, `DATA_READ`, or `DATA_WRITE`. When you call a method, Cloud Commerce Consumer Procurement API generates an audit log whose category is dependent on the `type` property of the permission required to perform the method. Methods that require an IAM permission with the `type` property value of `DATA_READ`, `DATA_WRITE`, or `ADMIN_READ` generate [Data Access](https://docs.cloud.google.com/logging/docs/audit#data-access) audit logs. Methods that require an IAM permission with the `type` property value of `ADMIN_WRITE` generate [Admin Activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity) audit logs.

Permission type | Methods  
---|---  
`ADMIN_READ` | `google.cloud.commerce.consumer.procurement.v1.ConsumerProcurementService.GetOrder`  
`google.cloud.commerce.consumer.procurement.v1.ConsumerProcurementService.ListOrders`  
`google.cloud.commerce.consumer.procurement.v1.LicenseManagementService.EnumerateLicensedUsers`  
`google.cloud.commerce.consumer.procurement.v1.LicenseManagementService.GetLicensePool`  
`google.cloud.commerce.consumer.procurement.v1alpha1.ConsumerProcurementService.GetOrder`  
`google.cloud.commerce.consumer.procurement.v1alpha1.ConsumerProcurementService.ListOrders`  
`ADMIN_WRITE` | `google.cloud.commerce.consumer.procurement.v1.ConsumerProcurementService.CancelOrder`  
`google.cloud.commerce.consumer.procurement.v1.ConsumerProcurementService.ModifyOrder`  
`google.cloud.commerce.consumer.procurement.v1.ConsumerProcurementService.PlaceOrder`  
`google.cloud.commerce.consumer.procurement.v1.LicenseManagementService.Assign`  
`google.cloud.commerce.consumer.procurement.v1.LicenseManagementService.Unassign`  
`google.cloud.commerce.consumer.procurement.v1alpha1.ConsumerProcurementService.PlaceOrder`  
  
## API interface audit logs

For information about how and which permissions are evaluated for each method, see the Identity and Access Management documentation for Cloud Commerce Consumer Procurement API.

### `google.cloud.commerce.consumer.procurement.v1.ConsumerProcurementService`

The following audit logs are associated with methods belonging to `google.cloud.commerce.consumer.procurement.v1.ConsumerProcurementService`.

#### `CancelOrder`

  * **Method** : `google.cloud.commerce.consumer.procurement.v1.ConsumerProcurementService.CancelOrder`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `consumerprocurement.orders.cancel - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.commerce.consumer.procurement.v1.ConsumerProcurementService.CancelOrder" `  




#### `GetOrder`

  * **Method** : `google.cloud.commerce.consumer.procurement.v1.ConsumerProcurementService.GetOrder`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `consumerprocurement.orders.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.commerce.consumer.procurement.v1.ConsumerProcurementService.GetOrder" `  




#### `ListOrders`

  * **Method** : `google.cloud.commerce.consumer.procurement.v1.ConsumerProcurementService.ListOrders`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `consumerprocurement.orders.list - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.commerce.consumer.procurement.v1.ConsumerProcurementService.ListOrders" `  




#### `ModifyOrder`

  * **Method** : `google.cloud.commerce.consumer.procurement.v1.ConsumerProcurementService.ModifyOrder`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `consumerprocurement.orders.modify - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.commerce.consumer.procurement.v1.ConsumerProcurementService.ModifyOrder" `  




#### `PlaceOrder`

  * **Method** : `google.cloud.commerce.consumer.procurement.v1.ConsumerProcurementService.PlaceOrder`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `consumerprocurement.orders.place - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.commerce.consumer.procurement.v1.ConsumerProcurementService.PlaceOrder" `  




### `google.cloud.commerce.consumer.procurement.v1.LicenseManagementService`

The following audit logs are associated with methods belonging to `google.cloud.commerce.consumer.procurement.v1.LicenseManagementService`.

#### `Assign`

  * **Method** : `google.cloud.commerce.consumer.procurement.v1.LicenseManagementService.Assign`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `consumerprocurement.licensePools.assign - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.commerce.consumer.procurement.v1.LicenseManagementService.Assign" `  




#### `EnumerateLicensedUsers`

  * **Method** : `google.cloud.commerce.consumer.procurement.v1.LicenseManagementService.EnumerateLicensedUsers`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `consumerprocurement.licensePools.enumerateLicensedUsers - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.commerce.consumer.procurement.v1.LicenseManagementService.EnumerateLicensedUsers" `  




#### `GetLicensePool`

  * **Method** : `google.cloud.commerce.consumer.procurement.v1.LicenseManagementService.GetLicensePool`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `consumerprocurement.licensePools.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.commerce.consumer.procurement.v1.LicenseManagementService.GetLicensePool" `  




#### `Unassign`

  * **Method** : `google.cloud.commerce.consumer.procurement.v1.LicenseManagementService.Unassign`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `consumerprocurement.licensePools.unassign - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.commerce.consumer.procurement.v1.LicenseManagementService.Unassign" `  




### `google.cloud.commerce.consumer.procurement.v1alpha1.ConsumerProcurementService`

The following audit logs are associated with methods belonging to `google.cloud.commerce.consumer.procurement.v1alpha1.ConsumerProcurementService`.

#### `GetOrder`

  * **Method** : `google.cloud.commerce.consumer.procurement.v1alpha1.ConsumerProcurementService.GetOrder`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `consumerprocurement.orders.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.commerce.consumer.procurement.v1alpha1.ConsumerProcurementService.GetOrder" `  




#### `ListOrders`

  * **Method** : `google.cloud.commerce.consumer.procurement.v1alpha1.ConsumerProcurementService.ListOrders`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `consumerprocurement.orders.list - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.commerce.consumer.procurement.v1alpha1.ConsumerProcurementService.ListOrders" `  




#### `PlaceOrder`

  * **Method** : `google.cloud.commerce.consumer.procurement.v1alpha1.ConsumerProcurementService.PlaceOrder`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `consumerprocurement.orders.place - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.commerce.consumer.procurement.v1alpha1.ConsumerProcurementService.PlaceOrder" `  




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
