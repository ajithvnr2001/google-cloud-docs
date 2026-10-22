---
url: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/apis/service/virtualmachine/v1/virtualmachine-v1/
title: KRM API virtualmachine.gdc.goog/v1 \u00a0|\u00a0 Google Distributed Cloud Hosted Appliance \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:16:31.703911+00:00
---

# KRM API virtualmachine.gdc.goog/v1  |  Google Distributed Cloud Hosted Appliance  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/apis/service/virtualmachine/v1/virtualmachine-v1/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Distributed, hybrid, and multicloud ](https://docs.cloud.google.com/docs/dhm-cloud)
  * [ Google Distributed Cloud ](https://docs.cloud.google.com/distributed-cloud/docs)
  * [ Air-gapped ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdch)
  * [ Appliance ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance)
  * [ 1.0.7 ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance)
  * [ Reference ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/reference/reference-overview)



Send feedback 

#  KRM API virtualmachine.gdc.goog/v1 Stay organized with collections  Save and categorize content based on your preferences. 

## virtualmachine.gdc.goog/v1

Contains API Schema definitions for the virtualmachine.gdc.goog v1 API group.

### AccessManagementConfig

Specifies the `AccessManagement` feature configuration in the guest environment.

_Appears in:_ \- GuestEnvironment

Field | Description  
---|---  
`enable` _boolean_ | Specifies whether to `enable` the `AccessManagement` feature in the VM's guest environment. See the `GuestEnvironment` field description for information about the default value of the field.  
  
### Compute

Specifies the CPU and memory attributes of a VM. You must specify _either_ `vcpus` and `memory` exclusively, _or_ specify only `VirtualMachineType`.

Specifying `vcpus` without `memory`, or vice versa, creates an invalid combination. Specifying `virtualMachineType` while specifying either `vcpus` or `memory`, or both also creates an invalid combination.

_Appears in:_ \- VirtualMachineSpec

Field | Description  
---|---  
`virtualMachineType` _string_ | Specifies the name of the referenced `VirtualMachineType`. The reference requires a predefined, or golden `VirtualMachineType` name.  
`vcpus` _integer_ | Specifies the number of VCPUs that are available to the instance. Specify `vcpus` as an integer. This value must be a multiple of 2, with 2 as the minimum and 128 as the maximum allowed.  
`memory` _Quantity_ | Specifies the amount of physical memory available to the instance. memory must have a minimum value of `1Gi`, and can be up to (including) `400Gi`.  
  
### DiskAttachment

Represents the attachment relationship between the `VirtualMachine` and the `VirtualMachineDisk`.

_Appears in:_ \- VirtualMachineSpec

Field | Description  
---|---  
`boot` _boolean_ | Specifies whether this disk is the boot device for the `VirtualMachine`. There must be exactly one disk marked as `boot`.  
`autoDelete` _boolean_ | Specifies whether the disk should be deleted when the `VirtualMachine` is deleted. `AutoDelete` only applies while a disk is attached to a `VirtualMachine`. A `VirtualMachineDisk` lifecycle is decoupled from the `VirtualMachine` once it is no longer referenced in `.spec.disks`.  
`virtualMachineDiskRef` _[LocalObjectReference](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.25/#localobjectreference-v1-core)_ | Refers to a `VirtualMachineDisk` in the same `namespace`.  
  
### DiskReplicationStatus

_Appears in:_ \- VirtualMachineDiskStatus

Field | Description  
---|---  
`role` _ReplicationRole_ | The role that this disk has in the replication relationship. Valid values are "primary" and "secondary".  
`primaryDisk` _ReplicatedDiskInfo_ | The primary disk that this disk is being replicated from, if this disk is a secondary disk. Will be nil for primary disks.  
`secondaryDisk` _ReplicatedDiskInfo_ | The secondary disk that this disk is being replicated to, if this disk is a primary disk. Will be nil for secondary disks.  
`volumeReplicationRelationship` _string_ | The name of the volume replication relationship object that is managing the replication.  
`conditions` _[Condition](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.25/#condition-v1-meta) array_ | The latest observations of the replications state.  
`errorStatus` _ErrorStatus_ | A list of any errors that occurred during replication.  
  
### DiskSource

Defines the source for the disk. Specify exactly one of the supported sources to use to populate a disk.

_Appears in:_ \- VirtualMachineDiskSpec

Field | Description  
---|---  
`image` _ImageDiskSource_ | Denotes that the disk is created from a disk Image.  
  
### FilterSpec

Defines the fine-grained restore Filter.

_Appears in:_ \- VirtualMachineRestoreRequestSpec

Field | Description  
---|---  
`targetedVirtualMachines` _VirtualMachineResourceConfig array_ | The set of VMs that needs to be restored. These VMs should be the ones that are part of the VirtualMachineBackup resource that is provided in the same VirtualMachineRestoreRequest.  
`targetedVirtualMachineDisks` _VirtualMachineResourceConfig array_ | The set of VMDisks that needs to be restored. These VMDisks should be the ones that are part of the VirtualMachineBackup resource that is provided in the same VirtualMachineRestoreRequest.  
`virtualMachineDiskOptions` _VirtualMachineDiskFilterOptions_ | Specifies the filter options for restoring disks. Specifying this field will not restore VirtualMachines, it will only restore VirtualMachineDisks based on selected field in VirtualMachineDiskFilterOptions. This field shouldn't be specified if one of TargetedVirtualMachines or TargetedVirtualMachineDisks is specified.  
  
### Firmware

Specifies the VM initialization options at boot time.

_Appears in:_ \- VirtualMachineSpec

Field | Description  
---|---  
`type` _string_ | Specifies whether to boot via UEFI or BIOS. Defaults to `bios`. Deprecated: Use ShieldConfig.BootType instead.  
`enableSecureBoot` _boolean_ | Enables or disables boot loader certificate verification. This is to assist in blocking modified or malicious code from loading. The default value is `true` if `type` is `uefi`. If `type` is set to `bios`, the default value is `false` and cannot be modified since boot loader certificate verification is not available for BIOS. Deprecated: Use ShieldConfig.EnableSecureBoot instead.  
  
### GCSReference

Represents the GCS source from which to store the image.

_Appears in:_ \- VirtualMachineImageSpec

Field | Description  
---|---  
`url` _string_ | The URL of the GCS object.  
  
### GuestEnvironment

Specifies the guest environment configuration.

_Appears in:_ \- VirtualMachineSpec

Field | Description  
---|---  
`accessManagement` _AccessManagementConfig_ | Specifies the access management configuration.  
  
### IPAddress

_Appears in:_ \- NetworkInterfaceSpec

Field | Description  
---|---  
`address` _string_ | The IP address. In GDC connected, the address may contain a subnet mask. If subnet mask is not included, /32 is taken as default. For example, 1.2.3.4 will be taken as 1.2.3.4/32. Alternatively, the input can be 1.2.3.4/24. In GDC airgapped, the address may not contain a subnet mask. Subnet information is retrieved from the Subnet object.  
`managed` _boolean_ | Whether the lifecycle of the Subnet associated with this IP address should be managed by the system in GDC airgapped. Unused in GDC connected. If true (default), a Subnet is created automatically for this IP and deleted during VM deletion. If false, the user must have created a Subnet and the Subnet must be in ready status.  
  
### ImageDestinationReference

Points to the destination to which the image contents are uploaded. Only one destination can be specified. Only supported in GDC Connected deployments. This field is required if the specified `ImageSourceReference` is `GCS`.

_Appears in:_ \- VirtualMachineImageImportSpec

Field | Description  
---|---  
`gcs` _ImageGCSDestinationReference_ | The bucket details for an image that is populated to gcs.  
  
### ImageDiskSource

Reference to the Image Source.

_Appears in:_ \- DiskSource

Field | Description  
---|---  
`name` _string_ | The name of the `VirtualMachineImage` API object.  
`namespace` _string_ | The namespace of the `VirtualMachineImage` API object. For golden images use `vm-system`. For images in the current project, set this as empty or use the current `namespace` value.  
  
### ImageGCSDestinationReference

Represents the GCS destination to which to import an image.

_Appears in:_ \- ImageDestinationReference

Field | Description  
---|---  
`bucketName` _string_ | The GCS Bucket name that holds this image.  
  
### ImageGCSSourceReference

Represents the GCS source from which to import an image.

_Appears in:_ \- ImageSourceReference

Field | Description  
---|---  
`bucketName` _string_ | The GCS Bucket name that holds this image.  
`objectName` _string_ | The name of the image within the bucket.  
  
### ImageMetadataInput

The specification for the `VirtualMachineImage`.

_Appears in:_ \- VirtualMachineImageImportSpec

Field | Description  
---|---  
`name` _string_ | The image name, such as `ubuntu-20.04-server-cloudimg`.  
`operatingSystem` _OSName_ | The name of the OS to which this image belongs, such as `ubuntu-2004`.  
`minimumDiskSize` _Quantity_ | The minimum size of the disk to which the image can be applied. This specifies only the recommended size for future disks that are created from this image. It does not represent the size of the image itself. This field is required if the image is being imported from object storage.  
  
### ImageObjectStorageSourceReference

Represents the object storage source from which to import an image.

_Appears in:_ \- ImageSourceReference

Field | Description  
---|---  
`bucketRef` _[LocalObjectReference](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.25/#localobjectreference-v1-core)_ | The name of the `Bucket` custom resource that holds this image. The `Bucket` custom resource must be in the same namespace as this object.  
`objectName` _string_ | The name of the image within the bucket.  
  
### ImagePrepareOptions

Represents the options for image preparation.

_Appears in:_ \- VirtualMachineImageImportSpec

Field | Description  
---|---  
`installGuestEnvironment` _boolean_ | Specifies whether to install the GDC air-gapped guest environment. Defaults to `true`.  
  
### ImageSourceReference

Points to the resource from which the image contents are populated. Only one source can be specified.

_Appears in:_ \- VirtualMachineImageImportSpec

Field | Description  
---|---  
`diskRef` _[LocalObjectReference](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.25/#localobjectreference-v1-core)_ | Specified when the image is populated from an existing `VirtualMachineDisk`.  
`objectStorage` _ImageObjectStorageSourceReference_ | The bucket details for an image that is populated from object storage.  
`gcs` _ImageGCSSourceReference_ | The bucket details for an image that is populated from gcs.  
  
### NetworkInterfaceSpec

Specifies the network interface configuration. In GDC connected, only Network and IPAddresses can be specified. In GDC airgapped, one of Network, Subnet, or IPAddresses must be specified. Subnet and IPAddresses can optionally be specified together.

_Appears in:_ \- NetworkSpec

Field | Description  
---|---  
`network` _string_ | The network that the interface is connected to. In GDC airgapped, valid values are: `default`, `multicast`.  
`subnet` _string_ | The subnet that the interface is connected to in GDC airgapped. Unused in GDC connected. If unspecified, defaults to the default subnet of the specified network.  
`subnetNamespace` _string_ | The namespace that the Subnet the interface is connected to in GDC airgapped. Unused in GDC connected. If unspecified, defaults to the same namespace as the VirtualMachine.  
`ipAddresses` _IPAddress array_ | The IP address to be assigned to the interface. Only the first IP address is assigned to the interface. In GDC airgapped, an IP address will be dynamically allocated if unspecified. In GDC connected, if the network is configured to use an external DHCP server, this field can optionally be used to specify a static address. If the network is not configured to use an external DHCP server, this field is required.  
  
### NetworkInterfaceStatus

NetworkInterfaceStatus is the status for the NetworkInterface resource.

_Appears in:_ \- NetworkStatus

Field | Description  
---|---  
`name` _string_ | Name denotes the name of the network interface exposed inside the VM, e.g. "eth0", "eth1".  
`ipAddresses` _string array_ | IpAddresses are the IP addresses assigned to the NetworkInterface.  
`macAddress` _string_ | MacAddress is the MAC address assigned to the NetworkInterface.  
  
### NetworkPerformanceSpec

_Appears in:_ \- NetworkSpec

Field | Description  
---|---  
`highThroughputMode` _boolean_ | Whether high-throughput optimization is enabled for all interfaces in the VM in GDC airgapped. Unused in GDC connected. If true, this uses features such as multiqueue to improve network performance. Defaults to `false`.  
  
### NetworkSpec

Specifies the network configuration.

_Appears in:_ \- VirtualMachineSpec

Field | Description  
---|---  
`interfaces` _NetworkInterfaceSpec array_ | The network interfaces attached to the VM. If no unicast interfaces are specified, a `default` interface is automatically added. Users in a multicast-enabled organization can add the `multicast` interface. The first interface specified will be treated as the default interface when setting up the default route inside the VM.  
`performanceSpec` _NetworkPerformanceSpec_ | Specifies the configuration for high performance networking.  
  
### NetworkStatus

NetworkStatus is the status for the network of the Virtual Machine.

_Appears in:_ \- VirtualMachineStatus

Field | Description  
---|---  
`interfaces` _NetworkInterfaceStatus array_ |   
  
### OSName

_Underlying type:_ `string` The list of valid OSes for use.

_Appears in:_ \- ImageMetadataInput \- OperatingSystemSpec

### OperatingSystemSpec

Contains the operating system information of an image.

_Appears in:_ \- VirtualMachineImageSpec

Field | Description  
---|---  
`name` _OSName_ | The name of the OS to which this image belongs, e.g. "windows-2016".  
  
### ReplicatedDiskInfo

_Appears in:_ \- DiskReplicationStatus

Field | Description  
---|---  
`name` _string_ | The name of the `VirtualMachineDisk` instance.  
`zone` _string_ | The zone of the `VirtualMachineDisk` instance.  
  
### SSHSpec

Stores the ssh credentials used to establish the connection.

_Appears in:_ \- VirtualMachineAccessRequestSpec

Field | Description  
---|---  
`key` _string_ | Specifies the public key to program for SSH access.  
`ttl` _[Duration](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.25/#duration-v1-meta)_ | Specifies the length of time for which this key is valid, expressed in hours, minutes and seconds. The default value is `24h0m0s`.  
  
### ServicePort

ServicePort contains information on service's port.

_Appears in:_ \- VirtualMachineExternalAccessSpec

Field | Description  
---|---  
`name` _string_ | The name of this port within the service.  
`protocol` _[Protocol](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.25/#protocol-v1-core)_ | The IP protocol for this port. Supports "TCP", "UDP", and "SCTP".  
`port` _integer_ | The port that will be exposed by this service.  
  
### ShieldConfig

Specifies the VM's security-related configurations.

_Appears in:_ \- VirtualMachineSpec

Field | Description  
---|---  
`bootType` _string_ | Specifies whether to boot via UEFI or BIOS. Defaults to `bios`.  
`enableSecureBoot` _boolean_ | Enables or disables boot loader certificate verification. This is to assist in blocking modified or malicious code from loading. The default value is `true` if `bootType` is `uefi`. If `bootType` is set to `bios`, the default value is `false` and cannot be modified since boot loader certificate verification is not available for BIOS.  
`enableVtpm` _boolean_ | Whether to emulate a VTPM device. Defaults to `false`.  
  
### StartupScript

Defines a startup script for a VM. Supports the specification of a startup script either as a plain text string or a Kubernetes secret. If the field `script` is specified, then the field `scriptSecretRef` should not be provided, and vice versa.

_Appears in:_ \- VirtualMachineSpec

Field | Description  
---|---  
`name` _string_ | Specifies the name of a script. Must match the regex `[\w][\w\-.]*` and be at most 255 characters. If specifying a script for a Windows VM, the name must include a '-' followed by the script extension as a suffix. For example, use the name `hello-world-ps1` for a Powershell script named `hello-world`.  
`script` _string_ | Specifies a plain text string that contains the script. The script content size must be lesser than 2048 bytes.  
`scriptSecretRef` _[LocalObjectReference](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.25/#localobjectreference-v1-core)_ | References a Kubernetes secret that contains the script. The `ScriptSecretRef` name must match the name of the Kubernetes secret.  
  
### VMMError

Wrapper for all VMM errors, including error codes.

_Appears in:_ \- VirtualMachineAccessRequestStatus \- VirtualMachineDiskStatus \- VirtualMachineExternalAccessStatus \- VirtualMachineImageImportStatus \- VirtualMachineImageStatus \- VirtualMachinePasswordResetRequestStatus \- VirtualMachineStatus

Field | Description  
---|---  
`code` _string_ | The code for the error. It includes a prefix with letters followed by a four-digit numeric code.  
`message` _string_ | The human-readable error message.  
  
### VirtualMachine

Represents the Virtual Machine's configuration and state.

_Appears in:_ \- VirtualMachineList

Field | Description  
---|---  
`apiVersion` _string_ | `virtualmachine.gdc.goog/v1`  
`kind` _string_ | `VirtualMachine`  
`metadata` _[ObjectMeta](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.25/#objectmeta-v1-meta)_ | Refer to Kubernetes API documentation for fields of `metadata`.  
`spec` _VirtualMachineSpec_ |   
`status` _VirtualMachineStatus_ |   
  
### VirtualMachineAccessRequest

Represents an access request to a VM.

_Appears in:_ \- VirtualMachineAccessRequestList

Field | Description  
---|---  
`apiVersion` _string_ | `virtualmachine.gdc.goog/v1`  
`kind` _string_ | `VirtualMachineAccessRequest`  
`metadata` _[ObjectMeta](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.25/#objectmeta-v1-meta)_ | Refer to Kubernetes API documentation for fields of `metadata`.  
`spec` _VirtualMachineAccessRequestSpec_ |   
`status` _VirtualMachineAccessRequestStatus_ |   
  
### VirtualMachineAccessRequestList

Contains a list of VirtualMachineAccessRequest objects.

Field | Description  
---|---  
`apiVersion` _string_ | `virtualmachine.gdc.goog/v1`  
`kind` _string_ | `VirtualMachineAccessRequestList`  
`metadata` _[ListMeta](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.25/#listmeta-v1-meta)_ | Refer to Kubernetes API documentation for fields of `metadata`.  
`items` _VirtualMachineAccessRequest array_ |   
  
### VirtualMachineAccessRequestSpec

Defines the `VirtualMachineAccessRequest` specification.

_Appears in:_ \- VirtualMachineAccessRequest

Field | Description  
---|---  
`vm` _string_ | Specifies the name of the VM to access.  
`user` _string_ | Specifies the username for accessing the VM.  
`ssh` _SSHSpec_ | Holds the ssh credentials used to access the VM.  
  
### VirtualMachineAccessRequestState

_Underlying type:_ `string` State of `VirtualMachineAccessRequest`.

_Appears in:_ \- VirtualMachineAccessRequestStatus

### VirtualMachineAccessRequestStatus

Describes the status of the VirtualMachineAccessRequest.

_Appears in:_ \- VirtualMachineAccessRequest

Field | Description  
---|---  
`state` _VirtualMachineAccessRequestState_ | Specifies the state of `VirtualMachineAccessRequest`.  
`reason` _string_ | Indicates the reason for the current status.  
`message` _string_ | Provides additional context for the current status.  
`processedAt` _[Time](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.25/#time-v1-meta)_ | Specifies the time when the request was processed.  
`errors` _VMMError array_ | A list of any errors that occurred during the reconciliation of this resource.  
  
### VirtualMachineAttachment

Contains information about which `VirtualMachine` this `VirtualMachineDisk` is attached to, and how it is attached.

_Appears in:_ \- VirtualMachineDiskStatus

Field | Description  
---|---  
`nameRef` _[LocalObjectReference](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.25/#localobjectreference-v1-core)_ | The name of an attached `VirtualMachine`.  
`uid` _UID_ | The UID of the attached `VirtualMachine`.  
`autoDelete` _boolean_ | Reflective of how the `VirtualMachine` attaches this disk. The disk is deleted when all VMs attached have `autoDelete` set to `true` and all VMs are deleted. If a minimum of one VM has `autoDelete` set to `false`, the disk will not be deleted.  
  
### VirtualMachineBackup

The Schema for the VirtualMachineBackups API.

_Appears in:_ \- VirtualMachineBackupList

Field | Description  
---|---  
`apiVersion` _string_ | `virtualmachine.gdc.goog/v1`  
`kind` _string_ | `VirtualMachineBackup`  
`metadata` _[ObjectMeta](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.25/#objectmeta-v1-meta)_ | Refer to Kubernetes API documentation for fields of `metadata`.  
`spec` _VirtualMachineBackupSpec_ |   
`status` _VirtualMachineBackupStatus_ |   
  
### VirtualMachineBackupConfig

Contains configuration details for executing the backup, including scope, location, and volume backup strategy.

_Appears in:_ \- VirtualMachineBackupPlanSpec \- VirtualMachineBackupSpec

Field | Description  
---|---  
`backupRepository` _string_ | Identifies the secondary storage location for this `VirtualMachineBackupPlan`. This field is meant for internal use only. Provide Backup repository only through VirtualMachineBackupPlanTemplate  
`backupScope` _VirtualMachineBackupScope_ | Specifies the resource(s) covered by this `VirtualMachineBackupPlan`.  
`volumeStrategy` _VolumeStrategy_ | Declares the strategy to use for backing-up volumes; for example, use a local snapshot vs. using remote or provisioner-specific backup.  
  
### VirtualMachineBackupList

Contains a list of VirtualMachineBackup.

Field | Description  
---|---  
`apiVersion` _string_ | `virtualmachine.gdc.goog/v1`  
`kind` _string_ | `VirtualMachineBackupList`  
`metadata` _[ListMeta](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.25/#listmeta-v1-meta)_ | Refer to Kubernetes API documentation for fields of `metadata`.  
`items` _VirtualMachineBackup array_ |   
  
### VirtualMachineBackupPlan

The Schema for the VirtualMachineBackupPlans API.

_Appears in:_ \- VirtualMachineBackupPlanList

Field | Description  
---|---  
`apiVersion` _string_ | `virtualmachine.gdc.goog/v1`  
`kind` _string_ | `VirtualMachineBackupPlan`  
`metadata` _[ObjectMeta](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.25/#objectmeta-v1-meta)_ | Refer to Kubernetes API documentation for fields of `metadata`.  
`spec` _VirtualMachineBackupPlanSpec_ |   
`status` _VirtualMachineBackupPlanStatus_ |   
  
### VirtualMachineBackupPlanList

Contains a list of VirtualMachineBackupPlan.

Field | Description  
---|---  
`apiVersion` _string_ | `virtualmachine.gdc.goog/v1`  
`kind` _string_ | `VirtualMachineBackupPlanList`  
`metadata` _[ListMeta](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.25/#listmeta-v1-meta)_ | Refer to Kubernetes API documentation for fields of `metadata`.  
`items` _VirtualMachineBackupPlan array_ |   
  
### VirtualMachineBackupPlanSpec

Defines a `VirtualMachineBackupPlan` which provides instructions for creating an underlying `BackupPlan` resource and `ProtectedApplication` to perform backups.

_Appears in:_ \- VirtualMachineBackupPlan

Field | Description  
---|---  
`virtualMachineBackupPlanTemplate` _string_ | The `VirtualMachineBackupPlanTemplate` must live in the same `namespace` as this vm backup plan.  
`backupConfig` _VirtualMachineBackupConfig_ | Defines the configuration and scope of the backup.  
`backupSchedule` _Schedule_ | The scheduled backup creation under this VM backup plan. Schedule is a mutable field which can be edited after creation By default, VM backup plan will be paused  
`retentionPolicy` _RetentionPolicy_ | The lifecycle of backups created under this plan. by default, backups can be deleted without any locking period by default, backups are not deleted by automatic schedule and retention policy can be modified  
  
### VirtualMachineBackupPlanStatus

Defines the observed state of `VirtualMachineBackupPlan`.

_Appears in:_ \- VirtualMachineBackupPlan

Field | Description  
---|---  
`backupPlan` _string_ | The name of the underlying backup plan managed by this `VirtualMachineBackupPlan`, used in GDC air-gapped Org v1 Architecture.  
`backupPlanStatus` _BackupPlanStatus_ | The embedded status of the underlying backup plan.  
`configBackupPlan` _string_ | The name of the underlying config backup plan managed by this `VirtualMachineBackupPlan`. Config here refers to VM and VM Disk, used in GDC air-gapped Org v2 Architecture.  
`volumeBackupPlan` _string_ | The name of the underlying volume backup plan managed by this `VirtualMachineBackupPlan`, used in GDC air-gapped Org v2 Architecture.  
`lastBackupTime` _[Time](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.25/#time-v1-meta)_ | The timestamp for the most recently executed backup. This field is used to schedule next backup  
`nextBackupTime` _[Time](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.25/#time-v1-meta)_ | The timestamp for the next scheduled backup. This field is used to schedule next backup  
`lastReconcileTime` _[Time](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.25/#time-v1-meta)_ | The timestamp of last reconciliation of this resource.  
`errorMessage` _string_ | ErrorMessage holds the error message that occurred during the last reconciliation attempt. This field is optional and will only be populated if an error occurred.  
  
### VirtualMachineBackupPlanTemplate

The `VirtualMachineBackupPlanTemplates` API schema.

_Appears in:_ \- VirtualMachineBackupPlanTemplateList

Field | Description  
---|---  
`apiVersion` _string_ | `virtualmachine.gdc.goog/v1`  
`kind` _string_ | `VirtualMachineBackupPlanTemplate`  
`metadata` _[ObjectMeta](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.25/#objectmeta-v1-meta)_ | Refer to Kubernetes API documentation for fields of `metadata`.  
`spec` _VirtualMachineBackupPlanTemplateSpec_ |   
`status` _VirtualMachineBackupPlanTemplateStatus_ |   
  
### VirtualMachineBackupPlanTemplateList

Contains a list of VirtualMachineBackupPlanTemplate.

Field | Description  
---|---  
`apiVersion` _string_ | `virtualmachine.gdc.goog/v1`  
`kind` _string_ | `VirtualMachineBackupPlanTemplateList`  
`metadata` _[ListMeta](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.25/#listmeta-v1-meta)_ | Refer to Kubernetes API documentation for fields of `metadata`.  
`items` _VirtualMachineBackupPlanTemplate array_ |   
  
### VirtualMachineBackupPlanTemplateSpec

Defines the template that the `VirtualMachineBackupPlans` use for deriving common parameters.

_Appears in:_ \- VirtualMachineBackupPlanTemplate

Field | Description  
---|---  
`backupRepository` _string_ | The name of a `BackupRepository` resource.  
  
### VirtualMachineBackupRequest

The Schema for the VirtualMachineBackupRequests API.

_Appears in:_ \- VirtualMachineBackupRequestList

Field | Description  
---|---  
`apiVersion` _string_ | `virtualmachine.gdc.goog/v1`  
`kind` _string_ | `VirtualMachineBackupRequest`  
`metadata` _[ObjectMeta](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.25/#objectmeta-v1-meta)_ | Refer to Kubernetes API documentation for fields of `metadata`.  
`spec` _VirtualMachineBackupRequestSpec_ |   
`status` _VirtualMachineBackupRequestStatus_ |   
  
### VirtualMachineBackupRequestList

Contains a list of VirtualMachineBackupRequest.

Field | Description  
---|---  
`apiVersion` _string_ | `virtualmachine.gdc.goog/v1`  
`kind` _string_ | `VirtualMachineBackupRequestList`  
`metadata` _[ListMeta](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.25/#listmeta-v1-meta)_ | Refer to Kubernetes API documentation for fields of `metadata`.  
`items` _VirtualMachineBackupRequest array_ |   
  
### VirtualMachineBackupRequestSpec

Defines the desired state of `VirtualMachineBackupRequest`.

_Appears in:_ \- VirtualMachineBackupRequest

Field | Description  
---|---  
`virtualMachineBackupPlanTemplate` _string_ | The name of the `VirtualMachineBackupPlanTemplate` resource used to generate a `VirtualMachineBackupPlan`. Re-uses the pre-existing `VirtualMachineBackupPlan` made from this template, if there is one. The `VirtualMachineBackupPlanTemplate` must live in the same `namespace` as this request. Specify **only one** of either `VirtualMachineBackupPlanTemplate` OR `VirtualMachineBackupPlan`.  
`virtualMachineBackupPlan` _string_ | The virtual machine backup plan which this request uses for adhoc request with backup scope VirtualMachine and VirtualMachineDisk fields should be omitted when this field is provided The `VirtualMachineBackupPlan` must live in the same `namespace` as this request.  
`virtualMachine` _string_ | The `VirtualMachine` that is being backed up. This is used with the `VirtualMachineBackupPlanTemplate` to automatically generate a `VirtualMachineBackupPlan` if one does not exist. Specify **only one** of either `VirtualMachine` OR `VirtualMachineDisk`. When `virtualMachine` is specified, the backup strategy is always `ProvisionerSpecific`.  
`virtualMachineDisk` _string_ | The `VirtualMachineDisk` being backed-up. This is used with `VirtualMachineBackupPlanTemplate` to automatically generate a `VirtualMachineBackupPlan` if one does not exist. When `virtualMachineDisk` is specified to be backed-up, the backup strategy is `SnapshotOnly`. Specify **only one** of either `VirtualMachine` OR `VirtualMachineDisk`.  
`virtualMachineBackupName` _string_ | The name of the `VirtualMachineBackup` to be created. The backup is always created in the same namespace as the request.  
  
### VirtualMachineBackupRequestStatus

Defines the observed state of VirtualMachineBackupRequest.

_Appears in:_ \- VirtualMachineBackupRequest

Field | Description  
---|---  
`timeToExpire` _[Time](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.25/#time-v1-meta)_ | When this ephemeral resource will be deleted.  
`statusField` _StatusFields_ | Describes the observed state of the VirtualMachineBackupRequest  
  
### VirtualMachineBackupScope

Defines the scope of resources for the `VirtualMachineBackupPlan` to capture.

_Appears in:_ \- VirtualMachineBackupConfig

Field | Description  
---|---  
`selectedVirtualMachines` _VirtualMachineResourceConfig array_ | Specifies the VMs for the `VirtualMachineBackupPlan` to capture.  
`selectedVirtualMachineDisks` _VirtualMachineResourceConfig array_ | Specifies the disks for this `VirtualMachineBackupPlan` to capture.  
`vmResourceLabelSelector` _object (keys:string, values:string)_ | Specifies the label(s) selecting one/multiple VM or VM disk resources in same namespace as backup plan  
  
### VirtualMachineBackupSpec

Defines the desired state of `VirtualMachineBackup`.

_Appears in:_ \- VirtualMachineBackup

Field | Description  
---|---  
`virtualMachineBackupPlan` _string_ | The name of the `VirtualMachineBackupPlan` from which this `VirtualMachineBackup` was created. This `VirtualMachineBackupPlan` exists in the same `namespace` as the `VirtualMachineBackupPlan`.  
`backupConfig` _VirtualMachineBackupConfig_ | Defines the configuration and scope of the backup.  
  
### VirtualMachineBackupStatus

Defines the observed state of a `VirtualMachineBackup`.

_Appears in:_ \- VirtualMachineBackup

Field | Description  
---|---  
`backup` _string_ | The name of the underlying backup which this `VirtualMachineBackup` references. The backup must be in the same `namespace` as this VM backup, used in GDC air-gapped Org v1 Architecture.  
`backupStatus` _BackupStatus_ | The status of the underlying backup(s) which this `VirtualMachineBackup` references, used in GDC air-gapped Org v1 Architecture.  
`configBackup` _string_ | The name of the underlying Config Backup which this `VirtualMachineBackup` references. Config refers to VM and VM Disk. The config backup must be in the same `namespace` as this VM backup, used in GDC air-gapped Org v2 Architecture.  
`configBackupStatus` _BackupStatus_ | The status of the underlying config backup which this `VirtualMachineBackup` references, used in GDC air-gapped Org v2 Architecture.  
`volumeBackup` _string_ | The name of the underlying Volume Backup which this `VirtualMachineBackup` references. The volume backup must be in the same `namespace` as this VM backup, used in GDC air-gapped Org v2 Architecture.  
`volumeBackupStatus` _BackupStatus_ | The status of the underlying volume backup which this `VirtualMachineBackup` references, used in GDC air-gapped Org v2 Architecture.  
`backedUpVirtualMachines` _string array_ | Lists the names of all VMs that are included in this backup.  
`backedUpVirtualMachineDisks` _string array_ | Lists the names of all the VM disks that are included in this backup. If this backup is a disk snapshot, this is a list of VM disks that you provide. If this is a VM backup, it is the list of the disks which back that VM.  
  
### VirtualMachineDeleteBackupRequest

The Schema for the `VirtualMachineDeleteBackupRequests` API.

_Appears in:_ \- VirtualMachineDeleteBackupRequestList

Field | Description  
---|---  
`apiVersion` _string_ | `virtualmachine.gdc.goog/v1`  
`kind` _string_ | `VirtualMachineDeleteBackupRequest`  
`metadata` _[ObjectMeta](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.25/#objectmeta-v1-meta)_ | Refer to Kubernetes API documentation for fields of `metadata`.  
`spec` _VirtualMachineDeleteBackupRequestSpec_ |   
`status` _VirtualMachineDeleteBackupRequestStatus_ |   
  
### VirtualMachineDeleteBackupRequestList

Contains a list of `VirtualMachineDeleteBackupRequest`.

Field | Description  
---|---  
`apiVersion` _string_ | `virtualmachine.gdc.goog/v1`  
`kind` _string_ | `VirtualMachineDeleteBackupRequestList`  
`metadata` _[ListMeta](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.25/#listmeta-v1-meta)_ | Refer to Kubernetes API documentation for fields of `metadata`.  
`items` _VirtualMachineDeleteBackupRequest array_ |   
  
### VirtualMachineDeleteBackupRequestSpec

Defines the desired state of `VirtualMachineDeleteBackupRequest`.

_Appears in:_ \- VirtualMachineDeleteBackupRequest

Field | Description  
---|---  
`virtualMachineBackupRef` _[LocalObjectReference](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.25/#localobjectreference-v1-core)_ | The name of the `VirtualMachineBackup` to delete. This request is always created in the same `namespace` as the backup.  
  
### VirtualMachineDeleteBackupRequestStatus

Defines the observed state of `VirtualMachineDeleteBackupRequest`.

_Appears in:_ \- VirtualMachineDeleteBackupRequest

Field | Description  
---|---  
`timeToExpire` _[Time](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.25/#time-v1-meta)_ | Defines the time to delete this ephemeral resource.  
`statusField` _StatusFields_ | Describes the observed state of the `VirtualMachineDeleteBackupRequest`.  
  
### VirtualMachineDisk

Schema for the virtualmachinedisks API.

_Appears in:_ \- VirtualMachineDiskList

Field | Description  
---|---  
`apiVersion` _string_ | `virtualmachine.gdc.goog/v1`  
`kind` _string_ | `VirtualMachineDisk`  
`metadata` _[ObjectMeta](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.25/#objectmeta-v1-meta)_ | Refer to Kubernetes API documentation for fields of `metadata`.  
`spec` _VirtualMachineDiskSpec_ |   
`status` _VirtualMachineDiskStatus_ |   
  
### VirtualMachineDiskFilterOptions

Specifies the filter options for restoring disks.

_Appears in:_ \- FilterSpec

Field | Description  
---|---  
`allDisks` _boolean_ | Specifies that all disks from VirtualMachineBackup needs to be restored.  
  
### VirtualMachineDiskList

Contains a list of VirtualMachineDisk.

Field | Description  
---|---  
`apiVersion` _string_ | `virtualmachine.gdc.goog/v1`  
`kind` _string_ | `VirtualMachineDiskList`  
`metadata` _[ListMeta](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.25/#listmeta-v1-meta)_ | Refer to Kubernetes API documentation for fields of `metadata`.  
`items` _VirtualMachineDisk array_ |   
  
### VirtualMachineDiskSpec

Defines the desired state of `VirtualMachineDisk`.

_Appears in:_ \- VirtualMachineDisk

Field | Description  
---|---  
`source` _DiskSource_ | Specifies the source from which the disk contents are populated. If this field is omitted a blank disk gets provisioned.  
`size` _Quantity_ | Specifies the size of the disk: 5GiB, 600MiB, and so on. Size must be specified for a blank disk. For disks from other sources, the size depends on the source. For image source, the size is optional and is inferred as being equivalent to `Image.spec.minimumDiskSize`. If the size is specified it has to be greater than the `Image.spec.minimumDiskSize`.  
`type` _DiskType_ | Specifies the type of the disk. Defaults to `Standard`. In GDC air-gapped, supported types are: `Standard`, `Local`. In GDC connected, supported types are: `Standard`.  
  
### VirtualMachineDiskStatus

Defines the observed state of VirtualMachineDisk.

_Appears in:_ \- VirtualMachineDisk

Field | Description  
---|---  
`phase` _VirtualMachineDiskPhase_ | The current phase of the Disk.  
`progress` _VirtualMachineDiskProgress_ | Progress is the current progress of the Disk provision. Value is between 0 and 100 inclusive, N/A if not available.  
`size` _Quantity_ | The current size of the disk.  
`conditions` _[Condition](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.25/#condition-v1-meta) array_ | The latest observations of the `VirtualMachineDisk` state.  
`virtualMachineAttachments` _VirtualMachineAttachment array_ | The list of `VirtualMachine` instances to which the `VirtualMachineDisk` is attached.  
`replicationStatus` _DiskReplicationStatus_ | The status of disk replication.  
`provisionTime` _[Duration](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.25/#duration-v1-meta)_ | The time taken to provision the `VirtualMachineDisk` and to reach a `Ready` state. The time taken to provision the `VirtualMachineDisk` and to reach a `Ready` state. For example, this is the time spent downloading an image, and so on.  
`errors` _VMMError array_ | A list of any errors that occurred during the reconciliation of this resource.  
  
### VirtualMachineExternalAccess

Represents the request of accessing the external VRF for a VirtualMachine.

_Appears in:_ \- VirtualMachineExternalAccessList

Field | Description  
---|---  
`apiVersion` _string_ | `virtualmachine.gdc.goog/v1`  
`kind` _string_ | `VirtualMachineExternalAccess`  
`metadata` _[ObjectMeta](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.25/#objectmeta-v1-meta)_ | Refer to Kubernetes API documentation for fields of `metadata`.  
`spec` _VirtualMachineExternalAccessSpec_ |   
`status` _VirtualMachineExternalAccessStatus_ |   
  
### VirtualMachineExternalAccessList

Field | Description  
---|---  
`apiVersion` _string_ | `virtualmachine.gdc.goog/v1`  
`kind` _string_ | `VirtualMachineExternalAccessList`  
`metadata` _[ListMeta](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.25/#listmeta-v1-meta)_ | Refer to Kubernetes API documentation for fields of `metadata`.  
`items` _VirtualMachineExternalAccess array_ |   
  
### VirtualMachineExternalAccessSpec

Defines the specification of the `VirtualMachineExternalAccess` object.

_Appears in:_ \- VirtualMachineExternalAccess

Field | Description  
---|---  
`enabled` _boolean_ | Specifies whether the external vrf is accessible for the VirtualMachine.  
`ports` _ServicePort array_ | The list of ports that are exposed by the VirtualMachine ingress service.  
  
### VirtualMachineExternalAccessStatus

Defines the observed state of the `VirtualMachineExternalAccess` object.

_Appears in:_ \- VirtualMachineExternalAccess

Field | Description  
---|---  
`ingressIP` _string_ | IngressIP specifies the IP address on the VirtualMachine ingress service.  
`egressIP` _string_ | EgressIP specifies the IP address on the egress NAT which is used by the VirtualMachine.  
`conditions` _[Condition](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.25/#condition-v1-meta) array_ | Details of observed state.  
`errors` _VMMError array_ | A list of any errors that occurred during the reconciliation of this resource.  
  
### VirtualMachineImage

Represents the disk image that can be used on virtual machine.

_Appears in:_ \- VirtualMachineImageList

Field | Description  
---|---  
`apiVersion` _string_ | `virtualmachine.gdc.goog/v1`  
`kind` _string_ | `VirtualMachineImage`  
`metadata` _[ObjectMeta](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.25/#objectmeta-v1-meta)_ | Refer to Kubernetes API documentation for fields of `metadata`.  
`spec` _VirtualMachineImageSpec_ |   
`status` _VirtualMachineImageStatus_ |   
  
### VirtualMachineImageImport

Represents the operation to import and convert VM resources that contain data; for example, to import and convert 'VirtualMachineDisk`into a`VirtualMachineImage`.

_Appears in:_ \- VirtualMachineImageImportList

Field | Description  
---|---  
`apiVersion` _string_ | `virtualmachine.gdc.goog/v1`  
`kind` _string_ | `VirtualMachineImageImport`  
`metadata` _[ObjectMeta](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.25/#objectmeta-v1-meta)_ | Refer to Kubernetes API documentation for fields of `metadata`.  
`spec` _VirtualMachineImageImportSpec_ |   
`status` _VirtualMachineImageImportStatus_ |   
  
### VirtualMachineImageImportList

A list of `VirtualMachineImageImport` objects.

Field | Description  
---|---  
`apiVersion` _string_ | `virtualmachine.gdc.goog/v1`  
`kind` _string_ | `VirtualMachineImageImportList`  
`metadata` _[ListMeta](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.25/#listmeta-v1-meta)_ | Refer to Kubernetes API documentation for fields of `metadata`.  
`items` _VirtualMachineImageImport array_ |   
  
### VirtualMachineImageImportSpec

Specifies the source and metadata for the image that you want to create.

_Appears in:_ \- VirtualMachineImageImport

Field | Description  
---|---  
`source` _ImageSourceReference_ | Refers to the resource from which contents are imported. The source must be from the same namespace.  
`destination` _ImageDestinationReference_ | Refers to the resource to which contents are imported. Only supported in GDC Connected deployments. This field is required if the specified `ImageSourceReference` is `GCS`.  
`imageMetadata` _ImageMetadataInput_ | Specifies the properties of the `VirtualMachineImage` you want to create.  
`prepareImage` _boolean_ | Specifies whether to prepare this image for a GDC air-gapped deployment with a value to, for example, install the required packages. If this is not specified, preparation occurs only if the image is from object storage.  
`prepareOptions` _ImagePrepareOptions_ | These are the options for image preparation. This is only valid when `prepareImage` is `true`.  
  
### VirtualMachineImageImportStatus

Provides the image import status.

_Appears in:_ \- VirtualMachineImageImport

Field | Description  
---|---  
`conditions` _[Condition](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.25/#condition-v1-meta) array_ | Provide the `Ready` status of the import progress.  
`imageName` _string_ | Refers to the `VirtualMachineImage` once successfully created. The image is in the same namespace as the image import.  
`errors` _VMMError array_ | A list of any errors that occurred during the reconciliation of this resource.  
  
### VirtualMachineImageList

Contains a list of `VirtualMachineImage` objects.

Field | Description  
---|---  
`apiVersion` _string_ | `virtualmachine.gdc.goog/v1`  
`kind` _string_ | `VirtualMachineImageList`  
`metadata` _[ListMeta](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.25/#listmeta-v1-meta)_ | Refer to Kubernetes API documentation for fields of `metadata`.  
`items` _VirtualMachineImage array_ |   
  
### VirtualMachineImageSpec

Defines the specification of the virtual machine image.

_Appears in:_ \- VirtualMachineImage

Field | Description  
---|---  
`operatingSystem` _OperatingSystemSpec_ | The details of the OS.  
`minimumDiskSize` _Quantity_ | The minimum size of the disk the image can be applied to. This specifies only the recommended size for the future disks that are created from this image. It does not represent the size of the Image itself.  
`gcs` _GCSReference_ | Refers to the GCS resource from which image are stored.  
  
### VirtualMachineImageStatus

Contains the observed state of the `VirtualMachineImage` object.

_Appears in:_ \- VirtualMachineImage

Field | Description  
---|---  
`conditions` _[Condition](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.25/#condition-v1-meta) array_ | The conditions of the virtual machine image.  
`errors` _VMMError array_ | A list of any errors that occurred during the reconciliation of this resource.  
`storageLocation` _string_ | The zone where this virtual machine image is stored.  
  
### VirtualMachineList

Contains a list of `VirtualMachine` objects.

Field | Description  
---|---  
`apiVersion` _string_ | `virtualmachine.gdc.goog/v1`  
`kind` _string_ | `VirtualMachineList`  
`metadata` _[ListMeta](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.25/#listmeta-v1-meta)_ | Refer to Kubernetes API documentation for fields of `metadata`.  
`items` _VirtualMachine array_ |   
  
### VirtualMachinePasswordResetRequest

Represents a password reset request for a given VM.

_Appears in:_ \- VirtualMachinePasswordResetRequestList

Field | Description  
---|---  
`apiVersion` _string_ | `virtualmachine.gdc.goog/v1`  
`kind` _string_ | `VirtualMachinePasswordResetRequest`  
`metadata` _[ObjectMeta](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.25/#objectmeta-v1-meta)_ | Refer to Kubernetes API documentation for fields of `metadata`.  
`spec` _VirtualMachinePasswordResetRequestSpec_ |   
`status` _VirtualMachinePasswordResetRequestStatus_ |   
  
### VirtualMachinePasswordResetRequestList

Contains a list of `VirtualMachinePasswordResetRequest` resources.

Field | Description  
---|---  
`apiVersion` _string_ | `virtualmachine.gdc.goog/v1`  
`kind` _string_ | `VirtualMachinePasswordResetRequestList`  
`metadata` _[ListMeta](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.25/#listmeta-v1-meta)_ | Refer to Kubernetes API documentation for fields of `metadata`.  
`items` _VirtualMachinePasswordResetRequest array_ |   
  
### VirtualMachinePasswordResetRequestSpec

Defines the `VirtualMachinePasswordResetRequest` specification.

_Appears in:_ \- VirtualMachinePasswordResetRequest

Field | Description  
---|---  
`vmName` _string_ | The name of the VM to request a password reset. This field is immutable and cannot be updated after creating a password reset request.  
`user` _string_ | The name of the user to perform the password reset for a specified VM. This field is immutable and cannot be updated after creating a password reset request.  
`publicKey` _string_ | The public key to encrypt the new password for a VM. This field is immutable and cannot be updated after creating a password reset request.  
  
### VirtualMachinePasswordResetRequestState

_Underlying type:_ `string` Defines the state of a `VirtualMachinePasswordResetRequest` resource.

_Appears in:_ \- VirtualMachinePasswordResetRequestStatus

### VirtualMachinePasswordResetRequestStatus

Describes the status of the `VirtualMachinePasswordResetRequest` resource.

_Appears in:_ \- VirtualMachinePasswordResetRequest

Field | Description  
---|---  
`state` _VirtualMachinePasswordResetRequestState_ | The state of the `VirtualMachinePasswordResetRequest` resource.  
`reason` _string_ | The reason for the current status of the resource.  
`message` _string_ | A field that provides additional information for the current status.  
`processedAt` _[Time](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.25/#time-v1-meta)_ | A field that specifies the time when the request processed.  
`encryptedPassword` _string_ | The new password encrypted using the public key provided in the request and encoded using base64. To decrypt the password, use base64 to decode the string and decrypt the result using RSA decryption.  
`errors` _VMMError array_ | A list of any errors that occurred during the reconciliation of this resource.  
  
### VirtualMachineProvisionTime

Tracks the VirtualMachine provision time.

_Appears in:_ \- VirtualMachineStatus

Field | Description  
---|---  
`initProvisionTime` _[Duration](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.25/#duration-v1-meta)_ | Time taken for the first VM provision. i.e. Time taken from the object being created till the VM is in running status.  
`lastProvisionTime` _[Duration](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.25/#duration-v1-meta)_ | Time taken for the most recent VM provision. It can be equal to InitProvisionTime if the VM is only being provisioned once.  
  
### VirtualMachineResourceConfig

Specifies a VM resource and additional parameters for backing up that resource.

_Appears in:_ \- FilterSpec \- VirtualMachineBackupScope

Field | Description  
---|---  
`resourceName` _string_ | The name of the resource being backed up. It must exist in the same `namespace` as the plan.  
  
### VirtualMachineRestore

The Schema for the VirtualMachineRestores API.

_Appears in:_ \- VirtualMachineRestoreList

Field | Description  
---|---  
`apiVersion` _string_ | `virtualmachine.gdc.goog/v1`  
`kind` _string_ | `VirtualMachineRestore`  
`metadata` _[ObjectMeta](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.25/#objectmeta-v1-meta)_ | Refer to Kubernetes API documentation for fields of `metadata`.  
`spec` _VirtualMachineRestoreSpec_ |   
`status` _VirtualMachineRestoreStatus_ |   
  
### VirtualMachineRestoreList

Contains a list of VirtualMachineRestore.

Field | Description  
---|---  
`apiVersion` _string_ | `virtualmachine.gdc.goog/v1`  
`kind` _string_ | `VirtualMachineRestoreList`  
`metadata` _[ListMeta](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.25/#listmeta-v1-meta)_ | Refer to Kubernetes API documentation for fields of `metadata`.  
`items` _VirtualMachineRestore array_ |   
  
### VirtualMachineRestoreRequest

The Schema for the VirtualMachineRestoreRequests API.

_Appears in:_ \- VirtualMachineRestoreRequestList

Field | Description  
---|---  
`apiVersion` _string_ | `virtualmachine.gdc.goog/v1`  
`kind` _string_ | `VirtualMachineRestoreRequest`  
`metadata` _[ObjectMeta](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.25/#objectmeta-v1-meta)_ | Refer to Kubernetes API documentation for fields of `metadata`.  
`spec` _VirtualMachineRestoreRequestSpec_ |   
`status` _VirtualMachineRestoreRequestStatus_ |   
  
### VirtualMachineRestoreRequestList

Contains a list of VirtualMachineRestoreRequest.

Field | Description  
---|---  
`apiVersion` _string_ | `virtualmachine.gdc.goog/v1`  
`kind` _string_ | `VirtualMachineRestoreRequestList`  
`metadata` _[ListMeta](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.25/#listmeta-v1-meta)_ | Refer to Kubernetes API documentation for fields of `metadata`.  
`items` _VirtualMachineRestoreRequest array_ |   
  
### VirtualMachineRestoreRequestSpec

Defines the desired state of `VirtualMachineRestoreRequest`.

_Appears in:_ \- VirtualMachineRestoreRequest

Field | Description  
---|---  
`virtualMachineBackup` _string_ | The name of the VM backup that to restore. The `VirtualMachineBackup` resides in the same `namespace` as does this `VirtualMachineRestoreRequest`.  
`restoreName` _string_ | The name given to the `VirtualMachineRestore` resource created.  
`restoredResourceName` _string_ | The prefix given to the resources which are restored by `VirtualMachineBackup`. The name of the restored resource would be the prefix + name of backed up resource.  
`restoredResourceDescription` _string_ | The description given to the newly created resource.  
`filter` _FilterSpec_ | The filters that can be used to refine the VM resource selection during the Restore.  
  
### VirtualMachineRestoreRequestStatus

Defines the observed state of `VirtualMachineRestoreRequest`.

_Appears in:_ \- VirtualMachineRestoreRequest

Field | Description  
---|---  
`timeToExpire` _[Time](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.25/#time-v1-meta)_ | When this ephemeral resource will be deleted.  
`statusField` _StatusFields_ | Describes the observed state of the `VirtualMachineRestoreRequest`.  
  
### VirtualMachineRestoreSpec

Defines the desired state of `VirtualMachineRestore`.

_Appears in:_ \- VirtualMachineRestore

Field | Description  
---|---  
`virtualMachineBackup` _string_ | The name of the VM backup that this `VirtualMachineRestore` is restoring. The `VirtualMachineBackup` is in the same `namespace` as this `VirtualMachineRestore`.  
`targetVirtualMachines` _string array_ | The list of all VMs. created when the underlying restore is successful.  
`targetVirtualMachineDisks` _string array_ | The list of all VM disks. created when the underlying restore is successful.  
  
### VirtualMachineRestoreStatus

Defines the observed state of `VirtualMachineRestore`.

_Appears in:_ \- VirtualMachineRestore

Field | Description  
---|---  
`restore` _string_ | The name of the underlying restore which this `VirtualMachineRestore` references. The restore must be in the same `namespace` as this VM backup, used in GDC air-gapped Org v1 Architecture.  
`restoreStatus` _RestoreStatus_ | The status of the underlying restore which this `VirtualMachineRestore` references. Used in GDC air-gapped Org v1 Architecture.  
`configRestore` _string_ | The name of the underlying Config Restore which this `VirtualMachineRestore` references. Config refers to VM and VM Disk. The config restore must be in the same `namespace` as this VM Restore, used in GDC air-gapped Org v2 Architecture.  
`configRestoreStatus` _RestoreStatus_ | The status of the underlying config restore which this `VirtualMachineRestore` references, used in GDC air-gapped Org v2 Architecture.  
`volumeRestore` _string_ | The name of the underlying Volume Restore which this `VirtualMachineRestore` references. The volume restore must be in the same `namespace` as this VM Restore, used in GDC air-gapped Org v2 Architecture.  
`volumeRestoreStatus` _RestoreStatus_ | The status of the underlying volume restore which this `VirtualMachineRestore` references, used in GDC air-gapped Org v2 Architecture.  
  
### VirtualMachineSpec

Defines the specification of the Virtual Machine.

_Appears in:_ \- VirtualMachine

Field | Description  
---|---  
`runningState` _VirtualMachineRunningState_ | Indicates the requested running state of the VirtualMachine. Defaults to Running.  
`disks` _DiskAttachment array_ | Specifies the list of disks attached to this vm. There must be exactly one boot disk. Changes to disk attachments require a reboot to take effect.  
`compute` _Compute_ | Specifies the CPU and Memory of the VM. CPU and Memory can be defined directly or through the VirtualMachineType. Changes to Compute require a reboot to take effect. Compute is immutable when the VM is in `Unknown` state.  
`startupScripts` _StartupScript array_ | Specifies the list of startup scripts for the VM. Linux VMs must have `cloud-init` installed for `StartupScripts` to take effect. The scripts are executed in alphabetical order, based on the name of each startup script. In Windows VMs the type of script impacts the order of execution. Scripts are executed in the order ps1, bat, cmd. If two scripts are of the same type they are executed in alphabetical order, based on the name.  
`guestEnvironment` _GuestEnvironment_ | Specifies the VM's guest environment configuration. If the field is nil the `enable` field in `AccessManagement` is `true` by default. Otherwise, the non-nil configuration for each sub-feature inside the structure overrides the default configuration of the sub-feature.  
`firmware` _Firmware_ | Specifies the VM initialization options at boot time.  
`shieldConfig` _ShieldConfig_ | Specifies the VM's security-related configurations.  
`network` _NetworkSpec_ | Specifies the network configuration.  
  
### VirtualMachineStatus

Contains the observed state of the Virtual Machine.

_Appears in:_ \- VirtualMachine

Field | Description  
---|---  
`state` _VirtualMachineState_ | Observed state of the VM.  
`reason` _VirtualMachineStateReason_ | Reason why the VM is in the observed state. Populated if applicable for the observed state.  
`message` _string_ | Additional details about the state of the VM.  
`network` _NetworkStatus_ | Status of the VM networks.  
`conditions` _[Condition](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.25/#condition-v1-meta) array_ | Details of observed state.  
`stateTransitionTime` _object (keys:VirtualMachineState, values:[Time](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.25/#time-v1-meta))_ | Last transition time of each state.  
`provisionTime` _VirtualMachineProvisionTime_ | Time taken to provision the VM.  
`errors` _VMMError array_ | A list of any errors that occurred during the reconciliation of this resource.  
  
### VirtualMachineType

Defines the CPU and Memory resource of a VM.

_Appears in:_ \- VirtualMachineTypeList

Field | Description  
---|---  
`apiVersion` _string_ | `virtualmachine.gdc.goog/v1`  
`kind` _string_ | `VirtualMachineType`  
`metadata` _[ObjectMeta](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.25/#objectmeta-v1-meta)_ | Refer to Kubernetes API documentation for fields of `metadata`.  
`spec` _VirtualMachineTypeSpec_ |   
`status` _VirtualMachineTypeStatus_ |   
  
### VirtualMachineTypeList

VirtualMachineTypeList contains a list of VirtualMachineType.

Field | Description  
---|---  
`apiVersion` _string_ | `virtualmachine.gdc.goog/v1`  
`kind` _string_ | `VirtualMachineTypeList`  
`metadata` _[ListMeta](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.25/#listmeta-v1-meta)_ | Refer to Kubernetes API documentation for fields of `metadata`.  
`items` _VirtualMachineType array_ |   
  
### VirtualMachineTypeSpec

Defines the configurations of a `VirtualMachineType`.

_Appears in:_ \- VirtualMachineType

Field | Description  
---|---  
`vcpus` _integer_ | Specifies the number of VCPUs that are available to the instance. Specify `vcpus` as an integer that is a multiple of 2, between 2 and 128, inclusive.  
`memory` _Quantity_ | Specifies the amount of physical memory available to the instance. `memory` must have a value that is between 1G and 400G, inclusive.  
  
### VirtualMachineTypeStatus

_Appears in:_ \- VirtualMachineType

Field | Description  
---|---  
`supported` _boolean_ | Specifies if given vmtype is supported or not by the underlying hardware  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
