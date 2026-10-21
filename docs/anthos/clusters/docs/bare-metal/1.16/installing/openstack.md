---
url: https://docs.cloud.google.com/anthos/clusters/docs/bare-metal/1.16/installing/openstack/
title: Configure your clusters to use OpenStack \u00a0|\u00a0 Google Distributed Cloud Virtual for Bare Metal \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-15T20:46:14.434709+00:00
---

# Configure your clusters to use OpenStack  |  Google Distributed Cloud Virtual for Bare Metal  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/anthos/clusters/docs/bare-metal/1.16/installing/openstack/

**Version 1.16**. This version is no longer supported. For information about how to upgrade to version 1.28, see [ Upgrade clusters](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/how-to/upgrade) in the latest documentation. For more information about supported and unsupported versions, see the [Versioning](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/version-history) page in the latest documentation.

  * [ Home ](https://docs.cloud.google.com/)
  * [ Google Distributed Cloud ](https://docs.cloud.google.com/distributed-cloud)
  * [ Documentation ](https://docs.cloud.google.com/kubernetes-engine/enterprise/clusters/docs)
  * [ GDCV for Bare Metal 1.16 ](https://docs.cloud.google.com/anthos/clusters/docs/bare-metal/1.16)
  * [ Guides ](https://docs.cloud.google.com/anthos/clusters/docs/bare-metal/1.16/concepts/about-bare-metal)



Send feedback 

#  Configure your clusters to use OpenStack Stay organized with collections  Save and categorize content based on your preferences. 

Version 1.16 keyboard_arrow_down

  * [ Latest ](https://docs.cloud.google.com/anthos/clusters/docs/bare-metal/latest/installing/openstack)
  * [ Version 1.16 ](https://docs.cloud.google.com/anthos/clusters/docs/bare-metal/1.16/installing/openstack)
  * [ Earlier versions (unsupported) ](https://docs.cloud.google.com/anthos/clusters/docs/bare-metal/1.16/getting-support#version-support)



Distributed Cloud supports the OpenStack Kubernetes Cloud provider. Use this feature to automatically provision OpenStack Load Balancing as a Service (LBaaS) resources. Those resources can replace the MetalLB resources to easily expose services running on your Anthos on bare metal clusters to other OpenStack tenants or outside the OpenStack network.

## Before you begin

Decide the Anthos clusters that need to use OpenStack LBaaS resources.

**Warning:** After initializing your clusters, you can't change the configuration to switch to MetalLB resources. Make sure you initialize your clusters with the correct cloud provider configuration.

Ensure you have access to the machines you are trying to configure.

Learn more about[ running the cloud-controller-manager in the Kubernetes documentation](https://kubernetes.io/docs/tasks/administer-cluster/running-cloud-controller/#running-cloud-controller-manager).

## Change your clusters' configuration file

The OpenStack Kubernetes Cloud Provider requires that `kubelet` runs on all the nodes with the following argument:
    
    
    cloud-provider: "external"
    

To ensure your Anthos clusters easily meet this requirement, add the `baremetal.cluster.gke.io/external-cloud-provider: "true"` annotation to your clusters' configuration file under the metadata section before initializing them.

The entry in your configuration file should look like the following example:
    
    
    apiVersion: baremetal.cluster.gke.io/v1
    kind: Cluster
    metadata:
      name: cluster1
      namespace: cluster-cluster1
      annotations:
        baremetal.cluster.gke.io/external-cloud-provider: "true"
    spec:
      ..
    

Some cloud providers on other cloud platforms require a special format for `providerID`, Google Distributed Cloud will generate a `providerID` for each machine. The format is like `baremetal://MACHINE_ADDRESS`. If you want to have a different `providerID`, you can specify one for each node along with the IP address. The configuration will look like:
    
    
     apiVersion: baremetal.cluster.gke.io/v1
     kind: Cluster
     metadata:
       name: cluster1
       namespace: cluster-cluster1
     spec:
       clusterNetwork:
         pods:
           cidrBlocks:
           - 192.168.0.0/16
         services:
           cidrBlocks:
           - 10.96.0.0/20
       controlPlane:
         nodePoolSpec:
           nodes:
           - address: 10.200.0.1
    +        providerID: some-prefix://unique-string
           - address: 10.200.0.2
    +        providerID: some-prefix2://unique-string2
      ...
    
    ---
     apiVersion: baremetal.cluster.gke.io/v1
     kind: NodePool
     metadata:
       name: nodepool1
       namespace: cluster-admin1
     spec:
       clusterName: admin1
       nodes:
       - address: 172.18.0.2
    +    providerID: some-prefix3://unique-string3
    

After you edit the configuration file, use the following command to initialize your cluster:
    
    
    bmctl create cluster -c cluster1
    

Now, all nodes in `cluster1` run with the required argument: `cloud-provider: "external"`

All nodes also have the following fields added to their configuration files:
    
    
    taints:
    - effect: NoSchedule
      key: node.cloudprovider.kubernetes.io/uninitialized
      value: "true"
    

These fields are removed after you initialize your cloud provider on this cluster.

`kubelet` will run with your provided `providerID` if you specified one for this node.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
