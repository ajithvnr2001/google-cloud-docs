---
url: https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.13/how-to/ip-block-file/
title: IP block file \u00a0|\u00a0 Anthos clusters on VMware \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T20:03:15.506549+00:00
---

# IP block file  |  Anthos clusters on VMware  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.13/how-to/ip-block-file/

**Version 1.13**. This version is no longer supported. For more information see the [ version support policy](https://cloud.google.com/anthos/clusters/docs/on-prem/latest/getting-support#version_support_policy). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Google Kubernetes Engine (GKE) ](https://docs.cloud.google.com/kubernetes-engine)
  * [ GKE Enterprise ](https://docs.cloud.google.com/kubernetes-engine/enterprise/docs)
  * [ Clusters ](https://docs.cloud.google.com/anthos/clusters)
  * [ Documentation ](https://docs.cloud.google.com/anthos/clusters/docs)
  * [ Anthos clusters on VMware 1.13 ](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.13)
  * [ Guides ](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.13/overview)



Send feedback 

#  IP block file Stay organized with collections  Save and categorize content based on your preferences. 

Version 1.13 keyboard_arrow_down

  * [ Latest version ](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/latest/how-to/ip-block-file)
  * [ Version 1.16 ](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.16/how-to/ip-block-file)
  * [ Earlier versions (unsupported) ](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/latest/version-history#expandable-1)



This page describes the fields in an IP block file, which is used in the setup of Google Distributed Cloud.

You use an IP block file to describe a set of machines and the network that the machines are on. Here are some examples of how you would use an IP block file:

  * List the hostnames and static IP addresses for the nodes in your admin cluster.

  * List the hostnames and static IP addresses for the nodes in a user cluster.

  * List the hostnames and static IP addresses for the VMs that run the bundled Seesaw load balancer for your admin cluster.

  * List the hostnames and static IP addresses for the VMs that run the bundled Seesaw load balancer for a user cluster.


**Note:** If your system uses a Docker runtime, note that the default network of the docker daemon is 172.17.0.0/16. Make sure that the IP addresses you select for the VMs for the admin cluster and user clusters are not in that network.

**Template**

Click to see a template for an IP block file.
    
    
      blocks:
      - netmask: ""
        gateway: ""
        ips:
        - ip: ""
          hostname: ""
        - ip: ""
          hostname: ""
        ...
      

## Filling in the fields in an IP block file

## `blocks`

An array of objects, each of which describes a set of hosts.

### `blocks[i].netmask`

String. The subnet mask for the set of hosts. For example:
    
    
    blocks:
    - netmask: "255.255.252.0"
    

### `blocks[i].gateway`

String. The address of the default gateway for the set of hosts. For example:
    
    
    blocks:
    - netmask: "255.255.252.0"
      gateway: "172.16.23.254"
    

### `blocks[i].ips`

An array of objects. Each object has an individual IP address or a [CIDR](https://tools.ietf.org/html/rfc4632) block of IP addresses. If the object has an individual IP address, it can also have a hostname.

For example:
    
    
    blocks:
    - netmask: "255.255.252.0"
      gateway: "172.16.23.254"
      ips:
      - ip: 172.16.20.10
        hostname: admin-host1
      - ip: 172.16.20.11
        hostname: admin-host2
      - ip: 172.16.20.12/30
    

The preceding example specifies six IP addresses: two individual addresses and a CIDR block of four addresses.

If you set `ip` to a CIDR block, do not specify a value for `hostname`.

When you do not specify a value for `hostname`, Google Distributed Cloud uses the VM's name from vSphere as the hostname.

## Old fields

Previous versions of Google Distributed Cloud used a `hostconfig` section in the IP block file:
    
    
    hostconfig:
      dns: ""
      tod: ""
      otherdns:
      - ""
      ...
      othertod:
      - ""
      ...
      searchdomainsfordns:
      - ""
      ...
    

Do not provide a `hostconfig` section in your IP block file. Instead, fill in the `network.hostConfig` section of your [admin cluster configuration file](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.13/how-to/admin-cluster-configuration-file#network-hostconfig-section) or [user cluster configuration file](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.13/how-to/user-cluster-configuration-file#network-hostconfig-section).

If you fill in the `network.hostConfig` section of a cluster configuration file, Google Distributed Cloud ignores the `hostconfig` sections of all IP block files associated with the cluster.

If you do not fill in the `network.hostConfig` section of a cluster configuration file, then for backward compatibility, Google Distributed Cloud reads the `hostconfig` sections of the IP block files associated with the cluster.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
