---
url: https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/ip-block-file/
title: IP block file \u00a0|\u00a0 Google Distributed Cloud software only for VMware \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:22:44.558383+00:00
---

# IP block file  |  Google Distributed Cloud software only for VMware  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/ip-block-file/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Google Distributed Cloud ](https://docs.cloud.google.com/distributed-cloud)
  * [ Documentation ](https://docs.cloud.google.com/kubernetes-engine/enterprise/clusters/docs)
  * [ GDC for VMware ](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs)
  * [ Guides ](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/overview)



Send feedback 

#  IP block file Stay organized with collections  Save and categorize content based on your preferences. 

This page describes the fields in an IP block file, which is used in the setup of Google Distributed Cloud.

You use an IP block file to describe a set of node machines and the network that the machines are connected to. You create a separate IP block file for each cluster. Both the admin and user cluster configuration files have a field called `network.ipMode.ipBlockFilePath`. You specify the absolute or relative path of the IP block in this field.

Use an IP block file to list the IP addresses and optionally the hostnames in the following cases:

  * User clusters:

    * If [`network.ipMode.type`](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/user-cluster-configuration-file-latest#network-ipmode-type-field) is set to `"static"` in the user cluster configuration file, list the IP addresses for worker nodes in the user cluster IP block file.

    * If [`infraConfigFilePath`](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/admin-cluster-configuration-file-latest#infra-config-file-path-field) is configured in the admin cluster configuration file (which enables topology domains), list the IP addresses for the control-plane nodes in the user cluster IP block file. The IP addresses for control-plane nodes are always static IP addresses even if worker nodes use DHCP.

  * Admin clusters:

    * If [`infraConfigFilePath`](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/admin-cluster-configuration-file-latest#infra-config-file-path-field) is configured in the admin cluster configuration file (which enables topology domains), list the IP addresses for the control-plane nodes in the admin cluster IP block file.

    * 1.16 and lower non-HA admin cluster: list the IP addresses for the control-plane node and add-on nodes in the admin cluster IP block file.

    * 1.16 and lower HA admin cluster: list the IP addresses for add-on nodes in an IP block file.

    * 1.29 and lower kubeception user clusters: list the IP addresses for the user cluster control-plane nodes in the admin cluster IP block file.


**Note:** If your system uses a Docker runtime, the default network of the Docker daemon is `172.17.0.0/16`. Make sure that the IP addresses you select for the VMs for the admin cluster aren't in that network.

**Template**

Click to see a template for an IP block file.
    
    
      blocks:
      - netmask: "NETMASK"
        gateway: "GATEWAY"
        ips:
        - ip: "IP_ADDRESS_1"
          hostname: "HOSTNAME_1"
        - ip: "IP_ADDRESS_2"
          hostname: "HOSTNAME_2"
        - ip: "IP_ADDRESS_3"
          hostname: "HOSTNAME_3"
        ...
      

## Filling in the fields in an IP block file

This section describes the fields in an IP block file.

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

An array of objects. Each object has an individual IP address or a [CIDR](https://tools.ietf.org/html/rfc4632) block of IP addresses.

  * If the object has an individual IP address, optionally, it can also have a hostname.

  * If you set `ip` to a CIDR block, don't specify a value for `hostname`.

  * When you don't specify a value for `hostname`, Google Distributed Cloud uses the VM's name from vSphere as the hostname.




### `blocks[i].isControlPlane`

If `infraConfigFilePath` is configured in the admin cluster configuration file, and if the IP address is for a control-plane node, include `isControlPlane: true`. For user cluster worker nodes, specify `false` or omit the field because the default value is `false`.

## Example configuration files

The section provides some configurations with examples values filled in.

### Example 1

This example specifies six IP addresses: two individual addresses and a CIDR block of four addresses.
    
    
    blocks:
    - netmask: "255.255.252.0"
      gateway: "203.0.113.1"
      ips:
      - ip: 198.51.100.10
        hostname: worker-node1
      - ip: 198.51.100.11
        hostname: worker-node2
      - ip: 198.51.100.12/30  # 198.51.100.12 - 198.51.100.15
    

### Example 2

This example shows an IP block file configured for topology domains.
    
    
    blocks:
    - netmask: 255.255.255.0
      gateway: 100.115.222.254
      ips:
      - ip: 100.115.222.204
        hostname: worker-1
      - ip: 100.115.222.205
        hostname: cp-1
        isControlPlane: true
      - ip: 100.115.222.206
        hostname: cp-2
        isControlPlane: true
      - ip: 100.115.222.207
        hostname: cp-3
        isControlPlane: true
      - ip: 100.115.222.220/28 # 100.115.222.208 - 100.115.222.223
    - netmask: 255.255.255.0
      gateway: 100.115.223.254
      ips:
      - ip: 100.115.223.206
        hostname: worker-2
      - ip: 100.115.223.220/28 # 100.115.223.208 - 100.115.223.223
    - netmask: 255.255.255.0
      gateway: 100.115.224.254
      ips:
      - ip: 100.115.224.206
        hostname: worker-3
      - ip: 100.115.224.220/28 # 100.115.224.208 - 100.115.224.223
    

This example IP block file reserved IP addresses from three subnets, and each subnet is represented as `blocks[i]`. The `blocks[i].gateway` is important, as it works as the identification of the IP block. You add the same IP address to `topologyDomains[i].network.gateway` in the `VSphereInfraConfig` custom resource inside the [vSphere Infrastructure Configuration File.](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/reference/vsphere-infrastructure-configuration-file)

There are three IPs configured with `isControlPlane: true`, which indicates that these IP addresses are reserved for control-plane nodes only. In the IP block file of the admin cluster or user cluster, there must be three IP addresses reserved for control-plane nodes. Reserve them in the target subnet according to the applicable topology of the cluster.

Because the control-plane nodes must be in a single topology domain, the IP addresses for the control-plane nodes must be in the same IP block.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
