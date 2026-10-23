---
url: https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/installing/openstack/
title: Configure your clusters to use OpenStack \u00a0|\u00a0 Google Distributed Cloud software only for bare metal \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:22:15.647724+00:00
---

# Configure your clusters to use OpenStack  |  Google Distributed Cloud software only for bare metal  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/installing/openstack/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Distributed, hybrid, and multicloud ](https://docs.cloud.google.com/docs/dhm-cloud)
  * [ Google Distributed Cloud ](https://docs.cloud.google.com/distributed-cloud/docs)
  * [ GDC for bare metal ](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs)
  * [ Guides ](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/concepts/about-bare-metal)



Send feedback 

#  Configure your clusters to use OpenStack Stay organized with collections  Save and categorize content based on your preferences. 

Running Distributed Cloud software only for bare metal on OpenStack lets you integrate your clusters with OpenStack Infrastructure as a Service (IaaS), Load Balancing as a Service (LBaaS), and Storage. Configuring your clusters for an external cloud provider delegates the node initialization process to OpenStack.

You can automatically provision OpenStack LBaaS resources instead of MetalLB to expose Services running on your clusters to other OpenStack tenants or outside the OpenStack network. For more information about OpenStack features and benefits, see the [OpenStack documentation](https://docs.openstack.org/2023.2/).

## Related examples

This document only covers how to configure your cluster for use with OpenStack. The following guides walk you through an example deployment:

  * [Deploy a cluster on OpenStack](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/installing/openstack-abm-install) walks you through a sample deployment of a hybrid cluster on OpenStack virtual machines (VMs). The deployment uses a script to simplify the installation. The guide also shows you one way to enable load balancing as a Service (LBaaS).

  * [Configure the OpenStack Cloud Provider for Kubernetes](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/installing/openstack-k8s-provider) shows you how to install the OpenStack Cloud Provider on a cluster that's been deployed on OpenStack. The OpenStack Cloud Provider isn't required to use Google Distributed Cloud software with OpenStack.




## Before you begin

  * Decide which clusters need to use OpenStack LBaaS resources.

Once you've created a cluster configured to use OpenStack LBaaS resources, you can't change the configuration to switch to MetalLB resources. Make sure that you initialize your clusters with the correct cloud provider configuration.

  * Ensure you have access to the machines you're trying to configure.




Learn more about [running the cloud-controller-manager](https://kubernetes.io/docs/tasks/administer-cluster/running-cloud-controller/#running-cloud-controller-manager) in the Kubernetes documentation.

## Change your cluster configuration file

The OpenStack Kubernetes Cloud Provider requires that `kubelet` runs on all the nodes with the following argument:

**Note:** The OpenStack Cloud Provider is used as an example in [Configure the OpenStack Cloud Provider for Kubernetes](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/installing/openstack-k8s-provider), but it isn't required to integrate Google Distributed Cloud with OpenStack.
    
    
    cloud-provider: "external"
    

To ensure that your cluster meets this requirement, add the `baremetal.cluster.gke.io/external-cloud-provider: "true"` annotation to your cluster configuration file under the metadata section before you create the cluster.

The entry in your configuration file should look like the following example:
    
    
    apiVersion: baremetal.cluster.gke.io/v1
    kind: Cluster
    metadata:
      name: cluster1
      namespace: cluster-cluster1**  annotations:
        baremetal.cluster.gke.io/external-cloud-provider: "true"**
    spec:
      ...
    

Some cloud providers on other cloud platforms require a special format for `providerID`. Google Distributed Cloud generates a `providerID` with a format like `baremetal://MACHINE_ADDRESS` for each node machine. If you want to have a different `providerID`, you can specify one for each node along with the IP address.

The following sample cluster configuration file shows how you specify `providerID` for your cluster nodes:
    
    
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
           - address: 10.200.0.1** +        providerID: some-prefix://unique-string**
           - address: 10.200.0.2** +        providerID: some-prefix2://unique-string2**
      ...
    
    ---
     apiVersion: baremetal.cluster.gke.io/v1
     kind: NodePool
     metadata:
       name: nodepool1
       namespace: cluster-cluster1
     spec:
       clusterName: cluster1
       nodes:
       - address: 172.18.0.2** +    providerID: some-prefix3://unique-string3**
    

## Create your cluster

After you edit the configuration file, use the following command to initialize your cluster:
    
    
    bmctl create cluster -c cluster1
    

For more information about creating clusters, see [Cluster creation overview](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/installing/creating-clusters/create-clusters-overview).

## Node configuration

When you create a cluster configured for OpenStack, the cluster nodes have the following changes:

  * All nodes in `cluster1` run with the required argument: `cloud-provider: "external"`.

  * All nodes also have the following taint added to their configuration files:
        
        taints:
        - effect: NoSchedule
          key: node.cloudprovider.kubernetes.io/uninitialized
          value: "true"
        

These taints are removed after you initialize your cloud provider on this cluster.

  * `kubelet` runs with the `providerID` you specified in the cluster configuration file.




## What's next

  * [Deploy a cluster on OpenStack](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/installing/openstack-abm-install)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
