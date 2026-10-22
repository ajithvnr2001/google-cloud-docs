---
url: https://docs.cloud.google.com/kubernetes-engine/multi-cloud/docs/azure/how-to/audit-logging/
title: GKE Multi-Cloud audit logging \u00a0|\u00a0 GKE on Azure \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T15:09:30.235799+00:00
---

# GKE Multi-Cloud audit logging  |  GKE on Azure  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/multi-cloud/docs/azure/how-to/audit-logging/

The product described by this documentation, GKE on Azure, is now in [maintenance mode](https://docs.cloud.google.com/kubernetes-engine/multi-cloud/docs/azure/deprecations/deprecation-announcement) and will be shut down on March 17, 2027. 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ Google Kubernetes Engine (GKE) ](https://docs.cloud.google.com/kubernetes-engine/docs)
  * [ GKE on Azure ](https://docs.cloud.google.com/kubernetes-engine/multi-cloud/docs/azure)
  * [ Guides ](https://docs.cloud.google.com/kubernetes-engine/multi-cloud/docs/azure/concepts/architecture)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# GKE Multi-Cloud audit logging

This document describes audit logging for GKE Multi-Cloud products, including GKE on AWS, GKE on AWS, and GKE attached clusters (EKS, AKS, and generic). Google Cloud services generate audit logs that record administrative and access activities within your Google Cloud resources. For more information about Cloud Audit Logs, see the following: 

  * [Types of audit logs](https://docs.cloud.google.com/logging/docs/audit#types)
  * [Audit log entry structure](https://docs.cloud.google.com/logging/docs/audit#audit_log_entry_structure)
  * [Storing and routing audit logs](https://docs.cloud.google.com/logging/docs/audit#storing_and_routing_audit_logs)
  * [Cloud Logging pricing summary](https://docs.cloud.google.com/stackdriver/pricing#logs-pricing-summary)
  * [Enable Data Access audit logs](https://docs.cloud.google.com/logging/docs/audit/configure-data-access)



## Service name

GKE Multi-Cloud products, including GKE on AWS, GKE on AWS, and GKE attached clusters (EKS, AKS, and generic) audit logs use the service name `gkemulticloud.googleapis.com`. Filter for this service: 
    
    
        protoPayload.serviceName="gkemulticloud.googleapis.com"
      

## Methods by permission type

Each IAM permission has a `type` property, whose value is an enum that can be one of four values: `ADMIN_READ`, `ADMIN_WRITE`, `DATA_READ`, or `DATA_WRITE`. When you call a method, GKE Multi-Cloud products, including GKE on AWS, GKE on AWS, and GKE attached clusters (EKS, AKS, and generic) generates an audit log whose category is dependent on the `type` property of the permission required to perform the method. Methods that require an IAM permission with the `type` property value of `DATA_READ`, `DATA_WRITE`, or `ADMIN_READ` generate [Data Access](https://docs.cloud.google.com/logging/docs/audit#data-access) audit logs. Methods that require an IAM permission with the `type` property value of `ADMIN_WRITE` generate [Admin Activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity) audit logs.

API methods in the following list that are marked with (LRO) are long-running operations (LROs). These methods usually generate two audit log entries: one when the operation starts and another when it ends. For more information see [Audit logs for long-running operations](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro). Permission type | Methods  
---|---  
`ADMIN_READ` | `google.cloud.gkemulticloud.v1.AttachedClusters.GenerateAttachedClusterInstallManifest`  
`google.cloud.gkemulticloud.v1.AttachedClusters.GetAttachedCluster`  
`google.cloud.gkemulticloud.v1.AttachedClusters.GetAttachedServerConfig`  
`google.cloud.gkemulticloud.v1.AttachedClusters.ListAttachedClusters`  
`google.cloud.gkemulticloud.v1.AwsClusters.GenerateAwsAccessToken`  
`google.cloud.gkemulticloud.v1.AwsClusters.GetAwsCluster`  
`google.cloud.gkemulticloud.v1.AwsClusters.GetAwsNodePool`  
`google.cloud.gkemulticloud.v1.AwsClusters.GetAwsServerConfig`  
`google.cloud.gkemulticloud.v1.AwsClusters.ListAwsClusters`  
`google.cloud.gkemulticloud.v1.AwsClusters.ListAwsNodePools`  
`google.cloud.gkemulticloud.v1.AzureClusters.GenerateAzureAccessToken`  
`google.cloud.gkemulticloud.v1.AzureClusters.GetAzureClient`  
`google.cloud.gkemulticloud.v1.AzureClusters.GetAzureCluster`  
`google.cloud.gkemulticloud.v1.AzureClusters.GetAzureNodePool`  
`google.cloud.gkemulticloud.v1.AzureClusters.GetAzureServerConfig`  
`google.cloud.gkemulticloud.v1.AzureClusters.ListAzureClients`  
`google.cloud.gkemulticloud.v1.AzureClusters.ListAzureClusters`  
`google.cloud.gkemulticloud.v1.AzureClusters.ListAzureNodePools`  
`ADMIN_WRITE` | `google.cloud.gkemulticloud.v1.AttachedClusters.CreateAttachedCluster` (LRO)  
`google.cloud.gkemulticloud.v1.AttachedClusters.DeleteAttachedCluster` (LRO)  
`google.cloud.gkemulticloud.v1.AttachedClusters.ImportAttachedCluster`  
`google.cloud.gkemulticloud.v1.AttachedClusters.UpdateAttachedCluster` (LRO)  
`google.cloud.gkemulticloud.v1.AwsClusters.CreateAwsCluster` (LRO)  
`google.cloud.gkemulticloud.v1.AwsClusters.CreateAwsNodePool` (LRO)  
`google.cloud.gkemulticloud.v1.AwsClusters.DeleteAwsCluster` (LRO)  
`google.cloud.gkemulticloud.v1.AwsClusters.DeleteAwsNodePool` (LRO)  
`google.cloud.gkemulticloud.v1.AwsClusters.UpdateAwsCluster` (LRO)  
`google.cloud.gkemulticloud.v1.AwsClusters.UpdateAwsNodePool` (LRO)  
`google.cloud.gkemulticloud.v1.AzureClusters.CreateAzureClient` (LRO)  
`google.cloud.gkemulticloud.v1.AzureClusters.CreateAzureCluster` (LRO)  
`google.cloud.gkemulticloud.v1.AzureClusters.CreateAzureNodePool` (LRO)  
`google.cloud.gkemulticloud.v1.AzureClusters.DeleteAzureClient` (LRO)  
`google.cloud.gkemulticloud.v1.AzureClusters.DeleteAzureCluster` (LRO)  
`google.cloud.gkemulticloud.v1.AzureClusters.DeleteAzureNodePool` (LRO)  
`google.cloud.gkemulticloud.v1.AzureClusters.UpdateAzureCluster` (LRO)  
`google.cloud.gkemulticloud.v1.AzureClusters.UpdateAzureNodePool` (LRO)  
  
## Audit logs for each API interface

### `google.cloud.gkemulticloud.v1.AttachedClusters`

The following audit logs are associated with methods belonging to `google.cloud.gkemulticloud.v1.AttachedClusters`.

#### `CreateAttachedCluster`

  * **Method** : `google.cloud.gkemulticloud.v1.AttachedClusters.CreateAttachedCluster`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `gkemulticloud.attachedClusters.create - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.gkemulticloud.v1.AttachedClusters.CreateAttachedCluster" `  




#### `DeleteAttachedCluster`

  * **Method** : `google.cloud.gkemulticloud.v1.AttachedClusters.DeleteAttachedCluster`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `gkemulticloud.attachedClusters.delete - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.gkemulticloud.v1.AttachedClusters.DeleteAttachedCluster" `  




#### `GenerateAttachedClusterInstallManifest`

  * **Method** : `google.cloud.gkemulticloud.v1.AttachedClusters.GenerateAttachedClusterInstallManifest`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `gkemulticloud.attachedClusters.generateInstallManifest - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.gkemulticloud.v1.AttachedClusters.GenerateAttachedClusterInstallManifest" `  




#### `GetAttachedCluster`

  * **Method** : `google.cloud.gkemulticloud.v1.AttachedClusters.GetAttachedCluster`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `gkemulticloud.attachedClusters.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.gkemulticloud.v1.AttachedClusters.GetAttachedCluster" `  




#### `GetAttachedServerConfig`

  * **Method** : `google.cloud.gkemulticloud.v1.AttachedClusters.GetAttachedServerConfig`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `gkemulticloud.attachedServerConfigs.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.gkemulticloud.v1.AttachedClusters.GetAttachedServerConfig" `  




#### `ImportAttachedCluster`

  * **Method** : `google.cloud.gkemulticloud.v1.AttachedClusters.ImportAttachedCluster`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `gkemulticloud.attachedClusters.import - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.gkemulticloud.v1.AttachedClusters.ImportAttachedCluster" `  




#### `ListAttachedClusters`

  * **Method** : `google.cloud.gkemulticloud.v1.AttachedClusters.ListAttachedClusters`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `gkemulticloud.attachedClusters.list - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.gkemulticloud.v1.AttachedClusters.ListAttachedClusters" `  




#### `UpdateAttachedCluster`

  * **Method** : `google.cloud.gkemulticloud.v1.AttachedClusters.UpdateAttachedCluster`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `gkemulticloud.attachedClusters.update - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.gkemulticloud.v1.AttachedClusters.UpdateAttachedCluster" `  




### `google.cloud.gkemulticloud.v1.AwsClusters`

The following audit logs are associated with methods belonging to `google.cloud.gkemulticloud.v1.AwsClusters`.

#### `CreateAwsCluster`

  * **Method** : `google.cloud.gkemulticloud.v1.AwsClusters.CreateAwsCluster`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `gkemulticloud.awsClusters.create - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.gkemulticloud.v1.AwsClusters.CreateAwsCluster" `  




#### `CreateAwsNodePool`

  * **Method** : `google.cloud.gkemulticloud.v1.AwsClusters.CreateAwsNodePool`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `gkemulticloud.awsNodePools.create - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.gkemulticloud.v1.AwsClusters.CreateAwsNodePool" `  




#### `DeleteAwsCluster`

  * **Method** : `google.cloud.gkemulticloud.v1.AwsClusters.DeleteAwsCluster`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `gkemulticloud.awsClusters.delete - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.gkemulticloud.v1.AwsClusters.DeleteAwsCluster" `  




#### `DeleteAwsNodePool`

  * **Method** : `google.cloud.gkemulticloud.v1.AwsClusters.DeleteAwsNodePool`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `gkemulticloud.awsNodePools.delete - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.gkemulticloud.v1.AwsClusters.DeleteAwsNodePool" `  




#### `GenerateAwsAccessToken`

  * **Method** : `google.cloud.gkemulticloud.v1.AwsClusters.GenerateAwsAccessToken`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `gkemulticloud.awsClusters.generateAccessToken - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.gkemulticloud.v1.AwsClusters.GenerateAwsAccessToken" `  




#### `GetAwsCluster`

  * **Method** : `google.cloud.gkemulticloud.v1.AwsClusters.GetAwsCluster`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `gkemulticloud.awsClusters.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.gkemulticloud.v1.AwsClusters.GetAwsCluster" `  




#### `GetAwsNodePool`

  * **Method** : `google.cloud.gkemulticloud.v1.AwsClusters.GetAwsNodePool`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `gkemulticloud.awsNodePools.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.gkemulticloud.v1.AwsClusters.GetAwsNodePool" `  




#### `GetAwsServerConfig`

  * **Method** : `google.cloud.gkemulticloud.v1.AwsClusters.GetAwsServerConfig`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `gkemulticloud.awsServerConfigs.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.gkemulticloud.v1.AwsClusters.GetAwsServerConfig" `  




#### `ListAwsClusters`

  * **Method** : `google.cloud.gkemulticloud.v1.AwsClusters.ListAwsClusters`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `gkemulticloud.awsClusters.list - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.gkemulticloud.v1.AwsClusters.ListAwsClusters" `  




#### `ListAwsNodePools`

  * **Method** : `google.cloud.gkemulticloud.v1.AwsClusters.ListAwsNodePools`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `gkemulticloud.awsNodePools.list - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.gkemulticloud.v1.AwsClusters.ListAwsNodePools" `  




#### `UpdateAwsCluster`

  * **Method** : `google.cloud.gkemulticloud.v1.AwsClusters.UpdateAwsCluster`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `gkemulticloud.awsClusters.update - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.gkemulticloud.v1.AwsClusters.UpdateAwsCluster" `  




#### `UpdateAwsNodePool`

  * **Method** : `google.cloud.gkemulticloud.v1.AwsClusters.UpdateAwsNodePool`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `gkemulticloud.awsNodePools.update - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.gkemulticloud.v1.AwsClusters.UpdateAwsNodePool" `  




### `google.cloud.gkemulticloud.v1.AzureClusters`

The following audit logs are associated with methods belonging to `google.cloud.gkemulticloud.v1.AzureClusters`.

#### `CreateAzureClient`

  * **Method** : `google.cloud.gkemulticloud.v1.AzureClusters.CreateAzureClient`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `gkemulticloud.azureClients.create - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.gkemulticloud.v1.AzureClusters.CreateAzureClient" `  




#### `CreateAzureCluster`

  * **Method** : `google.cloud.gkemulticloud.v1.AzureClusters.CreateAzureCluster`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `gkemulticloud.azureClusters.create - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.gkemulticloud.v1.AzureClusters.CreateAzureCluster" `  




#### `CreateAzureNodePool`

  * **Method** : `google.cloud.gkemulticloud.v1.AzureClusters.CreateAzureNodePool`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `gkemulticloud.azureNodePools.create - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.gkemulticloud.v1.AzureClusters.CreateAzureNodePool" `  




#### `DeleteAzureClient`

  * **Method** : `google.cloud.gkemulticloud.v1.AzureClusters.DeleteAzureClient`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `gkemulticloud.azureClients.delete - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.gkemulticloud.v1.AzureClusters.DeleteAzureClient" `  




#### `DeleteAzureCluster`

  * **Method** : `google.cloud.gkemulticloud.v1.AzureClusters.DeleteAzureCluster`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `gkemulticloud.azureClusters.delete - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.gkemulticloud.v1.AzureClusters.DeleteAzureCluster" `  




#### `DeleteAzureNodePool`

  * **Method** : `google.cloud.gkemulticloud.v1.AzureClusters.DeleteAzureNodePool`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `gkemulticloud.azureNodePools.delete - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.gkemulticloud.v1.AzureClusters.DeleteAzureNodePool" `  




#### `GenerateAzureAccessToken`

  * **Method** : `google.cloud.gkemulticloud.v1.AzureClusters.GenerateAzureAccessToken`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `gkemulticloud.azureClusters.generateAccessToken - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.gkemulticloud.v1.AzureClusters.GenerateAzureAccessToken" `  




#### `GetAzureClient`

  * **Method** : `google.cloud.gkemulticloud.v1.AzureClusters.GetAzureClient`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `gkemulticloud.azureClients.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.gkemulticloud.v1.AzureClusters.GetAzureClient" `  




#### `GetAzureCluster`

  * **Method** : `google.cloud.gkemulticloud.v1.AzureClusters.GetAzureCluster`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `gkemulticloud.azureClusters.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.gkemulticloud.v1.AzureClusters.GetAzureCluster" `  




#### `GetAzureNodePool`

  * **Method** : `google.cloud.gkemulticloud.v1.AzureClusters.GetAzureNodePool`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `gkemulticloud.azureNodePools.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.gkemulticloud.v1.AzureClusters.GetAzureNodePool" `  




#### `GetAzureServerConfig`

  * **Method** : `google.cloud.gkemulticloud.v1.AzureClusters.GetAzureServerConfig`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `gkemulticloud.azureServerConfigs.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.gkemulticloud.v1.AzureClusters.GetAzureServerConfig" `  




#### `ListAzureClients`

  * **Method** : `google.cloud.gkemulticloud.v1.AzureClusters.ListAzureClients`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `gkemulticloud.azureClients.list - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.gkemulticloud.v1.AzureClusters.ListAzureClients" `  




#### `ListAzureClusters`

  * **Method** : `google.cloud.gkemulticloud.v1.AzureClusters.ListAzureClusters`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `gkemulticloud.azureClusters.list - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.gkemulticloud.v1.AzureClusters.ListAzureClusters" `  




#### `ListAzureNodePools`

  * **Method** : `google.cloud.gkemulticloud.v1.AzureClusters.ListAzureNodePools`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `gkemulticloud.azureNodePools.list - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.gkemulticloud.v1.AzureClusters.ListAzureNodePools" `  




#### `UpdateAzureCluster`

  * **Method** : `google.cloud.gkemulticloud.v1.AzureClusters.UpdateAzureCluster`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `gkemulticloud.azureClusters.update - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.gkemulticloud.v1.AzureClusters.UpdateAzureCluster" `  




#### `UpdateAzureNodePool`

  * **Method** : `google.cloud.gkemulticloud.v1.AzureClusters.UpdateAzureNodePool`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `gkemulticloud.azureNodePools.update - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.gkemulticloud.v1.AzureClusters.UpdateAzureNodePool" `  




## Methods that don't produce audit logs

A method might not produce audit logs for one or more of the following reasons: 

  * It is a high volume method involving significant log generation and storage costs.
  * It has low auditing value.
  * Another audit or platform log already provides method coverage.



The following methods don't produce audit logs:

  * `google.cloud.gkemulticloud.v1.AttachedClusters.GenerateAttachedClusterAgentToken`
  * `google.cloud.gkemulticloud.v1.AwsClusters.GenerateAwsClusterAgentToken`
  * `google.cloud.gkemulticloud.v1.AwsClusters.GetAwsJsonWebKeys`
  * `google.cloud.gkemulticloud.v1.AwsClusters.GetAwsOpenIdConfig`
  * `google.cloud.gkemulticloud.v1.AwsClusters.RollbackAwsNodePoolUpdate`
  * `google.cloud.gkemulticloud.v1.AzureClusters.GenerateAzureClusterAgentToken`
  * `google.cloud.gkemulticloud.v1.AzureClusters.GetAzureJsonWebKeys`
  * `google.cloud.gkemulticloud.v1.AzureClusters.GetAzureOpenIdConfig`
  * `google.longrunning.Operations.CancelOperation`
  * `google.longrunning.Operations.DeleteOperation`
  * `google.longrunning.Operations.GetOperation`
  * `google.longrunning.Operations.ListOperations`
  * `google.longrunning.Operations.WaitOperation`



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
