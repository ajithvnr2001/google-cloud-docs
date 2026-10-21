---
url: https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.6/how-to/vsphere-requirements-basic/
title: vSphere requirements \u00a0|\u00a0 Anthos clusters on VMware \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-16T13:57:26.001746+00:00
---

# vSphere requirements  |  Anthos clusters on VMware  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.6/how-to/vsphere-requirements-basic/

**Version 1.6**. This version is no longer supported. For more information see the [ version support policy](https://cloud.google.com/anthos/clusters/docs/on-prem/latest/getting-support#version_support_policy). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Google Kubernetes Engine (GKE) ](https://docs.cloud.google.com/kubernetes-engine)
  * [ GKE Enterprise ](https://docs.cloud.google.com/kubernetes-engine/enterprise/docs)
  * [ Clusters ](https://docs.cloud.google.com/anthos/clusters)
  * [ Documentation ](https://docs.cloud.google.com/anthos/clusters/docs)
  * [ Anthos clusters on VMware 1.6 ](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.6)
  * [ Guides ](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.6/overview)



Send feedback 

#  vSphere requirements Stay organized with collections  Save and categorize content based on your preferences. 

Google Distributed Cloud runs in your data center in a [vSphere 6.5 or 6.7 Update 3](https://www.vmware.com/products/vsphere.html) environment. This topic describes requirements for your vSphere environment, including storage, CPU, RAM, and virtual networks.

## vSphere requirements

The vSphere requirements vary according to which version of Google Distributed Cloud you are using. For more information, see the version compatibility matrix for [fully supported versions](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.6/version-history#version-compatibility) and [earlier versions](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.6/version-history#expandable-4).

vSphere is VMware's [server virtualization](https://www.vmware.com/topics/glossary/content/server-virtualization) software. Google Distributed Cloud uses VMware's [vCenter Server](https://www.vmware.com/products/vcenter-server.html) to manage your clusters. To learn about installing vSphere and vCenter Server, see [Overview of the vSphere Installation and Setup Process](https://docs.vmware.com/en/VMware-vSphere/6.5/com.vmware.vsphere.install.doc/GUID-B64AA6D3-40A1-4E3E-B03C-94AD2E95C9F5.html) in the VMware documentation.

### License edition and version requirements

Google Distributed Cloud requires VMware vSphere 6.5 or 6.7 Update 3. You need the following VMware licenses:

  * A vSphere Enterprise Plus or vSphere Standard license.

The Enterprise Plus license is recommended, because it allows you to enable the VMware [Distributed Resource Scheduler (DRS)](https://www.vmware.com/products/vsphere/drs-dpm.html).

Along with this license, you must purchase a support subscription for at least one year.

  * A vCenter Server Standard license.

Along with this license, you must purchase a support subscription for at least one year.




### Hardware requirements

Google Distributed Cloud runs on a set of physical hosts that run the VMware [ESXi hypervisor](https://www.vmware.com/products/esxi-and-esx.html). To learn about the hardware requirements for ESXi, see [ESXi Hardware Requirements](https://docs.vmware.com/en/VMware-vSphere/6.5/com.vmware.vsphere.upgrade.doc/GUID-DEB8086A-306B-4239-BF76-E354679202FC.html).

By default, Google Distributed Cloud automatically creates VMware [Distributed Resource Scheduler](https://www.vmware.com/products/vsphere/drs-dpm.html) (DRS) anti-affinity rules for your admin cluster and user cluster's nodes, causing them to be spread across at least three physical hosts in your datacenter.

This feature requires that your vSphere environment meets the following conditions:

  * VMware DRS is enabled. VMware DRS requires vSphere Enterprise Plus license edition.

  * Your vSphere user account has the [`Host.Inventory.Modify cluster`](https://docs.vmware.com/en/VMware-vSphere/6.7/com.vmware.vsphere.security.doc/GUID-71C3E5D6-8E57-4C86-B133-DB7F5ADAC1A4.html) privilege.

  * There are at least three physical hosts available.




Recall that if you have a [vSphere Standard license](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.6/how-to/vsphere-requirements-basic#license-edition-and-version-requirements), you cannot enable VMware DRS.

If you do not have DRS enabled, or if you do not have at least three hosts where vSphere VMs can be scheduled, set `antiAffinityGroups.enabled` to `false` in admin cluster and user cluster configurations.

### vSphere storage requirements

Google Distributed Cloud does not support Storage vMotion and Storage DRS.

### vCenter user account privileges

You can define custom roles in vCenter or use a [vCenter system roles](https://docs.vmware.com/en/VMware-vSphere/6.5/com.vmware.vsphere.security.doc/GUID-93B962A7-93FA-4E96-B68F-AE66D3D6C663.html) for the various various users in your organization, including your Anthos cluster administrator and the users who develop on those clusters.

The vCenter user account that you use to install Google Distributed Cloud must have sufficient privileges. For example, a user account that is assigned the vCenter's _Administrator_ role has privileges for complete access to all vCenter objects and provides an Anthos cluster administrator with full access.

For other vCenter user accounts, you [create custom roles](https://docs.vmware.com/en/VMware-vSphere/6.5/com.vmware.vsphere.security.doc/GUID-41E5E52E-A95B-4E81-9724-6AD6800BEF78.html) to assign the necessary privileges to your cluster's users.

  * Use the following table to understand what the minimum required set of privileges are for your Anthos cluster users. 

#### View the minimum set of required vCenter privileges.

Entity | Privilege  
---|---  
Cloud Native Storage | 
    * Searchable  
Datastore | 
    * Allocate space
    * Browse datastore
    * Low level file operations
    * Remove file
    * Update virtual machine files
    * Update virtual machine metadata  
Folder | 
    * Create folder
    * Delete folder
    * Move folder
    * Rename folder  
Host Inventory | 
    * Modify cluster  
vSphere Tagging | 
    * Assign or Unassign vSphere Tag  
Root vCenter Server | 
    * Validate session  
Network | 
    * Assign network  
Resource | 
    * Apply recommendation
    * Assign virtual machine to resource pool
    * Migrate powered off virtual machine
    * Migrate powered on virtual machine
    * Query vMotion  
Storage views | 
    * View  
System | 
    * Anonymous
    * Read
    * View  
Tasks | 
    * Create task
    * Update task  
vApp | 
    * Import
    * vApp application configuration
    * vApp instance configuration  
Virtual machines | 
    * Configuration
      * Add existing disk
      * Add new disk
      * Add or remove device
      * Advanced
      * Change CPU count
      * Change resource
      * Configure managedBy
      * Disk change tracking
      * Disk lease
      * Display connection settings
      * Extend virtual disk
      * Host USB device
      * Memory
      * Modify device settings
      * Query Fault Tolerance compatibility
      * Query unowned files
      * Raw device
      * Reload from path
      * Remove disk
      * Rename
      * Reset guest information
      * Set annotation
      * Settings
      * Swapfile placement
      * Toggle fork parent
      * Upgrade virtual machine compatibility
    * Guest operations
      * Guest operation alias modification
      * Guest operation alias query
      * Guest operation modifications
      * Guest operation program execution
      * Guest operation queries
    * Interaction
      * Answer question
      * Backup operation on virtual machine
      * Configure CD media
      * Configure floppy media
      * Console interaction
      * Create screenshot
      * Defragment all disks
      * Device connection
      * Drag and drop
      * Guest operating system management by VIX API
      * Inject USB HID scan codes
      * Pause or Unpause
      * Perform wipe or shrink operations
      * Power off
      * Power on
      * Record session on virtual machine
      * Replay session on virtual machine
      * Reset
      * Resume Fault Tolerance
      * Suspend
      * Suspend Fault Tolerance
      * Test failover
      * Test restart Secondary VM
      * Turn off Fault Tolerance
      * Turn on Fault Tolerance
      * VMware Tools install
    * Inventory
      * Create from existing
      * Create new
      * Move
      * Register
      * Remove
      * Unregister
    * Provisioning
      * Allow disk access
      * Allow file access
      * Allow read-only disk access
      * Allow virtual machine download
      * Allow virtual machine files upload
      * Clone template
      * Clone virtual machine
      * Create template from virtual machine
      * Customize
      * Deploy template
      * Mark as template
      * Mark as virtual machine
      * Modify customization specification
      * Promote disks
      * Read customization specifications
    * Service configuration
      * Allow notifications
      * Allow polling of global event notifications
      * Manage service configurations
      * Modify service configuration
      * Query service configurations
      * Read service configuration
    * Snapshot management
      * Create snapshot
      * Remove snapshot
      * Rename snapshot
      * Revert to snapshot
    * vSphere Replication
      * Configure replication
      * Manage replication
      * Monitor replication  
  * A user account with administrator privileges can use the following commands to create a custom vCenter role, define the minimum required privileges to that role, and then assign that custom role to an existing vCenter user account. 

#### View the commands to create and assign user roles.
        
        export GOVC_USERNAME=ADMINISTRATOR_ACCOUNT@vsphere.local
        export GOVC_PASSWORD=ADMINISTRATOR_PASSWORD
        cat <<END |xargs govc role.create anthos
          Datastore.AllocateSpace Datastore.Browse Datastore.Config Datastore.DeleteFile
          Datastore.FileManagement Datastore.UpdateVirtualMachineFiles
          Datastore.UpdateVirtualMachineMetadata Folder.Create Folder.Delete Folder.Move
          Folder.Rename Host.Inventory.EditCluster InventoryService.Tagging.CreateTag
          Network.Assign Resource.ApplyRecommendation Resource.AssignVMToPool
          Resource.ColdMigrate Resource.HotMigrate Resource.QueryVMotion
          Sessions.ValidateSession StorageViews.View System.Anonymous System.Read
          System.View Task.Create Task.Update VApp.ApplicationConfig VApp.Import
          VApp.InstanceConfig VirtualMachine.Config.AddExistingDisk
          VirtualMachine.Config.AddNewDisk VirtualMachine.Config.AddRemoveDevice
          VirtualMachine.Config.AdvancedConfig VirtualMachine.Config.Annotation
          VirtualMachine.Config.CPUCount VirtualMachine.Config.ChangeTracking
          VirtualMachine.Config.DiskExtend VirtualMachine.Config.DiskLease
          VirtualMachine.Config.EditDevice VirtualMachine.Config.HostUSBDevice
          VirtualMachine.Config.ManagedBy VirtualMachine.Config.Memory
          VirtualMachine.Config.MksControl VirtualMachine.Config.QueryFTCompatibility
          VirtualMachine.Config.QueryUnownedFiles VirtualMachine.Config.RawDevice
          VirtualMachine.Config.ReloadFromPath VirtualMachine.Config.RemoveDisk
          VirtualMachine.Config.Rename VirtualMachine.Config.ResetGuestInfo
          VirtualMachine.Config.Resource VirtualMachine.Config.Settings
          VirtualMachine.Config.SwapPlacement VirtualMachine.Config.ToggleForkParent
          VirtualMachine.Config.UpgradeVirtualHardware
          VirtualMachine.GuestOperations.Execute VirtualMachine.GuestOperations.Modify
          VirtualMachine.GuestOperations.ModifyAliases
          VirtualMachine.GuestOperations.Query
          VirtualMachine.GuestOperations.QueryAliases
          VirtualMachine.Hbr.ConfigureReplication VirtualMachine.Hbr.MonitorReplication
          VirtualMachine.Hbr.ReplicaManagement VirtualMachine.Interact.AnswerQuestion
          VirtualMachine.Interact.Backup VirtualMachine.Interact.ConsoleInteract
          VirtualMachine.Interact.CreateScreenshot
          VirtualMachine.Interact.CreateSecondary
          VirtualMachine.Interact.DefragmentAllDisks
          VirtualMachine.Interact.DeviceConnection
          VirtualMachine.Interact.DisableSecondary VirtualMachine.Interact.DnD
          VirtualMachine.Interact.EnableSecondary VirtualMachine.Interact.GuestControl
          VirtualMachine.Interact.MakePrimary VirtualMachine.Interact.Pause
          VirtualMachine.Interact.PowerOff
          VirtualMachine.Interact.PowerOn VirtualMachine.Interact.PutUsbScanCodes
          VirtualMachine.Interact.Record VirtualMachine.Interact.Replay
          VirtualMachine.Interact.Reset
          VirtualMachine.Interact.SESparseMaintenance VirtualMachine.Interact.SetCDMedia
          VirtualMachine.Interact.SetFloppyMedia VirtualMachine.Interact.Suspend
          VirtualMachine.Interact.TerminateFaultTolerantVM
          VirtualMachine.Interact.ToolsInstall
          VirtualMachine.Interact.TurnOffFaultTolerance VirtualMachine.Inventory.Create
          VirtualMachine.Inventory.CreateFromExisting VirtualMachine.Inventory.Delete
          VirtualMachine.Inventory.Move VirtualMachine.Inventory.Register
          VirtualMachine.Inventory.Unregister VirtualMachine.Namespace.Event
          VirtualMachine.Namespace.EventNotify VirtualMachine.Namespace.Management
          VirtualMachine.Namespace.ModifyContent VirtualMachine.Namespace.Query
          VirtualMachine.Namespace.ReadContent VirtualMachine.Provisioning.Clone
          VirtualMachine.Provisioning.CloneTemplate
          VirtualMachine.Provisioning.CreateTemplateFromVM
          VirtualMachine.Provisioning.Customize
          VirtualMachine.Provisioning.DeployTemplate
          VirtualMachine.Provisioning.DiskRandomAccess
          VirtualMachine.Provisioning.DiskRandomRead
          VirtualMachine.Provisioning.FileRandomAccess
          VirtualMachine.Provisioning.GetVmFiles
          VirtualMachine.Provisioning.MarkAsTemplate
          VirtualMachine.Provisioning.MarkAsVM
          VirtualMachine.Provisioning.ModifyCustSpecs
          VirtualMachine.Provisioning.PromoteDisks
          VirtualMachine.Provisioning.PutVmFiles
          VirtualMachine.Provisioning.ReadCustSpecs
          VirtualMachine.State.CreateSnapshot VirtualMachine.State.RemoveSnapshot
          VirtualMachine.State.RenameSnapshot VirtualMachine.State.RevertToSnapshot
        END
        govc permissions.set -principal CLUSTER_USER_ACCOUNT@vsphere.local \
         -role anthos -propagate=true
        




To learn how to manage privileges, refer to [Managing Permissions for vCenter Components](https://docs.vmware.com/en/VMware-vSphere/6.5/com.vmware.vsphere.security.doc/GUID-3B78EEB3-23E2-4CEB-9FBD-E432B606011A.html).

### vCenter user account privileges with folders

Starting with Google Distributed Cloud version 1.4, you can place VM images and templates in a separate VM folder, as opposed to the global datacenter folder. This is only supported in the v1 format of the [admin cluster configuration](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.6/how-to/admin-cluster-configuration-file).

In your [admin cluster configuration file](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.6/how-to/admin-cluster-configuration-file), create a new key called `folder`. Set the value of `folder` to the name of the vCenter folder that you want to use for this Google Distributed Cloud deployment. All user clusters will inherit the folder automatically. Do not specify a folder in your [user cluster configuration files](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.6/how-to/user-cluster-configuration-file).

If the `folder` key is not specified, or if the value is left blank, the top level Datacenter VM folder is used. Like other vCenter resources, the folder must be created prior to deployment, with the appropriate permissions.

For example, in the `admin-cluster.yaml` for your deployment:
    
    
    apiVersion: v1
    kind: AdminCluster
    #...
    vCenter:
      address: mtv-example-vc01.anthos
      datacenter: mtv-example-vc01
      cluster: admin-permissions
      resourcePool: example-cluster-resourcepool
      datastore: example-cluster-datastore
      # insert the following new line with the path to the vcenter folder here.
      folder: my-vm-folder
    

### Setting permissions when using a folder

In Google Distributed Cloud versions older than 1.4, we required a set of permissions to be applied to the entire vCenter cluster. While this was simpler to configure, these permissions did not constrain the Google Distributed Cloud vCenter user sufficiently. While the set of permissions remain the same in Google Distributed Cloud 1.4, we can now apply them to a much smaller set of objects, provided a folder is specified for the deployment, as described above.

The following is a set of roles, their permissions, and the objects the roles must be applied to. Entries marked "(recursively)" must be applied with the Propagate field set to true, so the permissions are inherited by all child objects.

### Role: ClusterEditor

**Description** : Apply DRS rules to Clusters + Read Only Access

**Objects** : $VCenter.Cluster(recursively)

**Privileges** : System.Read System.View System.Anonymous Host.Inventory.EditCluster

### Role: SessionValidator

**Description** : Validate an existing VCenter session + Read Only Access

**Objects** : $VCenter.Root

**Privileges** : System.Read System.View System.Anonymous Session.ValidateSessions

### Role: ReadOnly

**Description** : Built in role that permits enumerating objects

**Objects** : $VCenter.Datacenter(recursively), $VCenter "VM Network"

**Privileges** : System.Read System.View System.Anonymous

### Role: Anthos

**Description** : Set of permissions required to deploy, manage and monitor clusters. This role represents the set of permissions that was applied to the entire VCenter environment in GKE OnPrem 1.3 and earlier.

**Objects** : $VCenter.Datastore(recursively), $VCenter.ResourcePool(recursively), $VCenter.Folder(recursively), $VCenter.Network(recursively)

Click to see the privileges in the Anthos role.

**Privileges** :

  * Datastore.AllocateSpace
  * Datastore.Browse
  * Datastore.Config
  * Datastore.DeleteFile
  * Datastore.FileManagement
  * Datastore.UpdateVirtualMachineFiles
  * Datastore.UpdateVirtualMachineMetadata
  * Folder.Create
  * Folder.Delete
  * Folder.Move
  * Folder.Rename
  * Host.Inventory.EditCluster
  * InventoryService.Tagging.CreateTag
  * Network.Assign
  * Resource.ApplyRecommendation
  * Resource.AssignVMToPool
  * Resource.ColdMigrate
  * Resource.HotMigrate
  * Resource.QueryVMotion
  * Sessions.ValidateSession
  * StorageViews.View
  * System.Anonymous
  * System.Read
  * System.View
  * Task.Create
  * Task.Update
  * VApp.ApplicationConfig
  * VApp.Import
  * VApp.InstanceConfig
  * VirtualMachine.Config.AddExistingDisk
  * VirtualMachine.Config.AddNewDisk
  * VirtualMachine.Config.AddRemoveDevice
  * VirtualMachine.Config.AdvancedConfig
  * VirtualMachine.Config.Annotation
  * VirtualMachine.Config.CPUCount
  * VirtualMachine.Config.ChangeTracking
  * VirtualMachine.Config.DiskExtend
  * VirtualMachine.Config.DiskLease
  * VirtualMachine.Config.EditDevice
  * VirtualMachine.Config.HostUSBDevice
  * VirtualMachine.Config.ManagedBy
  * VirtualMachine.Config.Memory
  * VirtualMachine.Config.MksControl
  * VirtualMachine.Config.QueryFTCompatibility
  * VirtualMachine.Config.QueryUnownedFiles
  * VirtualMachine.Config.RawDevice
  * VirtualMachine.Config.ReloadFromPath
  * VirtualMachine.Config.RemoveDisk
  * VirtualMachine.Config.Rename
  * VirtualMachine.Config.ResetGuestInfo
  * VirtualMachine.Config.Resource
  * VirtualMachine.Config.Settings
  * VirtualMachine.Config.SwapPlacement
  * VirtualMachine.Config.ToggleForkParent
  * VirtualMachine.Config.UpgradeVirtualHardware
  * VirtualMachine.GuestOperations.Execute
  * VirtualMachine.GuestOperations.Modify
  * VirtualMachine.GuestOperations.ModifyAliases
  * VirtualMachine.GuestOperations.Query
  * VirtualMachine.GuestOperations.QueryAliases
  * VirtualMachine.Hbr.ConfigureReplication
  * VirtualMachine.Hbr.MonitorReplication
  * VirtualMachine.Hbr.ReplicaManagement
  * VirtualMachine.Interact.AnswerQuestion
  * VirtualMachine.Interact.Backup
  * VirtualMachine.Interact.ConsoleInteract
  * VirtualMachine.Interact.CreateScreenshot
  * VirtualMachine.Interact.CreateSecondary
  * VirtualMachine.Interact.DefragmentAllDisks
  * VirtualMachine.Interact.DeviceConnection
  * VirtualMachine.Interact.DisableSecondary
  * VirtualMachine.Interact.DnD
  * VirtualMachine.Interact.EnableSecondary
  * VirtualMachine.Interact.GuestControl
  * VirtualMachine.Interact.MakePrimary
  * VirtualMachine.Interact.Pause
  * VirtualMachine.Interact.PowerOff
  * VirtualMachine.Interact.PowerOn
  * VirtualMachine.Interact.PutUsbScanCodes
  * VirtualMachine.Interact.Record
  * VirtualMachine.Interact.Replay
  * VirtualMachine.Interact.Reset
  * VirtualMachine.Interact.SESparseMaintenance
  * VirtualMachine.Interact.SetCDMedia
  * VirtualMachine.Interact.SetFloppyMedia
  * VirtualMachine.Interact.Suspend
  * VirtualMachine.Interact.TerminateFaultTolerantVM
  * VirtualMachine.Interact.ToolsInstall
  * VirtualMachine.Interact.TurnOffFaultTolerance
  * VirtualMachine.Inventory.Create
  * VirtualMachine.Inventory.CreateFromExisting
  * VirtualMachine.Inventory.Delete
  * VirtualMachine.Inventory.Move
  * VirtualMachine.Inventory.Register
  * VirtualMachine.Inventory.Unregister
  * VirtualMachine.Namespace.Event
  * VirtualMachine.Namespace.EventNotify
  * VirtualMachine.Namespace.Management
  * VirtualMachine.Namespace.ModifyContent
  * VirtualMachine.Namespace.Query
  * VirtualMachine.Namespace.ReadContent
  * VirtualMachine.Provisioning.Clone
  * VirtualMachine.Provisioning.CloneTemplate
  * VirtualMachine.Provisioning.CreateTemplateFromVM
  * VirtualMachine.Provisioning.Customize
  * VirtualMachine.Provisioning.DeployTemplate
  * VirtualMachine.Provisioning.DiskRandomAccess
  * VirtualMachine.Provisioning.DiskRandomRead
  * VirtualMachine.Provisioning.FileRandomAccess
  * VirtualMachine.Provisioning.GetVmFiles
  * VirtualMachine.Provisioning.MarkAsTemplate
  * VirtualMachine.Provisioning.MarkAsVM
  * VirtualMachine.Provisioning.ModifyCustSpecs
  * VirtualMachine.Provisioning.PromoteDisks
  * VirtualMachine.Provisioning.PutVmFiles
  * VirtualMachine.Provisioning.ReadCustSpecs
  * VirtualMachine.State.CreateSnapshot
  * VirtualMachine.State.RemoveSnapshot
  * VirtualMachine.State.RenameSnapshot
  * VirtualMachine.State.RevertToSnapshot



### Known issue: installer fails when creating vSphere datadisk

(Issue ID 156233307)

The Google Distributed Cloud installer can fail if custom roles are bound at the wrong permissions level.

When the role binding is incorrect, creating a vSphere datadisk with `govc` hangs and the disk is created with a size equal to 0. To fix the issue, you should bind the custom role at the vSphere vcenter level (root).

If you want to bind the custom role at the DC level (or lower than root), you also need to to bind the read-only role to the user at the root vCenter level.

For more information on role creation, see [vCenter user account privileges.](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.6/how-to/vsphere-requirements-basic#vcenter-user-account-privileges)

## Resource requirements for admin workstation, admin cluster, and user clusters

The physical ESXi hosts in your data center must provide enough storage, CPU, and RAM resources to fulfill the needs of the virtual machines that you will create during your initial installation of Google Distributed Cloud. Your data center must also provide enough virtual disk space to fulfill [PersistentVolumeClaims (PVCs)](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.20/#persistentvolumeclaim-v1-core) created by Prometheus and Google Cloud Observability.

The initial installation of Google Distributed Cloud requires these resources:

  * 36 vCPU
  * 98241 MB RAM
  * 2280 GB virtual disk space



For more detailed information on resource requirements, see [CPU, RAM, and Storage requirements](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.6/how-to/cpu-ram-storage).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
