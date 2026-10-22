---
url: https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/installing/creating-clusters/create-user-cluster-api/
title: Create a user cluster using GKE On-Prem API clients \u00a0|\u00a0 Google Distributed Cloud software only for bare metal \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:57:40.406688+00:00
---

# Create a user cluster using GKE On-Prem API clients  |  Google Distributed Cloud software only for bare metal  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/installing/creating-clusters/create-user-cluster-api/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Distributed, hybrid, and multicloud ](https://docs.cloud.google.com/docs/dhm-cloud)
  * [ Google Distributed Cloud ](https://docs.cloud.google.com/distributed-cloud/docs)
  * [ GDC for bare metal ](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs)
  * [ Guides ](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/concepts/about-bare-metal)



Send feedback 

#  Create a user cluster using GKE On-Prem API clients Stay organized with collections  Save and categorize content based on your preferences. 

This page describes how to create a user cluster by using the Google Cloud console, the Google Cloud CLI (gcloud CLI), or Terraform.

## What is the GKE On-Prem API?

The GKE On-Prem API is a Google Cloud-hosted API that lets you manage the lifecycle of your on-premises clusters using Terraform and standard Google Cloud applications. The GKE On-Prem API runs in Google Cloud's infrastructure. Terraform, the console, and the gcloud CLI are clients of the API, and they use the API to create clusters in your data center.

To manage the lifecycle of your clusters, the GKE On-Prem API must store metadata about your cluster's state in Google Cloud, using the Google Cloud region that you specify when creating the cluster. This metadata lets the API manage the cluster lifecycle and doesn't include workload-specific data.

When you create a cluster using an GKE On-Prem API client, you specify a Google Cloud project. After the cluster is created, it is automatically registered to the specified project's [fleet](https://docs.cloud.google.com/anthos/fleet-management/docs). This project is referred to as the [fleet host project](https://docs.cloud.google.com/anthos/fleet-management/docs/fleet-concepts#fleet-host-project). The fleet host project can't be changed after the cluster is created.

If you prefer, you can create a user cluster by creating a user cluster configuration file and using `bmctl`, as described in [Creating a user cluster](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/installing/creating-clusters/user-cluster-creation).

If you want to use Terraform, the console or gcloud CLI to manage the lifecycle of clusters that were created using `bmctl`, see [Configure a user cluster to be managed by the GKE On-Prem API](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/how-to/enroll-cluster)..

## Before you begin

This section describes the requirements for creating a user cluster using GKE On-Prem API clients.

### Grant IAM permissions

If you aren't a project owner, you must be granted [roles/gkeonprem.admin](https://docs.cloud.google.com/iam/docs/roles-permissions/gkeonprem).

If you want to access the Google Kubernetes Engine pages in the console, you must also have the following roles:

  * [roles/container.viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/container).
  * [roles/gkehub.viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/gkehub#gkehub.viewer)



After the cluster is created, if your aren't a project owner and you want to use the connect gateway to connect to the user cluster by the command line, the following roles are required:

  * [roles/gkehub.gatewayAdmin](https://docs.cloud.google.com/iam/docs/roles-permissions/gkehub#gkehub.gatewayAdmin): This role lets you access the Connect Gateway API. If you only need read-only access to the cluster, the `roles/gkehub.gatewayReader` is sufficient.

  * [roles/gkehub.viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/gkehub#gkehub.viewer): This role lets you retrieve cluster credentials.




For information on granting the roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access).

### Required Google APIs

Make sure that all the [required Google APIs](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/installing/configure-sa#enable_apis) are enabled in the fleet host project.

If you will be using the gcloud CLI to create the cluster, you must enable the GKE On-Prem API. If you are using the console to create the cluster, it enables the GKE On-Prem API automatically.
    
    
    gcloud services enable --project FLEET_HOST_PROJECT_ID \
        gkeonprem.googleapis.com
    

### Admin cluster prerequisites

You need a working admin cluster before you can create a user cluster. The admin cluster must:

  * Have access to the Kubernetes API server on the user cluster after it is created.

  * Have network connectivity to all nodes on the user cluster after it is created.

  * Must be registered to a [fleet](https://docs.cloud.google.com/kubernetes-engine/fleet-management/docs/fleet-concepts). The project ID that is configured in the [`gkeConnect.projectID`](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/reference/cluster-config-ref#gkeconnect-projectid), field of that admin cluster, which is referred to as the [fleet host project](https://docs.cloud.google.com/kubernetes-engine/fleet-management/docs/fleet-concepts#fleet-host-project), must be the same project that you will be creating the user cluster in.




### Cluster node machine prerequisites

Review [Cluster node machine prerequisites](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/installing/node-machine-prerequisites) to make sure that the machines that will be running the user cluster meet the prerequisites.

### Command line access

After the cluster is created, if you want to use the connect gateway to run `kubectl` against the user cluster on computers other than the admin workstation, install the following command-line tools on the computer that you plan to use.

**Note:** If you are using Cloud Shell as your shell environment for interacting with Google Cloud, these tools are installed for you.

  * The latest version of the [gcloud CLI](https://docs.cloud.google.com/sdk/docs/install).
  * `kubectl` for running commands against Kubernetes clusters. If you need to install `kubectl`, follow these [instructions](https://docs.cloud.google.com/kubernetes-engine/fleet-management/docs/before-you-begin#install-kubectl).



## Create a user cluster

You can use Terraform, the Google Cloud console, or the Google Cloud CLI (gcloud CLI) to create a cluster that is managed by the GKE On-Prem API. If this is your first time installing Google Distributed Cloud, you might find the console the easiest tool to use.

After you are more familiar with the information that you need to provide to create clusters, you might find Terraform or the gcloud CLI more convenient, particularly if you will be creating more than one cluster. [Terraform](https://developer.hashicorp.com/terraform/intro) is an industry-standard infrastructure as code tool. If your organization already uses Terraform, then you will likely want to use it for creating clusters and managing the cluster lifecycle.

With the gcloud CLI, you can save the command with its arguments to a text file and make changes as needed to create additional clusters. If you are using a CI/CD tool, such as [Cloud Build](https://docs.cloud.google.com/build/docs/overview), you can use the `gcloud` commands to create a cluster and node pool and specify the `--impersonate-service-account` flag to automate the creation.

### Console

Most of the settings in the console correspond to the fields in the [cluster configuration file](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/reference/cluster-config-ref).

  1. In the console, go to the **Create a bare metal cluster** page.

[Go to Create a bare metal cluster](https://console.cloud.google.com/kubernetes/baremetal/add)

  2. Select the Google Cloud project that you want to create the cluster in. The selected project is also used as the fleet host project. This must be the same project that the admin cluster is registered to. After the user cluster is created, it is automatically registered to the selected project's fleet.

  3. Click **Next** to begin configuring the cluster.




The following sections guide you through configuring the user cluster.

### Cluster basics

Enter basic information about the cluster.

  1. Enter a **Name** for the user cluster.
  2. Under **Admin cluster** , select the admin cluster from the list.

  3. In the **Google Cloud API Location** field, select the Google Cloud region from the list. This setting specifies the region where the following APIs and services run:

     * GKE On-Prem API (`gkeonprem.googleapis.com`)
     * Fleet service (`gkehub.googleapis.com`)
     * Connect service (`gkeconnect.googleapis.com`)

This setting also controls the region in which the following are stored:

     * The user cluster metadata that the GKE On-Prem API needs to manage the cluster lifecycle
     * The Cloud Logging and Cloud Monitoring data of system components
     * The Admin Audit log created by Cloud Audit Logs

The cluster name, project, and location together uniquely identify the cluster in Google Cloud.

  4. Select the version for your user cluster. User clusters must be either the same minor version as the admin cluster or one minor version lower than the admin cluster.

  5. As the cluster creator, you are granted cluster admin privileges to the cluster. Optionally, enter the email address of another user who will administer the cluster in the **Admin user** field.

When the cluster is created, the GKE On-Prem API applies the Kubernetes role-based access control (RBAC) policies to the cluster to grant you and other admin users the Kubernetes `clusterrole/cluster-admin` role, which provides full access to every resource in the cluster in all namespaces.

**Note:** In addition to the Kubernetes RBAC policies, you must grant some Identity and Access Management (IAM) roles to the users who aren't project owners. For details on granting the IAM roles, see [Grant required roles](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/how-to/anthos-ui#grant_required_roles).
  6. In the **Node configuration** section, specify the following:

     * **Maximum Pods per node** : Enter the maximum number of Pods that can be run on a single node. Allowable values are between `32`–`250`, inclusive. Kubernetes assigns a [Classless Inter-Domain Routing (CIDR) block](https://tools.ietf.org/html/rfc1918) to each node so that each pod can have a unique IP address. The size of the CIDR block corresponds to the maximum number of pods per node. For more information about setting the maximum number of pods per node, [Pod networking](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/concepts/network-reqs#pod_networking).

     * **Container runtime** : **containerd** is the only available container runtime for your cluster.

  7. Click **Next** to go to the **Networking** section.




### Networking

In this section, you specify the IP addresses for your cluster's nodes, Pods, and Services. If you are using bundled load balancing with MetalLB, you configure that as well.

  1. In the **Control plane** node section, enter the IPv4 address of each control plane node. Control plane nodes run the system workload. Typically, this is either a single machine if using a minimum deployment or three machines if using a high availability (HA) deployment. Specify an odd number of nodes to have a majority quorum for HA. This field can be changed whenever you update or upgrade a cluster.

Click **\+ Add IP Address** as needed to enter more IP addresses.

  2. In the **Load balancer** section, select the load balancer from the **Mode** list to set up for your cluster. See [Overview of load balancers](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/installing/load-balance) for more information.

### Bundled with MetalLB

Configure load balancing with the bundled MetalLB load balancer. With this option, Google Distributed Cloud deploys Layer 4 load balancers that run on either a dedicated pool of worker nodes or on the same nodes as the control plane.

     1. In the **Load balancer node pools** section, select one of the following:

        * **Use control plane nodes** : Choose this option to run the load balancers on the same nodes as the control plane.

        * **Create load balancer node pool** : Choose this advanced option if you need to run the load balancers on a dedicated pool of worker nodes. All nodes in the load balancer node pool must be in the same Layer 2 subnet as the load balancer virtual IPs (VIPs) that you configure in the **Load balancer address pools** section.

          1. In the **Load balancer node pool IP 1** field, enter an IPv4 address for a node in your load-balancer node pool.

          2. Click **\+ Add IP address** as needed to enter additional IP addresses.

     2. In the **Load balancer address pools** section, add one or more address pools for the MetalLB controller to choose from and assign to Services of type `LoadBalancer`. The ingress VIP, which you specify in the **Virtual IPs** section, must be in one of these pools.

        1. Enter a name for the address pool.

        2. Enter an IP address range in either CIDR notation (for example: 192.0.2.0/26) or range notation (for example: 192.0.2.64-192.0.2.72). To specify a single IP address in a pool, use /32 in the CIDR notation (for example: 192.0.2.1/32).

        3. If the ingress VIP isn't in the address range, select **\+ Add IP Address Range** and enter another address range that includes the ingress VIP.

The IP addresses in each pool cannot overlap, and must be in the same subnet as the cluster nodes.

        4. Under **Assignment of IP addresses** , select one of the following:

           * **Automatic** : Choose this option if you want the MetalLB controller to automatically assign IP addresses from the address pool to Services of type `LoadBalancer`.
           * **Manual** : Choose this option if you intend to use addresses from the pool to manually specify addresses for Services of type `LoadBalancer`.
        5. Click **Avoid buggy IP addresses** if you want the MetalLB controller to not use addresses from the pool that end in .0 or .255. This avoids the problem of buggy consumer devices mistakenly dropping traffic sent to those special IP addresses.

        6. When you're finished click **Done**.

        7. If needed, click **Add Address Pool**.

### Manual load balancer

With manual load balancing, you configure your own load-balancing solutions for control plane and data plane traffic. You must configure your control plane VIP on the external load balancer before creating a cluster. The external control plane load balancer can also be used for data plane traffic, or you can set up a separate load balancer for the data plane. For more information, see [Configure manual load balancing](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/installing/manual-lb).

  3. In the **Virtual IPs** section, enter the following:

     * **Control plane VIP** : The destination IP address to be used for traffic sent to the user cluster's Kubernetes API server. The control plane VIP must be in the same subnet as the load balancer nodes and must not be in any of the address ranges used for the load balancer address pools.

     * **Port** : The destination port used for traffic sent to the Kubernetes API server. The default is 443.

     * **Ingress VIP** : The IP address to be configured on the load balancer for the ingress proxy. Enter an address from one of the load balancer address pools.

  4. In the **Service and Pod CIDRs** section, specify the Kubernetes Service and Pod IP address ranges in CIDR notation. They must not overlap with each other, nor with any address outside the cluster that you want to reach from inside the cluster. We recommend that you use the private IP address ranges defined by [RFC 1918](https://datatracker.ietf.org/doc/html/rfc1918). The console provides the following default address ranges, but you can change them:

     * **Service CIDR** : `10.96.0.0/20` If you don't accept the default, enter a CIDR range between /24 and /12, where /12 provides the most IP addresses.

     * **Pod CIDR** : `192.168.0.0/16` If you don't accept the default, enter a CIDR range between between /18 and /8, where /8 provides the most IP addresses.

  5. In the **Advanced attributes** attributes section, optionally specify the following:

     * **Proxy URL** : The HTTP address of your proxy server. Include the port number even if it's the same as the scheme's default port, for example: `http://my-proxy.example.local:80`

     * **URLs** : A comma-separated list of IP addresses, IP address ranges, host names, and domain names that shouldn't go through the proxy server. When Google Distributed Cloud sends a request to one of these addresses, hosts, or domains, the request is sent directly.

  6. Click **Next**.




### Storage

Distributed Cloud software only provides block and file storage interfaces. They have default options, but you can customize the configurations. For more information, see [Configure local storage](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/installing/configure-local-storage).

  1. Optionally, you can configure the following:

     * **Local volume provisioner node mounts** : Specifies the configuration for local `PersistentVolumes` (PVs) backed by mounted disks. You need to format and mount these disks, which you can do before or after cluster creation.

     * **Local volume provisioner share** : Specifies the configuration for local `PersistentVolumes` backed by subdirectories in a shared file system. These subdirectories are automatically created during cluster creation.

  2. Click **Next**.




### Features

To help you monitor, troubleshoot, and operate your cluster, the following are enabled automatically and can't be disabled:

  * Cloud Logging of system services
  * Cloud Monitoring of system services
  * The [Admin Activity audit log](https://docs.cloud.google.com/logging/docs/audit#admin-activity)



### Create a node pool in the console

Your cluster must have at least one node pool for worker nodes. A node pool is a template for the groups of worker nodes created in this cluster.

In the console, you configure at least one node pool (or accept the default values) and then create the cluster. You can add additional node pools after the cluster is created. With the gcloud CLI, you create the cluster first and then add one or more node pools to the newly-created cluster.

  1. Click **default pool** in the left navigation bar.

  2. In the **Node pool defaults** section, enter the **Node pool name** or accept "default-pool" as the name.

  3. In the **Worker nodes** section, enter the IP addresses of machines for the cluster to run on.

  4. In the **Node pool metadata (optional)** section, if you want to add Kubernetes [labels](https://kubernetes.io/docs/concepts/overview/working-with-objects/labels/) and [taints](https://kubernetes.io/docs/concepts/scheduling-eviction/taint-and-toleration/) do the following:

     1. Click **\+ Add Kubernetes Labels**. Enter the **Key** and **Value** for the label. Repeat as needed.
     2. Click **\+ Add Taint**. Enter the **Key** , **Value** , and **Effect** for the taint. Repeat as needed.
  5. Click **Verify and Complete** to create the user cluster. It takes 15 minutes or more to create the user cluster. The console displays status messages as it verifies the settings and creates the cluster in your data center.

If there is a problem with the configuration, the console displays an error message that should be clear enough for you to fix the configuration issue and try again to create the cluster.




###  gcloud CLI 

You use the following command to create a user cluster:
    
    
    gcloud container bare-metal clusters create
    

After creating the cluster, you need to create at least one node pool using the following command:
    
    
    gcloud container bare-metal node-pools create
    

Most of the flags for creating the cluster and the node pool correspond to the fields in the [user cluster configuration file](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/reference/cluster-config-ref). To help you get started, you can test the complete command in the Examples section. For information about the flags, see the sections that follow the examples, or refer to the [gcloud CLI reference](https://docs.cloud.google.com/sdk/gcloud/reference/beta/container/bare-metal).

### Before you begin

The version that you select when creating a user cluster must be a version that your admin cluster supports. Additionally, the latest minor or patch versions aren't available in the GKE On-Prem API until 7 to 14 days after the release. You can run a `gcloud` command to get a list of supported cluster versions that you can install.

  1. Make sure to update components:
         
         gcloud components update
         

  2. Get the name and the fleet membership location of your admin cluster:
         
         gcloud container fleet memberships list \
           --project=FLEET_HOST_PROJECT_ID
         

Replace `FLEET_HOST_PROJECT_ID` with ID of the project that the admin cluster is registered to.

The output is similar to the following:
         
         NAME             EXTERNAL_ID                           LOCATION
         admin-cluster-1  bb7803b4-8438-4b22-859f-4559b4b29072  global
         admin-cluster-2  ee16ee2b-6ec0-49fc-9413-3c89cbc70854  global
         admin-cluster-3  fc2b7ef5-39ff-4b63-b919-04c5adc67be4  us-west1
         

The location specifies where the Fleet and Connect services run. Admin clusters created prior to 1.28 are managed by the global Fleet and Connect services. In 1.28 and later, you can specify either `global` or a Google Cloud region when you create the admin cluster. You specify the region in the `--admin-cluster-membership-location` flag in the example commands that follow.

  3. Get a list of available versions to install on the user cluster:
         
         gcloud container bare-metal clusters query-version-config \
           --admin-cluster-membership=ADMIN_CLUSTER_NAME \
           --admin-cluster-membership-project=FLEET_HOST_PROJECT_ID \
           --admin-cluster-membership-location=ADMIN_CLUSTER_REGION \
           --location=REGION
         

Replace the following:

     * `ADMIN_CLUSTER_NAME`: The name of the admin cluster.

     * `FLEET_HOST_PROJECT_ID`: The ID of the project that the admin cluster is registered to.

     * `ADMIN_CLUSTER_REGION`: The admin cluster's fleet membership region. This is either global or a Google Cloud region. Use the location for the admin cluster from the output of `gcloud container fleet memberships list`.

     * `REGION`: The Google Cloud region that you will use when you create the cluster. This is the region in which the GKE On-Prem API and the Fleet and Connect services run. Specify `us-west1` or another [supported region](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/reference/supported-regions-on-prem-api).

The output of the command is similar to the following:
    
    versions:
    - version: 1.16.2
    - version: 1.16.1
    - version: 1.16.0
    - version: 1.15.7
    - version: 1.15.6
    - version: 1.15.5
    




We suggest that you use the highest supported version to get the latest fixes and improvements.

### Examples

This section provides an example of a command that creates a cluster using the MetalLB load balancer and an example using a manual load balancer. The information that you specify varies depending on the type of load balancer you will be using. See [Overview of load balancers](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/installing/load-balance) for more information.

The examples create the cluster without any node pools. After the cluster is running, you must add a node pool before deploying workloads.

### MetalLB

This example shows how to create a user cluster with the bundled MetalLB load balancer.
    
    
    gcloud container bare-metal clusters create USER_CLUSTER_NAME \
      --project=FLEET_HOST_PROJECT_ID \
      --admin-cluster-membership=ADMIN_CLUSTER_NAME \
      --admin-cluster-membership-project=FLEET_HOST_PROJECT_ID \
      --admin-cluster-membership-location=ADMIN_CLUSTER_REGION \
      --location=REGION \
      --version=VERSION \
      --admin-users=YOUR_EMAIL_ADDRESS \
      --admin-users=ANOTHER_EMAIL_ADDRESS \
      --metal-lb-address-pools='pool=NAME,avoid-buggy-ips=True|False,manual-assign=True|False,addresses=IP_ADDRESS_RANGE_1;IP_ADDRESS_RANGE_2;...' \
      --control-plane-node-configs='node-ip=CP_IP_ADDRESS_1,labels=CP_KEY_1.1=CP_VALUE_1.1;CP_KEY_1.2=CP_VALUE_1.2;...' \
      --control-plane-vip=CONTROL_PLANE_VIP \
      --control-plane-load-balancer-port=CONTROL_PLANE_LB_PORT \
      --ingress-vip=INGRESS_VIP \
      --island-mode-service-address-cidr-blocks=SERVICE_CIDR_BLOCK \
      --island-mode-pod-address-cidr-blocks=POD_CIDR_BLOCK \
      --lvp-share-path=/mnt/localpv-share \
      --lvp-share-storage-class=local-shared \
      --lvp-node-mounts-config-path=/mnt/localpv-disk \
      --lvp-node-mounts-config-storage-class=local-disks
    

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

  * `REGION`: The Google Cloud region in which the GKE On-Prem API (`gkeonprem.googleapis.com`), Fleet service (`gkehub.googleapis.com`), and the Connect service (`gkeconnect.googleapis.com`) run. Specify `us-west1` or another [supported region](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/reference/supported-regions-on-prem-api). The region can't be changed after the cluster is created. This setting specifies the region where the following are stored: 
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

**Note:** In addition to the Kubernetes RBAC policies, you must grant some Identity and Access Management (IAM) roles to the users who aren't project owners. For details on granting the IAM roles, see [Grant required roles](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/how-to/anthos-ui#grant_required_roles). 




#### MetalLB address pools

  * `--metal-lb-address-pools`: Specify the configuration for address pools to be used by the MetalLB load balancer. The value for the flag has the following format:


    
    
    'pool=NAME,avoid-buggy-ips=True|False,manual-assign=True|False,addresses=IP_ADDRESS_RANGE_1;IP_ADDRESS_RANGE_2;...' \
    

The value has segments that start with the keywords `pool`, `avoid-buggy-ip`, `manual-assign`, and `addresses`. Separate each segment with a comma.

  * `pool`: A name of your choice for the pool.

  * `avoid-buggy-ips`: If you set this to `True`, the MetalLB controller doesn't assign IP addresses ending in .0 or .255 to Services. This avoids the problem of buggy consumer devices mistakenly dropping traffic sent to those special IP addresses. If not specified, defaults to `False`.

  * `manual-assign`: If you don't want the MetalLB controller to automatically assign IP addresses from this pool to Services, set this to `True`. Then a developer can create a Service of type `LoadBalancer` and manually specify one of the addresses from the pool. If not specified, `manual-assign` is set to `False`.

  * In the list of `addresses`: Each address must be a range either in [CIDR](https://tools.ietf.org/html/rfc4632) or hyphenated-range format. To specify a single IP address in a pool (such as for the ingress VIP), use /32 in CIDR notation (ex. 192.0.2.1/32).




Note the following syntax rules:

  * Surround the entire value in single quotes.
  * Whitespace isn't allowed.
  * Separate each IP address range with a semicolon.



You can specify more than one instance of the flag, as shown in the following example:
    
    
    --metal-lb-address-pools='pool=pool1,avoid-buggy-ips=False,manual-assign=True,addresses=192.0.2.0/26;192.0.2.64-192.0.2.72'
    --metal-lb-address-pools='pool=pool2,avoid-buggy-ips=True,manual-assign=True,addresses=10.251.133.0/24;10.251.134.80/32'
    

#### MetalLB nodes

  * Optional: `--metal-lb-load-balancer-node-configs`: By default, the load balancer runs on the same nodes as the control plane. If you need to run the load balancer on a dedicated pool of worker nodes, specify this flag for each node. All nodes in the load balancer node pool must be in the same Layer 2 subnet as the load balancer virtual IPs (VIPs).

**Important:** If you create your cluster without a dedicated load balancer node pool, you can't add it later. For clusters configured with at least one load balancer node, you can update the cluster to add more nodes to the load balancer node pool.

The value for the flag has the following format:
        
        'node-ip=LB_IP_ADDRESS_1,labels=LB_KEY_1.1=LB_VALUE_1.1;LB_KEY_1.2=LB_VALUE_1.2;...' \
        

The value has segments that start with the keywords `node-ip` and `labels`. Separate each segment with a comma.

    * `node-ip`: The IP address of a node in your load-balancer node pool. You can specify only one `node-ip` per flag. If you need to specify more than one node, include the flag again for each node.

    * `labels`: One or more key=value pairs attached to the node.

Note the following syntax rules:

    * Surround the entire value in single quotes.
    * Whitespace isn't allowed.
    * Separate each key=value pair in the `labels` segment with a semicolon.

If you specify `--metal-lb-load-balancer-node-configs`, you can optionally include the following flags:

    * `--metal-lb-load-balancer-node-labels`: Use this flag to add [labels](https://kubernetes.io/docs/concepts/overview/working-with-objects/labels/) to all nodes in the load balancer node pool. Separate the list of key=value pairs with a comma.
          
          --metal-lb-load-balancer-node-labels=KEY_1=VALUE_1,KEY_2=VALUE_2
          

    * `--metal-lb-load-balancer-node-taints`: Use this flag to add [taints](https://kubernetes.io/docs/concepts/scheduling-eviction/taint-and-toleration/) to all node in the load balancer node pool. Each taint is a key=value pair associated with an effect, which must be one of the following: `PreferNoSchedule`, `NoSchedule`, or `NoExecute`.
          
          --metal-lb-load-balancer-node-taints=KEY_1=VALUE_1:EFFECT_1,KEY_2=VALUE_2:EFFECT_2
          

The following example adds three nodes to the load balancer node pool. All the nodes are labeled with `lb-pool-key=lb-pool-value` and have the taint `dedicated=experimental:PreferNoSchedule`,
    
    --metal-lb-load-balancer-node-configs='node-ip=192.0.2.1' \
    --metal-lb-load-balancer-node-configs='node-ip=192.0.2.2,labels=key2.1=value2.1' \
    --metal-lb-load-balancer-node-configs='node-ip=192.0.2.3,labels=key3.1=value3.1;key3.2=value3.2' \
    --metal-lb-load-balancer-node-labels=lb-pool-key=lb-pool-value \
    --metal-lb-load-balancer-node-taints=dedicated=experimental:PreferNoSchedule \
    




#### Control plane nodes

  * `--control-plane-node-configs`: The IPv4 address of a control plane node. Control plane nodes run the system workload. Specify this flag for each control plane node. Typically, you have a single machine if using a minimum deployment, or three machines if using a high availability (HA) deployment. Specify an odd number of nodes to have a majority quorum for HA. You can change these addresses whenever you update or upgrade a cluster. 

The value for the flag has the following format:
        
        'node-ip=CP_IP_ADDRESS_1,labels=CP_KEY_1.1=CP_VALUE_1.1;CP_KEY_1.2=CP_VALUE_1.2;...' \

The value has segments that start with the keywords `node-ip` and `labels`. Separate each segment with a comma.

  * `node-ip`: The IP address of a control plane node. You can specify only one `node-ip` per flag. If you need to specify more than one node, include the flag again for each node. 
  * `labels`: One or more key=value pairs attached to the node. 

Note the following syntax rules:

    * Surround the entire value in single quotes.
    * Whitespace isn't allowed.
    * Separate each key=value pair in the `labels` segment with a semicolon.

Optionally, include the following flags:

  * `--control-plane-node-labels`: Use this flag to add [ labels](https://kubernetes.io/docs/concepts/overview/working-with-objects/labels/) to all control plane nodes. Separate the list of key=value pairs with a comma. 
        
        --control-plane-node-labels=KEY_1=VALUE_1,KEY_2=VALUE_2

  * `--control-plane-node-taints`: Use this flag to add [ taints](https://kubernetes.io/docs/concepts/scheduling-eviction/taint-and-toleration/) to all control plane nodes. Each taint is a key=value pair associated with an effect, which must be one of the following: `PreferNoSchedule`, `NoSchedule`, or `NoExecute`. 

The following example adds three nodes to the control plane nodes. All the nodes are labeled with `cp-node-pool-key=cp-node-pool-value` and have the taint `dedicated=experimental:PreferNoSchedule`.
        
        --control-plane-node-configs='node-ip=192.0.2.1' \
          --control-plane-node-configs='node-ip=192.0.2.2,labels=key2.1=value2.1' \
          --control-planer-node-configs='node-ip=192.0.2.3,labels=key3.1=value3.1;key3.2=value3.2' \
          --control-plane-node-labels=cp-node-pool-key=cp-node-pool-value \
          --control-plane-node-taints=dedicated=experimental:PreferNoSchedule \




#### Virtual IPs

  * `CONTROL_PLANE_VIP`: The IP address that you have chosen to configure on the load balancer for the Kubernetes API server of the user cluster. 

Example: `--control-plane-vip=203.0.113.3`

  * `CONTROL_PLANE_LB_PORT`: The port that the load balancer serves the Kubernetes API server on. 

Example: `-control-plane-load-balancer-port=443`

  * `INGRESS_VIP`: The IP address that you have chosen to configure on the load balancer for the ingress proxy. 

Example: `--ingress-vip=10.251.134.80`

The IP address for the ingress VIP must be in one of the MetalLB address pools. 




#### Service and Pod CIDRs

  * `SERVICE_CIDR_BLOCK`: A range of IP addresses, in CIDR format, to be used for Services in your cluster. The CIDR range must be between /24 and /12, where /12 provides the most IP addresses. 

Example: `--island-mode-service-address-cidr-blocks=10.96.0.0/20`

  * `POD_CIDR_BLOCK`: A range of IP addresses, in CIDR format, to be used for Pods in your cluster. The CIDR range must be between /18 and /8, where /8 provides the most IP addresses. 

Example: `--island-mode-pod-address-cidr-blocks=192.168.0.0/16`




#### Storage

  1. `--lvp-share-path`: This is the host machine path where subdirectories can be created. A local PersistentVolume (PV) is created for each subdirectory. 
  2. `--lvp-share-storage-class`: This is the StorageClass to use to create persistent volumes. The StorageClass is created during cluster creation. 
  3. `--lvp-node-mounts-config-path`: This is the host machine path where mounted disks can be discovered. A local PersistentVolume (PV) is created for each mount. 
  4. `--lvp-node-mounts-config-storage`: The storage class that PVs are created with during cluster creation. 



For more information about storage, see [Configure local storage](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/installing/configure-local-storage). 

### Manual

With manual load balancing, you configure your own load-balancing solutions for control plane and data plane traffic. You must configure your control plane VIP on the external load balancer before creating a cluster. The external control plane load balancer can also be used for data plane traffic, or you can set up a separate load balancer for the data plane. For more information, see [Configure manual load balancing](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/installing/manual-lb).

Be sure to scroll over if needed to fill in the `ADMIN_CLUSTER_NAME` placeholder for the `--admin-cluster-membership` flag.
    
    
    gcloud container bare-metal clusters create USER_CLUSTER_NAME \
      --project=FLEET_HOST_PROJECT_ID \
      --admin-cluster-membership=ADMIN_CLUSTER_NAME \
      --admin-cluster-membership-project=FLEET_HOST_PROJECT_ID \
      --admin-cluster-membership-location=ADMIN_CLUSTER_REGION \
      --location=REGION \
      --version=VERSION \
      --admin-users=YOUR_EMAIL_ADDRESS \
      --admin-users=ANOTHER_EMAIL_ADDRESS \
      --enable-manual-lb \
      --control-plane-node-configs='node-ip=CP_IP_ADDRESS_1,labels=CP_KEY_1.1=CP_VALUE_1.1;CP_KEY_1.2=CP_VALUE_1.2;...' \
      --control-plane-vip=CONTROL_PLANE_VIP \
      --control-plane-load-balancer-port=CONTROL_PLANE_LB_PORT \
      --ingress-vip=INGRESS_VIP \
      --island-mode-service-address-cidr-blocks=SERVICE_CIDR_BLOCK \
      --island-mode-pod-address-cidr-blocks=POD_CIDR_BLOCK \
      --lvp-share-path=/mnt/localpv-share \
      --lvp-share-storage-class=local-shared \
      --lvp-node-mounts-config-path=/mnt/localpv-disk \
      --lvp-node-mounts-config-storage-class=local-disks
    

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

  * `REGION`: The Google Cloud region in which the GKE On-Prem API (`gkeonprem.googleapis.com`), Fleet service (`gkehub.googleapis.com`), and the Connect service (`gkeconnect.googleapis.com`) run. Specify `us-west1` or another [supported region](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/reference/supported-regions-on-prem-api). The region can't be changed after the cluster is created. This setting specifies the region where the following are stored: 
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

**Note:** In addition to the Kubernetes RBAC policies, you must grant some Identity and Access Management (IAM) roles to the users who aren't project owners. For details on granting the IAM roles, see [Grant required roles](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/how-to/anthos-ui#grant_required_roles). 




#### Control plane nodes

  * `--control-plane-node-configs`: The IPv4 address of a control plane node. Control plane nodes run the system workload. Specify this flag for each control plane node. Typically, you have a single machine if using a minimum deployment, or three machines if using a high availability (HA) deployment. Specify an odd number of nodes to have a majority quorum for HA. You can change these addresses whenever you update or upgrade a cluster. 

The value for the flag has the following format:
        
        'node-ip=CP_IP_ADDRESS_1,labels=CP_KEY_1.1=CP_VALUE_1.1;CP_KEY_1.2=CP_VALUE_1.2;...' \

The value has segments that start with the keywords `node-ip` and `labels`. Separate each segment with a comma.

  * `node-ip`: The IP address of a control plane node. You can specify only one `node-ip` per flag. If you need to specify more than one node, include the flag again for each node. 
  * `labels`: One or more key=value pairs attached to the node. 

Note the following syntax rules:

    * Surround the entire value in single quotes.
    * Whitespace isn't allowed.
    * Separate each key=value pair in the `labels` segment with a semicolon.

Optionally, include the following flags:

  * `--control-plane-node-labels`: Use this flag to add [ labels](https://kubernetes.io/docs/concepts/overview/working-with-objects/labels/) to all control plane nodes. Separate the list of key=value pairs with a comma. 
        
        --control-plane-node-labels=KEY_1=VALUE_1,KEY_2=VALUE_2

  * `--control-plane-node-taints`: Use this flag to add [ taints](https://kubernetes.io/docs/concepts/scheduling-eviction/taint-and-toleration/) to all control plane nodes. Each taint is a key=value pair associated with an effect, which must be one of the following: `PreferNoSchedule`, `NoSchedule`, or `NoExecute`. 

The following example adds three nodes to the control plane nodes. All the nodes are labeled with `cp-node-pool-key=cp-node-pool-value` and have the taint `dedicated=experimental:PreferNoSchedule`.
        
        --control-plane-node-configs='node-ip=192.0.2.1' \
          --control-plane-node-configs='node-ip=192.0.2.2,labels=key2.1=value2.1' \
          --control-planer-node-configs='node-ip=192.0.2.3,labels=key3.1=value3.1;key3.2=value3.2' \
          --control-plane-node-labels=cp-node-pool-key=cp-node-pool-value \
          --control-plane-node-taints=dedicated=experimental:PreferNoSchedule \




#### Virtual IPs

  * `CONTROL_PLANE_VIP`: The IP address that you have chosen to configure on the load balancer for the Kubernetes API server of the user cluster. 

Example: `--control-plane-vip=203.0.113.3`

  * `CONTROL_PLANE_LB_PORT`: The port that the load balancer serves the Kubernetes API server on. 

Example: `-control-plane-load-balancer-port=443`

  * `INGRESS_VIP`: The IP address that you have chosen to configure on the load balancer for the ingress proxy. 

Example: `--ingress-vip=10.251.134.80`

The IP address for the ingress VIP must be in one of the MetalLB address pools. 




#### Service and Pod CIDRs

  * `SERVICE_CIDR_BLOCK`: A range of IP addresses, in CIDR format, to be used for Services in your cluster. The CIDR range must be between /24 and /12, where /12 provides the most IP addresses. 

Example: `--island-mode-service-address-cidr-blocks=10.96.0.0/20`

  * `POD_CIDR_BLOCK`: A range of IP addresses, in CIDR format, to be used for Pods in your cluster. The CIDR range must be between /18 and /8, where /8 provides the most IP addresses. 

Example: `--island-mode-pod-address-cidr-blocks=192.168.0.0/16`




#### Storage

  1. `--lvp-share-path`: This is the host machine path where subdirectories can be created. A local PersistentVolume (PV) is created for each subdirectory. 
  2. `--lvp-share-storage-class`: This is the StorageClass to use to create persistent volumes. The StorageClass is created during cluster creation. 
  3. `--lvp-node-mounts-config-path`: This is the host machine path where mounted disks can be discovered. A local PersistentVolume (PV) is created for each mount. 
  4. `--lvp-node-mounts-config-storage`: The storage class that PVs are created with during cluster creation. 



For more information about storage, see [Configure local storage](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/installing/configure-local-storage). 

Before running the `gcloud` command to create the cluster, you might want to include `--validate-only` to validate the configuration that you specified in the flags to the `gcloud` command. When you are ready to create the cluster, remove this flag and run the command.

The output from the command is similar to the following:
    
    
    Waiting for operation [projects/example-project-12345/locations/us-west1/operations/operation-1679543737105-5f7893fd5bae9-942b3f97-75e59179] to complete.
    

In the example output, the string `operation-1679543737105-5f7893fd5bae9-942b3f97-75e59179` is the `OPERATION_ID` of the long-running operation. You can find out the status of the operation with the following command:
    
    
    gcloud container bare-metal operations describe OPERATION_ID \
      --project=FLEET_HOST_PROJECT_ID \
      --location=REGION
    

It takes 15 minutes or more to create the user cluster. You can view the cluster in the Google Cloud console on the [**GKE clusters**](https://console.cloud.google.com/kubernetes/list/overview) page.

For a complete list of the flags and their descriptions, see the [gcloud CLI reference](https://docs.cloud.google.com/sdk/gcloud/reference/container/bare-metal/clusters/create).

### Create a node pool

After the cluster is created, you need to create at least one node pool before deploying workloads. A node pool is a template for the groups of worker nodes created in this cluster. With the gcloud CLI, you create the cluster first and then add one or more node pools to the newly-created cluster.
    
    
    gcloud container bare-metal node-pools create NODE_POOL_NAME \
      --cluster=USER_CLUSTER_NAME \
      --project=FLEET_HOST_PROJECT_ID \
      --location=REGION \
      --node-configs='node-ip=NP_IP_ADDRESS_1,labels=NP_KEY_1.1=NP_VALUE_1.1;NP_KEY_1.2=NP_VALUE_1.2;...'

Replace the following:

  * `NODE_POOL_NAME`: A name of your choice for the node pool. The name must:

    * contain at most 40 characters
    * contain only lowercase alphanumeric characters or a hyphen (`-`)
    * start with an alphabetic character
    * end with an alphanumeric character
  * `USER_CLUSTER_NAME`: The name of the newly-created user cluster.

  * `FLEET_HOST_PROJECT_ID`: The ID of the project that the cluster is registered to.

  * `REGION`: The Google Cloud region that you specified when you created the cluster.

  * `--node-configs`: The IPv4 address of a worker node machine. Specify this flag for each node. The value for the flag has the following format:
        
        'node-ip=NP_IP_ADDRESS_1,labels=NP_KEY_1.1=NP_VALUE_1.1;NP_KEY_1.2=NP_VALUE_1.2;...' \
        

The value has segments that start with the keywords `node-ip` and `labels`. Separate each segment with a comma.

    * `node-ip`: The IP address of a worker node. You can specify only one `node-ip` per flag. Add this flag again for each node in the node pool.

    * `labels`: One or more key=value pairs attached to the node.

Note the following syntax rules:

    * Surround the entire value in single quotes.
    * Whitespace isn't allowed.
    * Separate each key=value pair in the `labels` segment with a semicolon.

Optionally, you can specify the following:

    * `--node-labels=KEY=VALUE,...`: A comma-separated list of [Kubernetes labels](https://kubernetes.io/docs/concepts/overview/working-with-objects/labels/) (key=value pairs) applied to each node in the pool.

    * `--node-taints=KEY=VALUE:EFFECT,...` A comma-separated list of [Kubernetes taints](https://kubernetes.io/docs/concepts/scheduling-eviction/taint-and-toleration/) applied to each node in the pool. Taints are key=value pairs associated with an effect. Taints are used with tolerations for Pod scheduling. Specify one of the following for `EFFECT`: `NoSchedule`, `PreferNoSchedule`, `NoExecute`.




The following example creates a node pool called `default-pool` on `user-cluster-`, and adds two nodes to the node pool. All both nodes are labeled with `node-pool-key=node-pool-value` and have the taint `dedicated=experimental:PreferNoSchedule`,
    
    
    gcloud container bare-metal node-pools create default-pool \
      --cluster=user-cluster-1  \
      --project=example-project-12345 \
      --location=us-west1 \
      --node-configs='node-ip=10.200.0.10' \
      --node-configs='node-ip=10.200.0.11,labels=key2.1=value2.1' \
      --node-labels=node-pool-key=node-pool-value \
      --node-taints=dedicated=experimental:PreferNoSchedule
    

For more information, see the [gcloud CLI reference](https://docs.cloud.google.com/sdk/gcloud/reference/container/bare-metal/node-pools/create).

### Terraform

### Before you begin

The Distributed Cloud software only for bare metal version that you select when creating a user cluster must be a version that your admin cluster supports. Additionally, the latest minor or patch versions aren't available in the GKE On-Prem API until 7 to 14 days after the release. You can run a `gcloud` command to get a list of supported versions that you can use to install the user cluster.

  1. Make sure to update components:
         
         gcloud components update
         

  2. Get the name and the fleet membership location of your admin cluster:
         
         gcloud container fleet memberships list \
           --project=FLEET_HOST_PROJECT_ID
         

Replace `FLEET_HOST_PROJECT_ID` with ID of the project that the admin cluster is registered to.

The output is similar to the following:
         
         NAME             EXTERNAL_ID                           LOCATION
         admin-cluster-1  bb7803b4-8438-4b22-859f-4559b4b29072  global
         admin-cluster-2  ee16ee2b-6ec0-49fc-9413-3c89cbc70854  global
         admin-cluster-3  fc2b7ef5-39ff-4b63-b919-04c5adc67be4  us-west1
         

The location specifies where the Fleet and Connect services run. Admin clusters created prior to 1.28 are managed by the global Fleet and Connect services. In 1.28 and later, you can specify either `global` or a Google Cloud region when you create the admin cluster. You specify the region in the `--admin-cluster-membership-location` flag in the example commands that follow.

  3. Get a list of available versions to install on the user cluster:
         
         gcloud container bare-metal clusters query-version-config \
           --admin-cluster-membership=ADMIN_CLUSTER_NAME \
           --admin-cluster-membership-project=FLEET_HOST_PROJECT_ID \
           --admin-cluster-membership-location=ADMIN_CLUSTER_REGION \
           --location=REGION
         

Replace the following:

     * `ADMIN_CLUSTER_NAME`: The name of the admin cluster.

     * `FLEET_HOST_PROJECT_ID`: The ID of the project that the admin cluster is registered to.

     * `ADMIN_CLUSTER_REGION`: The admin cluster's fleet membership region. This is either global or a Google Cloud region. Use the location for the admin cluster from the output of `gcloud container fleet memberships list`.

     * `REGION`: The Google Cloud region that you will use when you create the cluster. This is the region in which the GKE On-Prem API and the Fleet and Connect services run. Specify `us-west1` or another [supported region](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/reference/supported-regions-on-prem-api).

The output of the command is similar to the following:
    
    versions:
    - version: 1.16.2
    - version: 1.16.1
    - version: 1.16.0
    - version: 1.15.7
    - version: 1.15.6
    - version: 1.15.5
    




We suggest that you use the highest supported version to get the latest fixes and improvements.

## Example

You can use the following basic configuration sample to create a user cluster with bundled MetalLB load balancer. For more information, see the [`google_gkeonprem_bare_metal_cluster` reference documentation](https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/gkeonprem_bare_metal_cluster).

### Set variables in `terraform.tfvars`

The sample provides an example variables file to pass in to `main.tf`, which shows how to configure the bundled MetalLB load balancer.

  1. Clone the `anthos-samples` repository and change to the directory where the Terraform sample is located:
         
         git clone https://github.com/GoogleCloudPlatform/anthos-samples
         cd anthos-samples/anthos-onprem-terraform/abm_user_cluster_metallb
         

The sample provides an example variables file to pass in to `main.tf`.

  2. Make a copy of the `terraform.tfvars.sample` file:
         
         cp terraform.tfvars.sample terraform.tfvars
         

  3. Modify the parameters values in `terraform.tfvars` and save the file.
         
         project_id          = "PROJECT_ID"
         region              = "ON_PREM_API_REGION"
         admin_cluster_name  = "ADMIN_CLUSTER_NAME"
         bare_metal_version  = "VERSION"
         admin_user_emails   = ["YOUR_EMAIL_ADDRESS", "ADMIN_2_EMAIL_ADDRESS"]
         cluster_name        = "abm-user-cluster-metallb"
         control_plane_ips   = ["10.200.0.4"]
         worker_node_ips     = ["10.200.0.5", "10.200.0.6"]
         control_plane_vip   = "10.200.0.50"
         ingress_vip         = "10.200.0.51"
         lb_address_pools    = [
             { name = "lbpool_1", addresses = ["10.200.0.51-10.200.0.70"] }
         ]
         

The following list describes the variables:

     * `project_id`: The ID of the project that you want to create the cluster in. The specified project is also used as the fleet host project. This must be the same project that the admin cluster is registered to. After the user cluster is created, it is automatically registered to the selected project's fleet. The fleet host project can't be changed after the cluster is created.

     * `region`: The Google Cloud region in which the GKE On-Prem API (`gkeonprem.googleapis.com`), Fleet service (`gkehub.googleapis.com`), and the Connect service (`gkeconnect.googleapis.com`) run. Specify `us-west1` or another [supported region](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/reference/supported-regions-on-prem-api).

**Important:** If you plan to install Cloud Service Mesh, you must install version 1.19.3 or later. This is required because the Fleet and Connect services run in a region.
     * `admin_cluster_name`: The name of the admin cluster that manages the user cluster. The example assumes that the admin cluster uses `global` as the region. If you have a regional admin cluster:

       1. Open `main.tf` in a text editor.

       2. Search for `admin_cluster_membership`, which looks like the following:
              
              admin_cluster_membership = "projects/${var.project_id}/locations/global/memberships/${var.admin_cluster_name}"

       3. Change `global` to the region that the admin cluster uses and save the file.

     * `bare_metal_version`: The Google Distributed Cloud version for your user cluster. Specify either the same version as the admin cluster, or a version that is no more than one minor version _lower_ than the admin cluster.

     * `admin_user_emails`: A list of email addresses of the users to be granted administrative privileges on the cluster. Be sure to add your email address if you intend to administer the cluster.

When the cluster is created, the GKE On-Prem API applies the Kubernetes role-based access control (RBAC) policies to the cluster to grant the admin users the Kubernetes `clusterrole/cluster-admin` role, which provides full access to every resource in the cluster in all namespaces. This also lets users log on to the console using their Google identity.

     * `cluster_name`: A name of your choice for your user cluster. The name can't be changed after the cluster is created. The name must:

       * contain at most 40 characters
       * contain only lowercase alphanumeric characters or a hyphen (`-`)
       * start with an alphabetic character
       * end with an alphanumeric character
     * `control_plane_ips`: A list of one or more IPv4 addresses for the control plane nodes. Control plane nodes run the system workload. Typically, you have a single machine if using a minimum deployment, or three machines if using a high availability (HA) deployment. Specify an odd number of nodes to have a majority quorum for HA. You can change these addresses whenever you update or upgrade a cluster.

     * `worker_node_ips`: A list of one or more IPv4 addresses for the worker node machines.

     * `control_plane_vip`: The virtual IP address (VIP) that you have chosen to configure on the load balancer for the Kubernetes API server of the user cluster.

     * `ingress_vip`: The IP address that you have chosen to configure on the load balancer for the ingress proxy.

     * `lb_address_pools`: A list of maps that define the address pools to be used by the MetalLB load balancer. The ingress VIP must be in one of these pools.

  4. Save the changes in `terraform.tfvars`.

  5. Initialize and create the Terraform plan:
         
         terraform init
         

Terraform installs any needed libraries, such as the Google Cloud provider. 

  6. Review the configuration and make changes if needed:
         
         terraform plan
         

  7. Apply the Terraform plan to create the user cluster:
         
         terraform apply
         

It takes 15 minutes or more to create the user cluster. You can view the cluster in the Google Cloud console on the [**GKE clusters**](https://console.cloud.google.com/kubernetes/list/overview) page.




## Connect to the user cluster

When you create a user cluster in the console, the cluster is configured with the Kubernetes role-based access control (RBAC) policies so that you can log in to the cluster using your Google Cloud identity. When you create a user cluster with the gcloud CLI, by default you are granted these RBAC policies if you **don't** include the `--admin-users` flag. If you include `--admin-users` to designate another user as an administrator, you override the default and you need to include both your email address and the email address of the other administrator. For more information about the required IAM and RBAC policies, see [Set up Google identity authentication](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/how-to/anthos-ui#set_up_google_identity_authentication).

All clusters have a canonical endpoint. The endpoint exposes the Kubernetes API server that `kubectl` and other services use to communicate with your cluster control plane over TCP port 443. This endpoint is not accessible on the public internet. If you have access to your cluster's private endpoint through your VPC, you can connect directly to the private endpoint and generate a `kubeconfig` file directly. Otherwise, you can use [connect gateway](https://docs.cloud.google.com/kubernetes-engine/enterprise/multicluster-management/gateway).

To access the user cluster from the command line, you need a `kubeconfig` file. There are two ways to get a `kubeconfig` file:

  * Use the connect gateway to access the cluster from a computer that has the Google Cloud CLI installed on it. In this case, `kubectl` uses the Connect gateway's `kubeconfig`, which securely forwards the traffic to the private endpoint on your behalf.

  * For direct access to private endpoints, create a `kubeconfig` file on your admin workstation and manage the cluster from your admin workstation.




Be sure to wait until the Google Cloud console indicates that user cluster status is healthy.

###  Connect gateway 

  1. Either [initialize](https://docs.cloud.google.com/sdk/docs/install-sdk#initializing_the) the gcloud CLI for use with the fleet host project, or run the following commands to log in with your Google Account, set your fleet host project as the default, and update components:
         
         gcloud auth login
         gcloud config set project PROJECT_ID
         gcloud components update
         

  2. Fetch the cluster credentials used to interact with connect gateway. In the following command, replace`MEMBERSHIP_NAME` with your cluster's name. For Distributed Cloud software only for bare metal, the membership name is the same as the cluster name.
         
         gcloud container fleet memberships get-credentials MEMBERSHIP_NAME
         

This command returns a special **connect gateway-specific`kubeconfig`** that lets you connect to the cluster through the gateway.




After you have the necessary credentials, you can run commands using `kubectl` as you normally would for any Kubernetes cluster, and you don't need to specify the name of the `kubeconfig` file, for example:
    
    
    kubectl get namespaces
    

### Admin workstation

Use the `bmctl get credentials` command to retrieve a `kubeconfig` file for the newly created user cluster.
    
    
    bmctl get credentials --cluster CLUSTER_NAME --admin-kubeconfig ADMIN_KUBECONFIG_PATH
    

Replace the following:

  * CLUSTER_NAME: the name of the target user cluster.

  * ADMIN_KUBECONFIG_PATH: the path to the admin cluster `kubeconfig` file.




A `kubeconfig` with the user cluster's credentials are written to a file, `bmctl-workspace/CLUSTER_NAME/CLUSTER_NAME-TIMESTAMP-kubeconfig`. The TIMESTAMP in the filename indicates the date and time the file was created.

Because this file contains authentication credentials for your cluster, you should store it in a secure location with restricted access.

## What's next

  * [Secure your containers using SELinux](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/installing/configure-selinux)
  * [Manage clusters from the Google Cloud console](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/how-to/anthos-ui)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-14 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-14 UTC."],[],[]] 
