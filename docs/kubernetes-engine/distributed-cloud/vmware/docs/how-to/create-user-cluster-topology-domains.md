---
url: https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/create-user-cluster-topology-domains/
title: Create a user cluster for use with topology domains \u00a0|\u00a0 Google Distributed Cloud software only for VMware \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:57:27.073801+00:00
---

# Create a user cluster for use with topology domains  |  Google Distributed Cloud software only for VMware  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/create-user-cluster-topology-domains/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Google Distributed Cloud ](https://docs.cloud.google.com/distributed-cloud)
  * [ Documentation ](https://docs.cloud.google.com/kubernetes-engine/enterprise/clusters/docs)
  * [ GDC for VMware ](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs)
  * [ Guides ](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/overview)



Send feedback 

#  Create a user cluster for use with topology domains Stay organized with collections  Save and categorize content based on your preferences. 

**Preview**

This feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

In Google Distributed Cloud, your workloads run on one or more user clusters. This page shows how to create a user cluster for use in Google Distributed Cloud [topology domains](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/topology-domains-set-up). Google Distributed Cloud version 1.31 or higher is required to use topology domains.

Setting up a topology domain requires that you enable [advanced cluster](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/user-cluster-configuration-file-latest#enable-advanced-cluster-field). Note the following limitations with the advanced cluster preview:

  * You can enable advanced cluster at cluster creation time for new 1.31 clusters only.
  * After advanced cluster is enabled, you won't be able to upgrade the cluster to 1.32. Only enable advanced cluster in a test environment.



This page is for Admins, Architects, and Operators who set up, monitor, and manage the tech infrastructure. To learn more about common roles and example tasks that we reference in Google Cloud content, see [Common GKE user roles and tasks](https://docs.cloud.google.com/kubernetes-engine/enterprise/docs/concepts/roles-tasks).

## Before you begin

  * Make sure you have set up and can sign in to your admin workstation as described in [Create an admin workstation](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/create-admin-workstation). The admin workstation has the tools you need to create your user cluster. Do all the steps in this document on your admin workstation.

  * If you haven't already done so, set up your Google Cloud resources as described in these documents:

    * [Install the Google Cloud CLI](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/cloud-sdk)
    * [Create Cloud projects](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/multiple-gcp-projects)
    * [Create service accounts](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/service-accounts)
  * Before you create a user cluster, you must have an admin cluster to manage the user cluster. If you haven't already done so, create an [admin workstation](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/create-admin-workstation) and an [admin cluster for use with topology domains](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/create-admin-cluster-topology-domains).

  * Determine the version of the user cluster that you want to install. When you create a user cluster, you typically install the version that matches the version of the admin cluster. If you want to install a different version on a user cluster, see [Version rules](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/upgrade-overview#verson_rules).

  * Review the [IP addresses planning document](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/plan-ip-addresses), and ensure that you have enough IP addresses available.

  * Configure your load balancer for [manual load balancing](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/manual-load-balance). Your load balancer must be set up before you create the user cluster.

  * Think about how many [node pools](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/managing-node-pools) you need and which operating system you want to run in each of your pools.

  * Gather the information that you need to access each instance of vCenter Server. You need this information to fill in the [`Secret`](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/reference/vsphere-infrastructure-configuration-file#secret-section) section and the [`VSphereInfraConfig.credentials.vCenters`](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/reference/vsphere-infrastructure-configuration-file#credentials-vcenters-section) section in the vSphere infrastructure configuration file. See the following for how to obtain the needed information:

    * [vCenter user account privileges](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/vsphere-requirements#vcenter-user-account-privileges)
    * [Determine your vCenter server address](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/vcenter-server-address)
    * [Getting your vCenter CA root certificate](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/vcenter-ca-cert-path)



## Procedure overview

The following primary steps are involved in using `gkectl` to create a user cluster:

  1. Fill in your user cluster configuration file
    Specify the details for your new cluster in the user cluster configuration file.
  2. Fill in your IP block file
    Specify the IP addresses for the gateway, netmask, control-plane nodes, and optionally, worker nodes in an IP block file.
  3. Create a user cluster
    Run `gkectl create cluster` to create a cluster as specified in your configuration files.
  4. Verify that your user cluster is running
    Use `kubectl` to view your cluster nodes.



At the end of this procedure, you will have a running user cluster where you can deploy your workloads.

## Fill in your user cluster configuration file

If you used `gkeadm` to create your admin workstation, then `gkeadm` generated a template for your user cluster configuration file named `user-cluster.yaml`. Additionally, `gkeadm` filled in some of the fields for you.

If you didn't use `gkeadm` to create your admin workstation, you can use `gkectl` to generate a template for your user cluster configuration file.

To generate a template for your user cluster configuration file:
    
    
    gkectl create-config cluster --config=OUTPUT_FILENAME --gke-on-prem-version=VERSION
    

Replace the following:

`OUTPUT_FILENAME`: a path of your choice for the generated template. If you omit this flag, `gkectl` names the file `user-cluster.yaml` and puts it in the current directory.

`VERSION`: the desired version number. For example: `gkectl create-config cluster --gke-on-prem-version=1.36.100-gke.144`.

Familiarize yourself with the configuration file by scanning the [user cluster configuration file](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/user-cluster-configuration-file-latest) document. You might want to keep this document open in a separate tab or window, because you will refer to it as you complete the following steps.

### `name`

Set the [`name`](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/user-cluster-configuration-file-latest#name-field) field to a name of your choice for the user cluster.

### `gkeOnPremVersion`

This field is already filled in for you. It specifies the version of Google Distributed Cloud. For example, `1.36.100-gke.144`.

### `enableAdvancedCluster`

Set [`enableAdvancedCluster`](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/user-cluster-configuration-file-latest#enable-advanced-cluster-field) to `true`.

### `enableControlplaneV2`

Controlplane V2 is required for all 1.30 and higher user clusters. Set [`enableControlplaneV2`](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/user-cluster-configuration-file-latest#enablecontrolplanev2-field) to `true`.

When Controlplane V2 is enabled, the control plane for the user cluster runs on nodes in the user cluster itself.

### `enableDataplaneV2`

Set [enableDataplaneV2](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/user-cluster-configuration-file-latest#enabledataplanev2-field) to `true`.

### `vCenter`

Remove this entire section. Instead, you configure the vCenter information in the [vSphere infrastructure configuration file](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/reference/vsphere-infrastructure-configuration-file) per topology domain.

### `network`

  * Remove the following from the configuration file:

    * The entire `network.hostConfig` section. This information is configured in the vSphere infrastructure configuration file per topology domain.
    * The `network.vCenter.networkName` field. This field is configured in the vSphere infrastructure configuration file per topology domain.
    * The entire `network.controlPlaneIPBlock` section. The IP addresses for the gateway, netmask, and the control plane nodes are configured in an [IP block file](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/ip-block-file).
  * Set [`network.ipMode.ipBlockFilePath`](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/user-cluster-configuration-file-latest#network-ipmode.ipblockfilepath-field) to the path to the IP block file.

  * Decide how you want your worker nodes to get their IP addresses. The options are:

    * From a DHCP server that you set up ahead of time. Set `network.ipMode.type` to `"dhcp"`.

    * From a list of static IP addresses that you provide in the IP block file. Set `network.ipMode.type` to `"static"`.

The control-plane nodes for your user cluster must get their IP addresses from a list of static addresses that you provide in the IP block file. This is the case even if your worker nodes get their addresses from a DHCP server.

Regardless of whether you rely on a DHCP server or specify a list of static IP addresses, you need to have enough IP addresses available for your user cluster. For an explanation of how many IP addresses you need, see [Plan your IP addresses](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/plan-ip-addresses).

  * The [network.podCIDR](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/user-cluster-configuration-file-latest#network-podcidr-field) and [network.serviceCIDR](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/user-cluster-configuration-file-latest#network-servicecidr-field) have prepopulated values that you can leave unchanged unless they conflict with addresses already being used in your network. Kubernetes uses these ranges to assign IP addresses to Pods and Services in your cluster.




### `loadBalancer`

  * Set aside a VIP for the Kubernetes API server of your user cluster. Provide your VIP as the value for [`loadBalancer.vips.controlPlaneVIP`](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/user-cluster-configuration-file-latest#loadbalancer-vips-controlplanevip-field)

  * Set aside another VIP for the ingress service of your user cluster. Provide your VIP as the value for [`loadBalancer.vips.ingressVIP`](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/user-cluster-configuration-file-latest#loadbalancer-vips-ingressvip-field).

  * Set `loadBalancer.kind` to `"ManualLB"`, and fill in the [`manualLB`](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/user-cluster-configuration-file-latest#loadbalancer-manuallb-section) section. For more information, see [Manual load balancing](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/manual-load-balance).




### `advancedNetworking`

If you plan to create an [egress NAT gateway](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/egress-nat-gateway), set [advancedNetworking](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/user-cluster-configuration-file-latest#advancednetworking-field) to `true`.

### `multipleNetworkInterfaces`

Set [multipleNetworkInterfaces](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/user-cluster-configuration-file-latest#multiplenetworkinterfaces-field) to `false`. Multiple network interfaces for Pods aren't supported with topology domains.

### `storage`

Set [storage.vSphereCSIDisabled](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/user-cluster-configuration-file-latest#storagevspherecsidisabled) to `true` to disable the deployment of vSphere CSI components.

### `masterNode`

  * If you want to specify CPU and memory for the control-plane nodes of the user cluster, fill in the `cpus` and `memoryMB` fields in the [`masterNode`](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/user-cluster-configuration-file-latest#masternode-section) section.

  * Only highly-available (HA) clusters are supported. Set the `replicas` field to `3` to specify that the cluster will have three control-plane nodes.

  * To enable automatic resizing for the control-plane nodes, set `autoResize.enabled` to `true`.

  * Remove the entire [`masterNode.vsphere`](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/user-cluster-configuration-file-latest#masternode-vsphere-section) section.

  * Fill in the [`masterNode.topologyDomains`](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/user-cluster-configuration-file-latest#masternode-topology-domains-field) field with the name of the [topology domain](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/reference/vsphere-infrastructure-configuration-file#topology-domains-name) that you want the control plane nodes to be in.




### `nodePools`

A node pool is a group of worker nodes in a cluster that all have the same configuration. For example, you might want to set up a separate topology domain for each node pool. You must specify at least one node pool by filling in the [`nodePools`](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/user-cluster-configuration-file-latest#nodepools-section) section.

For each node pool that you specify:

  * Fill in the [`nodePools[i].topologyDomains`](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/user-cluster-configuration-file-latest#nodepool-topology-domains-field) field with the name of the [topology domain](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/reference/vsphere-infrastructure-configuration-file#topology-domains-name) that you want the node pool to be in.

  * Remove all fields in the `nodePools[i].vsphere` section except for `nodePools[i].vsphere.tags`. You specify this information in the vSphere infrastructure configuration file per topology domain.

  * Set the `nodePools[i].osImageType` to `ubuntu_cgv2`. 




For more general information about node pools, see [Node pools](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/node-pools) and [Creating and managing node pools](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/managing-node-pools).

### `antiAffinityGroups`

Set [`antiAffinityGroups.enabled`](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/user-cluster-configuration-file-latest#antiaffinitygroups-enabled-field) to `false`. [Distributed Resource Scheduler](https://techdocs.broadcom.com/us/en/vmware-cis/vsphere/vsphere-sdks-tools/9-1.html) (DRS) anti-affinity rules aren't supported with topology domains.

### `stackdriver`

Fill in the [`stackdriver`](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/user-cluster-configuration-file-latest#stackdriver-section) section to enable [Cloud Logging and Cloud Monitoring](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/concepts/logging-and-monitoring) for your cluster.

Note the following requirements:

  * The ID in `stackdriver.projectID` must be the same as the ID in `gkeConnect.projectID` and `cloudAuditLogging.projectID`.

  * The Google Cloud region set in `stackdriver.clusterLocation` must be the same as the region set in `cloudAuditLogging.clusterLocation` and `gkeConnect.location`. Additionally, if `gkeOnPremAPI.enabled` is `true`, the same region must be set in `gkeOnPremAPI.location`.




If the project IDs and regions aren't the same, cluster creation fails.

### `gkeConnect`

Your user cluster must be [registered to a Google Cloud fleet](https://docs.cloud.google.com/anthos/fleet-management/docs/fleet-creation).

Fill in the [`gkeConnect`](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/user-cluster-configuration-file-latest#gkeconnect-section) section to specify a [fleet host project](https://docs.cloud.google.com/anthos/fleet-management/docs/fleet-concepts#fleet-host-project) and an associated service account. The ID in `gkeConnect.projectID` must be the same as the ID set in `stackdriver.projectID` and `cloudAuditLogging.projectID`. If the project IDs aren't the same, cluster creation fails.

You can optionally specify a region where the fleet and Connect services run in `gkeConnect.location`. If you don't include this field, the cluster uses the global instances of these services.

**Important:** If you plan to install Cloud Service Mesh on a regional cluster, you must install version 1.19.3 or later.

If you include `gkeConnect.location` in your configuration file, the region that you specify must be the same as the region configured in `cloudAuditLogging.clusterLocation`, `stackdriver.clusterLocation`, and `gkeOnPremAPI.location`. If the regions aren't the same, cluster creation fails.

### `gkeOnPremAPI`

This section describes how clusters are [enrolled in the GKE On-Prem API](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/enroll-cluster).

The `gkectl` command line tool is the only available [cluster lifecycle management tool](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/cluster-lifecycle-management-tools) for clusters using topology domains. Although the Google Cloud console, the Google Cloud CLI, and Terraform aren't supported for clusters using topology domains, you can optionally enroll the cluster in the GKE On-Prem API when it is created.

If the GKE On-Prem API is enabled in your Google Cloud project, all clusters in the project are enrolled in the GKE On-Prem API automatically in the region configured in `stackdriver.clusterLocation`. The `gkeOnPremAPI.location` region must be the same as the region specified in `cloudAuditLogging.clusterLocation`, `gkeConnect.location`, and `stackdriver.clusterLocation`.

  * If you want to enroll all clusters in the project in the GKE On-Prem API, be sure to do the steps in [Before you begin](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/enroll-cluster#before_you_begin) to activate and use the GKE On-Prem API in the project.

  * If you don't want to enroll the cluster in the GKE On-Prem API, include this section and set `gkeOnPremAPI.enabled` to `false`. If you don't want to enroll any clusters in the project, disable `gkeonprem.googleapis.com` (the service name for the GKE On-Prem API) in the project. For instructions, see [Disabling services](https://docs.cloud.google.com/service-usage/docs/enable-disable#disabling).




### `cloudAuditLogging`

If you want to integrate the audit logs from your cluster's Kubernetes API server with [Cloud Audit Logs](https://docs.cloud.google.com/logging/docs/audit), fill in the [`cloudAuditLogging`](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/user-cluster-configuration-file-latest#cloudauditlogging-section) section.

Note the following requirements:

### # advanced-cluster-change #

Set `cloudAuditLogging.serviceAccountKeyPath` to the same path as `stackdriver.serviceAccountKeyPath`.

  * The ID in `cloudAuditLogging.projectID` must be the same as the ID in `gkeConnect.projectID` and `stackdriver.projectID`.

  * The region in `cloudAuditLogging.clusterLocation` must be the same as the region set in `gkeConnect.location` (if the field is included in your configuration file) and `stackdriver.clusterLocation`. Additionally, if `gkeOnPremAPI.enabled` is `true`, the same region must be set in `gkeOnPremAPI.location`.




If the project IDs and regions aren't the same, cluster creation fails.

### `preparedSecrets`

Remove the `preparedSecrets` field. [Prepared credentials](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/prepared-credentials-admin) aren't supported when topology domains is enabled.

### `schedulerConfiguration`

If you want to set up additional configurations that will be passed to `kube-scheduler`, add the [`schedulerConfiguration`](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/user-cluster-configuration-file-latest#scheduler-configuration-section) section to your configuration file.

### Example of filled-in configuration files

Here is an example of an IP block file and a user cluster configuration file:

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
      - netmask: 255.255.255.0
        gateway: 100.115.223.254
        ips:
        - ip: 100.115.222.205
          hostname: cp-1
          isControlPlane: true
        - ip: 100.115.222.206
          hostname: cp-2
          isControlPlane: true
        - ip: 100.115.222.207
          hostname: cp-3
          isControlPlane: true
    

#### user-cluster.yaml
    
    
    cat user-cluster.yaml
    apiVersion: v1
    kind: UserCluster
    name: "my-user-cluster"
    gkeOnPremVersion: 1.36.100-gke.144
    enableAdvancedCluster: true
    enableControlplaneV2: true
    enableDataplaneV2: true
    network:
      ipMode:
        type: "static"
        ipBlockFilePath: "user-ipblock.yaml"
      serviceCIDR: 10.96.0.0/20
      podCIDR: 192.168.0.0/16
    loadBalancer:
      vips:
        controlPlaneVIP: "100.115.222.200"
        ingressVIP: "172.16.21.30"
      kind: "ManualLB"
      manualLB:
        ingressHTTPNodePort: 32527
        ingressHTTPSNodePort: 30139
        controlPlaneNodePort: 30968
    masterNode:
      cpus: 4
      memoryMB: 8192
      replicas: 3
    nodePools:
    - name: "worker-node-pool1"
      cpus: 4
      memoryMB: 8192
      replicas: 3
      topologyDomains:
      - "domain1"
    antiAffinityGroups:
      enabled: false
    gkeConnect:
      projectID: "my-project-123"
      location: "us-central1"
      registerServiceAccountKeyPath: "connect-register-sa-2203040617.json"
    stackdriver:
      projectID: "my-project-123"
      clusterLocation: "us-central1"
      enableVPC: false
      serviceAccountKeyPath: "log-mon-sa-2203040617.json"
    autoRepair:
      enabled: true
    

These are the important points to understand in the preceding example:

  * The `nodePools.replicas` field is set to `3`, which means there are three worker nodes in `"worker-node-pool"`. All worker nodes use static IP addresses because `network.ipMode.type` is set to `"static"`.

  * The IP addresses for the control-plane nodes and worker nodes are specified in an IP block file. The IP block file has four addresses for worker nodes even though there are only three worker nodes. The extra worker node IP address is needed during cluster upgrade, update, and auto repair. The IP addresses for the control-plane nodes have the `isControlPlane: true` flag.

  * Advanced clusters, Controlplane V2, and Dataplane V2 are enabled.

  * The `masterNode.replicas` field is set to `3`, so the cluster will have a high-availability control plane.

  * The control-plane VIP is in the same VLAN as the control-plane nodes, and the ingress VIP is in the same VLAN as the worker nodes




## Fill in your IP block file

Copy the template for the [IP block file](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/ip-block-file) to the file in the directory that you specified in the `network.ipMode.ipBlockFilePath` field in the user cluster configuration file. Create separate IP block files for the admin cluster and for each user cluster.

Add the IP addresses for the gateway, netmask, and the control plane nodes to the IP block file. For each control-plane node IP address, add `isControlPlane: true` as shown in the previous example. If you want a high-availability (HA) user cluster, specify three IP addresses. Otherwise, specify one IP address. The number of IP addresses the you specify for control-plane nodes must match the number in the `masterNode.replicas` field in the user cluster configuration file.

If `network.ipMode.type` is set to `"static"`, add the IP addresses for the worker nodes to the IP block file. Be sure to specify one additional IP address for use during cluster upgrade, update, and auto repair.

Each gateway address in the IP block file must match the address specified in a `topologyDomains[i].network.gateway` field in the vSphere infrastructure configuration file. For more information, see [example for topology domains](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/ip-block-file#example_2).

## Create a user cluster

Run the following command to create a user cluster:
    
    
    gkectl create cluster --kubeconfig ADMIN_CLUSTER_KUBECONFIG --config USER_CLUSTER_CONFIG
    

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
    

## Configure your `PodTemplate`

The topology label is populated to labels of nodes in the topology domain. Unless your topology domain setup used the default constraint, [`"topology.kubernetes.io/zone"`](https://kubernetes.io/docs/reference/labels-annotations-taints/#topologykubernetesiozone) as the topology key, you need to configure the topology key in the pod template of your Deployment, StatefulSet, or ReplicaSet, as applicable.

For example, suppose you defined the key in the topology label as `"topology.examplepetstore.com/zone"`. In the `PodTemplate`, you specify the key as the value for the `topologySpreadConstraints.topologyKey` field. This lets the Kubernetes scheduler distribute Pods across the topology domain to ensure high availability and prevent over-concentration in any single area in case of failure.

## Troubleshooting

See [Troubleshooting cluster creation and upgrade](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/troubleshooting/create-upgrade).

## What's next

  * [Connect to your cluster from the Google Cloud console](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/connect-to-cluster-console).
  * [Deploy an application](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/deploy-first-app).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-14 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-14 UTC."],[],[]] 
