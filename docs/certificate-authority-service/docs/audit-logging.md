---
url: https://docs.cloud.google.com/certificate-authority-service/docs/audit-logging/
title: Certificate Authority Service audit logging \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T14:59:37.186871+00:00
---

# Certificate Authority Service audit logging  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/certificate-authority-service/docs/audit-logging/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Certificate Authority Service ](https://docs.cloud.google.com/certificate-authority-service/docs)
  * [ Guides ](https://docs.cloud.google.com/certificate-authority-service/docs/ca-service-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Certificate Authority Service audit logging

This document lists the audited methods for Certificate Authority Service. Google Cloud services generate audit logs that record administrative and access activities within your Google Cloud resources. For more information about Cloud Audit Logs, see the following: 

  * [Types of audit logs](https://docs.cloud.google.com/logging/docs/audit#types)
  * [Audit log entry structure](https://docs.cloud.google.com/logging/docs/audit#audit_log_entry_structure)
  * [Storing and routing audit logs](https://docs.cloud.google.com/logging/docs/audit#storing_and_routing_audit_logs)
  * [Cloud Logging pricing summary](https://docs.cloud.google.com/stackdriver/pricing#logs-pricing-summary)
  * [Enable Data Access audit logs](https://docs.cloud.google.com/logging/docs/audit/configure-data-access)



## Service name

To view the Certificate Authority Service audit logs, do the following:

  1. In the Google Cloud console, go to the Logs Explorer page:

[Go to Logs Explorer](https://console.cloud.google.com/logs/query)

  2. Copy and paste the following query into the **Query** field of the Logs Explorer, and then click **Run query**.
         
         protoPayload.serviceName="privateca.googleapis.com"
           




## Methods by permission type

Each IAM permission has a `type` property, whose value is an enum that can be one of four values: `ADMIN_READ`, `ADMIN_WRITE`, `DATA_READ`, or `DATA_WRITE`. When you call a method, Certificate Authority Service generates an audit log whose category is dependent on the `type` property of the permission required to perform the method. Methods that require an IAM permission with the `type` property value of `DATA_READ`, `DATA_WRITE`, or `ADMIN_READ` generate [Data Access](https://docs.cloud.google.com/logging/docs/audit#data-access) audit logs. Methods that require an IAM permission with the `type` property value of `ADMIN_WRITE` generate [Admin Activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity) audit logs.

API methods in the following list that are marked with (LRO) are long-running operations (LROs). These methods usually generate two audit log entries: one when the operation starts and another when it ends. For more information see [Audit logs for long-running operations](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro). Permission type | Methods  
---|---  
`ADMIN_READ` | `google.cloud.security.privateca.v1.CertificateAuthorityService.FetchCaCerts`  
`google.cloud.security.privateca.v1.CertificateAuthorityService.FetchCertificateAuthorityCsr`  
`google.cloud.security.privateca.v1.CertificateAuthorityService.GetCaPool`  
`google.cloud.security.privateca.v1.CertificateAuthorityService.GetCertificateAuthority`  
`google.cloud.security.privateca.v1.CertificateAuthorityService.GetCertificateTemplate`  
`google.cloud.security.privateca.v1.CertificateAuthorityService.ListCaPools`  
`google.cloud.security.privateca.v1.CertificateAuthorityService.ListCertificateAuthorities`  
`google.cloud.security.privateca.v1.CertificateAuthorityService.ListCertificateTemplates`  
`GetIamPolicy`  
`google.longrunning.Operations.GetOperation`  
`google.longrunning.Operations.ListOperations`  
`ADMIN_WRITE` | `google.cloud.security.privateca.v1.CertificateAuthorityService.ActivateCertificateAuthority` (LRO)  
`google.cloud.security.privateca.v1.CertificateAuthorityService.CreateCaPool` (LRO)  
`google.cloud.security.privateca.v1.CertificateAuthorityService.CreateCertificateAuthority` (LRO)  
`google.cloud.security.privateca.v1.CertificateAuthorityService.CreateCertificateTemplate` (LRO)  
`google.cloud.security.privateca.v1.CertificateAuthorityService.DeleteCaPool` (LRO)  
`google.cloud.security.privateca.v1.CertificateAuthorityService.DeleteCertificateAuthority` (LRO)  
`google.cloud.security.privateca.v1.CertificateAuthorityService.DeleteCertificateTemplate` (LRO)  
`google.cloud.security.privateca.v1.CertificateAuthorityService.DisableCertificateAuthority` (LRO)  
`google.cloud.security.privateca.v1.CertificateAuthorityService.EnableCertificateAuthority` (LRO)  
`google.cloud.security.privateca.v1.CertificateAuthorityService.UndeleteCertificateAuthority` (LRO)  
`google.cloud.security.privateca.v1.CertificateAuthorityService.UpdateCaPool` (LRO)  
`google.cloud.security.privateca.v1.CertificateAuthorityService.UpdateCertificateAuthority` (LRO)  
`google.cloud.security.privateca.v1.CertificateAuthorityService.UpdateCertificateTemplate` (LRO)  
`SetIamPolicy`  
`google.longrunning.Operations.CancelOperation`  
`google.longrunning.Operations.DeleteOperation`  
`DATA_READ` | `google.cloud.security.privateca.v1.CertificateAuthorityService.GetCertificate`  
`google.cloud.security.privateca.v1.CertificateAuthorityService.GetCertificateRevocationList`  
`google.cloud.security.privateca.v1.CertificateAuthorityService.ListCertificateRevocationLists`  
`google.cloud.security.privateca.v1.CertificateAuthorityService.ListCertificates`  
`DATA_WRITE` | `google.cloud.security.privateca.v1.CertificateAuthorityService.CreateCertificate`  
`google.cloud.security.privateca.v1.CertificateAuthorityService.RevokeCertificate`  
`google.cloud.security.privateca.v1.CertificateAuthorityService.UpdateCertificate`  
`google.cloud.security.privateca.v1.CertificateAuthorityService.UpdateCertificateRevocationList` (LRO)  
  
## API interface audit logs

For information about how and which permissions are evaluated for each method, see the Identity and Access Management documentation for Certificate Authority Service.

### `google.cloud.security.privateca.v1.CertificateAuthorityService`

The following audit logs are associated with methods belonging to `google.cloud.security.privateca.v1.CertificateAuthorityService`.

#### `ActivateCertificateAuthority`

  * **Method** : `google.cloud.security.privateca.v1.CertificateAuthorityService.ActivateCertificateAuthority`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `privateca.certificateAuthorities.update - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.security.privateca.v1.CertificateAuthorityService.ActivateCertificateAuthority" `  




#### `CreateCaPool`

  * **Method** : `google.cloud.security.privateca.v1.CertificateAuthorityService.CreateCaPool`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `privateca.caPools.create - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.security.privateca.v1.CertificateAuthorityService.CreateCaPool" `  




#### `CreateCertificate`

  * **Method** : `google.cloud.security.privateca.v1.CertificateAuthorityService.CreateCertificate`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `privateca.certificates.create - DATA_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.security.privateca.v1.CertificateAuthorityService.CreateCertificate" `  


**Note:** Permission `privateca.certificateTemplates.use` is only needed when method `google.cloud.security.privateca.v1.CertificateAuthorityService.CreateCertificate` is called with a certificate template being specified in the request. In this case, enabling either `DATA_WRITE` or `DATA_READ` will enable this log.

#### `CreateCertificateAuthority`

  * **Method** : `google.cloud.security.privateca.v1.CertificateAuthorityService.CreateCertificateAuthority`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `privateca.certificateAuthorities.create - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.security.privateca.v1.CertificateAuthorityService.CreateCertificateAuthority" `  




#### `CreateCertificateTemplate`

  * **Method** : `google.cloud.security.privateca.v1.CertificateAuthorityService.CreateCertificateTemplate`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `privateca.certificateTemplates.create - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.security.privateca.v1.CertificateAuthorityService.CreateCertificateTemplate" `  




#### `DeleteCaPool`

  * **Method** : `google.cloud.security.privateca.v1.CertificateAuthorityService.DeleteCaPool`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `privateca.caPools.delete - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.security.privateca.v1.CertificateAuthorityService.DeleteCaPool" `  




#### `DeleteCertificateAuthority`

  * **Method** : `google.cloud.security.privateca.v1.CertificateAuthorityService.DeleteCertificateAuthority`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `privateca.certificateAuthorities.delete - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.security.privateca.v1.CertificateAuthorityService.DeleteCertificateAuthority" `  




#### `DeleteCertificateTemplate`

  * **Method** : `google.cloud.security.privateca.v1.CertificateAuthorityService.DeleteCertificateTemplate`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `privateca.certificateTemplates.delete - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.security.privateca.v1.CertificateAuthorityService.DeleteCertificateTemplate" `  




#### `DisableCertificateAuthority`

  * **Method** : `google.cloud.security.privateca.v1.CertificateAuthorityService.DisableCertificateAuthority`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `privateca.certificateAuthorities.update - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.security.privateca.v1.CertificateAuthorityService.DisableCertificateAuthority" `  




#### `EnableCertificateAuthority`

  * **Method** : `google.cloud.security.privateca.v1.CertificateAuthorityService.EnableCertificateAuthority`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `privateca.certificateAuthorities.update - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.security.privateca.v1.CertificateAuthorityService.EnableCertificateAuthority" `  




#### `FetchCaCerts`

  * **Method** : `google.cloud.security.privateca.v1.CertificateAuthorityService.FetchCaCerts`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `privateca.caPools.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.security.privateca.v1.CertificateAuthorityService.FetchCaCerts" `  




#### `FetchCertificateAuthorityCsr`

  * **Method** : `google.cloud.security.privateca.v1.CertificateAuthorityService.FetchCertificateAuthorityCsr`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `privateca.certificateAuthorities.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.security.privateca.v1.CertificateAuthorityService.FetchCertificateAuthorityCsr" `  




#### `GetCaPool`

  * **Method** : `google.cloud.security.privateca.v1.CertificateAuthorityService.GetCaPool`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `privateca.caPools.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.security.privateca.v1.CertificateAuthorityService.GetCaPool" `  




#### `GetCertificate`

  * **Method** : `google.cloud.security.privateca.v1.CertificateAuthorityService.GetCertificate`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `privateca.certificates.get - DATA_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.security.privateca.v1.CertificateAuthorityService.GetCertificate" `  




#### `GetCertificateAuthority`

  * **Method** : `google.cloud.security.privateca.v1.CertificateAuthorityService.GetCertificateAuthority`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `privateca.certificateAuthorities.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.security.privateca.v1.CertificateAuthorityService.GetCertificateAuthority" `  




#### `GetCertificateRevocationList`

  * **Method** : `google.cloud.security.privateca.v1.CertificateAuthorityService.GetCertificateRevocationList`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `privateca.certificateRevocationLists.get - DATA_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.security.privateca.v1.CertificateAuthorityService.GetCertificateRevocationList" `  




#### `GetCertificateTemplate`

  * **Method** : `google.cloud.security.privateca.v1.CertificateAuthorityService.GetCertificateTemplate`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `privateca.certificateTemplates.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.security.privateca.v1.CertificateAuthorityService.GetCertificateTemplate" `  




#### `ListCaPools`

  * **Method** : `google.cloud.security.privateca.v1.CertificateAuthorityService.ListCaPools`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `privateca.caPools.list - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.security.privateca.v1.CertificateAuthorityService.ListCaPools" `  




#### `ListCertificateAuthorities`

  * **Method** : `google.cloud.security.privateca.v1.CertificateAuthorityService.ListCertificateAuthorities`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `privateca.certificateAuthorities.list - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.security.privateca.v1.CertificateAuthorityService.ListCertificateAuthorities" `  




#### `ListCertificateRevocationLists`

  * **Method** : `google.cloud.security.privateca.v1.CertificateAuthorityService.ListCertificateRevocationLists`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `privateca.certificateRevocationLists.list - DATA_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.security.privateca.v1.CertificateAuthorityService.ListCertificateRevocationLists" `  




#### `ListCertificateTemplates`

  * **Method** : `google.cloud.security.privateca.v1.CertificateAuthorityService.ListCertificateTemplates`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `privateca.certificateTemplates.list - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.security.privateca.v1.CertificateAuthorityService.ListCertificateTemplates" `  




#### `ListCertificates`

  * **Method** : `google.cloud.security.privateca.v1.CertificateAuthorityService.ListCertificates`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `privateca.certificates.list - DATA_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.security.privateca.v1.CertificateAuthorityService.ListCertificates" `  




#### `RevokeCertificate`

  * **Method** : `google.cloud.security.privateca.v1.CertificateAuthorityService.RevokeCertificate`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `privateca.certificates.update - DATA_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.security.privateca.v1.CertificateAuthorityService.RevokeCertificate" `  




#### `UndeleteCertificateAuthority`

  * **Method** : `google.cloud.security.privateca.v1.CertificateAuthorityService.UndeleteCertificateAuthority`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `privateca.certificateAuthorities.update - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.security.privateca.v1.CertificateAuthorityService.UndeleteCertificateAuthority" `  




#### `UpdateCaPool`

  * **Method** : `google.cloud.security.privateca.v1.CertificateAuthorityService.UpdateCaPool`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `privateca.caPools.update - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.security.privateca.v1.CertificateAuthorityService.UpdateCaPool" `  




#### `UpdateCertificate`

  * **Method** : `google.cloud.security.privateca.v1.CertificateAuthorityService.UpdateCertificate`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `privateca.certificates.update - DATA_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.security.privateca.v1.CertificateAuthorityService.UpdateCertificate" `  




#### `UpdateCertificateAuthority`

  * **Method** : `google.cloud.security.privateca.v1.CertificateAuthorityService.UpdateCertificateAuthority`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `privateca.certificateAuthorities.update - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.security.privateca.v1.CertificateAuthorityService.UpdateCertificateAuthority" `  




#### `UpdateCertificateRevocationList`

  * **Method** : `google.cloud.security.privateca.v1.CertificateAuthorityService.UpdateCertificateRevocationList`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `privateca.certificateRevocationLists.update - DATA_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.security.privateca.v1.CertificateAuthorityService.UpdateCertificateRevocationList" `  




#### `UpdateCertificateTemplate`

  * **Method** : `google.cloud.security.privateca.v1.CertificateAuthorityService.UpdateCertificateTemplate`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `privateca.certificateTemplates.update - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.security.privateca.v1.CertificateAuthorityService.UpdateCertificateTemplate" `  




### `google.iam.v1.IAMPolicy`

The following audit logs are associated with methods belonging to `google.iam.v1.IAMPolicy`.

#### `GetIamPolicy`

  * **Method** : `GetIamPolicy`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `privateca.caPools.getIamPolicy - ADMIN_READ`
    * `privateca.certificateRevocationLists.getIamPolicy - ADMIN_READ`
    * `privateca.certificateTemplates.getIamPolicy - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="GetIamPolicy" `  




#### `SetIamPolicy`

  * **Method** : `SetIamPolicy`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `privateca.caPools.setIamPolicy - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="SetIamPolicy" `  




### `google.longrunning.Operations`

The following audit logs are associated with methods belonging to `google.longrunning.Operations`.

#### `CancelOperation`

  * **Method** : `google.longrunning.Operations.CancelOperation`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `privateca.operations.cancel - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.longrunning.Operations.CancelOperation" `  




#### `DeleteOperation`

  * **Method** : `google.longrunning.Operations.DeleteOperation`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `privateca.operations.delete - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.longrunning.Operations.DeleteOperation" `  




#### `GetOperation`

  * **Method** : `google.longrunning.Operations.GetOperation`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `privateca.operations.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.longrunning.Operations.GetOperation" `  




#### `ListOperations`

  * **Method** : `google.longrunning.Operations.ListOperations`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `privateca.operations.list - ADMIN_READ`
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

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
