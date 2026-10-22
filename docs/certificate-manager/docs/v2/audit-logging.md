---
url: https://docs.cloud.google.com/certificate-manager/docs/v2/audit-logging/
title: Audit logging \u00a0|\u00a0 Certificate Manager (2nd gen) \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:11:40.490934+00:00
---

# Audit logging  |  Certificate Manager (2nd gen)  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/certificate-manager/docs/v2/audit-logging/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Certificate Manager ](https://docs.cloud.google.com/certificate-manager)
  * [ Certificate Manager (2nd gen) ](https://docs.cloud.google.com/certificate-manager/docs/v2/overview)



Send feedback 

#  Audit logging Stay organized with collections  Save and categorize content based on your preferences. 

****

This product or feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA products and features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

This document lists the audited methods for Certificate Manager. Google Cloud services generate audit logs that record administrative and access activities within your Google Cloud resources. For more information about Cloud Audit Logs, see the following: 

  * [Types of audit logs](https://docs.cloud.google.com/logging/docs/audit#types)
  * [Audit log entry structure](https://docs.cloud.google.com/logging/docs/audit#audit_log_entry_structure)
  * [Storing and routing audit logs](https://docs.cloud.google.com/logging/docs/audit#storing_and_routing_audit_logs)
  * [Cloud Logging pricing summary](https://docs.cloud.google.com/stackdriver/pricing#logs-pricing-summary)
  * [Enable Data Access audit logs](https://docs.cloud.google.com/logging/docs/audit/configure-data-access)



## Service name

To view the Certificate Manager audit logs, do the following:

  1. In the Google Cloud console, go to the Logs Explorer page:

[Go to Logs Explorer](https://console.cloud.google.com/logs/query)

  2. Copy and paste the following query into the **Query** field of the Logs Explorer, and then click **Run query**.
         
         protoPayload.serviceName="certificatemanager.googleapis.com"
           




## Methods by permission type

Each IAM permission has a `type` property, whose value is an enum that can be one of four values: `ADMIN_READ`, `ADMIN_WRITE`, `DATA_READ`, or `DATA_WRITE`. When you call a method, Certificate Manager generates an audit log whose category is dependent on the `type` property of the permission required to perform the method. Methods that require an IAM permission with the `type` property value of `DATA_READ`, `DATA_WRITE`, or `ADMIN_READ` generate [Data Access](https://docs.cloud.google.com/logging/docs/audit#data-access) audit logs. Methods that require an IAM permission with the `type` property value of `ADMIN_WRITE` generate [Admin Activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity) audit logs.

API methods in the following list that are marked with (LRO) are long-running operations (LROs). These methods usually generate two audit log entries: one when the operation starts and another when it ends. For more information see [Audit logs for long-running operations](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro). Permission type | Methods  
---|---  
`ADMIN_READ` | `google.cloud.certificatemanager.v1.CertificateManager.GetCertificate`  
`google.cloud.certificatemanager.v1.CertificateManager.GetCertificateIssuanceConfig`  
`google.cloud.certificatemanager.v1.CertificateManager.GetCertificateMap`  
`google.cloud.certificatemanager.v1.CertificateManager.GetCertificateMapEntry`  
`google.cloud.certificatemanager.v1.CertificateManager.GetDnsAuthorization`  
`google.cloud.certificatemanager.v1.CertificateManager.GetTrustConfig`  
`google.cloud.certificatemanager.v1.CertificateManager.ListCertificateIssuanceConfigs`  
`google.cloud.certificatemanager.v1.CertificateManager.ListCertificateMapEntries`  
`google.cloud.certificatemanager.v1.CertificateManager.ListCertificateMaps`  
`google.cloud.certificatemanager.v1.CertificateManager.ListCertificates`  
`google.cloud.certificatemanager.v1.CertificateManager.ListDnsAuthorizations`  
`google.cloud.certificatemanager.v1.CertificateManager.ListTrustConfigs`  
`google.cloud.certificatemanager.v2alpha.CertificateLifecycle.GetObservedCertificate`  
`google.cloud.certificatemanager.v2alpha.CertificateLifecycle.ListObservedCertificates`  
`google.longrunning.Operations.GetOperation`  
`google.longrunning.Operations.ListOperations`  
`ADMIN_WRITE` | `google.cloud.certificatemanager.v1.CertificateManager.CreateCertificate` (LRO)  
`google.cloud.certificatemanager.v1.CertificateManager.CreateCertificateIssuanceConfig` (LRO)  
`google.cloud.certificatemanager.v1.CertificateManager.CreateCertificateMap` (LRO)  
`google.cloud.certificatemanager.v1.CertificateManager.CreateCertificateMapEntry` (LRO)  
`google.cloud.certificatemanager.v1.CertificateManager.CreateDnsAuthorization` (LRO)  
`google.cloud.certificatemanager.v1.CertificateManager.CreateTrustConfig` (LRO)  
`google.cloud.certificatemanager.v1.CertificateManager.DeleteCertificate` (LRO)  
`google.cloud.certificatemanager.v1.CertificateManager.DeleteCertificateIssuanceConfig` (LRO)  
`google.cloud.certificatemanager.v1.CertificateManager.DeleteCertificateMap` (LRO)  
`google.cloud.certificatemanager.v1.CertificateManager.DeleteCertificateMapEntry` (LRO)  
`google.cloud.certificatemanager.v1.CertificateManager.DeleteDnsAuthorization` (LRO)  
`google.cloud.certificatemanager.v1.CertificateManager.DeleteTrustConfig` (LRO)  
`google.cloud.certificatemanager.v1.CertificateManager.UpdateCertificate` (LRO)  
`google.cloud.certificatemanager.v1.CertificateManager.UpdateCertificateIssuanceConfig` (LRO)  
`google.cloud.certificatemanager.v1.CertificateManager.UpdateCertificateMap` (LRO)  
`google.cloud.certificatemanager.v1.CertificateManager.UpdateCertificateMapEntry` (LRO)  
`google.cloud.certificatemanager.v1.CertificateManager.UpdateDnsAuthorization` (LRO)  
`google.cloud.certificatemanager.v1.CertificateManager.UpdateTrustConfig` (LRO)  
`google.longrunning.Operations.CancelOperation`  
`google.longrunning.Operations.DeleteOperation`  
  
## API interface audit logs

For information about how and which permissions are evaluated for each method, see the Identity and Access Management documentation for Certificate Manager.

### `google.cloud.certificatemanager.v1.CertificateManager`

The following audit logs are associated with methods belonging to `google.cloud.certificatemanager.v1.CertificateManager`.

#### `CreateCertificate`

  * **Method** : `[google.cloud.certificatemanager.v1.CertificateManager.CreateCertificate](https://docs.cloud.google.com/certificate-manager/docs/reference/certificate-manager/rpc/google.cloud.certificatemanager.v1#google.cloud.certificatemanager.v1.CertificateManager.CreateCertificate)`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `certificatemanager.certs.create - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.certificatemanager.v1.CertificateManager.CreateCertificate" `  




#### `CreateCertificateIssuanceConfig`

  * **Method** : `[google.cloud.certificatemanager.v1.CertificateManager.CreateCertificateIssuanceConfig](https://docs.cloud.google.com/certificate-manager/docs/reference/certificate-manager/rpc/google.cloud.certificatemanager.v1#google.cloud.certificatemanager.v1.CertificateManager.CreateCertificateIssuanceConfig)`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `certificatemanager.certissuanceconfigs.create - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.certificatemanager.v1.CertificateManager.CreateCertificateIssuanceConfig" `  




#### `CreateCertificateMap`

  * **Method** : `[google.cloud.certificatemanager.v1.CertificateManager.CreateCertificateMap](https://docs.cloud.google.com/certificate-manager/docs/reference/certificate-manager/rpc/google.cloud.certificatemanager.v1#google.cloud.certificatemanager.v1.CertificateManager.CreateCertificateMap)`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `certificatemanager.certmaps.create - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.certificatemanager.v1.CertificateManager.CreateCertificateMap" `  




#### `CreateCertificateMapEntry`

  * **Method** : `[google.cloud.certificatemanager.v1.CertificateManager.CreateCertificateMapEntry](https://docs.cloud.google.com/certificate-manager/docs/reference/certificate-manager/rpc/google.cloud.certificatemanager.v1#google.cloud.certificatemanager.v1.CertificateManager.CreateCertificateMapEntry)`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `certificatemanager.certmapentries.create - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.certificatemanager.v1.CertificateManager.CreateCertificateMapEntry" `  




#### `CreateDnsAuthorization`

  * **Method** : `[google.cloud.certificatemanager.v1.CertificateManager.CreateDnsAuthorization](https://docs.cloud.google.com/certificate-manager/docs/reference/certificate-manager/rpc/google.cloud.certificatemanager.v1#google.cloud.certificatemanager.v1.CertificateManager.CreateDnsAuthorization)`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `certificatemanager.dnsauthorizations.create - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.certificatemanager.v1.CertificateManager.CreateDnsAuthorization" `  




#### `CreateTrustConfig`

  * **Method** : `[google.cloud.certificatemanager.v1.CertificateManager.CreateTrustConfig](https://docs.cloud.google.com/certificate-manager/docs/reference/certificate-manager/rpc/google.cloud.certificatemanager.v1#google.cloud.certificatemanager.v1.CertificateManager.CreateTrustConfig)`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `certificatemanager.trustconfigs.create - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.certificatemanager.v1.CertificateManager.CreateTrustConfig" `  




#### `DeleteCertificate`

  * **Method** : `[google.cloud.certificatemanager.v1.CertificateManager.DeleteCertificate](https://docs.cloud.google.com/certificate-manager/docs/reference/certificate-manager/rpc/google.cloud.certificatemanager.v1#google.cloud.certificatemanager.v1.CertificateManager.DeleteCertificate)`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `certificatemanager.certs.delete - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.certificatemanager.v1.CertificateManager.DeleteCertificate" `  




#### `DeleteCertificateIssuanceConfig`

  * **Method** : `[google.cloud.certificatemanager.v1.CertificateManager.DeleteCertificateIssuanceConfig](https://docs.cloud.google.com/certificate-manager/docs/reference/certificate-manager/rpc/google.cloud.certificatemanager.v1#google.cloud.certificatemanager.v1.CertificateManager.DeleteCertificateIssuanceConfig)`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `certificatemanager.certissuanceconfigs.delete - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.certificatemanager.v1.CertificateManager.DeleteCertificateIssuanceConfig" `  




#### `DeleteCertificateMap`

  * **Method** : `[google.cloud.certificatemanager.v1.CertificateManager.DeleteCertificateMap](https://docs.cloud.google.com/certificate-manager/docs/reference/certificate-manager/rpc/google.cloud.certificatemanager.v1#google.cloud.certificatemanager.v1.CertificateManager.DeleteCertificateMap)`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `certificatemanager.certmaps.delete - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.certificatemanager.v1.CertificateManager.DeleteCertificateMap" `  




#### `DeleteCertificateMapEntry`

  * **Method** : `[google.cloud.certificatemanager.v1.CertificateManager.DeleteCertificateMapEntry](https://docs.cloud.google.com/certificate-manager/docs/reference/certificate-manager/rpc/google.cloud.certificatemanager.v1#google.cloud.certificatemanager.v1.CertificateManager.DeleteCertificateMapEntry)`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `certificatemanager.certmapentries.delete - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.certificatemanager.v1.CertificateManager.DeleteCertificateMapEntry" `  




#### `DeleteDnsAuthorization`

  * **Method** : `[google.cloud.certificatemanager.v1.CertificateManager.DeleteDnsAuthorization](https://docs.cloud.google.com/certificate-manager/docs/reference/certificate-manager/rpc/google.cloud.certificatemanager.v1#google.cloud.certificatemanager.v1.CertificateManager.DeleteDnsAuthorization)`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `certificatemanager.dnsauthorizations.delete - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.certificatemanager.v1.CertificateManager.DeleteDnsAuthorization" `  




#### `DeleteTrustConfig`

  * **Method** : `[google.cloud.certificatemanager.v1.CertificateManager.DeleteTrustConfig](https://docs.cloud.google.com/certificate-manager/docs/reference/certificate-manager/rpc/google.cloud.certificatemanager.v1#google.cloud.certificatemanager.v1.CertificateManager.DeleteTrustConfig)`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `certificatemanager.trustconfigs.delete - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.certificatemanager.v1.CertificateManager.DeleteTrustConfig" `  




#### `GetCertificate`

  * **Method** : `[google.cloud.certificatemanager.v1.CertificateManager.GetCertificate](https://docs.cloud.google.com/certificate-manager/docs/reference/certificate-manager/rpc/google.cloud.certificatemanager.v1#google.cloud.certificatemanager.v1.CertificateManager.GetCertificate)`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `certificatemanager.certs.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.certificatemanager.v1.CertificateManager.GetCertificate" `  




#### `GetCertificateIssuanceConfig`

  * **Method** : `[google.cloud.certificatemanager.v1.CertificateManager.GetCertificateIssuanceConfig](https://docs.cloud.google.com/certificate-manager/docs/reference/certificate-manager/rpc/google.cloud.certificatemanager.v1#google.cloud.certificatemanager.v1.CertificateManager.GetCertificateIssuanceConfig)`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `certificatemanager.certissuanceconfigs.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.certificatemanager.v1.CertificateManager.GetCertificateIssuanceConfig" `  




#### `GetCertificateMap`

  * **Method** : `[google.cloud.certificatemanager.v1.CertificateManager.GetCertificateMap](https://docs.cloud.google.com/certificate-manager/docs/reference/certificate-manager/rpc/google.cloud.certificatemanager.v1#google.cloud.certificatemanager.v1.CertificateManager.GetCertificateMap)`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `certificatemanager.certmaps.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.certificatemanager.v1.CertificateManager.GetCertificateMap" `  




#### `GetCertificateMapEntry`

  * **Method** : `[google.cloud.certificatemanager.v1.CertificateManager.GetCertificateMapEntry](https://docs.cloud.google.com/certificate-manager/docs/reference/certificate-manager/rpc/google.cloud.certificatemanager.v1#google.cloud.certificatemanager.v1.CertificateManager.GetCertificateMapEntry)`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `certificatemanager.certmapentries.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.certificatemanager.v1.CertificateManager.GetCertificateMapEntry" `  




#### `GetDnsAuthorization`

  * **Method** : `[google.cloud.certificatemanager.v1.CertificateManager.GetDnsAuthorization](https://docs.cloud.google.com/certificate-manager/docs/reference/certificate-manager/rpc/google.cloud.certificatemanager.v1#google.cloud.certificatemanager.v1.CertificateManager.GetDnsAuthorization)`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `certificatemanager.dnsauthorizations.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.certificatemanager.v1.CertificateManager.GetDnsAuthorization" `  




#### `GetTrustConfig`

  * **Method** : `[google.cloud.certificatemanager.v1.CertificateManager.GetTrustConfig](https://docs.cloud.google.com/certificate-manager/docs/reference/certificate-manager/rpc/google.cloud.certificatemanager.v1#google.cloud.certificatemanager.v1.CertificateManager.GetTrustConfig)`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `certificatemanager.trustconfigs.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.certificatemanager.v1.CertificateManager.GetTrustConfig" `  




#### `ListCertificateIssuanceConfigs`

  * **Method** : `[google.cloud.certificatemanager.v1.CertificateManager.ListCertificateIssuanceConfigs](https://docs.cloud.google.com/certificate-manager/docs/reference/certificate-manager/rpc/google.cloud.certificatemanager.v1#google.cloud.certificatemanager.v1.CertificateManager.ListCertificateIssuanceConfigs)`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `certificatemanager.certissuanceconfigs.list - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.certificatemanager.v1.CertificateManager.ListCertificateIssuanceConfigs" `  




#### `ListCertificateMapEntries`

  * **Method** : `[google.cloud.certificatemanager.v1.CertificateManager.ListCertificateMapEntries](https://docs.cloud.google.com/certificate-manager/docs/reference/certificate-manager/rpc/google.cloud.certificatemanager.v1#google.cloud.certificatemanager.v1.CertificateManager.ListCertificateMapEntries)`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `certificatemanager.certmapentries.list - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.certificatemanager.v1.CertificateManager.ListCertificateMapEntries" `  




#### `ListCertificateMaps`

  * **Method** : `[google.cloud.certificatemanager.v1.CertificateManager.ListCertificateMaps](https://docs.cloud.google.com/certificate-manager/docs/reference/certificate-manager/rpc/google.cloud.certificatemanager.v1#google.cloud.certificatemanager.v1.CertificateManager.ListCertificateMaps)`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `certificatemanager.certmaps.list - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.certificatemanager.v1.CertificateManager.ListCertificateMaps" `  




#### `ListCertificates`

  * **Method** : `[google.cloud.certificatemanager.v1.CertificateManager.ListCertificates](https://docs.cloud.google.com/certificate-manager/docs/reference/certificate-manager/rpc/google.cloud.certificatemanager.v1#google.cloud.certificatemanager.v1.CertificateManager.ListCertificates)`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `certificatemanager.certs.list - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.certificatemanager.v1.CertificateManager.ListCertificates" `  




#### `ListDnsAuthorizations`

  * **Method** : `[google.cloud.certificatemanager.v1.CertificateManager.ListDnsAuthorizations](https://docs.cloud.google.com/certificate-manager/docs/reference/certificate-manager/rpc/google.cloud.certificatemanager.v1#google.cloud.certificatemanager.v1.CertificateManager.ListDnsAuthorizations)`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `certificatemanager.dnsauthorizations.list - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.certificatemanager.v1.CertificateManager.ListDnsAuthorizations" `  




#### `ListTrustConfigs`

  * **Method** : `[google.cloud.certificatemanager.v1.CertificateManager.ListTrustConfigs](https://docs.cloud.google.com/certificate-manager/docs/reference/certificate-manager/rpc/google.cloud.certificatemanager.v1#google.cloud.certificatemanager.v1.CertificateManager.ListTrustConfigs)`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `certificatemanager.trustconfigs.list - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.certificatemanager.v1.CertificateManager.ListTrustConfigs" `  




#### `UpdateCertificate`

  * **Method** : `[google.cloud.certificatemanager.v1.CertificateManager.UpdateCertificate](https://docs.cloud.google.com/certificate-manager/docs/reference/certificate-manager/rpc/google.cloud.certificatemanager.v1#google.cloud.certificatemanager.v1.CertificateManager.UpdateCertificate)`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `certificatemanager.certs.update - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.certificatemanager.v1.CertificateManager.UpdateCertificate" `  




#### `UpdateCertificateIssuanceConfig`

  * **Method** : `[google.cloud.certificatemanager.v1.CertificateManager.UpdateCertificateIssuanceConfig](https://docs.cloud.google.com/certificate-manager/docs/reference/certificate-manager/rpc/google.cloud.certificatemanager.v1#google.cloud.certificatemanager.v1.CertificateManager.UpdateCertificateIssuanceConfig)`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `certificatemanager.certissuanceconfigs.update - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.certificatemanager.v1.CertificateManager.UpdateCertificateIssuanceConfig" `  




#### `UpdateCertificateMap`

  * **Method** : `[google.cloud.certificatemanager.v1.CertificateManager.UpdateCertificateMap](https://docs.cloud.google.com/certificate-manager/docs/reference/certificate-manager/rpc/google.cloud.certificatemanager.v1#google.cloud.certificatemanager.v1.CertificateManager.UpdateCertificateMap)`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `certificatemanager.certmaps.update - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.certificatemanager.v1.CertificateManager.UpdateCertificateMap" `  




#### `UpdateCertificateMapEntry`

  * **Method** : `[google.cloud.certificatemanager.v1.CertificateManager.UpdateCertificateMapEntry](https://docs.cloud.google.com/certificate-manager/docs/reference/certificate-manager/rpc/google.cloud.certificatemanager.v1#google.cloud.certificatemanager.v1.CertificateManager.UpdateCertificateMapEntry)`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `certificatemanager.certmapentries.update - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.certificatemanager.v1.CertificateManager.UpdateCertificateMapEntry" `  




#### `UpdateDnsAuthorization`

  * **Method** : `[google.cloud.certificatemanager.v1.CertificateManager.UpdateDnsAuthorization](https://docs.cloud.google.com/certificate-manager/docs/reference/certificate-manager/rpc/google.cloud.certificatemanager.v1#google.cloud.certificatemanager.v1.CertificateManager.UpdateDnsAuthorization)`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `certificatemanager.dnsauthorizations.update - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.certificatemanager.v1.CertificateManager.UpdateDnsAuthorization" `  




#### `UpdateTrustConfig`

  * **Method** : `[google.cloud.certificatemanager.v1.CertificateManager.UpdateTrustConfig](https://docs.cloud.google.com/certificate-manager/docs/reference/certificate-manager/rpc/google.cloud.certificatemanager.v1#google.cloud.certificatemanager.v1.CertificateManager.UpdateTrustConfig)`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `certificatemanager.trustconfigs.update - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.certificatemanager.v1.CertificateManager.UpdateTrustConfig" `  




### `google.cloud.certificatemanager.v2alpha.CertificateLifecycle`

The following audit logs are associated with methods belonging to `google.cloud.certificatemanager.v2alpha.CertificateLifecycle`.

#### `GetObservedCertificate`

  * **Method** : `[google.cloud.certificatemanager.v2alpha.CertificateLifecycle.GetObservedCertificate](https://docs.cloud.google.com/certificate-manager/docs/reference/certificate-manager/rpc/google.cloud.certificatemanager.v2alpha#google.cloud.certificatemanager.v2alpha.CertificateLifecycle.GetObservedCertificate)`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `certificatemanager.observedcerts.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.certificatemanager.v2alpha.CertificateLifecycle.GetObservedCertificate" `  




#### `ListObservedCertificates`

  * **Method** : `[google.cloud.certificatemanager.v2alpha.CertificateLifecycle.ListObservedCertificates](https://docs.cloud.google.com/certificate-manager/docs/reference/certificate-manager/rpc/google.cloud.certificatemanager.v2alpha#google.cloud.certificatemanager.v2alpha.CertificateLifecycle.ListObservedCertificates)`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `certificatemanager.observedcerts.list - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.certificatemanager.v2alpha.CertificateLifecycle.ListObservedCertificates" `  




### `google.longrunning.Operations`

The following audit logs are associated with methods belonging to `google.longrunning.Operations`.

#### `CancelOperation`

  * **Method** : `google.longrunning.Operations.CancelOperation`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `certificatemanager.operations.cancel - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.longrunning.Operations.CancelOperation" `  




#### `DeleteOperation`

  * **Method** : `google.longrunning.Operations.DeleteOperation`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `certificatemanager.operations.delete - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.longrunning.Operations.DeleteOperation" `  




#### `GetOperation`

  * **Method** : `google.longrunning.Operations.GetOperation`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `certificatemanager.operations.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.longrunning.Operations.GetOperation" `  




#### `ListOperations`

  * **Method** : `google.longrunning.Operations.ListOperations`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `certificatemanager.operations.list - ADMIN_READ`
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



## Sample queries

Query description | Expression  
---|---  
Certificate Manager audit logs | 
    
    
    logName="projects/PROJECT_ID/logs/cloudaudit.googleapis.com%2Factivity"
    resource.type="certificate_manager_certificate"
    protoPayload.serviceName="certificatemanager.googleapis.com"  
  
## What's next

  * [How Certificate Manager (2nd gen) works](https://docs.cloud.google.com/certificate-manager/docs/v2/core-components)
  * [Roles and permissions](https://docs.cloud.google.com/certificate-manager/docs/v2/roles)
  * [Monitor resources using Cloud Monitoring](https://docs.cloud.google.com/certificate-manager/docs/v2/cloud-monitoring)
  * [Troubleshoot issues](https://docs.cloud.google.com/certificate-manager/docs/v2/troubleshoot)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
