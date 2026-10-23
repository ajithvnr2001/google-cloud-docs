---
url: https://docs.cloud.google.com/kubernetes-engine/docs/how-to/allocate-network-resources-dra/
title: Allocate network resources by using GKE managed DRANET \u00a0|\u00a0 GKE networking \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:23:46.950533+00:00
---

# Allocate network resources by using GKE managed DRANET  |  GKE networking  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/docs/how-to/allocate-network-resources-dra/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ Google Kubernetes Engine (GKE) ](https://docs.cloud.google.com/kubernetes-engine/docs)
  * [ GKE networking ](https://docs.cloud.google.com/kubernetes-engine/networking/docs)
  * [ Guides ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/explore-gke-networking-docs-use-cases)



Send feedback 

#  Allocate network resources by using GKE managed DRANET Stay organized with collections  Save and categorize content based on your preferences. 

[ Autopilot ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/autopilot-overview) [ Standard ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/choose-cluster-mode)

Google Kubernetes Engine (GKE) DRANET is a managed GKE feature that builds upon the [open-source DRANET](https://github.com/kubernetes-sigs/dranet) project, which implements the Kubernetes DRA API for networking resources. DRANET lets you request and allocate high-performance networking resources for your Pods, including network interfaces that support Remote Direct Memory Access (RDMA). This approach provides a portable, upstream-aligned API for network resource management.

This document provides a conceptual overview of GKE DRANET and shows you how to allocate network resources to workloads in your GKE clusters.

This document is intended for Cloud architects and Networking specialists who design networks for their organizations. For an overview of all GKE documentation, see [Explore GKE documentation](https://docs.cloud.google.com/kubernetes-engine/docs/about). To learn about common roles and tasks referenced in Google Cloud content, see [Common GKE user roles and tasks](https://docs.cloud.google.com/kubernetes-engine/enterprise/docs/concepts/roles-tasks).

Before reading this document, ensure that you are familiar with the following:

  * [Dynamic Resource Allocation](https://kubernetes.io/docs/concepts/scheduling-eviction/dynamic-resource-allocation)
  * [About dynamic resource allocation in GKE](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/about-dynamic-resource-allocation)
  * [Kubernetes concepts](https://kubernetes.io/docs/concepts/)
  * [GKE networking](https://docs.cloud.google.com/kubernetes-engine/docs/learn/learn-gke-net-architecture)
  * [GKE Networking fundamentals](https://docs.cloud.google.com/kubernetes-engine/docs/learn/learn-gke-net-fundamentals)



## How GKE managed DRANET works

GKE managed DRANET is implemented through a `networking-dra-driver` DaemonSet. This DaemonSet runs on nodes with GPUs, TPUs, or storage-optimized VMs that have GKE DRANET enabled.

It functions as a node-level agent to make network interfaces discoverable and allocatable to Pods through the [Kubernetes Dynamic Resource Allocation (DRA) APIs](https://kubernetes.io/docs/concepts/scheduling-eviction/dynamic-resource-allocation/#api).

In GKE versions 1.34.1-gke.1829001 and later, GKE automatically installs `DeviceClass` resources for networking. These classes define the types of network devices that you can request. For example, GKE creates the `mrdma.google.com` class for GPU VMs, the `netdev.google.com` class for TPU and other network devices, and the `irdma.google.com` class for storage-optimized VMs (such as Z4M).

To use GKE DRANET, you first enable the GKE DRANET driver on a node pool with GPUs, TPUs, or storage-optimized VMs.

To request network devices for a workload, define a `ResourceClaimTemplate`. This template specifies the `DeviceClass` and the allocation mode, such as requesting all available devices on a node. In your Pod specification, reference this template in a `resourceClaims` field to grant your Pod access to the requested network interfaces on the node.

## When to use GKE managed DRANET

GKE DRANET provides a standardized way to manage network resources that are aware of topology and dependencies. This standardization makes it a suitable solution for AI and ML, large parallel file systems, and other data-intensive storage workloads that require high-performance networking.

Common use cases for requesting network interfaces for a Pod include:

  * Requesting all available RDMA-capable interfaces.
  * Requesting a specific number of RDMA-capable interfaces.
  * Requesting all available non-RDMA interfaces.
  * Requesting a specific number of non-RDMA interfaces.



## Key considerations by using GKE managed DRANET for networking

Consider the following points by using GKE DRANET for networking:

  * **Dedicated network interfaces**

When you use GKE DRANET to claim a network interface for a Pod, that interface is dedicated to that Pod. Other Pods on the same node can't share it. This approach helps ensure that the Pod has sole access to the full bandwidth and resources of that interface, which is a key benefit for performance-sensitive workloads.

  * **Use the GKE managed DRANET driver independently**

You can enable the GKE DRA driver to manage network resources without enabling other GKE DRANET drivers. To do so, add the `cloud.google.com/gke-networking-dra-driver=true` label to a node pool with GPUs, TPUs, or storage-optimized VMs.

  * **Use other GKE DRA drivers**

To achieve higher throughput in demanding AI/ML workloads, combine the DRA API for accelerators (like GPUs and TPUs) with GKE DRANET managed networking. This combined approach improves resource alignment and topology awareness. To learn more about using DRA for other resources, see [Prepare GKE infrastructure for DRA workloads](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/set-up-dra).

  * **Avoid conflicting configurations**

The GKE DRANET driver manages RDMA interfaces and gVNICs that don't have any secondary IP address ranges configured. Don't use both the GKE DRANET driver and the GKE multi-network API with a Network resource of `Device` type in the same cluster. Using the driver and API together is not supported because both APIs attempt to manage the same set of NICs, which can lead to an incorrect setup and unpredictable behavior.

  * **Managed lifecycle of the DRANET driver**

In GKE version 1.34 and later, GKE automatically creates the managed `gke-managed-networking-dra-driver` namespace in your cluster. Similar to several other GKE system workloads, the DRANET driver's Pods only run on nodes where they are relevant (such as nodes with GPUs, TPUs, and other specialized hardware). On nodes where the driver is not relevant, no Pods for this driver run. _Do not manually modify the`networking-dra-driver` DaemonSet._ Manual changes, such as updating the `nodeAffinity` field, can interfere with GKE's management of the DRANET feature and cause the DRANET daemon Pods to schedule on unsupported nodes.




## Requirements

To use GKE managed DRANET, your environment must meet the following requirements:

  * Standard: 1.34.1-gke.1829001 or later (1.36.3-gke.1767000 or later for Z4M VMs).
  * Autopilot: 1.35.2-gke.1842000 or later (1.37.0-gke.4713000 or later for Z4M VMs).
  * GKE Dataplane V2 is enabled on the cluster.



You must also use one of the following accelerator-optimized or storage-optimized machine types:

Machine series | Machine type | Accelerator model | Networking technology | DeviceClass  
---|---|---|---|---  
A3 Ultra | `a3-ultragpu-8g` | NVIDIA H200 GPU | RDMA | `mrdma.google.com`  
A4 | `a4-highgpu-8g` | NVIDIA B200 GPU | RDMA | `mrdma.google.com`  
A4X | `a4x-highgpu-4g` | NVIDIA GB200 GPU | RDMA | `mrdma.google.com`  
A4X Max | `a4x-maxgpu-4g-metal` | NVIDIA B300 GPU | RDMA | `mrdma.google.com`  
TPU v7 | `tpu7x-standard-4t` | TPU v7 | NetDevice | `netdev.google.com`  
TPU v6e | `ct6e-standard-8t` | Trillium TPU | NetDevice | `netdev.google.com`  
TPU v6e | `ct6e-standard-4t` | Trillium TPU | NetDevice | `netdev.google.com`  
TPU v6e | `ct6e-standard-1t` | Trillium TPU | NetDevice | `netdev.google.com`  
Z4M |  Any [Z4M machine type](https://docs.cloud.google.com/compute/docs/storage-optimized-machines#z4m_machine_types) that supports IRDMA  | Not applicable (storage-optimized) | RDMA | `irdma.google.com`  
  
## Limitations

GKE DRANET has the following limitations:

  * You can't use GKE DRANET to allocate the default network interface card (NIC) or virtual NICs (such as veth).
  * Certain instance types, specifically bare metal nodes like `a4x-max`, are incompatible with Autoscaling and Autopilot clusters.



## Machine-specific considerations

Depending on the underlying hardware architecture of your nodes, some machine series require additional node pool flags, container image packages, or system DaemonSets to configure RDMA interfaces with GKE DRANET.

### A4X Max bare metal

  * **Deploy asapd-lite** : When using bare metal GPU nodes, such as A4X Max, you must deploy the `asapd-lite` DaemonSet to your cluster. The `asapd-lite` DaemonSet configures the RDMA network interface cards (NICs). Without it, child interfaces aren't created, and the `dranet` driver filters out the RDMA NICs, preventing RDMA functionality within your Pods. For complete setup instructions, see [Configure the MRDMA NICs with asapd-lite](https://docs.cloud.google.com/ai-hypercomputer/docs/create/gke-create-a4x-max#configure-mrdma-nics).



### Z4M storage-optimized VMs

  * **Container image requirements** : To use RDMA on Z4M instances, you must use a Rocky Linux 8 container image configured with the required user-space RDMA packages. Other distributions, such as Ubuntu or Debian, aren't supported. Standard upstream packages for these distributions lack the custom ABI extensions that the IRDMA driver requires. Without these extensions, the packages fail at runtime with an `-ENOSPC` error. For setup instructions, see Use RDMA interfaces in a storage-optimized node pool.



## Before you begin

Before you start, make sure that you have performed the following tasks: 

  * Enable the Google Kubernetes Engine API. 
[ Enable Google Kubernetes Engine API ](https://console.cloud.google.com/apis/enableflow?apiid=container.googleapis.com)
  * To use the Google Cloud CLI for this task, [install](https://docs.cloud.google.com/sdk/docs/install) and then [initialize](https://docs.cloud.google.com/sdk/docs/initialize) the gcloud CLI. If you previously installed the gcloud CLI, get the latest version by running the `gcloud components update` command. Earlier gcloud CLI versions might not support running the commands in this document. **Note:** For existing gcloud CLI installations, make sure to set the `compute/region` [property](https://docs.cloud.google.com/sdk/docs/properties#setting_properties). If you use primarily zonal clusters, set the `compute/zone` instead. By setting a default location, you can avoid errors in the gcloud CLI like the following: `One of [--zone, --region] must be supplied: Please specify location`. You might need to specify the location in certain commands if the location of your cluster differs from the default that you set.



### Required roles

To get the permissions that you need to create node pools and allocate network resources, ask your administrator to grant you the [Kubernetes Engine Admin ](https://docs.cloud.google.com/iam/docs/roles-permissions/container#container.admin) (`roles/container.admin`) IAM role on your project. For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

You might also be able to get the required permissions through [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

## Create a cluster

Create a GKE Standard cluster that uses GKE Dataplane V2:
    
    
    gcloud container clusters create CLUSTER_NAME \
        --enable-dataplane-v2 \
        --region=CONTROL_PLANE_LOCATION \
        --project=PROJECT_ID \
        --cluster-version=CLUSTER_VERSION
    

Replace the following:

  * `CLUSTER_NAME`: the name of your new cluster.
  * `CONTROL_PLANE_LOCATION`: the region or zone for the cluster control plane, such as `us-central1` or `us-central1-a`.
  * `PROJECT_ID`: your Google Cloud project ID.
  * `CLUSTER_VERSION`: the GKE version for your cluster: 
    * **Z4M VMs** : `1.36.3-gke.1767000` or later
    * **All other supported VMs or bare metal instances** : `1.34.1-gke.1829001` or later



## Use RDMA interfaces from a GPU node pool

The following sections describe how to configure a GPU node pool and workload to use RDMA network interfaces with GKE DRANET.

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
         




## Use non-RDMA network interfaces in a TPU node pool

The following sections describe how to configure a TPU node pool and workload to use non-RDMA network interfaces with GKE DRANET.

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
         




## Use RDMA interfaces in a storage-optimized node pool

The following sections describe how to configure a storage-optimized node pool and workload to use RDMA network interfaces with GKE DRANET, by using a Z4M (`z4m-highmem-192`) VM as an example.

### Create a storage-optimized node pool

Create a storage-optimized node pool with the `--accelerator-network-profile=auto` flag so that GKE automatically provisions and attaches the underlying Falcon VPC networks, subnets, and secondary network interfaces. On Z4M node pools, GKE enables DRANET by default, so you don't need to specify the `cloud.google.com/gke-networking-dra-driver=true` node label when you create the node pool. This example uses the `z4m-highmem-192` machine type, which has dual physical Titanium NICs and provides two RDMA interfaces. For the list of supported machine types, see Requirements.
    
    
    gcloud container node-pools create NODE_POOL_NAME \
        --cluster=CLUSTER_NAME \
        --project=PROJECT_ID \
        --zone=ZONE \
        --machine-type=z4m-highmem-192 \
        --num-nodes=NUM_NODES \
        --accelerator-network-profile=auto
    

Replace the following:

  * `NODE_POOL_NAME`: the name of your new node pool.
  * `CLUSTER_NAME`: the name of your cluster.
  * `PROJECT_ID`: your Google Cloud project ID.
  * `ZONE`: the Google Cloud zone for your node pool.
  * `NUM_NODES`: the number of nodes in the node pool. To test RDMA traffic across nodes with the example `rdma-server` and `rdma-client` Pods, specify at least `2`.



### Prepare the storage-optimized workload container image

Workloads that use Cloud RDMA on storage-optimized nodes require a Rocky Linux 8 container image with the custom user-space RDMA libraries (`rdma-core`) for Cloud RDMA installed. Don't use default upstream packages; they lack the custom ABI extensions required by the host IRDMA driver and fail at runtime with `-ENOSPC` errors. To verify IP address assignments and test RDMA connectivity, also install `iproute`, `libibverbs-utils`, `librdmacm-utils`, `infiniband-diags`, and `perftest`.

For an example `Dockerfile` that configures the required package repository, see [Prepare your Docker image](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/run-hpc-workloads#prepare-docker-image). In the `dnf install` command, include `iproute` so that you can inspect IP assignments with the `ip` command. For more information about the required packages, see [Cloud RDMA RPMs](https://docs.cloud.google.com/compute/docs/images/building-custom-os#rdma-packages).

### Deploy a workload with RDMA resources

To allocate RDMA interfaces to a Pod on a storage-optimized node, create a `ResourceClaimTemplate` that requests the `irdma.google.com` `DeviceClass`:

  1. Create a `ResourceClaimTemplate` manifest and save it as `irdma-template.yaml`:
         
         apiVersion: resource.k8s.io/v1
         kind: ResourceClaimTemplate
         metadata:
           name: irdma-template
         spec:
           spec:
             devices:
               requests:
               - name: irdma
                 exactly:
                   deviceClassName: irdma.google.com
                   allocationMode: ExactCount
                   count: 2
         

In this manifest:

     * `deviceClassName: irdma.google.com`: requests IRDMA network interfaces managed by GKE DRANET on storage-optimized nodes.
     * `allocationMode: ExactCount` and `count: 2`: requests both of the IRDMA interfaces available on a `z4m-highmem-192` node. If your workload only needs a single RDMA interface, or if you use a Z4M machine type that provides one IRDMA interface, then specify `1`.
  2. Apply the manifest:
         
         kubectl apply -f irdma-template.yaml
         

  3. Create a manifest that defines two Pods, `rdma-server` and `rdma-client`, so that you can test RDMA traffic between nodes. Each Pod adds the `IPC_LOCK` capability and references the `irdma-template` `ResourceClaimTemplate`. Save the manifest as `irdma-pods.yaml`:
         
         apiVersion: v1
         kind: Pod
         metadata:
           name: rdma-server
           labels:
             app: perftest
             role: server
         spec:
           restartPolicy: Never
           affinity:
             podAntiAffinity:
               requiredDuringSchedulingIgnoredDuringExecution:
               - labelSelector:
                   matchExpressions:
                   - key: app
                     operator: In
                     values: ["perftest"]
                 topologyKey: "kubernetes.io/hostname"
           containers:
           - name: perftest
             image: IMAGE_URI
             command: ["sleep", "infinity"]
             securityContext:
               capabilities:
                 add: ["IPC_LOCK"]
             resources:
               claims:
               - name: irdma
           resourceClaims:
           - name: irdma
             resourceClaimTemplateName: irdma-template
         ---
         apiVersion: v1
         kind: Pod
         metadata:
           name: rdma-client
           labels:
             app: perftest
             role: client
         spec:
           restartPolicy: Never
           affinity:
             podAntiAffinity:
               requiredDuringSchedulingIgnoredDuringExecution:
               - labelSelector:
                   matchExpressions:
                   - key: app
                     operator: In
                     values: ["perftest"]
                 topologyKey: "kubernetes.io/hostname"
           containers:
           - name: perftest
             image: IMAGE_URI
             command: ["sleep", "infinity"]
             securityContext:
               capabilities:
                 add: ["IPC_LOCK"]
             resources:
               claims:
               - name: irdma
           resourceClaims:
           - name: irdma
             resourceClaimTemplateName: irdma-template
         

Replace both instances of `IMAGE_URI` with the URI of your Rocky Linux 8 RDMA container image.

In this manifest:

     * `metadata.labels`: labels each Pod with `app: perftest` and a `role` label. Both Pods share the `app: perftest` label so that the anti-affinity rule applies to them. The `role` label distinguishes the `rdma-server` Pod (`role: server`) from the `rdma-client` Pod (`role: client`) so that you can test Pod-to-Pod RDMA connectivity across nodes.
     * `affinity.podAntiAffinity`: prevents Kubernetes from scheduling Pods that share the `app: perftest` label on the same node. Because both Pods have this label, they run on separate physical hosts for cross-node RDMA testing, even when your `ResourceClaimTemplate` requests only one interface (`count: 1`). Your node pool must have at least two nodes to schedule both Pods.
     * `securityContext.capabilities.add: ["IPC_LOCK"]`: lets the container lock memory pages, which is required for RDMA user-space libraries to register memory regions for direct memory access.
     * `spec.resourceClaims`: generates a Pod-specific `ResourceClaim` (named `irdma`) from the `irdma-template` `ResourceClaimTemplate`.
     * `containers.resources.claims`: grants the `perftest` container access to the interfaces allocated by the `irdma` claim.
  4. Apply the manifest:
         
         kubectl apply -f irdma-pods.yaml
         

  5. Verify that the allocated RDMA interfaces (`rdma0` and `rdma1`) are visible inside the server Pod:
         
         kubectl exec rdma-server -- ip -br addr show
         

The output is similar to the following:
         
         lo               UNKNOWN        127.0.0.1/8
         rdma1            UP             10.5.0.3/32
         rdma0            UP             10.31.0.3/32
         eth0@if18        UP             10.120.2.6/32
         




To verify RDMA traffic between the two Pods, run `rping` between `rdma-server` and `rdma-client`:

  1. Start the `rping` server on the server Pod:
         
         kubectl exec -it rdma-server -- rping -s -a RDMA_IP -v -d
         

Replace `RDMA_IP` with the `rdma0` or `rdma1` IP address of the server Pod, such as `10.31.0.3`.

  2. In a second terminal, run the `rping` client on the client Pod:
         
         kubectl exec -it rdma-client -- rping -c -a RDMA_IP -C 5 -v -d
         

In the client output, verify the following indicators of a successful RDMA connection:

     * `RDMA_CM_EVENT_ADDR_RESOLVED` and `RDMA_CM_EVENT_ROUTE_RESOLVED`: confirms that the RDMA Communication Manager resolved the target RDMA IP address and route.
     * `ESTABLISHED` and `rdma_connect successful`: confirms that the client created the Queue Pair (`qp`), Completion Queue (`cq`), and Protection Domain (`pd`), and established the RDMA connection.
     * Five `send completion`, `recv completion`, and `ping data: rdma-ping-` entries: confirms that five RDMA read and write round-trip iterations completed over the RDMA interface before closing the connection (`destroy cm_id`).



## Enable DRANET with custom ComputeClass

To use GKE managed DRANET in Autopilot clusters or with [node auto-provisioning](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/node-auto-provisioning) in Standard clusters, you must use a custom ComputeClass resource to opt in to the feature.

  1. Create a ComputeClass manifest that enables the DRANET driver and sets the accelerator network profile to `auto`:
         
         apiVersion: cloud.google.com/v1
         kind: ComputeClass
         metadata:
           name: dranet-compute-class
         spec:
           nodePoolAutoCreation:
             enabled: true
           nodePoolConfig:
             dra:
               networking:
                 enabled: true
           priorities:
           - machineType: MACHINE_TYPE
             # Omit the gpu section for storage-optimized VMs (such as Z4M).
             gpu:
               count: GPU_COUNT
               type: GPU_TYPE
             acceleratorNetworkProfile: auto
         

Replace the following:

     * `MACHINE_TYPE`: the machine type for the node pool, such as `a3-ultragpu-8g` or `z4m-highmem-192`.
     * `GPU_COUNT`: the number of GPUs for the machine type.
     * `GPU_TYPE`: the type of GPU, such as `nvidia-h200`.
  2. Apply the manifest:
         
         kubectl apply -f COMPUTE_CLASS_FILENAME.yaml
         

  3. In your Pod specification, reference the ComputeClass by using the `cloud.google.com/compute-class` node selector:
         
         apiVersion: v1
         kind: Pod
         metadata:
           name: dranet-pod
         spec:
           nodeSelector:
             cloud.google.com/compute-class: "dranet-compute-class"
           ...
         




## Request a specific number of network devices

The preceding GPU and TPU examples show how to request all available network devices of a certain type by setting `allocationMode` to `All`. To request a specific number of devices instead, set `allocationMode` to `ExactCount` in your `ResourceClaimTemplate`, as shown in Deploy a workload with RDMA resources.

The following example requests two RDMA network devices:
    
    
    apiVersion: resource.k8s.io/v1
    kind: ResourceClaimTemplate
    metadata:
      name: two-mrdma
    spec:
      spec:
        devices:
          requests:
          - name: req-mrdma
            exactly:
              deviceClassName: mrdma.google.com
              allocationMode: ExactCount
              count: 2
    

## What's next

  * Learn more about [Dynamic Resource Allocation](https://kubernetes.io/docs/concepts/scheduling-eviction/dynamic-resource-allocation/).
  * Learn more about [Configure automated networking for accelerator VMs](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/config-auto-net-for-accelerators).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
