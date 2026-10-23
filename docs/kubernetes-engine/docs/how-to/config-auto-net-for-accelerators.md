---
url: https://docs.cloud.google.com/kubernetes-engine/docs/how-to/config-auto-net-for-accelerators/
title: Configure automated networking for accelerator VMs \u00a0|\u00a0 GKE networking \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:23:35.750880+00:00
---

# Configure automated networking for accelerator VMs  |  GKE networking  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/docs/how-to/config-auto-net-for-accelerators/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ Google Kubernetes Engine (GKE) ](https://docs.cloud.google.com/kubernetes-engine/docs)
  * [ GKE networking ](https://docs.cloud.google.com/kubernetes-engine/networking/docs)
  * [ Guides ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/explore-gke-networking-docs-use-cases)



Send feedback 

#  Configure automated networking for accelerator VMs Stay organized with collections  Save and categorize content based on your preferences. 

[ Autopilot ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/autopilot-overview) [ Standard ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/choose-cluster-mode)

This document shows you how to use _automated networking_ for accelerator VMs, such as GPUs and TPUs, to simplify the network configuration for Google Kubernetes Engine (GKE) accelerator workloads. This is essential for running artificial intelligence (AI), machine learning (ML), and high performance computing (HPC) on accelerator-optimized machines.

This document assumes familiarity with fundamental GKE concepts, GPU and TPU workloads, and VPC networking. Specifically, you should be familiar with:

  * [Kubernetes](https://kubernetes.io/docs/concepts/)
  * [GKE networking](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/network-overview)
  * [VPC networking concepts](https://docs.cloud.google.com/vpc/docs/vpc)



This page is intended for Cloud architects and Networking specialists who design and architect their organization's network. For an overview of all GKE documentation sets, see [Explore GKE documentation](https://docs.cloud.google.com/kubernetes-engine/docs/about). To learn more about common roles and example tasks referenced in Google Cloud content, see [Common GKE user roles and tasks](https://docs.cloud.google.com/kubernetes-engine/enterprise/docs/concepts/roles-tasks).

GKE simplifies running high-performance AI and ML on specialized accelerators. With automated networking for accelerator VMs, you can enable high-speed, multi-network connectivity—essential for protocols like RDMA—with a single configuration flag. This automation eliminates the complex, manual process of setting up multiple VPC networks, managing IP address ranges, and configuring network interfaces for every node pool and Pod. By using a single parameter when creating a node pool, GKE provides all the necessary cloud and Kubernetes networking resources.

## Terminology

The following terms are key to understanding the networking architecture for accelerator VMs.

  * **Virtual Private Cloud (VPC)** : a [VPC](https://docs.cloud.google.com/vpc/docs/vpc) is a virtual version of a physical network, implemented inside of Google's production network. It provides connectivity for your Compute Engine virtual machine (VM) instances, GKE clusters, and other resources.
  * **[Titanium NIC](https://cloud.google.com/titanium?e=48754805)** : a smart NIC that offloads network processing tasks from the CPU, freeing the CPU to focus on your workloads. On GPU machines, they handle all traffic that is not direct GPU-to-GPU communication. On TPU machines, all NICs are Titanium NICs.
  * **Subnetwork** : a [subnetwork](https://docs.cloud.google.com/vpc/docs/subnets) is a segmented piece of a larger VPC. Each subnetwork is associated with a region and has a defined IP address range.
  * **Network Interface Controller (NIC)** : a [NIC](https://docs.cloud.google.com/compute/docs/multiple-interfaces-concepts) is a virtual network interface that connects a VM instance to a network. Each NIC is attached to a specific VPC and subnetwork.
  * **Host network** : the primary network used by the node's main network interfaces (NICs) for general cluster communication, such as control plane traffic and regular Pod networking.
  * **Data network** : a dedicated network for high-performance data transfer between accelerator VMs. For GPUs, this is often a GPUDirect VPC with RDMA. For TPUs, this might be a second host network.
  * **Remote Direct Memory Access(RDMA)** : [RDMA](https://en.wikipedia.org/wiki/Remote_direct_memory_access) is a technology that allows network devices to exchange data directly with the main memory of a computer without involving the operating system or CPU. This significantly reduces latency and improves throughput, which is critical for HPC and ML workloads.
  * **NVLink** : [NVLink](https://www.nvidia.com/en-us/data-center/nvlink/) is a high-speed interconnect technology developed by NVIDIA to connect multiple GPUs within a single node, enabling them to share memory and work together on large datasets.
  * **Kubernetes dynamic resource allocation (DRA)** : [DRA](https://kubernetes.io/docs/concepts/scheduling-eviction/dynamic-resource-allocation/) is a Kubernetes feature that provides a more flexible way for Pods to request and consume resources, such as GPUs and other specialized hardware. It allows for fine-grained control over resource allocation.



## How automated networking works

Accelerator-optimized machines have a specialized network architecture to support high-throughput, low-latency communication between GPUs and TPUs. Each physical machine contains multiple GPUs or TPUs, often connected by high-speed interconnects like NVLink. The machines also have one or more NICs for general networking and multiple GPU NICs for high-speed interconnects.

When you create a GKE node that uses an accelerator-optimized machine type, GKE configures multiple NICs on the underlying VM. Host NICs connect to host VPC networks for general cluster communication and management to communicate with the control plane. GPU NICs connect to a dedicated, high-performance VPC network, often with RDMA enabled and a high MTU setting (8896), to facilitate GPUDirect communication.

When a Pod requests GPUs or TPUs, you can configure it to access the high-performance network interfaces on the node. You can request all available NICs or a specific subset. Each claimed network interface is dedicated to a single Pod and isn't shared. This network configuration helps ensure the Pod has sole access to the full bandwidth and resources of that interface, a key benefit for performance-sensitive workloads.

## Limitations

  * Automated networking requires the cluster to use GKE Dataplane V2.
  * Automated networking is supported on A3, A4, and TPU Trillium (v6e) accelerator-optimized machine families, as well as the Z4M storage-optimized machine series.
  * You must use a node pool with a single zone.
  * You can't use automated networking in a cluster that uses [Shared VPC](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/cluster-shared-vpc).
  * When using GKE managed DRANET to configure workloads, see the [key considerations](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/allocate-network-resources-dra#key-considerations) and [limitations](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/allocate-network-resources-dra#limitations) for GKE managed DRANET.
  * You can't use both the [multi-network API](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/setup-multinetwork-support-for-pods#create-gke-node-pool) and DRANET in the same nodepool. You must choose one method for network attachment for your Pods.
  * For regional clusters, you must specify the target zone when you enable accelerator network profiles. If your workload spans multiple zones, you must enable the network profile for each zone independently.



## Machine network configurations

Accelerator-optimized and storage-optimized machines have varying network configurations depending on their type. The following tables summarize the network specifications for various machine types.

### GPU accelerator VMs

Machine type | Number of GPUs | Number of Titanium NICs | Number of GPU NICs | GPUDirect Technology | Additional VPCs  
---|---|---|---|---|---  
A3 | 8 (H100) | 1 | 4 | TCPX | 4 for GPU NICs  
A3 Mega | 8 (H100) | 1 | 8 | TCPXO | 8 for GPU NICs  
A3 Ultra | 8 (H200) | 2 | 8 | RDMA | 2 (1 for second NIC, 1 for GPU NICs)  
A4 | 8 (B200) | 2 | 8 | RDMA | 2 (1 for second NIC, 1 for GPU NICs)  
A4X | 4 (GB200) | 2 | 4 | RDMA | 2 (1 for second NIC, 1 for GPU NICs)  
A4X BM | 8 | 2 | 8 | BM-RDMA | 2 (1 for second NIC, 1 for GPU NICs)  
  
### TPU accelerator VMs

Machine type | Number of TPU chips | Number of NICs | Additional VPCs  
---|---|---|---  
TPU Trillium (v6e) (ct6e-standard-1t) | 1 | 0.25 | 1  
TPU Trillium (v6e) (ct6e-standard-4t) | 4 | 2 | 2 (1 for 2nd NIC, 1 for extra VNIC on 1st NIC)  
TPU Trillium (v6e) (ct6e-standard-8t) | 8 | 4 | 4  
tpu7x-standard-4t | 4 | 2 | 2  
  
### Storage-optimized VMs

On Z4M instances, the two physical Titanium NICs support both general network traffic (gVNIC) and up to two IRDMA virtual network interfaces (vNICs) for Cloud RDMA communication.

Machine type | Number of physical Titanium NICs | Number of RDMA vNICs | Networking technology | Additional VPCs  
---|---|---|---|---  
Z4M (`z4m-highmem-192`) | 2 | Up to 2 (shared on physical NICs) | RDMA | 2 for RDMA vNICs  
  
## Before you begin

Before you start, make sure that you have performed the following tasks: 

  * Enable the Google Kubernetes Engine API. 
[ Enable Google Kubernetes Engine API ](https://console.cloud.google.com/apis/enableflow?apiid=container.googleapis.com)
  * To use the Google Cloud CLI for this task, [install](https://docs.cloud.google.com/sdk/docs/install) and then [initialize](https://docs.cloud.google.com/sdk/docs/initialize) the gcloud CLI. If you previously installed the gcloud CLI, get the latest version by running the `gcloud components update` command. Earlier gcloud CLI versions might not support running the commands in this document. **Note:** For existing gcloud CLI installations, make sure to set the `compute/region` [property](https://docs.cloud.google.com/sdk/docs/properties#setting_properties). If you use primarily zonal clusters, set the `compute/zone` instead. By setting a default location, you can avoid errors in the gcloud CLI like the following: `One of [--zone, --region] must be supplied: Please specify location`. You might need to specify the location in certain commands if the location of your cluster differs from the default that you set.


  * Ensure your cluster uses GKE version 1.34.1-gke.2037000 or later.
  * To enable [node auto-provisioning](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/node-auto-provisioning) and [custom ComputeClasses](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/about-custom-compute-classes), ensure that your cluster uses GKE version 1.35.2-gke.1302000 or later.

  * Ensure that the GKE service account in your project has the `compute.networkAdmin` role.

  * Ensure that your cluster has GKE Dataplane V2 enabled. You can enable GKE Dataplane V2 only when you create a new cluster on GKE version 1.34.1-gke.2037000 or later. You can't enable GKE Dataplane V2 on clusters prior to this version.
        
        gcloud container clusters create CLUSTER_NAME \
            --cluster-version=CLUSTER_VERSION \
            --enable-dataplane-v2
        

  * If you plan to deploy GPU or Z4M workloads that use RDMA, verify the existence of the `DeviceClass` resources (`mrdma.google.com` for GPUs or `irdma.google.com` for Z4M):
        
        kubectl get deviceclass mrdma.google.com
        




## Configure automated networking

You can enable automated networking by specifying an accelerator network profile when you create a node pool. You can also create a ComputeClass resource for clusters that use node auto-provisioning.

### Create a node pool with a default network profile

To automatically create a network that connects all GPUs or TPUs machines within a single zone, create a node pool with the `auto` accelerator network profile.

### gcloud

To create a node pool with an automatically configured network profile, run the following command:
    
    
    gcloud beta container node-pools create NODE_POOL_NAME \
        --accelerator-network-profile=auto \
        --node-locations=ZONE \
        --machine-type=MACHINE_TYPE
    

When you create a node pool with the `--accelerator-network-profile=auto` flag, GKE automatically adds the `gke.networks.io/accelerator-network-profile: auto` label to the nodes. To schedule workloads on these nodes, you must include this label in your workload's `nodeSelector`.

For more information about creating node pools with accelerators, see [Run GPUs in Autopilot node pools](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/gpus) and [Deploy TPU workloads in Autopilot](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/tpus). When you follow the instructions in these documents, append the `--accelerator-network-profile=auto` flag to the `gcloud container node-pools create` command.

For multi-host TPU slice node pools, you also need to add the `--tpu-topology` flag.

Replace the following:

  * `NODE_POOL_NAME`: the name of your new node pool.
  * `ZONE`: the zone for the node pool.
  * `MACHINE_TYPE`: the machine type for the nodes, for example, `a3-ultragpu-8g`.



### REST

In a request to the `nodePools.create` method, specify the `accelerator_network_profile` field:
    
    
    {
      "nodePool": {
        "name": "NODE_POOL_NAME",
        "machineType": "MACHINE_TYPE",
        ...
        "accelerator_network_profile": "auto"
      }
    }
    

Replace the following:

  * `NODE_POOL_NAME`: the name of your new node pool.
  * `MACHINE_TYPE`: the machine type for the nodes, for example, `a3-ultragpu-8g`.



### Enable automated networking with node auto-provisioning

To configure automated networking in Autopilot clusters or Standard clusters that use node auto-provisioning, add the `acceleratorNetworkProfile` field to a ComputeClass resource.

  1. The following example ComputeClass manifest enables automated networking for A3 Mega machines. Save the following manifest as `anp-compute-class.yaml`:
         
         apiVersion: cloud.google.com/v1
         kind: ComputeClass
         metadata:
           name: anp-a3-mega-class
         spec:
           autopilot:
             enabled: true
           nodePoolAutoCreation:
             enabled: true
           priorities:
           # Priority 1: A3 Mega in us-central1-a
           - machineType: a3-megagpu-8g
             gpu:
               count: 8
               driverVersion: default
               type: nvidia-h100-mega-80gb
             flexStart:
               enabled: true
             location:
               zones: [us-central1-a]
             acceleratorNetworkProfile: auto
           whenUnsatisfiable: DoNotScaleUp
         

  2. Apply the manifest to your cluster:
         
         kubectl apply -f anp-compute-class.yaml
         




When you deploy a workload that selects this ComputeClass resource, GKE automatically configures the necessary network interfaces for the provisioned nodes.

## Schedule a workload that uses GPUs

The following sections show you how to configure a GPU node pool and workload to use RDMA network interfaces with GKE managed DRANET. For more details, see [Allocate network resources using GKE managed DRANET](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/allocate-network-resources-dra).

### Enable GKE managed DRANET driver on a GPU node pool

To enable the GKE DRANET driver on a GPU node pool that supports RDMA, add the `cloud.google.com/gke-networking-dra-driver=true` label when you create the node pool.
    
    
    gcloud beta container node-pools create NODE_POOL_NAME \
      --region=REGION \
      --cluster=CLUSTER_NAME \
      --node-locations=NODE_LOCATIONS \
      --accelerator type=ACCELERATOR_TYPE,count=ACCELERATOR_COUNT,gpu-driver-version=DRIVER_VERSION \
      --machine-type=MACHINE_TYPE \
      --num-nodes=NUM_NODES \
      --reservation-affinity=specific \
      --reservation=projects/RESERVATION_PROJECT/reservations/RESERVATION_NAME/reservationBlocks/RESERVATION_BLOCK \
      --accelerator-network-profile=auto \
      **--node-labels =cloud.google.com/gke-networking-dra-driver=true**
    

Replace the following:

  * `NODE_POOL_NAME`: the name of your new node pool.
  * `REGION`: the Google Cloud region for your cluster.
  * `CLUSTER_NAME`: the name of your cluster.
  * `ACCELERATOR_TYPE`: the type of [GPU accelerator](https://docs.cloud.google.com/compute/docs/gpus):

For example:

    * A4 VMs: enter `nvidia-b200`.
    * A3 Ultra VMs: enter `nvidia-h200-141gb`.
  * `ACCELERATOR_COUNT`: the number of GPUs to attach to nodes in the node pool. For example, for both a4-highgpu-8g and a3-ultragpu-8g VMs, the amount of GPUs is 8.

  * `DRIVER_VERSION`: the GPU driver version to use. For example, `default` or `latest`.

  * `MACHINE_TYPE`: the machine type for the node pool, for example, `a3-ultragpu-8g`.

  * `NUM_NODES`: the number of nodes for the node pool. For flex-start, this value must be set to 0.

  * `RESERVATION_PROJECT`: the project ID of the reservation.

  * `RESERVATION_NAME`: the name of your reservation. To find this value, see [View future reservation requests](https://docs.cloud.google.com/compute/docs/instances/reservations-view#view-future-reservations).

  * `RESERVATION_BLOCK`: the name of a specific block within the reservation. To find this value, see [View future reservation requests](https://docs.cloud.google.com/compute/docs/instances/reservations-view#view-future-reservations).




This command uses accelerator network profiles to automatically configure VPC networks and subnets for your accelerator VMs. Alternatively, you can explicitly [specify your VPC network](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/setup-multinetwork-support-for-pods#create-gke-node-pool) and subnets.

### Deploy a workload RDMA resources

To allocate RDMA resources for a Pod, specify a `ResourceClaimTemplate`.

  1. Create a `ResourceClaimTemplate` to define how to allocate the RDMA devices. The following manifest requests all available `mrdma` devices on the node. Save the manifest as `all-mrdma-template.yaml`:
         
         apiVersion: resource.k8s.io/v1
         kind: ResourceClaimTemplate
         metadata:
           name: all-mrdma
         spec:
           spec:
             devices:
               requests:
               - name: req-mrdma
                 exactly:
                   deviceClassName: mrdma.google.com
                   allocationMode: All
         

  2. Apply the manifest:
         
         kubectl apply -f all-mrdma-template.yaml
         

  3. Deploy your workload and reference the `ResourceClaimTemplate`. The following manifest deploys a Pod that references the `all-mrdma` template, which grants the Pod access to the RDMA interfaces on the node. Save the manifest as `agnhost-rdma-pod.yaml`:
         
         apiVersion: v1
         kind: Pod
         metadata:
           name: agnhost-rdma
           namespace: default
           labels:
             app: agnhost
         spec:
           containers:
           - name: agnhost
             image: registry.k8s.io/e2e-test-images/agnhost:2.39
             args: ["netexec", "--http-port", "80"]
             ports:
             - name: agnhost-port
               containerPort: 80
             resources:
               claims:
               - name: rdma
               limits:
                 nvidia.com/gpu: 1
           resourceClaims:
           - name: rdma
             resourceClaimTemplateName: all-mrdma
         

  4. Apply the manifest:
         
         kubectl apply -f agnhost-rdma-pod.yaml
         

  5. Verify that the additional allocated network interfaces are visible inside the Pod.
         
         kubectl exec agnhost-rdma -- ls /sys/class/net
         

The following example output shows the default `eth0` and `lo` interfaces, as well as the allocated RDMA interfaces, such as `gpu0rdma0`. The number and names of the network interfaces (NICs) vary based on the GKE node's machine type.
         
         eth0
         gpu0rdma0
         gpu1rdma0
         gpu2rdma0
         gpu3rdma0
         lo
         




## Schedule a workload that uses TPUs

The following sections show you how to configure a TPU node pool and workload to use non-RDMA network interfaces with GKE managed DRANET. For more details, see [Allocate network resources using GKE managed DRANET](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/allocate-network-resources-dra).

### Verify networking DeviceClasses

Verify that the `DeviceClass` resources for networking exist in your cluster.
    
    
    kubectl get deviceclass netdev.google.com
    

The output is similar to the following:
    
    
    NAME                AGE
    netdev.google.com   2d22h
    

### Enable GKE managed DRANET driver on a TPU slice node pool

To enable the GKE DRANET driver when creating a TPU slice node pool, add the `cloud.google.com/gke-networking-dra-driver=true` label.
    
    
    gcloud beta container node-pools create NODE_POOL_NAME \
        --location=LOCATION \
        --cluster=CLUSTER_NAME \
        --node-locations=NODE_LOCATIONS \
        --machine-type=MACHINE_TYPE \
        --tpu-topology=TPU_TOPOLOGY \
        --num-nodes=NUM_NODES \
        --accelerator-network-profile=auto \
        **--node-labels =cloud.google.com/gke-networking-dra-driver=true**
    

Replace the following:

  * `NODE_POOL_NAME`: The name of your new node pool.
  * `LOCATION`: The Google Cloud region or zone for your cluster.
  * `CLUSTER_NAME`: The name of your cluster.
  * `NODE_LOCATIONS`: The Google Cloud zones for the nodes in the node pool.
  * `MACHINE_TYPE`: The type of machine to use for nodes. For more information about TPU-compatible machine types, see [Choose the TPU version](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/plan-tpus#choose-tpu-version).
  * `TPU_TOPOLOGY`: The TPU topology, for example, `2x4x4`. The format of the topology depends on the TPU version. To learn more about TPU topologies, see [Choose a topology](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/plan-tpus#topology).
  * `NUM_NODES`: The number of nodes in the node pool.



For more information, see [Create a single-host TPU slice node pool](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/tpus#single-host).

### Deploy a workload claiming all network devices

To allocate non-RDMA network devices for a Pod, specify a `ResourceClaimTemplate`.

  1. Create a `ResourceClaimTemplate` that references the `netdev.google.com` `DeviceClass`. The following manifest requests all available non-RDMA network devices on the node.

Save the manifest as `all-netdev-template.yaml`:
         
         apiVersion: resource.k8s.io/v1
         kind: ResourceClaimTemplate
         metadata:
           name: all-netdev
         spec:
           spec:
             devices:
               requests:
               - name: req-netdev
                 exactly:
                   deviceClassName: netdev.google.com
                   allocationMode: All
         

  2. Apply the manifest:
         
         kubectl apply -f all-netdev-template.yaml
         

  3. Deploy your workload and reference the `ResourceClaimTemplate`. The following manifest deploys a Pod that uses the `all-netdev` template to grant the Pod access to all non-RDMA network devices on the node. Save the manifest as `netdev-pod.yaml`:
         
         apiVersion: v1
         kind: Pod
         metadata:
           name: agnhost-netdev
           namespace: default
           labels:
             app: agnhost
         spec:
           containers:
           - name: agnhost
             image: registry.k8s.io/e2e-test-images/agnhost:2.39
             args: ["netexec", "--http-port", "80"]
             ports:
             - name: agnhost-port
               containerPort: 80
             resources:
               claims:
               - name: netdev
               limits:
                 google.com/tpu: 4
           nodeSelector:
             cloud.google.com/gke-tpu-accelerator: TPU_ACCELERATOR
             cloud.google.com/gke-tpu-topology: TPU_TOPOLOGY
           resourceClaims:
           - name: netdev
             resourceClaimTemplateName: all-netdev
         

Replace the following:

     * `TPU_ACCELERATOR`: The TPU accelerator type, for example, `tpu-v5p-slice`.
     * `TPU_TOPOLOGY`: The TPU topology, for example, `2x4x4`.
  4. Apply the manifest:
         
         kubectl apply -f netdev-pod.yaml
         

  5. Verify that the additional allocated network interfaces are visible inside the Pod.
         
         kubectl exec agnhost-netdev -- ls /sys/class/net
         

The following example output shows the default `eth0` and `lo` interfaces, along with the allocated network devices, which have names like `eth1` and `eth2`. The number of NICs and their names will vary based on the machine type of the GKE node.
         
         eth0
         eth1
         eth2
         lo
         




## Troubleshoot

To check the network setup for a node pool, run the following command:
    
    
    gcloud beta container node-pools describe NODE_POOL_NAME \
        --zone=ZONE \
        --cluster=CLUSTER_NAME
    

Replace the following:

  * `NODE_POOL_NAME`: the name of your node pool.
  * `ZONE`: the zone of the node pool.
  * `CLUSTER_NAME`: the name of your cluster.



The output shows the additional networks and subnetworks attached to the node pool.

## What's next

  * Read about [accelerator-optimized machines](https://docs.cloud.google.com/compute/docs/accelerator-optimized-machines).
  * Learn how to [Provision GPUs with DRA](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/set-up-dra).
  * Learn how to [Set up multi-network support for pods](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/setup-multinetwork-support-for-pods).
  * Learn about [Allocate network resources using GKE managed DRANET](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/allocate-network-resources-dra)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
