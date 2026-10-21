---
url: https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.15/how-to/create-user-cluster-controlplane-v2/
title: Create a user cluster (Controlplane V2) \u00a0|\u00a0 Google Distributed Cloud Virtual for VMware \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T17:11:53.281648+00:00
---

# Create a user cluster (Controlplane V2)  |  Google Distributed Cloud Virtual for VMware  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.15/how-to/create-user-cluster-controlplane-v2/

**Version 1.15**. This version is no longer supported. For more information see the [ version support policy](https://cloud.google.com/anthos/clusters/docs/on-prem/latest/getting-support#version_support_policy). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Google Distributed Cloud ](https://docs.cloud.google.com/distributed-cloud)
  * [ Documentation ](https://docs.cloud.google.com/kubernetes-engine/enterprise/clusters/docs)
  * [ GDCV for VMware 1.15 ](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.15)
  * [ Guides ](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.15/overview)



Send feedback 

#  Create a user cluster (Controlplane V2) Stay organized with collections  Save and categorize content based on your preferences. 

Version 1.15 keyboard_arrow_down

  * [ Latest version ](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/latest/how-to/create-user-cluster-controlplane-v2)
  * [ Version 1.16 ](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.16/how-to/create-user-cluster-controlplane-v2)
  * [ Earlier versions (unsupported) ](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/latest/version-history#expandable-1)



This document shows how to create a user cluster with Controlplane V2 enabled.

With Controlplane V2, the control plane for a user cluster runs on one or more nodes in the user cluster itself. Controlplane V2 is the default and recommended setting for cluster creation.

## Procedure overview

These are the primary steps involved in creating a user cluster:

  1. Connect to your admin workstation
    The admin workstation is a VM that has the necessary tools for creating a user cluster.
  2. Fill in your configuration files
    Specify the details for your new cluster by completing a user cluster configuration file, a credentials configuration file, and possibly an IP block file.
  3. (Optional) Import OS images to vSphere, and push container images to the
private registry if applicable.
    Run `gkectl prepare`.
  4. Create a user cluster
    Run `gkectl create cluster` to create a cluster as specified in your configuration file.
  5. Verify that your user cluster is running
    Use `kubectl` to view your cluster nodes.



At the end of this procedure, you will have a running user cluster where you can deploy your workloads.

## Before you begin

  * Ensure that you have created an [admin workstation](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.15/how-to/create-admin-workstation) and an [admin cluster](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.15/how-to/create-admin-cluster).

  * Review the [IP addresses planning document](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.15/how-to/plan-ip-addresses). Ensure that you have enough IP addresses available, and revisit your decision about how you want your cluster nodes to get their IP addresses: DHCP or static. If you decide to use static IP addresses, you must fill in an [IP block file](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.15/how-to/ip-block-file) that contains your chosen addresses.

  * Review the [load balancing overview](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.15/how-to/setup-load-balance) and revisit your decision about the kind of load balancer you want to use. You can use the bundled MetalLB load balancer, or you can manually configure a load balancer of your choice. For manual load balancing, you must set up the load balancer before you create your user cluster.

  * Look ahead at the vCenter section. Think about whether you want to use separate vSphere clusters for your admin cluster and user clusters, and whether you want to use separate data centers. Also think about whether you want to use separate instances of vCenter Server.

  * Look ahead at the nodePools section. Think about how many node pools you need and which operating system you want to run in each of your pools.




## 1\. Connect to your admin workstation

[Get an SSH connection](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.15/how-to/create-admin-workstation#getting_an_ssh_connection_to_your_admin_workstation) to your admin workstation.

Recall that `gkeadm` activated your component access service account on the admin workstation.

Do all the remaining steps in this topic on your admin workstation in the home directory.

## 2\. Fill in your configuration file

When `gkeadm` created your admin workstation, it generated a configuration file named `user-cluster.yaml`. This configuration file is for creating your user cluster.

Familiarize yourself with the configuration file by scanning the [user cluster configuration file](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.15/how-to/user-cluster-configuration-file) document. You might want to keep this document open in a separate tab or window, because you will refer to it as you complete the following steps.

### `name`

Set the [`name`](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.15/how-to/user-cluster-configuration-file#name-field) field to a name of your choice for the user cluster.

### `gkeOnPremVersion`

This field is already filled in for you. It specifies the version of Google Distributed Cloud. For example, `1.15.0-gke.581`

### `enableControlplaneV2`

Set [`enableControlplaneV2`](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.15/how-to/user-cluster-configuration-file#enablecontrolplanev2-field) to `true`.

### `enableDataplaneV2`

Set [enableDataplaneV2](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.15/how-to/user-cluster-configuration-file#enabledataplanev2-field) to `true`.

### `vCenter`

The values you set in the `vCenter` section of your [admin cluster configuration file](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.15/how-to/admin-cluster-configuration-file) are global. That is, they apply to your admin cluster and its associated user clusters.

For each user cluster that you create, you have the option of overriding some of the global `vCenter` values.

To override any of the global `vCenter` values, fill in the relevant fields in the [`vCenter`](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.15/how-to/user-cluster-configuration-file#vcenter-section) section of your user cluster configuration file.

In particular, you might want to use separate vSphere clusters for your admin cluster and user clusters, and you might want to use separate data centers for your admin cluster and user clusters.

#### Using one data center and one vSphere cluster

The default option is to use one data center and one vSphere cluster for the admin cluster and the user cluster. For this option, do not set any `vCenter` values in the user cluster configuration file. The `vCenter` values will be inherited from the admin cluster.

#### Using separate vSphere clusters

If you want to create a user cluster that is in its own vSphere cluster, specify a value for `vCenter.cluster` in the user cluster configuration file.

If your admin cluster and user cluster are in separate vSphere clusters, they can be in the same data center or different data centers.

#### Using separate vSphere data centers

The user cluster and admin cluster can be in different [data centers](https://docs.vmware.com/en/VMware-vSphere/7.0/com.vmware.vsphere.vcenterhost.doc/GUID-7FDFBDBE-F8AC-4D00-AE5E-3F14D7472FAF.html). In that case, they are also in separate vSphere clusters.

If you specify `vCenter.datacenter` in the user cluster configuration file, then you must also specify `vCenter.datastore` and `vCenter.networkName`, and you must specify either `vCenter.cluster` or `vCenter.resourcePool`.

#### Using separate vCenter accounts

A user cluster can use a different vCenter account, with different `vCenter.credentials`, from the admin cluster. The vCenter account for the admin cluster needs access to the admin cluster data center, while the vCenter account for the user cluster only needs access to the user cluster data center.

#### Using separate instances of vCenter Server

In certain situations, it makes sense to create a user cluster that uses its own instance of vCenter Server. That is, the admin cluster and an associated user cluster use different instances of vCenter Server.

For example, in an edge location, you might want to have a physical machine running vCenter Server and one or more physical machines running ESXi. You could then use your local instance of vCenter Server to create a vSphere object hierarchy, including data centers, clusters, resource pools, datastores, and folders.

Fill in the entire [`vCenter`](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.15/how-to/user-cluster-configuration-file#vcenter-section) section of your user cluster configuration file. In particular, specify a value for `vCenter.address` that is different from the vCenter Server address you specified in the admin cluster configuration file. For example:
    
    
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
    

Also fill in the [`network.vCenter.networkName`](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.15/how-to/user-cluster-configuration-file#network-vcenter-networkname-field) field.

### `network`

Decide how you want your worker nodes to get their IP addresses. The options are:

  * From a DHCP server that you set up ahead of time. Set `network.ipMode.type` to `"dhcp"`.

  * From a list of static IP addresses that you provide. Set `network.ipMode.type` to `"static"`, and create an [IP block file](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.15/how-to/ip-block-file) that provides the static IP addresses. For an example of an IP block file, see Example of filled-in configuration files.




If you have decided to use static IP addresses for your worker nodes, fill in the [`network.ipMode.ipBlockFilePath`](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.15/how-to/user-cluster-configuration-file#network-ipmode.ipblockfilepath-field) field.

The control-plane nodes for your user cluster must get their IP addresses from a list of static addresses that you provide. This is the case even if your worker nodes get their addresses from a DHCP server. To specify static IP addresses for your control-plane nodes, fill in the [`network.controlPlaneIPBlock`](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.15/how-to/user-cluster-configuration-file#network-controlplaneipblock-section) section. If you want a high-availability (HA) user cluster, specify three IP addresses. Otherwise, specify one IP address.

Specify DNS and NTP servers by filling in the `hostConfig` section. These DNS and NTP servers are for the control-plane nodes. If you are using static IP addresses for your worker nodes, then these DNS and NTP servers are also for the worker nodes.

The [network.podCIDR](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.15/how-to/user-cluster-configuration-file#network-podcidr-field) and [network.serviceCIDR](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.15/how-to/user-cluster-configuration-file#network-servicecidr-field) have prepopulated values that you can leave unchanged unless they conflict with addresses already being used in your network. Kubernetes uses these ranges to assign IP addresses to Pods and Services in your cluster.

Regardless of whether you rely on a DHCP server or specify a list of static IP addresses, you need to have enough IP addresses available for your user cluster. For an explanation of how many IP addresses you need, see [Plan your IP addresses](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.15/how-to/plan-ip-addresses).

### `loadBalancer`

Set aside a VIP for the Kubernetes API server of your user cluster. Set aside another VIP for the ingress service of your user cluster. Provide your VIPs as values for [`loadBalancer.vips.controlPlaneVIP`](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.15/how-to/user-cluster-configuration-file#loadbalancer-vips-controlplanevip-field) and [`loadBalancer.vips.ingressVIP`](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.15/how-to/user-cluster-configuration-file#loadbalancer-vips-ingressvip-field).

Decide what type of load balancing you want to use. The options are:

  * MetalLB bundled load balancing. Set [`loadBalancer.kind`](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.15/how-to/user-cluster-configuration-file#loadbalancer-kind-field) to `"MetalLB"`. Also fill in the [`loadBalancer.metalLB.addressPools`](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.15/how-to/user-cluster-configuration-file#loadbalancer-metallb-section) section, and set `enableLoadBalancer` to `true` for at least one of your node pools. For more information, see [Bundled load balancing with MetalLB](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.15/how-to/bundled-load-balance-metallb).

  * Manual load balancing. Set `loadBalancer.kind` to `"ManualLB"`, and fill in the [`manualLB`](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.15/how-to/user-cluster-configuration-file#loadbalancer-manuallb-section) section. For more information, see [Manual load balancing](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.15/how-to/manual-load-balance).




For more information about load balancing options, see [Overview of load balancing](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.15/how-to/setup-load-balance).

### `advancedNetworking`

If you plan to create an [egress NAT gateway](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.15/how-to/egress-nat-gateway), set [advancedNetworking](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.15/how-to/user-cluster-configuration-file#advancednetworking-field) to `true`.

### `multipleNetworkInterfaces`

Decide whether you want to configure [multiple network interfaces](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.15/how-to/multi-nic) for Pods, and set [multipleNetworkInterfaces](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.15/how-to/user-cluster-configuration-file#multiplenetworkinterfaces-field) accordingly.

### `storage`

If you want to disable the deployment of vSphere CSI components, set [storage.vSphereCSIDisabled](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.15/how-to/user-cluster-configuration-file#storagevspherecsidisabled) to `true`.

### `masterNode`

In the [`masterNode`](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.15/how-to/user-cluster-configuration-file#masternode-section) section, you can specify how many control-plane nodes you want for your user cluster: one or three. You can also specify a datastore for the control-plane nodes and whether you want to enable automatic resizing for the control-plane nodes.

Recall that you specified IP addresses for the control-plane nodes in the [`network.controlPlaneIPBlock`](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.15/how-to/user-cluster-configuration-file#network-controlplaneipblock-section) section.

### `nodePools`

A node pool is a group of nodes in a cluster that all have the same configuration. For example, the nodes in one pool could run Windows and the nodes in another pool could run Linux.

You must specify at least one node pool by filling in the [`nodePools`](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.15/how-to/user-cluster-configuration-file#nodepools-section) section.

For more information, see [Node pools](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/node-pools) and [Creating and managing node pools](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.15/how-to/managing-node-pools).

### `antiAffinityGroups`

Set [`antiAffinityGroups.enabled`](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.15/how-to/user-cluster-configuration-file#antiaffinitygroups-enabled-field) to `true` or `false`.

This field specifies whether Google Distributed Cloud creates [Distributed Resource Scheduler](https://www.vmware.com/products/vsphere/drs-dpm.html) (DRS) anti-affinity rules for your worker nodes, causing them to be spread across at least three physical hosts in your data center.

### `stackdriver`

If you want to enable [Cloud Logging and Cloud Monitoring](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.15/concepts/logging-and-monitoring) for your cluster, fill in the [`stackdriver`](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.15/how-to/user-cluster-configuration-file#stackdriver-section) section.

This section is required by default. That is, if you don't fill in this section, you must include the `--skip-validation-stackdriver` flag when you run `gkectl create cluster`.

### `gkeConnect`

Your user cluster must be [registered to a Google Cloud fleet](https://docs.cloud.google.com/anthos/fleet-management/docs/fleet-creation).

Fill in the [`gkeConnect`](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.15/how-to/user-cluster-configuration-file#gkeconnect-section) section to specify a [fleet host project](https://docs.cloud.google.com/anthos/fleet-management/docs/fleet-concepts#fleet-host-project) and an associated service account.

### `usageMetering`

If you want to enable usage metering for your cluster, then fill in the [`usageMetering`](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.15/how-to/user-cluster-configuration-file#usagemetering-section) section.

### `cloudAuditLogging`

If you want to integrate the audit logs from your cluster's Kubernetes API server with [Cloud Audit Logs](https://docs.cloud.google.com/logging/docs/audit), fill in the [`cloudAuditLogging`](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.15/how-to/user-cluster-configuration-file#cloudauditlogging-section) section.

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
    
    
    cat user-cluster.yaml 
    apiVersion: v1
    kind: UserCluster
    name: "my-user-cluster"
    gkeOnPremVersion: 1.15.0-gke.581
    enableControlplaneV2: true
    enableDataplaneV2: true
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
    masterNode:
      cpus: 4
      memoryMB: 8192
      replicas: 3
    nodePools:
    - name: "worker-node-pool"
      cpus: 4
      memoryMB: 8192
      replicas: 3
      enableLoadBalancer: true
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
    

These are the important points to understand in the preceding example:

  * The static IP addresses for the worker nodes are specified in an IP block file. The IP block file has four addresses even though there are only three worker nodes. The extra IP address is needed during cluster upgrade, update, and auto repair.

  * DNS and NTP servers are specified in the `hostConfig` section. In this example, these DNS and NTP servers are for the control-plane nodes and the worker nodes. That is because the worker nodes have static IP addresses. If the worker nodes were to get their IP addresses from a DHCP server, then these DNS and NTP servers would be only for the control-plane nodes.

  * The static IP addresses for the three control-plane nodes are specified in the `network.controlPlaneIPBlock` section of the user cluster configuration file. There is no need for an extra IP address in this block.

  * The `masterNode.replicas` field is set to `3`.

  * The control-plane VIP and the ingress VIP are both in the same VLAN as the worker nodes and the control-plane nodes.

  * The VIPs that are set aside for Services of type LoadBalancer are specified in the `loadBalancer.metalLB.addressPools` section of the user cluster configuration file. These VIPs are in the same VLAN as the worker nodes and the control-plane nodes. The set of VIPs specified in this section must include the ingress VIP and must not include the control-plane VIP.

  * The user cluster configuration file does not include a `vCenter` section. So the user cluster uses the same vSphere resources as the admin cluster.




### Validate your configuration file

After you've filled in your user cluster configuration file, run `gkectl check-config` to verify that the file is valid:
    
    
    gkectl check-config --kubeconfig ADMIN_CLUSTER_KUBECONFIG --config USER_CLUSTER_CONFIG
    

Replace the following:

  * ADMIN_CLUSTER_KUBECONFIG: the path of the kubeconfig file for your admin cluster

  * USER_CLUSTER_CONFIG: the path of your user cluster configuration file




If the command returns any failure messages, fix the issues and validate the file again.

If you want to skip the more time-consuming validations, pass the `--fast` flag. To skip individual validations, use the `--skip-validation-xxx` flags. To learn more about the `check-config` command, see [Running preflight checks](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.15/how-to/preflight-checks).

## 3\. (Optional) Import OS images to vSphere, and push container images to a private registry

Run `gkectl prepare` if any of the following are true:

  * Your user cluster is in a different vSphere data center from your admin cluster.

  * Your user cluster has a different vCenter Server from your admin cluster.

  * Your user cluster uses a private container registry that is different from the private registry used by your admin cluster.



    
    
    gkectl prepare --kubeconfig ADMIN_CLUSTER_KUBECONFIG \ 
        --bundle-path BUNDLE \
        --user-cluster-config USER_CLUSTER_CONFIG
    

Replace the following:

  * ADMIN_CLUSTER_KUBECONFIG: the path of your admin cluster kubeconfig file

  * BUNDLE: the path of the bundle file. This file is on your admin workstation in `/var/lib/gke/bundles/`. For example:
        
        /var/lib/gke/bundles/gke-onprem-vsphere-1.14.0-gke.421-full.tgz
        

  * USER_CLUSTER_CONFIG: the path of your user cluster configuration file




## 4\. Create a user cluster

#### Create a user cluster:
    
    
    gkectl create cluster --kubeconfig ADMIN_CLUSTER_KUBECONFIG --config USER_CLUSTER_CONFIG 
    

#### Locate the user cluster kubeconfig file

The `gkectl create cluster` command creates a kubeconfig file named `USER_CLUSTER_NAME-kubeconfig` in the current directory. You will need this kubeconfig file later to interact with your user cluster.

The kubeconfig file contains the name of your user cluster. To view the cluster name, you can run:
    
    
    kubectl config get-clusters --kubeconfig USER_CLUSTER_KUBECONFIG
    

The output shows the name of the cluster. For example:
    
    
    NAME
    my-user-cluster
    

If you like, you can change the name and location of your kubeconfig file.

## 5\. Verify that your user cluster is running

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
    

## Upgrade a user cluster

Follow the instructions in [Upgrading Anthos clusters on VMware](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.15/how-to/upgrading).

## Delete a cluster

To delete a user cluster that has Controlplane V2 enabled, follow the instructions in [Deleting a user cluster](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.15/how-to/deleting-a-user-cluster).

When you delete a user cluster that has Controlplane V2 enabled, the data disk is automatically deleted.

## Troubleshooting

See [Troubleshooting cluster creation and upgrade](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.15/troubleshoot-cluster-creation-upgrade).

## What's next

  * [Connect to your cluster from the Google Cloud console](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.15/how-to/connecting-to-a-cluster).
  * [Deploy an application](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.15/how-to/deploy-first-app).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
