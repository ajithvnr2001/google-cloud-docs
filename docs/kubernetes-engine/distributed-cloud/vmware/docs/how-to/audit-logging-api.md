---
url: https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/audit-logging-api/
title: GKE On-Prem API audit logging \u00a0|\u00a0 Google Distributed Cloud software only for VMware \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T03:19:50.278916+00:00
---

# GKE On-Prem API audit logging  |  Google Distributed Cloud software only for VMware  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/audit-logging-api/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Google Distributed Cloud ](https://docs.cloud.google.com/distributed-cloud)
  * [ Documentation ](https://docs.cloud.google.com/kubernetes-engine/enterprise/clusters/docs)
  * [ GDC for VMware ](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs)
  * [ Guides ](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/overview)



Send feedback 

#  GKE On-Prem API audit logging Stay organized with collections  Save and categorize content based on your preferences. 

This document describes audit logging for GKE On-Prem API. Google Cloud services generate audit logs that record administrative and access activities within your Google Cloud resources. For more information about Cloud Audit Logs, see the following: 

  * [Types of audit logs](https://docs.cloud.google.com/logging/docs/audit#types)
  * [Audit log entry structure](https://docs.cloud.google.com/logging/docs/audit#audit_log_entry_structure)
  * [Storing and routing audit logs](https://docs.cloud.google.com/logging/docs/audit#storing_and_routing_audit_logs)
  * [Cloud Logging pricing summary](https://docs.cloud.google.com/stackdriver/pricing#logs-pricing-summary)
  * [Enable Data Access audit logs](https://docs.cloud.google.com/logging/docs/audit/configure-data-access)



## Service name

GKE On-Prem API audit logs use the service name `gkeonprem.googleapis.com`. Filter for this service: 
    
    
        protoPayload.serviceName="gkeonprem.googleapis.com"
      

## Methods by permission type

Each IAM permission has a `type` property, whose value is an enum that can be one of four values: `ADMIN_READ`, `ADMIN_WRITE`, `DATA_READ`, or `DATA_WRITE`. When you call a method, GKE On-Prem API generates an audit log whose category is dependent on the `type` property of the permission required to perform the method. Methods that require an IAM permission with the `type` property value of `DATA_READ`, `DATA_WRITE`, or `ADMIN_READ` generate [Data Access](https://docs.cloud.google.com/logging/docs/audit#data-access) audit logs. Methods that require an IAM permission with the `type` property value of `ADMIN_WRITE` generate [Admin Activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity) audit logs.

API methods in the following list that are marked with (LRO) are long-running operations (LROs). These methods usually generate two audit log entries: one when the operation starts and another when it ends. For more information see [Audit logs for long-running operations](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro). Permission type | Methods  
---|---  
`ADMIN_READ` | `google.cloud.gkeonprem.v1.GkeOnPrem.GetBareMetalAdminCluster`  
`google.cloud.gkeonprem.v1.GkeOnPrem.GetBareMetalCluster`  
`google.cloud.gkeonprem.v1.GkeOnPrem.GetBareMetalNodePool`  
`google.cloud.gkeonprem.v1.GkeOnPrem.GetVmwareAdminCluster`  
`google.cloud.gkeonprem.v1.GkeOnPrem.GetVmwareCluster`  
`google.cloud.gkeonprem.v1.GkeOnPrem.GetVmwareNodePool`  
`google.cloud.gkeonprem.v1.GkeOnPrem.ListBareMetalAdminClusters`  
`google.cloud.gkeonprem.v1.GkeOnPrem.ListBareMetalClusters`  
`google.cloud.gkeonprem.v1.GkeOnPrem.ListBareMetalNodePools`  
`google.cloud.gkeonprem.v1.GkeOnPrem.ListVmwareAdminClusters`  
`google.cloud.gkeonprem.v1.GkeOnPrem.ListVmwareClusters`  
`google.cloud.gkeonprem.v1.GkeOnPrem.ListVmwareNodePools`  
`google.cloud.gkeonprem.v1.GkeOnPrem.QueryBareMetalAdminVersionConfig`  
`google.cloud.gkeonprem.v1.GkeOnPrem.QueryBareMetalVersionConfig`  
`google.cloud.gkeonprem.v1.GkeOnPrem.QueryVmwareVersionConfig`  
`ADMIN_WRITE` | `google.cloud.gkeonprem.v1.GkeOnPrem.CreateBareMetalAdminCluster` (LRO)  
`google.cloud.gkeonprem.v1.GkeOnPrem.CreateBareMetalCluster` (LRO)  
`google.cloud.gkeonprem.v1.GkeOnPrem.CreateBareMetalNodePool` (LRO)  
`google.cloud.gkeonprem.v1.GkeOnPrem.CreateVmwareCluster` (LRO)  
`google.cloud.gkeonprem.v1.GkeOnPrem.CreateVmwareNodePool` (LRO)  
`google.cloud.gkeonprem.v1.GkeOnPrem.DeleteBareMetalCluster` (LRO)  
`google.cloud.gkeonprem.v1.GkeOnPrem.DeleteBareMetalNodePool` (LRO)  
`google.cloud.gkeonprem.v1.GkeOnPrem.DeleteVmwareCluster` (LRO)  
`google.cloud.gkeonprem.v1.GkeOnPrem.DeleteVmwareNodePool` (LRO)  
`google.cloud.gkeonprem.v1.GkeOnPrem.EnrollBareMetalAdminCluster` (LRO)  
`google.cloud.gkeonprem.v1.GkeOnPrem.EnrollBareMetalCluster` (LRO)  
`google.cloud.gkeonprem.v1.GkeOnPrem.EnrollBareMetalNodePool` (LRO)  
`google.cloud.gkeonprem.v1.GkeOnPrem.EnrollVmwareAdminCluster` (LRO)  
`google.cloud.gkeonprem.v1.GkeOnPrem.EnrollVmwareCluster` (LRO)  
`google.cloud.gkeonprem.v1.GkeOnPrem.EnrollVmwareNodePool` (LRO)  
`google.cloud.gkeonprem.v1.GkeOnPrem.UnenrollBareMetalAdminCluster` (LRO)  
`google.cloud.gkeonprem.v1.GkeOnPrem.UnenrollBareMetalCluster` (LRO)  
`google.cloud.gkeonprem.v1.GkeOnPrem.UnenrollBareMetalNodePool` (LRO)  
`google.cloud.gkeonprem.v1.GkeOnPrem.UnenrollVmwareAdminCluster` (LRO)  
`google.cloud.gkeonprem.v1.GkeOnPrem.UnenrollVmwareCluster` (LRO)  
`google.cloud.gkeonprem.v1.GkeOnPrem.UnenrollVmwareNodePool` (LRO)  
`google.cloud.gkeonprem.v1.GkeOnPrem.UpdateBareMetalAdminCluster` (LRO)  
`google.cloud.gkeonprem.v1.GkeOnPrem.UpdateBareMetalCluster` (LRO)  
`google.cloud.gkeonprem.v1.GkeOnPrem.UpdateBareMetalNodePool` (LRO)  
`google.cloud.gkeonprem.v1.GkeOnPrem.UpdateVmwareAdminCluster` (LRO)  
`google.cloud.gkeonprem.v1.GkeOnPrem.UpdateVmwareCluster` (LRO)  
`google.cloud.gkeonprem.v1.GkeOnPrem.UpdateVmwareNodePool` (LRO)  
`google.longrunning.Operations.CancelOperation`  
`google.longrunning.Operations.DeleteOperation`  
  
## API interface audit logs

For information about how and which permissions are evaluated for each method, see the Identity and Access Management documentation for GKE On-Prem API.

### `google.cloud.gkeonprem.v1.GkeOnPrem`

The following audit logs are associated with methods belonging to `google.cloud.gkeonprem.v1.GkeOnPrem`.

#### `CreateBareMetalAdminCluster`

  * **Method** : `google.cloud.gkeonprem.v1.GkeOnPrem.CreateBareMetalAdminCluster`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `gkeonprem.bareMetalAdminClusters.create - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.gkeonprem.v1.GkeOnPrem.CreateBareMetalAdminCluster" `  




#### `CreateBareMetalCluster`

  * **Method** : `google.cloud.gkeonprem.v1.GkeOnPrem.CreateBareMetalCluster`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `gkeonprem.bareMetalClusters.create - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.gkeonprem.v1.GkeOnPrem.CreateBareMetalCluster" `  




#### `CreateBareMetalNodePool`

  * **Method** : `google.cloud.gkeonprem.v1.GkeOnPrem.CreateBareMetalNodePool`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `gkeonprem.bareMetalNodePools.create - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.gkeonprem.v1.GkeOnPrem.CreateBareMetalNodePool" `  




#### `CreateVmwareCluster`

  * **Method** : `google.cloud.gkeonprem.v1.GkeOnPrem.CreateVmwareCluster`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `gkeonprem.vmwareClusters.create - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.gkeonprem.v1.GkeOnPrem.CreateVmwareCluster" `  




#### `CreateVmwareNodePool`

  * **Method** : `google.cloud.gkeonprem.v1.GkeOnPrem.CreateVmwareNodePool`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `gkeonprem.vmwareNodePools.create - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.gkeonprem.v1.GkeOnPrem.CreateVmwareNodePool" `  




#### `DeleteBareMetalCluster`

  * **Method** : `google.cloud.gkeonprem.v1.GkeOnPrem.DeleteBareMetalCluster`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `gkeonprem.bareMetalClusters.delete - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.gkeonprem.v1.GkeOnPrem.DeleteBareMetalCluster" `  




#### `DeleteBareMetalNodePool`

  * **Method** : `google.cloud.gkeonprem.v1.GkeOnPrem.DeleteBareMetalNodePool`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `gkeonprem.bareMetalNodePools.delete - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.gkeonprem.v1.GkeOnPrem.DeleteBareMetalNodePool" `  




#### `DeleteVmwareCluster`

  * **Method** : `google.cloud.gkeonprem.v1.GkeOnPrem.DeleteVmwareCluster`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `gkeonprem.vmwareClusters.delete - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.gkeonprem.v1.GkeOnPrem.DeleteVmwareCluster" `  




#### `DeleteVmwareNodePool`

  * **Method** : `google.cloud.gkeonprem.v1.GkeOnPrem.DeleteVmwareNodePool`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `gkeonprem.vmwareNodePools.delete - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.gkeonprem.v1.GkeOnPrem.DeleteVmwareNodePool" `  




#### `EnrollBareMetalAdminCluster`

  * **Method** : `google.cloud.gkeonprem.v1.GkeOnPrem.EnrollBareMetalAdminCluster`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `gkeonprem.bareMetalAdminClusters.enroll - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.gkeonprem.v1.GkeOnPrem.EnrollBareMetalAdminCluster" `  




#### `EnrollBareMetalCluster`

  * **Method** : `google.cloud.gkeonprem.v1.GkeOnPrem.EnrollBareMetalCluster`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `gkeonprem.bareMetalClusters.enroll - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.gkeonprem.v1.GkeOnPrem.EnrollBareMetalCluster" `  




#### `EnrollBareMetalNodePool`

  * **Method** : `google.cloud.gkeonprem.v1.GkeOnPrem.EnrollBareMetalNodePool`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `gkeonprem.bareMetalNodePools.enroll - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.gkeonprem.v1.GkeOnPrem.EnrollBareMetalNodePool" `  




#### `EnrollVmwareAdminCluster`

  * **Method** : `google.cloud.gkeonprem.v1.GkeOnPrem.EnrollVmwareAdminCluster`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `gkeonprem.vmwareAdminClusters.enroll - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.gkeonprem.v1.GkeOnPrem.EnrollVmwareAdminCluster" `  




#### `EnrollVmwareCluster`

  * **Method** : `google.cloud.gkeonprem.v1.GkeOnPrem.EnrollVmwareCluster`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `gkeonprem.vmwareClusters.enroll - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.gkeonprem.v1.GkeOnPrem.EnrollVmwareCluster" `  




#### `EnrollVmwareNodePool`

  * **Method** : `google.cloud.gkeonprem.v1.GkeOnPrem.EnrollVmwareNodePool`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `gkeonprem.vmwareNodePools.enroll - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.gkeonprem.v1.GkeOnPrem.EnrollVmwareNodePool" `  




#### `GetBareMetalAdminCluster`

  * **Method** : `google.cloud.gkeonprem.v1.GkeOnPrem.GetBareMetalAdminCluster`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `gkeonprem.bareMetalAdminClusters.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.gkeonprem.v1.GkeOnPrem.GetBareMetalAdminCluster" `  




#### `GetBareMetalCluster`

  * **Method** : `google.cloud.gkeonprem.v1.GkeOnPrem.GetBareMetalCluster`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `gkeonprem.bareMetalClusters.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.gkeonprem.v1.GkeOnPrem.GetBareMetalCluster" `  




#### `GetBareMetalNodePool`

  * **Method** : `google.cloud.gkeonprem.v1.GkeOnPrem.GetBareMetalNodePool`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `gkeonprem.bareMetalNodePools.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.gkeonprem.v1.GkeOnPrem.GetBareMetalNodePool" `  




#### `GetVmwareAdminCluster`

  * **Method** : `google.cloud.gkeonprem.v1.GkeOnPrem.GetVmwareAdminCluster`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `gkeonprem.vmwareAdminClusters.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.gkeonprem.v1.GkeOnPrem.GetVmwareAdminCluster" `  




#### `GetVmwareCluster`

  * **Method** : `google.cloud.gkeonprem.v1.GkeOnPrem.GetVmwareCluster`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `gkeonprem.vmwareClusters.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.gkeonprem.v1.GkeOnPrem.GetVmwareCluster" `  




#### `GetVmwareNodePool`

  * **Method** : `google.cloud.gkeonprem.v1.GkeOnPrem.GetVmwareNodePool`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `gkeonprem.vmwareNodePools.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.gkeonprem.v1.GkeOnPrem.GetVmwareNodePool" `  




#### `ListBareMetalAdminClusters`

  * **Method** : `google.cloud.gkeonprem.v1.GkeOnPrem.ListBareMetalAdminClusters`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `gkeonprem.bareMetalAdminClusters.list - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.gkeonprem.v1.GkeOnPrem.ListBareMetalAdminClusters" `  




#### `ListBareMetalClusters`

  * **Method** : `google.cloud.gkeonprem.v1.GkeOnPrem.ListBareMetalClusters`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `gkeonprem.bareMetalClusters.list - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.gkeonprem.v1.GkeOnPrem.ListBareMetalClusters" `  




#### `ListBareMetalNodePools`

  * **Method** : `google.cloud.gkeonprem.v1.GkeOnPrem.ListBareMetalNodePools`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `gkeonprem.bareMetalNodePools.list - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.gkeonprem.v1.GkeOnPrem.ListBareMetalNodePools" `  




#### `ListVmwareAdminClusters`

  * **Method** : `google.cloud.gkeonprem.v1.GkeOnPrem.ListVmwareAdminClusters`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `gkeonprem.vmwareAdminClusters.list - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.gkeonprem.v1.GkeOnPrem.ListVmwareAdminClusters" `  




#### `ListVmwareClusters`

  * **Method** : `google.cloud.gkeonprem.v1.GkeOnPrem.ListVmwareClusters`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `gkeonprem.vmwareClusters.list - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.gkeonprem.v1.GkeOnPrem.ListVmwareClusters" `  




#### `ListVmwareNodePools`

  * **Method** : `google.cloud.gkeonprem.v1.GkeOnPrem.ListVmwareNodePools`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `gkeonprem.vmwareNodePools.list - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.gkeonprem.v1.GkeOnPrem.ListVmwareNodePools" `  




#### `QueryBareMetalAdminVersionConfig`

  * **Method** : `google.cloud.gkeonprem.v1.GkeOnPrem.QueryBareMetalAdminVersionConfig`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `gkeonprem.bareMetalAdminClusters.queryVersionConfig - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.gkeonprem.v1.GkeOnPrem.QueryBareMetalAdminVersionConfig" `  




#### `QueryBareMetalVersionConfig`

  * **Method** : `google.cloud.gkeonprem.v1.GkeOnPrem.QueryBareMetalVersionConfig`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `gkeonprem.bareMetalClusters.queryVersionConfig - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.gkeonprem.v1.GkeOnPrem.QueryBareMetalVersionConfig" `  




#### `QueryVmwareVersionConfig`

  * **Method** : `google.cloud.gkeonprem.v1.GkeOnPrem.QueryVmwareVersionConfig`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `gkeonprem.vmwareClusters.queryVersionConfig - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.gkeonprem.v1.GkeOnPrem.QueryVmwareVersionConfig" `  




#### `UnenrollBareMetalAdminCluster`

  * **Method** : `google.cloud.gkeonprem.v1.GkeOnPrem.UnenrollBareMetalAdminCluster`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `gkeonprem.bareMetalAdminClusters.unenroll - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.gkeonprem.v1.GkeOnPrem.UnenrollBareMetalAdminCluster" `  




#### `UnenrollBareMetalCluster`

  * **Method** : `google.cloud.gkeonprem.v1.GkeOnPrem.UnenrollBareMetalCluster`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `gkeonprem.bareMetalClusters.unenroll - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.gkeonprem.v1.GkeOnPrem.UnenrollBareMetalCluster" `  




#### `UnenrollBareMetalNodePool`

  * **Method** : `google.cloud.gkeonprem.v1.GkeOnPrem.UnenrollBareMetalNodePool`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `gkeonprem.bareMetalNodePools.unenroll - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.gkeonprem.v1.GkeOnPrem.UnenrollBareMetalNodePool" `  




#### `UnenrollVmwareAdminCluster`

  * **Method** : `google.cloud.gkeonprem.v1.GkeOnPrem.UnenrollVmwareAdminCluster`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `gkeonprem.vmwareAdminClusters.unenroll - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.gkeonprem.v1.GkeOnPrem.UnenrollVmwareAdminCluster" `  




#### `UnenrollVmwareCluster`

  * **Method** : `google.cloud.gkeonprem.v1.GkeOnPrem.UnenrollVmwareCluster`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `gkeonprem.vmwareClusters.unenroll - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.gkeonprem.v1.GkeOnPrem.UnenrollVmwareCluster" `  




#### `UnenrollVmwareNodePool`

  * **Method** : `google.cloud.gkeonprem.v1.GkeOnPrem.UnenrollVmwareNodePool`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `gkeonprem.vmwareNodePools.unenroll - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.gkeonprem.v1.GkeOnPrem.UnenrollVmwareNodePool" `  




#### `UpdateBareMetalAdminCluster`

  * **Method** : `google.cloud.gkeonprem.v1.GkeOnPrem.UpdateBareMetalAdminCluster`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `gkeonprem.bareMetalAdminClusters.update - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.gkeonprem.v1.GkeOnPrem.UpdateBareMetalAdminCluster" `  




#### `UpdateBareMetalCluster`

  * **Method** : `google.cloud.gkeonprem.v1.GkeOnPrem.UpdateBareMetalCluster`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `gkeonprem.bareMetalClusters.update - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.gkeonprem.v1.GkeOnPrem.UpdateBareMetalCluster" `  




#### `UpdateBareMetalNodePool`

  * **Method** : `google.cloud.gkeonprem.v1.GkeOnPrem.UpdateBareMetalNodePool`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `gkeonprem.bareMetalNodePools.update - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.gkeonprem.v1.GkeOnPrem.UpdateBareMetalNodePool" `  




#### `UpdateVmwareAdminCluster`

  * **Method** : `google.cloud.gkeonprem.v1.GkeOnPrem.UpdateVmwareAdminCluster`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `gkeonprem.vmwareAdminClusters.update - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.gkeonprem.v1.GkeOnPrem.UpdateVmwareAdminCluster" `  




#### `UpdateVmwareCluster`

  * **Method** : `google.cloud.gkeonprem.v1.GkeOnPrem.UpdateVmwareCluster`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `gkeonprem.vmwareClusters.update - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.gkeonprem.v1.GkeOnPrem.UpdateVmwareCluster" `  




#### `UpdateVmwareNodePool`

  * **Method** : `google.cloud.gkeonprem.v1.GkeOnPrem.UpdateVmwareNodePool`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `gkeonprem.vmwareNodePools.update - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.gkeonprem.v1.GkeOnPrem.UpdateVmwareNodePool" `  




### `google.longrunning.Operations`

The following audit logs are associated with methods belonging to `google.longrunning.Operations`.

#### `CancelOperation`

  * **Method** : `google.longrunning.Operations.CancelOperation`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `gkeonprem.operations.cancel - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.longrunning.Operations.CancelOperation" `  




#### `DeleteOperation`

  * **Method** : `google.longrunning.Operations.DeleteOperation`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `gkeonprem.operations.delete - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.longrunning.Operations.DeleteOperation" `  




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
