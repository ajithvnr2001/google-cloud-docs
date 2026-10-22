---
url: https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/vsphere-requirements/
title: vSphere requirements \u00a0|\u00a0 Google Distributed Cloud software only for VMware \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:57:18.877001+00:00
---

# vSphere requirements  |  Google Distributed Cloud software only for VMware  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/vsphere-requirements/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Google Distributed Cloud ](https://docs.cloud.google.com/distributed-cloud)
  * [ Documentation ](https://docs.cloud.google.com/kubernetes-engine/enterprise/clusters/docs)
  * [ GDC for VMware ](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs)
  * [ Guides ](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/overview)



Send feedback 

#  vSphere requirements Stay organized with collections  Save and categorize content based on your preferences. 

Google Distributed Cloud runs on your premises in a [vSphere](https://www.vmware.com/products/vsphere.html) environment. This document describes requirements for your vSphere environment.

This page is for Admins and architects who define IT solutions and system architecture in accordance with company strategy, and create and manage policies related to user permissions. To learn more about common roles and example tasks that we reference in Google Cloud content, see [Common GKE user roles and tasks](https://docs.cloud.google.com/kubernetes-engine/enterprise/docs/concepts/roles-tasks).

## Version compatibility

The vSphere requirements vary according to which version of Google Distributed Cloud you are using. For more information, see the version compatibility matrix for [fully supported versions](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/version-history).

## Supported versions

[vSphere](https://www.vmware.com/products/vsphere.html) is VMware's server virtualization software. vSphere includes [ESXi](https://www.vmware.com/products/esxi-and-esx.html) and [vCenter Server](https://www.vmware.com/products/vcenter-server.html).

Google Distributed Cloud supports these versions of [ESXi](https://kb.vmware.com/s/article/2143832) and [vCenter Server](https://kb.vmware.com/s/article/2143838)

  * 9.0 and 9.1
  * 8.0 and later updates of version 8.0



We recommend that you use 9.1.

If you want to create CSI volume snapshots, then you must have one of the following versions:

  * 9.0 and 9.1
  * 8.0 or a later update of version 8.0



## License requirements

You need one of the following licenses:

  * [vSphere Enterprise Plus](https://www.vmware.com/products/vsphere.html#compare-editions) license. Along with this license, you must have a valid support subscription.

  * [vSphere Standard](https://www.vmware.com/products/vsphere.html#compare-editions) license. Along with this license, you must have a valid support subscription. With this license, you cannot enable [anti-affinity groups](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/admin-cluster-configuration-file-latest#antiaffinitygroups-enabled-field). Also, you cannot specify your own [resource pool](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/admin-cluster-configuration-file-latest#vcenter-resourcepool-field). You must use the default resource pool.




## Hardware requirements

Google Distributed Cloud runs on a set of physical hosts that run the VMware [ESXi hypervisor](https://www.vmware.com/products/esxi-and-esx.html). To learn about the hardware requirements for ESXi, see [ESXi Hardware Requirements](https://techdocs.broadcom.com/us/en/vmware-cis/vsphere/vsphere/9-1/esx-installation-and-setup.html).

For production environments, we strongly recommend the following:

  * Enable [VMware Distributed Resource Scheduler (DRS)](https://www.vmware.com/products/vsphere/drs-dpm.html).

  * Have at least four ESXi hosts available for your cluster VMs.

  * Enable [Network File Copy (NFC)](http://techdocs.broadcom.com/us/en/vmware-cis/vsphere/vsphere-sdks-tools/9-1/virtual-disk-development-kit-programming-guide/virtual-disk-interfaces/virtual-disk-transport-methods/nbdssl-transport/nfc-session-limits-and-timeouts.html) traffic among ESXi hosts to allow OS template sharing, if you plan to deploy Anthos clusters on VMware on different vSphere clusters or resource pools within the same vSphere datacenter.

  * Set [`antiAffinityGroups.enabled`](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/admin-cluster-configuration-file-latest#antiaffinitygroups-enabled-field) to `true` in your cluster configuration files.




If you set `antiAffinityGroups.enabled` to `true`, Google Distributed Cloud creates DRS anti-affinity rules for your cluster nodes, causing them to be spread across at least three physical ESXi hosts. Even though the DRS rules require that cluster nodes are spread across three ESXi hosts, we strongly recommend that you have at least four ESXi hosts available. This protects you from losing your cluster control plane. For example, suppose you have only three ESXi hosts, and your admin cluster control-plane node is on an ESXi host that fails. The DRS rule will prevent the control-plane node from being placed on one of the remaining two ESXi hosts.

For evaluation and proof of concept, you can set `antiAffinityGroups.enabled` to `false`, and use only one ESXi host. For more information, see [Set up minimal infrastructure](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/minimal-infrastructure).

## vCenter user account privileges

To set up a vSphere environment, an organization administrator might choose to use a vCenter user account that has the [vCenter Server Administrator role](https://techdocs.broadcom.com/us/en/vmware-cis/vsphere/vsphere/9-1/vsphere-security.html). This role provides full access to all vSphere objects.

After the vSphere environment is set up, a cluster administrator can create admin clusters and user clusters. The cluster administrator does not need all the privileges provided by the vCenter Server Administrator role.

When a cluster administrator or developer creates a cluster, they provide a vCenter user account in a [credentials configuration file](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/credentials-configuration-file). We recommend that the vCenter user account that is listed in a credentials configuration file be assigned one or more [custom roles](https://techdocs.broadcom.com/us/en/vmware-cis/vsphere/vsphere/9-1/vsphere-security.html) that have the minimum [privileges](https://techdocs.broadcom.com/us/en/vmware-cis/vsphere/vsphere/9-1/vsphere-security.html) required for cluster creation and management.

There are two different approaches an organization administrator can take:

  * Create several roles with varying degrees of privilege. Then create permissions that assign those limited roles to a user or group on individual vSphere objects. We recommend this approach, because it limits access and increases the security of your vCenter Server environment. For more information, see [vSphere Security](https://techdocs.broadcom.com/us/en/vmware-cis/vsphere/vsphere/9-1/vsphere-security.html).

  * Create one role that has all the needed privileges. Then create a [global permission](https://techdocs.broadcom.com/us/en/vmware-cis/vsphere/vsphere/9-1/vsphere-security.html) that assigns that role to a particular user or group on all objects in your vSphere hierarchies. For information on using this approach, see Create one global permission.




The following table shows four custom roles that an organization administrator can create. The administrator can then use the custom roles to assign permissions on specific vSphere objects:

Custom role| Privileges| Objects| Propagate to  
child objects?  
---|---|---|---  
ClusterEditor |  [System](https://techdocs.broadcom.com/us/en/vmware-cis/vsphere/vsphere/9-1/vsphere-security.html).Read  
System.View  
System.Anonymous  
[Host.Inventory](https://techdocs.broadcom.com/us/en/vmware-cis/vsphere/vsphere/9-1/vsphere-security.html).Modify cluster  |  [cluster](https://techdocs.broadcom.com/us/en/vmware-cis/vsphere/vsphere/9-1/vcenter-and-host-management.html) | Yes  
SessionValidator |  System.Read  
System.View  
System.Anonymous  
[Sessions](https://techdocs.broadcom.com/us/en/vmware-cis/vsphere/vsphere/9-1/vsphere-security.html).Validate session  
[Cns](https://techdocs.broadcom.com/us/en/vmware-cis/vsphere/vsphere/9-1/vsphere-security.html).Searchable  
[Profile-driven storage](https://techdocs.broadcom.com/us/en/vmware-cis/vsphere/vsphere/9-1/vsphere-security.html).Profile-driven storage view  | Root vCenter Server | No  
ReadOnly |  System.Read  
System.View  
System.Anonymous  |  [data center](https://techdocs.broadcom.com/us/en/vmware-cis/vsphere/vsphere/9-1/vcenter-and-host-management.html)  
[network](https://techdocs.broadcom.com/us/en/vmware-cis/vsphere/vsphere/9-1/vsphere-networking.html) | Yes  
Anthos | Privileges in the Anthos role |  [datastore](https://techdocs.broadcom.com/us/en/vmware-cis/vsphere/vsphere/9-1/vsphere-storage.html)  
[resource pool](https://techdocs.broadcom.com/us/en/vmware-cis/vsphere/vsphere/9-1/vsphere-resource-management.html)  
[VM folder](https://techdocs.broadcom.com/us/en/vmware-cis/vsphere/vsphere/9-1/vcenter-and-host-management.html)  
[network](https://techdocs.broadcom.com/us/en/vmware-cis/vsphere/vsphere/9-1/vsphere-networking.html) | Yes  
  
## Privileges in the Anthos custom role

#### View the privileges in the Anthos custom role.

Category | Privileges  
---|---  
[Cloud Native Store](https://techdocs.broadcom.com/us/en/vmware-cis/vsphere/vsphere/9-1/vsphere-security.html) | 

  * Searchable

  
[Datastore](https://techdocs.broadcom.com/us/en/vmware-cis/vsphere/vsphere/9-1/vsphere-security.html) | 

  * Allocate space
  * Browse datastore
  * Configure datastore
  * Low level file operations
  * Remove file
  * Update virtual machine files
  * Update virtual machine metadata

  
Cryptographic operations | 

  * Direct Access

  
[Folder](https://techdocs.broadcom.com/us/en/vmware-cis/vsphere/vsphere/9-1/vsphere-security.html) | 

  * Create folder
  * Delete folder
  * Move folder
  * Rename folder

  
[Host Inventory](https://techdocs.broadcom.com/us/en/vmware-cis/vsphere/vsphere/9-1/vsphere-security.html) | 

  * Modify cluster

  
[vSphere Tagging](https://techdocs.broadcom.com/us/en/vmware-cis/vsphere/vsphere/9-1/vsphere-security.html) | 

  * Create vSphere Tag
  * Delete vSphere Tag
  * Assign or Unassign vSphere Tag
  * Assign or Unassign vSphere Tag on Object

  
[Sessions](https://techdocs.broadcom.com/us/en/vmware-cis/vsphere/vsphere/9-1/vsphere-security.html) | 

  * Validate session

  
[Network](https://techdocs.broadcom.com/us/en/vmware-cis/vsphere/vsphere/9-1/vsphere-security.html) | 

  * Assign network

  
[Resource](https://techdocs.broadcom.com/us/en/vmware-cis/vsphere/vsphere/9-1/vsphere-security.html) | 

  * Apply recommendation
  * Assign virtual machine to resource pool
  * Migrate powered off virtual machine
  * Migrate powered on virtual machine
  * Query vMotion

  
[Storage Views](https://techdocs.broadcom.com/us/en/vmware-cis/vsphere/vsphere/9-1/vsphere-security.html) | 

  * View

  
[System](https://techdocs.broadcom.com/us/en/vmware-cis/vsphere/vsphere/9-1/vsphere-security.html) | 

  * Anonymous
  * Read
  * View

  
[Tasks](https://techdocs.broadcom.com/us/en/vmware-cis/vsphere/vsphere/9-1/vsphere-security.html) | 

  * Create task
  * Update task

  
[vApp](https://techdocs.broadcom.com/us/en/vmware-cis/vsphere/vsphere/9-1/vsphere-security.html) | 

  * Import
  * vApp application configuration
  * vApp instance configuration

  
Virtual Machine | 

  * [Configuration](https://techdocs.broadcom.com/us/en/vmware-cis/vsphere/vsphere/9-1/vsphere-security.html)
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
  * [Guest Operations](https://techdocs.broadcom.com/us/en/vmware-cis/vsphere/vsphere/9-1/vsphere-security.html)
    * Guest Operation Alias modification
    * Guest Operation Alias query
    * Guest Operation Modifications
    * Guest Operation Program Execution
    * Guest Operation Queries
  * [Interaction](https://techdocs.broadcom.com/us/en/vmware-cis/vsphere/vsphere/9-1/vsphere-security.html)
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
  * [Inventory](https://techdocs.broadcom.com/us/en/vmware-cis/vsphere/vsphere/9-1/vsphere-security.html)
    * Create from existing
    * Create new
    * Move
    * Register
    * Remove
    * Unregister
  * [Provisioning](https://techdocs.broadcom.com/us/en/vmware-cis/vsphere/vsphere/9-1/vsphere-security.html)
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
  * [Service configuration](https://techdocs.broadcom.com/us/en/vmware-cis/vsphere/vsphere/9-1/vsphere-security.html)
    * Allow notifications
    * Allow polling of global event notifications
    * Manage service configurations
    * Modify service configuration
    * Query service configurations
    * Read service configuration
  * [Snapshot management](https://techdocs.broadcom.com/us/en/vmware-cis/vsphere/vsphere/9-1/vsphere-security.html)
    * Create snapshot
    * Remove snapshot
    * Rename snapshot
    * Revert to snapshot
  * [vSphere replication](https://techdocs.broadcom.com/us/en/vmware-cis/vsphere/vsphere/9-1/vsphere-security.html)
    * Configure Replication
    * Manage Replication
    * Monitor Replication

  
  
## Create custom roles and permissions

An organization administrator can use the [govc](https://github.com/vmware/govmomi/tree/master/govc) command-line tool to create custom roles and permissions.

The organization administrator must have a vCenter Server account that has sufficient privileges for creating roles and permissions. For example, an account that has the Administrator role would be appropriate.

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

See [Installer fails when creating vSphere datadisk](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/troubleshooting/known-issues#installer-fails-when-creating-vsphere-datadisk).

## What's next

[CPU, RAM, and storage requirements](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/cpu-ram-storage)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-14 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-14 UTC."],[],[]] 
