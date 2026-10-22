---
url: https://docs.cloud.google.com/kubernetes-engine/docs/how-to/multi-subnet-cluster/
title: Add subnets to clusters \u00a0|\u00a0 GKE networking \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T15:00:21.068789+00:00
---

# Add subnets to clusters  |  GKE networking  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/docs/how-to/multi-subnet-cluster/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ Google Kubernetes Engine (GKE) ](https://docs.cloud.google.com/kubernetes-engine/docs)
  * [ GKE networking ](https://docs.cloud.google.com/kubernetes-engine/networking/docs)
  * [ Guides ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/explore-gke-networking-docs-use-cases)



Send feedback 

#  Add subnets to clusters Stay organized with collections  Save and categorize content based on your preferences. 

[ Autopilot ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/autopilot-overview) [ Standard ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/choose-cluster-mode)

This page shows you how to assign additional subnets to a VPC-native cluster. Additional subnets assigned to a cluster let you create new node pools where IPv4 addresses for both nodes _and_ Pods come from the additional subnet ranges.

This page is for Networking specialists who design and architect the network for their organization. To learn more about common roles and example tasks that we reference in Google Cloud content, see [Common GKE user roles and tasks](https://docs.cloud.google.com/kubernetes-engine/enterprise/docs/concepts/roles-tasks).

## Overview

When you create a new VPC-native GKE cluster, you select a default subnet for the cluster. The cluster's default subnet provides IPv4 addresses for nodes, Pods, and Services as described in [IP address ranges for VPC-native clusters](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/alias-ips#cluster_sizing).

You can assign up to eight additional subnets to a VPC-native cluster, allowing for significant cluster growth. Each newly assigned additional subnet is called a _non-default subnet_.

## Before you begin

Before you start, make sure that you have performed the following tasks: 

  * Enable the Google Kubernetes Engine API. 
[ Enable Google Kubernetes Engine API ](https://console.cloud.google.com/apis/enableflow?apiid=container.googleapis.com)
  * To use the Google Cloud CLI for this task, [install](https://docs.cloud.google.com/sdk/docs/install) and then [initialize](https://docs.cloud.google.com/sdk/docs/initialize) the gcloud CLI. If you previously installed the gcloud CLI, get the latest version by running the `gcloud components update` command. Earlier gcloud CLI versions might not support running the commands in this document. **Note:** For existing gcloud CLI installations, make sure to set the `compute/region` [property](https://docs.cloud.google.com/sdk/docs/properties#setting_properties). If you use primarily zonal clusters, set the `compute/zone` instead. By setting a default location, you can avoid errors in the gcloud CLI like the following: `One of [--zone, --region] must be supplied: Please specify location`. You might need to specify the location in certain commands if the location of your cluster differs from the default that you set.



### Requirements and limitations

This section describes the requirements and limitations that apply when you assign and use additional subnets to a cluster. You must meet all the requirements before you assign additional subnets.

  * Make sure that your GKE cluster is a VPC-native cluster that runs GKE version 1.30.3-gke.1211000 or later. Routes-based clusters and clusters on [legacy networks](https://docs.cloud.google.com/vpc/docs/legacy) don't support additional subnets.
  * You can assign up to eight additional subnets per cluster.
  * The additional subnets provide only IPv4 addresses for nodes and Pods. Additional subnets can't be used to provide IPv6 addresses for nodes or Pods.
  * Only new node pools can use the additional subnets, not existing node pools. By default, GKE automatically selects an appropriate subnet for the node pool. You can optionally manually specify a subnet when creating a node pool.
  * Subnet secondary IPv4 address ranges in a non-default subnet can only be used by a single cluster.
  * If you use [multi-network support for Pods](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/about-multinetwork-support-for-pods), the primary and Pod IPv4 address ranges of an additional subnet must not overlap with any CIDR ranges that are configured within your multi-network setup. Additional subnets that you configure apply only to the _default_ network. This limitation means that any additional network interfaces on your nodes and Pods can't use the IP addresses provided by these additional subnets.
  * When you add a subnet to clusters that have Cloud Service Mesh enabled, the mesh can't route traffic to Pods in the non-default subnet.



### Load balancer requirements for clusters with additional subnets

This section describes the load balancer requirements that apply when you use additional subnets on your cluster. These requirements apply each time you create an external Ingress, external Gateway, or external LoadBalancer Service.

  * To use an external Ingress, Gateway, or LoadBalancer Service in a cluster with additional subnets, your cluster must run GKE version 1.33.2-gke.4780000 or later.
  * External Ingress objects using the GKE Ingress controller must use [container-native load balancing](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/ingress#container-native_load_balancing).
  * [Enable GKE subsetting](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/internal-load-balancing#enable_ilb_subsetting_existing_cluster) for internal LoadBalancer Services. GKE subsetting affects only _new_ internal LoadBalancer Services. Therefore, you must delete and recreate any existing Services in your cluster after you enable GKE subsetting.
  * To [create a backend service-based regional external passthrough Network Load Balancer](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/backend-service-based-external-load-balancer#create-the-external-lb-service), new external LoadBalancer Services must include the `spec.loadBalancerClass` field set to `networking.gke.io/l4-regional-external`. This field affects only _new_ external LoadBalancer Services and doesn't apply to existing external LoadBalancer Services. Delete and recreate all external LoadBalancer Services that were created _without_ the `spec.loadBalancerClass` field. This field requires GKE version 1.33.1-gke.1779000 or later.

The backend type that's used (`GCE_VM_IP` NEG backends or instance group backends) depends on the GKE version when you create the external LoadBalancer Service. For more information, see [Node grouping](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/service-load-balancer#endpoint-grouping).




## Add a new subnet with one Pod IPv4 address range

  1. Create a new subnet and add a new subnet secondary IPv4 address range. The subnet must in the same region and VPC network as the cluster:
         
         gcloud compute networks subnets create SUBNET_NAME \
              --network=NETWORK \
              --region=REGION \
              --range=PRIMARY_RANGE \
              --secondary-range=POD_RANGE_NAME=SECONDARY_RANGE \
              --enable-private-ip-google-access
         

Replace the following:

     * `SUBNET_NAME`: the name of the new subnet.
     * `NETWORK`: the name of the VPC network that contains the new subnet.
     * `REGION`: the region in which the subnet is located.
     * `PRIMARY_RANGE`: the primary IPv4 range for the new subnet, in CIDR notation. For more information, see [IPv4 subnet ranges](https://docs.cloud.google.com/vpc/docs/subnets#manually_created_subnet_ip_ranges).
     * `POD_RANGE_NAME`: a name for the secondary range.
     * `SECONDARY_RANGE`: the secondary IPv4 range in CIDR notation. For valid ranges, see [IPv4 subnet ranges](https://docs.cloud.google.com/vpc/docs/subnets#manually_created_subnet_ip_ranges).

For more information, see [Work with subnets](https://docs.cloud.google.com/vpc/docs/create-modify-vpc-networks#subnet-rules).

  2. Update your cluster to use the additional subnet by using the gcloud CLI:
         
         gcloud container clusters update CLUSTER_NAME \
              --additional-ip-ranges=subnetwork=SUBNET_NAME,pod-ipv4-range=POD_RANGE_NAME
         

Replace the following:

     * `CLUSTER_NAME`: the name of your existing cluster.
     * `SUBNET_NAME`: the name of the new subnet that you created.
     * `POD_RANGE_NAME`: the name of the subnet secondary IPv4 address range that you want to use for the Pod IPv4 address range.



## Add a new subnet with multiple Pod IPv4 address ranges

  1. [Create a new subnet](https://docs.cloud.google.com/vpc/docs/create-modify-vpc-networks#add-subnets) in the same region and VPC network as the cluster. Set the subnet primary IPv4 address range to an additional IPv4 address range for nodes.

  2. For each additional Pod IPv4 address range you need, [add a new subnet secondary IPv4 address range](https://docs.cloud.google.com/vpc/docs/create-modify-vpc-networks#edit-secondary) to the subnet you created in the previous step.

  3. Update your cluster to use the additional subnet by using the gcloud CLI. The following example adds one subnet that has two subnet secondary IPv4 address ranges for Pods.
         
         gcloud container clusters update CLUSTER_NAME \
              --additional-ip-ranges=subnetwork=SUBNET_NAME,pod-ipv4-range=POD_RANGE_NAME_1 \
              --additional-ip-ranges=subnetwork=SUBNET_NAME,pod-ipv4-range=POD_RANGE_NAME_2
         

Replace the following:

     * `CLUSTER_NAME`: the name of your existing cluster.
     * `SUBNET_NAME`: the name of the new subnet that you created.
     * `POD_RANGE_NAME_1` and `POD_RANGE_NAME_2`: the names of the subnet secondary IPv4 address ranges that you want to use for Pod IPv4 address ranges.



### Verify the subnets

**By cluster** : To see the details of all subnets associated with a cluster, run the following command:
    
    
       gcloud container clusters describe CLUSTER_NAME
    

Replace `CLUSTER_NAME` with the name of your cluster.

The output is similar to the following:
    
    
    ipAllocationPolicy:
      additionalIPRangesConfig:
      - podIpv4RangeNames:
        - pod-range-1
        subnetwork: projects/user-gke-dev-2/regions/us-central1/subnetworks/shared-msc-subnets
    

**By node pool** : To see the details of all subnets associated with a node pool, run the following command:
    
    
    gcloud container node-pools describe POOL_NAME \
        --cluster=CLUSTER_NAME \
    

Replace the following:

  * `POOL_NAME`: the name of the node pool.
  * `CLUSTER_NAME`: the name of the cluster.



The output is similar to the following:
    
    
    name: pool-1
    networkConfig:
      podRange: pod-range-1
      subnetwork: projects/user-gke-dev-2/regions/us-central1/subnetworks/shared-msc-subnets
    

## How node pools select a subnet

By default, when you create a new node pool and multiple subnets are available, GKE automatically selects an appropriate subnet for the node pool based on the requirements for IP addresses and the availability of IP addresses in all cluster subnets.

## Manually specify a subnet during node pool creation

To specify a subnet when you create a node pool, use the `--subnetwork` flag with the `gcloud container node-pools create` command. The subnet you specify must already be assigned to the cluster (either as the default subnet or as an additional subnet). If you don't specify a Pod IPv4 range, GKE automatically selects an available secondary range from the specified subnet. If the specified subnet or Pod range doesn't have enough available IP addresses for the node pool, GKE returns an error.
    
    
    gcloud container node-pools create POOL_NAME \
        --cluster=CLUSTER_NAME \
        --location=LOCATION \
        --subnetwork=SUBNET_NAME
    

### Specify the Pod IPv4 address range along with the subnet

If the specified subnet has multiple secondary IPv4 address ranges, you can use both the `--pod-ipv4-range` flag and the `--subnetwork` flag to specify which range to use for the Pods in the node pool. 
    
    
    gcloud container node-pools create POOL_NAME \
        --cluster=CLUSTER_NAME \
        --location=LOCATION \
        --subnetwork=SUBNET_NAME \
        --pod-ipv4-range=POD_RANGE_NAME
    

Replace the following:

  * `POOL_NAME`: a name for the new node pool.
  * `CLUSTER_NAME`: the name of the cluster.
  * `LOCATION`: the region or zone of the cluster.
  * `SUBNET_NAME`: the name or full resource path of the subnet you want to use.
  * `POD_RANGE_NAME`: the name of the subnet secondary range to use for Pods in this node pool.



## Remove a non-default subnet

Removing a non-default subnet from a cluster instructs the cluster to no longer use the subnet's ranges in any of the cluster's node pools. Removal has the following effects:

  * The non-default subnet's primary IPv4 address range can't be used for node IPv4 address ranges.
  * The subnet secondary IPv4 ranges in the non-default subnet can't be used for Pod IPv4 ranges.



Before you remove a non-default subnet, you must delete all node pools that use this subnet. Setting the subnet to draining status is the recommended first step. Subnets in the draining status won't be considered for usage by newly created node pools. This prevents cluster autoscaler operations (like node pool scale-up) from selecting the subnet you intend to remove, without needing to disable autoscaling for the entire cluster.

The steps to remove a subnet:

  1. Set the non-default subnet to draining status. This prevents new node pools from selecting this subnet, which is useful when you enable autoscaling on the cluster.
  2. Delete all node pools that are using this subnet.
  3. Remove the subnet from the cluster.



To remove a non-default subnet from the cluster, run the following command:
    
    
       gcloud container clusters update CLUSTER_NAME \
         --remove-additional-ip-ranges=subnetwork=SUBNET_NAME
    

Replace the following:

  * `CLUSTER_NAME`: the name of your cluster.
  * `SUBNET_NAME`: the name of the subnet that you want to remove from the cluster.



To set the status of a non-default subnet to draining, run the following command:
    
    
       gcloud container clusters update CLUSTER_NAME \
         --drain-additional-ip-ranges=subnetwork=SUBNET_NAME
    

Replace the following:

  * `CLUSTER_NAME`: the name of your cluster.
  * `SUBNET_NAME`: the name of the subnet that you want to set to drain status.



To undrain a non-default subnet, run the following command:
    
    
       gcloud container clusters update CLUSTER_NAME \
         --undrain-additional-ip-ranges=subnetwork=SUBNET_NAME
    

Replace the following:

  * `CLUSTER_NAME`: the name of your cluster.
  * `SUBNET_NAME`: the name of the subnet that you want to undrain.



After removing a non-default subnet from the cluster, you can [delete the non-default subnet](https://docs.cloud.google.com/vpc/docs/create-modify-vpc-networks#deleting_subnets).

## Remove a non-default subnet secondary IPv4 range

When you remove a non-default subnet secondary IPv4 range from a cluster, GKE instructs the cluster to not use that range for Pod IPv4 ranges in any node pool. If the non-default subnet secondary IPv4 range that you remove is the only range of the non-default subnet that's used by this cluster, GKE also instructs the cluster to stop using this subnet's primary IPv4 address for node IPv4 addresses.

Before you remove a non-default subnet secondary IPv4 range, you must delete all node pools that use the range for Pod IPv4 addresses.

To remove a non-default subnet secondary IPv4 range from the cluster, run the following command:
    
    
       gcloud container clusters update CLUSTER_NAME \
         --remove-additional-ip-ranges=subnetwork=SUBNET_NAME,pod-ipv4-range=POD_RANGE_NAME
    

Replace the following:

  * `CLUSTER_NAME`: the name of the cluster.
  * `SUBNET_NAME`: the name of the non-default subnet.
  * `POD_RANGE_NAME`: the name of the non-default subnet secondary IPv4 range that you want to remove from the cluster.



After removing a non-default subnet secondary IPv4 range from the cluster, you can [delete the non-default subnet secondary IPv4 range](https://docs.cloud.google.com/vpc/docs/create-modify-vpc-networks#edit-secondary).

## Use additional subnets in Shared VPC

Before you proceed, make sure you have the following:

  * A functional Shared VPC environment where the host and service projects are attached. For instructions, see [Set up a cluster with Shared VPC](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/cluster-shared-vpc#before_you_begin).
  * A running GKE cluster located in the service project.
  * All necessary APIs are enabled in both the host and service projects.


  1. Create an additional subnet in the host project under the same network of the GKE cluster:
         
         gcloud compute networks subnets create ADDITIONAL_SUBNET_NAME \
           --project HOST_PROJECT_ID \
           --network shared-net \
           --range 172.16.4.0/22 \
           --region COMPUTE_REGION \
           --secondary-range ADDITIONAL_SUBNET_NAME-services=172.16.16.0/20,ADDITIONAL_SUBNET_NAME-pods=172.20.0.0/14
         

  2. Get the IAM policy. To enable the GKE cluster in the Service Project to access additional subnets within the host project's Shared VPC, you must configure the necessary IAM permissions. If permissions are not already configured, proceed with the following steps. No action is needed if the permissions already exist.
         
         gcloud compute networks subnets get-iam-policy ADDITIONAL_SUBNET_NAME \
             --project HOST_PROJECT_ID \
             --region COMPUTE_REGION
         

The output contains an `etag` field. Make a note of the `etag` value.

  3. Create a file named ADDITIONAL_SUBNET_NAME-policy.yaml that has the following content:
         
         bindings:
           - members:
             - serviceAccount:SERVICE_PROJECT_NUM@cloudservices.gserviceaccount.com
             - serviceAccount:service-SERVICE_PROJECT_NUM@container-engine-robot.iam.gserviceaccount.com
             role: roles/compute.networkUser
           etag: ETAG_STRING
         

Replace `ETAG_STRING` with the `etag` value that you noted previously.

  4. Set the IAM policy for the ADDITIONAL_SUBNET_NAME subnet:
         
         gcloud compute networks subnets set-iam-policy ADDITIONAL_SUBNET_NAME \
               ADDITIONAL_SUBNET_NAME-policy.yaml \
               --project HOST_PROJECT_ID \
               --region COMPUTE_REGION
         

  5. Verify usable subnets and secondary IP address ranges, as described in [shared vpc verify usable subnets](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/cluster-shared-vpc#verify_usable_subnets).

  6. Update the Shared VPC cluster of the additional subnets:



    
    
        gcloud container clusters update CLUSTER_NAME \
            --project=SERVICE_PROJECT_ID \
            --location=CONTROL_PLANE_LOCATION \
            --additional-ip-ranges=subnetwork=projects/HOST_PROJECT_ID/regions/COMPUTE_REGION/subnetworks/ADDITIONAL_SUBNET_NAME,pod-ipv4-range=ADDITIONAL_SUBNET_NAME-pods
    

Replace the following:

  * CLUSTER_NAME: the name of your GKE cluster in the service project.
  * ADDITIONAL_SUBNET_NAME: the name of the additional subnet you created in the host project (e.g., tier-2).
  * HOST_PROJECT_ID: the host project ID.
  * SERVICE_PROJECT_NUM: the service project name.
  * COMPUTE_REGION: the region in which the subnet is located.



This lets you use the additional subnets in a Shared VPC environment.

## What's next

  * Learn more about [VPC-native clusters](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/alias-ips).
  * Read more about how to [add Pod IPv4 address ranges](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/multi-pod-cidr).
  * Learn more about optimizing IP address allocation by [configuring maximum Pods per node](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/flexible-pod-cidr).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
