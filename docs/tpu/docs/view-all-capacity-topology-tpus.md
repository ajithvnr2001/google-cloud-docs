---
url: https://docs.cloud.google.com/tpu/docs/view-all-capacity-topology-tpus/
title: View the topology and health status of All Capacity mode reservations \u00a0|\u00a0 Cloud TPU \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T03:53:53.346761+00:00
---

# View the topology and health status of All Capacity mode reservations  |  Cloud TPU  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/tpu/docs/view-all-capacity-topology-tpus/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Cloud TPU ](https://docs.cloud.google.com/tpu/docs)
  * [ Guides ](https://docs.cloud.google.com/tpu/docs/intro-to-tpu)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# View the topology and health status of All Capacity mode reservations

**Caution:** The [Compute Engine Service Level Agreement (SLA)](https://cloud.google.com/compute/sla) doesn't apply to All Capacity mode TPUs.

You can retrieve topology and health information about your All Capacity mode capacity using the Google Cloud console or the Google Cloud CLI before or after you provision TPU slices. You can also retrieve the physical location of a TPU VM instance through the Compute Engine Instance API or through a `curl` command from within the TPU VM's guest OS. Topology and health status information at the cluster, block, sub-block, host, and VM levels let you to make topology-aware placement decisions for your workloads, target specific blocks or sub-blocks for deployment, and understand the relative proximity between TPU VM instances.

## View capacity topology in the Google Cloud console

To use the Google Cloud console to view the details of your reservation:

  1. In the Google Cloud console, use the search bar to search for "reservations" and navigate to the [reservation page](https://console.cloud.google.com/compute/reservations).
  2. Select the **On-demand reservations** tab and find your TPU All Capacity mode reservation. Your account team will tell you the name of your reservation.
  3. Select your reservation to view the details page.



For an All Capacity mode reservation, the **Operational mode** is set to **All capacity**. A list of blocks is displayed along with a summary of their utilization and health status.

Select a block from the list to see the block detail page. The block's topology is displayed in the **Cluster Location** section. This section displays the cluster name, the hashed ID of a block, and the hashed ID of a sub-block.

Cluster names are globally unique across all Google organizations. In other words, two different customers may see the same cluster name. Unlike cluster names, the hashed ID of blocks or sub-blocks are unique within your Google Cloud organization's projects.

You can select a sub-block to display the sub-block detail page which only shows you physical hosts with active TPU VM instances. Unused physical hosts are not displayed.

## View capacity topology using Google Cloud CLI

You can use the Google Cloud CLI `list` and `describe` commands on reservations, blocks, and sub-blocks to find topology and health information about your capacity.

You can use the information displayed by the commands in this section to determine the topology hierarchy of the physical capacity in your reservation.

### Describe a reservation

You can use the `gcloud compute reservations describe` to see an overview of the capacity in your reservation. The following command displays a summary of an reservation:
    
    
    gcloud compute reservations describe RESERVATION_NAME \
       --project=PROJECT_ID \
       --zone=ZONE

Replace the following:

  * RESERVATION_NAME: The name of your reservation.
  * PROJECT_ID: Your project ID.
  * ZONE: The zone where your reservation is located.



The output is similar to the following:
    
    
    advancedDeploymentControl:
      **reservationOperationalMode: ALL_CAPACITY**
    aggregateReservation:
      inUseResources:
      - accelerator:
          **acceleratorCount: 48**
          **acceleratorType: projects/example-project/zones/us-central1-c/acceleratorTypes/tpu7x**
      reservedResources:
      - accelerator:
          **acceleratorCount: 128**
          acceleratorType: projects/example-project/zones/us-central1-c/acceleratorTypes/tpu7x
      vmFamily: VM_FAMILY_CLOUD_TPU_POD_SLICE_TPU7X
      workloadType: UNSPECIFIED
    creationTimestamp: '2025-11-05T14:16:30.571-08:00'
    deleteAtTime: '2026-11-06T08:00:00Z'
    **deploymentType: DENSE **
    enableEmergentMaintenance: false
    id: '8873145979824927313'
    kind: compute#reservation
    linkedCommitments:
    - https://www.googleapis.com/compute/v1/projects/example-project/regions/us-central1/commitments/example-cud
    name: example-reservation
    protectionTier: STANDARD
    reservationSharingPolicy:
      **serviceShareType: ALLOW_ALL**
    resourceStatus:
      **healthInfo:    degradedBlockCount: 0
        healthStatus: HEALTHY
        healthyBlockCount: 1
      reservationBlockCount: 1
      reservationMaintenance:
        schedulingType: **
    schedulingType: GROUPED
    selfLink: https://www.googleapis.com/compute/v1/projects/example-project/zones/us-central1-c/reservations/example-reservation
    shareSettings:
      projectMap:
        '111111111111':
          **projectId: '111111111111'**
      shareType: SPECIFIC_PROJECTS
    specificReservationRequired: true
    status: READY
    zone: https://www.googleapis.com/compute/v1/projects/example-project/zones/us-central1-c

The following values from the output describe the reservation:

  * `advancedDeploymentControl.reservationOperationalMode`: the capacity mode for the reservation
  * `aggregateReservation.inUseResources.accelerator.acceleratorCount`: the number of TPU chips in use
  * `aggregateReservation.inUseResources.accelerator.acceleratorType`: the TPU version
  * `reservedResources.accelerator.acceleratorCount`: the number of TPU chips in the reservation
  * `deploymentType`: the deployment type (will always be `DENSE` for TPUs)
  * `reservationSharingPolicy.serviceShareType`: the service share type
  * `resourceStatus.healthInfo.healthStatus`: overall health of the capacity
  * `resourceStatus.healthInfo.healthyBlockCount`: the number of healthy blocks in the reservation
  * `resourceStatus.reservationBlockCount`: the number of blocks in the reservation



### List all reservation blocks

You can use the `gcloud compute reservations blocks list` command to display capacity, topology and health information for all the blocks in a reservation.

Each block, sub-block, and host object is identified by a hash ID. The ID of the parent object is displayed in the physical topology fields of child objects. You can use the hash IDs to construct a topology hierarchy view of the capacity.
    
    
    gcloud compute reservations blocks list RESERVATION_NAME \
      --project=PROJECT_ID \
      --zone=ZONE

Replace the following:

  * RESERVATION_NAME: The name of your reservation.
  * PROJECT_ID: Your project ID.
  * ZONE: The zone where your reservation is located.



The command displays the following output:
    
    
    **count: 32**
    creationTimestamp: '2025-11-05T15:00:15.223-08:00'
    **healthInfo:  degradedSubBlockCount: 0
      healthStatus: HEALTHY
      healthySubBlockCount: 2
      id: '2996501069483632657'**
    **inUseCount: 12**
    **kind: compute#reservationBlock**
    **name: example-reservation-block-0001**
    **physicalTopology:  block: 9a0e671424e45fd480ca172ad7a4e25d
      cluster: example-cluster**
    reservationMaintenance:
      schedulingType: GROUPED
    reservationSubBlockCount: 2
    reservationSubBlockInUseCount: 1
    selfLink: https://www.googleapis.com/compute/v1/projects/example-project/zones/us-central1-c/reservations/example-reservation/reservationBlocks/example-reservation-block-0001
    selfLinkWithId: https://www.googleapis.com/compute/v1/projects/example-project/zones/us-central1-c/reservations/example-reservation/reservationBlocks/2996501069483632657
    status: READY
    zone: https://www.googleapis.com/compute/v1/projects/example-project/zones/us-central1-c
    
    
    **count: 128**
    creationTimestamp: '2025-08-19T18:23:32.825-07:00'
    **healthInfo:**
      **degradedSubBlockCount: 0**
      **healthStatus: HEALTHY**
      **healthySubBlockCount: 4**
    **id: '9a0e671424e45fd480ca172ad7a4e25d'**
    **inUseCount: 64**
    **kind: compute#reservationBlock**
    **name: example-reservation-block-0002**
    **physicalTopology:**
      **block: 3feffcdeb6434d68bb818a836f75c1b8**
      **cluster: example-cluster**
    reservationMaintenance:
      schedulingType: GROUPED
    reservationSubBlockCount: 2
    reservationSubBlockInUseCount: 1
    selfLink: https://www.googleapis.com/compute/v1/projects/example-project/zones/us-central1-c/reservations/example-reservation/reservationBlocks/example-reservation-block-0001
    selfLinkWithId: https://www.googleapis.com/compute/v1/projects/example-project/zones/us-central1-c/reservations/example-reservation/reservationBlocks/2996501069483632657
    status: READY
    zone: https://www.googleapis.com/compute/v1/projects/example-project/zones/us-central1-c

The following values from the output describe the blocks in the reservation:

  * `count`: the number of physical hosts
  * `healthInfo.healthStatus`: the overall health of the block
  * `healthInfo.healthySubblockCount`: the number of healthy sub-blocks in the block
  * `id`: the block's ID
  * `inUseCount`: the number of physical hosts in use
  * `kind`: the kind of object described
  * `name`: the name of the block
  * `physicalTopology.block`: the block ID
  * `physicalTopology.cluster`: the cluster where the block is located
  * `reservationSubBlockCount`: the number of sub-blocks in this block
  * `reservationSubBlockInUseCount`: the number of sub-blocks in use



### Describe a reservation block

You can use the `gcloud compute reservations blocks describe` command on a specific block to display information for the block you specify.
    
    
    gcloud compute reservations blocks describe RESERVATION_NAME \
      --block-name=BLOCK_NAME \
      --project=PROJECT_ID \
      --zone=ZONE

Replace the following:

  * RESERVATION_NAME: The name of your reservation.
  * BLOCK_NAME: The name of the reservation block.
  * PROJECT_ID: Your project ID.
  * ZONE: The zone where your reservation is located.



This command displays the following output:
    
    
    resource:
      **count: 32**
      creationTimestamp: '2025-11-05T15:00:15.223-08:00'
      healthInfo:
        degradedSubBlockCount: 0
        **healthStatus: HEALTHY**
        **healthySubBlockCount: 2**
      **id: '2996501069483632657'**
      **inUseCount: 12**
      **kind: compute#reservationBlock**
      **name: example-reservation-block-0001**
      **physicalTopology:    block: 9a0e671424e45fd480ca172ad7a4e25d
        cluster: example-cluster**
      reservationMaintenance:
        schedulingType: GROUPED
      **reservationSubBlockCount: 2**
      **reservationSubBlockInUseCount: 1**
      selfLink: https://www.googleapis.com/compute/v1/projects/example-project/zones/us-central1-c/reservations/example-reservation/reservationBlocks/example-reservation-block-0001
      selfLinkWithId: https://www.googleapis.com/compute/v1/projects/example-project/zones/us-central1-c/reservations/example-reservation/reservationBlocks/2996501069483632657
      status: READY
      zone: https://www.googleapis.com/compute/v1/projects/example-project/zones/us-central1-c

The following values from the output describe the blocks in the reservation:

  * `count`: the number of hosts in the block
  * `healthInfo.healthStatus`: the overall health of the block
  * `healthInfo.healthySubblockCount`: the number of healthy sub-blocks in the block
  * `id`: the block's ID
  * `inUseCount`: the number of hosts in use
  * `kind`: the kind of object described
  * `name`: the name of the block
  * `physicalTopology.block`: the block ID
  * `physicalTopology.cluster`: the cluster where the block is located
  * `reservationSubBlockCount`: the number of sub-blocks in this block
  * `reservationSubBlockInUseCount`: the number of sub-blocks in use



### List all sub-blocks of a block

You can list the sub-blocks in a block to display information for each sub-block:
    
    
    gcloud compute reservations sub-blocks list RESERVATION_NAME \
      --block-name=BLOCK_NAME \
      --project=PROJECT_ID \
      --zone=ZONE

Replace the following:

  * RESERVATION_NAME: The name of your reservation.
  * BLOCK_NAME: The name of the reservation block.
  * PROJECT_ID: Your project ID.
  * ZONE: The zone where your reservation is located.



This command displays the following information:
    
    
    **count: 16**
    creationTimestamp: '2025-11-05T15:00:16.738-08:00'
    healthInfo:
      degradedHostCount: 0
      **degradedInfraCount: 0**
      **healthStatus: HEALTHY**
      **healthyHostCount: 16**
      healthyInfraCount: 1
    **id: '8309376980435233263'**
    **inUseCount: 0**
    **kind: compute#reservationSubBlock**
    **name: example-reservation-block-0001-subblock-0001**
    **physicalTopology:  block: 9a0e671424e45fd480ca172ad7a4e25d
      cluster: example-cluster
      subBlock: a0122935eb54d02750b65eef2d4f0366**
    reservationSubBlockMaintenance:
      schedulingType: GROUPED
    selfLink: https://www.googleapis.com/compute/v1/projects/example-project/zones/us-central1-c/reservations/example-reservation/reservationBlocks/example-reservation-block-0001/reservationSubBlocks/example-reservation-block-0001-subblock-0001
    selfLinkWithId: https://www.googleapis.com/compute/v1/projects/example-project/zones/us-central1-c/reservations/example-reservation/reservationBlocks/example-reservation-block-0001/reservationSubBlocks/8309376980435233263
    status: READY
    zone: https://www.googleapis.com/compute/v1/projects/example-project/zones/us-central1-c
    ---
    **count: 16**
    creationTimestamp: '2025-11-05T15:00:16.736-08:00'
    **healthInfo:  degradedHostCount: 0
      degradedInfraCount: 0
      healthStatus: HEALTHY
      healthyHostCount: 16
      healthyInfraCount: 1**
    **id: '5629213080155482607'**
    **inUseCount: 12**
    **kind: compute#reservationSubBlock**
    **name: example-reservation-block-0001-subblock-0002**
    **physicalTopology:  block: 9a0e671424e45fd480ca172ad7a4e25d
      cluster: example-cluster
      subBlock: 7aca49831e54d32970631524bc060d9c**
    reservationSubBlockMaintenance:
      schedulingType: GROUPED
    selfLink: https://www.googleapis.com/compute/v1/projects/example-project/zones/us-central1-c/reservations/example-reservation/reservationBlocks/example-reservation-block-0001/reservationSubBlocks/example-reservation-block-0001-subblock-0002
    selfLinkWithId: https://www.googleapis.com/compute/v1/projects/example-project/zones/us-central1-c/reservations/example-reservation/reservationBlocks/example-reservation-block-0001/reservationSubBlocks/5629213080155482607
    status: READY
    zone: https://www.googleapis.com/compute/v1/projects/example-project/zones/us-central1-c

The following values from the output describe the sub-blocks in the reservation:

  * `count`: the number of hosts
  * `healthInfo.degradedInfraCount`: the healthy state of an Ironwood cube's Optical Circuit Switch (OCS). If this value is 1, it indicates the Ironwood cube's OCS has degraded. This value does not apply to Trillium
  * `healthInfo.healthStatus`: the overall health of the sub-block
  * `healthInfo.healthyHostCount`: the number of healthy hosts in the sub-block
  * `id`: the block's ID
  * `inUseCount`: the number of hosts in use
  * `kind`: the kind of object described
  * `name`: the name of the sub-block
  * `physicalTopology.block`: the ID of the block that contains this sub-block
  * `physicalTopology.cluster`: the cluster where the block is located
  * `physicalTopology.subblock`: the sub-block's ID



### Describe a reservation sub-block

You can use the `gcloud compute sub-blocks describe` to see information about a sub-block:
    
    
    gcloud compute reservations sub-blocks describe RESERVATION_NAME \
      --block-name=BLOCK_NAME \
      --sub-block-name=SUB_BLOCK_NAME \
      --project=PROJECT_ID \
      --zone=ZONE

Replace the following:

  * RESERVATION_NAME: The name of your reservation.
  * BLOCK_NAME: The name of the reservation block.
  * SUB_BLOCK_NAME: The name of the reservation sub-block.
  * PROJECT_ID: Your project ID.
  * ZONE: The zone where your reservation is located.



This command displays the following information:
    
    
    resource:
      **count: 16**
      creationTimestamp: '2025-11-05T15:00:16.736-08:00'
      **healthInfo:**
        **degradedHostCount: 0**
        **degradedInfraCount: 0**
        **healthStatus: HEALTHY**
        **healthyHostCount: 16**
        **healthyInfraCount: 1**
      **id: '5629213080155482607'**
      **inUseCount: 12**
      **kind: compute#reservationSubBlock**
      **name: example-reservation-block-0001-subblock-0002**
      **physicalTopology:**
        **block: 9a0e671424e45fd480ca172ad7a4e25d**
        **cluster: example-cluster**
        **subBlock: 7aca49831e54d32970631524bc060d9c**
      reservationSubBlockMaintenance:
        schedulingType: GROUPED
      selfLink: https://www.googleapis.com/compute/v1/projects/example-project/zones/us-central1-c/reservations/example-reservation/reservationBlocks/example-reservation-block-0001/reservationSubBlocks/example-reservation-block-0001-subblock-0002
      selfLinkWithId: https://www.googleapis.com/compute/v1/projects/example-project/zones/us-central1-c/reservations/example-reservation/reservationBlocks/example-reservation-block-0001/reservationSubBlocks/5629213080155482607
      status: READY
      zone: https://www.googleapis.com/compute/v1/projects/example-project/zones/us-central1-c

The following values from the output describe the sub-blocks in the reservation:

  * `count`: the number of hosts
  * `healthInfo.degradedInfraCount`: the healthy state of an Ironwood cube's Optical Circuit Switch (OCS). If this value is 1, it indicates the Ironwood cube's OCS has degraded. This value does not apply to Trillium
  * `healthInfo.healthStatus`: the overall health of the sub-block
  * `healthInfo.healthyHostCount`: the number of healthy hosts in the sub-block
  * `id`: the block's ID
  * `inUseCount`: the number of hosts in use
  * `kind`: the kind of object described
  * `name`: the name of the sub-block
  * `physicalTopology.block`: the ID of the block that contains this sub-block
  * `physicalTopology.cluster`: the cluster where the block is located
  * `physicalTopology.subblock`: the sub-block's ID



### Find the physical location of a TPU VM instance

Once you provision TPU slices, you can retrieve the physical location of your TPU VM instances. This lets you understand the relative distances between TPU VM instances for workload scheduling optimization.

You can find the physical location of a TPU VM instance using `curl` or the Google Cloud CLI:

### curl
    
    
    curl -s -H "Metadata-Flavor: Google" http://metadata.google.internal/computeMetadata/v1/instance/attributes/physical_host_topology

### gcloud
    
    
    gcloud compute instances describe VM_NAME \
        --format="table[box,title=VM-Position](resourceStatus.physical_host_topology:label=location)" \
        --zone=ZONE

Replace the following:

  * VM_NAME: The name of your TPU VM.
  * ZONE: The zone where your TPU VM is located.



Both of these commands display information about the cluster, block, sub-block, and host of the TPU VM you specify:
    
    
    block: 3feffcdeb6434d68bb818a836f75c1b8
    cluster: southamerica-west1-cluster-njga
    subblock: cbee689cb721abdb0c7f80a4f2d0c1c7
    host: 36b2d9731c1e1cf8594a759c8c4178f0

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
