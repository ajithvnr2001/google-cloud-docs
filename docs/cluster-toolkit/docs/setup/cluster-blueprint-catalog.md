---
url: https://docs.cloud.google.com/cluster-toolkit/docs/setup/cluster-blueprint-catalog/
title: Cluster blueprint catalog \u00a0|\u00a0 Cluster Toolkit \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T12:23:08.949100+00:00
---

# Cluster blueprint catalog  |  Cluster Toolkit  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/cluster-toolkit/docs/setup/cluster-blueprint-catalog/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ Cluster Toolkit ](https://docs.cloud.google.com/cluster-toolkit/docs)
  * [ Guides ](https://docs.cloud.google.com/cluster-toolkit/docs/overview)



Send feedback 

#  Cluster blueprint catalog Stay organized with collections  Save and categorize content based on your preferences. 

This page describes Google's catalog of cluster blueprints, which are reusable YAML configuration files for deploying specific, opinionated solutions with the Cluster Toolkit. Each blueprint defines a specific environment, including the scheduler, storage, machine types, and base operating system. By default, cluster blueprints use a Rocky Linux 9 OS image.

You can filter the catalog by your required scheduler, storage, machine types, and base operating system. Each entry highlights featured applications and Google Cloud resources that the blueprint leverages.

A cluster blueprint is a `YAML` file that defines a reusable configuration and describes the specific environment that you want to deploy using Cluster Toolkit. A cluster blueprint implements and documents a specific opinionated solution. For more information about cluster blueprints, see [Cluster blueprints](https://docs.cloud.google.com/cluster-toolkit/docs/setup/cluster-blueprint).

To search the catalog, you can filter by a combination of your required scheduler, storage, machine types, and base operating system. For machine types that have NVIDIA GPUs automatically attached, the GPU type is listed in brackets. For each cluster blueprint, featured applications and Google Cloud resources that can be leveraged by using the blueprint are also highlighted.

BatchGKESlurmHTCondorNoneCloud StorageFilestoreGoogle Cloud Managed LustreLocal SSDgke-persistent-volumegke-storagepre-existing-network-storageNoneA4X Max (NVIDIA GB300)A4 (NVIDIA B200)A4X (NVIDIA GB200 Superchips)A3 Ultra (NVIDIA H200)A3 Mega (NVIDIA H100)A3 High (NVIDIA H100)A2 (NVIDIA A100)C2 C2DC3E2G4 (NVIDIA RTX PRO 6000)G2 (NVIDIA L4)H4DH3N2N1TPUv4TPU v6eTPU7xContainer-Optimized OSdebian-12hpc-centos-7hpc-rocky-linux-8hpc-rocky-linux-9rocky-linux-9-optimized-gcprocky-linux-9slurm-gcp-6-4-tf-2.14.0ubuntu-2004-ltsubuntu-2204-ltsubuntu-2404-ltsubuntu-accelerator-2404-amd64-with-nvidia-580ubuntu-accelerator-2404-arm64-with-nvidia-580Advanced Compute ImagesAnsys FluentBare metalGPUsTPUsGROMACSJAXKueueJobsetMaxtextNCCLNVIDIA IMEXOpenFoamPackerPyTorchQSimSpackStar CCM+TensorFlowVDI with VMDWRF

Clear all

**Cluster blueprint** | **Guide** | **Scheduler** | **Storage** | **Machine types** | **Base operating system** | **Featured software and compute resources** | **Collection**  
---|---|---|---|---|---|---|---  
[a4x-maxgpu-4g-metal](https://github.com/GoogleCloudPlatform/cluster-toolkit/tree/main/examples/machine-learning/a4x-maxgpu-4g-metal) | [A4X Max for Slurm](https://docs.cloud.google.com/cluster-toolkit/docs/deploy/slurm/create-a4x-max-cluster) | Slurm | Cloud Storage, Google Cloud Managed Lustre | A4X Max | `ubuntu-accelerator-2404-arm64-with-nvidia-580` | 

  * NVIDIA ConnectX-8
  * Bare metal
  * NVIDIA IMEX
  * GPUs
  * RDMA

| Core  
[gke-a4x-max-bm](https://github.com/GoogleCloudPlatform/cluster-toolkit/tree/main/examples/gke-a4x-max-bm) | [A4X Max for GKE](https://docs.cloud.google.com/cluster-toolkit/docs/deploy/gke/create-a4x-max-cluster) | GKE | Filestore, Cloud Storage | A4X Max | Container-Optimized OS | 

  * NVIDIA ConnectX-8
  * Bare metal
  * GPUs
  * Jobset
  * Kueue

| Core  
[gke-tpu-7x](https://github.com/GoogleCloudPlatform/cluster-toolkit/tree/main/examples/gke-tpu-7x) | [TPU 7x for GKE](https://docs.cloud.google.com/cluster-toolkit/docs/deploy/gke/gke-tpu-7x) | GKE | None | TPU7x | Container-Optimized OS | 

  * TPUs
  * Jobset
  * Kueue
  * JAX
  * Multi-VPC Networking

| Core  
[gke-tpu-v6e](https://github.com/GoogleCloudPlatform/cluster-toolkit/tree/main/examples/gke-tpu-v6e) | [TPU v6e for GKE](https://docs.cloud.google.com/cluster-toolkit/docs/deploy/gke/gke-tpu-v6e) | GKE | None | TPU v6e | Container-Optimized OS | 

  * TPUs
  * Jobset
  * Kueue
  * JAX
  * Multi-VPC Networking

| Core  
[a4-highgpu-8g](https://github.com/GoogleCloudPlatform/cluster-toolkit/tree/main/examples/machine-learning/a4-highgpu-8g) | [A4 for Slurm](https://docs.cloud.google.com/cluster-toolkit/docs/deploy/slurm/create-a4-cluster) | Slurm | Filestore, Cloud Storage, Google Cloud Managed Lustre | A4  | `ubuntu-2404-lts` | 

  * Advanced Compute Images
  * NVIDIA ConnectX-7
  * Google Virtual NIC (gVNIC)
  * GPUs
  * Virtual Private Cloud

| Core  
[a4x-highgpu-4g](https://github.com/GoogleCloudPlatform/cluster-toolkit/tree/main/examples/machine-learning/a4x-highgpu-4g) | [A4X for Slurm](https://docs.cloud.google.com/cluster-toolkit/docs/deploy/slurm/create-a4x-cluster) | Slurm | Cloud Storage, Google Cloud Managed Lustre | A4X | `ubuntu-2404-lts` | 

  * Advanced Compute Images
  * NVIDIA ConnectX-7
  * Google Virtual NIC (gVNIC)
  * NVIDIA IMEX
  * GPUs

| Core  
[gke-a4x](https://github.com/GoogleCloudPlatform/cluster-toolkit/tree/main/examples/gke-a4x) | [A4X for GKE](https://docs.cloud.google.com/cluster-toolkit/docs/deploy/gke/create-a4x-cluster) | GKE | Cloud Storage, gke-persistent-volume | A4X | Container-Optimized OS | 

  * GPUs
  * Jobset
  * Kueue

| Core  
[gke-a3-ultragpu](https://github.com/GoogleCloudPlatform/cluster-toolkit/tree/main/examples/gke-a3-ultragpu) | [A3 Ultra for GKE](https://docs.cloud.google.com/cluster-toolkit/docs/deploy/gke/create-a3-ultra-cluster) | GKE | Filestore, Cloud Storage | A3 Ultra | Container-Optimized OS | 

  * NVIDIA ConnectX-7
  * Google Virtual NIC (gVNIC)
  * GPUs

| Core  
[ gke-a3-highgpu](https://github.com/GoogleCloudPlatform/cluster-toolkit/tree/main/examples/gke-a3-highgpu) |  [ A3 High for GKE](https://docs.cloud.google.com/cluster-toolkit/docs/deploy/gke/create-a3-high-cluster) | GKE | None | A3 High | Container-Optimized OS | 

  * GPUs
  * JobSet
  * Kueue

| Core  
[ gke-a3-megagpu](https://github.com/GoogleCloudPlatform/cluster-toolkit/tree/main/examples/gke-a3-megagpu) |  [ A3 Mega for GKE](https://docs.cloud.google.com/cluster-toolkit/docs/deploy/gke/deploy-a3-mega-gke-cluster) | GKE | None | A3 Mega | Container-Optimized OS | 

  * GPUs
  * JobSet
  * Kueue

| Core  
[gke-managed-hyperdisk](https://github.com/GoogleCloudPlatform/cluster-toolkit/tree/main/examples/README.md#gke-managed-hyperdiskyaml--) |  | GKE | gke-storage | C3 | Container-Optimized OS |  | Core, Experimental  
[gke-managed-lustre](https://github.com/GoogleCloudPlatform/cluster-toolkit/tree/main/examples/README.md#gke-managed-lustreyaml-) |  | GKE | Google Cloud Managed Lustre | N2 | Container-Optimized OS |  | Core  
[gke-a4](https://github.com/GoogleCloudPlatform/cluster-toolkit/tree/main/examples/gke-a4) | [A4 for GKE](https://docs.cloud.google.com/cluster-toolkit/docs/deploy/gke/create-a4-cluster) | GKE | Filestore, Cloud Storage, gke-persistent-volume | A4  | Container-Optimized OS | 

  * GPUs
  * Jobset
  * Kueue

| Core  
[gke-g4](https://github.com/GoogleCloudPlatform/cluster-toolkit/tree/main/examples/gke-g4) |  | GKE | None | G4 | Container-Optimized OS | 

  * GPUs
  * Jobset
  * Kueue

| Core  
[gke-h4d](https://github.com/GoogleCloudPlatform/cluster-toolkit/tree/main/examples/gke-h4d) |  | GKE | Filestore, gke-persistent-volume | H4D | Container-Optimized OS | 

  * Google Virtual NIC (gVNIC) and Cloud RDMA
  * Kueue and Jobset
  * Service account

| Core  
[a3-ultragpu-8g](https://github.com/GoogleCloudPlatform/cluster-toolkit/tree/main/examples/machine-learning/a3-ultragpu-8g) | [A3 Ultra for Slurm](https://docs.cloud.google.com/cluster-toolkit/docs/deploy/slurm/create-a3-ultra-cluster) | Slurm | Cloud Storage, Google Cloud Managed Lustre | A3 Ultra | `ubuntu-2404-lts` | 

  * Advanced Compute Images
  * NVIDIA ConnectX-7
  * Google Virtual NIC (gVNIC)
  * GPUs

| Core  
[a3-highgpu-8g](https://github.com/GoogleCloudPlatform/cluster-toolkit/tree/main/examples/machine-learning/a3-highgpu-8g) | [A3 High for Slurm](https://docs.cloud.google.com/cluster-toolkit/docs/deploy/slurm/create-a3-high-cluster) | Slurm | Filestore, Cloud Storage | A3 High | `ubuntu-2204-lts*` | 

  * Google Virtual NIC (gVNIC)
  * GPUs

| Core  
[a3-megagpu-8g](https://github.com/GoogleCloudPlatform/cluster-toolkit/tree/main/examples/machine-learning/a3-megagpu-8g) | [A3 Mega for Slurm](https://docs.cloud.google.com/cluster-toolkit/docs/deploy/slurm/deploy-a3-mega-cluster) | Slurm | Filestore, Cloud Storage | A3 Mega | `ubuntu-accelerator-2404-amd64-with-nvidia-580` | 

  * Google Virtual NIC (gVNIC)
  * GPUs

| Core  
[h4d-vm](https://github.com/GoogleCloudPlatform/cluster-toolkit/blob/main/examples/h4d-vm.yaml) |  | None | Filestore, Local SSD | H4D | hpc-rocky-linux-9 | 

  * Google Virtual NIC (gVNIC)
  * Cloud RDMA

| Core, Experimental  
[hpc-slurm-h4d](https://github.com/GoogleCloudPlatform/cluster-toolkit/blob/main/examples/hpc-slurm-h4d/) | [RDMA cluster with H4D](https://docs.cloud.google.com/cluster-toolkit/docs/quickstarts/create-a-slurm-cluster-h4d) | Slurm | Filestore, Local SSD | N2, H4D | hpc-rocky-linux-9 | 

  * Google Virtual NIC (gVNIC)
  * Cloud RDMA

| Core  
[hpc-slurm](https://github.com/GoogleCloudPlatform/cluster-toolkit/blob/main/examples/README.md#hpc-slurmyaml-) | [Slurm cluster](https://docs.cloud.google.com/cluster-toolkit/docs/quickstarts/slurm-cluster) | Slurm | Filestore | N2, C2, H3 | `hpc-rocky-linux-9*` |  | Core  
[hpc-slurm6-tpu-maxtext](https://github.com/GoogleCloudPlatform/cluster-toolkit/tree/main/examples#hpc-slurm6-tpu-maxtextyaml--) |  | Slurm | None | TPUv4, N2, C2  | `slurm-gcp-6-4-tf-2.14.0*` | 

  * TPUs
  * Maxtext

| Community, Experimental  
[ml-slurm](https://github.com/GoogleCloudPlatform/cluster-toolkit/blob/main/examples/README.md#ml-slurmyaml-) |  | Slurm | Filestore | N2, A2, G2 | `debian-12*` | 

  * GPUs
  * NCCL
  * PyTorch
  * TensorFlow

| Core  
[batch](https://github.com/GoogleCloudPlatform/cluster-toolkit/blob/main/examples/README.md#batchyaml-) |  | Batch | Filestore | N2 | `rocky-linux-9-optimized-gcp` |  | Core  
[batch-mpi](https://github.com/GoogleCloudPlatform/cluster-toolkit/tree/main/examples#batch-mpiyaml-) |  | Batch | Filestore | C2  | `hpc-rocky-linux-9` | 

  * Spack
  * Weather Research and Forecasting (WRF)

| Core  
[tutorial-starccm](https://github.com/GoogleCloudPlatform/cluster-toolkit/blob/main/community/examples/tutorial-starccm.yaml) | [Simcenter STAR CCM+](https://docs.cloud.google.com/cluster-toolkit/docs/simcenter-star-ccm/run-workload) | None | Filestore | C2  | `hpc-centos-7` | 

  * Star CCM+

| Community, Experimental  
[tutorial-fluent](https://github.com/GoogleCloudPlatform/cluster-toolkit/blob/main/community/examples/tutorial-fluent.yaml) | [Ansys Fluent](https://docs.cloud.google.com/cluster-toolkit/docs/tutorials/ansys-fluent) | None | Filestore | C2  | `hpc-rocky-linux-9` | 

  * Ansys Fluent

| Community, Experimental  
[image-builder](https://github.com/GoogleCloudPlatform/cluster-toolkit/blob/main/examples/README.md#image-builderyaml-) |  | Slurm | None | C2, N2 | `hpc-rocky-linux-9*` | 

  * Packer

| Core  
[hpc-build-slurm-image](https://github.com/GoogleCloudPlatform/cluster-toolkit/blob/main/examples/README.md#hpc-build-slurm-imageyaml--) |  | Slurm | None | N2D | `hpc-rocky-linux-9*` | 

  * Packer
  * Building Slurm

| Community, Experimental  
[hpc-amd-slurm](https://github.com/GoogleCloudPlatform/cluster-toolkit/blob/main/community/examples/AMD/README.md) |  | Slurm | Filestore | C2D | `hpc-rocky-linux-9*` | 

  * AMD
  * AMD Optimizing C/C++ and Fortran Compilers (AOCC)
  * OpenFoam
  * Spack

| Community  
[hpc-slurm-local-ssd](https://github.com/GoogleCloudPlatform/cluster-toolkit/blob/main/examples/README.md#hpc-slurm-local-ssdyaml--) |  | Slurm | Filestore, Local SSD | N1 | `hpc-rocky-linux-9*` | 


| Community, Experimental  
[hpc-slurm-ubuntu2204](https://github.com/GoogleCloudPlatform/cluster-toolkit/blob/main/community/examples/hpc-slurm-ubuntu2204.yaml) |  | Slurm | Filestore | N2, C2  | `ubuntu-2204-lts` |  | Community  
[hpc-slurm-gromacs](https://github.com/GoogleCloudPlatform/cluster-toolkit/blob/main/examples/README.md#hpc-slurm-gromacsyaml--) |  | Slurm | Filestore | C2  | `hpc-rocky-linux-9*` | 

  * GROMACS
  * Spack

| Community, Experimental  
[hpc-slurm-hcls](https://github.com/GoogleCloudPlatform/cluster-toolkit/tree/main/docs/videos/healthcare-and-life-sciences) |  | Slurm | Cloud Storage, Filestore | A2, C2  | `hpc-rocky-linux-9*` | 

  * GPUs
  * GROMACS on GPUs
  * Spack
  * VDI with VMD

| Community  
[htc-htcondor](https://github.com/GoogleCloudPlatform/cluster-toolkit/blob/main/examples/README.md#htc-htcondoryaml--) |  | HTCondor | None | C2  | `hpc-rocky-linux-8` |  | Community, Experimental  
[ml-gke](https://github.com/GoogleCloudPlatform/cluster-toolkit/blob/main/examples/README.md#ml-gkeyaml-) |  | GKE | None | G2 | Container-Optimized OS | 

  * GPUs

| Core  
[hpc-gke](https://github.com/GoogleCloudPlatform/cluster-toolkit/blob/main/examples/README.md#hpc-gkeyaml-) |  | GKE | None | N2, C2  | Container-Optimized OS |  | Core  
[storage-gke](https://github.com/GoogleCloudPlatform/cluster-toolkit/blob/main/examples/README.md#storage-gkeyaml-) |  | GKE | Filestore, Local SSD, Cloud Storage, gke-persistent-volume | N2D | Container-Optimized OS | 

  * CSI Drivers
  * Persistent Volumes

| Core  
[client-google-cloud-storage](https://github.com/GoogleCloudPlatform/cluster-toolkit/blob/main/examples/README.md#client-google-cloud-storageyaml--) |  | None | Cloud Storage, pre-existing-network-storage | E2 | `hpc-rocky-linux-9` |  | Community, Experimental  
[hpc-slurm-sharedvpc](https://github.com/GoogleCloudPlatform/cluster-toolkit/blob/main/examples/README.md#hpc-slurm-sharedvpcyaml--) |  | Slurm | Filestore | N2, C2  | `hpc-rocky-linux-9*` | 

  * Shared VPC configuration

| Community, Experimental  
  
*This OS image is an optimized Schedmd's Slurm image that is based on the specified operating system.

†This OS image has DAOS drivers pre-installed and needs to be built following instructions in the DAOS project.

## What's next

  * To set up your environment, see [Set up Cluster Toolkit](https://docs.cloud.google.com/cluster-toolkit/docs/setup/configure-environment).
  * To learn about the deployment process, see [Cluster deployment overview](https://docs.cloud.google.com/cluster-toolkit/docs/deploy/deploy-cluster-overview).
  * To change the functionality of your blueprints using modules, see [Modules](https://docs.cloud.google.com/cluster-toolkit/docs/modules/overview).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-16 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-16 UTC."],[],[]] 
