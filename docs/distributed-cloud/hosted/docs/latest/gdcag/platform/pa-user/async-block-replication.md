---
url: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform/pa-user/async-block-replication/
title: Replicate volumes asynchronously \u00a0|\u00a0 Google Distributed Cloud air-gapped \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T23:44:01.433857+00:00
---

# Replicate volumes asynchronously  |  Google Distributed Cloud air-gapped  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform/pa-user/async-block-replication/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Distributed, hybrid, and multicloud ](https://docs.cloud.google.com/docs/dhm-cloud)
  * [ Google Distributed Cloud ](https://docs.cloud.google.com/distributed-cloud/docs)
  * [ Air-gapped ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdch)
  * [ 1.16.2 (Latest) ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag)



Send feedback 

#  Replicate volumes asynchronously Stay organized with collections  Save and categorize content based on your preferences. 

This page shows you how to set up and perform asynchronous replication of Google Distributed Cloud (GDC) air-gapped block storage volumes.

Asynchronous replication is used to replicate data from one GDC zone to another. This replicated data can be used in a failover scenario in case the data in the source zone is unavailable. Note that once a failover has been created, the original volume can't be set up to replicate to the same destination volume. Instead, a new replication relationship must be created.

For Application Operators preferring to use the `gdcloud` CLI, see [Replicate volumes asynchronously for Application Operators](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/application/ao-user/async-block-replication).

## Before you begin

In order to use asynchronous block replication, your Infrastructure Operator (IO) must first set up two zones for asynchronous replication. 

Next, ensure you have the `volume-replication-admin-global` role to administer the VolumeReplicationRelationship resource. In cases where the global API is unavailable, the `app-volume-replication-admin` role can be used to directly modify the zonal VolumeReplicationRelationshipReplica resource.

## Set up replication

The VolumeReplicationRelationship Custom Resource (CR) services the asynchronous block replication API. This CR exists in the global management API. In order to enable replication for a given block device, a VolumeReplicationRelationship CR needs to be created on the global management API:

###  PVC API 

Project Binding is required. Make sure you have [attached your project to each Cluster resource](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform-application/pa-ao-operations/cluster#attach-project-to-cluster) in each participating zone.
    
    
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



This example assumes that a project named PROJECT is created in an org named `my-org` and that a PVC named PVC_NAME has already been provisioned. The SOURCE_USER_CLUSTER_NAME is the name of the source cluster on which the PVC exists and DESTINATION_USER_CLUSTER_NAME is the name of the destination cluster where a new PVC will exist.

The `source` and `destination` fields of the specification indicate where the data is being replicated _from_ and _to_ respectively. In this example, the data is replicated from SOURCE_ZONE_NAME to DESTINATION_ZONE_NAME.

**Note:** The asynchronous block replication service automatically creates a PVC in the destination zone for writing the replicated data. By default, this PVC has the same name as the source PVC; however, the `VolumeOverrideName` field can be used to specify the name of the created PVC. Until a VolumeReplicationFailover is created, though, the destination PVC remains read-only and won't be mountable by any workloads.

###  VM Disk API 

## Replicate virtual machine disks

`VolumeReplicationRelationship` also services the asynchronous virtual machine disk (VM disk) replication API. The source disk being replicated is called the primary disk. The destination disk that is being replicated to is called the secondary disk. Starting asynchronous replication on a primary disk will automatically create the secondary disk.

### Request permissions and access

To replicate VM disks, you must have the Project VirtualMachine Admin role. Follow the steps to [verify](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/application/ao-user/vms/preparation#verify-user-access) that you have the Project VirtualMachine Admin (`project-vm-admin`) role in the namespace of the project where the VM disk resides.

For VM operations using the gdcloud CLI, request your Project IAM Admin to assign you both the Project VirtualMachine Admin role and the Project Viewer (`project-viewer`) role.

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
  * `SOURCE_ZONE_NAME`: the name of the source Zone Resource.
  * `DESTINATION_ZONE_NAME`: the name of the destination Zone Resource.
  * `VIRTUAL_MACHINE_SOURCE_DISK_NAME`: the name of the VirtualMachineDisk resource on the source.
  * `VIRTUAL_MACHINE_DESTINATION_DISK_NAME`: the name of the VirtualMachineDisk resource on the destination.



This example assumes that a project named PROJECT is created in an org named `my-org` and that a `VirtualMachineDisk` named VIRTUAL_MACHINE_SOURCE_DISK_NAME has already been provisioned to the `VirtualMachine` resource.

The `source` and `destination` fields of the specification indicate where the data is being replicated _from_ and _to_ respectively. In this example, the data is replicated from SOURCE_ZONE_NAME to DESTINATION_ZONE_NAME.

**Note:** The asynchronous block replication service automatically creates a `VirtualMachineDisk` in the destination zone for writing the replicated data. By default, this `VirtualMachineDisk` has the same name as the source `VirtualMachineDisk`; however, the `volumeOverrideName` field can be used to specify the name of the created `VirtualMachineDisk`. Until a `VolumeReplicationFailover` is created, though, the destination `VirtualMachineDisk` remains read-only and won't be mountable by any workloads.

## Verification

Check the status of the replication relationship by retrieving the VolumeReplicationRelationship CR from the global API. Reference the following example. Note that the output has been truncated for simplification:
    
    
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

In case the source zone is unavailable for any reason, a `VolumeFailover` CR can be created in the organization's management plane of the destination zone. For a v2 organization, this would be the management API server. For a v1 organization, this would be the organization admin cluster. For example, if a `VolumeReplicationRelationship` was created which specifies `zone2` as the destination zone and a PVC or `VirtualMachineDisk` exists in the `my-org` organization, then the `VolumeFailover` CR is created in the `my-org` management plane in `zone2`. This breaks the replication relationship between the two zones, and allows the PVC or `VirtualMachineDisk` in the destination zone to be mounted by a workload:
    
    
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

  * After, a successful failover is reflected in the status of the CR:
        
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
    

  * Now, it's safe to delete the `VolumeReplicationRelationship` as it's the only action remaining that can be done on this CR.
        
        kubectl --kubeconfig MANAGEMENT_API_SERVER delete volumereplicationrelationship VRR_NAME \
                -n PROJECT
        




## Resize volumes

If at any point the source volume is resized, the corresponding volume in the destination zone, which is created on behalf of the user when a `VolumeReplicationRelationship` is created, should also be resized to match.

Refer to the [Expand VM disks](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/application/ao-user/vms/manage-vms/operations-and-lifecycle/expand-vm-disks) documentation or the [Expand volume capacity](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/application/ao-user/containers/access-persistent-storage#expand_volume_capacity) for resizing storage on both source and destination zones.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
