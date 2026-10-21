---
url: https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.15/how-to/vsphere-requirements/
title: vSphere requirements \u00a0|\u00a0 Google Distributed Cloud Virtual for VMware \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T17:11:50.818314+00:00
---

# vSphere requirements  |  Google Distributed Cloud Virtual for VMware  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.15/how-to/vsphere-requirements/

**Version 1.15**. This version is no longer supported. For more information see the [ version support policy](https://cloud.google.com/anthos/clusters/docs/on-prem/latest/getting-support#version_support_policy). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Google Distributed Cloud ](https://docs.cloud.google.com/distributed-cloud)
  * [ Documentation ](https://docs.cloud.google.com/kubernetes-engine/enterprise/clusters/docs)
  * [ GDCV for VMware 1.15 ](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.15)
  * [ Guides ](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.15/overview)



Send feedback 

#  vSphere requirements Stay organized with collections  Save and categorize content based on your preferences. 

Version 1.15 keyboard_arrow_down

  * [ Latest version ](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/latest/how-to/vsphere-requirements)
  * [ Version 1.16 ](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.16/how-to/vsphere-requirements)
  * [ Earlier versions (unsupported) ](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/latest/version-history#expandable-1)



Google Distributed Cloud runs on your premises in a [vSphere](https://www.vmware.com/products/vsphere.html) environment. This document describes requirements for your vSphere environment.

## Version compatibility

The vSphere requirements vary according to which version of Google Distributed Cloud you are using. For more information, see the version compatibility matrix for [fully supported versions](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.15/version-history#version-compatibility) and [earlier versions](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.15/version-history#expandable-4).

## Supported versions

[vSphere](https://www.vmware.com/products/vsphere.html) is VMware's server virtualization software. vSphere includes [ESXi](https://www.vmware.com/products/esxi-and-esx.html) and [vCenter Server](https://www.vmware.com/products/vcenter-server.html).

Google Distributed Cloud supports these versions of [ESXi](https://kb.vmware.com/s/article/2143832) and [vCenter Server](https://kb.vmware.com/s/article/2143838)

  * 7.0 Update 2 and later updates of version 7.0
  * 8.0 (**Preview**)



We recommend that you use 7.0 Update 3 or a later update of version 7.0.

If you want to create CSI volume snapshots, then you must have one of the following versions:

  * 7.0 Update 3 or a later update of version 7.0
  * 8.0



## License requirements

You need one of the following licenses:

  * [vSphere Enterprise Plus](https://www.vmware.com/products/vsphere.html#compare-editions) license. Along with this license, you must have a valid support subscription.

  * [vSphere Standard](https://www.vmware.com/products/vsphere.html#compare-editions) license. Along with this license, you must have a valid support subscription. With this license, you cannot enable [anti-affinity groups](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.15/how-to/admin-cluster-configuration-file#antiaffinitygroups-enabled-field). Also, you cannot specify your own [resource pool](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.15/how-to/admin-cluster-configuration-file#vcenter-resourcepool-field). You must use the default resource pool.




## Hardware requirements

Google Distributed Cloud runs on a set of physical hosts that run the VMware [ESXi hypervisor](https://www.vmware.com/products/esxi-and-esx.html). To learn about the hardware requirements for ESXi, see [ESXi Hardware Requirements](https://docs.vmware.com/en/VMware-vSphere/7.0/com.vmware.esxi.install.doc/GUID-DEB8086A-306B-4239-BF76-E354679202FC.html).

For production environments, we strongly recommend the following:

  * Enable [VMware Distributed Resource Scheduler (DRS)](https://www.vmware.com/products/vsphere/drs-dpm.html).

  * Have at least four ESXi hosts available for your cluster VMs.

  * Enable [Network File Copy (NFC)](https://docs.vmware.com/en/VMware-vSphere/6.5/com.vmware.vsphere.upgrade.doc/GUID-171B99EA-15B3-4CC5-8B9A-577D8336FAA0.html) traffic among ESXi hosts to allow OS template sharing, if you plan to deploy Anthos clusters on VMware on different vSphere clusters or resource pools within the same vSphere datacenter.

  * Set [`antiAffinityGroups.enabled`](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.15/how-to/admin-cluster-configuration-file#antiaffinitygroups-enabled-field) to `true` in your cluster configuration files.




If you set `antiAffinityGroups.enabled` to `true`, Google Distributed Cloud creates DRS anti-affinity rules for your cluster nodes, causing them to be spread across at least three physical ESXi hosts. Even though the DRS rules require that cluster nodes are spread across three ESXi hosts, we strongly recommend that you have at least four ESXi hosts available. This protects you from losing your cluster control plane. For example, suppose you have only three ESXi hosts, and your admin cluster control-plane node is on an ESXi host that fails. The DRS rule will prevent the control-plane node from being placed on one of the remaining two ESXi hosts.

For evaluation and proof of concept, you can set `antiAffinityGroups.enabled` to `false`, and use only one ESXi host. For more information, see [Set up minimal infrastructure](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.15/how-to/minimal-infrastructure).

## vCenter user account privileges

To set up a vSphere environment, an organization administrator might choose to use a vCenter user account that has the [vCenter Server Administrator role](https://docs.vmware.com/en/VMware-vSphere/7.0/com.vmware.vsphere.security.doc/GUID-93B962A7-93FA-4E96-B68F-AE66D3D6C663.html). This role provides full access to all vSphere objects.

After the vSphere environment is set up, a cluster administrator can create admin clusters and user clusters. The cluster administrator does not need all the privileges provided by the vCenter Server Administrator role.

When a cluster administrator or developer creates a cluster, they provide a vCenter user account in a [credentials configuration file](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.15/how-to/credentials-configuration-file). We recommend that the vCenter user account that is listed in a credentials configuration file be assigned one or more [custom roles](https://docs.vmware.com/en/VMware-vSphere/7.0/com.vmware.vsphere.security.doc/GUID-41E5E52E-A95B-4E81-9724-6AD6800BEF78.html) that have the minimum [privileges](https://docs.vmware.com/en/VMware-vSphere/7.0/com.vmware.vsphere.security.doc/GUID-ED56F3C4-77D0-49E3-88B6-B99B8B437B62.html) required for cluster creation and management.

There are two different approaches an organization administrator can take:

  * Create several roles with varying degrees of privilege. Then create permissions that assign those limited roles to a user or group on individual vSphere objects.

  * Create one role that has all the needed privileges. Then create a [global permission](https://docs.vmware.com/en/VMware-vSphere/7.0/com.vmware.vsphere.security.doc/GUID-C7702E31-1623-4189-89CB-E1136AA27972.html) that assigns that role to a particular user or group on all objects in your vSphere hierarchies.




We recommend the first approach, because it limits access and increases the security of your vCenter Server environment. For more information, see [Using Roles to Assign Privileges](https://docs.vmware.com/en/VMware-vSphere/7.0/com.vmware.vsphere.security.doc/GUID-18071E9A-EED1-4968-8D51-E0B4F526FDA3.html) and [Best Practices for Roles and Permissions](https://docs.vmware.com/en/VMware-vSphere/7.0/com.vmware.vsphere.security.doc/GUID-FAA074CC-E8C9-4F13-ABCF-6CF7F15F04EE.html)

For information on using the second approach, see Create one global permission.

The following table shows four custom roles that an organization administrator can create. The administrator can then use the custom roles to assign permissions on specific vSphere objects:

Custom role| Privileges| Objects| Propagate to  
child objects?  
---|---|---|---  
ClusterEditor |  [System](https://docs.vmware.com/en/VMware-vSphere/7.0/com.vmware.vsphere.security.doc/GUID-18071E9A-EED1-4968-8D51-E0B4F526FDA3.html).Read  
System.View  
System.Anonymous  
[Host.Inventory](https://docs.vmware.com/en/VMware-vSphere/7.0/com.vmware.vsphere.security.doc/GUID-71C3E5D6-8E57-4C86-B133-DB7F5ADAC1A4.html).Modify cluster  | [cluster](https://docs.vmware.com/en/VMware-vSphere/7.0/com.vmware.vsphere.vcenterhost.doc/GUID-F7818000-26E3-4E2A-93D2-FCDCE7114508.html) | Yes  
SessionValidator |  System.Read  
System.View  
System.Anonymous  
[Sessions](https://docs.vmware.com/en/VMware-vSphere/7.0/com.vmware.vsphere.security.doc/GUID-84BDB0C4-AAB8-41AA-BB52-66C5E2A5B5A1.html).Validate session  
[Cns](https://docs.vmware.com/en/VMware-vSphere/7.0/com.vmware.vsphere.security.doc/GUID-C04F1605-D158-4B65-810F-6F5B109BCDEC.html).Searchable  
[Profile-driven storage](https://docs.vmware.com/en/VMware-vSphere/7.0/com.vmware.vsphere.security.doc/GUID-9A79C4A8-8415-433B-A2E9-6A5999E92207.html).Profile-driven storage view  | Root vCenter Server | No  
ReadOnly |  System.Read  
System.View  
System.Anonymous  |  [data center](https://docs.vmware.com/en/VMware-vSphere/7.0/com.vmware.vsphere.vcenterhost.doc/GUID-7FDFBDBE-F8AC-4D00-AE5E-3F14D7472FAF.html)  
[network](https://docs.vmware.com/en/VMware-vSphere/7.0/com.vmware.vsphere.networking.doc/GUID-2B11DBB8-CB3C-4AFF-8885-EFEA0FC562F4.html) | Yes  
Anthos | Privileges in the Anthos role |  [datastore](https://docs.vmware.com/en/VMware-vSphere/7.0/com.vmware.vsphere.storage.doc/GUID-3CC7078E-9C30-402C-B2E1-2542BEE67E8F.html)  
[resource pool](https://docs.vmware.com/en/VMware-vSphere/7.0/com.vmware.vsphere.resmgmt.doc/GUID-60077B40-66FF-4625-934A-641703ED7601.html)  
[VM folder](https://docs.vmware.com/en/VMware-vSphere/7.0/com.vmware.vsphere.vcenterhost.doc/GUID-031BDB12-D3B2-4E2D-80E6-604F304B4D0C.html)  
[network](https://docs.vmware.com/en/VMware-vSphere/7.0/com.vmware.vsphere.networking.doc/GUID-2B11DBB8-CB3C-4AFF-8885-EFEA0FC562F4.html) | Yes  
  
## Privileges in the Anthos custom role

#### View the privileges in the Anthos custom role.

Category | Privileges  
---|---  
[Cloud Native Store](https://docs.vmware.com/en/VMware-vSphere/7.0/com.vmware.vsphere.security.doc/GUID-C04F1605-D158-4B65-810F-6F5B109BCDEC.html) | 

  * Searchable

  
[Datastore](https://docs.vmware.com/en/VMware-vSphere/7.0/com.vmware.vsphere.security.doc/GUID-B2426ACC-D73F-4732-8BBC-DE9B1B2263D9.html) | 

  * Allocate space
  * Browse datastore
  * Configure datastore
  * Low level file operations
  * Remove file
  * Update virtual machine files
  * Update virtual machine metadata

  
[Cryptographic operations](https://docs.vmware.com/en/VMware-vSphere/7.0/com.vmware.vsphere.security.doc/GUID-660CCB35-847F-46B3-81CA-10DDDB9D7AA9.html) | 

  * Direct Access

  
[Folder](https://docs.vmware.com/en/VMware-vSphere/7.0/com.vmware.vsphere.security.doc/GUID-383BBC13-7B79-49E0-8D0A-E929046F0A41.html) | 

  * Create folder
  * Delete folder
  * Move folder
  * Rename folder

  
[Host Inventory](https://docs.vmware.com/en/VMware-vSphere/7.0/com.vmware.vsphere.security.doc/GUID-71C3E5D6-8E57-4C86-B133-DB7F5ADAC1A4.html) | 

  * Modify cluster

  
[vSphere Tagging](https://docs.vmware.com/en/VMware-vSphere/7.0/com.vmware.vsphere.security.doc/GUID-2F8C5B02-7EF6-428A-BDB6-B2CC3D307097.html) | 

  * Create vSphere Tag
  * Delete vSphere Tag
  * Assign or Unassign vSphere Tag
  * Assign or Unassign vSphere Tag on Object (vSphere 7)

  
[Sessions](https://docs.vmware.com/en/VMware-vSphere/7.0/com.vmware.vsphere.security.doc/GUID-84BDB0C4-AAB8-41AA-BB52-66C5E2A5B5A1.html) | 

  * Validate session

  
[Network](https://docs.vmware.com/en/VMware-vSphere/7.0/com.vmware.vsphere.security.doc/GUID-836D61D6-13F6-4C98-BC1B-34C62A0F4E2D.html) | 

  * Assign network

  
[Resource](https://docs.vmware.com/en/VMware-vSphere/7.0/com.vmware.vsphere.security.doc/GUID-7BA4AE08-233C-4FF3-9A78-5B4BD4A6E28D.html) | 

  * Apply recommendation
  * Assign virtual machine to resource pool
  * Migrate powered off virtual machine
  * Migrate powered on virtual machine
  * Query vMotion

  
[Storage Views](https://docs.vmware.com/en/VMware-vSphere/7.0/com.vmware.vsphere.security.doc/GUID-DB976EAC-6F7E-4954-ABF4-2EAD5B6A68C0.html) | 

  * View

  
[System](https://docs.vmware.com/en/VMware-vSphere/7.0/com.vmware.vsphere.security.doc/GUID-18071E9A-EED1-4968-8D51-E0B4F526FDA3.html) | 

  * Anonymous
  * Read
  * View

  
[Tasks](https://docs.vmware.com/en/VMware-vSphere/7.0/com.vmware.vsphere.security.doc/GUID-29B4F59D-DF27-4F98-9BAB-0651EA94E74B.html) | 

  * Create task
  * Update task

  
[vApp](https://docs.vmware.com/en/VMware-vSphere/7.0/com.vmware.vsphere.security.doc/GUID-20C1A2F2-F7ED-4E03-A62C-E2E6F3743E39.html) | 

  * Import
  * vApp application configuration
  * vApp instance configuration

  
Virtual Machine | 

  * [Configuration](https://docs.vmware.com/en/VMware-vSphere/7.0/com.vmware.vsphere.security.doc/GUID-FEAB5DF5-F7A2-412D-BF3D-7420A355AE8F.html)
    * Add existing disk
    * Add new disk
    * Add or remove device
    * Advanced configuration
    * Change CPU count
    * Change resource
    * Configure managedBy
    * Toggle disk change tracking
    * Acquire disk lease 
    * Display connection settings
    * Extend virtual disk
    * Configure Host USB device.
    * Change Memory.
    * Modify device settings
    * Query Fault Tolerance compatibility
    * Query unowned files
    * Configure Raw Device.
    * Reload from path
    * Remove disk
    * Rename
    * Reset guest information
    * Set annotation
    * Change Settings.
    * Change Swapfile placement.
    * Toggle fork parent
    * Upgrade virtual machine compatibility
  * [Guest Operations](https://docs.vmware.com/en/VMware-vSphere/7.0/com.vmware.vsphere.security.doc/GUID-6A952214-0E5E-4CCF-9D2A-90948FF643EC.html)
    * Guest Operation Alias modification
    * Guest Operation Alias query
    * Guest Operation Modifications
    * Guest Operation Program Execution
    * Guest Operation Queries
  * [Interaction](https://docs.vmware.com/en/VMware-vSphere/7.0/com.vmware.vsphere.security.doc/GUID-3D47149A-947D-4608-88B3-E5811129EFA8.html)
    * Answer question
    * Backup operation on virtual machine
    * Configure CD media
    * Configure floppy media
    * Console interaction
    * Create screenshot
    * Defragment all disks
    * Device connection
    * Drag and Drop
    * Guest operating system management by VIX API
    * Inject USB HID scan codes
    * Pause or Unpause
    * Perform wipe or shrink operations
    * Power Off
    * Power On
    * Record session on Virtual Machine
    * Replay session on Virtual Machine
    * Reset
    * Resume Fault Tolerance
    * Suspend
    * Suspend Fault Tolerance
    * Test failover
    * Test restart Secondary VM
    * Turn Off Fault Tolerance
    * Turn On Fault Tolerance
    * VMware Tools install
  * [Inventory](https://docs.vmware.com/en/VMware-vSphere/7.0/com.vmware.vsphere.security.doc/GUID-C81A92E3-4A73-4CE7-88D5-031079A53693.html)
    * Create from existing
    * Create new
    * Move
    * Register
    * Remove
    * Unregister
  * [Provisioning](https://docs.vmware.com/en/VMware-vSphere/7.0/com.vmware.vsphere.security.doc/GUID-31C6CD2D-41CA-4646-994A-C61AD5FF1880.html)
    * Allow disk access
    * Allow file access
    * Allow read-only disk access
    * Allow virtual machine download
    * Allow virtual machine files upload
    * Clone template
    * Clone virtual machine
    * Create template from virtual machine
    * Customize guest.
    * Deploy template
    * Mark as template
    * Mark as virtual machine
    * Modify customization specification
    * Promote disks
    * Read customization specifications
  * [Service configuration](https://docs.vmware.com/en/VMware-vSphere/7.0/com.vmware.vsphere.security.doc/GUID-6876B8A5-6DB5-4FC0-9B25-215632A1F041.html)
    * Allow notifications
    * Allow polling of global event notifications
    * Manage service configurations
    * Modify service configuration
    * Query service configurations
    * Read service configuration
  * [Snapshot management](https://docs.vmware.com/en/VMware-vSphere/7.0/com.vmware.vsphere.security.doc/GUID-222FE721-0968-4E9E-9F98-7CB03E7185E8.html)
    * Create snapshot
    * Remove snapshot
    * Rename snapshot
    * Revert to snapshot
  * [vSphere replication](https://docs.vmware.com/en/VMware-vSphere/7.0/com.vmware.vsphere.security.doc/GUID-384E8D8A-8BE6-4765-8BEE-020DD4CA0F2F.html)
    * Configure Replication
    * Manage Replication
    * Monitor Replication

  
  
## Create custom roles and permissions

An organization administrator can use the [govc](https://github.com/vmware/govmomi/tree/master/govc) command-line tool to create custom roles and permissions.

The organization administrator must have a vCenter Server account that has sufficient [privileges](https://docs.vmware.com/en/VMware-vSphere/7.0/com.vmware.vsphere.security.doc/GUID-F747882C-55C8-42E7-9066-EBFC3E26C9C8.html) for creating roles and permissions. For example, an account that has the Administrator role would be appropriate.

Before you run `govc`, set some environment variables:

  * Set GOVC_URL to the URL of your instance of vCenter Server.

  * Set GOVC_USERNAME to the username of the organization administrator's vCenter Server account.

  * Set GOVC_PASSWORD to the password of the organization administrator's vCenter Server account.




For example:
    
    
    export GOVC_URL=vc-01.example
    export GOVC_USERNAME=alice@vsphere.local
    export GOVC_PASSWORD=8ODQYHo2Yl@
    

### Create custom roles

Create the ClusterEditor, SessionValidator, and ReadOnly custom roles:
    
    
    govc role.create ClusterEditor System.Read System.View System.Anonymous Host.Inventory.EditCluster
    govc role.create SessionValidator System.Read System.View System.Anonymous Sessions.ValidateSession Cns.Searchable StorageProfile.View
    govc role.create ReadOnly System.Read System.View System.Anonymous
    

#### View the command to create the Anthos custom role.
    
    
    govc role.create anthos
    Cns.Searchable
    Cryptographer.Access
    Datastore.AllocateSpace
    Datastore.Browse
    Datastore.Config
    Datastore.FileManagement
    Datastore.DeleteFile
    Datastore.UpdateVirtualMachineFiles
    Datastore.UpdateVirtualMachineMetadata
    Folder.Create
    Folder.Delete
    Folder.Move
    Folder.Rename
    Host.Inventory.EditCluster
    InventoryService.Tagging.CreateTag
    InventoryService.Tagging.DeleteTag
    InventoryService.Tagging.AttachTag
    InventoryService.Tagging.ObjectAttachable
    Sessions.ValidateSession
    Network.Assign
    Resource.ApplyRecommendation
    Resource.AssignVMToPool
    Resource.ColdMigrate
    Resource.HotMigrate
    Resource.QueryVMotion
    StorageViews.View
    System.Anonymous
    System.Read
    System.View
    Task.Create
    Task.Update
    VApp.Import
    VApp.ApplicationConfig
    VApp.InstanceConfig
    VirtualMachine.Config.AddExistingDisk
    VirtualMachine.Config.AddNewDisk
    VirtualMachine.Config.AddRemoveDevice
    VirtualMachine.Config.AdvancedConfig
    VirtualMachine.Config.Annotation
    VirtualMachine.Config.CPUCount
    VirtualMachine.Config.Resource
    VirtualMachine.Config.ManagedBy
    VirtualMachine.Config.ChangeTracking
    VirtualMachine.Config.DiskLease
    VirtualMachine.Config.MksControl
    VirtualMachine.Config.DiskExtend
    VirtualMachine.Config.HostUSBDevice
    VirtualMachine.Config.Memory
    VirtualMachine.Config.EditDevice
    VirtualMachine.Config.QueryFTCompatibility
    VirtualMachine.Config.QueryUnownedFiles
    VirtualMachine.Config.RawDevice
    VirtualMachine.Config.ReloadFromPath
    VirtualMachine.Config.RemoveDisk
    VirtualMachine.Config.Rename
    VirtualMachine.Config.ResetGuestInfo
    VirtualMachine.Config.Settings
    VirtualMachine.Config.SwapPlacement
    VirtualMachine.Config.ToggleForkParent
    VirtualMachine.Config.UpgradeVirtualHardware
    VirtualMachine.GuestOperations.ModifyAliases
    VirtualMachine.GuestOperations.QueryAliases
    VirtualMachine.GuestOperations.Modify
    VirtualMachine.GuestOperations.Execute
    VirtualMachine.GuestOperations.Query
    VirtualMachine.Interact.AnswerQuestion
    VirtualMachine.Interact.Backup
    VirtualMachine.Interact.SetCDMedia
    VirtualMachine.Interact.SetFloppyMedia
    VirtualMachine.Interact.ConsoleInteract
    VirtualMachine.Interact.CreateScreenshot
    VirtualMachine.Interact.DefragmentAllDisks
    VirtualMachine.Interact.DeviceConnection
    VirtualMachine.Interact.DnD
    VirtualMachine.Interact.GuestControl
    VirtualMachine.Interact.PutUsbScanCodes
    VirtualMachine.Interact.Pause
    VirtualMachine.Interact.SESparseMaintenance
    VirtualMachine.Interact.PowerOff
    VirtualMachine.Interact.PowerOn
    VirtualMachine.Interact.Record
    VirtualMachine.Interact.Replay
    VirtualMachine.Interact.Reset
    VirtualMachine.Interact.EnableSecondary
    VirtualMachine.Interact.Suspend
    VirtualMachine.Interact.DisableSecondary
    VirtualMachine.Interact.MakePrimary
    VirtualMachine.Interact.TerminateFaultTolerantVM
    VirtualMachine.Interact.TurnOffFaultTolerance
    VirtualMachine.Interact.CreateSecondary
    VirtualMachine.Interact.ToolsInstall
    VirtualMachine.Inventory.CreateFromExisting
    VirtualMachine.Inventory.Create
    VirtualMachine.Inventory.Move
    VirtualMachine.Inventory.Register
    VirtualMachine.Inventory.Delete
    VirtualMachine.Inventory.Unregister
    VirtualMachine.Provisioning.DiskRandomAccess
    VirtualMachine.Provisioning.FileRandomAccess
    VirtualMachine.Provisioning.DiskRandomRead
    VirtualMachine.Provisioning.GetVmFiles
    VirtualMachine.Provisioning.PutVmFiles
    VirtualMachine.Provisioning.CloneTemplate
    VirtualMachine.Provisioning.Clone
    VirtualMachine.Provisioning.CreateTemplateFromVM
    VirtualMachine.Provisioning.Customize
    VirtualMachine.Provisioning.DeployTemplate
    VirtualMachine.Provisioning.MarkAsTemplate
    VirtualMachine.Provisioning.MarkAsVM
    VirtualMachine.Provisioning.ModifyCustSpecs
    VirtualMachine.Provisioning.PromoteDisks
    VirtualMachine.Provisioning.ReadCustSpecs
    VirtualMachine.Namespace.Event
    VirtualMachine.Namespace.EventNotify
    VirtualMachine.Namespace.Management
    VirtualMachine.Namespace.ModifyContent
    VirtualMachine.Namespace.Query
    VirtualMachine.Namespace.ReadContent
    VirtualMachine.State.CreateSnapshot
    VirtualMachine.State.RemoveSnapshot
    VirtualMachine.State.RenameSnapshot
    VirtualMachine.State.RevertToSnapshot
    VirtualMachine.Hbr.ConfigureReplication
    VirtualMachine.Hbr.ReplicaManagement
    VirtualMachine.Hbr.MonitorReplication
    

### Create a permission that grants the ClusterEditor role

A permissions takes a (user, role) pair and associates it with an object. When you assign a permission on an object, you can specify whether the permission propagates to child objects. With `govc`, you do this by setting the `--propagate` flag to either `true` or `false`. The default is `false`.

Create a permission that grants the ClusterEditor role to a user on a cluster object. This permission propagates to all child objects of the cluster object:
    
    
    govc permissions.set -principal ACCOUNT \
     -role ClusterEditor -propagate=true CLUSTER_PATH`
    

Replace the following:

  * ACCOUNT: the vCenter Server user account that is being granted the role

  * CLUSTER_PATH: the path of the cluster in the vSphere object hierarchy




For example, the following command creates a permission that associates the pair (bob@vsphere.local, ClusterEditor with my-dc/host/my-cluster. The permission propagates to all child objects of my-dc/host/my-cluster:
    
    
    govc permissions.set -principal bob@vsphere.local \
        -role ClusterEditor -propagate=true my-dc/host/my-cluster
    

### Create additional permissions

This section gives examples of creating additional permissions. Replace the example object paths as needed for your environment.

Create a permission that grants the SessionValidator role to an account on the root vCenter Server object. This permission does not propagate to child objects:
    
    
    govc permissions.set -principal ACCOUNT \
        -role SessionValidator -propagate=false
    

Create permissions that grant the ReadOnly role to an account on a data center object and a network object. These permissions propagate to child objects:
    
    
    govc permissions.set -principal ACCOUNT \
        -role ReadOnly -propagate=true \
        /my-dc \
        /my-dc/network/my-net
    

Create permissions that grant the Anthos role to an account on four objects: a datastore, a VM folder, a resource pool, and a network. These permissions propagate to child objects:
    
    
    govc permissions.set -principal ACCOUNT -role Anthos -propagate=true \
        /my-dc/datastore/my-ds  \
        /my-dc/vm/my-folder \
        /my-dc/host/my-cluster/Resources/my-rp \
        /my-dc/network/my-net
    

## Create one global permission

This section gives an alternative to creating several roles and several permissions. We do not recommend this approach because it grants a large set of privileges on all objects in your vSphere hierarchies.

If you have not already created the Anthos custom role, create it now.

Create one global permission:
    
    
    govc permissions.set -principal ACCOUNT \
     -role Anthos -propagate=true
    

Replace the following:

Replace ACCOUNT with the vCenter Server user account that is being granted the role

For example, the following command creates a global permission that grants the Anthos role to bob@vsphere.local. The permission propagates to all objects in your vSphere hierarchies:
    
    
    govc permissions.set -principal bob@vsphere.local -role Anthos -propagate=true
    

## Known issues

See [Installer fails when creating vSphere datadisk](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.15/known-issues#installer-failes-creating-vsphere-datadisk).

## What's next

[CPU, RAM, and storage requirements](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.15/how-to/cpu-ram-storage)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
