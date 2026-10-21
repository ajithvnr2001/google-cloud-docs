---
url: https://docs.cloud.google.com/transfer-appliance/docs/4.0/audit-logging/
title: Transfer Appliance audit logging \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T03:26:11.604984+00:00
---

# Transfer Appliance audit logging  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/transfer-appliance/docs/4.0/audit-logging/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Storage ](https://docs.cloud.google.com/docs/storage)
  * [ Transfer Appliance ](https://docs.cloud.google.com/transfer-appliance/docs)
  * [ Resources ](https://docs.cloud.google.com/transfer-appliance/docs/4.0/resources)



Send feedback 

#  Transfer Appliance audit logging Stay organized with collections  Save and categorize content based on your preferences. 

This document describes audit logging for Transfer Appliance. Google Cloud services generate audit logs that record administrative and access activities within your Google Cloud resources. For more information about Cloud Audit Logs, see the following: 

  * [Types of audit logs](https://docs.cloud.google.com/logging/docs/audit#types)
  * [Audit log entry structure](https://docs.cloud.google.com/logging/docs/audit#audit_log_entry_structure)
  * [Storing and routing audit logs](https://docs.cloud.google.com/logging/docs/audit#storing_and_routing_audit_logs)
  * [Cloud Logging pricing summary](https://docs.cloud.google.com/stackdriver/pricing#logs-pricing-summary)
  * [Enable Data Access audit logs](https://docs.cloud.google.com/logging/docs/audit/configure-data-access)



## Service name

Transfer Appliance audit logs use the service name `transferappliance.googleapis.com`. Filter for this service: 
    
    
        protoPayload.serviceName="transferappliance.googleapis.com"
      

## Methods by permission type

Each IAM permission has a `type` property, whose value is an enum that can be one of four values: `ADMIN_READ`, `ADMIN_WRITE`, `DATA_READ`, or `DATA_WRITE`. When you call a method, Transfer Appliance generates an audit log whose category is dependent on the `type` property of the permission required to perform the method. Methods that require an IAM permission with the `type` property value of `DATA_READ`, `DATA_WRITE`, or `ADMIN_READ` generate [Data Access](https://docs.cloud.google.com/logging/docs/audit#data-access) audit logs. Methods that require an IAM permission with the `type` property value of `ADMIN_WRITE` generate [Admin Activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity) audit logs.

Permission type | Methods  
---|---  
`ADMIN_READ` | `cloud.transfer.appliance.ccfe.api.v1alpha1.TransferAppliance.ExportApplianceUserData`  
`cloud.transfer.appliance.ccfe.api.v1alpha1.TransferAppliance.GetAppliance`  
`cloud.transfer.appliance.ccfe.api.v1alpha1.TransferAppliance.GetCredential`  
`cloud.transfer.appliance.ccfe.api.v1alpha1.TransferAppliance.GetCredentialMetadata`  
`cloud.transfer.appliance.ccfe.api.v1alpha1.TransferAppliance.GetDownloadLinks`  
`cloud.transfer.appliance.ccfe.api.v1alpha1.TransferAppliance.GetOrder`  
`cloud.transfer.appliance.ccfe.api.v1alpha1.TransferAppliance.GetSavedAddress`  
`cloud.transfer.appliance.ccfe.api.v1alpha1.TransferAppliance.ListAppliances`  
`cloud.transfer.appliance.ccfe.api.v1alpha1.TransferAppliance.ListOrders`  
`cloud.transfer.appliance.ccfe.api.v1alpha1.TransferAppliance.ListSavedAddresses`  
`ADMIN_WRITE` | `cloud.transfer.appliance.ccfe.api.v1alpha1.TransferAppliance.CreateAppliance`  
`cloud.transfer.appliance.ccfe.api.v1alpha1.TransferAppliance.CreateOrder`  
`cloud.transfer.appliance.ccfe.api.v1alpha1.TransferAppliance.CreateSavedAddress`  
`cloud.transfer.appliance.ccfe.api.v1alpha1.TransferAppliance.DeleteAppliance`  
`cloud.transfer.appliance.ccfe.api.v1alpha1.TransferAppliance.DeleteOrder`  
`cloud.transfer.appliance.ccfe.api.v1alpha1.TransferAppliance.DeleteSavedAddress`  
`cloud.transfer.appliance.ccfe.api.v1alpha1.TransferAppliance.SubmitOrder`  
`cloud.transfer.appliance.ccfe.api.v1alpha1.TransferAppliance.UpdateAppliance`  
`cloud.transfer.appliance.ccfe.api.v1alpha1.TransferAppliance.UpdateOrder`  
`cloud.transfer.appliance.ccfe.api.v1alpha1.TransferAppliance.UpdateSavedAddress`  
  
## API interface audit logs

For information about how and which permissions are evaluated for each method, see the Identity and Access Management documentation for Transfer Appliance.

### `cloud.transfer.appliance.ccfe.api.v1alpha1.TransferAppliance`

The following audit logs are associated with methods belonging to `cloud.transfer.appliance.ccfe.api.v1alpha1.TransferAppliance`.

#### `CreateAppliance`

  * **Method** : `cloud.transfer.appliance.ccfe.api.v1alpha1.TransferAppliance.CreateAppliance`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `transferappliance.appliances.create - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="cloud.transfer.appliance.ccfe.api.v1alpha1.TransferAppliance.CreateAppliance" `  




#### `CreateOrder`

  * **Method** : `cloud.transfer.appliance.ccfe.api.v1alpha1.TransferAppliance.CreateOrder`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `transferappliance.orders.create - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="cloud.transfer.appliance.ccfe.api.v1alpha1.TransferAppliance.CreateOrder" `  




#### `CreateSavedAddress`

  * **Method** : `cloud.transfer.appliance.ccfe.api.v1alpha1.TransferAppliance.CreateSavedAddress`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `transferappliance.savedAddresses.create - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="cloud.transfer.appliance.ccfe.api.v1alpha1.TransferAppliance.CreateSavedAddress" `  




#### `DeleteAppliance`

  * **Method** : `cloud.transfer.appliance.ccfe.api.v1alpha1.TransferAppliance.DeleteAppliance`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `transferappliance.appliances.delete - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="cloud.transfer.appliance.ccfe.api.v1alpha1.TransferAppliance.DeleteAppliance" `  




#### `DeleteOrder`

  * **Method** : `cloud.transfer.appliance.ccfe.api.v1alpha1.TransferAppliance.DeleteOrder`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `transferappliance.orders.delete - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="cloud.transfer.appliance.ccfe.api.v1alpha1.TransferAppliance.DeleteOrder" `  




#### `DeleteSavedAddress`

  * **Method** : `cloud.transfer.appliance.ccfe.api.v1alpha1.TransferAppliance.DeleteSavedAddress`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `transferappliance.savedAddresses.delete - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="cloud.transfer.appliance.ccfe.api.v1alpha1.TransferAppliance.DeleteSavedAddress" `  




#### `ExportApplianceUserData`

  * **Method** : `cloud.transfer.appliance.ccfe.api.v1alpha1.TransferAppliance.ExportApplianceUserData`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `transferappliance.appliances.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="cloud.transfer.appliance.ccfe.api.v1alpha1.TransferAppliance.ExportApplianceUserData" `  




#### `GetAppliance`

  * **Method** : `cloud.transfer.appliance.ccfe.api.v1alpha1.TransferAppliance.GetAppliance`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `transferappliance.appliances.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="cloud.transfer.appliance.ccfe.api.v1alpha1.TransferAppliance.GetAppliance" `  




#### `GetCredential`

  * **Method** : `cloud.transfer.appliance.ccfe.api.v1alpha1.TransferAppliance.GetCredential`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `transferappliance.credentials.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="cloud.transfer.appliance.ccfe.api.v1alpha1.TransferAppliance.GetCredential" `  




#### `GetCredentialMetadata`

  * **Method** : `cloud.transfer.appliance.ccfe.api.v1alpha1.TransferAppliance.GetCredentialMetadata`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `transferappliance.credentials.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="cloud.transfer.appliance.ccfe.api.v1alpha1.TransferAppliance.GetCredentialMetadata" `  




#### `GetDownloadLinks`

  * **Method** : `cloud.transfer.appliance.ccfe.api.v1alpha1.TransferAppliance.GetDownloadLinks`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `transferappliance.appliances.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="cloud.transfer.appliance.ccfe.api.v1alpha1.TransferAppliance.GetDownloadLinks" `  




#### `GetOrder`

  * **Method** : `cloud.transfer.appliance.ccfe.api.v1alpha1.TransferAppliance.GetOrder`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `transferappliance.orders.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="cloud.transfer.appliance.ccfe.api.v1alpha1.TransferAppliance.GetOrder" `  




#### `GetSavedAddress`

  * **Method** : `cloud.transfer.appliance.ccfe.api.v1alpha1.TransferAppliance.GetSavedAddress`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `transferappliance.savedAddresses.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="cloud.transfer.appliance.ccfe.api.v1alpha1.TransferAppliance.GetSavedAddress" `  




#### `ListAppliances`

  * **Method** : `cloud.transfer.appliance.ccfe.api.v1alpha1.TransferAppliance.ListAppliances`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `transferappliance.appliances.list - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="cloud.transfer.appliance.ccfe.api.v1alpha1.TransferAppliance.ListAppliances" `  




#### `ListOrders`

  * **Method** : `cloud.transfer.appliance.ccfe.api.v1alpha1.TransferAppliance.ListOrders`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `transferappliance.orders.list - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="cloud.transfer.appliance.ccfe.api.v1alpha1.TransferAppliance.ListOrders" `  




#### `ListSavedAddresses`

  * **Method** : `cloud.transfer.appliance.ccfe.api.v1alpha1.TransferAppliance.ListSavedAddresses`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `transferappliance.savedAddresses.list - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="cloud.transfer.appliance.ccfe.api.v1alpha1.TransferAppliance.ListSavedAddresses" `  




#### `SubmitOrder`

  * **Method** : `cloud.transfer.appliance.ccfe.api.v1alpha1.TransferAppliance.SubmitOrder`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `transferappliance.appliances.update - ADMIN_WRITE`
    * `transferappliance.orders.update - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="cloud.transfer.appliance.ccfe.api.v1alpha1.TransferAppliance.SubmitOrder" `  




#### `UpdateAppliance`

  * **Method** : `cloud.transfer.appliance.ccfe.api.v1alpha1.TransferAppliance.UpdateAppliance`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `transferappliance.appliances.update - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="cloud.transfer.appliance.ccfe.api.v1alpha1.TransferAppliance.UpdateAppliance" `  




#### `UpdateOrder`

  * **Method** : `cloud.transfer.appliance.ccfe.api.v1alpha1.TransferAppliance.UpdateOrder`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `transferappliance.orders.update - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="cloud.transfer.appliance.ccfe.api.v1alpha1.TransferAppliance.UpdateOrder" `  




#### `UpdateSavedAddress`

  * **Method** : `cloud.transfer.appliance.ccfe.api.v1alpha1.TransferAppliance.UpdateSavedAddress`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `transferappliance.savedAddresses.update - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="cloud.transfer.appliance.ccfe.api.v1alpha1.TransferAppliance.UpdateSavedAddress" `  




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
