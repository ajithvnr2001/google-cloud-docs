---
url: https://docs.cloud.google.com/billing/docs/audit-logging/
title: Cloud Billing audit logging \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T08:59:08.040109+00:00
---

# Cloud Billing audit logging  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/billing/docs/audit-logging/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Costs and usage management ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Cloud Billing ](https://docs.cloud.google.com/billing/docs)
  * [ Resources ](https://docs.cloud.google.com/billing/docs/resources)



Send feedback 

#  Cloud Billing audit logging Stay organized with collections  Save and categorize content based on your preferences. 

This document lists the audited methods for Cloud Billing. Google Cloud services generate audit logs that record administrative and access activities within your Google Cloud resources. For more information about Cloud Audit Logs, see the following: 

  * [Types of audit logs](https://docs.cloud.google.com/logging/docs/audit#types)
  * [Audit log entry structure](https://docs.cloud.google.com/logging/docs/audit#audit_log_entry_structure)
  * [Storing and routing audit logs](https://docs.cloud.google.com/logging/docs/audit#storing_and_routing_audit_logs)
  * [Cloud Logging pricing summary](https://docs.cloud.google.com/stackdriver/pricing#logs-pricing-summary)
  * [Enable Data Access audit logs](https://docs.cloud.google.com/logging/docs/audit/configure-data-access)



## Service name

To view the Cloud Billing audit logs, do the following:

  1. In the Google Cloud console, go to the Logs Explorer page:

[Go to Logs Explorer](https://console.cloud.google.com/logs/query)

  2. Copy and paste the following query into the **Query** field of the Logs Explorer, and then click **Run query**.
         
         protoPayload.serviceName="cloudbilling.googleapis.com"
           




## Methods by permission type

Each IAM permission has a `type` property, whose value is an enum that can be one of four values: `ADMIN_READ`, `ADMIN_WRITE`, `DATA_READ`, or `DATA_WRITE`. When you call a method, Cloud Billing generates an audit log whose category is dependent on the `type` property of the permission required to perform the method. Methods that require an IAM permission with the `type` property value of `DATA_READ`, `DATA_WRITE`, or `ADMIN_READ` generate [Data Access](https://docs.cloud.google.com/logging/docs/audit#data-access) audit logs. Methods that require an IAM permission with the `type` property value of `ADMIN_WRITE` generate [Admin Activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity) audit logs.

API methods in the following list that are marked with (LRO) are long-running operations (LROs). These methods usually generate two audit log entries: one when the operation starts and another when it ends. For more information see [Audit logs for long-running operations](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro). Permission type | Methods  
---|---  
`ADMIN_READ` | `ListBillingAccountResources`  
`GetIamPolicy`  
`ADMIN_WRITE` | `ActivateInstrumentlessBillingAccount`  
`AssignResourceToBillingAccount`  
`CloseBillingAccount`  
`CreateSignupAssociationRecord`  
`DisableResourceBilling`  
`MigrateAccountSettings`  
`MigrateBillableServices`  
`ReopenBillingAccount`  
`UpdateBillingAccountAnacomCvpNumber`  
`UpdateBillingAccountCurrency`  
`UpdateBillingAccountDisplayName`  
`UpdateBillingAccountPurchaseOrderNumber`  
`UpdateParentOrganization`  
`UpdateResourceBillingProtection`  
`UpgradeFreeTrial`  
`CreateBillingAccount`  
`SetIamPolicy`  
`DATA_READ` | `CheckReopenability`  
`ListStateHistory`  
`google.cloud.billing.billingaccountprices.v1beta.BillingAccountPrices.GetBillingAccountPrice`  
`google.cloud.billing.billingaccountprices.v1beta.BillingAccountPrices.ListBillingAccountPrices`  
`google.cloud.billing.billingaccountprices.v2beta.BillingAccountPrices.GetBillingAccountPrice`  
`google.cloud.billing.billingaccountprices.v2beta.BillingAccountPrices.ListBillingAccountPrices`  
`google.cloud.billing.billingaccountservices.v1beta.BillingAccountServices.GetBillingAccountService`  
`google.cloud.billing.billingaccountservices.v1beta.BillingAccountServices.ListBillingAccountServices`  
`google.cloud.billing.billingaccountskugroups.v1beta.BillingAccountSkuGroups.GetBillingAccountSkuGroup`  
`google.cloud.billing.billingaccountskugroups.v1beta.BillingAccountSkuGroups.ListBillingAccountSkuGroups`  
`google.cloud.billing.billingaccountskugroupskus.v1beta.BillingAccountSkuGroupSkus.GetBillingAccountSkuGroupSku`  
`google.cloud.billing.billingaccountskugroupskus.v1beta.BillingAccountSkuGroupSkus.ListBillingAccountSkuGroupSkus`  
`google.cloud.billing.billingaccountskus.v1beta.BillingAccountSkus.GetBillingAccountSku`  
`google.cloud.billing.billingaccountskus.v1beta.BillingAccountSkus.ListBillingAccountSkus`  
`GetBillingAccount`  
`ListBillingAccounts`  
`OTHER` | `GetResourceBillingInfo`: To enable this log, enable `ADMIN_READ` under the service `cloudresourcemanager.googleapis.com`.  
`GetResourceBillingInfoBatch`: To enable this log, enable `ADMIN_READ` under the service `cloudresourcemanager.googleapis.com`.  
`GetProjectBillingInfo`: To enable this log, enable `ADMIN_READ` under the service `cloudresourcemanager.googleapis.com`.  
  
## API interface audit logs

For information about how and which permissions are evaluated for each method, see the Identity and Access Management documentation for Cloud Billing.

### `google.cloud.billing.billingaccountprices.v1beta.BillingAccountPrices`

The following audit logs are associated with methods belonging to `google.cloud.billing.billingaccountprices.v1beta.BillingAccountPrices`.

#### `GetBillingAccountPrice`

  * **Method** : `google.cloud.billing.billingaccountprices.v1beta.BillingAccountPrices.GetBillingAccountPrice`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `billing.billingAccountPrice.get - DATA_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.billing.billingaccountprices.v1beta.BillingAccountPrices.GetBillingAccountPrice" `  




#### `ListBillingAccountPrices`

  * **Method** : `google.cloud.billing.billingaccountprices.v1beta.BillingAccountPrices.ListBillingAccountPrices`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `billing.billingAccountPrices.list - DATA_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.billing.billingaccountprices.v1beta.BillingAccountPrices.ListBillingAccountPrices" `  




### `google.cloud.billing.billingaccountprices.v2beta.BillingAccountPrices`

The following audit logs are associated with methods belonging to `google.cloud.billing.billingaccountprices.v2beta.BillingAccountPrices`.

#### `GetBillingAccountPrice`

  * **Method** : `google.cloud.billing.billingaccountprices.v2beta.BillingAccountPrices.GetBillingAccountPrice`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `billing.billingAccountPrice.get - DATA_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.billing.billingaccountprices.v2beta.BillingAccountPrices.GetBillingAccountPrice" `  




#### `ListBillingAccountPrices`

  * **Method** : `google.cloud.billing.billingaccountprices.v2beta.BillingAccountPrices.ListBillingAccountPrices`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `billing.billingAccountPrices.list - DATA_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.billing.billingaccountprices.v2beta.BillingAccountPrices.ListBillingAccountPrices" `  




### `google.cloud.billing.billingaccountservices.v1beta.BillingAccountServices`

The following audit logs are associated with methods belonging to `google.cloud.billing.billingaccountservices.v1beta.BillingAccountServices`.

#### `GetBillingAccountService`

  * **Method** : `google.cloud.billing.billingaccountservices.v1beta.BillingAccountServices.GetBillingAccountService`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `billing.billingAccountServices.get - DATA_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.billing.billingaccountservices.v1beta.BillingAccountServices.GetBillingAccountService" `  




#### `ListBillingAccountServices`

  * **Method** : `google.cloud.billing.billingaccountservices.v1beta.BillingAccountServices.ListBillingAccountServices`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `billing.billingAccountServices.list - DATA_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.billing.billingaccountservices.v1beta.BillingAccountServices.ListBillingAccountServices" `  




### `google.cloud.billing.billingaccountskugroups.v1beta.BillingAccountSkuGroups`

The following audit logs are associated with methods belonging to `google.cloud.billing.billingaccountskugroups.v1beta.BillingAccountSkuGroups`.

#### `GetBillingAccountSkuGroup`

  * **Method** : `google.cloud.billing.billingaccountskugroups.v1beta.BillingAccountSkuGroups.GetBillingAccountSkuGroup`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `billing.billingAccountSkuGroups.get - DATA_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.billing.billingaccountskugroups.v1beta.BillingAccountSkuGroups.GetBillingAccountSkuGroup" `  




#### `ListBillingAccountSkuGroups`

  * **Method** : `google.cloud.billing.billingaccountskugroups.v1beta.BillingAccountSkuGroups.ListBillingAccountSkuGroups`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `billing.billingAccountSkuGroups.list - DATA_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.billing.billingaccountskugroups.v1beta.BillingAccountSkuGroups.ListBillingAccountSkuGroups" `  




### `google.cloud.billing.billingaccountskugroupskus.v1beta.BillingAccountSkuGroupSkus`

The following audit logs are associated with methods belonging to `google.cloud.billing.billingaccountskugroupskus.v1beta.BillingAccountSkuGroupSkus`.

#### `GetBillingAccountSkuGroupSku`

  * **Method** : `google.cloud.billing.billingaccountskugroupskus.v1beta.BillingAccountSkuGroupSkus.GetBillingAccountSkuGroupSku`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `billing.billingAccountSkuGroupSkus.get - DATA_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.billing.billingaccountskugroupskus.v1beta.BillingAccountSkuGroupSkus.GetBillingAccountSkuGroupSku" `  




#### `ListBillingAccountSkuGroupSkus`

  * **Method** : `google.cloud.billing.billingaccountskugroupskus.v1beta.BillingAccountSkuGroupSkus.ListBillingAccountSkuGroupSkus`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `billing.billingAccountSkuGroupSkus.list - DATA_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.billing.billingaccountskugroupskus.v1beta.BillingAccountSkuGroupSkus.ListBillingAccountSkuGroupSkus" `  




### `google.cloud.billing.billingaccountskus.v1beta.BillingAccountSkus`

The following audit logs are associated with methods belonging to `google.cloud.billing.billingaccountskus.v1beta.BillingAccountSkus`.

#### `GetBillingAccountSku`

  * **Method** : `google.cloud.billing.billingaccountskus.v1beta.BillingAccountSkus.GetBillingAccountSku`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `billing.billingAccountSkus.get - DATA_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.billing.billingaccountskus.v1beta.BillingAccountSkus.GetBillingAccountSku" `  




#### `ListBillingAccountSkus`

  * **Method** : `google.cloud.billing.billingaccountskus.v1beta.BillingAccountSkus.ListBillingAccountSkus`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `billing.billingAccountSkus.list - DATA_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.billing.billingaccountskus.v1beta.BillingAccountSkus.ListBillingAccountSkus" `  




### `google.cloud.billing.v1.CloudBilling`

The following audit logs are associated with methods belonging to `google.cloud.billing.v1.CloudBilling`.

#### `CreateBillingAccount`

  * **Method** : `CreateBillingAccount`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `billing.accounts.create - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="CreateBillingAccount" `  




#### `GetBillingAccount`

  * **Method** : `GetBillingAccount`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `billing.accounts.get - DATA_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="GetBillingAccount" `  




#### `GetIamPolicy`

  * **Method** : `GetIamPolicy`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `billing.accounts.getIamPolicy - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="GetIamPolicy" `  




#### `GetProjectBillingInfo`

  * **Method** : `GetProjectBillingInfo`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `resourcemanager.projects.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="GetProjectBillingInfo" `  




#### `ListBillingAccounts`

  * **Method** : `ListBillingAccounts`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `billing.accounts.get - DATA_READ`
    * `billing.accounts.list - DATA_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="ListBillingAccounts" `  




#### `SetIamPolicy`

  * **Method** : `SetIamPolicy`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `billing.accounts.setIamPolicy - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="SetIamPolicy" `  




### `other`

The following audit logs are associated with methods belonging to `other`.

#### `ActivateInstrumentlessBillingAccount`

  * **Method** : `ActivateInstrumentlessBillingAccount`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `billing.accounts.update - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="ActivateInstrumentlessBillingAccount" `  




#### `AssignResourceToBillingAccount`

  * **Method** : `AssignResourceToBillingAccount`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `billing.resourceAssociations.create - ADMIN_WRITE`
    * `billing.resourceAssociations.delete - ADMIN_WRITE`
    * `resourcemanager.projects.createBillingAssignment - ADMIN_WRITE`
    * `resourcemanager.projects.deleteBillingAssignment - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="AssignResourceToBillingAccount" `  




#### `CheckReopenability`

  * **Method** : `CheckReopenability`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `billing.accounts.get - DATA_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="CheckReopenability" `  




#### `CloseBillingAccount`

  * **Method** : `CloseBillingAccount`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `billing.accounts.close - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="CloseBillingAccount" `  




#### `CreateSignupAssociationRecord`

  * **Method** : `CreateSignupAssociationRecord`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `billing.accounts.update - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="CreateSignupAssociationRecord" `  




#### `DisableResourceBilling`

  * **Method** : `DisableResourceBilling`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `billing.resourceAssociations.delete - ADMIN_WRITE`
    * `resourcemanager.projects.deleteBillingAssignment - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="DisableResourceBilling" `  




#### `GetResourceBillingInfo`

  * **Method** : `GetResourceBillingInfo`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `resourcemanager.projects.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="GetResourceBillingInfo" `  




#### `GetResourceBillingInfoBatch`

  * **Method** : `GetResourceBillingInfoBatch`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `resourcemanager.projects.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="GetResourceBillingInfoBatch" `  




#### `ListBillingAccountResources`

  * **Method** : `ListBillingAccountResources`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `billing.resourceAssociations.list - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="ListBillingAccountResources" `  




#### `ListStateHistory`

  * **Method** : `ListStateHistory`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `billing.accounts.get - DATA_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="ListStateHistory" `  




#### `MigrateAccountSettings`

  * **Method** : `MigrateAccountSettings`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `billing.accounts.setIamPolicy - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="MigrateAccountSettings" `  




#### `MigrateBillableServices`

  * **Method** : `MigrateBillableServices`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `billing.accounts.update - ADMIN_WRITE`
    * `billing.subscriptions.create - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="MigrateBillableServices" `  




#### `ReopenBillingAccount`

  * **Method** : `ReopenBillingAccount`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `billing.accounts.reopen - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="ReopenBillingAccount" `  




#### `UpdateBillingAccountAnacomCvpNumber`

  * **Method** : `UpdateBillingAccountAnacomCvpNumber`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `billing.accounts.update - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="UpdateBillingAccountAnacomCvpNumber" `  




#### `UpdateBillingAccountCurrency`

  * **Method** : `UpdateBillingAccountCurrency`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `billing.accounts.update - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="UpdateBillingAccountCurrency" `  




#### `UpdateBillingAccountDisplayName`

  * **Method** : `UpdateBillingAccountDisplayName`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `billing.accounts.update - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="UpdateBillingAccountDisplayName" `  




#### `UpdateBillingAccountPurchaseOrderNumber`

  * **Method** : `UpdateBillingAccountPurchaseOrderNumber`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `billing.accounts.update - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="UpdateBillingAccountPurchaseOrderNumber" `  




#### `UpdateParentOrganization`

  * **Method** : `UpdateParentOrganization`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `billing.accounts.create - ADMIN_WRITE`
    * `billing.accounts.move - ADMIN_WRITE`
    * `billing.accounts.removeFromOrganization - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="UpdateParentOrganization" `  




#### `UpdateResourceBillingProtection`

  * **Method** : `UpdateResourceBillingProtection`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `billing.resourceAssociations.create - ADMIN_WRITE`
    * `billing.resourceAssociations.delete - ADMIN_WRITE`
    * `resourcemanager.projects.createBillingAssignment - ADMIN_WRITE`
    * `resourcemanager.projects.deleteBillingAssignment - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="UpdateResourceBillingProtection" `  




#### `UpgradeFreeTrial`

  * **Method** : `UpgradeFreeTrial`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `billing.accounts.update - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="UpgradeFreeTrial" `  




## Methods that don't produce audit logs

A method might not produce audit logs for one or more of the following reasons: 

  * It is a high volume method involving significant log generation and storage costs.
  * It has low auditing value.
  * Another audit or platform log already provides method coverage.



The following methods don't produce audit logs:

  * `a2a.v1.A2AService.CancelTask`
  * `a2a.v1.A2AService.CreateTaskPushNotificationConfig`
  * `a2a.v1.A2AService.DeleteTaskPushNotificationConfig`
  * `a2a.v1.A2AService.GetAgentCard`
  * `a2a.v1.A2AService.GetTask`
  * `a2a.v1.A2AService.GetTaskPushNotificationConfig`
  * `a2a.v1.A2AService.ListTaskPushNotificationConfig`
  * `a2a.v1.A2AService.SendMessage`
  * `a2a.v1.A2AService.SendStreamingMessage`
  * `a2a.v1.A2AService.TaskSubscription`
  * `google.cloud.billing.agentic.v1beta.BillingAgenticService.GenerateInsights`
  * `google.cloud.billing.prices.v1beta.Prices.GetPrice`
  * `google.cloud.billing.prices.v1beta.Prices.ListPrices`
  * `google.cloud.billing.prices.v2beta.Prices.GetPrice`
  * `google.cloud.billing.prices.v2beta.Prices.ListPrices`
  * `google.cloud.billing.services.v2beta.Services.GetService`
  * `google.cloud.billing.services.v2beta.Services.ListServices`
  * `google.cloud.billing.skugroups.v1beta.SkuGroups.GetSkuGroup`
  * `google.cloud.billing.skugroups.v1beta.SkuGroups.ListSkuGroups`
  * `google.cloud.billing.skugroupskus.v1beta.SkuGroupSkus.GetSkuGroupSku`
  * `google.cloud.billing.skugroupskus.v1beta.SkuGroupSkus.ListSkuGroupSkus`
  * `google.cloud.billing.skus.v2beta.Skus.GetSku`
  * `google.cloud.billing.skus.v2beta.Skus.ListSkus`
  * `google.cloud.billing.v1.CloudCatalog.ListServices`
  * `google.cloud.billing.v1.CloudCatalog.ListSkus`



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
