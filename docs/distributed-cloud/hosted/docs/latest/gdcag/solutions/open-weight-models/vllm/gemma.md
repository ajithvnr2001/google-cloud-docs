---
url: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/solutions/open-weight-models/vllm/gemma/
title: Gemma models with vLLM user guide on GDC air-gapped \u00a0|\u00a0 Google Distributed Cloud air-gapped \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T10:20:14.991048+00:00
---

# Gemma models with vLLM user guide on GDC air-gapped  |  Google Distributed Cloud air-gapped  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/solutions/open-weight-models/vllm/gemma/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Distributed, hybrid, and multicloud ](https://docs.cloud.google.com/docs/dhm-cloud)
  * [ Google Distributed Cloud ](https://docs.cloud.google.com/distributed-cloud/docs)
  * [ Air-gapped ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdch)
  * [ 1.16.2 (Latest) ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag)



Send feedback 

#  Gemma models with vLLM user guide on GDC air-gapped Stay organized with collections  Save and categorize content based on your preferences. 

This document provides step-by-step instructions for deploying open weight models from Google DeepMind, specifically the Gemma 4 family, on Google Distributed Cloud (GDC) air-gapped environments. It covers using vLLM for high-throughput serving, using the GDC platform's capabilities, including Kubernetes, Harbor, and GPU resources. Select the model and the GPU option in the Model section; every other step is the same for all models.

## Supported models

Model | Hugging Face repository | Parameters | License | GPU options  
---|---|---|---|---  
Gemma 4 E2B Instruct | [`google/gemma-4-E2B-it`](https://huggingface.co/google/gemma-4-E2B-it) | 5.1B (2B effective) | [Gemma Terms of Use](https://ai.google.dev/gemma/terms) | 1 x any GPU  
Gemma 4 E4B Instruct | [`google/gemma-4-E4B-it`](https://huggingface.co/google/gemma-4-E4B-it) | 8.0B (4B effective) | [Gemma Terms of Use](https://ai.google.dev/gemma/terms) | 1 x any GPU  
Gemma 4 12B Instruct | [`google/gemma-4-12B-it`](https://huggingface.co/google/gemma-4-12B-it) | 12B (dense) | [Gemma Terms of Use](https://ai.google.dev/gemma/terms) | 1 x any GPU  
Gemma 4 26B-A4B Instruct | [`google/gemma-4-26B-A4B-it`](https://huggingface.co/google/gemma-4-26B-A4B-it) | 25.8B total / 4B active (mixture of experts) | [Gemma Terms of Use](https://ai.google.dev/gemma/terms) | 1 x NVIDIA A100 80 GB  
1 x NVIDIA H100 94 GB  
1 x NVIDIA H200 141 GB or B300 288 GB  
Gemma 4 31B Instruct | [`google/gemma-4-31B-it`](https://huggingface.co/google/gemma-4-31B-it) | 31.3B (dense) | [Gemma Terms of Use](https://ai.google.dev/gemma/terms) | 1 x NVIDIA A100 80 GB  
1 x NVIDIA H100 94 GB  
1 x NVIDIA H200 141 GB or B300 288 GB  
**Note:** For gated Hugging Face repositories, you must accept the license terms on the model's Hugging Face repository page with the account whose access token is configured in `${HOME}/gdcag-solutions/open-weight-models/vllm/secrets/huggingface_token` before downloading the weights.

## Architecture

The solution involves deploying a containerized serving backend (vLLM) as a Deployment within a standard cluster. Model weights are stored on Persistent Volumes, populated from files downloaded locally and uploaded using a loader pod. A Kubernetes `Service` of type `LoadBalancer` exposes the backend API, and `NetworkPolicy` / `ProjectNetworkPolicy` objects secure access to it.

**Note:** Without a ReadOnlyMany StorageClass, this solution can deploy only one replica.

## Before you begin

**Note:** This guide requires GDC air-gapped 1.16.2-hf1 (1.16.2-gdch.1353-1) or later, and a standard cluster.

Complete the [Open Weight Models with vLLM reference implementation](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/solutions/open-weight-models/vllm/reference-implementation) on the workstation, and make sure you have access to the `${HOME}/gdcag-solutions` directory.

### Identity and Access Management

Ensure that the necessary IAM accounts, roles, and permissions are properly configured.

**GDC User** roles on **organization** :

  * Optional: Standard Cluster Admin (View clusters from the console)



**GDC User** roles on **project** :

  * Standard Cluster Admin (`standard-cluster-admin`)



**GDC User** role on the **standard cluster** :

  * `StandardClusterRoleBinding` to the `StandardClusterRole` `cluster-admin` (created by a Project IAM Admin, see the _Identity and Access Management_ section of the reference implementation)



### Workstation

Run all commands in this guide from a workstation with the required tools and connectivity to the environment and internet, unless a step states otherwise.

The environment configuration is layered:

  * `${HOME}/gdcag-solutions/env.sh` loads the platform and registry settings.
  * `${HOME}/gdcag-solutions/open-weight-models/vllm/env.sh` adds the vLLM settings.

  * This user guide adds `env.d/model.sh` (the model) and `env.d/accelerator.sh` (the GPU option and runtime settings), which you write in the Model section; and `env.d/model-common.sh` (the values derived from them).



  1. Create the user guide directory structure:
         
         mkdir -p ${HOME}/gdcag-solutions/open-weight-models/vllm/gemma/env.d
         

  2. Create the common model environment configuration file. It derives every path and resource name from `GDCS_HF_MODEL`, so it is the same for all models:
         
         cat << 'EOF' > ${HOME}/gdcag-solutions/open-weight-models/vllm/gemma/env.d/model-common.sh && echo "Successfully created." || echo "Failed to create!"
         # Model (derived from env.d/model.sh)
         export GDCS_HF_DOWNLOAD_PATH="${GDCS_USER_GUIDE_HOME}/hf-models"
         export GDCS_HF_MODEL_LOWERCASE="${GDCS_HF_MODEL,,}"
         export GDCS_HF_MODEL_DOWNLOAD_DIR="${GDCS_HF_DOWNLOAD_PATH}/${GDCS_HF_MODEL_LOWERCASE}"
         export GDCS_HF_PV_MOUNT_PATH="/mnt/hf-model"
         
         GDCS_HF_MODEL_KUBERNETES="${GDCS_HF_MODEL_LOWERCASE//\//-}"
         export GDCS_HF_MODEL_KUBERNETES="${GDCS_HF_MODEL_KUBERNETES//./-}"
         
         # Workload
         export GDCS_WORKLOAD_NAMESPACE="vllm-gemma"
         export GDCS_WORKLOAD_NAME="${GDCS_HF_MODEL_KUBERNETES}"
         export GDCS_MODEL_LOADER_POD_NAME="loader-${GDCS_HF_MODEL_KUBERNETES}"
         EOF
         

  3. Create the user guide environment loader file:
         
         cat << 'EOF' > ${HOME}/gdcag-solutions/open-weight-models/vllm/gemma/env.sh && echo "Successfully created." || echo "Failed to create!"
         source "${HOME}/gdcag-solutions/open-weight-models/vllm/env.sh"
         
         export GDCS_USER_GUIDE_HOME="${HOME}/gdcag-solutions/open-weight-models/vllm/gemma"
         echo "GDCS_USER_GUIDE_HOME=${GDCS_USER_GUIDE_HOME}"
         
         # Sourced in dependency order: the model selection, the accelerator and runtime settings, then the values derived from them
         source "${GDCS_USER_GUIDE_HOME}/env.d/model.sh"
         source "${GDCS_USER_GUIDE_HOME}/env.d/accelerator.sh"
         source "${GDCS_USER_GUIDE_HOME}/env.d/model-common.sh"
         echo "GDCS_HF_MODEL=${GDCS_HF_MODEL} (${GDCS_WORKLOAD_ACCELERATOR_COUNT} x ${GDCS_WORKLOAD_ACCELERATOR_TYPE:-unset})"
         EOF
         




### Model

Select the model and the GPU option that matches the GPU nodes of your standard cluster. GDC air-gapped offers the following GPUs (see [Cluster node machine types](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform/pa-user/cluster-node-machines)); the accelerator resource type is the name under which the nodes expose the GPU to Kubernetes.

GPU | Memory | Machine types | Accelerator resource type  
---|---|---|---  
NVIDIA A100 | 40 GB | `a2-highgpu-1g-gdc` | `nvidia.com/gpu-pod-NVIDIA_A100_PCIE_40GB`  
NVIDIA A100 | 80 GB | `a2-ultragpu-1g-gdc`, `a2-ultragpu-2g-gdc` | `nvidia.com/gpu-pod-NVIDIA_A100_80GB_PCIE`  
NVIDIA H100 | 94 GB | `a3-highgpu-1g-gdc` (Preview), `a3-highgpu-2g-gdc` (Preview), `a3-highgpu-4g-gdc` | `nvidia.com/gpu-pod-NVIDIA_H100_NVL`  
NVIDIA H200 | 141 GB | `a3-ultragpu-8g-gdc` | `nvidia.com/gpu-pod-NVIDIA_H200`  
NVIDIA B300 | 288 GB | `a4-ultragpu-8g-gdc` | `nvidia.com/gpu-pod-NVIDIA_B300_SXM6_AC`  
  
Each tab lists the model facts, the command that writes the model environment file `env.d/model.sh`, and nested tabs that write the accelerator environment file `env.d/accelerator.sh` for your chosen GPU option with pre-filled resource types and vLLM settings. To switch models or GPU options later, write different environment files, source the environment again, and repeat the Implementation section; the workloads of several models can run side by side in the same namespace because every resource name is derived from the model name.

  1. Create the model and accelerator environment files for the model and GPU option you want to deploy.

### Gemma 4 E2B Instruct

Attribute | Value  
---|---  
**Hugging Face repository** | [`google/gemma-4-E2B-it`](https://huggingface.co/google/gemma-4-E2B-it)  
**Parameters** | 5.1B (2B effective)  
**License** | [Gemma Terms of Use](https://ai.google.dev/gemma/terms)  
**Weights used by vLLM** | Hugging Face format (`model-*.safetensors`), about 10.2 GB  
**Context length** | 128k tokens; this guide serves `--max-model-len 32768`  
  
Create the model environment file:
         
         cat << 'EOF' > ${HOME}/gdcag-solutions/open-weight-models/vllm/gemma/env.d/model.sh && echo "Successfully created." || echo "Failed to create!"
         # Model: Gemma 4 E2B Instruct
         export GDCS_HF_MODEL="google/gemma-4-E2B-it"
         export GDCS_HF_MODEL_REVISION="main"  # Hugging Face branch, tag, or commit to download
         export GDCS_HF_DOWNLOAD_EXCLUDE=""
         EOF
         

Create the accelerator environment file for your GPU option:

### NVIDIA A100 40 GB
         
         cat << 'EOF' > ${HOME}/gdcag-solutions/open-weight-models/vllm/gemma/env.d/accelerator.sh && echo "Successfully created." || echo "Failed to create!"
         # Accelerator: NVIDIA A100 40 GB
         export GDCS_WORKLOAD_ACCELERATOR_TYPE="nvidia.com/gpu-pod-NVIDIA_A100_PCIE_40GB"
         export GDCS_WORKLOAD_ACCELERATOR_COUNT="1"
         
         # vLLM
         export GDCS_VLLM_MAX_MODEL_LEN="32768"
         export GDCS_VLLM_EXTRA_ARGS=""
         export GDCS_VLLM_STARTUP_FAILURE_THRESHOLD="60"
         export GDCS_VLLM_TEST_MAX_TOKENS="128"
         EOF
         

### NVIDIA A100 80 GB
         
         cat << 'EOF' > ${HOME}/gdcag-solutions/open-weight-models/vllm/gemma/env.d/accelerator.sh && echo "Successfully created." || echo "Failed to create!"
         # Accelerator: NVIDIA A100 80 GB
         export GDCS_WORKLOAD_ACCELERATOR_TYPE="nvidia.com/gpu-pod-NVIDIA_A100_80GB_PCIE"
         export GDCS_WORKLOAD_ACCELERATOR_COUNT="1"
         
         # vLLM
         export GDCS_VLLM_MAX_MODEL_LEN="32768"
         export GDCS_VLLM_EXTRA_ARGS=""
         export GDCS_VLLM_STARTUP_FAILURE_THRESHOLD="60"
         export GDCS_VLLM_TEST_MAX_TOKENS="128"
         EOF
         

### NVIDIA H100 94 GB
         
         cat << 'EOF' > ${HOME}/gdcag-solutions/open-weight-models/vllm/gemma/env.d/accelerator.sh && echo "Successfully created." || echo "Failed to create!"
         # Accelerator: NVIDIA H100 94 GB
         export GDCS_WORKLOAD_ACCELERATOR_TYPE="nvidia.com/gpu-pod-NVIDIA_H100_NVL"
         export GDCS_WORKLOAD_ACCELERATOR_COUNT="1"
         
         # vLLM
         export GDCS_VLLM_MAX_MODEL_LEN="32768"
         export GDCS_VLLM_EXTRA_ARGS=""
         export GDCS_VLLM_STARTUP_FAILURE_THRESHOLD="60"
         export GDCS_VLLM_TEST_MAX_TOKENS="128"
         EOF
         

### NVIDIA H200 141 GB
         
         cat << 'EOF' > ${HOME}/gdcag-solutions/open-weight-models/vllm/gemma/env.d/accelerator.sh && echo "Successfully created." || echo "Failed to create!"
         # Accelerator: NVIDIA H200 141 GB
         export GDCS_WORKLOAD_ACCELERATOR_TYPE="nvidia.com/gpu-pod-NVIDIA_H200"
         export GDCS_WORKLOAD_ACCELERATOR_COUNT="1"
         
         # vLLM
         export GDCS_VLLM_MAX_MODEL_LEN="32768"
         export GDCS_VLLM_EXTRA_ARGS=""
         export GDCS_VLLM_STARTUP_FAILURE_THRESHOLD="60"
         export GDCS_VLLM_TEST_MAX_TOKENS="128"
         EOF
         

### NVIDIA B300 288 GB
         
         cat << 'EOF' > ${HOME}/gdcag-solutions/open-weight-models/vllm/gemma/env.d/accelerator.sh && echo "Successfully created." || echo "Failed to create!"
         # Accelerator: NVIDIA B300 288 GB
         export GDCS_WORKLOAD_ACCELERATOR_TYPE="nvidia.com/gpu-pod-NVIDIA_B300_SXM6_AC"
         export GDCS_WORKLOAD_ACCELERATOR_COUNT="1"
         
         # vLLM
         export GDCS_VLLM_MAX_MODEL_LEN="32768"
         export GDCS_VLLM_EXTRA_ARGS=""
         export GDCS_VLLM_STARTUP_FAILURE_THRESHOLD="60"
         export GDCS_VLLM_TEST_MAX_TOKENS="128"
         EOF
         

### Gemma 4 E4B Instruct

Attribute | Value  
---|---  
**Hugging Face repository** | [`google/gemma-4-E4B-it`](https://huggingface.co/google/gemma-4-E4B-it)  
**Parameters** | 8.0B (4B effective)  
**License** | [Gemma Terms of Use](https://ai.google.dev/gemma/terms)  
**Weights used by vLLM** | Hugging Face format (`model-*.safetensors`), about 16.0 GB  
**Context length** | 128k tokens; this guide serves `--max-model-len 32768`  
  
Create the model environment file:
         
         cat << 'EOF' > ${HOME}/gdcag-solutions/open-weight-models/vllm/gemma/env.d/model.sh && echo "Successfully created." || echo "Failed to create!"
         # Model: Gemma 4 E4B Instruct
         export GDCS_HF_MODEL="google/gemma-4-E4B-it"
         export GDCS_HF_MODEL_REVISION="main"  # Hugging Face branch, tag, or commit to download
         export GDCS_HF_DOWNLOAD_EXCLUDE=""
         EOF
         

Create the accelerator environment file for your GPU option:

### NVIDIA A100 40 GB
         
         cat << 'EOF' > ${HOME}/gdcag-solutions/open-weight-models/vllm/gemma/env.d/accelerator.sh && echo "Successfully created." || echo "Failed to create!"
         # Accelerator: NVIDIA A100 40 GB
         export GDCS_WORKLOAD_ACCELERATOR_TYPE="nvidia.com/gpu-pod-NVIDIA_A100_PCIE_40GB"
         export GDCS_WORKLOAD_ACCELERATOR_COUNT="1"
         
         # vLLM
         export GDCS_VLLM_MAX_MODEL_LEN="32768"
         export GDCS_VLLM_EXTRA_ARGS=""
         export GDCS_VLLM_STARTUP_FAILURE_THRESHOLD="120"
         export GDCS_VLLM_TEST_MAX_TOKENS="128"
         EOF
         

### NVIDIA A100 80 GB
         
         cat << 'EOF' > ${HOME}/gdcag-solutions/open-weight-models/vllm/gemma/env.d/accelerator.sh && echo "Successfully created." || echo "Failed to create!"
         # Accelerator: NVIDIA A100 80 GB
         export GDCS_WORKLOAD_ACCELERATOR_TYPE="nvidia.com/gpu-pod-NVIDIA_A100_80GB_PCIE"
         export GDCS_WORKLOAD_ACCELERATOR_COUNT="1"
         
         # vLLM
         export GDCS_VLLM_MAX_MODEL_LEN="32768"
         export GDCS_VLLM_EXTRA_ARGS=""
         export GDCS_VLLM_STARTUP_FAILURE_THRESHOLD="120"
         export GDCS_VLLM_TEST_MAX_TOKENS="128"
         EOF
         

### NVIDIA H100 94 GB
         
         cat << 'EOF' > ${HOME}/gdcag-solutions/open-weight-models/vllm/gemma/env.d/accelerator.sh && echo "Successfully created." || echo "Failed to create!"
         # Accelerator: NVIDIA H100 94 GB
         export GDCS_WORKLOAD_ACCELERATOR_TYPE="nvidia.com/gpu-pod-NVIDIA_H100_NVL"
         export GDCS_WORKLOAD_ACCELERATOR_COUNT="1"
         
         # vLLM
         export GDCS_VLLM_MAX_MODEL_LEN="32768"
         export GDCS_VLLM_EXTRA_ARGS=""
         export GDCS_VLLM_STARTUP_FAILURE_THRESHOLD="120"
         export GDCS_VLLM_TEST_MAX_TOKENS="128"
         EOF
         

### NVIDIA H200 141 GB
         
         cat << 'EOF' > ${HOME}/gdcag-solutions/open-weight-models/vllm/gemma/env.d/accelerator.sh && echo "Successfully created." || echo "Failed to create!"
         # Accelerator: NVIDIA H200 141 GB
         export GDCS_WORKLOAD_ACCELERATOR_TYPE="nvidia.com/gpu-pod-NVIDIA_H200"
         export GDCS_WORKLOAD_ACCELERATOR_COUNT="1"
         
         # vLLM
         export GDCS_VLLM_MAX_MODEL_LEN="32768"
         export GDCS_VLLM_EXTRA_ARGS=""
         export GDCS_VLLM_STARTUP_FAILURE_THRESHOLD="120"
         export GDCS_VLLM_TEST_MAX_TOKENS="128"
         EOF
         

### NVIDIA B300 288 GB
         
         cat << 'EOF' > ${HOME}/gdcag-solutions/open-weight-models/vllm/gemma/env.d/accelerator.sh && echo "Successfully created." || echo "Failed to create!"
         # Accelerator: NVIDIA B300 288 GB
         export GDCS_WORKLOAD_ACCELERATOR_TYPE="nvidia.com/gpu-pod-NVIDIA_B300_SXM6_AC"
         export GDCS_WORKLOAD_ACCELERATOR_COUNT="1"
         
         # vLLM
         export GDCS_VLLM_MAX_MODEL_LEN="32768"
         export GDCS_VLLM_EXTRA_ARGS=""
         export GDCS_VLLM_STARTUP_FAILURE_THRESHOLD="120"
         export GDCS_VLLM_TEST_MAX_TOKENS="128"
         EOF
         

### Gemma 4 12B Instruct

Attribute | Value  
---|---  
**Hugging Face repository** | [`google/gemma-4-12B-it`](https://huggingface.co/google/gemma-4-12B-it)  
**Parameters** | 12B (dense)  
**License** | [Gemma Terms of Use](https://ai.google.dev/gemma/terms)  
**Weights used by vLLM** | Hugging Face format (`model-*.safetensors`), about 23.9 GB  
**Context length** | 256k tokens; this guide serves `--max-model-len 32768`  
  
Create the model environment file:
         
         cat << 'EOF' > ${HOME}/gdcag-solutions/open-weight-models/vllm/gemma/env.d/model.sh && echo "Successfully created." || echo "Failed to create!"
         # Model: Gemma 4 12B Instruct
         export GDCS_HF_MODEL="google/gemma-4-12B-it"
         export GDCS_HF_MODEL_REVISION="main"  # Hugging Face branch, tag, or commit to download
         export GDCS_HF_DOWNLOAD_EXCLUDE=""
         EOF
         

Create the accelerator environment file for your GPU option:

### NVIDIA A100 40 GB
         
         cat << 'EOF' > ${HOME}/gdcag-solutions/open-weight-models/vllm/gemma/env.d/accelerator.sh && echo "Successfully created." || echo "Failed to create!"
         # Accelerator: NVIDIA A100 40 GB
         export GDCS_WORKLOAD_ACCELERATOR_TYPE="nvidia.com/gpu-pod-NVIDIA_A100_PCIE_40GB"
         export GDCS_WORKLOAD_ACCELERATOR_COUNT="1"
         
         # vLLM
         export GDCS_VLLM_MAX_MODEL_LEN="32768"
         export GDCS_VLLM_EXTRA_ARGS=""
         export GDCS_VLLM_STARTUP_FAILURE_THRESHOLD="180"
         export GDCS_VLLM_TEST_MAX_TOKENS="128"
         EOF
         

### NVIDIA A100 80 GB
         
         cat << 'EOF' > ${HOME}/gdcag-solutions/open-weight-models/vllm/gemma/env.d/accelerator.sh && echo "Successfully created." || echo "Failed to create!"
         # Accelerator: NVIDIA A100 80 GB
         export GDCS_WORKLOAD_ACCELERATOR_TYPE="nvidia.com/gpu-pod-NVIDIA_A100_80GB_PCIE"
         export GDCS_WORKLOAD_ACCELERATOR_COUNT="1"
         
         # vLLM
         export GDCS_VLLM_MAX_MODEL_LEN="32768"
         export GDCS_VLLM_EXTRA_ARGS=""
         export GDCS_VLLM_STARTUP_FAILURE_THRESHOLD="180"
         export GDCS_VLLM_TEST_MAX_TOKENS="128"
         EOF
         

### NVIDIA H100 94 GB
         
         cat << 'EOF' > ${HOME}/gdcag-solutions/open-weight-models/vllm/gemma/env.d/accelerator.sh && echo "Successfully created." || echo "Failed to create!"
         # Accelerator: NVIDIA H100 94 GB
         export GDCS_WORKLOAD_ACCELERATOR_TYPE="nvidia.com/gpu-pod-NVIDIA_H100_NVL"
         export GDCS_WORKLOAD_ACCELERATOR_COUNT="1"
         
         # vLLM
         export GDCS_VLLM_MAX_MODEL_LEN="32768"
         export GDCS_VLLM_EXTRA_ARGS=""
         export GDCS_VLLM_STARTUP_FAILURE_THRESHOLD="180"
         export GDCS_VLLM_TEST_MAX_TOKENS="128"
         EOF
         

### NVIDIA H200 141 GB
         
         cat << 'EOF' > ${HOME}/gdcag-solutions/open-weight-models/vllm/gemma/env.d/accelerator.sh && echo "Successfully created." || echo "Failed to create!"
         # Accelerator: NVIDIA H200 141 GB
         export GDCS_WORKLOAD_ACCELERATOR_TYPE="nvidia.com/gpu-pod-NVIDIA_H200"
         export GDCS_WORKLOAD_ACCELERATOR_COUNT="1"
         
         # vLLM
         export GDCS_VLLM_MAX_MODEL_LEN="32768"
         export GDCS_VLLM_EXTRA_ARGS=""
         export GDCS_VLLM_STARTUP_FAILURE_THRESHOLD="180"
         export GDCS_VLLM_TEST_MAX_TOKENS="128"
         EOF
         

### NVIDIA B300 288 GB
         
         cat << 'EOF' > ${HOME}/gdcag-solutions/open-weight-models/vllm/gemma/env.d/accelerator.sh && echo "Successfully created." || echo "Failed to create!"
         # Accelerator: NVIDIA B300 288 GB
         export GDCS_WORKLOAD_ACCELERATOR_TYPE="nvidia.com/gpu-pod-NVIDIA_B300_SXM6_AC"
         export GDCS_WORKLOAD_ACCELERATOR_COUNT="1"
         
         # vLLM
         export GDCS_VLLM_MAX_MODEL_LEN="32768"
         export GDCS_VLLM_EXTRA_ARGS=""
         export GDCS_VLLM_STARTUP_FAILURE_THRESHOLD="180"
         export GDCS_VLLM_TEST_MAX_TOKENS="128"
         EOF
         

### Gemma 4 26B-A4B Instruct

Attribute | Value  
---|---  
**Hugging Face repository** | [`google/gemma-4-26B-A4B-it`](https://huggingface.co/google/gemma-4-26B-A4B-it)  
**Parameters** | 25.8B total / 4B active (mixture of experts)  
**License** | [Gemma Terms of Use](https://ai.google.dev/gemma/terms)  
**Weights used by vLLM** | Hugging Face format (`model-*.safetensors`), about 51.6 GB  
**Context length** | 256k tokens; this guide serves `--max-model-len 32768`  
  
Create the model environment file:
         
         cat << 'EOF' > ${HOME}/gdcag-solutions/open-weight-models/vllm/gemma/env.d/model.sh && echo "Successfully created." || echo "Failed to create!"
         # Model: Gemma 4 26B-A4B Instruct
         export GDCS_HF_MODEL="google/gemma-4-26B-A4B-it"
         export GDCS_HF_MODEL_REVISION="main"  # Hugging Face branch, tag, or commit to download
         export GDCS_HF_DOWNLOAD_EXCLUDE=""
         EOF
         

Create the accelerator environment file for your GPU option:

### NVIDIA A100 80 GB
         
         cat << 'EOF' > ${HOME}/gdcag-solutions/open-weight-models/vllm/gemma/env.d/accelerator.sh && echo "Successfully created." || echo "Failed to create!"
         # Accelerator: NVIDIA A100 80 GB
         export GDCS_WORKLOAD_ACCELERATOR_TYPE="nvidia.com/gpu-pod-NVIDIA_A100_80GB_PCIE"
         export GDCS_WORKLOAD_ACCELERATOR_COUNT="1"
         
         # vLLM
         export GDCS_VLLM_MAX_MODEL_LEN="32768"
         export GDCS_VLLM_EXTRA_ARGS=""
         export GDCS_VLLM_STARTUP_FAILURE_THRESHOLD="300"
         export GDCS_VLLM_TEST_MAX_TOKENS="128"
         EOF
         

### NVIDIA H100 94 GB
         
         cat << 'EOF' > ${HOME}/gdcag-solutions/open-weight-models/vllm/gemma/env.d/accelerator.sh && echo "Successfully created." || echo "Failed to create!"
         # Accelerator: NVIDIA H100 94 GB
         export GDCS_WORKLOAD_ACCELERATOR_TYPE="nvidia.com/gpu-pod-NVIDIA_H100_NVL"
         export GDCS_WORKLOAD_ACCELERATOR_COUNT="1"
         
         # vLLM
         export GDCS_VLLM_MAX_MODEL_LEN="32768"
         export GDCS_VLLM_EXTRA_ARGS=""
         export GDCS_VLLM_STARTUP_FAILURE_THRESHOLD="300"
         export GDCS_VLLM_TEST_MAX_TOKENS="128"
         EOF
         

### NVIDIA H200 141 GB
         
         cat << 'EOF' > ${HOME}/gdcag-solutions/open-weight-models/vllm/gemma/env.d/accelerator.sh && echo "Successfully created." || echo "Failed to create!"
         # Accelerator: NVIDIA H200 141 GB
         export GDCS_WORKLOAD_ACCELERATOR_TYPE="nvidia.com/gpu-pod-NVIDIA_H200"
         export GDCS_WORKLOAD_ACCELERATOR_COUNT="1"
         
         # vLLM
         export GDCS_VLLM_MAX_MODEL_LEN="32768"
         export GDCS_VLLM_EXTRA_ARGS=""
         export GDCS_VLLM_STARTUP_FAILURE_THRESHOLD="300"
         export GDCS_VLLM_TEST_MAX_TOKENS="128"
         EOF
         

### NVIDIA B300 288 GB
         
         cat << 'EOF' > ${HOME}/gdcag-solutions/open-weight-models/vllm/gemma/env.d/accelerator.sh && echo "Successfully created." || echo "Failed to create!"
         # Accelerator: NVIDIA B300 288 GB
         export GDCS_WORKLOAD_ACCELERATOR_TYPE="nvidia.com/gpu-pod-NVIDIA_B300_SXM6_AC"
         export GDCS_WORKLOAD_ACCELERATOR_COUNT="1"
         
         # vLLM
         export GDCS_VLLM_MAX_MODEL_LEN="32768"
         export GDCS_VLLM_EXTRA_ARGS=""
         export GDCS_VLLM_STARTUP_FAILURE_THRESHOLD="300"
         export GDCS_VLLM_TEST_MAX_TOKENS="128"
         EOF
         

### Gemma 4 31B Instruct

Attribute | Value  
---|---  
**Hugging Face repository** | [`google/gemma-4-31B-it`](https://huggingface.co/google/gemma-4-31B-it)  
**Parameters** | 31.3B (dense)  
**License** | [Gemma Terms of Use](https://ai.google.dev/gemma/terms)  
**Weights used by vLLM** | Hugging Face format (`model-*.safetensors`), about 62.5 GB  
**Context length** | 256k tokens; this guide serves `--max-model-len 32768`  
  
Create the model environment file:
         
         cat << 'EOF' > ${HOME}/gdcag-solutions/open-weight-models/vllm/gemma/env.d/model.sh && echo "Successfully created." || echo "Failed to create!"
         # Model: Gemma 4 31B Instruct
         export GDCS_HF_MODEL="google/gemma-4-31B-it"
         export GDCS_HF_MODEL_REVISION="main"  # Hugging Face branch, tag, or commit to download
         export GDCS_HF_DOWNLOAD_EXCLUDE=""
         EOF
         

Create the accelerator environment file for your GPU option:

### NVIDIA A100 80 GB

Serving on an 80 GB GPU leaves little memory for the KV cache, so this option sets `--max-model-len 16384`.
         
         cat << 'EOF' > ${HOME}/gdcag-solutions/open-weight-models/vllm/gemma/env.d/accelerator.sh && echo "Successfully created." || echo "Failed to create!"
         # Accelerator: NVIDIA A100 80 GB
         export GDCS_WORKLOAD_ACCELERATOR_TYPE="nvidia.com/gpu-pod-NVIDIA_A100_80GB_PCIE"
         export GDCS_WORKLOAD_ACCELERATOR_COUNT="1"
         
         # vLLM
         export GDCS_VLLM_MAX_MODEL_LEN="16384"
         export GDCS_VLLM_EXTRA_ARGS=""
         export GDCS_VLLM_STARTUP_FAILURE_THRESHOLD="360"
         export GDCS_VLLM_TEST_MAX_TOKENS="128"
         EOF
         

### NVIDIA H100 94 GB
         
         cat << 'EOF' > ${HOME}/gdcag-solutions/open-weight-models/vllm/gemma/env.d/accelerator.sh && echo "Successfully created." || echo "Failed to create!"
         # Accelerator: NVIDIA H100 94 GB
         export GDCS_WORKLOAD_ACCELERATOR_TYPE="nvidia.com/gpu-pod-NVIDIA_H100_NVL"
         export GDCS_WORKLOAD_ACCELERATOR_COUNT="1"
         
         # vLLM
         export GDCS_VLLM_MAX_MODEL_LEN="32768"
         export GDCS_VLLM_EXTRA_ARGS=""
         export GDCS_VLLM_STARTUP_FAILURE_THRESHOLD="360"
         export GDCS_VLLM_TEST_MAX_TOKENS="128"
         EOF
         

### NVIDIA H200 141 GB
         
         cat << 'EOF' > ${HOME}/gdcag-solutions/open-weight-models/vllm/gemma/env.d/accelerator.sh && echo "Successfully created." || echo "Failed to create!"
         # Accelerator: NVIDIA H200 141 GB
         export GDCS_WORKLOAD_ACCELERATOR_TYPE="nvidia.com/gpu-pod-NVIDIA_H200"
         export GDCS_WORKLOAD_ACCELERATOR_COUNT="1"
         
         # vLLM
         export GDCS_VLLM_MAX_MODEL_LEN="32768"
         export GDCS_VLLM_EXTRA_ARGS=""
         export GDCS_VLLM_STARTUP_FAILURE_THRESHOLD="360"
         export GDCS_VLLM_TEST_MAX_TOKENS="128"
         EOF
         

### NVIDIA B300 288 GB
         
         cat << 'EOF' > ${HOME}/gdcag-solutions/open-weight-models/vllm/gemma/env.d/accelerator.sh && echo "Successfully created." || echo "Failed to create!"
         # Accelerator: NVIDIA B300 288 GB
         export GDCS_WORKLOAD_ACCELERATOR_TYPE="nvidia.com/gpu-pod-NVIDIA_B300_SXM6_AC"
         export GDCS_WORKLOAD_ACCELERATOR_COUNT="1"
         
         # vLLM
         export GDCS_VLLM_MAX_MODEL_LEN="32768"
         export GDCS_VLLM_EXTRA_ARGS=""
         export GDCS_VLLM_STARTUP_FAILURE_THRESHOLD="360"
         export GDCS_VLLM_TEST_MAX_TOKENS="128"
         EOF
         

  2. Source the environment file:
         
         source ${HOME}/gdcag-solutions/open-weight-models/vllm/gemma/env.sh
         

The output is similar to the following:
         
         GDCS_ROOT_HOME=HOME_DIRECTORY_PATH/gdcag-solutions
         GDCS_IMPLEMENTATION_HOME=HOME_DIRECTORY_PATH/gdcag-solutions/open-weight-models/vllm
         GDCS_USER_GUIDE_HOME=HOME_DIRECTORY_PATH/gdcag-solutions/open-weight-models/vllm/gemma
         GDCS_HF_MODEL=HUGGING_FACE_REPOSITORY (ACCELERATOR_COUNT x ACCELERATOR_RESOURCE_TYPE)
         


**Note:** Any time a new terminal or shell is started, the environment file needs to be sourced.

### Cluster

  1. Configure `gdcloud`:
         
         gdcloud config set core/account "default-user"
         gdcloud config set core/organization_console_url "${GDC_ZONAL_CONSOLE_URL}"
         gdcloud config set core/project "${GDC_PROJECT}"
         gdcloud config set core/zone "${GDC_ZONE}"
         

  2. Authenticate to the GDC environment:
         
         gdcloud auth login
         

  3. Retrieve cluster credentials:
         
         gdcloud clusters get-credentials "${GDC_STANDARD_CLUSTER_NAME}" \
         --project="${GDC_PROJECT}" \
         --standard \
         --zone="${GDC_ZONE}"
         

  4. Verify connectivity to the cluster:
         
         kubectl get nodes -L node.cluster.private.gdc.goog/machine-class
         

  5. Verify that the accelerator resource type of the accelerator environment file is available in the cluster. The command lists the accelerator resource types that the nodes expose (the name depends on the installed GPU model; it is empty on clusters without GPU nodes) and the configured value:
         
         kubectl get nodes --output=json | jq -r '[.items[].status.allocatable | keys[] | select(startswith("nvidia.com/"))] | unique[]'
         echo "GDCS_WORKLOAD_ACCELERATOR_TYPE=${GDCS_WORKLOAD_ACCELERATOR_TYPE}"
         

**Note:** If the configured value isn't in the list, set `GDCS_WORKLOAD_ACCELERATOR_TYPE` in `env.d/accelerator.sh` to one of the listed resource types and source the environment file again.



## Implementation

### Namespace

  1. Create the namespace:
         
         kubectl create namespace "${GDCS_WORKLOAD_NAMESPACE}" \
         --dry-run=client \
         --output=yaml | kubectl apply -f -
         

  2. Add the `imagePullSecret`:
         
         kubectl create secret docker-registry "${GDCS_HARBOR_K8S_PULL_SECRET}" \
         --dry-run=client \
         --from-file=.dockerconfigjson=${GDCS_HARBOR_K8S_DOCKER_CONFIG}/config.json \
         --namespace="${GDCS_WORKLOAD_NAMESPACE}" \
         --output=yaml | kubectl apply -f -
         




### Model weights

  1. Download the model weights (only the files vLLM needs for the selected model, `GDCS_HF_DOWNLOAD_EXCLUDE` skips the rest) and remove the `.cache` directory:
         
         EXCLUDE_ARGS=()
         if [[ -n "${GDCS_HF_DOWNLOAD_EXCLUDE:-}" ]]; then
           read -r -a EXCLUDE_PATTERNS <<< "${GDCS_HF_DOWNLOAD_EXCLUDE}"
           EXCLUDE_ARGS=(--exclude "${EXCLUDE_PATTERNS[@]}")
         fi
         hf download "${GDCS_HF_MODEL}" --revision "${GDCS_HF_MODEL_REVISION}" --local-dir "${GDCS_HF_MODEL_DOWNLOAD_DIR}" "${EXCLUDE_ARGS[@]}" && \
         rm -rf "${GDCS_HF_MODEL_DOWNLOAD_DIR}/.cache"
         

  2. Calculate the required `PersistentVolumeClaim` size from the downloaded model weights with 25% overhead (rounded up to the next whole GiB):
         
         MODEL_KIB=$(du -sk "${GDCS_HF_MODEL_DOWNLOAD_DIR}" | awk '{print $1}')
         export GDCS_MODEL_PVC_SIZE="$(( (MODEL_KIB * 125 / 100 + 1048575) / 1048576 ))Gi"
         echo "GDCS_MODEL_PVC_SIZE=${GDCS_MODEL_PVC_SIZE}"
         

  3. Create the manifest for the ReadWriteOnce PersistentVolumeClaim for the model weights:
         
         cat <<EOF > "${GDCS_USER_GUIDE_HOME}/${GDCS_WORKLOAD_NAME}-rwo-pvc.yaml"
         apiVersion: v1
         kind: PersistentVolumeClaim
         metadata:
           name: ${GDCS_WORKLOAD_NAME}-rwo
         spec:
           accessModes:
             - ReadWriteOnce
           resources:
             requests:
               storage: ${GDCS_MODEL_PVC_SIZE}
           storageClassName: standard-rwo
           volumeMode: Filesystem
         EOF
         

  4. Apply the manifest for the PersistentVolumeClaim for the model weights:
         
         kubectl apply \
         --filename="${GDCS_USER_GUIDE_HOME}/${GDCS_WORKLOAD_NAME}-rwo-pvc.yaml" \
         --namespace="${GDCS_WORKLOAD_NAMESPACE}"
         

  5. Wait for the `PersistentVolumeClaim` to bind and print the values that the Infrastructure Operator needs to adjust the I/O quality of service (QoS) policy:
         
         kubectl wait \
         --for=jsonpath='{.status.phase}'=Bound \
         "pvc/${GDCS_WORKLOAD_NAME}-rwo" \
         --namespace="${GDCS_WORKLOAD_NAMESPACE}" \
         --timeout=120s
         BACKING_PVC=$(kubectl get pvc "${GDCS_WORKLOAD_NAME}-rwo" \
         --namespace="${GDCS_WORKLOAD_NAMESPACE}" \
         --output=jsonpath='{.spec.volumeName}')
         echo "BACKING_PVC=${BACKING_PVC} ORG=${GDC_ORG}"
         

  6. If `performance-rwo` isn't available on your cluster, ask your Infrastructure Operator to apply the high-performance QoS policy (`system-performance-<ORG>-admin`, 30 IOPS per GiB with a 6,148 IOPS minimum floor) to the volume that backs the `PersistentVolumeClaim`. Provide the `BACKING_PVC` and `ORG` values that the previous step printed. The Infrastructure Operator applies the policy as described in [FILE-R0097](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/gdcag-io/service-manual/file/runbooks/file-r0097); it takes effect on the live volume, so you can continue with the next steps.

**Note:** If high-performance block storage is enabled on your cluster, you can set `storageClassName: performance-rwo` in the `PersistentVolumeClaim` manifest instead of requesting the QoS policy. If `kubectl get storageclass performance-rwo` returns nothing, the Infrastructure Operator has not enabled high-performance block storage.
  7. Create the manifest for the model loader Pod:
         
         cat <<EOF > "${GDCS_USER_GUIDE_HOME}/${GDCS_MODEL_LOADER_POD_NAME}-pod.yaml"
         apiVersion: v1
         kind: Pod
         metadata:
           name: ${GDCS_MODEL_LOADER_POD_NAME}
         spec:
           containers:
             - name: uploader
               image: ${GDCS_HARBOR_PROJECT_URI}/library/busybox:${GDCS_BUSYBOX_IMAGE_TAG}
               command: ["sleep", "infinity"]
               volumeMounts:
                 - name: model-data
                   mountPath: ${GDCS_HF_PV_MOUNT_PATH}
           imagePullSecrets:
             - name: ${GDCS_HARBOR_K8S_PULL_SECRET}
           volumes:
             - name: model-data
               persistentVolumeClaim:
                 claimName: ${GDCS_WORKLOAD_NAME}-rwo
         EOF
         

  8. Apply the manifest for the model loader Pod:
         
         kubectl apply \
         --filename="${GDCS_USER_GUIDE_HOME}/${GDCS_MODEL_LOADER_POD_NAME}-pod.yaml" \
         --namespace="${GDCS_WORKLOAD_NAMESPACE}"
         

  9. Wait for the model loader Pod to be Running:
         
         watch --color --interval 5 --no-title \
         "kubectl get pod/${GDCS_MODEL_LOADER_POD_NAME} \
         --namespace=${GDCS_WORKLOAD_NAMESPACE} | GREP_COLORS='mt=01;92' grep -E --color=always -e '^' -e 'Running'"
         

  10. Upload the model weights to the `PersistentVolume` (the script skips files that already exist with the same size, so it can be re-run):
         
         export LOCAL_MODEL_DIR="${GDCS_HF_MODEL_DOWNLOAD_DIR}"
         export REMOTE_MODEL_DIR="${GDCS_HF_PV_MOUNT_PATH}/${GDCS_HF_MODEL_LOWERCASE}"
         export REMOTE_MOUNT_DIR="${GDCS_HF_PV_MOUNT_PATH}"
         
         ${GDCS_IMPLEMENTATION_HOME}/model_weight_upload.sh
         

  11. Delete the model loader Pod:
         
         kubectl delete pod/${GDCS_MODEL_LOADER_POD_NAME} \
         --namespace="${GDCS_WORKLOAD_NAMESPACE}"
         




### Inference server

  1. Create the manifest for the vLLM Deployment. The ConfigMap carries the model-specific vLLM settings from the environment, so the manifest is the same for every model and GPU option:
         
         cat <<EOF > "${GDCS_USER_GUIDE_HOME}/${GDCS_WORKLOAD_NAME}-deployment.yaml"
         apiVersion: v1
         kind: ConfigMap
         metadata:
           name: ${GDCS_WORKLOAD_NAME}
         data:
           MAX_MODEL_LEN: "${GDCS_VLLM_MAX_MODEL_LEN}"
           MODEL: "${GDCS_HF_PV_MOUNT_PATH}/${GDCS_HF_MODEL_LOWERCASE}"
           PORT: "8000"
           TENSOR_PARALLEL_SIZE: "${GDCS_WORKLOAD_ACCELERATOR_COUNT}"
           VLLM_EXTRA_ARGS: "${GDCS_VLLM_EXTRA_ARGS}"
         ---
         apiVersion: apps/v1
         kind: Deployment
         metadata:
           name: ${GDCS_WORKLOAD_NAME}
           labels:
             app: ${GDCS_WORKLOAD_NAME}
         spec:
           replicas: 1
           selector:
             matchLabels:
               app: ${GDCS_WORKLOAD_NAME}
           strategy:
             type: Recreate
           template:
             metadata:
               labels:
                 app: ${GDCS_WORKLOAD_NAME}
             spec:
               containers:
                 - command:
                     - /bin/sh
                     - -c
                   args:
                     - exec vllm serve "\$MODEL" --port="\$PORT" --tensor-parallel-size="\$TENSOR_PARALLEL_SIZE" --max-model-len="\$MAX_MODEL_LEN" \$VLLM_EXTRA_ARGS
                   envFrom:
                     - configMapRef:
                         name: ${GDCS_WORKLOAD_NAME}
                   image: ${GDCS_HARBOR_PROJECT_URI}/vllm/vllm-openai:${GDCS_VLLM_IMAGE_TAG}-fips
                   livenessProbe:
                     failureThreshold: 3
                     httpGet:
                       path: /health
                       port: 8000
                     periodSeconds: 20
                     timeoutSeconds: 5
                   name: vllm
                   ports:
                     - containerPort: 8000
                   readinessProbe:
                     failureThreshold: 3
                     httpGet:
                       path: /health
                       port: 8000
                     periodSeconds: 10
                     successThreshold: 1
                     timeoutSeconds: 5
                   resources:
                     limits:
                       ${GDCS_WORKLOAD_ACCELERATOR_TYPE}: "${GDCS_WORKLOAD_ACCELERATOR_COUNT}"
                     requests:
                       ${GDCS_WORKLOAD_ACCELERATOR_TYPE}: "${GDCS_WORKLOAD_ACCELERATOR_COUNT}"
                   startupProbe:
                     httpGet:
                       path: /health
                       port: 8000
                     failureThreshold: ${GDCS_VLLM_STARTUP_FAILURE_THRESHOLD}
                     periodSeconds: 10
                     timeoutSeconds: 5
                   volumeMounts:
                     - name: model-weights
                       mountPath: ${GDCS_HF_PV_MOUNT_PATH}
                     - name: shm
                       mountPath: /dev/shm
               securityContext:
                 seLinuxOptions:
                   type: spc_t
               imagePullSecrets:
                 - name: ${GDCS_HARBOR_K8S_PULL_SECRET}
               volumes:
                 - name: model-weights
                   persistentVolumeClaim:
                     claimName: ${GDCS_WORKLOAD_NAME}-rwo
                 - name: shm
                   emptyDir:
                     medium: Memory
                     sizeLimit: "8Gi"
         ---
         apiVersion: v1
         kind: Service
         metadata:
           name: ${GDCS_WORKLOAD_NAME}
         spec:
           ports:
             - name: vllm-http
               port: 80
               protocol: TCP
               targetPort: 8000
           selector:
             app: ${GDCS_WORKLOAD_NAME}
           type: LoadBalancer
         EOF
         

**Note:** The startup probe allows `GDCS_VLLM_STARTUP_FAILURE_THRESHOLD` x 10 seconds for vLLM to load the weights and compile the CUDA graphs; the accelerator environment file (`env.d/accelerator.sh`) sets a value that matches the size of the model. The `exec vllm serve` form appends the space-separated `VLLM_EXTRA_ARGS` as individual arguments, so the values must not contain quotes; use vLLM's dotted form for JSON-typed flags, for example `--limit-mm-per-prompt.image=0`.
  2. Apply the manifest for the vLLM Deployment:
         
         kubectl apply \
         --filename="${GDCS_USER_GUIDE_HOME}/${GDCS_WORKLOAD_NAME}-deployment.yaml" \
         --namespace="${GDCS_WORKLOAD_NAMESPACE}"
         

  3. Create the manifest for the vLLM `NetworkPolicy`:
         
         cat << EOF > "${GDCS_USER_GUIDE_HOME}/vllm-networkpolicy.yaml" && echo "Successfully created." || echo "Failed to create!"
         apiVersion: networking.k8s.io/v1
         kind: NetworkPolicy
         metadata:
           name: allow-vllm-ingress
           namespace: ${GDCS_WORKLOAD_NAMESPACE}
         spec:
           ingress:
           - from:
             - ipBlock:
                 cidr: 0.0.0.0/0
             - namespaceSelector: {}
             ports:
             - port: 8000
               protocol: TCP
           podSelector: {}
           policyTypes:
           - Ingress
         EOF
         

  4. Apply the manifest for the vLLM `NetworkPolicy`:
         
         kubectl apply \
         --filename="${GDCS_USER_GUIDE_HOME}/vllm-networkpolicy.yaml"
         


**Note:** The `NetworkPolicy` admits traffic from any source to the workload port inside the cluster. Access to the LoadBalancer IP address from outside the project additionally requires a `ProjectNetworkPolicy` (`networking.gdc.goog/v1`) created in the project namespace by a Project NetworkPolicy Admin, see [Configure project network policies](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform/pa-user/pnp/pnp-overview).

  1. Wait for the Pod to be Running:
         
         watch --color --interval 5 --no-title \
         "kubectl get pods --selector=app=${GDCS_WORKLOAD_NAME} \
         --namespace=${GDCS_WORKLOAD_NAMESPACE} | GREP_COLORS='mt=01;92' grep -E --color=always -e '^' -e 'Running'"
         

  2. Wait for the Deployment to be Ready:
         
         watch --color --interval 5 --no-title \
         "kubectl get deployment/${GDCS_WORKLOAD_NAME} \
         --namespace=${GDCS_WORKLOAD_NAMESPACE} | GREP_COLORS='mt=01;92' grep -E --color=always -e '^' -e '1/1     1            1'"
         

  3. Optional: Stream the container logs to monitor startup progress:
         
         kubectl logs deployment/${GDCS_WORKLOAD_NAME} \
         --follow \
         --namespace="${GDCS_WORKLOAD_NAMESPACE}"
         




## Validation

  1. Retrieve the LoadBalancer IP address for vLLM:
         
         export VLLM_LB_IP=$(kubectl get service/${GDCS_WORKLOAD_NAME} --namespace="${GDCS_WORKLOAD_NAMESPACE}" --output=jsonpath='{.status.loadBalancer.ingress[*].ip}')
         echo "VLLM_LB_IP=${VLLM_LB_IP}"
         

  2. Send a test request to vLLM. The `max_tokens` value is `GDCS_VLLM_TEST_MAX_TOKENS` from `env.d/accelerator.sh`:
         
         curl http://${VLLM_LB_IP}/v1/models
         
         curl http://${VLLM_LB_IP}/v1/chat/completions \
         -H "Content-Type: application/json" \
         -d '{
           "model": "'${GDCS_HF_PV_MOUNT_PATH}/${GDCS_HF_MODEL_LOWERCASE}'",
           "messages": [
             {"role": "user", "content": "Explain Google Distributed Cloud air-gapped briefly."}
           ],
           "max_tokens": '${GDCS_VLLM_TEST_MAX_TOKENS}'
         }'
         

**Note:** Gemma 4 is a thinking model, and reasoning tokens count against `max_tokens`. If `content` is empty and `finish_reason` is `length`, raise `GDCS_VLLM_TEST_MAX_TOKENS` in `env.d/accelerator.sh`, source the environment file, and send the request again. This guide covers text generation only: multimodal vision and audio input wasn't validated with the FIPS-compatible vLLM image.
  3. If the LoadBalancer IP address isn't reachable from the workstation, for example because no `ProjectNetworkPolicy` admits it yet, send the requests through port forwarding:
         
         kubectl port-forward service/${GDCS_WORKLOAD_NAME} \
         --namespace="${GDCS_WORKLOAD_NAMESPACE}" 8000:80 &
         PF_PID=$!
         
         sleep 1
         
         curl http://127.0.0.1:8000/v1/models
         
         kill ${PF_PID}
         




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
