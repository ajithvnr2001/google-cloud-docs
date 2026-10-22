---
url: https://docs.cloud.google.com/api-gateway/docs/audit-logging/
title: API Gateway audit logging \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:29:03.688499+00:00
---

# API Gateway audit logging  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/api-gateway/docs/audit-logging/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ API Gateway ](https://docs.cloud.google.com/api-gateway/docs)
  * [ Guides ](https://docs.cloud.google.com/api-gateway/docs/secure-traffic-gcloud)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# API Gateway audit logging

This document lists the audited methods for API Gateway. Google Cloud services generate audit logs that record administrative and access activities within your Google Cloud resources. For more information about Cloud Audit Logs, see the following: 

  * [Types of audit logs](https://docs.cloud.google.com/logging/docs/audit#types)
  * [Audit log entry structure](https://docs.cloud.google.com/logging/docs/audit#audit_log_entry_structure)
  * [Storing and routing audit logs](https://docs.cloud.google.com/logging/docs/audit#storing_and_routing_audit_logs)
  * [Cloud Logging pricing summary](https://docs.cloud.google.com/stackdriver/pricing#logs-pricing-summary)
  * [Enable Data Access audit logs](https://docs.cloud.google.com/logging/docs/audit/configure-data-access)



## Service name

To view the API Gateway audit logs, do the following:

  1. In the Google Cloud console, go to the Logs Explorer page:

[Go to Logs Explorer](https://console.cloud.google.com/logs/query)

  2. Copy and paste the following query into the **Query** field of the Logs Explorer, and then click **Run query**.
         
         protoPayload.serviceName="apigateway.googleapis.com"
           




## Methods by permission type

Each IAM permission has a `type` property, whose value is an enum that can be one of four values: `ADMIN_READ`, `ADMIN_WRITE`, `DATA_READ`, or `DATA_WRITE`. When you call a method, API Gateway generates an audit log whose category is dependent on the `type` property of the permission required to perform the method. Methods that require an IAM permission with the `type` property value of `DATA_READ`, `DATA_WRITE`, or `ADMIN_READ` generate [Data Access](https://docs.cloud.google.com/logging/docs/audit#data-access) audit logs. Methods that require an IAM permission with the `type` property value of `ADMIN_WRITE` generate [Admin Activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity) audit logs.

API methods in the following list that are marked with (LRO) are long-running operations (LROs). These methods usually generate two audit log entries: one when the operation starts and another when it ends. For more information see [Audit logs for long-running operations](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro). Permission type | Methods  
---|---  
`ADMIN_READ` | `google.cloud.apigateway.v1.ApiGatewayService.GetApi`  
`google.cloud.apigateway.v1.ApiGatewayService.GetApiConfig`  
`google.cloud.apigateway.v1.ApiGatewayService.GetGateway`  
`google.cloud.apigateway.v1.ApiGatewayService.ListApiConfigs`  
`google.cloud.apigateway.v1.ApiGatewayService.ListApis`  
`google.cloud.apigateway.v1.ApiGatewayService.ListGateways`  
`google.cloud.apigateway.v1beta.ApiGatewayService.GetApi`  
`google.cloud.apigateway.v1beta.ApiGatewayService.GetApiConfig`  
`google.cloud.apigateway.v1beta.ApiGatewayService.GetGateway`  
`google.cloud.apigateway.v1beta.ApiGatewayService.ListApiConfigs`  
`google.cloud.apigateway.v1beta.ApiGatewayService.ListApis`  
`google.cloud.apigateway.v1beta.ApiGatewayService.ListGateways`  
`GetIamPolicy`  
`google.longrunning.Operations.GetOperation`  
`google.longrunning.Operations.ListOperations`  
`ADMIN_WRITE` | `google.cloud.apigateway.v1.ApiGatewayService.CreateApi` (LRO)  
`google.cloud.apigateway.v1.ApiGatewayService.CreateApiConfig` (LRO)  
`google.cloud.apigateway.v1.ApiGatewayService.CreateGateway` (LRO)  
`google.cloud.apigateway.v1.ApiGatewayService.DeleteApi` (LRO)  
`google.cloud.apigateway.v1.ApiGatewayService.DeleteApiConfig` (LRO)  
`google.cloud.apigateway.v1.ApiGatewayService.DeleteGateway` (LRO)  
`google.cloud.apigateway.v1.ApiGatewayService.UpdateApi` (LRO)  
`google.cloud.apigateway.v1.ApiGatewayService.UpdateApiConfig` (LRO)  
`google.cloud.apigateway.v1.ApiGatewayService.UpdateGateway` (LRO)  
`google.cloud.apigateway.v1beta.ApiGatewayService.CreateApi` (LRO)  
`google.cloud.apigateway.v1beta.ApiGatewayService.CreateApiConfig` (LRO)  
`google.cloud.apigateway.v1beta.ApiGatewayService.CreateGateway` (LRO)  
`google.cloud.apigateway.v1beta.ApiGatewayService.DeleteApi` (LRO)  
`google.cloud.apigateway.v1beta.ApiGatewayService.DeleteApiConfig` (LRO)  
`google.cloud.apigateway.v1beta.ApiGatewayService.DeleteGateway` (LRO)  
`google.cloud.apigateway.v1beta.ApiGatewayService.UpdateApi` (LRO)  
`google.cloud.apigateway.v1beta.ApiGatewayService.UpdateApiConfig` (LRO)  
`google.cloud.apigateway.v1beta.ApiGatewayService.UpdateGateway` (LRO)  
`SetIamPolicy`  
`google.longrunning.Operations.CancelOperation`  
`google.longrunning.Operations.DeleteOperation`  
  
## API interface audit logs

For information about how and which permissions are evaluated for each method, see the Identity and Access Management documentation for API Gateway.

### `google.cloud.apigateway.v1.ApiGatewayService`

The following audit logs are associated with methods belonging to `google.cloud.apigateway.v1.ApiGatewayService`.

#### `CreateApi`

  * **Method** : `google.cloud.apigateway.v1.ApiGatewayService.CreateApi`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `apigateway.apis.create - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.apigateway.v1.ApiGatewayService.CreateApi" `  




#### `CreateApiConfig`

  * **Method** : `google.cloud.apigateway.v1.ApiGatewayService.CreateApiConfig`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `apigateway.apiconfigs.create - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.apigateway.v1.ApiGatewayService.CreateApiConfig" `  




#### `CreateGateway`

  * **Method** : `google.cloud.apigateway.v1.ApiGatewayService.CreateGateway`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `apigateway.gateways.create - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.apigateway.v1.ApiGatewayService.CreateGateway" `  




#### `DeleteApi`

  * **Method** : `google.cloud.apigateway.v1.ApiGatewayService.DeleteApi`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `apigateway.apis.delete - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.apigateway.v1.ApiGatewayService.DeleteApi" `  




#### `DeleteApiConfig`

  * **Method** : `google.cloud.apigateway.v1.ApiGatewayService.DeleteApiConfig`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `apigateway.apiconfigs.delete - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.apigateway.v1.ApiGatewayService.DeleteApiConfig" `  




#### `DeleteGateway`

  * **Method** : `google.cloud.apigateway.v1.ApiGatewayService.DeleteGateway`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `apigateway.gateways.delete - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.apigateway.v1.ApiGatewayService.DeleteGateway" `  




#### `GetApi`

  * **Method** : `google.cloud.apigateway.v1.ApiGatewayService.GetApi`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `apigateway.apis.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.apigateway.v1.ApiGatewayService.GetApi" `  




#### `GetApiConfig`

  * **Method** : `google.cloud.apigateway.v1.ApiGatewayService.GetApiConfig`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `apigateway.apiconfigs.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.apigateway.v1.ApiGatewayService.GetApiConfig" `  




#### `GetGateway`

  * **Method** : `google.cloud.apigateway.v1.ApiGatewayService.GetGateway`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `apigateway.gateways.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.apigateway.v1.ApiGatewayService.GetGateway" `  




#### `ListApiConfigs`

  * **Method** : `google.cloud.apigateway.v1.ApiGatewayService.ListApiConfigs`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `apigateway.apiconfigs.list - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.apigateway.v1.ApiGatewayService.ListApiConfigs" `  




#### `ListApis`

  * **Method** : `google.cloud.apigateway.v1.ApiGatewayService.ListApis`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `apigateway.apis.list - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.apigateway.v1.ApiGatewayService.ListApis" `  




#### `ListGateways`

  * **Method** : `google.cloud.apigateway.v1.ApiGatewayService.ListGateways`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `apigateway.gateways.list - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.apigateway.v1.ApiGatewayService.ListGateways" `  




#### `UpdateApi`

  * **Method** : `google.cloud.apigateway.v1.ApiGatewayService.UpdateApi`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `apigateway.apis.update - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.apigateway.v1.ApiGatewayService.UpdateApi" `  




#### `UpdateApiConfig`

  * **Method** : `google.cloud.apigateway.v1.ApiGatewayService.UpdateApiConfig`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `apigateway.apiconfigs.update - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.apigateway.v1.ApiGatewayService.UpdateApiConfig" `  




#### `UpdateGateway`

  * **Method** : `google.cloud.apigateway.v1.ApiGatewayService.UpdateGateway`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `apigateway.gateways.update - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.apigateway.v1.ApiGatewayService.UpdateGateway" `  




### `google.cloud.apigateway.v1beta.ApiGatewayService`

The following audit logs are associated with methods belonging to `google.cloud.apigateway.v1beta.ApiGatewayService`.

#### `CreateApi`

  * **Method** : `google.cloud.apigateway.v1beta.ApiGatewayService.CreateApi`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `apigateway.apis.create - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.apigateway.v1beta.ApiGatewayService.CreateApi" `  




#### `CreateApiConfig`

  * **Method** : `google.cloud.apigateway.v1beta.ApiGatewayService.CreateApiConfig`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `apigateway.apiconfigs.create - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.apigateway.v1beta.ApiGatewayService.CreateApiConfig" `  




#### `CreateGateway`

  * **Method** : `google.cloud.apigateway.v1beta.ApiGatewayService.CreateGateway`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `apigateway.gateways.create - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.apigateway.v1beta.ApiGatewayService.CreateGateway" `  




#### `DeleteApi`

  * **Method** : `google.cloud.apigateway.v1beta.ApiGatewayService.DeleteApi`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `apigateway.apis.delete - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.apigateway.v1beta.ApiGatewayService.DeleteApi" `  




#### `DeleteApiConfig`

  * **Method** : `google.cloud.apigateway.v1beta.ApiGatewayService.DeleteApiConfig`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `apigateway.apiconfigs.delete - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.apigateway.v1beta.ApiGatewayService.DeleteApiConfig" `  




#### `DeleteGateway`

  * **Method** : `google.cloud.apigateway.v1beta.ApiGatewayService.DeleteGateway`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `apigateway.gateways.delete - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.apigateway.v1beta.ApiGatewayService.DeleteGateway" `  




#### `GetApi`

  * **Method** : `google.cloud.apigateway.v1beta.ApiGatewayService.GetApi`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `apigateway.apis.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.apigateway.v1beta.ApiGatewayService.GetApi" `  




#### `GetApiConfig`

  * **Method** : `google.cloud.apigateway.v1beta.ApiGatewayService.GetApiConfig`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `apigateway.apiconfigs.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.apigateway.v1beta.ApiGatewayService.GetApiConfig" `  




#### `GetGateway`

  * **Method** : `google.cloud.apigateway.v1beta.ApiGatewayService.GetGateway`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `apigateway.gateways.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.apigateway.v1beta.ApiGatewayService.GetGateway" `  




#### `ListApiConfigs`

  * **Method** : `google.cloud.apigateway.v1beta.ApiGatewayService.ListApiConfigs`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `apigateway.apiconfigs.list - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.apigateway.v1beta.ApiGatewayService.ListApiConfigs" `  




#### `ListApis`

  * **Method** : `google.cloud.apigateway.v1beta.ApiGatewayService.ListApis`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `apigateway.apis.list - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.apigateway.v1beta.ApiGatewayService.ListApis" `  




#### `ListGateways`

  * **Method** : `google.cloud.apigateway.v1beta.ApiGatewayService.ListGateways`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `apigateway.gateways.list - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.apigateway.v1beta.ApiGatewayService.ListGateways" `  




#### `UpdateApi`

  * **Method** : `google.cloud.apigateway.v1beta.ApiGatewayService.UpdateApi`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `apigateway.apis.update - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.apigateway.v1beta.ApiGatewayService.UpdateApi" `  




#### `UpdateApiConfig`

  * **Method** : `google.cloud.apigateway.v1beta.ApiGatewayService.UpdateApiConfig`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `apigateway.apiconfigs.update - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.apigateway.v1beta.ApiGatewayService.UpdateApiConfig" `  




#### `UpdateGateway`

  * **Method** : `google.cloud.apigateway.v1beta.ApiGatewayService.UpdateGateway`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `apigateway.gateways.update - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.apigateway.v1beta.ApiGatewayService.UpdateGateway" `  




### `google.iam.v1.IAMPolicy`

The following audit logs are associated with methods belonging to `google.iam.v1.IAMPolicy`.

#### `GetIamPolicy`

  * **Method** : `GetIamPolicy`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `apigateway.apis.getIamPolicy - ADMIN_READ`
    * `apigateway.gateways.getIamPolicy - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="GetIamPolicy" `  




#### `SetIamPolicy`

  * **Method** : `SetIamPolicy`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `apigateway.apiconfigs.setIamPolicy - ADMIN_WRITE`
    * `apigateway.apis.setIamPolicy - ADMIN_WRITE`
    * `apigateway.gateways.setIamPolicy - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="SetIamPolicy" `  




### `google.longrunning.Operations`

The following audit logs are associated with methods belonging to `google.longrunning.Operations`.

#### `CancelOperation`

  * **Method** : `google.longrunning.Operations.CancelOperation`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `apigateway.operations.cancel - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.longrunning.Operations.CancelOperation" `  




#### `DeleteOperation`

  * **Method** : `google.longrunning.Operations.DeleteOperation`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `apigateway.operations.delete - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.longrunning.Operations.DeleteOperation" `  




#### `GetOperation`

  * **Method** : `google.longrunning.Operations.GetOperation`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `apigateway.operations.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.longrunning.Operations.GetOperation" `  




#### `ListOperations`

  * **Method** : `google.longrunning.Operations.ListOperations`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `apigateway.operations.list - ADMIN_READ`
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
