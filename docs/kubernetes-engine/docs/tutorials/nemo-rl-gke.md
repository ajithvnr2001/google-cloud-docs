---
url: https://docs.cloud.google.com/kubernetes-engine/docs/tutorials/nemo-rl-gke/
title: Fine-tune and scale reinforcement learning with NVIDIA NeMo RL on GKE \u00a0|\u00a0 GKE AI/ML \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T15:09:24.969055+00:00
---

# Fine-tune and scale reinforcement learning with NVIDIA NeMo RL on GKE  |  GKE AI/ML  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/docs/tutorials/nemo-rl-gke/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ Google Kubernetes Engine (GKE) ](https://docs.cloud.google.com/kubernetes-engine/docs)
  * [ GKE AI/ML ](https://docs.cloud.google.com/kubernetes-engine/docs/integrations/ai-infra)
  * [ Guides ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/machine-learning)



Send feedback 

#  Fine-tune and scale reinforcement learning with NVIDIA NeMo RL on GKE Stay organized with collections  Save and categorize content based on your preferences. 

[ Standard ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/choose-cluster-mode)

This tutorial shows you how to orchestrate a distributed training environment for reinforcement learning (RL) on Google Kubernetes Engine (GKE). You use Ray and the _NVIDIA NeMo RL_ framework to set up a distributed training environment to fine-tune a model.

This tutorial focuses on the Group Relative Policy Optimization (GRPO) training pipeline on GKE with Ray and NeMo RL. GRPO is a reinforcement learning algorithm designed to improve a model's reasoning ability. This memory-efficient algorithm simplifies the RL process by eliminating the Critic, or _value model_ , and using a relative group-based calculation instead.

Before you run this tutorial, complete the [Fine-tune and scale reinforcement learning with verl on GKE](https://docs.cloud.google.com/kubernetes-engine/docs/tutorials/scaling-rl-verl-gke) tutorial. This tutorial uses the same cluster setup and configuration as the fine-tuning and scaling RL with verl tutorial.

## Background

The following sections provide a brief overview of the concepts used in this tutorial.

### Reinforcement learning (RL)

RL teaches models through experience, exploration, and feedback rather than static imitation. Although pre-training teaches a model what to say, reinforcement learning from human feedback (RLHF) teaches it how to be helpful, safe, and logical. RL serves as the bridge between a base model and a fine-tuned model for a specialized use case.

For more information, see [What is reinforcement learning?](https://cloud.google.com/discover/what-is-reinforcement-learning)

### Group Relative Policy Optimization (GRPO)

_GRPO_ , an algorithm popularized by DeepSeek, offers a memory-efficient alternative to Proximal Policy Optimization (PPO) for LLM alignment by removing the Critic model. Instead of a Critic network, GRPO generates a group of responses for the same prompt and uses the average reward of that group as the baseline.

For more information, see [GRPO](https://verl.readthedocs.io/en/latest/algo/grpo.html).

### NVIDIA NeMo RL

_NeMo RL_ is NVIDIA's open-source post-training library designed for scalable RL. Part of the broader NeMo framework ecosystem, NeMo RL enables both small-scale experiments on a single GPU and multi-node deployments across thousands of GPUs.

For more information, see [NVIDIA NeMo RL](https://github.com/NVIDIA/NeMo-RL).

### GSM8k dataset

In this tutorial, you use the GSM8k dataset, which contains 8,500 high-quality, linguistically diverse grade-school math word problems.

By using GSM8k and GRPO, the model generates a group of _n_ different responses for the same problem. GRPO compares these responses against the group average. The model is rewarded more for paths that are consistently correct and logically sound compared to the rest of the group. Over time, the model learns that articulating its steps clearly is the most reliable way to maximize reward, effectively reducing the reward for low-performance answers.

For more information, see [GSM8k](https://huggingface.co/datasets/openai/gsm8k).

## Objectives

This tutorial shows you how to set up RL on GKE with NeMo RL by completing the following steps:

  1. Prepare your environment.
  2. Set up a GKE cluster with B200 or H200 GPUs.
  3. Configure KubeRay to manage a distributed Ray cluster.
  4. Use Managed Lustre for high-performance storage.
  5. Run a GRPO training job that uses NeMo RL.

**Note:** This tutorial uses the same cluster setup and configuration as the [Fine-tune and scale reinforcement learning with verl on GKE](https://docs.cloud.google.com/kubernetes-engine/docs/tutorials/scaling-rl-verl-gke) tutorial. If you have already completed that tutorial, you can skip to the Prepare your environment and Set up infrastructure sections. In your already set up infrastructure, you can proceed to the Deploy RayCluster section to deploy a Ray cluster.

## Before you begin

  1. Sign in to your Google Cloud account. If you're new to Google Cloud, [ create an account](https://console.cloud.google.com/freetrial) to evaluate how our products perform in real-world scenarios. New customers also get $300 in free credits to run, test, and deploy workloads. 
  2. [Install](https://docs.cloud.google.com/sdk/docs/install) the Google Cloud CLI. 

**Note:** If you installed the gcloud CLI previously, make sure you have the latest version by running `gcloud components update`. 
  3. If you're using an external identity provider (IdP), you must first [ sign in to the gcloud CLI with your federated identity](https://docs.cloud.google.com/iam/docs/workforce-log-in-gcloud). 

  4. To [initialize](https://docs.cloud.google.com/sdk/docs/initializing) the gcloud CLI, run the following command: 
         
         gcloud init

  5. [Create or select a Google Cloud project](https://cloud.google.com/resource-manager/docs/creating-managing-projects).

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

  6. [Verify that billing is enabled for your Google Cloud project](https://docs.cloud.google.com/billing/docs/how-to/verify-billing-enabled#confirm_billing_is_enabled_on_a_project). 

  7. Enable the required APIs, if any are not already enabled: 

**Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you created the project, then you likely already have this permission through the Owner role (`roles/owner`). Otherwise, you can get this permission through the Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
         
         gcloud services enable container.googleapis.com storage.googleapis.com compute.googleapis.com servicenetworking.googleapis.com lustre.googleapis.com

  8. [Install](https://docs.cloud.google.com/sdk/docs/install) the Google Cloud CLI. 

**Note:** If you installed the gcloud CLI previously, make sure you have the latest version by running `gcloud components update`. 
  9. If you're using an external identity provider (IdP), you must first [ sign in to the gcloud CLI with your federated identity](https://docs.cloud.google.com/iam/docs/workforce-log-in-gcloud). 

  10. To [initialize](https://docs.cloud.google.com/sdk/docs/initializing) the gcloud CLI, run the following command: 
         
         gcloud init

  11. [Create or select a Google Cloud project](https://cloud.google.com/resource-manager/docs/creating-managing-projects).

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

  12. [Verify that billing is enabled for your Google Cloud project](https://docs.cloud.google.com/billing/docs/how-to/verify-billing-enabled#confirm_billing_is_enabled_on_a_project). 

  13. Enable the required APIs, if any are not already enabled: 

**Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you created the project, then you likely already have this permission through the Owner role (`roles/owner`). Otherwise, you can get this permission through the Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
         
         gcloud services enable container.googleapis.com storage.googleapis.com compute.googleapis.com servicenetworking.googleapis.com lustre.googleapis.com

  14. Grant roles to your user account. Run the following command once for each of the following IAM roles: `roles/container.admin, roles/iam.serviceAccountAdmin, roles/storage.admin, roles/servicenetworking.networksAdmin, roles/compute.networkAdmin, roles/lustre.admin`
         
         gcloud projects add-iam-policy-binding PROJECT_ID --member="user:USER_IDENTIFIER" --role=ROLE

Replace the following:

     * `PROJECT_ID`: Your project ID.
     * `USER_IDENTIFIER`: The identifier for your user account. For example, `myemail@example.com`. 
     * `ROLE`: The IAM role that you grant to your user account.
  15. Create a [Hugging Face](https://huggingface.co/) account, if you don't already have one. 
  16. Ensure that you have a [Hugging Face token](https://huggingface.co/docs/hub/security-tokens) with `read access`. 
  17. Create a [Weights & Biases (Wandb)](https://wandb.ai/) account, if you don't have one.
  18. Create a [ Wandb API key](https://docs.wandb.ai/models/track/public-api-guide#create-an-api-key).
  19. Ensure your Google Cloud project has sufficient quota for B200 and H200 GPUs. To learn more, see [Plan GPU quota](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/gpus#gpu-quota) and [GPU quota](https://docs.cloud.google.com/compute/resource-usage#gpu_quota).
  20. Verify that your Google Cloud project has the necessary quota for Managed Lustre. For more information, see [ Managed Lustre quotas and limits](https://docs.cloud.google.com/managed-lustre/docs/quotas).



## Prepare your environment

In this tutorial, you use [Cloud Shell](https://docs.cloud.google.com/shell).

  1. Go to the [Google Cloud console](https://console.cloud.google.com/).

  2. At the top of the Google Cloud console window, click the **Activate Cloud Shell** button.

  3. Set the following environment variables:
         
         export CONTROL_PLANE_REGION="YOUR_REGION"
         export NODE_ZONE="YOUR_ZONE"
         export LUSTRE_ZONE="YOUR_LUSTRE_ZONE"
         export CLUSTER_NAME="YOUR_CLUSTER_NAME"
         export GPU_TYPE="YOUR_GPU_TYPE"
         export MACHINE_TYPE="YOUR_MACHINE_TYPE"
         export CPU_MACHINE_TYPE="YOUR_CPU_MACHINE_TYPE"
         export KSA_NAME="generic-ksa"
         export NAMESPACE="default"
         export RESERVATION="YOUR_RESERVATION_NAME"
         export LUSTRE_NAME="YOUR_LUSTRE_NAME"
         export HF_TOKEN="YOUR_HF_TOKEN"
         export WANDB_API_KEY="YOUR_WANDB_API_KEY"
         
         export PROJECT_ID=$(gcloud config get project)
         export PROJECT_NUMBER=$(gcloud projects describe "${PROJECT_ID}" --format="value(projectNumber)")

Replace the following values:

     * `YOUR_REGION`: the Compute Engine region for the GKE cluster control plane.
     * `YOUR_ZONE`: the zone for your nodes. Select a [zone where NVIDIA B200 or H200 GPUs are available](https://docs.cloud.google.com/compute/docs/regions-zones/gpu-regions-zones#view-using-table).
     * `YOUR_LUSTRE_ZONE`: the zone for your Managed Lustre instance. Select a [zone where Managed Lustre is available](https://docs.cloud.google.com/managed-lustre/docs/locations). To improve performance, reduce latency, and avoid network egress costs, use the same zone as `YOUR_ZONE`.
     * `YOUR_CLUSTER_NAME`: the name of your GKE cluster.
     * `YOUR_GPU_TYPE`: the accelerator that you reserved in the Compute Engine capacity reservation. Must be one of the following values: 
       * **`nvidia-b200`** : NVIDIA B200 (180 GB)
       * **`nvidia-h200-141gb`** : NVIDIA H200 (141 GB)
     * `YOUR_MACHINE_TYPE`: the type of machine to use: 
       * For NVIDIA B200 (180 GB) GPUs, use `a4-highgpu-8g` or later.
       * For NVIDIA H200 (141 GB) GPUs, use `a3-ultragpu-8g` or later.
     * `YOUR_CPU_MACHINE_TYPE`: the Compute Engine machine type for the CPU default node pool. Use a `highmem` machine type with at least 16 vCPUs that is supported in your cluster zone, such as `n4-highmem-16` or `n2d-highmem-16`.
     * `YOUR_RESERVATION_NAME`: the name of your GPU reservation.
     * `YOUR_LUSTRE_NAME`: the name of your Lustre instance.
     * `YOUR_HF_TOKEN`: your Hugging Face token.
     * `YOUR_WANDB_API_KEY`: your Wandb API key.
  4. Create the following environment variables for the network:
         
         export NETWORK_PREFIX="YOUR_NETWORK_NAME"
         export NETWORK="${NETWORK_PREFIX}-nemo-rl"
         export GVNIC_NETWORK_PREFIX="YOUR_GVNIC_NETWORK_PREFIX"
         export RDMA_NETWORK_PREFIX="YOUR_RDMA_NETWORK_PREFIX"

Replace the following values:

     * `YOUR_NETWORK_NAME`: the prefix used to generate the name of the VPC network for your GKE cluster.
     * `YOUR_GVNIC_NETWORK_PREFIX`: the prefix for the gVNIC network name. You can use any prefix you want.
     * `YOUR_RDMA_NETWORK_PREFIX`: the prefix for the remote direct memory access (RDMA) network. You can use any prefix you want.
  5. Install the KubeRay plugin (beta) for the `kubectl` CLI, if it isn't already installed:
         
         KUBECTL_RAY_VERSION="v1.3.2"
         curl -LO "https://github.com/ray-project/kuberay/releases/download/${KUBECTL_RAY_VERSION}/kubectl-ray_${KUBECTL_RAY_VERSION}_linux_amd64.tar.gz"
         tar -xvf "kubectl-ray_${KUBECTL_RAY_VERSION}_linux_amd64.tar.gz"
         sudo cp kubectl-ray /usr/local/bin/
         sudo chmod +x /usr/local/bin/kubectl-ray
         rm -f "kubectl-ray_${KUBECTL_RAY_VERSION}_linux_amd64.tar.gz" kubectl-ray

This plugin provides commands to manage Ray workloads on Kubernetes, such as opening interactive sessions and submitting jobs.




## Set up infrastructure

In this section, you create VPC networks and a GKE cluster.

### Create a VPC network

  1. Create a VPC network for the gVNIC interface:
         
         gcloud compute networks create ${NETWORK} --subnet-mode=auto
         
         gcloud compute networks create ${GVNIC_NETWORK_PREFIX}-net \
             --subnet-mode=custom
         
         gcloud compute networks subnets create ${GVNIC_NETWORK_PREFIX}-sub \
             --network=${GVNIC_NETWORK_PREFIX}-net \
             --region=${CONTROL_PLANE_REGION} \
             --range=192.168.0.0/24
         
         gcloud compute firewall-rules create ${GVNIC_NETWORK_PREFIX}-internal \
             --network=${GVNIC_NETWORK_PREFIX}-net \
             --action=ALLOW \
             --rules=tcp:0-65535,udp:0-65535,icmp \
             --source-ranges=192.168.0.0/16

  2. Create a VPC network and subnets for RDMA that includes eight subnets for eight GPUs:
         
         gcloud compute networks create ${RDMA_NETWORK_PREFIX}-net \
             --network-profile=${NODE_ZONE}-vpc-roce \
             --subnet-mode=custom
         
         for N in $(seq 0 7); do
           gcloud compute networks subnets create ${RDMA_NETWORK_PREFIX}-sub-$N \
             --network=${RDMA_NETWORK_PREFIX}-net \
             --region=${CONTROL_PLANE_REGION} \
             --range=192.168.$((N+1)).0/24 &
         done
         wait




### Create the GKE cluster

You can set NeMo RL in a GKE Standard cluster.

  1. Create a Standard cluster:
         
         gcloud container clusters create ${CLUSTER_NAME} \
             --location=${CONTROL_PLANE_REGION} \
             --workload-pool=${PROJECT_ID}.svc.id.goog \
             --enable-dataplane-v2 \
             --enable-ip-alias \
             --enable-multi-networking \
             --addons=RayOperator,LustreCsiDriver \
             --enable-legacy-lustre-port \
             --machine-type=${CPU_MACHINE_TYPE} \
             --num-nodes=1 \
             --min-nodes=1 \
             --max-nodes=5 \
             --enable-autoscaling \
             --network=${NETWORK}

  2. Get credentials for your cluster:
         
         gcloud container clusters get-credentials $CLUSTER_NAME \
             --location=$CONTROL_PLANE_REGION

  3. Create the GPU node pool:
         
         gcloud container node-pools create gpu-pool \
             --cluster=${CLUSTER_NAME} \
             --location=${CONTROL_PLANE_REGION} \
             --node-locations=${NODE_ZONE} \
             --machine-type=${MACHINE_TYPE} \
             --accelerator=type=${GPU_TYPE},count=8,gpu-driver-version=DEFAULT \
             --reservation-affinity=specific \
             --reservation=${RESERVATION} \
             --enable-autoscaling \
             --num-nodes=0 \
             --total-max-nodes=2 \
             --additional-node-network=network=${GVNIC_NETWORK_PREFIX}-net,subnetwork=${GVNIC_NETWORK_PREFIX}-sub \
             --additional-node-network=network=${RDMA_NETWORK_PREFIX}-net,subnetwork=${RDMA_NETWORK_PREFIX}-sub-0 \
             --additional-node-network=network=${RDMA_NETWORK_PREFIX}-net,subnetwork=${RDMA_NETWORK_PREFIX}-sub-1 \
             --additional-node-network=network=${RDMA_NETWORK_PREFIX}-net,subnetwork=${RDMA_NETWORK_PREFIX}-sub-2 \
             --additional-node-network=network=${RDMA_NETWORK_PREFIX}-net,subnetwork=${RDMA_NETWORK_PREFIX}-sub-3 \
             --additional-node-network=network=${RDMA_NETWORK_PREFIX}-net,subnetwork=${RDMA_NETWORK_PREFIX}-sub-4 \
             --additional-node-network=network=${RDMA_NETWORK_PREFIX}-net,subnetwork=${RDMA_NETWORK_PREFIX}-sub-5 \
             --additional-node-network=network=${RDMA_NETWORK_PREFIX}-net,subnetwork=${RDMA_NETWORK_PREFIX}-sub-6 \
             --additional-node-network=network=${RDMA_NETWORK_PREFIX}-net,subnetwork=${RDMA_NETWORK_PREFIX}-sub-7

  4. Install the NCCL RDMA installer:
         
         kubectl apply -f https://raw.githubusercontent.com/GoogleCloudPlatform/container-engine-accelerators/64f0eeb0dc1d980eaef8939584f832bb10e3d482/gpudirect-rdma/nccl-rdma-installer.yaml




### Configure network mappings

  1. Save the following manifest as `network-mapping.yaml`:
         
         # Copyright 2026 Google LLC. All rights reserved.
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




## Prepare storage

In this section, you create a [Managed Lustre](https://cloud.google.com/products/managed-lustre) instance, which provisions the high-performance storage required for your RL workload.

  1. Allocate an IP address range for private services access:
         
         gcloud compute addresses create ${LUSTRE_NAME}-range \
             --global --purpose=VPC_PEERING \
             --prefix-length=20 --network=${NETWORK}

  2. Connect the peering:
         
         gcloud services vpc-peerings connect \
             --service=servicenetworking.googleapis.com \
             --ranges=${LUSTRE_NAME}-range \
             --network=${NETWORK}

  3. Create a Managed Lustre instance:
         
         gcloud lustre instances create ${LUSTRE_NAME} \
             --per-unit-storage-throughput=500 \
             --capacity-gib=18000 \
             --filesystem=lustrefs \
             --location=${LUSTRE_ZONE} \
             --network=projects/${PROJECT_ID}/global/networks/${NETWORK} \
             --gke-support-enabled

  4. Access an existing Managed Lustre instance using the Managed Lustre CSI driver.

     1. Extract the IP address of the Managed Lustre instance.
            
            export LUSTRE_IP=$(gcloud lustre instances describe ${LUSTRE_NAME} \
                --location=${LUSTRE_ZONE} --format="value(mountPoint)" | awk -F'@' '{print $1}')

     2. Save the following manifest as `lustre-pv.yaml`:
            
            # Copyright 2026 Google LLC
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
            
            apiVersion: v1
            kind: PersistentVolume
            metadata:
              name: lustre-pv
            spec:
              storageClassName: lustre-rwx-500mbps-per-tib
              capacity:
                storage: 18000Gi
              accessModes:
                - ReadWriteMany
              persistentVolumeReclaimPolicy: Retain
              volumeMode: Filesystem
              claimRef:
                namespace: default
                name: lustre-pvc
              csi:
                driver: lustre.csi.storage.gke.io
                volumeHandle: "${PROJECT_ID}/${LUSTRE_ZONE}/${LUSTRE_NAME}"
                volumeAttributes:
                  ip: ${LUSTRE_IP}
                  filesystem: lustrefs

     3. Apply the manifest:
            
            envsubst < lustre-pv.yaml | kubectl apply -f -

     4. Save the following manifest as `lustre-pvc.yaml`:
            
            # Copyright 2026 Google LLC
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
            
            apiVersion: v1
            kind: PersistentVolumeClaim
            metadata:
              name: lustre-pvc
            spec:
              accessModes:
                - ReadWriteMany
              storageClassName: lustre-rwx-500mbps-per-tib
              volumeName: lustre-pv
              resources:
                requests:
                  storage: 18000Gi

     5. Apply the manifest:
            
            kubectl apply -f lustre-pvc.yaml




## Deploy RayCluster

In this section, you clone the sample repository, prepare the manifests, and deploy Ray cluster:

  1. Clone the sample repository and check out the verified commit:
         
         git clone https://github.com/GoogleCloudPlatform/kubernetes-engine-samples.git
         git -C kubernetes-engine-samples checkout 87fa0575c977b96f6d3af2cab58c9128f3cf0dc3

  2. Navigate to the working directory:
         
         cd kubernetes-engine-samples/ai-ml/nemo-rl-on-gke/nemoRL

  3. Inspect the `values.yaml` manifest:
         
         # Copyright 2026 Google LLC
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
         
         image:
           repository: "nvcr.io/nvidia/nemo-rl"
           tag: "v0.5.0" 
           pullPolicy: Always
         
         nameOverride: "kuberay"
         fullnameOverride: ""
         
         common:
           containerEnv: {}
         
         configMap:
           fluentbit:
             data:
               fluent-bit.conf: |
                 [INPUT]
                     Name              tail
                     Path              /tmp/ray/session_latest/logs/worker-*
                     Tag               ray-worker
                 [INPUT]
                     Name              tail
                     Path              /tmp/ray/session_latest/logs/raylet*
                     Tag               raylet
                 [INPUT]
                     Name              tail
                     Path              /tmp/ray/session_latest/logs/*
                     Exclude_Path      /tmp/ray/session_latest/logs/debug_state.txt,/tmp/ray/session_latest/logs/raylet*,/tmp/ray/session_latest/logs/worker-*
                     Tag               ray-misc
                 [OUTPUT]
                     Name              stackdriver
                     Match             *
                     resource          gce_instance
                     labels_key        labels
         
         # --- Head Node Configuration ---
         head:
           enableInTreeAutoscaling: false
           serviceAccountName: ""
           rayStartParams:
             dashboard-host: '0.0.0.0'
           template:
             metadata:
               annotations:
                 gke-gcsfuse/volumes: "true"
                 networking.gke.io/default-interface: 'eth0'
           containerEnv:
           - name: RAY_GROUP
             value: "head"
           nodeSelector:
             cloud.google.com/gke-nodepool: default-pool
           resources:
             limits:
               cpu: "64"
               memory: "500G"
               nvidia.com/gpu: 0
             requests:
               cpu: "64"
               memory: "500G"
               nvidia.com/gpu: 0
           tolerations:
             # - operator: "Exists"
             #   key: "components.gke.io/gke-managed-components"
             # - key: "nvidia.com/gpu"
             #   operator: "Exists"
             #   effect: "NoSchedule"
           volumeMounts:
             - mountPath: /data
               name: lustre-data
         
           volumes:
             - name: log-volume
               emptyDir: {}
             - name: fluentbit-config-volume
               configMap:
                 name: "ray-cluster-kuberay-fluentbit-config"
             - name: lustre-data
               persistentVolumeClaim:
                 claimName: lustre-pvc
           sidecarContainers:
             - name: fluent-bit
               image: fluent/fluent-bit:latest
               env:
               - name: RAY_GROUP
                 value: "head"
               volumeMounts:
                 - name: fluentbit-config-volume
                   mountPath: /fluent-bit/etc/
                 - mountPath: /tmp/ray
                   name: log-volume
         
           # --- HEAD POD STARTUP SCRIPT ---
           command:
             - "bash"
             - "-c"
             - |
               set -ex
               echo "--- Head Pod Setup ---"
               apt-get update
               apt-get install -y sudo netcat-openbsd pciutils
               cd /opt/nemo-rl
               /usr/bin/python -m pip install uv
               /usr/bin/python -m uv venv
               echo "Head pod setup complete. Starting Ray..."
         
               exec ${KUBERAY_GEN_RAY_START_CMD}
         
           args: []
           headService: {}
           # nodeSelector:
           #   cloud.google.com/gke-accelerator: nvidia-b200 #cloud.google.com/gke-nodepool: cpu-node-pool-llama #cpu-node-pool
         
         # --- Default Worker (Disabled) ---
         worker:
           disabled: true
         
         # --- A4 GPU Worker Groups ---
         additionalWorkerGroups:
           worker-grp-0:
             disabled: false
             replicas: 4
             annotations:
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
             containerEnv:
               - name: RAY_GROUP
                 valueFrom:
                   fieldRef:
                     fieldPath: metadata.labels['ray.io/group']
               - name: NCCL_NET  
                 value: "gIB"
               - name: NCCL_IB_GID_INDEX
                 value: "3"   
               - name: GLOO_SOCKET_IFNAME
                 value: "eth0"
               - name: NCCL_CROSS_NIC
                 value: "0"
               - name: NCCL_SOCKET_IFNAME
                 value: "eth0"
               - name: TP_SOCKET_IFNAME # Specific to DTensor/PyTorch Distributed
                 value: "eth0"
               - name: NCCL_TUNER_CONFIG_PATH
                 value: "/usr/local/gib/configs/tuner_config_a4.txtpb"
               - name: NCCL_NET_GDR_LEVEL
                 value: "PIX"
               - name: LD_LIBRARY_PATH
                 value: /usr/local/nvidia/lib64
             resources:
               limits:
                 nvidia.com/gpu: 8
                 cpu: "206"
                 memory: "2400Gi"
               requests:
                 nvidia.com/gpu: 8
                 cpu: "206"
                 memory: "2400Gi"
         
             nodeSelector:
               cloud.google.com/gke-accelerator: nvidia-b200
             tolerations:
               - operator: "Exists"
                 key: "nvidia.com/gpu"
               - operator: "Exists"
                 key: "cloud.google.com/impending-node-termination"
               - operator: "Exists"
                 key: "user-workload"
             securityContext:
               privileged: true
             volumes:
               - name: log-volume
                 emptyDir: {}
               - name: shared-memory
                 emptyDir:
                   medium: "Memory"
                   sizeLimit: 240Gi
               - name: ray-tmp
                 emptyDir:
                   medium: "Memory"
               - name: fluentbit-config-volume
                 configMap:
                   name: "ray-cluster-kuberay-fluentbit-config"
               - name: nvidia-install-dir-host
                 hostPath:
                   path: /home/kubernetes/bin/nvidia
               - name: gib-nccl-plugin-volume
                 hostPath: 
                   path: /home/kubernetes/bin/gib
               - name: lustre-data
                 persistentVolumeClaim:
                   claimName: lustre-pvc
             volumeMounts:
               - mountPath: /tmp/ray
                 name: log-volume
               - name: shared-memory
                 mountPath: /dev/shm
               - name: nvidia-install-dir-host
                 mountPath: /usr/local/nvidia
               - name: gib-nccl-plugin-volume
                 mountPath: /usr/local/gib
               - mountPath: /data
                 name: lustre-data   
             # --- WORKER POD STARTUP SCRIPT ---
             command:
               - "bash"
               - "-c"
               - |
                 set -ex
         
                 echo "--- Worker Pod Setup ---"
                 apt-get update
                 apt-get install -y sudo netcat-openbsd pciutils
                 cd /opt/nemo-rl
                 /usr/bin/python -m pip install uv
                 /usr/bin/python -m uv venv
         
                 ldconfig /usr/local/nvidia/lib64/
                 ldconfig -p | grep libcuda | sed 's/^/  /'
                 export LD_LIBRARY_PATH="/usr/local/gib/lib64:$LD_LIBRARY_PATH"
                 source /usr/local/gib/scripts/set_nccl_env.sh
         
                 echo "Worker pod setup complete. Starting Ray..."
         
                 exec ${KUBERAY_GEN_RAY_START_CMD}
         
         
             sidecarContainers:
               - name: fluent-bit
                 env:
                   - name: RAY_GROUP
                     valueFrom:
                       fieldRef:
                         fieldPath: metadata.labels['ray.io/group']
                 image: fluent/fluent-bit:latest
                 volumeMounts:
                   - name: fluentbit-config-volume
                     mountPath: /fluent-bit/etc/
                   - mountPath: /tmp/ray
                     name: log-volume
         
         # --- Service Config ---
         service:
           type: ClusterIP
         

Replace `NCCL_TUNER_CONFIG_PATH` with any of the following values, based on the accelerator you use in this tutorial:

     * **NVIDIA B200 (180 GB)** : `/usr/local/gib/configs/tuner_config_a4.txtpb`
     * **NVIDIA H200 (141 GB)** : `/usr/local/gib/configs/tuner_config_a3u.txtpb`

In this manifest, the head node manages the Job and hosts the Ray Dashboard. The worker nodes run the training Jobs.

  4. Deploy the Ray cluster:
         
         export REPLICA_COUNT=2
         helm install ray-cluster . \
           --set additionalWorkerGroups.worker-grp-0.replicas=$REPLICA_COUNT \
           --set head.resources.requests.cpu=12 \
           --set head.resources.requests.memory=96Gi \
           --set head.resources.limits.cpu=12 \
           --set head.resources.limits.memory=96Gi

For this tutorial, you use two worker nodes. If you want to change the number of worker nodes, change the `REPLICA_COUNT` value.

  5. Verify that the Pods hosting the Ray head and worker nodes are running:
         
         kubectl get pods

The output is similar to the following:
         
         NAME                                          READY STATUS RESTARTS AGE
         ray-cluster-kuberay-head-sw7dp                2/2   Running 0      33h
         ray-cluster-kuberay-worker-grp-0-worker-gkbxw 2/2   Running 0      33h
         ray-cluster-kuberay-worker-grp-0-worker-kdg62 2/2   Running 0      33h
         

It can take about 10 minutes for the Pods to start.

  6. Verify the Ray cluster is running:
         
         kubectl ray get cluster

The output is similar to the following:
         
         NAME                 NAMESPACE DESIRED WORKERS AVAILABLE WORKERS CPUS GPUS TPUS MEMORY CONDITION STATUS AGE
         ray-cluster-kuberay  default   2       2           618     17   0    1573741824k RayClusterProvisioned ready 33h
         




## Launch the GRPO Job

After your Ray cluster is ready, you can submit a Ray Job to your running Ray cluster on GKE. NeMo RL automatically downloads the model during the execution of the RL training Job.

To submit a Ray Job, start an interactive session to execute the Job.

  1. To establish a local connection to your Ray cluster, run this command:
         
         kubectl ray session ray-cluster-kuberay

This command initiates port forwarding between your local machine and the Ray head node in your GKE cluster. Note that your terminal will be occupied while this session is active; to proceed, open a separate terminal instance.

  2. In a separate terminal, navigate to `kubernetes-engine-samples/ai-ml/nemo-rl-on-gke/nemoRL/gemma3-27b-it` and edit the `gemma3-27b-gsm8k.sh` file:
         
         # Copyright 2026 Google LLC
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
         
         #!/bin/bash
         WANDB_API_KEY='YOUR_WANDB_API_KEY' # Update this with your WANDB API key
         HF_TOKEN='YOUR_HF_TOKEN' # Update this with your HF token
         WORLD_SIZE=16
         
         # --- Step 1: Find the Ray Head Pod ---
         echo "Finding Ray head pod..."
         export HEAD_POD_NAME=$(kubectl get pods --selector=ray.io/node-type=head -o jsonpath='{.items[0].metadata.name}')
         if [ -z "$HEAD_POD_NAME" ]; then
             echo "Error: No running Ray head pod found. Please check your cluster."
             exit 1
         fi
         echo "Found head pod: $HEAD_POD_NAME"
         echo ""
         
         # --- Step 2: Define the Job Script to Run ---
         # This is the script that will be executed *inside* the head pod.
         # It assumes the 'uv venv' setup from the values.yaml is already done.
         JOB_SCRIPT=$(cat <<EOF
         set -ex
         
         echo "--- Running on Ray Head Pod ($HOSTNAME) ---"
         cd /opt/nemo-rl
         
         git pull && git checkout main
         
         sed -i 's/subset: Optional\[str\] = None/subset: Optional[str] = "main"/' /opt/nemo-rl/nemo_rl/data/datasets/response_datasets/response_dataset.py
         sed -i 's/raw_dataset = load_dataset(data_path)/raw_dataset = load_dataset(data_path, "main")/' /opt/nemo-rl/nemo_rl/data/datasets/utils.py
         
         echo "Setting environment variables..."
         export WANDB_API_KEY=$WANDB_API_KEY
         export HF_TOKEN=$HF_TOKEN
         export HF_HOME=/opt/nemo-rl/
         
         ###-----Example to launch Gemma3-27B on 2 nodes (16 GPUs)----------
         uv run python examples/run_grpo_math.py \
           --config examples/configs/recipes/llm/grpo-gemma3-27b-it-8n4g-fsdp2tp4-actckpt-long.yaml \
           cluster.num_nodes=2 \
           cluster.gpus_per_node=8 \
           grpo.max_num_steps=10 \
           checkpointing.checkpoint_dir=/data/nemo_rl_gemma3_27b_3_17 \
           data.dataset_name=ResponseDataset \
           +data.train_data_path=openai/gsm8k \
           +data.val_data_path=openai/gsm8k \
           +data.val_split=test \
           +data.train_split=train \
           +data.subset="main" \
           +data.input_key="question" \
           +data.output_key="answer" \
           logger.tensorboard_enabled=False \
           logger.wandb_enabled=True \
           logger.wandb.name='nemo_rl_gemma3_27b_3_17' \
           grpo.num_prompts_per_step=16 \
           grpo.num_generations_per_prompt=32 \
           policy.generation.colocated.enabled=False \
           policy.generation.colocated.resources.num_nodes=1 \
           policy.generation.colocated.resources.gpus_per_node=8 \
           policy.generation.vllm_cfg.tensor_parallel_size=8 \
           policy.generation.vllm_cfg.gpu_memory_utilization=0.9 \
           policy.dtensor_cfg.tensor_parallel_size=8
         
         echo "--- Job Finished ---"
         EOF
         )
         
         # --- Step 3: Execute the Job ---
         echo "Submitting job to $HEAD_POD_NAME..."
         echo "$JOB_SCRIPT" | tr -d '\r' | kubectl exec -i $HEAD_POD_NAME -c ray-head -- /bin/bash
         
         echo ""
         echo "Job submission complete."
         

Replace the following values in the `gemma3-27b-gsm8k.sh` file:

     * `YOUR_WANDB_API_KEY`: your WandB API key.
     * `YOUR_HF_TOKEN`: your Hugging Face token.

In this file, you can see the configuration to run a Job with the gemma3-27b-it model on the GSM8k dataset. To complete the GRPO training pipeline, this script defines the following parameters:

     * `num_prompts_per_step: 16` and `num_generations_per_prompt: 32`: the Gemma3-27b-it model generates a large group of responses for every prompt. In this configuration, the model produces 512 total responses (16 × 32 = 512).
     * `policy.generation.colocated.enabled=False`: this parameter disables the colocated generation feature, which means that the model doesn't generate responses in the same node as the training process. In standard RL, the same GPUs handle both training and generation. In this NeMo RL setup, you dedicate specific nodes (managed with the `policy.generation.colocated.resources` parameter) solely to [vLLM](https://github.com/vllm-project/vllm) inference, while the rest of the cluster focuses on the heavy-duty training math. By separating these workloads, you prevent resource contention between the memory-intensive training buffers and the compute-intensive inference workloads.
  3. In your initial terminal window, submit the Job:
         
         bash gemma3-27b-it/gemma3-27b-gsm8k.sh

When the Job is running, the output shows the training results, timing, and performance metrics.


**Success:** NeMo RL is orchestrating a distributed lifecycle across the GPU VMs in the cluster.

## Monitor the health of the GRPO Job

After Ray finishes the Job, NeMo RL stores the checkpoints in the configured path.

  1. To check the output of the GRPO Job, create an SSH session to the `ray-head` container:
         
         kubectl exec -it $(kubectl get pods -l ray.io/node-type=head -o name) -c ray-head -- bash

  2. Install the apt tree utility within the `ray-head` container's terminal:
         
         apt update && apt install -y tree

  3. List the directory structure of the `ray-head` container:
         
         tree /data/nemo_rl_gemma3_27b_3_17/

The output is similar to the following:
         
         root@ray-cluster-kuberay-worker-grp-0-worker-gkbxw:/opt/nemo-rl# tree /data/nemo_rl_gemma3_27b_3_17/
         /data/nemo_rl_gemma3_27b_3_17/
         `-- step_10
             |-- config.yaml
             |-- policy
             |   |-- optimizer
             |   |   |-- __0_0.distcp
             |   |   |-- __10_0.distcp
             |   |   |-- __11_0.distcp
             |   |   |-- __12_0.distcp
             |   |   |-- __13_0.distcp
             |   |   |-- __14_0.distcp
             |   |   |-- __15_0.distcp
             |   |   |-- __1_0.distcp
             |   |   |-- __2_0.distcp
             |   |   |-- __3_0.distcp
             |   |   |-- __4_0.distcp
             |   |   |-- __5_0.distcp
             |   |   |-- __6_0.distcp
             |   |   |-- __7_0.distcp
             |   |   |-- __8_0.distcp
             |   |   `-- __9_0.distcp
             |   |-- tokenizer
             |   |   |-- chat_template.jinja
             |   |   |-- special_tokens_map.json
             |   |   |-- tokenizer.json
             |   |   `-- tokenizer_config.json
             |   `-- weights
             |       |-- __0_0.distcp
             |       |-- __10_0.distcp
             |       |-- __11_0.distcp
             |       |-- __12_0.distcp
             |       |-- __13_0.distcp
             |       |-- __14_0.distcp
             |       |-- __15_0.distcp
             |       |-- __1_0.distcp
             |       |-- __2_0.distcp
             |       |-- __3_0.distcp
             |       |-- __4_0.distcp
             |       |-- __5_0.distcp
             |       |-- __6_0.distcp
             |       |-- __7_0.distcp
             |       |-- __8_0.distcp
             |       `-- __9_0.distcp
             |-- train_dataloader.pt
             `-- training_info.json
         
         6 directories, 39 files
         


**Note:** The checkpoints generated by NeMo RL are in PyTorch distributed checkpoint format. To evaluate or serve the model, you need to convert the checkpoint to Hugging Face weight format. For instructions on how to convert the checkpoint, see [Convert the PyTorch DCP format to HF format](https://github.com/GoogleCloudPlatform/kubernetes-engine-samples/tree/main/ai-ml/nemo-rl-on-gke/nemoRL/gemma3-27b-it#convert-the-pytorch-dcp-format-to-hf-format).

## Clean up

To avoid incurring charges to your Google Cloud account for the resources used in this tutorial, either delete the individual resources, or delete the project that contains them.

### Delete the resources

  1. Delete your Slurm cluster:
         
         helm delete ray-cluster

  2. Delete your GKE cluster:
         
         gcloud container clusters delete ${CLUSTER_NAME} \
             --location=${CONTROL_PLANE_REGION} \
             --quiet || true

  3. Delete your Lustre file system:
         
         gcloud lustre instances delete ${LUSTRE_NAME} \
             --location=${LUSTRE_ZONE} \
             --quiet || true

  4. Delete VPC peering:
         
         gcloud services vpc-peerings delete \
             --service=servicenetworking.googleapis.com \
             --network=${NETWORK} \
             --quiet || true

  5. Delete the Lustre private IP address range:
         
         gcloud compute addresses delete ${LUSTRE_NAME}-range --global --quiet || true

  6. Delete RDMA and gVNIC subnets:
         
         gcloud compute networks subnets delete ${GVNIC_NETWORK_PREFIX}-sub \
             --region=${CONTROL_PLANE_REGION} \
             --quiet || true
         
         for N in $(seq 0 7); do
           gcloud compute networks subnets delete ${RDMA_NETWORK_PREFIX}-sub-$N \
             --region=${CONTROL_PLANE_REGION} --quiet || true &
         done
         wait

  7. Delete firewall rules and networks:
         
         echo "[$(date)] ========== Deleting firewall rules and networks =========="
         
         NETWORKS=(
             "${RDMA_NETWORK_PREFIX}-net"
             "${GVNIC_NETWORK_PREFIX}-net"
             "${NETWORK}"
         )
         
         for NW in "${NETWORKS[@]}"; do
         
           # Skip if empty, named 'default', or not starting with a lowercase letter (invalid resource name)
           if [[ "${NW}" == "default" || ! "${NW}" =~ ^[a-z] ]]; then
             echo "Skipping protected/invalid network: '${NW}'"
             continue
           fi
         
           echo "========== Deleting firewall rules for ${NW} =========="
           while true; do
               rules=$(gcloud compute firewall-rules list \
                 --filter="network:${NW}" \
                 --format="value(name)" \
                 --project="${PROJECT_ID}")
         
                 if [[ -z "${rules}" ]]; then
                   echo "No firewall rules remain for ${NW}"
                   break
                 fi
         
                 for rule in ${rules}; do
                   echo "Deleting firewall rule ${rule}..."
                   gcloud compute firewall-rules delete "${rule}" --project="${PROJECT_ID}" --quiet || true
                 done
         
                 sleep 3
               done
         
               echo "[$(date)] ========== Deleting network ${NW} =========="
               gcloud compute networks delete ${NW} --quiet || true
         done




### Delete your project

**Caution** : Deleting a project has the following effects: 

  * **Everything in the project is deleted.** If you used an existing project for the tasks in this document, when you delete it, you also delete any other work you've done in the project. 
  * **Custom project IDs are lost.** When you created this project, you might have created a custom project ID that you want to use in the future. To preserve the URLs that use the project ID, such as an `appspot.com` URL, delete selected resources inside the project instead of deleting the whole project. 



If you plan to explore multiple architectures, tutorials, or quickstarts, reusing projects can help you avoid exceeding project quota limits. 

Delete a Google Cloud project:
    
    
    gcloud projects delete PROJECT_ID

## What's next

  * [Learn about Ray on GKE](https://docs.cloud.google.com/kubernetes-engine/docs/add-on/ray-on-gke/concepts/overview)
  * [Explore NVIDIA NeMo RL documentation](https://docs.nvidia.com/nemo/rl/latest/index.html)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
