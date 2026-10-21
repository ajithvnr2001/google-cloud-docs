---
url: https://docs.cloud.google.com/kubernetes-engine/fleet-management/docs/connect-agent/audit-logging/
title: Connect audit logging \u00a0|\u00a0 Fleet management \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T01:05:53.403860+00:00
---

# Connect audit logging  |  Fleet management  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/fleet-management/docs/connect-agent/audit-logging/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Google Kubernetes Engine (GKE) ](https://docs.cloud.google.com/kubernetes-engine)
  * [ Fleet management ](https://docs.cloud.google.com/kubernetes-engine/fleet-management/docs)



Send feedback 

#  Connect audit logging Stay organized with collections  Save and categorize content based on your preferences. 

This document describes audit logging for Connect. Google Cloud services generate audit logs that record administrative and access activities within your Google Cloud resources. For more information about Cloud Audit Logs, see the following: 

  * [Types of audit logs](https://docs.cloud.google.com/logging/docs/audit#types)
  * [Audit log entry structure](https://docs.cloud.google.com/logging/docs/audit#audit_log_entry_structure)
  * [Storing and routing audit logs](https://docs.cloud.google.com/logging/docs/audit#storing_and_routing_audit_logs)
  * [Cloud Logging pricing summary](https://docs.cloud.google.com/stackdriver/pricing#logs-pricing-summary)
  * [Enable Data Access audit logs](https://docs.cloud.google.com/logging/docs/audit/configure-data-access)



## Service name

Connect audit logs use the service name `gkeconnect.googleapis.com`. Filter for this service: 
    
    
        protoPayload.serviceName="gkeconnect.googleapis.com"
      

## Methods by permission type

Connect audit logs are enabled by turning on audit logging for `gkehub.googleapis.com`.

Each IAM permission has a `type` property, whose value is an enum that can be one of four values: `ADMIN_READ`, `ADMIN_WRITE`, `DATA_READ`, or `DATA_WRITE`. When you call a method, Connect generates an audit log whose category is dependent on the `type` property of the permission required to perform the method. Methods that require an IAM permission with the `type` property value of `DATA_READ`, `DATA_WRITE`, or `ADMIN_READ` generate [Data Access](https://docs.cloud.google.com/logging/docs/audit#data-access) audit logs. Methods that require an IAM permission with the `type` property value of `ADMIN_WRITE` generate [Admin Activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity) audit logs.

API methods in the following list that are marked with (LRO) are long-running operations (LROs). These methods usually generate two audit log entries: one when the operation starts and another when it ends. For more information see [Audit logs for long-running operations](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro). Permission type | Methods  
---|---  
`DATA_READ` | `google.cloud.gkeconnect.v1.EgressService.Egress`  
`google.cloud.gkeconnect.v1beta1.EgressService.Egress`  
  
## API interface audit logs

For information about how and which permissions are evaluated for each method, see the Identity and Access Management documentation for Connect.

### `google.cloud.gkeconnect.v1.EgressService`

The following audit logs are associated with methods belonging to `google.cloud.gkeconnect.v1.EgressService`.

#### `Egress`

  * **Method** : `google.cloud.gkeconnect.v1.EgressService.Egress`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `gkehub.endpoints.connect - DATA_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.gkeconnect.v1.EgressService.Egress" `  




### `google.cloud.gkeconnect.v1beta1.EgressService`

The following audit logs are associated with methods belonging to `google.cloud.gkeconnect.v1beta1.EgressService`.

#### `Egress`

  * **Method** : `google.cloud.gkeconnect.v1beta1.EgressService.Egress`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `gkehub.endpoints.connect - DATA_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.gkeconnect.v1beta1.EgressService.Egress" `  




## Kubernetes audit logging

In addition to Cloud Audit Logs, [Kubernetes audit logging](https://kubernetes.io/docs/tasks/debug/debug-cluster/audit/) provides a way for administrators to retain, query, process, and alert on events that occur in registered clusters. Administrators can use the logged information to do forensic analysis and real-time alerting, or for cataloging how a fleet of clusters are being used and by whom.

The Connect Agent talks to the local API server running in the registered cluster, and each cluster will have its own set of Kubernetes audit logs. All actions that users perform from the UI through Connect are logged by that cluster.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
