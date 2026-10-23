---
url: https://docs.cloud.google.com/kubernetes-engine/docs/how-to/alias-ips/
title: Create a VPC-native cluster \u00a0|\u00a0 GKE networking \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:23:36.357143+00:00
---

# Create a VPC-native cluster  |  GKE networking  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/docs/how-to/alias-ips/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ Google Kubernetes Engine (GKE) ](https://docs.cloud.google.com/kubernetes-engine/docs)
  * [ GKE networking ](https://docs.cloud.google.com/kubernetes-engine/networking/docs)
  * [ Guides ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/explore-gke-networking-docs-use-cases)



Send feedback 

#  Create a VPC-native cluster Stay organized with collections  Save and categorize content based on your preferences. 

[ Autopilot ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/autopilot-overview) [ Standard ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/choose-cluster-mode)

This page explains how to configure VPC-native [clusters](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/cluster-architecture) in Google Kubernetes Engine (GKE).

To learn more about the benefits and requirements of VPC-native clusters, see the overview for [VPC-native clusters](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/alias-ips).

For GKE Autopilot clusters, VPC-native networks are enabled by default and can't be overridden.

## Before you begin

Before you start, make sure that you have performed the following tasks: 

  * Enable the Google Kubernetes Engine API. 
[ Enable Google Kubernetes Engine API ](https://console.cloud.google.com/apis/enableflow?apiid=container.googleapis.com)
  * To use the Google Cloud CLI for this task, [install](https://docs.cloud.google.com/sdk/docs/install) and then [initialize](https://docs.cloud.google.com/sdk/docs/initialize) the gcloud CLI. If you previously installed the gcloud CLI, get the latest version by running the `gcloud components update` command. Earlier gcloud CLI versions might not support running the commands in this document. **Note:** For existing gcloud CLI installations, make sure to set the `compute/region` [property](https://docs.cloud.google.com/sdk/docs/properties#setting_properties). If you use primarily zonal clusters, set the `compute/zone` instead. By setting a default location, you can avoid errors in the gcloud CLI like the following: `One of [--zone, --region] must be supplied: Please specify location`. You might need to specify the location in certain commands if the location of your cluster differs from the default that you set.



### Limitations

  * You can't convert a VPC-native cluster into a routes-based cluster, and you can't convert a routes-based cluster into a VPC-native cluster.

  * VPC-native clusters require VPC networks. [Legacy networks](https://docs.cloud.google.com/vpc/docs/legacy) are not supported.

  * As with any GKE cluster, [Service](https://kubernetes.io/docs/concepts/services-networking/service/) (ClusterIP) addresses are only available from within the cluster. If you need to access a Kubernetes Service from VM instances outside of the cluster, but within the cluster's VPC network and region, create an [internal passthrough Network Load Balancer](https://docs.cloud.google.com/load-balancing/docs/internal).

  * If you use all of the Pod IP addresses in a subnet, you can't replace the subnet's secondary IP address range without putting the cluster into an unstable state. However, you can create additional Pod IP address ranges using [discontiguous multi-Pod CIDR](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/multi-pod-cidr).




## Create a cluster

This section shows you how to complete the following tasks at cluster creation time:

  * Create a cluster and subnet simultaneously.
  * Create a cluster in an existing subnet.
  * Create a cluster and select the control plane IP address range.
  * Create a cluster with dual-stack networking in a new subnet (available in Autopilot clusters version 1.25 or later, and Standard clusters version 1.24 or later).
  * Create a dual-stack cluster and a dual-stack subnet simultaneously (available in Autopilot clusters version 1.25 or later, and Standard clusters version 1.24 or later).



You can also create a cluster and enable auto IP address management in your cluster ([Preview](https://cloud.google.com/products#product-launch-stages)), which means that GKE automatically creates subnets and manages IP addresses for you. For more information, see [Use auto IP address management](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/enable-auto-ipam).

After you create the cluster, you can modify access to the cluster's control plane. To learn more, see [Customize your network isolation in GKE](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/latest/network-isolation#verify-control-plane-configuration).

### Create a cluster and subnet simultaneously

The following directions demonstrate how to create a VPC-native GKE cluster and subnet at the same time. The [secondary range assignment method](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/alias-ips#range_management) is managed by GKE when you perform these two steps with one command.

If using [Shared VPC](https://docs.cloud.google.com/vpc/docs/shared-vpc), you can't simultaneously create the cluster and subnet. Instead, a Network administrators in the Shared VPC host project must create the subnet first. Then you can create the cluster in an existing subnet with a secondary range assignment method of user-managed.

### gcloud

To create a VPC-native cluster and subnet simultaneously, run the following command:
    
    
    gcloud container clusters create CLUSTER_NAME \
        --location=COMPUTE_LOCATION \
        --enable-ip-alias \
        --create-subnetwork name=SUBNET_NAME,range=NODE_IP_RANGE \
        --cluster-ipv4-cidr=POD_IP_RANGE \
        --services-ipv4-cidr=SERVICES_IP_RANGE
    

Replace the following:

  * `CLUSTER_NAME`: the name of the GKE cluster.
  * `COMPUTE_LOCATION`: the [Compute Engine location](https://docs.cloud.google.com/compute/docs/regions-zones/viewing-regions-zones) for the cluster.
  * `SUBNET_NAME`: the name of the subnet to create. The subnet's region is the same region as the cluster (or the region containing the zonal cluster). Use an empty string (`name=""`) if you want GKE to generate a name for you.
  * `NODE_IP_RANGE`: an IP address range in CIDR notation, such as `10.5.0.0/20`, or the size of a CIDR block's subnet mask, such as `/20`. This is used to create the subnet's primary IP address range for nodes. If omitted, GKE chooses an available IP range in the VPC with a size of `/20`.
  * `POD_IP_RANGE`: an IP address range in CIDR notation, such as `10.0.0.0/14`, or the size of a CIDR block's subnet mask, such as `/14`. This is used to create the subnet's secondary IP address range for Pods. If omitted, GKE uses a randomly chosen `/14` range containing 218 addresses. The automatically chosen range is randomly selected from `10.0.0.0/8` (a range of 224 addresses) and does not include IP address ranges allocated to VMs, existing [routes](https://docs.cloud.google.com/vpc/docs/routes), or ranges allocated to other clusters. The automatically chosen range might conflict with [reserved IP addresses](https://docs.cloud.google.com/vpc/docs/reserve-static-external-ip-address), [dynamic routes](https://docs.cloud.google.com/vpc/docs/routes#dynamic_routes), or routes within VPCs that peer with this cluster. If you use these any of these, you should specify `--cluster-ipv4-cidr` to prevent conflicts.
  * `SERVICES_IP_RANGE`: an IP address range in CIDR notation, such as `10.4.0.0/19`, or the size of a CIDR block's subnet mask, such as `/19`. This is used to create the subnet's secondary IP address range for Services. If omitted, GKE uses `/20`, the default Services IP address range size.



### Console

You can't create a cluster and subnet simultaneously using the Google Cloud console. Instead, first [create a subnet](https://docs.cloud.google.com/vpc/docs/create-modify-vpc-networks#add-subnets) then create the cluster in an existing subnet.

### API

To create a VPC-native cluster, define an [IPAllocationPolicy](https://docs.cloud.google.com/kubernetes-engine/docs/reference/rest/v1/projects.locations.clusters#Cluster.IPAllocationPolicy) object in your cluster resource:
    
    
    {
      "name": CLUSTER_NAME,
      "description": DESCRIPTION,
      ...
      "ipAllocationPolicy": {
        "useIpAliases": true,
        "createSubnetwork": true,
        "subnetworkName": SUBNET_NAME
      },
      ...
    }
    

The `createSubnetwork` field automatically creates and provisions a subnetwork for the cluster. The `subnetworkName` field is optional; if left empty, a name is automatically chosen for the subnetwork.

After you create the cluster, you can modify access to the cluster's control plane. To learn more, see [Customize your network isolation in GKE](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/latest/network-isolation#verify-control-plane-configuration).

### Create a cluster in an existing subnet

The following instructions demonstrate how to create a VPC-native GKE cluster in an existing subnet with your choice of [secondary range assignment method](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/alias-ips#range_management).

### gcloud

  * To use a [secondary range assignment method](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/alias-ips#range_management) of _managed by GKE_ , run the following command:
        
        gcloud container clusters create CLUSTER_NAME \
            --location=COMPUTE_LOCATION \
            --enable-ip-alias \
            --subnetwork=SUBNET_NAME \
            --cluster-ipv4-cidr=POD_IP_RANGE \
            --services-ipv4-cidr=SERVICES_IP_RANGE
        

  * To use a [secondary range assignment method](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/alias-ips#range_management) of _user-managed_ , run the following command:
        
        gcloud container clusters create CLUSTER_NAME \
            --location=COMPUTE_LOCATION \
            --enable-ip-alias \
            --subnetwork=SUBNET_NAME \
            --cluster-secondary-range-name=SECONDARY_RANGE_PODS \
            --services-secondary-range-name=SECONDARY_RANGE_SERVICES
        




Replace the following:

  * `CLUSTER_NAME`: the name of the GKE cluster.
  * `COMPUTE_LOCATION`: the [Compute Engine location](https://docs.cloud.google.com/compute/docs/regions-zones/viewing-regions-zones) for the cluster.
  * `SUBNET_NAME`: the name of an existing subnet. The subnet's primary IP address range is used for nodes. The subnet must exist in the same region as the one used by the cluster. If omitted, GKE attempts to use a subnet in the `default` VPC network in the cluster's region.
  * If the secondary range assignment method is _managed by GKE_ : 
    * `POD_IP_RANGE`: an IP address range in CIDR notation, such as `10.0.0.0/14`, or the size of a CIDR block's subnet mask, such as `/14`. This is used to create the subnet's secondary IP address range for Pods. If you omit the `--cluster-ipv4-cidr` option, GKE chooses a `/14` range (218 addresses) automatically. The automatically chosen range is randomly selected from `10.0.0.0/8` (a range of 224 addresses) and won't include IP address ranges allocated to VMs, existing [routes](https://docs.cloud.google.com/vpc/docs/routes), or ranges allocated to other clusters. The automatically chosen range might conflict with [reserved IP addresses](https://docs.cloud.google.com/vpc/docs/reserve-static-external-ip-address), [dynamic routes](https://docs.cloud.google.com/vpc/docs/routes#dynamic_routes), or routes within VPCs that peer with this cluster. If you use these any of these, you should specify `--cluster-ipv4-cidr` to prevent conflicts.
    * `SERVICES_IP_RANGE`: an IP address range in CIDR notation (for example, `10.4.0.0/19`) or the size of a CIDR block's subnet mask (for example, `/19`). This is used to create the subnet's secondary IP address range for Services.
  * If the secondary range assignment method is _user-managed_ : 
    * `SECONDARY_RANGE_PODS`: the name of an existing secondary IP address range in the specified `SUBNET_NAME`. GKE uses the entire subnet secondary IP address range for the cluster's Pods.
    * `SECONDARY_RANGE_SERVICES`: the name of an existing secondary IP address range in the `SUBNET_NAME`.



### Console

  1. In the Google Cloud console, go to the **Create an Autopilot cluster** page. 

[Go to Create an Autopilot cluster](https://console.cloud.google.com/kubernetes/auto/add)

You can also complete this task by [creating a Standard cluster](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/creating-a-cluster).

  2. From the navigation pane, under **Cluster** , click **Networking**.
  3. Under **Control Plane Access** , configure access to the [control plane endpoints](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/latest/network-isolation#configure-control-plane-access).
  4. In the **Cluster networking** section, in the **Network** drop-down list, select a VPC.
  5. In the **Node subnet** drop-down list, select a subnet for the cluster.
  6. Ensure the **Enable VPC-native traffic routing (uses alias IP)** checkbox is selected.
  7. Select the **Automatically create secondary ranges** checkbox if you want the secondary range assignment method to be managed by GKE. Clear this checkbox if you have already created secondary ranges for the chosen subnet and would like the secondary range assignment method to be user-managed.
  8. In the **Pod address range** field, enter a Pod range, such as `10.0.0.0/14`.
  9. In the **Service address range** field, enter a service range, such as `10.4.0.0/19`.
  10. Configure your cluster.
  11. Click **Create**.



### Terraform

You can create a VPC-native cluster with Terraform using a [Terraform module](https://github.com/terraform-google-modules/terraform-google-kubernetes-engine).

For example, you can add the following block to your Terraform configuration:
    
    
    module "gke" {
      source  = "terraform-google-modules/kubernetes-engine/google"
      version = "~> 12.0"
    
      project_id        = "PROJECT_ID"
      name              = "CLUSTER_NAME"
      region            = "COMPUTE_LOCATION"
      network           = "NETWORK_NAME"
      subnetwork        = "SUBNET_NAME"
      ip_range_pods     = "SECONDARY_RANGE_PODS"
      ip_range_services = "SECONDARY_RANGE_SERVICES"
    }
    

Replace the following:

  * `PROJECT_ID`: your project ID.
  * `CLUSTER_NAME`: the name of the GKE cluster.
  * `COMPUTE_LOCATION`: the [Compute Engine location](https://docs.cloud.google.com/compute/docs/regions-zones/viewing-regions-zones) for the cluster. For Terraform, the Compute Engine region.
  * `NETWORK_NAME`: the name of an existing network.
  * `SUBNET_NAME`: the name of an existing subnet. The subnet's primary IP address range is used for nodes. The subnet must exist in the same region as the one used by the cluster.
  * `SECONDARY_RANGE_PODS`: the name of an existing secondary IP address range in `SUBNET_NAME`.
  * `SECONDARY_RANGE_SERVICES`: the name of an existing secondary IP address range in `SUBNET_NAME`.



### API

When you create a VPC-native cluster, you define an [IPAllocationPolicy](https://docs.cloud.google.com/kubernetes-engine/docs/reference/rest/v1/projects.locations.clusters#Cluster.IPAllocationPolicy) object. You can reference existing subnet secondary IP address ranges or you can specify CIDR blocks. Reference existing subnet secondary IP address ranges to create a cluster whose secondary range assignment method is user-managed. Provide CIDR blocks if you want the range assignment method to be managed by GKE.
    
    
    {
      "name": CLUSTER_NAME,
      "description": DESCRIPTION,
      ...
      "ipAllocationPolicy": {
        "useIpAliases": true,
        "clusterIpv4CidrBlock"      : string,
        "servicesIpv4CidrBlock"     : string,
        "clusterSecondaryRangeName" : string,
        "servicesSecondaryRangeName": string,
    
      },
      ...
    }
    

This command includes the following values:

  * `"clusterIpv4CidrBlock"`: the CIDR range for Pods. This determines the size of the secondary range for Pods, and can be in CIDR notation, such as `10.0.0.0/14`. An empty space with the given size is chosen from the available space in your VPC. If left blank, a valid range is found and created with a default size.
  * `"servicesIpv4CidrBlock"`: the CIDR range for Services. See description of `"clusterIpv4CidrBlock"`.
  * `"clusterSecondaryRangeName"`: the name of the secondary range for Pods. The secondary range must already exist and belong to the subnetwork associated with the cluster.
  * `"serviceSecondaryRangeName"`: the name of the secondary range for Services. The secondary range must already exist and belong to the subnetwork associated with the cluster.



After you create the cluster, you can modify access to the cluster's control plane. To learn more, see [Customize your network isolation in GKE](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/latest/network-isolation#verify-control-plane-configuration).

### Create a cluster and select the control plane IP address range

By default, clusters in version 1.29 or later use the primary subnet range to provision the internal IP address assigned to the control plane endpoint. You can override this default setting by selecting a different subnet range during the cluster creation time only.

The following sections show you how to create a cluster and override the subnet range.

### gcloud
    
    
    gcloud container clusters create CLUSTER_NAME \
        --enable-private-nodes \
        --enable-ip-alias \
        --private-endpoint-subnetwork=SUBNET_NAME \
        --location=COMPUTE_LOCATION
    

Where:

  * The `enable-private-nodes` flag is optional and tells GKE to create the cluster with private nodes.
  * The `private-endpoint-subnetwork` flag defines the IP address range of the control plane internal endpoint. You can use the `master-ipv4-cidr` flag instead of `private-endpoint-subnetwork` flag to provision the internal IP address for the control plane. To choose which flag to use, consider the following configurations: 
    * If you create a cluster with the `enable-private-nodes` flag, the `master-ipv4-cidr` and `private-endpoint-subnetwork` flags are optional.
    * If you use the `private-endpoint-subnetwork` flag, GKE provisions the control plane internal endpoint with an IP address from the range that you define.
    * If you use the `master-ipv4-cidr` flag, GKE creates a new subnet from the values that you provide. GKE provisions the control plane internal endpoint with an IP address from this new range.
    * If you omit the `private-endpoint-subnetwork` and the `master-ipv4-cidr` flags, GKE provisions the control plane internal endpoint with an IP address from the secondary cluster's subnetwork.



Replace the following:

  * `CLUSTER_NAME`: the name of the GKE cluster.
  * `SUBNET_NAME`: the name of an existing subnet to provision the internal IP address.
  * `COMPUTE_LOCATION`: the [Compute Engine location](https://docs.cloud.google.com/compute/docs/regions-zones/viewing-regions-zones) for the cluster.



GKE creates a [cluster with Private Service Connect](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/private-service-connect#clusters-private-service-connect). After you create the cluster, you can modify access to the cluster's control plane. To learn more, see [Customize your network isolation in GKE](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/latest/network-isolation#verify-control-plane-configuration).

### Console

To assign a subnet to the control plane of a new cluster, you must [add a subnet](https://docs.cloud.google.com/vpc/docs/using-vpc#add-subnets) first. Complete the following steps:

  1. In the Google Cloud console, go to the **Create an Autopilot cluster** page. 

[Go to Create an Autopilot cluster](https://console.cloud.google.com/kubernetes/auto/add)

You can also complete this task by [creating a Standard cluster](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/creating-a-cluster).

  2. In the Standard or Autopilot section, click **Configure**.
  3. For the **Name** , enter your cluster name.
  4. From the navigation pane, under **Cluster** , click **Networking**.
  5. Under **Control Plane Access** , configure access to the [control plane endpoints](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/latest/network-isolation#configure-control-plane-access).
  6. In the **Cluster networking** section, select the **Override control plane's default private endpoint subnet** checkbox.
  7. In the **Private endpoint subnet** list, select your created subnet.
  8. Click **Done**. Add additional authorized networks as needed.



#### Project metadata for secondary IP address ranges

When you create or upgrade a GKE cluster, GKE automatically adds project-level metadata entries like `google_compute_project_metadata` to track secondary IP address range usage, including in Shared VPC environments. This metadata verifies that GKE correctly allocates IP addresses for Pods and Services, which helps prevent conflicts.

GKE automatically manages this metadata.

**Warning** : Don't manually modify or remove this metadata, because it might cause issues with the IP address allocation and disrupt the operation of your GKE cluster.**Note:** If you use Infrastructure as Code (IaC) tools, such as Terraform, you must configure your IaC tool to ignore these metadata entries to prevent configuration drift.

The metadata has the following format:
    
    
    key:   gke-REGION-CLUSTER_NAME-GKE_UID-secondary-ranges
    value: pods:SHARED_VPC_NETWORK:SHARED_VPC_SUBNETWORK:CLUSTER_PODS_SECONDARY_RANGE_NAME
    

where:

  * `REGION`: the Google Cloud region where the cluster is located.

  * `CLUSTER_NAME`: the name of the GKE cluster.

  * `GKE_UID`: a unique identifier for the GKE cluster.

  * `VPC_NETWORK`: the name of the VPC network used by the cluster.

  * `VPC_SUBNETWORK`: the name of the subnetwork within the VPC network used by the cluster.

  * `CLUSTER_PODS_SECONDARY_RANGE_NAME`: the name of the secondary IP address range that is used for the cluster's Pods.


**Note:** The `VPC_NETWORK` and `VPC_SUBNETWORK` variables refer to the network and subnetwork used by the cluster, which could be a Shared VPC host network or the cluster's own VPC network.

### Create a cluster with dual-stack networking

You can create a cluster with IPv4/IPv6 dual-stack networking on a new or existing dual-stack subnet. Dual-stack subnet is available in Autopilot clusters version 1.25 or later, and Standard clusters version 1.24 or later. Dual-stack subnet is not supported with Windows Server node pools.

**Note:** You can [configure your cluster](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/latest/network-isolation#enable-private-nodes-cluster) to have nodes with internal (private) or external (public) access by using the `enable-private-nodes` flag. The `enable-private-nodes` flag only affects the IPv4 address of the nodes in your cluster. Therefore, this flag _doesn't_ affect the configuration of the IPv4/IPv6 dual-stack networking that you define in this section.

Before setting up dual-stack clusters, we recommend that you complete the following actions:

  * Learn more about the [benefits and requirements](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/alias-ips#dual_stack_network) of GKE clusters with dual-stack networking.
  * See the [restrictions and limitations of dual-stack networking](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/alias-ips#dual_stack_limitations).



In this section, you create a dual-stack subnet first and use this subnet to create a cluster.

  1. To create a dual-stack subnet, run the following command:
         
         gcloud compute networks subnets create SUBNET_NAME \
             --enable-dataplane-v2 \
             --stack-type=ipv4-ipv6 \
             --ipv6-access-type=ACCESS_TYPE \
             --network=NETWORK_NAME \
             --range=PRIMARY_RANGE \
             --region=COMPUTE_REGION
         

Replace the following:

     * `SUBNET_NAME`: the name of the subnet that you choose.
     * `ACCESS_TYPE`: the routability to the public internet. Use `INTERNAL` for internal IPv6 addresses or `EXTERNAL` for external IPv6 addresses. If `--ipv6-access-type` is not specified, the default access type is `EXTERNAL`.
     * `NETWORK_NAME`: the name of the network that will contain the new subnet. This network must meet the following conditions: 
       * It must be a custom mode VPC network. For more information, see how to [switch a VPC network from auto mode to custom mode](https://docs.cloud.google.com/vpc/docs/create-modify-vpc-networks#switch-network-mode).
       * If you replace the `ACCESS_TYPE` with `INTERNAL`, the network must use [Unique Local IPv6 Unicast Addresses (ULA)](https://datatracker.ietf.org/doc/html/rfc4193).
     * `PRIMARY_RANGE`: the primary IPv4 IP address range for the new subnet, in CIDR notation. For more information, see [Subnet ranges](https://docs.cloud.google.com/vpc/docs/vpc#manually_created_subnet_ip_ranges).
     * `COMPUTE_REGION`: the [compute region](https://docs.cloud.google.com/compute/docs/regions-zones#available) for the cluster.
  2. To create a cluster with a dual-stack subnet, either use the `gcloud CLI` or the Google Cloud console:




### gcloud

  * For Autopilot clusters, run the following command:
        
        gcloud container clusters create-auto CLUSTER_NAME \
              --location=COMPUTE_LOCATION \
              --network=NETWORK_NAME \
              --subnetwork=SUBNET_NAME
        

Replace the following:

    * `CLUSTER_NAME`: the name of your new Autopilot cluster.
    * `COMPUTE_LOCATION`: the [Compute Engine location](https://docs.cloud.google.com/compute/docs/regions-zones/viewing-regions-zones) for the cluster.
    * `NETWORK_NAME`: the name of a VPC network that contains the subnet. This VPC network must be a custom mode VPC network. For more information, see how to [switch a VPC network from auto mode to custom mode](https://docs.cloud.google.com/vpc/docs/create-modify-vpc-networks#switch-network-mode).
    * `SUBNET_NAME`: the name of the dual-stack subnet.

GKE Autopilot clusters default to a dual-stack cluster when you use a dual-stack subnet. After cluster creation, you can update the Autopilot cluster to be IPv4-only.

  * For Standard clusters, run the following command:
        
        gcloud container clusters create CLUSTER_NAME \
            --enable-ip-alias \
            --enable-dataplane-v2 \
            --stack-type=ipv4-ipv6 \
            --network=NETWORK_NAME \
            --subnetwork=SUBNET_NAME \
            --location=COMPUTE_LOCATION
        

Replace the following:

    * `CLUSTER_NAME`: the name of the new cluster.
    * `NETWORK_NAME`: the name of a VPC network that contains the subnet. This VPC network must be a custom mode VPC network that uses [Unique Local IPv6 Unicast Addresses (ULA)](https://datatracker.ietf.org/doc/html/rfc4193). For more information, see how to [switch a VPC network from auto mode to custom mode](https://docs.cloud.google.com/vpc/docs/create-modify-vpc-networks#switch-network-mode).
    * `SUBNET_NAME`: the name of the subnet.
    * `COMPUTE_LOCATION`: the [Compute Engine location](https://docs.cloud.google.com/compute/docs/regions-zones/viewing-regions-zones) for the cluster.



### Console

  1. In the Google Cloud console, go to the **Create an Autopilot cluster** page. 

[Go to Create an Autopilot cluster](https://console.cloud.google.com/kubernetes/auto/add)

You can also complete this task by [creating a Standard cluster](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/creating-a-cluster).

  2. In the Standard or Autopilot section, click **Configure**.
  3. Configure your cluster as needed.
  4. From the navigation pane, under **Cluster** , click **Networking**.
  5. Under **Control Plane Access** , configure access to the [control plane endpoints](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/latest/network-isolation#configure-control-plane-access).
  6. In the **Cluster networking** section, in the **Network** list, select the name of your network.
  7. In the **Node subnet** list, select the name of your dual-stack subnet.
  8. For Standard clusters, select the **IPv4 and IPv6 (dual stack)** radio button. This option is available only if you selected a dual-stack subnet.

Autopilot clusters default to a dual-stack cluster when you use a dual-stack subnet.

  9. Click **Create**.




### Create a dual-stack cluster and a subnet simultaneously

You can create a subnet and a dual-stack cluster simultaneously. GKE creates an IPv6 subnet and assigns an external IPv6 primary range to the subnet.

If using [Shared VPC](https://docs.cloud.google.com/vpc/docs/shared-vpc), you can't simultaneously create the cluster and subnet. Instead, a Network Admin in the Shared VPC host project must create the dual-stack subnet first.

  * For Autopilot clusters, run the following command:
        
        gcloud container clusters create-auto CLUSTER_NAME \
            --location=COMPUTE_LOCATION \
            --network=NETWORK_NAME \
            --create-subnetwork name=SUBNET_NAME
        

Replace the following:

    * `CLUSTER_NAME`: the name of your new Autopilot cluster.
    * `COMPUTE_LOCATION`: the [Compute Engine location](https://docs.cloud.google.com/compute/docs/regions-zones/viewing-regions-zones) for the cluster.
    * `NETWORK_NAME`: the name of a VPC network that contains the subnet. This VPC network must be a custom mode VPC network that uses [Unique Local IPv6 Unicast Addresses (ULA)](https://datatracker.ietf.org/doc/html/rfc4193). For more information, see how to [switch a VPC network from auto mode to custom mode](https://docs.cloud.google.com/vpc/docs/create-modify-vpc-networks#switch-network-mode).
    * `SUBNET_NAME`: the name of the new subnet. GKE can create the subnet based on your [organization policies](https://docs.cloud.google.com/resource-manager/docs/organization-policy/org-policy-constraints): 
      * If your organization policies allow dual-stack, and the network is custom mode, GKE creates a dual-stack subnet and assigns an external IPv6 primary range to the subnet .
      * If your organization policies don't allow dual-stack, or if the network is in auto mode, GKE creates a single stack (IPv4) subnet.
  * For Standard clusters, run the following command:
        
        gcloud container clusters create CLUSTER_NAME \
            --enable-ip-alias \
            --stack-type=ipv4-ipv6 \
            --ipv6-access-type=ACCESS_TYPE \
            --network=NETWORK_NAME \
            --create-subnetwork name=SUBNET_NAME,range=PRIMARY_RANGE \
            --location=COMPUTE_LOCATION
        

Replace the following:

    * `CLUSTER_NAME`: the name of the new cluster that you choose.
    * `ACCESS_TYPE`: the routability to the public internet. Use `INTERNAL` for internal IPv6 addresses or `EXTERNAL` for external IPv6 addresses. If `--ipv6-access-type` is not specified, the default access type is `EXTERNAL`.
    * `NETWORK_NAME`: the name of the network that will contain the new subnet. This network must meet the following conditions: 
      * It must be a custom mode VPC network. For more information, see how to [switch a VPC network from auto mode to custom mode](https://docs.cloud.google.com/vpc/docs/create-modify-vpc-networks#switch-network-mode).
      * If you replace the `ACCESS_TYPE` with `INTERNAL`, the network must use [Unique Local IPv6 Unicast Addresses (ULA)](https://datatracker.ietf.org/doc/html/rfc4193).
    * `SUBNET_NAME`: the name of the new subnet that you choose.
    * `PRIMARY_RANGE`: the primary IPv4 address range for the new subnet, in CIDR notation. For more information, see [Subnet ranges](https://docs.cloud.google.com/vpc/docs/vpc#manually_created_subnet_ip_ranges).
    * `COMPUTE_LOCATION`: the [Compute Engine location](https://docs.cloud.google.com/compute/docs/regions-zones/viewing-regions-zones) for the cluster.



## Update the stack type

You can change the stack type of an existing cluster or a update an existing subnet to a dual-stack subnet.

### Update the stack type on an existing cluster

Before you change the stack type on an existing cluster, consider the following limitations:

  * Changing the stack type is supported in new GKE clusters running version 1.25 or later. GKE clusters that have been upgraded from versions 1.24 to versions 1.25 or 1.26 might get validation errors when enabling dual-stack network. In case of errors, contact the Google Cloud [support team](https://cloud.google.com/support-hub/). 

  * Changing the stack type is a disruptive operation because GKE restarts components in both the control plane and nodes.

  * GKE respects your configured maintenance windows when recreating nodes. This means that the cluster stack type won't be operational on the cluster until the next maintenance window occurs. If you prefer not to wait, you can manually upgrade the node pool by setting the `--cluster-version` flag to the same GKE version the control plane is already running. You must use the gcloud CLI if you use this workaround. For more information, see [caveats for maintenance windows](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/maintenance-windows-and-exclusions#caveats).

  * Changing the stack type does not automatically change the IP family of existing Services. The following conditions apply:

    * If you change a single stack to dual-stack, the existing Services remain single stack.
    * If you change a dual-stack to single stack, the existing Services with IPv6 addresses get into an error state. Delete the Service and create one with the correct `ipFamilies`. To learn more, see an [example of how to set up a Deployment](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.8/how-to/create-service-ingress#expose_your_deployment_with_a_service).



To update an existing VPC-native cluster, you can use gcloud CLI or the Google Cloud console:

### gcloud

Run the following command:
    
    
      gcloud container clusters update CLUSTER_NAME \
          --stack-type=STACK_TYPE \
          --location=COMPUTE_LOCATION
    

Replace the following:

  * `CLUSTER_NAME`: the name of the cluster you want to update.
  * `STACK_TYPE`: the stack type. Replace with one of the following values: 
    * `ipv4`: to update a dual-stack cluster to IPv4 only cluster. GKE uses the primary IPv4 address range of the cluster's subnet.
    * `ipv4-ipv6`: to update an existing IPv4 cluster to dual-stack. You can only change a cluster to dual-stack if the underlying subnet supports dual-stack. To learn more, see [Update an existing subnet to a dual-stack subnet](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/alias-ips#update_an_existing_subnet_to_a_dual-stack_subnet).
  * `COMPUTE_LOCATION`: the [Compute Engine location](https://docs.cloud.google.com/compute/docs/regions-zones/viewing-regions-zones) for the cluster.



### Console

  1. Go to the **Google Kubernetes Engine** page in the Google Cloud console.

[Go to Google Kubernetes Engine](https://console.cloud.google.com/kubernetes/list)

  2. Next to the cluster you want to edit, click _more_vert_ **Actions** , then click _edit_ **Edit**.

  3. In the **Networking** section, next to **Stack type** , click _edit_ **Edit**.

  4. In the **Edit stack type** dialog, select the checkbox for the cluster stack type you need.

  5. Click **Save Changes**.




Update an existing subnet to a dual-stack subnet (available in Autopilot clusters version 1.25 or later, and Standard clusters version 1.24 or later).

### Update an existing subnet to a dual-stack subnet

To update an existing subnet to a dual-stack subnet, run the following command. Updating a subnet does not affect any existing IPv4 clusters in the subnet.
    
    
    gcloud compute networks subnets update SUBNET_NAME \
        --stack-type=ipv4-ipv6 \
        --ipv6-access-type=ACCESS_TYPE \
        --region=COMPUTE_REGION
    

Replace the following:

  * `SUBNET_NAME`: the name of the subnet.
  * `ACCESS_TYPE`: the routability to the public internet. Use `INTERNAL` for internal IPv6 addresses or `EXTERNAL` for external IPv6 addresses. If `--ipv6-access-type` is not specified, the default access type is `EXTERNAL`.
  * `COMPUTE_REGION`: the [compute region](https://docs.cloud.google.com/compute/docs/regions-zones#available) for the cluster.



## Verify the stack type, Pod, and Service IP address ranges

After you create a VPC-native cluster, you can verify its Pod and Service ranges.

### gcloud

To verify the cluster, run the following command:
    
    
    gcloud container clusters describe CLUSTER_NAME
    

The output has an `ipAllocationPolicy` block. The `stackType` field describes the type of network definition. For each type, you can see the following network information:

  * IPv4 network information:

    * `clusterIpv4Cidr` is the secondary range for Pods.
    * `servicesIpv4Cidr` is the secondary range for Services.
  * IPv6 network information (if a cluster has dual-stack networking):

    * `ipv6AccessType`: The routability to the public internet. `INTERNAL` for internal IPv6 addresses and `EXTERNAL` for external IPv6 addresses.
    * `subnetIpv6CidrBlock`: The secondary IPv6 address range for the new subnet.
    * `servicesIpv6CidrBlock`: The address range assigned for the IPv6 Services on the dual-stack cluster.



### Console

To verify the cluster, perform the following steps:

  1. Go to the **Google Kubernetes Engine** page in the Google Cloud console.

[Go to Google Kubernetes Engine](https://console.cloud.google.com/kubernetes/list)

  2. In the cluster list, click the name of the cluster you want to inspect.




The secondary ranges are displayed in the **Networking** section:

  * **Pod address range** is the secondary range for Pods
  * **Service address range** is the secondary range for Services



## Delete your cluster

To delete your cluster, follow the steps in [Deleting a cluster](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/deleting-a-cluster).

GKE tries to clean up the created subnetwork when the cluster is deleted. But if the subnetwork is being used by other resources, GKE does not delete the subnetwork, and you must manage the life of the subnetwork yourself.

## Advanced configuration for internal IP addresses

The following sections show how to use non-RFC 1918 private IP address ranges and how to enable privately used public IP address ranges.

### Use non-RFC 1918 IP address ranges

GKE clusters can use IP address ranges outside of the RFC 1918 ranges for nodes, Pods, and Services. See [valid ranges](https://docs.cloud.google.com/vpc/docs/subnets#valid-ranges) in the VPC network documentation for a list of non-RFC 1918 private ranges that can be used as internal IP addresses for subnet ranges.

This feature is not supported with Windows Server node pools.

Non-RFC 1918 private ranges are subnet ranges — you can use them exclusively or in conjunction with RFC 1918 subnet ranges. Nodes, Pods, and Services continue to use subnet ranges as described in [IP ranges for VPC-native clusters](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/alias-ips#cluster_sizing). If you use non-RFC 1918 ranges, keep the following in mind:

  * Subnet ranges, even those using non-RFC 1918 ranges, must be [assigned](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/alias-ips#range_management) manually or by GKE _before_ the cluster's nodes are created. You can't switch to or cease using non-RFC 1918 subnet ranges for node or Service IP addresses on an existing cluster unless you replace the cluster. However, you can add additional Pod CIDR ranges, including non-RFC 1918 ranges, to an existing VPC-native cluster. For more information about adding additional Pod CIDR ranges, see [expand the IP address ranges of a GKE cluster](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/multi-pod-cidr).

  * [Internal passthrough Network Load Balancers](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/internal-load-balancing) only use IP addresses from the subnet's primary IP address range. To create an internal passthrough Network Load Balancer with a non-RFC 1918 address, your subnet's primary IP address range must be non-RFC 1918.




Destinations outside your cluster might have difficulties receiving traffic from private, non-RFC 1918 ranges. For example, RFC 1112 (class E) private ranges are typically used as multicast addresses. If a destination outside of your cluster can't process packets whose sources are private IP addresses _outside_ of the RFC 1918 range, you can do the following:

  * Use an RFC 1918 range for the subnet's primary IP address range. This way, nodes in the cluster use RFC 1918 addresses.

  * Ensure that your cluster is running the [IP masquerade agent](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/ip-masquerade-agent) and that the destinations are _not_ in the `nonMasqueradeCIDRs` list. This way, packets sent from Pods have their sources changed (SNAT) to node addresses, which are RFC 1918.




### Enable privately used external IP address ranges

GKE clusters can privately use certain external IP address ranges as internal, subnet IP address ranges. You can privately use any external IP address except for [certain restricted ranges](https://docs.cloud.google.com/vpc/docs/subnets#restricted-ranges) as described the VPC network documentation. This feature is not supported with Windows Server node pools.

Your cluster _must_ be a VPC-native cluster in order to use privately used external IP address ranges. Routes-based clusters are _not_ supported.

Privately used external ranges are subnet ranges. You can use them exclusively or in conjunction with other subnet ranges that use private addresses. Nodes, Pods, and Services continue to use subnet ranges as described in [IP ranges for VPC-native clusters](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/alias-ips#cluster_sizing). Keep the following in mind when re-using external IP addresses privately:

  * When you use a external IP address range as a subnet range, your cluster can no longer communicate with systems on the Internet that use that external range. The range becomes an internal IP address range in the cluster's VPC network.

  * Subnet ranges, even those that privately use external IP address ranges, must be [assigned](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/alias-ips#range_management) manually or by GKE _before_ the cluster's nodes are created. You can't switch to or cease using non-RFC 1918 subnet ranges for node or service IP addresses on an existing cluster unless you replace the cluster. However, you can add additional Pod CIDR ranges, including non-RFC 1918 ranges, to an existing VPC-native cluster. For more information about adding additional Pod CIDR ranges, see [expand the IP address ranges of a GKE cluster](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/multi-pod-cidr).




GKE by default implements SNAT on the nodes to external IP destinations. If you have configured the Pod CIDR to use external IP addresses, the SNAT rules apply to Pod-to-Pod traffic. To avoid this you have 2 options:

  * Create your cluster with the [`--disable-default-snat`](https://docs.cloud.google.com/sdk/gcloud/reference/beta/container/clusters/create#--disable-default-snat) flag. For more details about this flag, refer to [IP masquerading in GKE](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/ip-masquerade-agent#how_ipmasq_works).
  * Configure the [configMap `ip-masq-agent`](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/ip-masquerade-agent) including in the `nonMasqueradeCIDRs` list at least the Pod CIDR, the Service CIDR, and the nodes subnet.



For Standard clusters, if the cluster version is 1.14 or later, both options will work. If your cluster version is earlier than 1.14, you can only use the second option (configuring `ip-masq-agent`).

## What's next

  * [Read the GKE network overview](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/network-overview).
  * [Learn about internal load balancing](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/internal-load-balancing).
  * [Learn about configuring authorized networks](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/authorized-networks).
  * [Learn about creating cluster network policies](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/network-policy).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
