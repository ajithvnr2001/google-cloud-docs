---
url: https://docs.cloud.google.com/kms/docs/audit-logging-kms-inventory/
title: Cloud KMS Inventory Service audit logging \u00a0|\u00a0 Cloud Key Management Service \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T15:09:39.130622+00:00
---

# Cloud KMS Inventory Service audit logging  |  Cloud Key Management Service  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kms/docs/audit-logging-kms-inventory/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Cloud KMS ](https://docs.cloud.google.com/kms/docs)
  * [ Guides ](https://docs.cloud.google.com/kms/docs/key-management-service)



Send feedback 

#  Cloud KMS Inventory Service audit logging Stay organized with collections  Save and categorize content based on your preferences. 

This document lists the audited methods for Cloud KMS Inventory Service. Google Cloud services generate audit logs that record administrative and access activities within your Google Cloud resources. For more information about Cloud Audit Logs, see the following: 

  * [Types of audit logs](https://docs.cloud.google.com/logging/docs/audit#types)
  * [Audit log entry structure](https://docs.cloud.google.com/logging/docs/audit#audit_log_entry_structure)
  * [Storing and routing audit logs](https://docs.cloud.google.com/logging/docs/audit#storing_and_routing_audit_logs)
  * [Cloud Logging pricing summary](https://docs.cloud.google.com/stackdriver/pricing#logs-pricing-summary)
  * [Enable Data Access audit logs](https://docs.cloud.google.com/logging/docs/audit/configure-data-access)



## Service name

To view the Cloud KMS Inventory Service audit logs, do the following:

  1. In the Google Cloud console, go to the Logs Explorer page:

[Go to Logs Explorer](https://console.cloud.google.com/logs/query)

  2. Copy and paste the following query into the **Query** field of the Logs Explorer, and then click **Run query**.
         
         protoPayload.serviceName="kmsinventory.googleapis.com"
           




## Methods by permission type

Each IAM permission has a `type` property, whose value is an enum that can be one of four values: `ADMIN_READ`, `ADMIN_WRITE`, `DATA_READ`, or `DATA_WRITE`. When you call a method, Cloud KMS Inventory Service generates an audit log whose category is dependent on the `type` property of the permission required to perform the method. Methods that require an IAM permission with the `type` property value of `DATA_READ`, `DATA_WRITE`, or `ADMIN_READ` generate [Data Access](https://docs.cloud.google.com/logging/docs/audit#data-access) audit logs. Methods that require an IAM permission with the `type` property value of `ADMIN_WRITE` generate [Admin Activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity) audit logs.

API methods in the following list that are marked with (LRO) are long-running operations (LROs). These methods usually generate two audit log entries: one when the operation starts and another when it ends. For more information see [Audit logs for long-running operations](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro). Permission type | Methods  
---|---  
`OTHER` | `google.cloud.kms.inventory.v1.KeyDashboardService.ListCryptoKeys`: To enable this log, enable `ADMIN_READ` under the service `cloudkms.googleapis.com`.  
`google.cloud.kms.inventory.v1.KeyTrackingService.GetProtectedResourcesSummary`: To enable this log, enable `ADMIN_READ` under the service `cloudkms.googleapis.com`.  
`google.cloud.kms.inventory.v1.KeyTrackingService.SearchProtectedResources`: To enable this log, enable `ADMIN_READ` under the service `cloudkms.googleapis.com`.  
  
## API interface audit logs

For information about how and which permissions are evaluated for each method, see the Identity and Access Management documentation for Cloud KMS Inventory Service.

### `google.cloud.kms.inventory.v1.KeyDashboardService`

The following audit logs are associated with methods belonging to `google.cloud.kms.inventory.v1.KeyDashboardService`.

#### `ListCryptoKeys`

  * **Method** : `google.cloud.kms.inventory.v1.KeyDashboardService.ListCryptoKeys`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `cloudkms.cryptoKeys.list - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.kms.inventory.v1.KeyDashboardService.ListCryptoKeys" `  




### `google.cloud.kms.inventory.v1.KeyTrackingService`

The following audit logs are associated with methods belonging to `google.cloud.kms.inventory.v1.KeyTrackingService`.

#### `GetProtectedResourcesSummary`

  * **Method** : `google.cloud.kms.inventory.v1.KeyTrackingService.GetProtectedResourcesSummary`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `cloudkms.cryptoKeys.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.kms.inventory.v1.KeyTrackingService.GetProtectedResourcesSummary" `  




#### `SearchProtectedResources`

  * **Method** : `google.cloud.kms.inventory.v1.KeyTrackingService.SearchProtectedResources`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `cloudkms.cryptoKeys.get - ADMIN_READ`
    * `cloudkms.protectedResources.search - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.kms.inventory.v1.KeyTrackingService.SearchProtectedResources" `  




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
