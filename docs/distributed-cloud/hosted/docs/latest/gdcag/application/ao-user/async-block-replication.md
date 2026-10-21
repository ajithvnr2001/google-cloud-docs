---
url: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/application/ao-user/async-block-replication/
title: Replicate volumes asynchronously \u00a0|\u00a0 Google Distributed Cloud air-gapped \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-15T05:09:37.951668+00:00
---

# Replicate volumes asynchronously  |  Google Distributed Cloud air-gapped  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/application/ao-user/async-block-replication/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Distributed, hybrid, and multicloud ](https://docs.cloud.google.com/docs/dhm-cloud)
  * [ Google Distributed Cloud ](https://docs.cloud.google.com/distributed-cloud/docs)
  * [ Air-gapped ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdch)
  * [ 1.16.2 (Latest) ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag)



Send feedback 

#  Replicate volumes asynchronously Stay organized with collections  Save and categorize content based on your preferences. 

This page describes how to set up and perform asynchronous replication of Google Distributed Cloud (GDC) air-gapped block storage volumes.

Asynchronous replication is used to replicate data from one GDC zone to another. The replicated data can be used for failover if the source zone data becomes unavailable. Note that once a failover is created, the original volume cannot be replicated to the same destination volume. Instead, a new replication relationship must be created.

For Platform Administrators managing PVCs using the KRM API, see [Replicate volumes asynchronously for Platform Administrators](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform/pa-user/async-block-replication).

## Before you begin

To use asynchronous block replication, your Infrastructure Operator (IO) must first set up two zones for asynchronous replication. 

Then, ensure that you have the `app-volume-replication-admin-global` role to administer the VolumeReplicationRelationship resource. In cases where the global API is unavailable, the `volume-replication-admin` role can be used to directly modify the zonal VolumeReplicationRelationshipReplica resource.

## Set up replication

The VolumeReplicationRelationship Custom Resource (CR) services the asynchronous block replication API. This CR exists in the global management API. To enable replication for a given block device, a VolumeReplicationRelationship CR needs to be created on the global management API:

### Replicate PVC API

**Note:** Project Binding is required. Make sure you have [attached your project to each Cluster resource](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform-application/pa-ao-operations/cluster#attach-project-to-cluster) in each participating zone.
    
    
    kubectl --kubeconfig MANAGEMENT_API_SERVER apply -f - <<EOF
    apiVersion: storage.global.gdc.goog/v1
    kind: VolumeReplicationRelationship
    metadata:
      name: VRR_NAME
      namespace: PROJECT
    spec:
      source:
        pvc:
          clusterRef: SOURCE_USER_CLUSTER_NAME
          pvcRef: PVC_NAME
        zoneRef: SOURCE_ZONE_NAME
      destination:
        pvc:
          clusterRef: DESTINATION_USER_CLUSTER_NAME
        zoneRef: DESTINATION_ZONE_NAME
    EOF
    

Replace the following:

  * `MANAGEMENT_API_SERVER`: the zonal API server's kubeconfig path.
  * `VRR_NAME`: the name of the VolumeReplicationRelationship resource.
  * `PROJECT`: the namespace of the Project resource.
  * `SOURCE_USER_CLUSTER_NAME`: the name of the source user Cluster resource to be connected.
  * `PVC_NAME`: the name of the PersistentVolumeClaim Resource.
  * `SOURCE_ZONE_NAME`: the name of the source Zone Resource.
  * `DESTINATION_USER_CLUSTER_NAME`: the name of the destination user Cluster resource to be connected.
  * `DESTINATION_ZONE_NAME`: the name of the destination Zone Resource.



This example assumes a project named PROJECT is created in an org named `my-org` and that a PVC named PVC_NAME has already been provisioned. The SOURCE_USER_CLUSTER_NAME is the name of the source cluster on which the PVC exists and DESTINATION_USER_CLUSTER_NAME is the name of the destination cluster where a new PVC will exist.

The `source` and `destination` fields of the specification indicate where the data is being replicated _from_ and _to_ , respectively. In this example, the data is replicated from SOURCE_ZONE_NAME to DESTINATION_ZONE_NAME.

**Note:** The asynchronous block replication service automatically creates a PVC in the destination zone for writing the replicated data. By default, this PVC has the same name as the source PVC; however, you can use the `volumeOverrideName` field to specify the name of the created PVC. Until a VolumeReplicationFailover is created, though, the destination PVC remains read-only and is not mountable by any workloads.

### Replicate virtual machine disks

`VolumeReplicationRelationship` also services the asynchronous virtual machine disk (VM disk) replication API. The source disk being replicated is called the primary disk. The destination disk that is being replicated to is called the secondary disk. Starting asynchronous replication on a primary disk automatically creates the secondary disk.

#### Request permissions and access

To replicate virtual machine disks, you must have the Project VirtualMachine Admin role. Follow the steps to [verify that you have the Project VirtualMachine Admin role](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/application/ao-user/vms/preparation#verify-user-access) (`project-vm-admin`) in the namespace of the project where the VM disk resides.

For virtual machine operations using the gdcloud CLI, request your Project IAM Admin to assign you both the Project VirtualMachine Admin role and the Project Viewer (`project-viewer`) role.

###  gdcloud 
    
    
    gdcloud compute disks start-async-replication PRIMARY_DISK_NAME \
      --project PROJECT --zone PRIMARY_ZONE \
      --secondary-disk SECONDARY_DISK_NAME --secondary-zone SECONDARY_ZONE
    

Replace the following:

Variable| Definition | `PRIMARY_DISK_NAME` | The name of the source disk being replicated.  
---|---  
`PROJECT` | The GDC project of the primary disk.  
`PRIMARY_ZONE` | The zone where the primary disk resides.  
`SECONDARY_DISK_NAME` | The name of the destination disk to replicate to.  
`SECONDARY_ZONE` | The zone where the secondary disk must reside.  
  
###  VM Disk API 

### Start asynchronous replication

Start asynchronous replication on a VM disk using `kubectl`.
    
    
    kubectl --kubeconfig MANAGEMENT_API_SERVER apply -f - <<EOF
    apiVersion: storage.global.gdc.goog/v1
    kind: VolumeReplicationRelationship
    metadata:
      name: VRR_NAME
      namespace: PROJECT
    spec:
      destination:
        volumeOverrideName: VIRTUAL_MACHINE_DESTINATION_DISK_NAME
        zoneRef: DESTINATION_ZONE_NAME
      source:
        virtualMachineDisk:
          virtualMachineDiskRef: VIRTUAL_MACHINE_SOURCE_DISK_NAME
        zoneRef: SOURCE_ZONE_NAME
    EOF
    

Replace the following:

  * `MANAGEMENT_API_SERVER`: the zonal API server's kubeconfig path.
  * `VRR_NAME`: the name of the VolumeReplicationRelationship resource.
  * `PROJECT`: the namespace of the Project resource.
  * `VIRTUAL_MACHINE_DESTINATION_DISK_NAME`: the name of the VirtualMachineDisk resource on the destination.
  * `DESTINATION_ZONE_NAME`: the name of the destination Zone Resource.
  * `VIRTUAL_MACHINE_SOURCE_DISK_NAME`: the name of the VirtualMachineDisk resource on the source.
  * `SOURCE_ZONE_NAME`: the name of the source Zone Resource.



This example assumes that a project named PROJECT is created in an org named `my-org` and that a `VirtualMachineDisk` named VIRTUAL_MACHINE_SOURCE_DISK_NAME has already been provisioned to the `VirtualMachine` resource.

The `source` and `destination` fields of the specification indicate where the data is being replicated _from_ and _to_ respectively. In this example, the data is replicated from SOURCE_ZONE_NAME to DESTINATION_ZONE_NAME.

**Note:** The asynchronous block replication service automatically creates a `VirtualMachineDisk` in the destination zone for writing the replicated data. By default, this `VirtualMachineDisk` has the same name as the source `VirtualMachineDisk`; however, you can use the `volumeOverrideName` field to specify the name of the created `VirtualMachineDisk`. Until a `VolumeReplicationFailover` is created, though, the destination `VirtualMachineDisk` remains read-only and won't be mountable by any workloads.

## Verification

Check the status of the replication relationship by retrieving the `VolumeReplicationRelationship` CR from the global API. Reference the following example. Note that the output has been truncated for simplification:
    
    
    kubectl --kubeconfig MANAGEMENT_API_SERVER get volumereplicationrelationship VRR_NAME \
            -n PROJECT -o yaml
    

The output is similar to the following:

###  PVC API 
    
    
    apiVersion: storage.global.gdc.goog/v1
    kind: VolumeReplicationRelationship
    metadata:
      name: my-pvc-repl
      namespace: my-project
    spec:
      destination:
        pvc:
          clusterRef: my-pvc-cluster
        zoneRef: zone2
      source:
        pvc:
          clusterRef: my-pvc-cluster
          pvcRef: my-block-pvc
        zoneRef: zone1
    status:
      zones:
      - name: zone1
        replicaStatus:
          message: SnapMirror relationship has been established. Please check the destination
            zone for relationship state
          replicationID: a096621e-f062-11ef-ad24-00a0b89f23fb
          state: Established
      - name: zone2
        replicaStatus:
          exportedSnapshotName: snapmirror.c34f8845-e8c0-11ef-ad24-00a0b89f23fb_2150007868.2025-02-21_150000
          message: SnapMirror relationship has been successfully established
          replicationID: a096621e-f062-11ef-ad24-00a0b89f23fb
          state: Idle
    

###  VM Disk API 
    
    
    apiVersion: storage.global.gdc.goog/v1
    kind: VolumeReplicationRelationship
    metadata:
      name: my-vmdisk-vrr
      namespace: my-project
    spec:
      destination:
        zoneRef: zone2
      source:
        virtualMachineDisk:
          virtualMachineDiskRef: my-vmdisk
        zoneRef: zone1
    status:
      zones:
      - name: zone1
        replicaStatus:
          message: SnapMirror relationship has been established. Please check the destination
            zone for relationship state
          replicationID: a096621e-f062-11ef-ad24-00a0b89f23fb
          state: Established
      - name: zone2
        replicaStatus:
          exportedSnapshotName: snapmirror.c34f8845-e8c0-11ef-ad24-00a0b89f23fb_2150007868.2025-02-21_150000
          message: SnapMirror relationship has been successfully established
          replicationID: a096621e-f062-11ef-ad24-00a0b89f23fb
          state: Idle
    

## Create failover

In case the source zone is unavailable for any reason, a `VolumeFailover` CR can be created in the organization's management plane of the destination zone. For a v2 organization, this would be the management API server. For a v1 organization, this would be the organization admin cluster. For example, if a `VolumeReplicationRelationship` was created which specifies `zone2` as the destination zone and a PVC or `VirtualMachineDisk` exists in the `my-org` organization, then the `VolumeFailover` CR is created in the `my-org` management plane in `zone2`. This breaks the replication relationship between the two zones, and allows a workload to mount the PVC or `VirtualMachineDisk` in the destination zone:
    
    
      kubectl --kubeconfig MANAGEMENT_API_SERVER apply -f - <<EOF
      apiVersion: storage.gdc.goog/v1
      kind: VolumeFailover
      metadata:
        name: FAILOVER_NAME
        namespace: PROJECT
      spec:
        volumeReplicationRelationshipRef: VRR_NAME
      EOF
    

Replace the following:

  * `FAILOVER_NAME`: the name of the VolumeFailover resource.
  * `MANAGEMENT_API_SERVER`: the zonal API server's kubeconfig path.
  * `VRR_NAME`: the name of the VolumeReplicationRelationship resource.
  * `PROJECT`: the namespace of the Project resource.



After, a successful failover is reflected in the status of the CR:
    
    
      kubectl --kubeconfig MANAGEMENT_API_SERVER get volumefailover FAILOVER_NAME \
              -n PROJECT -o yaml
    

  * The output is similar to the following:
        
        apiVersion: storage.gdc.goog/v1
        kind: VolumeFailover
        metadata:
          name: my-failover
          namespace: my-project
        spec:
          volumeReplicationRelationshipRef: my-vrr-repl
        status:
            state: Completed
        

  * After the failover is created, the `my-vrr-repl` `VolumeReplicationRelationship` transitions to a `Broken Off` state. The PVC or VirtualMachineDisk in `zone2` is now mountable.

  * At this point, the `VolumeReplicationRelationship` will look similar to the following example. Again, this output has been truncated for simplification:
        
        kubectl --kubeconfig MANAGEMENT_API_SERVER get volumereplicationrelationship VRR_NAME \
                -n PROJECT -o yaml
        

  * The output is similar to the following:




###  PVC API 
    
    
    apiVersion: storage.global.gdc.goog/v1
    kind: VolumeReplicationRelationship
    metadata:
      name: my-vrr-repl
      namespace: my-project
    spec:
      destination:
        pvc:
          clusterRef: my-pvc-cluster
        zoneRef: zone2
      source:
        pvc:
          clusterRef: my-pvc-cluster
          pvcRef: my-block-pvc
        zoneRef: zone1
    status:
      zones:
      - name: zone1
        replicaStatus:
          message: SnapMirror relationship has been broken off
          replicationID: a096621e-f062-11ef-ad24-00a0b89f23fb
          state: Broken Off
      - name: zone2
        replicaStatus:
          exportedSnapshotName: snapmirror.c34f8845-e8c0-11ef-ad24-00a0b89f23fb_2150007868.2025-02-21_150000
          message: SnapMirror relationship has been broken off
          replicationID: a096621e-f062-11ef-ad24-00a0b89f23fb
          state: Broken Off
    

###  VM Disk API 
    
    
    apiVersion: storage.global.gdc.goog/v1
    kind: VolumeReplicationRelationship
    metadata:
      name: my-vmdisk-vrr
      namespace: my-project
    spec:
      destination:
        zoneRef: zone2
      source:
        virtualMachineDisk:
          virtualMachineDiskRef: my-vmdisk
        zoneRef: zone1
    status:
      zones:
      - name: zone1
        replicaStatus:
          message: SnapMirror relationship has been broken off
          replicationID: a096621e-f062-11ef-ad24-00a0b89f23fb
          state: Broken Off
      - name: zone2
        replicaStatus:
          exportedSnapshotName: snapmirror.c34f8845-e8c0-11ef-ad24-00a0b89f23fb_2150007868.2025-02-21_150000
          message: SnapMirror relationship has been broken off
          replicationID: a096621e-f062-11ef-ad24-00a0b89f23fb
          state: Broken Off
    

  * You can now safely delete the `VolumeReplicationRelationship` because it is the only action remaining that can be done on this CR.
        
        kubectl --kubeconfig MANAGEMENT_API_SERVER delete volumereplicationrelationship VRR_NAME \
                -n PROJECT
        




## Resize volumes

If at any point the source volume is resized, you must also resize the corresponding volume in the destination zone to match. The destination zone volume is created when you create the `VolumeReplicationRelationship`.

Refer to the [Expand VM disks](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/application/ao-user/vms/manage-vms/operations-and-lifecycle/expand-vm-disks) documentation or the [Expand volume capacity](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/application/ao-user/containers/access-persistent-storage#expand_volume_capacity) for resizing storage on both source and destination zones.

### List asynchronous replication relationships

List asynchronous replication relationships in a project using `kubectl`.
    
    
    kubectl --kubeconfig MANAGEMENT_API_SERVER get volumereplicationrelationships -n PROJECT
    

Replace the following:

  * PROJECT: The GDC project of the primary disk.
  * MANAGEMENT_API_SERVER: The kubeconfig file for the zonal management API server.



The output looks similar to the following:
    
    
    NAME       AGE     SOURCE ZONE   SOURCE PVC   SOURCE PVC CLUSTER   SOURCE VM DISK      DEST. ZONE   DEST. PVC CLUSTER   DEST. VOLUME OVERRIDE     STATE
    my-vrr     3m21s   zone1                                           my-vm-boot-disk     zone2                            my-vm-boot-disk-replica
    test-vrr   7s      zone1                                           test-vm-boot-disk   zone2
    

### Stop asynchronous replication

Stop asynchronous replication on a primary VM disk using gdcloud or `kubectl`.

###  gdcloud 
    
    
    gdcloud compute disks stop-async-replication PRIMARY_DISK_NAME \
      --project PROJECT --zone PRIMARY_ZONE
    

Replace the following:

Variable| Definition | `PRIMARY_DISK_NAME` | The name of the source disk being replicated.  
---|---  
`PROJECT` | The GDC project of the primary disk.  
`PRIMARY_ZONE` | The zone where the primary disk resides.  
  
###  API 

  1. Find the volume replication relationships corresponding to the primary VM disk.
         
         kubectl --kubeconfig MANAGEMENT_API_SERVER get volumereplicationrelationships \
           -n PROJECT -o json | \
           jq -r '.items[] | select(.spec.source.virtualMachineDisk.virtualMachineDiskRef == "PRIMARY_DISK_NAME"
           and .spec.source.zoneRef == "PRIMARY_ZONE") | .metadata.name'
         

  2. Delete each of the volume replication relationships listed in the previous step. Replace VRR_NAMES with the names of the volume replication relationships.
         
         kubectl --kubeconfig MANAGEMENT_API_SERVER delete volumereplicationrelationships \
           -n PROJECT VRR_NAMES
         

Replace the following:

Variable| Definition | `MANAGEMENT_API_SERVER` | The kubeconfig file for the global management API server.  
---|---  
`PROJECT` | The GDC project of the primary disk.  
`PRIMARY_DISK_NAME` | The name of the source disk being replicated.  
`PRIMARY_ZONE` | The zone where the primary disk resides.  



If the source zone is unavailable for any reason, create a volume failover to stop replication.

### Attach the replicated disk to a VM

While replication is enabled, the secondary disk cannot be attached to a VM. After replication is stopped, you can attach the secondary disk to a [newly created VM](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/application/ao-user/vms/create-a-vm/create-and-start) or to an [existing VM](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/application/ao-user/vms/manage-storage/add-a-vm-disk#attach-a-disk-to-vm).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
