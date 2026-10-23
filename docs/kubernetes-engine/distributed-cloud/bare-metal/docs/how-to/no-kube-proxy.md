---
url: https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/how-to/no-kube-proxy/
title: Create a cluster without kube-proxy \u00a0|\u00a0 Google Distributed Cloud software only for bare metal \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:23:20.362312+00:00
---

# Create a cluster without kube-proxy  |  Google Distributed Cloud software only for bare metal  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/how-to/no-kube-proxy/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Distributed, hybrid, and multicloud ](https://docs.cloud.google.com/docs/dhm-cloud)
  * [ Google Distributed Cloud ](https://docs.cloud.google.com/distributed-cloud/docs)
  * [ GDC for bare metal ](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs)
  * [ Guides ](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/concepts/about-bare-metal)



Send feedback 

#  Create a cluster without kube-proxy Stay organized with collections  Save and categorize content based on your preferences. 

**Preview**

This feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

This document shows how to create a cluster that does not use `kube-proxy`.

`kube-proxy` is a controller that runs on each worker node in a cluster. It watches Kubernetes Service objects, and creates [iptables](https://help.ubuntu.com/community/IptablesHowTo?action=show&redirect=Iptables) rules to forward packets that are sent to Service addresses. An alternative to using `kube-proxy` and iptables for this purpose is to use Dataplane V2 in kube-proxy-replacement mode. This allows for the removal of `kube-proxy` from the cluster.

## Supported operating systems

To create a cluster that does not use `kube-proxy`, use one of the supported [Red Hat Enterprise Linux](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/installing/configure-os/rhel) operating systems or a supported [Ubuntu](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/installing/configure-os/ubuntu) operating system with kernel version 5.7.0 or later. If your cluster uses an Ubuntu operating system with kernel version earlier than 5.7.0, this feature is not supported.

## Advantages of removing `kube-proxy`

  * Avoid the resource consumption required for maintaining a large set of iptables rules.

  * Improve performance. Creating iptables rules is time consuming, especially for large clusters.




## Create a cluster without `kube-proxy`

**Warning:** If you create a cluster that has `kube-proxy` removed, you cannot reverse that decision. That is, you cannot add `kube-proxy` to the cluster at a later time.

Follow the instructions in one of the [cluster creation](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/installing/creating-clusters/create-clusters-overview) topics.

As you fill in your cluster configuration file, include the following annotation:
    
    
    preview.baremetal.cluster.gke.io/kube-proxy-free: "enable"
    

For example:
    
    
    apiVersion: baremetal.cluster.gke.io/v1
    kind: Cluster
    metadata:
      name: alice
      namespace: cluster-alice
      annotations:
        preview.baremetal.cluster.gke.io/kube-proxy-free: "enable"
    ...
    

## Verify that `kube-proxy` is not in your cluster

List the DaemonSets in the cluster:
    
    
    kubectl --kubeconfig CLUSTER_KUBECONFIG \
        get daemonsets --all-namespaces
    

Replace CLUSTER_KUBECONFIG with the path of the cluster kubeconfig file.

Verify that `kube-proxy` is not in the list. For example:
    
    
    kube-system   anetd
    kube-system   audit-proxy
    kube-system   etcd-defrag
    kube-system   gke-metrics-agent
    kube-system   kube-control-plane-metrics-proxy
    kube-system   localpv
    kube-system   metallb-speaker
    kube-system   node-exporter
    kube-system   stackdriver-log-forwarder
    

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
