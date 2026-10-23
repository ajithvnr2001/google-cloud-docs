---
url: https://docs.cloud.google.com/kms/docs/audit-logging/
title: Cloud Key Management Service audit logging \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T12:36:33.488443+00:00
---

# Cloud Key Management Service audit logging  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kms/docs/audit-logging/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Cloud KMS ](https://docs.cloud.google.com/kms/docs)
  * [ Guides ](https://docs.cloud.google.com/kms/docs/key-management-service)



Send feedback 

#  Cloud Key Management Service audit logging Stay organized with collections  Save and categorize content based on your preferences. 

Cloud Key Management Service is updating the format of the `protoPayload` field in its Data Access audit log entries. During the migration period, the `protoPayload` within Data Access audit log entries will remain backward-compatible. However, new or future code applications should use the recommended replacement fields as follows: Recommended replacement field | Deprecated field | Description  
---|---|---  
`protoPayload.status.details` | `protoPayload.metadata` | Error detail for `EXTERNAL` (i.e., Cloud EKM) key operations.  
`protoPayload.metadata.entries.caller_provided_context` | `protoPayload.request.caller_provided_context` | Context from the caller associated with this Cloud KMS operation.  
  
  


This document lists the audited methods for Cloud Key Management Service. Google Cloud services generate audit logs that record administrative and access activities within your Google Cloud resources. For more information about Cloud Audit Logs, see the following: 

  * [Types of audit logs](https://docs.cloud.google.com/logging/docs/audit#types)
  * [Audit log entry structure](https://docs.cloud.google.com/logging/docs/audit#audit_log_entry_structure)
  * [Storing and routing audit logs](https://docs.cloud.google.com/logging/docs/audit#storing_and_routing_audit_logs)
  * [Cloud Logging pricing summary](https://docs.cloud.google.com/stackdriver/pricing#logs-pricing-summary)
  * [Enable Data Access audit logs](https://docs.cloud.google.com/logging/docs/audit/configure-data-access)



## Service name

To view the Cloud Key Management Service audit logs, do the following:

  1. In the Google Cloud console, go to the Logs Explorer page:

[Go to Logs Explorer](https://console.cloud.google.com/logs/query)

  2. Copy and paste the following query into the **Query** field of the Logs Explorer, and then click **Run query**.
         
         protoPayload.serviceName="cloudkms.googleapis.com"
           




## Methods by permission type

Each IAM permission has a `type` property, whose value is an enum that can be one of four values: `ADMIN_READ`, `ADMIN_WRITE`, `DATA_READ`, or `DATA_WRITE`. When you call a method, Cloud Key Management Service generates an audit log whose category is dependent on the `type` property of the permission required to perform the method. Methods that require an IAM permission with the `type` property value of `DATA_READ`, `DATA_WRITE`, or `ADMIN_READ` generate [Data Access](https://docs.cloud.google.com/logging/docs/audit#data-access) audit logs. Methods that require an IAM permission with the `type` property value of `ADMIN_WRITE` generate [Admin Activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity) audit logs.

API methods in the following list that are marked with (LRO) are long-running operations (LROs). These methods usually generate two audit log entries: one when the operation starts and another when it ends. For more information see [Audit logs for long-running operations](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro). Permission type | Methods  
---|---  
`ADMIN_READ` | `google.cloud.kms.v1.Autokey.GetKeyHandle`  
`google.cloud.kms.v1.Autokey.ListKeyHandles`  
`google.cloud.kms.v1.AutokeyAdmin.GetAutokeyConfig`  
`google.cloud.kms.v1.AutokeyAdmin.ShowEffectiveAutokeyConfig`  
`GetEkmConfig`  
`GetEkmConnection`  
`ListEkmConnections`  
`VerifyConnectivity`  
`google.cloud.kms.v1.HsmManagement.GetSingleTenantHsmInstance`  
`google.cloud.kms.v1.HsmManagement.GetSingleTenantHsmInstanceProposal`  
`google.cloud.kms.v1.HsmManagement.ListSingleTenantHsmInstanceProposals`  
`google.cloud.kms.v1.HsmManagement.ListSingleTenantHsmInstances`  
`google.cloud.kms.v1.KeyAccessJustificationsConfig.GetKeyAccessJustificationsPolicyConfig`  
`google.cloud.kms.v1.KeyAccessJustificationsConfig.ShowEffectiveKeyAccessJustificationsEnrollmentConfig`  
`google.cloud.kms.v1.KeyAccessJustificationsConfig.ShowEffectiveKeyAccessJustificationsPolicyConfig`  
`GetCryptoKey`  
`GetCryptoKeyVersion`  
`GetImportJob`  
`GetKeyRing`  
`GetRetiredResource`  
`ListCryptoKeyVersions`  
`ListCryptoKeys`  
`ListImportJobs`  
`ListKeyRings`  
`ListRetiredResources`  
`GetIamPolicy`  
`GetOperation`  
`ADMIN_WRITE` | `google.cloud.kms.v1.Autokey.CreateKeyHandle` (LRO)  
`google.cloud.kms.v1.AutokeyAdmin.UpdateAutokeyConfig`  
`CreateEkmConnection`  
`UpdateEkmConfig`  
`UpdateEkmConnection`  
`google.cloud.kms.v1.HsmManagement.ApproveSingleTenantHsmInstanceProposal`  
`google.cloud.kms.v1.HsmManagement.CreateSingleTenantHsmInstance` (LRO)  
`google.cloud.kms.v1.HsmManagement.CreateSingleTenantHsmInstanceProposal` (LRO)  
`google.cloud.kms.v1.HsmManagement.DeleteSingleTenantHsmInstanceProposal`  
`google.cloud.kms.v1.HsmManagement.ExecuteSingleTenantHsmInstanceProposal` (LRO)  
`google.cloud.kms.v1.KeyAccessJustificationsConfig.UpdateKeyAccessJustificationsPolicyConfig`  
`CreateCryptoKey`  
`CreateCryptoKeyVersion`  
`CreateImportJob`  
`CreateKeyRing`  
`DeleteCryptoKey`  
`DeleteCryptoKeyVersion`  
`DeleteKeyRing`  
`DestroyCryptoKeyVersion`  
`ExportTrustedKeyWrappedCryptoKeyVersion`  
`ImportCryptoKeyVersion`  
`ImportTrustedKeyWrappedCryptoKeyVersion`  
`RestoreCryptoKeyVersion`  
`UpdateCryptoKey`  
`UpdateCryptoKeyPrimaryVersion`  
`UpdateCryptoKeyVersion`  
`SetIamPolicy`  
`DATA_READ` | `AsymmetricDecrypt`  
`AsymmetricSign`  
`Decapsulate`  
`Decrypt`  
`Encrypt`  
`GetPublicKey`  
`MacSign`  
`MacVerify`  
`RawDecrypt`  
`RawEncrypt`  
  
## API interface audit logs

For information about how and which permissions are evaluated for each method, see the Identity and Access Management documentation for Cloud Key Management Service.

### `google.cloud.kms.v1.Autokey`

The following audit logs are associated with methods belonging to `google.cloud.kms.v1.Autokey`.

#### `CreateKeyHandle`

  * **Method** : `google.cloud.kms.v1.Autokey.CreateKeyHandle`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `cloudkms.keyHandles.create - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.kms.v1.Autokey.CreateKeyHandle" `  




#### `GetKeyHandle`

  * **Method** : `google.cloud.kms.v1.Autokey.GetKeyHandle`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `cloudkms.keyHandles.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.kms.v1.Autokey.GetKeyHandle" `  




#### `ListKeyHandles`

  * **Method** : `google.cloud.kms.v1.Autokey.ListKeyHandles`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `cloudkms.keyHandles.list - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.kms.v1.Autokey.ListKeyHandles" `  




### `google.cloud.kms.v1.AutokeyAdmin`

The following audit logs are associated with methods belonging to `google.cloud.kms.v1.AutokeyAdmin`.

#### `GetAutokeyConfig`

  * **Method** : `google.cloud.kms.v1.AutokeyAdmin.GetAutokeyConfig`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `cloudkms.autokeyConfigs.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.kms.v1.AutokeyAdmin.GetAutokeyConfig" `  




#### `ShowEffectiveAutokeyConfig`

  * **Method** : `google.cloud.kms.v1.AutokeyAdmin.ShowEffectiveAutokeyConfig`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `cloudkms.folders.showEffectiveAutokeyConfig - ADMIN_READ`
    * `cloudkms.projects.showEffectiveAutokeyConfig - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.kms.v1.AutokeyAdmin.ShowEffectiveAutokeyConfig" `  




#### `UpdateAutokeyConfig`

  * **Method** : `google.cloud.kms.v1.AutokeyAdmin.UpdateAutokeyConfig`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `cloudkms.autokeyConfigs.update - ADMIN_WRITE`
    * `cloudkms.cryptoKeys.setIamPolicy - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.kms.v1.AutokeyAdmin.UpdateAutokeyConfig" `  




### `google.cloud.kms.v1.EkmService`

The following audit logs are associated with methods belonging to `google.cloud.kms.v1.EkmService`.

#### `CreateEkmConnection`

  * **Method** : `CreateEkmConnection`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `cloudkms.ekmConnections.create - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="CreateEkmConnection" `  




#### `GetEkmConfig`

  * **Method** : `GetEkmConfig`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `cloudkms.ekmConfigs.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="GetEkmConfig" `  




#### `GetEkmConnection`

  * **Method** : `GetEkmConnection`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `cloudkms.ekmConnections.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="GetEkmConnection" `  




#### `ListEkmConnections`

  * **Method** : `ListEkmConnections`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `cloudkms.ekmConnections.list - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="ListEkmConnections" `  




#### `UpdateEkmConfig`

  * **Method** : `UpdateEkmConfig`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `cloudkms.ekmConfigs.update - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="UpdateEkmConfig" `  




#### `UpdateEkmConnection`

  * **Method** : `UpdateEkmConnection`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `cloudkms.ekmConnections.update - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="UpdateEkmConnection" `  




#### `VerifyConnectivity`

  * **Method** : `VerifyConnectivity`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `cloudkms.ekmConnections.verifyConnectivity - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="VerifyConnectivity" `  




### `google.cloud.kms.v1.HsmManagement`

The following audit logs are associated with methods belonging to `google.cloud.kms.v1.HsmManagement`.

#### `ApproveSingleTenantHsmInstanceProposal`

  * **Method** : `google.cloud.kms.v1.HsmManagement.ApproveSingleTenantHsmInstanceProposal`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `cloudkms.singleTenantHsmInstanceProposals.approve - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.kms.v1.HsmManagement.ApproveSingleTenantHsmInstanceProposal" `  




#### `CreateSingleTenantHsmInstance`

  * **Method** : `google.cloud.kms.v1.HsmManagement.CreateSingleTenantHsmInstance`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `cloudkms.singleTenantHsmInstances.create - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.kms.v1.HsmManagement.CreateSingleTenantHsmInstance" `  




#### `CreateSingleTenantHsmInstanceProposal`

  * **Method** : `google.cloud.kms.v1.HsmManagement.CreateSingleTenantHsmInstanceProposal`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `cloudkms.singleTenantHsmInstanceProposals.create - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.kms.v1.HsmManagement.CreateSingleTenantHsmInstanceProposal" `  




#### `DeleteSingleTenantHsmInstanceProposal`

  * **Method** : `google.cloud.kms.v1.HsmManagement.DeleteSingleTenantHsmInstanceProposal`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `cloudkms.singleTenantHsmInstanceProposals.delete - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.kms.v1.HsmManagement.DeleteSingleTenantHsmInstanceProposal" `  




#### `ExecuteSingleTenantHsmInstanceProposal`

  * **Method** : `google.cloud.kms.v1.HsmManagement.ExecuteSingleTenantHsmInstanceProposal`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `cloudkms.singleTenantHsmInstanceProposals.execute - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.kms.v1.HsmManagement.ExecuteSingleTenantHsmInstanceProposal" `  




#### `GetSingleTenantHsmInstance`

  * **Method** : `google.cloud.kms.v1.HsmManagement.GetSingleTenantHsmInstance`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `cloudkms.singleTenantHsmInstances.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.kms.v1.HsmManagement.GetSingleTenantHsmInstance" `  




#### `GetSingleTenantHsmInstanceProposal`

  * **Method** : `google.cloud.kms.v1.HsmManagement.GetSingleTenantHsmInstanceProposal`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `cloudkms.singleTenantHsmInstanceProposals.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.kms.v1.HsmManagement.GetSingleTenantHsmInstanceProposal" `  




#### `ListSingleTenantHsmInstanceProposals`

  * **Method** : `google.cloud.kms.v1.HsmManagement.ListSingleTenantHsmInstanceProposals`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `cloudkms.singleTenantHsmInstanceProposals.list - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.kms.v1.HsmManagement.ListSingleTenantHsmInstanceProposals" `  




#### `ListSingleTenantHsmInstances`

  * **Method** : `google.cloud.kms.v1.HsmManagement.ListSingleTenantHsmInstances`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `cloudkms.singleTenantHsmInstances.list - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.kms.v1.HsmManagement.ListSingleTenantHsmInstances" `  




### `google.cloud.kms.v1.KeyAccessJustificationsConfig`

The following audit logs are associated with methods belonging to `google.cloud.kms.v1.KeyAccessJustificationsConfig`.

#### `GetKeyAccessJustificationsPolicyConfig`

  * **Method** : `google.cloud.kms.v1.KeyAccessJustificationsConfig.GetKeyAccessJustificationsPolicyConfig`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `cloudkms.kajPolicyConfigs.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.kms.v1.KeyAccessJustificationsConfig.GetKeyAccessJustificationsPolicyConfig" `  




#### `ShowEffectiveKeyAccessJustificationsEnrollmentConfig`

  * **Method** : `google.cloud.kms.v1.KeyAccessJustificationsConfig.ShowEffectiveKeyAccessJustificationsEnrollmentConfig`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `cloudkms.projects.showEffectiveKajEnrollmentConfig - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.kms.v1.KeyAccessJustificationsConfig.ShowEffectiveKeyAccessJustificationsEnrollmentConfig" `  




#### `ShowEffectiveKeyAccessJustificationsPolicyConfig`

  * **Method** : `google.cloud.kms.v1.KeyAccessJustificationsConfig.ShowEffectiveKeyAccessJustificationsPolicyConfig`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `cloudkms.projects.showEffectiveKajPolicyConfig - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.kms.v1.KeyAccessJustificationsConfig.ShowEffectiveKeyAccessJustificationsPolicyConfig" `  




#### `UpdateKeyAccessJustificationsPolicyConfig`

  * **Method** : `google.cloud.kms.v1.KeyAccessJustificationsConfig.UpdateKeyAccessJustificationsPolicyConfig`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `cloudkms.kajPolicyConfigs.update - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.kms.v1.KeyAccessJustificationsConfig.UpdateKeyAccessJustificationsPolicyConfig" `  




### `google.cloud.kms.v1.KeyManagementService`

The following audit logs are associated with methods belonging to `google.cloud.kms.v1.KeyManagementService`.

#### `AsymmetricDecrypt`

  * **Method** : `AsymmetricDecrypt`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `cloudkms.cryptoKeyVersions.useToDecrypt - DATA_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="AsymmetricDecrypt" `  




#### `AsymmetricSign`

  * **Method** : `AsymmetricSign`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `cloudkms.cryptoKeyVersions.useToSign - DATA_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="AsymmetricSign" `  




#### `CreateCryptoKey`

  * **Method** : `CreateCryptoKey`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `cloudkms.cryptoKeys.create - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="CreateCryptoKey" `  




#### `CreateCryptoKeyVersion`

  * **Method** : `CreateCryptoKeyVersion`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `cloudkms.cryptoKeyVersions.create - ADMIN_WRITE`
    * `cloudkms.cryptoKeyVersions.manageRawPKCS1Keys - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="CreateCryptoKeyVersion" `  




#### `CreateImportJob`

  * **Method** : `CreateImportJob`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `cloudkms.importJobs.create - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="CreateImportJob" `  




#### `CreateKeyRing`

  * **Method** : `CreateKeyRing`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `cloudkms.keyRings.create - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="CreateKeyRing" `  




#### `Decapsulate`

  * **Method** : `Decapsulate`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `cloudkms.cryptoKeyVersions.useToDecapsulate - DATA_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="Decapsulate" `  




#### `Decrypt`

  * **Method** : `Decrypt`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `cloudkms.cryptoKeyVersions.useToDecrypt - DATA_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="Decrypt" `  




#### `DeleteCryptoKey`

  * **Method** : `DeleteCryptoKey`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `cloudkms.cryptoKeys.delete - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="DeleteCryptoKey" `  




#### `DeleteCryptoKeyVersion`

  * **Method** : `DeleteCryptoKeyVersion`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `cloudkms.cryptoKeyVersions.delete - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="DeleteCryptoKeyVersion" `  




#### `DeleteKeyRing`

  * **Method** : `DeleteKeyRing`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `cloudkms.keyRings.delete - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="DeleteKeyRing" `  




#### `DestroyCryptoKeyVersion`

  * **Method** : `DestroyCryptoKeyVersion`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `cloudkms.cryptoKeyVersions.destroy - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="DestroyCryptoKeyVersion" `  




#### `Encrypt`

  * **Method** : `Encrypt`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `cloudkms.cryptoKeyVersions.useToEncrypt - DATA_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="Encrypt" `  




#### `ExportTrustedKeyWrappedCryptoKeyVersion`

  * **Method** : `ExportTrustedKeyWrappedCryptoKeyVersion`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `cloudkms.cryptoKeyVersions.get - ADMIN_READ`
    * `cloudkms.cryptoKeyVersions.trustedImportExport - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="ExportTrustedKeyWrappedCryptoKeyVersion" `  




#### `GetCryptoKey`

  * **Method** : `GetCryptoKey`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `cloudkms.cryptoKeys.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="GetCryptoKey" `  




#### `GetCryptoKeyVersion`

  * **Method** : `GetCryptoKeyVersion`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `cloudkms.cryptoKeyVersions.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="GetCryptoKeyVersion" `  




#### `GetImportJob`

  * **Method** : `GetImportJob`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `cloudkms.importJobs.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="GetImportJob" `  




#### `GetKeyRing`

  * **Method** : `GetKeyRing`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `cloudkms.keyRings.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="GetKeyRing" `  




#### `GetPublicKey`

  * **Method** : `GetPublicKey`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `cloudkms.cryptoKeyVersions.viewPublicKey - DATA_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="GetPublicKey" `  




#### `GetRetiredResource`

  * **Method** : `GetRetiredResource`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `cloudkms.retiredResources.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="GetRetiredResource" `  




#### `ImportCryptoKeyVersion`

  * **Method** : `ImportCryptoKeyVersion`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `cloudkms.cryptoKeyVersions.create - ADMIN_WRITE`
    * `cloudkms.cryptoKeyVersions.update - ADMIN_WRITE`
    * `cloudkms.importJobs.useToImport - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="ImportCryptoKeyVersion" `  




#### `ImportTrustedKeyWrappedCryptoKeyVersion`

  * **Method** : `ImportTrustedKeyWrappedCryptoKeyVersion`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `cloudkms.cryptoKeyVersions.create - ADMIN_WRITE`
    * `cloudkms.cryptoKeyVersions.trustedImportExport - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="ImportTrustedKeyWrappedCryptoKeyVersion" `  




#### `ListCryptoKeyVersions`

  * **Method** : `ListCryptoKeyVersions`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `cloudkms.cryptoKeyVersions.list - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="ListCryptoKeyVersions" `  




#### `ListCryptoKeys`

  * **Method** : `ListCryptoKeys`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `cloudkms.cryptoKeys.list - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="ListCryptoKeys" `  




#### `ListImportJobs`

  * **Method** : `ListImportJobs`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `cloudkms.importJobs.list - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="ListImportJobs" `  




#### `ListKeyRings`

  * **Method** : `ListKeyRings`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `cloudkms.keyRings.list - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="ListKeyRings" `  




#### `ListRetiredResources`

  * **Method** : `ListRetiredResources`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `cloudkms.retiredResources.list - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="ListRetiredResources" `  




#### `MacSign`

  * **Method** : `MacSign`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `cloudkms.cryptoKeyVersions.useToSign - DATA_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="MacSign" `  




#### `MacVerify`

  * **Method** : `MacVerify`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `cloudkms.cryptoKeyVersions.useToVerify - DATA_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="MacVerify" `  




#### `RawDecrypt`

  * **Method** : `RawDecrypt`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `cloudkms.cryptoKeyVersions.useToDecrypt - DATA_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="RawDecrypt" `  




#### `RawEncrypt`

  * **Method** : `RawEncrypt`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `cloudkms.cryptoKeyVersions.useToEncrypt - DATA_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="RawEncrypt" `  




#### `RestoreCryptoKeyVersion`

  * **Method** : `RestoreCryptoKeyVersion`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `cloudkms.cryptoKeyVersions.restore - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="RestoreCryptoKeyVersion" `  




#### `UpdateCryptoKey`

  * **Method** : `UpdateCryptoKey`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `cloudkms.cryptoKeys.update - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="UpdateCryptoKey" `  




#### `UpdateCryptoKeyPrimaryVersion`

  * **Method** : `UpdateCryptoKeyPrimaryVersion`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `cloudkms.cryptoKeys.update - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="UpdateCryptoKeyPrimaryVersion" `  




#### `UpdateCryptoKeyVersion`

  * **Method** : `UpdateCryptoKeyVersion`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `cloudkms.cryptoKeyVersions.update - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="UpdateCryptoKeyVersion" `  




### `google.iam.v1.IAMPolicy`

The following audit logs are associated with methods belonging to `google.iam.v1.IAMPolicy`.

#### `GetIamPolicy`

  * **Method** : `GetIamPolicy`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `cloudkms.cryptoKeys.getIamPolicy - ADMIN_READ`
    * `cloudkms.keyRings.getIamPolicy - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="GetIamPolicy" `  




#### `SetIamPolicy`

  * **Method** : `SetIamPolicy`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `cloudkms.cryptoKeys.setIamPolicy - ADMIN_WRITE`
    * `cloudkms.keyRings.setIamPolicy - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="SetIamPolicy" `  




### `google.longrunning.Operations`

The following audit logs are associated with methods belonging to `google.longrunning.Operations`.

#### `GetOperation`

  * **Method** : `GetOperation`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `cloudkms.operations.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="GetOperation" `  




## Methods that don't produce audit logs

A method might not produce audit logs for one or more of the following reasons: 

  * It is a high volume method involving significant log generation and storage costs.
  * It has low auditing value.
  * Another audit or platform log already provides method coverage.



The following methods don't produce audit logs:

  * `google.cloud.kms.v1.KeyManagementService.GenerateRandomBytes`
  * `google.cloud.location.Locations.GetLocation`
  * `google.cloud.location.Locations.ListLocations`



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
