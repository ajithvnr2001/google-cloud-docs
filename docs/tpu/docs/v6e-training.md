---
url: https://docs.cloud.google.com/tpu/docs/v6e-training/
title: Train a model using TPU v6e \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T12:36:11.381690+00:00
---

# Train a model using TPU v6e  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/tpu/docs/v6e-training/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Cloud TPU ](https://docs.cloud.google.com/tpu/docs)
  * [ Guides ](https://docs.cloud.google.com/tpu/docs/intro-to-tpu)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Train a model using TPU v6e

**Caution:** This page applies to the Cloud TPU API, which is no longer under active development. The Cloud TPU API will receive bug fixes and security updates only. For the latest features and support for the latest TPU versions, we recommend using Compute Engine or Google Kubernetes Engine to manage TPU resources. For more information, see [TPU resources in Compute Engine](https://docs.cloud.google.com/tpu/docs/tpus-in-compute-engine) and [About TPUs in GKE](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/tpus). The Cloud TPU API is not supported on TPU7x and later TPU versions. 

This document guides you through training models on Cloud TPU v6e (also called Trillium), covering environment setup, performance optimization, and practical training examples using JAX and PyTorch.

TPU v6e, also called Trillium, is Google's 6th generation of TPUs. On all technical surfaces, such as the API and logs, and throughout this document, Trillium will be referred to as v6e. With 256 chips per Pod, the architecture of TPU v6e shares many similarities with [v5e](https://docs.cloud.google.com/tpu/docs/v5e). TPU v6e is optimized for transformer, text-to-image, and convolutional neural network (CNN) training, fine-tuning, and serving. For more information about the TPU v6e system architecture and configurations, see [TPU v6e](https://docs.cloud.google.com/tpu/docs/v6e).

For information about running inference on Cloud TPU v6e, see the following tutorials:

  * [MaxDiffusion inference on v6e](https://docs.cloud.google.com/tpu/docs/tutorials/LLM/maxdiffusion-inference-v6e)
  * [vLLM inference on v6e](https://docs.cloud.google.com/tpu/docs/tutorials/LLM/vllm-inference-v6e)
  * [Perform multihost inference using Pathways](https://docs.cloud.google.com/ai-hypercomputer/docs/workloads/pathways-on-cloud/multihost-inference)



## Before you begin

Before you begin, you need to:

  * Set up a Google Cloud project for TPUs
  * Install Google Cloud CLI
  * Enable the Compute Engine API
  * Create a Compute Engine service account and grant permissions



For more information, see [Set up the Cloud TPU environment](https://docs.cloud.google.com/tpu/docs/setup-gcp-account-compute).

### Verify quota and permissions

Verify that your project has the following quotas:

  * [Compute Engine TPU-accelerator quota](https://docs.cloud.google.com/compute/resource-usage#tpu_quota)
  * [Compute Engine VM quota](https://docs.cloud.google.com/compute/resource-usage#vm_instance_quota)
  * [IP address quota](https://docs.cloud.google.com/vpc/docs/quota)
  * [Quota for Hyperdisk Balanced and for any other disk types you want to use](https://docs.cloud.google.com/compute/resource-usage#disk_quota)

**Note:** v6e supports Hyperdisk Balanced and Hyperdisk ML. v6e doesn't support Persistent Disk (PD). For more information, see [Storage options for Cloud TPU data](https://docs.cloud.google.com/tpu/docs/storage-options).



If you're using Google Kubernetes Engine (GKE) with XPK (Accelerated Processing Kit), you need additional permissions in the Google Cloud console. For more information, see [Permissions needed on Google Cloud console ](https://github.com/AI-Hypercomputer/xpk/blob/main/README.md#permissions-needed-on-cloud-console).

## Provisioning options

You can provision and manage TPU v6e using the following methods:

  * **Compute Engine (Google Cloud CLI)** : You can use the Google Cloud CLI tool to manage TPU VMs directly as Compute Engine resources. You can provision individual TPU VMs or use Managed Instance Groups (MIGs) to manage groups of TPU VMs. For more information, see [TPU creation overview](https://docs.cloud.google.com/tpu/docs/create-tpu-vm-compute).
  * **GKE** : You can use GKE to provision and manage TPUs as a pool of accelerators for your containerized machine learning workloads. For more information, see [About TPUs in GKE](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/tpus).
  * **GKE and XPK** : XPK is a command-line tool that simplifies cluster creation and workload execution on GKE. It's designed for ML practitioners to provision TPUs and run training jobs without needing deep Kubernetes expertise. For more information, see [the XPK GitHub repository](https://github.com/AI-Hypercomputer/xpk/tree/main).



## Provision v6e TPUs with GKE and XPK

If you are using GKE with v6e TPUs, you can use Kubernetes commands or [XPK](https://github.com/AI-Hypercomputer/xpk/blob/main/README.md) to provision TPUs and train or serve models. For more information about using GKE with TPUs, see [About TPUs in GKE](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/tpus).

Cloud TPU v6e supports network interface card (NIC) configurations that let you scale throughput across multiple networks. The following sections provide commands to create a GKE cluster with single-NIC support or multi-NIC support using XPK. For most single-slice workloads, single-NIC provides sufficient performance with less configuration. For Multislice workloads and workloads that require high data ingestion speeds, use multi-NIC.

### Create a cluster with single-NIC support using XPK

For most single-slice workloads, single-NIC provides sufficient performance with less configuration. For Multislice workloads and workloads that require high data ingestion speeds, use multi-NIC.

The following sections show how to create a GKE cluster with single-NIC support using XPK.

#### Install XPK and set up environment variables

  1. Install XPK. Follow the instructions in the [XPK GitHub repository](https://github.com/AI-Hypercomputer/xpk/blob/main/docs/installation.md).

  2. Set up environment variables for your cluster:
         
         export CLUSTER_NAME=XPK_CLUSTER_NAME
         export ZONE=us-east1-d
         export PROJECT_ID=PROJECT_ID
         export ACCELERATOR_TYPE=ACCELERATOR_TYPE
         export NUM_SLICES=1

Set the following environment variables:

     * `CLUSTER_NAME`: A name for your cluster.
     * `ZONE`: The zone where the TPU cluster will be created. For more information about supported zones, see [Regions and zones](https://docs.cloud.google.com/tpu/docs/regions-zones).
     * `PROJECT_ID`: Your Google Cloud project ID.
     * `ACCELERATOR_TYPE`: The TPU type, also called accelerator type, specifies the version and size of the Cloud TPU you want to create. For example, `v6e-256`. For more information about supported accelerator types for each TPU version, see [TPU versions](https://docs.cloud.google.com/tpu/docs/system-architecture-tpu-vm#versions).
     * `NUM_SLICES`: The number of TPU slices for your cluster. Each slice has the number of chips specified in `ACCELERATOR_TYPE`. For a single-slice cluster, set `NUM_SLICES` to 1. For a Multislice cluster, specify the number of slices based on your workload's scalability requirements. The total number of chips in the cluster is the number of chips in `ACCELERATOR_TYPE` multiplied by `NUM_SLICES`.



#### Create the cluster

Choose one of the following options to create your cluster. Using a custom network with 8,896 MTU is recommended for optimal performance. For more information, see [Configure MTU](https://docs.cloud.google.com/tpu/docs/performance-guide#configure-mtu).

### Custom network

To create a custom network with 8,896 MTU and use it for your cluster, follow these steps:

  1. Set environment variables for the network and firewall names:
         
         export NETWORK_NAME=NETWORK_NAME
         export NETWORK_FW_NAME=FIREWALL_NAME

Replace the following:

     * NETWORK_NAME: A name for the network.
     * FIREWALL_NAME: A name for the network firewall rule.
  2. Create a custom network with an MTU of 8,896:
         
         gcloud compute networks create ${NETWORK_NAME} \
             --mtu=8896 \
             --project=${PROJECT_ID} \
             --subnet-mode=auto \
             --bgp-routing-mode=regional

  3. Create a firewall rule that allows TCP, ICMP, and UDP traffic on your network:
         
         gcloud compute firewall-rules create ${NETWORK_FW_NAME} \
             --network=${NETWORK_NAME} \
             --allow tcp,icmp,udp \
             --project=${PROJECT_ID}

  4. Set an environment variable for the XPK cluster arguments to use the network you created:
         
         export CLUSTER_ARGUMENTS="--network=${NETWORK_NAME} --subnetwork=${NETWORK_NAME}"

  5. Create the XPK cluster. The following command provisions on-demand capacity:
         
         xpk cluster create --cluster=${CLUSTER_NAME} \
             --cluster-cpu-machine-type=e2-standard-8 \
             --num-slices=${NUM_SLICES} \
             --tpu-type=${ACCELERATOR_TYPE} \
             --zone=${ZONE} \
             --project=${PROJECT_ID} \
             --on-demand \
             --custom-cluster-arguments="${CLUSTER_ARGUMENTS}"

To use reserved capacity, replace `--on-demand` with `--reservation=RESERVATION_NAME`. To use TPU Spot VMs, replace `--on-demand` with `--spot`.




### Default network

If you don't require a high-MTU network, you can create a cluster that uses the default VPC network. The following command provisions on-demand capacity:
    
    
    xpk cluster create --cluster=${CLUSTER_NAME} \
        --cluster-cpu-machine-type=e2-standard-8 \
        --num-slices=${NUM_SLICES} \
        --tpu-type=${ACCELERATOR_TYPE} \
        --zone=${ZONE} \
        --project=${PROJECT_ID} \
        --on-demand

To use reserved capacity, replace `--on-demand` with `--reservation=RESERVATION_NAME`. To use TPU Spot VMs, replace `--on-demand` with `--spot`.

**Note:** The `--cluster-cpu-machine-type` flag specifies the machine type for the CPU host VMs in the cluster. While `e2-standard-8` is a recommended default for many workloads, you can select a different machine type if your workload has specific CPU or memory requirements for tasks like data preprocessing.

### Create a cluster with multi-NIC support using XPK

For Multislice workloads or other workloads that require high network bandwidth, such as for data ingestion, you can use multi-NIC to improve performance. When you use multi-NIC, each TPU VM is allocated additional network interfaces, each connected to a unique VPC network, increasing overall network throughput. For most single-slice workloads, single-NIC provides sufficient performance with less configuration.

**Note:** The two subnetworks must have mutually exclusive IP ranges. This includes both the primary and secondary IP CIDR ranges in the subnetwork.

The following sections show how to create a GKE cluster with multi-NIC support using XPK.

#### Install XPK and set up environment variables

  1. Install XPK. Follow the instructions in the [XPK GitHub repository](https://github.com/AI-Hypercomputer/xpk/blob/main/docs/installation.md).

  2. Set up environment variables for your cluster and primary network:
         
         export CLUSTER_NAME=XPK_CLUSTER_NAME
         export REGION=REGION
         export ZONE=us-east1-d
         export PROJECT_ID=PROJECT_ID
         export ACCELERATOR_TYPE=ACCELERATOR_TYPE
         export NUM_SLICES=2
         
         export NETWORK_NAME_1=${CLUSTER_NAME}-mtu9k-1-${ZONE}
         export SUBNET_NAME_1=${CLUSTER_NAME}-privatesubnet-1-${ZONE}
         export FIREWALL_RULE_NAME_1=${CLUSTER_NAME}-privatefirewall-1-${ZONE}
         export ROUTER_NAME_1=${CLUSTER_NAME}-network-1-${ZONE}
         export NAT_CONFIG_1=${CLUSTER_NAME}-natconfig-1-${ZONE}
         
         export NETWORK_NAME_2=${CLUSTER_NAME}-mtu9k-2-${ZONE}
         export SUBNET_NAME_2=${CLUSTER_NAME}-privatesubnet-2-${ZONE}
         export FIREWALL_RULE_NAME_2=${CLUSTER_NAME}-privatefirewall-2-${ZONE}
         export ROUTER_NAME_2=${CLUSTER_NAME}-network-2-${ZONE}
         export NAT_CONFIG_2=${CLUSTER_NAME}-natconfig-2-${ZONE}

Set the following environment variables:

     * `CLUSTER_NAME`: A name for your cluster.
     * `REGION`: The region where your TPU cluster will be created.
     * `ZONE`: The zone where the TPU cluster will be created. For more information about supported zones, see [Regions and zones](https://docs.cloud.google.com/tpu/docs/regions-zones).
     * `PROJECT_ID`: Your Google Cloud project ID.
     * `ACCELERATOR_TYPE`: The accelerator type specifies the version and size of the Cloud TPU you want to create. For example, `v6e-256`. For more information about supported accelerator types for each TPU version, see [TPU versions](https://docs.cloud.google.com/tpu/docs/system-architecture-tpu-vm#versions).
     * `NUM_SLICES`: The number of TPU slices for your cluster. Each slice has the number of chips specified in `ACCELERATOR_TYPE`. For a single-slice cluster, set `NUM_SLICES` to 1. For a Multislice cluster, specify the number of slices based on your workload's scalability requirements. The total number of chips in the cluster is the number of chips in `ACCELERATOR_TYPE` multiplied by `NUM_SLICES`.



#### Create the primary network resources

  1. Create the primary network with a maximum transmission unit (MTU) of 8,896:
         
         gcloud compute networks create ${NETWORK_NAME_1} \
             --mtu=8896 \
             --bgp-routing-mode=regional \
             --subnet-mode=custom \
             --project=${PROJECT_ID}

Using a custom network with an MTU of 8,896 provides better performance. For more information, see [Configure MTU](https://docs.cloud.google.com/tpu/docs/performance-guide#configure-mtu).

  2. Create the primary subnetwork:
         
         gcloud compute networks subnets create ${SUBNET_NAME_1} \
             --network=${NETWORK_NAME_1} \
             --range=10.11.0.0/18 \
             --region=${REGION} \
             --project=${PROJECT_ID}

  3. Create a firewall rule for the primary network that allows `tcp`, `icmp`, and `udp` traffic on the primary network:
         
         gcloud compute firewall-rules create ${FIREWALL_RULE_NAME_1} \
             --network=${NETWORK_NAME_1} \
             --allow tcp,icmp,udp \
             --project=${PROJECT_ID}

  4. Create a Cloud Router for the primary network:
         
         gcloud compute routers create ${ROUTER_NAME_1} \
             --project=${PROJECT_ID} \
             --network=${NETWORK_NAME_1} \
             --region=${REGION}

  5. Configure NAT for the primary network. The following command allows traffic from your cluster to reach the internet:
         
         gcloud compute routers nats create ${NAT_CONFIG_1} \
             --router=${ROUTER_NAME_1} \
             --region=${REGION} \
             --auto-allocate-nat-external-ips \
             --nat-all-subnet-ip-ranges \
             --project=${PROJECT_ID} \
             --enable-logging




#### Create the secondary network resources

  1. Create the secondary network:
         
         gcloud compute networks create ${NETWORK_NAME_2} --mtu=8896 \
             --bgp-routing-mode=regional \
             --subnet-mode=custom \
             --project=${PROJECT_ID}
         

  2. Create a subnetwork for the secondary network:
         
         gcloud compute networks subnets create ${SUBNET_NAME_2} \
             --network=${NETWORK_NAME_2} \
             --range=10.10.0.0/18 \
             --region=${REGION} \
             --project=${PROJECT_ID}
         

  3. Create a firewall rule to allow traffic within the new network:
         
         gcloud compute firewall-rules create ${FIREWALL_RULE_NAME_2} \
             --network=${NETWORK_NAME_2} \
             --allow tcp,icmp,udp \
             --source-ranges 10.10.0.0/18 \
             --project=${PROJECT_ID}
         

  4. Create a Cloud Router for the secondary network:
         
         gcloud compute routers create ${ROUTER_NAME_2} \
             --project=${PROJECT_ID} \
             --network=${NETWORK_NAME_2} \
             --region=${REGION}
         

  5. Create a NAT configuration for the Cloud Router:
         
         gcloud compute routers nats create ${NAT_CONFIG_2} \
             --router=${ROUTER_NAME_2} \
             --region=${REGION} \
             --auto-allocate-nat-external-ips \
             --nat-all-subnet-ip-ranges \
             --project=${PROJECT_ID} \
             --enable-logging
         




#### Create the cluster

  1. Set an environment variable for the cluster and node pool arguments to use the networks and subnetworks you created:
         
         export CLUSTER_ARGUMENTS="--enable-dataplane-v2 --enable-ip-alias --enable-multi-networking --network=${NETWORK_NAME_1} --subnetwork=${SUBNET_NAME_1}"
         export NODE_POOL_ARGUMENTS="--additional-node-network network=${NETWORK_NAME_2},subnetwork=${SUBNET_NAME_2}"
         

These arguments configure the cluster to use the two networks you created for multi-NIC support.

  2. Create the cluster. The following command provisions on-demand capacity:
         
         xpk cluster create \
             --cluster=${CLUSTER_NAME} \
             --cluster-cpu-machine-type=e2-standard-8 \
             --num-slices=${NUM_SLICES} \
             --tpu-type=${ACCELERATOR_TYPE} \
             --zone=${ZONE}  \
             --project=${PROJECT_ID} \
             --on-demand \
             --custom-cluster-arguments="${CLUSTER_ARGUMENTS}" \
             --custom-nodepool-arguments="${NODE_POOL_ARGUMENTS}" \
             --create-vertex-tensorboard

To use reserved capacity, replace `--on-demand` with `--reservation=RESERVATION_NAME`. To use TPU Spot VMs, replace `--on-demand` with `--spot`.

**Note:** The `--cluster-cpu-machine-type` flag specifies the machine type for the CPU host VMs in the cluster. While `e2-standard-8` is a recommended default for many workloads, you can select a different machine type if your workload has specific CPU or memory requirements for tasks like data preprocessing.



#### Validate multi-NIC setup

After you create a cluster with multi-NIC support, you can validate that both NICs are being used by creating an [XPK workload](https://github.com/AI-Hypercomputer/xpk/blob/main/docs/usage/workloads.md) and adding the `--command ifconfig` flag.

  1. Use the following command to display the output of the `ifconfig` command in Google Cloud console logs. You must either specify the `--base-docker-image maxtext_base_image` flag to use the MaxText base image, as in the following example, or specify the `--docker-image` flag and the image you want to use.
         
         xpk workload create \
             --cluster ${CLUSTER_NAME} \
             --base-docker-image maxtext_base_image \
             --workload=${USER}-xpk-${ACCELERATOR_TYPE}-${NUM_SLICES} \
             --tpu-type=${ACCELERATOR_TYPE} \
             --num-slices=${NUM_SLICES}  \
             --on-demand \
             --zone=${ZONE} \
             --project=${PROJECT_ID} \
             --command "ifconfig"

If you want to enable debug logs or use  Vertex AI TensorBoard, add the following optional arguments to the command:
         
         --enable-debug-logs \
         --use-vertex-tensorboard

  2. Verify that both eth0 and eth1 have MTU set to 8,896 by checking the output of the XPK workload in Google Cloud console logs.




## Set up JAX or PyTorch

The following resources show how to set up JAX or PyTorch on your TPU, depending on which provisioning and management method you use:

  * **GKE Autopilot** : [Prepare your TPU application](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/tpus-autopilot#prepare-tpu-application)
  * **GKE Standard** : [Prepare your workloads](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/tpus#workload_preparation)
  * **GKE and XPK** : [XPK README](https://github.com/AI-Hypercomputer/xpk/blob/main/README.md)
  * **Single-host Cloud TPU using JAX** : [Run a calculation on a Cloud TPU VM using JAX](https://docs.cloud.google.com/tpu/docs/run-calculation-jax)
  * **Multi-host Cloud TPU using JAX** : [Run JAX code on TPU slices](https://docs.cloud.google.com/tpu/docs/jax-pods)
  * **Cloud TPU using PyTorch** : [PyTorch on Cloud TPU](https://docs.cloud.google.com/tpu/docs/pytorch-on-tpu)



To set up and run XPK with [MaxText](https://maxtext.readthedocs.io/en/latest/index.html), see [Running MaxText at Scale with XPK ](https://maxtext.readthedocs.io/en/latest/run_maxtext/run_maxtext_via_xpk.html).

## Use SkyPilot

You can use Cloud TPU v6e with [SkyPilot](https://github.com/skypilot-org/skypilot). SkyPilot is an open-source framework that simplifies the process of running, managing, and scaling AI workloads. You can add v6e-related location and pricing information to SkyPilot. For more information, see the [SkyPilot TPU v6e example](https://github.com/skypilot-org/skypilot/tree/master/examples/tpu/v6e).

## Training examples

The following sections provide examples for training MaxText, MaxDiffusion, and PyTorch models on Cloud TPU v6e.

These examples have been tested with the following software versions:

  * Python `3.10` or later
  * Nightly software versions: 
    * Nightly JAX `0.4.32.dev20240912`
    * Nightly LibTPU `0.1.dev20240912+nightly`
  * Stable software versions: 
    * JAX + JAX Lib of v0.4.37



### Train MaxText and MaxDiffusion on Cloud TPU v6e

The following sections cover the training lifecycle of the [MaxText](https://github.com/AI-Hypercomputer/maxtext) and [MaxDiffusion](https://github.com/AI-Hypercomputer/maxdiffusion) models.

In general, the high-level steps are:

  1. Build the workload base image.
  2. Run your workload using XPK. 
     1. Build the training command for the workload.
     2. Deploy the workload.
  3. Follow the workload and view metrics.
  4. Delete the XPK workload if it isn't needed.
  5. Delete the cluster when it's no longer needed.



#### Build base image

Install MaxText or MaxDiffusion and build the Docker image:

  1. Clone the repository you want to use and change to the directory for the repository:

MaxText:
         
         git clone https://github.com/google/maxtext.git
         cd maxtext
         git checkout maxtext-v0.2.0
         

MaxDiffusion:
         
         git clone https://github.com/google/maxdiffusion.git && cd maxdiffusion && git checkout 4a8155ec0129512812b31930f0a91c6d5a141103
         

  2. Configure Docker to use the Google Cloud CLI:
         
         gcloud auth configure-docker
         

  3. Build the Docker image using the following command or using a JAX AI image. For more information about JAX AI images, see [JAX AI images](https://docs.cloud.google.com/ai-hypercomputer/docs/images#jax_ai_images).

MaxText:
         
         bash dependencies/scripts/docker_build_dependency_image.sh MODE=stable
         

MaxDiffusion:
         
         bash .github/workflows/build_and_upload_images.sh CLOUD_IMAGE_NAME=maxdiffusion_jax_stable_stack MODE=jax_ai_image PROJECT=${PROJECT_ID} LOCAL_IMAGE_NAME=maxdiffusion_jax_stable_stack BASEIMAGE=us-docker.pkg.dev/cloud-tpu-images/jax-ai-image/tpu:latest
         

  4. Set your project ID in your active gcloud CLI configuration:
         
         gcloud config set project ${PROJECT_ID}
         

  5. If you're launching the workload from a machine that doesn't have the image built locally, upload the image.

**Note:** Make sure you are using bash version 4.2 or newer.
     1. Set the `CLOUD_IMAGE_NAME` environment variable:
            
            export CLOUD_IMAGE_NAME=${USER}_runner
            

     2. Upload the image:
            
            bash dependencies/scripts/docker_upload_runner.sh ${CLOUD_IMAGE_NAME}
            




#### Run your workload using XPK

  1. Set the following environment variables if you're not using the [default values set by MaxText](https://github.com/AI-Hypercomputer/maxtext/blob/maxtext-v0.2.0/src/maxtext/configs/base.yml) or [MaxDiffusion](https://github.com/AI-Hypercomputer/maxdiffusion/blob/main/src/maxdiffusion/configs/base_2_base.yml):
         
         export BASE_OUTPUT_DIR=gs://YOUR_BUCKET
         export PER_DEVICE_BATCH_SIZE=2
         export NUM_STEPS=30
         export MAX_TARGET_LENGTH=8192

  2. Build your model script. This script will be copied as a training command in a later step.

Don't execute the model script yet.

**Note:** Autocheckpointing is not enabled. If you see errors like, `Could not find a known environment for initializing distributed JAX`, use `JAX_FORCE_TPU_INIT=true`.

### MaxText

[MaxText](https://github.com/AI-Hypercomputer/maxtext/tree/main) is a high performance, highly scalable, open-source LLM written in pure Python and JAX and targeting Google Cloud TPUs and GPUs for training and inference.
         
         JAX_PLATFORMS=tpu,cpu \
         ENABLE_PJRT_COMPATIBILITY=true \
         TPU_SLICE_BUILDER_DUMP_CHIP_FORCE=true \
         TPU_SLICE_BUILDER_DUMP_ICI=true && \
         python3 -m maxtext.trainers.pre_train.train src/maxtext/configs/base.yml \
              base_output_directory=${BASE_OUTPUT_DIR} \
              dataset_type=synthetic \
              per_device_batch_size=${PER_DEVICE_BATCH_SIZE} \
              enable_checkpointing=false \
              gcs_metrics=true \
              profiler=xplane \
              skip_first_n_steps_for_profiler=5 \
              steps=${NUM_STEPS}  # attention='dot_product'"
         

### Gemma2

[Gemma](https://ai.google.dev/gemma) is a family of open-weights LLMs developed by Google DeepMind, based on Gemini research and technology.

**Note:** To run this model, you must provision a TPU that is v6e-256 or larger.
         
         python3 -m maxtext.trainers.pre_train.train src/maxtext/configs/base.yml \
             model_name=gemma2-27b \
             run_name=gemma2-27b-run \
             base_output_directory=${BASE_OUTPUT_DIR} \
             max_target_length=${MAX_TARGET_LENGTH} \
             per_device_batch_size=${PER_DEVICE_BATCH_SIZE} \
             steps=${NUM_STEPS} \
             enable_checkpointing=false \
             use_iota_embed=true \
             gcs_metrics=true \
             dataset_type=synthetic \
             profiler=xplane \
             attention=flash
         

### Mixtral 8x7b

[Mixtral](https://mistral.ai/news/mixtral-of-experts/) is a state-of-the-art AI model developed by Mistral AI, utilizing a sparse mixture-of-experts (MoE) architecture.

**Note:** To run this model, you must provision a TPU that is v6e-256 or larger.
         
         python3 -m maxtext.trainers.pre_train.train src/maxtext/configs/base.yml \
             base_output_directory=${BASE_OUTPUT_DIR} \
             per_device_batch_size=${PER_DEVICE_BATCH_SIZE} \
             model_name=mixtral-8x7b \
             steps=${NUM_STEPS} \
             max_target_length=${MAX_TARGET_LENGTH} \
             tokenizer_path=assets/tokenizer.mistral-v1 \
             attention=flash \
             dtype=bfloat16 \
             dataset_type=synthetic \
             profiler=xplane
         

### MaxDiffusion

[MaxDiffusion](https://github.com/AI-Hypercomputer/maxdiffusion) is a collection of reference implementations of various latent diffusion models written in pure Python and JAX that run on XLA devices including Cloud TPUs and GPUs. Stable Diffusion is a latent text-to-image model that generates photo-realistic images from any text input.

You need to install a specific Git branch to run MaxDiffusion as shown in the following training script.
         
         git clone https://github.com/google/maxdiffusion.git
         && cd maxdiffusion
         && git checkout 4a8155ec0129512812b31930f0a91c6d5a141103
         && pip install -r requirements.txt && pip install .
         && pip install huggingface_hub==0.30.2 && OUT_DIR=${BASE_OUTPUT_DIR}
         && python src/maxdiffusion/train_sdxl.py \
             src/maxdiffusion/configs/base_xl.yml \
             revision=refs/pr/95 \
             activations_dtype=bfloat16 \
             weights_dtype=bfloat16 \
             resolution=1024 \
             per_device_batch_size=1 \
             output_dir=${OUT_DIR} \
             jax_cache_dir=${OUT_DIR}/cache_dir/ \
             max_train_steps=200 \
             attention=flash \
             run_name=sdxl-ddp-v6e
         

**Note:** Optionally, set the `dcn_data_parallelism` for Multislice runs.

  3. Export the following variables:
         
         export CLUSTER_NAME=CLUSTER_NAME
         export ACCELERATOR_TYPE=ACCELERATOR_TYPE
         export NUM_SLICES=NUM_SLICES
         export YOUR_MODEL_SCRIPT=YOUR_MODEL_SCRIPT

#### Environment variable descriptions

     * `CLUSTER_NAME`: The name of your cluster.
     * `ACCELERATOR_TYPE`: The accelerator type specifies the version and size of the Cloud TPU you want to create. For more information about supported accelerator types for each TPU version, see [TPU versions](https://docs.cloud.google.com/tpu/docs/system-architecture-tpu-vm#versions).
     * `NUM_SLICES`: The number of TPU slices.
     * `YOUR_MODEL_SCRIPT`: The model script to execute as a training command.
  4. Run the model using the script you created in the previous step. You must either specify the `--base-docker-image` flag to use the MaxText base image or specify the `--docker-image` flag and the image you want to use.

You can choose to add the following optional flags:

     * You can enable debug logging by including the `--enable-debug-logs` flag. For more information, see Debug JAX on MaxText.
     * You can create a Vertex AI Experiment to upload data to Vertex AI TensorBoard by including the `--use-vertex-tensorboard` flag. For more information, see Monitor JAX on MaxText using Vertex AI.
    
    xpk workload create \
      --cluster ${CLUSTER_NAME} \
      {--base-docker-image maxtext_base_image | --docker-image gcr.io/${PROJECT_ID}/${CLOUD_IMAGE_NAME}:latest} \
      --workload=${USER}-xpk-${ACCELERATOR_TYPE}-${NUM_SLICES} \
      --tpu-type=${ACCELERATOR_TYPE} \
      --num-slices=${NUM_SLICES}  \
      --on-demand \
      --zone=${ZONE} \
      --project=${PROJECT_ID} \
      --command="${YOUR_MODEL_SCRIPT}"

The output includes a link to follow your workload. Open the link and click the **Logs** tab to track your workload in real time.




#### Debug JAX on MaxText

Use supplemental XPK commands to diagnose why the cluster or workload isn't running:

  * [XPK workload list](https://github.com/AI-Hypercomputer/xpk?tab=readme-ov-file#workload-list)
  * [XPK inspector](https://github.com/google/xpk?tab=readme-ov-file#inspector)
  * Enable verbose logging in your workload logs using the `--enable-debug-logs` flag when you create the XPK workload



#### Monitor JAX on MaxText using Vertex AI

To use TensorBoard, your Google Cloud user account must have the `aiplatform.user` role. Run the following command to grant this role:
    
    
    gcloud projects add-iam-policy-binding your-project-id \
       --member='user:your-email' \
       --role='roles/aiplatform.user'

View scalar and profile data through the Vertex AI managed TensorBoard.

  1. Increase resource management (CRUD) requests for the zone you're using from 600 to 5000. This might not be an issue for small workloads using less than 16 VMs.

  2. Install dependencies such as `cloud-accelerator-diagnostics` for Vertex AI:
         
         # xpk dependencies will install cloud-accelerator-diagnostics for Vertex AI
         cd ~/xpk
         pip install .

  3. Create your cluster using the `--create-vertex-tensorboard` flag, as documented in [Create Vertex AI TensorBoard](https://github.com/google/xpk/tree/main?tab=readme-ov-file#create-vertex-ai-tensorboard). You can also run this command on existing clusters.

  4. Create your Vertex AI experiment when running your XPK workload using the `--use-vertex-tensorboard` flag and the optional `--experiment-name` flag. For the full list of steps, see [Create Vertex AI Experiment to upload data to Vertex AI TensorBoard](https://github.com/google/xpk/tree/main?tab=readme-ov-file#create-vertex-ai-experiment-to-upload-data-to-vertex-ai-tensorboard).


**Note:** If you're running a non-MaxText workload, use this [MaxText example](https://github.com/google/maxtext/pull/570) to make the corresponding data upload changes.

The logs include a link to a Vertex AI TensorBoard, similar to the following:
    
    
    View your TensorBoard at https://us-central1.tensorboard.googleusercontent.com/experiment/project_id+locations+us-central1+tensorboards+hash+experiments+name

You can also find the Vertex AI TensorBoard link in the Google Cloud console. Go to [Vertex AI Experiments](https://console.cloud.google.com/vertex-ai/experiments) in the Google Cloud console. Select the appropriate region from the drop-down.

The TensorBoard directory is also written to the Cloud Storage bucket that you specified with `${BASE_OUTPUT_DIR}`.

#### Delete your XPK workload

Use the [`xpk workload delete` command](https://github.com/google/xpk?tab=readme-ov-file#workload-delete) to delete one or more workloads based on the job prefix or job status. This command might be useful if you sent XPK workloads that no longer need to be run, or if you have jobs that are stuck in the queue.

#### Delete your cluster

Use the [`xpk cluster delete` command](https://github.com/google/xpk?tab=readme-ov-file#cluster-delete) to delete your cluster:
    
    
    xpk cluster delete --cluster ${CLUSTER_NAME} \
        --zone=${ZONE} --project=${PROJECT_ID}

#### MaxDiffusion benchmarking results

We ran the training script for MaxDiffusion on a v6e-4, a v6e-16, and two v6e-16. The following table shows the measured throughputs.

| v6e-4  | v6e-16  | Two v6e-16   
---|---|---|---  
Training steps  | 0.069  | 0.073  | 0.13   
Global batch size  | 8  | 32  | 64   
Throughput (examples/sec)  | 115.9  | 438.4  | 492.3   
  
### Train a model using PyTorch on Cloud TPU

You can use [TorchTPU](https://torchtpu.readthedocs.io/en/latest/) directly to train your model or reuse the [TorchTitan](https://github.com/google-pytorch/torchtitan) reference library. To get started with v6e workloads, see [Get started with TorchTPU on a TPU VM](https://torchtpu.readthedocs.io/en/latest/get_started_on_a_vm/) and the [TorchTitan Trillium recipes](https://github.com/google-pytorch/torchtitan/tree/main/torchtitan/experiments/tpu/recipes/trillium). For more information about the PyTorch ecosystem on Cloud TPU, see [PyTorch on Cloud TPU](https://docs.cloud.google.com/tpu/docs/pytorch-on-tpu).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
