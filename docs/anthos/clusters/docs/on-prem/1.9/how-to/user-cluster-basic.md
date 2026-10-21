---
url: https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.9/how-to/user-cluster-basic/
title: Create a user cluster (quickstart) \u00a0|\u00a0 Anthos clusters on VMware \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-15T15:04:54.072919+00:00
---

# Create a user cluster (quickstart)  |  Anthos clusters on VMware  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.9/how-to/user-cluster-basic/

**Version 1.9**. This version is no longer supported. For more information see the [ version support policy](https://cloud.google.com/anthos/clusters/docs/on-prem/latest/getting-support#version_support_policy). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Google Kubernetes Engine (GKE) ](https://docs.cloud.google.com/kubernetes-engine)
  * [ GKE Enterprise ](https://docs.cloud.google.com/kubernetes-engine/enterprise/docs)
  * [ Clusters ](https://docs.cloud.google.com/anthos/clusters)
  * [ Documentation ](https://docs.cloud.google.com/anthos/clusters/docs)
  * [ Anthos clusters on VMware 1.9 ](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.9)
  * [ Guides ](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.9/overview)



Send feedback 

#  Create a user cluster (quickstart) Stay organized with collections  Save and categorize content based on your preferences. 

Version 1.9 keyboard_arrow_down

  * [ Latest version ](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/latest/how-to/user-cluster-quickstart)
  * [ Version 1.16 ](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.16/how-to/user-cluster-quickstart)
  * [ Earlier versions (unsupported) ](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/latest/version-history#expandable-1)



This document shows how to create a user cluster for Google Distributed Cloud.

The instructions here are part of a quickstart. For full instructions on how to create a user cluster, see [Creating a user cluster](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.9/how-to/create-user-cluster).

## Before you begin

[Create an admin cluster (quickstart)](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.9/how-to/admin-cluster-quickstart)

## Get an SSH connection to your admin workstation

[Get an SSH connection to your admin workstation](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.9/how-to/admin-workstation-quickstart#getting_an_ssh_connection_to_your_admin_workstation).

Your component access service account is activated on your admin workstation.

Do all the remaining steps in this topic on your admin workstation in the home directory.

## Specify static IPs for your user cluster

To specify the static IP addresses that you want to use for your user cluster, create an [IP block file](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.9/how-to/ip-block-file) named `user-cluster-ipblock.yaml`. For this exercise, you need to specify three IP addresses to be used by the user cluster.

Here is an example of an IP block file with three hosts:
    
    
    blocks:
      - netmask: 255.255.252.0
        gateway: 172.16.23.254
        ips:
        - ip: 172.16.20.15
          hostname: user-host1
        - ip: 172.16.20.16
          hostname: user-host2
        - ip: 172.16.20.17
          hostname: user-host3

The `ips` field is an array of IP addresses and hostnames. These are the IP addresses and hostnames that Google Distributed Cloud will assign to your user cluster nodes.

In the IP block file, you also specify the addresses of the DNS servers, time servers, and default gateway that the user cluster nodes will use.

## User cluster configuration file

When `gkeadm` created your admin workstation, it generated a configuration file named `user-cluster.yaml`. This configuration file is for creating your user cluster.

## Fill in your user cluster configuration file

Several fields in your user cluster configuration file are already filled in with default values, generated values, or values that you provided when you created your admin workstation. You can leave those fields unchanged.

Fill in the following fields. For instructions on how to fill in the fields, see [User cluster configuration file](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.9/how-to/user-cluster-configuration-file).
    
    
    name: "Fill in"
    network:
      hostConfig:
        dnsServers:
        - "Fill in"
        ntpServers:
        - "Fill in"
        searchDomainsForDNS:
        - "Fill in (optional)"
      ipMode:
        type: Fill in. Set to "static".
        ipBlockFilePath: "Fill in"
    loadBalancer:
      vips:
        controlPlaneVIP: "Fill in"
        ingressVIP: "Fill in"
      seesaw:
        ipBlockFilePath: "Fill in"
        vrid: Fill in
        masterIP: "Fill in"
    

## Validate the user cluster configuration file

Verify that the your user cluster configuration file is valid and can be used for cluster creation:
    
    
    gkectl check-config --kubeconfig kubeconfig --config user-cluster.yaml
    

## Create a load balancer for your user cluster

Create and configure the VM for your Seesaw load balancer:
    
    
    gkectl create loadbalancer --kubeconfig kubeconfig --config user-cluster.yaml
    

## Create the user cluster

Create the user cluster:
    
    
    gkectl create cluster --kubeconfig kubeconfig --config user-cluster.yaml
    

## Locate the user cluster kubeconfig file

The `gkectl create cluster` command creates a kubeconfig file named `USER_CLUSTER_NAME-kubeconfig` in the current directory. You will need this kubeconfig file later to interact with your user cluster.

## Verify that your user cluster is running

Verify that your user cluster is running:
    
    
    kubectl get nodes --kubeconfig USER_CLUSTER_KUBECONFIG
    

Replace USER_CLUSTER_KUBECONFIG with the path of your kubeconfig file.

The output shows the user cluster nodes. For example:
    
    
    my-user-cluster-node-pool-69-d46d77885-7b7tx   Ready ...
    my-user-cluster-node-pool-69-d46d77885-lsvzk   Ready ...
    my-user-cluster-node-pool-69-d46d77885-sswjk   Ready ...
    

## What's next

  * [Deploy an application](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.9/how-to/deploy-first-app).
  * [Connect to your cluster from the Google Cloud console](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.9/how-to/connecting-to-a-cluster).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
