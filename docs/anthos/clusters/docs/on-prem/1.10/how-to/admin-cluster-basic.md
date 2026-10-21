---
url: https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.10/how-to/admin-cluster-basic/
title: Create an admin cluster (quickstart) \u00a0|\u00a0 Anthos clusters on VMware \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-15T16:26:53.077936+00:00
---

# Create an admin cluster (quickstart)  |  Anthos clusters on VMware  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.10/how-to/admin-cluster-basic/

**Version 1.10**. This version is no longer supported. For more information see the [ version support policy](https://cloud.google.com/anthos/clusters/docs/on-prem/latest/getting-support#version_support_policy). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Google Kubernetes Engine (GKE) ](https://docs.cloud.google.com/kubernetes-engine)
  * [ GKE Enterprise ](https://docs.cloud.google.com/kubernetes-engine/enterprise/docs)
  * [ Clusters ](https://docs.cloud.google.com/anthos/clusters)
  * [ Documentation ](https://docs.cloud.google.com/anthos/clusters/docs)
  * [ Anthos clusters on VMware 1.10 ](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.10)
  * [ Guides ](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.10/overview)



Send feedback 

#  Create an admin cluster (quickstart) Stay organized with collections  Save and categorize content based on your preferences. 

Version 1.10 keyboard_arrow_down

  * [ Latest version ](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/latest/how-to/admin-cluster-quickstart)
  * [ Version 1.16 ](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.16/how-to/admin-cluster-quickstart)
  * [ Earlier versions (unsupported) ](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/latest/version-history#expandable-1)



This document shows how to create an admin cluster for Google Distributed Cloud.

The instructions here are part of a quickstart. For full instructions on how to create an admin cluster, see [Creating an admin cluster](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.10/how-to/create-admin-cluster).

## Before you begin

[Create an Admin workstation (quickstart)](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.10/how-to/admin-workstation-quickstart)

[Prepare to create a Seesaw load balancer (quickstart)](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.10/how-to/seesaw-load-balance-quickstart)

## Get an SSH connection to your admin workstation

[Get an SSH connection](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.10/how-to/admin-workstation-quickstart#getting_an_ssh_connection_to_your_admin_workstation) to your admin workstation.

Recall that `gkeadm` activated your component access service account on the admin workstation.

Do all the remaining steps in this topic on your admin workstation in the home directory.

**Note:** If you're using internal DNS names, or your workstation cannot access Google public DNS addresses (8.8.8.8 or 8.8.4.4), you must specify your internal nameserver in [`/etc/resolv.conf`](https://ubuntu.com/server/docs#name-resolution).

## Specify static IPs for your admin cluster

To specify the static IP addresses that you want to use for your admin cluster, create an [IP block file](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.10/how-to/ip-block-file) named `admin-cluster-ipblock.yaml`.

You need five IP addresses for the following nodes in your admin cluster:

  * Three nodes to run the admin cluster control plane and add-ons

  * An additional node to be used temporarily during upgrades

  * One node to run the control plane for the user cluster that you will create later




Here is an example of an IP block file with five hosts:
    
    
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

The `ips` field is an array of IP addresses and hostnames. These are the IP addresses and hostnames that Google Distributed Cloud will assign to your admin cluster nodes.

In the IP block file, you also specify a subnet mask and a default gateway for the admin cluster nodes.

## Credentials configuration file

When you used `gkeadm` to create your admin workstation, you filled in a credentials configuration file named `credential.yaml`. This file holds the username and password for your vCenter server.

## Admin cluster configuration file

When `gkeadm` created your admin workstation, it generated a configuration file named `admin-cluster.yaml`. This configuration file is for creating your admin cluster.

## Fill in your admin cluster configuration file

Several fields in your admin cluster configuration file are already filled in with default values, generated values, or values that you provided when you created your admin workstation. You can leave those fields unchanged.

Fill in the following fields. For instructions on how to fill in the fields, see [Admin cluster configuration file](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.10/how-to/admin-cluster-configuration-file).
    
    
    vCenter:
      dataDisk: "Fill in"
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
      seesaw:
        ipBlockFilePath: "Fill in"
        vrid: Fill in
        masterIP: "Fill in"
    

## Validate the admin cluster configuration file

Verify that the your admin cluster configuration file is valid and can be used for cluster creation:
    
    
    gkectl check-config --config admin-cluster.yaml
    

## Prepare your vSphere environment

Run `gkectl prepare` to initialize your vSphere environment:
    
    
    gkectl prepare --config admin-cluster.yaml
    

## Create a load balancer for your admin cluster

Create and configure the VM for your [Seesaw load balancer](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.10/how-to/seesaw-load-balance-quickstart):
    
    
    gkectl create loadbalancer --config admin-cluster.yaml
    

## Create the admin cluster

Create the admin cluster:
    
    
    gkectl create admin --config admin-cluster.yaml
    

## Locate the admin cluster kubeconfig file

The `gkectl create admin` command creates a kubeconfig file named `kubeconfig` in the current directory. You will need this kubeconfig file later to interact with your admin cluster.

## Verify that your admin cluster is running

Verify that your admin cluster is running:
    
    
    kubectl get nodes --kubeconfig kubeconfig
    

The output shows the admin cluster nodes. For example:
    
    
    gke-admin-master-hdn4z            Ready    control-plane,master ...
    gke-admin-node-7f46cc8c47-g7w2c   Ready ...
    gke-admin-node-7f46cc8c47-kwlrs   Ready ...
    

## What's next

[Create a user cluster (quickstart)](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.10/how-to/user-cluster-quickstart)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
