---
url: https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.6/how-to/create-user-cluster/
title: Creating a user cluster \u00a0|\u00a0 Anthos clusters on VMware \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-16T13:57:30.107555+00:00
---

# Creating a user cluster  |  Anthos clusters on VMware  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.6/how-to/create-user-cluster/

**Version 1.6**. This version is no longer supported. For more information see the [ version support policy](https://cloud.google.com/anthos/clusters/docs/on-prem/latest/getting-support#version_support_policy). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Google Kubernetes Engine (GKE) ](https://docs.cloud.google.com/kubernetes-engine)
  * [ GKE Enterprise ](https://docs.cloud.google.com/kubernetes-engine/enterprise/docs)
  * [ Clusters ](https://docs.cloud.google.com/anthos/clusters)
  * [ Documentation ](https://docs.cloud.google.com/anthos/clusters/docs)
  * [ Anthos clusters on VMware 1.6 ](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.6)
  * [ Guides ](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.6/overview)



Send feedback 

#  Creating a user cluster Stay organized with collections  Save and categorize content based on your preferences. 

This page shows how to create a user cluster for Google Distributed Cloud.

The instructions here are complete. For a shorter introduction to creating a user cluster, see [Create a user cluster (quickstart)](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.6/how-to/user-cluster-quickstart).

## Before you begin

[Create an admin cluster](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.6/how-to/create-admin-cluster).

# Get an SSH connection to your admin workstation

[Get an SSH connection](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.6/how-to/create-admin-workstation#getting_an_ssh_connection_to_your_admin_workstation) to your admin workstation.

Recall that `gkeadm` activated your component access service account on the admin workstation.

Do all the remaining steps in this topic on your admin workstation in the home directory.

## Credentials configuration file

When you used `gkeadm` to create your admin workstation, you filled in a credentials configuration file named `credential.yaml`. This file holds the username and password for your vCenter server.

## Admin cluster configuration file

When `gkeadm` created your admin workstation, it generated a configuration file named `user-cluster.yaml`. This configuration file is for creating your user cluster.

## Filling in your configuration file

### `name`

Set the [`name`](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.6/how-to/user-cluster-configuration-file#name-field) field to a name of your choice for the user cluster.

### `gkeOnPremVersion`

This field is already filled in for you.

### `vCenter`

The values you set in the `vCenter` section of your [admin cluster configuration file](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.6/how-to/admin-cluster-configuration-file) are global. That is, they apply to your admin cluster and your user clusters.

For each user cluster that you create, you have the option of overriding some of the global `vCenter` values.

If you want to override any of the global `vCenter` values, fill in the relevant fields in the [`vCenter`](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.6/how-to/user-cluster-configuration-file#vcenter-section) section of your user cluster configuration file.

### `network`

Set `network.ipMode.type` to the same value that you set in your [admin cluster configuration file](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.6/how-to/admin-cluster-configuration-file): either `"dhcp"` or `"static"`.

If you set `ipMode.type` to `"static"`, create an [IP block file](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.6/how-to/ip-block-file) that provides the static IP addresses for the nodes in your user cluster. Then set [`network.ipMode.ipBlockFilePath`](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.6/how-to/user-cluster-configuration-file#network-ipblockfilepath-field) to the path of your IP block file.

Provide values for the remaining fields in the [`network`](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.6/how-to/user-cluster-configuration-file#network) section.

Regardless of whether you rely on a DHCP server or specify a list of static IP addresses, you need enough IP addresses to satisfy the following:

  * The nodes in your user cluster

  * An additional node in the user cluster to be used temporarily during upgrades




As mentioned previously, if you want to use static IP addresses, then you need to provide an IP block file. Here is an example of an IP block file with six hosts. This is enough addresses for a cluster that has five nodes and an occasional sixth node for upgrades:
    
    
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

### `loadBalancer`

Set aside a VIP for the Kubernetes API server of your user cluster. Set aside another VIP for the ingress service of your user cluster. Provide your VIPs as values for [`loadBalancer.vips.controlPlaneVIP`](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.6/how-to/user-cluster-configuration-file#loadbalancer-controlplanevip-field) and [`loadBalancer.vips.ingressVIP`](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.6/how-to/user-cluster-configuration-file#loadbalancer-ingresssvip-field).

Set `loadBalancer.kind` to the same value that you set in your [admin cluster configuration file](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.6/how-to/admin-cluster-configuration-file): `"ManualLB"`, `"F5BigIP"`, or `"Seesaw"`. Then fill in the corresponding section: [`manualLB`](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.6/how-to/user-cluster-configuration-file#loadbalancer-manuallb-section), [`f5BigIP`](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.6/how-to/user-cluster-configuration-file#loadbalancer-f5bigip-section), or [`seesaw`](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.6/how-to/user-cluster-configuration-file#loadbalancer-seesaw-section).

### `proxy`

If the network that will have your user cluster nodes is behind a proxy server, fill in the [`proxy`](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.6/how-to/user-cluster-configuration-file#proxy-section) section.

### `masterNode`

Fill in the [`masterNode`](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.6/how-to/user-cluster-configuration-file#masternode-section) section.

### `nodePools`

Fill in the [`nodePools`](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.6/how-to/user-cluster-configuration-file#nodepools-section) section.

### `antiAffinityGroups`

Set [`antiAffinityGroups.enabled`](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.6/how-to/user-cluster-configuration-file#antiaffinitygroups-enabled-field) to `true` or `false`.

### `authentication`

If you want to use OpenID Connect (OIDC) to authenticate users, fill in the [`authentication.oidc`](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.6/how-to/user-cluster-configuration-file#authentication-oidc-section) section.

If you want to provide an additional serving certificate for your user cluster's vCenter server, fill in the [`authentication.sni`](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.6/how-to/user-cluster-configuration-file#authentication-snir-section) section.

### `stackdriver`

Fill in the [`stackdriver`](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.6/how-to/user-cluster-configuration-file#stackdriver-section) section.

### `gkeConnect`

Fill in the [`gkeConnect`](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.6/how-to/user-cluster-configuration-file#gkeconnect-section) section.

### `cloudRun`

Set [`cloudRun.enabled`](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.6/how-to/user-cluster-configuration-file#cloudrun-section) to `true` or `false`.

### `usageMetering`

If you want to enable usage metering for your cluster, then fill in the [`usageMetering`](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.6/how-to/user-cluster-configuration-file#usagemetering-section) section.

### `cloudAuditLogging`

If you want to integrate the audit logs from your cluster's Kubernetes API server with Cloud Audit Logs, fill in the [`cloudAuditLogging`](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.6/how-to/user-cluster-configuration-file#cloudauditlogging-section) section.

## Validating your configuration file

After you've filled in your user cluster configuration file, run `gkectl check-config` to verify that the file is valid:
    
    
    gkectl check-config --kubeconfig [ADMIN_CLUSTER_KUBECONFIG] --config [CONFIG_PATH]
    

where:

  * [ADMIN_CLUSTER_KUBECONFIG] is the path of the kubeconfig file for your admin cluster.

  * [CONFIG_PATH] is the path of your user cluster configuration file.




If the command returns any failure messages, fix the issues and validate the file again.

If you want to skip the more time-consuming validations, pass the `--fast` flag. To skip individual validations, use the `--skip-validation-xxx` flags. To learn more about the `check-config` command, see [Running preflight checks](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.6/how-to/preflight-checks).

## Creating a Seesaw load balancer for your user cluster

If you have chosen to use the bundled Seesaw load balancer, do the step in this section. Otherwise, skip this section.

Create and configure the VMs for your [Seesaw load balancer](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.6/how-to/load-balance-basic#creating_ipblock_files):
    
    
    gkectl create loadbalancer --kubeconfig [ADMIN_CLUSTER_KUBECONFIG] --config [CONFIG_PATH]
    

where:

  * [ADMIN_CLUSTER_KUBECONFIG] is the path of the kubeconfig file for your admin cluster.

  * [CONFIG_PATH] is the path of your user cluster configuration file.




## Creating the user cluster

Create the user cluster:
    
    
    gkectl create cluster --kubeconfig [ADMIN_CLUSTER_KUBECONFIG]  \
      --config [CONFIG_PATH] --skip-validation-all
    

where 

  * [CONFIG_PATH] is the path of your user cluster configuration file.

  * [ADMIN_CLUSTER_KUBECONFIG] is the path of the kubeconfig file for your admin cluster.




The `gkectl create cluster` command creates a kubeconfig file named `[USER_CLUSTER_NAME]-kubeconfig` in the current directory. You will need this kubeconfig file later to interact with your user cluster.

Do not use the `--skip-validation-all` flag if you did not previously validate your user cluster configuration file.

## Verifying that your user cluster is running

Verify that your user cluster is running:
    
    
    kubectl get nodes --kubeconfig [USER_CLUSTER_KUBECONFIG]
    

where [USER_CLUSTER_KUBECONFIG] is the path of your kubeconfig file.

The output shows the user cluster nodes.

## Troubleshooting

See [Troubleshooting cluster creation and upgrade](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.6/troubleshoot-cluster-creation-upgrade).

## What's next

  * [Connect to your cluster from the Google Cloud console](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.6/how-to/connecting-to-a-cluster).
  * [Deploy an application](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.6/how-to/deploy-first-app).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
