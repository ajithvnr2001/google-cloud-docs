---
url: https://docs.cloud.google.com/resource-manager/docs/essential-contacts-audit-logging/
title: Essential Contacts audit logging \u00a0|\u00a0 Resource Manager \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T05:43:57.049541+00:00
---

# Essential Contacts audit logging  |  Resource Manager  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/resource-manager/docs/essential-contacts-audit-logging/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Resource Manager ](https://docs.cloud.google.com/resource-manager/docs)



Send feedback 

#  Essential Contacts audit logging Stay organized with collections  Save and categorize content based on your preferences. 

This document lists the audited methods for Essential Contacts. Google Cloud services generate audit logs that record administrative and access activities within your Google Cloud resources. For more information about Cloud Audit Logs, see the following: 

  * [Types of audit logs](https://docs.cloud.google.com/logging/docs/audit#types)
  * [Audit log entry structure](https://docs.cloud.google.com/logging/docs/audit#audit_log_entry_structure)
  * [Storing and routing audit logs](https://docs.cloud.google.com/logging/docs/audit#storing_and_routing_audit_logs)
  * [Cloud Logging pricing summary](https://docs.cloud.google.com/stackdriver/pricing#logs-pricing-summary)
  * [Enable Data Access audit logs](https://docs.cloud.google.com/logging/docs/audit/configure-data-access)



## Service name

To view the Essential Contacts audit logs, do the following:

  1. In the Google Cloud console, go to the Logs Explorer page:

[Go to Logs Explorer](https://console.cloud.google.com/logs/query)

  2. Copy and paste the following query into the **Query** field of the Logs Explorer, and then click **Run query**.
         
         protoPayload.serviceName="essentialcontacts.googleapis.com"
           




## Methods by permission type

Each IAM permission has a `type` property, whose value is an enum that can be one of four values: `ADMIN_READ`, `ADMIN_WRITE`, `DATA_READ`, or `DATA_WRITE`. When you call a method, Essential Contacts generates an audit log whose category is dependent on the `type` property of the permission required to perform the method. Methods that require an IAM permission with the `type` property value of `DATA_READ`, `DATA_WRITE`, or `ADMIN_READ` generate [Data Access](https://docs.cloud.google.com/logging/docs/audit#data-access) audit logs. Methods that require an IAM permission with the `type` property value of `ADMIN_WRITE` generate [Admin Activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity) audit logs.

API methods in the following list that are marked with (LRO) are long-running operations (LROs). These methods usually generate two audit log entries: one when the operation starts and another when it ends. For more information see [Audit logs for long-running operations](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro). Permission type | Methods  
---|---  
`DATA_READ` | `google.cloud.essentialcontacts.v1.EssentialContactsService.ComputeContacts`  
`google.cloud.essentialcontacts.v1.EssentialContactsService.GetContact`  
`google.cloud.essentialcontacts.v1.EssentialContactsService.ListContacts`  
`google.cloud.essentialcontacts.v1alpha1.EssentialContactsService.ComputeContacts`  
`google.cloud.essentialcontacts.v1alpha1.EssentialContactsService.GetContact`  
`google.cloud.essentialcontacts.v1alpha1.EssentialContactsService.ListContacts`  
`google.cloud.essentialcontacts.v1beta1.EssentialContactsService.ComputeContacts`  
`google.cloud.essentialcontacts.v1beta1.EssentialContactsService.GetContact`  
`google.cloud.essentialcontacts.v1beta1.EssentialContactsService.ListContacts`  
`DATA_WRITE` | `google.cloud.essentialcontacts.v1.EssentialContactsService.CreateContact`  
`google.cloud.essentialcontacts.v1.EssentialContactsService.DeleteContact`  
`google.cloud.essentialcontacts.v1.EssentialContactsService.SendTestMessage`  
`google.cloud.essentialcontacts.v1.EssentialContactsService.UpdateContact`  
`google.cloud.essentialcontacts.v1alpha1.EssentialContactsService.CreateContact`  
`google.cloud.essentialcontacts.v1alpha1.EssentialContactsService.DeleteContact`  
`google.cloud.essentialcontacts.v1alpha1.EssentialContactsService.SendTestMessage`  
`google.cloud.essentialcontacts.v1alpha1.EssentialContactsService.UpdateContact`  
`google.cloud.essentialcontacts.v1beta1.EssentialContactsService.CreateContact`  
`google.cloud.essentialcontacts.v1beta1.EssentialContactsService.DeleteContact`  
`google.cloud.essentialcontacts.v1beta1.EssentialContactsService.SendTestMessage`  
`google.cloud.essentialcontacts.v1beta1.EssentialContactsService.UpdateContact`  
  
## API interface audit logs

For information about how and which permissions are evaluated for each method, see the Identity and Access Management documentation for Essential Contacts.

### `google.cloud.essentialcontacts.v1.EssentialContactsService`

The following audit logs are associated with methods belonging to `google.cloud.essentialcontacts.v1.EssentialContactsService`.

#### `ComputeContacts`

  * **Method** : `google.cloud.essentialcontacts.v1.EssentialContactsService.ComputeContacts`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `essentialcontacts.contacts.get - DATA_READ`
    * `essentialcontacts.contacts.list - DATA_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.essentialcontacts.v1.EssentialContactsService.ComputeContacts" `  




#### `CreateContact`

  * **Method** : `google.cloud.essentialcontacts.v1.EssentialContactsService.CreateContact`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `essentialcontacts.contacts.create - DATA_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.essentialcontacts.v1.EssentialContactsService.CreateContact" `  




#### `DeleteContact`

  * **Method** : `google.cloud.essentialcontacts.v1.EssentialContactsService.DeleteContact`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `essentialcontacts.contacts.delete - DATA_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.essentialcontacts.v1.EssentialContactsService.DeleteContact" `  




#### `GetContact`

  * **Method** : `google.cloud.essentialcontacts.v1.EssentialContactsService.GetContact`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `essentialcontacts.contacts.get - DATA_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.essentialcontacts.v1.EssentialContactsService.GetContact" `  




#### `ListContacts`

  * **Method** : `google.cloud.essentialcontacts.v1.EssentialContactsService.ListContacts`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `essentialcontacts.contacts.list - DATA_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.essentialcontacts.v1.EssentialContactsService.ListContacts" `  




#### `SendTestMessage`

  * **Method** : `google.cloud.essentialcontacts.v1.EssentialContactsService.SendTestMessage`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `essentialcontacts.contacts.send - DATA_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.essentialcontacts.v1.EssentialContactsService.SendTestMessage" `  




#### `UpdateContact`

  * **Method** : `google.cloud.essentialcontacts.v1.EssentialContactsService.UpdateContact`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `essentialcontacts.contacts.update - DATA_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.essentialcontacts.v1.EssentialContactsService.UpdateContact" `  




### `google.cloud.essentialcontacts.v1alpha1.EssentialContactsService`

The following audit logs are associated with methods belonging to `google.cloud.essentialcontacts.v1alpha1.EssentialContactsService`.

#### `ComputeContacts`

  * **Method** : `google.cloud.essentialcontacts.v1alpha1.EssentialContactsService.ComputeContacts`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `essentialcontacts.contacts.list - DATA_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.essentialcontacts.v1alpha1.EssentialContactsService.ComputeContacts" `  




#### `CreateContact`

  * **Method** : `google.cloud.essentialcontacts.v1alpha1.EssentialContactsService.CreateContact`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `essentialcontacts.contacts.create - DATA_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.essentialcontacts.v1alpha1.EssentialContactsService.CreateContact" `  




#### `DeleteContact`

  * **Method** : `google.cloud.essentialcontacts.v1alpha1.EssentialContactsService.DeleteContact`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `essentialcontacts.contacts.delete - DATA_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.essentialcontacts.v1alpha1.EssentialContactsService.DeleteContact" `  




#### `GetContact`

  * **Method** : `google.cloud.essentialcontacts.v1alpha1.EssentialContactsService.GetContact`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `essentialcontacts.contacts.get - DATA_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.essentialcontacts.v1alpha1.EssentialContactsService.GetContact" `  




#### `ListContacts`

  * **Method** : `google.cloud.essentialcontacts.v1alpha1.EssentialContactsService.ListContacts`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `essentialcontacts.contacts.list - DATA_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.essentialcontacts.v1alpha1.EssentialContactsService.ListContacts" `  




#### `SendTestMessage`

  * **Method** : `google.cloud.essentialcontacts.v1alpha1.EssentialContactsService.SendTestMessage`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `essentialcontacts.contacts.send - DATA_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.essentialcontacts.v1alpha1.EssentialContactsService.SendTestMessage" `  




#### `UpdateContact`

  * **Method** : `google.cloud.essentialcontacts.v1alpha1.EssentialContactsService.UpdateContact`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `essentialcontacts.contacts.update - DATA_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.essentialcontacts.v1alpha1.EssentialContactsService.UpdateContact" `  




### `google.cloud.essentialcontacts.v1beta1.EssentialContactsService`

The following audit logs are associated with methods belonging to `google.cloud.essentialcontacts.v1beta1.EssentialContactsService`.

#### `ComputeContacts`

  * **Method** : `google.cloud.essentialcontacts.v1beta1.EssentialContactsService.ComputeContacts`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `essentialcontacts.contacts.get - DATA_READ`
    * `essentialcontacts.contacts.list - DATA_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.essentialcontacts.v1beta1.EssentialContactsService.ComputeContacts" `  




#### `CreateContact`

  * **Method** : `google.cloud.essentialcontacts.v1beta1.EssentialContactsService.CreateContact`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `essentialcontacts.contacts.create - DATA_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.essentialcontacts.v1beta1.EssentialContactsService.CreateContact" `  




#### `DeleteContact`

  * **Method** : `google.cloud.essentialcontacts.v1beta1.EssentialContactsService.DeleteContact`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `essentialcontacts.contacts.delete - DATA_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.essentialcontacts.v1beta1.EssentialContactsService.DeleteContact" `  




#### `GetContact`

  * **Method** : `google.cloud.essentialcontacts.v1beta1.EssentialContactsService.GetContact`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `essentialcontacts.contacts.get - DATA_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.essentialcontacts.v1beta1.EssentialContactsService.GetContact" `  




#### `ListContacts`

  * **Method** : `google.cloud.essentialcontacts.v1beta1.EssentialContactsService.ListContacts`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `essentialcontacts.contacts.list - DATA_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.essentialcontacts.v1beta1.EssentialContactsService.ListContacts" `  




#### `SendTestMessage`

  * **Method** : `google.cloud.essentialcontacts.v1beta1.EssentialContactsService.SendTestMessage`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `essentialcontacts.contacts.send - DATA_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.essentialcontacts.v1beta1.EssentialContactsService.SendTestMessage" `  




#### `UpdateContact`

  * **Method** : `google.cloud.essentialcontacts.v1beta1.EssentialContactsService.UpdateContact`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `essentialcontacts.contacts.update - DATA_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.essentialcontacts.v1beta1.EssentialContactsService.UpdateContact" `  




## Methods that don't produce audit logs

A method might not produce audit logs for one or more of the following reasons: 

  * It is a high volume method involving significant log generation and storage costs.
  * It has low auditing value.
  * Another audit or platform log already provides method coverage.



The following methods don't produce audit logs:

  * `google.cloud.essentialcontacts.v1alpha1.EssentialContactsService.ResendVerification`
  * `google.cloud.essentialcontacts.v1alpha1.EssentialContactsService.VerifyContact`



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
