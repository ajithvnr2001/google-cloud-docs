---
url: https://docs.cloud.google.com/config-connector/docs/reference/resource-docs/compute/computeinstancetemplate/
title: ComputeInstanceTemplate \u00a0|\u00a0 Config Connector \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T16:41:39.314704+00:00
---

# ComputeInstanceTemplate  |  Config Connector  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/config-connector/docs/reference/resource-docs/compute/computeinstancetemplate/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Access and resource management ](https://docs.cloud.google.com/docs/access-resources)
  * [ Config Connector ](https://docs.cloud.google.com/config-connector/docs)
  * [ API and reference ](https://docs.cloud.google.com/config-connector/docs/reference/overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# ComputeInstanceTemplate

**Property** | **Value**  
---|---  
Google Cloud Service Name | Compute Engine  
Google Cloud Service Documentation | [/compute/docs/](https://docs.cloud.google.com/compute/docs)  
Google Cloud REST Resource Name | v1.instancetemplates  
Google Cloud REST Resource Documentation | [/compute/docs/reference/rest/v1/instanceTemplates](https://docs.cloud.google.com/compute/docs/reference/rest/v1/instanceTemplates)  
Config Connector Resource Short Names | computeinstancetemplate  
gcpcomputeinstancetemplate  
gcpcomputeinstancetemplates  
Config Connector Service Name | compute.googleapis.com  
Config Connector Resource Fully Qualified Name | computeinstancetemplates.compute.cnrm.cloud.google.com  
Can Be Referenced by IAMPolicy/IAMPolicyMember | No  
Config Connector Default Average Reconcile Interval In Seconds | 600  
  
## Custom Resource Definition Properties

### Annotations

Fields  
---  
`cnrm.cloud.google.com/project-id`  
  
### Spec

#### Schema
    
    
    advancedMachineFeatures:
      enableNestedVirtualization: boolean
      threadsPerCore: integer
      visibleCoreCount: integer
    canIpForward: boolean
    confidentialInstanceConfig:
      enableConfidentialCompute: boolean
    description: string
    disk:
    - autoDelete: boolean
      boot: boolean
      deviceName: string
      diskEncryptionKey:
        kmsKeyRef:
          external: string
          name: string
          namespace: string
      diskName: string
      diskSizeGb: integer
      diskType: string
      interface: string
      labels:
        string: string
      mode: string
      provisionedIops: integer
      resourcePolicies:
      - external: string
        name: string
        namespace: string
      sourceDiskRef:
        external: string
        name: string
        namespace: string
      sourceImageEncryptionKey:
        kmsKeySelfLinkRef:
          external: string
          name: string
          namespace: string
        kmsKeyServiceAccountRef:
          external: string
          name: string
          namespace: string
      sourceImageRef:
        external: string
        name: string
        namespace: string
      sourceSnapshotEncryptionKey:
        kmsKeySelfLinkRef:
          external: string
          name: string
          namespace: string
        kmsKeyServiceAccountRef:
          external: string
          name: string
          namespace: string
      sourceSnapshotRef:
        external: string
        name: string
        namespace: string
      type: string
    enableDisplay: boolean
    guestAccelerator:
    - count: integer
      type: string
    instanceDescription: string
    machineType: string
    metadata:
    - key: string
      value: string
    metadataStartupScript: string
    minCpuPlatform: string
    namePrefix: string
    networkInterface:
    - accessConfig:
      - natIpRef:
          external: string
          name: string
          namespace: string
        networkTier: string
        publicPtrDomainName: string
      aliasIpRange:
      - ipCidrRange: string
        subnetworkRangeName: string
      internalIpv6PrefixLength: integer
      ipv6AccessConfig:
      - externalIpv6: string
        externalIpv6PrefixLength: string
        name: string
        networkTier: string
        publicPtrDomainName: string
      ipv6AccessType: string
      ipv6Address: string
      name: string
      networkAttachment: string
      networkIp: string
      networkRef:
        external: string
        name: string
        namespace: string
      nicType: string
      queueCount: integer
      stackType: string
      subnetworkProject: string
      subnetworkRef:
        external: string
        name: string
        namespace: string
    networkPerformanceConfig:
      totalEgressBandwidthTier: string
    region: string
    reservationAffinity:
      specificReservation:
        key: string
        values:
        - string
      type: string
    resourceID: string
    resourcePolicies:
    - external: string
      name: string
      namespace: string
    scheduling:
      automaticRestart: boolean
      instanceTerminationAction: string
      localSsdRecoveryTimeout:
      - nanos: integer
        seconds: integer
      maintenanceInterval: string
      maxRunDuration:
        nanos: integer
        seconds: integer
      minNodeCpus: integer
      nodeAffinities:
      - value: {}
      onHostMaintenance: string
      preemptible: boolean
      provisioningModel: string
    serviceAccount:
      scopes:
      - string
      serviceAccountRef:
        external: string
        name: string
        namespace: string
    shieldedInstanceConfig:
      enableIntegrityMonitoring: boolean
      enableSecureBoot: boolean
      enableVtpm: boolean
    tags:
    - string
    

Fields  
---  
`advancedMachineFeatures` _Optional_ |  `object` Immutable. Controls for advanced machine-related behavior features.  
`advancedMachineFeatures.enableNestedVirtualization` _Optional_ |  `boolean` Immutable. Whether to enable nested virtualization or not.  
`advancedMachineFeatures.threadsPerCore` _Optional_ |  `integer` Immutable. The number of threads per physical core. To disable simultaneous multithreading (SMT) set this to 1. If unset, the maximum number of threads supported per core by the underlying processor is assumed.  
`advancedMachineFeatures.visibleCoreCount` _Optional_ |  `integer` Immutable. The number of physical cores to expose to an instance. Multiply by the number of threads per core to compute the total number of virtual CPUs to expose to the instance. If unset, the number of cores is inferred from the instance\'s nominal CPU count and the underlying platform\'s SMT width.  
`canIpForward` _Optional_ |  `boolean` Immutable. Whether to allow sending and receiving of packets with non-matching source or destination IPs. This defaults to false.  
`confidentialInstanceConfig` _Optional_ |  `object` Immutable. The Confidential VM config being used by the instance. on_host_maintenance has to be set to TERMINATE or this will fail to create.  
`confidentialInstanceConfig.enableConfidentialCompute` _Required*_ |  `boolean` Immutable. Defines whether the instance should have confidential compute enabled.  
`description` _Optional_ |  `string` Immutable. A brief description of this resource.  
`disk` _Required_ |  `list (object)` Immutable. Disks to attach to instances created from this template. This can be specified multiple times for multiple disks.  
`disk[]` _Required_ |  `object`  
`disk[].autoDelete` _Optional_ |  `boolean` Immutable. Whether or not the disk should be auto-deleted. This defaults to true.  
`disk[].boot` _Optional_ |  `boolean` Immutable. Indicates that this is a boot disk.  
`disk[].deviceName` _Optional_ |  `string` Immutable. A unique device name that is reflected into the /dev/ tree of a Linux operating system running within the instance. If not specified, the server chooses a default device name to apply to this disk.  
`disk[].diskEncryptionKey` _Optional_ |  `object` Immutable. Encrypts or decrypts a disk using a customer-supplied encryption key.  
`disk[].diskEncryptionKey.kmsKeyRef` _Required*_ |  `object`  
`disk[].diskEncryptionKey.kmsKeyRef.external` _Optional_ |  `string` Allowed value: The `selfLink` field of a `KMSCryptoKey` resource.  
`disk[].diskEncryptionKey.kmsKeyRef.name` _Optional_ |  `string` Name of the referent. More info: https://kubernetes.io/docs/concepts/overview/working-with-objects/names/#names  
`disk[].diskEncryptionKey.kmsKeyRef.namespace` _Optional_ |  `string` Namespace of the referent. More info: https://kubernetes.io/docs/concepts/overview/working-with-objects/namespaces/  
`disk[].diskName` _Optional_ |  `string` Immutable. Name of the disk. When not provided, this defaults to the name of the instance.  
`disk[].diskSizeGb` _Optional_ |  `integer` Immutable. The size of the image in gigabytes. If not specified, it will inherit the size of its base image. For SCRATCH disks, the size must be one of 375 or 3000 GB, with a default of 375 GB.  
`disk[].diskType` _Optional_ |  `string` Immutable. The Google Compute Engine disk type. Such as "pd-ssd", "local-ssd", "pd-balanced" or "pd-standard".  
`disk[].interface` _Optional_ |  `string` Immutable. Specifies the disk interface to use for attaching this disk.  
`disk[].labels` _Optional_ |  `map (key: string, value: string)` Immutable. A set of key/value label pairs to assign to disks,.  
`disk[].mode` _Optional_ |  `string` Immutable. The mode in which to attach this disk, either READ_WRITE or READ_ONLY. If you are attaching or creating a boot disk, this must read-write mode.  
`disk[].provisionedIops` _Optional_ |  `integer` Immutable. Indicates how many IOPS to provision for the disk. This sets the number of I/O operations per second that the disk can handle. Values must be between 10,000 and 120,000. For more details, see the [Extreme persistent disk documentation](https://cloud.google.com/compute/docs/disks/extreme-persistent-disk).  
`disk[].resourcePolicies` _Optional_ |  `list (object)`  
`disk[].resourcePolicies[]` _Optional_ |  `object`  
`disk[].resourcePolicies[].external` _Optional_ |  `string` Allowed value: The `selfLink` field of a `ComputeResourcePolicy` resource.  
`disk[].resourcePolicies[].name` _Optional_ |  `string` Name of the referent. More info: https://kubernetes.io/docs/concepts/overview/working-with-objects/names/#names  
`disk[].resourcePolicies[].namespace` _Optional_ |  `string` Namespace of the referent. More info: https://kubernetes.io/docs/concepts/overview/working-with-objects/namespaces/  
`disk[].sourceDiskRef` _Optional_ |  `object`  
`disk[].sourceDiskRef.external` _Optional_ |  `string` Allowed value: The `name` field of a `ComputeDisk` resource.  
`disk[].sourceDiskRef.name` _Optional_ |  `string` Name of the referent. More info: https://kubernetes.io/docs/concepts/overview/working-with-objects/names/#names  
`disk[].sourceDiskRef.namespace` _Optional_ |  `string` Namespace of the referent. More info: https://kubernetes.io/docs/concepts/overview/working-with-objects/namespaces/  
`disk[].sourceImageEncryptionKey` _Optional_ |  `object` Immutable. The customer-supplied encryption key of the source image. Required if the source image is protected by a customer-supplied encryption key. Instance templates do not store customer-supplied encryption keys, so you cannot create disks for instances in a managed instance group if the source images are encrypted with your own keys.  
`disk[].sourceImageEncryptionKey.kmsKeySelfLinkRef` _Required*_ |  `object` The self link of the encryption key that is stored in Google Cloud KMS.  
`disk[].sourceImageEncryptionKey.kmsKeySelfLinkRef.external` _Optional_ |  `string` Allowed value: The `selfLink` field of a `KMSCryptoKey` resource.  
`disk[].sourceImageEncryptionKey.kmsKeySelfLinkRef.name` _Optional_ |  `string` Name of the referent. More info: https://kubernetes.io/docs/concepts/overview/working-with-objects/names/#names  
`disk[].sourceImageEncryptionKey.kmsKeySelfLinkRef.namespace` _Optional_ |  `string` Namespace of the referent. More info: https://kubernetes.io/docs/concepts/overview/working-with-objects/namespaces/  
`disk[].sourceImageEncryptionKey.kmsKeyServiceAccountRef` _Optional_ |  `object` The service account being used for the encryption request for the given KMS key. If absent, the Compute Engine default service account is used.  
`disk[].sourceImageEncryptionKey.kmsKeyServiceAccountRef.external` _Optional_ |  `string` Allowed value: The `email` field of an `IAMServiceAccount` resource.  
`disk[].sourceImageEncryptionKey.kmsKeyServiceAccountRef.name` _Optional_ |  `string` Name of the referent. More info: https://kubernetes.io/docs/concepts/overview/working-with-objects/names/#names  
`disk[].sourceImageEncryptionKey.kmsKeyServiceAccountRef.namespace` _Optional_ |  `string` Namespace of the referent. More info: https://kubernetes.io/docs/concepts/overview/working-with-objects/namespaces/  
`disk[].sourceImageRef` _Optional_ |  `object`  
`disk[].sourceImageRef.external` _Optional_ |  `string` Allowed value: The `selfLink` field of a `ComputeImage` resource.  
`disk[].sourceImageRef.name` _Optional_ |  `string` Name of the referent. More info: https://kubernetes.io/docs/concepts/overview/working-with-objects/names/#names  
`disk[].sourceImageRef.namespace` _Optional_ |  `string` Namespace of the referent. More info: https://kubernetes.io/docs/concepts/overview/working-with-objects/namespaces/  
`disk[].sourceSnapshotEncryptionKey` _Optional_ |  `object` Immutable. The customer-supplied encryption key of the source snapshot.  
`disk[].sourceSnapshotEncryptionKey.kmsKeySelfLinkRef` _Required*_ |  `object` The self link of the encryption key that is stored in Google Cloud KMS.  
`disk[].sourceSnapshotEncryptionKey.kmsKeySelfLinkRef.external` _Optional_ |  `string` Allowed value: The `selfLink` field of a `KMSCryptoKey` resource.  
`disk[].sourceSnapshotEncryptionKey.kmsKeySelfLinkRef.name` _Optional_ |  `string` Name of the referent. More info: https://kubernetes.io/docs/concepts/overview/working-with-objects/names/#names  
`disk[].sourceSnapshotEncryptionKey.kmsKeySelfLinkRef.namespace` _Optional_ |  `string` Namespace of the referent. More info: https://kubernetes.io/docs/concepts/overview/working-with-objects/namespaces/  
`disk[].sourceSnapshotEncryptionKey.kmsKeyServiceAccountRef` _Optional_ |  `object` The service account being used for the encryption request for the given KMS key. If absent, the Compute Engine default service account is used.  
`disk[].sourceSnapshotEncryptionKey.kmsKeyServiceAccountRef.external` _Optional_ |  `string` Allowed value: The `email` field of an `IAMServiceAccount` resource.  
`disk[].sourceSnapshotEncryptionKey.kmsKeyServiceAccountRef.name` _Optional_ |  `string` Name of the referent. More info: https://kubernetes.io/docs/concepts/overview/working-with-objects/names/#names  
`disk[].sourceSnapshotEncryptionKey.kmsKeyServiceAccountRef.namespace` _Optional_ |  `string` Namespace of the referent. More info: https://kubernetes.io/docs/concepts/overview/working-with-objects/namespaces/  
`disk[].sourceSnapshotRef` _Optional_ |  `object` The source snapshot to create this disk. When creating a new instance, one of initializeParams.sourceSnapshot, initializeParams.sourceImage, or disks.source is required except for local SSD.  
`disk[].sourceSnapshotRef.external` _Optional_ |  `string` Allowed value: The `selfLink` field of a `ComputeSnapshot` resource.  
`disk[].sourceSnapshotRef.name` _Optional_ |  `string` Name of the referent. More info: https://kubernetes.io/docs/concepts/overview/working-with-objects/names/#names  
`disk[].sourceSnapshotRef.namespace` _Optional_ |  `string` Namespace of the referent. More info: https://kubernetes.io/docs/concepts/overview/working-with-objects/namespaces/  
`disk[].type` _Optional_ |  `string` Immutable. The type of Google Compute Engine disk, can be either "SCRATCH" or "PERSISTENT".  
`enableDisplay` _Optional_ |  `boolean` Immutable. Enable Virtual Displays on this instance. Note: allow_stopping_for_update must be set to true in order to update this field.  
`guestAccelerator` _Optional_ |  `list (object)` Immutable. List of the type and count of accelerator cards attached to the instance.  
`guestAccelerator[]` _Optional_ |  `object`  
`guestAccelerator[].count` _Required*_ |  `integer` Immutable. The number of the guest accelerator cards exposed to this instance.  
`guestAccelerator[].type` _Required*_ |  `string` Immutable. The accelerator type resource to expose to this instance. E.g. nvidia-tesla-t4.  
`instanceDescription` _Optional_ |  `string` Immutable. A description of the instance.  
`machineType` _Required_ |  `string` Immutable. The machine type to create. To create a machine with a custom type (such as extended memory), format the value like custom-VCPUS-MEM_IN_MB like custom-6-20480 for 6 vCPU and 20GB of RAM.  
`metadata` _Optional_ |  `list (object)`  
`metadata[]` _Optional_ |  `object`  
`metadata[].key` _Required*_ |  `string`  
`metadata[].value` _Required*_ |  `string`  
`metadataStartupScript` _Optional_ |  `string` Immutable. An alternative to using the startup-script metadata key, mostly to match the compute_instance resource. This replaces the startup-script metadata key on the created instance and thus the two mechanisms are not allowed to be used simultaneously.  
`minCpuPlatform` _Optional_ |  `string` Immutable. Specifies a minimum CPU platform. Applicable values are the friendly names of CPU platforms, such as Intel Haswell or Intel Skylake.  
`namePrefix` _Optional_ |  `string` Immutable. Creates a unique name beginning with the specified prefix. Conflicts with name.  
`networkInterface` _Optional_ |  `list (object)` Immutable. Networks to attach to instances created from this template. This can be specified multiple times for multiple networks.  
`networkInterface[]` _Optional_ |  `object`  
`networkInterface[].accessConfig` _Optional_ |  `list (object)`  
`networkInterface[].accessConfig[]` _Optional_ |  `object`  
`networkInterface[].accessConfig[].natIpRef` _Optional_ |  `object`  
`networkInterface[].accessConfig[].natIpRef.external` _Optional_ |  `string` Allowed value: The `address` field of a `ComputeAddress` resource.  
`networkInterface[].accessConfig[].natIpRef.name` _Optional_ |  `string` Name of the referent. More info: https://kubernetes.io/docs/concepts/overview/working-with-objects/names/#names  
`networkInterface[].accessConfig[].natIpRef.namespace` _Optional_ |  `string` Namespace of the referent. More info: https://kubernetes.io/docs/concepts/overview/working-with-objects/namespaces/  
`networkInterface[].accessConfig[].networkTier` _Optional_ |  `string` Immutable. The networking tier used for configuring this instance template. This field can take the following values: PREMIUM, STANDARD, FIXED_STANDARD. If this field is not specified, it is assumed to be PREMIUM.  
`networkInterface[].accessConfig[].publicPtrDomainName` _Optional_ |  `string` The DNS domain name for the public PTR record.The DNS domain name for the public PTR record.  
`networkInterface[].aliasIpRange` _Optional_ |  `list (object)` Immutable. An array of alias IP ranges for this network interface. Can only be specified for network interfaces on subnet-mode networks.  
`networkInterface[].aliasIpRange[]` _Optional_ |  `object`  
`networkInterface[].aliasIpRange[].ipCidrRange` _Required*_ |  `string` Immutable. The IP CIDR range represented by this alias IP range. This IP CIDR range must belong to the specified subnetwork and cannot contain IP addresses reserved by system or used by other network interfaces. At the time of writing only a netmask (e.g. /24) may be supplied, with a CIDR format resulting in an API error.  
`networkInterface[].aliasIpRange[].subnetworkRangeName` _Optional_ |  `string` Immutable. The subnetwork secondary range name specifying the secondary range from which to allocate the IP CIDR range for this alias IP range. If left unspecified, the primary range of the subnetwork will be used.  
`networkInterface[].internalIpv6PrefixLength` _Optional_ |  `integer` The prefix length of the primary internal IPv6 range.  
`networkInterface[].ipv6AccessConfig` _Optional_ |  `list (object)` An array of IPv6 access configurations for this interface. Currently, only one IPv6 access config, DIRECT_IPV6, is supported. If there is no ipv6AccessConfig specified, then this instance will have no external IPv6 Internet access.  
`networkInterface[].ipv6AccessConfig[]` _Optional_ |  `object`  
`networkInterface[].ipv6AccessConfig[].externalIpv6` _Optional_ |  `string` The first IPv6 address of the external IPv6 range associated with this instance, prefix length is stored in externalIpv6PrefixLength in ipv6AccessConfig. The field is output only, an IPv6 address from a subnetwork associated with the instance will be allocated dynamically.  
`networkInterface[].ipv6AccessConfig[].externalIpv6PrefixLength` _Optional_ |  `string` The prefix length of the external IPv6 range.  
`networkInterface[].ipv6AccessConfig[].name` _Optional_ |  `string` The name of this access configuration.  
`networkInterface[].ipv6AccessConfig[].networkTier` _Required*_ |  `string` The service-level to be provided for IPv6 traffic when the subnet has an external subnet. Only PREMIUM tier is valid for IPv6.  
`networkInterface[].ipv6AccessConfig[].publicPtrDomainName` _Optional_ |  `string` The domain name to be used when creating DNSv6 records for the external IPv6 ranges.  
`networkInterface[].ipv6AccessType` _Optional_ |  `string` One of EXTERNAL, INTERNAL to indicate whether the IP can be accessed from the Internet. This field is always inherited from its subnetwork.  
`networkInterface[].ipv6Address` _Optional_ |  `string` An IPv6 internal network address for this network interface. If not specified, Google Cloud will automatically assign an internal IPv6 address from the instance's subnetwork.  
`networkInterface[].name` _Optional_ |  `string` The name of the network_interface.  
`networkInterface[].networkAttachment` _Optional_ |  `string` Immutable. The URL of the network attachment that this interface should connect to in the following format: projects/{projectNumber}/regions/{region_name}/networkAttachments/{network_attachment_name}.  
`networkInterface[].networkIp` _Optional_ |  `string` Immutable. The private IP address to assign to the instance. If empty, the address will be automatically assigned.  
`networkInterface[].networkRef` _Optional_ |  `object`  
`networkInterface[].networkRef.external` _Optional_ |  `string` Allowed value: The `selfLink` field of a `ComputeNetwork` resource.  
`networkInterface[].networkRef.name` _Optional_ |  `string` Name of the referent. More info: https://kubernetes.io/docs/concepts/overview/working-with-objects/names/#names  
`networkInterface[].networkRef.namespace` _Optional_ |  `string` Namespace of the referent. More info: https://kubernetes.io/docs/concepts/overview/working-with-objects/namespaces/  
`networkInterface[].nicType` _Optional_ |  `string` Immutable. The type of vNIC to be used on this interface. Possible values:GVNIC, VIRTIO_NET.  
`networkInterface[].queueCount` _Optional_ |  `integer` Immutable. The networking queue count that's specified by users for the network interface. Both Rx and Tx queues will be set to this number. It will be empty if not specified.  
`networkInterface[].stackType` _Optional_ |  `string` The stack type for this network interface to identify whether the IPv6 feature is enabled or not. If not specified, IPV4_ONLY will be used.  
`networkInterface[].subnetworkProject` _Optional_ |  `string` Immutable. The ID of the project in which the subnetwork belongs. If it is not provided, the provider project is used.  
`networkInterface[].subnetworkRef` _Optional_ |  `object`  
`networkInterface[].subnetworkRef.external` _Optional_ |  `string` Allowed value: The `selfLink` field of a `ComputeSubnetwork` resource.  
`networkInterface[].subnetworkRef.name` _Optional_ |  `string` Name of the referent. More info: https://kubernetes.io/docs/concepts/overview/working-with-objects/names/#names  
`networkInterface[].subnetworkRef.namespace` _Optional_ |  `string` Namespace of the referent. More info: https://kubernetes.io/docs/concepts/overview/working-with-objects/namespaces/  
`networkPerformanceConfig` _Optional_ |  `object` Immutable. Configures network performance settings for the instance. If not specified, the instance will be created with its default network performance configuration.  
`networkPerformanceConfig.totalEgressBandwidthTier` _Required*_ |  `string` Immutable. The egress bandwidth tier to enable. Possible values:TIER_1, DEFAULT.  
`region` _Optional_ |  `string` Immutable. An instance template is a global resource that is not bound to a zone or a region. However, you can still specify some regional resources in an instance template, which restricts the template to the region where that resource resides. For example, a custom subnetwork resource is tied to a specific region. Defaults to the region of the Provider if no value is given.  
`reservationAffinity` _Optional_ |  `object` Immutable. Specifies the reservations that this instance can consume from.  
`reservationAffinity.specificReservation` _Optional_ |  `object` Immutable. Specifies the label selector for the reservation to use.  
`reservationAffinity.specificReservation.key` _Required*_ |  `string` Immutable. Corresponds to the label key of a reservation resource. To target a SPECIFIC_RESERVATION by name, specify compute.googleapis.com/reservation-name as the key and specify the name of your reservation as the only value.  
`reservationAffinity.specificReservation.values` _Required*_ |  `list (string)` Immutable. Corresponds to the label values of a reservation resource.  
`reservationAffinity.specificReservation.values[]` _Required*_ |  `string`  
`reservationAffinity.type` _Required*_ |  `string` Immutable. The type of reservation from which this instance can consume resources.  
`resourceID` _Optional_ |  `string` Immutable. Optional. The name of the resource. Used for creation and acquisition. When unset, the value of `metadata.name` is used as the default.  
`resourcePolicies` _Optional_ |  `list (object)`  
`resourcePolicies[]` _Optional_ |  `object`  
`resourcePolicies[].external` _Optional_ |  `string` Allowed value: The `selfLink` field of a `ComputeResourcePolicy` resource.  
`resourcePolicies[].name` _Optional_ |  `string` Name of the referent. More info: https://kubernetes.io/docs/concepts/overview/working-with-objects/names/#names  
`resourcePolicies[].namespace` _Optional_ |  `string` Namespace of the referent. More info: https://kubernetes.io/docs/concepts/overview/working-with-objects/namespaces/  
`scheduling` _Optional_ |  `object` Immutable. The scheduling strategy to use.  
`scheduling.automaticRestart` _Optional_ |  `boolean` Immutable. Specifies whether the instance should be automatically restarted if it is terminated by Compute Engine (not terminated by a user). This defaults to true.  
`scheduling.instanceTerminationAction` _Optional_ |  `string` Immutable. Specifies the action GCE should take when SPOT VM is preempted.  
`scheduling.localSsdRecoveryTimeout` _Optional_ |  `list (object)` Specifies the maximum amount of time a Local Ssd Vm should wait while recovery of the Local Ssd state is attempted. Its value should be in between 0 and 168 hours with hour granularity and the default value being 1 hour.  
`scheduling.localSsdRecoveryTimeout[]` _Optional_ |  `object`  
`scheduling.localSsdRecoveryTimeout[].nanos` _Optional_ |  `integer` Immutable. Span of time that's a fraction of a second at nanosecond resolution. Durations less than one second are represented with a 0 seconds field and a positive nanos field. Must be from 0 to 999,999,999 inclusive.  
`scheduling.localSsdRecoveryTimeout[].seconds` _Required*_ |  `integer` Immutable. Span of time at a resolution of a second. Must be from 0 to 315,576,000,000 inclusive.  
`scheduling.maintenanceInterval` _Optional_ |  `string` Specifies the frequency of planned maintenance events. The accepted values are: PERIODIC.  
`scheduling.maxRunDuration` _Optional_ |  `object` Immutable. The timeout for new network connections to hosts.  
`scheduling.maxRunDuration.nanos` _Optional_ |  `integer` Immutable. Span of time that's a fraction of a second at nanosecond resolution. Durations less than one second are represented with a 0 seconds field and a positive nanos field. Must be from 0 to 999,999,999 inclusive.  
`scheduling.maxRunDuration.seconds` _Required*_ |  `integer` Immutable. Span of time at a resolution of a second. Must be from 0 to 315,576,000,000 inclusive.  
`scheduling.minNodeCpus` _Optional_ |  `integer` Minimum number of cpus for the instance.  
`scheduling.nodeAffinities` _Optional_ |  `list (object)`  
`scheduling.nodeAffinities[]` _Optional_ |  `object`  
`scheduling.nodeAffinities[].value` _Optional_ |  `object`  
`scheduling.onHostMaintenance` _Optional_ |  `string` Immutable. Defines the maintenance behavior for this instance.  
`scheduling.preemptible` _Optional_ |  `boolean` Immutable. Allows instance to be preempted. This defaults to false.  
`scheduling.provisioningModel` _Optional_ |  `string` Immutable. Whether the instance is spot. If this is set as SPOT.  
`serviceAccount` _Optional_ |  `object` Immutable. Service account to attach to the instance.  
`serviceAccount.scopes` _Required*_ |  `list (string)` Immutable. A list of service scopes. Both OAuth2 URLs and gcloud short names are supported. To allow full access to all Cloud APIs, use the cloud-platform scope.  
`serviceAccount.scopes[]` _Required*_ |  `string`  
`serviceAccount.serviceAccountRef` _Optional_ |  `object`  
`serviceAccount.serviceAccountRef.external` _Optional_ |  `string` Allowed value: The `email` field of an `IAMServiceAccount` resource.  
`serviceAccount.serviceAccountRef.name` _Optional_ |  `string` Name of the referent. More info: https://kubernetes.io/docs/concepts/overview/working-with-objects/names/#names  
`serviceAccount.serviceAccountRef.namespace` _Optional_ |  `string` Namespace of the referent. More info: https://kubernetes.io/docs/concepts/overview/working-with-objects/namespaces/  
`shieldedInstanceConfig` _Optional_ |  `object` Immutable. Enable Shielded VM on this instance. Shielded VM provides verifiable integrity to prevent against malware and rootkits. Defaults to disabled. Note: shielded_instance_config can only be used with boot images with shielded vm support.  
`shieldedInstanceConfig.enableIntegrityMonitoring` _Optional_ |  `boolean` Immutable. Compare the most recent boot measurements to the integrity policy baseline and return a pair of pass/fail results depending on whether they match or not. Defaults to true.  
`shieldedInstanceConfig.enableSecureBoot` _Optional_ |  `boolean` Immutable. Verify the digital signature of all boot components, and halt the boot process if signature verification fails. Defaults to false.  
`shieldedInstanceConfig.enableVtpm` _Optional_ |  `boolean` Immutable. Use a virtualized trusted platform module, which is a specialized computer chip you can use to encrypt objects like keys and certificates. Defaults to true.  
`tags` _Optional_ |  `list (string)` Immutable. Tags to attach to the instance.  
`tags[]` _Optional_ |  `string`  
  
* Field is required when parent field is specified

### Status

#### Schema
    
    
    conditions:
    - lastTransitionTime: string
      message: string
      reason: string
      status: string
      type: string
    metadataFingerprint: string
    observedGeneration: integer
    selfLink: string
    selfLinkUnique: string
    tagsFingerprint: string
    

Fields  
---  
`conditions` |  `list (object)` Conditions represent the latest available observation of the resource's current state.  
`conditions[]` |  `object`  
`conditions[].lastTransitionTime` |  `string` Last time the condition transitioned from one status to another.  
`conditions[].message` |  `string` Human-readable message indicating details about last transition.  
`conditions[].reason` |  `string` Unique, one-word, CamelCase reason for the condition's last transition.  
`conditions[].status` |  `string` Status is the status of the condition. Can be True, False, Unknown.  
`conditions[].type` |  `string` Type is the type of the condition.  
`metadataFingerprint` |  `string` The unique fingerprint of the metadata.  
`observedGeneration` |  `integer` ObservedGeneration is the generation of the resource that was most recently observed by the Config Connector controller. If this is equal to metadata.generation, then that means that the current reported status reflects the most recent desired state of the resource.  
`selfLink` |  `string` The URI of the created resource.  
`selfLinkUnique` |  `string` A special URI of the created resource that uniquely identifies this instance template.  
`tagsFingerprint` |  `string` The unique fingerprint of the tags.  
  
## Sample YAML(s)

### Typical Use Case
    
    
    # Copyright 2020 Google LLC
    #
    # Licensed under the Apache License, Version 2.0 (the "License");
    # you may not use this file except in compliance with the License.
    # You may obtain a copy of the License at
    #
    #     http://www.apache.org/licenses/LICENSE-2.0
    #
    # Unless required by applicable law or agreed to in writing, software
    # distributed under the License is distributed on an "AS IS" BASIS,
    # WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
    # See the License for the specific language governing permissions and
    # limitations under the License.
    
    apiVersion: compute.cnrm.cloud.google.com/v1beta1
    kind: ComputeInstanceTemplate
    metadata:
      name: instancetemplate-sample
      labels:
        env: "dev"
    spec:
      description: a sample instance template
      tags:
        - foo
        - bar
      instanceDescription: a sample instance created from the sample instance template
      machineType: n1-standard-1
      region: us-west1
      disk:
        - sourceDiskRef:
            name: instancetemplate-dep
          autoDelete: false
          boot: true
        - sourceImageRef:
            name: instancetemplate-dep
          autoDelete: true
          boot: false
          diskName: sample-attached-disk
          deviceName: attachment
          interface: SCSI
          diskType: pd-ssd
          diskSizeGb: 10
          type: PERSISTENT
      networkInterface:
        - networkRef:
            name: instancetemplate-dep
          subnetworkRef:
            name: instancetemplate-dep
          networkIp: "10.2.0.1"
          aliasIpRange:
            - ipCidrRange: /16
              subnetworkRangeName: sub-range
      canIpForward: false
      scheduling:
        automaticRestart: true
        onHostMaintenance: "MIGRATE"
        preemptible: false
      metadataStartupScript: "echo hi > /test.txt"
      serviceAccount:
        serviceAccountRef:
          name: instancetemplate-dep
        scopes:
          - userinfo-email
          - compute-ro
          - storage-ro
      guestAccelerator:
        - type: nvidia-tesla-t4
          count: 1
      minCpuPlatform: "Intel Skylake"
      shieldedInstanceConfig:
        enableSecureBoot: false
        enableVtpm: true
        enableIntegrityMonitoring: true
    ---
    apiVersion: compute.cnrm.cloud.google.com/v1beta1
    kind: ComputeDisk
    metadata:
      name: instancetemplate-dep
    spec:
      description: a sample encrypted, blank disk
      physicalBlockSizeBytes: 4096
      size: 1
      type: pd-ssd
      location: us-west1-c
    ---
    apiVersion: compute.cnrm.cloud.google.com/v1beta1
    kind: ComputeImage
    metadata:
      name: instancetemplate-dep
    spec:
      description: A sample image created from an empty disk resource
      diskRef:
        name: instancetemplate-dep
    ---
    apiVersion: compute.cnrm.cloud.google.com/v1beta1
    kind: ComputeNetwork
    metadata:
      name: instancetemplate-dep
    spec:
      routingMode: REGIONAL
      autoCreateSubnetworks: false
    ---
    apiVersion: compute.cnrm.cloud.google.com/v1beta1
    kind: ComputeSubnetwork
    metadata:
      name: instancetemplate-dep
    spec:
      ipCidrRange: 10.2.0.0/16
      region: us-west1
      description: a sample subnetwork
      privateIpGoogleAccess: false
      networkRef:
        name: instancetemplate-dep
      logConfig:
        aggregationInterval: INTERVAL_10_MIN
        flowSampling: 0.5
        metadata: INCLUDE_ALL_METADATA
    ---
    apiVersion: iam.cnrm.cloud.google.com/v1beta1
    kind: IAMServiceAccount
    metadata:
      name: instancetemplate-dep
    spec:
      displayName: a sample Service Account
    

**Note:** If you have any trouble with instantiating the resource, refer to [Troubleshoot Config Connector](https://docs.cloud.google.com/config-connector/docs/troubleshooting).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
