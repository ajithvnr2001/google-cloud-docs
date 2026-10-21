---
url: https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.10/how-to/install-static-ips/
title: Creating an admin cluster \u00a0|\u00a0 Anthos clusters on VMware \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-15T16:26:59.391535+00:00
---

# Creating an admin cluster  |  Anthos clusters on VMware  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.10/how-to/install-static-ips/

**Version 1.10**. This version is no longer supported. For more information see the [ version support policy](https://cloud.google.com/anthos/clusters/docs/on-prem/latest/getting-support#version_support_policy). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Google Kubernetes Engine (GKE) ](https://docs.cloud.google.com/kubernetes-engine)
  * [ GKE Enterprise ](https://docs.cloud.google.com/kubernetes-engine/enterprise/docs)
  * [ Clusters ](https://docs.cloud.google.com/anthos/clusters)
  * [ Documentation ](https://docs.cloud.google.com/anthos/clusters/docs)
  * [ Anthos clusters on VMware 1.10 ](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.10)
  * [ Guides ](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.10/overview)



Send feedback 

#  Creating an admin cluster Stay organized with collections  Save and categorize content based on your preferences. 

Version 1.10 keyboard_arrow_down

  * [ Latest version ](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/latest/how-to/create-admin-cluster)
  * [ Version 1.16 ](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.16/how-to/create-admin-cluster)
  * [ Earlier versions (unsupported) ](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/latest/version-history#expandable-1)



This page shows how to create an admin cluster for Google Distributed Cloud.

The instructions here are complete. For a shorter introduction to creating an admin cluster, see [Create an admin cluster (quickstart)](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.10/how-to/admin-cluster-quickstart).

## Before you begin

[Create an admin workstation](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.10/how-to/create-admin-workstation).

## Get an SSH connection to your admin workstation

[Get an SSH connection](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.10/how-to/create-admin-workstation#getting_an_ssh_connection_to_your_admin_workstation) to your admin workstation.

Recall that `gkeadm` activated your component access service account on the admin workstation.

Do all the remaining steps in this topic on your admin workstation in the home directory.

## Credentials configuration file

When you used `gkeadm` to create your admin workstation, you filled in a credentials configuration file named `credential.yaml`. This file holds the username and password for your vCenter server.

## Admin cluster configuration file

When `gkeadm` created your admin workstation, it generated a configuration file named `admin-cluster.yaml`. This configuration file is for creating your admin cluster.

## Filling in your configuration file

### `name`

If you want to specify a name for your admin cluster, fill in the [`name`](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.10/how-to/admin-cluster-configuration-file#name-field) field.

### `bundlePath`

This field is already filled in for you.

### `vCenter`

Most of the fields in this section are already filled in with values that you entered when you created your admin workstation. The exception is the [`dataDisk`](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.10/how-to/admin-cluster-configuration-file#vcenter-datadisk-field) field, which you must fill in now.

### `network`

Decide how you want your cluster nodes to get their IP addresses. The options are:

  * From a DHCP server. Set `network.ipMode.type` to `"dhcp"`.

  * From a list of static IP addresses that you provide. Set `network.ipMode.type` to `"static"`, and create an [IP block file](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.10/how-to/ip-block-file) that provides the static IP addresses.




Provide values for the remaining fields in the [`network`](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.10/how-to/admin-cluster-configuration-file#network-section) section.

Regardless of whether you rely on a DHCP server or specify a list of static IP addresses, you need enough IP addresses to satisfy the following:

  * Three nodes in the admin cluster to run the admin cluster control plane and add-ons.

  * An additional node in the admin cluster to be used temporarily during upgrades.

  * For each user cluster that you intend to create, one or three nodes in the admin cluster to run the control-plane components for the user cluster. If you want a high availability (HA) control plane for a user cluster, then you need three nodes in the admin cluster for the user cluster control plane. Otherwise, you need only one node in the admin cluster for the user cluster control plane.




For example, suppose you intend to create two user clusters: one with an HA control plane and one with a non-HA control plane. Then you would need eight IP addresses for the following nodes in the admin cluster:

  * Three nodes for the admin cluster control plane and add-ons
  * One temporary node
  * Three nodes for the HA user-cluster control plane
  * One node for the non-HA user-cluster control plane



As mentioned previously, if you want to use static IP addresses, then you need to provide an IP block file. Here is an example of an IP block file with eight hosts:
    
    
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

### `loadBalancer`

Set aside a VIP for the Kubernetes API server of your admin cluster. Set aside another VIP for the add-ons server. Provide your VIPs as values for [`loadBalancer.vips.controlPlaneVIP`](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.10/how-to/admin-cluster-configuration-file#loadbalancer-vips-controlplanevip-field) and [`loadBalancer.vips.addonsVIP`](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.10/how-to/admin-cluster-configuration-file#loadbalancer-vips-addonsvip-field).

Decide what type of load balancing you want to use. The options are:

  * Seesaw bundled load balancing. Set `loadBalancer.kind` to `"Seesaw"`, and fill in the [`loadBalancer.seesaw`](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.10/how-to/admin-cluster-configuration-file#loadbalancer-seesaw-section) section.

  * Integrated load balancing with F5 BIG-IP. Set `loadBalancer.kind` to `"F5BigIP"`, and fill in the [`f5BigIP`](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.10/how-to/admin-cluster-configuration-file#loadbalancer-f5bigip-section) section.

  * Manual load balancing. Set `loadBalancer.kind` to `"ManualLB"`, and fill in the [`manualLB`](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.10/how-to/admin-cluster-configuration-file#loadbalancer-manuallb-section) section.




### `antiAffinityGroups`

Set [`antiAffinityGroups.enabled`](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.10/how-to/admin-cluster-configuration-file#antiaffinitygroups-enabled-field) to `true` or `false` according to your preference.

### `adminMaster`

Fill in the [`adminMaster`](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.10/how-to/admin-cluster-configuration-file#adminmaster-section) section or remove it according to your preference.

### `addonNode`

Set [`addonNode.autoResize.enabled`](https://cloud.google.com/anthos/clusters/docs/on-prem/1.10/how-to/admin-cluster-configuration-file#addonnode-autoresize-enabled-field) to `true` or `false` according to your preference.

### `proxy`

If the network that will have your admin cluster nodes is behind a proxy server, fill in the [`proxy`](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.10/how-to/admin-cluster-configuration-file#proxy-section) section.

### `privateRegistry`

Decide where you want to keep container images for the Google Distributed Cloud components. The options are:

  * Container Registry

  * Your own private Docker registry.




If you want to create your own private Docker registry, fill in the [`privateRegistry`](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.10/how-to/admin-cluster-configuration-file#privateregistry-section) section.

### `componentAccessServiceAccountKeyPath`

This field is already filled in for you.

### `gkeConnect`

If you want to [register your admin cluster](https://docs.cloud.google.com/anthos/multicluster-management/connect/registering-a-cluster#register_clusters_outside) to a Google Cloud fleet, fill in the [`gkeConnect`](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.10/how-to/admin-cluster-configuration-file#gkeconnect-section) section.

### `stackdriver`

If you want to enable [Cloud Logging and Cloud Monitoring](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.10/concepts/logging-and-monitoring) for your cluster, fill in the [`stackdriver`](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.10/how-to/admin-cluster-configuration-file#stackdriver-section) section.

### `cloudAuditLogging`

If you want to enable [Cloud Audit Logs](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.10/how-to/audit-logging) for your cluster, fill in the [`cloudAuditLogging`](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.10/how-to/admin-cluster-configuration-file#cloudauditlogging-section) section.

### `clusterBackup`

Set [`clusterBackup.datastore`](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.10/how-to/admin-cluster-configuration-file#clusterbackup-datastore-field) to `true` or `false` according to your preference.

### `autoRepair`

Set [`autoRepair.enabled`](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.10/how-to/admin-cluster-configuration-file#autorepair-enabled-field) to `true` or `false` according to your preference.

### `secretsEncryption`

If you want to enable [always-on Secrets encryption](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.10//how-to/always-on-secrets-encryption), fill in the [`secretsEncryption`](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.10/how-to/admin-cluster-configuration-file#secretsencryption-section) section.

### `osImageType`

Decide what type of OS image you want to use for the admin cluster nodes in the `osImageType` section. The options are:

  * `ubuntu_containerd`

  * `cos` (preview)




By default,the `osImageType` is set to `ubuntu_containerd`.

Note that the `osImageType` section only supports the `gkectl create` and `gkectl upgrade` commands.

## Validating your configuration file

After you've filled in your admin cluster configuration file, run `gkectl check-config` to verify that the file is valid:
    
    
    gkectl check-config --config [CONFIG_PATH]
    

where [CONFIG_PATH] is the path of your admin cluster configuration file.

If the command returns any failure messages, fix the issues and validate the file again.

If you want to skip the more time-consuming validations, pass the `--fast` flag. To skip individual validations, use the `--skip-validation-xxx` flags. To learn more about the `check-config` command, see [Running preflight checks](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.10/how-to/preflight-checks).

## Running `gkectl prepare`

Run `gkectl prepare` to initialize your vSphere environment:
    
    
    gkectl prepare --config [CONFIG_PATH]

The `gkectl prepare` command performs the following preparatory tasks:

  * Imports the OS images to vSphere and marks them as VM templates.

  * If you are using a private Docker registry, this command pushes the Docker container images to your registry.

  * Optionally, this command validates the container images' build attestations, thereby verifying the images were built and signed by Google and are ready for deployment.


**Note:** If you're using internal DNS names, or your workstation cannot access Google public DNS addresses (8.8.8.8 or 8.8.4.4), you must specify your internal nameserver in [`/etc/resolv.conf`](https://ubuntu.com/server/docs#name-resolution).

## Creating a Seesaw load balancer for your admin cluster

If you have chosen to use the bundled Seesaw load balancer, do the step in this section. Otherwise, you can skip this section.

Create and configure the VMs for your [Seesaw load balancer](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.10/how-to/bundled-load-balance):
    
    
    gkectl create loadbalancer --config [CONFIG_PATH]
    

## Creating the admin cluster

Create the admin cluster:
    
    
    gkectl create admin --config [CONFIG_PATH]

where [CONFIG_PATH] is the path of your admin cluster configuration file.

## Locating the admin cluster kubeconfig file

The `gkectl create admin` command creates a kubeconfig file named `kubeconfig` in the current directory. You will need this kubeconfig file later to interact with your admin cluster.

If you like, you can change the name and location of your kubeconfig file.

## Verifying that your admin cluster is running

Verify that your admin cluster is running:
    
    
    kubectl get nodes --kubeconfig ADMIN_CLUSTER_KUBECONFIG
    

Replace ADMIN_CLUSTER_KUBECONFIG with the path of your admin cluster kubeconfig file.

The output shows the admin cluster nodes. For example:
    
    
    gke-admin-master-hdn4z            Ready    control-plane,master ...
    gke-admin-node-7f46cc8c47-g7w2c   Ready ...
    gke-admin-node-7f46cc8c47-kwlrs   Ready ...
    

## Managing the `checkpoint.yaml` file

When you ran the `gkectl create admin` command to create the admin cluster, it created a `checkpoint.yaml` file in the same datastore folder as the admin cluster data disk. By default, this file has the name DATA_DISK_NAME‑checkpoint.yaml. If the length of DATA_DISK_NAME is greater than or equal to 245 characters, then, due to the vSphere limit on filename length, the name is DATA_DISK_NAME.yaml. Replace DATA_DISK_NAME with the name of the data disk.

This file contains the admin cluster state and credentials and is used for future upgrades. As with the admin cluster datadisk, do not delete this file unless you are following the process for [deleting the admin cluster](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.10/how-to/deleting-an-admin-cluster).

If you have enabled VM encryption in your vCenter, then you must have `Cryptographer.Access` permission before you create or upgrade your admin cluster, if you want the checkpoint file to be uploaded. If you cannot obtain this permission, then you can disable uploading the checkpoint file with the hidden flag `--disable-checkpoint` when you run a relevant command.

The checkpoint.yaml file is automatically updated when you run the `gkectl upgrade admin` command, or when you run a `gkectl update` command that affects the admin cluster.

## Troubleshooting

See [Troubleshooting cluster creation and upgrade](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.10/troubleshoot-cluster-creation-upgrade)

## What's next

[Creating a user cluster](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.10/how-to/create-user-cluster)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
