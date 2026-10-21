---
url: https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.15/how-to/create-user-cluster-api/
title: Create a user cluster using GKE On-Prem API clients \u00a0|\u00a0 Google Distributed Cloud Virtual for VMware \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T17:11:52.902225+00:00
---

# Create a user cluster using GKE On-Prem API clients  |  Google Distributed Cloud Virtual for VMware  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.15/how-to/create-user-cluster-api/

**Version 1.15**. This version is no longer supported. For more information see the [ version support policy](https://cloud.google.com/anthos/clusters/docs/on-prem/latest/getting-support#version_support_policy). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Google Distributed Cloud ](https://docs.cloud.google.com/distributed-cloud)
  * [ Documentation ](https://docs.cloud.google.com/kubernetes-engine/enterprise/clusters/docs)
  * [ GDCV for VMware 1.15 ](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.15)
  * [ Guides ](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.15/overview)



Send feedback 

#  Create a user cluster using GKE On-Prem API clients Stay organized with collections  Save and categorize content based on your preferences. 

Version 1.15 keyboard_arrow_down

  * [ Latest version ](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/latest/how-to/create-user-cluster-api)
  * [ Version 1.16 ](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.16/how-to/create-user-cluster-api)
  * [ Earlier versions (unsupported) ](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/latest/version-history#expandable-1)



This page describes how to create a user cluster by using the Google Cloud console, the Google Cloud CLI (gcloud CLI), or Terraform.

## What is the GKE On-Prem API?

The GKE On-Prem API is a Google Cloud-hosted API that lets you manage the lifecycle of your on-premises clusters using Terraform and standard Google Cloud applications. The GKE On-Prem API runs in Google Cloud's infrastructure. Terraform, the console, and the gcloud CLI are clients of the API, and they use the API to create clusters in your data center.

To manage the lifecycle of your clusters, the GKE On-Prem API must store metadata about your cluster's state in Google Cloud, using the Google Cloud region that you specify when creating the cluster. This metadata lets the API manage the cluster lifecycle and doesn't include workload-specific data.

When you create a cluster using an GKE On-Prem API client, you specify a Google Cloud project. After the cluster is created, it is automatically registered to the specified project's [fleet](https://docs.cloud.google.com/anthos/fleet-management/docs). This project is referred to as the [fleet host project](https://docs.cloud.google.com/anthos/fleet-management/docs/fleet-concepts#fleet-host-project). The fleet host project can't be changed after the cluster is created.

If you prefer, you can create a user cluster by creating a user cluster configuration file and using `gkectl`, as described in [Creating a user cluster using gkectl](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.15/how-to/create-user-cluster).

If you want to use Terraform, the console or gcloud CLI to manage the lifecycle of clusters that were created using `gkectl`, see [Configure a user cluster to be managed by the GKE On-Prem API](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.15/how-to/enroll-user-cluster).

## Before you begin

This section describes the requirements for creating a user cluster using GKE On-Prem API clients.

### Grant IAM permissions

If you aren't a project owner, you must be granted [roles/gkeonprem.admin](https://docs.cloud.google.com/iam/docs/roles-permissions/gkeonprem).

If you want to access the GKE Enterprise and Google Kubernetes Engine pages in the console, you must also have the following roles:

  * [roles/container.viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/container).
  * [roles/gkehub.viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/gkehub#gkehub.viewer)



After the cluster is created, if your aren't a project owner and you want to use the Connect gateway to connect to the user cluster by the command line, the following roles are required:

  * [roles/gkehub.gatewayAdmin](https://docs.cloud.google.com/iam/docs/roles-permissions/gkehub#gkehub.gatewayAdmin): This role lets you access the Connect gateway API. If you only need read-only access to the cluster, the `roles/gkehub.gatewayReader` is sufficient.

  * [roles/gkehub.viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/gkehub#gkehub.viewer): This role lets you retrieve cluster credentials.




For information on granting the roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access)

### Register the admin cluster

You must have an admin cluster and it must be registered to a [fleet](https://docs.cloud.google.com/anthos/multicluster-management) before you can create user clusters using GKE On-Prem API clients.

  * If you haven't created an admin cluster yet, fill in the [`gkeConnect` section](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.15/how-to/admin-cluster-configuration-file#gkeconnect-section) in your admin cluster configuration file.

  * If you have an admin cluster, but you haven't registered it, see [Register an admin cluster](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.15/how-to/updating-general#register_an_admin_cluster).




### Enable Admin Activity audit logs for the admin cluster

Admin activity logging to [Cloud Audit Logs](https://docs.cloud.google.com/logging/docs/audit) must be enabled on the admin cluster.

  * If you haven't created an admin cluster yet, fill in the [`cloudAuditLogging`](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.15/how-to/admin-cluster-configuration-file#cloudauditlogging-section) section in your admin cluster configuration file.

  * To update an existing admin cluster, see [Enable or disable logging to Cloud Audit Logs for the admin cluster](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.15/how-to/updating-general#enable_or_disable_logging_to_cloud_audit_log_for_the_admin_cluster).




### Enable system-level logging and monitoring for the admin cluster

[Cloud Logging](https://docs.cloud.google.com/logging/docs) and [Cloud Monitoring](https://docs.cloud.google.com/monitoring/docs) must be enabled on the admin cluster.

  * If you haven't created an admin cluster yet, fill in the [`stackdriver`](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.15/how-to/admin-cluster-configuration-file#stackdriver-section) section in your admin cluster configuration file.

  * To update an existing admin cluster, see [Enable or disable logging and monitoring for the admin cluster](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.15/how-to/updating-general#enable_or_disable_logging_and_monitoring_for_the_admin_cluster).




### Required Google APIs

Make sure that all the [required Google APIs](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.15/how-to/multiple-gcp-projects#enabling_apis_in_your_fleet_host_project) are enabled in the fleet host project.

In addition, you need to enable the GKE On-Prem API:
    
    
    gcloud services enable --project FLEET_HOST_PROJECT_ID \
        gkeonprem.googleapis.com
    

### Command line access

After the cluster is created, if you want to use the [Connect gateway](https://docs.cloud.google.com/anthos/multicluster-management/gateway) to connect to the user cluster by the command line, do the following:

Ensure that you have the following command-line tools installed:

  * The latest version of the [gcloud CLI](https://docs.cloud.google.com/sdk/docs/install).
  * `kubectl` for running commands against Kubernetes clusters. If you need to install `kubectl`, follow these [instructions](https://docs.cloud.google.com/anthos/fleet-management/docs/before-you-begin#install-kubectl).



If you are using Cloud Shell as your shell environment for interacting with Google Cloud, these tools are installed for you.

### Available versions for new installations

When you create a user cluster, you typically install the Google Distributed Cloud version that matches the admin cluster. But you can install a later patch version or one later minor version. For example, you might want to install the latest patch release when you create a user cluster to pick up bug fixes. It takes about 7 to 10 days after a Google Distributed Cloud release for the version to be available in the GKE On-Prem API.

If you want to create a user cluster that is a later version than the admin cluster, first download a version-specific bundle of the components that the admin cluster needs to manage user clusters at that version, and then deploy the components. For more information, see Install a later version than the admin cluster version.

### Choose a tool to create the cluster

You can use Terraform, the Google Cloud console, or the Google Cloud CLI (gcloud CLI) to create a cluster that is managed by the GKE On-Prem API. If this is your first time installing Google Distributed Cloud, you might find the console the easiest tool to use.

After you are more familiar with the information that you need to provide to create clusters, you might find Terraform or the gcloud CLI more convenient, particularly if you will be creating more than one cluster. [Terraform](https://developer.hashicorp.com/terraform/intro) is an industry-standard infrastructure as code tool. If your organization already uses Terraform, then you will likely want to use it for creating clusters and managing the cluster lifecycle.

With the gcloud CLI, you can save the command with its arguments to a text file and make changes as needed to create additional clusters. If you are using a CI/CD tool, such as [Cloud Build](https://docs.cloud.google.com/build/docs/overview), you can use the `gcloud` commands to create a cluster and node pool and specify the `--impersonate-service-account` flag to automate the creation.

## Create a user cluster

### Console

Most of the fields in the Google Cloud console correspond to the fields in the [user cluster configuration file](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.15/how-to/user-cluster-configuration-file).

  1. In the Google Cloud console, go to the **Create a Google Distributed Cloud cluster** page.

[Go to Create a Google Distributed Cloud cluster](https://console.cloud.google.com/kubernetes/vmware/add)

  2. Select the Google Cloud project that you want to create the cluster in. The selected project is also used as the fleet host project. This must be the same project that the admin cluster is registered to. After the user cluster is created, it is automatically registered to the selected project's fleet.




The following sections guide you through configuring the user cluster.

### Cluster basics

Enter basic information about the cluster.

  1. Enter a **Name** for the user cluster.
  2. Under **Admin cluster** , select the admin cluster from the list. If you didn't specify a name for the admin cluster when you created it, the name is generated in the form `gke-admin-[HASH]`. If you don't recognize the admin cluster name, run the following command on your admin workstation:
         
         KUBECONFIG=ADMIN_CLUSTER_KUBECONFIG
         kubectl get OnPremAdminCluster -n kube-system -o=jsonpath='{.items[0].metadata.name}'
         

If the admin cluster that you want to use isn't displayed, see the troubleshooting section [The admin cluster isn't displayed on the **Cluster basics** drop-down list](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.15/troubleshoot-user-cluster-create-api).

  3. In the **GCP API Location** field, select the Google Cloud region from the list. This setting specifies the region where the GKE On-Prem API runs, and the region in which the following are stored:

     * The user cluster metadata that the GKE On-Prem API needs to manage the cluster lifecycle
     * The Cloud Logging and Cloud Monitoring data of system components
     * The Admin Audit log created by Cloud Audit Logs

The cluster name, project, and location together uniquely identify Google Cloud.

  4. Select the Google Distributed Cloud version for your user cluster.

  5. As the cluster creator, you are granted cluster admin privileges to the cluster. Optionally, enter the email address of another user who will administer the cluster in the **Cluster admin user** field in the **Authorization** section.

When the cluster is created, the GKE On-Prem API applies the Kubernetes role-based access control (RBAC) policies to the cluster to grant you and other admin users the Kubernetes `clusterrole/cluster-admin` role, which provides full access to every resource in the cluster in all namespaces.

**Note:** In addition to the Kubernetes RBAC policies, you must grant some Identity and Access Management (IAM) roles to the users who aren't project owners. For details on granting the IAM roles, see [Grant required roles](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.15/how-to/connect-to-cluster-console#grant_required_roles).
  6. Click **Next** to go to the **Control plane** section.




### Control Plane

All the fields in the **Control plane** section are set with default values. Review the defaults and optionally, change them as needed.

  1. In the **Control-plane node vCPUs** field, enter the number of vCPUs (minimum 4) for each control plane node for your user cluster.
  2. In the **Control-plane node memory** field, enter the memory size in MiB (minimum 8192 and must be a multiple of 4) for each control plane for your user cluster.
  3. Under **Control-plane nodes** , select the number of control-plane nodes for your user cluster. For example, you may select 1 control-plane node for a development environment and 3 control-planes nodes for high availability (HA), production environments.
  4. Optionally, select **Automatic node resizing**. Resizing means that the vCPU and memory resources assigned to a node are adjusted automatically. When enabled, the control-plane nodes for the user cluster are resized according to the number of worker nodes in the user cluster. So as you add more worker nodes to the user cluster, the control-plane nodes are increased in size.
  5. Optionally, select **Enable control plane v2**. Enabling Controlplane V2 means the control plane for a user cluster runs on one or more nodes in the user cluster itself instead of in the admin cluster (referred to as the kubeception model).

When you select **Enable control plane v2** , the **Control plane node IPs** section displays. Enter the IP address for the gateway, the subnet mask, and the IP addresses for the control-plane nodes.

When Controlplane V2 is enabled, the vCPU and memory fields apply to the control plane nodes in the user cluster. The number of nodes is determined by the number of IP address that you enter. When Controlplane V2 isn't enabled, the vCPU, memory, and number of control-plane nodes fields apply to the nodes in the admin cluster. Make sure you set aside [enough IP addresses for your admin cluster](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.15/how-to/manage-node-ip-addresses#how_many_ip_addresses_does_an_admin_cluster_need).

  6. Click **Next** to go to the **Networking** section.




### Networking

In this section, you specify the IP addresses for your cluster's nodes, Pods, and Services. A user cluster needs to have one IP address for each node and an additional IP address for a temporary node that is needed during cluster upgrades, updates, and auto repair. For more information, see [How many IP addresses does a user cluster need?](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.15/how-to/manage-node-ip-addresses#how_many_ip_addresses_does_a_user_cluster_need).

  1. In the **Node IPs** section, select the **IP mode** for the user cluster. Select one of the following:

     * **DHCP** : Choose **DHCP** if you want your cluster nodes to get their IP address from a DHCP server.

     * **Static** : Choose **Static** if you want to provide static IP addresses for your cluster nodes, or if you want to set up manual load-balancing.

  2. If you selected **DHCP** skip to the next step to specify **Service and Pod CIDRs**. For **Static IP mode** , provide the following information:

     1. Enter the IP address of the **Gateway** for the user cluster.
     2. Enter the **Subnet mask** for the user cluster nodes.

     3. In the **IP Addresses** section, enter the IP addresses and optionally, the hostnames for the nodes in the user cluster. You can enter either an individual IP v4 address (such as 192.0.2.1) or a [CIDR](https://en.wikipedia.org/wiki/Classless_Inter-Domain_Routing) block of IPv4 addresses (such as 192.0.2.0/24).

        * If you enter a CIDR block, don't enter a hostname.
        * If you enter an individual IP address, you can optionally enter a hostname. If you don't enter a hostname, Google Distributed Cloud uses the VM's name from vSphere as the hostname.
     4. Click **\+ Add IP Address** as needed to enter more IP addresses.

  3. In the **Service and Pod CIDRs** section, the console provides the following address ranges for your Kubernetes Services and Pods:

     * **Service CIDR** : 10.96.0.0/20
     * **Pod CIDR** : 192.168.0.0/16

If you prefer to enter your own address ranges, see [IP addresses for Pods and Services](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.15/how-to/minimal-infrastructure#ip-addresses-pods-services) for best practices.

  4. If you selected **Static IP mode** or **Enable control plane v2** , specify the following information in the **Host config** section:

     1. Enter the IP addresses of the DNS servers.
     2. Enter the IP addresses of the NTP servers.
     3. Optionally, enter DNS search domains.
  5. Click **Next** to go to the **Load balancer** section.




### Load balancer

Choose the load balancer to set up for your cluster. See [Load balancer overview](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.15/how-to/setup-load-balance) for more information.

Select the **Load balancer type** from the list.

### Bundled with MetalLB

Configure bundled load balancing with MetalLB. You can use MetalLB for the user cluster only if your admin cluster is using SeeSaw or MetalLB. This option requires minimal configuration. MetalLB runs directly on your cluster nodes and doesn't require extra VMs. For more information about the benefits of using MetalLB and how it compares to the other load balancing options, see [Bundled load balancing with MetalLB](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.15/how-to/bundled-load-balance-metallb).

  1. In the **Address pools** section, configure at least one address pool, as follows:

     1. Enter a name for the address pool.

     2. Enter an IP address range that contains the ingress VIP in either CIDR notation (ex. 192.0.2.0/26) or range notation (ex. 192.0.2.64-192.0.2.72). To specify a single IP address in a pool, use /32 in the CIDR notation (ex. 192.0.2.1/32).

     3. If the IP addresses for your Services of type `LoadBalancer` aren't in the same IP address range as the ingress VIP, click **\+ Add IP Address Range** and enter another address range.

The IP addresses in each pool cannot overlap, and must be in the same subnet as the cluster nodes.

     4. Under **Assignment of IP addresses** , select one of the following:

        * **Automatic** : Choose this option if you want the MetalLB controller to automatically assign IP addresses from the address pool to Services of type `LoadBalancer`
        * **Manual** : Choose this option if you intend to use addresses from the pool to manually specify addresses for Services of type `LoadBalancer`
     5. Click **Avoid buggy IP addresses** if you want the MetalLB controller to not use addresses from the pool that end in .0 or .255. This avoids the problem of buggy consumer devices mistakenly dropping traffic sent to those special IP addresses.

     6. When you're finished click **Done**.

  2. If needed, click **Add Address Pool**.

  3. In the **Virtual IPs** section, enter the following:

     * **Control plane VIP** : The destination IP address to be used for traffic sent to the [Kubernetes API server](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.15/how-to/user-cluster-configuration-file#loadbalancer-vips-controlplanevip-field) of the user cluster. The Kubernetes API server for the user cluster runs on a node in the admin cluster. This IP address must be in the same L2 domain as the admin cluster nodes. Don't add this address in the **Address pools** section.

     * **Ingress VIP** : The IP address to be configured on the load balancer for the ingress proxy. You must add this to an address pool in the **Address pools** section.

  4. Click **Continue**.




### F5 Big-IP load balancer

You can use F5 for the user cluster only if your admin cluster is using F5. Be sure to install and configure the F5 BIG-IP ADC before integrating it with Google Distributed Cloud.

  1. In the **Virtual IPs** section, enter the following:

     * **Control plane VIP** : The destination IP address to be used for traffic sent to the [Kubernetes API server](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.15/how-to/user-cluster-configuration-file#loadbalancer-vips-controlplanevip-field).

     * **Ingress VIP** : The IP address to be configured on the load balancer for the ingress proxy.

  2. In the **Address** field, enter the address of your F5 BIG-IP load balancer.

  3. In the **Partition** field, enter the name of a BIG-IP partition that you created for your user cluster.

  4. In the **sNAT pool name** field, enter the name of your SNAT pool, if applicable.

  5. Click **Continue**.




### Manual load balancer

Configure manual load balancing. You can use a manual load balancer for the user cluster only if your admin cluster uses a manual load balancer. In Google Distributed Cloud, the Kubernetes API server, ingress proxy, and the add-on service for log aggregation are each exposed by a Kubernetes Service of type `LoadBalancer`. Choose your own `nodePort` values in the 30000 - 32767 range for these Services. For the ingress proxy, choose a `nodePort` value for both HTTP and HTTPS traffic. See [Enabling manual load balancing mode](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.15/how-to/manual-load-balance) for more information.

  1. In the **Virtual IPs** section, enter the following:

     * **Control plane VIP** : The destination IP address to be used for traffic sent to the [Kubernetes API server](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.15/how-to/user-cluster-configuration-file#loadbalancer-vips-controlplanevip-field).

     * **Ingress VIP** : The IP address to be configured on the load balancer for the ingress proxy.

  2. In the **Control-plan node port** field, enter a `nodePort` value for the Kubernetes API server. The Kubernetes API server of a user cluster runs on the admin cluster.

  3. In the **Ingress HTTP node port** field, enter a `nodePort` value for HTTP traffic to the ingress proxy.

  4. In the **Ingress HTTPS node port** field, enter a `nodePort` value for HTTPS traffic to the ingress proxy.

  5. In the **Konnectivity server node port** field, enter a `nodePort` value for the Konnectivity server.

  6. Click **Continue**.




### Features

This section displays the features and operations that are enabled on the cluster.

The following are enabled automatically and can't be disabled:

  * Cloud Logging of system services 
  * Cloud Monitoring of system services 
  * The [Admin Activity audit log](https://docs.cloud.google.com/logging/docs/audit#admin-activity)


  1. The following are enabled by default, but you can disable them:

     * **Enable vSphere CSI driver** : Also called the vSphere Container Storage Plug-in. The Container Storage Interface (CSI) driver runs in a native Kubernetes cluster deployed in vSphere to provision persistent volumes on vSphere storage. For more information, see [Using the vSphere Container Storage Interface driver](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.15/how-to/using-vsphere-csi-driver).
     * **Enable anti-affinity groups** : VMware Distributed Resource Scheduler (DRS) anti-affinity rules are automatically created for your user cluster's nodes, causing them to be spread across at least 3 physical hosts in your data center. Make sure that your vSphere environment meets the [requirements](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.15/how-to/user-cluster-configuration-file#antiaffinitygroups-enabled-field).
**Note:** If you followed [Set up minimal infrastructure](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.15/how-to/minimal-infrastructure), you only have one ESXi host, so be sure to clear **Enable anti-affinity groups**.
  2. Click **Next** to configure a node pool




### Node pools

Your cluster will be created with at least one node pool. A node pool is a template for the groups of nodes created in this cluster. For more information, see [Creating and managing node pools ](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.15/how-to/managing-node-pools).

  1. In the **Node pool defaults** section, complete the following:

     1. Enter the **Node pool name** or accept "default-pool" as the name.
     2. Enter the number of **vCPUs** for each node in the pool (minimum 4 per user cluster worker).
     3. Enter the **memory** size in mebibytes (MiB) for each node in the pool (minimum 8192 MiB per user cluster worker node and must be a multiple of 4).
     4. In the **Nodes** field, enter the number of nodes in the pool (minimum of 3). If you entered static IP addresses for the **Node IPs** in the **Networking** section, make sure that you entered enough IP addresses to accommodate these user cluster nodes.
     5. Select the **OS image type** : **Ubuntu** , **Ubuntu Containerd** , or **COS**.
     6. Enter the **Boot disk size** in gibibytes (GiB) (minimum 40 GiB).
     7. If you are using MetalLB as the load balancer, MetalLB must be enabled in at least one node pool. Either leave **Use this node pool for MetalLB load balancing** selected, or add another node pool to use for MetalLB.
  2. In the **Node pool metadata (optional)** section, if you want to add Kubernetes [labels](https://kubernetes.io/docs/concepts/overview/working-with-objects/labels/) and [taints](https://kubernetes.io/docs/concepts/scheduling-eviction/taint-and-toleration/), do the following:

     1. Click **\+ Add Kubernetes Labels**. Enter the **Key** and **Value** for the label. Repeat as needed.
     2. Click **\+ Add Taint**. Enter the **Key** , **Value** , and **Effect** for the taint. Repeat as needed.
  3. Click **Verify and Complete** to create the user cluster. It takes 15 minutes or more to create the user cluster. The console displays status messages as it verifies the settings and creates the cluster in your data center.

If an error is encountered verifying the settings, the console displays an error message that should be clear enough for you to fix the configuration issue and try again to create the cluster.

For more information about possible errors and how to fix them, see [Troubleshoot user cluster creation in the Google Cloud console](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.15/troubleshoot-user-cluster-create-api).




###  gcloud CLI 

You use the following command to create a user cluster:
    
    
    gcloud container vmware clusters create
    

After creating the cluster, you need to create at least one node pool using the following command:
    
    
    gcloud container vmware node-pools create
    

Most of the flags for creating the cluster and the node pool correspond to the fields in the [user cluster configuration file](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.15/how-to/user-cluster-configuration-file). To help you get started, you can test a complete command in the examples section.

### Before you begin

  1. Log in with your Google account.
         
         gcloud auth login
         

  2. Make sure to update components:
         
         gcloud components update
         

  3. Get a list of available versions:
         
         gcloud container vmware clusters query-version-config \
           --admin-cluster-membership=ADMIN_CLUSTER_NAME \
           --admin-cluster-membership-project=FLEET_HOST_PROJECT_ID \
           --location=REGION
         

Replace the following:

     * `ADMIN_CLUSTER_NAME`: The name of the admin cluster.

     * `FLEET_HOST_PROJECT_ID`: The ID of the project that the admin cluster is registered to.

     * `REGION`: The Google Cloud region that you specified when you enrolled the cluster in the GKE On-Prem API.

The output of the command is similar to the following:
    
    versions:
    - isInstalled: true
      version: 1.14.3-gke.25
    - version: 1.14.4-gke.54
    - version: 1.15.0-gke.581
    




Versions that you can use to create a user cluster are annotated with `isInstalled=true`, which means the admin cluster has the version-specific components it needs to manage user clusters of that version. If you want to create a user cluster with a another available version, see Install a later version than the admin cluster version.

### Examples

The following examples show how to create a user cluster with different load balancers. For information about the available load balancing options, see [Load balancer overview](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.15/how-to/setup-load-balance) for more information.

The examples use the default values for configuring the control plane nodes. If you want to change any of the defaults, include the flags described in the Control plane flags section. If needed, you can also change some vSphere settings.

After the cluster is running, you must add a node pool before deploying workloads, as described in the Create a node pool section.

### MetalLB & DHCP

This example shows how to create a user cluster with the bundled MetalLB load balancer and using your DHCP server to get IP addresses for your cluster nodes.

You can use MetalLB for the user cluster only if your admin cluster is using SeeSaw or MetalLB. This load balancing option requires minimal configuration. MetalLB runs directly on your cluster nodes and doesn't require extra VMs. For more information about the benefits of using MetalLB and how it compares to the other load balancing options, see [Bundled load balancing with MetalLB](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.15/how-to/bundled-load-balance-metallb).

Be sure to scroll over if needed to fill in the `ADMIN_CLUSTER_NAME` placeholder for the `--admin-cluster-membership` flag. This example uses the fully-specified admin cluster name, so you don't need to include `--admin-cluster-membership-location` and `--admin-cluster-membership-project`.
    
    
    gcloud container vmware clusters create USER_CLUSTER_NAME \
      --project=FLEET_HOST_PROJECT_ID \
      --admin-cluster-membership=projects/FLEET_HOST_PROJECT_ID/locations/global/memberships/ADMIN_CLUSTER_NAME \
      --location=REGION \
      --version=VERSION \
      --admin-users=YOUR_EMAIL_ADDRESS \
      --admin-users=ANOTHER_EMAIL_ADDRESS \
      --service-address-cidr-blocks=SERVICE_CIDR_BLOCK \
      --pod-address-cidr-blocks=POD_CIDR_BLOCK \
      --metal-lb-config-address-pools='pool=NAME,avoid-buggy-ips=True|False,manual-assign=True|False,addresses=IP_ADDRESS_RANGE_1;IP_ADDRESS_RANGE_2;...' \
      --control-plane-vip=CONTROL_PLANE_VIP \
      --ingress-vip=INGRESS_VIP \
      --enable-dhcp
    

  * `USER_CLUSTER_NAME`: A name of your choice for your user cluster. The name can't be changed after the cluster is created. The name must: 
    * contain at most 40 characters
    * contain only lowercase alphanumeric characters or a hyphen (`-`)
    * start with an alphabetic character
    * end with an alphanumeric character
  * `FLEET_HOST_PROJECT_ID`: The ID of the project that you want to create the cluster in. The specified project is also used as the fleet host project. This must be the same project that the admin cluster is registered to. After the user cluster is created, it is automatically registered to the selected project's fleet. The fleet host project can't be changed after the cluster is created. 
  * `ADMIN_CLUSTER_NAME`: The name of the admin cluster that manages the user cluster. In the `--admin-cluster-membership` flag, you can use the fully-specified cluster name, which has the following format: 
        
        projects/FLEET_HOST_PROJECT_ID/locations/ADMIN_CLUSTER_REGION/memberships/ADMIN_CLUSTER_NAME

Alternativly, you can set `--admin-cluster-membership` to the admin cluster's name, as in the example command. When you use only the admin cluster's name, set the admin cluster's project ID with the `--admin-cluster-membership-project` and location with `--admin-cluster-membership-location`. The admin cluster's location is either `global` or a Google Cloud region. If you need to find the region, run `gcloud container fleet memberships list`. 

  * `REGION`: The Google Cloud region in which the GKE On-Prem API (`gkeonprem.googleapis.com`), Fleet service (`gkehub.googleapis.com`), and the Connect service (`gkeconnect.googleapis.com`) run. Specify `us-west1` or another [supported region](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/reference/supported-regions-on-prem-api). The region can't be changed after the cluster is created. This setting specifies the region where the following are stored: 
    * The user cluster metadata that the GKE On-Prem API needs to manage the cluster lifecycle
    * The Cloud Logging and Cloud Monitoring data of system components
    * The Admin Audit log created by Cloud Audit Logs

The cluster name, project, and location together uniquely identify the cluster in Google Cloud.

**Important** If you plan to install Cloud Service Mesh, you must install version 1.19.3 or later. This is required because the Fleet and Connect services run in a region.
  * `VERSION`: The Google Distributed Cloud version for your user cluster. 
  * `YOUR_EMAIL_ADDRESS` and `ANOTHER_EMAIL_ADDRESS`: If you don't include the `--admin-users` flag, as the cluster creator, by default you are granted cluster admin privileges. But If you include `--admin-users` to designate another user as an administrator, you override the default and need to include both your email address and the email address of the other administrator. For example, to add two administrators: 
        
        --admin-users=sara@example.com \
            --admin-users=amal@example.com

When the cluster is created, the GKE On-Prem API applies the Kubernetes role-based access control (RBAC) policies to the cluster to grant you and other admin users the Kubernetes `clusterrole/cluster-admin` role, which provides full access to every resource in the cluster in all namespaces. 

**Note:** In addition to the Kubernetes RBAC policies, you must grant some Identity and Access Management (IAM) roles to the users who aren't project owners. For details on granting the IAM roles, see [Grant required roles](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/connect-to-cluster-console#grant_required_roles). 



  * `SERVICE_CIDR_BLOCK`: A range of IP addresses, in CIDR format, to be used for Services in your cluster. Must be at least a /24 range. 

Example: `--service-address-cidr-blocks=10.96.0.0/20`

  * `POD_CIDR_BLOCK`: A range of IP addresses, in CIDR format, to be used for Pods in your cluster. Must be at least a /18 range. 

Example: `--pod-address-cidr-blocks=192.168.0.0/16`



  * `--metal-lb-config-address-pools`: Include this flag to specify the configuration for address pools to be used by the MetalLB load balancer. The value for the flag has the following format: 
        
        --metal-lb-config-address-pool 'pool=NAME,avoid-buggy-ips=True|False,manual-assign=True|False,addresses=IP_ADDRESS_RANGE_1;IP_ADDRESS_RANGE_2;...' \

The value has segments that start with the keywords `pool`, `avoid-buggy-ip`, `manual-assign`, and `addresses`. Separate each segment with a comma. 

    * `pool`: A name of your choice for the pool. 
    * `avoid-buggy-ips`1: If you set this to `True`, the MetalLB controller will not assign IP addresses ending in .0 or .255 to Services. This avoids the problem of buggy consumer devices mistakenly dropping traffic sent to those special IP addresses. If not specified, defaults to `False`. 
    * `manual-assign`: If you do not want the MetalLB controller to automatically assign IP addresses from this pool to Services, set this to `True`. Then a developer can create a Service of type `LoadBalancer` and manually specify one of the addresses from the pool. If not specified, `manual-assign` is set to `False`. 
    * In the list of `addresses`: Each address must be a range either in [CIDR](https://tools.ietf.org/html/rfc4632) notation or hyphenated-range format. To specify a single IP address in a pool (such as for the ingress VIP), use /32 in CIDR notation, for example: `192.0.2.1/32`. 

Note the following:

    * Surround the entire value in single quotes.
    * Whitespace isn't allowed.
    * Separate each IP address range with a semicolon.

For example:
    
    --metal-lb-config-address-pool 'pool=pool1,avoid-buggy-ips=True,manual-assign=True,addresses=10.251.134.80/32;192.168.1.0/26;192.168.1.2-192.168.1.3'



  * `CONTROL_PLANE_VIP`: The IP address that you have chosen to configure on the load balancer for the Kubernetes API server of the user cluster. 

Example: `--control-plane-vip=203.0.113.3`

  * `INGRESS_VIP`: The IP address that you have chosen to configure on the load balancer for the ingress proxy. 

Example: `--ingress-vip=10.251.134.80`

The IP address for the ingress VIP must be in one of the MetalLB address pools. 



  * `--enable-dhcp`: Include `--enable-dhcp` if you want your cluster nodes to get their IP address from a DHCP server that you provide. Don't include this flag if you want to provide static IP addresses for your cluster nodes, or if you want to set up manual load balancing.



### MetalLB & Static IPs

This example shows how to create a user cluster with the bundled MetalLB load balancer and assigning static IP addresses to your cluster nodes.

You can use MetalLB for the user cluster only if your admin cluster is using SeeSaw or MetalLB. This load balancing option requires minimal configuration. MetalLB runs directly on your cluster nodes and doesn't require extra VMs. For more information about the benefits of using MetalLB and how it compares to the other load balancing options, see [Bundled load balancing with MetalLB](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.15/how-to/bundled-load-balance-metallb).

Be sure to scroll over if needed to fill in the `ADMIN_CLUSTER_NAME` placeholder for the `--admin-cluster-membership` flag. This example uses the fully-specified admin cluster name, so you don't need to include `--admin-cluster-membership-location` and `--admin-cluster-membership-project`.
    
    
    gcloud container vmware clusters create USER_CLUSTER_NAME \
      --project=FLEET_HOST_PROJECT_ID \
      --admin-cluster-membership=projects/FLEET_HOST_PROJECT_ID/locations/global/memberships/ADMIN_CLUSTER_NAME \
      --location=REGION \
      --version=VERSION \
      --admin-users=YOUR_EMAIL_ADDRESS \
      --admin-users=ANOTHER_EMAIL_ADDRESS \
      --service-address-cidr-blocks=SERVICE_CIDR_BLOCK \
      --pod-address-cidr-blocks=POD_CIDR_BLOCK \
      --metal-lb-config-address-pools='pool=NAME,avoid-buggy-ips=True|False,manual-assign=True|False,addresses=IP_ADDRESS_RANGE_1;IP_ADDRESS_RANGE_2;...' \
      --control-plane-vip=CONTROL_PLANE_VIP \
      --ingress-vip=INGRESS_VIP \
      --static-ip-config-ip-blocks='gateway=GATEWAY,netmask=NETMASK,ips=IP_ADDRESS_1;IP_ADDRESS_2 HOST_2;...' \
      --dns-servers=DNS_SERVER,... \
      --dns-search-domains=DNS_SEARCH_DOMAIN,... \
      --ntp-servers=NTP_SERVER,...
    

Replace the following:

  * `USER_CLUSTER_NAME`: A name of your choice for your user cluster. The name can't be changed after the cluster is created. The name must: 
    * contain at most 40 characters
    * contain only lowercase alphanumeric characters or a hyphen (`-`)
    * start with an alphabetic character
    * end with an alphanumeric character
  * `FLEET_HOST_PROJECT_ID`: The ID of the project that you want to create the cluster in. The specified project is also used as the fleet host project. This must be the same project that the admin cluster is registered to. After the user cluster is created, it is automatically registered to the selected project's fleet. The fleet host project can't be changed after the cluster is created. 
  * `ADMIN_CLUSTER_NAME`: The name of the admin cluster that manages the user cluster. In the `--admin-cluster-membership` flag, you can use the fully-specified cluster name, which has the following format: 
        
        projects/FLEET_HOST_PROJECT_ID/locations/ADMIN_CLUSTER_REGION/memberships/ADMIN_CLUSTER_NAME

Alternativly, you can set `--admin-cluster-membership` to the admin cluster's name, as in the example command. When you use only the admin cluster's name, set the admin cluster's project ID with the `--admin-cluster-membership-project` and location with `--admin-cluster-membership-location`. The admin cluster's location is either `global` or a Google Cloud region. If you need to find the region, run `gcloud container fleet memberships list`. 

  * `REGION`: The Google Cloud region in which the GKE On-Prem API (`gkeonprem.googleapis.com`), Fleet service (`gkehub.googleapis.com`), and the Connect service (`gkeconnect.googleapis.com`) run. Specify `us-west1` or another [supported region](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/reference/supported-regions-on-prem-api). The region can't be changed after the cluster is created. This setting specifies the region where the following are stored: 
    * The user cluster metadata that the GKE On-Prem API needs to manage the cluster lifecycle
    * The Cloud Logging and Cloud Monitoring data of system components
    * The Admin Audit log created by Cloud Audit Logs

The cluster name, project, and location together uniquely identify the cluster in Google Cloud.

**Important** If you plan to install Cloud Service Mesh, you must install version 1.19.3 or later. This is required because the Fleet and Connect services run in a region.
  * `VERSION`: The Google Distributed Cloud version for your user cluster. 
  * `YOUR_EMAIL_ADDRESS` and `ANOTHER_EMAIL_ADDRESS`: If you don't include the `--admin-users` flag, as the cluster creator, by default you are granted cluster admin privileges. But If you include `--admin-users` to designate another user as an administrator, you override the default and need to include both your email address and the email address of the other administrator. For example, to add two administrators: 
        
        --admin-users=sara@example.com \
            --admin-users=amal@example.com

When the cluster is created, the GKE On-Prem API applies the Kubernetes role-based access control (RBAC) policies to the cluster to grant you and other admin users the Kubernetes `clusterrole/cluster-admin` role, which provides full access to every resource in the cluster in all namespaces. 

**Note:** In addition to the Kubernetes RBAC policies, you must grant some Identity and Access Management (IAM) roles to the users who aren't project owners. For details on granting the IAM roles, see [Grant required roles](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/connect-to-cluster-console#grant_required_roles). 



  * `SERVICE_CIDR_BLOCK`: A range of IP addresses, in CIDR format, to be used for Services in your cluster. Must be at least a /24 range. 

Example: `--service-address-cidr-blocks=10.96.0.0/20`

  * `POD_CIDR_BLOCK`: A range of IP addresses, in CIDR format, to be used for Pods in your cluster. Must be at least a /18 range. 

Example: `--pod-address-cidr-blocks=192.168.0.0/16`



  * `--metal-lb-config-address-pools`: Include this flag to specify the configuration for address pools to be used by the MetalLB load balancer. The value for the flag has the following format: 
        
        --metal-lb-config-address-pool 'pool=NAME,avoid-buggy-ips=True|False,manual-assign=True|False,addresses=IP_ADDRESS_RANGE_1;IP_ADDRESS_RANGE_2;...' \

The value has segments that start with the keywords `pool`, `avoid-buggy-ip`, `manual-assign`, and `addresses`. Separate each segment with a comma. 

    * `pool`: A name of your choice for the pool. 
    * `avoid-buggy-ips`1: If you set this to `True`, the MetalLB controller will not assign IP addresses ending in .0 or .255 to Services. This avoids the problem of buggy consumer devices mistakenly dropping traffic sent to those special IP addresses. If not specified, defaults to `False`. 
    * `manual-assign`: If you do not want the MetalLB controller to automatically assign IP addresses from this pool to Services, set this to `True`. Then a developer can create a Service of type `LoadBalancer` and manually specify one of the addresses from the pool. If not specified, `manual-assign` is set to `False`. 
    * In the list of `addresses`: Each address must be a range either in [CIDR](https://tools.ietf.org/html/rfc4632) notation or hyphenated-range format. To specify a single IP address in a pool (such as for the ingress VIP), use /32 in CIDR notation, for example: `192.0.2.1/32`. 

Note the following:

    * Surround the entire value in single quotes.
    * Whitespace isn't allowed.
    * Separate each IP address range with a semicolon.

For example:
    
    --metal-lb-config-address-pool 'pool=pool1,avoid-buggy-ips=True,manual-assign=True,addresses=10.251.134.80/32;192.168.1.0/26;192.168.1.2-192.168.1.3'



  * `CONTROL_PLANE_VIP`: The IP address that you have chosen to configure on the load balancer for the Kubernetes API server of the user cluster. 

Example: `--control-plane-vip=203.0.113.3`

  * `INGRESS_VIP`: The IP address that you have chosen to configure on the load balancer for the ingress proxy. 

Example: `--ingress-vip=10.251.134.80`

The IP address for the ingress VIP must be in one of the MetalLB address pools. 



  * `--static-ip-config-ip-blocks`: Specify the default gateway, subnet mask, and a list of the static IP addresses for the worker nodes in the user cluster. The value for the flag has the following format: 
        
        --static-ip-config-ip-blocks 'gateway=GATEWAY,netmask=NETMASK,ips=IP_ADDRESS_1;IP_ADDRESS_2 HOST_2;...'

The value has segments that start with the keywords `gateway`, `netmask`, and `ips`. Separate the segments with a comma. 

Note the following:

    * Surround the entire value in single quotes.
    * Whitespace isn't allowed except between an IP address and a hostname.

In the list of IP addresses:

    * You can specify an individual IP address or a [CIDR](https://tools.ietf.org/html/rfc4632) block of IP addresses. 
    * Separate each IP address or CIDR block with a semicolon. 
    * For an individual IP address, you can optionally specify a hostname after the IP address. Separate the IP address and the hostname with a space. When you don't specify a hostname, Google Distributed Cloud uses the VM's name from vSphere as the hostname. 
    * If you specify a CIDR block, do not specify a value for hostname. 

For example:
    
    --static-ip-config-ip-blocks 'gateway=172.16.23.254,netmask=255.255.252.0,ips=172.16.20.10;172.16.20.11 host2;172.16.20.12/30'

  * `DNS_SERVER`: A comma-separated list of the IP addresses of DNS servers for the VMs. 
  * `DNS_SEARCH_DOMAIN`: A comma-separated list of the DNS search domains for the hosts to use. These domains are used as part of a domain search list. 

For example:
        
        --dns-search-domains example.com,examplepetstore.com

  * `NTP_SERVER`: A comma-separated list of the IP addresses of time servers for the VMs to use. 



### F5 BIG-IP & DHCP

This example shows how to create a user cluster with your F5 BIG-IP load balancer and using your DHCP server to get IP addresses for your cluster nodes.

You can use F5 for the user cluster only if your admin cluster is using F5. Be sure to install and configure the F5 BIG-IP ADC before integrating it with Google Distributed Cloud. [See F5 BIG-IP ADC installation guide](https://docs.cloud.google.com/architecture/partners/installing-f5-big-ip-adc-for-gke-on-prem) for more information. The F5 username and password are inherited from the admin cluster.

Be sure to scroll over if needed to fill in the `ADMIN_CLUSTER_NAME` placeholder for the `--admin-cluster-membership` flag. This example uses the fully-specified admin cluster name, so you don't need to include `--admin-cluster-membership-location` and `--admin-cluster-membership-project`.
    
    
    gcloud container vmware clusters create USER_CLUSTER_NAME \
      --project=FLEET_HOST_PROJECT_ID \
      --admin-cluster-membership=projects/FLEET_HOST_PROJECT_ID/locations/global/memberships/ADMIN_CLUSTER_NAME \
      --location=REGION \
      --version=VERSION \
      --admin-users=YOUR_EMAIL_ADDRESS \
      --admin-users=ANOTHER_EMAIL_ADDRESS \
      --service-address-cidr-blocks=SERVICE_CIDR_BLOCK \
      --pod-address-cidr-blocks=POD_CIDR_BLOCK \
      --f5-config-address=F5_CONFIG_ADDRESS \
      --f5-config-partition=F5_CONFIG_PARTITION \
      --f5-config-snat-pool=F5_CONFIG_SNAT_POOL \
      --control-plane-vipCONTROL_PLANE_VIP \
      --ingress-vip=INGRESS_VIP \
      --enable-dhcp
    

  * `USER_CLUSTER_NAME`: A name of your choice for your user cluster. The name can't be changed after the cluster is created. The name must: 
    * contain at most 40 characters
    * contain only lowercase alphanumeric characters or a hyphen (`-`)
    * start with an alphabetic character
    * end with an alphanumeric character
  * `FLEET_HOST_PROJECT_ID`: The ID of the project that you want to create the cluster in. The specified project is also used as the fleet host project. This must be the same project that the admin cluster is registered to. After the user cluster is created, it is automatically registered to the selected project's fleet. The fleet host project can't be changed after the cluster is created. 
  * `ADMIN_CLUSTER_NAME`: The name of the admin cluster that manages the user cluster. In the `--admin-cluster-membership` flag, you can use the fully-specified cluster name, which has the following format: 
        
        projects/FLEET_HOST_PROJECT_ID/locations/ADMIN_CLUSTER_REGION/memberships/ADMIN_CLUSTER_NAME

Alternativly, you can set `--admin-cluster-membership` to the admin cluster's name, as in the example command. When you use only the admin cluster's name, set the admin cluster's project ID with the `--admin-cluster-membership-project` and location with `--admin-cluster-membership-location`. The admin cluster's location is either `global` or a Google Cloud region. If you need to find the region, run `gcloud container fleet memberships list`. 

  * `REGION`: The Google Cloud region in which the GKE On-Prem API (`gkeonprem.googleapis.com`), Fleet service (`gkehub.googleapis.com`), and the Connect service (`gkeconnect.googleapis.com`) run. Specify `us-west1` or another [supported region](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/reference/supported-regions-on-prem-api). The region can't be changed after the cluster is created. This setting specifies the region where the following are stored: 
    * The user cluster metadata that the GKE On-Prem API needs to manage the cluster lifecycle
    * The Cloud Logging and Cloud Monitoring data of system components
    * The Admin Audit log created by Cloud Audit Logs

The cluster name, project, and location together uniquely identify the cluster in Google Cloud.

**Important** If you plan to install Cloud Service Mesh, you must install version 1.19.3 or later. This is required because the Fleet and Connect services run in a region.
  * `VERSION`: The Google Distributed Cloud version for your user cluster. 
  * `YOUR_EMAIL_ADDRESS` and `ANOTHER_EMAIL_ADDRESS`: If you don't include the `--admin-users` flag, as the cluster creator, by default you are granted cluster admin privileges. But If you include `--admin-users` to designate another user as an administrator, you override the default and need to include both your email address and the email address of the other administrator. For example, to add two administrators: 
        
        --admin-users=sara@example.com \
            --admin-users=amal@example.com

When the cluster is created, the GKE On-Prem API applies the Kubernetes role-based access control (RBAC) policies to the cluster to grant you and other admin users the Kubernetes `clusterrole/cluster-admin` role, which provides full access to every resource in the cluster in all namespaces. 

**Note:** In addition to the Kubernetes RBAC policies, you must grant some Identity and Access Management (IAM) roles to the users who aren't project owners. For details on granting the IAM roles, see [Grant required roles](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/connect-to-cluster-console#grant_required_roles). 



  * `SERVICE_CIDR_BLOCK`: A range of IP addresses, in CIDR format, to be used for Services in your cluster. Must be at least a /24 range. 

Example: `--service-address-cidr-blocks=10.96.0.0/20`

  * `POD_CIDR_BLOCK`: A range of IP addresses, in CIDR format, to be used for Pods in your cluster. Must be at least a /18 range. 

Example: `--pod-address-cidr-blocks=192.168.0.0/16`



  * `F5_CONFIG_ADDRESS`: The address of your F5 BIG-IP load balancer.

  * `F5_CONFIG_PARTITION`:The name of a BIG-IP partition that you created for your user cluster.

  * `F5_CONFIG_SNAT_POOL`: The name of your SNAT pool, if applicable.



  * `CONTROL_PLANE_VIP`: The IP address that you have chosen to configure on the load balancer for the Kubernetes API server of the user cluster. 

Example: `--control-plane-vip=203.0.113.3`

  * `INGRESS_VIP`: The IP address that you have chosen to configure on the load balancer for the ingress proxy. 

Example: `--ingress-vip=10.251.134.80`

The IP address for the ingress VIP must be in one of the MetalLB address pools. 



  * `--enable-dhcp`: Include `--enable-dhcp` if you want your cluster nodes to get their IP address from a DHCP server that you provide. Don't include this flag if you want to provide static IP addresses for your cluster nodes, or if you want to set up manual load balancing.



### Manual LB & Static IPs

This example shows how to create a user cluster with a manual load balancer and assigning static IP addresses to your cluster nodes.

You can use a manual load balancer for the user cluster only if your admin cluster uses a manual load balancer. In Google Distributed Cloud, the Kubernetes API server, ingress proxy, and the add-on service for log aggregation are each exposed by a Kubernetes Service of type `LoadBalancer`. Choose your own `nodePort` values in the 30000 - 32767 range for these Services. For the ingress proxy, choose a `nodePort` value for both HTTP and HTTPS traffic. See [Enabling manual load balancing mode](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.15/how-to/manual-load-balance) for more information.

Be sure to scroll over if needed to fill in the `ADMIN_CLUSTER_NAME` placeholder for the `--admin-cluster-membership` flag. This example uses the fully-specified admin cluster name, so you don't need to include `--admin-cluster-membership-location` and `--admin-cluster-membership-project`.
    
    
    gcloud container vmware clusters create USER_CLUSTER_NAME \
      --project=FLEET_HOST_PROJECT_ID \
      --admin-cluster-membership=projects/FLEET_HOST_PROJECT_ID/locations/global/memberships/ADMIN_CLUSTER_NAME \
      --location=REGION \
      --version=VERSION \
      --admin-users=YOUR_EMAIL_ADDRESS \
      --admin-users=ANOTHER_EMAIL_ADDRESS \
      --service-address-cidr-blocks=SERVICE_CIDR_BLOCK \
      --pod-address-cidr-blocks=POD_CIDR_BLOCK \
      --control-plane-vip=CONTROL_PLANE_VIP \
      --control-plane-node-port=CONTROL_PLANE_NODE_PORT \
      --ingress-vip=INGRESS_VIP \
      --ingress-http-node-port=INGRESS_HTTP_NODE_PORT \
      --ingress-https-node-port=INGRESS_HTTPS_NODE_PORT \
      --konnectivity-server-node-port=KONNECTIVITY_SERVER_NODE_PORT
    

Replace the following:

  * `USER_CLUSTER_NAME`: A name of your choice for your user cluster. The name can't be changed after the cluster is created. The name must: 
    * contain at most 40 characters
    * contain only lowercase alphanumeric characters or a hyphen (`-`)
    * start with an alphabetic character
    * end with an alphanumeric character
  * `FLEET_HOST_PROJECT_ID`: The ID of the project that you want to create the cluster in. The specified project is also used as the fleet host project. This must be the same project that the admin cluster is registered to. After the user cluster is created, it is automatically registered to the selected project's fleet. The fleet host project can't be changed after the cluster is created. 
  * `ADMIN_CLUSTER_NAME`: The name of the admin cluster that manages the user cluster. In the `--admin-cluster-membership` flag, you can use the fully-specified cluster name, which has the following format: 
        
        projects/FLEET_HOST_PROJECT_ID/locations/ADMIN_CLUSTER_REGION/memberships/ADMIN_CLUSTER_NAME

Alternativly, you can set `--admin-cluster-membership` to the admin cluster's name, as in the example command. When you use only the admin cluster's name, set the admin cluster's project ID with the `--admin-cluster-membership-project` and location with `--admin-cluster-membership-location`. The admin cluster's location is either `global` or a Google Cloud region. If you need to find the region, run `gcloud container fleet memberships list`. 

  * `REGION`: The Google Cloud region in which the GKE On-Prem API (`gkeonprem.googleapis.com`), Fleet service (`gkehub.googleapis.com`), and the Connect service (`gkeconnect.googleapis.com`) run. Specify `us-west1` or another [supported region](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/reference/supported-regions-on-prem-api). The region can't be changed after the cluster is created. This setting specifies the region where the following are stored: 
    * The user cluster metadata that the GKE On-Prem API needs to manage the cluster lifecycle
    * The Cloud Logging and Cloud Monitoring data of system components
    * The Admin Audit log created by Cloud Audit Logs

The cluster name, project, and location together uniquely identify the cluster in Google Cloud.

**Important** If you plan to install Cloud Service Mesh, you must install version 1.19.3 or later. This is required because the Fleet and Connect services run in a region.
  * `VERSION`: The Google Distributed Cloud version for your user cluster. 
  * `YOUR_EMAIL_ADDRESS` and `ANOTHER_EMAIL_ADDRESS`: If you don't include the `--admin-users` flag, as the cluster creator, by default you are granted cluster admin privileges. But If you include `--admin-users` to designate another user as an administrator, you override the default and need to include both your email address and the email address of the other administrator. For example, to add two administrators: 
        
        --admin-users=sara@example.com \
            --admin-users=amal@example.com

When the cluster is created, the GKE On-Prem API applies the Kubernetes role-based access control (RBAC) policies to the cluster to grant you and other admin users the Kubernetes `clusterrole/cluster-admin` role, which provides full access to every resource in the cluster in all namespaces. 

**Note:** In addition to the Kubernetes RBAC policies, you must grant some Identity and Access Management (IAM) roles to the users who aren't project owners. For details on granting the IAM roles, see [Grant required roles](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/connect-to-cluster-console#grant_required_roles). 



  * `SERVICE_CIDR_BLOCK`: A range of IP addresses, in CIDR format, to be used for Services in your cluster. Must be at least a /24 range. 

Example: `--service-address-cidr-blocks=10.96.0.0/20`

  * `POD_CIDR_BLOCK`: A range of IP addresses, in CIDR format, to be used for Pods in your cluster. Must be at least a /18 range. 

Example: `--pod-address-cidr-blocks=192.168.0.0/16`



  * `CONTROL_PLANE_VIP`: The IP address that you have chosen to configure on the load balancer for the Kubernetes API server of the user cluster.

Example: `--control-plane-vip=203.0.113.3`

  * `CONTROL_PLANE_NODE_PORT`: A `nodePort` value for the Kubernetes API server.

  * `INGRESS_VIP`: The IP address that you have chosen to configure on the load balancer for the ingress proxy.

Example: `--ingress-vip=203.0.113.4`

  * `INGRESS_HTTP_NODE_PORT`: A `nodePort` value for HTTP traffic to the ingress proxy.

  * `INGRESS_HTTPS_NODE_PORT`: A `nodePort` value for HTTPS traffic to the ingress proxy.

  * `KONNECTIVITY_SERVER_NODE_PORT`: A `nodePort` value for the Konnectivity server.



  * `--static-ip-config-ip-blocks`: Specify the default gateway, subnet mask, and a list of the static IP addresses for the worker nodes in the user cluster. The value for the flag has the following format: 
        
        --static-ip-config-ip-blocks 'gateway=GATEWAY,netmask=NETMASK,ips=IP_ADDRESS_1;IP_ADDRESS_2 HOST_2;...'

The value has segments that start with the keywords `gateway`, `netmask`, and `ips`. Separate the segments with a comma. 

Note the following:

    * Surround the entire value in single quotes.
    * Whitespace isn't allowed except between an IP address and a hostname.

In the list of IP addresses:

    * You can specify an individual IP address or a [CIDR](https://tools.ietf.org/html/rfc4632) block of IP addresses. 
    * Separate each IP address or CIDR block with a semicolon. 
    * For an individual IP address, you can optionally specify a hostname after the IP address. Separate the IP address and the hostname with a space. When you don't specify a hostname, Google Distributed Cloud uses the VM's name from vSphere as the hostname. 
    * If you specify a CIDR block, do not specify a value for hostname. 

For example:
    
    --static-ip-config-ip-blocks 'gateway=172.16.23.254,netmask=255.255.252.0,ips=172.16.20.10;172.16.20.11 host2;172.16.20.12/30'

  * `DNS_SERVER`: A comma-separated list of the IP addresses of DNS servers for the VMs. 
  * `DNS_SEARCH_DOMAIN`: A comma-separated list of the DNS search domains for the hosts to use. These domains are used as part of a domain search list. 

For example:
        
        --dns-search-domains example.com,examplepetstore.com

  * `NTP_SERVER`: A comma-separated list of the IP addresses of time servers for the VMs to use. 



For a complete list of the flags and their descriptions, see the [gcloud CLI reference](https://docs.cloud.google.com/sdk/gcloud/reference/container/vmware/clusters/create).

### Control plane flags

If you want to use non-default values for the control plane configuration, include one or more of the following flags:

  * `--cpus=vCPUS`: The number of vCPUs (minimum 4) for each control-plane node for your user cluster. If not specified, the default is 4 vCPUs.

  * `--memory=MEMORY`: The memory size in mebibytes (MiB) for each control-plane for your user cluster. The minimum value is 8192 and it must be a multiple of 4. If not specified, the default is 8192.

  * `--replicas=NODES`: The number of control-plane nodes for your user cluster. For example, you may select 1 control-plane node for a development environment and 3 control-planes nodes for high availability (HA), production environments.

  * `--enable-auto-resize`: If you want to enable automatic resizing of the control-plane nodes for the user cluster, include `--enable-auto-resize`. Resizing means that the vCPU and memory resources assigned to a node are adjusted automatically. When enabled, the control-plane nodes for the user cluster are resized according to the number of worker nodes in the user cluster. So as you add more worker nodes to the user cluster, the control-plane nodes are increased in size.

  * `--enable-control-plane-v2`: If you want to enable Controlplane V2, include `--enable-control-plane-v2`. When Controlplane V2 is enabled, the control plane for a user cluster runs on one or more nodes in the user cluster itself. By default, the control plane for a user cluster runs on one or more nodes on the admin cluster (referred to as the kubeception model). When Controlplane V2 is enabled, the values for `--cpus` and `--memory` apply to the control plane nodes in the user cluster. The number of nodes is determined by the number of IP addresses that you enter in `--control-plane-ip-block`. When Controlplane V2 isn't enabled, the values for `--cpus`, `--memory`, and `--replicas` apply to the control plane nodes in the admin cluster. Make sure you set aside [enough IP addresses for your admin cluster](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.15/how-to/manage-node-ip-addresses#how_many_ip_addresses_does_an_admin_cluster_need).

If you enable Controlplane V2, you must also specify the following flags:

    * `--dns-servers=DNS_SERVER_1,...`: A comma-separated list of the IP addresses of DNS servers for the VMs.

    * `--ntp-servers=NTP_SERVER_1,...`: A comma-separated list of the IP addresses of time servers for the VMs to use.

    * `--control-plane-ip-block`, which has the following format:
          
          --control-plane-ip-block 'gateway=CP_GATEWAY,netmask=CP_NETMASK,ips=CP_IP_ADDRESS_1;CP_IP_ADDRESS_2 CP_HOST_2'

The value has segments that start with the keywords `gateway`, `netmask`, and `ips`. Separate the segments with a comma.

Note the following:

      * Surround the entire value in single quotes.
      * Whitespace isn't allowed except between an IP address and a hostname.

In the list of IP addresses:

      * You can specify an individual IP address or a [CIDR](https://tools.ietf.org/html/rfc4632) block of IP addresses.

      * Separate each IP address or CIDR block with a semicolon.

      * For an individual IP address, you can optionally specify a hostname after the IP address. Separate the IP address and the hostname with a space.

      * If you specify a CIDR block, do not specify a value for hostname.

For example:
    
    --control-plane-ip-block 'gateway=192.168.0.1,netmask=255.0.0.0,ips=192.168.1.1;192.168.1.2 hostname-2;192.168.2.2/28`
    

    * Optional: `--dns-search-domains=DNS_SEARCH_DOMAIN_1,...`: A comma-separated list of the DNS search domains for the hosts to use. These domains are used as part of a domain search list.

For example:
          
          --dns-search-domains example.com,examplepetstore.com




For a complete list of the flags and their descriptions, see the [gcloud CLI reference](https://docs.cloud.google.com/sdk/gcloud/reference/container/vmware/clusters/create).

### vSphere flags

Specify the following optional flags if needed:

  * `--disable-aag-config`: If you don't include this flag the VMware Distributed Resource Scheduler (DRS) anti-affinity rules are automatically created for your user cluster's nodes, causing them to be spread across at least 3 physical hosts in your data center. Make sure that your vSphere environment meets the [requirements](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.15/how-to/user-cluster-configuration-file#antiaffinitygroups-enabled-field). If your cluster doesn't meet the requirements, include this flag.

**Note:** If you followed [Set up minimal infrastructure](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.15/how-to/minimal-infrastructure), you only have one ESXi host, so be sure to include this flag.
  * `--disable-vsphere-csi`: If you don't include this flag, the vSphere Container Storage Interface (CSI) components are deployed in the user cluster. The CSI driver runs in a native Kubernetes cluster deployed in vSphere to provision persistent volumes on vSphere storage. For more information, see [Using the vSphere Container Storage Interface driver](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.15/how-to/using-vsphere-csi-driver). If you don't want to deploy the CSI components, include this flag.




For a complete list of the flags and their descriptions, see the [gcloud CLI reference](https://docs.cloud.google.com/sdk/gcloud/reference/container/vmware/clusters/create)

Before running the `gcloud` command to create the cluster, you might want to include `--validate-only` to validate the configuration that you specified in the flags to the `gcloud` command. When you are ready to create the cluster, remove this flag and run the command.

It takes 15 minutes or more to create the user cluster. You can view the cluster in the Google Cloud console on the [Anthos clusters](https://console.cloud.google.com/anthos/clusters) page.

### Create a node pool

After the cluster is created, you need to create at least one node pool before deploying workloads.
    
    
    gcloud container vmware node-pools create NODE_POOL_NAME \
    --cluster=USER_CLUSTER_NAME  \
    --project=FLEET_HOST_PROJECT_ID \
    --location=REGION \
    --image-type=IMAGE_TYPE  \
    --boot-disk-size=BOOT_DISK_SIZE \
    --cpus=vCPUS \
    --memory=MEMORY \
    --replicas=NODES \
    --enable-load-balancer
    

Replace the following:

  * `NODE_POOL_NAME`: A name of your choice for the node pool. The name must:

    * contain at most 40 characters
    * contain only lowercase alphanumeric characters or a hyphen (`-`)
    * start with an alphabetic character
    * end with an alphanumeric character
  * `USER_CLUSTER_NAME`: The name of the newly-created user cluster.

  * `FLEET_HOST_PROJECT_ID`: The ID of the project that the cluster is registered to.

  * `REGION`: The Google Cloud location that you specified when you created the cluster.

  * `IMAGE_TYPE`: The type of OS image to run on the VMs in the node pool. Set to one of the follow: `ubuntu_containerd` or `cos`.

  * `BOOT_DISK_SIZE`: The size of the boot disk in gibibytes (GiB) for each node in the pool. The minimum is 40 GiB.

  * `vCPUs`: The number of vCPUs for each node in the node pool. The minimum is 4.

  * `MEMORY`: The memory size in mebibytes (MiB) for each node in the pool. The minimum is 8192 MiB per user cluster worker node and the value must be a multiple of 4.

  * `NODES`: The number of nodes in the node pool. The minimum is 3.

  * If you are using MetalLB as the load balancer, optionally, include `--enable-load-balancer` if you want to allow the MetalLB speaker to run on the nodes in the pool. MetalLB must be enabled in at least one node pool. If you don't include this flag, you must create another node pool to use for MetalLB.




For information about optional flags, see [Add a node pool](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.15/how-to/managing-node-pools#add_a_node_pool) and the [gcloud CLI reference](https://docs.cloud.google.com/sdk/gcloud/reference/container/vmware/node-pools/create).

### Terraform

You can use the following basic configuration sample to create a user cluster with the bundled MetalLB load balancer and one node pool.

For more information and other examples, see the [`google_gkeonprem_vmware_cluster` reference documentation](https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/gkeonprem_vmware_cluster).

  1. Clone the `anthos-samples` repository and change to the directory where the Terraform sample is located:
         
         git clone https://github.com/GoogleCloudPlatform/anthos-samples
         cd anthos-samples/anthos-onprem-terraform/avmw_user_cluster_metallb
         




### Set variables in `terraform.tfvars`

The sample provides an example variables file to pass in to `main.tf`, which shows how to configure the bundled MetalLB load balancer and enable your cluster nodes to get their IP addresses from a DHCP server that you provide.

  1. Make a copy of the `terraform.tfvars.sample` file:
         
         cp terraform.tfvars.sample terraform.tfvars
         

  2. Modify the parameters values in `terraform.tfvars`.
         
         project_id                  = "FLEET_HOST_PROJECT_ID"
         region                      = "REGION"
         admin_cluster_name          = "ADMIN_CLUSTER_NAME"
         on_prem_version             = "VERSION"
         admin_user_emails           = ["YOUR_EMAIL_ADDRESS", "ADMIN_2_EMAIL_ADDRESS"]
         cluster_name                = "avmw-user-cluster-metallb"
         control_plane_node_cpus     = 4
         control_plane_node_memory   = 8192
         control_plane_node_replicas = 3
         control_plane_vip           = "CONTROL_PLANE_VIP"
         ingress_vip                 = "INGRESS_VIP"
         lb_address_pools            = [
             { name = "lbpool_1", addresses = ["10.200.0.51-10.200.0.70"] }
         ]
         

The following list describes the variables:

     * `project_id`: The ID of the project that you want to create the cluster in. The specified project is also used as the fleet host project. This must be the same project that the admin cluster is registered to. After the user cluster is created, it is automatically registered to the selected project's fleet. The fleet host project can't be changed after the cluster is created.

     * `region`: The Google Cloud region in which the GKE On-Prem API runs. Specify `us-west1` or another [supported region](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.15/reference/supported-regions-on-prem-api).

     * `admin_cluster_name`: The name of the admin cluster that manages the user cluster.

     * `on_prem_version`: The Google Distributed Cloud version for your user cluster. Typically, you specify the same version as the admin cluster. To specify a later version, Install a later version than the admin cluster version. If you don't know the admin cluster version, run `gcloud container vmware clusters query-version-config`, which is the first step in Install a later version than the admin cluster version.

     * `admin_user_emails`: A list of email addresses of the users to be granted administrative privileges on the cluster. Be sure to add your email address if you intend to administer the cluster.

When the cluster is created, the GKE On-Prem API applies the Kubernetes role-based access control (RBAC) policies to the cluster to grant the admin users the Kubernetes `clusterrole/cluster-admin` role, which provides full access to every resource in the cluster in all namespaces. This also lets users log on to the console using their Google identity.

     * `cluster_name`: A name of your choice for your user cluster. The name can't be changed after the cluster is created. The name must:

       * contain at most 40 characters
       * contain only lowercase alphanumeric characters or a hyphen (`-`)
       * start with an alphabetic character
       * end with an alphanumeric character
     * `control_plane_node_cpus`: The number of vCPUs for each control-plane node for your user cluster. The minimum is 4 vCPUs.

     * `control_plane_node_memory`: The memory size in mebibytes (MiB) for each control-plane for your user cluster. The minimum value is 8192 and it must be a multiple of 4.

     * `control_plane_node_replicas`: The number of control-plane nodes for your user cluster. For example, you may enter 1 control-plane node for a development environment and 3 control-planes nodes for high availability (HA), production environments.

     * `control_plane_vip`: The virtual IP address (VIP) that you have chosen to configure on the load balancer for the Kubernetes API server of the user cluster.

     * `ingress_vip`: The IP address that you have chosen to configure on the load balancer for the ingress proxy.

     * `lb_address_pools`: A list of maps that define the address pools to be used by the MetalLB load balancer. The ingress VIP must be in one of these pools. Specify the following:

       * `name`: A name for the pool.
       * `addresses`: An address range either in [CIDR](https://tools.ietf.org/html/rfc4632) notation or hyphenated-range format. To specify a single IP address in a pool (such as for the ingress VIP), use /32 in CIDR notation, for example: `192.0.2.1/32`.

Replace the example IP addresses with your values, and add additional address pools if needed.

  3. Save the changes in `terraform.tfvars`. If you don't want to make any optional changes to `main.tf`, skip to the section that follows, Create the cluster and one node pool.




### Optional: Configure cluster settings in `main.tf`

This section explains some optional configuration changes that you can make in `main.tf`. Before making changes, make a backup of `main.tf`:
    
    
    cp main.tf main.tf.bak
    

#### Worker node IP addressing mode

By default, `main.tf` configures the cluster to use a DHCP server that you provide to assign IP addresses to the cluster's worker nodes. DHCP is configured by including the `dhcp_config` map within the `network_config` block. If you want to provide static IP addresses for your worker nodes, make the following changes to `main.tf`:

  1. Replace the `network_config` block and include a `static_ip_config` block. For example:
         
         network_config {
           service_address_cidr_blocks = ["10.96.0.0/12"]
           pod_address_cidr_blocks = ["192.168.0.0/16"]
           host_config {
             dns_servers = ["10.254.41.1"]
             ntp_servers = ["216.239.35.8"]
           }
           static_ip_config {
             ip_blocks {
               netmask = "255.255.252.0"
               gateway = "10.251.31.254"
               ips {
                 ip = "10.251.30.153"
                 hostname = "vm-1"
               }
               ips {
                 ip = "10.251.31.206"
                 hostname = "vm-2"
               }
               ips {
                 ip = "10.251.31.193"
                 hostname = "vm-3"
               }
               ips {
                 ip = "10.251.30.230"
                 hostname = "vm-4"
               }
             }
           }
         }
         

  2. Replace the following with your values:

     * `service_address_cidr_blocks`: A range of IP addresses, in CIDR format, to be used for Services in your cluster. Must be at least a /24 range.

     * `pod_address_cidr_blocks`: A range of IP addresses, in CIDR format, to be used for Pods in your cluster. Must be at least a /18 range.

     * `dns_servers`: A list of the IP addresses of DNS servers for the VMs.

     * `ntp_servers`: A list of the IP addresses of time servers for the VMs to use.

     * In the `static_ip_config` block, replace the values for `netmask` and `gateway` with the addresses for your network. Replace`ip` and `hostname` with the IP addresses and hostnames of your worker nodes.




#### Configure Controlplane V2

By default, `main.tf` configures the control plane for the user cluster to run on one or more nodes on the admin cluster (referred to as the kubeception model). If you prefer, you can enable Controlplane V2. When Controlplane V2 is enabled, the control plane for a user cluster runs on one or more nodes in the user cluster itself. To configure Controlplane V2, make the following changes to `main.tf`:

  1. Add the following line after the line with `admin_cluster_membership`:
         
         enable_control_plane_v2 = "true"
         

  2. Add a `control_plane_v2_config` map to the `network_config` block, for example:
         
         control_plane_v2_config {
           control_plane_ip_block {
             netmask = "255.255.252.0"
             gateway = "10.250.71.254"
             ips {
               ip = "10.250.68.54"
               hostname = "cpv2-vm1"
             }
             ips {
               ip = "10.250.68.128"
               hostname = "cpv2-vm2"
             }
             ips {
               ip = "10.250.71.50"
               hostname = "cpv2-vm3"
             }
           }
         }
         

  3. Replace the values for `netmask` and `gateway` with IP addresses from your network. Replace `ip` and `hostname` with the IP addresses of your conrol plane nodes.




### Create the cluster and one node pool

  1. Initialize and create the Terraform plan:
         
         terraform init
         

Terraform installs any needed libraries, such as the Google Cloud provider. 

  2. Review the configuration and make changes if needed:
         
         terraform plan
         

  3. Apply the Terraform plan to create the user cluster:
         
         terraform apply
         

It takes about 15 minutes or more to create the user cluster, and another 15 minutes to create the node pool. You can view the cluster in the Google Cloud console on the [Anthos clusters](https://console.cloud.google.com/anthos/clusters) page.




## Connect to the user cluster

When you create a user cluster using a GKE On-Prem API client, you have the option to add yourself and other users as cluster adimistrators by specifying Google Cloud account email addresses:

  * In the console, your email address is automatically added on the **Cluster basics** page in the **Authorization** section, and you have the option to add other cluster admin users.

  * With the gcloud CLI, include the `--admin-users` flag set to your email address. The flag doesn't take a list. Add the `--admin-users` flag for each cluster admin user.

  * With the Terraform sample, you can specify yourself and other admin users in the `admin_user_emails` variable in the `terraform.tvars.sample` file.




The cluster is configured with the Kubernetes role-based access control (RBAC) policies that grant admin users the `cluster-admin` role and lets them log in to the cluster from the console using their Google Cloud identity. For more information about see [Set up Google identity authentication](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.15/how-to/connect-to-cluster-console#set_up_google_identity_authentication).

All clusters have a canonical endpoint. The endpoint exposes the Kubernetes API server that `kubectl` and other services use to communicate with your cluster control plane over TCP port 443. This endpoint is not accessible on the public internet. If you have access to your cluster's private endpoint through your VPC, you can connect directly to the private endpoint and generate a kubeconfig file directly. Otherwise, you can use the Connect gateway. In this case `kubectl` uses Connect, which then securely forwards the traffic to the private endpoint on your behalf.

To access the user cluster from the command line, you need a kubeconfig file. There are two ways to get a kubeconfig file:

  * Use the Connect gateway to access the cluster from a computer that has the Google Cloud CLI installed on it. The Connect gateway lets you easily and securely manage your clusters. For more information, see [Connecting to registered clusters with the Connect gateway](https://docs.cloud.google.com/anthos/multicluster-management/gateway).

  * For direct access to private endpoints, create a kubeconfig file on your admin workstation and manage the cluster from your admin workstation.




Be sure to wait until the console indicates that user cluster status is healthy.

### Connect gateway

  1. Either [initialize](https://docs.cloud.google.com/sdk/docs/install-sdk#initializing_the) the gcloud CLI for use with the fleet host project, or run the following commands to log in with your Google account, set your fleet host project as the default, and update components:
         
         gcloud auth login
         gcloud config set project PROJECT_ID
         gcloud components update
         

  2. Fetch the cluster credentials used to interact with Connect gateway. In the following command, replace`MEMBERSHIP_NAME` with your cluster's name. In Google Distributed Cloud, the membership name is the same as the cluster name.
         
         gcloud container fleet memberships get-credentials MEMBERSHIP_NAME
         

This command returns a special **Connect gateway-specific`kubeconfig`** that lets you connect to the cluster through the gateway.

After you have the necessary credentials, you can run commands using `kubectl` as you normally would for any Kubernetes cluster, and you don't need to specify the name of the kubeconfig file, for example:
         
         kubectl get namespaces
         




### Admin workstation

To create the user cluster kubeconfig file on your admin workstation, run the following command to save a new `kubeconfig` file for the user cluster locally. Replace the following:

  * CLUSTER_NAME: the name of the newly-created user cluster
  * ADMIN_CLUSTER_KUBECONFIG: the path to the admin cluster `kubeconfig` file
  * USER_CLUSTER_KUBECONFIG: the name of the user cluster `kubeconfig` file that the command outputs


    
    
    kubectl get secret admin \
      --kubeconfig ADMIN_CLUSTER_KUBECONFIG \
      -n CLUSTER_NAME \
      -o=jsonpath='{.data.admin\.conf}' | base64 -d > USER_CLUSTER_KUBECONFIG
    

After the file has been saved, you can begin accessing the user cluster using `kubectl` on the admin workstation, for example:
    
    
    kubectl --kubeconfig USER_CLUSTER_KUBECONFIG get namespaces
    

## Install a later version than the admin cluster version

An admin cluster can manage user clusters at different versions. If you want to create a user cluster that is a later version than the admin cluster, you need to download and deploy the components that the admin cluster needs to manage user clusters of that version, as follows:

  1. Get a list of available versions:
         
         gcloud container vmware clusters query-version-config \
             --admin-cluster-membership=ADMIN_CLUSTER_NAME \
             --admin-cluster-membership-project=FLEET_HOST_PROJECT_ID \
             --location=REGION
         

Replace the following:

     * `ADMIN_CLUSTER_NAME`: The name of the admin cluster.

     * `FLEET_HOST_PROJECT_ID`: The ID of the project that the admin cluster is registered to.

     * `REGION`: The Google Cloud region in which the GKE On-Prem API runs. This is the region that you will specify when you create the user cluster. Specify `us-west1` or another [supported region](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.15/reference/supported-regions-on-prem-api).

The output of the command is similar to the following:
    
    versions:
    - isInstalled: true
      version: 1.14.3-gke.25
    - version: 1.14.4-gke.54
    - version: 1.15.0-gke.581
    

Versions installed on the admin cluster are annotated with `isInstalled=true`.

  2. If you haven't already, [enroll the admin cluster in the GKE On-Prem API](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.15/how-to/enroll-cluster). After the cluster is enrolled in the GKE On-Prem API, you don't need to do this step again.

  3. Download the new version of the components and deploy them in the admin cluster:
         
         gcloud beta vmware admin-clusters update ADMIN_CLUSTER_NAME \
             --project=FLEET_HOST_PROJECT_ID \
             --location=REGION \
             --required-platform-version=VERSION
         

This command downloads the version of the components that you specify in `--required-platform-version` to the admin cluster, and then deploys the the components. You can now create a user cluster with the specified version.




## What's next

  * [Deploy an application](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.15/how-to/deploy-first-app)
  * [Troubleshoot issues creating a user cluster in the Cloud console](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.15/troubleshoot-user-cluster-create-api)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
