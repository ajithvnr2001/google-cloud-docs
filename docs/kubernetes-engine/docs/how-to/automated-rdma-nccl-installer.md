---
url: https://docs.cloud.google.com/kubernetes-engine/docs/how-to/automated-rdma-nccl-installer/
title: Configure GPUDirect RDMA with the automated NCCL installer \u00a0|\u00a0 GKE networking \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:23:18.286583+00:00
---

# Configure GPUDirect RDMA with the automated NCCL installer  |  GKE networking  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/docs/how-to/automated-rdma-nccl-installer/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ Google Kubernetes Engine (GKE) ](https://docs.cloud.google.com/kubernetes-engine/docs)
  * [ GKE networking ](https://docs.cloud.google.com/kubernetes-engine/networking/docs)
  * [ Guides ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/explore-gke-networking-docs-use-cases)



Send feedback 

#  Configure GPUDirect RDMA with the automated NCCL installer Stay organized with collections  Save and categorize content based on your preferences. 

[ Autopilot ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/autopilot-overview) [ Standard ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/choose-cluster-mode)

When you run distributed AI/ML workloads, your applications often require high-throughput and low-latency communication between GPUs across multiple nodes. The A4 virtual machine (VM) instances and A3 Ultra VM instances come with the Titanium ML network adapter, which is built on NVIDIA ConnectX-7 (CX7) network interface controllers (NICs). Both VM families deliver non-blocking 3.2 Tbps of inter-node GPU-to-GPU traffic by using RDMA over Converged Ethernet (RoCE). RoCE enables scaling and collaboration across multiple GPUs by delivering a high-performance cloud experience for AI workloads.

While GPUDirect RDMA provides this direct communication path, manually configuring the necessary network plugins and resource claims can be complex and error-prone.

To solve this operational challenge, you can combine the automated RDMA NCCL installer with automated networking and Google Kubernetes Engine (GKE) managed DRANET to simplify GPUDirect RDMA configuration for AI workloads across multiple hosts on GKE. The automated RDMA NCCL installer automatically deploys the required NCCL and gIB binaries on node pools that use A3 Ultra or A4 machine types. When you use these features together, you can focus on deploying your AI workloads rather than manually managing the underlying network infrastructure and resource claims.

For more information, see [Create a cluster with GPUDirect RDMA](https://docs.cloud.google.com/ai-hypercomputer/docs/create/gke-ai-hypercompute-custom#create-with-rdma).

## Benefits

The automated RDMA NCCL installer provides the following benefits:

  * **Automatic installation of RDMA NCCL libraries:** starting with GKE version 1.36.2-gke.1368000, you can enable automatic installation of the RDMA [NCCL/gIB libraries](https://docs.cloud.google.com/ai-hypercomputer/docs/nccl/overview) designed for optimal GPU networking performance on Google Cloud during node pool creation by using a single flag.
  * **Simplified configuration for running RDMA workloads:** by combining the automated RDMA NCCL installer, [automated networking for accelerator VMs](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/config-auto-net-for-accelerators), and [GKE managed DRANET](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/allocate-network-resources-dra), you can deploy RDMA-enabled AI workloads without manual network configuration.
  * **Compatibility and safe upgrades:** the RDMA NCCL binaries provided by the installer pass end-to-end qualification tests before each GKE release. This testing ensures that the RDMA user-space libraries remain compatible with the specific kernel versions used in GKE, so that you can safely upgrade your clusters and node pools without disrupting running workloads.



## Limitations

The automated RDMA NCCL installer has the following limitations:

  * The automated RDMA NCCL installer is supported on GKE version 1.36.2-gke.1368000 or later.
  * You can use the automated RDMA NCCL installer only on `a3-ultragpu-8g` and `a4-highgpu-8g` machine types.
  * If you use GKE managed DRANET to configure workloads, review the [key considerations and limitations for GKE managed DRANET](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/allocate-network-resources-dra#key-considerations).
  * You can't use both the multi-network API and DRANET in the same node pool. You must choose one method for network attachment for your Pods.
  * The GKE nodes must use a Container-Optimized OS node image. Ubuntu and Windows node images are not supported.
  * You must meet all other [requirements for running A3 Ultra and A4](https://docs.cloud.google.com/ai-hypercomputer/docs/create/gke-ai-hypercompute-custom#create-with-rdma) with GPUDirect RDMA on GKE.



## Before you begin

Before you start, make sure you have performed the following tasks:

  * Verify that your cluster uses GKE version 1.36.2-gke.1368000 or later.
  * Verify that you use the [Google Cloud CLI](https://docs.cloud.google.com/sdk/gcloud) version 550.0.0 or later.
  * Ensure that you have an existing Autopilot or Standard cluster. To create a new cluster, see [Create an Autopilot cluster](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/creating-an-autopilot-cluster).
  * Verify that your cluster has [GKE Dataplane V2 enabled](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/dataplane-v2#create-cluster). (You can enable GKE Dataplane V2 when you create a new cluster by specifying the `--enable-dataplane-v2` flag.) GKE Dataplane V2 is enabled by default for all new Autopilot clusters.
  * Verify that you set up cluster and node pool networking by using one of the following methods: 
    * **Automated networking with DRANET (recommended):** use [automated networking for accelerator VMs](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/config-auto-net-for-accelerators#configure-automated-networking) with an accelerator network profile and [GKE managed DRANET](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/allocate-network-resources-dra) for network attachment.
    * **Manual networking with the multi-network API:** follow the manual workflow to [create VPC networks and subnets](https://docs.cloud.google.com/ai-hypercomputer/docs/create/gke-ai-hypercompute-custom#create-vpcs-and-subnets), enable the [GKE multi-network API](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/setup-multinetwork-support-for-pods), and configure additional node networks on the accelerator node pool.
  * Verify that you have a minimum virtual machine (VM) instance quota of two. This minimum quota corresponds to 16 GPUs if you use the `a4-highgpu-8g` or `a3-ultragpu-8g` machine types.



## Create a node pool with the installer and automated networking

To enable GPUDirect RDMA for multi-host AI workloads, configure a GPU node pool that combines the automated RDMA NCCL installer, automated networking, and GKE managed DRANET.

Select one of the following options:

### gcloud (Standard)

To enable the automated RDMA NCCL installer on a Standard node pool, specify `rdma` as the value for the `--gpudirect-strategy` flag. GKE automatically deploys the RDMA NCCL plugin compatible with the node version.

  1. Set the following environment variables:
         
         export CLUSTER_NAME=CLUSTER_NAME
         export CONTROL_PLANE_LOCATION=CONTROL_PLANE_LOCATION
         export PROJECT_ID=PROJECT_ID
         export NODE_POOL_NAME=NODE_POOL_NAME
         export NODEPOOL_LOCATION=NODEPOOL_LOCATION
         export ACCELERATOR_TYPE=ACCELERATOR_TYPE
         export ACCELERATOR_COUNT=ACCELERATOR_COUNT
         export DRIVER_VERSION=DRIVER_VERSION
         export MACHINE_TYPE=MACHINE_TYPE
         export NUM_NODES=NUM_NODES
         export RESERVATION_PROJECT=RESERVATION_PROJECT
         export RESERVATION_NAME=RESERVATION_NAME
         export RESERVATION_BLOCK=RESERVATION_BLOCK
         

Replace the following:

     * `CLUSTER_NAME`: the name of your cluster.
     * `CONTROL_PLANE_LOCATION`: the location for the cluster control plane.
     * `PROJECT_ID`: your project ID.
     * `NODE_POOL_NAME`: the name for the new node pool.
     * `NODEPOOL_LOCATION`: the location for the node pool.
     * `ACCELERATOR_TYPE`: the accelerator type, such as `nvidia-h200-141gb` or `nvidia-b200`.
     * `ACCELERATOR_COUNT`: the number of accelerators, such as `8`.
     * `DRIVER_VERSION`: the GPU driver version, such as `default` or `latest`.
     * `MACHINE_TYPE`: the machine type, which must be `a3-ultragpu-8g` or `a4-highgpu-8g`.
     * `NUM_NODES`: the number of nodes in the node pool.
     * `RESERVATION_PROJECT`: the project ID where the reservation is located.
     * `RESERVATION_NAME`: the name of the reservation.
     * `RESERVATION_BLOCK`: the reservation block.
  2. Create the node pool:
         
         gcloud container node-pools create ${NODE_POOL_NAME} \
           --location=${CONTROL_PLANE_LOCATION} \
           --cluster=${CLUSTER_NAME} \
           --project=${PROJECT_ID} \
           --node-locations=${NODEPOOL_LOCATION} \
           --accelerator type=${ACCELERATOR_TYPE},count=${ACCELERATOR_COUNT},gpu-driver-version=${DRIVER_VERSION} \
           --machine-type=${MACHINE_TYPE} \
           --num-nodes=${NUM_NODES} \
           --reservation-affinity=specific \
           --reservation=projects/${RESERVATION_PROJECT}/reservations/${RESERVATION_NAME}/reservationBlocks/${RESERVATION_BLOCK} \
           --accelerator-network-profile=auto \
           --node-labels=cloud.google.com/gke-networking-dra-driver=true \
           --gpudirect-strategy=rdma
         




### ComputeClass (Autopilot and Standard)

To use the automated RDMA NCCL installer in Autopilot clusters or in Standard clusters with node pool auto-creation, configure a custom [ComputeClass](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/about-custom-compute-classes) resource with `gpuDirect: rdma`, `acceleratorNetworkProfile: auto`, and DRANET enabled.

  1. Save the following manifest as `rdma-compute-class.yaml`:
         
         apiVersion: cloud.google.com/v1
         kind: ComputeClass
         metadata:
           name: COMPUTE_CLASS_NAME
         spec:
           nodePoolConfig:
             dra:
               networking:
                 enabled: true
           priorities:
           - gpu:
               type: ACCELERATOR_TYPE
               count: ACCELERATOR_COUNT
             machineType: MACHINE_TYPE
             # Optional: include the reservations block if you use a reservation
             reservations:
               affinity: Specific
               specific:
               - name: RESERVATION_NAME
                 zones:
                 - RESERVATION_ZONE
             acceleratorNetworkProfile: auto
             gpuDirect: rdma
           nodePoolAutoCreation:
             enabled: true
         

Replace the following:

     * `COMPUTE_CLASS_NAME`: the name for the ComputeClass.
     * `ACCELERATOR_TYPE`: the accelerator type, such as `nvidia-h200-141gb` or `nvidia-b200`.
     * `ACCELERATOR_COUNT`: the number of accelerators, such as `8`.
     * `MACHINE_TYPE`: the machine type, which must be `a3-ultragpu-8g` or `a4-highgpu-8g`.
     * `RESERVATION_NAME`: the name of your reservation.
     * `RESERVATION_ZONE`: the zone where the reservation is located.
  2. Apply the manifest:
         
         kubectl apply -f rdma-compute-class.yaml
         

When you deploy a workload that uses this ComputeClass, add the `cloud.google.com/compute-class: COMPUTE_CLASS_NAME` node selector to your Pod specification.




### Terraform

You can use Terraform to provision your GKE cluster and node pool with the automated RDMA NCCL installer configured.

  1. Install Terraform on your local machine following the [official Terraform documentation](https://developer.hashicorp.com/terraform/install).

  2. Create an empty directory to hold your configuration and change into it. Create a file named `main.tf` and populate it with the following:
         
         # main.tf
         
         terraform {
           required_providers {
             google = {
               source  = "hashicorp/google"
               version = ">= 7.34.0" # Min version that supports the automated RDMA NCCL installer
             }
           }
         }
         
         provider "google" {
           project = "PROJECT_ID"
           region  = "REGION"
           zone    = "ZONE"
         }
         

Replace the following:

     * `PROJECT_ID`: your project ID.
     * `REGION`: the compute region.
     * `ZONE`: a zone that supports A3 Ultra or A4 machine types.
  3. Run the following commands in the same directory to authenticate with Google Cloud and initialize Terraform's state:
         
         gcloud auth application-default login
         terraform init
         

  4. Add the following configuration to your `main.tf` or a separate Terraform configuration file. This configuration deploys a cluster with three `a3-ultragpu-8g` nodes in `us-central1-b` that are configured to use the automated RDMA NCCL installer, an automatic accelerator network profile, and GKE managed DRANET:
         
         resource "google_container_cluster" "cluster" {
           name               = "example-rdma-tf"
           location           = "us-central1-b"
         
           initial_node_count  = 3 # Number of CPU nodes in default pool
           deletion_protection = false # Optional, allows Terraform to delete clusters
         
           min_master_version      = "1.36.2-gke.1368000" # Required, min version with automated RDMA NCCL installer support
           datapath_provider       = "ADVANCED_DATAPATH" # Required, enable GKE Dataplane v2
         }
         
         resource "google_container_node_pool" "rdma_pool" {
           cluster    = google_container_cluster.cluster.name
           location   = google_container_cluster.cluster.location
         
           network_config {
             accelerator_network_profile = "auto" # Required if per-NIC networks are not manually configured
           }
         
           node_config {
             machine_type = "a3-ultragpu-8g"
             guest_accelerator {
               type  = "nvidia-h200-141gb"
               count = 8
             }
         
             ephemeral_storage_local_ssd_config { # Required, see https://github.com/hashicorp/terraform-provider-google/issues/17068
               data_cache_count = 0
               local_ssd_count = 32
             }
         
             gpudirect_strategy = "RDMA"
         
             labels = {
               "cloud.google.com/gke-networking-dra-driver" = "true" # Automatically install DRANET driver
             }
           }
         }
         

  5. Run `terraform plan -out=tfplan` to view the changes Terraform makes based on the current configuration. After verifying the plan, run it by using the following command:
         
         terraform apply tfplan
         

**Note:** Cluster and node pool creation can take several minutes to complete. Run `TF_LOG=INFO terraform apply` for detailed progress logs.



## Create a ResourceClaimTemplate

To allow Pods to dynamically request and receive RDMA devices, create a `ResourceClaimTemplate` object, helping to provide high-performance networking for AI workloads. The `allocationMode: All` setting allocates all available `mrdma.google.com` RDMA devices. Allocating all available devices is crucial for AI workloads across multiple hosts that require full utilization of GPU and RDMA capabilities.

  1. Save the following manifest as `all-mrdma-template.yaml`:
         
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
                   allocationMode: All
         

  2. Apply the manifest:
         
         kubectl apply -f all-mrdma-template.yaml
         




## Deploy and run a NCCL RDMA test workload

To verify the RDMA configuration, deploy a test workload and then run a NCCL all-gather test to confirm the setup.

  1. Save the following manifest as `nccl-test-workload.yaml`:
         
         apiVersion: v1
         kind: Service
         metadata:
           name: nccl-host-1
         spec:
           selector:
             name: nccl-host-1
           clusterIP: None
         ---
         apiVersion: v1
         kind: Service
         metadata:
           name: nccl-host-2
         spec:
           selector:
             name: nccl-host-2
           clusterIP: None
         ---
         apiVersion: v1
         kind: Pod
         metadata:
           name: nccl-test-host-1
           labels:
             name: nccl-host-1
         spec:
           # Uncomment the following lines if you use a custom ComputeClass:
           # nodeSelector:
           #   cloud.google.com/compute-class: COMPUTE_CLASS_NAME
           volumes:
             - name: library-dir-host
               hostPath:
                 path: /home/kubernetes/bin/nvidia
             - name: gib
               hostPath:
                 path: /home/kubernetes/bin/gib
             - name: shared-memory
               emptyDir:
                 medium: "Memory"
                 sizeLimit: 250Gi
           resourceClaims:
           - name: rdma
             resourceClaimTemplateName: all-mrdma
           containers:
             - image: us-docker.pkg.dev/gce-ai-infra/gpudirect-gib/nccl-plugin-gib-diagnostic:v1.1.2
               name: test
               resources:
                 requests:
                   cpu: 150m
                 limits:
                   nvidia.com/gpu: 8
                 claims:
                 - name: rdma
               volumeMounts:
                 - name: library-dir-host
                   mountPath: /usr/local/nvidia
                 - name: gib
                   mountPath: /usr/local/gib
                 - name: shared-memory
                   mountPath: /dev/shm
               env:
                 - name: LD_LIBRARY_PATH
                   value: /usr/local/nvidia/lib64
               command: ["/bin/bash", "-c"]
               args:
                 - |
                   /scripts/container_entry.sh shell
                   source /usr/local/gib/scripts/set_nccl_env.sh
                   sleep infinity
         ---
         apiVersion: v1
         kind: Pod
         metadata:
           name: nccl-test-host-2
           labels:
             name: nccl-host-2
         spec:
           # Uncomment the following lines if you use a custom ComputeClass:
           # nodeSelector:
           #   cloud.google.com/compute-class: COMPUTE_CLASS_NAME
           volumes:
             - name: library-dir-host
               hostPath:
                 path: /home/kubernetes/bin/nvidia
             - name: gib
               hostPath:
                 path: /home/kubernetes/bin/gib
             - name: shared-memory
               emptyDir:
                 medium: "Memory"
                 sizeLimit: 250Gi
           resourceClaims:
           - name: rdma
             resourceClaimTemplateName: all-mrdma
           containers:
             - image: us-docker.pkg.dev/gce-ai-infra/gpudirect-gib/nccl-plugin-gib-diagnostic:v1.1.2
               name: test
               resources:
                 requests:
                   cpu: 150m
                 limits:
                   nvidia.com/gpu: 8
                 claims:
                 - name: rdma
               volumeMounts:
                 - name: library-dir-host
                   mountPath: /usr/local/nvidia
                 - name: gib
                   mountPath: /usr/local/gib
                 - name: shared-memory
                   mountPath: /dev/shm
               env:
                 - name: LD_LIBRARY_PATH
                   value: /usr/local/nvidia/lib64
               command: ["/bin/bash", "-c"]
               args:
                 - |
                   /scripts/container_entry.sh shell
                   source /usr/local/gib/scripts/set_nccl_env.sh
                   sleep infinity
         

  2. Apply the test workload manifest:
         
         kubectl apply -f nccl-test-workload.yaml
         

  3. Run a NCCL all-gather test between the two test hosts:
         
         kubectl exec nccl-test-host-1 -it -- /usr/local/gib/scripts/run_nccl_tests.sh -t all_gather -b 1K -e 8G nccl-host-1 nccl-host-2
         




## Deploy your AI/ML workload

To run your distributed training jobs efficiently, your ML applications need to request the RDMA devices provisioned by the installer. After verifying the RDMA configuration with the test workload, you can deploy your AI/ML applications. Your application Pods must reference the `ResourceClaimTemplate` object you created earlier (`all-mrdma`) to dynamically request and receive RDMA devices.

The following Pod manifest uses the `all-mrdma` `ResourceClaimTemplate` object. Replace `IMAGE` with your AI/ML workload container image and `COMMAND` with your application's entry point.
    
    
    apiVersion: v1
    kind: Pod
    metadata:
      name: my-rdma-workload
    spec:
      restartPolicy: OnFailure
      # Uncomment the following lines if you use a custom ComputeClass:
      # nodeSelector:
      #   cloud.google.com/compute-class: COMPUTE_CLASS_NAME
      volumes:
        - name: library-dir-host
          hostPath:
            path: /home/kubernetes/bin/nvidia
        - name: gib
          hostPath:
            path: /home/kubernetes/bin/gib
        - name: shared-memory
          emptyDir:
            medium: "Memory"
            sizeLimit: 250Gi
      resourceClaims:
      - name: mrdma-claim
        resourceClaimTemplateName: all-mrdma
      containers:
      - name: my-container
        image: IMAGE # Replace with your AI/ML workload image, for example, gcr.io/your-project/your-ai-app:latest
        command: ["/bin/bash", "-c"]
        args:
          - |
            source /usr/local/gib/scripts/set_nccl_env.sh
            COMMAND # Replace with your workload command, for example, python3 train.py
        resources:
          limits:
            nvidia.com/gpu: 8 # Specify the required GPU count
          claims:
          - name: mrdma-claim
        volumeMounts:
          - name: library-dir-host
            mountPath: /usr/local/nvidia
          - name: gib
            mountPath: /usr/local/gib
          - name: shared-memory
            mountPath: /dev/shm
        env:
          - name: LD_LIBRARY_PATH
            value: /usr/local/nvidia/lib64
          - name: MASTER_ADDR
            value: "nccl-test-host-1" # Example for distributed training
          - name: MASTER_PORT
            value: "29500"
    

To deploy this workload, save the manifest as `workload.yaml` and apply it:
    
    
    kubectl apply -f workload.yaml
    

## Advanced configurations

You can also enable the automated RDMA NCCL installer on node pools that use manual multi-network configurations instead of automated networking with DRANET.

### Create a node pool on a cluster with multi-network enabled

If you followed the cluster configurations in [GPUDirect RDMA support on GKE](https://docs.cloud.google.com/ai-hypercomputer/docs/create/gke-ai-hypercompute-custom), you can use the following instructions to create a new node pool with the automated RDMA NCCL installer enabled on existing clusters with multi-network enabled.

To check if your cluster has multi-network enabled, run the following command:
    
    
    export CLUSTER_NAME=CLUSTER_NAME
    export CONTROL_PLANE_LOCATION=CONTROL_PLANE_LOCATION
    export PROJECT_ID=PROJECT_ID
    export CLUSTER_VERSION=CLUSTER_VERSION
    
    gcloud container clusters describe ${CLUSTER_NAME} \
      --location ${CONTROL_PLANE_LOCATION} --project ${PROJECT_ID} \
      --format="value(networkConfig.enableMultiNetworking)"
    

To reuse the VPC networks for additional NICs on the A3 Ultra and A4 VM instances, set the following variables:
    
    
    export REGION=REGION
    export ZONE=ZONE
    export GVNIC_NETWORK_PREFIX=GVNIC_NETWORK_PREFIX
    export RDMA_NETWORK_PREFIX=RDMA_NETWORK_PREFIX
    

To create a node pool with the automated RDMA NCCL installer, run the following command:
    
    
    export NODE_POOL_NAME=NODE_POOL_NAME
    export PROJECT_ID=PROJECT_ID
    export NODE_COUNT=NODE_COUNT
    export ACCELERATOR_TYPE=ACCELERATOR_TYPE
    export ACCELERATOR_COUNT=ACCELERATOR_COUNT
    export DRIVER_VERSION=DRIVER_VERSION
    export MACHINE_TYPE=MACHINE_TYPE
    export RESERVATION=RESERVATION
    
    gcloud container node-pools create ${NODE_POOL_NAME} --project ${PROJECT_ID} \
      --zone ${ZONE} --cluster ${CLUSTER_NAME} --num-nodes=${NODE_COUNT} \
      --machine-type ${MACHINE_TYPE} \
      --accelerator type=${ACCELERATOR_TYPE},count=${ACCELERATOR_COUNT},gpu-driver-version=${DRIVER_VERSION} \
      --additional-node-network network=${GVNIC_NETWORK_PREFIX}-net-0,subnetwork=${GVNIC_NETWORK_PREFIX}-sub-0 \
      --additional-node-network network=${RDMA_NETWORK_PREFIX},subnetwork=${RDMA_NETWORK_PREFIX}-sub-0 \
      --additional-node-network network=${RDMA_NETWORK_PREFIX},subnetwork=${RDMA_NETWORK_PREFIX}-sub-1 \
      --additional-node-network network=${RDMA_NETWORK_PREFIX},subnetwork=${RDMA_NETWORK_PREFIX}-sub-2 \
      --additional-node-network network=${RDMA_NETWORK_PREFIX},subnetwork=${RDMA_NETWORK_PREFIX}-sub-3 \
      --additional-node-network network=${RDMA_NETWORK_PREFIX},subnetwork=${RDMA_NETWORK_PREFIX}-sub-4 \
      --additional-node-network network=${RDMA_NETWORK_PREFIX},subnetwork=${RDMA_NETWORK_PREFIX}-sub-5 \
      --additional-node-network network=${RDMA_NETWORK_PREFIX},subnetwork=${RDMA_NETWORK_PREFIX}-sub-6 \
      --additional-node-network network=${RDMA_NETWORK_PREFIX},subnetwork=${RDMA_NETWORK_PREFIX}-sub-7 \
      --scopes "https://www.googleapis.com/auth/cloud-platform" \
      --reservation-affinity=specific \
      --reservation=${RESERVATION} \
      --gpudirect-strategy=rdma
    

## What's next

  * Learn more about [GPUDirect RDMA support on GKE](https://docs.cloud.google.com/ai-hypercomputer/docs/create/gke-ai-hypercompute-custom#create-with-rdma).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
