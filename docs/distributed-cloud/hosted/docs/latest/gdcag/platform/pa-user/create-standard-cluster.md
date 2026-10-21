---
url: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform/pa-user/create-standard-cluster/
title: Create a standard cluster to run container workloads \u00a0|\u00a0 Google Distributed Cloud air-gapped \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T23:43:57.433239+00:00
---

# Create a standard cluster to run container workloads  |  Google Distributed Cloud air-gapped  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform/pa-user/create-standard-cluster/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Distributed, hybrid, and multicloud ](https://docs.cloud.google.com/docs/dhm-cloud)
  * [ Google Distributed Cloud ](https://docs.cloud.google.com/distributed-cloud/docs)
  * [ Air-gapped ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdch)
  * [ 1.16.2 (Latest) ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag)



Send feedback 

#  Create a standard cluster to run container workloads Stay organized with collections  Save and categorize content based on your preferences. 

[ Standard ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform/pa-user/cluster-configs#standard-cluster)

This document explains how to create a standard Kubernetes cluster in a Google Distributed Cloud (GDC) air-gapped zone. A standard cluster provides a project-scoped, highly configurable Kubernetes cluster that includes a minimal set of included managed services. The standard cluster offers more flexibility for service configuration than the shared cluster, but also requires more management overhead. For more information about standard clusters, see [Kubernetes cluster configurations](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform/pa-user/cluster-configs).

Standard clusters are a [zonal resource](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/resources/multi-zone/api-servers#resource-types) and cannot span multiple zones. To operate clusters in a multi-zone universe, you must manually create clusters in each zone.

This document is for audiences such as application developers within the application operator group, who are responsible for managing container workloads within their organization. For more information, see [Audiences for GDC air-gapped documentation](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/resources/audiences).

## Before you begin

To create a standard cluster, request the necessary permissions and prepare your environment.

### Request IAM roles

Contact your Organization IAM Admin to grant you the following roles:

  * **Project IAM Admin** (`project-iam-admin`): grant other users the necessary roles for managing access within standard clusters.
  * **Standard Cluster Admin** (`standard-cluster-admin`): create standard clusters in the project.



These roles are bound to your project namespace.

### Prepare your environment

  * Verify that you have the appropriate setup to access and manage standard clusters. For more information, see [Manage access to standard clusters](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/application/ao-user/iam/standard-clusters).
  * Generate the kubeconfig file of the zonal API server to host your cluster. Set the environment variable `MANAGEMENT_API_SERVER` to the kubeconfig path. For more information, see [Zonal management API server resources](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform/pa-user/iam/sign-in#zonal-resources-kubeconfig).
  * Review the cluster [limits](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/resources/system-limits#cluster-management) for resource considerations.



## Plan the pod CIDR block

To allocate the appropriate sized pod CIDR block for your workloads, you must calculate the amount of IP addresses that are required for your Kubernetes cluster before you create it. Most networking parameters cannot be changed after the cluster is created.

A Kubernetes cluster follows the proceeding logic when allocating IP addresses:

  * Kubernetes assigns a `/24` CIDR block consisting of 256 addresses to each of the nodes. This amount adheres to the default maximum of 110 pods per node for Kubernetes clusters.
  * The size of the CIDR block assigned to a node depends on the maximum pods per node value.
  * The block always contains at least twice as many addresses as the maximum number of pods per node.



See the following example to understand how the default value of _Per node mask size= /24_ was calculated to accommodate 110 pods:
    
    
    Maximum pods per node = 110
    Total number of IP addresses required = 2 * 110 = 220
    
    Per node mask size = /24
    Number of IP addresses in a /24 = 2(32 - 24) = 256
    

Determine the required pod CIDR mask to configure for the Kubernetes cluster based on the required number of nodes. Plan for future node additions to the cluster while configuring the CIDR range:
    
    
      Total number of nodes supported = 2(Per node mask size - pod CIDR mask)

Given there's a default _Per node mask size= /24_ , refer to the following table that maps the pod CIDR mask to the number of nodes supported.

**Pod CIDR Mask** | **Calculation: 2(Per node mask size - CIDR mask)** | **Maximum number of nodes supported including control plane nodes**  
---|---|---  
/21 | 2(24 - 21) | 8  
/20 | 2(24-20) | 16  
/19 | 2(24 - 19) | 32  
/18 | 2(24 - 18) | 64  
**Warning:** If an insufficient CIDR mask is provided, cluster creation might become stuck in a reconciling phase with pods showing the state `CrashLoopBackOff`.

After calculating your pod CIDR block for your Kubernetes cluster, configure it as part of the cluster creation workflow in the next section.

## Create a standard cluster

To create a standard cluster, complete the following steps:

###  Console 

  1. In the [project picker](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform/pa-user/manage-projects#select-project), select your project.

Standard clusters are project-scoped resources. If you select an organization instead, you'll create a shared cluster, which is organization-scoped. For more information, see the [resource hierarchy](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/resources/resource-hierarchy#cluster).

  2. In the navigation menu, select **Kubernetes Engine > Clusters**.

  3. Click **Create Cluster**.

  4. In the **Name** field, specify a name for the cluster.

  5. Select the zone in which to create the cluster.

  6. Select the Kubernetes version for the cluster.

  7. Click **Next**.

  8. Configure the network settings for your cluster. You can't change these network settings after you create the cluster. The default and only supported Internet Protocol for Kubernetes clusters is Internet Protocol version 4 (IPv4).

     1. If you want to create dedicated _load balancer nodes_ , enter the number of nodes to create. By default, you receive zero nodes, and load balancer traffic runs through the control plane nodes.

     2. Select the **Service CIDR** (Classless Inter-Domain Routing) to use. Your deployed services, such as load balancers, are allocated IP addresses from this range.

**Important:** The range can be any RFC 1918 range that doesn't conflict with other IP address ranges in the cluster and node pool resources. For more information, see [RFC 1918](https://tools.ietf.org/html/rfc1918).
     3. Select the **Pod CIDR** to use. The cluster allocates IP addresses from this range to your pods and VMs.

     4. Click **Next**.

  9. Review the details of the auto-generated default node pool for the cluster. Click _edit_ **Edit** to modify the default node pool.

**Important:** If you intend the cluster to run graphics processing unit (GPU) workloads, you must provision a GPU machine type in your cluster. For more information, see [GPU workloads in a Kubernetes cluster](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform/pa-user/clusters#gpu).
  10. To create additional node pools, select **Add Node Pool**. When editing the default node pool or adding a new node pool, you customize it with the following options:

     1. Assign a name for the node pool. You cannot modify the name after you create the node pool.
     2. Specify the number of worker nodes to create in the node pool.
     3. Select your machine class that best suits your workload requirements. View the list of the following settings:

        * Machine type
        * CPU
        * Memory
     4. Click **Save**.

  11. Click **Create** to create the cluster.




Standard cluster creation can take up to 60 minutes to complete.

###  API 

  1. Create a `Cluster` custom resource and save it as a YAML file, such as `cluster.yaml`:
         
         apiVersion: cluster.gdc.goog/v1
         kind: Cluster
         metadata:
           name: CLUSTER_NAME
           namespace: PROJECT_NAME
         spec:
           clusterNetwork:
             podCIDRSize: POD_CIDR
             serviceCIDRSize: SERVICE_CIDR
           initialVersion:
             kubernetesVersion: KUBERNETES_VERSION
           nodePools:
           - machineTypeName: MACHINE_TYPE
             name: NODE_POOL_NAME
             nodeCount: NUMBER_OF_WORKER_NODES
             taints: TAINTS
             labels: LABELS
             acceleratorOptions:
               gpuPartitionScheme: GPU_PARTITION_SCHEME
           releaseChannel:
             channel: UNSPECIFIED
         

Replace the following:

     * `CLUSTER_NAME`: the name of the cluster. The cluster name must not end with `-system`. The `-system` suffix is reserved for clusters created by GDC.
     * `PROJECT_NAME`: the name of the project to create the cluster within.
     * `POD_CIDR`: the size of network ranges from which pod virtual IP addresses are allocated. If unset, a default value `21` is used.
     * `SERVICE_CIDR`: the size of network ranges from which service virtual IP addresses are allocated. If unset, a default value `23` is used.
     * `KUBERNETES_VERSION`: the Kubernetes version of the cluster, such as `1.26.5-gke.2100`. To list the available Kubernetes versions to configure, see [List available Kubernetes versions for a cluster](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform-application/pa-ao-operations/cluster#available-kubernetes-versions).
     * `MACHINE_TYPE`: the machine type for the worker nodes of the node pool. View the [available machine types](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform/pa-user/cluster-node-machines#available-machine-types) for what is available to configure.
     * `NODE_POOL_NAME`: the name of the node pool.
     * `NUMBER_OF_WORKER_NODES`: the number of worker nodes to provision in the node pool.
     * `TAINTS`: the taints to apply to the nodes of this node pool. This is an optional field.
     * `LABELS`: the labels to apply to the nodes of this node pool. It contains a list of key-value pairs. This is an optional field.
     * `GPU_PARTITION_SCHEME`: the GPU partitioning scheme, if you're running GPU workloads. This is an optional field. For example, `mixed-2`. The GPU is not partitioned if this field is not set. For more information about available Multi-Instance GPU (MIG) profiles, see [Supported MIG profiles](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform/pa-user/cluster-node-machines#mig-profiles).
**Note:** You cannot edit node configurations, such as GPU partitioning, after a cluster node pool is created.
  2. Apply the custom resource to your GDC instance:
         
         kubectl apply -f cluster.yaml --kubeconfig MANAGEMENT_API_SERVER
         

Replace `MANAGEMENT_API_SERVER` with the zonal API server's kubeconfig path. If you have not yet generated a kubeconfig file for the API server in your targeted zone, see [Sign in](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform/pa-user/iam/sign-in#zonal-resources-kubeconfig).




Standard cluster creation can take up to 60 minutes to complete.

###  Terraform 

  1. In a Terraform configuration file, insert the following code snippet:
         
         provider "kubernetes" {
           config_path = "MANAGEMENT_API_SERVER"
         }
         
         resource "kubernetes_manifest" "cluster-create" {
           manifest = {
             "apiVersion" = "cluster.gdc.goog/v1"
             "kind" = "Cluster"
             "metadata" = {
               "name" = "CLUSTER_NAME"
               "namespace" = "PROJECT_NAME"
             }
             "spec" = {
               "clusterNetwork" = {
                 "podCIDRSize" = "POD_CIDR"
                 "serviceCIDRSize" = "SERVICE_CIDR"
               }
               "initialVersion" = {
                 "kubernetesVersion" = "KUBERNETES_VERSION"
               }
               "nodePools" = [{
                 "machineTypeName" = "MACHINE_TYPE"
                 "name" = "NODE_POOL_NAME"
                 "nodeCount" = "NUMBER_OF_WORKER_NODES"
                 "taints" = "TAINTS"
                 "labels" = "LABELS"
                 "acceleratorOptions" = {
                   "gpuPartitionScheme" = "GPU_PARTITION_SCHEME"
                 }
               }]
               "releaseChannel" = {
                 "channel" = "UNSPECIFIED"
               }
             }
           }
         }
         

Replace the following:

     * `MANAGEMENT_API_SERVER`: the zonal API server's kubeconfig path. If you have not yet generated a kubeconfig file for the API server in your targeted zone, see [Sign in](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform/pa-user/iam/sign-in#zonal-resources-kubeconfig).
     * `CLUSTER_NAME`: the name of the cluster. The cluster name must not end with `-system`. The `-system` suffix is reserved for clusters created by GDC.
     * `PROJECT_NAME`: the name of the project to create the cluster within.
     * `POD_CIDR`: the size of network ranges from which pod virtual IP addresses are allocated. If unset, a default value `21` is used.
     * `SERVICE_CIDR`: the size of network ranges from which service virtual IP addresses are allocated. If unset, a default value `23` is used.
     * `KUBERNETES_VERSION`: the Kubernetes version of the cluster, such as `1.26.5-gke.2100`. To list the available Kubernetes versions to configure, see [List available Kubernetes versions for a cluster](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform-application/pa-ao-operations/cluster#available-kubernetes-versions).
     * `MACHINE_TYPE`: the machine type for the worker nodes of the node pool. View the [available machine types](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform/pa-user/cluster-node-machines#available-machine-types) for what is available to configure.
     * `NODE_POOL_NAME`: the name of the node pool.
     * `NUMBER_OF_WORKER_NODES`: the number of worker nodes to provision in the node pool.
     * `TAINTS`: the taints to apply to the nodes of this node pool. This is an optional field.
     * `LABELS`: the labels to apply to the nodes of this node pool. It contains a list of key-value pairs. This is an optional field.
     * `GPU_PARTITION_SCHEME`: the GPU partitioning scheme, if you're running GPU workloads. This is an optional field. For example, `mixed-2`. The GPU is not partitioned if this field is not set. For more information about available Multi-Instance GPU (MIG) profiles, see [Supported MIG profiles](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform/pa-user/cluster-node-machines#mig-profiles).
  2. Apply the new standard cluster using Terraform:
         
         terraform apply
         




Standard cluster creation can take up to 60 minutes to complete.

## What's next

  * [Manage access to standard clusters](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/application/ao-user/iam/standard-clusters)
  * [Deploy an HA container app](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform-application/pa-ao-operations/ha-apps/deploy-ha-container-app)
  * [Container workloads in GDC](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/application/ao-user/containers/containers-intro)
  * [Resource hierarchy](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/resources/resource-hierarchy)
  * [Configure Cloud NAT for standard clusters](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform/pa-user/cloud-nat-standard-clusters)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
