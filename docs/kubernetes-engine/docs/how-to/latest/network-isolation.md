---
url: https://docs.cloud.google.com/kubernetes-engine/docs/how-to/latest/network-isolation/
title: Customize your network isolation in GKE \u00a0|\u00a0 GKE networking \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:22:33.858565+00:00
---

# Customize your network isolation in GKE  |  GKE networking  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/docs/how-to/latest/network-isolation/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ Google Kubernetes Engine (GKE) ](https://docs.cloud.google.com/kubernetes-engine/docs)
  * [ GKE networking ](https://docs.cloud.google.com/kubernetes-engine/networking/docs)
  * [ Guides ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/explore-gke-networking-docs-use-cases)



Send feedback 

#  Customize your network isolation in GKE Stay organized with collections  Save and categorize content based on your preferences. 

[ Autopilot ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/autopilot-overview) [ Standard ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/choose-cluster-mode)

Version 1.29 and later keyboard_arrow_down

  * [ Latest ](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/latest/network-isolation)
  * [ Version 1.28 and earlier ](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/legacy/network-isolation)



This page explains how to configure network isolation for Google Kubernetes Engine (GKE) clusters when you create or update your cluster.

**Best practice** : 

Plan and design your cluster network isolation with your organization's Network architects, Network administrators, or any other Network engineers team responsible for defining, implementing, and maintaining the network architecture.

## How cluster network isolation works

In a GKE cluster, network isolation depends on who can access the cluster components and how. You can control:

  * **Control plane access** : You can customize external access, limited access, or unrestricted access to the control plane.
  * **Cluster networking** : You can choose who can access the nodes in Standard clusters, or the workloads in Autopilot clusters.



Before you create your cluster, consider the following:

  1. Who can access the control plane and how is the control plane exposed?
  2. How are your nodes or workloads exposed?



To answer these questions, follow the plan and design guidelines in [About network isolation](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/network-isolation).

## Restrictions and limitations

By default, GKE creates your clusters as [VPC-native clusters](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/alias-ips). VPC-native clusters don't support [legacy networks](https://docs.cloud.google.com/vpc/docs/legacy).

**Node pool-level Pod secondary ranges** : when creating a GKE cluster, if you specify a Pod secondary range smaller than `/24` per node pool using the UI, you might encounter the following error:
    
    
    Getting Pod secondary range 'pod' must have a CIDR block larger or equal to /24
    

GKE does not support specifying a range smaller than `/24` at the node pool level. However, specifying a smaller range at the cluster level is supported. This can be done by using Google Cloud CLI with the `--cluster-ipv4-cidr` argument. For more information, see [Creating a cluster with a specific CIDR range](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/alias-ips#cluster_sizing).

Expand the following sections to view the rules around IP address ranges and traffic when creating a cluster.

#### Control plane

  * You can add up to 100 authorized networks, including both external and internal IP addresses, in a project . For more information, refer to [Define the IP addresses that can access the control plane](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/latest/network-isolation#define-ip-access).   
  
For clusters that were created on versions prior to 1.29, you can add up to only 50 authorized networks if your cluster meets the following conditions. You can check these conditions by running the [`gcloud container clusters describe`](https://docs.cloud.google.com/sdk/gcloud/reference/container/clusters/describe) command: 
    * The `privateClusterConfig` resource does not exist.
    * Or, if `privateClusterConfig` exists, the resource has both of the following values:
      * The `peeringName` field is empty or doesn't exist.
      * The `privateEndpoint` field doesn't have any value assigned.
  * While GKE can detect overlap with the control plane address block, it cannot detect overlap within a [Shared VPC](https://docs.cloud.google.com/vpc/docs/shared-vpc) network.



#### Cluster networking

  * Internal IP addresses for nodes come from the primary IP address range of the subnet you choose for the cluster. Pod IP addresses and Service IP addresses come from two subnet secondary IP address ranges of that same subnet. For more information, see [IP ranges for VPC-native clusters](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/alias-ips#cluster_sizing).
  * GKE supports any internal IP address ranges, including private ranges (RFC 1918 and other private ranges) and privately used external IP address ranges. See the VPC documentation for a list of [valid internal IP address ranges](https://docs.cloud.google.com/vpc/docs/subnets#valid-ranges).
  * If you [expand the primary IP range of a subnet](https://docs.cloud.google.com/vpc/docs/create-modify-vpc-networks#expand-subnet) to accommodate additional nodes, then you must add the expanded subnet's primary IP address range to the list of authorized networks for your cluster. If you don't, ingress-allow firewall rules relevant to the control plane aren't updated, and new nodes created in the expanded IP address space won't be able to register with the control plane. This can lead to an outage where new nodes are continuously deleted and replaced. Such an outage can happen when performing node pool upgrades or when nodes are automatically replaced due to liveness probe failures.
  * All nodes in a cluster with only private nodes are created without an external IP; they have limited access to Google Cloud APIs and services. To provide outbound internet access for your private nodes, you can use [Cloud NAT](https://docs.cloud.google.com/nat/docs/overview#NATwithGKE).
  * [Private Google Access](https://docs.cloud.google.com/vpc/docs/private-google-access) is enabled automatically when you create a cluster unless you are using Shared VPC. You must not disable Private Google Access unless you are using NAT to access the internet.



## Before you begin

Before you start, make sure that you have performed the following tasks: 

  * Enable the Google Kubernetes Engine API. 
[ Enable Google Kubernetes Engine API ](https://console.cloud.google.com/apis/enableflow?apiid=container.googleapis.com)
  * To use the Google Cloud CLI for this task, [install](https://docs.cloud.google.com/sdk/docs/install) and then [initialize](https://docs.cloud.google.com/sdk/docs/initialize) the gcloud CLI. If you previously installed the gcloud CLI, get the latest version by running the `gcloud components update` command. Earlier gcloud CLI versions might not support running the commands in this document. **Note:** For existing gcloud CLI installations, make sure to set the `compute/region` [property](https://docs.cloud.google.com/sdk/docs/properties#setting_properties). If you use primarily zonal clusters, set the `compute/zone` instead. By setting a default location, you can avoid errors in the gcloud CLI like the following: `One of [--zone, --region] must be supplied: Please specify location`. You might need to specify the location in certain commands if the location of your cluster differs from the default that you set.



## Configure control plane access

When you create a GKE cluster in any version by using Google Cloud CLI or in version 1.29 and later using the Console, the control plane is accessible through the following interfaces:

  * DNS-based endpoint.
  * IP-based endpoints.



### DNS-based endpoint

Access to the control plane depends on the DNS resolution of the source traffic. Enable the DNS-based endpoint to get the following benefits:

  * Create a dynamic access policy based on IAM policies.
  * Access the control plane from other VPC networks or external locations without the need of setting up bastion host or proxy nodes.



To configure access to the DNS-based endpoint, see Define the DNS-based endpoint access.

### IP-based endpoints

Access to control plane endpoints depends on the source IP address and is controlled by your authorized networks. You can manage access to the IP-based endpoints of the control plane, including:

  * Enable or disable the IP-based endpoint.
  * Enable or disable the external endpoint to allow access from external traffic. The internal endpoint is always enabled when you enable the control plane IP-based endpoints.
  * Add [authorized networks](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/network-isolation#how_authorized_networks_work) to allowlist or deny access from public IP addresses. If you don't configure authorized networks, the control plane is accessible from any external IP address. This includes public internet or Google Cloud external IP addresses addresses with no restrictions.
  * Allowlist or deny access from any or all private IP addresses in the cluster.
  * Allowlist or deny access from [Google Cloud external IP addresses](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/network-isolation#terminology), which are external IP addresses assigned to any VM used by any customer hosted on Google Cloud.

**Caution:** We don't recommend that you allowlist access from all Google Cloud external IP addresses to the control plane because it provides minimal security benefits. Consider adding authorized networks to restrict access to the control plane from specific ranges that you control, or use a DNS-based endpoint.
  * Allowlist or deny access from IP addresses in other Google Cloud regions.




Review the [limitations of using IP-based endpoints](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/network-isolation#limitations-ip-endpoints) before you define the control plane access.

### Create a cluster and define control plane access

To create or update an Autopilot or a Standard cluster, use either the Google Cloud CLI or the Google Cloud console.

### Console

To create a cluster, complete the following steps:

  1. Go to the **Google Kubernetes Engine** page in the Google Cloud console.

[Go to Google Kubernetes Engine](https://console.cloud.google.com/kubernetes/list)

  2. Click _add_box_ **Create**.

  3. Configure the attributes of your cluster based on your project needs.

  4. In the navigation menu, click **Networking**.

  5. Under **Control Plane Access** , configure the control plane endpoints:

     1. Select the **Access using DNS** checkbox to enable the control plane DNS-based endpoints.
     2. Optional: Enable authentication to the DNS-based endpoint by using Kubernetes credentials:

        * To use Kubernetes ServiceAccount bearer tokens, select the **Enable Kubernetes tokens via DNS** checkbox.
        * To use X.509 client certificates, select the **Enable Kubernetes certificates via DNS** checkbox.
**Best practice** : 

ServiceAccount tokens and client certificates can add complexity and management overhead to your security configuration. Unless your use case requires one of these authentication methods, [use IAM credentials to authenticate to your control plane](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/api-server-authentication).

     3. Select the **Access using IPv4 addresses** checkbox to enable the control plane IP-based endpoints. Use the configuration included in Define the IP addresses that can access the control plane to customize access to the IP-based endpoints.




### gcloud

For Autopilot clusters, run the following command:
    
    
      gcloud container clusters create-auto CLUSTER_NAME \
        --enable-ip-access  \
        --enable-dns-access
    

For Standard clusters, run the following command:
    
    
      gcloud container clusters create CLUSTER_NAME \
          --enable-ip-access \
          --enable-dns-access
    

Replace the following:

  * `CLUSTER_NAME`: the name of your cluster.



Both commands include flags that enable the following:

  * `enable-dns-access`: Enables access to the control plane by using the DNS-based endpoint of the control plane. If you specify this flag, you can also specify the following optional flags:

    * `enable-k8s-tokens-via-dns`: enable authentication to the DNS-based endpoint by using Kubernetes ServiceAccount bearer tokens.
    * `enable-k8s-certs-via-dns`: enable authentication to the DNS-based endpoint by using Kubernetes X.509 client certificates.
**Best practice** : 

ServiceAccount tokens and client certificates can add complexity and management overhead to your security configuration. Unless your use case requires one of these authentication methods, [use IAM credentials to authenticate to your control plane](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/api-server-authentication).

  * `enable-ip-access`: Enables access to the control plane by using IPv4 addresses. If you want to disable both the internal and external endpoints of the control plane, use the `no-enable-ip-access` flag instead.


**Note:** The `get-credentials` command automatically uses the IP-based endpoint if the IP-based endpoint access is enabled. To instruct `get-credentials` to use the DNS-based endpoint, add the `--dns-endpoint` flag when running the `get-credentials` command.

Use the flags listed in Define the IP addresses that can access the control plane to customize access to the IP-based endpoints.

#### Define access to the DNS-based endpoint

You can manage authentication and authorization to the DNS-based endpoint by configuring the IAM permission `container.clusters.connect`. To configure this permission, assign one of the following IAM [roles](https://docs.cloud.google.com/iam/docs/roles-permissions/container) to your Google Cloud project:

  * `roles/container.developer`
  * `roles/container.viewer`



Optionally, you can manage the reachability of the DNS-based endpoint by using the following features:

  * **VPC Service Controls** : the DNS-based endpoint supports [VPC Service Controls](https://docs.cloud.google.com/vpc-service-controls/docs/overview) to add a layer of security to your control plane access. VPC Service Controls work consistently across Google Cloud APIs.

  * **Access to the DNS-based endpoint from clients with no public internet access** : the DNS-based endpoint is accessible through Google Cloud APIs that are available on the public internet. To access the DNS-based endpoint from private clients, you can use [Private Google Access](https://docs.cloud.google.com/vpc/docs/private-google-access), [Cloud NAT gateway](https://docs.cloud.google.com/nat/docs/overview), or [Private Service Connect for Google Cloud APIs](https://docs.cloud.google.com/vpc/docs/configure-private-service-connect-apis).


**Note:** If you want to use a Private Service Connect endpoint to access the DNS-based endpoint, in addition to [creating an endpoint](https://docs.cloud.google.com/vpc/docs/configure-private-service-connect-apis), you must also [create DNS records](https://docs.cloud.google.com/vpc/docs/configure-private-service-connect-apis#configure-dns-default) for the `gke.goog` domain. With this configuration, GKE reroutes requests for `*.gke.goog` domain to the internal IP address of the Private Service Connect endpoint, not the default public Google IP address.

  * **Access to the DNS-based endpoint from on-premises clients** : the DNS-based endpoint is accessible by on-premises clients through Private Google Access. To configure Private Google Access, complete the steps in [Configure Private Google Access for on-premises hosts](https://docs.cloud.google.com/vpc/docs/configure-private-google-access-hybrid).



#### Define the IP addresses that can access the control plane

To define the IP addresses that can access the control plane, complete the following steps:

### Console

  1. Under **Control Plane Access** , select **Enable authorized networks**.
  2. Click **Add authorized network**.
  3. Enter a **Name** for the network.
  4. For **Network** , enter a CIDR range that you want to grant access to your cluster control plane.
  5. Click **Done**.
  6. Add additional authorized networks if you need.



##### Define the control plane IP address firewall rules

To define the control plane IP address firewall rules, complete the following steps:

  1. Expand the **Show IP address firewall rules** section.
  2. Select the **Access using the control plane's external IP address** checkbox to allow access to the control plane from public IP addresses.

**Best practice** : 

Define **control plane authorized networks** to restrict access to the control plane.

  3. Select the **Access using the control plane's internal IP address from any region** checkbox. Internal IP addresses from any Google Cloud region can access the control plane internal endpoint.

  4. Select **Enforce authorized networks on the control plane's internal endpoint.** Only the IP addresses that you defined in the **Add authorized networks** list can access to the control plane internal endpoint. The internal endpoint is enabled by default.

  5. Select **Add Google Cloud external IP addresses to authorized networks**. All public IP addresses from Google Cloud can access the control plane.




### gcloud

You can configure the IP addresses that can access the control plane external and internal endpoints by using the following flags:

  * `enable-private-endpoint`: Specifies that access to the external endpoint is disabled. Omit this flag if you want to allow access to the control plane from external IP addresses. In this case, we strongly recommend that you control access to the external endpoint with the `enable-master-authorized-networks` flag.
  * `enable-master-authorized-networks:` Specifies that access to the external endpoint is restricted to IP address ranges that you authorize.
  * `master-authorized-networks`: Lists the CIDR values for the authorized networks. This list is comma-delimited list. For example, `8.8.8.8/32,8.8.8.0/24`.

**Best practice** : 

Use the `enable-master-authorized-networks` flag so that access to control plane is restricted.

  * `enable-authorized-networks-on-private-endpoint`: Specifies that access to the internal endpoint is restricted to IP address ranges that you authorize with the `enable-master-authorized-networks` flag.

  * `no-enable-google-cloud-access`: Denies access to the control plane from Google Cloud external IP addresses. Note that updating this setting does not take effect immediately. It might take several hours for GKE to propagate and enforce the firewall rule changes.

  * `enable-master-global-access`: Allows access from IP addresses in other Google Cloud regions.

You can continue to configure the cluster network by defining node or Pod isolation on a cluster level.




You can also create a cluster and define attributes at the cluster level, such as node network and subnet, IP stack type, and IP address allocation. To learn more, see [Create a VPC-native cluster](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/alias-ips#create_a_cluster_and_select_the_control_plane_ip_address_range).

### Modify the control plane access

To change control plane access for a cluster, use either the gcloud CLI or the Google Cloud console.

### Console

  1. Go to the **Google Kubernetes Engine** page in the Google Cloud console.

[Go to Google Kubernetes Engine](https://console.cloud.google.com/kubernetes/list)

  2. In the cluster list, click the cluster name.

  3. In the **Cluster details** tab, under **Control Plane Networking** , click _edit_.

  4. In the **Edit control plane networking** dialog, modify the control plane access based on your use case requirements.

  5. Verify your control plane configuration.




### gcloud

Run the following command and append the flags that meet your use case. You can use the following flags:

  * `enable-dns-access`: Enables access to the control plane by using the DNS-based endpoint of the control plane. If you specify this flag, you can also specify the following optional flags:

    * `enable-k8s-tokens-via-dns`: enable authentication to the DNS-based endpoint by using Kubernetes ServiceAccount bearer tokens.
    * `enable-k8s-certs-via-dns`: enable authentication to the DNS-based endpoint by using Kubernetes X.509 client certificates.
**Best practice** : 

ServiceAccount tokens and client certificates can add complexity and management overhead to your security configuration. Unless your use case requires one of these authentication methods, [use IAM credentials to authenticate to your control plane](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/api-server-authentication).

  * `enable-ip-access`: Enables access to the control plane by using IPv4 addresses. If you want to disable both the internal and external endpoints of the control plane, use the `no-enable-ip-access` flag instead.

  * `enable-private-endpoint`: Specifies that access to the external endpoint is disabled. Omit this flag if you want to allow access to the control plane from external IP addresses. In this case, we strongly recommend that you control access to the external endpoint with the `enable-master-authorized-networks` flag.

  * `enable-master-authorized-networks:` Specifies that access to the external endpoint is restricted to IP address ranges that you authorize.

  * `master-authorized-networks`: Lists the CIDR values for the authorized networks. This list is comma-delimited list. For example, `8.8.8.8/32,8.8.8.0/24`.

**Best practice** : 

Use the `enable-master-authorized-networks` flag so that access to control plane is restricted.

  * `enable-authorized-networks-on-private-endpoint`: Specifies that access to the internal endpoint is restricted to IP address ranges that you authorize with the `enable-master-authorized-networks` flag.

  * `no-enable-google-cloud-access`: Denies access to the control plane from Google Cloud external IP addresses. Note that updating this setting does not take effect immediately. It might take several hours for GKE to propagate and enforce the firewall rule changes.

  * `enable-master-global-access`: Allows access from IP addresses in other Google Cloud regions.
        
        gcloud container clusters update CLUSTER_NAME
        

Replace `CLUSTER_NAME` with the name of the cluster.




### Verify your control plane configuration

You can view your cluster's endpoints using the gcloud CLI or the Google Cloud console.

### Console

  1. Go to the **Google Kubernetes Engine** page in the Google Cloud console.

[Go to Google Kubernetes Engine](https://console.cloud.google.com/kubernetes/list)

  2. In the cluster list, click the cluster name.

  3. In the **Cluster details** tab, under **Control plane** , you can check the following characteristics of the control plane endpoints:

     * **DNS endpoint** includes the name of the DNS-based endpoint of your cluster, if you've enabled this endpoint.
     * **Control plane access using IPv4 addresses** includes the status of the IP-based endpoint. If enabled, you can see the information of the public and private endpoints.
     * **Access using control plane's internal IP address from any region** shows the status as **Enabled** when the control plane can be accessed by Google IP addresses from other regions.
     * **Authorized networks** shows the list of CIDRs that can access the control plane, if you've enabled authorized networks.
     * **Enforce authorized networks on control plane's internal endpoint** shows the **Enabled** status if only the CIDRs in the **Authorized networks** field can access the internal endpoint.
     * **Add Google Cloud external IP addresses to authorized networks** shows the **Enabled** status if the external IP addresses from Google Cloud can access the control plane.



To modify any attribute, click the _edit_ **Control plane access using IPv4 addresses** and adjust based on your use case.

### gcloud

To verify the control plane configuration, run the following command:
    
    
    gcloud container clusters describe CLUSTER_NAME
    

The output has an `controlPlaneEndpointsConfig` block that describes the network definition. You can see an output similar to the following:
    
    
    controlPlaneEndpointsConfig:
    dnsEndpointConfig:
      allowExternalTraffic: true
      endpoint: gke-dc6d549babec45f49a431dc9ca926da159ca-518563762004.us-central1-c.autopush.gke.goog
    ipEndpointsConfig:
      authorizedNetworksConfig:
        cidrBlocks:
        - cidrBlock: 8.8.8.8/32
        - cidrBlock: 8.8.8.0/24
        enabled: true
        gcpPublicCidrsAccessEnabled: false
        privateEndpointEnforcementEnabled: true
      enablePublicEndpoint: false
      enabled: true
      globalAccess: true
      privateEndpoint: 10.128.0.13
    

In this example, the cluster has the following configuration:

  * Both DNS and IP-address based endpoints are enabled.
  * Authorized networks are enabled and the CIDR ranges are defined. These authorized networks are enforced for the internal IP address.
  * Access to the control plane from Google Cloud external IP addresses is denied.



#### Examples of control plane access configuration

This section details the configuration of the following network isolation examples. Evaluate these examples for similarity to your use case:

  * **Example 1** : The control plane is accessible from _certain_ IP addresses that you define. These might include IP addresses from other Google Cloud regions or Google-reserved IP addresses.
  * **Example 2** : The control plane is not accessible by any external IP address.



##### Example 1: The control plane is accessible from certain IP addresses

In this section, you create a cluster with the following network isolation configurations:

  * The control plane has the DNS-based endpoint enabled.
  * The control plane has the external endpoint enabled in addition to the internal endpoint enabled by default.
  * The control plane has authorized networks defined, allowing only the following authorized networks to reach the control plane: 
    * A range of external IP addresses that you define.
    * All the internal IP addresses in your cluster.
    * [Google Cloud external IP addresses](https://docs.cloud.google.com/compute/docs/faq#find_ip_range).



To create this cluster, use either the Google Cloud CLI or the Google Cloud console.

### Console

  1. Go to the **Google Kubernetes Engine** page in the Google Cloud console.

[Go to Google Kubernetes Engine](https://console.cloud.google.com/kubernetes/list)

  2. Click _add_box_ **Create**.

  3. Configure your cluster to suit your requirements.

  4. In the navigation menu, click **Networking**.

  5. Under **Control Plane Access** , configure the control plane endpoints:

     1. Select the **Access using DNS** checkbox.
     2. Select the **Access using IPV4 addresses** checkbox.
  6. Select **Enable authorized networks**.

  7. Click **Add authorized network**.

  8. Enter a **Name** for the network.

  9. For **Network** , enter a CIDR range that you want to grant access to your cluster control plane.

  10. Click **Done**.

  11. Add additional authorized networks if you need.

  12. Expand the **Show IP address firewall rules** section.

  13. Select **Access using the control plane's internal IP address from any region**. Internal IP addresses from any Google Cloud region can access the control plane over the internal IP address.

  14. Select **Add Google Cloud external IP addresses to authorized networks.** All external IP addresses from Google Cloud can access the control plane.




You can continue configuring the cluster network by defining node or Pod isolation on a cluster level.

### gcloud

Run the following command:
    
    
    gcloud container clusters create-auto CLUSTER_NAME \
        --enable-dns-access \
        --enable-ip-access \
        --enable-master-authorized-networks \
        --enable-master-global-access \
        --master-authorized-networks CIDR1,CIDR2,...
    

Replace the following:

  * `CLUSTER_NAME`: the name of the GKE cluster.
  * `CIDR1,CIDR2,...`: A comma-delimited list of CIDR values for the authorized networks. For example, `8.8.8.8/32,8.8.8.0/24`.



##### Example 2: The control plane is accessible from internal IP addresses

In this section, you create a cluster with the following network isolation configurations:

  * The control plane has the DNS-based endpoint enabled.
  * The control plane has the external endpoint disabled.
  * The control plane has authorized networks enabled.
  * All access to the control plane over the internal IP address from any Google Cloud region is allowed.
  * [Google Cloud external IP addresses](https://docs.cloud.google.com/compute/docs/faq#find_ip_range) don't have access to your cluster.



You can create this cluster by using the Google Cloud CLI or the Google Cloud console.

### Console

  1. Go to the **Google Kubernetes Engine** page in the Google Cloud console.

[Go to Google Kubernetes Engine](https://console.cloud.google.com/kubernetes/list)

  2. Click _add_box_ **Create**.

  3. Configure your cluster to suit your requirements.

  4. In the navigation menu, click **Networking**.

  5. Under **Control Plane Access** , configure the control plane endpoints:

     1. Select the **Access using DNS** checkbox.
     2. Select the **Access using IPV4 addresses** checkbox.
  6. Expand the **Show IP address firewall rules** section.

  7. Unselect **Access using the control plane's external IP address.** The control plane is not accessible by any external IP address.

  8. Under **Control Plane Access** , select **Enable authorized networks**.

  9. Select the **Access using the control plane's internal IP address from any region** checkbox. Internal IP addresses from any Google Cloud region can access the control plane over the internal IP address.




You can continue the cluster network configuration by defining node or Pod isolation on a cluster level.

### gcloud

Run the following command:
    
    
    gcloud container clusters create-auto CLUSTER_NAME \
        --enable-dns-access \
        --enable-ip-access \
        --enable-private-endpoint \
        --enable-master-authorized-networks \
        --master-authorized-networks CIDR1,CIDR2,... \
        --no-enable-google-cloud-access \
        --enable-master-global-access
    

Replace the following:

  * `CLUSTER_NAME`: the name of the cluster..
  * `CIDR1,CIDR2,...`: A comma-delimited list of CIDR values for the authorized networks. For example, `8.8.8.8/32,8.8.8.0/24`.



## Configure cluster networking

In this section, you configure your cluster to have nodes with internal (private) or external (public) access. GKE lets you combine the node network configuration depending on the type of cluster that you use:

  * **Standard cluster** : You can create or update your node pools to provision private or public nodes in the same cluster. For example, if you create a node pool with private nodes, then GKE provisions its nodes with only internal IP addresses. GKE doesn't modify existing node pools. You can also define the default networking configuration at a cluster level. GKE applies this default network configuration only when new node pools don't have any network configuration defined.
  * **Autopilot clusters** : You can create or update your cluster to define the default network configuration for all your workloads. GKE schedules new and existing workloads on public or private nodes based on your configuration. You can also explicitly define the cluster network configuration of an individual workload.



### Configure your cluster

In this section, configure the cluster networking at a cluster level. GKE considers this configuration when your node pool or workload doesn't have this configuration defined.

To define cluster-level configuration, use either the Google Cloud CLI or the Google Cloud console.

**Note:** If you use VPC-native clusters, you can [create subnets with IPv4/IPv6 dual-stack networking](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/alias-ips#dual_stack_network). However, dual-stack networking subnets are not affected by the cluster networking configuration described in the following section. The configuration of cluster networking at a cluster level only affects the IPV4 address of the nodes in your cluster.

### Console

#### Create a cluster

  1. Go to the **Google Kubernetes Engine** page in the Google Cloud console.

[Go to Google Kubernetes Engine](https://console.cloud.google.com/kubernetes/list)

  2. Click _add_box_ **Create** , then in the Standard or Autopilot section, click **Configure**.

  3. Configure your cluster to suit your requirements.

  4. In the navigation menu, click **Networking**.

  5. In the **Cluster networking** section, complete the following based on your use case:

     1. Select **Enable private nodes** to provision nodes with only internal IP addresses (private nodes) which prevent external clients from accessing the nodes. You can change these settings at any time.
     2. Unselect **Enable private nodes** to provision nodes with only external IP addresses (public) which enables external clients to access the nodes.
  6. In the **Advanced networking options** section, configure additional VPC-native attributes. To learn more, see [Create a VPC-native cluster](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/alias-ips#console).

  7. Click **Create**.




#### Update an existing Cluster

  1. Go to the **Google Kubernetes Engine** page in the Google Cloud console.

[Go to Google Kubernetes Engine](https://console.cloud.google.com/kubernetes/list)

  2. In the cluster list, click the cluster name.

  3. In **Private Nodes** , under **Default New Node-Pool Configuration** tab, click _edit_ **Edit Private Nodes**.

  4. In the **Edit Private Nodes** dialog, do any of the following:

     1. Select **Enable private nodes** to provision nodes with only internal IP addresses (private nodes) which prevent external clients from accessing the nodes. You can change these settings at any time.
     2. Unselect **Enable private nodes** to provision nodes with only external IP addresses (public) which enables external clients to access the nodes.
  5. Click **Save changes**.




### gcloud

Use any of the following flags to define the cluster networking:

  * `enable-private-nodes`: To provision nodes with only internal IP addresses (private nodes). Consider the following conditions when using this flag: 
    * The `enable-ip-alias` flag is required when using `enable-private-nodes`.
    * The `master-ipv4-cidr` flag is optional to create private subnets. If you use this flag, GKE creates a new subnet that uses the values you defined in `master-ipv4-cidr` and uses the new subnet to provision the internal IP address for the control plane.
  * `no-enable-private-nodes`: To provision nodes with only external IP addresses (public nodes).



In Autopilot clusters, [create](https://docs.cloud.google.com/sdk/gcloud/reference/container/clusters/create-auto) or [update](https://docs.cloud.google.com/sdk/gcloud/reference/container/clusters/update) the cluster with the `enable-private-nodes` flag.

  * To create a cluster use the following command:
        
        gcloud container clusters create-auto CLUSTER_NAME \
            --enable-private-nodes \
            --enable-ip-alias
        

  * To update a cluster use the following command.
        
        gcloud container clusters update CLUSTER_NAME \
            --enable-private-nodes \
            --enable-ip-alias
        

The cluster update takes effect only after all the node pools have been re-scheduled. This process might take several hours.




In Standard clusters, [create](https://docs.cloud.google.com/sdk/gcloud/reference/container/clusters/create) or [update](https://docs.cloud.google.com/sdk/gcloud/reference/container/clusters/update) the cluster with the `enable-private-nodes` flag.

  * To create a cluster use the following command:
        
        gcloud container clusters create CLUSTER_NAME \
            --enable-private-nodes \
            --enable-ip-alias
        

  * To update a cluster use the following command:
        
        gcloud container clusters update CLUSTER_NAME \
            --enable-private-nodes \
            --enable-ip-alias
        

The cluster update takes effect only on new node pools. GKE doesn't update this configuration on existing node pools.




The cluster configuration is overwritten by the network configuration in the [node pool](https://docs.cloud.google.com/sdk/gcloud/reference/container/node-pools/create#--enable-private-nodes) or workload level.

### Configure your node pools or workloads

To configure private or public nodes at the workload level for Autopilot clusters, or node pools for Standard clusters use either the Google Cloud CLI or the Google Cloud console. If you don't define the network configuration at the workload or node pool level, GKE applies the default configuration at the cluster level.

### Console

In Standard clusters, complete the following steps:

  1. Go to the **Google Kubernetes Engine** page in the Google Cloud console.

[Go to Google Kubernetes Engine](https://console.cloud.google.com/kubernetes/list)

  2. On the **Cluster details** page, click the name of the cluster you want to modify.

  3. Click the **Nodes** tab.

  4. Click _add_box_ **Create user-managed node pool**.

  5. Configure the **Enable private nodes** checkbox based on your use case:

     1. Select **Enable private nodes** to provision nodes with only internal IP addresses (private nodes).
     2. Unselect **Enable private nodes** to provision nodes with only external IP addresses (public) which enables external clients to access the nodes. You can change this configuration at any time.
  6. Configure your new node pool.

  7. Click **Create**.




To learn more about node pool management, see [Add and manage node pools](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/node-pools).

### gcloud

  * In Autopilot clusters and in Standard node pools that use node auto-provisioning, add the following `nodeSelector` to your Pod specification:
        
        cloud.google.com/private-node=true
        

Use `private-node=true` to schedule a Pod on nodes that have only internal IP addresses (private nodes).

GKE recreates your Pods on private nodes or public nodes, based on your configuration. To avoid workload disruption, migrate each workload independently and monitor the migration.

  * In Standard clusters, to provision nodes through private IP addresses in an existing node pool, run the following command:
        
        gcloud container node-pools update NODE_POOL_NAME \
            --cluster=CLUSTER_NAME \
            --enable-private-nodes \
            --enable-ip-alias
        

Replace the following:

    * `NODE_POOL_NAME`: the name of the node pool that you want to edit.
    * `CLUSTER_NAME`: the name of your existing cluster.

Use any of the following flags to define the node pool networking configuration:

    * `enable-private-nodes`: To provision nodes with only internal IP addresses (private nodes).
    * `no-enable-private-nodes`: To provision nodes with only external IP addresses (public nodes).



## Advanced configurations

The following sections describe advanced configurations that you might want when configuring your cluster network isolation.

### Access a cluster without an external endpoint

If the external endpoint of your cluster's control plane is disabled, you can't access your GKE control plane with Cloud Shell. If you want to use [Cloud Shell](https://docs.cloud.google.com/shell/docs/deploy-gke-app) to access your cluster, we recommend that you enable the [DNS-based endpoint](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/latest/network-isolation#dns-based-endpoint).

To verify access to your cluster, complete the following steps:

  1. If you have enabled the DNS-based endpoint, run the following command to get credentials for your cluster:
         
         gcloud container clusters get-credentials CLUSTER_NAME \
             --dns-endpoint
         

If you have enabled the IP-based endpoint, run the following command to get credentials for your cluster:
         
         gcloud container clusters get-credentials CLUSTER_NAME \
             --project=PROJECT_ID \
             --internal-ip
         

Replace `PROJECT_ID` with your project ID.

  2. Use `kubectl` in Cloud Shell to access your cluster:
         
         kubectl get nodes
         

The output is similar to the following:
         
         NAME                                               STATUS   ROLES    AGE    VERSION
         gke-cluster-1-default-pool-7d914212-18jv   Ready    <none>   104m   v1.21.5-gke.1302
         gke-cluster-1-default-pool-7d914212-3d9p   Ready    <none>   104m   v1.21.5-gke.1302
         gke-cluster-1-default-pool-7d914212-wgqf   Ready    <none>   104m   v1.21.5-gke.1302
         




The `get-credentials` command automatically uses the DNS-based endpoint if the IP-based endpoint access is disabled.

### Add firewall rules for specific use cases

This section explains how to add a firewall rule to a cluster. By default, firewall rules restrict your cluster control plane to only initiate TCP connections to your nodes and Pods on ports `443` (HTTPS) and `10250` (kubelet). For some Kubernetes features, you might need to add firewall rules to allow access on additional ports. Don't create firewall rules or [hierarchical firewall policy rules](https://docs.cloud.google.com/vpc/docs/firewall-policies#hierarchical_firewall_policy_rule_details) that have a [higher priority](https://docs.cloud.google.com/vpc/docs/firewalls#priority_order_for_firewall_rules) than the [automatically created firewall rules](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/firewall-rules#cluster-fws).

**Note:** The allowed ports (`443` and `10250`) refer to the ports exposed by your nodes and Pods, _not_ the ports exposed by any Kubernetes services. For example, if the cluster control plane attempts to access a service on port `443`, but the service is _implemented_ by a pod using port `9443`, this will be blocked by the firewall unless you add a firewall rule to explicitly allow ingress to port `9443`.

Kubernetes features that require additional firewall rules include:

  * [Admission webhooks](https://kubernetes.io/docs/reference/access-authn-authz/extensible-admission-controllers/)
  * [Aggregated API servers](https://kubernetes.io/docs/concepts/extend-kubernetes/api-extension/apiserver-aggregation/)
  * [Webhook conversion](https://kubernetes.io/docs/tasks/extend-kubernetes/custom-resources/custom-resource-definition-versioning/#webhook-conversion)
  * [Dynamic audit configuration](https://kubernetes.io/docs/tasks/debug/debug-cluster/audit/#service-reference)
  * Generally, any API that has a ServiceReference field requires additional firewall rules.



Adding a firewall rule allows traffic from the cluster control plane to all of the following:

  * The specified port of each node (hostPort).
  * The specified port of each Pod running on these nodes.
  * The specified port of each Service running on these nodes.



To learn about firewall rules, refer to [Firewall rules](https://docs.cloud.google.com/load-balancing/docs/https#firewall_rules) in the Cloud Load Balancing documentation.

To add a firewall rule in a cluster, you need to record the cluster control plane's CIDR block and the target used. After you have recorded this you can create the rule.

#### View control plane's CIDR block

You need the cluster control plane's CIDR block to add a firewall rule.

### Console

  1. Go to the **Google Kubernetes Engine** page in the Google Cloud console.

[Go to Google Kubernetes Engine](https://console.cloud.google.com/kubernetes/list)

  2. In the cluster list, click the cluster name.




In the **Details** tab, under **Networking** , take note of the value in the **Control plane address range** field.

### gcloud

Run the following command:
    
    
    gcloud container clusters describe CLUSTER_NAME
    

Replace `CLUSTER_NAME` with the name of your cluster.

In the command output, take note of the value in the **masterIpv4CidrBlock** field.

#### View existing firewall rules

You need to specify the [_target_](https://docs.cloud.google.com/vpc/docs/firewalls#rule_assignment) (in this case, the destination nodes) that the cluster's existing firewall rules use.

### Console

  1. Go to the **Firewall policies** page in the Google Cloud console.

[Go to Firewall policies](https://console.cloud.google.com/net-security/firewall-manager/firewall-policies/list)

  2. For **Filter table** for **VPC firewall rules** , enter `gke-CLUSTER_NAME`.




In the results, take note of the value in the **Targets** field.

### gcloud

Run the following command:
    
    
    gcloud compute firewall-rules list \
        --filter 'name~^gke-CLUSTER_NAME' \
        --format 'table(
            name,
            network,
            direction,
            sourceRanges.list():label=SRC_RANGES,
            allowed[].map().firewall_rule().list():label=ALLOW,
            targetTags.list():label=TARGET_TAGS
        )'
    

In the command output, take note of the value in the **Targets** field.

To view firewall rules for a Shared VPC, add the `--project HOST_PROJECT_ID` flag to the command.

#### Add a firewall rule

### Console

  1. Go to the **Firewall policies** page in the Google Cloud console.

[Go to Firewall policies](https://console.cloud.google.com/net-security/firewall-manager/firewall-policies/list)

  2. Click _add_box_ **Create Firewall Rule**.

  3. For **Name** , enter the name for the firewall rule.

  4. In the **Network** list, select the relevant network.

  5. In **Direction of traffic** , click **Ingress**.

  6. In **Action on match** , click **Allow**.

  7. In the **Targets** list, select **Specified target tags**.

  8. For **Target tags** , enter the target value that you noted previously.

  9. In the **Source filter** list, select **IPv4 ranges**.

  10. For **Source IPv4 ranges** , enter the cluster control plane's CIDR block.

  11. In **Protocols and ports** , click **Specified protocols and ports** , select the checkbox for the relevant protocol (**tcp** or **udp**), and enter the port number in the protocol field.

  12. Click **Create**.




### gcloud

Run the following command:
    
    
    gcloud compute firewall-rules create FIREWALL_RULE_NAME \
        --action ALLOW \
        --direction INGRESS \
        --source-ranges CONTROL_PLANE_RANGE \
        --rules PROTOCOL:PORT \
        --target-tags TARGET
    

Replace the following:

  * `FIREWALL_RULE_NAME`: the name you choose for the firewall rule.
  * `CONTROL_PLANE_RANGE`: the cluster control plane's IP address range (`masterIpv4CidrBlock`) that you collected previously.
  * `PROTOCOL:PORT`: the port and its protocol, `tcp` or `udp`.
  * `TARGET`: the target (`Targets`) value that you collected previously.



To add a firewall rule for a Shared VPC, add the following flags to the command:
    
    
    --project HOST_PROJECT_ID
    --network NETWORK_ID
    

### Granting private nodes outbound internet access

To provide outbound internet access for your private nodes, such as to pull images from an external registry, use [Cloud NAT](https://docs.cloud.google.com/nat/docs/overview) to create and configure a Cloud Router. Cloud NAT lets private nodes establish outbound connections over the internet to send and receive packets.

The Cloud Router allows all your nodes in the region to use Cloud NAT for all primary and [alias IP ranges](https://docs.cloud.google.com/vpc/docs/alias-ip). It also automatically allocates the external IP addresses for the NAT gateway.

For instructions to create and configure a Cloud Router, refer to [Create a Cloud NAT configuration using Cloud Router](https://docs.cloud.google.com/nat/docs/gke-example#create-nat) in the Cloud NAT documentation.

**Note:** To provide outbound internet access for your Pods and Services, configure Cloud NAT to [Specify subnet ranges for NAT](https://docs.cloud.google.com/nat/docs/set-up-manage-network-address-translation#specify_subnet_ranges_for_nat)

### Deploying a Windows Server container application

To learn how to deploy a Windows Server container application to a cluster with private nodes, refer to the [Windows node pool documentation](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/deploying-windows-app#deploying_a_windows_server_application_to_a_private_cluster).

## What's next

  * Learn more about [network isolation in GKE](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/network-isolation).
  * Learn how to [create a VPC-native cluster](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/alias-ips).
  * Learn more about [Private Service Connect](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/private-service-connect).
  * Learn how to [install kubectl and configure cluster access](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/cluster-access-for-kubectl).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
