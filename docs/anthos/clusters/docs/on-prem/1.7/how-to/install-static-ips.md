---
url: https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.7/how-to/install-static-ips/
title: Creating an admin cluster \u00a0|\u00a0 Anthos clusters on VMware \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-15T09:11:18.317949+00:00
---

# Creating an admin cluster  |  Anthos clusters on VMware  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.7/how-to/install-static-ips/

**Version 1.7**. This version is no longer supported. For more information see the [ version support policy](https://cloud.google.com/anthos/clusters/docs/on-prem/latest/getting-support#version_support_policy). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Google Kubernetes Engine (GKE) ](https://docs.cloud.google.com/kubernetes-engine)
  * [ GKE Enterprise ](https://docs.cloud.google.com/kubernetes-engine/enterprise/docs)
  * [ Clusters ](https://docs.cloud.google.com/anthos/clusters)
  * [ Documentation ](https://docs.cloud.google.com/anthos/clusters/docs)
  * [ Anthos clusters on VMware 1.7 ](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.7)
  * [ Guides ](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.7/overview)



Send feedback 

#  Creating an admin cluster Stay organized with collections  Save and categorize content based on your preferences. 

This page shows how to create an admin cluster for Google Distributed Cloud.

The instructions here are complete. For a shorter introduction to creating an admin cluster, see [Create an admin cluster (quickstart)](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.7/how-to/admin-cluster-quickstart).

## Before you begin

[Create an admin workstation](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.7/how-to/create-admin-workstation).

## Get an SSH connection to your admin workstation

[Get an SSH connection](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.7/how-to/create-admin-workstation#getting_an_ssh_connection_to_your_admin_workstation) to your admin workstation.

Recall that `gkeadm` activated your component access service account on the admin workstation.

Do all the remaining steps in this topic on your admin workstation in the home directory.

## Credentials configuration file

When you used `gkeadm` to create your admin workstation, you filled in a credentials configuration file named `credential.yaml`. This file holds the username and password for your vCenter server.

## Admin cluster configuration file

When `gkeadm` created your admin workstation, it generated a configuration file named `admin-cluster.yaml`. This configuration file is for creating your admin cluster.

## Filling in your configuration file

### `bundlePath`

This field is already filled in for you.

### `vCenter`

Most of the fields in this are already filled in with values that you entered when you created your admin workstation. The exception is the [`dataDisk` field](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.7/how-to/admin-cluster-configuration-file#vcenter-datadisk-field), which you must fill in now.

### `network`

Decide how you want your cluster nodes to get their IP addresses. The options are:

  * From a DHCP server. Set `network.ipMode.type` to `"dhcp"`.

  * From a list of static IP addresses that you provide. Set `network.ipMode.type` to `"static"`, and create an [IP block file](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.7/how-to/ip-block-file) that provides the static IP addresses.




Provide values for the remaining fields in the [`network`](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.7/how-to/admin-cluster-configuration-file#network-section) section.

Regardless of whether you rely on a DHCP server or specify a list of static IP addresses, you need enough IP addresses to satisfy the following:

  * Three nodes in the admin cluster to run the admin cluster control plane and add-ons.

  * An additional node in the admin cluster to be used temporarily during upgrades.

  * For each user cluster that you intend to create, one or three nodes in the admin cluster to run the control-plane components for the user cluster. If you want the control plane for a user cluster to be highly available (HA), then you need three nodes in the admin cluster for the user cluster control plane. Otherwise, you need only one node in the admin cluster for the user cluster control plane.




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

Set aside a VIP for the Kubernetes API server of your admin cluster. Set aside another VIP for the add-ons server. Provide your VIPs as values for [`loadBalancer.vips.controlPlaneVIP`](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.7/how-to/admin-cluster-configuration-file#loadbalancer-vips-controlplanevip-field) and [`loadBalancer.vips.addonsVIP`](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.7/how-to/admin-cluster-configuration-file#loadbalancer-vips-addonsvip-field).

Decide what type of load balancing you want to use. The options are:

  * Seesaw bundled load balancing. Set `loadBalancer.kind` to `"Seesaw"`, and fill in the [`loadBalancer.seesaw`](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.7/how-to/admin-cluster-configuration-file#loadbalancer-seesaw-section) section.

  * Integrated load balancing with F5 BIG-IP. Set `loadBalancer.kind` to `"F5BigIP"`, and fill in the [`f5BigIP`](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.7/how-to/admin-cluster-configuration-file#loadbalancer-f5bigip-section) section.

  * Manual load balancing. Set `loadBalancer.kind` to `"ManualLB"`, and fill in the [`manualLB`](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.7/how-to/admin-cluster-configuration-file#loadbalancer-manuallb-section) section.




### `antiAffinityGroups`

Set [`antiAffinityGroups.enabled`](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.7/how-to/admin-cluster-configuration-file#antiaffinitygroups-enabled-field) to `true` or `false` according to your preference.

### `proxy`

If the network that will have your admin cluster nodes is behind a proxy server, fill in the [`proxy`](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.7/how-to/admin-cluster-configuration-file#proxy-section) section.

### `privateRegistry`

Decide where you want to keep container images for the Google Distributed Cloud components. The options are:

  * gcr.io. Do not fill in the `privateRegistry` section.

  * Your own private Docker registry. Fill in the [`privateRegistry`](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.7/how-to/admin-cluster-configuration-file#privateregistry-section) section.




## `gcrKeyPath`

Set `gcrKeyPath` to the path of the JSON key file for your [component access service account](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.7/how-to/service-accounts#component_access_service_account).

### `stackdriver`

Fill in the [`stackdriver`](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.7/how-to/admin-cluster-configuration-file#stackdriver-section) section.

### `cloudAuditLogging`

If you want Kubernetes audit logs to be integrated with Cloud Audit Logs, fill in the [`cloudAuditLogging`](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.7/how-to/admin-cluster-configuration-file#cloudauditlogging-section) section.

### `autoRepair`

If you want to enable [node auto repair](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.7/how-to/node-auto-repair), set `autoRepair.enabled` to `true`. Otherwise, set it to `false`.

## Validating your configuration file

After you've filled in your admin cluster configuration file, run `gkectl check-config` to verify that the file is valid:
    
    
    gkectl check-config --config [CONFIG_PATH]
    

where [CONFIG_PATH] is the path of your admin cluster configuration file.

If the command returns any failure messages, fix the issues and validate the file again.

If you want to skip the more time-consuming validations, pass the `--fast` flag. To skip individual validations, use the `--skip-validation-xxx` flags. To learn more about the `check-config` command, see [Running preflight checks](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.7/how-to/preflight-checks).

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

Create and configure the VMs for your [Seesaw load balancer](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.7/how-to/bundled-load-balance):
    
    
    gkectl create loadbalancer --config [CONFIG_PATH]
    

## Creating the admin cluster

Create the admin cluster:
    
    
    gkectl create admin --config [CONFIG_PATH]

where [CONFIG_PATH] is the path of your admin cluster configuration file.

The `gkectl create admin` command creates a kubeconfig file named `kubeconfig` in the current directory. You will need this kubeconfig file later to interact with your admin cluster.

## Verifying that your admin cluster is running

Verify that your admin cluster is running:
    
    
    kubectl get nodes --kubeconfig [ADMIN_CLUSTER_KUBECONFIG]
    

where [ADMIN_CLUSTER_KUBECONFIG] is the path of your kubeconfig file.

The output shows the admin cluster nodes.

## Troubleshooting

See [Troubleshooting cluster creation and upgrade](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.7/troubleshoot-cluster-creation-upgrade)

## What's next

[Creating a user cluster](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.7/how-to/create-user-cluster)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
