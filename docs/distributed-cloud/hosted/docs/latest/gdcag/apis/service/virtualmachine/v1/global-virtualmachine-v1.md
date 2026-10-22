---
url: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/apis/service/virtualmachine/v1/global-virtualmachine-v1/
title: KRM API virtualmachine.global.gdc.goog/v1 \u00a0|\u00a0 Google Distributed Cloud air-gapped \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T12:56:43.130079+00:00
---

# KRM API virtualmachine.global.gdc.goog/v1  |  Google Distributed Cloud air-gapped  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/apis/service/virtualmachine/v1/global-virtualmachine-v1/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Distributed, hybrid, and multicloud ](https://docs.cloud.google.com/docs/dhm-cloud)
  * [ Google Distributed Cloud ](https://docs.cloud.google.com/distributed-cloud/docs)
  * [ Air-gapped ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdch)
  * [ 1.16.2 (Latest) ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag)
  * [ Reference ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/reference/reference-overview)



Send feedback 

#  KRM API virtualmachine.global.gdc.goog/v1 Stay organized with collections  Save and categorize content based on your preferences. 

## virtualmachine.global.gdc.goog/v1

### VirtualMachineDiskTemplate

VirtualMachineTemplateDisk defines the properties of a disk to be created and attached to a VM instantiated from a template.

_Appears in:_ \- VirtualMachineTemplateSpec

Field | Description  
---|---  
`boot` _boolean_ | Specifies whether this disk will be the boot device. Exactly one disk in the template must be marked as the boot disk.  
`autoDelete` _boolean_ | Specifies whether the disk should be automatically deleted when the VirtualMachine is deleted.  
`spec` _VirtualMachineDiskSpec_ | Spec defines the properties of the disk itself (e.g., size, source image).  
  
### VirtualMachineImage

Represents the disk image that can be used on virtual machine.

_Appears in:_ \- VirtualMachineImageList

Field | Description  
---|---  
`apiVersion` _string_ | `virtualmachine.global.gdc.goog/v1`  
`kind` _string_ | `VirtualMachineImage`  
`metadata` _[ObjectMeta](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.25/#objectmeta-v1-meta)_ | Refer to Kubernetes API documentation for fields of `metadata`.  
`spec` _VirtualMachineImageSpec_ |   
`status` _VirtualMachineImageStatus_ |   
  
### VirtualMachineImageList

Represents a collection of virtual machine images.

Field | Description  
---|---  
`apiVersion` _string_ | `virtualmachine.global.gdc.goog/v1`  
`kind` _string_ | `VirtualMachineImageList`  
`metadata` _[ListMeta](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.25/#listmeta-v1-meta)_ | Refer to Kubernetes API documentation for fields of `metadata`.  
`items` _VirtualMachineImage array_ |   
  
### VirtualMachineImageStatus

Defines the status of a Virtual Machine Image.

_Appears in:_ \- VirtualMachineImage

Field | Description  
---|---  
`conditions` _[Condition](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.25/#condition-v1-meta) array_ | Conditions of the virtual machine image.  
`errors` _VMMError array_ | A list of any errors that occurred during the reconciliation of this resource.  
`storageLocations` _string array_ | The list of zones where this Virtual Machine Image is stored.  
`zones` _VirtualMachineImageZoneStatus array_ | The list of zone statuses where the resource is propagated to.  
  
### VirtualMachineImageZoneStatus

Provides the status of a zone rolling out to a particular zone.

_Appears in:_ \- VirtualMachineImageStatus

Field | Description  
---|---  
`name` _string_ | The name of the zone where the replica this status represents is in.  
`conditions` _[Condition](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.25/#condition-v1-meta) array_ | The observations of the current rollout.  
  
### VirtualMachineTemplate

Represents a template of a Virtual Machine.

_Appears in:_ \- VirtualMachineTemplateList

Field | Description  
---|---  
`apiVersion` _string_ | `virtualmachine.global.gdc.goog/v1`  
`kind` _string_ | `VirtualMachineTemplate`  
`metadata` _[ObjectMeta](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.25/#objectmeta-v1-meta)_ | Refer to Kubernetes API documentation for fields of `metadata`.  
`spec` _VirtualMachineTemplateSpec_ |   
`status` _VirtualMachineTemplateStatus_ |   
  
### VirtualMachineTemplateList

Defines a list of `VirtualMachineTemplate` resources.

Field | Description  
---|---  
`apiVersion` _string_ | `virtualmachine.global.gdc.goog/v1`  
`kind` _string_ | `VirtualMachineTemplateList`  
`metadata` _[ListMeta](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.25/#listmeta-v1-meta)_ | Refer to Kubernetes API documentation for fields of `metadata`.  
`items` _VirtualMachineTemplate array_ |   
  
### VirtualMachineTemplateReplica

Represents a template of a Virtual Machine Template.

_Appears in:_ \- VirtualMachineTemplateReplicaList

Field | Description  
---|---  
`apiVersion` _string_ | `virtualmachine.global.gdc.goog/v1`  
`kind` _string_ | `VirtualMachineTemplateReplica`  
`metadata` _[ObjectMeta](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.25/#objectmeta-v1-meta)_ | Refer to Kubernetes API documentation for fields of `metadata`.  
`spec` _VirtualMachineTemplateSpec_ |   
`status` _VirtualMachineTemplateReplicaStatus_ |   
  
### VirtualMachineTemplateReplicaList

Represents a collection of `VirtualMachineTemplateReplica` resources.

Field | Description  
---|---  
`apiVersion` _string_ | `virtualmachine.global.gdc.goog/v1`  
`kind` _string_ | `VirtualMachineTemplateReplicaList`  
`metadata` _[ListMeta](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.25/#listmeta-v1-meta)_ | Refer to Kubernetes API documentation for fields of `metadata`.  
`items` _VirtualMachineTemplateReplica array_ |   
  
### VirtualMachineTemplateReplicaStatus

Contains the observed state of the Virtual Machine Template Replica.

_Appears in:_ \- VirtualMachineTemplateReplica \- VirtualMachineTemplateZoneStatus

Field | Description  
---|---  
`conditions` _[Condition](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.25/#condition-v1-meta) array_ | Conditions of the Virtual Machine Template Replica.  
  
### VirtualMachineTemplateSpec

Defines the specification of a Virtual Machine Template.

_Appears in:_ \- VirtualMachineTemplate \- VirtualMachineTemplateReplica

Field | Description  
---|---  
`compute` _Compute_ | Specifies the CPU and Memory of the VM. CPU and Memory can be defined directly or through the VirtualMachineType. Changes to Compute require a reboot to take effect. Compute is immutable when the VM is in Unknown state.  
`virtualMachineDiskTemplates` _VirtualMachineDiskTemplate array_ | Disks specifies the list of disks to create and attach.  
`startupScripts` _StartupScript array_ | Specifies the list of startup scripts for the VM. StartupScripts only take effect on VMs that have cloud-init installed. They are executed in alphabetical order, based on the name of each startup script.  
`guestEnvironment` _GuestEnvironment_ | Specifies the VM's guest environment configuration. If the field is nil the enable field in AccessManagement is true by default. Otherwise, the non-nil configuration for each sub-feature inside the structure overrides the default configuration of the sub-feature.  
`shieldConfig` _ShieldConfig_ | Specifies the VM's security-related configurations.  
`network` _NetworkSpec_ | Specifies the network configuration.  
`gracefulShutdown` _GracefulShutdown_ | GracefulShutdown configures graceful shutdown for the VM.  
  
### VirtualMachineTemplateStatus

Contains the observed state of the Virtual Machine Template.

_Appears in:_ \- VirtualMachineTemplate

Field | Description  
---|---  
`conditions` _[Condition](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.25/#condition-v1-meta) array_ | The observations of the overall state of the resource. Known condition types: Ready.  
`rollout` _RolloutStatus_ | The current strategy used to roll out the resource to each zone.  
`zones` _VirtualMachineTemplateZoneStatus array_ | The list of zone statuses where the resource is rolled out to.  
  
### VirtualMachineTemplateZoneStatus

Provides the status of a Virtual Machine Template rolling out to a particular zone.

_Appears in:_ \- VirtualMachineTemplateStatus

Field | Description  
---|---  
`name` _string_ | The name of the zone where the replica this status represents is in.  
`rolloutStatus` _ZoneRolloutStatus_ | The status of rolling out the replica to the zone.  
`replicaStatus` _VirtualMachineTemplateReplicaStatus_ | The reconciliation status of the replica collected from the zone. Any condition within the field that has an .observedGeneration less than .rolloutStatus.replicaGeneration is out of date.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
