---
url: https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.13/how-to/install-static-ips/
title: Create an admin cluster \u00a0|\u00a0 Anthos clusters on VMware \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T20:03:19.337910+00:00
---

# Create an admin cluster  |  Anthos clusters on VMware  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.13/how-to/install-static-ips/

**Version 1.13**. This version is no longer supported. For more information see the [ version support policy](https://cloud.google.com/anthos/clusters/docs/on-prem/latest/getting-support#version_support_policy). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Google Kubernetes Engine (GKE) ](https://docs.cloud.google.com/kubernetes-engine)
  * [ GKE Enterprise ](https://docs.cloud.google.com/kubernetes-engine/enterprise/docs)
  * [ Clusters ](https://docs.cloud.google.com/anthos/clusters)
  * [ Documentation ](https://docs.cloud.google.com/anthos/clusters/docs)
  * [ Anthos clusters on VMware 1.13 ](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.13)
  * [ Guides ](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.13/overview)



Send feedback 

#  Create an admin cluster Stay organized with collections  Save and categorize content based on your preferences. 

Version 1.13 keyboard_arrow_down

  * [ Latest version ](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/latest/how-to/create-admin-cluster)
  * [ Version 1.16 ](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.16/how-to/create-admin-cluster)
  * [ Earlier versions (unsupported) ](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/latest/version-history#expandable-1)



This document shows how to create an admin cluster for Google Distributed Cloud. The admin cluster runs the Kubernetes control plane for the admin cluster itself and for the associated user clusters. You must create an admin cluster before you create any user clusters to run your workloads.

For more details about the admin cluster, see the [installation overview](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.13/how-to/install-overview).

## Procedure overview

These are the primary steps involved in creating an admin cluster:

  1. Connect to your admin workstation.
    This VM has the necessary tools to create new clusters.
  2. Fill in your configuration files.
    Specify the details for your new admin cluster by completing and validating an admin cluster configuration file, a credentials configuration file, and possibly an IP block file.
  3. Import OS images to vSphere, and push container images to the private registry if applicable.
    Run `gkectl prepare`.
  4. (Optional) Create a Seesaw load balancer.
    If you have decided to use the Seesaw load balancer, run `gkectl create loadbalancer`.
  5. Create an admin cluster.
    Use `gkectl` to create a new admin cluster as specified in your completed configuration files. The `onprem-admin-cluster-controller` in the temporary bootstrap cluster manages admin cluster creation.
  6. Verify that your admin cluster is running.
    Use `kubectl` to view your cluster nodes.



At the end of this procedure, you will have a running admin cluster that you can use to create and manage user clusters.

## Before you begin

  * Ensure that you have [created an admin workstation](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.13/how-to/create-admin-workstation).

  * Review the [IP addresses planning document](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.13/how-to/plan-ip-addresses). Ensure that you have enough IP addresses available, and revisit your decision about how you want your cluster nodes to get their IP addresses: DHCP or static. If you decide to use static IP addresses, you must fill in an [IP block file](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.13/how-to/ip-block-file) that contains your chosen addresses.

  * Review the [load balancing overview](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.13/how-to/setup-load-balance) and revisit your decision about the kind of load balancer you want to use. For certain load balancers, you must set up the load balancer before you create your admin cluster.

  * Look ahead at the `privateRegistry` section, and decide whether you want to use a public or private registry for Google Distributed Cloud components.

  * Look ahead at the osImageType field, and decide what type of operating system you want to run on your admin cluster nodes




## 1\. Connect to your admin workstation

Follow the instructions to [get an SSH connection](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.13/how-to/create-admin-workstation#getting_an_ssh_connection_to_your_admin_workstation) to your admin workstation. The admin workstation has the tools you need to create your admin cluster. The admin workstation also has your component access service account activated.

Do all the remaining steps in this topic on your admin workstation in the home directory.

## 2\. Fill in your configuration file

When `gkeadm` created your admin workstation, it generated a configuration file named `admin-cluster.yaml`. This configuration file is for creating your admin cluster.

Familiarize yourself with the configuration file by scanning the [admin cluster configuration file](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.13/how-to/admin-cluster-configuration-file) document. You might want to keep this document open in a separate tab or window, because you will refer to it as you complete the following steps.

### `name`

If you want to specify a name for your admin cluster, fill in the [`name`](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.13/how-to/admin-cluster-configuration-file#name-field) field.

### `bundlePath`

The bundle is a zipped file that contains cluster components. It is included with the admin workstation. This field is already filled in for you.

### `vCenter`

Most of the fields in this section are already filled in with values that you entered when you created your admin workstation. The exception is the [`dataDisk`](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.13/how-to/admin-cluster-configuration-file#vcenter-datadisk-field) field, which you must fill in now.

### `network`

Decide how you want your cluster nodes to get their IP addresses. The options are:

  * From a DHCP server that you set up ahead of time. Set `network.ipMode.type` to `"dhcp"`.

  * From a list of static IP addresses that you provide. Set `network.ipMode.type` to `"static"`, and create an [IP block file](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.13/how-to/ip-block-file) that provides the static IP addresses. For an example of an IP block file, see Example of filled-in configuration files.




Fill in the rest of the fields in the [network section of the configuration file](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.13/how-to/admin-cluster-configuration-file#network-section) as needed:

  * If you have decided to use static IP addresses for your cluster nodes, the [`network.ipMode.ipBlockFilePath`](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.13/how-to/admin-cluster-configuration-file#network-ipmode.ipblockfilepath-field) field and the [`network.hostconfig`](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.13/how-to/admin-cluster-configuration-file#network-hostconfig-section) section are required. The `network.hostconfig` section holds information about NTP servers, DNS servers, and DNS search domains used by your cluster nodes.

If you are using the Seesaw load balancer, the `network.hostconfig` section is required even if you intend to use DHCP for your cluster nodes.

  * The [network.podCIDR](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.13/how-to/admin-cluster-configuration-file#network-podcidr-field%7D) and [network.serviceCIDR](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.13/how-to/admin-cluster-configuration-file#network-servicecidr-field) fields have prepopulated values that you can leave unchanged unless they conflict with addresses already being used in your network. Kubernetes uses these ranges to assign IP addresses to Pods and Services in your cluster.




Regardless of whether you rely on a DHCP server or specify a list of static IP addresses, you need to have enough IP addresses available for your admin cluster nodes. This includes the nodes in the admin cluster that run the control planes for any associated user clusters. For an explanation of how many IP addresses you need, see [Plan your IP addresses](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.13/how-to/plan-ip-addresses).

### `loadBalancer`

Set aside a VIP for the Kubernetes API server of your admin cluster. Set aside another VIP for the add-ons server. Provide your VIPs as values for [`loadBalancer.vips.controlPlaneVIP`](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.13/how-to/admin-cluster-configuration-file#loadbalancer-vips-controlplanevip-field) and [`loadBalancer.vips.addonsVIP`](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.13/how-to/admin-cluster-configuration-file#loadbalancer-vips-addonsvip-field).

For more information, see [VIPs in the admin cluster subnet](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.13/how-to/plan-ip-addresses#example_ip_addresses_vips_in_the_admin_cluster_subnet).

Decide what type of load balancing you want to use. The options are:

  * MetalLB bundled load balancing. Set [`loadBalancer.kind`](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.13/how-to/admin-cluster-configuration-file#loadbalancerkind) to `"MetalLB"`.

  * Seesaw bundled load balancing. Set `loadBalancer.kind` to `"Seesaw"`, and fill in the [`loadBalancer.seesaw`](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.13/how-to/admin-cluster-configuration-file#loadbalancer-seesaw-section) section.

  * Integrated load balancing with F5 BIG-IP. Set `loadBalancer.kind` to `"F5BigIP"`, and fill in the [`f5BigIP`](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.13/how-to/admin-cluster-configuration-file#loadbalancer-f5bigip-section) section.

  * Manual load balancing. Set `loadBalancer.kind` to `"ManualLB"`, and fill in the [`manualLB`](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.13/how-to/admin-cluster-configuration-file#loadbalancer-manuallb-section) section.




For more information about load balancing options, see [Overview of load balancing](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.13/how-to/setup-load-balance).

### `antiAffinityGroups`

Set [`antiAffinityGroups.enabled`](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.13/how-to/admin-cluster-configuration-file#antiaffinitygroups-enabled-field) to `true` or `false` according to your preference.

Use this field to specify whether you want Google Distributed Cloud to create VMware [Distributed Resource Scheduler](https://www.vmware.com/products/vsphere/drs-dpm.html) (DRS) anti-affinity rules for your admin cluster nodes, causing them to be spread across at least three physical hosts in your data center.

### `adminMaster`

If you want to specify CPU and memory for the control-plane node of the admin cluster, fill in the [`adminMaster`](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.13/how-to/admin-cluster-configuration-file#adminmaster-section).

### `addonNode`

Set [`addonNode.autoResize.enabled`](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.13/how-to/admin-cluster-configuration-file#addonnode-autoresize-enabled-field) to `true` or `false` according to your preference.

### `proxy`

If the network that will have your admin cluster nodes is behind a proxy server, fill in the [`proxy`](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.13/how-to/admin-cluster-configuration-file#proxy-section) section.

### `privateRegistry`

Decide where you want to keep container images for the Google Distributed Cloud components. The options are:

  * Container Registry

  * Your own private Docker registry.




If you want to use your own private registry, fill in the [`privateRegistry`](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.13/how-to/admin-cluster-configuration-file#privateregistry-section) section.

### `componentAccessServiceAccountKeyPath`

Google Distributed Cloud uses your component access service account to download cluster components from Container Registry. This field holds the path of a JSON key file for your component access service account.

This field is already filled in for you.

### `gkeConnect`

[Register your admin cluster](https://docs.cloud.google.com/anthos/multicluster-management/connect/registering-a-cluster#register_clusters_outside) to a Google Cloud fleet by filling in the [`gkeConnect`](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.13/how-to/admin-cluster-configuration-file#gkeconnect-section) section.

### `stackdriver`

If you want to enable [Cloud Logging and Cloud Monitoring](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.13/concepts/logging-and-monitoring) for your cluster, fill in the [`stackdriver`](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.13/how-to/admin-cluster-configuration-file#stackdriver-section) section.

This is section is required by default. That is, if you don't fill in this section, you must you include the `--skip-validation-stackdriver` flag when you run `gkectl create admin`.

### `cloudAuditLogging`

If you want to integrate the audit logs from your cluster's Kubernetes API server with Cloud Audit Logs, fill in the [`cloudAuditLogging`](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.13/how-to/admin-cluster-configuration-file#cloudauditlogging-section) section.

### `clusterBackup`

If you want to enable [backing up of the admin cluster](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.13/how-to/back-up-and-restore-an-admin-cluster-with-gkectl), set [`clusterBackup.datastore`](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.13/how-to/admin-cluster-configuration-file#clusterbackup-datastore-field) to the [vSphere datastore](https://docs.vmware.com/en/VMware-vSphere/7.0/com.vmware.vsphere.storage.doc/GUID-3CC7078E-9C30-402C-B2E1-2542BEE67E8F.html) where you want to save cluster backups.

### `autoRepair`

If you want to [enable automatic node repair](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.13/how-to/node-auto-repair) for your admin cluster, set [`autoRepair.enabled`](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.13/how-to/admin-cluster-configuration-file#autorepair-enabled-field) to `true`.

### `secretsEncryption`

If you want to enable [always-on Secrets encryption](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.13/how-to/always-on-secrets-encryption), fill in the [`secretsEncryption`](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.13/how-to/admin-cluster-configuration-file#secretsencryption-section) section.

### `osImageType`

Decide what type of OS image you want to use for the admin cluster nodes, and fill in the [`osImageType`](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.13/how-to/admin-cluster-configuration-file#osimagetype) section accordingly.

### Example of filled-in configuration files

Here is an example of a filled-in IP block file and a filled-in admin cluster configuration file. The configuration enables some, but not all, of the available features.

#### vc-01-ipblock.yaml
    
    
    blocks:
      - netmask: 255.255.252.0
        gateway: 172.16.23.254
        ips:
        - ip: 172.16.20.10
          hostname: admin-host1
        - ip: 172.16.20.11
          hostname: admin-host2
        - ip: 172.16.20.12
          hostname: admin-host3
        - ip: 172.16.20.13
          hostname: admin-host4
        - ip: 172.16.20.14
          hostname: admin-host5
        - ip: 172.16.20.15
          hostname: admin-host6
        - ip: 172.16.20.16
          hostname: admin-host7
        - ip: 172.16.20.17
          hostname: admin-host8
    

#### vc-01-admin-cluster.yaml
    
    
    apiVersion: v1
    kind: AdminCluster
    name: "gke-admin-01"
    bundlePath: "/var/lib/gke/bundles/gke-onprem-vsphere-1.11.0-gke.543-full.tgz"
    vCenter:
      address: "vc01.example"
      datacenter: "vc-01"
      cluster: "vc01-workloads-1"
      resourcePool: "vc-01-pool-1"
      datastore: "vc01-datastore-1"
      caCertPath: "/usr/local/google/home/me/certs/vc01-cert.pem""
      credentials:
        fileRef:
          path: "credential.yaml"
          entry: "vCenter"
      dataDisk: "vc01-admin-disk.vmdk"
    network:
      hostConfig:
        dnsServers:
        - "203.0.113.1"
        - "198.51.100.1"
        ntpServers:
        - "216.239.35.4"
      ipMode:
        type: "static"
        ipBlockFilePath: "vc-01-ipblock.yaml"
      serviceCIDR: "10.96.232.0/24"
      podCIDR: "192.168.0.0/16"
      vCenter:
        networkName: "vc01-net-1"
    loadBalancer:
      vips:
        controlPlaneVIP: "172.16.20.59"
        addonsVIP: "172.16.20.60"
      kind: "MetalLB"
    antiAffinityGroups:
      enabled: true
    componentAccessServiceAccountKeyPath: "sa-key.json"
    gkeConnect:
      projectID: "my-project-123"
      registerServiceAccountKeyPath: "connect-register-sa-2203040617.json"
    stackdriver:
      projectID: "my-project-123"
      clusterLocation: "us-central1"
      enableVPC: false
      serviceAccountKeyPath: "log-mon-sa-2203040617.json"
      disableVsphereResourceMetrics: false
    clusterBackup:
      datastore: "vc-01-datastore-bu"
    autoRepair:
      enabled: true
    osImageType: "ubuntu_containerd"
    

### Validate your configuration file

After you've filled in your admin cluster configuration file, run `gkectl check-config` to verify that the file is valid:
    
    
    gkectl check-config --config ADMIN_CLUSTER_CONFIG
    

Replace ADMIN_CLUSTER_CONFIG with the path of your admin cluster configuration file.

If the command returns any failure messages, fix the issues and validate the file again.

If you want to skip the more time-consuming validations, pass the `--fast` flag. To skip individual validations, use the `--skip-validation-xxx` flags. To learn more about the `check-config` command, see [Running preflight checks](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.13/how-to/preflight-checks).

## 3\. Get OS images

Run `gkectl prepare` to initialize your vSphere environment:
    
    
    gkectl prepare --config ADMIN_CLUSTER_CONFIG
    

The `gkectl prepare` command performs the following preparatory tasks:

  * Imports OS images to vSphere and marks them as VM templates.

  * If you are using a private Docker registry, pushes the container images to your registry.

  * Optionally, validates the container images' build attestations, thereby verifying the images were built and signed by Google and are ready for deployment.


**Note:** If you're using internal DNS names, or your workstation cannot access Google public DNS addresses (8.8.8.8 or 8.8.4.4), you must specify your internal nameserver in [`/etc/resolv.conf`](https://ubuntu.com/server/docs#name-resolution).

## 4\. (Optional) Create a Seesaw load balancer

Recall that you have several load balancing options for your admin cluster: Metal LB, Seesaw, F5 BIG-IP, or manual.

If you have chosen to use the Seesaw load balancer, do the step in this section. Otherwise, you can skip this section.

Create and configure the VMs for your [Seesaw load balancer](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.13/how-to/bundled-load-balance):
    
    
    gkectl create loadbalancer --config ADMIN_CLUSTER_CONFIG
    

## 5\. Create the admin cluster

Create the admin cluster:
    
    
    gkectl create admin --config ADMIN_CLUSTER_CONFIG
    

### Resume creation of the admin cluster after a failure

If the admin cluster creation fails or is canceled, you can run the `create` command again:
    
    
    gkectl create admin --config ADMIN_CLUSTER_CONFIG
    

### Locate the admin cluster kubeconfig file

The `gkectl create admin` command creates a kubeconfig file named `kubeconfig` in the current directory. You will need this kubeconfig file later to interact with your admin cluster.

If you like, you can change the name and location of your kubeconfig file.

### Manage the `checkpoint.yaml` file

When you ran the `gkectl create admin` command to create the admin cluster, it created a checkpoint file in the same datastore folder as the admin cluster data disk. By default, this file has the name DATA_DISK_NAME`‑checkpoint.yaml`. If the length of DATA_DISK_NAME is greater than or equal to 245 characters, then, due to the vSphere limit on filename length, the name is DATA_DISK_NAME`.yaml`.

This file contains the admin cluster state and credentials, and is used for future upgrades. Do not delete this file unless you are following the process for [deleting an admin cluster](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.13/how-to/deleting-an-admin-cluster).

If you have enabled VM encryption in your instance of vCenter Server, then you must have the [Cryptographic operations.Direct Access](https://docs.vmware.com/en/VMware-vSphere/7.0/com.vmware.vsphere.security.doc/GUID-660CCB35-847F-46B3-81CA-10DDDB9D7AA9.html) privilege before you create or upgrade your admin cluster. Otherwise the checkpoint will not be uploaded. If you cannot obtain this privilege, then you can disable uploading the checkpoint file by using the hidden flag `--disable-checkpoint` when you run a relevant command.

The `checkpoint.yaml` file is automatically updated when you run the `gkectl upgrade admin` command, or when you run a `gkectl update` command that affects the admin cluster.

## 6\. Verify that your admin cluster is running

Verify that your admin cluster is running:
    
    
    kubectl get nodes --kubeconfig ADMIN_CLUSTER_KUBECONFIG
    

Replace ADMIN_CLUSTER_KUBECONFIG with the path of your admin cluster kubeconfig file.

The output shows the admin cluster nodes. For example:
    
    
    gke-admin-master-hdn4z            Ready    control-plane,master ...
    gke-admin-node-7f46cc8c47-g7w2c   Ready ...
    gke-admin-node-7f46cc8c47-kwlrs   Ready ...
    

## Troubleshooting

See [Troubleshooting cluster creation and upgrade](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.13/troubleshoot-cluster-creation-upgrade).

## What's next

[Create a user cluster](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.13/how-to/create-user-cluster)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
