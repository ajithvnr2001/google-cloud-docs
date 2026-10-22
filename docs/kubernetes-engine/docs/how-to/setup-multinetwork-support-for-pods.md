---
url: https://docs.cloud.google.com/kubernetes-engine/docs/how-to/setup-multinetwork-support-for-pods/
title: Set up multi-network support for Pods \u00a0|\u00a0 GKE networking \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:59:35.391650+00:00
---

# Set up multi-network support for Pods  |  GKE networking  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/docs/how-to/setup-multinetwork-support-for-pods/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ Google Kubernetes Engine (GKE) ](https://docs.cloud.google.com/kubernetes-engine/docs)
  * [ GKE networking ](https://docs.cloud.google.com/kubernetes-engine/networking/docs)
  * [ Guides ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/explore-gke-networking-docs-use-cases)



Send feedback 

#  Set up multi-network support for Pods Stay organized with collections  Save and categorize content based on your preferences. 

[ Autopilot ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/autopilot-overview) [ Standard ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/choose-cluster-mode)

You can configure Google Kubernetes Engine (GKE) clusters with multi-network support for Pods to connect Pods and nodes to multiple distinct networks simultaneously. This capability helps you address specialized network requirements, such as isolating traffic or improving throughput for high performance computing (HPC) or network function virtualization (NFV) workloads.

By default, Pods and nodes in GKE clusters use a single primary network interface for all traffic. Before you begin, ensure you understand general [networking concepts](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/network-overview), the [terminology and concepts](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/about-multinetwork-support-for-pods#terminology-concepts) specific to GKE multi-network support, and its requirements and limitations.

For more information, see [About multi-network support for Pods](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/about-multinetwork-support-for-pods).

## Requirements and limitations

Multi-network support for Pods has the following requirements and limitations:

### Requirements

  * GKE Standard version 1.28 or later.
  * GKE Autopilot version 1.29.5-gke.1091000 and later or version 1.30.1-gke.1280000 and later.
  * Multi-network support for Pods uses the same [VM-level specifications](https://docs.cloud.google.com/vpc/docs/multiple-interfaces-concepts#specifications) as multi-NIC for Compute Engine.
  * Multi-network support for Pods requires GKE Dataplane V2.
  * Multi-network support for Pods is available for Container-Optimized OS. Ubuntu support is available on nodes that are running version GKE version 1.32.3-gke.1785000 or later.



### General limitations

  * Multi-network support for Pods doesn't work for clusters that are enabled for [dual-stack networking](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/alias-ips#dual_stack_network).
  * Shared VPC is supported only on GKE version 1.28 or later.
  * [Multi-Pod CIDR](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/multi-pod-cidr) is supported only on GKE version 1.29 or later, and only for default Pod network.
  * Any Pod-networks in a single GKE cluster can't have overlapping CIDR ranges.
  * When you enable multi-network support for Pods, you can't add or remove node-network interfaces or Pod-networks after creating a node pool. To change these settings, you must recreate the node pool.
  * By default, internet access is not available on additional interfaces of Pod-networks inside the Pod. However, you can enable it manually using Cloud NAT.
  * You can't change the default Gateway inside a Pod with multiple interfaces through the API. The default Gateway must be connected to the default Pod-network.
  * The default Pod-network must always be included in Pods, even if you create additional Pod-networks or interfaces.
  * You can't configure the multi-network feature when Managed Hubble has been configured.
  * To use Shared VPC, ensure that your GKE cluster is running version 1.28.4 or later.
  * For Shared VPC deployments, all network interfaces (NICs) attached to nodes must belong to the same project as the host project.
  * Name of device typed network objects can't exceed 41 characters. The full path of each UNIX domain socket is composed, including the corresponding network name. Linux has a limitation on socket path lengths (under [107 bytes](https://linux.die.net/man/7/unix)). After accounting for the directory, filename prefix, and the `.sock` extension, the network name is limited to a maximum of 41 characters.
  * You can't mutate `Network` and `GKENetworkParamSet` objects. To update these objects, delete and recreate them.



### Device and Data Plane Development Kit (DPDK) limitations

  * A VM NIC passed into a Pod as a `Device` type NIC is not available to other Pods on the same node.
  * Pods that use DPDK mode must be run in privileged mode to access VFIO devices.
  * Autopilot mode does not support DPDK.
  * In DPDK mode, a device is treated as a node resource and is only attached to the first container (non-init) in the Pod. If you want to split multiple DPDK devices among containers in the same Pod, you need to run those containers in separate Pods.
  * On Ubuntu nodes, `DPDK-VFIO` networks are only supported with GKE version 1.33.1-gke.1959000 and later.



### Scaling limitations

GKE provides a flexible network architecture that lets you scale your cluster. You can add additional node-networks and Pod-networks to your cluster. You can scale your cluster as follows:

  * You can add up to 8 additional node-networks to each GKE node pool. This is the same scale limit for Compute Engine VMs.
  * Each pod must have fewer than 8 additional networks attached.
  * You can configure up to 35 Pod-networks across the 8 node-networks within a single node pool. You can break it down into different combinations, such as: 
    * 7 node-networks with 5 Pod-networks each
    * 5 node-networks with 7 Pod-networks each
    * 1 node-network with 30 Pod-networks. The limit for secondary ranges per subnet is 30.
  * You can configure up to 50 Pod-networks per cluster.
  * You can configure up to a maximum of 32 multi-network Pods per node.
  * You can have up to 5,000 nodes with multiple interfaces.
  * You can have up to 100,000 additional interfaces across all Pods.



## Deploy multi-network Pods

To deploy multi-network Pods, do the following:

  1. Prepare an additional VPC, subnet (node-network), and secondary ranges (Pod-network).
  2. Create a multi-network enabled GKE cluster using the Google Cloud CLI command.
  3. Create a new GKE node pool that is connected to the additional node-network and Pod-network using the Google Cloud CLI command.
  4. Create Pod network and reference the correct VPC, subnet, and secondary ranges in multi-network objects using the Kubernetes API.
  5. In your workload configuration, reference the prepared Network Kubernetes object using the Kubernetes API.



## Before you begin

Before you start, make sure that you have performed the following tasks: 

  * Enable the Google Kubernetes Engine API. 
[ Enable Google Kubernetes Engine API ](https://console.cloud.google.com/apis/enableflow?apiid=container.googleapis.com)
  * To use the Google Cloud CLI for this task, [install](https://docs.cloud.google.com/sdk/docs/install) and then [initialize](https://docs.cloud.google.com/sdk/docs/initialize) the gcloud CLI. If you previously installed the gcloud CLI, get the latest version by running the `gcloud components update` command. Earlier gcloud CLI versions might not support running the commands in this document. **Note:** For existing gcloud CLI installations, make sure to set the `compute/region` [property](https://docs.cloud.google.com/sdk/docs/properties#setting_properties). If you use primarily zonal clusters, set the `compute/zone` instead. By setting a default location, you can avoid errors in the gcloud CLI like the following: `One of [--zone, --region] must be supplied: Please specify location`. You might need to specify the location in certain commands if the location of your cluster differs from the default that you set.


  * Review the requirements and limitations.



## Prepare an additional VPC

Google Cloud creates a default Pod network during cluster creation associated with the GKE node pool used during the initial creation of the GKE cluster. The default Pod network is available on all cluster nodes and Pods. To facilitate multi-network capabilities within the node pool, you must prepare existing or new VPCs, which support `Layer 3` and `Device` type networks.

For preparing additional VPC, consider the following requirements:

  * `Layer 3` and `Netdevice` type network:

    * Create a secondary range if you are using `Layer 3` type networks.
    * Ensure that the CIDR size for the secondary range is large enough to satisfy the number of nodes in the node pool and the number of Pods per node you want to have.
    * Similar to the default Pod-network, the other Pod-networks use IP address overprovisioning. The secondary IP address range must have twice as many IP addresses per node as the number of Pods per node.
  * `Device` type network requirements: Create a regular subnet on a VPC. You don't require a secondary range.




To enable multi-network capabilities in the node pool, you must prepare the VPCs to which you want to establish additional connections. You can use an existing VPC or [Create a new VPC](https://docs.cloud.google.com/vpc/docs/create-modify-vpc-networks) specifically for the node pool.

**Note:** After the node pool is created, you can't add a new VPC to connect to the existing node pool.

### Create a VPC network that supports `Layer 3` type device

To create a VPC network that supports `Layer 3` type device, do the following:

  * Ensure that the CIDR size for the secondary range is large enough to satisfy the number of nodes in the node pool and the number of Pods per node you want to have.
  * Similar to the default Pod-network, the other Pod-networks use IP address overprovisioning. The secondary IP address range must have twice as many IP addresses per node as the number of Pods per node.




### gcloud
    
    
    gcloud compute networks subnets create SUBNET_NAME \
        --project=PROJECT_ID \
        --range=SUBNET_RANGE \
        --network=NETWORK_NAME \
        --region=REGION \
        --secondary-range=SECONDARY_RANGE_NAME=<SECONDARY_RANGE_RANGE>
    

Replace the following:

  * `SUBNET_NAME`: the name of the subnet.
  * `PROJECT_ID`: the ID of the project that contains the VPC network where the subnet is created.
  * `SUBNET_RANGE`: the primary IPv4 address range for the new subnet, in CIDR notation.
  * `NETWORK_NAME`: the name of the VPC network that contains the new subnet.
  * `REGION`: the Google Cloud region in which the new subnet is created.
  * `SECONDARY_RANGE_NAME`: the name for the secondary range.
  * `SECONDARY_IP_RANGE` the secondary IPv4 address range in CIDR notation.



###  Console 

  1. In the Google Cloud console, go to the **VPC networks** page.

  2. Click **Create VPC network**.

  3. In the **Name** field, enter the name of the network. For example, `l3-vpc`.

  4. To configure the maximum transmission unit (MTU) of the network, do the following:

     * To use the default value of `1460`, keep the **Set MTU automatically** checkbox selected.
     * To set a custom value, do the following: 
       1. Review the information in [Maximum transmission unit](https://docs.cloud.google.com/vpc/docs/mtu).
       2. Clear the **Set MTU automatically** checkbox.
       3. In the **Maximum transmission unit (MTU)** field, choose an MTU value.
  5. In the **Subnet creation mode** section, choose **Custom**.

  6. Click **ADD SUBNET**.

  7. In the **New subnet** section, specify the following configuration parameters for a subnet:

     1. Provide a **Name**. For example, `l3-subnet`.

     2. Select a **Region**.

     3. Enter an **IP address range**. This is the [primary IPv4 range](https://docs.cloud.google.com/vpc/docs/vpc#vpc_networks_and_subnets) for the subnet.

If you select a range that is not an RFC 1918 address, confirm that the range doesn't conflict with an existing configuration. For more information, see [IPv4 subnet ranges](https://docs.cloud.google.com/vpc/docs/subnets#manually_created_subnet_ip_ranges).

     4. To define a secondary range for the subnet, click **Create secondary IP address range**.

If you select a range that is not an RFC 1918 address, confirm that the range doesn't conflict with an existing configuration. For more information, see [IPv4 subnet ranges](https://docs.cloud.google.com/vpc/docs/subnets#manually_created_subnet_ip_ranges).

     5. **Private Google access** : You can enable [Private Google Access](https://docs.cloud.google.com/vpc/docs/private-access-options) for the subnet when you create it or later by editing it.

     6. **Flow logs** : You can enable [VPC flow logs](https://docs.cloud.google.com/vpc/docs/using-flow-logs) for the subnet when you create it or later by editing it.

     7. Click **Done**.

**Note:** To add more subnets, click **Add subnet**. You can also [add more subnets](https://docs.cloud.google.com/vpc/docs/create-modify-vpc-networks#add-subnets) to the network after you have created the network.
  8. In the **Firewall rules** section, under **IPv4 firewall rules** , select zero or more predefined [firewall rules](https://docs.cloud.google.com/vpc/docs/firewalls).

The rules address common use cases for connectivity to instances. You can [create your own firewall rules](https://docs.cloud.google.com/vpc/docs/using-firewalls) after you create the network. Each predefined rule name starts with the name of the VPC network that you are creating.

  9. Under **IPv4 firewall rules** , to edit the predefined ingress firewall rule named `allow-custom`, click **EDIT**.

You can edit subnets, add additional IPv4 ranges, and specify protocols and ports.

The `allow-custom` firewall rule is not automatically updated if you add additional subnets later. If you need firewall rules for the new subnets, to add the rules, you must update the firewall configuration.

  10. In the **Dynamic routing mode** section, for the VPC network. For more information, see [dynamic routing mode](https://docs.cloud.google.com/vpc/docs/vpc#routing_for_hybrid_networks). You can [change the dynamic routing mode](https://docs.cloud.google.com/vpc/docs/create-modify-vpc-networks#switch-dynamic-routing) later.

  11. Click **Create**.




### Create a VPC network that supports `Netdevice` or `DPDK` type devices

### gcloud
    
    
    gcloud compute networks subnets create SUBNET_NAME \
        --project=PROJECT_ID \
        --range=SUBNET_RANGE \
        --network=NETWORK_NAME \
        --region=REGION
    

Replace the following:

  * `SUBNET_NAME`: the name of the subnet.
  * `PROJECT_ID`: the ID of the project that contains the VPC network where the subnet is created.
  * `SUBNET_RANGE`: the primary IPv4 address range for the new subnet, in CIDR notation.
  * `NETWORK_NAME`: the name of the VPC network that contains the new subnet.
  * `REGION`: the Google Cloud region in which the new subnet is created.



###  Console 

  1. In the Google Cloud console, go to the **VPC networks** page.

  2. Click **Create VPC network**.

  3. In the **Name** field, enter the name of the network. For example, `netdevice-vpc` or `dpdk-vpc`.

  4. From the **Maximum transmission unit (MTU)** drop-down, choose appropriate MTU value.

**Note:** Before setting the MTU to a value higher than `1460`, review the [Maximum transmission unit](https://docs.cloud.google.com/vpc/docs/mtu).
  5. In the **Subnet creation mode** section, choose **Custom**.

  6. In the **New subnet** section, specify the following configuration parameters for a subnet: 

     1. Provide a **Name**. For example, `netdevice-subnet` or `dpdk-vpc`.

     2. Select a **Region**.

     3. Enter an **IP address range**. This is the [primary IPv4 range](https://docs.cloud.google.com/vpc/docs/vpc#vpc_networks_and_subnets) for the subnet.

If you select a range that is not an RFC 1918 address, confirm that the range doesn't conflict with an existing configuration. For more information, see [IPv4 subnet ranges](https://docs.cloud.google.com/vpc/docs/subnets#manually_created_subnet_ip_ranges).

     4. **Private Google Access** : Choose whether to enable [Private Google Access](https://docs.cloud.google.com/vpc/docs/private-access-options) for the subnet when you create it or later by editing it.

     5. **Flow logs** : You can enable [VPC flow logs](https://docs.cloud.google.com/vpc/docs/using-flow-logs) for the subnet when you create it or later by editing it.

     6. Click **Done**.

**Note:** To add more subnets, click **Add subnet**. You can also [add more subnets](https://docs.cloud.google.com/vpc/docs/create-modify-vpc-networks#add-subnets) to the network after you have created the network.
  7. In the **Firewall rules** section, under **IPv4 firewall rules** , select zero or more predefined [firewall rules](https://docs.cloud.google.com/vpc/docs/firewalls).

The rules address common use cases for connectivity to instances. You can [create your own firewall rules](https://docs.cloud.google.com/vpc/docs/using-firewalls) after you create the network. Each predefined rule name starts with the name of the VPC network that you are creating.

  8. Under **IPv4 firewall rules** , to edit the predefined ingress firewall rule named `allow-custom`, click **EDIT**.

You can edit subnets, add additional IPv4 ranges, and specify protocols and ports.

The `allow-custom` firewall rule is not automatically updated if you add additional subnets later. If you need firewall rules for the new subnets, to add the rules, you must update the firewall configuration.

  9. In the **Dynamic routing mode** section, for the VPC network. For more information, see [dynamic routing mode](https://docs.cloud.google.com/vpc/docs/vpc#routing_for_hybrid_networks). You can [change the dynamic routing mode](https://docs.cloud.google.com/vpc/docs/create-modify-vpc-networks#switch-dynamic-routing) later.

  10. Click **Create**.




## Create a GKE cluster with multi-network capabilities

Enabling multi-networking for a cluster adds the necessary CustomResourceDefinitions (CRDs) to the API server for that cluster. It also deploys a network-controller-manager, which is responsible for reconciling and managing multi-network objects. You can't modify the cluster configuration after it is created.

### Create a GKE Autopilot cluster with multi-network capabilities

Create a GKE Autopilot cluster with multi-network capabilities:
    
    
    gcloud container clusters create-auto CLUSTER_NAME \
        --cluster-version=CLUSTER_VERSION \
        --enable-multi-networking
    

Replace the following:

  * `CLUSTER_NAME`: the name of the cluster.
  * `CLUSTER_VERSION`: the version of the cluster.



The `--enable-multi-networking` flag enables multi-networking Custom Resource Definitions (CRDs) in the API server for this cluster, and deploys a network-controller-manager which contains the reconciliation and lifecycle management for multi-network objects.

### Create a GKE Standard cluster with multi-network capabilities

### gcloud

Create a GKE Standard cluster with multi-network capabilities:
    
    
    gcloud container clusters create CLUSTER_NAME \
        --cluster-version=CLUSTER_VERSION \
        --enable-dataplane-v2 \
        --enable-ip-alias \
        --enable-multi-networking
    

Replace the following:

  * `CLUSTER_NAME`: the name of the cluster.
  * `CLUSTER_VERSION`: the version of the cluster.



This command includes the following flags:

  * `--enable-multi-networking:` enables multi-networking Custom Resource Definitions (CRDs) in the API server for this cluster, and deploys a network-controller-manager which contains the reconciliation and lifecycle management for multi-network objects.
  * `--enable-dataplane-v2:` enables GKE Dataplane V2. This flag is required to enable multi-network.



### Console

  1. In the Google Cloud console, go to the **Create a Kubernetes cluster** page. 

[Go to Create a Kubernetes cluster](https://console.cloud.google.com/kubernetes/add)

  2. Configure your Standard cluster. For more information, see [Create a zonal cluster](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/creating-a-zonal-cluster#creating-a-cluster) or [Create a regional cluster](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/creating-a-regional-cluster). While creating the cluster, select the appropriate Network and Node subnet.
  3. From the navigation pane, under **Cluster** , click **Networking**.
  4. Select the **Enable Dataplane V2** checkbox.
  5. Select **Enable multi-networking**.
  6. Click **Create**.



#### Create a GKE Standard node pool connected to additional VPCs

Create a node pool that includes nodes connected to the node-network (VPC and subnet) and Pod-network (secondary range) created in Create Pod network.

To create the new node pool and associate it with the additional networks in the GKE cluster:

### gcloud
    
    
    gcloud container node-pools create POOL_NAME \
      --cluster=CLUSTER_NAME \
      --additional-node-network network=NETWORK_NAME,subnetwork=SUBNET_NAME \
      --additional-pod-network subnetwork=subnet-dp,pod-ipv4-range=POD_IP_RANGE,max-pods-per-node=NUMBER_OF_PODS
    

Replace the following:

  * `POOL_NAME` with the name of the new node pool.
  * `CLUSTER_NAME` with the name of the existing cluster to which you are adding the node pool.
  * `NETWORK_NAME` with the name of the network to attach the node pool's nodes.
  * `SUBNET_NAME` with the name of the subnet within the network to use for the nodes.
  * `POD_IP_RANGE` the Pod IP address range within the subnet.
  * `NUMBER_OF_PODS` maximum number of Pods per node.



This command contains the following flags:

  * `--additional-node-network`: Defines details of the additional network interface, network, and subnetwork. This is used to specify the node-networks for connecting to the node pool nodes. Specify this parameter when you want to connect to another VPC. If you don't specify this parameter, the default VPC associated with the cluster is used. For `Layer 3` type networks, specify the `additional-pod-network` flag that defines the Pod-network, which is exposed inside the GKE cluster as the `Network` object. When using the `--additional-node-network` flag, you must provide a network and subnetwork as mandatory parameters. Make sure to separate the network and subnetwork values with a comma and avoid using spaces.

Optionally, you can also specify the `stack-type` parameter ([Preview](https://cloud.google.com/products#product-launch-stages)) to configure the IP address stack type for the network interface (valid values are `ipv4`, `ipv4-ipv6`, or `ipv6`). The final network interface configuration depends on both the value that you specified for the `stack-type` field and the underlying subnet's configuration:

    * For `IPv4_ONLY` subnets, the valid value for the `stack-type` field is `ipv4`.
    * For `IPv4_IPv6` subnets, valid values for the `stack-type` field are `ipv4`, `ipv4-ipv6`, and `ipv6`.
    * For `IPv6_ONLY` subnets, the valid value for the `stack-type` field is `ipv6`.

If you don't specify a value for the `stack-type` field, the stack type defaults to IPv4 address on the NIC for IPv4-only or dual-stack subnets, and IPv6 address for IPv6-only subnets. Unless the value of the `stack-type` field is explicitly changed for dual-stack subnets, the value defaults to `ipv4` to maintain backward compatibility. For more information, see [Stack types](https://docs.cloud.google.com/vpc/docs/multiple-interfaces-concepts#stack-types).

  * `--additional-pod-network`: Specifies the details of the secondary range to be used for the Pod-network. This parameter is not required if you use a `Device` type network. This argument specifies the following key values: `subnetwork`, `pod-ipv4-range`, and `max-pods-per-node`. When using the `--additional-pod-network`, you must provide the `pod-ipv4-range` and `max-pods-per-node` values, separated by commas and without spaces.

    * `subnetwork`: links the node-network with Pod-network. The subnetwork is optional. If you don't specify it, the additional Pod-network is associated with the default subnetwork provided during cluster creation.
    * `--max-pods-per-node`: The `max-pods-per-node` must be specified and has to be a power of 2. The minimum value is 4. The `max-pods-per-node` must not be more than the `max-pods-per-node` value on the node pool.



### Console

  1. Go to the **Google Kubernetes Engine** page in the Google Cloud console.

[Go to Google Kubernetes Engine](https://console.cloud.google.com/kubernetes/list)

  2. From the navigation pane, click **Clusters**.

  3. In the **Kubernetes clusters** section, click the cluster you created.

  4. Click the **Nodes** tab.

  5. Click _add_box_ **Create user-managed node pool**.

  6. In the **Node pool details** section, complete the following:

     1. Enter a **Name** for the [node pool](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/node-pools).
     2. Enter the **Number of nodes** to create in the node pool.
  7. From the navigation pane, under **Node Pools** , click **Nodes**.

     1. From the **Image type** drop-down list, select the **Container-Optimized OS with containerd (cos_containerd)** node image.
  8. When you create a VM, you select a machine type from a [machine family](https://docs.cloud.google.com/compute/docs/machine-types) that determines the resources available to that VM. For example, a machine type like `e2-standard-4` contains 4 vCPUs, therefore can support up to 4 VPCs total. There are several machine families you can choose from and each machine family is further organized into machine series and predefined or custom machine types within each series. Each machine type is billed differently. For more information, refer to the [machine type price sheet](https://cloud.google.com/compute/pricing#standard_machine_types).

  9. From the navigation pane, select **Networking**.

  10. In the section **Node Networking** , specify the maximum number of Pods per node. The Node Networks section displays the VPC network utilized to create the cluster. It is necessary to designate extra Node Networks that correlate with previously established VPC Networks and Device types.

  11. Create node pool association:

     1. For `Layer 3` type device: 
        1. In the **Node Networks** section, click **ADD A NODE NETWORK**.
        2. From the network drop-down list select the VPC that supports Layer 3 type device.
        3. Select the subnet created for `Layer 3` VPC.
        4. In the section **Alias Pod IP address ranges** , click **Add Pod IP address range**.
        5. Select the **Secondary subnet** and indicate the **Max number of Pods per node**.
        6. Select **Done**.
     2. For `Netdevice` and `DPDK` type device: 
        1. In the **Node Networks** section, click **ADD A NODE NETWORK**.
        2. From the network drop-down list select the VPC that supports `Netdevice` or `DPDK` type devices.
        3. Select the subnet created for `Netdevice` or `DPDK` VPC.
        4. Select **Done**.
  12. Click **Create**.




**Notes:**

  * When you enable an IPv6 address on additional NICs by setting `stack-type`, ensure that your VPC firewall policies are correctly configured for IPv6 addresses. Unlike for IPv4 addresses, if Global Unicast Addresses (GUA) are used, the nodes could be exposed to the public internet if they are not properly restricted.
  * If multiple additional Pod-networks are specified within the same node-network, they must be in the same subnet.
  * You can't reference the same secondary range of a subnet multiple times.



**Example** The following example creates a node pool named pool-multi-net that attaches two additional networks to the nodes, dataplane (`Layer 3` type network) and highperformance (netdevice type network). This example assumes that you already created a GKE cluster named `cluster-1`:
    
    
    gcloud container node-pools create pool-multi-net \
      --project my-project \
      --cluster cluster-1 \
      --location us-central1-c \
      --additional-node-network network=dataplane,subnetwork=subnet-dp \
      --additional-pod-network subnetwork=subnet-dp,pod-ipv4-range=sec-range-blue,max-pods-per-node=8 \
      --additional-node-network network=highperformance,subnetwork=subnet-highperf
    

To specify additional node-network and Pod-network interfaces, define the `--additional-node-network` and `--additional-pod-network` parameters multiple times as shown in the following example:
    
    
    --additional-node-network network=dataplane,subnetwork=subnet-dp \
    --additional-pod-network subnetwork=subnet-dp,pod-ipv4-range=sec-range-blue,max-pods-per-node=8 \
    --additional-pod-network subnetwork=subnet-dp,pod-ipv4-range=sec-range-green,max-pods-per-node=8 \
    --additional-node-network network=managementdataplane,subnetwork=subnet-mp \
    --additional-pod-network subnetwork=subnet-mp,pod-ipv4-range=sec-range-red,max-pods-per-node=4
    

To specify additional Pod-networks directly on the primary VPC interface of the node pool, as shown in the following example:
    
    
    --additional-pod-network subnetwork=subnet-def,pod-ipv4-range=sec-range-multinet,max-pods-per-node=8
    

To add an IPv6-only secondary network interface, add the `stack-type` parameter as shown in the following example:
    
    
    --additional-node-network network=highperformance,subnetwork=ipv6-only-subnet,stack-type=ipv6
    

To add a dual-stack secondary network interface for both IPv4 and IPv6 address connectivity, add the `stack-type` parameter as shown in the following example:
    
    
    --additional-node-network network=service-net,subnetwork=dual-stack-subnet,stack-type=ipv4-ipv6
    

## Create Pod network

Define the Pod networks that the Pods will access by defining Kubernetes objects and linking them to the corresponding Compute Engine resources, such as VPCs, subnets, and secondary ranges.

To create Pod network, you must define the Network CRD objects in the cluster.

### Configure `Layer 3` VPC network

### YAML

For the `Layer 3` VPC, create `Network` and `GKENetworkParamSet` objects:

  1. Save the following sample manifest as `blue-network.yaml`:
         
         apiVersion: networking.gke.io/v1
         kind: Network
         metadata:
           name: blue-network
         spec:
           type: "L3"
           parametersRef:
             group: networking.gke.io
             kind: GKENetworkParamSet
             name: "l3-vpc"
         

The manifest defines a `Network` resource named `blue-network` of the type `Layer 3`. The `Network` object references the `GKENetworkParamSet` object called `l3-vpc`, which associates a network with Compute Engine resources.

  2. Apply the manifest to the cluster:
         
         kubectl apply -f blue-network.yaml
         

  3. Save the following manifest as `l3-vpc.yaml` :
         
         apiVersion: networking.gke.io/v1
         kind: GKENetworkParamSet
         metadata:
           name: "l3-vpc"
         spec:
           vpc: "l3-vpc"
           vpcSubnet: "subnet-dp"
           podIPv4Ranges:
             rangeNames:
             - "sec-range-blue"
         

This manifest defines the `GKENetworkParamSet` object named `l3-vpc` by setting the VPC name as `l3-vpc`, the subnet name as `subnet-dp`, and the secondary IPv4 address range for Pods as `sec-range-blue`.

  4. Apply the manifest to the cluster:
         
         kubectl apply -f l3-vpc.yaml
         




### Console

  1. Go to the **Google Kubernetes Engine** page in the Google Cloud console.

[Go to Google Kubernetes Engine](https://console.cloud.google.com/kubernetes/list)

  2. From the navigation pane, click **Network Function Optimizer**.

  3. At the top of the page, click _add_box_ **Create** to create your Pod network.

  4. In the **Before you begin** section, verify the details.

  5. Click **NEXT: POD NETWORK LOCATION**.

  6. In the **Pod network location** section, from the **Cluster** drop-down, select the GKE cluster that has multi-networking and GKE Dataplane V2 enabled.

  7. Click **NEXT: VPC NETWORK REFERENCE**.

  8. In the **VPC network reference** section, from the **VPC network reference** drop-down, select the VPC network used for `Layer 3` multinic Pods.

  9. Click **NEXT: POD NETWORK TYPE**.

  10. In the **Pod network type** section, select **L3** and enter the **Pod network name**.

  11. Click **NEXT: POD NETWORK SECONDARY RANGE**.

  12. In the **Pod network secondary range** section, enter the **Secondary range**.

  13. Click **NEXT: POD NETWORK ROUTES**.

  14. In the **Pod network routes** section, to define **Custom routes** , select **ADD ROUTE**.

  15. Click **CREATE POD NETWORK**.




### Configure DPDK network

### YAML

For DPDK VPC, create `Network` and `GKENetworkParamSet` objects.

  1. Save the following sample manifest as `dpdk-network.yaml`:
         
         apiVersion: networking.gke.io/v1
         kind: Network
         metadata:
           name: dpdk-network
         spec:
           type: "Device"
           parametersRef:
             group: networking.gke.io
             kind: GKENetworkParamSet
             name: "dpdk"
         

This manifest defines a `Network` resource named `dpdk-network` with a type of `Device`. The `Network` resource references a `GKENetworkParamSet` object called `dpdk` for its configuration.

  2. Apply the manifest to the cluster:
         
         kubectl apply -f dpdk-network.yaml
         

  3. For the `GKENetworkParamSet` object, save the following manifest as `dpdk.yaml`:
         
         apiVersion: networking.gke.io/v1
         kind: GKENetworkParamSet
         metadata:
           name: "dpdk"
         spec:
           vpc: "dpdk"
           vpcSubnet: "subnet-dpdk"
           deviceMode: "DPDK-VFIO"
         

This manifest defines the `GKENetworkParamSet` object named `dpdk`, sets the VPC name as `dpdk`, subnet name as `subnet-dpdk`, and deviceMode name as `DPDK-VFIO`.

  4. Apply the manifest to the cluster:
         
         kubectl apply -f dpdk.yaml
         




### Console

  1. Go to the **Google Kubernetes Engine** page in the Google Cloud console.

[Go to Google Kubernetes Engine](https://console.cloud.google.com/kubernetes/list)

  2. From the navigation pane, click **Network Function Optimizer**.

  3. At the top of the page, click _add_box_ **Create** to create your Pod network.

  4. In the **Before you begin** section, verify the details.

  5. Click **NEXT: POD NETWORK LOCATION**.

  6. In the **Pod network location** section, from the **Cluster** drop-down, select the GKE cluster that has multi-networking and GKE Dataplane V2 enabled.

  7. Click **NEXT: VPC NETWORK REFERENCE**.

  8. In the **VPC network reference** section, from the **VPC network reference** drop-down, select the VPC network used for dpdk multinic Pods.

  9. Click **NEXT: POD NETWORK TYPE**.

  10. In the **Pod network type** section, select **DPDK-VFIO (Device)** and enter the **Pod network name**.

  11. Click **NEXT: POD NETWORK SECONDARY RANGE**. The Pod network secondary range section will be unavailable

  12. Click **NEXT: POD NETWORK ROUTES**. In the Pod network routes section, select ADD ROUTE to define custom routes

  13. Click **CREATE POD NETWORK**.




**Note:** For `DPDK` network, the NIC is bound to the VFIO driver which won't show up as a normal kernel network device seen in the `ip link`.

### Configure netdevice network

For the `netdevice` VPC, create `Network` and `GKENetworkParamSet` objects.

### YAML

  1. Save the following sample manifest as `netdevice-network.yaml`:
         
         apiVersion: networking.gke.io/v1
         kind: Network
         metadata:
             name: netdevice-network
         spec:
             type: "Device"
             parametersRef:
               group: networking.gke.io
               kind: GKENetworkParamSet
               name: "netdevice"
         

This manifest defines a `Network` resource named `netdevice-network` with a type of `Device`. It references the `GKENetworkParamSet` object named `netdevice`.

  2. Apply the manifest to the cluster:
         
         kubectl apply -f netdevice-network.yaml
         

  3. Save the following manifest as `netdevice.yaml` :
         
         apiVersion: networking.gke.io/v1
         kind: GKENetworkParamSet
         metadata:
           name: netdevice
         spec:
           vpc: "netdevice"
           vpcSubnet: "subnet-netdevice"
           deviceMode: "NetDevice"
         

This manifest defines a `GKENetworkParamSet` resource named `netdevice`, sets the VPC name as `netdevice`, the subnet name as `subnet-netdevice`, and specifies the device mode as `NetDevice`.

  4. Apply the manifest to the cluster:
         
         kubectl apply -f netdevice.yaml
         




### Console

  1. Go to the **Google Kubernetes Engine** page in the Google Cloud console.

[Go to Google Kubernetes Engine](https://console.cloud.google.com/kubernetes/list)

  2. From the navigation pane, click **Network Function Optimizer**.

  3. At the top of the page, click _add_box_ **Create** to create your Pod network.

  4. In the **Before you begin** section, verify the details.

  5. Click **NEXT: POD NETWORK LOCATION**.

  6. In the **Pod network location** section, from the **Cluster** drop-down, select the GKE cluster that has multi-networking and GKE Dataplane V2 enabled.

  7. Click **NEXT: VPC NETWORK REFERENCE**.

  8. In the **VPC network reference** section, from the **VPC network reference** drop-down, select the VPC network used for netdevice multinic Pods.

  9. Click **NEXT: POD NETWORK TYPE**.

  10. In the **Pod network type** section, select **NetDevice (Device)** and enter the **Pod network name**.

  11. Click **NEXT: POD NETWORK SECONDARY RANGE**. The Pod network secondary range section will be unavailable

  12. Click **NEXT: POD NETWORK ROUTES**. In the Pod network routes section, to define custom routes, select **ADD ROUTE**.

  13. Click **CREATE POD NETWORK**.




### Configuring network routes

Configuring network route lets you define custom routes for a specific network, which are setup on the Pods to direct traffic to the corresponding interface within the Pod.

### YAML

  1. Save the following manifest as `red-network.yaml`:
         
         apiVersion: networking.gke.io/v1
         kind: Network
         metadata:
           name: red-network
         spec:
           type: "L3"
           parametersRef:
             group: networking.gke.io
             kind: GKENetworkParamSet
             name: "management"
           routes:
           -   to: "10.0.2.0/28"
         

This manifest defines a Network resource named `red-network` with a type of `Layer 3` and custom route "10.0.2.0/28" through that Network interface.

  2. Apply the manifest to the cluster:
         
         kubectl apply -f red-network.yaml
         




### Console

  1. Go to the Network Function Optimizer page in the Google Cloud console.

[Go to Network Function Optimizer](https://console.cloud.google.com/kubernetes/nfo)

  2. Click **Create**.

  3. Select a cluster that has multi-networking enabled.

  4. Configure the network preferences.

  5. Click **Create Pod network**.




## Reference the prepared `Network`

In your workload configuration, reference the prepared `Network` Kubernetes object using the Kubernetes API.

### Connect Pod to specific networks

To connect Pods to the specified networks, you must include the names of the `Network` objects as annotations inside the Pod configuration. Make sure to include both the `default` `Network` and the selected additional networks in the annotations to establish the connections.

  1. Save the following sample manifest as `sample-l3-pod.yaml`:
         
         apiVersion: v1
         kind: Pod
         metadata:
           name: sample-l3-pod
           annotations:
             networking.gke.io/default-interface: 'eth0'
             networking.gke.io/interfaces: |
               [
                 {"interfaceName":"eth0","network":"default"},
                 {"interfaceName":"eth1","network":"blue-network"}
               ]
         spec:
           containers:
           - name: sample-l3-pod
             image: busybox
             command: ["sleep", "10m"]
             ports:
             - containerPort: 80
           restartPolicy: Always
         

This manifest creates a Pod named `sample-l3-pod` with two network interfaces, `eth0` and `eth1`, associated with the `default` and `blue-network` networks, respectively.

  2. Apply the manifest to the cluster:
         
         kubectl apply -f sample-l3-pod.yaml
         




### Connect Pod with multiple networks

  1. Save the following sample manifest as `sample-l3-netdevice-pod.yaml`:
         
         apiVersion: v1
         kind: Pod
         metadata:
           name: sample-l3-netdevice-pod
           annotations:
             networking.gke.io/default-interface: 'eth0'
             networking.gke.io/interfaces: |
               [
                 {"interfaceName":"eth0","network":"default"},
                 {"interfaceName":"eth1","network":"blue-network"},
                 {"interfaceName":"eth2","network":"netdevice-network"}
               ]
         spec:
           containers:
           - name: sample-l3-netdevice-pod
             image: busybox
             command: ["sleep", "10m"]
             ports:
             - containerPort: 80
           restartPolicy: Always
         

This manifest creates a Pod named `sample-l3-netdevice-pod` with three network interfaces, `eth0`, `eth1` and `eth2` associated with the `default`, `blue-network`, and `netdevice` networks, respectively.

  2. Apply the manifest to the cluster:
         
         kubectl apply -f sample-l3-netdevice-pod.yaml
         




You can use the same annotation in any ReplicaSet (Deployment or DaemonSet) in the template's annotation section.

Sample configuration of a Pod with multiple interfaces:
    
    
    1: lo: <LOOPBACK,UP,LOWER_UP> mtu 65536 qdisc noqueue state UNKNOWN group default qlen 1000
        link/loopback 00:00:00:00:00:00 brd 00:00:00:00:00:00
        inet 127.0.0.1/8 scope host lo
          valid_lft forever preferred_lft forever
    2: eth0@if9: <BROADCAST,MULTICAST,UP,LOWER_UP> mtu 1460 qdisc noqueue state UP group default
        link/ether 2a:92:4a:e5:da:35 brd ff:ff:ff:ff:ff:ff link-netnsid 0
        inet 10.60.45.4/24 brd 10.60.45.255 scope global eth0
          valid_lft forever preferred_lft forever
    10: eth1@if11: <BROADCAST,MULTICAST,UP,LOWER_UP> mtu 1460 qdisc noqueue state UP group default qlen 1000
        link/ether ba:f0:4d:eb:e8:02 brd ff:ff:ff:ff:ff:ff link-netnsid 0
        inet 172.16.1.2/32 scope global eth1
          valid_lft forever preferred_lft forever
    

## Verification

  * Ensure that you create clusters with `--enable-multi-networking` only if `--enable-dataplane-v2` is enabled.
  * Verify that all node pools in the cluster are running Container-Optimized OS images at the time of cluster and node pool creation.
  * Verify that node pools are created with `--additional-node-network` or `--additional-pod-network` only if multi-networking is enabled on the cluster.
  * Ensure that the same subnet is not specified twice as `--additional-node-network` argument to a node pool.
  * Verify that the same secondary range is not specified as the `--additional-pod-network` argument to a node pool.
  * Follow the scale limits specified for network objects, considering the maximum number of nodes, Pods, and IP addresses allowed.
  * Verify that there is only one `GKENetworkParamSet` object which refers to a particular subnet and secondary range.
  * Verify that each network object refers to a different `GKENetworkParamSet` object.
  * Verify that the network object if it is created with a specific subnet with `Device` network, is not being used on the same node with another network with a secondary range. You can only validate this at runtime.
  * Verify that the various secondary ranges assigned to the node pools don't have overlapping IP addresses.



## Troubleshoot multi-networking parameters in GKE

To help ensure a correct network setup, Google Cloud validates multi-networking parameters when you create clusters and node pools.

**Note:** When troubleshooting issues with `Device` type networks, ensure that the `high-perf-device-plugin` and `anetd` are installed on the nodes. Also, verify that the node label `google.cloud.com/run-high-perf-daemons: "true"` is present on the nodes. This label specifically controls the `high-perf-device-plugin`.

Starting from GKE version 1.32 and later, the `high-perf-config-daemon` is only required when a `DPDK-VFIO` network is present on the node. To check the `high-perf-config-daemon`, verify that the node label `cloud.google.com/run-high-perf-config-daemons: "true"` is present. The absence of the required plugins or node labels for the specific network type may indicate an incomplete or incorrect setup.

### Invalid stack type error

When creating a node pool with an additional network interface, you might see the following error:
    
    
    Google Compute Engine: Invalid value for field 'resource.properties.networkInterfaces[1].stackType': 'UNSPECIFIED_STACK_TYPE'.
    

This error typically occurs when you use an IPv6-only subnet without explicitly setting the value of the `stack-type` field in earlier GKE versions or configurations. To resolve the issue, ensure you update the gcloud CLI components, use a newer GKE version, and explicitly include the `stack-type=ipv6` parameter in your command.

If you fail to create multi-network workloads, you can check the Pod status and events for more information:
    
    
    kubectl describe pods samplepod
    

The output is similar to the following:
    
    
    Name:         samplepod
    Namespace:    default
    Status:       Running
    IP:           192.168.6.130
    IPs:
      IP:  192.168.6.130
    ...
    Events:
      Type     Reason                  Age   From               Message
      ----     ------                  ----  ----               -------
      Normal   NotTriggerScaleUp  9s               cluster-autoscaler  pod didn't trigger scale-up:
      Warning  FailedScheduling   8s (x2 over 9s)  default-scheduler   0/1 nodes are available: 1 Insufficient networking.gke.io.networks/my-net.IP. preemption: 0/1 nodes are available: 1 No preemption victims found for incoming pod
    

The following are general reasons for Pod creation failure:

  * Failed to schedule Pod due to multi-networking resource requirements not met
  * Failed to identify specified networks



### Troubleshoot creation of Kubernetes networks

After you successfully create a network, nodes that should have access to the configured network are annotated with a network-status annotation.

To observe annotations, run the following command:
    
    
    kubectl describe node NODE_NAME
    

Replace `NODE_NAME` with the name of the node.

The output is similar to the following:
    
    
    networking.gke.io/network-status: [{"name":"default"},{"name":"dp-network"}]
    

The output lists each network available on the node. If the expected network status is not seen on the node, do the following:

#### Check if the node can access the network

If the network is not showing up in the node's network-status annotation:

  1. Verify that the node is part of a pool configured for multi-networking.
  2. Check the node's interfaces to see if it has an interface for the network you're configuring.
  3. If a node is missing network-status and has only one network interface, you must still create a pool of nodes with multi-networking enabled.
  4. If your node contains the interface for the network you're configuring but it is not seen in the network status annotation, check the `Network` and `GKENetworkParamSet` (GNP) resources.



#### Check the `Network` and `GKENetworkParamSet` resources

The status of both `Network` and `GKENetworkParamSet` (GNP) resources includes a conditions field for reporting configuration errors. We recommended checking GNP first, as it does not rely on another resource to be valid.

To inspect the conditions field, run the following command:
    
    
    kubectl get gkenetworkparamsets GNP_NAME -o yaml
    

Replace `GNP_NAME` with the name of the `GKENetworkParamSet` resource.

When the `Ready` condition is equal to true, the configuration is valid and the output is similar to the following:
    
    
    apiVersion: networking.gke.io/v1
    kind: GKENetworkParamSet
    ...
    spec:
      podIPv4Ranges:
        rangeNames:
        -   sec-range-blue
      vpc: dataplane
      vpcSubnet: subnet-dp
    status:
      conditions:
      -   lastTransitionTime: "2023-06-26T17:38:04Z"
        message: ""
        reason: GNPReady
        status: "True"
        type: Ready
      networkName: dp-network
      podCIDRs:
        cidrBlocks:
        -   172.16.1.0/24
    

When the `Ready` condition is equal to false, the output displays the reason and is similar to the following:
    
    
    apiVersion: networking.gke.io/v1
    kind: GKENetworkParamSet
    ...
    spec:
      podIPv4Ranges:
        rangeNames:
        -   sec-range-blue
      vpc: dataplane
      vpcSubnet: subnet-nonexist
    status:
      conditions:
      -   lastTransitionTime: "2023-06-26T17:37:57Z"
        message: 'subnet: subnet-nonexist not found in VPC: dataplane'
        reason: SubnetNotFound
        status: "False"
        type: Ready
      networkName: ""
    

If you encounter a similar message, ensure your GNP was configured correctly. If it already is, ensure your Google Cloud network configuration is correct. After updating Google Cloud network configuration, you may need to recreate the GNP resource to manually trigger a resync. This is to avoid infinite polling of the Google Cloud API.

Once the GNP is ready, check the `Network` resource.
    
    
    kubectl get networks NETWORK_NAME -o yaml
    

Replace `NETWORK_NAME` with the name of the `Network` resource.

The output of a valid configuration is similar to the following:
    
    
    apiVersion: networking.gke.io/v1
    kind: Network
    ...
    spec:
      parametersRef:
        group: networking.gke.io
        kind: GKENetworkParamSet
        name: dp-gnp
      type: L3
    status:
      conditions:
      -   lastTransitionTime: "2023-06-07T19:31:42Z"
        message: ""
        reason: GNPParamsReady
        status: "True"
        type: ParamsReady
      -   lastTransitionTime: "2023-06-07T19:31:51Z"
        message: ""
        reason: NetworkReady
        status: "True"
        type: Ready
    

  * `reason: NetworkReady` indicates that the Network resource is configured correctly. `reason: NetworkReady` does not imply that the Network resource is necessarily available on a specific node or actively being used.
  * If there is a misconfiguration or error, the `reason` field in the condition specifies the exact reason for the issue. In such cases, adjust the configuration accordingly.
  * GKE populates the ParamsReady field, if the parametersRef field is set to an `GKENetworkParamSet` resource that exists in the cluster. If you've specified a `GKENetworkParamSet` type parametersRef and the condition isn't appearing, make sure the name, kind, and group match the GNP resource that exists within your cluster.



## What's next

  * [Learn how to create VPC-native clusters](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/alias-ips)
  * [Codelabs](https://codelabs.developers.google.com/codelabs/gke-multinic-l3netdevice)
  * [Demo video](https://youtu.be/cLL2IvZXbIc?feature=shared)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
