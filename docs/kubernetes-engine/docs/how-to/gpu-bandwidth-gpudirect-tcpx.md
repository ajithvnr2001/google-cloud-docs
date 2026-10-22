---
url: https://docs.cloud.google.com/kubernetes-engine/docs/how-to/gpu-bandwidth-gpudirect-tcpx/
title: Maximize GPU network bandwidth in Standard mode clusters \u00a0|\u00a0 GKE networking \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T15:01:28.108779+00:00
---

# Maximize GPU network bandwidth in Standard mode clusters  |  GKE networking  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/docs/how-to/gpu-bandwidth-gpudirect-tcpx/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ Google Kubernetes Engine (GKE) ](https://docs.cloud.google.com/kubernetes-engine/docs)
  * [ GKE networking ](https://docs.cloud.google.com/kubernetes-engine/networking/docs)
  * [ Guides ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/explore-gke-networking-docs-use-cases)



Send feedback 

#  Maximize GPU network bandwidth in Standard mode clusters Stay organized with collections  Save and categorize content based on your preferences. 

[ Standard ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/choose-cluster-mode)

This page shows you how to maximize network bandwidth and throughput for high-performance GPU workloads in Google Kubernetes Engine (GKE) Standard clusters by using GPUDirect-TCPXO, GPUDirect-TCPX, gVNIC, and multi-networking. If you use Autopilot clusters, see [Maximize GPU network bandwidth in Autopilot mode clusters](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/gpu-bandwidth-gpudirect-tcpx-autopilot). 

This page is intended for machine learning (ML) engineers and platform administrators who facilitate ML workloads. To learn more about common roles and example tasks that we reference in Google Cloud content, see [Common GKE user roles and tasks](https://docs.cloud.google.com/kubernetes-engine/enterprise/docs/concepts/roles-tasks).

Artificial intelligence (AI), ML, and high performance computing (HPC) applications require powerful acceleration to optimize performance by reducing job completion times. For example, ML models that focus on conversational AI and image generation require high scalability and compute power.

Before reading this page, ensure that you're familiar with networking technologies, such as network interface cards (NICs) and TCP, and with accelerator technologies like the NVIDIA Collective Communications Library (NCCL).

## About Google Cloud GPU machine types

Google Cloud offers different machine types to support your various workloads. The [accelerator-optimized A series machine types](https://docs.cloud.google.com/compute/docs/gpus)—especially the later generation A series—are ideal for scalable, massive models. These GPU machine types can get up to 3,600 Gbps of network bandwidth.

Your GKE workload must use all available GPUs and all available secondary NICs on a single node and use a significant portion of the available bandwidth. The solution described in this document is ideal for workloads that require high performance, high throughput, and low latency.

### Required features and capabilities for maximized bandwidth

To maximize your network bandwidth in A3 machine series—including the A3 Mega and A3 High machine types used for the instructions here—use **all** of the following features:

  * **GPUDirect networking stack** : The A3 machine series supports three networking stacks for custom, remote direct memory access (RDMA): 
    * On A3 High and A3 Edge machine types and NVIDIA H100 GPUs, use _GPUDirect-TCPX_ to reduce the overhead required to transfer packet payloads to and from GPUs, which significantly improves throughput at scale compared to GPUs that don't use GPUDirect.
    * On A3 Mega machine types and NVIDIA H100 Mega GPUs, use _GPUDirect-TCPXO_ which further improves GPU to VM communication.
    * On A3 Ultra machine types and NVIDIA H200 GPUs, and later machine series such as A4, A4X, and A4X Max, use _GPUDirect RDMA_ to run distributed AI workloads with further throughput improvements. To get started, [create an AI-optimized GKE cluster that uses A4 or A3 Ultra](https://docs.cloud.google.com/ai-hypercomputer/docs/create/gke-create-a4-a3-ultra).
  * **gVNIC** : Enable GPUDirect capabilities such as packet header splitting, flow steering, and buffer management. gVNIC is required to use GPUDirect-TCPX or GPUDirect-TCPXO. For details about gVNIC, see [Increase network traffic speed for GPU nodes](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/using-gvnic).
  * **Multi-networking** : Add secondary NICs to the accelerator-optimized machine. Each NIC is associated with a separate subnet in its own VPC to avoid conflicts. For details about multi-network support, see [Setup multi-network support for Pods](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/setup-multinetwork-support-for-pods).
  * **Placement policies** : Use a resource placement policy to place all GPU nodes for a specific workload on physically close servers to minimize latency. For details, see [Define compact placement for GKE nodes](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/compact-placement).



### Procedure outline

To use all of these capabilities together, you'll do the following:

  1. Create Virtual Private Cloud (VPC)s and subnets
  2. Create the GKE environment
  3. Install the GPUDirect binary and the NCCL plugin
  4. Deploy the NRI device injector plugin
  5. Deploy a test workload to verify GPUDirect setup
  6. Adopt GPUDirect for your own workloads



## Before you begin

Before you start, make sure that you have performed the following tasks: 

  * Enable the Google Kubernetes Engine API. 
[ Enable Google Kubernetes Engine API ](https://console.cloud.google.com/apis/enableflow?apiid=container.googleapis.com)
  * To use the Google Cloud CLI for this task, [install](https://docs.cloud.google.com/sdk/docs/install) and then [initialize](https://docs.cloud.google.com/sdk/docs/initialize) the gcloud CLI. If you previously installed the gcloud CLI, get the latest version by running the `gcloud components update` command. Earlier gcloud CLI versions might not support running the commands in this document. **Note:** For existing gcloud CLI installations, make sure to set the `compute/region` [property](https://docs.cloud.google.com/sdk/docs/properties#setting_properties). If you use primarily zonal clusters, set the `compute/zone` instead. By setting a default location, you can avoid errors in the gcloud CLI like the following: `One of [--zone, --region] must be supplied: Please specify location`. You might need to specify the location in certain commands if the location of your cluster differs from the default that you set.


  * Ensure that you have capacity for A3 Mega or A3 High VMs. To obtain this capacity, first, choose from the [consumption options](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/consumption-option#choose-consumption-options). To follow the instructions on this page, you can use either on-demand capacity, on-demand reservations, Future reservations, or Future reservations for up to 90 days (in calendar mode). After you've chosen a consumption option, follow the respective instructions to obtain capacity using the consumption option that you've chosen.
  * Ensure that you have enough quota for H100 GPUs. To request more quota, see [GPU quotas](https://docs.cloud.google.com/compute/resource-usage#gpu_quota).



### Requirements

The following requirements apply to both GPUDirect-TCPX and GPUDirect-TCPXO unless otherwise indicated.

  * GPUDirect-TCPX requires the `a3-highgpu-8g` machine type and is supported with all [available GKE minor versions](https://docs.cloud.google.com/kubernetes-engine/docs/release-schedule#schedule-for-release-channels) using specific patch versions:

    * For GKE version 1.30 to 1.33, use any patch version.
    * For GKE version 1.34, use patch version 1.34.5-gke.1153000 or later.
    * For GKE version 1.35, use patch version 1.35.2-gke.1485000 or later.
    * For GKE version 1.36 or later, use any patch version.
  * GPUDirect-TCPXO requires the `a3-megagpu-8g` machine type and is supported with all [available GKE minor versions](https://docs.cloud.google.com/kubernetes-engine/docs/release-schedule#schedule-for-release-channels) using specific patch versions:

    * For GKE version 1.30, use GKE patch version 1.30.4-gke.1129000 or later.
    * For GKE version 1.31, use GKE patch version 1.31.1-gke.2008000 or later.
    * For GKE version 1.32, use GKE patch version 1.32.2-gke.1489001 or later.
    * For GKE version 1.33 or any later minor version, use any patch version.
  * The GKE node must use a Container-Optimized OS (COS) node image. Ubuntu and Windows node images are not supported.



  * Your GPU nodes must use NVIDIA driver version 535 or later.
  * You must use GKE Dataplane V2.
  * On GKE version 1.34 and later, you must use version 3.1.9 or later of the GPUDirect-TCPX installer and version 2.0.12 or later of the GPUDirect-TCPX sidecar. The installer and sidecar versions have a one-to-one mapping and must correspond. For example, installer version 3.1.12 corresponds to sidecar version 2.0.15. For more information about installer and sidecar versions, see [GPUDirect-TCPX Release Notes](https://github.com/GoogleCloudPlatform/container-engine-accelerators/tree/master/gpudirect-tcpx).
  * For GPUDirect-TCPX or GPUDirect-TCPXO workloads that run across multiple node pools, all of the node pools must be in the same Compute Engine zones and must use the same network sets, such as VPCs and subnets.



### Limitations

The following limitations apply:

  * GPUDirect-TCPX and GPUDirect-TCPXO are not supported with [multi-instance GPUs](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/gpus-multi), [GPU time-sharing](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/timesharing-gpus), or [NVIDIA MPS](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/nvidia-mps-gpus).
  * You can't use [NCCL FastSocket](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/nccl-fast-socket) with GPUDirect-TCPX or GPUDirect-TCPXO.
  * Your GKE workload **must** use all available GPUs and all available secondary NICs on a single node. Multiple pods cannot use GPUDirect-TCPX or GPUDirect-TCPXO on a single node. 
  * You can only use the `a3-highgpu-8g`, `a3-megagpu-8g`, and `a3-edgegpu-8g` machine types. Other A3 machine types aren't supported.



## Create VPCs and subnets

Create separate VPC networks in your project for each virtual NIC that you'll add to your nodes. Each VPC network must have a subnet and a firewall rule that allows internal network traffic.

  1. Create the VPC networks for GPUDirect in your project, each with a subnet and a firewall rule. Choose the GPUDirect-TCPX tab for A3 High machine types, or choose the GPUDirect-TCPXO tab for A3 Mega machine types, then complete the following instructions:

### GPUDirect-TCPXO

To maximize your bandwidth, we recommend that you create eight new networks.
         
         for N in $(seq 1 8); do
         gcloud compute networks create PREFIX-net-$N \
             --subnet-mode=custom \
             --mtu=8244
         
         gcloud compute networks subnets create PREFIX-sub-$N \
             --network=PREFIX-net-$N \
             --region=REGION \
             --range=SUBNET_RANGE
         
         gcloud compute firewall-rules create PREFIX-internal-$N \
           --network=PREFIX-net-$N \
           --action=ALLOW \
           --rules=tcp:0-65535,udp:0-65535,icmp \
           --source-ranges=SOURCE_RANGE
         done
         

Replace the following:

     * `PROJECT_ID`: your Google Cloud project ID.
     * `REGION`: the Compute Engine region for each subnet.
     * `SUBNET_RANGE`: the IP address range of each subnet in CIDR notation. This example command iterates for eight subnets, so you should use a variable to change the IP address for each subnet. For example, specify `192.168.$N.0/24` so that the first subnet uses `192.168.1.0/24`, the second subnet uses `192.168.2.0/24`, and so on.
     * `SOURCE_RANGE`: The source IP address range for the firewall rule to allow ingress traffic, in CIDR notation. For example, `192.168.0.0/16`.

### GPUDirect-TCPX

To maximize your bandwidth, we recommend that you create four new networks.
    
    for N in $(seq 1 4); do
    gcloud compute networks create PREFIX-net-$N \
        --subnet-mode=custom \
        --mtu=8244
    
    gcloud compute networks subnets create PREFIX-sub-$N \
        --network=PREFIX-net-$N \
        --region=REGION \
        --range=SUBNET_RANGE
    
    gcloud compute firewall-rules create PREFIX-internal-$N \
      --network=PREFIX-net-$N \
      --action=ALLOW \
      --rules=tcp:0-65535,udp:0-65535,icmp \
      --source-ranges=SOURCE_RANGE
    done
    

Replace the following:

     * `PROJECT_ID`: your Google Cloud project ID.
     * `REGION`: the Compute Engine region for each subnet.
     * `SUBNET_RANGE`: the IP address range of each subnet in CIDR notation. This example command iterates for four subnets, so you should use a variable to change the IP address for each subnet. For example, specify `192.168.$N.0/24` so that the first subnet uses `192.168.1.0/24`, the second subnet uses `192.168.2.0/24`, etc.
     * `SOURCE_RANGE`: The source IP address range for the firewall rule to allow ingress traffic, in CIDR notation. For example, `192.168.0.0/16`.

  2. Verify that the networks were created:
         
         gcloud compute networks list
         




## Create the GKE environment

Create a new GKE cluster that uses multi-networking (Preview) and create a GPU node pool that has the following characteristics: 

  * gVNIC enabled
  * Multi-networking subnets specified for each secondary NIC
  * A3 machine series with H100 GPUs backing the nodes
  * Latest NVIDIA drivers installed



You can't update an existing cluster to use multi-networking. 

### GPUDirect-TCPXO

  1. Choose an available GKE version that supports GPUDirect-TCPXO. To list the versions, run this command:
         
         gcloud container get-server-config \
             --format="yaml(validMasterVersions)" \
             --region=REGION \
             --project=PROJECT_ID
         

Replace the following:

     * `REGION`: the [compute region](https://docs.cloud.google.com/compute/docs/regions-zones#available) for the cluster control plane.
     * `PROJECT_ID`: your Google Cloud project ID.
  2. Create a cluster:
         
         gcloud beta container clusters create CLUSTER_NAME \
           --enable-dataplane-v2 \
           --enable-ip-alias \
           --location=CONTROL_PLANE_LOCATION \
           --enable-multi-networking \
           --cluster-version=VERSION \
           --no-enable-autoupgrade \
           --project=PROJECT_ID
         

Replace the following:

     * `CLUSTER_NAME`: the name of your new cluster.
     * `VERSION`: a GKE version that supports GPUDirect-TCPXO, as described in Requirements.
     * `CONTROL_PLANE_LOCATION`: the Compute Engine [location](https://docs.cloud.google.com/compute/docs/regions-zones#available) of the control plane of your cluster. Provide a region for regional clusters, or a zone for zonal clusters. 
  3. Create Network and GKENetworkParamSet resources in the cluster that correspond to the VPC networks and subnetworks that you created:
         
         kubectl apply -f - <<EOF
         apiVersion: networking.gke.io/v1
         kind: Network
         metadata:
           name: vpc1
         spec:
           parametersRef:
             group: networking.gke.io
             kind: GKENetworkParamSet
             name: vpc1
           type: Device
         ---
         apiVersion: networking.gke.io/v1
         kind: Network
         metadata:
           name: vpc2
         spec:
           parametersRef:
             group: networking.gke.io
             kind: GKENetworkParamSet
             name: vpc2
           type: Device
         ---
         apiVersion: networking.gke.io/v1
         kind: Network
         metadata:
           name: vpc3
         spec:
           parametersRef:
             group: networking.gke.io
             kind: GKENetworkParamSet
             name: vpc3
           type: Device
         ---
         apiVersion: networking.gke.io/v1
         kind: Network
         metadata:
           name: vpc4
         spec:
           parametersRef:
             group: networking.gke.io
             kind: GKENetworkParamSet
             name: vpc4
           type: Device
         ---
         apiVersion: networking.gke.io/v1
         kind: Network
         metadata:
           name: vpc5
         spec:
           parametersRef:
             group: networking.gke.io
             kind: GKENetworkParamSet
             name: vpc5
           type: Device
         ---
         apiVersion: networking.gke.io/v1
         kind: Network
         metadata:
           name: vpc6
         spec:
           parametersRef:
             group: networking.gke.io
             kind: GKENetworkParamSet
             name: vpc6
           type: Device
         ---
         apiVersion: networking.gke.io/v1
         kind: Network
         metadata:
           name: vpc7
         spec:
           parametersRef:
             group: networking.gke.io
             kind: GKENetworkParamSet
             name: vpc7
           type: Device
         ---
         apiVersion: networking.gke.io/v1
         kind: Network
         metadata:
           name: vpc8
         spec:
           parametersRef:
             group: networking.gke.io
             kind: GKENetworkParamSet
             name: vpc8
           type: Device
         ---
         apiVersion: networking.gke.io/v1
         kind: GKENetworkParamSet
         metadata:
           name: vpc1
         spec:
           vpc: PREFIX-net-1
           vpcSubnet: PREFIX-sub-1
           deviceMode: NetDevice
         ---
         apiVersion: networking.gke.io/v1
         kind: GKENetworkParamSet
         metadata:
           name: vpc2
         spec:
           vpc: PREFIX-net-2
           vpcSubnet: PREFIX-sub-2
           deviceMode: NetDevice
         ---
         apiVersion: networking.gke.io/v1
         kind: GKENetworkParamSet
         metadata:
           name: vpc3
         spec:
           vpc: PREFIX-net-3
           vpcSubnet: PREFIX-sub-3
           deviceMode: NetDevice
         ---
         apiVersion: networking.gke.io/v1
         kind: GKENetworkParamSet
         metadata:
           name: vpc4
         spec:
           vpc: PREFIX-net-4
           vpcSubnet: PREFIX-sub-4
           deviceMode: NetDevice
         ---
         apiVersion: networking.gke.io/v1
         kind: GKENetworkParamSet
         metadata:
           name: vpc5
         spec:
           vpc: PREFIX-net-5
           vpcSubnet: PREFIX-sub-5
           deviceMode: NetDevice
         ---
         apiVersion: networking.gke.io/v1
         kind: GKENetworkParamSet
         metadata:
           name: vpc6
         spec:
           vpc: PREFIX-net-6
           vpcSubnet: PREFIX-sub-6
           deviceMode: NetDevice
         ---
         apiVersion: networking.gke.io/v1
         kind: GKENetworkParamSet
         metadata:
           name: vpc7
         spec:
           vpc: PREFIX-net-7
           vpcSubnet: PREFIX-sub-7
           deviceMode: NetDevice
         ---
         apiVersion: networking.gke.io/v1
         kind: GKENetworkParamSet
         metadata:
           name: vpc8
         spec:
           vpc: PREFIX-net-8
           vpcSubnet: PREFIX-sub-8
           deviceMode: NetDevice
         EOF
         

These resources tell GKE to configure the NICs for GPU traffic in passthrough mode. GKE doesn't apply built-in networking programming using eBPF to this traffic.




### GPUDirect-TCPX

  1. Create a cluster:
         
         gcloud beta container clusters create CLUSTER_NAME \
           --enable-dataplane-v2 \
           --enable-ip-alias \
           --location=CONTROL_PLANE_LOCATION \
           --enable-multi-networking \
           --cluster-version=VERSION \
           --no-enable-autoupgrade \
           --project=PROJECT_ID
         

Replace the following:

     * `CLUSTER_NAME`: the name of your new cluster.
     * `CONTROL_PLANE_LOCATION`: the Compute Engine [location](https://docs.cloud.google.com/compute/docs/regions-zones#available) of the control plane of your cluster. Provide a region for regional clusters, or a zone for zonal clusters.
     * `VERSION`: a GKE version that supports GPUDirect-TCPX, as described in Requirements.
  2. Create Network and GKENetworkParamSet resources in the cluster that correspond to the VPC networks and subnetworks that you created:
         
         kubectl apply -f - <<EOF
         apiVersion: networking.gke.io/v1
         kind: Network
         metadata:
           name: vpc1
         spec:
           parametersRef:
             group: networking.gke.io
             kind: GKENetworkParamSet
             name: vpc1
           type: Device
         ---
         apiVersion: networking.gke.io/v1
         kind: Network
         metadata:
           name: vpc2
         spec:
           parametersRef:
             group: networking.gke.io
             kind: GKENetworkParamSet
             name: vpc2
           type: Device
         ---
         apiVersion: networking.gke.io/v1
         kind: Network
         metadata:
           name: vpc3
         spec:
           parametersRef:
             group: networking.gke.io
             kind: GKENetworkParamSet
             name: vpc3
           type: Device
         ---
         apiVersion: networking.gke.io/v1
         kind: Network
         metadata:
           name: vpc4
         spec:
           parametersRef:
             group: networking.gke.io
             kind: GKENetworkParamSet
             name: vpc4
           type: Device
         ---
         apiVersion: networking.gke.io/v1
         kind: GKENetworkParamSet
         metadata:
           name: vpc1
         spec:
           vpc: PREFIX-net-1
           vpcSubnet: PREFIX-sub-1
           deviceMode: NetDevice
         ---
         apiVersion: networking.gke.io/v1
         kind: GKENetworkParamSet
         metadata:
           name: vpc2
         spec:
           vpc: PREFIX-net-2
           vpcSubnet: PREFIX-sub-2
           deviceMode: NetDevice
         ---
         apiVersion: networking.gke.io/v1
         kind: GKENetworkParamSet
         metadata:
           name: vpc3
         spec:
           vpc: PREFIX-net-3
           vpcSubnet: PREFIX-sub-3
           deviceMode: NetDevice
         ---
         apiVersion: networking.gke.io/v1
         kind: GKENetworkParamSet
         metadata:
           name: vpc4
         spec:
           vpc: PREFIX-net-4
           vpcSubnet: PREFIX-sub-4
           deviceMode: NetDevice
         EOF
         

These resources tell GKE to configure the NICs for GPU traffic in passthrough mode. GKE doesn't apply built-in networking programming using eBPF to this traffic.




### Create a GPU node pool

**Best practice** : After you create the cluster, create a separate node pool to run the GPUs.

### GPUDirect-TCPXO

Create a node pool for the H100 GPUs:
    
    
    gcloud beta container node-pools create NODE_POOL_NAME \
        --location=CONTROL_PLANE_LOCATION \
        --cluster=CLUSTER_NAME \
        --project=PROJECT_ID \
        --accelerator=type=nvidia-h100-mega-80gb,count=8,gpu-driver-version=LATEST \
        --machine-type=a3-megagpu-8g \
        --num-nodes=2 \
        --additional-node-network network=PREFIX-net-1,subnetwork=PREFIX-sub-1 \
        --additional-node-network network=PREFIX-net-2,subnetwork=PREFIX-sub-2 \
        --additional-node-network network=PREFIX-net-3,subnetwork=PREFIX-sub-3 \
        --additional-node-network network=PREFIX-net-4,subnetwork=PREFIX-sub-4 \
        --additional-node-network network=PREFIX-net-5,subnetwork=PREFIX-sub-5 \
        --additional-node-network network=PREFIX-net-6,subnetwork=PREFIX-sub-6 \
        --additional-node-network network=PREFIX-net-7,subnetwork=PREFIX-sub-7 \
        --additional-node-network network=PREFIX-net-8,subnetwork=PREFIX-sub-8 \
        --enable-gvnic \
        --no-enable-autoupgrade \
        --scopes "https://www.googleapis.com/auth/cloud-platform" [\
        --placement-policy=POLICY_NAME \
        --reservation-affinity=specific \
        --reservation=projects/PROJECT_ID/reservations/RESERVATION_NAME/reservationBlocks/BLOCK_NAME \
        --host-maintenance-interval=PERIODIC]
    

Replace `NODE_POOL_NAME` with your node pool name.

In the example, the `--scopes` "https://www.googleapis.com/auth/cloud-platform" argument sets the node instance's scope to be `cloud-platform` for testing convenience. For production, you may want to limit the scope to configure finer-grained credentials.

To use a reservation, use the `--placement-policy`, `--reservation-affinity`, and `--reservation` flags. Specify these flags to configure the policy name and reservation in the node pool. If the reservation doesn't require a resource policy, omit the `--placement-policy` flag.

The `--reservation-affinity` flag can take the values of `specific` or `any`. However, for high performance distributed AI workloads, we recommend that you use a specific reservation. You can find information about your reservation, such as the name of your reservation or the name of a specific block in your reservation. To find these values for on-demand reservations, [view a list of your reservations](https://docs.cloud.google.com/compute/docs/hpc/view-reserved-capacity#list-reservations), or, [view future reservation requests](https://docs.cloud.google.com/compute/docs/instances/reservations-view#view-future-reservations).

Replace the following to use a reservation:

  * `PROJECT_ID`: optionally, your Google Cloud project ID. If the reservation is located in the current project (not a [shared reservation](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/consuming-reservations#specific_shared)) you can omit `projects/PROJECT_ID/reservations/` from the reservation value.
  * `RESERVATION_NAME`: the name of your reservation.
  * `BLOCK_NAME`: optionally, the name of a specific block within the reservation. Omit `/reservationBlocks/BLOCK_NAME` if you don't want to use a specific block.



If this command fails, you might not have enough H100 GPU quota in your project. Ensure that you have quota and retry the command.

### GPUDirect-TCPX

Create a node pool for the H100 GPUs:
    
    
    gcloud container node-pools create NODE_POOL_NAME \
        --cluster=CLUSTER_NAME \
        --location=CONTROL_PLANE_LOCATION \
        --machine-type=a3-highgpu-8g \
        --accelerator=type=nvidia-h100-80gb,count=8,gpu-driver-version=LATEST \
        --additional-node-network=network=PREFIX-net-1,subnetwork=PREFIX-sub-1 \
        --additional-node-network=network=PREFIX-net-2,subnetwork=PREFIX-sub-2 \
        --additional-node-network=network=PREFIX-net-3,subnetwork=PREFIX-sub-3 \
        --additional-node-network=network=PREFIX-net-4,subnetwork=PREFIX-sub-4 \
        --enable-gvnic \
        --no-enable-autoupgrade [\
        --placement-policy=POLICY_NAME \
        --reservation-affinity=specific \
        --reservation=projects/PROJECT_ID/reservations/RESERVATION_NAME/reservationBlocks/BLOCK_NAME]
    

Replace `NODE_POOL_NAME` with the name of the node pool.

To use a reservation, use the `--placement-policy`, `--reservation-affinity`, and `--reservation` flags. Specify these flags to configure the policy name and reservation in the node pool. If the reservation doesn't require a resource policy, omit the `--placement-policy` flag.

The `--reservation-affinity` flag can take the values of `specific` or `any`. However, for high performance distributed AI workloads, we recommend that you use a specific reservation. You can find information about your reservation, such as the name of your reservation or the name of a specific block in your reservation. To find these values for on-demand reservations, [view a list of your reservations](https://docs.cloud.google.com/compute/docs/hpc/view-reserved-capacity#list-reservations), or, [view future reservation requests](https://docs.cloud.google.com/compute/docs/instances/reservations-view#view-future-reservations).

Replace the following to use a reservation:

  * `PROJECT_ID`: optionally, your Google Cloud project ID. If the reservation is located in the current project (not a [shared reservation](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/consuming-reservations#specific_shared)) you can omit `projects/PROJECT_ID/reservations/` from the reservation value.
  * `RESERVATION_NAME`: the name of your reservation.
  * `BLOCK_NAME`: optionally, the name of a specific block within the reservation. Omit `/reservationBlocks/BLOCK_NAME` if you don't want to use a specific block.



If this command fails, you might not have enough H100 GPU quota in your project. Ensure that you have quota and retry the command.

After you create the node pool, verify that each node has the attached GPUs:

  1. Get a list of nodes in the cluster:
         
         kubectl get nodes
         

  2. Verify that each GPU node has eight GPUs:
         
         kubectl describe node NODE_NAME
         

Replace `NODE_NAME` with the name of the node to describe.

The output is similar to the following:
         
         Capacity:
           ...
           nvidia.com/gpu:             8
         Allocatable:
           ...
           nvidia.com/gpu:             8
         




## Install the GPUDirect binary and configure NCCL

This section shows you how to install the GPUDirect binary, based on your A3 machine type (GPUDirect-TCPX for A3 High, GPUDirect-TCPXO for A3 Mega) and a specific NCCL library version using a DaemonSet.

### GPUDirect-TCPXO

This DaemonSet does the following:

  1. Pre-installation to setup GPUDirect-TCPXO related configurations.
  2. Installs the NCCL library and GPUDirect-TCPXO binary on the node.
  3. Stores the library and the binary in the `/home/kubernetes/bin/nvidia/lib64` directory on the VM. By default, GKE mounts this directory into the `/usr/local/nvidia/lib64` path in GPU containers that need to use NCCL and GPUDirect-TCPXO.



To install the binary and configure NCCL, do the following steps:

  1. Review the [`nccl-tcpxo-installer.yaml` Daemonset manifest in GitHub](https://raw.githubusercontent.com/GoogleCloudPlatform/container-engine-accelerators/master/gpudirect-tcpxo/nccl-tcpxo-installer.yaml).

  2. Deploy the DaemonSet:
         
         kubectl apply -f https://raw.githubusercontent.com/GoogleCloudPlatform/container-engine-accelerators/master/gpudirect-tcpxo/nccl-tcpxo-installer.yaml
         

The NCCL plugin takes approximately two minutes to start running.

  3. Verify the status of the DaemonSet Pods:
         
         kubectl get pods -n=kube-system -l=name=nccl-tcpxo-installer
         

The output is similar to the following:
         
         # Output
         nccl-tcpxo-installer-6c2pv                    1/1     Running   0          2m11s
         nccl-tcpxo-installer-qgg82                    1/1     Running   0          2m11s
         




### GPUDirect-TCPX

This DaemonSet does the following:

  1. Installs the NCCL library and GPUDirect-TCPX binary on the node.
  2. Stores the library and the binary in the `/home/kubernetes/bin/nvidia/lib64` directory on the VM. By default, GKE mounts this directory into the `/usr/local/nvidia/lib64` path in GPU containers that need to use NCCL and GPUDirect-TCPX.



To install the binary and configure NCCL, do the following:

  1. Review the [`nccl-tcpx-installer.yaml` Daemonset manifest in GitHub](https://raw.githubusercontent.com/GoogleCloudPlatform/container-engine-accelerators/master/gpudirect-tcpx/nccl-tcpx-installer.yaml).

  2. Deploy the DaemonSet:
         
         kubectl apply -f https://raw.githubusercontent.com/GoogleCloudPlatform/container-engine-accelerators/master/gpudirect-tcpx/nccl-tcpx-installer.yaml
         

The NCCL plugin takes approximately two minutes to start running.

  3. Verify the status of the DaemonSet Pods:
         
         kubectl get pods -n=kube-system -l=name=nccl-tcpx-installer
         

The output is similar to the following:
         
         nccl-tcpx-installer-6c2pv                    1/1     Running   0          2m11s
         nccl-tcpx-installer-qgg82                    1/1     Running   0          2m11s
         




## Deploy NRI device injector plugin

This section shows you how to install the NRI device injector by using a DaemonSet. Both H100 GPU machine types install the same NRI device injector plugin. This plugin does the following:

  1. Enables Node Resource Interface (NRI) on the node that has H100 GPUs. NRI is enabled by default on GKE version 1.29 and later.
  2. Deploys a NRI device injector plugin container that injects GPU devices into containers specified by Pod annotations.



To install the plugin, do the following:

  1. Review the [`nri-device-injector.yaml` Deployment manifest in GitHub](https://raw.githubusercontent.com/GoogleCloudPlatform/container-engine-accelerators/master/nri_device_injector/nri-device-injector.yaml).

  2. Deploy the DaemonSet:
         
         kubectl apply -f https://raw.githubusercontent.com/GoogleCloudPlatform/container-engine-accelerators/master/nri_device_injector/nri-device-injector.yaml
         

The NCCL plugin takes approximately two minutes to start running.

  3. Verify the status of the DaemonSet Pods:
         
         kubectl get pods -n=kube-system -l=name=device-injector
         

The output is similar to the following:
         
         # Output
         device-injector-md6hb                         1/1     Running   0       4h54m
         device-injector-vh9bm                         1/1     Running   0       4h54m
         




## Deploy a test workload

In this section, you deploy a sample workload to verify that NCCL and GPUDirect-TCPX or GPUDirect-TCPXO work as expected. This sample workload does the following:

  1. Deploys two Pods, each of which runs in a node that has H100 GPUs.
  2. Deploys a sidecar container in each Pod to let those Pods use GPUDirect-TCPXO or GPUDirect-TCPX.



To deploy this sample workload, do the following:

### GPUDirect-TCPXO

This workload includes a sidecar container named the _tcpxo-daemon_ , which runs a service that lets the Pod use GPUDirect-TCPXO. **You must add this sidecar container to any Pods in your own environment that need to use GPUDirect-TCPXO.** For a snippet of the required fields to add to your manifests, see Add GPUDirect to your manifest.

  1. Review the [`nccl-test-latest.yaml` manifest in GitHub](https://raw.githubusercontent.com/GoogleCloudPlatform/container-engine-accelerators/master/gpudirect-tcpxo/nccl-test-latest.yaml). 

  2. Deploy two Pods with the test workload:
         
         kubectl apply -f https://raw.githubusercontent.com/GoogleCloudPlatform/container-engine-accelerators/master/gpudirect-tcpxo/nccl-test-latest.yaml
         

  3. Verify that the Pods are running and ready. Note that the images are large (approximately 5 GB) and can take several minutes to download.
         
         kubectl get pods -w
         

The command watches for updates and prints a new line when a Pod's status changes. The output is similar to the following:
         
         NAME               READY   STATUS              RESTARTS   AGE
         nccl-test-host-1   0/2     ContainerCreating   0          23s
         nccl-test-host-2   2/2     Running             0          23s
         nccl-test-host-1   2/2     Running             0          46s
         

Wait until the `STATUS` message for all Pods is `Running` and the value of `READY` is `2/2` before proceeding to the next step.

  4. After the Pods deploy, trigger an all-gather test:
         
         kubectl exec --stdin --tty --container=nccl-test nccl-test-host-1 -- /scripts/allgather.sh nccl-host-1 nccl-host-2
         

The output is similar to the following:
         
         #                                                              out-of-place                       in-place
         #        size         count      type   redop    root     time   algbw   busbw #wrong     time   algbw   busbw #wrong
         #         (B)    (elements)                               (us)  (GB/s)  (GB/s)            (us)  (GB/s)  (GB/s)
                     0             0     float    none      -1     0.24    0.00    0.00      0     0.18    0.00    0.00      0
                     0             0     float    none      -1     0.19    0.00    0.00      0     0.17    0.00    0.00      0
                     0             0     float    none      -1     0.17    0.00    0.00      0     0.17    0.00    0.00      0
                     0             0     float    none      -1     0.17    0.00    0.00      0     0.17    0.00    0.00      0
                     0             0     float    none      -1     0.17    0.00    0.00      0     0.17    0.00    0.00      0
                   256             4     float    none      -1    235.2    0.00    0.00      0    235.1    0.00    0.00      0
                   512             8     float    none      -1    241.0    0.00    0.00      0    236.1    0.00    0.00      0
                  1024            16     float    none      -1    236.3    0.00    0.00      0    233.3    0.00    0.00      0
                  2048            32     float    none      -1    234.1    0.01    0.01      0    233.4    0.01    0.01      0
                  4096            64     float    none      -1    237.1    0.02    0.02      0    235.3    0.02    0.02      0
                  8192           128     float    none      -1    236.2    0.03    0.03      0    235.2    0.03    0.03      0
                 16384           256     float    none      -1    236.6    0.07    0.06      0    238.5    0.07    0.06      0
                 32768           512     float    none      -1    237.9    0.14    0.13      0    238.8    0.14    0.13      0
                 65536          1024     float    none      -1    242.3    0.27    0.25      0    239.4    0.27    0.26      0
                131072          2048     float    none      -1    263.0    0.50    0.47      0    275.1    0.48    0.45      0
                262144          4096     float    none      -1    279.2    0.94    0.88      0    269.9    0.97    0.91      0
                524288          8192     float    none      -1    273.5    1.92    1.80      0    273.5    1.92    1.80      0
               1048576         16384     float    none      -1    315.1    3.33    3.12      0    314.1    3.34    3.13      0
               2097152         32768     float    none      -1    319.2    6.57    6.16      0    311.5    6.73    6.31      0
               4194304         65536     float    none      -1    331.8   12.64   11.85      0    331.3   12.66   11.87      0
               8388608        131072     float    none      -1    356.3   23.54   22.07      0    353.8   23.71   22.23      0
              16777216        262144     float    none      -1    409.1   41.01   38.45      0    405.2   41.40   38.81      0
              33554432        524288     float    none      -1    451.4   74.34   69.69      0    447.7   74.94   70.26      0
              67108864       1048576     float    none      -1    713.4   94.07   88.19      0    713.8   94.01   88.13      0
             134217728       2097152     float    none      -1   1122.1  119.62  112.14      0   1116.3  120.23  112.72      0
             268435456       4194304     float    none      -1   1785.8  150.32  140.92      0   1769.2  151.72  142.24      0
             536870912       8388608     float    none      -1   2859.7  187.74  176.00      0   2852.6  188.20  176.44      0
            1073741824      16777216     float    none      -1   5494.1  195.44  183.22      0   5568.2  192.83  180.78      0
            2147483648      33554432     float    none      -1    10841  198.09  185.71      0    10798  198.88  186.45      0
            4294967296      67108864     float    none      -1    21453  200.21  187.70      0    21490  199.86  187.37      0
            8589934592     134217728     float    none      -1    42603  201.63  189.03      0    42670  201.31  188.73      0
         # Out of bounds values : 0 OK
         # Avg bus bandwidth    : 45.7587
         #
         

**Success:** At this point, you've successfully installed GPUDirect-TCPXO on your nodes and can use it to optimize the throughput of GPU-heavy workloads that run on those nodes. The required fields to use GPUDirect-TCPXO in your own Pods are described in Add GPUDirect to your manifests in this document.



### GPUDirect-TCPX

This workload includes a sidecar container named the _tcpx-daemon_ , which runs a service that lets the Pod use GPUDirect-TCPX. **You must add this sidecar container to any Pods in your own environment that need to use GPUDirect-TCPX.** For a snippet of the required fields to add to your manifests, see Add GPUDirect to your manifest.

  1. Review the [`nccl-config.yaml` ConfigMap manifest in GitHub](https://raw.githubusercontent.com/GoogleCloudPlatform/container-engine-accelerators/master/gpudirect-tcpx/nccl-config.yaml). This manifest deploys scripts that initialize an NCCL all-gather test and sets NCCL-specific configuration settings.

  2. Review the [`nccl-test-latest.yaml` Deployment manifest in GitHub](https://raw.githubusercontent.com/GoogleCloudPlatform/container-engine-accelerators/master/gpudirect-tcpx/nccl-test-latest.yaml). 

  3. Deploy the ConfigMap and the test workload:
         
         kubectl apply -f https://raw.githubusercontent.com/GoogleCloudPlatform/container-engine-accelerators/master/gpudirect-tcpx/nccl-config.yaml
         kubectl apply -f https://raw.githubusercontent.com/GoogleCloudPlatform/container-engine-accelerators/master/gpudirect-tcpx/nccl-test-latest.yaml
         

  4. Verify that the Pods are running and ready. Note that the images are large (approximately 5 GB) and can take several minutes to download.
         
         kubectl get pods -w
         

The command watches for updates and prints a new line when a Pod's status changes. The output is similar to the following:
         
         NAME               READY   STATUS              RESTARTS   AGE
         nccl-test-host-1   0/2     ContainerCreating   0          23s
         nccl-test-host-2   2/2     Running             0          23s
         nccl-test-host-1   2/2     Running             0          46s
         

Wait until the `STATUS` message for all Pods is `Running` and the value of `READY` is `2/2` before proceeding to the next step.

  5. Run the following commands to trigger an NCCL all-gather test for the nodes:
         
         kubectl exec \
           --stdin --tty --container=nccl-test nccl-test-host-1 \
           -- /configs/allgather.sh nccl-host-1 nccl-host-2
         

The output is similar to the following:
         
         #                                                              out-of-place                       in-place
         #       size         count      type   redop    root     time   algbw   busbw #wrong     time   algbw   busbw #wrong
         #        (B)    (elements)                               (us)  (GB/s)  (GB/s)            (us)  (GB/s)  (GB/s)
             1048576         16384     float    none      -1    696.8    1.50    1.41      0    729.0    1.44    1.35      0
             2097152         32768     float    none      -1    776.4    2.70    2.53      0    726.7    2.89    2.71      0
             4194304         65536     float    none      -1    774.3    5.42    5.08      0    805.1    5.21    4.88      0
             8388608        131072     float    none      -1    812.1   10.33    9.68      0    817.6   10.26    9.62      0
            16777216        262144     float    none      -1   1035.2   16.21   15.19      0   1067.8   15.71   14.73      0
            33554432        524288     float    none      -1   1183.3   28.36   26.59      0   1211.8   27.69   25.96      0
            67108864       1048576     float    none      -1   1593.4   42.12   39.49      0   1510.5   44.43   41.65      0
           134217728       2097152     float    none      -1   2127.8   63.08   59.13      0   2312.7   58.03   54.41      0
           268435456       4194304     float    none      -1   3603.0   74.50   69.85      0   3586.2   74.85   70.17      0
           536870912       8388608     float    none      -1   7101.7   75.60   70.87      0   7060.9   76.03   71.28      0
         # Out of bounds values : 0 OK
         # Avg bus bandwidth    : 29.8293
         


**Success:** At this point, you've successfully installed GPUDirect-TCPX on your nodes and can use it to optimize the throughput of GPU-heavy workloads that run on those nodes. The required fields to use GPUDirect-TCPX in your own Pods are described in Add GPUDirect to your manifests in this document.

## Adopt GPUDirect for your own workloads

After you have verified that your cluster networking is working successfully with the sample test workload, the next step is to adopt GPUDirect for your actual workloads. To do this, you must update your NCCL settings and your Kubernetes Pod manifests.

### Use required NCCL configuration settings to improve performance

The following key-value pairs are the required NCCL configuration settings for GPUDirect-TCPX and GPUDirect-TCPXO. When deploying your workloads that use NCCL, set them as environment variables to optimize performance.

### GPUDirect-TCPXO
    
    
    "LD_LIBRARY_PATH=\"${LD_LIBRARY_PATH}:/usr/local/nvidia/lib64\"",
    "NCCL_FASTRAK_CTRL_DEV=eth0",
    "NCCL_FASTRAK_IFNAME=eth1,eth2,eth3,eth4,eth5,eth6,eth7,eth8",
    "NCCL_SOCKET_IFNAME=eth0",
    "NCCL_CROSS_NIC=0",
    "NCCL_ALGO=Ring,Tree",
    "NCCL_PROTO=Simple,LL128",
    "NCCL_MIN_NCHANNELS=4",
    "NCCL_TUNER_PLUGIN=libnccl-tuner.so",
    "NCCL_TUNER_CONFIG_PATH=/usr/local/nvidia/lib64/a3plus_tuner_config.textproto",
    "NCCL_SHIMNET_GUEST_CONFIG_CHECKER_CONFIG_FILE=/usr/local/nvidia/lib64/a3plus_guest_config.textproto",
    "NCCL_DYNAMIC_CHUNK_SIZE=524288",
    "NCCL_P2P_NET_CHUNKSIZE=524288",
    "NCCL_P2P_PCI_CHUNKSIZE=524288",
    "NCCL_P2P_NVL_CHUNKSIZE=1048576",
    "NCCL_FASTRAK_NUM_FLOWS=2",
    "NCCL_FASTRAK_USE_SNAP=1",
    "NCCL_FASTRAK_PLUGIN_ACCEPT_TIMEOUT_MS=600000",
    "NCCL_FASTRAK_ENABLE_CONTROL_CHANNEL=0",
    "NCCL_BUFFSIZE=8388608",
    "CUDA_VISIBLE_DEVICES=0,1,2,3,4,5,6,7",
    "NCCL_NET_GDR_LEVEL=PIX",
    "NCCL_FASTRAK_ENABLE_HOTPATH_LOGGING=0",
    "NCCL_FASTRAK_USE_LLCM=1",
    "NCCL_NVLS_ENABLE=0"
    

Optionally, you can set all the configurations at once by following these steps:

  1. In your workload container manifest, add the following key-value pair as an environment variable:
         
         NCCL_LIB_DIR="/usr/local/nvidia/lib64"
         

  2. Ensure the `nccl-env-profile.sh` script is executed when your workload container starts. For example, you can do this in your Pod specification by overriding the container's command to include the following:
         
         source ${NCCL_LIB_DIR}/nccl-env-profile.sh
         


**Note:** Starting from the `us-docker.pkg.dev/gce-ai-infra/gpudirect-tcpxo/nccl-plugin-gpudirecttcpx-dev:v1.0.9-1` NCCL plugin version, the LL128 NCCL communication protocol support becomes the default tuning parameter in GPUDirect-TCPXO. To use or disable LL128, see the LL128 support section.

### LL128 support

The NVIDIA LL128 (low-latency 128) NCCL communication protocol can significantly improve performance for small-to-medium sized collectives. GPUDirect-TCPXO supports the LL128 protocol.

To use LL128, ensure that the `nccl-tcpxo-installer.yaml` file in the Install the GPUDirect binary and configure NCCL section uses the following container image version or later:
    
    
    us-docker.pkg.dev/gce-ai-infra/gpudirect-tcpxo/nccl-plugin-gpudirecttcpx-
    dev:v1.0.8-1
    

To set up LL128, do the following:

  * For the `us-docker.pkg.dev/gce-ai-infra/gpudirect-tcpxo/nccl-plugin-gpudirecttcpx- dev:v1.0.8-1` NCCL plugin version, do these steps:

    1. In your workload manifest, set the following environment variable:
           
           NCCL_LIB_DIR="/usr/local/nvidia/lib64
           

    2. Configure your workload to execute the `nccl-env-profile-ll128.sh` script when the container starts. In your workload manifest, set the following command:
           
           source ${NCCL_LIB_DIR}/nccl-env-profile-ll128.sh
           

The `nccl-env-profile-ll128.sh` script has the following environment variables:
           
           NCCL_PROTO=Simple,LL128
           NCCL_TUNER_CONFIG_PATH=/usr/local/nvidia/lib64/a3plus_tuner_config_ll128.textproto
           NCCL_SHIMNET_GUEST_CONFIG_CHECKER_CONFIG_FILE=/usr/local/nvidia/lib64/a3plus_guest_config_ll128.textproto
           

  * For the `us-docker.pkg.dev/gce-ai-infra/gpudirect-tcpxo/nccl-plugin-gpudirecttcpx-dev:v1.0.9-1` NCCL plugin version and later, LL128 becomes a default parameter, so using either `nccl-env-profile.sh` script or `nccl-env-profile-ll128.sh` script enables LL128. To disable LL128:

    1. In your workload manifest, set the following environment variable:
           
           NCCL_LIB_DIR="/usr/local/nvidia/lib64
           

    2. Configure your workload to execute the `nccl-env-profile-ll128.sh` script when the container starts. In your workload manifest, set the following command:
           
           source ${NCCL_LIB_DIR}/nccl-env-profile-simple.sh
           

The `nccl-env-profile-simple.sh` script has the following environment variables:
           
           NCCL_PROTO=Simple
           NCCL_TUNER_CONFIG_PATH=/usr/local/nvidia/lib64/a3plus_tuner_config_simple.textproto
           NCCL_SHIMNET_GUEST_CONFIG_CHECKER_CONFIG_FILE=/usr/local/nvidia/lib64/a3plus_tuner_config_simple.textproto
           




### GPUDirect-TCPX
    
    
    "LD_LIBRARY_PATH=\"${LD_LIBRARY_PATH}:/usr/local/tcpx/lib64\"",
    "NCCL_SOCKET_IFNAME=\"eth0\"",
    "NCCL_ALGO=Ring",
    "NCCL_PROTO=Simple",
    "NCCL_CROSS_NIC=0",
    "NCCL_NET_GDR_LEVEL=PIX",
    "NCCL_P2P_PXN_LEVEL=0",
    "NCCL_GPUDIRECTTCPX_SOCKET_IFNAME=eth1,eth2,eth3,eth4",
    "NCCL_GPUDIRECTTCPX_CTRL_DEV=eth0",
    "NCCL_DYNAMIC_CHUNK_SIZE=524288",
    "NCCL_P2P_NET_CHUNKSIZE=524288",
    "NCCL_P2P_PCI_CHUNKSIZE=524288",
    "NCCL_P2P_NVL_CHUNKSIZE=1048576",
    "NCCL_BUFFSIZE=4194304",
    "NCCL_NSOCKS_PERTHREAD=4",
    "NCCL_SOCKET_NTHREADS=1",
    "NCCL_GPUDIRECTTCPX_TX_BINDINGS=\"eth1:8-21,112-125;eth2:8-21,112-125;eth3:60-73,164-177;eth4:60-73,164-177\"",
    "NCCL_GPUDIRECTTCPX_RX_BINDINGS=\"eth1:22-35,126-139;eth2:22-35,126-139;eth3:74-87,178-191;eth4:74-87,178-191\"",
    "NCCL_GPUDIRECTTCPX_PROGRAM_FLOW_STEERING_WAIT_MICROS=500000"
    

**Note:** In this configuration, `eth0` is used for control traffic of the GPUDirect-TCPX workload. Avoid rate limiting or restricting the primary `eth0` device. You can remove the `NCCL_GPUDIRECTTCPX_CTRL_DEV` setting, which specifies the network interface for `GPUDirect-TCPX` control traffic, and the control traffic will instead use its GPU aligned network device. However, NCCL itself will continue to use `eth0` for orchestration because it's set as the value for the `NCCL_SOCKET_IFNAME`.

### Add GPUDirect to your manifests

This section shows the required fields that you must add to your Kubernetes manifests for your Pods to use GPUDirect.

Depending on the type of GPUDirect, do the following:

### GPUDirect-TCPXO

  1. Add the following annotations to the Pod metadata. Without these annotations, `hostNetwork:true` will be required for the Pod, and `privileged:true` will be required for the `tcpxo-daemon` container. 
         
         metadata:
           annotations:
             devices.gke.io/container.tcpxo-daemon: |+
               - path: /dev/nvidia0
               - path: /dev/nvidia1
               - path: /dev/nvidia2
               - path: /dev/nvidia3
               - path: /dev/nvidia4
               - path: /dev/nvidia5
               - path: /dev/nvidia6
               - path: /dev/nvidia7
               - path: /dev/nvidiactl
               - path: /dev/nvidia-uvm
               - path: /dev/dmabuf_import_helper
             networking.gke.io/default-interface: 'eth0'
             networking.gke.io/interfaces: |
               [
                 {"interfaceName":"eth0","network":"default"},
                 {"interfaceName":"eth1","network":"vpc1"},
                 {"interfaceName":"eth2","network":"vpc2"},
                 {"interfaceName":"eth3","network":"vpc3"},
                 {"interfaceName":"eth4","network":"vpc4"},
                 {"interfaceName":"eth5","network":"vpc5"},
                 {"interfaceName":"eth6","network":"vpc6"},
                 {"interfaceName":"eth7","network":"vpc7"},
                 {"interfaceName":"eth8","network":"vpc8"}
               ]
         

  2. Add the following fields to the Pod specification:
         
         spec:
           volumes:
           - name: libraries
             hostPath:
               path: /home/kubernetes/bin/nvidia/lib64
           - name: sys
             hostPath:
               path: /sys
           - name: proc-sys
             hostPath:
               path: /proc/sys
           - name: aperture-devices
             hostPath:
               path: /dev/aperture_devices
         

  3. Add the following container to the manifest to run the `tcpxo-daemon` service. Replace (`TCPXO_DAEMON_IMAGE`) with the latest image—for example, `us-docker.pkg.dev/gce-ai-infra/gpudirect-tcpxo/tcpgpudmarxd-dev:v1.0.17`:
         
         - name: tcpxo-daemon
           image: TCPXO_DAEMON_IMAGE
           imagePullPolicy: Always
           command: ["/bin/sh", "-c"]
           args:
             - |
               set -ex
               chmod 755 /fts/entrypoint_rxdm_container.sh
               /fts/entrypoint_rxdm_container.sh --num_hops=2 --num_nics=8 --uid= --alsologtostderr
           securityContext:
             capabilities:
               add:
                 - NET_ADMIN
                 - NET_BIND_SERVICE
           volumeMounts:
             - name: libraries
               mountPath: /usr/local/nvidia/lib64
             - name: sys
               mountPath: /hostsysfs
             - name: proc-sys
               mountPath: /hostprocsysfs
           env:
             - name: LD_LIBRARY_PATH
               value: /usr/local/nvidia/lib64
         

  4. Add the following environment variable to every GPU container:
         
         env:
         - name: LD_LIBRARY_PATH
           value: /usr/local/nvidia/lib64
         - name: NCCL_FASTRAK_LLCM_DEVICE_DIRECTORY
           value: /dev/aperture_devices
         

  5. Add the following volumeMounts to every GPU container. Without `aperture_devices` setups, `privileged:true` is required for GPU containers:
         
         volumeMounts:
           - name: aperture-devices
             mountPath: /dev/aperture_devices
         

  6. Add environment variables to configure NCCL options. For details, see [Use recommended NCCL configuration settings to improve performance](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/gpu-bandwidth-gpudirect-tcpx#environment-variables-nccl).




For an example of a completed Pod specification, see the [nccl-test-latest.yaml](https://raw.githubusercontent.com/GoogleCloudPlatform/container-engine-accelerators/refs/heads/master/gpudirect-tcpxo/nccl-test-latest.yaml) manifest on GitHub.

### GPUDirect-TCPX

  1. Add the following annotations to the Pod metadata. Without these annotations, `hostNetwork:true` will be required for the Pod, and `privileged:true` will be required for the `tcpx-daemon` container. 
         
         metadata:
           annotations:
             devices.gke.io/container.tcpx-daemon: |+
               - path: /dev/nvidia0
               - path: /dev/nvidia1
               - path: /dev/nvidia2
               - path: /dev/nvidia3
               - path: /dev/nvidia4
               - path: /dev/nvidia5
               - path: /dev/nvidia6
               - path: /dev/nvidia7
               - path: /dev/nvidiactl
               - path: /dev/nvidia-uvm
             networking.gke.io/default-interface: 'eth0'
             networking.gke.io/interfaces: |
               [
                 {"interfaceName":"eth0","network":"default"},
                 {"interfaceName":"eth1","network":"vpc1"},
                 {"interfaceName":"eth2","network":"vpc2"},
                 {"interfaceName":"eth3","network":"vpc3"},
                 {"interfaceName":"eth4","network":"vpc4"},
               ]
         

  2. Add the following fields to the Pod specification:
         
         spec:
           volumes:
           - name: libraries
             hostPath:
               path: /home/kubernetes/bin/nvidia/lib64
           - name: sys
             hostPath:
               path: /sys
           - name: proc-sys
             hostPath:
               path: /proc/sys
         

  3. Add the following container to the manifest to run the _tcpx-daemon_ service:
         
         - name: tcpx-daemon
           image: us-docker.pkg.dev/gce-ai-infra/gpudirect-tcpx/tcpgpudmarxd-dev:v2.0.12
           command:
             - /tcpgpudmarxd/build/app/tcpgpudmarxd
             - --gpu_nic_preset
             - a3vm
             - --gpu_shmem_type
             - fd
             - --uds_path
             - /run/tcpx
             - --setup_param
             - \"--verbose 128 2 0 \"
           securityContext:
             capabilities:
                 add:
                   - NET_ADMIN
           volumeMounts:
             - name: libraries
               mountPath: /usr/local/nvidia/lib64
             - name: tcpx-socket
               mountPath: /run/tcpx
             - name: sys
               mountPath: /hostsysfs
             - name: proc-sys
               mountPath: /hostprocsysfs
           env:
             - name: LD_LIBRARY_PATH
               value: /usr/local/nvidia/lib64
         

  4. Add the following volume mounts to any containers that request GPUs:
         
         volumeMounts:
         - name: tcpx-socket
           mountPath: /tmp
         - name: libraries
           mountPath: /usr/local/nvidia/lib64
         

**Note:** The default tcpx-socket path is `/tmp` for containers that request GPUs. If you set the `NCCL_GPUDIRECTTCPX_UNIX_CLIENT_PREFIX` environment variable to a value other than `/tmp`, GKE mounts the `tcpx-socket` volume to that `mountPath`.
  5. Add environment variables to configure NCCL options. For details, see the Use recommended NCCL configuration settings to improve performance section in this document. 

  6. Add the following environment variable to every GPU container:
         
         env:
         - name: LD_LIBRARY_PATH
           value: /usr/local/nvidia/lib64
         




For an example of a completed Pod specification, see the [nccl-test-latest.yaml](https://raw.githubusercontent.com/GoogleCloudPlatform/container-engine-accelerators/refs/heads/master/gpudirect-tcpx/nccl-test-latest.yaml) manifest on GitHub.

## Collect NCCL debugging logs

To log NCCL errors, we recommend that you add the following NCCL config:
    
    
    NCCL_DEBUG=INFO
    NCCL_DEBUG_SUBSYS=INIT,NET,ENV,COLL,GRAPH
    NCCL_DEBUG_FILE=/DIRECTORY/FILE_NAME.%h.%p
    

  * `NCCL_DEBUG=INFO`: prints debugging information. 
    * For large-scale workloads (64 nodes or more), extensive logging can occur. To avoid this scenario—and unless you specified `NCCL_DEBUG_FILE`—we recommend setting `NCCL_DEBUG=WARN` to limit logs to errors only.
  * `NCCL_DEBUG_SUBSYS`: filters the subsystems for which NCCL collects debugging information. We recommend that you collect logs for the following subsystems:

    * `INIT`: the initialization phase of NCCL.
    * `NET`: the NCCL network.
    * `ENV`: the environment variables that NCCL uses.
    * `COLL`: collective operations.
    * `GRAPH`: topology detection and graph search.

If you want to collect logs for different subsystems, see [`NCCL_DEBUG_SUBSYS`](https://docs.nvidia.com/deeplearning/nccl/user-guide/docs/env.html#nccl-debug-subsys) in the NCCL documentation for a list of accepted values.

  * `NCCL_DEBUG_FILE` (Optional): directs the NCCL debug logging output to a file that you specify. This variable writes NCCL logs to standard files, which prevents the log output from mixing with application output. This variable also writes logs from different NCCL ranks to different files, which prevents the logs from mixing.

Use the following filename format:
        
        /DIRECTORY/FILE_NAME.%h.%p
        

Replace the following:

    * `DIRECTORY`: the directory where you want to store the log files.
    * `FILE_NAME`: the name of the log files.

The placeholder `%h` resolves to the hostname of the node, while `%p` resolves to the process ID (PID) of the process that's generating the log.




For more information about debugging NCCL logs, see [Troubleshoot GPUs in GKE](https://docs.cloud.google.com/kubernetes-engine/docs/troubleshooting/gpus#debug-with-nccl-logs).

## What's next

  * Read the [GPUDirect-TCPXO Release Notes](https://github.com/GoogleCloudPlatform/container-engine-accelerators/blob/master/gpudirect-tcpxo/README.md)
  * Learn more about the [best practice to run workloads with GPUDirect-TCPX(O)](https://github.com/GoogleCloudPlatform/container-engine-accelerators/blob/master/gpudirect-tcpxo/best-practice.md)
  * Learn about [best practices for GKE networking](https://docs.cloud.google.com/kubernetes-engine/docs/best-practices/networking).
  * Learn more about the [Nvidia GPUDirect family of technologies](https://developer.nvidia.com/gpudirect) for data movement and access on Nvidia GPUs.
  * Learn about [current GPU version availability](https://docs.cloud.google.com/compute/docs/gpus) and [requesting GPUs](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/gpus) in GKE.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
