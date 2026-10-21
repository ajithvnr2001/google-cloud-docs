---
url: https://docs.cloud.google.com/kubernetes-engine/docs/tutorials/scaling-rl-verl-gke/
title: Fine-tune and scale reinforcement learning with verl on GKE \u00a0|\u00a0 GKE AI/ML \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T12:26:02.178689+00:00
---

# Fine-tune and scale reinforcement learning with verl on GKE  |  GKE AI/ML  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/docs/tutorials/scaling-rl-verl-gke/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ Google Kubernetes Engine (GKE) ](https://docs.cloud.google.com/kubernetes-engine/docs)
  * [ GKE AI/ML ](https://docs.cloud.google.com/kubernetes-engine/docs/integrations/ai-infra)
  * [ Guides ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/machine-learning)



Send feedback 

#  Fine-tune and scale reinforcement learning with verl on GKE Stay organized with collections  Save and categorize content based on your preferences. 

[ Autopilot ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/autopilot-overview) [ Standard ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/choose-cluster-mode)

This tutorial shows you how to orchestrate a distributed training environment for reinforcement learning on Google Kubernetes Engine (GKE). You use Ray and the [**verl** (Volcano Engine Reinforcement Learning)](https://verl.readthedocs.io/en/latest/index.html) framework to set up a distributed training environment to fine-tune a Qwen2.5-32B-Instruct model on the GSM8K dataset.

This tutorial focuses on the Group Relative Policy Optimization (GRPO) training pipeline on GKE with Ray and **verl**. GRPO is a reinforcement learning algorithm designed to improve a model's reasoning ability. This memory-efficient algorithm simplifies the reinforcement learning (RL) process by eliminating the Critic, or _value model_ , and using a relative group-based calculation instead.

This tutorial is a good starting point if you need to set up a distributed training environment where data, model weights, and the training engine are decoupled for efficiency.

This tutorial supports the following GPU architectures:

  * **Intel or AMD-based GPU nodes** : Set up and scale using NVIDIA B200 or H200 GPUs, using GKE Dynamic Resource Allocation (DRA) for Autopilot path.
  * **Arm-based A4X (GB200) nodes** : Set up and scale using NVIDIA GB200 Grace Blackwell Superchips, using GKE Dynamic Resource Allocation (DRA) and Multi-Node NVLink (IMEX).



## Background

The following sections provide a brief overview of the concepts used in this tutorial.

### Reinforcement learning (RL)

RL teaches models through experience, exploration, and feedback rather than static imitation. Although pre-training teaches a model what to say, reinforcement learning from human feedback (RLHF) teaches it how to be helpful, safe, and logical. RL serves as the bridge between a base model and a fine-tuned model for a specialized use case.

For more information, see [What is reinforcement learning?](https://cloud.google.com/discover/what-is-reinforcement-learning)

### Group Relative Policy Optimization (GRPO)

_GRPO_ , an algorithm popularized by DeepSeek, offers a memory-efficient alternative to Proximal Policy Optimization (PPO) for LLM alignment by removing the Critic model. Instead of a Critic network, GRPO generates a group of responses for the same prompt and uses the average reward of that group as the baseline.

For more information, see [GRPO](https://verl.readthedocs.io/en/latest/algo/grpo.html).

### Volcano Engine Reinforcement Learning (verl)

**verl** is a high-performance framework designed to handle the complex memory and compute patterns of LLM-based RL.

For more information, see [verl](https://github.com/volcengine/verl).

## Objectives

This tutorial shows you how set up reinforcement learning on GKE with verl, by completing the following steps:

  1. Set up a GKE cluster with A4X (GB200 Superchips), A4 (B200 GPUs), or A3 Ultra (H200 GPUs).
  2. Configure KubeRay to manage a distributed Ray cluster.
  3. Use Cloud Storage FUSE to mount a Cloud Storage bucket across all nodes.
  4. Run a GRPO training job using **verl** to align the Qwen2.5-32B-Instruct model with the GSM8K dataset.



## Before you begin

  * This tutorial uses [Cloud Shell](https://docs.cloud.google.com/shell), which comes with the Google Cloud CLI and [`kubectl`](https://kubernetes.io/docs/tasks/tools/#kubectl) preinstalled. If you aren't using Cloud Shell, [install](https://docs.cloud.google.com/sdk/docs/install) and [initialize](https://docs.cloud.google.com/sdk/docs/initialize) the Google Cloud CLI, and [install `kubectl`](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/cluster-access-for-kubectl).



  * Sign in to your Google Cloud account. If you're new to Google Cloud, [ create an account](https://console.cloud.google.com/freetrial) to evaluate how our products perform in real-world scenarios. New customers also get $300 in free credits to run, test, and deploy workloads. 
  * [Install](https://docs.cloud.google.com/sdk/docs/install) the Google Cloud CLI. 

**Note:** If you installed the gcloud CLI previously, make sure you have the latest version by running `gcloud components update`. 
  * If you're using an external identity provider (IdP), you must first [ sign in to the gcloud CLI with your federated identity](https://docs.cloud.google.com/iam/docs/workforce-log-in-gcloud). 

  * To [initialize](https://docs.cloud.google.com/sdk/docs/initializing) the gcloud CLI, run the following command: 
        
        gcloud init

  * [Create or select a Google Cloud project](https://cloud.google.com/resource-manager/docs/creating-managing-projects).

**Roles required to select or create a project**

    * **Select a project** : Selecting a project doesn't require a specific IAM role—you can select any project that you've been granted a role on. 
    * **Create a project** : To create a project, you need the Project Creator role (`roles/resourcemanager.projectCreator`), which contains the `resourcemanager.projects.create` permission. [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
**Note** : If you don't plan to keep the resources that you create in this procedure, create a project instead of selecting an existing project. After you finish these steps, you can delete the project, removing all resources associated with the project.
    * Create a Google Cloud project:
          
          gcloud projects create PROJECT_ID

Replace `PROJECT_ID` with a name for the Google Cloud project you are creating.

    * Select the Google Cloud project that you created:
          
          gcloud config set project PROJECT_ID

Replace `PROJECT_ID` with your Google Cloud project name.

  * [Verify that billing is enabled for your Google Cloud project](https://docs.cloud.google.com/billing/docs/how-to/verify-billing-enabled#confirm_billing_is_enabled_on_a_project). 

  * Enable the required APIs, if any are not already enabled: 

**Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you created the project, then you likely already have this permission through the Owner role (`roles/owner`). Otherwise, you can get this permission through the Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
        
        gcloud services enable container.googleapis.com storage.googleapis.com compute.googleapis.com

  * [Install](https://docs.cloud.google.com/sdk/docs/install) the Google Cloud CLI. 

**Note:** If you installed the gcloud CLI previously, make sure you have the latest version by running `gcloud components update`. 
  * If you're using an external identity provider (IdP), you must first [ sign in to the gcloud CLI with your federated identity](https://docs.cloud.google.com/iam/docs/workforce-log-in-gcloud). 

  * To [initialize](https://docs.cloud.google.com/sdk/docs/initializing) the gcloud CLI, run the following command: 
        
        gcloud init

  * [Create or select a Google Cloud project](https://cloud.google.com/resource-manager/docs/creating-managing-projects).

**Roles required to select or create a project**

    * **Select a project** : Selecting a project doesn't require a specific IAM role—you can select any project that you've been granted a role on. 
    * **Create a project** : To create a project, you need the Project Creator role (`roles/resourcemanager.projectCreator`), which contains the `resourcemanager.projects.create` permission. [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
**Note** : If you don't plan to keep the resources that you create in this procedure, create a project instead of selecting an existing project. After you finish these steps, you can delete the project, removing all resources associated with the project.
    * Create a Google Cloud project:
          
          gcloud projects create PROJECT_ID

Replace `PROJECT_ID` with a name for the Google Cloud project you are creating.

    * Select the Google Cloud project that you created:
          
          gcloud config set project PROJECT_ID

Replace `PROJECT_ID` with your Google Cloud project name.

  * [Verify that billing is enabled for your Google Cloud project](https://docs.cloud.google.com/billing/docs/how-to/verify-billing-enabled#confirm_billing_is_enabled_on_a_project). 

  * Enable the required APIs, if any are not already enabled: 

**Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you created the project, then you likely already have this permission through the Owner role (`roles/owner`). Otherwise, you can get this permission through the Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
        
        gcloud services enable container.googleapis.com storage.googleapis.com compute.googleapis.com

  * Grant roles to your user account. Run the following command once for each of the following IAM roles: `roles/container.admin, roles/iam.serviceAccountAdmin, roles/storage.admin, roles/iam.serviceAccountUser`
        
        gcloud projects add-iam-policy-binding PROJECT_ID --member="user:USER_IDENTIFIER" --role=ROLE

Replace the following:

    * `PROJECT_ID`: Your project ID.
    * `USER_IDENTIFIER`: The identifier for your user account. For example, `myemail@example.com`. 
    * `ROLE`: The IAM role that you grant to your user account.


  * Create a [Hugging Face](https://huggingface.co/) account, if you don't already have one.
  * Ensure that you have a [Hugging Face token](https://huggingface.co/docs/hub/security-tokens).
  * Ensure your project has sufficient quota for A4X (GB200 Superchips), A4 (B200 GPUs), or A3 Ultra (H200 GPUs). To learn more, see [Plan GPU quota](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/gpus#gpu-quota) and [GPU quota](https://docs.cloud.google.com/compute/resource-usage#gpu_quota).
  * Ensure that you have an active capacity reservation for your GPU machine type. For more information, see [Reserve capacity through your account team](https://docs.cloud.google.com/ai-hypercomputer/docs/reserve-capacity#request-multiple-blocks).
  * For the A4X (GB200) setup, ensure that you have [Helm](https://helm.sh/docs/intro/install/) installed.



## Prepare your environment

In this tutorial, you use [Cloud Shell](https://docs.cloud.google.com/shell).

  1. Go to the [Google Cloud console](https://console.cloud.google.com/).

  2. At the top of the Google Cloud console window, click the **Activate Cloud Shell** button.

  3. Set the environment variables:

### A4 and A3 Ultra

### Autopilot
         
         export PROJECT_ID=$(gcloud config get project)
         export PROJECT_NUMBER=$(gcloud projects describe ${PROJECT_ID} --format="value(projectNumber)")
         export CONTROL_PLANE_REGION="YOUR_REGION"
         export NODE_ZONE="YOUR_ZONE"
         export CLUSTER_NAME="YOUR_CLUSTER_NAME"
         export KSA_NAME="YOUR_KSA_NAME"
         export GS_BUCKET="YOUR_GCS_BUCKET"
         export NAMESPACE="default"
         export GPU_TYPE="YOUR_GPU_TYPE"
         export MACHINE_TYPE="YOUR_MACHINE_TYPE"
         export RESERVATION="YOUR_RESERVATION_NAME"
         export HF_TOKEN="YOUR_HF_TOKEN"

### Standard
         
         export PROJECT_ID=$(gcloud config get project)
         export PROJECT_NUMBER=$(gcloud projects describe ${PROJECT_ID} --format="value(projectNumber)")
         export CONTROL_PLANE_REGION="YOUR_REGION"
         export NODE_ZONE="YOUR_ZONE"
         export CLUSTER_NAME="YOUR_CLUSTER_NAME"
         export KSA_NAME="YOUR_KSA_NAME"
         export GS_BUCKET="YOUR_GCS_BUCKET"
         export NAMESPACE="default"
         export GPU_TYPE="YOUR_GPU_TYPE"
         export MACHINE_TYPE="YOUR_MACHINE_TYPE"
         export CPU_MACHINE_TYPE="YOUR_CPU_MACHINE_TYPE"
         export RESERVATION="YOUR_RESERVATION_NAME"
         export HF_TOKEN="YOUR_HF_TOKEN"
         
         export GVNIC_NETWORK_PREFIX="YOUR_GVNIC_NAME"
         export RDMA_NETWORK_PREFIX="YOUR_RDMA_NAME"

### A4X
         
         export PROJECT_ID=$(gcloud config get project)
         export PROJECT_NUMBER=$(gcloud projects describe ${PROJECT_ID} --format="value(projectNumber)")
         export CONTROL_PLANE_REGION=YOUR_REGION
         export NODE_ZONE=YOUR_ZONE
         export CLUSTER_NAME=YOUR_CLUSTER_NAME
         export KSA_NAME=YOUR_KSA_NAME
         export GS_BUCKET=YOUR_GCS_BUCKET-${PROJECT_ID}
         export NAMESPACE=default
         export GPU_TYPE=YOUR_GPU_TYPE
         export MACHINE_TYPE=YOUR_MACINE_TYPE
         export RESERVATION=YOUR_RESERVATION_NAME
         export HF_TOKEN=YOUR_HF_TOKEN
         
         # A4X (GB200 Superchips) only variables
         export NUM_GPU_NODES=4
         export VERL_IMAGE=verlai/verl:vllm023.aarch64.dev1
         export VERL_REF=ddbcdb7
         

Replace the following values:

     * `YOUR_REGION`: the Compute Engine region for the GKE cluster control plane.
     * `YOUR_ZONE`: the zone where the nodes are reserved. For more information, see [GPU availability](https://docs.cloud.google.com/compute/docs/regions-zones/gpu-regions-zones#view-using-table).
     * `YOUR_CLUSTER_NAME`: the name of your GKE cluster. This name must be 40 characters or less and be composed of lowercase alphanumeric characters and hyphens.
     * `YOUR_KSA_NAME`: the name of your Kubernetes service account.
     * `YOUR_GCS_BUCKET`: the base name for your Cloud Storage bucket. You don't need to specify the `gs://` prefix.
     * `YOUR_GPU_TYPE`: the accelerator that you reserved in the Compute Engine capacity reservation. It must be one of the following values: 
       * **`nvidia-gb200`** : A4X (GB200 Superchips)
       * **`nvidia-b200`** : A4 (B200 GPUs)
       * **`nvidia-h200-141gb`** : A3 Ultra (H200 GPUs)
     * `YOUR_MACHINE_TYPE`: the type of machine to use: 
       * For A4X (GB200 Superchips), use `a4x-highgpu-4g`.
       * For A4 (B200 GPUs), use `a4-highgpu-8g` or later.
       * For A3 Ultra (H200 GPUs), use `a3-ultragpu-8g` or later.
     * `YOUR_CPU_MACHINE_TYPE`: the Compute Engine machine type for the CPU default node pool. Use a `highmem` machine type with at least 16 vCPUs that is supported in your cluster zone, such as `n4-highmem-16` or `n2d-highmem-16`.
     * `YOUR_RESERVATION_NAME`: the name of your capacity reservation.
     * `YOUR_HF_TOKEN`: your Hugging Face token.
     * Use the following variables when setting up your environment in GKE Standard clusters: 
       * `YOUR_GVNIC_NAME` (A4 or A3 Ultra only): the prefix for the gVNIC network name. You can use any prefix that you want.
       * `YOUR_RDMA_NAME` (A4 or A3 Ultra only): the prefix for the remote direct memory access (RDMA) network. You can use any prefix that you want.
  4. Clone the sample repository:
         
         git clone https://github.com/GoogleCloudSamples/AIHypercomputerSamples.git

In the rest of the tutorial, look in your clone of the sample repository to find the specific files that you need to inspect or apply.

  5. Navigate to the working directory for your chosen GKE mode:

### A4 and A3 Ultra

### Autopilot
         
         cd AIHypercomputerSamples/gpu/tuning/verl_rl_autopilot

### Standard
         
         cd AIHypercomputerSamples/gpu/tuning/verl_rl_standard

### A4X

No directory change is required. You can proceed directly to the next section.




## Set up infrastructure

In this section, you create standard VPC networks and the GKE cluster.

### Create RDMA network and subnets (GKE Standard - A4 and A3 Ultra only)

### A4 and A3 Ultra

### Autopilot

This section is required for GKE Standard A4 and A3 Ultra GPUs only.

If you use Autopilot, skip this section and proceed directly to **Create a GKE cluster**. GKE automatically provisions the necessary VPC networks and subnets, and uses GKE managed DRANET to allocate these resources to your Pods. You don't need to manually create any network infrastructure.

### Standard

  1. Create a VPC network for the gVNIC interface:
         
         gcloud compute networks create ${GVNIC_NETWORK_PREFIX}-net \
           --subnet-mode=custom \
           --project=${PROJECT_ID}
         
         gcloud compute networks subnets create ${GVNIC_NETWORK_PREFIX}-sub \
           --network=${GVNIC_NETWORK_PREFIX}-net \
           --region=${CONTROL_PLANE_REGION} \
           --range=192.168.0.0/24 \
           --project=${PROJECT_ID}
         
         gcloud compute firewall-rules create ${GVNIC_NETWORK_PREFIX}-internal \
           --network=${GVNIC_NETWORK_PREFIX}-net \
           --action=ALLOW \
           --rules=tcp:0-65535,udp:0-65535,icmp \
           --source-ranges=192.168.0.0/16 \
           --project=${PROJECT_ID}

  2. Create a VPC network for RDMA:
         
         gcloud compute networks create ${RDMA_NETWORK_PREFIX}-net \
           --network-profile=${NODE_ZONE}-vpc-roce \
           --subnet-mode=custom \
           --project=${PROJECT_ID}

  3. Create the 8 RDMA subnets for the 8 GPUs:
         
         for N in $(seq 0 7); do
           if ! gcloud compute networks subnets describe ${RDMA_NETWORK_PREFIX}-sub-$N --region=${CONTROL_PLANE_REGION} --project=${PROJECT_ID} >/dev/null 2>&1; then
             gcloud compute networks subnets create ${RDMA_NETWORK_PREFIX}-sub-$N \
               --network=${RDMA_NETWORK_PREFIX}-net \
               --region=${CONTROL_PLANE_REGION} \
               --range=192.168.$((N+1)).0/24 \
               --project=${PROJECT_ID} &
           else
             echo "Subnet ${RDMA_NETWORK_PREFIX}-sub-$N already exists."
           fi
         done
         wait




### A4X

This section is required for GKE Standard A4 and A3 Ultra GPUs only.

If you use A4X (GB200) GPUs, skip this section and proceed directly to **Create a GKE cluster**. For A4X (GB200) GPUs or Autopilot, GKE creates the networks automatically when the node pool uses the `auto` accelerator network profile. The Cluster Toolkit blueprint enables this profile by using the `enable_dranet:true` flag.

### Create a GKE cluster

Create a GKE cluster corresponding to your GPU architecture:

### A4 and A3 Ultra

Select the GKE cluster mode that you want to use:

### Autopilot

  1. Create an Autopilot cluster:
         
         gcloud container clusters create-auto ${CLUSTER_NAME} \
             --location=${CONTROL_PLANE_REGION} \
             --release-channel=rapid \
             --enable-ray-operator

  2. Get credentials for your cluster:
         
         gcloud container clusters get-credentials ${CLUSTER_NAME} \
             --location=${CONTROL_PLANE_REGION}




### Standard

  1. Create a Standard cluster:
         
         gcloud container clusters create ${CLUSTER_NAME} \
             --location=${CONTROL_PLANE_REGION} \
             --node-locations=${NODE_ZONE} \
             --enable-dataplane-v2 \
             --workload-pool=${PROJECT_ID}.svc.id.goog \
             --enable-ip-alias \
             --enable-multi-networking \
             --addons=RayOperator,GcsFuseCsiDriver \
             --machine-type=${CPU_MACHINE_TYPE} \
             --num-nodes=1 \
             --min-nodes=1 \
             --max-nodes=5 \
             --enable-autoscaling \
             --project=${PROJECT_ID}

  2. Get credentials for your cluster:
         
         gcloud container clusters get-credentials ${CLUSTER_NAME} \
             --location=${CONTROL_PLANE_REGION} \
             --project=${PROJECT_ID}

  3. Create the GPU node pool. These node pools use your reservation to ensure availability. You start with two nodes:
         
         RESERVATION_ARGS=("--reservation-affinity=none")
         if [ -n "${RESERVATION:-}" ]; then
           RESERVATION_ARGS=("--reservation-affinity=specific" "--reservation=${RESERVATION}")
         fi
         gcloud container node-pools create gpu-pool \
             --cluster="${CLUSTER_NAME}" \
             --location="${CONTROL_PLANE_REGION}" \
             --node-locations="${NODE_ZONE}" \
             --machine-type="${MACHINE_TYPE}" \
             --accelerator="type=${GPU_TYPE},count=8,gpu-driver-version=DEFAULT" \
             --num-nodes=2 \
             "${RESERVATION_ARGS[@]}" \
             --additional-node-network="network=${GVNIC_NETWORK_PREFIX}-net,subnetwork=${GVNIC_NETWORK_PREFIX}-sub" \
             --additional-node-network="network=${RDMA_NETWORK_PREFIX}-net,subnetwork=${RDMA_NETWORK_PREFIX}-sub-0" \
             --additional-node-network="network=${RDMA_NETWORK_PREFIX}-net,subnetwork=${RDMA_NETWORK_PREFIX}-sub-1" \
             --additional-node-network="network=${RDMA_NETWORK_PREFIX}-net,subnetwork=${RDMA_NETWORK_PREFIX}-sub-2" \
             --additional-node-network="network=${RDMA_NETWORK_PREFIX}-net,subnetwork=${RDMA_NETWORK_PREFIX}-sub-3" \
             --additional-node-network="network=${RDMA_NETWORK_PREFIX}-net,subnetwork=${RDMA_NETWORK_PREFIX}-sub-4" \
             --additional-node-network="network=${RDMA_NETWORK_PREFIX}-net,subnetwork=${RDMA_NETWORK_PREFIX}-sub-5" \
             --additional-node-network="network=${RDMA_NETWORK_PREFIX}-net,subnetwork=${RDMA_NETWORK_PREFIX}-sub-6" \
             --additional-node-network="network=${RDMA_NETWORK_PREFIX}-net,subnetwork=${RDMA_NETWORK_PREFIX}-sub-7" \
             --project="${PROJECT_ID}"

  4. Install the NCCL RDMA installer used for Standard clusters:
         
         kubectl apply -f https://raw.githubusercontent.com/GoogleCloudPlatform/container-engine-accelerators/refs/heads/master/gpudirect-rdma/nccl-rdma-installer.yaml




### A4X

  1. Create a GKE cluster and node pool by using the [Cluster Toolkit `gke-a4x` blueprint](https://github.com/GoogleCloudPlatform/cluster-toolkit). The blueprint provisions the GKE cluster, including the A4X node pool bound to your reservation, the accelerator networks (one additional gVNIC plus four RDMA rails), and the managed DRANET driver that exposes the CX-7 NICs as DRA devices.

Use the blueprint's deployment instructions to configure your parameters (such as `PROJECT_ID`, `CONTROL_PLANE_REGION`, `NODE_ZONE`, reservation, and `NUM_GPU_NODES`), then deploy the cluster. Alternatively, you can follow the [A4X GKE cluster creation guide](https://docs.cloud.google.com/ai-hypercomputer/docs/create/gke-ai-hypercompute-custom-a4x) to create a cluster manually.

     1. Get credentials for your cluster:
    
    gcloud container clusters get-credentials ${CLUSTER_NAME} --location=${CONTROL_PLANE_REGION}
    

  2. Verify that the cluster exposes RDMA NICs through DRA:
         
         kubectl get deviceclasses
         

The output must include `mrdma.google.com`.

  3. Verify that the A4X nodes are present:
         
         kubectl get nodes -l cloud.google.com/gke-accelerator=nvidia-gb200
         

  4. Install the gIB NCCL plugin (A4X variant):
         
         kubectl apply -f https://raw.githubusercontent.com/GoogleCloudPlatform/container-engine-accelerators/master/gpudirect-rdma/nccl-rdma-installer-a4x.yaml
         

  5. Install the NVIDIA DRA driver, which provides `ComputeDomain` (IMEX) channels for multi-node NVLink:
         
         helm repo add nvidia https://helm.ngc.nvidia.com/nvidia && helm repo update
         kubectl create namespace nvidia-dra-driver-gpu
         kubectl apply -f - <<EOF
         apiVersion: v1
         kind: ResourceQuota
         metadata:
           name: nvidia-dra-driver-gpu-quota
           namespace: nvidia-dra-driver-gpu
         spec:
           hard:
             pods: "$((2 * NUM_GPU_NODES + 1))"
           scopeSelector:
             matchExpressions:
             - operator: In
               scopeName: PriorityClass
               values:
               - system-node-critical
               - system-cluster-critical
         EOF
         helm upgrade --install nvidia-dra-driver-gpu nvidia/nvidia-dra-driver-gpu \
           --version=25.3.1 --namespace nvidia-dra-driver-gpu \
           --set nvidiaDriverRoot=/home/kubernetes/bin/nvidia \
           --set resources.gpus.enabled=false \
           --set kubeletPlugin.tolerations[0].key=nvidia.com/gpu \
           --set kubeletPlugin.tolerations[0].operator=Exists \
           --set kubeletPlugin.tolerations[1].key=kubernetes.io/arch \
           --set kubeletPlugin.tolerations[1].operator=Exists
         

  6. Install the KubeRay operator, scoped to the workload namespace:
         
         kubectl create namespace ${NAMESPACE}
         helm repo add kuberay https://ray-project.github.io/kuberay-helm/ && helm repo update
         helm upgrade --install kuberay-operator kuberay/kuberay-operator \
           --namespace ${NAMESPACE} \
           --set singleNamespaceInstall=true --set "watchNamespace={${NAMESPACE}}"
         




### Configure network mappings (GKE Standard - A4 and A3 Ultra only)

### A4 and A3 Ultra

### Autopilot

This step is required for GKE Standard GPU setups (A4 and A3 Ultra only). If you use A4X (GB200), GKE manages network interfaces automatically, so skip this section.

### Standard

  1. Inspect the `network-mapping.yaml` manifest:
         
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
         ---
         apiVersion: networking.gke.io/v1
         kind: GKENetworkParamSet
         metadata:
           name: rdma-4
         spec:
           vpc: ${RDMA_NETWORK_PREFIX}-net
           vpcSubnet: ${RDMA_NETWORK_PREFIX}-sub-4
           deviceMode: RDMA
         ---
         apiVersion: networking.gke.io/v1
         kind: Network
         metadata:
           name: rdma-4
         spec:
           type: "Device"
           parametersRef:
             group: networking.gke.io
             kind: GKENetworkParamSet
             name: rdma-4
         ---
         apiVersion: networking.gke.io/v1
         kind: GKENetworkParamSet
         metadata:
           name: rdma-5
         spec:
           vpc: ${RDMA_NETWORK_PREFIX}-net
           vpcSubnet: ${RDMA_NETWORK_PREFIX}-sub-5
           deviceMode: RDMA
         ---
         apiVersion: networking.gke.io/v1
         kind: Network
         metadata:
           name: rdma-5
         spec:
           type: "Device"
           parametersRef:
             group: networking.gke.io
             kind: GKENetworkParamSet
             name: rdma-5
         ---
         apiVersion: networking.gke.io/v1
         kind: GKENetworkParamSet
         metadata:
           name: rdma-6
         spec:
           vpc: ${RDMA_NETWORK_PREFIX}-net
           vpcSubnet: ${RDMA_NETWORK_PREFIX}-sub-6
           deviceMode: RDMA
         ---
         apiVersion: networking.gke.io/v1
         kind: Network
         metadata:
           name: rdma-6
         spec:
           type: "Device"
           parametersRef:
             group: networking.gke.io
             kind: GKENetworkParamSet
             name: rdma-6
         ---
         apiVersion: networking.gke.io/v1
         kind: GKENetworkParamSet
         metadata:
           name: rdma-7
         spec:
           vpc: ${RDMA_NETWORK_PREFIX}-net
           vpcSubnet: ${RDMA_NETWORK_PREFIX}-sub-7
           deviceMode: RDMA
         ---
         apiVersion: networking.gke.io/v1
         kind: Network
         metadata:
           name: rdma-7
         spec:
           type: "Device"
           parametersRef:
             group: networking.gke.io
             kind: GKENetworkParamSet
             name: rdma-7

  2. Apply the manifest:
         
         envsubst < network-mapping.yaml | kubectl apply -f -




### A4X

This step is required for GKE Standard GPU setups (A4 and A3 Ultra only). If you use A4X (GB200), GKE manages network interfaces automatically, so skip this section.

## Prepare data and storage

Configure Cloud Storage and Kubernetes resources:

  1. Create a Cloud Storage bucket:
         
         gcloud storage buckets create "gs://${GS_BUCKET}" \
           --location="${CONTROL_PLANE_REGION}" \
           --project="${PROJECT_ID}" \
           --enable-hierarchical-namespace \
           --uniform-bucket-level-access

  2. Create a Kubernetes Service Account (KSA) and bind it to the bucket:
         
         kubectl create serviceaccount ${KSA_NAME} -n ${NAMESPACE}
         gcloud storage buckets add-iam-policy-binding "gs://${GS_BUCKET}" \
           --member="principal://iam.googleapis.com/projects/${PROJECT_NUMBER}/locations/global/workloadIdentityPools/${PROJECT_ID}.svc.id.goog/subject/ns/${NAMESPACE}/sa/${KSA_NAME}" \
           --role="roles/storage.objectUser"

  3. Create the Secret for Hugging Face:
         
         kubectl create secret generic hf-secret --from-literal=hf_token=${HF_TOKEN}

  4. Inspect the `gcsfuse-storage.yaml` manifest:
         
         apiVersion: v1
         kind: PersistentVolume
         metadata:
           name: training-bucket-pv
         spec:
           accessModes:
           -   ReadWriteMany
           capacity:
             storage: 768Gi
           persistentVolumeReclaimPolicy: Delete
           storageClassName: gcsfuse-sc
           mountOptions:
           -   implicit-dirs
           -   metadata-cache:negative-ttl-secs:0
           -   metadata-cache:ttl-secs:0
           -   metadata-cache:stat-cache-max-size-mb:-1
           -   metadata-cache:type-cache-max-size-mb:-1
           -   file-cache:max-size-mb:-1
           -   file-cache:cache-file-for-range-read:true
           -   file-cache:enable-parallel-downloads:true
           -   read_ahead_kb=1024
           -   write:enable-streaming-writes:true
           -   write:global-max-blocks:200000
           csi:
             driver: gcsfuse.csi.storage.gke.io
             volumeHandle: ${GS_BUCKET}
             volumeAttributes:
               skipCSIBucketAccessCheck: "true"
               gcsfuseMetadataPrefetchOnMount: "true"
         ---
         apiVersion: v1
         kind: PersistentVolumeClaim
         metadata:
           name: training-bucket-pvc
         spec:
           accessModes:
           -   ReadWriteMany
           resources:
             requests:
               storage: 768Gi
           storageClassName: gcsfuse-sc

  5. Apply the manifest:
         
         envsubst < gcsfuse-storage.yaml | kubectl apply -f - 




## Setup DRANET

Configure your DRANET:

### A4 and A3 Ultra

### Autopilot

  1. Create the ComputeClass manifest:
         
         echo "Generating computeclass-dranet.yaml..."
         cat <<EOF > computeclass-dranet.yaml
         apiVersion: cloud.google.com/v1
         kind: ComputeClass
         metadata:
           name: dranet-a4-computeclass-v3
         spec:
           nodePoolAutoCreation:
             enabled: true
           nodePoolConfig:
             dra:
               networking:
                 enabled: true
           priorities:
           - machineType: ${MACHINE_TYPE}
             gpu:
               count: 8
               type: ${GPU_TYPE}
             acceleratorNetworkProfile: auto
         EOF
         
         if [ -n "${RESERVATION:-}" ]; then
           echo "Adding reservation affinity for ${RESERVATION} to ComputeClass..."
           cat <<EOF >> computeclass-dranet.yaml
             reservations:
               affinity: Specific
               specific:
               - name: ${RESERVATION}
                 project: ${PROJECT_ID}
         EOF
         fi

  2. Apply both the `computeclass-dranet.yaml` manifest (created in the previous step) and the `resourceclaim-dranet.yaml` manifest (included in the sample repository):
         
         echo "Applying ComputeClass..."
         kubectl apply -f computeclass-dranet.yaml
         
         echo "Applying ResourceClaimTemplate..."
         kubectl apply -f resourceclaim-dranet.yaml




### Standard

No DRANET setup is required. You can proceed directly to the next section.

### A4X

DRANET is set by Cluster Toolkit. You can proceed directly to the next section.

## Prepare model and data

Populate your Cloud Storage bucket with the model weights and datasets. You can run these commands locally or on a GKE Pod to populate the bucket:

### A4 and A3 Ultra

### Autopilot

  1. Inspect the `data-prep-job.yaml` manifest, which configures the data preparation Job:
         
         apiVersion: batch/v1
         kind: Job
         metadata:
           name: data-prep-job
           namespace: ${NAMESPACE}
         spec:
           template:
             metadata:
               annotations:
                 gke-gcsfuse/volumes: "true"
                 gke-gcsfuse/cpu-limit: "4"
                 gke-gcsfuse/memory-limit: "8Gi"
                 gke-gcsfuse/ephemeral-storage-limit: "50Gi"
             spec:
               serviceAccountName: ${KSA_NAME}
               restartPolicy: OnFailure
               nodeSelector:
                 cloud.google.com/compute-class: Performance
                 cloud.google.com/machine-family: c3
               containers:
               - name: prep-data
                 image: verlai/verl:vllm011.latest
                 resources:
                   requests:
                     cpu: "8"
                     memory: "16Gi"
                     ephemeral-storage: "50Gi"
                   limits:
                     cpu: "8"
                     memory: "16Gi"
                     ephemeral-storage: "50Gi"
                 env:
                 - name: HF_TOKEN
                   valueFrom:
                     secretKeyRef:
                       name: hf-secret
                       key: hf_token
                 - name: HF_HOME
                   value: /data/.cache/huggingface
                 - name: HF_HUB_DISABLE_XET
                   value: "1"
                 command: ["/bin/bash", "-c"]
                 args:
                 - |
                   set -euo pipefail
         
                   # Clone verl to GCS (for worker pods)
                   if [ ! -d "/data/verl" ]; then
                     echo "Cloning verl to GCS..."
                     git clone --depth 1 --branch v0.6.1 https://github.com/volcengine/verl.git /data/verl
         
                     echo "Installing verl on GCS to generate metadata..."
                     pip3 install --no-deps -e /data/verl
                   else
                     echo "verl already exists in /data/verl"
                   fi
         
                   # Clone verl locally for fast installation
                   echo "Cloning verl locally..."
                   git clone --depth 1 --branch v0.6.1 https://github.com/volcengine/verl.git /tmp/verl
         
                   # Install verl package from local clone
                   echo "Installing verl package..."
                   pip3 install --no-cache-dir --no-deps /tmp/verl
                   rm -rf /tmp/verl
         
                   # Preprocess GSM8K
                   if [ ! -d "/data/gsm8k" ]; then
                     echo "Preprocessing GSM8K..."
                     python /data/verl/examples/data_preprocess/gsm8k.py --local_save_dir /data/gsm8k
                   else
                     echo "GSM8K data already exists in /data/gsm8k"
                   fi
         
                   # Download model sequentially to support GCS FUSE direct streaming writes
                   if [ ! -d "/data/Qwen2.5-32B-Instruct" ]; then
                     echo "Downloading Qwen2.5-32B-Instruct..."
                     huggingface-cli download Qwen/Qwen2.5-32B-Instruct --local-dir /data/Qwen2.5-32B-Instruct --local-dir-use-symlinks False
                   else
                     echo "Model Qwen2.5-32B-Instruct already exists in /data/Qwen2.5-32B-Instruct"
                   fi
         
                   echo "Data preparation complete!"
                 volumeMounts:
                 - name: training-bucket-vol
                   mountPath: /data
               volumes:
               - name: training-bucket-vol
                 persistentVolumeClaim:
                   claimName: training-bucket-pvc

**Note:** In Autopilot, specifying `cloud.google.com/compute-class: Performance` without a machine series defaults to the C4 machine series. If you don't have C4 quota in your region, then the Pod might remain in the `Pending` state. This manifest specifies `cloud.google.com/machine-family: c3`. You can change this value in `data-prep-job.yaml` to another [supported machine series](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/performance-pods#supported-machine-series) (such as `c2` or `c4`) based on regional availability and your project's quota.
  2. Launch the job:
         
         envsubst < "data-prep-job.yaml" | kubectl apply -f -

  3. Check the Pod status:
         
         watch kubectl get pods -n ${NAMESPACE}

After the `data-prep-job` Pod has reached the `Running` status, press `Control+C` to stop watching.

  4. Monitor the job:
         
         kubectl logs -n ${NAMESPACE} -l job-name=data-prep-job -f

The `kubectl logs` command returns minimal or no output until the Pod reaches the `Running` status.




### Standard

  1. Inspect the `data-prep-job.yaml` manifest, which configures the data preparation Job:
         
         apiVersion: batch/v1
         kind: Job
         metadata:
           name: data-prep-job
           namespace: ${NAMESPACE}
         spec:
           template:
             metadata:
               annotations:
                 gke-gcsfuse/volumes: "true"
                 gke-gcsfuse/cpu-limit: "2"
                 gke-gcsfuse/memory-limit: "4Gi"
                 gke-gcsfuse/ephemeral-storage-limit: "20Gi"
             spec:
               serviceAccountName: ${KSA_NAME}
               restartPolicy: OnFailure
               nodeSelector:
                 cloud.google.com/gke-nodepool: "default-pool"
               containers:
               - name: prep-data
                 image: verlai/verl:vllm011.latest
                 resources:
                   requests:
                     cpu: "4"
                     memory: "8Gi"
                     ephemeral-storage: "10Gi"
                   limits:
                     cpu: "4"
                     memory: "8Gi"
                     ephemeral-storage: "10Gi"
                 env:
                 - name: HF_TOKEN
                   valueFrom:
                     secretKeyRef:
                       name: hf-secret
                       key: hf_token
                 - name: HF_HOME
                   value: /data/.cache/huggingface
                 - name: HF_HUB_DISABLE_XET
                   value: "1"
                 command: ["/bin/bash", "-c"]
                 args:
                 - |
                   set -euo pipefail
         
                   # Clone verl to GCS (for worker pods)
                   if [ ! -d "/data/verl" ]; then
                     echo "Cloning verl to GCS..."
                     git clone --depth 1 --branch v0.6.1 https://github.com/volcengine/verl.git /data/verl
                   else
                     echo "verl already exists in /data/verl"
                   fi
         
                   # Clone verl locally for fast installation
                   echo "Cloning verl locally..."
                   git clone --depth 1 --branch v0.6.1 https://github.com/volcengine/verl.git /tmp/verl
         
                   # Install verl package from local clone
                   echo "Installing verl package..."
                   pip3 install --no-cache-dir --no-deps /tmp/verl
                   rm -rf /tmp/verl
         
                   # Preprocess GSM8K
                   if [ ! -d "/data/gsm8k" ]; then
                     echo "Preprocessing GSM8K..."
                     python /data/verl/examples/data_preprocess/gsm8k.py --local_save_dir /data/gsm8k
                   else
                     echo "GSM8K data already exists in /data/gsm8k"
                   fi
         
                   # Download model
                   if [ ! -d "/data/Qwen2.5-32B-Instruct" ]; then
                     echo "Downloading Qwen2.5-32B-Instruct..."
                     huggingface-cli download Qwen/Qwen2.5-32B-Instruct --local-dir /data/Qwen2.5-32B-Instruct --local-dir-use-symlinks False
                   else
                     echo "Model Qwen2.5-32B-Instruct already exists in /data/Qwen2.5-32B-Instruct"
                   fi
         
                   echo "Data preparation complete!"
                 volumeMounts:
                 - name: training-bucket-vol
                   mountPath: /data
               volumes:
               - name: training-bucket-vol
                 persistentVolumeClaim:
                   claimName: training-bucket-pvc

  2. Launch the Job:
         
         envsubst < data-prep-job.yaml | kubectl apply -f -
         echo "Waiting for data-prep-job Pod to be created and pull image (this takes ~5 minutes)..."
         until [ -n "$(kubectl get pods -l job-name=data-prep-job -n "${NAMESPACE}" --no-headers 2>/dev/null)" ]; do
           sleep 2
         done
         kubectl wait --for=condition=ready pod -l job-name=data-prep-job -n "${NAMESPACE}" --timeout=600s

  3. Monitor the Job:
         
         kubectl logs -n ${NAMESPACE} -l job-name=data-prep-job -f




### A4X

  1. Clone the verl repository, prepare the virtual environment, and process the **GSM8K** dataset:
         
         git clone https://github.com/volcengine/verl.git
         git -C verl checkout ${VERL_REF}
         
         VENV_DIR=.venv
         python3 -m venv $VENV_DIR
         source $VENV_DIR/bin/activate
         pip install verl
         
         python verl/examples/data_preprocess/gsm8k.py --local_save_dir ~/data/gsm8k
         

  2. Download the **Qwen2.5-32B-Instruct** model by using the Hugging Face CLI (this download requires around 66 GB of disk space):
         
         hf download Qwen/Qwen2.5-32B-Instruct --local-dir Qwen2.5-32B-Instruct
         

  3. Upload the model, data, and the verl code to your Cloud Storage bucket:
         
         gcloud storage cp --recursive verl gs://${GS_BUCKET}/verl
         gcloud storage cp --recursive Qwen2.5-32B-Instruct gs://${GS_BUCKET}/Qwen2.5-32B-Instruct
         gcloud storage cp --recursive ~/data/gsm8k/* gs://${GS_BUCKET}/gsm8k/
         




## Deploy RayCluster custom resource

Deploy a RayCluster custom resource, which consists of one system head Pod and multiple GPU-backed worker Pods.

### A4 and A3 Ultra

Select the GKE cluster mode that you used to create your cluster:

### Autopilot

  1. Inspect the RayCluster workload:
         
         apiVersion: ray.io/v1
         kind: RayCluster
         metadata:
           name: b200-ray-cluster-dranet
         spec:
           rayVersion: '2.47.0'
           headGroupSpec:
             rayStartParams:
               dashboard-host: '0.0.0.0'
             template:
               metadata:
                 annotations:
                   gke-gcsfuse/volumes: "true"
               spec:
                 serviceAccountName: ${KSA_NAME}
                 nodeSelector:
                   cloud.google.com/gke-spot: "true"
                   cloud.google.com/machine-family: "c2"
                   cloud.google.com/compute-class: Performance
                 containers:
                 - name: ray-head
                   image: verlai/verl:vllm011.latest 
                   ports:
                     - containerPort: 6379
                       name: gcs-server
                     - containerPort: 8265
                       name: dashboard
                     - containerPort: 10001
                       name: client
                   resources:
                     limits:
                       cpu: "12"
                       memory: "32G"
                       ephemeral-storage: "9Gi"
                     requests:
                       cpu: "12"
                       memory: "32G"
                       ephemeral-storage: "9Gi"
                   volumeMounts:
                     - mountPath: /tmp/ray
                       name: ray-logs
                     - name: training-bucket-vol
                       mountPath: /data
                 volumes:
                   - name: ray-logs
                     emptyDir: {}
                   - name: training-bucket-vol
                     persistentVolumeClaim:
                       claimName: training-bucket-pvc
           workerGroupSpecs:
           - replicas: 2
             minReplicas: 2
             maxReplicas: 2
             groupName: gpu-group
             rayStartParams:
               num-cpus: "220"
             template:
               metadata:
                 annotations:
                   gke-gcsfuse/volumes: "true"
               spec:
                 resourceClaims:
                   - name: rdma-claim
                     resourceClaimTemplateName: all-mrdma
                 initContainers:
                 - name: verl-setup
                   image: verlai/verl:vllm011.latest
                   command: ["/bin/bash", "-c"]
                   args:
                     - |
                       echo "Installing GIB plugins..."
                       curl -s https://packages.cloud.google.com/apt/doc/apt-key.gpg | gpg --dearmor -o /etc/apt/trusted.gpg.d/cloud.google.gpg
                       echo 'deb https://packages.cloud.google.com/apt gpudirect-gib-apt main' | tee /etc/apt/sources.list.d/nccl-gib.list
                       apt-get update && apt-get install -y nccl-gib-plugins
         
                       echo "Local install skipped (handled by data prep)"
                   volumeMounts:
                   - name: training-bucket-vol
                     mountPath: /data
                   - name: gib
                     mountPath: /usr/local/gib
                 serviceAccountName: ${KSA_NAME}
                 nodeSelector:
                   cloud.google.com/compute-class: dranet-a4-computeclass-v3
                 tolerations:
                   - key: "nvidia.com/gpu"
                     operator: "Exists"
                     effect: "NoSchedule"
                 containers:
                 - name: ray-worker
                   image: verlai/verl:vllm011.latest
                   env:
                    - name: LD_LIBRARY_PATH
                      value: /usr/local/nvidia/lib64:/usr/local/gib/lib64
                   resources:
                     limits:
                       cpu: "180"
                       memory: "2000Gi"
                       nvidia.com/gpu: "8"
                       ephemeral-storage: "1000Gi"
                     requests:
                       cpu: "180"
                       memory: "2000Gi"
                       nvidia.com/gpu: "8"
                       ephemeral-storage: "1000Gi"
                     claims:
                     - name: rdma-claim
                   volumeMounts:
                   - name: gib
                     mountPath: /usr/local/gib
                     readOnly: true
                   - name: shared-memory
                     mountPath: /dev/shm
                   - name: ray-tmp-storage
                     mountPath: /tmp
                   - name: training-bucket-vol
                     mountPath: /data
                 volumes:
                 - name: gib
                   emptyDir: {}
                 - name: shared-memory
                   emptyDir:
                     medium: "Memory"
                     sizeLimit: 250Gi 
                 - name: ray-tmp-storage
                   emptyDir: {}
                 - name: training-bucket-vol
                   persistentVolumeClaim:
                     claimName: training-bucket-pvc

  2. Apply the RayCluster:
         
         envsubst < "ray-cluster-auto-dranet.yaml" | kubectl apply -n "${NAMESPACE}" -f -




### Standard

  1. Inspect the RayCluster workload:
         
         apiVersion: ray.io/v1
         kind: RayCluster
         metadata:
           name: b200-ray-cluster
           annotations:
         spec:
           rayVersion: '2.47.0'
           headGroupSpec:
             rayStartParams:
               dashboard-host: '0.0.0.0'
             template:
               metadata:
                 annotations:
                   gke-gcsfuse/volumes: "true"
               spec:
                 serviceAccountName: ${KSA_NAME}
                 nodeSelector:
                   cloud.google.com/gke-nodepool: "default-pool"
                 containers:
                 - name: ray-head
                   image: verlai/verl:vllm011.latest 
                   ports:
                     - containerPort: 6379
                       name: gcs-server
                     - containerPort: 8265
                       name: dashboard
                     - containerPort: 10001
                       name: client
                   resources:
                     limits:
                       cpu: "12"
                       memory: "32G"
                       ephemeral-storage: "9Gi"
                     requests:
                       cpu: "12"
                       memory: "32G"
                       ephemeral-storage: "9Gi"
                   volumeMounts:
                     - mountPath: /tmp/ray
                       name: ray-logs
                     - name: training-bucket-vol
                       mountPath: /data
                 volumes:
                   - name: ray-logs
                     emptyDir: {}
                   - name: training-bucket-vol
                     persistentVolumeClaim:
                       claimName: training-bucket-pvc
           workerGroupSpecs:
           - replicas: 2
             minReplicas: 2
             maxReplicas: 2
             groupName: gpu-group
             rayStartParams:
               num-cpus: "220"
             template:
               metadata:
                 annotations:
                   gke-gcsfuse/volumes: "true"
                   networking.gke.io/default-interface: 'eth0'
                   networking.gke.io/interfaces: |
                     [
                       {"interfaceName":"eth0","network":"default"},
                       {"interfaceName":"eth1","network":"gvnic-1"},
                       {"interfaceName":"eth2","network":"rdma-0"},
                       {"interfaceName":"eth3","network":"rdma-1"},
                       {"interfaceName":"eth4","network":"rdma-2"},
                       {"interfaceName":"eth5","network":"rdma-3"},
                       {"interfaceName":"eth6","network":"rdma-4"},
                       {"interfaceName":"eth7","network":"rdma-5"},
                       {"interfaceName":"eth8","network":"rdma-6"},
                       {"interfaceName":"eth9","network":"rdma-7"}
                     ]
               spec:
                 serviceAccountName: ${KSA_NAME}
                 nodeSelector:
                   cloud.google.com/gke-accelerator: ${GPU_TYPE}
                 tolerations:
                   - key: "nvidia.com/gpu"
                     operator: "Exists"
                     effect: "NoSchedule"
                 containers:
                 - name: ray-worker
                   image: verlai/verl:vllm011.latest
                   env:
                    - name: LD_LIBRARY_PATH
                      value: /usr/local/nvidia/lib64
                   resources:
                     limits:
                       cpu: "220"
                       memory: "2800Gi"
                       nvidia.com/gpu: "8"
                       ephemeral-storage: "1000Gi"
                     requests:
                       cpu: "220"
                       memory: "2800Gi"
                       nvidia.com/gpu: "8"
                       ephemeral-storage: "1000Gi"
                   volumeMounts:
                   - name: nvidia
                     mountPath: /usr/local/nvidia
                   - name: gib
                     mountPath: /usr/local/gib
                   - name: shared-memory
                     mountPath: /dev/shm
                   - name: ray-tmp-storage
                     mountPath: /tmp
                   - name: training-bucket-vol
                     mountPath: /data
                 volumes:
                 - name: gib
                   hostPath:
                     path: /home/kubernetes/bin/gib
                 - name: nvidia
                   hostPath:
                     path: /home/kubernetes/bin/nvidia
                 - name: lib64
                   hostPath:
                     path: /lib64
                 - name: shared-memory
                   emptyDir:
                     medium: "Memory"
                     sizeLimit: 250Gi 
                 - name: sys
                   hostPath:
                     path: /sys
                 - name: proc-sys
                   hostPath:
                     path: /proc/sys
                 - name: ray-tmp-storage
                   emptyDir: {}
                 - name: training-bucket-vol
                   persistentVolumeClaim:
                     claimName: training-bucket-pvc

  2. Apply the RayCluster:
         
         envsubst < "ray-cluster-standard.yaml" | kubectl apply -f -
         echo "Waiting for Ray head and GPU worker Pods to pull images and become Ready (this takes ~2–5 minutes)..."
         until [ -n "$(kubectl get pods -l ray.io/cluster=b200-ray-cluster -n "${NAMESPACE}" --no-headers 2>/dev/null)" ]; do
           sleep 2
         done
         kubectl wait --for=condition=ready pod -l ray.io/cluster=b200-ray-cluster -n "${NAMESPACE}" --timeout=1200s




### A4X

  1. Create the RDMA `ResourceClaimTemplate` and the NVIDIA `ComputeDomain`. Each GPU worker Pod claims four RDMA NICs (all rails of its node) and one IMEX channel. Save the following manifest to `compute-domain-a4x.yaml`:
         
         apiVersion: resource.k8s.io/v1
         kind: ResourceClaimTemplate
         metadata:
           name: verl-rdma-nic
           namespace: ${NAMESPACE}
         spec:
           spec:
             devices:
               requests:
               - name: nic
                 exactly:
                   deviceClassName: mrdma.google.com
                   allocationMode: ExactCount
                   count: 1
         ---
         apiVersion: resource.nvidia.com/v1beta1
         kind: ComputeDomain
         metadata:
           name: verl-compute-domain
           namespace: ${NAMESPACE}
         spec:
           numNodes: ${NUM_GPU_NODES}
           channel:
             resourceClaimTemplate:
               name: verl-compute-domain-channel
         

  2. Apply the manifest:
         
         kubectl apply -f compute-domain-a4x.yaml
         

  3. Deploy the RayCluster. The Ray head Pod runs on an A4X node without requesting GPUs (since the image is `arm64`-only). Save the following configurations to `ray-cluster-a4x.yaml`:
         
         apiVersion: ray.io/v1
         kind: RayCluster
         metadata:
           name: gb200-ray-cluster
           namespace: ${NAMESPACE}
         spec:
           rayVersion: '2.49.0'
           headGroupSpec:
             rayStartParams:
               dashboard-host: '0.0.0.0'
               num-cpus: "0"
             template:
               metadata:
                 annotations:
                   gke-gcsfuse/volumes: "true"
               spec:
                 serviceAccountName: ${KSA_NAME}
                 nodeSelector:
                   cloud.google.com/gke-accelerator: nvidia-gb200
                 tolerations:
                 - key: nvidia.com/gpu
                   operator: Exists
                   effect: NoSchedule
                 - key: kubernetes.io/arch
                   operator: Exists
                   effect: NoSchedule
                 containers:
                 - name: ray-head
                   image: ${VERL_IMAGE}
                   lifecycle:
                     postStart:
                       exec:
                         command:
                         - /bin/bash
                         - -c
                         - pip3 install --quiet TransferQueue==0.1.8
                   ports:
                   - containerPort: 6379
                     name: gcs-server
                   - containerPort: 8265
                     name: dashboard
                   - containerPort: 10001
                     name: client
                   resources:
                     limits:
                       cpu: "12"
                       memory: 32Gi
                       ephemeral-storage: 20Gi
                     requests:
                       cpu: "12"
                       memory: 32Gi
                       ephemeral-storage: 20Gi
                   volumeMounts:
                   - mountPath: /tmp/ray
                     name: ray-logs
                   - name: training-bucket-vol
                     mountPath: /data
                 volumes:
                 - name: ray-logs
                   emptyDir: {}
                 - name: training-bucket-vol
                   persistentVolumeClaim:
                     claimName: training-bucket-pvc
           workerGroupSpecs:
           - replicas: ${NUM_GPU_NODES}
             minReplicas: ${NUM_GPU_NODES}
             maxReplicas: ${NUM_GPU_NODES}
             groupName: gpu-group
             rayStartParams:
               num-cpus: "120"
             template:
               metadata:
                 annotations:
                   gke-gcsfuse/volumes: "true"
               spec:
                 serviceAccountName: ${KSA_NAME}
                 nodeSelector:
                   cloud.google.com/gke-accelerator: nvidia-gb200
                 affinity:
                   podAntiAffinity:
                     requiredDuringSchedulingIgnoredDuringExecution:
                     - labelSelector:
                         matchLabels:
                           ray.io/group: gpu-group
                       topologyKey: kubernetes.io/hostname
                 tolerations:
                 - key: nvidia.com/gpu
                   operator: Exists
                   effect: NoSchedule
                 - key: kubernetes.io/arch
                   operator: Exists
                   effect: NoSchedule
                 containers:
                 - name: ray-worker
                   image: ${VERL_IMAGE}
                   lifecycle:
                     postStart:
                       exec:
                         command:
                         - /bin/bash
                         - -c
                         - pip3 install --quiet TransferQueue==0.1.8
                   env:
                   - name: LD_LIBRARY_PATH
                     value: /usr/local/nvidia/lib64
                   resources:
                     limits:
                       cpu: "120"
                       memory: 600Gi
                       nvidia.com/gpu: "4"
                       ephemeral-storage: 500Gi
                     requests:
                       cpu: "120"
                       memory: 600Gi
                       nvidia.com/gpu: "4"
                       ephemeral-storage: 500Gi
                     claims:
                     - name: rdma-nic-0
                     - name: rdma-nic-1
                     - name: rdma-nic-2
                     - name: rdma-nic-3
                     - name: compute-domain-channel
                   volumeMounts:
                   - name: nvidia
                     mountPath: /usr/local/nvidia
                   - name: gib
                     mountPath: /usr/local/gib
                   - name: shared-memory
                     mountPath: /dev/shm
                   - name: ray-tmp-storage
                     mountPath: /tmp
                   - name: training-bucket-vol
                     mountPath: /data
                 resourceClaims:
                 - name: rdma-nic-0
                   resourceClaimTemplateName: verl-rdma-nic
                 - name: rdma-nic-1
                   resourceClaimTemplateName: verl-rdma-nic
                 - name: rdma-nic-2
                   resourceClaimTemplateName: verl-rdma-nic
                 - name: rdma-nic-3
                   resourceClaimTemplateName: verl-rdma-nic
                 - name: compute-domain-channel
                   resourceClaimTemplateName: verl-compute-domain-channel
                 volumes:
                 - name: gib
                   hostPath:
                     path: /home/kubernetes/bin/gib
                 - name: nvidia
                   hostPath:
                     path: /home/kubernetes/bin/nvidia
                 - name: shared-memory
                   emptyDir:
                     medium: Memory
                     sizeLimit: 200Gi
                 - name: ray-tmp-storage
                   emptyDir: {}
                 - name: training-bucket-vol
                   persistentVolumeClaim:
                     claimName: training-bucket-pvc
         

  4. Apply the RayCluster manifest:
         
         envsubst < ray-cluster-a4x.yaml | kubectl apply -f -
         

  5. Wait until one head Pod and four worker Pods are in the `Running` state:
         
         kubectl get pods -w
         




## Launch the GRPO Job

Configure and submit the reinforcement learning training job:

### A4 and A3 Ultra

Select the GKE cluster mode that you used to create your cluster:

### Autopilot

  1. Set up the Ray Client:
         
         if [ ! -d "env" ]; then
           python3 -m venv env
         else
           echo "Found virtual environment env, not recreating"
         fi
         
         source env/bin/activate
         pip3 install --upgrade pip
         pip3 install ray[default]

  2. Recover the Ray Head Service:
         
         SVC_NAME="$(kubectl get svc -l "ray.io/node-type=head" -o jsonpath='{..metadata.name}')"
         echo "Ray head service name: ${SVC_NAME}"

  3. Set up port forwarding to the Ray dashboard node. The process runs in the background, so you can continue running commands in the same terminal session.
         
         echo "Starting auto-restarting port-forwarding to ${SVC_NAME} on port 8265..."
         run_port_forward() {
             while true; do
                 kubectl port-forward --address 0.0.0.0 svc/"${SVC_NAME}" 8265:8265 -n "${NAMESPACE}" >/dev/null 2>&1 || true
                 sleep 1
             done
         }
         run_port_forward &
         PF_LOOP_PID=$!
         export RAY_ADDRESS="http://localhost:8265"

To stop the port-forwarding loop, use the `kill ${PF_LOOP_PID}` command.

  4. Inspect the `runtime-env.yaml` manifest:
         
         py_modules: ["."]
         working_dir: "."
         excludes:
           - ".git"
           - "env"
           - "venv"
           - ".venv"
           - "__pycache__"
           - "*.pyc"
           - ".cache"
           - "*.log"
           - "*.tmp"
           - "build"
           - "dist"
         env_vars:
           PYTHONPATH: "/data/verl"
           LD_LIBRARY_PATH: "/usr/local/nvidia/lib64:/usr/local/gib/lib64"
           NCCL_DEBUG: "INFO"
           NCCL_ENV_PLUGIN: "gcp"
           NCCL_CONF_FILE: "/usr/local/gib/configs/nccl.a4.conf"
           NCCL_IB_GID_INDEX: "3"
           NCCL_NVLS_ENABLE: "0"
           NCCL_TUNER_CONFIG_PATH: "/usr/local/gib/configs"
           NUM_WORKERS: "2"
           CPUS_PER_WORKER: "192"
           GPUS_PER_WORKER: "8"
           HF_HOME: "/data/huggingface_cache"
           GLOO_SOCKET_IFNAME: "eth0"

If you're using **H200** GPUs, change the value of the `NCCL_CONF_FILE` environment variable to `/usr/local/gib/configs/nccl.a3u.conf`.

This file is used by the Ray client. You don't need to apply this manifest to the cluster.

  5. Submit the job using the `ray job submit` command:
         
         SUBMIT_OUT=$(ray job submit \
           --address "http://localhost:8265" \
           --no-wait \
           --runtime-env runtime-env.yaml \
           -- \
           bash -c "
               cd /data/verl && PYTHONUNBUFFERED=1 python3 -m verl.trainer.main_ppo \
               data.train_files=/data/gsm8k/train.parquet \
               data.val_files=/data/gsm8k/test.parquet \
               data.train_batch_size=256 \
               data.max_prompt_length=512 \
               data.max_response_length=512 \
               actor_rollout_ref.model.path=/data/Qwen2.5-32B-Instruct \
               actor_rollout_ref.actor.optim.lr=1e-5 \
               actor_rollout_ref.actor.ppo_mini_batch_size=256 \
               actor_rollout_ref.actor.ppo_micro_batch_size_per_gpu=16 \
               actor_rollout_ref.rollout.name=vllm \
               actor_rollout_ref.rollout.log_prob_micro_batch_size_per_gpu=8 \
               actor_rollout_ref.rollout.tensor_model_parallel_size=8 \
               actor_rollout_ref.rollout.gpu_memory_utilization=0.6 \
               actor_rollout_ref.ref.log_prob_micro_batch_size_per_gpu=4 \
               actor_rollout_ref.actor.strategy=fsdp2 \
               algorithm.kl_ctrl.kl_coef=0.001 \
               trainer.logger=console \
               trainer.val_before_train=False \
               trainer.n_gpus_per_node=8 \
               trainer.nnodes=2 \
               trainer.save_freq=10 \
               trainer.test_freq=10 \
               trainer.total_training_steps=10 \
               trainer.default_local_dir=/data/verl/checkpoints \
               algorithm.adv_estimator=grpo \
               actor_rollout_ref.rollout.n=8 \
               actor_rollout_ref.actor.use_torch_compile=False \
               actor_rollout_ref.actor.fsdp_config.use_torch_compile=False \
               actor_rollout_ref.ref.use_torch_compile=False \
               actor_rollout_ref.ref.fsdp_config.use_torch_compile=False \
               trainer.total_epochs=1")
         echo "${SUBMIT_OUT}"
         JOB_ID=$(echo "${SUBMIT_OUT}" | grep "submitted successfully" | awk -F"'" '{print $2}' || true)

  6. Monitor the training job logs and look for the `critic/score/mean` metric to increase, which indicates that the model is learning:

     * **Ray Dashboard** : 
       1. Open `http://localhost:8265` in your browser. If you are using Cloud Shell, click **Web Preview** , select **Change port** , and enter `8265`.
       2. Go to the **Jobs** tab.
       3. Click your **Job ID**.
       4. Filter the logs by the keyword `critic` to inspect `critic/score/mean`.
     * **Terminal** : Because the job is submitted asynchronously with the `--no-wait` flag, stream job logs in your terminal by running the following command:
           
           ray job logs "${JOB_ID}" --address "http://localhost:8265" --follow

  7. After the training finishes, verify that the model checkpoints were saved to your Cloud Storage bucket by listing the directory contents:
         
         gcloud storage ls "gs://${GS_BUCKET}/verl/checkpoints/"

Alternatively, view the checkpoints in the Google Cloud console by going to **Cloud Storage** > **Buckets** , selecting `YOUR_GCS_BUCKET`, and opening the `verl/checkpoints` folder.




### Standard

  1. Set up the Ray Client:
         
         if [ ! -d "env" ]; then
           echo "Creating local virtual environment for Ray client..."
           python3 -m venv env
         else
           echo "Found virtual environment env, not recreating"
         fi
         source env/bin/activate
         pip3 install --upgrade pip
         pip3 install ray[default]

  2. Recover the Ray Head Service:
         
         SVC_NAME="$(kubectl get svc -l "ray.io/node-type=head" -o jsonpath='{..metadata.name}')"
         echo "Ray head service name: ${SVC_NAME}"

  3. Set up port forwarding to the Ray dashboard node. The process runs in the background, so you can continue running commands in the same terminal session.
         
         echo "Starting port-forwarding loop to ${SVC_NAME} on port 8265..."
         run_port_forward() {
             while true; do
                 kubectl port-forward --address 0.0.0.0 svc/"${SVC_NAME}" 8265:8265 -n "${NAMESPACE}" >/dev/null 2>&1 || true
                 sleep 1
             done
         }
         run_port_forward &
         PF_PID=$!
         export RAY_ADDRESS="http://localhost:8265"
         sleep 3

To stop the port-forwarding loop, use the `kill ${PF_PID}` command.

  4. Inspect the `runtime-env.yaml` manifest:
         
         working_dir: "."
         excludes:
           - ".git"
           - "env"
           - ".cache"
           - ".zip"
           - ".log"
         env_vars:
           PYTHONPATH: "/data/verl"
           LD_LIBRARY_PATH: "/usr/local/nvidia/lib64"
           NCCL_DEBUG: "WARN"
           NCCL_NVLS_ENABLE: "0"
           NUM_WORKERS: "2"
           CPUS_PER_WORKER: "192"
           GPUS_PER_WORKER: "8"
           NCCL_NET_PLUGIN: "/usr/local/gib/lib64/libnccl-net_internal.so"
           NCCL_CROSS_NIC: "0"
           NCCL_NET_GDR_LEVEL: "PIX"
           NCCL_P2P_NET_CHUNKSIZE: "131072"
           NCCL_NVLS_CHUNKSIZE: "524288"
           NCCL_IB_ADAPTIVE_ROUTING: "1"
           NCCL_IB_QPS_PER_CONNECTION: "4"
           NCCL_IB_TC: "52"
           NCCL_IB_FIFO_TC: "84"
           NCCL_TUNER_CONFIG_PATH: "/usr/local/gib/configs/tuner_config_a4.txtpb"
           HF_HOME: "/data/huggingface_cache"
           GLOO_SOCKET_IFNAME: "eth0"

If you're using **H200** GPUs, change the value of the `NCCL_TUNER_CONFIG_PATH` environment variable to `/usr/local/gib/configs/tuner_config_a3u.txtpb`.

This file is used by the Ray client. You don't need to apply this manifest to the cluster.

  5. Submit the job:
         
         SUBMIT_OUT=$(ray job submit \
           --address "http://localhost:8265" \
           --no-wait \
           --runtime-env runtime-env.yaml \
           -- \
           bash -c "
             cd /data/verl && PYTHONUNBUFFERED=1 python3 -m verl.trainer.main_ppo \
             data.train_files=/data/gsm8k/train.parquet \
             data.val_files=/data/gsm8k/test.parquet \
             data.train_batch_size=256 \
             data.max_prompt_length=512 \
             data.max_response_length=512 \
             actor_rollout_ref.model.path=/data/Qwen2.5-32B-Instruct \
             actor_rollout_ref.actor.optim.lr=1e-5 \
             actor_rollout_ref.actor.ppo_mini_batch_size=256 \
             actor_rollout_ref.actor.ppo_micro_batch_size_per_gpu=8 \
             actor_rollout_ref.rollout.name=vllm \
             actor_rollout_ref.rollout.log_prob_micro_batch_size_per_gpu=2 \
             actor_rollout_ref.rollout.tensor_model_parallel_size=8 \
             actor_rollout_ref.rollout.gpu_memory_utilization=0.5 \
             actor_rollout_ref.ref.log_prob_micro_batch_size_per_gpu=2 \
             actor_rollout_ref.actor.strategy=fsdp2 \
             algorithm.kl_ctrl.kl_coef=0.001 \
             trainer.logger=console \
             trainer.val_before_train=False \
             trainer.n_gpus_per_node=8 \
             trainer.nnodes=2 \
             trainer.save_freq=10 \
             trainer.test_freq=10 \
             trainer.total_training_steps=10 \
             trainer.default_local_dir=/data/verl/checkpoints \
             algorithm.adv_estimator=grpo \
             actor_rollout_ref.rollout.n=8 \
             trainer.total_epochs=1")
         echo "${SUBMIT_OUT}"
         JOB_ID=$(echo "${SUBMIT_OUT}" | grep "submitted successfully" | awk -F"'" '{print $2}' || true)

  6. Monitor the training job logs and look for the `critic/score/mean` metric to increase, which indicates that the model is learning:

     * **Ray Dashboard** : 
       1. Open `http://localhost:8265` in your browser. If you are using Cloud Shell, click **Web Preview** , select **Change port** , and enter `8265`.
       2. Go to the **Jobs** tab.
       3. Click your **Job ID**.
       4. Filter the logs by the `critic` keyword to inspect the `critic/score/mean` metric.
     * **Console output** : Because the job is submitted asynchronously with the `--no-wait` flag, stream the job logs in your terminal by running the following command:
           
           ray job logs "${JOB_ID}" --address "http://localhost:8265" --follow

  7. After the training finishes, verify that the model checkpoints were saved to your Cloud Storage bucket by listing the directory contents:
         
         gcloud storage ls "gs://${GS_BUCKET}/verl/checkpoints/"

Alternatively, view the checkpoints in the Google Cloud console by going to **Cloud Storage** > **Buckets** , selecting `YOUR_GCS_BUCKET`, and opening the `verl/checkpoints` folder.




### A4X

  1. Get the Ray head Pod name:
         
         export HEAD_POD=$(kubectl get pod -n ${NAMESPACE} -l ray.io/node-type=head -o jsonpath='{.items[0].metadata.name}')
         

  2. Configure the Ray runtime environment file directly on the head Pod:
         
         kubectl exec ${HEAD_POD} -c ray-head -- bash -c 'mkdir -p /tmp/submit && cat > /tmp/submit/runtime-env.yaml <<EOF
         working_dir: "."
         env_vars:
           PYTHONPATH: "/data/verl"
           LD_LIBRARY_PATH: "/usr/local/nvidia/lib64:/usr/local/gib/lib64"
           NCCL_DEBUG: "INFO"
           NCCL_ENV_PLUGIN: "gcp"
           HF_HOME: "/data/huggingface_cache"
           GLOO_SOCKET_IFNAME: "eth0"
         EOF'
         

  3. Submit the GRPO training job by running it on the Ray head Pod:
         
         kubectl exec ${HEAD_POD} -c ray-head -- bash -c 'cd /tmp/submit && \
         ray job submit --runtime-env runtime-env.yaml --no-wait -- \
           python3 -m verl.trainer.main_ppo \
             algorithm.adv_estimator=grpo \
             data.train_files=/data/gsm8k/train.parquet \
             data.val_files=/data/gsm8k/test.parquet \
             data.train_batch_size=256 \
             data.max_prompt_length=512 \
             data.max_response_length=512 \
             actor_rollout_ref.model.path=/data/Qwen2.5-32B-Instruct \
             actor_rollout_ref.actor.optim.lr=1e-5 \
             actor_rollout_ref.actor.ppo_mini_batch_size=64 \
             actor_rollout_ref.actor.ppo_micro_batch_size_per_gpu=8 \
             actor_rollout_ref.actor.use_kl_loss=True \
             actor_rollout_ref.actor.strategy=fsdp2 \
             actor_rollout_ref.rollout.name=vllm \
             actor_rollout_ref.rollout.tensor_model_parallel_size=4 \
             actor_rollout_ref.rollout.gpu_memory_utilization=0.6 \
             actor_rollout_ref.rollout.n=8 \
             actor_rollout_ref.rollout.log_prob_micro_batch_size_per_gpu=16 \
             actor_rollout_ref.ref.log_prob_micro_batch_size_per_gpu=16 \
             algorithm.kl_ctrl.kl_coef=0.001 \
             trainer.logger=console \
             trainer.n_gpus_per_node=4 \
             trainer.nnodes=4 \
             trainer.save_freq=10 \
             trainer.test_freq=10 \
             trainer.total_epochs=2 \
             trainer.default_local_dir=/data/verl/checkpoints'
         

  4. Monitor the job logs (using the unique ID returned by `ray job submit`):
         
         kubectl exec ${HEAD_POD} -c ray-head -- ray job logs <var>JOB_ID</var> --follow
         

Replace `JOB_ID`. Confirm that cross-node NVLink is active by looking for NCCL lines in logs containing `via P2P/MNNVL`.




## Clean up

To avoid incurring charges, delete the resources:

### A4 and A3 Ultra

### Autopilot

  1. If the port-forwarding loop is still running in your background session, terminate it:
         
         kill ${PF_LOOP_PID}

  2. Delete the Ray cluster:
         
         envsubst < "ray-cluster-auto-dranet.yaml" | kubectl delete -f - --ignore-not-found=true || true

  3. Delete the Cloud Storage FUSE:
         
         kubectl delete job data-prep-job -n "${NAMESPACE:-default}" --ignore-not-found=true || true
         envsubst < "gcsfuse-storage.yaml" | kubectl delete --timeout=30s -f - --ignore-not-found=true || true

  4. Delete the DRANET resources:
         
         kubectl delete -f "resourceclaim-dranet.yaml" --ignore-not-found=true 2>/dev/null || true
         kubectl delete -f "computeclass-dranet.yaml" --ignore-not-found=true 2>/dev/null || true

  5. Delete the Cloud Storage bucket:
         
         gcloud storage rm -r "gs://${GS_BUCKET}" --project="${PROJECT_ID:-$(gcloud config get project)}" --quiet || {
           echo "First deletion attempt failed. Retrying in 5 seconds..."
           sleep 5
           gcloud storage rm -r "gs://${GS_BUCKET}" --project="${PROJECT_ID:-$(gcloud config get project)}" --quiet
         } || true

  6. Delete the GKE cluster:
         
         gcloud container clusters delete "${CLUSTER_NAME}" --location="${CONTROL_PLANE_REGION}" --quiet || true




### Standard

  1. If the port-forwarding loop is still running in your background session, terminate it:
         
         kill ${PF_PID}

  2. Delete the Ray cluster:
         
         envsubst < "ray-cluster-standard.yaml" | kubectl delete --timeout=30s -f - --ignore-not-found=true || true

  3. Delete the Cloud Storage FUSE:
         
         kubectl delete job data-prep-job -n ${NAMESPACE} --ignore-not-found=true || true
         envsubst < "gcsfuse-storage.yaml" | kubectl delete --timeout=30s -f - --ignore-not-found=true || true

  4. Delete the Cloud Storage bucket:
         
         gcloud storage rm -r "gs://${GS_BUCKET}" --project="${PROJECT_ID}" || {
           echo "First deletion attempt failed. Retrying in 5 seconds..."
           sleep 5
           gcloud storage rm -r "gs://${GS_BUCKET}" --project="${PROJECT_ID}"
         } || true

  5. Delete the GKE cluster:
         
         gcloud container clusters delete ${CLUSTER_NAME} --location=${CONTROL_PLANE_REGION} --project=${PROJECT_ID} --quiet || true

  6. Delete the VPC networks and subnets:
         
         # Function to safely delete all firewall rules for a given network
         delete_network_firewalls() {
           local NET_NAME=$1
           echo "Deleting all firewall rules associated with network ${NET_NAME}..."
           for rule in $(gcloud compute firewall-rules list --filter="network:${NET_NAME}" --format="value(name)" --project=${PROJECT_ID} 2>/dev/null); do
             echo "Deleting firewall rule ${rule}..."
             gcloud compute firewall-rules delete ${rule} --project=${PROJECT_ID} --quiet || true
           done
         }
         
         # Delete Firewalls for both networks
         delete_network_firewalls "${RDMA_NETWORK_PREFIX}-net"
         delete_network_firewalls "${GVNIC_NETWORK_PREFIX}-net"
         
         # Delete RDMA subnets
         echo "Deleting RDMA subnets..."
         for N in $(seq 0 7); do
           if gcloud compute networks subnets describe ${RDMA_NETWORK_PREFIX}-sub-$N --region=${CONTROL_PLANE_REGION} --project=${PROJECT_ID} >/dev/null 2>&1; then
             echo "Deleting subnet ${RDMA_NETWORK_PREFIX}-sub-$N..."
             gcloud compute networks subnets delete ${RDMA_NETWORK_PREFIX}-sub-$N --region=${CONTROL_PLANE_REGION} --project=${PROJECT_ID} --quiet || true
           fi
         done
         
         # Delete GVNIC subnet
         if gcloud compute networks subnets describe ${GVNIC_NETWORK_PREFIX}-sub --region=${CONTROL_PLANE_REGION} --project=${PROJECT_ID} >/dev/null 2>&1; then
           echo "Deleting GVNIC subnet ${GVNIC_NETWORK_PREFIX}-sub..."
           gcloud compute networks subnets delete ${GVNIC_NETWORK_PREFIX}-sub --region=${CONTROL_PLANE_REGION} --project=${PROJECT_ID} --quiet || true
         fi
         
         # Function to delete VPC Network with retry and firewall re-purge
         delete_vpc_network_with_retry() {
           local NET_NAME=$1
           if gcloud compute networks describe ${NET_NAME} --project=${PROJECT_ID} >/dev/null 2>&1; then
             echo "Deleting network ${NET_NAME}..."
             for attempt in {1..6}; do
               delete_network_firewalls "${NET_NAME}"
               if gcloud compute networks delete ${NET_NAME} --project=${PROJECT_ID} --quiet; then
                 echo "Successfully deleted network ${NET_NAME}"
                 break
               fi
               echo "Failed to delete network ${NET_NAME} on attempt ${attempt}. Retrying in 10s..."
               sleep 10
             done
           fi
         }
         
         # Delete Networks safely with retry
         delete_vpc_network_with_retry "${RDMA_NETWORK_PREFIX}-net"
         delete_vpc_network_with_retry "${GVNIC_NETWORK_PREFIX}-net"




### A4X
    
    
    kubectl delete raycluster gb200-ray-cluster
    kubectl delete computedomain verl-compute-domain
    gcloud storage rm -r gs://${GS_BUCKET}
    gcloud container clusters delete ${CLUSTER_NAME} --location=${CONTROL_PLANE_REGION}
    

## What's next

  * [Learn about Ray on GKE](https://docs.cloud.google.com/kubernetes-engine/docs/add-on/ray-on-gke/concepts/overview)
  * [Learn about A4X cluster creation on GKE](https://docs.cloud.google.com/ai-hypercomputer/docs/create/gke-ai-hypercompute-custom-a4x)
  * [Explore verl documentation](https://verl.readthedocs.io/)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-15 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-15 UTC."],[],[]] 
