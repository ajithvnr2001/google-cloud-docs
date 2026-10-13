---
url: https://docs.cloud.google.com/vmware-engine/docs/concepts-permission-model/
title: Private cloud vSphere permission model \u00a0|\u00a0 Google Cloud VMware Engine \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:24:08.180218+00:00
---

# Private cloud vSphere permission model  |  Google Cloud VMware Engine  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/vmware-engine/docs/concepts-permission-model/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ VMware Engine ](https://docs.cloud.google.com/vmware-engine/docs)
  * [ Guides ](https://docs.cloud.google.com/vmware-engine/docs/overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Private cloud vSphere permission model

Google Cloud VMware Engine retains full administrative access to your private cloud environment. You are granted sufficient administrator privileges to deploy and manage the virtual machines (VMs) in your environment. If needed, you can temporarily [elevate your privileges](https://docs.cloud.google.com/vmware-engine/docs/private-clouds/howto-elevate-privilege) to perform advanced administrative functions.

## CloudOwner user

When you create a private cloud, a default user, `CloudOwner@gve.local` is created in the vCenter Single Sign-On domain and given `Cloud-Owner-Role` access to manage objects in the private cloud.

## vCenter roles

Roles in vCenter define a set of privileges that let a user perform certain operations. When you create a private cloud, VMware Engine creates a set of roles in vCenter and assigns those roles to user groups.

Roles that have a name containing "Global" apply at the level of the `vCenter` object. All other roles apply at the level of `Datacenter` object on vCenter.

## vCenter user groups

Deploying a private cloud creates a group called `Cloud-Owner-Group`. Users in this group can administer various aspects of the vSphere environment in the private cloud. The `Cloud-Owner-Group` group is automatically given `Cloud-Owner-Role` privileges, and the `CloudOwner` user is added as a member of this group.

VMware Engine creates additional groups with limited privileges for ease of management. You can add any user to these pre-created groups, and this process assigns the corresponding privileges to the user.

For information about granting individual user permissions or creating new user groups, see [Managing vSphere permissions](https://docs.cloud.google.com/vmware-engine/docs/vmware-platform/howto-permissions-model).

### Pre-created vCenter user groups

Group name | Purpose | Role | Scope  
---|---|---|---  
Cloud-Owner-Group | Administrative privileges for the private cloud vCenter | Cloud-Owner-Global-Role | `vCenter` object  
Cloud-Owner-Role | `Datacenter` object  
Cloud-Global-Cluster-Admin-Group | Administrative privileges for clusters in the private cloud vCenter |  Cloud-Storage-Admin-Global-Role  | `vCenter` object  
Cloud-Cluster-Admin-Role | `Datacenter` object  
Cloud-Global-Storage-Admin-Group | Management privileges for VMs in the private cloud vCenter | Cloud-Storage-Admin-Role | `Datacenter` object  
Cloud-Global-Network-Admin-Group | Management privileges for networks and distributed port groups in the private cloud vCenter | Cloud-Network-Admin-Role | `Datacenter` object  
Cloud-Global-VM-Admin-Group | Management privileges for VMs in the private cloud vCenter  |  Cloud-VM-Admin-Global-Role  | `vCenter` object  
Cloud-VM-Admin-Role | `Datacenter` object  
**Warning:** New user groups must have permissions that are lower than `Cloud-Owner-Role`. Groups with permissions higher than `Cloud-Owner-Role` are automatically reset to `Cloud-Owner-Role`.

## List of vCenter privileges for default roles

The following sections list vCenter privileges for each role in the groups created by VMware Engine.

### Cloud-Owner-Global-Role

Category | Privilege  
---|---  
Alarms |  Acknowledge alarm  
Content Library |  Add library item Create local library Create subscribed library Delete library item Delete local library Delete subscribed library Download files Evict library item Evict subscribed library Import storage Probe subscription information Read storage Sync library item Sync subscribed library Type introspection Update configuration settings Update files Update library Update library item Update local library Update subscribed library View configuration settings  
Cryptographic operations |  Manage KMS Manage encryption policies  
Datastore |  Allocate space Browse datastore Configure datastore Low-level file operations Move datastore Remove datastore Remove file Rename datastore Update VM files Update VM metadata  
Global |  Cancel task Diagnostics Global tag Manage custom attributes Set custom attribute  
Host > vSphere Replication |  Manage replication  
vSphere tagging |  Assign or unassign vSphere tag Assign or unassign vSphere tag on Object Create vSphere tag Create vSphere tag category Edit vSphere tag Edit vSphere tag category  
Resource |  Assign VM to resource pool  
Profile-driven storage |  Profile-driven storage update Profile-driven storage view  
Virtual machine > Provisioning |  Customize guest Modify customization specification Read customization specifications  
  
### Cloud-Storage-Admin-Global-Role

Category | Privilege  
---|---  
Content Library |  Add library item Delete library item Update library item  
vSphere tagging |  Assign or unassign vSphere tag on Object  
Profile-driven storage |  Profile-driven storage view  
Virtual machine > Provisioning |  Customize guest Modify customization specification Read customization specifications  
  
### Cloud-VM-Admin-Global-Role

Category | Privilege  
---|---  
Content Library |  Add library item Delete library item Update library item  
vSphere tagging |  Assign or unassign vSphere tag on Object  
Profile-driven storage |  Profile-driven storage view  
Virtual machine > Provisioning |  Customize guest Modify customization specification Read customization specifications  
  
### Cloud-Owner-Role

Category | Privilege  
---|---  
Alarms |  Acknowledge alarm Create alarm Disable alarm action Modify alarm Remove alarm Set alarm status  
Permissions | Modify permission  
Content library |  Add library item Create local library Create subscribed library Delete library item Delete local library Delete subscribed library Download files Evict library item Evict subscribed library Import storage Probe subscription information Read storage Sync library item Sync subscribed library Type introspection Update configuration settings Update files Update library Update library item Update local library Update subscribed library View configuration settings  
Cryptographic operations |  Add disk Clone Decrypt Direct access Encrypt Encrypt new Manage KMS Manage encryption policies Manage keys Migrate Recrypt Register VM Register host  
dvPort group |  Create Delete Modify Policy operation Scope operation  
Datastore |  Allocate space Browse datastore Configure datastore Low-level file operations Move datastore Remove datastore Remove file Rename datastore Update VM files Update VM metadata  
ESX Agent Manager |  Config Modify View  
Extension |  Register extension Unregister extension Update extension  
External stats provider |  Register Unregister Update  
Folder |  Create folder Delete folder Move folder Rename folder  
Global |  Cancel task Capacity planning Diagnostics Disable methods Enable methods Global tag Health Licenses Log event Manage custom attributes Proxy Script action Service managers Set custom attribute System tag  
Health update provider |  Register Unregister Update  
Host > Inventory |  Modify cluster  
vSphere tagging |  Assign or unassign vSphere tag Create vSphere tag Create vSphere tag category Delete vSphere tag Delete vSphere tag category Edit vSphere tag Edit vSphere tag category Modify UsedBy field for category Modify UsedBy field for tag  
Network |  Assign network Configure Move network Remove  
Performance |  Modify intervals  
Host profile |  View  
Resource |  Apply recommendation Assign vApp to resource pool Assign VM to resource pool Create resource pool Migrate powered off virtual machine Migrate powered on virtual machine Modify resource pool Move resource pool Query vMotion Remove resource pool Rename resource pool  
Scheduled task | Create tasks Modify task Remove task Run task  
Sessions |  Impersonate user Message Validate session View and stop sessions  
Datastore cluster | Configure a datastore cluster  
Profile-driven storage |  Profile-driven storage update Profile-driven storage view  
Storage views |  Configure service View  
Tasks |  Create task Update task  
Transfer service | Manage Monitor  
vApp |  Add VM Assign resource pool Assign vApp Clone Create Delete Export Import Move Power off Power on Rename Suspend Unregister View OVF environment vApp application configuration vApp instance configuration vApp managedBy configuration vApp resource configuration  
VRMPolicy |  Query VRMPolicy Update VRMPolicy  
Virtual machine > Configuration |  Add existing disk Add new disk Add or remove device Advanced Change CPU count Change resource Configure managedBy Disk change tracking Disk lease Display connection settings Extend virtual disk Host USB device Memory Modify device settings Query fault tolerance compatibility Query unowned files Raw device Reload from path Remove disk Rename Reset guest information Set annotation Settings Swapfile placement Toggle fork parent Unlock VM Upgrade VM compatibility  
Virtual machine > Guest operations |  Guest operation alias modification Guest operation alias query Guest operation modifications Guest operation program execution Guest operation queries  
Virtual machine > Interaction |  Answer question Backup operation on VM Configure CD media Configure floppy media Console interaction Create screenshot Defragment all disks Device connection Drag and drop Guest operating system management by VIX API Inject USB HID scan codes Pause or Unpause Perform wipe or shrink operations Power off Power on Record session on VM Replay session on VM Reset Resume fault tolerance Suspend Suspend fault tolerance Test failover Test restart secondary VM Turn off fault tolerance Turn on fault tolerance VMware tools installation  
Virtual machine > Inventory |  Create from existing Create new Move Register Remove Unregister  
Virtual machine > Provisioning |  Allow disk access Allow file access Allow read-only disk access Allow VM download Allow VM files upload Clone template Clone VM Create template from VM Customize Deploy template Mark as template Mark as VM Modify customization specification Promote disks Read customization specifications  
Virtual machine > Service configuration |  Allow notifications Allow polling of global event notifications Manage service configurations Modify service configuration Query service configurations Read service configuration  
Virtual machine > Snapshot management |  Create snapshot Remove snapshot Rename snapshot Revert to snapshot  
Virtual machine > vSphere replication |  Configure replication Manage replication Monitor replication  
vService |  Create dependency Destroy dependency Reconfigure dependency configuration Update dependency  
  
### Cloud-Cluster-Admin-Role

Category | Privilege  
---|---  
Datastore |  Allocate space Browse datastore Configure datastore Low-level file operations Remove datastore Rename datastore Update VM files Update VM metadata  
Folder |  Create folder Delete folder Move folder Rename folder  
Host > Configuration | Storage partition configuration  
vSphere tagging |  Assign or unassign vSphere tag Create vSphere tag Create vSphere tag category Delete vSphere tag Delete vSphere tag category Edit vSphere tag Edit vSphere tag category Modify UsedBy field for category Modify UsedBy field for tag  
Network | Assign network  
Resource |  Apply recommendation Assign vApp to resource pool Assign VM to resource pool Create resource pool Migrate powered off VM Migrate powered on VM Modify resource pool Move resource pool Query vMotion Remove resource pool Rename resource pool  
vApp |  Add VM Assign resource pool Assign vApp Clone Create Delete Export Import Move Power off Power on Rename Suspend Unregister View OVF environment vApp application configuration vApp instance configuration vApp managedBy configuration vApp resource configuration  
VRMPolicy |  Query VRMPolicy Update VRMPolicy  
Virtual machine > Configuration |  Add existing disk Add new disk Add or remove device Advanced Change CPU count Change resource Configure managedBy Disk change tracking Disk lease Display connection settings Extend virtual disk Host USB device Memory Modify device settings Query fault tolerance compatibility Query unowned files Raw device Reload from path Remove disk Rename Reset guest information Set annotation Settings Swapfile placement Toggle fork parent Unlock VM Upgrade VM compatibility  
Virtual machine > Guest operations |  Guest operation alias modification Guest operation alias query Guest operation modifications Guest operation program execution Guest operation queries  
Virtual machine > Interaction |  Answer question Backup operation on VM Configure CD media Configure floppy media Console interaction Create screenshot Defragment all disks Device connection Drag and drop Guest operating system management by VIX API Inject USB HID scan codes Pause or unpause Perform wipe or shrink operations Power off Power on Record session on VM Replay session on VM Reset Resume fault tolerance Suspend Suspend fault tolerance Test failover Test restart secondary VM Turn off fault tolerance Turn on fault tolerance VMware tools install  
Virtual machine > Inventory |  Create from existing Create new Move Register Remove Unregister  
Virtual machine > Provisioning |  Allow disk access Allow file access Allow read-only disk access Allow VM download Allow VM files upload Clone template Clone VM Create template from VM Customize Deploy template Mark as template Mark as VM Modify customization specification Promote disks Read customization specifications  
Virtual machine > Service configuration |  Allow notifications Allow polling of global event notifications Manage service configurations Modify service configuration Query service configurations Read service configuration  
Virtual machine > Snapshot management |  Create snapshot Remove snapshot Rename snapshot Revert to snapshot  
Virtual machine > vSphere Replication |  Configure replication Manage replication Monitor replication  
vService |  Create dependency Destroy dependency Reconfigure dependency configuration Update dependency  
  
### Cloud-Storage-Admin-Role

Category | Privilege  
---|---  
Datastore |  Allocate space Browse datastore Configure datastore Low-level file operations Remove datastore Rename datastore Update VM files Update VM metadata  
Host > Configuration |  Storage partition configuration  
Datastore cluster |  Configure a datastore cluster  
Profile-driven storage |  Profile-driven storage update Profile-driven storage view  
Storage views |  Configure service View  
  
### Cloud-Network-Admin-Role

Category | Privilege  
---|---  
dvPort group |  Create Delete Modify Policy operation Scope operation  
Network |  Assign network Configure Move network Remove  
Virtual machine > Configuration |  Modify device settings  
  
### Cloud-VM-Admin-Role

Category | Privilege  
---|---  
Datastore |  Allocate space Browse datastore  
Network |  Assign network  
Resource |  Assign VM to resource pool Migrate powered off VM Migrate powered on VM  
vApp |  Export Import  
Virtual machine > Configuration |  Add existing disk Add new disk Add or remove device Advanced Change CPU count Change resource Configure managedBy Disk change tracking Disk lease Display connection settings Extend virtual disk Host USB device Memory Modify device settings Query fault tolerance compatibility Query unowned files Raw device Reload from path Remove disk Rename Reset guest information Set annotation Settings Swapfile placement Toggle fork parent Unlock VM Upgrade VM compatibility  
Virtual machine > Guest operations |  Guest operation alias modification Guest operation alias query Guest operation modifications Guest operation program execution Guest operation queries  
Virtual machine > Interaction |  Answer question Backup operation on VM Configure CD media Configure floppy media Console interaction Create screenshot Defragment all disks Device connection Drag and drop Guest operating system management by VIX API Inject USB HID scan codes Pause or unpause Perform wipe or shrink operations Power off Power on Record session on VM Replay session on VM Reset Resume fault tolerance Suspend Suspend fault tolerance Test failover Test restart secondary VM Turn off fault tolerance Turn on fault tolerance VMware tools install  
Virtual machine > Inventory |  Create from existing Create new Move Register Remove Unregister  
Virtual machine > Provisioning |  Allow disk access Allow file access Allow read-only disk access Allow VM download Allow VM files upload Clone template Clone VM Create template from VM Customize Deploy template Mark as template Mark as VM Modify customization specification Promote disks Read customization specifications  
Virtual machine > Service configuration |  Allow notifications Allow polling of global event notifications Manage service configurations Modify service configuration Query service configurations Read service configuration  
Virtual machine > Snapshot management |  Create snapshot Remove snapshot Rename snapshot Revert to snapshot  
Virtual machine > vSphere replication |  Configure replication Manage replication Monitor replication  
vService |  Create dependency Destroy dependency Reconfigure dependency configuration Update dependency  
  
## What's next

  * Learn how to [elevate private cloud privileges](https://docs.cloud.google.com/vmware-engine/docs/private-clouds/howto-elevate-privilege).
  * Learn how to [set up vCenter identity sources](https://docs.cloud.google.com/vmware-engine/docs/vmware-platform/howto-identity-sources).
  * Learn more about [VMware on your private cloud](https://docs.cloud.google.com/vmware-engine/docs/concepts-vmware-components).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
