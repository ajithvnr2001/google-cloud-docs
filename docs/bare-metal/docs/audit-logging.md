---
url: https://docs.cloud.google.com/bare-metal/docs/audit-logging/
title: Bare Metal Solution audit logging \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T07:53:39.364108+00:00
---

# Bare Metal Solution audit logging  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/bare-metal/docs/audit-logging/

The availability of Bare Metal Solution is transitioning to a specialized, allowlist-only model. If you are an existing customer, please contact your Google account team to explore the value of migrating to new [Oracle and Google Cloud strategic partnership offerings](https://docs.cloud.google.com/bare-metal/docs/explore-oracle-partnership-offerings). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Bare Metal ](https://docs.cloud.google.com/bare-metal/docs)
  * [ Guides ](https://docs.cloud.google.com/bare-metal/docs/bms-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Bare Metal Solution audit logging

This document lists the audited methods for Bare Metal Solution. Google Cloud services generate audit logs that record administrative and access activities within your Google Cloud resources. For more information about Cloud Audit Logs, see the following: 

  * [Types of audit logs](https://docs.cloud.google.com/logging/docs/audit#types)
  * [Audit log entry structure](https://docs.cloud.google.com/logging/docs/audit#audit_log_entry_structure)
  * [Storing and routing audit logs](https://docs.cloud.google.com/logging/docs/audit#storing_and_routing_audit_logs)
  * [Cloud Logging pricing summary](https://docs.cloud.google.com/stackdriver/pricing#logs-pricing-summary)
  * [Enable Data Access audit logs](https://docs.cloud.google.com/logging/docs/audit/configure-data-access)



## Service name

To view the Bare Metal Solution audit logs, do the following:

  1. In the Google Cloud console, go to the Logs Explorer page:

[Go to Logs Explorer](https://console.cloud.google.com/logs/query)

  2. Copy and paste the following query into the **Query** field of the Logs Explorer, and then click **Run query**.
         
         protoPayload.serviceName="baremetalsolution.googleapis.com"
           




## Methods by permission type

Each IAM permission has a `type` property, whose value is an enum that can be one of four values: `ADMIN_READ`, `ADMIN_WRITE`, `DATA_READ`, or `DATA_WRITE`. When you call a method, Bare Metal Solution generates an audit log whose category is dependent on the `type` property of the permission required to perform the method. Methods that require an IAM permission with the `type` property value of `DATA_READ`, `DATA_WRITE`, or `ADMIN_READ` generate [Data Access](https://docs.cloud.google.com/logging/docs/audit#data-access) audit logs. Methods that require an IAM permission with the `type` property value of `ADMIN_WRITE` generate [Admin Activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity) audit logs.

API methods in the following list that are marked with (LRO) are long-running operations (LROs). These methods usually generate two audit log entries: one when the operation starts and another when it ends. For more information see [Audit logs for long-running operations](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro). Permission type | Methods  
---|---  
`ADMIN_READ` | `google.cloud.baremetalsolution.v2.BareMetalSolution.GetInstance`  
`google.cloud.baremetalsolution.v2.BareMetalSolution.GetLun`  
`google.cloud.baremetalsolution.v2.BareMetalSolution.GetNetwork`  
`google.cloud.baremetalsolution.v2.BareMetalSolution.GetNfsShare`  
`google.cloud.baremetalsolution.v2.BareMetalSolution.GetOSImage`  
`google.cloud.baremetalsolution.v2.BareMetalSolution.GetVolume`  
`google.cloud.baremetalsolution.v2.BareMetalSolution.GetVolumeSnapshot`  
`google.cloud.baremetalsolution.v2.BareMetalSolution.ListInstances`  
`google.cloud.baremetalsolution.v2.BareMetalSolution.ListLuns`  
`google.cloud.baremetalsolution.v2.BareMetalSolution.ListNetworks`  
`google.cloud.baremetalsolution.v2.BareMetalSolution.ListNfsShares`  
`google.cloud.baremetalsolution.v2.BareMetalSolution.ListOSImages`  
`google.cloud.baremetalsolution.v2.BareMetalSolution.ListVolumeSnapshots`  
`google.cloud.baremetalsolution.v2.BareMetalSolution.ListVolumes`  
`google.cloud.baremetalsolution.v2.BareMetalSolution.LoadInstanceAuthInfo`  
`ADMIN_WRITE` | `google.cloud.baremetalsolution.v2.BareMetalSolution.CreateProvisioningConfig`  
`google.cloud.baremetalsolution.v2.BareMetalSolution.DetachLun`  
`google.cloud.baremetalsolution.v2.BareMetalSolution.DisableHyperthreading`  
`google.cloud.baremetalsolution.v2.BareMetalSolution.DisableInteractiveSerialConsole`  
`google.cloud.baremetalsolution.v2.BareMetalSolution.EnableHyperthreading`  
`google.cloud.baremetalsolution.v2.BareMetalSolution.EnableInteractiveSerialConsole`  
`google.cloud.baremetalsolution.v2.BareMetalSolution.EvictLun`  
`google.cloud.baremetalsolution.v2.BareMetalSolution.EvictVolume`  
`google.cloud.baremetalsolution.v2.BareMetalSolution.GetProvisioningConfig`  
`google.cloud.baremetalsolution.v2.BareMetalSolution.ListNetworkUsage`  
`google.cloud.baremetalsolution.v2.BareMetalSolution.ListProvisioningQuotas`  
`google.cloud.baremetalsolution.v2.BareMetalSolution.ReimageInstance`  
`google.cloud.baremetalsolution.v2.BareMetalSolution.RenameInstance`  
`google.cloud.baremetalsolution.v2.BareMetalSolution.RenameNetwork`  
`google.cloud.baremetalsolution.v2.BareMetalSolution.RenameNfsShare`  
`google.cloud.baremetalsolution.v2.BareMetalSolution.RenameVolume`  
`google.cloud.baremetalsolution.v2.BareMetalSolution.ResizeVolume`  
`google.cloud.baremetalsolution.v2.BareMetalSolution.StopInstance`  
`google.cloud.baremetalsolution.v2.BareMetalSolution.SubmitProvisioningConfig`  
`google.cloud.baremetalsolution.v2.BareMetalSolution.UpdateInstance`  
`google.cloud.baremetalsolution.v2.BareMetalSolution.UpdateNetwork`  
`google.cloud.baremetalsolution.v2.BareMetalSolution.UpdateProvisioningConfig`  
`DATA_READ` | `google.cloud.baremetalsolution.v2.BareMetalSolution.ListSSHKeys`  
`DATA_WRITE` | `google.cloud.baremetalsolution.v2.BareMetalSolution.CreateNfsShare`  
`google.cloud.baremetalsolution.v2.BareMetalSolution.CreateSSHKey`  
`google.cloud.baremetalsolution.v2.BareMetalSolution.CreateVolumeSnapshot`  
`google.cloud.baremetalsolution.v2.BareMetalSolution.DeleteNfsShare`  
`google.cloud.baremetalsolution.v2.BareMetalSolution.DeleteSSHKey`  
`google.cloud.baremetalsolution.v2.BareMetalSolution.DeleteVolumeSnapshot`  
`google.cloud.baremetalsolution.v2.BareMetalSolution.ResetInstance`  
`google.cloud.baremetalsolution.v2.BareMetalSolution.RestoreVolumeSnapshot`  
`google.cloud.baremetalsolution.v2.BareMetalSolution.StartInstance`  
`google.cloud.baremetalsolution.v2.BareMetalSolution.UpdateNfsShare`  
`google.cloud.baremetalsolution.v2.BareMetalSolution.UpdateVolume`  
  
## API interface audit logs

For information about how and which permissions are evaluated for each method, see the Identity and Access Management documentation for Bare Metal Solution.

### `google.cloud.baremetalsolution.v2.BareMetalSolution`

The following audit logs are associated with methods belonging to `google.cloud.baremetalsolution.v2.BareMetalSolution`.

#### `CreateNfsShare`

  * **Method** : `google.cloud.baremetalsolution.v2.BareMetalSolution.CreateNfsShare`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `baremetalsolution.nfsshares.create - DATA_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.baremetalsolution.v2.BareMetalSolution.CreateNfsShare" `  




#### `CreateProvisioningConfig`

  * **Method** : `google.cloud.baremetalsolution.v2.BareMetalSolution.CreateProvisioningConfig`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `baremetalsolution.instances.create - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.baremetalsolution.v2.BareMetalSolution.CreateProvisioningConfig" `  




#### `CreateSSHKey`

  * **Method** : `google.cloud.baremetalsolution.v2.BareMetalSolution.CreateSSHKey`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `baremetalsolution.sshKeys.create - DATA_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.baremetalsolution.v2.BareMetalSolution.CreateSSHKey" `  




#### `CreateVolumeSnapshot`

  * **Method** : `google.cloud.baremetalsolution.v2.BareMetalSolution.CreateVolumeSnapshot`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `baremetalsolution.volumesnapshots.create - DATA_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.baremetalsolution.v2.BareMetalSolution.CreateVolumeSnapshot" `  




#### `DeleteNfsShare`

  * **Method** : `google.cloud.baremetalsolution.v2.BareMetalSolution.DeleteNfsShare`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `baremetalsolution.nfsshares.delete - DATA_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.baremetalsolution.v2.BareMetalSolution.DeleteNfsShare" `  




#### `DeleteSSHKey`

  * **Method** : `google.cloud.baremetalsolution.v2.BareMetalSolution.DeleteSSHKey`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `baremetalsolution.sshKeys.delete - DATA_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.baremetalsolution.v2.BareMetalSolution.DeleteSSHKey" `  




#### `DeleteVolumeSnapshot`

  * **Method** : `google.cloud.baremetalsolution.v2.BareMetalSolution.DeleteVolumeSnapshot`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `baremetalsolution.volumesnapshots.delete - DATA_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.baremetalsolution.v2.BareMetalSolution.DeleteVolumeSnapshot" `  




#### `DetachLun`

  * **Method** : `google.cloud.baremetalsolution.v2.BareMetalSolution.DetachLun`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `baremetalsolution.instances.detachLun - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.baremetalsolution.v2.BareMetalSolution.DetachLun" `  




#### `DisableHyperthreading`

  * **Method** : `google.cloud.baremetalsolution.v2.BareMetalSolution.DisableHyperthreading`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `baremetalsolution.instances.disableHyperthreading - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.baremetalsolution.v2.BareMetalSolution.DisableHyperthreading" `  




#### `DisableInteractiveSerialConsole`

  * **Method** : `google.cloud.baremetalsolution.v2.BareMetalSolution.DisableInteractiveSerialConsole`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `baremetalsolution.instances.disableInteractiveSerialConsole - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.baremetalsolution.v2.BareMetalSolution.DisableInteractiveSerialConsole" `  




#### `EnableHyperthreading`

  * **Method** : `google.cloud.baremetalsolution.v2.BareMetalSolution.EnableHyperthreading`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `baremetalsolution.instances.enableHyperthreading - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.baremetalsolution.v2.BareMetalSolution.EnableHyperthreading" `  




#### `EnableInteractiveSerialConsole`

  * **Method** : `google.cloud.baremetalsolution.v2.BareMetalSolution.EnableInteractiveSerialConsole`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `baremetalsolution.instances.enableInteractiveSerialConsole - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.baremetalsolution.v2.BareMetalSolution.EnableInteractiveSerialConsole" `  




#### `EvictLun`

  * **Method** : `google.cloud.baremetalsolution.v2.BareMetalSolution.EvictLun`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `baremetalsolution.luns.evict - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.baremetalsolution.v2.BareMetalSolution.EvictLun" `  




#### `EvictVolume`

  * **Method** : `google.cloud.baremetalsolution.v2.BareMetalSolution.EvictVolume`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `baremetalsolution.volumes.evict - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.baremetalsolution.v2.BareMetalSolution.EvictVolume" `  




#### `GetInstance`

  * **Method** : `google.cloud.baremetalsolution.v2.BareMetalSolution.GetInstance`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `baremetalsolution.instances.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.baremetalsolution.v2.BareMetalSolution.GetInstance" `  




#### `GetLun`

  * **Method** : `google.cloud.baremetalsolution.v2.BareMetalSolution.GetLun`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `baremetalsolution.luns.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.baremetalsolution.v2.BareMetalSolution.GetLun" `  




#### `GetNetwork`

  * **Method** : `google.cloud.baremetalsolution.v2.BareMetalSolution.GetNetwork`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `baremetalsolution.networks.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.baremetalsolution.v2.BareMetalSolution.GetNetwork" `  




#### `GetNfsShare`

  * **Method** : `google.cloud.baremetalsolution.v2.BareMetalSolution.GetNfsShare`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `baremetalsolution.nfsshares.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.baremetalsolution.v2.BareMetalSolution.GetNfsShare" `  




#### `GetOSImage`

  * **Method** : `google.cloud.baremetalsolution.v2.BareMetalSolution.GetOSImage`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `baremetalsolution.osimages.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.baremetalsolution.v2.BareMetalSolution.GetOSImage" `  




#### `GetProvisioningConfig`

  * **Method** : `google.cloud.baremetalsolution.v2.BareMetalSolution.GetProvisioningConfig`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `baremetalsolution.instances.create - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.baremetalsolution.v2.BareMetalSolution.GetProvisioningConfig" `  




#### `GetVolume`

  * **Method** : `google.cloud.baremetalsolution.v2.BareMetalSolution.GetVolume`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `baremetalsolution.volumes.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.baremetalsolution.v2.BareMetalSolution.GetVolume" `  




#### `GetVolumeSnapshot`

  * **Method** : `google.cloud.baremetalsolution.v2.BareMetalSolution.GetVolumeSnapshot`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `baremetalsolution.volumesnapshots.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.baremetalsolution.v2.BareMetalSolution.GetVolumeSnapshot" `  




#### `ListInstances`

  * **Method** : `google.cloud.baremetalsolution.v2.BareMetalSolution.ListInstances`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `baremetalsolution.instances.list - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.baremetalsolution.v2.BareMetalSolution.ListInstances" `  




#### `ListLuns`

  * **Method** : `google.cloud.baremetalsolution.v2.BareMetalSolution.ListLuns`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `baremetalsolution.luns.list - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.baremetalsolution.v2.BareMetalSolution.ListLuns" `  




#### `ListNetworkUsage`

  * **Method** : `google.cloud.baremetalsolution.v2.BareMetalSolution.ListNetworkUsage`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `baremetalsolution.instances.create - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.baremetalsolution.v2.BareMetalSolution.ListNetworkUsage" `  




#### `ListNetworks`

  * **Method** : `google.cloud.baremetalsolution.v2.BareMetalSolution.ListNetworks`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `baremetalsolution.networks.list - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.baremetalsolution.v2.BareMetalSolution.ListNetworks" `  




#### `ListNfsShares`

  * **Method** : `google.cloud.baremetalsolution.v2.BareMetalSolution.ListNfsShares`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `baremetalsolution.nfsshares.list - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.baremetalsolution.v2.BareMetalSolution.ListNfsShares" `  




#### `ListOSImages`

  * **Method** : `google.cloud.baremetalsolution.v2.BareMetalSolution.ListOSImages`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `baremetalsolution.osimages.list - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.baremetalsolution.v2.BareMetalSolution.ListOSImages" `  




#### `ListProvisioningQuotas`

  * **Method** : `google.cloud.baremetalsolution.v2.BareMetalSolution.ListProvisioningQuotas`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `baremetalsolution.instances.create - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.baremetalsolution.v2.BareMetalSolution.ListProvisioningQuotas" `  




#### `ListSSHKeys`

  * **Method** : `google.cloud.baremetalsolution.v2.BareMetalSolution.ListSSHKeys`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `baremetalsolution.sshKeys.list - DATA_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.baremetalsolution.v2.BareMetalSolution.ListSSHKeys" `  




#### `ListVolumeSnapshots`

  * **Method** : `google.cloud.baremetalsolution.v2.BareMetalSolution.ListVolumeSnapshots`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `baremetalsolution.volumesnapshots.list - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.baremetalsolution.v2.BareMetalSolution.ListVolumeSnapshots" `  




#### `ListVolumes`

  * **Method** : `google.cloud.baremetalsolution.v2.BareMetalSolution.ListVolumes`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `baremetalsolution.volumes.list - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.baremetalsolution.v2.BareMetalSolution.ListVolumes" `  




#### `LoadInstanceAuthInfo`

  * **Method** : `google.cloud.baremetalsolution.v2.BareMetalSolution.LoadInstanceAuthInfo`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `baremetalsolution.instances.loadAuthInfo - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.baremetalsolution.v2.BareMetalSolution.LoadInstanceAuthInfo" `  




#### `ReimageInstance`

  * **Method** : `google.cloud.baremetalsolution.v2.BareMetalSolution.ReimageInstance`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `baremetalsolution.instances.reimage - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.baremetalsolution.v2.BareMetalSolution.ReimageInstance" `  




#### `RenameInstance`

  * **Method** : `google.cloud.baremetalsolution.v2.BareMetalSolution.RenameInstance`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `baremetalsolution.instances.rename - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.baremetalsolution.v2.BareMetalSolution.RenameInstance" `  




#### `RenameNetwork`

  * **Method** : `google.cloud.baremetalsolution.v2.BareMetalSolution.RenameNetwork`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `baremetalsolution.networks.rename - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.baremetalsolution.v2.BareMetalSolution.RenameNetwork" `  




#### `RenameNfsShare`

  * **Method** : `google.cloud.baremetalsolution.v2.BareMetalSolution.RenameNfsShare`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `baremetalsolution.nfsshares.rename - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.baremetalsolution.v2.BareMetalSolution.RenameNfsShare" `  




#### `RenameVolume`

  * **Method** : `google.cloud.baremetalsolution.v2.BareMetalSolution.RenameVolume`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `baremetalsolution.volumes.rename - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.baremetalsolution.v2.BareMetalSolution.RenameVolume" `  




#### `ResetInstance`

  * **Method** : `google.cloud.baremetalsolution.v2.BareMetalSolution.ResetInstance`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `baremetalsolution.instances.reset - DATA_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.baremetalsolution.v2.BareMetalSolution.ResetInstance" `  




#### `ResizeVolume`

  * **Method** : `google.cloud.baremetalsolution.v2.BareMetalSolution.ResizeVolume`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `baremetalsolution.volumes.resize - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.baremetalsolution.v2.BareMetalSolution.ResizeVolume" `  




#### `RestoreVolumeSnapshot`

  * **Method** : `google.cloud.baremetalsolution.v2.BareMetalSolution.RestoreVolumeSnapshot`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `baremetalsolution.volumesnapshots.restore - DATA_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.baremetalsolution.v2.BareMetalSolution.RestoreVolumeSnapshot" `  




#### `StartInstance`

  * **Method** : `google.cloud.baremetalsolution.v2.BareMetalSolution.StartInstance`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `baremetalsolution.instances.start - DATA_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.baremetalsolution.v2.BareMetalSolution.StartInstance" `  




#### `StopInstance`

  * **Method** : `google.cloud.baremetalsolution.v2.BareMetalSolution.StopInstance`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `baremetalsolution.instances.stop - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.baremetalsolution.v2.BareMetalSolution.StopInstance" `  




#### `SubmitProvisioningConfig`

  * **Method** : `google.cloud.baremetalsolution.v2.BareMetalSolution.SubmitProvisioningConfig`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `baremetalsolution.instances.create - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.baremetalsolution.v2.BareMetalSolution.SubmitProvisioningConfig" `  




#### `UpdateInstance`

  * **Method** : `google.cloud.baremetalsolution.v2.BareMetalSolution.UpdateInstance`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `baremetalsolution.instances.update - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.baremetalsolution.v2.BareMetalSolution.UpdateInstance" `  




#### `UpdateNetwork`

  * **Method** : `google.cloud.baremetalsolution.v2.BareMetalSolution.UpdateNetwork`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `baremetalsolution.networks.update - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.baremetalsolution.v2.BareMetalSolution.UpdateNetwork" `  




#### `UpdateNfsShare`

  * **Method** : `google.cloud.baremetalsolution.v2.BareMetalSolution.UpdateNfsShare`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `baremetalsolution.nfsshares.update - DATA_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.baremetalsolution.v2.BareMetalSolution.UpdateNfsShare" `  




#### `UpdateProvisioningConfig`

  * **Method** : `google.cloud.baremetalsolution.v2.BareMetalSolution.UpdateProvisioningConfig`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `baremetalsolution.instances.create - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.baremetalsolution.v2.BareMetalSolution.UpdateProvisioningConfig" `  




#### `UpdateVolume`

  * **Method** : `google.cloud.baremetalsolution.v2.BareMetalSolution.UpdateVolume`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `baremetalsolution.volumes.update - DATA_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.baremetalsolution.v2.BareMetalSolution.UpdateVolume" `  




## Methods that don't produce audit logs

A method might not produce audit logs for one or more of the following reasons: 

  * It is a high volume method involving significant log generation and storage costs.
  * It has low auditing value.
  * Another audit or platform log already provides method coverage.



The following methods don't produce audit logs:

  * `google.cloud.baremetalsolution.v2.BareMetalSolution.GetOperation`
  * `google.cloud.location.Locations.GetLocation`
  * `google.cloud.location.Locations.ListLocations`



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
