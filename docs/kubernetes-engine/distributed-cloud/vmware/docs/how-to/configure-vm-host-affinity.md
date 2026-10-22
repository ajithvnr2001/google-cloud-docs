---
url: https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/configure-vm-host-affinity/
title: Configure VM host Group affinity \u00a0|\u00a0 Google Distributed Cloud software only for VMware \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T10:21:50.973590+00:00
---

# Configure VM host Group affinity  |  Google Distributed Cloud software only for VMware  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/configure-vm-host-affinity/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Google Distributed Cloud ](https://docs.cloud.google.com/distributed-cloud)
  * [ Documentation ](https://docs.cloud.google.com/kubernetes-engine/enterprise/clusters/docs)
  * [ GDC for VMware ](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs)
  * [ Guides ](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/overview)



Send feedback 

#  Configure VM host Group affinity Stay organized with collections  Save and categorize content based on your preferences. 

This document gives an example of how to configure a Google Distributed Cloud cluster to use [VM host affinity](https://techdocs.broadcom.com/us/en/vmware-cis/vsphere/vsphere/9-1/vsphere-resource-management.html).

VM host group affinity is one of the mechanisms that Google Distributed Cloud provides to ensure high availability. With VM host Group affinity, you create groups of physical ESXi hosts. Then you configure your cluster to associate VM groups with host groups.

For example, you could configure all VMs in one node pool to run on a particular host group. And you could configure all VMs in a second node pool to run on a different host group. You could then treat each node pool as a failure domain. To differentiate the failure domains, you could add labels to the VMs in the various node pools.

On [advanced clusters](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/concepts/advanced-clusters), VM host Group affinity is supported in version 1.32.200 and version 1.33 and later. If your cluster uses [topology domains](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/topology-domains-set-up), configure host groups in the [`topologyDomains[i].compute.hostGroups`](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/reference/vsphere-infrastructure-configuration-file#topology-domains-compute-host-groups) field of the vSphere infrastructure configuration file instead of the `nodePools[i].vsphere.hostgroups` field in the user cluster configuration file.

## Before you begin

For this exercise, you need to have at least six ESXi hosts in your vSphere environment.

## Create host groups

Create two or more host DRS groups in your vSphere environment. For this exercise, two host groups with three hosts each would be appropriate. For instructions, see [Create a Host DRS Group](https://techdocs.broadcom.com/us/en/vmware-cis/vsphere/vsphere/9-1/vsphere-resource-management.html).

## Create a user cluster

This section gives an example of how to create a user cluster that uses VM host Group affinity. The cluster in this example uses [Controlplane V2](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/user-cluster-configuration-file-latest#enablecontrolplanev2-field). The cluster has a high-availability control plane, so there are three control-plane nodes. In addition to the control-plane nodes, there are six worker nodes: three in one node pool and three in a second node pool. All nodes use static IP addresses.

Start by following the instructions in [Create a user cluster](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/create-user-cluster) (or [Create a user cluster for use with topology domains](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/create-user-cluster-topology-domains) if your cluster uses topology domains).

As you fill in your configuration files:

  * **Without topology domains** : In your user cluster configuration file, specify two node pools for worker nodes. For each node pool, set `replicas` to `3`, and provide the name of an existing host group in [`nodePools[i].vsphere.hostgroups`](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/user-cluster-configuration-file-latest#nodepool-vsphere-hostgroups-section).
  * **With topology domains** : In your vSphere infrastructure configuration file, specify two topology domains and provide the name of an existing host group in [`topologyDomains[i].compute.hostGroups`](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/reference/vsphere-infrastructure-configuration-file#topology-domains-compute-host-groups) for each domain. In your user cluster configuration file, specify two node pools for worker nodes, set `replicas` to `3`, and set [`nodePools[i].topologyDomains`](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/user-cluster-configuration-file-latest#nodepool-topology-domains-field) to associate each node pool with a topology domain.



## Example configuration file

The following examples show how to configure VM host Group affinity without topology domains and with topology domains.

### Without topology domains

Here is an example of an IP block file and a portion of a user cluster configuration file for a cluster that doesn't use topology domains.

#### user-ipblock.yaml
    
    
    blocks:
      - netmask: 255.255.255.0
        gateway: 172.16.21.1
        ips:
        - ip: 172.16.21.2
        - ip: 172.16.21.3
        - ip: 172.16.21.4
        - ip: 172.16.21.5
        - ip: 172.16.21.6
        - ip: 172.16.21.7
        - ip: 172.16.21.8
    
    

#### user-cluster-yaml
    
    
    apiVersion: v1
    kind: UserCluster
    ...
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
      controlPlaneIPBlock:
        netmask: "255.255.255.0"
        gateway: "172.16.21.1"
        ips:
        - ip: "172.16.21.9"
          hostname: "cp-vm-1"
        - ip: "172.16.21.10"
          hostname: "cp-vm-2"
        - ip: "172.16.21.11"
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
    ...
    enableAdvancedCluster: true
    enableControlplaneV2: true
    masterNode:
      cpus: 4
      memoryMB: 8192
      replicas: 3
    nodePools:
    - name: "worker-pool-1"
      enableLoadBalancer: true
      replicas: 3
      vsphere:
        hostgroups:
        - "hostgroup-1"
      labels:
        failuredomain: "failuredomain-1"
    - name: "worker-pool-2"
      replicas: 3
      vsphere:
        hostgroups:
        - "hostgroup-2"
      labels:
        failuredomain: "failuredomain-2"
    ...
    

These are the important points to understand in the preceding example:

  * The static IP addresses for the worker nodes are specified in an IP block file. The IP block file has seven addresses even though there are only six worker nodes. The extra IP address is needed during cluster upgrade, update, and auto repair.

  * The static IP addresses for the three control-plane nodes are specified in the `network.controlPlaneIPBlock` section of the user cluster configuration file. There is no need for an extra IP address in this block.

  * The `masterNode.replicas` field is set to `3`, so there will be three control-plane nodes.

  * A cluster controller will create a VM DRS group that has the three nodes in the `worker-pool-1` node pool. A controller will also create a [VM host affinity rule](https://techdocs.broadcom.com/us/en/vmware-cis/vsphere/vsphere/9-1/vsphere-resource-management.html) that ensures nodes in `worker-pool-1` will run on hosts that are in `hostgroup-1`. The nodes in `worker-pool-1` have the label `failuredomain: "failuredomain-1"`

  * A cluster controller will create a VM DRS group that has the three nodes in the `worker-pool-2` node pool. A controller will also create a VM host affinity rule that ensures nodes in `worker-pool-2` will run on hosts that are in `hostgroup-2`. The nodes in `worker-pool-2` have the label `failuredomain: "failuredomain-2"`




Continue creating your user cluster as described in [Create a user cluster](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/create-user-cluster).

### With topology domains

Here is an example of a portion of a [vSphere infrastructure configuration file](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/reference/vsphere-infrastructure-configuration-file) and a user cluster configuration file for an advanced cluster that uses [topology domains](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/topology-domains-set-up).

#### vsphere-infra-config.yaml

Each topology domain in the vSphere infrastructure configuration file specifies a host group in `topologyDomains[i].compute.hostGroups` and a failure-domain label in `topologyDomains[i].topologyLabels`.
    
    
    apiVersion: vmware.cluster.gke.io/v1alpha1
    kind: VSphereInfraConfig
    metadata:
      name: default
    ...
    topologyDomains:
    - name: "topology-domain-1"
      topologyLabels:
        "topology.kubernetes.io/zone": "zone-1"
      compute:
        vcenter: "vc01.example"
        datacenter: "dc-1"
        cluster: "cls-1"
        resourcePool: "rp-1"
        hostGroups:
        - "hostgroup-1"
      storage:
        datastore: "vsanDatastore"
      network:
        vsphereNetwork: "vm-network-1"
        gateway: "172.16.21.1"
        dnsServers:
        - "203.0.113.2"
        - "198.51.100.2"
        ntpServers:
        - "216.239.35.4"
    - name: "topology-domain-2"
      topologyLabels:
        "topology.kubernetes.io/zone": "zone-2"
      compute:
        vcenter: "vc01.example"
        datacenter: "dc-1"
        cluster: "cls-1"
        resourcePool: "rp-1"
        hostGroups:
        - "hostgroup-2"
      storage:
        datastore: "vsanDatastore"
      network:
        vsphereNetwork: "vm-network-1"
        gateway: "172.16.21.1"
        dnsServers:
        - "203.0.113.2"
        - "198.51.100.2"
        ntpServers:
        - "216.239.35.4"
    

#### user-cluster.yaml

In the following example of a user cluster configuration file, the `nodePools[i].vsphere` section is removed, and each node pool references its topology domain in `nodePools[i].topologyDomains`.

A cluster controller creates a VM DRS group and a VM host affinity rule for `worker-pool-1` (in `topology-domain-1`) so that its nodes run on hosts in `hostgroup-1` and receive the label `topology.kubernetes.io/zone: "zone-1"`. Similarly, a cluster controller creates a VM DRS group and a VM host affinity rule for `worker-pool-2` (in `topology-domain-2`) so that its nodes run on hosts in `hostgroup-2` and receive the label `topology.kubernetes.io/zone: "zone-2"`.
    
    
    apiVersion: v1
    kind: UserCluster
    ...
    enableAdvancedCluster: true
    enableControlplaneV2: true
    masterNode:
      cpus: 4
      memoryMB: 8192
      replicas: 3
      topologyDomains:
      - "topology-domain-1"
    nodePools:
    - name: "worker-pool-1"
      replicas: 3
      osImageType: "ubuntu_cgv2"
      topologyDomains:
      - "topology-domain-1"
    - name: "worker-pool-2"
      replicas: 3
      osImageType: "ubuntu_cgv2"
      topologyDomains:
      - "topology-domain-2"
    ...
    

Continue to [create a user cluster for use with topology domains](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/create-user-cluster-topology-domains).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-21 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-21 UTC."],[],[]] 
