---
url: https://docs.cloud.google.com/kubernetes-engine/docs/add-on/ray-on-gke/how-to/ray-a4x/
title: Set up Ray on GKE with A4X and GB200 \u00a0|\u00a0 GKE AI/ML \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T00:27:37.432286+00:00
---

# Set up Ray on GKE with A4X and GB200  |  GKE AI/ML  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/docs/add-on/ray-on-gke/how-to/ray-a4x/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ Google Kubernetes Engine (GKE) ](https://docs.cloud.google.com/kubernetes-engine/docs)
  * [ GKE AI/ML ](https://docs.cloud.google.com/kubernetes-engine/docs/integrations/ai-infra)
  * [ Guides ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/machine-learning)



Send feedback 

#  Set up Ray on GKE with A4X and GB200 Stay organized with collections  Save and categorize content based on your preferences. 

[ Autopilot ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/autopilot-overview) [ Standard ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/choose-cluster-mode)

This document explains how to set up a Google Kubernetes Engine (GKE) cluster with [A4X virtual machines, which use NVIDIA GB200 GPUs](https://docs.cloud.google.com/ai-hypercomputer/docs/gpu#a4x), and run Ray applications.

For general instructions about creating GKE clusters that use A4X, see the following documents:

  * [Create an AI-optimized GKE cluster that uses A4X](https://docs.cloud.google.com/ai-hypercomputer/docs/create/gke-create-a4x)
  * [Create an AI-optimized GKE cluster with Cluster Toolkit](https://docs.cloud.google.com/ai-hypercomputer/docs/create/gke-ai-hypercompute)



This document is intended for Machine learning (ML) engineers and Platform admins and operators who facilitate ML workloads. To learn more about common roles and example tasks that we reference in Google Cloud content, see [Common GKE user roles and tasks](https://docs.cloud.google.com/kubernetes-engine/enterprise/docs/concepts/roles-tasks).

In this document, you complete the following steps:

  * Prepare your environment.
  * Set up networking by creating Google Virtual NIC (gVNIC) and RDMA VPC networks and subnets.
  * Create a GKE cluster with multi-networking enabled.
  * Create a node pool with A4X instances.
  * Install NVIDIA drivers.
  * Install and configure Ray.
  * Verify the Ray cluster configuration.



## About Ray and Ray Serve

Ray is an open-source scalable compute framework for AI/ML applications. Ray Serve is a model serving library for Ray used for scaling and serving models in a distributed environment. For more information, see [Ray Serve](https://docs.ray.io/en/latest/serve/index.html) in the Ray documentation.

## Before you begin

### Costs

In this document, you use the following billable components of Google Cloud: 

  * [GKE](https://docs.cloud.google.com/kubernetes-engine/pricing)



To generate a cost estimate based on your projected usage, use the [pricing calculator](https://docs.cloud.google.com/products/calculator). 

New Google Cloud users might be eligible for a [free trial](https://docs.cloud.google.com/free). 

When you finish the tasks that are described in this document, you can avoid continued billing by deleting the resources that you created. For more information, see Clean up.

### Activate Cloud Shell

[Cloud Shell](https://docs.cloud.google.com/shell) is preinstalled with the software you need for this tutorial, including [`kubectl`](https://kubernetes.io/docs/reference/kubectl/) and the [gcloud CLI](https://docs.cloud.google.com/sdk/gcloud). If you don't use Cloud Shell, you must install the gcloud CLI.

Before you start, make sure that you have performed the following tasks: 

     * Enable the Google Kubernetes Engine API. 
[ Enable Google Kubernetes Engine API ](https://console.cloud.google.com/apis/enableflow?apiid=container.googleapis.com)
     * To use the Google Cloud CLI for this task, [install](https://docs.cloud.google.com/sdk/docs/install) and then [initialize](https://docs.cloud.google.com/sdk/docs/initialize) the gcloud CLI. If you previously installed the gcloud CLI, get the latest version by running the `gcloud components update` command. Earlier gcloud CLI versions might not support running the commands in this document. **Note:** For existing gcloud CLI installations, make sure to set the `compute/region` [property](https://docs.cloud.google.com/sdk/docs/properties#setting_properties). If you use primarily zonal clusters, set the `compute/zone` instead. By setting a default location, you can avoid errors in the gcloud CLI like the following: `One of [--zone, --region] must be supplied: Please specify location`. You might need to specify the location in certain commands if the location of your cluster differs from the default that you set.



### Required roles

  1. Grant roles to your user account. Run the following command once for each of the following IAM roles: `roles/container.clusterAdmin, roles/container.admin`
         
         gcloud projects add-iam-policy-binding PROJECT_ID --member="user:USER_IDENTIFIER" --role=ROLE

Replace the following:

     * `PROJECT_ID`: Your project ID.
     * `USER_IDENTIFIER`: The identifier for your user account. For example, `myemail@example.com`. 
     * `ROLE`: The IAM role that you grant to your user account.
  2. Ensure that you have sufficient [quota](https://docs.cloud.google.com/docs/quotas/view-manage) for the `a4x-highgpu-4g` machine type and `nvidia-gb200` GPUs.



## Prepare your environment

  1. Set the environment variables for your project and region.
         
         export PROJECT=PROJECT_ID
         export REGION=us-central1
         export ZONE=us-central1-b
         export CLUSTER_NAME="a4x-ray-cluster"
         export GVNIC_NETWORK_PREFIX="a4x-gvnic"
         export RDMA_NETWORK_PREFIX="a4x-rdma"
         export GKE_VERSION=1.32.4-gke.1533000
         export WORKLOAD_POLICY_NAME=wp-ht-72
         export NODE_POOL_NAME=a4x-nodepool
         export NODE_COUNT=18
         export MACHINE_TYPE="a4x-highgpu-4g"
         export ACCELERATOR_CONFIG="type=nvidia-gb200,count=4"
         export ARM_NP_NAME=cpu-only-arm-nodepool
         

Replace `PROJECT_ID` with your project ID.




## Set up networking

  1. Create the gVNIC:
         
         gcloud compute networks create ${GVNIC_NETWORK_PREFIX}-net \
             --project=${PROJECT} \
             --subnet-mode=custom \
             --mtu=8896
         

  2. Create a subnet for the gVNIC:
         
         gcloud compute networks subnets create ${GVNIC_NETWORK_PREFIX}-sub \
             --project=${PROJECT} \
             --network=${GVNIC_NETWORK_PREFIX}-net \
             --region=${REGION} \
             --range=192.168.0.0/24
         

  3. Create a firewall for the gVNIC:
         
         gcloud compute firewall-rules create ${GVNIC_NETWORK_PREFIX}-internal \
             --project=${PROJECT} \
             --network=${GVNIC_NETWORK_PREFIX}-net \
             --action=ALLOW \
             --rules=tcp:0-65535,udp:0-65535,icmp \
             --source-ranges=192.168.0.0/16
         

  4. Create a VPC network. The following command creates a VPC with an RDMA network profile:
         
         gcloud compute networks create ${RDMA_NETWORK_PREFIX}-net \
             --project=${PROJECT} \
             --network-profile=${ZONE}-vpc-roce \
             --subnet-mode=custom
         

  5. Create four subnets for the VPC:
         
         for N in $(seq 0 3); do
           gcloud compute networks subnets create ${RDMA_NETWORK_PREFIX}-sub-$N \
             --project=${PROJECT} \
             --network=${RDMA_NETWORK_PREFIX}-net \
             --region=${REGION} \
             --range=192.168.$((N+1)).0/24
         done
         




## Create a GKE cluster

Create a GKE cluster with multi-networking enabled so that you can configure the VPC network that you created.

  1. Create the GKE cluster:
         
         gcloud container clusters create ${CLUSTER_NAME} \
             --project=${PROJECT} \
             --location=${REGION} \
             --cluster-version=${GKE_VERSION} \
             --machine-type=c4a-standard-72 \
             --enable-dataplane-v2 \
             --enable-ip-alias \
             --enable-multi-networking \
             --no-enable-autoupgrade \
             --enable-kubernetes-unstable-apis=resource.k8s.io/v1beta1/deviceclasses,resource.k8s.io/v1beta1/resourceclaims,resource.k8s.io/v1beta1/resourceclaimtemplates,resource.k8s.io/v1beta1/resourceslices
         

  2. Get credentials for the cluster:
         
         gcloud container clusters get-credentials ${CLUSTER_NAME} --location=${REGION}
         

  3. Save the following manifest as `network-parameters.yaml`. This manifest configures a CPU Titanium NIC (gVNIC) VPC with one subnet, and CX-7 RDMA NICs VPC with four subnets in `RDMA` mode:
         
         apiVersion: networking.gke.io/v1
          kind: GKENetworkParamSet
          metadata:
            name: gvnic-1
          spec:
            vpc: ${GVNIC_NETWORK_PREFIX}-net
            vpcSubnet: ${GVNIC_NETWORK_PREFIX}-sub
            deviceMode: NetDevice
          ---
          apiVersion: networking.gke.io/v1
          kind: Network
          metadata:
            name: gvnic-1
          spec:
            type: "Device"
            parametersRef:
              group: networking.gke.io
              kind: GKENetworkParamSet
              name: gvnic-1
          ---
          apiVersion: networking.gke.io/v1
          kind: GKENetworkParamSet
          metadata:
            name: rdma-0
          spec:
            vpc: ${RDMA_NETWORK_PREFIX}-net
            vpcSubnet: ${RDMA_NETWORK_PREFIX}-sub-0
            deviceMode: RDMA
          ---
          apiVersion: networking.gke.io/v1
          kind: Network
          metadata:
            name: rdma-0
          spec:
            type: "Device"
            parametersRef:
              group: networking.gke.io
              kind: GKENetworkParamSet
              name: rdma-0
          ---
          apiVersion: networking.gke.io/v1
          kind: GKENetworkParamSet
          metadata:
            name: rdma-1
          spec:
            vpc: ${RDMA_NETWORK_PREFIX}-net
            vpcSubnet: ${RDMA_NETWORK_PREFIX}-sub-1
            deviceMode: RDMA
          ---
          apiVersion: networking.gke.io/v1
          kind: Network
          metadata:
            name: rdma-1
          spec:
            type: "Device"
            parametersRef:
              group: networking.gke.io
              kind: GKENetworkParamSet
              name: rdma-1
          ---
          apiVersion: networking.gke.io/v1
          kind: GKENetworkParamSet
          metadata:
            name: rdma-2
          spec:
            vpc: ${RDMA_NETWORK_PREFIX}-net
            vpcSubnet: ${RDMA_NETWORK_PREFIX}-sub-2
            deviceMode: RDMA
          ---
          apiVersion: networking.gke.io/v1
          kind: Network
          metadata:
            name: rdma-2
          spec:
            type: "Device"
            parametersRef:
              group: networking.gke.io
              kind: GKENetworkParamSet
              name: rdma-2
          ---
          apiVersion: networking.gke.io/v1
          kind: GKENetworkParamSet
          metadata:
            name: rdma-3
          spec:
            vpc: ${RDMA_NETWORK_PREFIX}-net
            vpcSubnet: ${RDMA_NETWORK_PREFIX}-sub-3
            deviceMode: RDMA
          ---
          apiVersion: networking.gke.io/v1
          kind: Network
          metadata:
            name: rdma-3
          spec:
            type: "Device"
            parametersRef:
              group: networking.gke.io
              kind: GKENetworkParamSet
              name: rdma-3
         

  4. To create the GKE network objects, apply the `network-parameters.yaml` file:
         
         kubectl apply -f network-parameters.yaml
         




## Create a node pool

To create a node pool, you must create a workload policy, choose a reservation type, and then create the node pools.

  1. Create a high-throughput workload policy:
         
         gcloud beta compute resource-policies create workload-policy ${WORKLOAD_POLICY_NAME} \
             --project=${PROJECT} \
             --region=${REGION} \
             --type=HIGH_THROUGHPUT \
             --accelerator-topology=1x72
         

  2. To choose a reservation type, export one of the following names, which you use when you create the node pool in the next step:

     * If you want to use a reservation of any-subblock within any block, set the following variable:
           
           export RESERVATION_NAME=RESERVATION_NAME
           

     * If you want to use a block-targeted reservation, set the following variable:
           
           export RESERVATION_NAME=RESERVATION_NAME/reservationBlocks/BLOCK_NAME
           

     * If you want to use a sub-block targeted reservation where VMs are placed on a single sub-block within the block, set the following variable:
           
           export RESERVATION_NAME=RESERVATION_NAME/reservationBlocks/BLOCK_NAME/reservationSubBlocks/SUBBLOCK_NAME
           

     * If you want to use a shared reservation from another project, set the following variable:
           
           export RESERVATION_NAME=projects/RESERVATION_OWNER_PROJECT/reservations/RESERVATION_NAME
           

Replace `RESERVATION_NAME` with a name for your reservation. Replace the following variables as needed:

     * `BLOCK_NAME`: the name of the reservation block.
     * `SUBBLOCK_NAME`: the name of the reservation sub-block.
     * `RESERVATION_OWNER_PROJECT`: the ID of the project that owns the shared reservation.
  3. Create the node pool:
         
         gcloud container node-pools create ${NODE_POOL_NAME} \
             --project=${PROJECT} \
             --cluster=${CLUSTER_NAME} \
             --location=${REGION} \
             --node-locations=${ZONE} \
             --num-nodes=${NODE_COUNT} \
             --machine-type=${MACHINE_TYPE} \
             --accelerator=${ACCELERATOR_CONFIG} \
             --additional-node-network=network=${GVNIC_NETWORK_PREFIX}-net,subnetwork=${GVNIC_NETWORK_PREFIX}-sub \
             --additional-node-network=network=${RDMA_NETWORK_PREFIX}-net,subnetwork=${RDMA_NETWORK_PREFIX}-sub-0 \
             --additional-node-network=network=${RDMA_NETWORK_PREFIX}-net,subnetwork=${RDMA_NETWORK_PREFIX}-sub-1 \
             --additional-node-network=network=${RDMA_NETWORK_PREFIX}-net,subnetwork=${RDMA_NETWORK_PREFIX}-sub-2 \
             --additional-node-network=network=${RDMA_NETWORK_PREFIX}-net,subnetwork=${RDMA_NETWORK_PREFIX}-sub-3 \
             --no-enable-autoupgrade \
             --scopes="https://www.googleapis.com/auth/cloud-platform" \
             --reservation-affinity=specific \
             --reservation=${RESERVATION_NAME} \
             --placement-policy=${WORKLOAD_POLICY_NAME}
         

GKE automatically installs the required 570 GPU driver version on all A4X nodes that run GKE version 1.32.4-gke.1533000 or later.




## Install drivers

To install the NVIDIA and DRA drivers that you need, complete the following steps:

  1. One each node, apply a DaemonSet that installs RDMA binaries and the NCCL library:
         
         kubectl apply -f https://raw.githubusercontent.com/GoogleCloudPlatform/container-engine-accelerators/master/gpudirect-rdma/nccl-rdma-installer-a4x.yaml
         

  2. Install Helm:
         
         curl -fsSL -o get_helm.sh https://raw.githubusercontent.com/helm/helm/master/scripts/get-helm-3 \
         && chmod 700 get_helm.sh
         && ./get_helm.sh
         

  3. Add the NVIDIA Helm repository:
         
         helm repo add nvidia https://helm.ngc.nvidia.com/nvidia
         && helm repo update
         

  4. Create a namespace for the DRA driver:
         
         kubectl create ns nvidia-dra-driver-gpu
         

  5. To create a `ResourceQuota` object for the DRA driver, save the following manifest as `nvidia-driver.yaml`:
         
         apiVersion: v1
         kind: ResourceQuota
         metadata:
           name: nvidia-dra-driver-gpu-quota
         spec:
           hard:
             pods: POD_NUMBER
           scopeSelector:
             matchExpressions:
             -   operator: In
               scopeName: PriorityClass
               values:
                 -   system-node-critical
                 -   system-cluster-critical
         

Replace `POD_NUMBER` with the number of Pods. The number should be twice the number of A4X nodes in the cluster, plus one. For example, if you have 10 A4X nodes, you should set this number to 21.

  6. Apply the manifest:
         
         kubectl apply -f nvidia-driver.yaml
         

  7. Install the DRA driver:
         
         helm install nvidia-dra-driver-gpu nvidia/nvidia-dra-driver-gpu \
             --version="25.3.0-rc.3" \
             --namespace nvidia-dra-driver-gpu \
             -f <(cat <<EOF
         nvidiaDriverRoot: /home/kubernetes/bin/nvidia
         resources:
           gpus:
             enabled: false
         
         controller:
           affinity:
               nodeAffinity:
                 requiredDuringSchedulingIgnoredDuringExecution:
                   nodeSelectorTerms:
                   -   matchExpressions:
                     -   key: "nvidia.com/gpu"
                       operator: "DoesNotExist"
         
         kubeletPlugin:
           affinity:
             nodeAffinity:
               requiredDuringSchedulingIgnoredDuringExecution:
                 nodeSelectorTerms:
                   -   matchExpressions:
                       -   key: cloud.google.com/gke-accelerator
                         operator: In
                         values:
                           -   nvidia-gb200
                       -   key: kubernetes.io/arch
                         operator: In
                         values:
                           -   arm64
         
           tolerations:
             -   key: nvidia.com/gpu
               operator: Equal
               value: present
               effect: NoSchedule
             -   key: kubernetes.io/arch
               operator: Equal
               value: arm64
               effect: NoSchedule
         EOF
         )
         




## Configure Ray

The following section explains how to install and configure Ray to deploy a Ray cluster.

### Install KubeRay operator

To install the KubeRay operator, complete the following steps:

  1. To support `ResourceClaims`, install the KubeRay operator version 1.3.1 or later:
         
         helm install kuberay-operator kuberay/kuberay-operator --version 1.3.1
         

  2. (Optional) Create a C4A or T2A node pool to deploy the Ray head on a CPU-only machine type. This step lets you deploy the Ray head on a CPU-only ARM machine type, avoiding the need for a separate X86 image if your worker nodes are ARM-based.
         
         gcloud container node-pools create ${ARM_NP_NAME} \
             --cluster=${CLUSTER_NAME} \
             --machine-type=c4a-standard-72 \
             --location=${REGION} \
             --node-locations=${ZONE}
         




### (Optional) Build a custom Ray container image

We recommend creating a custom Ray image with specific Python packages because some Python packages require specific versions and are not included by default.

The following example `Dockerfile` uses Ray 2.44.1 with CUDA 12.8 on ARM and a nightly version of PyTorch:
    
    
    FROM rayproject/ray:2.44.1-py39-cu128-aarch64
    
    RUN sudo apt-get update && sudo apt-get install libnl-3-200 libnl-route-3-200
    
    RUN pip install --pre torch --index-url https://download.pytorch.org/whl/nightly/cu128
    

### Deploy the RayCluster

Configure your Ray workers to use multi-networking, RDMA, and the A4X nodes by completing the following steps:

  1. To create a `ComputeDomain` resource, save the following manifest as `a4x-compute-domain.yaml`:
         
         apiVersion: resource.nvidia.com/v1beta1
         kind: ComputeDomain
         metadata:
           name: a4x-compute-domain
         spec:
           numNodes: 18
           channel:
             resourceClaimTemplate:
               name: a4x-compute-domain-channel
         

  2. Apply the manifest:
         
         kubectl apply -f a4x-compute-domain.yaml
         

  3. To create a `RayCluster` resource, save the following manifest as `a4x-ray-cluster.yaml`:
         
         apiVersion: ray.io/v1
         kind: RayCluster
         metadata:
           name: a4x-ray-cluster
         spec:
           headGroupSpec:
             rayStartParams:
               dashboard-host: '0.0.0.0'
             template:
               spec:
                 containers:
                 -   name: ray-head
                   image: RAY_IMAGE_URI
                   volumeMounts:
                   -   mountPath: /tmp/ray
                     name: ray-logs
                   resources:
                     requests:
                       cpu: "64"
                       memory: "250Gi"
                     limits:
                       memory: "250Gi"
                   ports:
                   -   containerPort: 6379
                     name: gcs-server
                   -   containerPort: 8265
                     name: dashboard
                   -   containerPort: 10001
                     name: client
                 volumes:
                 -   name: ray-logs
                   emptyDir: {}
                 tolerations:
                 -   key: "kubernetes.io/arch"
                   operator: "Equal"
                   value: "arm64"
                   effect: "NoSchedule"
           workerGroupSpecs:
           -   replicas: 18
             minReplicas: 1
             maxReplicas: 18
             groupName: a4x-large-group
             rayStartParams: {}
             template:
               metadata:
                 annotations:
                   networking.gke.io/default-interface: 'eth0'
                   networking.gke.io/interfaces: |
                     [
                       {"interfaceName":"eth0","network":"default"},
                       {"interfaceName":"eth2","network":"rdma-0"},
                       {"interfaceName":"eth3","network":"rdma-1"},
                       {"interfaceName":"eth4","network":"rdma-2"},
                       {"interfaceName":"eth5","network":"rdma-3"}
                     ]
               spec:
                 containers:
                 -   name: ray-worker
                   image: RAY_IMAGE_URI
                   volumeMounts:
                   -   mountPath: /tmp/ray
                     name: ray-logs
                   -   name: library-dir-host
                     mountPath: /usr/local/nvidia
                   -   name: gib
                     mountPath: /usr/local/gib
                   env:
                   -   name: LD_LIBRARY_PATH
                     value: /usr/local/nvidia/lib64
                   -   name: NCCL_NET
                     value: "gIB"
                   -   name: NCCL_CROSS_NIC
                     value: "0"
                   -   name: NCCL_NET_GDR_LEVEL
                     value: "PHB"
                   -   name: NCCL_NET_GDR_C2C
                     value: "1"
                   -   name: NCCL_NVLS_ENABLE
                     value: "0"
                   -   name: NCCL_IB_MERGE_VFS
                     value: "0"
                   -   name: NCCL_IB_QPS_PER_CONNECTION
                     value: "4"
                   -   name: NCCL_IB_TC
                     value: "52"
                   -   name: NCCL_IB_FIFO_TC
                     value: "84"
                   -   name: NCCL_IB_ADAPTIVE_ROUTING
                     value: "1"
                   resources:
                     requests:
                       cpu: "120"
                       nvidia.com/gpu: "4"
                       memory: "750Gi"
                     limits:
                       nvidia.com/gpu: "4"
                       memory: "750Gi"
                     claims:
                     -   name: compute-domain-channel
                 volumes:
                 -   name: ray-logs
                   emptyDir: {}
                 -   name: library-dir-host
                   hostPath:
                     path: /home/kubernetes/bin/nvidia
                 -   name: gib
                   hostPath:
                     path: /home/kubernetes/bin/gib
                 tolerations:
                 -   key: "nvidia.com/gpu"
                   operator: "Exists"
                   effect: "NoSchedule"
                 -   key: "kubernetes.io/arch"
                   operator: "Exists"
                   effect: "NoSchedule"
                 resourceClaims:
                 -   name: compute-domain-channel
                   resourceClaimTemplateName: a4x-compute-domain-channel
         

Replace `RAY_IMAGE_URI` with the URI of the custom Ray container image that you built.

  4. Apply the manifest:
         
         kubectl apply -f a4x-ray-cluster.yaml
         




### Verify the Ray cluster configuration

After you deploy the `RayCluster`, verify that the resources are available and that CUDA is working correctly.

  1. Verify the cluster resources:
         
         ray job submit -- python -c "import ray; ray.init(); print(ray.cluster_resources())"
         

The output shows the available resources. A single NVLink domain contains 72 GPU resources (18 hosts * 4 chips):
         
         {'GPU': 72.0, 'memory': 9287866777600.0, ...}
         

  2. Validate CUDA availability with PyTorch by completing the following steps:

     1. Create a Python script named `ray_gpu_info.py`:
            
            import torch
            import ray
            
            @ray.remote(num_gpus=4)
            def get_gpu_info():
                print(torch.cuda.is_available())
                print(torch.cuda.device_count())
                print(torch.cuda.current_device())
                print(torch.cuda.get_device_name(0))
                print(ray.get_gpu_ids())
            
            ray.init()
            ray.get(get_gpu_info.remote())
            

     2. Submit the Ray job:
            
            ray job submit --working-dir . -- python ray_gpu_info.py
            

The output shows that CUDA is available and recognizes the four NVIDIA GB200 GPUs:
    
    (get_gpu_info pid=5838, ip=10.76.10.49) True
    (get_gpu_info pid=5838, ip=10.76.10.49) 4
    (get_gpu_info pid=5838, ip=10.76.10.49) 0
    (get_gpu_info pid=5838, ip=10.76.10.49) NVIDIA GB200
    (get_gpu_info pid=5838, ip=10.76.10.49) [0, 1, 2, 3]
    




## Troubleshoot

This section describes common issues and how to resolve them.

### Failed to initialize any NET plugin error

This error occurs when initializing NCCL if the `libnl-3-200` and `libnl-route-3-200` libraries are missing from your container image.

To resolve this issue, add the following command to your `Dockerfile` to install the libraries:
    
    
    RUN sudo apt-get update && sudo apt-get install libnl-3-200 libnl-route-3-200
    

### exec format error

This error occurs due to an architectural mismatch, for example, when you try to run an x86-based container image on an ARM-based node.

To resolve this issue, ensure that your container image supports the ARM architecture.

### NVLink stuck in `Not Ready` state

If the `ComputeDomain` resource shows a `Not Ready` state and the A4X node shows a `FailedPreparedDynamicResource` error, your KubeRay `RayCluster` CustomResourceDefinition might not have the correct template for `resourceClaims`.

To resolve this issue, delete the Ray CustomResourceDefinition and reinstall the KubeRay operator.

### CuPy missing NCCL support for ARM

Some Ray libraries rely on CuPy for NCCL integrations. ARM-based pip wheels for CuPy gained NCCL support in version 13.5.0. If you use an earlier version, you might encounter an `ImportError`.

To resolve this issue, use CuPy version 13.5.0 or later in your container image.

## Clean up

To avoid incurring charges to your Google Cloud account for the resources used in this tutorial, either delete the project that contains the resources, or keep the project and delete the individual resources. 

To avoid incurring charges to your Google Cloud account for the resources used in this tutorial, either delete the project that contains the resources, or keep the project and delete the individual resources.

### Delete the project

**Caution** : Deleting a project has the following effects: 
     * **Everything in the project is deleted.** If you used an existing project for the tasks in this document, when you delete it, you also delete any other work you've done in the project. 
     * **Custom project IDs are lost.** When you created this project, you might have created a custom project ID that you want to use in the future. To preserve the URLs that use the project ID, such as an `appspot.com` URL, delete selected resources inside the project instead of deleting the whole project. 

If you plan to explore multiple architectures, tutorials, or quickstarts, reusing projects can help you avoid exceeding project quota limits. 

Delete a Google Cloud project:
    
    gcloud projects delete PROJECT_ID




### Delete individual resources

To delete the cluster, type:
    
    
    gcloud container clusters delete ${CLUSTER_NAME}
    

## What's next

  * [Learn more about Ray on GKE](https://docs.cloud.google.com/kubernetes-engine/docs/add-on/ray-on-gke/concepts/overview).
  * [Learn more about Ray](https://www.ray.io/).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
