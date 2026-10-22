---
url: https://docs.cloud.google.com/cluster-toolkit/docs/modules/module-list-overview/
title: Supported modules \u00a0|\u00a0 Cluster Toolkit \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:25:23.974989+00:00
---

# Supported modules  |  Cluster Toolkit  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/cluster-toolkit/docs/modules/module-list-overview/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ Cluster Toolkit ](https://docs.cloud.google.com/cluster-toolkit/docs)
  * [ Guides ](https://docs.cloud.google.com/cluster-toolkit/docs/overview)



Send feedback 

#  Supported modules Stay organized with collections  Save and categorize content based on your preferences. 

This document describes the core module categories that are supported by Cluster Toolkit. Use these references to identify the right building blocks to construct a deployment tailored to your specific workload requirements.

For more information about module concepts and structure, see [Modules](https://docs.cloud.google.com/cluster-toolkit/docs/modules/overview).

For a complete list of supported modules, including experimental and community modules, see the [modules page](https://github.com/GoogleCloudPlatform/cluster-toolkit/tree/main/modules) in the Cluster Toolkit GitHub repository.

## Compute modules

Compute modules define the processing power of your cluster, including Compute Engine instances and autoscaling groups. Use these modules to provision resources that are optimized for your specific workloads, such as high performance computing (HPC) or AI/ML training.

The following modules let you configure compute resources:

  * [Create compute instances](https://docs.cloud.google.com/cluster-toolkit/docs/modules/vm-instances): This module creates one or more compute instances and configures options such as networking, storage, and placement policies.
  * [Create a Google Kubernetes Engine node pool](https://docs.cloud.google.com/cluster-toolkit/docs/modules/gke-node-pool): This module creates a GKE node pool and configures options such as autoscaling, local SSD storage, and GPU acceleration.
  * [Create a Google Kubernetes Engine job template](https://docs.cloud.google.com/cluster-toolkit/docs/modules/gke-job-template): This module creates a Kubernetes job template file configured to run on specified node pools, with support for shared and ephemeral storage.
  * [Create a resource policy](https://docs.cloud.google.com/cluster-toolkit/docs/modules/resource-policy): This module creates a Compute Engine resource policy that defines placement constraints for compute instances or GKE nodes.
  * [Deploy a Cloud Run service](https://docs.cloud.google.com/cluster-toolkit/docs/modules/cloud-run): This module deploys a Cloud Run service.



### Slurm compute resources

If you use the Slurm scheduler, then use specific modules to define the partitions and node sets that make up your cluster:

  * [Create a partition for a Slurm controller](https://docs.cloud.google.com/cluster-toolkit/docs/modules/slurm-partition): This module creates a compute partition composed of one or more nodesets and configures scheduling options such as job exclusivity and power management.
  * [Create a nodeset for a Slurm partition](https://docs.cloud.google.com/cluster-toolkit/docs/modules/slurm-nodeset): This module defines a set of compute nodes with specific hardware configurations, letting you build heterogeneous Slurm partitions by grouping multiple nodesets together.
  * [Create a TPU nodeset for a Slurm partition](https://docs.cloud.google.com/cluster-toolkit/docs/modules/slurm-nodeset-tpu): This module defines a nodeset of Tensor Processing Units (TPUs) to be used in a Slurm partition, that let you accelerate machine learning workloads with Google's custom Application-Specific Integrated Circuits (ASICs).
  * [Create a dynamic nodeset for a Slurm partition](https://docs.cloud.google.com/cluster-toolkit/docs/modules/slurm-nodeset-dynamic): This module creates an instance template and a dynamic nodeset configuration, letting your Slurm partition provision compute nodes on demand.



## Scheduler modules

Scheduler modules deploy and configure the workload managers that orchestrate your jobs. These modules handle the setup of controller nodes, login nodes, and the necessary software to manage job queues.

The following modules let you configure schedulers:

  * [Create a Batch job template](https://docs.cloud.google.com/cluster-toolkit/docs/modules/batch-job-template): This module creates a Google Cloud Batch job template and an associated instance template to configure compute resources, networking, and storage options.
  * [Create a Batch login node](https://docs.cloud.google.com/cluster-toolkit/docs/modules/batch-login-node): This module provisions a login node instance that mirrors the configuration of your Batch job, letting you test workloads and submit jobs.
  * [Create a GKE cluster](https://docs.cloud.google.com/cluster-toolkit/docs/modules/gke-cluster): This module creates a GKE cluster and configures options such as VPC-native networking, multi-networking, and inference gateways.
  * [Use an existing GKE cluster](https://docs.cloud.google.com/cluster-toolkit/docs/modules/pre-existing-gke-cluster): This module discovers an existing GKE cluster and outputs its attributes, letting you use the existing cluster as a drop-in substitute for a new cluster in your blueprints.
  * [Create a Slurm controller node](https://docs.cloud.google.com/cluster-toolkit/docs/modules/slurm-controller): This module deploys a Slurm controller node to orchestrate jobs and manage the cluster, with support for live reconfiguration and scheduled maintenance.
  * [Create a Slurm login node](https://docs.cloud.google.com/cluster-toolkit/docs/modules/slurm-login-node): This module creates a login node for a Slurm cluster to provide an access point for users to submit jobs and interact with the controller.



## File system modules

File system modules provision shared storage resources that your cluster nodes can access. These modules let you mount high-performance storage solutions for data-intensive applications.

The following modules let you configure storage:

  * [Create a Cloud Storage bucket](https://docs.cloud.google.com/cluster-toolkit/docs/modules/cloud-storage-bucket): This module creates a Cloud Storage bucket to provide scalable object storage for your cluster, with options to configure encryption and lifecycle rules.
  * [Create a Managed Lustre instance](https://docs.cloud.google.com/cluster-toolkit/docs/modules/managed-lustre-instance): This module creates a Google Cloud Managed Lustre instance to provide a high-performance network file system that you can mount to your cluster nodes, with options to import data from Cloud Storage.
  * [Create a Filestore instance](https://docs.cloud.google.com/cluster-toolkit/docs/modules/filestore-instance): This module creates a Filestore instance to provide high-performance network file storage for your compute instances and GKE clusters.
  * [Create a NetApp Volumes storage pool](https://docs.cloud.google.com/cluster-toolkit/docs/modules/netapp-storage-pool): This module creates a Google Cloud NetApp Volumes storage pool to provide managed file storage services.
  * [Create a NetApp Volumes](https://docs.cloud.google.com/cluster-toolkit/docs/modules/netapp-volume): This module creates a Google Cloud NetApp Volumes volume within a storage pool, letting you mount high-performance NFS or SMB shares to your nodes.
  * [Create a Google Kubernetes Engine persistent volume](https://docs.cloud.google.com/cluster-toolkit/docs/modules/gke-persistent-volume): This module creates Kubernetes Persistent Volume (PV) and Persistent Volume Claim (PVC) resources to connect storage modules to GKE jobs.
  * [Create a Google Kubernetes Engine storage class](https://docs.cloud.google.com/cluster-toolkit/docs/modules/gke-storage): This module creates a Kubernetes StorageClass (SC) to dynamically provision Google Cloud storage resources for GKE clusters.
  * [Use pre-existing network storage](https://docs.cloud.google.com/cluster-toolkit/docs/modules/pre-existing-network-storage): This module configures access to an existing file system, such as Network File System (NFS), Managed Lustre, or Cloud Storage, that lets you mount external storage resources to your cluster nodes.



## Networking modules

Networking modules define the connectivity layer of your cluster. Use these modules to create isolated networks, configure firewalls, or integrate your cluster into an existing VPC.

The following modules let you configure networking:

  * [Create a VPC network](https://docs.cloud.google.com/cluster-toolkit/docs/modules/vpc): This module creates a new VPC network with subnetworks and configures a Cloud Router, Cloud NAT, and firewall rules for connectivity.
  * [Create multiple VPC networks](https://docs.cloud.google.com/cluster-toolkit/docs/modules/multivpc): This module creates between 2 and 8 VPC networks with distinct IP ranges to support multi-networking configurations.
  * [Create a GPU RDMA VPC network](https://docs.cloud.google.com/cluster-toolkit/docs/modules/gpu-rdma-vpc): This module creates a network optimized for GPU Remote Direct Memory Access (RDMA) traffic, which is critical for high-performance AI training.
  * [Use a pre-existing VPC network](https://docs.cloud.google.com/cluster-toolkit/docs/modules/pre-existing-vpc): This module uses an existing VPC network and outputs its attributes, letting you use the existing network as a drop-in substitute for a new network in your blueprints.
  * [Use a pre-existing subnetwork](https://docs.cloud.google.com/cluster-toolkit/docs/modules/pre-existing-subnetwork): This module uses an existing subnetwork within an existing VPC network and retrieves its configuration.
  * [Create firewall rules](https://docs.cloud.google.com/cluster-toolkit/docs/modules/firewall-rules): This module creates custom ingress and egress firewall rules for existing networks, letting you granularly control network traffic.
  * [Configure private service access](https://docs.cloud.google.com/cluster-toolkit/docs/modules/private-service-access): This module configures private service access for a VPC network, enabling private connectivity to Google Cloud services like Cloud SQL or Managed Lustre.



## Observability modules

Observability modules help you monitor the health and performance of your cluster. For example, the [Create a Cloud Monitoring dashboard](https://docs.cloud.google.com/cluster-toolkit/docs/modules/monitoring) module creates a Cloud Monitoring dashboard that displays metrics for your cluster deployment, providing a default HPC-focused view that you can customize with additional widgets.

## Software and system setup modules

These modules let you customize the software environment of your compute instances and automate system configuration tasks.

  * [Build custom images with Packer](https://docs.cloud.google.com/cluster-toolkit/docs/modules/packer): This module uses Packer to build custom VM images by provisioning a temporary instance and applying configurations using shell scripts, Ansible playbooks, or startup scripts.
  * [Use startup scripts](https://docs.cloud.google.com/cluster-toolkit/docs/modules/startup-script): This module generates a startup script to customize your compute instances at boot time by executing a specified list of runners such as shell scripts or Ansible playbooks.
  * [Apply Kubernetes manifests](https://docs.cloud.google.com/cluster-toolkit/docs/modules/kubectl-apply): This module lets you deploy Kubernetes manifests to your GKE clusters from local files, remote URLs, or direct strings.



## Project and identity modules

These modules let you manage project-level resources and identity configurations.

  * [Create a service account](https://docs.cloud.google.com/cluster-toolkit/docs/modules/service-account): This module automates the creation of service accounts and the assignment of IAM roles to ensure secure access for your cluster resources.



## What's next

  * To see how these modules work together in a blueprint, see the [Module overview](https://docs.cloud.google.com/cluster-toolkit/docs/modules/overview).
  * For a complete list of all modules, including the community and experimental modules, see the [Cluster Toolkit GitHub repository](https://github.com/GoogleCloudPlatform/cluster-toolkit/tree/main/modules).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
