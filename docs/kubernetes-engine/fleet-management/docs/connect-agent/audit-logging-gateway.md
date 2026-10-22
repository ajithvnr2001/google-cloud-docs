---
url: https://docs.cloud.google.com/kubernetes-engine/fleet-management/docs/connect-agent/audit-logging-gateway/
title: Connect Gateway audit logging \u00a0|\u00a0 Fleet management \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T15:03:31.978288+00:00
---

# Connect Gateway audit logging  |  Fleet management  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/fleet-management/docs/connect-agent/audit-logging-gateway/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Google Kubernetes Engine (GKE) ](https://docs.cloud.google.com/kubernetes-engine)
  * [ Fleet management ](https://docs.cloud.google.com/kubernetes-engine/fleet-management/docs)



Send feedback 

#  Connect Gateway audit logging Stay organized with collections  Save and categorize content based on your preferences. 

This document describes audit logging for Connect Gateway. Google Cloud services generate audit logs that record administrative and access activities within your Google Cloud resources. For more information about Cloud Audit Logs, see the following: 

  * [Types of audit logs](https://docs.cloud.google.com/logging/docs/audit#types)
  * [Audit log entry structure](https://docs.cloud.google.com/logging/docs/audit#audit_log_entry_structure)
  * [Storing and routing audit logs](https://docs.cloud.google.com/logging/docs/audit#storing_and_routing_audit_logs)
  * [Cloud Logging pricing summary](https://docs.cloud.google.com/stackdriver/pricing#logs-pricing-summary)
  * [Enable Data Access audit logs](https://docs.cloud.google.com/logging/docs/audit/configure-data-access)



## Service name

Connect Gateway audit logs use the service name `connectgateway.googleapis.com`. Filter for this service: 
    
    
        protoPayload.serviceName="connectgateway.googleapis.com"
      

## Methods by permission type

Connect Gateway audit logs are enabled by turning on audit logging for `gkehub.googleapis.com`.

Each IAM permission has a `type` property, whose value is an enum that can be one of four values: `ADMIN_READ`, `ADMIN_WRITE`, `DATA_READ`, or `DATA_WRITE`. When you call a method, Connect Gateway generates an audit log whose category is dependent on the `type` property of the permission required to perform the method. Methods that require an IAM permission with the `type` property value of `DATA_READ`, `DATA_WRITE`, or `ADMIN_READ` generate [Data Access](https://docs.cloud.google.com/logging/docs/audit#data-access) audit logs. Methods that require an IAM permission with the `type` property value of `ADMIN_WRITE` generate [Admin Activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity) audit logs.

API methods in the following list that are marked with (LRO) are long-running operations (LROs). These methods usually generate two audit log entries: one when the operation starts and another when it ends. For more information see [Audit logs for long-running operations](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro). Permission type | Methods  
---|---  
`ADMIN_READ` | `google.cloud.gkeconnect.gateway.v1.GatewayService.GetResource`  
`google.cloud.gkeconnect.gateway.v1beta1.GatewayService.GetResource`  
`ADMIN_WRITE` | `google.cloud.gkeconnect.gateway.v1.GatewayService.DeleteResource`  
`google.cloud.gkeconnect.gateway.v1.GatewayService.PatchResource`  
`google.cloud.gkeconnect.gateway.v1.GatewayService.PostResource`  
`google.cloud.gkeconnect.gateway.v1.GatewayService.PutResource`  
`google.cloud.gkeconnect.gateway.v1.GatewayService.Stream`  
`google.cloud.gkeconnect.gateway.v1beta1.GatewayService.DeleteResource`  
`google.cloud.gkeconnect.gateway.v1beta1.GatewayService.PatchResource`  
`google.cloud.gkeconnect.gateway.v1beta1.GatewayService.PostResource`  
`google.cloud.gkeconnect.gateway.v1beta1.GatewayService.PutResource`  
`google.cloud.gkeconnect.gateway.v1beta1.GatewayService.Stream`  
  
## API interface audit logs

For information about how and which permissions are evaluated for each method, see the Identity and Access Management documentation for Connect Gateway.

### `google.cloud.gkeconnect.gateway.v1.GatewayService`

The following audit logs are associated with methods belonging to `google.cloud.gkeconnect.gateway.v1.GatewayService`.

#### `DeleteResource`

  * **Method** : `google.cloud.gkeconnect.gateway.v1.GatewayService.DeleteResource`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `gkehub.gateway.delete - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.gkeconnect.gateway.v1.GatewayService.DeleteResource" `  




#### `GetResource`

  * **Method** : `google.cloud.gkeconnect.gateway.v1.GatewayService.GetResource`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `gkehub.gateway.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : [**Streaming RPC**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#streaming)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.gkeconnect.gateway.v1.GatewayService.GetResource" `  




#### `PatchResource`

  * **Method** : `google.cloud.gkeconnect.gateway.v1.GatewayService.PatchResource`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `gkehub.gateway.patch - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.gkeconnect.gateway.v1.GatewayService.PatchResource" `  




#### `PostResource`

  * **Method** : `google.cloud.gkeconnect.gateway.v1.GatewayService.PostResource`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `gkehub.gateway.post - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.gkeconnect.gateway.v1.GatewayService.PostResource" `  




#### `PutResource`

  * **Method** : `google.cloud.gkeconnect.gateway.v1.GatewayService.PutResource`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `gkehub.gateway.put - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.gkeconnect.gateway.v1.GatewayService.PutResource" `  




#### `Stream`

  * **Method** : `google.cloud.gkeconnect.gateway.v1.GatewayService.Stream`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `gkehub.gateway.stream - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Streaming RPC**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#streaming)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.gkeconnect.gateway.v1.GatewayService.Stream" `  




### `google.cloud.gkeconnect.gateway.v1beta1.GatewayService`

The following audit logs are associated with methods belonging to `google.cloud.gkeconnect.gateway.v1beta1.GatewayService`.

#### `DeleteResource`

  * **Method** : `google.cloud.gkeconnect.gateway.v1beta1.GatewayService.DeleteResource`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `gkehub.gateway.delete - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.gkeconnect.gateway.v1beta1.GatewayService.DeleteResource" `  




#### `GetResource`

  * **Method** : `google.cloud.gkeconnect.gateway.v1beta1.GatewayService.GetResource`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `gkehub.gateway.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : [**Streaming RPC**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#streaming)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.gkeconnect.gateway.v1beta1.GatewayService.GetResource" `  




#### `PatchResource`

  * **Method** : `google.cloud.gkeconnect.gateway.v1beta1.GatewayService.PatchResource`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `gkehub.gateway.patch - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.gkeconnect.gateway.v1beta1.GatewayService.PatchResource" `  




#### `PostResource`

  * **Method** : `google.cloud.gkeconnect.gateway.v1beta1.GatewayService.PostResource`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `gkehub.gateway.post - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.gkeconnect.gateway.v1beta1.GatewayService.PostResource" `  




#### `PutResource`

  * **Method** : `google.cloud.gkeconnect.gateway.v1beta1.GatewayService.PutResource`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `gkehub.gateway.put - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.gkeconnect.gateway.v1beta1.GatewayService.PutResource" `  




#### `Stream`

  * **Method** : `google.cloud.gkeconnect.gateway.v1beta1.GatewayService.Stream`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `gkehub.gateway.stream - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Streaming RPC**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#streaming)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.gkeconnect.gateway.v1beta1.GatewayService.Stream" `  




## Kubernetes audit logging

In addition to Cloud Audit Logs, [Kubernetes audit logging](https://kubernetes.io/docs/tasks/debug/debug-cluster/audit/) provides a way for administrators to retain, query, process, and alert on events that occur in registered clusters. Administrators can use the logged information to do forensic analysis and real-time alerting, or for cataloging how a fleet of clusters are being used and by whom.

The Connect Agent talks to the local API server running in the registered cluster, and each cluster will have its own set of Kubernetes audit logs. All actions that users perform from the UI through Connect are logged by that cluster.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
