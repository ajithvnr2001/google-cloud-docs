---
url: https://docs.cloud.google.com/kubernetes-engine/docs/how-to/run-hpc-workloads/
title: Run high performance computing (HPC) workloads with H4D \u00a0|\u00a0 Google Kubernetes Engine (GKE) \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T15:31:58.787051+00:00
---

# Run high performance computing (HPC) workloads with H4D  |  Google Kubernetes Engine (GKE)  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/docs/how-to/run-hpc-workloads/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ Google Kubernetes Engine (GKE) ](https://docs.cloud.google.com/kubernetes-engine/docs)
  * [ Guides ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/kubernetes-engine-overview)



Send feedback 

#  Run high performance computing (HPC) workloads with H4D Stay organized with collections  Save and categorize content based on your preferences. 

[ Standard ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/choose-cluster-mode)

This document explains how to run high performance computing (HPC) workloads on Google Kubernetes Engine (GKE) clusters that use the H4D machine series and [remote direct memory access (RDMA)](https://en.wikipedia.org/wiki/Remote_direct_memory_access).

H4D is a machine series in the [Compute-optimized machine family for Compute Engine](https://docs.cloud.google.com/compute/docs/compute-optimized-machines). The machine series is optimized for high performance, low cost, and scalability. H4D works well for applications that scale across multiple nodes. H4D instances configured to use RDMA support up to 200 Gbps network bandwidth between nodes.

## Before you begin

Before you start, make sure that you have performed the following tasks: 

  * Enable the Google Kubernetes Engine API. 
[ Enable Google Kubernetes Engine API ](https://console.cloud.google.com/apis/enableflow?apiid=container.googleapis.com)
  * To use the Google Cloud CLI for this task, [install](https://docs.cloud.google.com/sdk/docs/install) and then [initialize](https://docs.cloud.google.com/sdk/docs/initialize) the gcloud CLI. If you previously installed the gcloud CLI, get the latest version by running the `gcloud components update` command. Earlier gcloud CLI versions might not support running the commands in this document. **Note:** For existing gcloud CLI installations, make sure to set the `compute/region` [property](https://docs.cloud.google.com/sdk/docs/properties#setting_properties). If you use primarily zonal clusters, set the `compute/zone` instead. By setting a default location, you can avoid errors in the gcloud CLI like the following: `One of [--zone, --region] must be supplied: Please specify location`. You might need to specify the location in certain commands if the location of your cluster differs from the default that you set.


  * Obtain capacity for H4D VMs after choosing a consumption option. Dense resource allocation is recommended for H4D VMs. Dense resource allocation is available with some of the provisioning models for H4D, and provides you with [enhanced cluster management capabilities](https://docs.cloud.google.com/compute/docs/hpc/overview-hpc-clusters#manage-cluster) for your H4D capacity. To obtain capacity, do the following:

    1. Review the [Provisioning models for VM and cluster creation](https://docs.cloud.google.com/compute/docs/hpc/overview-hpc-clusters#provisioning-overview).
    2. [Choose a consumption option and obtain capacity](https://docs.cloud.google.com/compute/docs/hpc/overview-hpc-clusters#consumption-and-capacity).
  * Ensure that you adhere to the following GKE version requirements:

    * Use GKE version 1.32.6-gke.1060000 or later to create a node pool with reserved H4D VMs in GKE Standard mode.
    * Use GKE version 1.33.2-gke.4731000 or later to create the following:

      * H4D nodes with [flex-start](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/dws)
      * H4D nodes with [Autopilot](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/autopilot-overview)
      * H4D nodes with [cluster autoscaling](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/cluster-autoscaler) in Standard clusters
      * H4D nodes with [node auto-provisioning](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/node-auto-provisioning) in Standard clusters
  * Use only locations where the H4D machine type is available. For more information, see the table in [Available regions and zones](https://docs.cloud.google.com/compute/docs/regions-zones#available), filtering for `H4D`.

  * Use only Container-Optimized OS [node images](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/node-images).

  * Review the [H4D limitations](https://docs.cloud.google.com/compute/docs/compute-optimized-machines#h4d_limitations).

  * Review how to handle host maintenance, because H4D machine types don't support live migration. For more information, see [Maintenance experience for H4D instances](https://docs.cloud.google.com/compute/docs/compute-optimized-machines#h4d_maintenance), and [Manage disruption to GKE nodes that don't live migrate](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/handle-disruption-gpu-tpu).




## Configure the GKE cluster and networks

You can use [Cluster Toolkit](https://docs.cloud.google.com/cluster-toolkit/docs/overview) to quickly create a production-ready GKE cluster which uses reservation-bound H4D VMs. The Cluster Toolkit instructions in this section use the [GKE H4D Blueprint](https://github.com/GoogleCloudPlatform/cluster-toolkit/tree/main/examples/gke-h4d).

Alternatively, you can use Google Cloud CLI for maximum flexibility in configuring your cluster environment with either reservation-bound or Flex-start VMs.

###  Cluster Toolkit 

  1. [Set up Cluster Toolkit](https://docs.cloud.google.com/cluster-toolkit/docs/setup/configure-environment). We recommend using Cloud Shell to do so because the dependencies are already pre-installed for Cluster Toolkit.

  2. Get the IP address for the host machine where you installed Cluster Toolkit:
         
         curl ifconfig.me
         

Save this IP address to use for the `IP_ADDRESS` variable in a later step.

  3. Create a Cloud Storage bucket to store the state of the Terraform deployment:
         
         gcloud storage buckets create gs://BUCKET_NAME \
             --default-storage-class=STANDARD \
             --project=PROJECT_ID \
             --location=COMPUTE_REGION_TERRAFORM_STATE \
             --uniform-bucket-level-access
         gcloud storage buckets update gs://BUCKET_NAME --versioning
         

Replace the following variables:

     * `BUCKET_NAME`: the name of the new Cloud Storage bucket.
     * `PROJECT_ID`: your Google Cloud project ID.
     * `COMPUTE_REGION_TERRAFORM_STATE`: the compute region where you want to store the state of the Terraform deployment.
  4. In the [`examples/gke-h4d/gke-h4d-deployment.yaml` blueprint from the GitHub repo](https://github.com/GoogleCloudPlatform/cluster-toolkit/blob/main/examples/gke-h4d/gke-h4d-deployment.yaml), fill in the following settings in the `terraform_backend_defaults` and `vars` sections to match the specific values for your deployment:

     * `DEPLOYMENT_NAME`: a unique name for the deployment, which must be between 6 and 30 characters in length. If the deployment name isn't unique within a project, cluster creation fails. The default value is `gke-h4d`.
     * `BUCKET_NAME`: the name of the Cloud Storage bucket you created in the previous step.
     * `PROJECT_ID`: your Google Cloud project ID.
     * `COMPUTE_REGION`: the compute region for the cluster, which must match the region where machines are available for your reservation.
     * `COMPUTE_ZONE`: the compute zone for the node pool of H4D machines. Note that this zone should match the zone where machines are available in your reservation.
     * `NODE_COUNT`: the number of H4D nodes in your cluster.
     * `IP_ADDRESS/SUFFIX`: The IP address range that you want to allow to connect with the cluster. This CIDR block must include the IP address of the machine that you want to use to call Terraform. For more information, see [How authorized networks work](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/network-isolation#how_authorized_networks_work).
     * For the `reservation` field, use one of the following, depending on whether you want to target specific [blocks](https://docs.cloud.google.com/compute/docs/hpc/overview-hpc-clusters#block) in a reservation when provisioning the node pool:

       * To place the node pool anywhere in the reservation, provide the name of your reservation (`RESERVATION_NAME`).
       * To target a specific block within your reservation, use the reservation and block names in the following format:
             
             RESERVATION_NAME/reservationBlocks/BLOCK_NAME
             

If you don't know which blocks are available in your reservation, see [View a reservation topology](https://docs.cloud.google.com/compute/docs/hpc/view-reserved-capacity#view-capacity-topology).

  5. [Generate Application Default Credentials (ADC)](https://docs.cloud.google.com/docs/authentication/provide-credentials-adc#google-idp) to provide access to Terraform. If you're using Cloud Shell, you can run the following command:
         
         gcloud auth application-default login
         

  6. Deploy the blueprint to provision the GKE infrastructure using the H4D machine types:
         
         ./gcluster deploy -d examples/gke-h4d/gke-h4d-deployment.yaml examples/gke-h4d/gke-h4d.yaml
         

  7. When prompted, select **(A)pply** to deploy the blueprint.

  8. Additionally, this blueprint provisions a Filestore instance and connects it to the GKE cluster with a Persistent Volume (PV). An example Job template is included in this blueprint. This template runs a parallel Job that reads and writes data to this shared storage. A `kubectl create` is displayed in the deployment outputs which can be used to trigger the sample Job.




###  Google Cloud CLI 

Replace the following values for the commands in this section:

  * `PROJECT_ID`: your Google Cloud project ID.
  * `CLUSTER_NAME`: the name of your cluster.
  * `CONTROL_PLANE_LOCATION`: the Compute Engine [location](https://docs.cloud.google.com/compute/docs/regions-zones#available) of the control plane of your cluster. Provide a region for regional clusters, or a zone for zonal clusters. Regional clusters are recommended for production workloads. For regional clusters, the region must include a zone in which H4D is available. For zonal clusters, the zone must have H4D availability. If you're using a reservation, the region and zone must match the region and zone of the reservation.
  * `COMPUTE_ZONE`: the zone of your node pool. This must be a zone in which H4D is available. If you're using a reservation, the region and zone must match the region and zone of the reservation. You can't create a multi-zone node pool if you want the H4D nodes to work with Cloud RDMA.
  * `RDMA_NETWORK_PREFIX`: the RDMA network prefix (for example, `h4d-rdma`).
  * `RDMA_SUBNET_CIDR`: the RDMA subnet CIDR range. Ensure that this range doesn't overlap with the cluster's default networks.
  * `NODE_POOL_NAME`: the name of your H4D node pool.
  * `NODE_COUNT`: the number of H4D nodes to create in the node pool.
  * `H4D_MACHINE_TYPE`: the [H4D machine type](https://docs.cloud.google.com/compute/docs/compute-optimized-machines#h4d_machine_types) to use (for example, `h4d-highmem-192-lssd`).



Create a cluster with the gcloud CLI using the following steps:

  1. **Create VPCs and subnets** : Configure the default [Virtual Private Cloud (VPC)](https://docs.cloud.google.com/vpc/docs/overview) and subnet for the cluster. For the IRDMA network interface card (NIC), create a dedicated VPC and subnet. The VPC created with the following instructions uses, as required, a [Falcon VPC network profile](https://docs.cloud.google.com/vpc/docs/rdma-network-profiles).

     1. Create a VPC for the IRDMA network interface that uses the RDMA over Falcon transport protocol:
            
            gcloud compute --project=PROJECT_ID \
              networks create RDMA_NETWORK_PREFIX-net \
              --network-profile=COMPUTE_ZONE-vpc-falcon \
              --subnet-mode=custom
            

     2. Create a subnet for the Falcon VPC network:
            
            gcloud compute --project=PROJECT_ID \
              networks subnets create \
              RDMA_NETWORK_PREFIX-sub-0 \
              --network=RDMA_NETWORK_PREFIX-net \
              --region=CONTROL_PLANE_LOCATION \
              --range=RDMA_SUBNET_CIDR
            

  2. **Create a GKE cluster with multi-networking** : Create the cluster. Optionally, with this command, you can explicitly provide the secondary CIDR ranges for services and Pods.

Run the following command:
         
         gcloud container clusters create CLUSTER_NAME --project PROJECT_ID \
           --enable-dataplane-v2 --enable-ip-alias --location=CONTROL_PLANE_LOCATION \
           --enable-multi-networking \
           [--services-ipv4-cidr=SERVICE_CIDR \
           --cluster-ipv4-cidr=POD_CIDR]
         

If you use these optional flags, replace the following additional values:

     * `SERVICE_CIDR`: the secondary CIDR range for services.
     * `POD_CIDR`: the secondary CIDR range for Pods.

When you use these flags, verify that the CIDR ranges don't overlap with subnet ranges for additional node networks. For example, `SERVICE_CIDR=10.65.0.0/19` and `POD_CIDR=10.64.0.0/19`.

  3. **Create GKE network objects** : Configure the VPC network by using GKE network parameter sets. Apply the `GKENetworkParamSet` and `Network` objects:
         
         kubectl apply -f - <<EOF
         apiVersion: networking.gke.io/v1
         kind: GKENetworkParamSet
         metadata:
           name: rdma-0
         spec:
           vpc: RDMA_NETWORK_PREFIX-net
           vpcSubnet: RDMA_NETWORK_PREFIX-sub-0
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
         EOF
         

  4. **Create an H4D node pool** : Create a node pool that uses H4D and connects to the Falcon VPC network. You can use reservation-bound H4D nodes and [compact placement](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/compact-placement). Or, you can use H4D nodes provisioned with flex-start. Select the tab that corresponds to your consumption option:

### Reservation-bound

     1. Create a resource policy for compact placement. Compact placement optimizes performance for tightly-coupled HPC workloads—which run across multiple nodes—by ensuring that nodes are physically located relative to each other within a zone.

Run the following command:
            
            gcloud compute resource-policies create group-placement POLICY_NAME \
                --region REGION --collocation collocated
            

Replace the following values:

        * `POLICY_NAME`: the name of the resource policy (for example, `h4d-compact`).
        * `REGION`: the region of your cluster.
     2. Create a node pool that uses H4D and connects to the RDMA network:
            
            gcloud container node-pools create NODE_POOL_NAME --project PROJECT_ID \
              --location=CONTROL_PLANE_LOCATION --cluster CLUSTER_NAME --num-nodes=NODE_COUNT \
              --node-locations=COMPUTE_ZONE \
              --machine-type H4D_MACHINE_TYPE \
              --additional-node-network network=RDMA_NETWORK_PREFIX-net,subnetwork=RDMA_NETWORK_PREFIX-sub-0 \
              --placement-policy POLICY_NAME \
              --max-surge-upgrade 0  \
              --max-unavailable-upgrade MAX_UNAVAILABLE
            

Replace `MAX_UNAVAILABLE` with the maximum number of nodes that can be unavailable at the same time during a node pool upgrade. For compact placement, we recommend [fast no surge upgrades](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/node-pool-upgrade-strategies#optimizing-surge) to optimize the likelihood of finding colocated nodes during upgrades.

###  Flex-start 

Create a node pool that uses H4D nodes provisioned with flex-start, and connects to the Falcon VPC network:
    
    gcloud container node-pools create NODE_POOL_NAME --project PROJECT_ID \
        --location=CONTROL_PLANE_LOCATION --cluster CLUSTER_NAME \
        --node-locations=COMPUTE_ZONE \
        --machine-type H4D_MACHINE_TYPE \
        --additional-node-network network=RDMA_NETWORK_PREFIX-net,subnetwork=RDMA_NETWORK_PREFIX-sub-0 \
        --flex-start --enable-autoscaling \
        --min-nodes=0 --max-nodes=MAX_NODES --num-nodes=0
    

Replace `MAX_NODES` with the maximum number of nodes to automatically scale to for the specified node pool per zone.




## Prepare your Docker image

Prepare your image by using the following example Dockerfile:
    
    
    FROM docker.io/rockylinux/rockylinux:8.10
    
    RUN dnf -y install https://depot.ciq.com/public/download/ciq-sigcloud-next-8/ciq-sigcloud-next-8.x86_64/Packages/c/ciq-sigcloud-next-release-6-1.el8_10.cld_next.noarch.rpm
        && dnf -y update ciq-sigcloud-next-release
        && dnf clean all
    
    RUN dnf install rdma-core libibverbs-utils librdmacm-utils infiniband-diags perftest -y
    
    CMD ["sleep", "infinity"]
    

For more information about which images support IRDMA, see the **Interfaces** tabs in the tables in [Operating system details](https://docs.cloud.google.com/compute/docs/images/os-details).

## Configure your manifests for RDMA

Enable Cloud RDMA by adding the following annotations to your Pod metadata:
    
    
    metadata:
      annotations:
        networking.gke.io/default-interface: 'eth0'
        networking.gke.io/interfaces: |
          [
            {"interfaceName":"eth0","network":"default"},
            {"interfaceName":"eth1","network":"rdma-0"},
          ]
    

## Test RDMA with rping

Verify Cloud RDMA functionality by running `rping` between a server and client Pod:

  1. On the server Pod, run the `rping` command:
         
         rping -s
         

  2. Get the server Pod's secondary RDMA internal IP address (`eth1`). You must use this secondary IP address to route traffic over the RDMA hardware; don't use the default Pod IP address:
         
         kubectl exec SERVER_POD_NAME -- ip -4 -o addr show eth1
         

Note the `inet` IP address from the output. You use this IP address as the `eth1` IP address in the following step.

  3. On the client Pod, run the `rping` command:
         
         rping -c -C 2 -d -a SERVER_IP
         

Replace `SERVER_IP` with the `eth1` IP address you retrieved in the previous step.

The output, if successful, resembles the following:
         
         created cm_id 0x5b597bf94800
         cma_event type RDMA_CM_EVENT_ADDR_RESOLVED cma_id 0x5b597bf94800 (parent)
         cma_event type RDMA_CM_EVENT_ROUTE_RESOLVED cma_id 0x5b597bf94800 (parent)
         rdma_resolve_addr - rdma_resolve_route successful
         created pd 0x5b597bf94fa0
         created channel 0x5b597bf96830
         created cq 0x5b597bf94ff0
         created qp 0x5b597bf96c00
         rping_setup_buffers called on cb 0x5b597bf8c820
         allocated & registered buffers...
         cq_thread started.
         cma_event type RDMA_CM_EVENT_ESTABLISHED cma_id 0x5b597bf94800 (parent)
         ESTABLISHED
         rdma_connect successful
         RDMA addr 5b597bf8cd80 rkey dadac8c4 len 64
         send completion
         recv completion
         RDMA addr 5b597bf8cff0 rkey 86ef015f len 64
         send completion
         recv completion
         RDMA addr 5b597bf8cd80 rkey dadac8c4 len 64
         send completion
         recv completion
         RDMA addr 5b597bf8cff0 rkey 86ef015f len 64
         send completion
         recv completion
         rping_free_buffers called on cb 0x5b597bf8c820
         destroy cm_id 0x5b597bf94800
         




## What's next

  * Learn more about [high performance computing](https://cloud.google.com/discover/what-is-high-performance-computing).
  * Learn [best practices for running HPC workloads on GKE](https://docs.cloud.google.com/kubernetes-engine/docs/best-practices/run-hpc).
  * Some HPC workloads require a Message Passing Interface (MPI) to run tightly-coupled, multi-node workloads with RDMA. For more information about setting MPI in your cluster for your H4D nodes, see [Run MPI Workloads on GKE H4D](https://github.com/GoogleCloudPlatform/kubernetes-engine-samples/tree/main/hpc/mpi#run-mpi-workloads-on-gke-h4d).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
