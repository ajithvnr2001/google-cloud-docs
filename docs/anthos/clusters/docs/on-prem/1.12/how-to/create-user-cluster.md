---
url: https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.12/how-to/create-user-cluster/
title: Create a user cluster \u00a0|\u00a0 Anthos clusters on VMware \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-15T03:06:32.420766+00:00
---

# Create a user cluster  |  Anthos clusters on VMware  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.12/how-to/create-user-cluster/

**Version 1.12**. This version is no longer supported. For more information see the [ version support policy](https://cloud.google.com/anthos/clusters/docs/on-prem/latest/getting-support#version_support_policy). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Google Kubernetes Engine (GKE) ](https://docs.cloud.google.com/kubernetes-engine)
  * [ GKE Enterprise ](https://docs.cloud.google.com/kubernetes-engine/enterprise/docs)
  * [ Clusters ](https://docs.cloud.google.com/anthos/clusters)
  * [ Documentation ](https://docs.cloud.google.com/anthos/clusters/docs)
  * [ Anthos clusters on VMware 1.12 ](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.12)
  * [ Guides ](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.12/overview)



Send feedback 

#  Create a user cluster Stay organized with collections  Save and categorize content based on your preferences. 

Version 1.12 keyboard_arrow_down

  * [ Latest version ](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/latest/how-to/create-user-cluster)
  * [ Version 1.16 ](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.16/how-to/create-user-cluster)
  * [ Earlier versions (unsupported) ](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/latest/version-history#expandable-1)



This document shows how to create a user cluster for Google Distributed Cloud. A user cluster is a place where you can run your workloads. Each user cluster is associated with an admin cluster.

For more details about admin clusters and user clusters, see the [installation overview](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.12/how-to/install-overview).

## Procedure overview

These are the primary steps involved in creating a user cluster:

  1. Connect to your admin workstation
    The admin workstation is a VM that has the necessary tools for creating a user cluster.
  2. Fill in your configuration files
    Specify the details for your new cluster by completing a user cluster configuration file, a credentials configuration file, and possibly an IP block file.
  3. (Optional) Create a Seesaw load balancer
    If you have chosen to use the Seesaw loadbalancer, run `gkectl create loadbalancer`.
  4. Create a user cluster
    Run `gkectl create cluster` to create a cluster as specified in your configuration file.
  5. Verify that your user cluster is running
    Use `kubectl` to view your cluster nodes.



At the end of this procedure, you will have a running user cluster where you can deploy your workloads.

## Before you begin

  * Ensure that you have created an [admin workstation](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.12/how-to/create-admin-workstation) and an [admin cluster](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.12/how-to/create-admin-cluster).

  * Review the [IP addresses planning document](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.12/how-to/plan-ip-addresses). Ensure that you have enough IP addresses available, and revisit your decision about how you want your cluster nodes to get their IP addresses: DHCP or static. If you decide to use static IP addresses, you must fill in an [IP block file](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.12/how-to/ip-block-file) that contains your chosen addresses.

  * Review the [load balancing overview](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.12/how-to/setup-load-balance) and revisit your decision about the kind of load balancer you want to use. For certain load balancers, you must set up the load balancer before you create your user cluster.

  * Look ahead at the vcenter section. Think about whether you want to use separate vSphere clusters for your admin cluster and user clusters, and whether you want to use separate data centers. The option to have separate vSphere clusters is in preview for 1.12.0 and GA for 1.12.1. 

  * Look ahead at the nodePools section. Think about how many node pools you need and which operating system you want to run in each of your pools.




## 1\. Connect to your admin workstation

[Get an SSH connection](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.12/how-to/create-admin-workstation#getting_an_ssh_connection_to_your_admin_workstation) to your admin workstation.

Recall that `gkeadm` activated your component access service account on the admin workstation.

Do all the remaining steps in this topic on your admin workstation in the home directory.

## 2\. Fill in your configuration file

When `gkeadm` created your admin workstation, it generated a configuration file named `user-cluster.yaml`. This configuration file is for creating your user cluster.

Familiarize yourself with the configuration file by scanning the [user cluster configuration file](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.12/how-to/user-cluster-configuration-file) document. You might want to keep this document open in a separate tab or window, because you will refer to it as you complete the following steps.

### `name`

Set the [`name`](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.12/how-to/user-cluster-configuration-file#name-field) field to a name of your choice for the user cluster.

### `gkeOnPremVersion`

This field is already filled in for you. It specifies the version of Google Distributed Cloud. For example, `1.11.0-gke.543`

### `vCenter`

The values you set in the `vCenter` section of your [admin cluster configuration file](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.12/how-to/admin-cluster-configuration-file) are global. That is, they apply to your admin cluster and its associated user clusters.

For each user cluster that you create, you have the option of overriding some of the global `vCenter` values.

To override any of the global `vCenter` values, fill in the relevant fields in the [`vCenter`](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.12/how-to/user-cluster-configuration-file#vcenter-section) section of your user cluster configuration file.

In particular, you might want to use separate vSphere clusters for your admin cluster and user clusters, and you might want to use separate data centers for your admin cluster and user clusters.

#### Use one data center and one vSphere cluster

The default option is to use one data center and one vSphere cluster for both the admin cluster and any user clusters. The values in the admin cluster configuration file are used for the user cluster as well. Do not set any `vCenter` values in the user cluster configuration file.

#### Create a user cluster in a separate vSphere cluster

This feature is in preview for version 1.12.0 and is GA for 1.12.1.

If you want to create a user cluster that is in its own vSphere cluster, specify a value for `vCenter.cluster` in the user cluster configuration file.

If your admin cluster and user cluster are in separate vSphere clusters, they can be in the same data center or different data centers.

#### Create a user cluster with a separate data center

The user cluster and admin cluster can be in different [data centers](https://docs.vmware.com/en/VMware-vSphere/7.0/com.vmware.vsphere.vcenterhost.doc/GUID-7FDFBDBE-F8AC-4D00-AE5E-3F14D7472FAF.html). In that case, they are also in separate vSphere clusters.

If you specify `vCenter.datacenter` in the user cluster configuration file, then you must also specify `vCenter.datastore` and `vCenter.networkName`, and you must specify either `vCenter.cluster` or `vCenter.resourcePool`.

To use different data centers for the admin cluster and user cluster, we recommend that you create a separate [datastore](https://docs.vmware.com/en/VMware-vSphere/7.0/com.vmware.vsphere.storage.doc/GUID-D5AB2BAD-C69A-4B8D-B468-25D86B8D39CE.html) for each user cluster control plane in the admin cluster data center, so that the admin cluster control plane and the user cluster control planes have isolated datastore failure domains. Although you can use the admin cluster datastore for user cluster control-plane nodes, that puts the user cluster control-plane nodes and the admin cluster into the same datastore failure domain.

#### Different vCenter account for a user cluster in its own data center

A user cluster can use a different vCenter account, with different `vCenter.credentials`, from the admin cluster. The vCenter account for the admin cluster needs access to the admin cluster data center, while the vCenter account for the user cluster only needs access to the user cluster datacenter.

### `network`

Decide how you want your cluster nodes to get their IP addresses. The options are:

  * From a DHCP server that you set up ahead of time. Set `network.ipMode.type` to `"dhcp"`.

  * From a list of static IP addresses that you provide. Set `network.ipMode.type` to `"static"`, and create an [IP block file](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.12/how-to/ip-block-file) that provides the static IP addresses. For an example of an IP block file, see Example of filled-in configuration files.




Fill in the rest of the fields in the [network](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.12/how-to/user-cluster-configuration-file#network-section) section as needed:

  * If you have decided to use static IP addresses for your user cluster nodes, the [`network.ipMode.ipBlockFilePath`](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.12/how-to/user-cluster-configuration-file#network-ipmode.ipblockfilepath-field) field and the [`network.hostconfig`](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.12/how-to/user-cluster-configuration-file#network-hostconfig-section) section are required. The `network.hostconfig` section holds information about NTP servers, DNS servers, and DNS search domains used by your cluster nodes.

If you are using the Seesaw load balancer, the `network.hostconfig` section is required even if you intend to use DHCP for your cluster nodes.

  * The [network.podCIDR](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.12/how-to/user-cluster-configuration-file#network-podcidr-field%7D) and [network.serviceCIDR](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.12/how-to/user-cluster-configuration-file#network-servicecidr-field) have prepopulated values that you can leave unchanged unless they conflict with addresses already being used in your network. Kubernetes uses these ranges to assign IP addresses to Pods and Services in your cluster.




Regardless of whether you rely on a DHCP server or specify a list of static IP addresses, you need to have enough IP addresses available for your user cluster. This includes the nodes in your user cluster and the nodes in the admin cluster that run the control plane for your user cluster. For an explanation of how many IP addresses you need, see [Plan your IP addresses](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.12/how-to/plan-ip-addresses).

#### Firewall rules for a user cluster with a separate `network.vCenter.networkName` value

In their respective configuration files, the admin cluster and the user cluster can use separate `network.vCenter.networkName` values that represent different VLANs and different datacenters. However, the following cross-VLAN communication must be allowed.

  * User nodes can access ports 443 and 8132 on the user cluster control-plane VIP address and get return packets from them.



### `loadBalancer`

Set aside a VIP for the Kubernetes API server of your user cluster. Set aside another VIP for the ingress service of your user cluster. Provide your VIPs as values for [`loadBalancer.vips.controlPlaneVIP`](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.12/how-to/user-cluster-configuration-file#loadbalancer-vips-controlplanevip-field) and [`loadBalancer.vips.ingressVIP`](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.12/how-to/user-cluster-configuration-file#loadbalancer-vips-ingressvip-field).

For more information, see [VIPs in the user cluster subnet](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.12/how-to/plan-ip-addresses#example_ip_addresses_vips_in_the_user_cluster_1_subnet) and [VIPs in the admin cluster subnet](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.12/how-to/plan-ip-addresses#example_ip_addresses_vips_in_the_admin_cluster_subnet).

Decide what type of load balancing you want to use. The options are:

  * MetalLB bundled load balancing. Set [`loadBalancer.kind`](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.12/how-to/user-cluster-configuration-file#loadbalancerkind) to `"MetalLB"`. Also fill in the [`loadBalancer.metalLB.addressPools`](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.12/how-to/user-cluster-configuration-file#loadbalancer-metallb-section) section, and set `enableLoadBalancer` to `true` for at least one of your node pools. For more information, see [Bundled load balancing with MetalLB](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.12/how-to/bundled-load-balance-metallb).

  * Seesaw bundled load balancing. Set `loadBalancer.kind` to `"Seesaw"`, and fill in the [`loadBalancer.seesaw`](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.12/how-to/user-cluster-configuration-file#loadbalancer-seesaw-section) section. For more information, see [Bundled load balancing with Seesaw](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.12/how-to/bundled-load-balance).

  * Integrated load balancing with F5 BIG-IP. Set `loadBalancer.kind` to `"F5BigIP"`, and fill in the [`f5BigIP`](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.12/how-to/user-cluster-configuration-file#loadbalancer-f5bigip-section) section. For more information, see [Load balancing with F5 BIG-IP](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.12/how-to/f5-big-ip-load-balance).

  * Manual load balancing. Set `loadBalancer.kind` to `"ManualLB"`, and fill in the [`manualLB`](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.12/how-to/user-cluster-configuration-file#loadbalancer-manuallb-section) section. For more information, see [Manual load balancing](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.12/how-to/manual-load-balance).




For more information about load balancing options, see [Overview of load balancing](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.12/how-to/setup-load-balance).

### `enableDataplaneV2`

Decide whether you want to enable [Dataplane V2](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/dataplane-v2) for your user cluster, and set [enableDataplaneV2](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.12/how-to/user-cluster-configuration-file#enabledataplanev2-field) accordingly.

### `enableWindowsDataplaneV2`

If you plan to have a [Windows node pool](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.12/how-to/user-guide-for-windows-server-os-node-pools), decide whether you want to enable Windows Dataplane V2, and set [enableWindowsDataplaneV2](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.12/how-to/user-cluster-configuration-file#enablewindowsdataplanev2-field) accordingly.

### `advancedNetworking`

If you plan to create an [egress NAT gateway](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.12/how-to/egress-nat-gateway), set [advancedNetworking](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.12/how-to/user-cluster-configuration-file#advancednetworking-field) to `true`.

### `multipleNetworkInterfaces`

Decide whether you want to configure [multiple network interfaces](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.12/how-to/multi-nic) for Pods, and set [multipleNetworkInterfaces](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.12/how-to/user-cluster-configuration-file#multiplenetworkinterfaces-field) accordingly.

### `storage`

If you want to disable the deployment of vSphere CSI components, set [storage.vSphereCSIDisabled](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.12/how-to/user-cluster-configuration-file#storage-vspherecsidisabled-field) to `true`.

### `masterNode`

The control plane for your user cluster runs on nodes in the admin cluster.

In the [`masterNode`](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.12/how-to/user-cluster-configuration-file#masternode-section) section, you can specify how many control-plane nodes you want for your user cluster. You can also specify a datastore for the control-plane nodes and whether you want to enable automatic resizing for the nodes.

### `nodePools`

A node pool is a group of nodes in a cluster that all have the same configuration. For example, the nodes in one pool could run Windows and the nodes in another pool could run Linux.

You must specify at least one node pool by filling in the [`nodePools`](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.12/how-to/user-cluster-configuration-file#nodepools-section) section.

For more information, see [Node pools](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/node-pools) and [Creating and managing node pools](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.12/how-to/managing-node-pools).

### `antiAffinityGroups`

Set [`antiAffinityGroups.enabled`](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.12/how-to/user-cluster-configuration-file#antiaffinitygroups-enabled-field) to `true` or `false`.

This field specifies whether Google Distributed Cloud creates [Distributed Resource Scheduler](https://www.vmware.com/products/vsphere/drs-dpm.html) (DRS) anti-affinity rules for your user cluster nodes, causing them to be spread across at least three physical hosts in your data center.

### `stackdriver`

If you want to enable [Cloud Logging and Cloud Monitoring](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.12/concepts/logging-and-monitoring) for your cluster, fill in the [`stackdriver`](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.12/how-to/user-cluster-configuration-file#stackdriver-section) section.

### `gkeConnect`

Your user cluster must be [registered to a Google Cloud fleet](https://docs.cloud.google.com/anthos/fleet-management/docs/fleet-creation).

Fill in the [`gkeConnect`](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.12/how-to/user-cluster-configuration-file#gkeconnect-section) section to specify a [fleet host project](https://docs.cloud.google.com/anthos/fleet-management/docs/fleet-concepts#fleet-host-project) and an associated service account.

### `usageMetering`

If you want to enable usage metering for your cluster, then fill in the [`usageMetering`](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.12/how-to/user-cluster-configuration-file#usagemetering-section) section.

### `cloudAuditLogging`

If you want to integrate the audit logs from your cluster's Kubernetes API server with [Cloud Audit Logs](https://docs.cloud.google.com/logging/docs/audit), fill in the [`cloudAuditLogging`](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.12/how-to/user-cluster-configuration-file#cloudauditlogging-section) section.

### Example of filled-in configuration files

Here is an example of a filled-in IP block file and a filled-in user cluster configuration file. The configuration enables some, but not all, of the available features.

#### vc-01-ipblock-user.yaml
    
    
    blocks:
      - netmask: 255.255.252.0
        gateway: 172.16.23.254
        ips:
        - ip: 172.16.20.21
          hostname: user-host1
        - ip: 172.16.20.22
          hostname: user-host2
        - ip: 172.16.20.23
          hostname: user-host3
        - ip: 172.16.20.24
          hostname: user-host4
        - ip: 172.16.20.25
          hostname: user-host5
        - ip: 172.16.20.26
          hostname: user-host6
    

#### vc-01-user-cluster.yaml
    
    
    apiVersion: v1
    kind: UserCluster
    name: "gke-user-01"
    gkeOnPremVersion: 1.11.0-gke.543
    network:
      hostConfig:
        dnsServers:
        - "203.0.113.1"
        - "198.51.100.1"
        ntpServers:
        - "216.239.35.4"
      ipMode:
        type: dhcp
        ipBlockFilePath: "vc-01-ipblock-user.yaml"
      serviceCIDR: 10.96.0.0/20
      podCIDR: 192.168.0.0/16
      vCenter:
        networkName: "vc01-net-1"
    loadBalancer:
      vips:
        controlPlaneVIP: "172.16.20.32"
        ingressVIP: "172.16.21.30"
      kind: "MetalLB"
       metalLB:
        addressPools:
        - name: "gke-address-pool-01"
          addresses:
          - "172.16.21.30 - 172.16.21.39"
    enableDataplaneV2: true
    masterNode:
      cpus: 4
      memoryMB: 8192
      replicas: 1
    nodePools:
    - name: "gke-node-pool-01"
      cpus: 4
      memoryMB: 8192
      replicas: 3
      osImageType: "ubuntu_containerd"
    antiAffinityGroups:
      enabled: true
    gkeConnect:
      projectID: "my-project-123"
      registerServiceAccountKeyPath: "connect-register-sa-2203040617.json"
    stackdriver:
      projectID: "my-project-123"
      clusterLocation: "us-central1"
      enableVPC: false
      serviceAccountKeyPath: "log-mon-sa-2203040617.json"
    autoRepair:
      enabled: true
    

### Validate your configuration file

After you've filled in your user cluster configuration file, run `gkectl check-config` to verify that the file is valid:
    
    
    gkectl check-config --kubeconfig ADMIN_CLUSTER_KUBECONFIG --config USER_CLUSTER_CONFIG
    

Replace the following:

  * ADMIN_CLUSTER_KUBECONFIG: the path of the kubeconfig file for your admin cluster

  * USER_CLUSTER_CONFIG: the path of your user cluster configuration file




If the command returns any failure messages, fix the issues and validate the file again.

If you want to skip the more time-consuming validations, pass the `--fast` flag. To skip individual validations, use the `--skip-validation-xxx` flags. To learn more about the `check-config` command, see [Running preflight checks](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.12/how-to/preflight-checks).

## 3\. (Optional) Create a Seesaw load balancer for your user cluster

If you have chosen to use the bundled Seesaw load balancer, do the step in this section. Otherwise, skip this section.

Create and configure the VMs for your [Seesaw load balancer](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.12/how-to/bundled-load-balance):
    
    
    gkectl create loadbalancer --kubeconfig ADMIN_CLUSTER_KUBECONFIG --config USER_CLUSTER_CONFIG
    

## 4\. Create a user cluster

#### Create a user cluster:
    
    
    gkectl create cluster --kubeconfig ADMIN_CLUSTER_KUBECONFIG --config USER_CLUSTER_CONFIG 
    

#### Locate the user cluster kubeconfig file

The `gkectl create cluster` command creates a kubeconfig file named `USER_CLUSTER_NAME-kubeconfig` in the current directory. You will need this kubeconfig file later to interact with your user cluster.

If you like, you can change the name and location of your kubeconfig file.

## 5\. Verify that your user cluster is running

Verify that your user cluster is running:
    
    
    kubectl get nodes --kubeconfig USER_CLUSTER_KUBECONFIG
    

Replace USER_CLUSTER_KUBECONFIG with the path of your user cluster kubeconfig file.

The output shows the user cluster nodes. For example:
    
    
    my-user-cluster-node-pool-69-d46d77885-7b7tx   Ready ...
    my-user-cluster-node-pool-69-d46d77885-lsvzk   Ready ...
    my-user-cluster-node-pool-69-d46d77885-sswjk   Ready ...
    

## Troubleshooting

See [Troubleshooting cluster creation and upgrade](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.12/troubleshoot-cluster-creation-upgrade).

## What's next

  * [Connect to your cluster from the Google Cloud console](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.12/how-to/connecting-to-a-cluster).
  * [Deploy an application](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.12/how-to/deploy-first-app).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
