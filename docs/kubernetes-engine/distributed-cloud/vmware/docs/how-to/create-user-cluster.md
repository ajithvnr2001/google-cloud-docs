---
url: https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/create-user-cluster/
title: Create a user cluster \u00a0|\u00a0 Google Distributed Cloud software only for VMware \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T10:13:43.193410+00:00
---

# Create a user cluster  |  Google Distributed Cloud software only for VMware  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/create-user-cluster/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Google Distributed Cloud ](https://docs.cloud.google.com/distributed-cloud)
  * [ Documentation ](https://docs.cloud.google.com/kubernetes-engine/enterprise/clusters/docs)
  * [ GDC for VMware ](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs)
  * [ Guides ](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/overview)



Send feedback 

#  Create a user cluster Stay organized with collections  Save and categorize content based on your preferences. 

In Google Distributed Cloud, your workloads run on one or more user clusters. This document shows how to create a user cluster. If you want to use topology domains, see [Create a user cluster for use with topology domains](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/create-user-cluster-topology-domains).

This page is for Admins, Architects, and Operators who set up, monitor, and manage the tech infrastructure. To learn more about common roles and example tasks that we reference in Google Cloud content, see [Common GKE user roles and tasks](https://docs.cloud.google.com/kubernetes-engine/enterprise/docs/concepts/roles-tasks).

In version 1.33 and higher, all new clusters are created as [advanced clusters](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/concepts/advanced-clusters). Be sure to review [Differences when running advanced clusters](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/concepts/advanced-clusters#adv-clusters-feature-support).

There are several tools that you can use to create a user cluster:

  * `gkectl`
  * Google Cloud console
  * `Google Cloud CLI`
  * Terraform



Three of these tools (the console, the gcloud CLI, and Terraform) are clients of the [GKE On-Prem API](https://docs.cloud.google.com/anthos/clusters/docs/on-prem-api/reference/rest).

For guidance on which tool you might like to use, see [Choose a tool to manage cluster lifecycle](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/cluster-lifecycle-management-tools).

## Before you begin

  * If you plan to use `gkectl` to create the user cluster, make sure you have set up and can sign in to your admin workstation as described in [Create an admin workstation](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/create-admin-workstation).

  * Make sure that your admin workstation has the required version of `gkectl`. Typically, you use the same version of `gkectl` as the version that will be used when you create the cluster. You specify the cluster version in the `gkeOnPremVersion` field in the cluster configuration file. The following version rules are enforced during cluster creation:

    * The `gkectl` minor version can't be lower than the minor version for the cluster. For example, creating a 1.30 cluster using `gkectl` version 1.29 isn't allowed. Patch versions don't matter. For example, you can use `gkectl` version 1.29.0-gke.1456 to create a cluster with a higher patch version, such as 1.29.1000-gke.94.

    * The `gkectl` minor version can't be more than two minor versions higher than the cluster version. For example, if you are creating a 1.28 cluster, the `gkectl` version can be 1.29 or 1.30. But you can't use `gkectl` version 1.31 because that is three minor versions higher than the cluster version.

If needed, see [Download `gkectl`](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/downloads#download_gkectl) to get a supported version of `gkectl`.

  * If you haven't already done so, set up your Google Cloud resources as described in these documents:

    * [Install the Google Cloud CLI](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/cloud-sdk)
    * [Create Cloud projects](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/multiple-gcp-projects)
    * [Create service accounts](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/service-accounts)

As you set up your [fleet host project](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/multiple-gcp-projects#fleet_host_project), keep in mind your choice of tool, because if you have chosen one of the GKE On-Prem API clients, there are additional APIs that you must enable. For the list of APIs, see [Enable APIs in your fleet host project](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/multiple-gcp-projects#enable_apis_in_your_fleet_host_project).

  * Before you create a user cluster, you must have an admin cluster to manage the user cluster. If you haven't already done so, create an [admin workstation](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/create-admin-workstation) and an [admin cluster](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/create-admin-cluster).

  * Determine the version of the user cluster that you want to install. When you create a user cluster, you typically install the version that matches the version of the admin cluster. If you want to install a different version on a user cluster, see [Version rules](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/upgrade-overview#verson_rules).

  * If you plan to install version 1.30 or a higher version, Controlplane V2 is required. Even if you are installing 1.29 or lower, we recommend that you enable Controlplane V2. When Controlplane V2 is enabled, the control plane for the user cluster runs on one or more nodes in the user cluster itself. The alternative is to create a user cluster that uses _kubeception_. In the kubeception case, the control plane for the user cluster runs on one or more nodes in the admin cluster.

  * Review the [IP addresses planning document](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/plan-ip-addresses), and ensure that you have enough IP addresses available.

  * Review the [load balancing overview](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/setup-load-balance) and revisit your decision about the kind of load balancer you want to use. You can use the bundled MetalLB load balancer, or you can manually configure a load balancer of your choice. For manual load balancing, you must set up the load balancer before you create your user cluster.

  * Think about how many [node pools](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/managing-node-pools) you need and which operating system you want to run in each of your pools.

  * Think about whether you want to use separate [vSphere clusters](https://techdocs.broadcom.com/us/en/vmware-cis/vsphere/vsphere/9-1/vcenter-and-host-management.html) for your admin cluster and user clusters, and whether you want to use separate [data centers](https://techdocs.broadcom.com/us/en/vmware-cis/vsphere/vsphere/9-1/vcenter-and-host-management.html). Also think about whether you want to use separate instances of [vCenter Server](https://www.vmware.com/products/vcenter.html).

  * In version 1.29 and higher, server-side preflight checks are enabled by default. Server-side preflight checks require additional firewall rules. In [Firewall rules for admin clusters](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/firewall-rules#firewall_rules_for_admin_clusters), search for "Preflight checks" and make sure all required firewall rules are configured.

With server-side preflight checks, when you create a user cluster using `gkectl`, the preflight checks are run on the admin cluster instead of locally on the admin workstation. Server-side preflight checks are also run if you use the Google Cloud console, the Google Cloud CLI, or Terraform to create a user cluster.




## Create a user cluster with the tool of your choice

This section provides steps for creating a user cluster using `gkectl`, the console, the gcloud CLI, and Terraform.

### gkectl

## Procedure overview

These are the primary steps involved in using `gkectl` to create a user cluster:

  1. Fill in your configuration files
    Specify the details for your new cluster by completing a user cluster configuration file, a credentials configuration file, and possibly an IP block file.
  2. (Optional) Import OS images to vSphere, and push container images to the private registry if applicable.
    Run `gkectl prepare`.
  3. Create a user cluster
    Run `gkectl create cluster` to create a cluster as specified in your configuration file.
  4. Verify that your user cluster is running
    Use `kubectl` to view your cluster nodes.



At the end of this procedure, you will have a running user cluster where you can deploy your workloads.

If you use VPC Service Controls, you might see errors when you run some `gkectl` commands, such as `"Validation Category: GCP - [UNKNOWN] GCP service: [Stackdriver] could not get GCP services"`. To avoid these errors, add the `--skip-validation-gcp` parameter to your commands.

## Fill in your configuration files

If you used `gkeadm` to create your admin workstation, then `gkeadm` generated a template for your user cluster configuration file named `user-cluster.yaml`. Additionally, `gkeadm` filled in some of the fields for you.

If you didn't use `gkeadm` to create your admin workstation, you can use `gkectl` to generate a template for your user cluster configuration file.

To generate a template for your user cluster configuration file:
    
    
    gkectl create-config cluster --config=OUTPUT_FILENAME --gke-on-prem-version=VERSION
    

Replace the following:

`OUTPUT_FILENAME`: a path of your choice for the generated template. If you omit this flag, `gkectl` names the file `user-cluster.yaml` and puts it in the current directory.

`VERSION`: the desired version number. For example: `gkectl create-config cluster --gke-on-prem-version=1.36.200-gke.118`.

Familiarize yourself with the configuration file by scanning the [user cluster configuration file](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/user-cluster-configuration-file-latest) document. You might want to keep this document open in a separate tab or window, because you will refer to it as you complete the following steps.

### `name`

Set the [`name`](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/user-cluster-configuration-file-latest#name-field) field to a name of your choice for the user cluster.

### `gkeOnPremVersion`

This field is already filled in for you. It specifies the version of Google Distributed Cloud. For example, `1.36.200-gke.118`.

### `enableAdvancedCluster`

In version 1.31, if you want to enable the advanced cluster feature, set [`enableAdvancedCluster`](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/user-cluster-configuration-file-latest#enable-advanced-cluster-field) to `true`. This field must be set to `true` if the admin cluster has [advanced cluster enabled](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/admin-cluster-configuration-file-latest#enable-advanced-cluster-field).

Note the following differences between versions:

  * In version 1.31, the advanced cluster feature is in preview:

    * You can enable advanced cluster at cluster creation time for new 1.31 clusters only.

    * After advanced cluster is enabled, you won't be able to upgrade the cluster to 1.32. Only enable advanced cluster in a test environment.

  * In version 1.32, the advanced cluster feature is GA.

    * By default, user clusters are created as advanced clusters. You have to explicitly set `enableAdvancedCluster` to `false` if you want to create a non-advanced cluster.

    * For clusters that have the advanced clusters feature enabled, cluster upgrades are supported.

  * In version 1.33 and higher, all clusters are created as advanced clusters. If you set `enableAdvancedCluster` to `false`, cluster creation fails.




### `enableControlplaneV2`

To create a user cluster that has Controlplane V2 enabled, set [`enableControlplaneV2`](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/user-cluster-configuration-file-latest#enablecontrolplanev2-field) to `true`.

If you [enable advanced cluster](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/user-cluster-configuration-file-latest#enable-advanced-cluster-field), then you must set `enableControlplaneV2` to `true`.

When Controlplane V2 is enabled, the control plane for the user cluster runs on nodes in the user cluster itself. We strongly recommend that you enable Controlplane V2.

#### kubeception

If you set this field to `false`, the cluster will use [kubeception](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/plan-ip-addresses-kubeception). With kubeception, the control plane for the user cluster runs on nodes in the admin cluster.

For a kubeception cluster:

  * Set `enableControlplaneV2` to `false`.

  * Don't fill in the `controlPlaneIPBlock` section.

  * Specify IP addresses for the control-plane nodes of the user cluster in the [IP block file](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/ip-block-file) of the admin cluster.




### `enableDataplaneV2`

Set [enableDataplaneV2](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/user-cluster-configuration-file-latest#enabledataplanev2-field) to `true`.

### `vCenter`

The values you set in the `vCenter` section of your [admin cluster configuration file](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/admin-cluster-configuration-file-latest) are global. That is, they apply to your admin cluster and its associated user clusters.

For each user cluster that you create, you have the option of overriding some of the global `vCenter` values.

To override any of the global `vCenter` values, fill in the relevant fields in the [`vCenter`](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/user-cluster-configuration-file-latest#vcenter-section) section of your user cluster configuration file.

In particular, you might want to use separate vSphere clusters for your admin cluster and user clusters, and you might want to use separate data centers for your admin cluster and user clusters.

#### Using one data center and one vSphere cluster

The default option is to use one data center and one vSphere cluster for the admin cluster and the user cluster. For this option, don't set any `vCenter` values in the user cluster configuration file. The `vCenter` values will be inherited from the admin cluster.

#### Using separate vSphere clusters

If you want to create a user cluster that is in its own vSphere cluster, specify a value for `vCenter.cluster` in the user cluster configuration file.

If your admin cluster and user cluster are in separate vSphere clusters, they can be in the same data center or different data centers.

#### Using separate vSphere data centers

The user cluster and admin cluster can be in different [data centers](https://techdocs.broadcom.com/us/en/vmware-cis/vsphere/vsphere/9-1/vcenter-and-host-management.html). In that case, they are also in separate vSphere clusters.

If you specify `vCenter.datacenter` in the user cluster configuration file, then you must also specify:

  * `vCenter.networkName`
  * Either `vCenter.datastore` or `vCenter.storagePolicyName`
  * Either `vCenter.cluster` or `vCenter.resourcePool`



#### Using separate vCenter accounts

A user cluster can use a different vCenter account, with different `vCenter.credentials`, from the admin cluster. The vCenter account for the admin cluster needs access to the admin cluster data center, while the vCenter account for the user cluster only needs access to the user cluster data center.

#### Using separate instances of vCenter Server

In certain situations, it makes sense to create a user cluster that uses its own instance of vCenter Server. That is, the admin cluster and an associated user cluster use different instances of vCenter Server.

For example, in an edge location, you might want to have a physical machine running vCenter Server and one or more physical machines running ESXi. You could then use your local instance of vCenter Server to create a vSphere object hierarchy, including data centers, clusters, resource pools, datastores, and folders.

Fill in the entire [`vCenter`](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/user-cluster-configuration-file-latest#vcenter-section) section of your user cluster configuration file. In particular, specify a value for `vCenter.address` that is different from the vCenter Server address you specified in the admin cluster configuration file. For example:
    
    
    vCenter:
      address: "vc-edge.example"
      datacenter: "vc-edge"
      cluster: "vc-edge-workloads"
      resourcePool: "vc-edge-pool
      datastore: "vc-edge-datastore
      caCertPath: "/usr/local/google/home/me/certs/edge-cacert.pem"
      credentials:
        fileRef:
          path: "credential.yaml"
          entry: "vCenter-edge"
      folder: "edge-vm-folder"
    

Also fill in the [`network.vCenter.networkName`](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/user-cluster-configuration-file-latest#network-vcenter-networkname-field) field.

### `network`

Decide how you want your worker nodes to get their IP addresses. The options are:

  * From a DHCP server that you set up ahead of time. Set `network.ipMode.type` to `"dhcp"`.

  * From a list of static IP addresses that you provide. Set `network.ipMode.type` to `"static"`, and create an [IP block file](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/ip-block-file) that provides the static IP addresses. For an example of an IP block file, see Example of filled-in configuration files.




If you have decided to use static IP addresses for your worker nodes, fill in the [`network.ipMode.ipBlockFilePath`](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/user-cluster-configuration-file-latest#network-ipmode.ipblockfilepath-field) field.

The control-plane nodes for your user cluster must get their IP addresses from a list of static addresses that you provide. This is the case even if your worker nodes get their addresses from a DHCP server. To specify static IP addresses for your control-plane nodes, fill in the [`network.controlPlaneIPBlock`](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/user-cluster-configuration-file-latest#network-controlplaneipblock-section) section. If you want a high-availability (HA) user cluster, specify three IP addresses. Otherwise, specify one IP address.

Specify DNS and NTP servers by filling in the `hostConfig` section. These DNS and NTP servers are for the control-plane nodes. If you are using static IP addresses for your worker nodes, then these DNS and NTP servers are also for the worker nodes.

The [network.podCIDR](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/user-cluster-configuration-file-latest#network-podcidr-field) and [network.serviceCIDR](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/user-cluster-configuration-file-latest#network-servicecidr-field) have prepopulated values that you can leave unchanged unless they conflict with addresses already being used in your network. Kubernetes uses these ranges to assign IP addresses to Pods and Services in your cluster.

Regardless of whether you rely on a DHCP server or specify a list of static IP addresses, you need to have enough IP addresses available for your user cluster. For an explanation of how many IP addresses you need, see [Plan your IP addresses](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/plan-ip-addresses).

### `loadBalancer`

Set aside a VIP for the Kubernetes API server of your user cluster. Set aside another VIP for the ingress service of your user cluster. Provide your VIPs as values for [`loadBalancer.vips.controlPlaneVIP`](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/user-cluster-configuration-file-latest#loadbalancer-vips-controlplanevip-field) and [`loadBalancer.vips.ingressVIP`](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/user-cluster-configuration-file-latest#loadbalancer-vips-ingressvip-field).

Decide what type of load balancing you want to use. The options are:

  * MetalLB bundled load balancing. Set [`loadBalancer.kind`](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/user-cluster-configuration-file-latest#loadbalancer-kind-field) to `"MetalLB"`. Also fill in the [`loadBalancer.metalLB.addressPools`](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/user-cluster-configuration-file-latest#loadbalancer-metallb-section) section, and set `enableLoadBalancer` to `true` for at least one of your node pools. For more information, see [Bundled load balancing with MetalLB](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/bundled-load-balance-metallb).

  * Manual load balancing. Set `loadBalancer.kind` to `"ManualLB"`, and fill in the [`manualLB`](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/user-cluster-configuration-file-latest#loadbalancer-manuallb-section) section. For more information, see [Manual load balancing](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/manual-load-balance).




For more information about load balancing options, see [Overview of load balancing](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/setup-load-balance).

### `advancedNetworking`

If you plan to create an [egress NAT gateway](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/egress-nat-gateway), set [advancedNetworking](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/user-cluster-configuration-file-latest#advancednetworking-field) to `true`.

### `multipleNetworkInterfaces`

Decide whether you want to configure [multiple network interfaces](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/multi-nic) for Pods, and set [multipleNetworkInterfaces](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/user-cluster-configuration-file-latest#multiplenetworkinterfaces-field) accordingly.

### `storage`

If you want to disable the deployment of vSphere CSI components, set [storage.vSphereCSIDisabled](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/user-cluster-configuration-file-latest#storagevspherecsidisabled) to `true`.

### `masterNode`

In the [`masterNode`](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/user-cluster-configuration-file-latest#masternode-section) section, you can specify how many control-plane nodes you want for your user cluster: specify `3` for a highly-available (HA) cluster or `1` for a non-HA cluster. You can also specify a datastore for the control-plane nodes and whether you want to enable automatic resizing for the control-plane nodes.

If the [`enableAdvancedCluster`](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/user-cluster-configuration-file-latest#enable-advanced-cluster-field) field is `true`, you must set the `replicas` field to `3`. Only HA user clusters are supported on advanced clusters.

Recall that you specified IP addresses for the control-plane nodes in the [`network.controlPlaneIPBlock`](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/user-cluster-configuration-file-latest#network-controlplaneipblock-section) section.

### `nodePools`

A node pool is a group of nodes in a cluster that all have the same configuration. For example, the nodes in one pool could run Windows and the nodes in another pool could run Linux.

You must specify at least one node pool by filling in the [`nodePools`](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/user-cluster-configuration-file-latest#nodepools-section) section.

If you enable advanced cluster, set `nodePools[i].osImageType` to `ubuntu_cgv2`.

For more information, see [Node pools](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/node-pools) and [Creating and managing node pools](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/managing-node-pools).

### `antiAffinityGroups`

Set [`antiAffinityGroups.enabled`](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/user-cluster-configuration-file-latest#antiaffinitygroups-enabled-field) to `true` or `false`.

This field specifies whether Google Distributed Cloud creates [Distributed Resource Scheduler](https://www.vmware.com/products/vsphere/drs-dpm.html) (DRS) anti-affinity rules for your worker nodes, causing them to be spread across at least three physical hosts in your data center.

### `stackdriver`

If you want to enable [Cloud Logging and Cloud Monitoring](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/concepts/logging-and-monitoring) for your cluster, fill in the [`stackdriver`](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/user-cluster-configuration-file-latest#stackdriver-section) section.

This section is required by default. That is, if you don't fill in this section, you must include the `--skip-validation-stackdriver` flag when you run `gkectl create cluster`.

Note the following requirements for new clusters:

  * The ID in `stackdriver.projectID` must be the same as the ID in `gkeConnect.projectID` and `cloudAuditLogging.projectID`.

  * The Google Cloud region set in `stackdriver.clusterLocation` must be the same as the region set in `cloudAuditLogging.clusterLocation` and `gkeConnect.location`. Additionally, if `gkeOnPremAPI.enabled` is `true`, the same region must be set in `gkeOnPremAPI.location`.




If the project IDs and regions aren't the same, cluster creation fails.

### `gkeConnect`

Your user cluster must be [registered to a Google Cloud fleet](https://docs.cloud.google.com/anthos/fleet-management/docs/fleet-creation).

Fill in the [`gkeConnect`](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/user-cluster-configuration-file-latest#gkeconnect-section) section to specify a [fleet host project](https://docs.cloud.google.com/anthos/fleet-management/docs/fleet-concepts#fleet-host-project) and an associated service account. The ID in `gkeConnect.projectID` must be the same as the ID set in `stackdriver.projectID` and `cloudAuditLogging.projectID`. If the project IDs aren't the same, cluster creation fails.

In 1.28 and later, you can optionally specify a region where the Fleet and Connect services run in `gkeConnect.location`. If you don't include this field, the cluster uses the global instances of these services.

**Important:** If you plan to install Cloud Service Mesh on a regional cluster, you must install version 1.19.3 or later.

If you include `gkeConnect.location` in your configuration file, the region that you specify must be the same as the region configured in `cloudAuditLogging.clusterLocation`, `stackdriver.clusterLocation`, and `gkeOnPremAPI.location`. If the regions aren't the same, cluster creation fails.

### `gkeOnPremAPI`

In 1.16 and later, if the GKE On-Prem API is enabled in your Google Cloud project, all clusters in the project are [enrolled in the GKE On-Prem API](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/enroll-cluster) automatically in the region configured in `stackdriver.clusterLocation`. The `gkeOnPremAPI.location` region must be the same as the region specified in `cloudAuditLogging.clusterLocation`, `gkeConnect.location` (if the field is included in your configuration file), and `stackdriver.clusterLocation`.

  * If you want to enroll all clusters in the project in the GKE On-Prem API, be sure to do the steps in [Before you begin](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/enroll-cluster#before_you_begin) to activate and use the GKE On-Prem API in the project.

  * If you don't want to enroll the cluster in the GKE On-Prem API, include this section and set `gkeOnPremAPI.enabled` to `false`. If you don't want to enroll any clusters in the project, disable `gkeonprem.googleapis.com` (the service name for the GKE On-Prem API) in the project. For instructions, see [Disabling services](https://docs.cloud.google.com/service-usage/docs/enable-disable#disabling).




### `cloudAuditLogging`

If you want to integrate the audit logs from your cluster's Kubernetes API server with [Cloud Audit Logs](https://docs.cloud.google.com/logging/docs/audit), fill in the [`cloudAuditLogging`](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/user-cluster-configuration-file-latest#cloudauditlogging-section) section.

Note the following requirements:

  * If you enable advanced cluster, set `cloudAuditLogging.serviceAccountKeyPath` to the same path as `stackdriver.serviceAccountKeyPath`.

  * The ID in `cloudAuditLogging.projectID` must be the same as the ID in `gkeConnect.projectID` and `stackdriver.projectID`.

  * The region in `cloudAuditLogging.clusterLocation` must be the same as the region set in `gkeConnect.location` and `stackdriver.clusterLocation`. Additionally, if `gkeOnPremAPI.enabled` is `true`, the same region must be set in `gkeOnPremAPI.location`.




If the project IDs and regions aren't the same, cluster creation fails.

### Example of filled-in configuration files

Here is an example of an IP block file and a user cluster configuration file;

#### user-ipblock.yaml
    
    
    blocks:
      - netmask: 255.255.255.0
        gateway: 172.16.21.1
        ips:
        - ip: 172.16.21.2
          hostname: worker-vm-1
        - ip: 172.16.21.3
          hostname: worker-vm-2
        - ip: 172.16.21.4
          hostname: worker-vm-3
        - ip: 172.16.21.5
          hostname: worker-vm-4
    

#### user-cluster.yaml
    
    
    apiVersion: v1
    kind: UserCluster
    name: "my-user-cluster"
    gkeOnPremVersion: 1.36.200-gke.118
    enableControlplaneV2: true
    enableAdvancedCluster: true
    network:
      hostConfig:
        dnsServers:
        - "203.0.113.2"
        - "198.51.100.2"
        ntpServers:
        - "216.239.35.4"
      ipMode:
        type: "static"
        ipBlockFilePath: "user-ipblock.yaml"
      serviceCIDR: 10.96.0.0/20
      podCIDR: 192.168.0.0/16
      controlPlaneIPBlock:
        netmask: "255.255.255.0"
        gateway: "172.16.21.1"
        ips:
        - ip: "172.16.21.6"
          hostname: "cp-vm-1"
        - ip: "172.16.21.7"
          hostname: "cp-vm-2"
        - ip: "172.16.21.8"
          hostname: "cp-vm-3"
    loadBalancer:
      vips:
        controlPlaneVIP: "172.16.21.40"
        ingressVIP: "172.16.21.30"
      kind: MetalLB
      metalLB:
        addressPools:
        - name: "address-pool-1"
          addresses:
          - "172.16.21.30-172.16.21.39"
    enableDataplaneV2: true
    masterNode:
      cpus: 4
      memoryMB: 8192
      replicas: 3
    nodePools:
    - name: "worker-node-pool"
      cpus: 4
      memoryMB: 8192
      replicas: 3
      osImageType: "ubuntu_cgv2"
      enableLoadBalancer: true
    antiAffinityGroups:
      enabled: true
    gkeConnect:
      projectID: "my-project-123"
      location: "us-central1"
      registerServiceAccountKeyPath: "connect-register-sa-2203040617.json"
    stackdriver:
      projectID: "my-project-123"
      clusterLocation: "us-central1"
      serviceAccountKeyPath: "log-mon-sa-2203040617.json"
      disableVsphereResourceMetrics: false
    cloudAuditLogging:
      projectID: "my-project-123"
      clusterLocation: "us-central1"
      serviceAccountKeyPath: "log-mon-sa-2203040617.json"
    autoRepair:
      enabled: true
    

These are the important points to understand in the preceding example:

  * The `nodePools.replicas` field is set to `3`, which means there are three worker nodes in `"worker-node-pool"`. All worker nodes use static IP addresses because `network.ipMode.type` is set to `"static"`.

  * The static IP addresses for the worker nodes are specified in an IP block file. The IP block file has four addresses even though there are only three worker nodes. The extra IP address is needed during cluster upgrade, update, and auto repair.

  * DNS and NTP servers are specified in the `hostConfig` section. In this example, these DNS and NTP servers are for the control-plane nodes and the worker nodes. That is because the worker nodes have static IP addresses. If the worker nodes were to get their IP addresses from a DHCP server, then these DNS and NTP servers would be only for the control-plane nodes.

  * The static IP addresses for the three control-plane nodes are specified in the `network.controlPlaneIPBlock` section of the user cluster configuration file. There is no need for an extra IP address in this block.

  * Controlplane V2 is enabled.

  * The `masterNode.replicas` field is set to `3`, so the cluster will have a high-availability control plane.

  * The control-plane VIP and the ingress VIP are both in the same VLAN as the worker nodes and the control-plane nodes.

  * The VIPs that are set aside for Services of type LoadBalancer are specified in the `loadBalancer.metalLB.addressPools` section of the user cluster configuration file. These VIPs are in the same VLAN as the worker nodes and the control-plane nodes. The set of VIPs specified in this section must include the ingress VIP and must not include the control-plane VIP.

  * The user cluster configuration file does not include a `vCenter` section. So the user cluster uses the same vSphere resources as the admin cluster.




### Validate your configuration file

After you've filled in your user cluster configuration file, run the `gkectl check-config` command to verify that the file is valid. Support for the `gkectl check-config` command on advanced user clusters was added in the following versions: 1.32.700+, 1.33.300+, and 1.34.0 and higher. If you are installing a lower version on an advanced cluster, the command will fail.
    
    
    gkectl check-config --kubeconfig ADMIN_CLUSTER_KUBECONFIG --config USER_CLUSTER_CONFIG
    

Replace the following:

  * ADMIN_CLUSTER_KUBECONFIG: the path of the kubeconfig file for your admin cluster

  * USER_CLUSTER_CONFIG: the path of your user cluster configuration file




If the command returns any failure messages, fix the issues and validate the file again.

If you want to skip the more time-consuming validations, pass the `--fast` flag. To skip individual validations, use the `--skip-validation-xxx` flags. To learn more about the `check-config` command, see [Running preflight checks](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/preflight-checks).

## (Optional) Import OS images to vSphere, and push container images to a private registry

Run `gkectl prepare` if any of the following are true:

  * Your user cluster is in a different vSphere data center from your admin cluster.

  * Your user cluster has a different vCenter Server from your admin cluster.

  * Your user cluster has a different vCenter folder from your admin cluster.

  * Your user cluster uses a private container registry that is different from the private registry used by your admin cluster.



    
    
    gkectl prepare --kubeconfig ADMIN_CLUSTER_KUBECONFIG \
        --bundle-path BUNDLE \
        --user-cluster-config USER_CLUSTER_CONFIG
    

Replace the following:

  * ADMIN_CLUSTER_KUBECONFIG: the path of your admin cluster kubeconfig file

  * BUNDLE: the path of the bundle file. This file is on your admin workstation in `/var/lib/gke/bundles/`. For example:
        
        /var/lib/gke/bundles/gke-onprem-vsphere-1.36.200-gke.118-full.tgz
        

  * USER_CLUSTER_CONFIG: the path of your user cluster configuration file




## Create a user cluster

Run the following command to create a user cluster:
    
    
    gkectl create cluster --kubeconfig ADMIN_CLUSTER_KUBECONFIG --config USER_CLUSTER_CONFIG
    

If you use VPC Service Controls, you might see errors when you run some `gkectl` commands, such as `"Validation Category: GCP - [UNKNOWN] GCP service: [Stackdriver] could not get GCP services"`. To avoid these errors, add the `--skip-validation-gcp` parameter to your commands.

#### Locate the user cluster kubeconfig file

The `gkectl create cluster` command creates a kubeconfig file named `USER_CLUSTER_NAME-kubeconfig` in the current directory. You will need this kubeconfig file later to interact with your user cluster.

The kubeconfig file contains the name of your user cluster. To view the cluster name, you can run:
    
    
    kubectl config get-clusters --kubeconfig USER_CLUSTER_KUBECONFIG
    

The output shows the name of the cluster. For example:
    
    
    NAME
    my-user-cluster
    

If you like, you can change the name and location of your kubeconfig file.

## Verify that your user cluster is running

Verify that your user cluster is running:
    
    
    kubectl get nodes --kubeconfig USER_CLUSTER_KUBECONFIG
    

Replace USER_CLUSTER_KUBECONFIG with the path of your user cluster kubeconfig file.

The output shows the user cluster nodes. For example:
    
    
    cp-vm-1       Ready    control-plane,master   18m
    cp-vm-2       Ready    control-plane,master   18m
    cp-vm-3       Ready    control-plane,master   18m
    worker-vm-1   Ready                           6m7s
    worker-vm-2   Ready                           6m6s
    worker-vm-3   Ready                           6m14s
    

### Console

### Get started

  1. In the Google Cloud console, go to the **Create VM cluster** page.

[Go to Create VM cluster](https://console.cloud.google.com/kubernetes/vmware/add)

  2. Select the Google Cloud project that you want to create the cluster in. The selected project is used as the fleet host project. This must be the same project that the admin cluster is registered to. After the user cluster is created, it is automatically registered to the selected project's fleet.

  3. In the **Choose your cluster type** section, select **Create a user cluster for an existing admin cluster**.




### Cluster basics

Enter basic information about the cluster.

  1. Enter a **Name** for the user cluster.

  2. Under **Admin cluster** , select the admin cluster from the list. If you didn't specify a name for the admin cluster when you created it, the name is generated in the form `gke-admin-[HASH]`. If you don't recognize the admin cluster name, run the following command on your admin workstation:
         
         KUBECONFIG=ADMIN_CLUSTER_KUBECONFIG
         kubectl get OnPremAdminCluster -n kube-system -o=jsonpath='{.items[0].metadata.name}'
         

If the admin cluster that you want to use isn't displayed, see the troubleshooting section [The admin cluster isn't displayed on the **Cluster basics** drop-down list](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/troubleshooting/on-prem-api).

  3. In the **GCP API Location** field, select the Google Cloud region from the list. This setting specifies the region where the following APIs and services run:

     * GKE On-Prem API (`gkeonprem.googleapis.com`)
     * Fleet service (`gkehub.googleapis.com`)
     * Connect service (`gkeconnect.googleapis.com`)

This setting also controls the region in which the following are stored:

     * The user cluster metadata that the GKE On-Prem API needs to manage the cluster lifecycle
     * The Cloud Logging and Cloud Monitoring data of system components
     * The Admin Audit log created by Cloud Audit Logs

The cluster name, project, and location together uniquely identify the cluster in Google Cloud.

  4. Select the Google Distributed Cloud version for your user cluster.

  5. As the cluster creator, you are granted cluster admin privileges to the cluster. Optionally, enter the email address of another user who will administer the cluster in the **Cluster admin user** field in the **Authorization** section.

When the cluster is created, the GKE On-Prem API applies the Kubernetes role-based access control (RBAC) policies to the cluster to grant you and other admin users the Kubernetes `clusterrole/cluster-admin` role, which provides full access to every resource in the cluster in all namespaces.

**Note:** In addition to the Kubernetes RBAC policies, you must grant some Identity and Access Management (IAM) roles to the users who aren't project owners. For details on granting the IAM roles, see [Grant required roles](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/connect-to-cluster-console#grant_required_roles).
  6. Click **Next** to go to the **Control plane** section.




### Control Plane

All the fields in the **Control plane** section are set with default values. Review the defaults and optionally, change them as needed.

  1. In the **Control-plane node vCPUs** field, enter the number of vCPUs (minimum 4) for each control plane node for your user cluster.

  2. In the **Control-plane node memory** field, enter the memory size in MiB (minimum 8192 and must be a multiple of 4) for each control plane for your user cluster.

  3. Under **Control-plane nodes** , select the number of control-plane nodes for your user cluster. For example, you may select 1 control-plane node for a development environment and 3 control-planes nodes for high availability (HA), production environments.

  4. Optionally, select **Automatic node resizing**. Resizing means that the vCPU and memory resources assigned to a node are adjusted automatically. When enabled, the control-plane nodes for the user cluster are resized according to the number of worker nodes in the user cluster. So as you add more worker nodes to the user cluster, the control-plane nodes are increased in size.

  5. In the **Control plane node IPs** section, enter the IP addresses for the gateway, the subnet mask, and the control-plane nodes.

  6. Click **Next** to go to the **Networking** section.




### Networking

In this section, you specify the IP addresses for your cluster's nodes, Pods, and Services. A user cluster needs to have one IP address for each node and an additional IP address for a temporary node that is needed during cluster upgrades, updates, and auto repair. For more information, see [How many IP addresses does a user cluster need?](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/manage-node-ip-addresses#how_many_ip_addresses_does_a_user_cluster_need).

  1. In the **Node IPs** section, select the **IP mode** for the user cluster. Select one of the following:

     * **DHCP** : Choose **DHCP** if you want your cluster nodes to get their IP address from a DHCP server.

     * **Static** : Choose **Static** if you want to provide static IP addresses for your cluster nodes, or if you want to set up manual load-balancing.

  2. If you selected **DHCP** , skip to the next step to specify **Service and Pod CIDRs**. For **Static IP mode** , provide the following information:

     1. Enter the IP address of the **Gateway** for the user cluster.

     2. Enter the **Subnet mask** for the user cluster nodes.

     3. In the **IP Addresses** section, enter the IP addresses and optionally, the hostnames for the nodes in the user cluster. You can enter either an individual IP v4 address (such as 192.0.2.1) or a [CIDR](https://en.wikipedia.org/wiki/Classless_Inter-Domain_Routing) block of IPv4 addresses (such as 192.0.2.0/24).

        * If you enter a CIDR block, don't enter a hostname.

        * If you enter an individual IP address, you can optionally enter a hostname. If you don't enter a hostname, Google Distributed Cloud uses the VM's name from vSphere as the hostname.

     4. Click **\+ Add IP Address** as needed to enter more IP addresses.

  3. In the **Service and Pod CIDRs** section, the console provides the following address ranges for your Kubernetes Services and Pods:

     * **Service CIDR** : 10.96.0.0/20
     * **Pod CIDR** : 192.168.0.0/16

If you prefer to enter your own address ranges, see [IP addresses for Pods and Services](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/minimal-infrastructure#ip-addresses-pods-services) for best practices.

  4. If you selected **Static IP mode** or **Enable control plane v2** , specify the following information in the **Host config** section:

     1. Enter the IP addresses of the DNS servers.
     2. Enter the IP addresses of the NTP servers.
     3. Optionally, enter DNS search domains.
  5. Click **Next** to go to the **Load balancer** section.




### Load balancer

Choose the load balancer to set up for your cluster. See [Load balancer overview](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/setup-load-balance) for more information.

Select the **Load balancer type** from the list.

### Bundled with MetalLB

Configure bundled load balancing with MetalLB. You can use MetalLB for the user cluster only if your admin cluster is using SeeSaw or MetalLB. This option requires minimal configuration. MetalLB runs directly on your cluster nodes and doesn't require extra VMs. For more information about the benefits of using MetalLB and how it compares to the other load balancing options, see [Bundled load balancing with MetalLB](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/bundled-load-balance-metallb). 

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

     * **Control plane VIP** : The destination IP address to be used for traffic sent to the [Kubernetes API server](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/user-cluster-configuration-file-latest#loadbalancer-vips-controlplanevip-field) of the user cluster. The Kubernetes API server for the user cluster runs on a node in the admin cluster. This IP address must be in the same L2 domain as the admin cluster nodes. Don't add this address in the **Address pools** section.

     * **Ingress VIP** : The IP address to be configured on the load balancer for the ingress proxy. You must add this to an address pool in the **Address pools** section.

  4. Click **Continue**. 




### F5 BIG-IP

You can use F5 BIG-IP for the user cluster only if your admin cluster is using F5 BIG-IP. Be sure to install and configure the F5 BIG-IP ADC before integrating it with Google Distributed Cloud. 

The F5 username and password are inherited from the admin cluster.

  1. In the **Virtual IPs** section, enter the following:

     * **Control plane VIP** : The destination IP address to be used for traffic sent to the [Kubernetes API server](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/user-cluster-configuration-file-latest#loadbalancer-vips-controlplanevip-field).

     * **Ingress VIP** : The IP address to be configured on the load balancer for the ingress proxy.

  2. In the **Address** field, enter the address of your F5 BIG-IP load balancer.

  3. In the **Partition** field, enter the name of a BIG-IP partition that you created for your user cluster.

  4. In the **sNAT pool name** field, enter the name of your SNAT pool, if applicable.

  5. Click **Continue**. 




### Manual

You can use a manual load balancer for the user cluster only if your admin cluster uses a manual load balancer. In Google Distributed Cloud, the Kubernetes API server and the ingress proxy are each exposed by a Kubernetes Service of type `LoadBalancer`. Choose your own `nodePort` values in the 30000 - 32767 range for these Services. For the ingress proxy, choose a `nodePort` value for both HTTP and HTTPS traffic. See [Enabling manual load balancing mode](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/manual-load-balance) for more information. 

  1. In the **Virtual IPs** section, enter the following:

     * **Control plane VIP** : The destination IP address to be used for traffic sent to the [Kubernetes API server](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/user-cluster-configuration-file-latest#loadbalancer-vips-controlplanevip-field).

     * **Ingress VIP** : The IP address to be configured on the load balancer for the ingress proxy.

  2. In the **Control-plan node port** field, enter a `nodePort` value for the Kubernetes API server.

  3. In the **Ingress HTTP node port** field, enter a `nodePort` value for HTTP traffic to the ingress proxy.

  4. In the **Ingress HTTPS node port** field, enter a `nodePort` value for HTTPS traffic to the ingress proxy.

  5. In the **Konnectivity server node port** field, enter a `nodePort` value for the Konnectivity server.

  6. Click **Continue**. 




### Features

This section displays the features and operations that are enabled on the cluster.

  1. The following are enabled automatically and can't be disabled:

     * Cloud Logging of system services 

     * Cloud Monitoring of system services 

     * The [Admin Activity audit log](https://docs.cloud.google.com/logging/docs/audit#admin-activity)

  2. The following are enabled by default, but you can disable them:

     * **Enable vSphere CSI driver** : Also called the vSphere Container Storage Plug-in. The Container Storage Interface (CSI) driver runs in a Kubernetes cluster deployed in vSphere to provision persistent volumes on vSphere storage. For more information, see [Using the vSphere Container Storage Interface driver](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/using-vsphere-csi-driver).

     * **Enable anti-affinity groups** : VMware Distributed Resource Scheduler (DRS) anti-affinity rules are automatically created for your user cluster's nodes, causing them to be spread across at least 3 physical hosts in your data center. Make sure that your vSphere environment meets the [requirements](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/user-cluster-configuration-file-latest#antiaffinitygroups-enabled-field).

**Note:** If you followed [Set up minimal infrastructure](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/minimal-infrastructure), you only have one ESXi host, so be sure to clear **Enable anti-affinity groups**.
  3. Click **Next** to configure a node pool




### Node pools

Your cluster will be created with at least one node pool. A node pool is a template for a group of worker nodes created in this cluster. For more information, see [Creating and managing node pools ](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/managing-node-pools).

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

For more information about possible errors and how to fix them, see [Troubleshoot user cluster creation in the Google Cloud console](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/troubleshooting/on-prem-api). 




### gcloud CLI

You use the following command to create a user cluster:
    
    
    gcloud container vmware clusters create
    

After creating the cluster, you need to create at least one node pool using the following command:
    
    
    gcloud container vmware node-pools create
    

Most of the flags for creating the cluster and the node pool correspond to the fields in the [user cluster configuration file](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/user-cluster-configuration-file-latest). To help you get started, you can test a complete command in the examples section.

### Gather information

Gather some information that you need to create the cluster.

  1. Get the name and the fleet membership location of your admin cluster:
         
         gcloud container fleet memberships list \
             --project=FLEET_HOST_PROJECT_ID
         

Replace `FLEET_HOST_PROJECT_ID` with ID of the project that the admin cluster is registered to.

The output is similar to the following:
         
         NAME             EXTERNAL_ID                           LOCATION
         admin-cluster-1  bb7803b4-8438-4b22-859f-4559b4b29072  global
         admin-cluster-2  ee16ee2b-6ec0-49fc-9413-3c89cbc70854  global
         admin-cluster-3  fc2b7ef5-39ff-4b63-b919-04c5adc67be4  us-west1
         

The location specifies where the Fleet and Connect services run. Admin clusters created prior to 1.28 are managed by the global Fleet and Connect services. In 1.28 and higher, you can specify either `global` or a Google Cloud region when you create the admin cluster. You specify the region in the `--admin-cluster-membership-location` flag in the example commands that follow.

  2. Get a list of available versions:
         
         gcloud container vmware clusters query-version-config \
             --admin-cluster-membership=ADMIN_CLUSTER_NAME \
             --admin-cluster-membership-project=FLEET_HOST_PROJECT_ID \
             --admin-cluster-membership-location=ADMIN_CLUSTER_REGION \
             --location=REGION
         

Replace the following:

     * `ADMIN_CLUSTER_NAME`: The name of the admin cluster.

     * `FLEET_HOST_PROJECT_ID`: The ID of the project that the admin cluster is registered to.

     * `ADMIN_CLUSTER_REGION`: The admin cluster's fleet membership region. This is either global or a Google Cloud region. Use the location for the admin cluster from the output of `gcloud container fleet memberships list`.

     * `REGION`: The Google Cloud region that you will use when you create the user cluster. This is the region that the GKE On-Prem API runs and stores its metadata.

       * If the admin cluster is [enrolled in the GKE On-Prem API](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/enroll-cluster), use the same region as the admin cluster. To find out the admin cluster's region, run the following command:
             
             gcloud container vmware admin-clusters list \
               --project=FLEET_HOST_PROJECT_ID \
               --location=-
             

       * If the admin cluster isn't enrolled in the GKE On-Prem API, specify `us-west1` or another [supported region](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/reference/supported-regions-on-prem-api). If you subsequently enroll the admin cluster in the GKE On-Prem API, use the same region that the user cluster is in.

The output of the `gcloud container vmware clusters query-version-config` command is similar to the following:
    
    versions:
    - isInstalled: true
      version: 1.28.800-gke.109
    - version: 1.29.0-gke.1456
    - version: 1.29.100-gke.248
    - version: 1.29.200-gke.245
    - version: 1.29.300-gke.184
    

The command also outputs an explanation of the versions that you can use for user cluster creation or upgrade. Allowable versions are annotated with `isInstalled: true`, which means the admin cluster has the version-specific components it needs to manage user clusters of that version. If you want to use a version that is installed on the admin cluster, skip to the Examples section to create the user cluster.




### Install a different version

An admin cluster can manage user clusters at different versions. The output of the `query-version-config` command lists other versions that you can use when you create the cluster. If you want to create a user cluster that is a different version than the admin cluster, you need to download and deploy the components that the admin cluster needs to manage user clusters of that version, as follows:
    
    
    gcloud container vmware admin-clusters update ADMIN_CLUSTER_NAME \
        --project=FLEET_HOST_PROJECT_ID \
        --location=REGION \
        --required-platform-version=VERSION

Replace `VERSION` with one of the versions listed in the output of the `query-version-config` command.

The command downloads the version of the components that you specify in `--required-platform-version` to the admin cluster, and then deploys the the components. You can now create a user cluster with the specified version.

If you rerun the `gcloud container vmware clusters query-version-config`, the version that you specified is annotated with `isInstalled: true`.

### Examples

The following examples show how to create a user cluster with different load balancers with Controlplane V2 enabled. With Controlplane V2, the control plane for a user cluster runs on one or more nodes in the user cluster itself. We recommend that you enable Controlplane V2, and in version 1.30 and higher, new user clusters are required to have Controlplane V2 enabled. For information about the available load balancing options, see [Load balancer overview](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/setup-load-balance).

Most of the examples use the default values for configuring the control plane nodes. If you want to change any of the defaults, include the flags described in the Control plane flags section. If needed, you can also change some vSphere settings.

Before running the `gcloud` command to create the cluster, you can include `--validate-only` to validate the configuration that you specified in the flags to the `gcloud` command. When you are ready to create the cluster, remove this flag and run the command.

If you get an error after the `gcloud container vmware clusters create` command has been running for about a minute or more, check if the cluster was partially created by running the following command:
    
    
    gcloud container vmware clusters list \
        --project=FLEET_HOST_PROJECT_ID \
        --location=-
    

If the cluster isn't listed in the output, fix the error and rerun `gcloud container vmware clusters create`.

If the cluster is listed in the output, delete the cluster using the following command:
    
    
    gcloud container vmware clusters delete USER_CLUSTER_NAME \
        --project=FLEET_HOST_PROJECT_ID \
        --location=REGION \
        --force \
        --allow-missing
    

Then fix the error and rerun `gcloud container vmware clusters create`.

After the cluster is running, you must add a node pool before deploying workloads, as described in the Create a node pool section.

### MetalLB & DHCP

This example shows how to create a user cluster with the bundled MetalLB load balancer and using your DHCP server to get IP addresses for your cluster worker nodes. 

You can use MetalLB for the user cluster only if your admin cluster is using MetalLB. This load balancing option requires minimal configuration. MetalLB runs directly on your cluster nodes and doesn't require extra VMs. For more information about the benefits of using MetalLB and how it compares to the other load balancing options, see [Bundled load balancing with MetalLB](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/bundled-load-balance-metallb).

The example command creates a user cluster with the following characteristics, which you can modify as needed for your environment.

Flag | Description  
---|---  
`--admin-users` | Grants you and another user full administrative rights on the cluster.  
`--enable-control-plane-v2` | Enables Controlplane V2, which is recommended and required in version 1.30 and higher.  
`--control-plane-ip-block` | One IP address for the control plane node. To create a high-availability (HA) user cluster, specify three IP address and add the flag `--replicas=3`.  
`--metal-lb-config-address-pools` | Two address pools for the MetalLB load balancer. You need at least one address pool, and you can specify more if needed. For convenience, the example contains an address pool with the name "ingress-vip-pool" as a reminder that the IP address for the ingress VIP must be in one of the address pools. You specify the CIDR for a single IP address by appending `/32` to the IP address.  
      
    
    gcloud container vmware clusters create USER_CLUSTER_NAME \
        --project=FLEET_HOST_PROJECT_ID \
        --admin-cluster-membership=ADMIN_CLUSTER_NAME \
        --admin-cluster-membership-project=FLEET_HOST_PROJECT_ID \
        --admin-cluster-membership-location=ADMIN_CLUSTER_REGION \
        --location=REGION \
        --version=VERSION \
        --admin-users=YOUR_EMAIL_ADDRESS \
        --admin-users=ANOTHER_EMAIL_ADDRESS \
        --service-address-cidr-blocks=10.96.0.0/20 \
        --pod-address-cidr-blocks=192.168.0.0/16 \
        --metal-lb-config-address-pools='pool=NAME,avoid-buggy-ips=AVOID_BUGGY_IPS,manual-assign=MANUAL_ASSIGN,addresses=IP_ADDRESS_RANGE_1' \
        --metal-lb-config-address-pools='pool=ingress-vip-pool,avoid-buggy-ips=False,manual-assign=True,addresses=INGRESS_VIP/32' \
        --enable-control-plane-v2 \
        --dns-servers=DNS_SERVER_1 \
        --ntp-servers=NTP_SERVER_1 \
        --control-plane-ip-block 'gateway=CP_GATEWAY,netmask=CP_NETMASK,ips=CP_IP_ADDRESS_1 CP_HOST_1' \
        --control-plane-vip=CONTROL_PLANE_VIP \
        --ingress-vip=INGRESS_VIP \
        --enable-dhcp
    

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



  * `--enable-dhcp`: Include `--enable-dhcp` if you want your cluster nodes to get their IP address from a DHCP server that you provide. Don't include this flag if you want to provide static IP addresses for your cluster nodes, or if you want to set up manual load balancing. 



### MetalLB & static IPs

This example shows how to create a user cluster with the bundled MetalLB load balancer and assigning static IP addresses to your cluster worker nodes. 

You can use MetalLB for the user cluster only if your admin cluster is using MetalLB. This load balancing option requires minimal configuration. MetalLB runs directly on your cluster nodes and doesn't require extra VMs. For more information about the benefits of using MetalLB and how it compares to the other load balancing options, see [Bundled load balancing with MetalLB](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/bundled-load-balance-metallb).

The example command creates a user cluster with the following characteristics, which you can modify as needed for your environment.

Flag | Description  
---|---  
`--admin-users` | Grants you and another user full administrative rights on the cluster.  
`--enable-control-plane-v2` | Enables Controlplane V2, which is recommended and required in version 1.30 and higher.  
`--control-plane-ip-block` | One IP address for the control plane node. To create a high-availability (HA) user cluster, specify three IP address and add the flag `--replicas=3`.  
`--metal-lb-config-address-pools` | Two address pools for the MetalLB load balancer. You need at least one address pool, and you can specify more if needed. For convenience, the example contains an address pool with the name "ingress-vip-pool" as a reminder that the IP address for the ingress VIP must be in one of the address pools. You specify the CIDR for a single IP address by appending `/32` to the IP address.  
`--static-ip-config-ip-blocks` | Four IP addresses for the worker nodes in the clusters. This includes an address for an extra node that can be used during upgrade and update. You can specify more IP addresses if needed. The hostname is optional.  
      
    
    gcloud container vmware clusters create USER_CLUSTER_NAME \
        --project=FLEET_HOST_PROJECT_ID \
        --admin-cluster-membership=ADMIN_CLUSTER_NAME \
        --admin-cluster-membership-project=FLEET_HOST_PROJECT_ID \
        --admin-cluster-membership-location=ADMIN_CLUSTER_REGION \
        --location=REGION \
        --version=VERSION \
        --admin-users=YOUR_EMAIL_ADDRESS \
        --admin-users=ANOTHER_EMAIL_ADDRESS \
        --service-address-cidr-blocks=10.96.0.0/20 \
        --pod-address-cidr-blocks=192.168.0.0/16 \
        --metal-lb-config-address-pools='pool=NAME,avoid-buggy-ips=AVOID_BUGGY_IPS,manual-assign=MANUAL_ASSIGN,addresses=IP_ADDRESS_RANGE_1' \
        --metal-lb-config-address-pools='pool=ingress-vip-pool,avoid-buggy-ips=False,manual-assign=True,addresses=INGRESS_VIP/32' \
        --enable-control-plane-v2 \
        --control-plane-ip-block 'gateway=CP_GATEWAY,netmask=CP_NETMASK,ips=CP_IP_ADDRESS_1 CP_HOST_1' \
        --control-plane-vip=CONTROL_PLANE_VIP \
        --ingress-vip=INGRESS_VIP \
        --static-ip-config-ip-blocks='gateway=GATEWAY,netmask=NETMASK,ips=IP_ADDRESS_1 HOST_1;IP_ADDRESS_2 HOST_2;IP_ADDRESS_3 HOST_3;IP_ADDRESS_4 HOST_4' \
        --dns-servers=DNS_SERVER_1 \
        --ntp-servers=NTP_SERVER_1
    

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



### Manual LB & static IPs

This example shows how to create a user cluster with a manual load balancer and assigning static IP addresses to your cluster worker nodes. 

You can use a manual load balancer for the user cluster only if your admin cluster uses a manual load balancer. In Google Distributed Cloud, the Kubernetes API server, ingress proxy, and the add-on service for log aggregation are each exposed by a Kubernetes Service of type `LoadBalancer`. Choose your own `nodePort` values in the 30000 - 32767 range for these Services. For the ingress proxy, choose a `nodePort` value for both HTTP and HTTPS traffic. See [Enabling manual load balancing mode](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/manual-load-balance) for more information.

The example command creates a user cluster with the following characteristics, which you can modify as needed for your environment.

Flag | Description  
---|---  
`--admin-users` | Grants you and another user full administrative rights on the cluster.  
`--enable-control-plane-v2` | Enables Controlplane V2, which is recommended and required in version 1.30 and higher.  
`--control-plane-ip-block` | One IP address for the control plane node. To create a high-availability (HA) user cluster, specify three IP address and add the flag `--replicas=3`.  
`--static-ip-config-ip-blocks` | Four IP addresses for the worker nodes in the clusters. This includes an address for an extra node that can be used during upgrade and update. You can specify more IP addresses if needed. The hostname is optional.  
      
    
    gcloud container vmware clusters create USER_CLUSTER_NAME \
        --project=FLEET_HOST_PROJECT_ID \
        --admin-cluster-membership=ADMIN_CLUSTER_NAME \
        --admin-cluster-membership-project=FLEET_HOST_PROJECT_ID \
        --admin-cluster-membership-location=ADMIN_CLUSTER_REGION \
        --location=REGION \
        --version=VERSION \
        --admin-users=YOUR_EMAIL_ADDRESS \
        --admin-users=ANOTHER_EMAIL_ADDRESS \
        --service-address-cidr-blocks=10.96.0.0/20 \
        --pod-address-cidr-blocks=192.168.0.0/16 \
        --enable-control-plane-v2 \
        --control-plane-ip-block 'gateway=CP_GATEWAY,netmask=CP_NETMASK,ips=CP_IP_ADDRESS_1 CP_HOST_1' \
        --control-plane-vip=CONTROL_PLANE_VIP \
        --ingress-vip=INGRESS_VIP \
        --ingress-http-node-port=INGRESS_HTTP_NODE_PORT \
        --ingress-https-node-port=INGRESS_HTTPS_NODE_PORT \
        --static-ip-config-ip-blocks='gateway=GATEWAY,netmask=NETMASK,ips=IP_ADDRESS_1 HOST_1;IP_ADDRESS_2 HOST_2;IP_ADDRESS_3 HOST_3;IP_ADDRESS_4 HOST_4' \
        --dns-servers=DNS_SERVER_1 \
        --ntp-servers=NTP_SERVER_1
    

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

  * `INGRESS_VIP`: The IP address that you have chosen to configure on the load balancer for the ingress proxy.

Example: `--ingress-vip=203.0.113.4`

  * `INGRESS_HTTP_NODE_PORT`: A `nodePort` value for HTTP traffic to the ingress proxy (such as `30243`).

  * `INGRESS_HTTPS_NODE_PORT`: A `nodePort` value for HTTPS traffic to the ingress proxy (such as `30879`).



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



### Control plane flags

If you want to use non-default values for the control plane configuration, include one or more of the following flags:

  * `--cpus=vCPUS`: The number of vCPUs (minimum 4) for each control-plane node for your user cluster. If not specified, the default is 4 vCPUs.

  * `--memory=MEMORY`: The memory size in mebibytes (MiB) for each control-plane node for your user cluster. The minimum value is 8192 and it must be a multiple of 4. If not specified, the default is 8192.

  * `--replicas=NODES`: The number of control-plane nodes for your user cluster. For example, you may select 1 control-plane node for a development environment and 3 control-planes nodes for high availability (HA), production environments.

  * `--enable-auto-resize`: If you want to enable automatic resizing of the control-plane nodes for the user cluster, include `--enable-auto-resize`. Resizing means that the vCPU and memory resources assigned to a node are adjusted automatically. When enabled, the control-plane nodes for the user cluster are resized according to the number of worker nodes in the user cluster. So as you add more worker nodes to the user cluster, the control-plane nodes are increased in size.

  * `--enable-control-plane-v2`: To enable Controlplane V2, which we recommend, include this flag. When Controlplane V2 is enabled, the control plane for a user cluster runs on one or more nodes in the user cluster itself. In version 1.30 and higher, Controlplane V2 is required.

When you enable Controlplane V2, you must also specify the following flags:

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

  * `--disable-aag-config`: If you don't include this flag the VMware Distributed Resource Scheduler (DRS) anti-affinity rules are automatically created for your user cluster's nodes, causing them to be spread across at least 3 physical hosts in your data center. Make sure that your vSphere environment meets the [requirements](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/user-cluster-configuration-file-latest#antiaffinitygroups-enabled-field). If your cluster doesn't meet the requirements, include this flag.

**Note:** If you followed [Set up minimal infrastructure](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/minimal-infrastructure), you only have one ESXi host, so be sure to include this flag.
  * `--disable-vsphere-csi`: If you don't include this flag, the vSphere Container Storage Interface (CSI) components are deployed in the user cluster. The CSI driver runs in a native Kubernetes cluster deployed in vSphere to provision persistent volumes on vSphere storage. For more information, see [Using the vSphere Container Storage Interface driver](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/using-vsphere-csi-driver). If you don't want to deploy the CSI components, include this flag.

For a complete list of the flags and their descriptions, see the [gcloud CLI reference](https://docs.cloud.google.com/sdk/gcloud/reference/container/vmware/clusters/create)

### Track cluster creation progress

The output from the cluster create command is similar to the following:
        
        Waiting for operation [projects/example-project-12345/locations/us-west1/operations/operation-1679543737105-5f7893fd5bae9-942b3f97-75e59179] to complete.
        

In the example output, the string `operation-1679543737105-5f7893fd5bae9-942b3f97-75e59179` is the `OPERATION_ID` of the long-running operation. You can find out the status of the operation with the following command:
        
        gcloud container vmware operations describe OPERATION_ID \
          --project=FLEET_HOST_PROJECT_ID \
          --location=REGION
        

For more information, see [gcloud container vmware operations](https://docs.cloud.google.com/sdk/gcloud/reference/container/vmware/operations).

It takes 15 minutes or more to create the user cluster. You can view the cluster in the Google Cloud console on the [GKE clusters](https://console.cloud.google.com/kubernetes/list/overview) page.

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

  * `REGION`: The Google Cloud region that you specified when you created the cluster.

  * `IMAGE_TYPE`: The type of OS image to run on the VMs in the node pool. Set to one of the following: `ubuntu_cgv2` or `cos_cgv2`.

  * `BOOT_DISK_SIZE`: The size of the boot disk in gibibytes (GiB) for each node in the pool. The minimum is 40 GiB.

  * `vCPUs`: The number of vCPUs for each node in the node pool. The minimum is 4.

  * `MEMORY`: The memory size in mebibytes (MiB) for each node in the pool. The minimum is 8192 MiB per user cluster worker node and the value must be a multiple of 4.

  * `NODES`: The number of nodes in the node pool. The minimum is 3.

  * If you are using MetalLB as the load balancer, optionally, include `--enable-load-balancer` if you want to allow the MetalLB speaker to run on the nodes in the pool. MetalLB must be enabled in at least one node pool. If you don't include this flag, you must create another node pool to use for MetalLB.

For information about optional flags, see [Add a node pool](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/managing-node-pools#add_a_node_pool) and the [gcloud CLI reference](https://docs.cloud.google.com/sdk/gcloud/reference/container/vmware/node-pools/create).




### Example gcloud commands

### MetalLB & DHCP
    
    
    gcloud container vmware clusters create user-cluster-1 \
        --project=example-project-12345 \
        --location=us-west1 \
        --admin-cluster-membership=projects/example-project-12345/locations/us-west1/memberships/admin-cluster-1 \
        --version=1.36.200-gke.118 \
        --admin-users=sara@example.com \
        --admin-users=amal@example.com \
        --enable-dhcp \
        --service-address-cidr-blocks=10.96.0.0/20 \
        --pod-address-cidr-blocks=192.168.0.0/16 \
        --metal-lb-config-address-pools='pool=lb-pool-1,manual-assign=False,avoid-buggy-ips=True,addresses=192.0.2.0/26;pool=lb-ingress-vip-pool,manual-assign=True,addresses=198.51.100.1/32' \
        --enable-control-plane-v2 \
        --control-plane-vip=203.0.113.1 \
        --ingress-vip=198.51.100.1
    

### MetalLB & static IPs
    
    
    gcloud container vmware clusters create user-cluster-3 \
        --project=example-project-12345 \
        --location=europe-west1 \
        --admin-cluster-membership=projects/example-project-12345/locations/global/memberships/admin-cluster-1 \
        --version=1.36.200-gke.118 \
        --admin-users=sara@example.com \
        --admin-users=amal@example.com \
        --static-ip-config-ip-blocks='gateway=192.0.2.254,netmask=255.255.255.0,ips=192.0.2.10 user-vm-1;192.0.2.11 user-vm-2' \
        --static-ip-config-ip-blocks='gateway=192.0.2.254,netmask=255.255.255.0,ips=192.0.2.12 user-vm-3;192.0.2.13 extra-vm' \
        --dns-servers=203.0.113.1,203.0.113.2  \
        --dns-search-domains=example.com,altostrat.com \
        --ntp-servers=203.0.113.3,203.0.113.4 \
        --service-address-cidr-blocks=10.96.0.0/20 \
        --pod-address-cidr-blocks=192.168.0.0/16 \
        --enable-control-plane-v2 \
        --control-plane-ip-block 'gateway=192.0.2.254,netmask=255.255.255.0,ips=198.51.100.1 cp-vm-1;198.51.100.2 cp-vm-2;198.51.100.3 cp-vm-3' \
        --replicas=3 \
        --metal-lb-config-address-pools='pool=lb-pool-1,manual-assign=False,avoid-buggy-ips=True,addresses=192.0.2.0/26;lb-ingress-vip-pool,manual-assign=True,addresses=198.51.100.1/32' \
        --control-plane-vip=172.16.20.61 \
        --ingress-vip=172.16.20.62
    

### Manual LB & static IPs
    
    
    gcloud container vmware clusters create user-cluster-4 \
        --project=example-project-12345 \
        --location=asia-east1 \
        --admin-cluster-membership=projects/example-project-12345/locations/asia-east1/memberships/admin-cluster-1 \
        --version=1.36.200-gke.118 \
        --admin-users=sara@example.com \
        --admin-users=amal@example.com \
        --static-ip-config-ip-blocks='gateway=192.0.2.254,netmask=255.255.255.0,ips=192.0.2.10 user-vm-1;192.0.2.11 user-vm-2';ips=192.0.2.12 user-vm-3;192.0.2.13 extra-vm'\
        --dns-servers=203.0.113.1,203.0.113.2  \
        --ntp-servers=203.0.113.3,203.0.113.4 \
        --service-address-cidr-blocks=10.96.0.0/20 \
        --pod-address-cidr-blocks=192.168.0.0/16 \
        --enable-control-plane-v2 \
        --control-plane-ip-block 'gateway=192.0.2.254,netmask=255.255.255.0,ips=198.51.100.1 cp-vm-1;198.51.100.2 cp-vm-2;198.51.100.3 cp-vm-3' \
        --replicas=3 \
        --control-plane-vip=192.0.2.60 \
        --ingress-vip=192.0.2.50 \
        --ingress-http-node-port=30243 \
        --ingress-https-node-port=30879
    

### Terraform

### Before you begin

  1. Get the name and the fleet membership location of your admin cluster:
         
         gcloud container fleet memberships list \
             --project=FLEET_HOST_PROJECT_ID
         

Replace `FLEET_HOST_PROJECT_ID` with ID of the project that the admin cluster is registered to.

The output is similar to the following:
         
         NAME             EXTERNAL_ID                           LOCATION
         admin-cluster-1  bb7803b4-8438-4b22-859f-4559b4b29072  global
         admin-cluster-2  ee16ee2b-6ec0-49fc-9413-3c89cbc70854  global
         admin-cluster-3  fc2b7ef5-39ff-4b63-b919-04c5adc67be4  us-west1
         

The location specifies where the Fleet and Connect services run. Admin clusters created prior to 1.28 are managed by the global Fleet and Connect services. In 1.28 and later, you can specify either `global` or a Google Cloud region when you create the cluster.

  2. Get a list of available versions:
         
         gcloud container vmware clusters query-version-config \
             --admin-cluster-membership=ADMIN_CLUSTER_NAME \
             --admin-cluster-membership-project=FLEET_HOST_PROJECT_ID \
             --admin-cluster-membership-location=ADMIN_CLUSTER_REGION \
             --location=REGION
         

Replace the following:

     * `ADMIN_CLUSTER_NAME`: The name of the admin cluster.

     * `FLEET_HOST_PROJECT_ID`: The ID of the project that the admin cluster is registered to.

     * `ADMIN_CLUSTER_REGION`: The admin cluster's fleet membership region. This is either global or a Google Cloud region. Use the location for the admin cluster from the output of `gcloud container fleet memberships list`.

     * `REGION`: The Google Cloud region that you will use when you create the cluster. This is the region in which the GKE On-Prem API and the Fleet and Connect services run. Specify `us-west1` or another [supported region](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/reference/supported-regions-on-prem-api).

The output of the command is similar to the following:
    
    versions:
    - isInstalled: true
      version: 1.14.3-gke.25
    - version: 1.14.4-gke.54
    - version: 1.15.0-gke.581
    

The command also outputs an explanation of the versions that you can use for user cluster creation or upgrade. Allowable versions are annotated with `isInstalled: true`, which means the admin cluster has the version-specific components it needs to manage user clusters of that version. If you want to use a version that is installed on the admin cluster, skip to the Example section to create the user cluster.




### Install a different version

An admin cluster can manage user clusters at different versions. The output of the `query-version-config` command lists other versions that you can use when you create the cluster. If you want to create a user cluster that is a different version than the admin cluster, you need to download and deploy the components that the admin cluster needs to manage user clusters of that version, as follows:
    
    
    gcloud container vmware admin-clusters update ADMIN_CLUSTER_NAME \
        --project=FLEET_HOST_PROJECT_ID \
        --location=REGION \
        --required-platform-version=VERSION

Replace `VERSION` with one of the versions listed in the output of the `query-version-config` command.

The command downloads the version of the components that you specify in `--required-platform-version` to the admin cluster, and then deploys the the components. You can now create a user cluster with the specified version.

If you rerun the `gcloud container vmware clusters query-version-config`, the version that you specified is annotated with `isInstalled: true`.

### Example

You can use the following basic configuration sample to create a user cluster with the bundled MetalLB load balancer and one node pool using the Google provider for Terraform.

When you create a user cluster, the Terraform configuration file must contain at least one [`google_gkeonprem_vmware_node_pool`](https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/gkeonprem_vmware_node_pool) resource to create a node pool. Terraform can't create the node pool resource, however, until it has completed all operations on the upstream `google_gkeonprem_vmware_cluster` user cluster resource. To enforce this dependency, include a `depends_on` statement in the `google_gkeonprem_vmware_node_pool` resource as shown in the following example `main.tf` file. For more information about using `depends_on` for specifying resource dependencies, see the [Terraform resource documentation](https://developer.hashicorp.com/terraform/language/block/resource#depends_on).

To learn more about the example, click the following link:

#### `main.tf` for creating a user cluster

The example `main.tf` contains the following modules and resources: 

  * `enable_google_apis_primary`: enables the required Google APIs in the project. You only need to enable the APIs in a project once. If the APIs have already been enabled in your project, you don't need to include this in a Terraform configuration file. 
  * `google_project_service`: enables the GKE On-Prem API in the project. Like the other required Google APIs, you only need to enable the GKE On-Prem API once. 
  * `gcloud_update_admin_cluster_platform_controller`: updates the platform controller on your admin cluster. This is necessary for user cluster upgrades. If the admin cluster is already on the correct version, then this module doesn't change anything. Although this module is optional, user cluster creation fails if there is a version mismatch between the version of the platform controller on the admin cluster and the version you specify for the user cluster. 
  * `google_gkeonprem_vmware_cluster`: creates the user cluster. This resource is required. The user cluster is enrolled in the GKE On-Prem API and is registered to the same fleet as the admin cluster. The example creates the cluster using the bundled MetalLB. The [`google_gkeonprem_vmware_cluster` reference documentation](https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/gkeonprem_vmware_cluster) provides an example of configuring a manual load balancer. 
  * `google_gkeonprem_vmware_node_pool`: creates a node pool. This resource is required in the Terraform configuration file. A newly created user cluster must have at least one node pool to transition to a healthy state. 


    
    
    module "enable_google_apis_primary" {
      source     = "terraform-google-modules/project-factory/google//modules/project_services"
      version    = "~> 18.0"
      project_id = var.project_id
      activate_apis = [
        "cloudresourcemanager.googleapis.com",
        "anthos.googleapis.com",
        "anthosgke.googleapis.com",
        "container.googleapis.com",
        "gkeconnect.googleapis.com",
        "gkehub.googleapis.com",
        "serviceusage.googleapis.com",
        "stackdriver.googleapis.com",
        "monitoring.googleapis.com",
        "logging.googleapis.com",
        "iam.googleapis.com",
        "compute.googleapis.com",
        "anthosaudit.googleapis.com",
        "opsconfigmonitoring.googleapis.com",
        "file.googleapis.com",
        "connectgateway.googleapis.com"
      ]
      disable_services_on_destroy = false
    }
    
    # Enable GKE OnPrem API
    resource "google_project_service" "default" {
      project            = var.project_id
      service            = "gkeonprem.googleapis.com"
      disable_on_destroy = false
    }
    
    # This module is used to update the platform controller on your admin cluster. This
    # is a necessary step for the user cluster version update. If the admin cluster is
    # already on the correct version, then this module does not change anything
    module "gcloud_update_admin_cluster_platform_controller" {
      source                = "terraform-google-modules/gcloud/google"
      version               = "~> 3.0"
      platform              = "linux"
      create_cmd_entrypoint = "gcloud"
      create_cmd_body       = <<EOT
        beta container vmware admin-clusters               \
        update ${var.admin_cluster_name}                   \
        --required-platform-version=${var.on_prem_version} \
        --project ${var.project_id}                        \
        --location ${var.region}
      EOT
    }
    
    # Create an anthos vmware user cluster and enroll it with the gkeonprem API
    resource "google_gkeonprem_vmware_cluster" "default" {
      name        = var.cluster_name
      description = "Anthos VMware user cluster with MetalLB"
      provider    = google-beta
      depends_on = [
        google_project_service.default,
        module.gcloud_update_admin_cluster_platform_controller
      ]
      location                 = var.region
      on_prem_version          = var.on_prem_version
      admin_cluster_membership = "projects/${var.project_id}/locations/global/memberships/${var.admin_cluster_name}"
      network_config {
        service_address_cidr_blocks = ["10.96.0.0/12"]
        pod_address_cidr_blocks     = ["192.168.0.0/16"]
        dhcp_ip_config {
          enabled = true
        }
      }
      control_plane_node {
        cpus     = var.control_plane_node_cpus
        memory   = var.control_plane_node_memory
        replicas = var.control_plane_node_replicas
      }
      load_balancer {
        vip_config {
          control_plane_vip = var.control_plane_vip
          ingress_vip       = var.ingress_vip
        }
        metal_lb_config {
          dynamic "address_pools" {
            for_each = var.lb_address_pools
            content {
              pool      = address_pools.value.name
              addresses = address_pools.value.addresses
            }
          }
        }
      }
      authorization {
        dynamic "admin_users" {
          for_each = var.admin_user_emails
          content {
            username = admin_users.value
          }
        }
      }
    }
    
    # Create a node pool for the anthos vmware user cluster
    resource "google_gkeonprem_vmware_node_pool" "default" {
      name           = "${var.cluster_name}-nodepool"
      display_name   = "Nodepool for ${var.cluster_name}"
      provider       = google-beta
      vmware_cluster = google_gkeonprem_vmware_cluster.default.name
      location       = var.region
      config {
        replicas             = 3
        image_type           = "ubuntu_containerd"
        enable_load_balancer = true
      }
      depends_on = [
        google_gkeonprem_vmware_cluster.default
      ]
    }

For more information and other examples, see the [`google_gkeonprem_vmware_cluster` reference documentation](https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/gkeonprem_vmware_cluster).

### Set variables in `terraform.tfvars`

The sample provides an example variables file to pass in to `main.tf`, which shows how to configure the bundled MetalLB load balancer and enable your cluster nodes to get their IP addresses from a DHCP server that you provide.

  1. Clone the `anthos-samples` repository and change to the directory where the Terraform sample is located:
         
         git clone https://github.com/GoogleCloudPlatform/anthos-samples
         cd anthos-samples/anthos-onprem-terraform/avmw_user_cluster_metallb
         

  2. Make a copy of the `terraform.tfvars.sample` file:
         
         cp terraform.tfvars.sample terraform.tfvars
         

  3. Modify the parameters values in `terraform.tfvars`.
         
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

     * `region`: The Google Cloud region in which the GKE On-Prem API (`gkeonprem.googleapis.com`), Fleet service (`gkehub.googleapis.com`), and the Connect service (`gkeconnect.googleapis.com`) run. Specify `us-west1` or another [supported region](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/reference/supported-regions-on-prem-api).

     * `admin_cluster_name`: The name of the admin cluster that manages the user cluster. The example assumes that the admin cluster uses global as the region. If you have a regional admin cluster:

       1. Open `main.tf` in a text editor.
       2. Search for `admin_cluster_membership`, which looks like the following:
    
    admin_cluster_membership = "projects/${var.project_id}/locations/global/memberships/${var.admin_cluster_name}"

       1. Change `global` to the region that the admin cluster uses and save the file.
     * `on_prem_version`: The Google Distributed Cloud version for your user cluster.

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

  4. Save the changes in `terraform.tfvars`. If you don't want to make any optional changes to `main.tf`, skip to the section that follows, Create the cluster and one node pool.




### Configure Controlplane V2

In version 1.30 and higher, you must enable Controlplane V2. The `main.tf` file in the example doesn't enable Controlplane V2. You must change `main.tf` to enable Controlplane V2 and add the IP addresses for the gateway, netmask, and control-plane nodes. Before making changes, make a backup of `main.tf`:
    
    
      cp main.tf main.tf.bak
      

To configure Controlplane V2, make the following changes to `main.tf`:

  1. Add the following line to the `resource` block:
         
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
         

  3. Replace the values for `netmask` and `gateway` with IP addresses from your network. Replace `ip` and `hostname` with the IP addresses of your control plane nodes.




### Optional: Enable advanced cluster

By default in version 1.32 and higher, user clusters created using Terraform don't have advanced cluster enabled. If you want to enable advanced cluster, add the following top-level field to `main.tf`:
    
    
    enable_advanced_cluster = true
    

Be sure to review [Differences when running advanced clusters](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/concepts/advanced-clusters#adv-clusters-feature-support) before enabling advanced cluster.

### Optional: Worker node IP addressing mode

This section explains some optional configuration changes that you can make in `main.tf`. Before making changes, make a backup of `main.tf`:
    
    
    cp main.tf main.tf.bak
    

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




### Create the cluster and one node pool

  1. Initialize and create the Terraform plan:
         
         terraform init
         

Terraform installs any needed libraries, such as the Google Cloud provider. 

  2. Review the configuration and make changes if needed:
         
         terraform plan
         

  3. Apply the Terraform plan to create the user cluster:
         
         terraform apply
         

It takes about 15 minutes or more to create the user cluster, and another 15 minutes to create the node pool. You can view the cluster in the Google Cloud console on the [GKE clusters](https://console.cloud.google.com/kubernetes/list/overview) page.




### Optional: Run command-line tools before resource creation

If needed, you can run command-line tools such as the gcloud CLI and `gkectl` to perform setup or configuration tasks before resource creation. You define the command lines to run within the Terraform configuration file using the `local-exec` provisioner, which lets you reuse the defined Terraform variables.

The following example shows how to modify `main.tf` to run the `gkectl prepare` command before cluster creation:
    
    
    resource "null_resource" "gkectl_prepare" {
      provisioner "local-exec" {
        command = "gkectl prepare --kubeconfig=${var.kubeconfig} --cluster-name=${var.cluster_name} --vcenter-username=${var.vcenter_username} --vcenter-password=${var.vcenter_password} --vcenter-address=${var.vcenter_address} --datacenter=${var.datacenter} --datastore=${var.datastore} --network=${var.network} --os-image=${var.os_image} --service-account-key-file=${var.service_account_key_file} --location=${var.location}"
        working_dir = path.module  # Important: Set working directory
        environment = {
            # Optional: set environment variables if needed.
            # Example: GOOGLE_APPLICATION_CREDENTIALS = "/path/to/your/credentials.json"
        }
      }
    }
    
    resource "google_gkeonprem_vmware_cluster" "cluster" {
      # ... your cluster configuration ...
      # Ensure this depends on the null_resource
      depends_on = [null_resource.gkectl_prepare]
    
      # ... rest of your cluster configuration ...
      location = var.location
      name = var.cluster_name
      # ... other required fields ...
    }
    

## Troubleshooting

See [Troubleshooting cluster creation and upgrade](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/troubleshooting/create-upgrade).

## What's next

  * [Connect to your cluster from the Google Cloud console](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/connect-to-cluster-console).
  * [Deploy an application](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/deploy-first-app).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-21 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-21 UTC."],[],[]] 
