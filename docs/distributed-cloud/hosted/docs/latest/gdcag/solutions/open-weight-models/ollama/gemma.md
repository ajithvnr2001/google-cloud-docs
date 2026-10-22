---
url: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/solutions/open-weight-models/ollama/gemma/
title: Gemma models with Ollama user guide on GDC air-gapped \u00a0|\u00a0 Google Distributed Cloud air-gapped \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T10:20:16.819657+00:00
---

# Gemma models with Ollama user guide on GDC air-gapped  |  Google Distributed Cloud air-gapped  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/solutions/open-weight-models/ollama/gemma/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Distributed, hybrid, and multicloud ](https://docs.cloud.google.com/docs/dhm-cloud)
  * [ Google Distributed Cloud ](https://docs.cloud.google.com/distributed-cloud/docs)
  * [ Air-gapped ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdch)
  * [ 1.16.2 (Latest) ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag)



Send feedback 

#  Gemma models with Ollama user guide on GDC air-gapped Stay organized with collections  Save and categorize content based on your preferences. 

This document provides step-by-step instructions for deploying open weight models from Google DeepMind, specifically the Gemma 4 family, using Ollama on Google Distributed Cloud (GDC) air-gapped environments. It covers using Ollama for simplified serving, using the GDC platform's capabilities, including Kubernetes, Harbor, and GPU resources. Select the model and the GPU option in the Model section; every other step is the same for all models.

## Supported models

Model | Ollama tag | Parameters | License | GPU options  
---|---|---|---|---  
Gemma 4 E2B | `gemma4:e2b` | 5.1B (2B effective) | [Gemma Terms of Use](https://ai.google.dev/gemma/terms) | 1 x any GPU  
Gemma 4 E4B | `gemma4:e4b` | 8.0B (4B effective) | [Gemma Terms of Use](https://ai.google.dev/gemma/terms) | 1 x any GPU  
Gemma 4 12B | `gemma4:12b` | 12B (dense) | [Gemma Terms of Use](https://ai.google.dev/gemma/terms) | 1 x any GPU  
Gemma 4 26B-A4B | `gemma4:26b` | 25.8B total / 4B active (mixture of experts) | [Gemma Terms of Use](https://ai.google.dev/gemma/terms) | 1 x any GPU  
Gemma 4 31B | `gemma4:31b` | 31.3B (dense) | [Gemma Terms of Use](https://ai.google.dev/gemma/terms) | 1 x any GPU  
  
## Architecture

The solution involves deploying Ollama as a containerized serving backend (`Deployment`) within a standard cluster. Model weights are stored on Persistent Volumes, populated from files downloaded locally and uploaded using a loader pod. A Kubernetes `Service` of type `LoadBalancer` exposes the backend API, and `NetworkPolicy` / `ProjectNetworkPolicy` objects secure access to it.

**Note:** Without a ReadOnlyMany StorageClass, this solution can deploy only one replica.

## Before you begin

**Note:** This guide requires GDC air-gapped 1.16.2-hf1 (1.16.2-gdch.1353-1) or later, and a standard cluster.

Complete the [Open Weight Models with Ollama reference implementation](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/solutions/open-weight-models/ollama/reference-implementation) on the workstation, and make sure you have access to the `${HOME}/gdcag-solutions` directory.

### Identity and Access Management

This guide assumes that you have the following roles on the standard cluster:

  * Optional: Standard Cluster Admin (View clusters from the console)
  * Standard Cluster Admin (`standard-cluster-admin`)
  * `StandardClusterRoleBinding` to the `StandardClusterRole` `cluster-admin` (created by a Project IAM Admin, see the _Identity and Access Management_ section of the reference implementation)



### Workstation

Run all commands in this guide from a workstation with the required tools and connectivity to the environment and internet, unless a step states otherwise.

The environment configuration is layered:

  * `${HOME}/gdcag-solutions/env.sh` loads the platform and registry settings.
  * `${HOME}/gdcag-solutions/open-weight-models/ollama/env.sh` adds the Ollama settings.

  * This user guide adds `env.d/model.sh` (the model) and `env.d/accelerator.sh` (the GPU option and runtime settings), which you write in the Model section; and `env.d/model-common.sh` (the values derived from them).



  1. Create the user guide directory structure:
         
         mkdir -p ${HOME}/gdcag-solutions/open-weight-models/ollama/gemma/env.d
         

  2. Create the common model environment configuration file. It computes the names and paths derived from the model name:
         
         cat << 'EOF' > ${HOME}/gdcag-solutions/open-weight-models/ollama/gemma/env.d/model-common.sh && echo "Successfully created." || echo "Failed to create!"
         # Model (derived from env.d/model.sh)
         export GDCS_OLLAMA_MODEL_LOWERCASE="${GDCS_OLLAMA_MODEL,,}"
         export GDCS_OLLAMA_MODEL_KUBERNETES="$(echo "${GDCS_OLLAMA_MODEL_LOWERCASE}" | tr ':' '-')"
         
         # Paths
         export GDCS_OLLAMA_MODEL_DOWNLOAD_DIR="${GDCS_USER_GUIDE_HOME}/models/${GDCS_OLLAMA_MODEL_LOWERCASE}"
         export GDCS_OLLAMA_PV_MOUNT_PATH="/root/.ollama/models"
         
         # Workload
         export GDCS_WORKLOAD_NAMESPACE="ollama-gemma"
         export GDCS_WORKLOAD_NAME="${GDCS_OLLAMA_MODEL_KUBERNETES}"
         export GDCS_MODEL_LOADER_POD_NAME="loader-${GDCS_OLLAMA_MODEL_KUBERNETES}"
         EOF
         

  3. Create the user guide environment loader file. It sources the root environment, the implementation environment, and the model environment:
         
         cat << 'EOF' > ${HOME}/gdcag-solutions/open-weight-models/ollama/gemma/env.sh && echo "Successfully created." || echo "Failed to create!"
         source "${HOME}/gdcag-solutions/open-weight-models/ollama/env.sh"
         
         export GDCS_USER_GUIDE_HOME="${HOME}/gdcag-solutions/open-weight-models/ollama/gemma"
         echo "GDCS_USER_GUIDE_HOME=${GDCS_USER_GUIDE_HOME}"
         
         # Sourced in dependency order: the model selection, the accelerator and runtime settings, then the values derived from them
         source "${GDCS_USER_GUIDE_HOME}/env.d/model.sh"
         source "${GDCS_USER_GUIDE_HOME}/env.d/accelerator.sh"
         source "${GDCS_USER_GUIDE_HOME}/env.d/model-common.sh"
         EOF
         




### Model

Each tab lists the model facts, the command that writes the model environment file `env.d/model.sh`, and nested tabs that write the accelerator environment file `env.d/accelerator.sh` for your chosen GPU option with pre-filled resource types and Ollama settings. To switch models or GPU options later, write different environment files, source the environment again, and repeat the Implementation section; the workloads of several models can run side by side in the same namespace because every resource name is derived from the model name.

GPU | Memory | Machine types | Accelerator resource type  
---|---|---|---  
NVIDIA A100 | 40 GB | `a2-highgpu-1g-gdc` | `nvidia.com/gpu-pod-NVIDIA_A100_PCIE_40GB`  
NVIDIA A100 | 80 GB | `a2-ultragpu-1g-gdc`, `a2-ultragpu-2g-gdc` | `nvidia.com/gpu-pod-NVIDIA_A100_80GB_PCIE`  
NVIDIA H100 | 94 GB | `a3-highgpu-1g-gdc` (Preview), `a3-highgpu-2g-gdc` (Preview), `a3-highgpu-4g-gdc` | `nvidia.com/gpu-pod-NVIDIA_H100_NVL`  
NVIDIA H200 | 141 GB | `a3-ultragpu-8g-gdc` | `nvidia.com/gpu-pod-NVIDIA_H200`  
NVIDIA B300 | 288 GB | `a4-ultragpu-8g-gdc` | `nvidia.com/gpu-pod-NVIDIA_B300_SXM6_AC`  
  
  * Create the model and accelerator environment files for the model and GPU option you want to deploy.

**Note:** CPU and memory limits are starting estimates; adjust them based on observed workload utilization.

### Gemma 4 E2B

Attribute | Value  
---|---  
**Ollama tag** | `gemma4:e2b`  
**Parameters** | 5.1B (2B effective)  
**License** | [Gemma Terms of Use](https://ai.google.dev/gemma/terms)  
**Weights** | Ollama default quantization, about 4.6 GB  
**Context length** | 128k tokens  
  
Create the model environment file:
    
    
    cat << 'EOF' > ${HOME}/gdcag-solutions/open-weight-models/ollama/gemma/env.d/model.sh && echo "Successfully created." || echo "Failed to create!"
    # Model: Gemma 4 E2B
    export GDCS_OLLAMA_MODEL="gemma4:e2b"
    EOF
    

Create the accelerator environment file for your GPU option:

### NVIDIA A100 40 GB
    
    
    cat << 'EOF' > ${HOME}/gdcag-solutions/open-weight-models/ollama/gemma/env.d/accelerator.sh && echo "Successfully created." || echo "Failed to create!"
    # Accelerator: NVIDIA A100 40 GB
    export GDCS_WORKLOAD_ACCELERATOR_TYPE="nvidia.com/gpu-pod-NVIDIA_A100_PCIE_40GB"
    export GDCS_WORKLOAD_ACCELERATOR_COUNT="1"
    
    # Resources
    export GDCS_WORKLOAD_CPU_LIMIT="4"
    export GDCS_WORKLOAD_CPU_REQUEST="2"
    export GDCS_WORKLOAD_MEMORY_LIMIT="12Gi"
    export GDCS_WORKLOAD_MEMORY_REQUEST="6Gi"
    
    # Ollama
    export GDCS_OLLAMA_NUM_PARALLEL="4"
    export GDCS_OLLAMA_TEST_NUM_PREDICT="128"
    EOF
    

### NVIDIA A100 80 GB
    
    
    cat << 'EOF' > ${HOME}/gdcag-solutions/open-weight-models/ollama/gemma/env.d/accelerator.sh && echo "Successfully created." || echo "Failed to create!"
    # Accelerator: NVIDIA A100 80 GB
    export GDCS_WORKLOAD_ACCELERATOR_TYPE="nvidia.com/gpu-pod-NVIDIA_A100_80GB_PCIE"
    export GDCS_WORKLOAD_ACCELERATOR_COUNT="1"
    
    # Resources
    export GDCS_WORKLOAD_CPU_LIMIT="4"
    export GDCS_WORKLOAD_CPU_REQUEST="2"
    export GDCS_WORKLOAD_MEMORY_LIMIT="12Gi"
    export GDCS_WORKLOAD_MEMORY_REQUEST="6Gi"
    
    # Ollama
    export GDCS_OLLAMA_NUM_PARALLEL="4"
    export GDCS_OLLAMA_TEST_NUM_PREDICT="128"
    EOF
    

### NVIDIA H100 94 GB
    
    
    cat << 'EOF' > ${HOME}/gdcag-solutions/open-weight-models/ollama/gemma/env.d/accelerator.sh && echo "Successfully created." || echo "Failed to create!"
    # Accelerator: NVIDIA H100 94 GB
    export GDCS_WORKLOAD_ACCELERATOR_TYPE="nvidia.com/gpu-pod-NVIDIA_H100_NVL"
    export GDCS_WORKLOAD_ACCELERATOR_COUNT="1"
    
    # Resources
    export GDCS_WORKLOAD_CPU_LIMIT="4"
    export GDCS_WORKLOAD_CPU_REQUEST="2"
    export GDCS_WORKLOAD_MEMORY_LIMIT="12Gi"
    export GDCS_WORKLOAD_MEMORY_REQUEST="6Gi"
    
    # Ollama
    export GDCS_OLLAMA_NUM_PARALLEL="4"
    export GDCS_OLLAMA_TEST_NUM_PREDICT="128"
    EOF
    

### NVIDIA H200 141 GB
    
    
    cat << 'EOF' > ${HOME}/gdcag-solutions/open-weight-models/ollama/gemma/env.d/accelerator.sh && echo "Successfully created." || echo "Failed to create!"
    # Accelerator: NVIDIA H200 141 GB
    export GDCS_WORKLOAD_ACCELERATOR_TYPE="nvidia.com/gpu-pod-NVIDIA_H200"
    export GDCS_WORKLOAD_ACCELERATOR_COUNT="1"
    
    # Resources
    export GDCS_WORKLOAD_CPU_LIMIT="4"
    export GDCS_WORKLOAD_CPU_REQUEST="2"
    export GDCS_WORKLOAD_MEMORY_LIMIT="12Gi"
    export GDCS_WORKLOAD_MEMORY_REQUEST="6Gi"
    
    # Ollama
    export GDCS_OLLAMA_NUM_PARALLEL="4"
    export GDCS_OLLAMA_TEST_NUM_PREDICT="128"
    EOF
    

### NVIDIA B300 288 GB
    
    
    cat << 'EOF' > ${HOME}/gdcag-solutions/open-weight-models/ollama/gemma/env.d/accelerator.sh && echo "Successfully created." || echo "Failed to create!"
    # Accelerator: NVIDIA B300 288 GB
    export GDCS_WORKLOAD_ACCELERATOR_TYPE="nvidia.com/gpu-pod-NVIDIA_B300_SXM6_AC"
    export GDCS_WORKLOAD_ACCELERATOR_COUNT="1"
    
    # Resources
    export GDCS_WORKLOAD_CPU_LIMIT="4"
    export GDCS_WORKLOAD_CPU_REQUEST="2"
    export GDCS_WORKLOAD_MEMORY_LIMIT="12Gi"
    export GDCS_WORKLOAD_MEMORY_REQUEST="6Gi"
    
    # Ollama
    export GDCS_OLLAMA_NUM_PARALLEL="4"
    export GDCS_OLLAMA_TEST_NUM_PREDICT="128"
    EOF
    

### Gemma 4 E4B

Attribute | Value  
---|---  
**Ollama tag** | `gemma4:e4b`  
**Parameters** | 8.0B (4B effective)  
**License** | [Gemma Terms of Use](https://ai.google.dev/gemma/terms)  
**Weights** | Ollama default quantization, about 6.6 GB  
**Context length** | 128k tokens  
  
Create the model environment file:
    
    
    cat << 'EOF' > ${HOME}/gdcag-solutions/open-weight-models/ollama/gemma/env.d/model.sh && echo "Successfully created." || echo "Failed to create!"
    # Model: Gemma 4 E4B
    export GDCS_OLLAMA_MODEL="gemma4:e4b"
    EOF
    

Create the accelerator environment file for your GPU option:

### NVIDIA A100 40 GB
    
    
    cat << 'EOF' > ${HOME}/gdcag-solutions/open-weight-models/ollama/gemma/env.d/accelerator.sh && echo "Successfully created." || echo "Failed to create!"
    # Accelerator: NVIDIA A100 40 GB
    export GDCS_WORKLOAD_ACCELERATOR_TYPE="nvidia.com/gpu-pod-NVIDIA_A100_PCIE_40GB"
    export GDCS_WORKLOAD_ACCELERATOR_COUNT="1"
    
    # Resources
    export GDCS_WORKLOAD_CPU_LIMIT="4"
    export GDCS_WORKLOAD_CPU_REQUEST="2"
    export GDCS_WORKLOAD_MEMORY_LIMIT="16Gi"
    export GDCS_WORKLOAD_MEMORY_REQUEST="8Gi"
    
    # Ollama
    export GDCS_OLLAMA_NUM_PARALLEL="4"
    export GDCS_OLLAMA_TEST_NUM_PREDICT="128"
    EOF
    

### NVIDIA A100 80 GB
    
    
    cat << 'EOF' > ${HOME}/gdcag-solutions/open-weight-models/ollama/gemma/env.d/accelerator.sh && echo "Successfully created." || echo "Failed to create!"
    # Accelerator: NVIDIA A100 80 GB
    export GDCS_WORKLOAD_ACCELERATOR_TYPE="nvidia.com/gpu-pod-NVIDIA_A100_80GB_PCIE"
    export GDCS_WORKLOAD_ACCELERATOR_COUNT="1"
    
    # Resources
    export GDCS_WORKLOAD_CPU_LIMIT="4"
    export GDCS_WORKLOAD_CPU_REQUEST="2"
    export GDCS_WORKLOAD_MEMORY_LIMIT="16Gi"
    export GDCS_WORKLOAD_MEMORY_REQUEST="8Gi"
    
    # Ollama
    export GDCS_OLLAMA_NUM_PARALLEL="4"
    export GDCS_OLLAMA_TEST_NUM_PREDICT="128"
    EOF
    

### NVIDIA H100 94 GB
    
    
    cat << 'EOF' > ${HOME}/gdcag-solutions/open-weight-models/ollama/gemma/env.d/accelerator.sh && echo "Successfully created." || echo "Failed to create!"
    # Accelerator: NVIDIA H100 94 GB
    export GDCS_WORKLOAD_ACCELERATOR_TYPE="nvidia.com/gpu-pod-NVIDIA_H100_NVL"
    export GDCS_WORKLOAD_ACCELERATOR_COUNT="1"
    
    # Resources
    export GDCS_WORKLOAD_CPU_LIMIT="4"
    export GDCS_WORKLOAD_CPU_REQUEST="2"
    export GDCS_WORKLOAD_MEMORY_LIMIT="16Gi"
    export GDCS_WORKLOAD_MEMORY_REQUEST="8Gi"
    
    # Ollama
    export GDCS_OLLAMA_NUM_PARALLEL="4"
    export GDCS_OLLAMA_TEST_NUM_PREDICT="128"
    EOF
    

### NVIDIA H200 141 GB
    
    
    cat << 'EOF' > ${HOME}/gdcag-solutions/open-weight-models/ollama/gemma/env.d/accelerator.sh && echo "Successfully created." || echo "Failed to create!"
    # Accelerator: NVIDIA H200 141 GB
    export GDCS_WORKLOAD_ACCELERATOR_TYPE="nvidia.com/gpu-pod-NVIDIA_H200"
    export GDCS_WORKLOAD_ACCELERATOR_COUNT="1"
    
    # Resources
    export GDCS_WORKLOAD_CPU_LIMIT="4"
    export GDCS_WORKLOAD_CPU_REQUEST="2"
    export GDCS_WORKLOAD_MEMORY_LIMIT="16Gi"
    export GDCS_WORKLOAD_MEMORY_REQUEST="8Gi"
    
    # Ollama
    export GDCS_OLLAMA_NUM_PARALLEL="4"
    export GDCS_OLLAMA_TEST_NUM_PREDICT="128"
    EOF
    

### NVIDIA B300 288 GB
    
    
    cat << 'EOF' > ${HOME}/gdcag-solutions/open-weight-models/ollama/gemma/env.d/accelerator.sh && echo "Successfully created." || echo "Failed to create!"
    # Accelerator: NVIDIA B300 288 GB
    export GDCS_WORKLOAD_ACCELERATOR_TYPE="nvidia.com/gpu-pod-NVIDIA_B300_SXM6_AC"
    export GDCS_WORKLOAD_ACCELERATOR_COUNT="1"
    
    # Resources
    export GDCS_WORKLOAD_CPU_LIMIT="4"
    export GDCS_WORKLOAD_CPU_REQUEST="2"
    export GDCS_WORKLOAD_MEMORY_LIMIT="16Gi"
    export GDCS_WORKLOAD_MEMORY_REQUEST="8Gi"
    
    # Ollama
    export GDCS_OLLAMA_NUM_PARALLEL="4"
    export GDCS_OLLAMA_TEST_NUM_PREDICT="128"
    EOF
    

### Gemma 4 12B

Attribute | Value  
---|---  
**Ollama tag** | `gemma4:12b`  
**Parameters** | 12B (dense)  
**License** | [Gemma Terms of Use](https://ai.google.dev/gemma/terms)  
**Weights** | Ollama default quantization, about 7.7 GB  
**Context length** | 256k tokens  
  
Create the model environment file:
    
    
    cat << 'EOF' > ${HOME}/gdcag-solutions/open-weight-models/ollama/gemma/env.d/model.sh && echo "Successfully created." || echo "Failed to create!"
    # Model: Gemma 4 12B
    export GDCS_OLLAMA_MODEL="gemma4:12b"
    EOF
    

Create the accelerator environment file for your GPU option:

### NVIDIA A100 40 GB
    
    
    cat << 'EOF' > ${HOME}/gdcag-solutions/open-weight-models/ollama/gemma/env.d/accelerator.sh && echo "Successfully created." || echo "Failed to create!"
    # Accelerator: NVIDIA A100 40 GB
    export GDCS_WORKLOAD_ACCELERATOR_TYPE="nvidia.com/gpu-pod-NVIDIA_A100_PCIE_40GB"
    export GDCS_WORKLOAD_ACCELERATOR_COUNT="1"
    
    # Resources
    export GDCS_WORKLOAD_CPU_LIMIT="4"
    export GDCS_WORKLOAD_CPU_REQUEST="2"
    export GDCS_WORKLOAD_MEMORY_LIMIT="16Gi"
    export GDCS_WORKLOAD_MEMORY_REQUEST="8Gi"
    
    # Ollama
    export GDCS_OLLAMA_NUM_PARALLEL="4"
    export GDCS_OLLAMA_TEST_NUM_PREDICT="128"
    EOF
    

### NVIDIA A100 80 GB
    
    
    cat << 'EOF' > ${HOME}/gdcag-solutions/open-weight-models/ollama/gemma/env.d/accelerator.sh && echo "Successfully created." || echo "Failed to create!"
    # Accelerator: NVIDIA A100 80 GB
    export GDCS_WORKLOAD_ACCELERATOR_TYPE="nvidia.com/gpu-pod-NVIDIA_A100_80GB_PCIE"
    export GDCS_WORKLOAD_ACCELERATOR_COUNT="1"
    
    # Resources
    export GDCS_WORKLOAD_CPU_LIMIT="4"
    export GDCS_WORKLOAD_CPU_REQUEST="2"
    export GDCS_WORKLOAD_MEMORY_LIMIT="16Gi"
    export GDCS_WORKLOAD_MEMORY_REQUEST="8Gi"
    
    # Ollama
    export GDCS_OLLAMA_NUM_PARALLEL="4"
    export GDCS_OLLAMA_TEST_NUM_PREDICT="128"
    EOF
    

### NVIDIA H100 94 GB
    
    
    cat << 'EOF' > ${HOME}/gdcag-solutions/open-weight-models/ollama/gemma/env.d/accelerator.sh && echo "Successfully created." || echo "Failed to create!"
    # Accelerator: NVIDIA H100 94 GB
    export GDCS_WORKLOAD_ACCELERATOR_TYPE="nvidia.com/gpu-pod-NVIDIA_H100_NVL"
    export GDCS_WORKLOAD_ACCELERATOR_COUNT="1"
    
    # Resources
    export GDCS_WORKLOAD_CPU_LIMIT="4"
    export GDCS_WORKLOAD_CPU_REQUEST="2"
    export GDCS_WORKLOAD_MEMORY_LIMIT="16Gi"
    export GDCS_WORKLOAD_MEMORY_REQUEST="8Gi"
    
    # Ollama
    export GDCS_OLLAMA_NUM_PARALLEL="4"
    export GDCS_OLLAMA_TEST_NUM_PREDICT="128"
    EOF
    

### NVIDIA H200 141 GB
    
    
    cat << 'EOF' > ${HOME}/gdcag-solutions/open-weight-models/ollama/gemma/env.d/accelerator.sh && echo "Successfully created." || echo "Failed to create!"
    # Accelerator: NVIDIA H200 141 GB
    export GDCS_WORKLOAD_ACCELERATOR_TYPE="nvidia.com/gpu-pod-NVIDIA_H200"
    export GDCS_WORKLOAD_ACCELERATOR_COUNT="1"
    
    # Resources
    export GDCS_WORKLOAD_CPU_LIMIT="4"
    export GDCS_WORKLOAD_CPU_REQUEST="2"
    export GDCS_WORKLOAD_MEMORY_LIMIT="16Gi"
    export GDCS_WORKLOAD_MEMORY_REQUEST="8Gi"
    
    # Ollama
    export GDCS_OLLAMA_NUM_PARALLEL="4"
    export GDCS_OLLAMA_TEST_NUM_PREDICT="128"
    EOF
    

### NVIDIA B300 288 GB
    
    
    cat << 'EOF' > ${HOME}/gdcag-solutions/open-weight-models/ollama/gemma/env.d/accelerator.sh && echo "Successfully created." || echo "Failed to create!"
    # Accelerator: NVIDIA B300 288 GB
    export GDCS_WORKLOAD_ACCELERATOR_TYPE="nvidia.com/gpu-pod-NVIDIA_B300_SXM6_AC"
    export GDCS_WORKLOAD_ACCELERATOR_COUNT="1"
    
    # Resources
    export GDCS_WORKLOAD_CPU_LIMIT="4"
    export GDCS_WORKLOAD_CPU_REQUEST="2"
    export GDCS_WORKLOAD_MEMORY_LIMIT="16Gi"
    export GDCS_WORKLOAD_MEMORY_REQUEST="8Gi"
    
    # Ollama
    export GDCS_OLLAMA_NUM_PARALLEL="4"
    export GDCS_OLLAMA_TEST_NUM_PREDICT="128"
    EOF
    

### Gemma 4 26B-A4B

Attribute | Value  
---|---  
**Ollama tag** | `gemma4:26b`  
**Parameters** | 25.8B total / 4B active (mixture of experts)  
**License** | [Gemma Terms of Use](https://ai.google.dev/gemma/terms)  
**Weights** | Ollama default quantization, about 16 GB  
**Context length** | 256k tokens  
  
Create the model environment file:
    
    
    cat << 'EOF' > ${HOME}/gdcag-solutions/open-weight-models/ollama/gemma/env.d/model.sh && echo "Successfully created." || echo "Failed to create!"
    # Model: Gemma 4 26B-A4B
    export GDCS_OLLAMA_MODEL="gemma4:26b"
    EOF
    

Create the accelerator environment file for your GPU option:

### NVIDIA A100 40 GB
    
    
    cat << 'EOF' > ${HOME}/gdcag-solutions/open-weight-models/ollama/gemma/env.d/accelerator.sh && echo "Successfully created." || echo "Failed to create!"
    # Accelerator: NVIDIA A100 40 GB
    export GDCS_WORKLOAD_ACCELERATOR_TYPE="nvidia.com/gpu-pod-NVIDIA_A100_PCIE_40GB"
    export GDCS_WORKLOAD_ACCELERATOR_COUNT="1"
    
    # Resources
    export GDCS_WORKLOAD_CPU_LIMIT="4"
    export GDCS_WORKLOAD_CPU_REQUEST="2"
    export GDCS_WORKLOAD_MEMORY_LIMIT="32Gi"
    export GDCS_WORKLOAD_MEMORY_REQUEST="16Gi"
    
    # Ollama
    export GDCS_OLLAMA_NUM_PARALLEL="4"
    export GDCS_OLLAMA_TEST_NUM_PREDICT="128"
    EOF
    

### NVIDIA A100 80 GB
    
    
    cat << 'EOF' > ${HOME}/gdcag-solutions/open-weight-models/ollama/gemma/env.d/accelerator.sh && echo "Successfully created." || echo "Failed to create!"
    # Accelerator: NVIDIA A100 80 GB
    export GDCS_WORKLOAD_ACCELERATOR_TYPE="nvidia.com/gpu-pod-NVIDIA_A100_80GB_PCIE"
    export GDCS_WORKLOAD_ACCELERATOR_COUNT="1"
    
    # Resources
    export GDCS_WORKLOAD_CPU_LIMIT="4"
    export GDCS_WORKLOAD_CPU_REQUEST="2"
    export GDCS_WORKLOAD_MEMORY_LIMIT="32Gi"
    export GDCS_WORKLOAD_MEMORY_REQUEST="16Gi"
    
    # Ollama
    export GDCS_OLLAMA_NUM_PARALLEL="4"
    export GDCS_OLLAMA_TEST_NUM_PREDICT="128"
    EOF
    

### NVIDIA H100 94 GB
    
    
    cat << 'EOF' > ${HOME}/gdcag-solutions/open-weight-models/ollama/gemma/env.d/accelerator.sh && echo "Successfully created." || echo "Failed to create!"
    # Accelerator: NVIDIA H100 94 GB
    export GDCS_WORKLOAD_ACCELERATOR_TYPE="nvidia.com/gpu-pod-NVIDIA_H100_NVL"
    export GDCS_WORKLOAD_ACCELERATOR_COUNT="1"
    
    # Resources
    export GDCS_WORKLOAD_CPU_LIMIT="4"
    export GDCS_WORKLOAD_CPU_REQUEST="2"
    export GDCS_WORKLOAD_MEMORY_LIMIT="32Gi"
    export GDCS_WORKLOAD_MEMORY_REQUEST="16Gi"
    
    # Ollama
    export GDCS_OLLAMA_NUM_PARALLEL="4"
    export GDCS_OLLAMA_TEST_NUM_PREDICT="128"
    EOF
    

### NVIDIA H200 141 GB
    
    
    cat << 'EOF' > ${HOME}/gdcag-solutions/open-weight-models/ollama/gemma/env.d/accelerator.sh && echo "Successfully created." || echo "Failed to create!"
    # Accelerator: NVIDIA H200 141 GB
    export GDCS_WORKLOAD_ACCELERATOR_TYPE="nvidia.com/gpu-pod-NVIDIA_H200"
    export GDCS_WORKLOAD_ACCELERATOR_COUNT="1"
    
    # Resources
    export GDCS_WORKLOAD_CPU_LIMIT="4"
    export GDCS_WORKLOAD_CPU_REQUEST="2"
    export GDCS_WORKLOAD_MEMORY_LIMIT="32Gi"
    export GDCS_WORKLOAD_MEMORY_REQUEST="16Gi"
    
    # Ollama
    export GDCS_OLLAMA_NUM_PARALLEL="4"
    export GDCS_OLLAMA_TEST_NUM_PREDICT="128"
    EOF
    

### NVIDIA B300 288 GB
    
    
    cat << 'EOF' > ${HOME}/gdcag-solutions/open-weight-models/ollama/gemma/env.d/accelerator.sh && echo "Successfully created." || echo "Failed to create!"
    # Accelerator: NVIDIA B300 288 GB
    export GDCS_WORKLOAD_ACCELERATOR_TYPE="nvidia.com/gpu-pod-NVIDIA_B300_SXM6_AC"
    export GDCS_WORKLOAD_ACCELERATOR_COUNT="1"
    
    # Resources
    export GDCS_WORKLOAD_CPU_LIMIT="4"
    export GDCS_WORKLOAD_CPU_REQUEST="2"
    export GDCS_WORKLOAD_MEMORY_LIMIT="32Gi"
    export GDCS_WORKLOAD_MEMORY_REQUEST="16Gi"
    
    # Ollama
    export GDCS_OLLAMA_NUM_PARALLEL="4"
    export GDCS_OLLAMA_TEST_NUM_PREDICT="128"
    EOF
    

### Gemma 4 31B

Attribute | Value  
---|---  
**Ollama tag** | `gemma4:31b`  
**Parameters** | 31.3B (dense)  
**License** | [Gemma Terms of Use](https://ai.google.dev/gemma/terms)  
**Weights** | Ollama default quantization, about 19 GB  
**Context length** | 256k tokens  
  
Create the model environment file:
    
    
    cat << 'EOF' > ${HOME}/gdcag-solutions/open-weight-models/ollama/gemma/env.d/model.sh && echo "Successfully created." || echo "Failed to create!"
    # Model: Gemma 4 31B
    export GDCS_OLLAMA_MODEL="gemma4:31b"
    EOF
    

Create the accelerator environment file for your GPU option:

### NVIDIA A100 40 GB
    
    
    cat << 'EOF' > ${HOME}/gdcag-solutions/open-weight-models/ollama/gemma/env.d/accelerator.sh && echo "Successfully created." || echo "Failed to create!"
    # Accelerator: NVIDIA A100 40 GB
    export GDCS_WORKLOAD_ACCELERATOR_TYPE="nvidia.com/gpu-pod-NVIDIA_A100_PCIE_40GB"
    export GDCS_WORKLOAD_ACCELERATOR_COUNT="1"
    
    # Resources
    export GDCS_WORKLOAD_CPU_LIMIT="4"
    export GDCS_WORKLOAD_CPU_REQUEST="2"
    export GDCS_WORKLOAD_MEMORY_LIMIT="40Gi"
    export GDCS_WORKLOAD_MEMORY_REQUEST="20Gi"
    
    # Ollama
    export GDCS_OLLAMA_NUM_PARALLEL="4"
    export GDCS_OLLAMA_TEST_NUM_PREDICT="128"
    EOF
    

### NVIDIA A100 80 GB
    
    
    cat << 'EOF' > ${HOME}/gdcag-solutions/open-weight-models/ollama/gemma/env.d/accelerator.sh && echo "Successfully created." || echo "Failed to create!"
    # Accelerator: NVIDIA A100 80 GB
    export GDCS_WORKLOAD_ACCELERATOR_TYPE="nvidia.com/gpu-pod-NVIDIA_A100_80GB_PCIE"
    export GDCS_WORKLOAD_ACCELERATOR_COUNT="1"
    
    # Resources
    export GDCS_WORKLOAD_CPU_LIMIT="4"
    export GDCS_WORKLOAD_CPU_REQUEST="2"
    export GDCS_WORKLOAD_MEMORY_LIMIT="40Gi"
    export GDCS_WORKLOAD_MEMORY_REQUEST="20Gi"
    
    # Ollama
    export GDCS_OLLAMA_NUM_PARALLEL="4"
    export GDCS_OLLAMA_TEST_NUM_PREDICT="128"
    EOF
    

### NVIDIA H100 94 GB
    
    
    cat << 'EOF' > ${HOME}/gdcag-solutions/open-weight-models/ollama/gemma/env.d/accelerator.sh && echo "Successfully created." || echo "Failed to create!"
    # Accelerator: NVIDIA H100 94 GB
    export GDCS_WORKLOAD_ACCELERATOR_TYPE="nvidia.com/gpu-pod-NVIDIA_H100_NVL"
    export GDCS_WORKLOAD_ACCELERATOR_COUNT="1"
    
    # Resources
    export GDCS_WORKLOAD_CPU_LIMIT="4"
    export GDCS_WORKLOAD_CPU_REQUEST="2"
    export GDCS_WORKLOAD_MEMORY_LIMIT="40Gi"
    export GDCS_WORKLOAD_MEMORY_REQUEST="20Gi"
    
    # Ollama
    export GDCS_OLLAMA_NUM_PARALLEL="4"
    export GDCS_OLLAMA_TEST_NUM_PREDICT="128"
    EOF
    

### NVIDIA H200 141 GB
    
    
    cat << 'EOF' > ${HOME}/gdcag-solutions/open-weight-models/ollama/gemma/env.d/accelerator.sh && echo "Successfully created." || echo "Failed to create!"
    # Accelerator: NVIDIA H200 141 GB
    export GDCS_WORKLOAD_ACCELERATOR_TYPE="nvidia.com/gpu-pod-NVIDIA_H200"
    export GDCS_WORKLOAD_ACCELERATOR_COUNT="1"
    
    # Resources
    export GDCS_WORKLOAD_CPU_LIMIT="4"
    export GDCS_WORKLOAD_CPU_REQUEST="2"
    export GDCS_WORKLOAD_MEMORY_LIMIT="40Gi"
    export GDCS_WORKLOAD_MEMORY_REQUEST="20Gi"
    
    # Ollama
    export GDCS_OLLAMA_NUM_PARALLEL="4"
    export GDCS_OLLAMA_TEST_NUM_PREDICT="128"
    EOF
    

### NVIDIA B300 288 GB
    
    
    cat << 'EOF' > ${HOME}/gdcag-solutions/open-weight-models/ollama/gemma/env.d/accelerator.sh && echo "Successfully created." || echo "Failed to create!"
    # Accelerator: NVIDIA B300 288 GB
    export GDCS_WORKLOAD_ACCELERATOR_TYPE="nvidia.com/gpu-pod-NVIDIA_B300_SXM6_AC"
    export GDCS_WORKLOAD_ACCELERATOR_COUNT="1"
    
    # Resources
    export GDCS_WORKLOAD_CPU_LIMIT="4"
    export GDCS_WORKLOAD_CPU_REQUEST="2"
    export GDCS_WORKLOAD_MEMORY_LIMIT="40Gi"
    export GDCS_WORKLOAD_MEMORY_REQUEST="20Gi"
    
    # Ollama
    export GDCS_OLLAMA_NUM_PARALLEL="4"
    export GDCS_OLLAMA_TEST_NUM_PREDICT="128"
    EOF
    

  1. Source the environment file:
         
         source ${HOME}/gdcag-solutions/open-weight-models/ollama/gemma/env.sh
         




### Cluster

  1. Retrieve cluster credentials:
         
         gdcloud clusters get-credentials "${GDC_STANDARD_CLUSTER_NAME}" \
         --project="${GDC_PROJECT}"
         

  2. Verify that the accelerator resource type of the accelerator environment file is available in the cluster:
         
         kubectl get nodes \
         -o custom-columns='NAME:.metadata.name,ACCELERATOR:.status.allocatable.'"${GDCS_WORKLOAD_ACCELERATOR_TYPE}"
         

**Note:** If the resource count is 0 or `<none>`, either the cluster doesn't have nodes with this GPU type or the node pool is still creating. Check the available types with `kubectl get nodes -L node.cluster.private.gdc.goog/machine-class`. To use a different GPU, set `GDCS_WORKLOAD_ACCELERATOR_TYPE` in `env.d/accelerator.sh` to one of the listed resource types, source the environment again, and re-run this step.



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

  1. Download the model weights:
         
         ${GDCS_IMPLEMENTATION_HOME}/ollama_model_weight_download.sh
         

  2. Calculate the required `PersistentVolumeClaim` size from the downloaded model weights with 25% overhead (rounded up to the next whole GiB):
         
         MODEL_KIB=$(du -sk "${GDCS_OLLAMA_MODEL_DOWNLOAD_DIR}" | awk '{print $1}')
         export GDCS_MODEL_PVC_SIZE="$(( (MODEL_KIB * 125 / 100 + 1048575) / 1048576 ))Gi"
         echo "GDCS_MODEL_PVC_SIZE=${GDCS_MODEL_PVC_SIZE}"
         

  3. Create the manifest for the `PersistentVolumeClaim` for the model weights:
         
         cat <<EOF > "${GDCS_USER_GUIDE_HOME}/${GDCS_WORKLOAD_NAME}-pvc.yaml" && echo "Successfully created." || echo "Failed to create!"
         apiVersion: v1
         kind: PersistentVolumeClaim
         metadata:
           name: ${GDCS_WORKLOAD_NAME}-rwo
           namespace: ${GDCS_WORKLOAD_NAMESPACE}
         spec:
           accessModes:
             - ReadWriteOnce
           resources:
             requests:
               storage: ${GDCS_MODEL_PVC_SIZE}
         EOF
         

  4. Apply the manifest for the `PersistentVolumeClaim` for the model weights:
         
         kubectl apply --filename="${GDCS_USER_GUIDE_HOME}/${GDCS_WORKLOAD_NAME}-pvc.yaml"
         

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
  7. Create the manifest for the model loader `Pod`:
         
         cat <<EOF > "${GDCS_USER_GUIDE_HOME}/${GDCS_WORKLOAD_NAME}-loader.yaml" && echo "Successfully created." || echo "Failed to create!"
         apiVersion: v1
         kind: Pod
         metadata:
           name: ${GDCS_MODEL_LOADER_POD_NAME}
           namespace: ${GDCS_WORKLOAD_NAMESPACE}
         spec:
           containers:
             - command: ["/bin/sh", "-c", "trap 'exit 0' TERM; while :; do sleep 1; done"]
               image: ${GDCS_HARBOR_PROJECT_URI}/busybox/busybox:${GDCS_BUSYBOX_IMAGE_TAG}
               imagePullPolicy: IfNotPresent
               name: loader
               volumeMounts:
                 - mountPath: ${GDCS_OLLAMA_PV_MOUNT_PATH}
                   name: model-cache
           imagePullSecrets:
             - name: ${GDCS_HARBOR_K8S_PULL_SECRET}
           restartPolicy: Never
           volumes:
             - name: model-cache
               persistentVolumeClaim:
                 claimName: ${GDCS_WORKLOAD_NAME}-rwo
         EOF
         

  8. Apply the manifest for the model loader `Pod`:
         
         kubectl apply --filename="${GDCS_USER_GUIDE_HOME}/${GDCS_WORKLOAD_NAME}-loader.yaml"
         

  9. Wait for the model loader `Pod` to be Running:
         
         kubectl wait \
         --for=jsonpath='{.status.phase}'=Running \
         "pod/${GDCS_MODEL_LOADER_POD_NAME}" \
         --namespace="${GDCS_WORKLOAD_NAMESPACE}" \
         --timeout=120s
         

  10. Upload the model weights:
         
         ${GDCS_IMPLEMENTATION_HOME}/model_weight_upload.sh \
         --local-dir="${GDCS_OLLAMA_MODEL_DOWNLOAD_DIR}" \
         --pod="${GDCS_MODEL_LOADER_POD_NAME}" \
         --target-dir="${GDCS_OLLAMA_PV_MOUNT_PATH}"
         

  11. Delete the model loader `Pod`:
         
         kubectl delete pod "${GDCS_MODEL_LOADER_POD_NAME}" \
         --namespace="${GDCS_WORKLOAD_NAMESPACE}"
         




### Inference server

  1. Create the manifest for the Ollama `Deployment`:
         
         cat <<EOF > "${GDCS_USER_GUIDE_HOME}/${GDCS_WORKLOAD_NAME}-deployment.yaml" && echo "Successfully created." || echo "Failed to create!"
         apiVersion: v1
         kind: ConfigMap
         metadata:
           name: ${GDCS_WORKLOAD_NAME}
         data:
           OLLAMA_FLASH_ATTENTION: "1"
           OLLAMA_HOST: "0.0.0.0"
           OLLAMA_KEEP_ALIVE: "-1"
           OLLAMA_MODELS: "${GDCS_OLLAMA_PV_MOUNT_PATH}"
           OLLAMA_NUM_PARALLEL: "${GDCS_OLLAMA_NUM_PARALLEL}"
           OLLAMA_ORIGINS: "*"
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
                 - envFrom:
                     - configMapRef:
                         name: ${GDCS_WORKLOAD_NAME}
                   image: ${GDCS_HARBOR_PROJECT_URI}/ollama/ollama:${GDCS_OLLAMA_IMAGE_TAG}
                   imagePullPolicy: IfNotPresent
                   lifecycle:
                     postStart:
                       exec:
                         command:
                           - /bin/sh
                           - -c
                           - |
                             echo "Waiting for local API to respond..."
                             timeout=60
                             until /bin/ollama list > /dev/null 2>&1 || [ "\$timeout" -le 0 ]; do
                               sleep 1
                               timeout=\$((timeout - 1))
                             done
                             if [ "\$timeout" -le 0 ]; then
                               echo "Timed out waiting for Ollama server to start." >&2
                               exit 1
                             fi
                             echo "Preloading model into memory..."
                             /bin/ollama run "${GDCS_OLLAMA_MODEL}" ""
                   livenessProbe:
                     failureThreshold: 3
                     httpGet:
                       path: /
                       port: 11434
                     periodSeconds: 30
                     timeoutSeconds: 10
                   name: ollama
                   ports:
                     - containerPort: 11434
                       name: http-ollama
                   readinessProbe:
                     failureThreshold: 3
                     httpGet:
                       path: /api/tags
                       port: 11434
                     periodSeconds: 10
                     successThreshold: 1
                     timeoutSeconds: 5
                   resources:
                     limits:
                       cpu: ${GDCS_WORKLOAD_CPU_LIMIT}
                       memory: ${GDCS_WORKLOAD_MEMORY_LIMIT}
                       ${GDCS_WORKLOAD_ACCELERATOR_TYPE}: "${GDCS_WORKLOAD_ACCELERATOR_COUNT}"
                     requests:
                       cpu: ${GDCS_WORKLOAD_CPU_REQUEST}
                       memory: ${GDCS_WORKLOAD_MEMORY_REQUEST}
                       ${GDCS_WORKLOAD_ACCELERATOR_TYPE}: "${GDCS_WORKLOAD_ACCELERATOR_COUNT}"
                   securityContext:
                     allowPrivilegeEscalation: false
                     seLinuxOptions:
                       type: spc_t
                   startupProbe:
                     failureThreshold: 60
                     httpGet:
                       path: /
                       port: 11434
                     periodSeconds: 10
                     timeoutSeconds: 5
                   volumeMounts:
                     - mountPath: ${GDCS_OLLAMA_PV_MOUNT_PATH}
                       name: model-cache
                     - mountPath: /dev/shm
                       name: shm
               imagePullSecrets:
                 - name: ${GDCS_HARBOR_K8S_PULL_SECRET}
               volumes:
                 - name: model-cache
                   persistentVolumeClaim:
                     claimName: ${GDCS_WORKLOAD_NAME}-rwo
                 - emptyDir:
                     medium: Memory
                     sizeLimit: "8Gi"
                   name: shm
         ---
         apiVersion: v1
         kind: Service
         metadata:
           name: ${GDCS_WORKLOAD_NAME}
         spec:
           ports:
             - name: http-ollama
               port: 80
               protocol: TCP
               targetPort: 11434
           selector:
             app: ${GDCS_WORKLOAD_NAME}
           type: LoadBalancer
         EOF
         

  2. Apply the manifest for the Ollama `Deployment`:
         
         kubectl apply --filename="${GDCS_USER_GUIDE_HOME}/${GDCS_WORKLOAD_NAME}-deployment.yaml" --namespace="${GDCS_WORKLOAD_NAMESPACE}"
         

  3. Create the manifest for the Ollama `NetworkPolicy`:
         
         cat <<EOF > "${GDCS_USER_GUIDE_HOME}/ollama-netpol.yaml" && echo "Successfully created." || echo "Failed to create!"
         apiVersion: networking.k8s.io/v1
         kind: NetworkPolicy
         metadata:
           name: allow-ollama-ingress
           namespace: ${GDCS_WORKLOAD_NAMESPACE}
         spec:
           ingress:
           - from:
             - ipBlock:
                 cidr: 0.0.0.0/0
             - namespaceSelector: {}
             ports:
             - port: 11434
               protocol: TCP
           podSelector: {}
           policyTypes:
           - Ingress
         EOF
         

  4. Apply the manifest for the Ollama `NetworkPolicy`:
         
         kubectl apply --filename="${GDCS_USER_GUIDE_HOME}/ollama-netpol.yaml"
         

  5. Wait for the `Pod` to be Running:
         
         kubectl wait \
         --for=jsonpath='{.status.phase}'=Running \
         "pod" \
         --selector="app=${GDCS_WORKLOAD_NAME}" \
         --namespace="${GDCS_WORKLOAD_NAMESPACE}" \
         --timeout=300s
         

  6. Wait for the `Deployment` to be Ready:
         
         kubectl wait \
         --for=condition=Available \
         "deployment/${GDCS_WORKLOAD_NAME}" \
         --namespace="${GDCS_WORKLOAD_NAMESPACE}" \
         --timeout=600s
         

  7. Optional: Stream the container logs to monitor startup progress:
         
         kubectl logs deployment/${GDCS_WORKLOAD_NAME} \
         --follow \
         --namespace="${GDCS_WORKLOAD_NAMESPACE}"
         




## Validation

  1. Retrieve the LoadBalancer IP address for Ollama:
         
         export OLLAMA_LB_IP=$(kubectl get service/${GDCS_WORKLOAD_NAME} --namespace="${GDCS_WORKLOAD_NAMESPACE}" --output=jsonpath='{.status.loadBalancer.ingress[*].ip}')
         echo "OLLAMA_LB_IP=${OLLAMA_LB_IP}"
         

  2. Send a test request to Ollama using the load balancer (Ollama API, text generation):
         
         curl http://${OLLAMA_LB_IP}/api/generate \
         -H "Content-Type: application/json" \
         -d '{
           "model": "'${GDCS_OLLAMA_MODEL}'",
           "prompt": "Explain Google Distributed Cloud air-gapped briefly.",
           "stream": false
         }'
         

  3. Send a streaming test request:
         
         curl http://${OLLAMA_LB_IP}/api/generate \
         -H "Content-Type: application/json" \
         -d '{
           "model": "'${GDCS_OLLAMA_MODEL}'",
           "prompt": "Explain Google Distributed Cloud air-gapped briefly.",
           "stream": true
         }'
         

  4. Send a test request to the OpenAI-compatible API of Ollama using the load balancer:
         
         curl http://${OLLAMA_LB_IP}/v1/chat/completions \
         -H "Content-Type: application/json" \
         -d '{
           "model": "'${GDCS_OLLAMA_MODEL}'",
           "messages": [
             {"role": "user", "content": "Explain Google Distributed Cloud air-gapped briefly."}
           ]
         }'
         

  5. Send a test request to Ollama using port forwarding:
         
         kubectl port-forward service/${GDCS_WORKLOAD_NAME} \
         --namespace="${GDCS_WORKLOAD_NAMESPACE}" 11434:80 &
         PF_PID=$!
         
         sleep 1
         
         curl http://127.0.0.1:11434/api/tags
         
         kill ${PF_PID}
         

**Note:** Gemma 4 is a thinking model. On the OpenAI-compatible endpoint the reasoning is returned in `choices[0].message.reasoning` and counts against `max_tokens`; with a small budget `content` can stay empty. Use the Ollama-specific `/api/chat` endpoint with `"think": false`, or a larger `max_tokens`, when a visible answer is required.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
