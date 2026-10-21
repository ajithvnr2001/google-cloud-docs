---
url: https://docs.cloud.google.com/ai-hypercomputer/docs/create/gke-create-a4x-max/
title: Create an AI-optimized GKE cluster that uses A4X Max \u00a0|\u00a0 AI Hypercomputer \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T05:34:53.500698+00:00
---

# Create an AI-optimized GKE cluster that uses A4X Max  |  AI Hypercomputer  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/ai-hypercomputer/docs/create/gke-create-a4x-max/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ AI Hypercomputer ](https://docs.cloud.google.com/ai-hypercomputer/docs)
  * [ Guides ](https://docs.cloud.google.com/ai-hypercomputer/docs/overview)



Send feedback 

#  Create an AI-optimized GKE cluster that uses A4X Max Stay organized with collections  Save and categorize content based on your preferences. 

[ Clustered GPUs ](https://docs.cloud.google.com/ai-hypercomputer/docs/evaluate-clustered-gpus)

This document shows you how to create an AI-optimized Google Kubernetes Engine (GKE) cluster that uses A4X Max Compute Engine instances to support your AI and ML workloads.

[The A4X Max and A4X series](https://docs.cloud.google.com/ai-hypercomputer/docs/evaluate-clustered-gpus#a4x) lets you run large-scale AI/ML clusters by using the [NVIDIA Multi-Node NVLink (MNNVL) system](https://docs.nvidia.com/multi-node-nvlink-systems/mnnvl-user-guide/overview.html), a rack-scale solution which enables higher GPU power and performance. These machines offer features such as targeted workload placement, topology-aware scheduling, and advanced cluster maintenance controls. For more information, see [Cluster management capabilities](https://docs.cloud.google.com/ai-hypercomputer/docs/cluster-capabilities). With A4X Max, GKE also provides an automated networking setup which simplifies cluster configuration.

AI and ML workloads, such as distributed training, require powerful acceleration to optimize performance by reducing job completion times. GKE provides a single platform surface to run a diverse set of workloads for your organizations, reducing the operational burden of managing multiple platforms. You can run workloads such as high-performance distributed pre-training, model fine-tuning, model inference, application serving, and supporting services. For workloads that require high performance, high throughput, and low latency, GPUDirect RDMA reduces the network hops that are required to transfer payloads to and from GPUs. This approach more efficiently uses the network bandwidth that's available. For more information, see [GPU networking stacks](https://docs.cloud.google.com/ai-hypercomputer/docs/networking-overview#networking-stacks).

In this document, you learn how to create a GKE cluster with the Google Cloud CLI for maximum flexibility in configuring your cluster based on the needs of your workload. To use the gcloud CLI to create clusters with other machine types, see the following:

  * **A4X** : [Create an AI-optimized GKE cluster that uses A4X](https://docs.cloud.google.com/ai-hypercomputer/docs/create/gke-create-a4x).
  * **A4 or A3 Ultra** : To create a cluster that uses A4 or A3 Ultra, see [Create an AI-optimized GKE cluster that uses A4 or A3 Ultra](https://docs.cloud.google.com/ai-hypercomputer/docs/create/gke-create-a4-a3-ultra). You can use these machine series for running workloads with or without GPUDirect RDMA.



Alternatively, you can choose to use Cluster Toolkit to quickly deploy your cluster with default settings that reflect best practices for many use cases. For more information, see [Create an AI-optimized GKE cluster with Cluster Toolkit](https://docs.cloud.google.com/ai-hypercomputer/docs/create/gke-ai-hypercompute).

## Before you begin

Before you start, make sure that you have performed the following tasks: 

  * Enable the Google Kubernetes Engine API. 
[ Enable Google Kubernetes Engine API ](https://console.cloud.google.com/apis/enableflow?apiid=container.googleapis.com)
  * To use the Google Cloud CLI for this task, [install](https://docs.cloud.google.com/sdk/docs/install) and then [initialize](https://docs.cloud.google.com/sdk/docs/initialize) the gcloud CLI. If you previously installed the gcloud CLI, get the latest version by running the `gcloud components update` command. Earlier gcloud CLI versions might not support running the commands in this document. **Note:** For existing gcloud CLI installations, make sure to set the `compute/region` [property](https://docs.cloud.google.com/sdk/docs/properties#setting_properties). If you use primarily zonal clusters, set the `compute/zone` instead. By setting a default location, you can avoid errors in the gcloud CLI like the following: `One of [--zone, --region] must be supplied: Please specify location`. You might need to specify the location in certain commands if the location of your cluster differs from the default that you set.



### Required roles

To get the permissions that you need to create and manage a GKE cluster, ask your administrator to grant you the following IAM roles: 

  * [Kubernetes Engine Admin ](https://docs.cloud.google.com/iam/docs/roles-permissions/container#container.admin) (`roles/container.admin`) on the project
  * [Cloud Build Editor ](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudbuild#cloudbuild.builds.editor) (`roles/cloudbuild.builds.editor`) on the project
  * [Compute Admin ](https://docs.cloud.google.com/iam/docs/roles-permissions/compute#compute.admin) (`roles/compute.admin`) on the project
  * [Project IAM Admin ](https://docs.cloud.google.com/iam/docs/roles-permissions/resourcemanager#resourcemanager.projectIamAdmin) (`roles/resourcemanager.projectIamAdmin`) on the project
  * [Service Account Admin ](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.serviceAccountAdmin) (`roles/iam.serviceAccountAdmin`) on the project
  * [Service Account User ](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.serviceAccountUser) (`roles/iam.serviceAccountUser`) on the project
  * [Service Usage Consumer ](https://docs.cloud.google.com/iam/docs/roles-permissions/serviceusage#serviceusage.serviceUsageConsumer) (`roles/serviceusage.serviceUsageConsumer`) on the project
  * To consume a single-project reservation: [Compute Instance Admin (v1) ](https://docs.cloud.google.com/iam/docs/roles-permissions/compute#compute.instanceAdmin.v1) (`roles/compute.instanceAdmin.v1`) on the project 
  * To consume a shared reservation: [Compute Instance Admin (v1) ](https://docs.cloud.google.com/iam/docs/roles-permissions/compute#compute.instanceAdmin.v1) (`roles/compute.instanceAdmin.v1`) on both the owner project and any consumer project where you want to consume the reservation 



For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

You might also be able to get the required permissions through [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

### Obtain capacity

You can obtain capacity for A4X Max compute instances by creating a future reservation. For more information about future reservations, see the **Future reservations in AI Hypercomputer** column in the table for [Choose a consumption option](https://docs.cloud.google.com/ai-hypercomputer/docs/consumption-models).

To obtain capacity with a future reservation, see the **Future reservations in AI Hypercomputer** row in the table for [How to obtain capacity](https://docs.cloud.google.com/ai-hypercomputer/docs/obtain-capacity#how_to_obtain_capacity).

**Note:** When you request A4X Max capacity, you obtain it in _all capacity mode_. This mode is the only supported reservation operational mode for A4X Max machine types. For more information about all capacity mode, see [Reservation operational mode](https://docs.cloud.google.com/ai-hypercomputer/docs/create/review-configurations#reservation-operational-mode).

### Requirements

The following requirements apply to an AI-optimized GKE cluster with A4X Max compute instances:

  * For A4X Max, you must use one of the following versions:

    * For 1.35 or later, use GKE version 1.35.0-gke.2745000 or later.
    * For 1.34, use GKE version 1.34.3-gke.1318000 or later.

These versions help to ensure that A4X Max uses the following:

    * R580.95.05, the minimum GPU driver version for A4X Max, which is enabled by default.
    * Coherent Driver-based Memory Management (CDMM), which is enabled by default. NVIDIA recommends that Kubernetes clusters enable this mode to resolve memory over-reporting. CDMM allows GPU memory to be managed through the driver instead of the operating system (OS). This approach helps you to avoid OS onlining of GPU memory, and exposes the GPU memory as a Non-Uniform Memory Access (NUMA) node to the OS. Multi-instance GPUs aren't supported when CDMM is enabled. For more information about CDMM, see [Hardware and Software Support](https://docs.nvidia.com/datacenter/tesla/tesla-release-notes-580-65-06/index.html#hardware-software-support).
    * GPUDirect RDMA and MNNVL, which are recommended to enable A4X Max node pools to use the networking capabilities of A4X Max.
  * The GKE nodes must use a Container-Optimized OS node image. Ubuntu and Windows node images are not supported.

  * Your GKE workload must use all available GPUs and your Pod must use all available secondary NICs on a single GKE node. Multiple Pods cannot share RDMA on a single GKE node.

  * You must use the [reservation-bound](https://docs.cloud.google.com/ai-hypercomputer/docs/create/review-configurations#reservation-bound) provisioning model to create clusters with A4X Max. Other provisioning models are not supported.

  * These instructions use [DRANET](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/allocate-network-resources-dra) to configure an AI-optimized GKE cluster with A4X Max. Multi-networking isn't supported for the `a4x-maxgpu-4g-metal` machine type.




### Considerations for creating a cluster

When you create a cluster, consider the following information:

  * **Choose a cluster location** : 
    * Verify that you use a location which has availability for the machine type that you choose. For more information, see [Accelerator availability](https://docs.cloud.google.com/compute/docs/regions-zones/accelerator-zones#view-using-table).
    * When you create node pools in a [regional cluster](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/regional-clusters)—which are recommended for production workloads—you can use the `--node-locations` flag to specify the zones for your GKE nodes.
  * **Choose a driver version** : 
    * The driver version can be one of the following values: 
      * `default`: install the default driver version for your GKE node version. For more information about the requirements for default driver versions, see the Requirements section.
      * `latest`: install the latest available driver version for your GKE version. This option is available only for nodes that use Container-Optimized OS.
      * `disabled`: skip automatic driver installation. You must [manually install a driver](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/gpus#installing_drivers) after you create the node pool.
    * For more information about the default and latest GPU driver versions for GKE node versions, see the table in the section [Manually install NVIDIA GPU drivers](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/gpus#installing_drivers).
  * **Choose a reservation affinity** :

    * You can find information about your reservation, such as the name of your reservation or the name of a specific block in your reservation. To find these values, see [View future reservation requests](https://docs.cloud.google.com/compute/docs/instances/reservations-view#view-future-reservations).
    * The `--reservation-affinity` flag can take the values of `specific` or `any`. However, for high performance distributed AI workloads, we recommend that you use a specific reservation.
    * When you use a specific reservation, including [shared reservations](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/consuming-reservations#specific_shared), specify the value of the `--reservation` flag in the following format:
          
          projects/PROJECT_ID/reservations/RESERVATION_NAME/reservationBlocks/BLOCK_NAME
          

Replace the following values:

      * `PROJECT_ID`: your Google Cloud project ID.
      * `RESERVATION_NAME`: the name of your reservation.
      * `BLOCK_NAME`: the name of a specific block within the reservation.

We also recommend that you use a sub-block targeted reservation so that compute instances are placed on a single sub-block within the `BLOCK_NAME`. Add the following to the end of the path:
    
    /reservationSubBlocks/SUB_BLOCK_NAME
    

Replace `SUB_BLOCK_NAME` with the name of the sub-block.

**Tip:** If the reservation is located in the current project, you can omit `projects/PROJECT_ID/reservations/`from the reservation value.



## Create an AI-optimized GKE cluster that uses A4X Max and GPUDirect RDMA

For distributed AI workloads, multiple GPU nodes are often linked together to work as a single computer. A4X Max is an exascale platform based on NVIDIA GB300 NVL72 rack-scale architecture. A4X Max compute instances use a multi-layered, hierarchical networking architecture with a rail-aligned design to optimize performance for various communication types. This machine type enables scaling and collaboration across multiple GPUs by delivering a high-performance cloud experience for AI workloads. For more information about the network architecture for A4X Max, including the network bandwidth and NIC arrangement, see [A4X Max machine type (bare metal)](https://docs.cloud.google.com/compute/docs/gpus/gpu-network-bandwidth#a4x-max-metal-machine-type).

To create a GKE Standard cluster with A4X Max that uses GPUDirect RDMA and MNNVL, complete the steps that are described in the following sections:

  1. Create the GKE cluster
  2. Create a workload policy
  3. Create a node pool with A4X Max
  4. Configure the MRDMA NICs with `asapd-lite`
  5. Install the NVIDIA Compute Domain CRD and DRA driver
  6. Configure your workload manifest for RDMA and IMEX domain



These instructions use [accelerator network profiles](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/config-auto-net-for-accelerators) to automatically configure VPC networks and subnets for your A4X Max nodes. Alternatively, you can explicitly [specify your VPC network and subnets](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/setup-multinetwork-support-for-pods#create-gke-node-pool).

### Create the GKE cluster

  1. Create a GKE Standard cluster:
         
         gcloud container clusters create CLUSTER_NAME \
           --enable-dataplane-v2 \
           --enable-ip-alias \
           --location=COMPUTE_REGION \
           --cluster-version=CLUSTER_VERSION [\
           --services-ipv4-cidr=SERVICE_CIDR \
           --cluster-ipv4-cidr=POD_CIDR \
           --addons=GcpFilestoreCsiDriver=ENABLED]
         

Replace the following:

     * `CLUSTER_NAME`: the name of your cluster.
     * `CLUSTER_VERSION`: the version of your new cluster. For more information about which version of GKE supports your configuration, see the Requirements in this document.
     * `COMPUTE_REGION`: the name of the compute region.
     * Optionally, you can explicitly provide the secondary CIDR ranges for services and Pods. If you use these optional flags, then replace the following variables:

       * `SERVICE_CIDR`: the secondary CIDR range for services.
       * `POD_CIDR`: the secondary CIDR range for Pods.

When you use these flags, you must verify that the CIDR ranges don't overlap with subnet ranges for additional node networks. For example, consider `SERVICE_CIDR=10.65.0.0/19` and `POD_CIDR=10.64.0.0/19`. For more information, see [Adding Pod IPv4 address ranges](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/multi-pod-cidr).

  2. To run the `kubectl` commands in the next sections, connect to your cluster:
         
         gcloud container clusters get-credentials CLUSTER_NAME --location=COMPUTE_REGION
         

Replace the following:

     * `CLUSTER_NAME`: the name of your cluster.
     * `COMPUTE_REGION`: the name of the compute region.

For more information, see [Install kubectl and configure cluster access](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/cluster-access-for-kubectl).




### Create a workload policy

A workload policy is required to create a partition. For more information, see [Workload policy for MIGs](https://docs.cloud.google.com/ai-hypercomputer/docs/placement-policy-and-workload-policy#workload-policy).

Create a `HIGH_THROUGHPUT` workload policy with the `accelerator_topology` field set to `1x72`.
    
    
    gcloud beta compute resource-policies create workload-policy WORKLOAD_POLICY_NAME \
        --type HIGH_THROUGHPUT \
        --accelerator-topology 1x72 \
        --project PROJECT \
        --region COMPUTE_REGION
    

Replace the following:

  * `WORKLOAD_POLICY_NAME`: the name of your workload policy.
  * `PROJECT`: the name of your project.
  * `COMPUTE_REGION`: the name of the compute region.



### Create a node pool with A4X Max

  1. Create the following configuration file to [pre-allocate hugepages](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/node-system-config#pre-allocated-hugepages) with the node pool:
         
         cat > node_custom.yaml <<EOF
         linuxConfig:
           hugepageConfig:
             hugepage_size2m: 4096
         EOF
         
         export NODE_CUSTOM=node_custom.yaml
         

  2. Create an A4X Max node pool:
         
         gcloud container node-pools create NODE_POOL_NAME \
             --cluster=CLUSTER_NAME \
             --location=COMPUTE_REGION \
             --node-locations=COMPUTE_ZONE \
             --num-nodes=NODE_COUNT \
             --placement-policy=WORKLOAD_POLICY_NAME \
             --machine-type=a4x-maxgpu-4g-metal \
             --accelerator=type=nvidia-gb300,count=4,gpu-driver-version=latest \
             --system-config-from-file=${NODE_CUSTOM} \
             --accelerator-network-profile=auto \
             --node-labels=cloud.google.com/gke-networking-dra-driver=true,cloud.google.com/gke-dpv2-unified-cni=cni-migration \
             --reservation-affinity=specific \
             --reservation=RESERVATION_NAME/reservationBlocks/BLOCK_NAME/reservationSubBlocks/SUB_BLOCK_NAME
         

Replace the following:

     * `NODE_POOL_NAME`: the name of the node pool.
     * `CLUSTER_NAME`: the name of your cluster.
     * `COMPUTE_REGION`: the compute region of the cluster.
     * `COMPUTE_ZONE`: the zone of your node pool.
     * `NODE_COUNT`: the number of nodes for the node pool, which must be 18 nodes or less. We recommend using 18 nodes to obtain the GPU topology of `1x72` in one sub-block using an NVLink domain.
     * `WORKLOAD_POLICY_NAME`: the name of the workload policy you created previously.
     * `RESERVATION_NAME`: the name of your reservation. To find this value, see [View future reservation requests](https://docs.cloud.google.com/compute/docs/instances/reservations-view#view-future-reservations).
     * `BLOCK_NAME`: the name of a specific block within the reservation. To find this value, see [View future reservation requests](https://docs.cloud.google.com/compute/docs/instances/reservations-view#view-future-reservations).

This command automatically creates a network that connects all the A4X Max nodes within a single zone by using the `auto` accelerator network profile. When you create a node pool with the `--accelerator-network-profile=auto` flag, GKE automatically adds the `gke.networks.io/accelerator-network-profile: auto` label to the nodes. To schedule workloads on these nodes, you must include this label in your workload's `nodeSelector` field.




## Configure the MRDMA NICs with `asapd-lite`

The `asapd-lite` DaemonSet configures the MRDMA NICs. An unhealthy `asapd-lite` DaemonSet might indicate no RDMA connectivity.

  1. Install the DaemonSet:
         
         kubectl apply -f https://raw.githubusercontent.com/GoogleCloudPlatform/container-engine-accelerators/refs/heads/master/asapd-lite-installer/asapd-lite-installer-a4x-max-bm-cos.yaml
         

  2. Validate the replicas in the `asapd-lite` DaemonSet:
         
         kubectl get daemonset -n kube-system asapd-lite
         

The output is similar to the following:
         
         NAME         DESIRED   CURRENT   READY   UP-TO-DATE   AVAILABLE   NODE SELECTOR   AGE
         asapd-lite   18        18        18      18           18          <none>          5m
         

The number of `READY` replicas should match the number of nodes that were created and are healthy in the node pool.




### Install the NVIDIA Compute Domain CRD and DRA driver

The following steps install the NVIDIA Compute Domain CRD and DRA driver to enable the use of MNNVL. For more information, see [NVIDIA DRA Driver for GPUs](https://docs.nvidia.com/datacenter/cloud-native/gpu-operator/latest/dra-cds.html).

  1. Verify that you have Helm installed in your development environment. Helm comes pre-installed on [Cloud Shell](https://docs.cloud.google.com/shell).

Although there is no specific Helm version requirement, you can use the following command to verify that you have Helm installed.
         
         helm version
         

If the output is similar to `Command helm not found`, then you can install the Helm CLI:
         
         curl -fsSL -o get_helm.sh https://raw.githubusercontent.com/helm/helm/master/scripts/get-helm-3 \
           && chmod 700 get_helm.sh \
           && ./get_helm.sh
         

  2. Add the NVIDIA Helm repository:
         
         helm repo add nvidia https://helm.ngc.nvidia.com/nvidia \
           && helm repo update
         

  3. Create a `ResourceQuota` object for the DRA Driver:
         
         export POD_QUOTA=POD_QUOTA
         
         kubectl create ns nvidia-dra-driver-gpu
         
         kubectl apply -n nvidia-dra-driver-gpu -f - << EOF
         apiVersion: v1
         kind: ResourceQuota
         metadata:
           name: nvidia-dra-driver-gpu-quota
         spec:
           hard:
             pods: ${POD_QUOTA}
           scopeSelector:
             matchExpressions:
             - operator: In
               scopeName: PriorityClass
               values:
                 - system-node-critical
                 - system-cluster-critical
         EOF
         

Replace `POD_QUOTA` with a number at least 2 times the number of A4X Max nodes in the cluster plus 1. For example, you must set the variable to at least 37 if you have 18 A4X Max nodes in your cluster.

  4. Install the ComputeDomain CRD and DRA driver:
         
         helm install nvidia-dra-driver-gpu nvidia/nvidia-dra-driver-gpu \
             --set controller.args.v=4 --set kubeletPlugin.args.v=4 \
             --version="25.8.0" \
             --create-namespace \
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
                   - matchExpressions:
                     - key: "nvidia.com/gpu"
                       operator: "DoesNotExist"
         
         kubeletPlugin:
           affinity:
             nodeAffinity:
               requiredDuringSchedulingIgnoredDuringExecution:
                 nodeSelectorTerms:
                   - matchExpressions:
                       - key: cloud.google.com/gke-accelerator
                         operator: In
                         values:
                           - nvidia-gb300
                       - key: kubernetes.io/arch
                         operator: In
                         values:
                           - arm64
         
           tolerations:
             - key: nvidia.com/gpu
               operator: Equal
               value: present
               effect: NoSchedule
             - key: kubernetes.io/arch
               operator: Equal
               value: arm64
               effect: NoSchedule
         EOF
         )
         

**Note:** If you plan to upgrade the ComputeDomain CRD and DRA driver, review the [k8s-dra-driver-gpu release notes](https://github.com/NVIDIA/k8s-dra-driver-gpu/releases) for more information about how to upgrade. The upgrade process might require extra steps.



### Configure your workload manifest for RDMA and IMEX domain

  1. Add a node affinity rule to schedule the workload on Arm nodes:
         
         spec:
           affinity:
             nodeAffinity:
               requiredDuringSchedulingIgnoredDuringExecution:
                 nodeSelectorTerms:
                 -   matchExpressions:
                   -   key: kubernetes.io/arch
                     operator: In
                     values:
                     -   arm64
         

  2. Add the following volume to the Pod specification:
         
         spec:
           volumes:
             - name: library-dir-host
               hostPath:
                 path: /home/kubernetes/bin/nvidia
         

  3. Add the following volume mounts, environment variable, and resource to the container that requests GPUs. Your workload container must request all four GPUs:
         
         containers:
           - name: my-container
             volumeMounts:
               - name: library-dir-host
                 mountPath: /usr/local/nvidia
         
             env:
               - name: LD_LIBRARY_PATH
                 value: /usr/local/nvidia/lib64
             resources:
               limits:
                 nvidia.com/gpu: 4
         

  4. Create the `ComputeDomain` resource for the workload:
         
         apiVersion: resource.nvidia.com/v1beta1
         kind: ComputeDomain
         metadata:
           name: a4x-max-compute-domain
         spec:
           numNodes: NUM_NODES
           channel:
             resourceClaimTemplate:
               name: a4x-max-compute-domain-channel
         

Replace `NUM_NODES` with the number of nodes the workload requires.

  5. Create a ResourceClaimTemplate to allocate network resources by using DRANET and request RDMA devices for your Pod:
         
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
                   allocationMode: ExactCount
                   count: 8
         

  6. Specify the ResourceClaimTemplate that the Pod uses:
         
         spec:
           ...
           volumes:
             ...
           containers:
             - name: my-container
               ...
               resources:
                 limits:
                   nvidia.com/gpu: 4
           claims:
                   - name: compute-domain-channel
                   - name: rdma
                 ...
         resourceClaims:
           - name: compute-domain-channel
             resourceClaimTemplateName: a4x-max-compute-domain-channel
           - name: rdma
             resourceClaimTemplateName: all-mrdma
         

  7. Install the latest userspace libraries in your container image:

### Debian 12+/Ubuntu 20.04+ (.deb package)
         
         apt update
         apt install curl
         
         # Fetch DOCA OFED userspace libraries
         export DOCA_URL="https://linux.mellanox.com/public/repo/doca/latest/ubuntu22.04/arm64-sbsa/"
         export BASE_URL="https://linux.mellanox.com/public/repo/doca"
         curl "${BASE_URL}/GPG-KEY-Mellanox.pub" | gpg --dearmor -o /etc/apt/trusted.gpg.d/GPG-KEY-Mellanox.pub
         echo "deb [signed-by=/etc/apt/trusted.gpg.d/GPG-KEY-Mellanox.pub] ${DOCA_URL} ./" | tee /etc/apt/sources.list.d/doca.list
         
         apt update
         apt install doca-ofed-userspace
         
         # Upgrade to latest NCCL for best compatibility
         apt install --only-upgrade --allow-change-held-packages libnccl2 libnccl-dev




A completed Pod specification looks like the following:
    
    
    apiVersion: resource.nvidia.com/v1beta1
    kind: ComputeDomain
    metadata:
      name: a4x-max-compute-domain
    spec:
      numNodes:  NUM_NODES
      channel:
        resourceClaimTemplate:
          name: a4x-max-compute-domain-channel
    ---
    apiVersion: apps/v1
    kind: Pod
    metadata:
      name: my-pod
      labels:
        k8s-app: my-pod
    spec:
      ...
      affinity:
        nodeAffinity:
          requiredDuringSchedulingIgnoredDuringExecution:
            nodeSelectorTerms:
            - matchExpressions:
              - key: kubernetes.io/arch
                operator: In
                values:
                - arm64
      volumes:
        - name: library-dir-host
          hostPath:
            path: /home/kubernetes/bin/nvidia
      hostNetwork: true
      containers:
        - name: my-container
          volumeMounts:
            - name: library-dir-host
              mountPath: /usr/local/nvidia
          env:
            - name: LD_LIBRARY_PATH
              value: /usr/local/nvidia/lib64
          resources:
            limits:
              nvidia.com/gpu: 4
            claims:
              - name: compute-domain-channel
              - name: rdma
            ...
      resourceClaims:
        - name: compute-domain-channel
          resourceClaimTemplateName: a4x-max-compute-domain-channel
        - name: rdma
          resourceClaimTemplateName: all-mrdma
    

## Test network performance

We recommend that you validate the functionality of the provisioned clusters. To do so, use NCCL/gIB tests, which are [NVIDIA Collective Communications Library (NCCL) tests](https://developer.nvidia.com/nccl) that are optimized for the Google environment.

For more information, see [Run NCCL on GKE clusters that use A4X Max](https://docs.cloud.google.com/ai-hypercomputer/docs/nccl/test-gke-custom-a4x-max).

## What's next

  * To learn about scheduling workloads on your GKE clusters by using TAS and Kueue, see [Schedule GKE workloads with Topology Aware Scheduling](https://docs.cloud.google.com/ai-hypercomputer/docs/workloads/schedule-gke-workloads-tas).
  * To learn about managing common events relevant to GKE clusters and AI workloads, see [Manage AI-optimized GKE clusters](https://docs.cloud.google.com/ai-hypercomputer/docs/manage/manage-gke-clusters). 



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
