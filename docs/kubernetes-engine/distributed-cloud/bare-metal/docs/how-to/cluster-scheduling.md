---
url: https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/how-to/cluster-scheduling/
title: Configure scheduling \u00a0|\u00a0 Google Distributed Cloud software only for bare metal \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T10:22:23.126402+00:00
---

# Configure scheduling  |  Google Distributed Cloud software only for bare metal  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/how-to/cluster-scheduling/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Distributed, hybrid, and multicloud ](https://docs.cloud.google.com/docs/dhm-cloud)
  * [ Google Distributed Cloud ](https://docs.cloud.google.com/distributed-cloud/docs)
  * [ GDC for bare metal ](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs)
  * [ Guides ](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/concepts/about-bare-metal)



Send feedback 

#  Configure scheduling Stay organized with collections  Save and categorize content based on your preferences. 

This page describes scheduler options and how to configure default pod scheduling constraints in your Google Distributed Cloud software-only for bare metal clusters.

Google Distributed Cloud provides a number of standard Kubernetes features that you can use to control scheduling pods, such as:

  * [`kube-scheduler`](https://kubernetes.io/docs/reference/command-line-tools-reference/kube-scheduler/)
  * [Topology spread constraints](https://kubernetes.io/docs/concepts/scheduling-eviction/topology-spread-constraints/)
  * Default custom scheduler



For information on pod topology spread constraints in Kubernetes, see [Kubernetes Scheduler](https://kubernetes.io/docs/concepts/scheduling-eviction/kube-scheduler/) in the Kubernetes documentation.

## Before you begin

Before configuring default pod spread, make sure each node in your cluster has the correct topology labels. You can use the `Nodepool.Spec.TaintsAndLabels` API to apply labels. Manually labeling nodes with `kubectl label` offers more flexibility, but requires manual labeling when you add a new node to the cluster.

## Configure default custom scheduler {#:config-default}

### Label nodes

  1. Add topology labels to your cluster and nodepool YAML files. The following example assumes two worker nodepools are in different racks, and control plane nodes are in `rack1`.
         
         apiVersion: baremetal.cluster.gke.io/v1
         kind: Cluster
         metadata:
           name: abm-cluster
           namespace: cluster-abm-cluster
         spec:
           controlPlane:
             nodePoolSpec:
               labels:
                 topology.k8s.io/rack: rack1
         ---
         apiVersion: baremetal.cluster.gke.io/v1
         kind: NodePool
         metadata:
           name: nodepool-rack1
           namespace: cluster-abm-cluster
         spec:
           labels:
             topology.k8s.io/rack: rack1
         ---
         apiVersion: baremetal.cluster.gke.io/v1
         kind: NodePool
         metadata:
           name: nodepool-rack2
           namespace: cluster-abm-cluster
         spec:
           labels:
             topology.k8s.io/rack: rack2
         

  2. Apply the updated cluster configuration.
         
         bmctl update cluster -c CLUSTER_NAME
         

Replace `CLUSTER_NAME` with the name of your cluster.

  3. Wait for the `topology.k8s.io/rack` label to propagate to all nodes in the cluster.




### Enable default pod spread constraints

  1. Add the `preview.baremetal.cluster.gke.io/custom-scheduler-configuration:enable` annotation to your cluster YAML file.

  2. Add the `schedulerConfiguration` section under `cluster.spec.controlPlane` in your cluster YAML file.
         
         apiVersion: baremetal.cluster.gke.io/v1
         kind: Cluster
         metadata:
           name: abm-cluster
           namespace: cluster-abm-cluster
           annotations:
             preview.baremetal.cluster.gke.io/custom-scheduler-configuration: enable
         spec:
           controlPlane:
             schedulerConfiguration:
               defaultTopologySpreadConstraint:
                 defaultConstraints:
                 - topologyKey: topology.k8s.io/rack
                   whenUnsatisfiable: DoNotSchedule
                   maxSkew: 1
                 defaultingType: List
         

  3. Apply the updated cluster configuration.
         
         bmctl update cluster -c CLUSTER_NAME
         

Replace `CLUSTER_NAME` with the name of your cluster.

  4. Wait for the cluster reconciliation to complete. Monitor `cluster.status.clusterState` until it shows `Running`. A `control-plane-update` job runs for each control plane node during this process.




### Verify pod spread configuration

  1. Create a test deployment with five replicas.

  2. Observe the pod distribution. The difference in the number of pods on `nodepool-rack1` and `nodepool-rack2` should be exactly one.

  3. Verify the `kube-scheduler-profile.config` file on each Control Plane node. The file, located at `/etc/kubernetes/kube-scheduler-profile.config`, must contain the topology spread configuration from `cluster.spec`.




## Troubleshoot

To diagnose and resolve issues with default pod spread, check the following:

  1. Review the `BareMetalMachine.Status.ControlPlaneComponents` for the feature's status.
  2. Examine logs from the `cluster-operator` and `cap-controller-manager` for relevant events.
  3. If `kube-scheduler` static pods crash, check that the scheduler configuration is correct in the cluster YAML file.



## What's next

  * Learn more about [pod topology spread constraints](https://kubernetes.io/docs/concepts/scheduling-eviction/topology-spread-constraints/) in the Kubernetes documentation.
  * See [Troubleshoot the Kubernetes scheduler](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/troubleshooting/kube-scheduler) if you run into issues.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-21 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-21 UTC."],[],[]] 
