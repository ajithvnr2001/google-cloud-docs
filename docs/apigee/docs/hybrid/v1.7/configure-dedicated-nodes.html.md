---
url: https://docs.cloud.google.com/apigee/docs/hybrid/v1.7/configure-dedicated-nodes.html
title: Configuring dedicated node pools \u00a0|\u00a0 Apigee \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-15T13:42:00.801053+00:00
---

# Configuring dedicated node pools  |  Apigee  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/apigee/docs/hybrid/v1.7/configure-dedicated-nodes.html

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Apigee ](https://docs.cloud.google.com/apigee/docs)
  * [ Guides ](https://docs.cloud.google.com/apigee/docs/api-platform/get-started/what-apigee)



Send feedback 

#  Configuring dedicated node pools Stay organized with collections  Save and categorize content based on your preferences. 

You are currently viewing version 1.7 of the Apigee hybrid documentation. **This version is end of life.** You should upgrade to a newer version. For more information, see [Supported versions](https://docs.cloud.google.com/apigee/docs/hybrid/supported-platforms#supported-versions).

Version 1.7 (unsupported)keyboard_arrow_down

Supported versions:

  * [ v1.17 (latest) ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.17/onfigure-dedicated-nodes.html)
  * [ v1.16 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/onfigure-dedicated-nodes.html)
  * [ v1.15 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.15/onfigure-dedicated-nodes.html)
  * [ v1.14 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.14/onfigure-dedicated-nodes.html)
  * [ List of supported versions ](https://docs.cloud.google.com/apigee/docs/hybrid/supported-platforms#supported-versions)

Unsupported versions:

  * [ v1.13 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.13/onfigure-dedicated-nodes.html)
  * [ v1.12 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.12/onfigure-dedicated-nodes.html)
  * [ v1.11 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.11/onfigure-dedicated-nodes.html)
  * [ v1.10 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.10/onfigure-dedicated-nodes.html)
  * [ v1.9 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.9/onfigure-dedicated-nodes.html)
  * [ v1.8 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.8/onfigure-dedicated-nodes.html)
  * [ v1.7 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.7/onfigure-dedicated-nodes.html)
  * [ v1.6 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.6/onfigure-dedicated-nodes.html)
  * [ v1.5 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.5/onfigure-dedicated-nodes.html)
  * [ v1.4 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.4/onfigure-dedicated-nodes.html)
  * [ v1.3 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.3/onfigure-dedicated-nodes.html)
  * [ v1.2 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.2/onfigure-dedicated-nodes.html)
  * [ v1.1 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.1/onfigure-dedicated-nodes.html)



##  About node pools 

A [node pool](https://cloud.google.com/kubernetes-engine/docs/concepts/node-pools) is a group of nodes within a cluster that all have the same configuration. Typically, you define separate node pools when you have pods with differing resource requirements. For example, the `apigee-cassandra` pods require persistent storage, while the other Apigee hybrid pods do not.

This topic discusses how to configure dedicated node pools for a hybrid installation. 

##  Using the default nodeSelectors 

The best practice is to set up two dedicated node pools: one for the Cassandra pods and one for all the other runtime pods. Using default [nodeSelector](https://kubernetes.io/docs/concepts/configuration/assign-pod-node/#nodeselector) configurations, the installer will assign the Cassandra pods to a _stateful_ node pool named `apigee-data` and all the other pods to a _stateless_ node pool named `apigee-runtime`. All you have to do is create node pools with these names, and Apigee hybrid handles the pod scheduling details for you: 

Default node pool name | Description  
---|---  
`apigee-data` | A stateful node pool.   
`apigee-runtime` | A stateless node pool.   
  
Following is the default `nodeSelector` configuration. The `apigeeData` property specifies a node pool for the Cassandra pods. The `apigeeRuntime` specifies the node pool for all the other pods. You can override these default settings in your overrides file, as explained later in this topic: 
    
    
    nodeSelector:
      requiredForScheduling: false
      apigeeRuntime:
        key: "cloud.google.com/gke-nodepool"
        value: "apigee-runtime"
      apigeeData:
        key: "cloud.google.com/gke-nodepool"
        value: "apigee-data"

Again, to ensure your pods are scheduled on the correct nodes, all you have to do is create two node pools with the names `apigee-data` and `apigee-runtime`. 

##  The requiredForScheduling property 

The `nodeSelector` config section has a property called `requiredForScheduling`:
    
    
    nodeSelector:
      **requiredForScheduling : false**
      apigeeRuntime:
        key: "cloud.google.com/gke-nodepool"
        value: "apigee-runtime"
      apigeeData:
        key: "cloud.google.com/gke-nodepool"
        value: "apigee-data"

If set to `false` (the default), underlying pods will be scheduled whether or not node pools are defined with the required names. This means that if you forget to create node pools or if you accidentally name a node pool other than `apigee-runtime` or `apigee-data`, the hybrid runtime installation will succeed. Kubernetes will decide where to run your pods. 

If you set `requiredForScheduling` to `true`, the installation will fail unless there are node pools that match the configured `nodeSelector` keys and values.

**Note:** The best practice is to set this value to `requiredForScheduling:true` for a production environment.

##  Using custom node pool names 

If you don't want to use node pools with the default names, you can create node pools with custom names and specify those names in the `nodeSelector` stanza. For example, the following configuration assigns the Cassandra pods to the pool named `my-cassandra-pool` and all other pods to the pool named `my-runtime-pool`: 
    
    
    nodeSelector:
      requiredForScheduling: false
      apigeeRuntime:
        key: "cloud.google.com/gke-nodepool"
        value: "**my-runtime-pool** "
      apigeeData:
        key: "cloud.google.com/gke-nodepool"
        value: "**my-cassandra-pool** "

##  Overriding the node pool for specific components on GKE 

You can also override node pool configurations at the individual component level. For example, the following configuration assigns the node pool with the value `apigee-custom` to the `runtime` component: 
    
    
    runtime:
      nodeSelector:
        key: cloud.google.com/gke-nodepool
        value: apigee-custom

You can specify a custom node pool on any of these components:

  * `istio`
  * `mart`
  * `synchronizer`
  * `runtime`
  * `cassandra`
  * `udca`
  * `logger`



## GKE node pool configuration

In GKE, node pools must have a unique name that you provide when you create the pools, and GKE automatically labels each node with the following:
    
    
    cloud.google.com/gke-nodepool=THE_NODE_POOL_NAME

As long as you create node pools named `apigee-data` and `apigee-runtime`, no further configuration is required. If you want to use custom node names, see Using custom node pool names. 

##  Anthos node pool configuration 

Apigee hybrid currently is only supported on Anthos 1.1.1. This version of Anthos does not support the node pool feature; therefore, you must manually label the worker nodes as explained below. Perform the following steps once your hybrid cluster is up and running: 

  1. Run the following command to get a list of the worker nodes in your cluster: 
         
         kubectl -n apigee get nodes

Example output: 
         
         NAME                   STATUS   ROLES    AGE     VERSION
         apigee-092d639a-4hqt   Ready    <none>   7d      v1.14.6-gke.2
         apigee-092d639a-ffd0   Ready    <none>   7d      v1.14.6-gke.2
         apigee-109b55fc-5tjf   Ready    <none>   7d      v1.14.6-gke.2
         apigee-c2a9203a-8h27   Ready    <none>   7d      v1.14.6-gke.2
         apigee-c70aedae-t366   Ready    <none>   7d      v1.14.6-gke.2
         apigee-d349e89b-hv2b   Ready    <none>   7d      v1.14.6-gke.2

  2. Label each node to differentiate between runtime nodes and data nodes. **Note:** Be sure to choose the nodes so that they are equally distributed among availability zones (AZs).

Use this command to label the nodes: 
         
         kubectl label node NODE_NAME KEY=VALUE

For example:
         
         $ kubectl label node apigee-092d639a-4hqt apigee.com/apigee-nodepool=apigee-runtime
         $ kubectl label node apigee-092d639a-ffd0 apigee.com/apigee-nodepool=apigee-runtime
         $ kubectl label node apigee-109b55fc-5tjf apigee.com/apigee-nodepool=apigee-runtime
         $ kubectl label node apigee-c2a9203a-8h27 apigee.com/apigee-nodepool=apigee-data
         $ kubectl label node apigee-c70aedae-t366 apigee.com/apigee-nodepool=apigee-data
         $ kubectl label node apigee-d349e89b-hv2b apigee.com/apigee-nodepool=apigee-data




##  Overriding the node pool for specific components on Anthos GKE 

You can also override node pool configurations at the individual component level for an Anthos GKE installation. For example, the following configuration assigns the node pool with the value `apigee-custom` to the `runtime` component: 
    
    
    runtime:
      nodeSelector:
        key: apigee.com/apigee-nodepool
        value: apigee-custom

You can specify a custom node pool on any of these components:

  * `istio`
  * `mart`
  * `synchronizer`
  * `runtime`
  * `cassandra`
  * `udca`
  * `logger`



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
