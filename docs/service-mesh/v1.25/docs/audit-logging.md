---
url: https://docs.cloud.google.com/service-mesh/v1.25/docs/audit-logging/
title: Cloud Service Mesh audit logging \u00a0|\u00a0 Cloud Service Mesh v1.25 \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T08:58:02.791884+00:00
---

# Cloud Service Mesh audit logging  |  Cloud Service Mesh v1.25  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/service-mesh/v1.25/docs/audit-logging/

You are viewing archived v1.25 Service Mesh documentation.

Available versions

[Cloud Service Mesh latest](https://docs.cloud.google.com/service-mesh/docs)  
[Cloud Service Mesh 1.28 archive](https://docs.cloud.google.com/service-mesh/v1.28/docs)  
[Cloud Service Mesh 1.27 archive](https://docs.cloud.google.com/service-mesh/v1.27/docs)  
[Cloud Service Mesh 1.26 archive](https://docs.cloud.google.com/service-mesh/v1.26/docs)  
[Cloud Service Mesh 1.25 archive](https://docs.cloud.google.com/service-mesh/v1.25/docs)  
[Cloud Service Mesh 1.24 archive](https://docs.cloud.google.com/service-mesh/v1.24/docs)  
[Cloud Service Mesh 1.23 archive](https://docs.cloud.google.com/service-mesh/v1.23/docs)  
[Cloud Service Mesh 1.22 archive](https://docs.cloud.google.com/service-mesh/v1.22/docs)  
[Cloud Service Mesh 1.21 archive](https://docs.cloud.google.com/service-mesh/v1.21/docs)  
[Cloud Service Mesh 1.20 archive](https://docs.cloud.google.com/service-mesh/v1.20/docs)  
[Anthos Service Mesh 1.19 archive](https://docs.cloud.google.com/service-mesh/v1.19/docs)  


  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Networking ](https://docs.cloud.google.com/docs/networking)
  * [ Cloud Service Mesh ](https://docs.cloud.google.com/service-mesh/docs)
  * [ v1.25 ](https://docs.cloud.google.com/service-mesh/v1.25/docs)
  * [ Guides ](https://docs.cloud.google.com/service-mesh/v1.25/docs/overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Cloud Service Mesh audit logging

This document describes audit logging for Cloud Service Mesh. Google Cloud services generate audit logs that record administrative and access activities within your Google Cloud resources. For more information about Cloud Audit Logs, see the following: 

  * [Types of audit logs](https://docs.cloud.google.com/logging/docs/audit#types)
  * [Audit log entry structure](https://docs.cloud.google.com/logging/docs/audit#audit_log_entry_structure)
  * [Storing and routing audit logs](https://docs.cloud.google.com/logging/docs/audit#storing_and_routing_audit_logs)
  * [Cloud Logging pricing summary](https://docs.cloud.google.com/stackdriver/pricing#logs-pricing-summary)
  * [Enable Data Access audit logs](https://docs.cloud.google.com/logging/docs/audit/configure-data-access)



## Service name

Cloud Service Mesh audit logs use the service name `meshconfig.googleapis.com`. Filter for this service: 
    
    
        protoPayload.serviceName="meshconfig.googleapis.com"
      

## Methods by permission type

Each IAM permission has a `type` property, whose value is an enum that can be one of four values: `ADMIN_READ`, `ADMIN_WRITE`, `DATA_READ`, or `DATA_WRITE`. When you call a method, Cloud Service Mesh generates an audit log whose category is dependent on the `type` property of the permission required to perform the method. Methods that require an IAM permission with the `type` property value of `DATA_READ`, `DATA_WRITE`, or `ADMIN_READ` generate [Data Access](https://docs.cloud.google.com/logging/docs/audit#data-access) audit logs. Methods that require an IAM permission with the `type` property value of `ADMIN_WRITE` generate [Admin Activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity) audit logs.

Permission type | Methods  
---|---  
`ADMIN_WRITE` | `google.cloud.meshconfig.v1alpha1.Admin.Initialize`  
`DATA_READ` | `envoy.service.discovery.v3.AggregatedDiscoveryService.StreamAggregatedResources`  
`google.cloud.meshconfig.v1alpha1.Webhook.Call`  
`google.cloud.meshconfig.v1alpha1.Webhook.GatewayInject`  
`google.cloud.meshconfig.v1alpha1.Webhook.Inject`  
`google.cloud.meshconfig.v1alpha1.Webhook.ProxylessBootstrapInject`  
`google.cloud.meshconfig.v1alpha1.Webhook.TDInject`  
`google.cloud.meshconfig.v1alpha1.Webhook.Validate`  
`DATA_WRITE` | `envoy.service.load_stats.v3.LoadReportingService.StreamLoadStats`  
  
## API interface audit logs

For information about how and which permissions are evaluated for each method, see the Identity and Access Management documentation for Cloud Service Mesh.

### `envoy.service.discovery.v3.AggregatedDiscoveryService`

The following audit logs are associated with methods belonging to `envoy.service.discovery.v3.AggregatedDiscoveryService`.

#### `StreamAggregatedResources`

  * **Method** : `envoy.service.discovery.v3.AggregatedDiscoveryService.StreamAggregatedResources`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `meshconfig.projects.get - DATA_READ`
  * **Method is a long-running or streaming operation** : [**Streaming RPC**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#streaming)   

  * **Filter for this method** : ` protoPayload.methodName="envoy.service.discovery.v3.AggregatedDiscoveryService.StreamAggregatedResources" `  




### `envoy.service.load_stats.v3.LoadReportingService`

The following audit logs are associated with methods belonging to `envoy.service.load_stats.v3.LoadReportingService`.

#### `StreamLoadStats`

  * **Method** : `envoy.service.load_stats.v3.LoadReportingService.StreamLoadStats`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `meshconfig.projects.report - DATA_WRITE`
  * **Method is a long-running or streaming operation** : [**Streaming RPC**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#streaming)   

  * **Filter for this method** : ` protoPayload.methodName="envoy.service.load_stats.v3.LoadReportingService.StreamLoadStats" `  




### `google.cloud.meshconfig.v1alpha1.Admin`

The following audit logs are associated with methods belonging to `google.cloud.meshconfig.v1alpha1.Admin`.

#### `Initialize`

  * **Method** : `google.cloud.meshconfig.v1alpha1.Admin.Initialize`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `meshconfig.projects.init - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.meshconfig.v1alpha1.Admin.Initialize" `  




### `google.cloud.meshconfig.v1alpha1.Webhook`

The following audit logs are associated with methods belonging to `google.cloud.meshconfig.v1alpha1.Webhook`.

#### `Call`

  * **Method** : `google.cloud.meshconfig.v1alpha1.Webhook.Call`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `meshconfig.projects.get - DATA_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.meshconfig.v1alpha1.Webhook.Call" `  




#### `GatewayInject`

  * **Method** : `google.cloud.meshconfig.v1alpha1.Webhook.GatewayInject`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `meshconfig.projects.get - DATA_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.meshconfig.v1alpha1.Webhook.GatewayInject" `  




#### `Inject`

  * **Method** : `google.cloud.meshconfig.v1alpha1.Webhook.Inject`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `meshconfig.projects.get - DATA_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.meshconfig.v1alpha1.Webhook.Inject" `  




#### `ProxylessBootstrapInject`

  * **Method** : `google.cloud.meshconfig.v1alpha1.Webhook.ProxylessBootstrapInject`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `meshconfig.projects.get - DATA_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.meshconfig.v1alpha1.Webhook.ProxylessBootstrapInject" `  




#### `TDInject`

  * **Method** : `google.cloud.meshconfig.v1alpha1.Webhook.TDInject`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `meshconfig.projects.get - DATA_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.meshconfig.v1alpha1.Webhook.TDInject" `  




#### `Validate`

  * **Method** : `google.cloud.meshconfig.v1alpha1.Webhook.Validate`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `meshconfig.projects.get - DATA_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.meshconfig.v1alpha1.Webhook.Validate" `  




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
