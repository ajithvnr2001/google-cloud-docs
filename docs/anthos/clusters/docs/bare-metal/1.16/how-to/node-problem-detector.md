---
url: https://docs.cloud.google.com/anthos/clusters/docs/bare-metal/1.16/how-to/node-problem-detector/
title: Node Problem Detector \u00a0|\u00a0 Google Distributed Cloud Virtual for Bare Metal \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-15T20:46:53.538273+00:00
---

# Node Problem Detector  |  Google Distributed Cloud Virtual for Bare Metal  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/anthos/clusters/docs/bare-metal/1.16/how-to/node-problem-detector/

**Version 1.16**. This version is no longer supported. For information about how to upgrade to version 1.28, see [ Upgrade clusters](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/how-to/upgrade) in the latest documentation. For more information about supported and unsupported versions, see the [Versioning](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/version-history) page in the latest documentation.

  * [ Home ](https://docs.cloud.google.com/)
  * [ Google Distributed Cloud ](https://docs.cloud.google.com/distributed-cloud)
  * [ Documentation ](https://docs.cloud.google.com/kubernetes-engine/enterprise/clusters/docs)
  * [ GDCV for Bare Metal 1.16 ](https://docs.cloud.google.com/anthos/clusters/docs/bare-metal/1.16)
  * [ Guides ](https://docs.cloud.google.com/anthos/clusters/docs/bare-metal/1.16/concepts/about-bare-metal)



Send feedback 

#  Node Problem Detector Stay organized with collections  Save and categorize content based on your preferences. 

Version 1.16 keyboard_arrow_down

  * [ Latest ](https://docs.cloud.google.com/anthos/clusters/docs/bare-metal/latest/how-to/node-problem-detector)
  * [ Version 1.16 ](https://docs.cloud.google.com/anthos/clusters/docs/bare-metal/1.16/how-to/node-problem-detector)
  * [ Earlier versions (unsupported) ](https://docs.cloud.google.com/anthos/clusters/docs/bare-metal/1.16/getting-support#version-support)



[Node Problem Detector](https://github.com/kubernetes/node-problem-detector) is an open source library that monitors the health of nodes and detects common node problems, such as hardware, kernel or container runtime issues. In Distributed Cloud, it runs as a [systemd](https://www.freedesktop.org/wiki/Software/systemd/) service on each node.

Starting with Distributed Cloud release 1.10.0, Node Problem Detector is enabled by default.

## What problems does it detect?

Node problem detector can detect the following kinds of issues:

  * Container runtime problems, such as unresponsive runtime daemons
  * Hardware problems, such as CPU, memory, or disk failures
  * Kernel problems, such as kernel deadlock conditions or corrupted file systems



It runs on a node and reports problems to the Kubernetes API server as either a [`NodeCondition`](https://kubernetes.io/docs/concepts/architecture/nodes/#condition) or as an [`Event`](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.23/#event-v1-core). (A `NodeCondition` is a problem that makes a node unable to run pods whereas an `Event` is a temporary problem that has a limited effect on pods, but is nonetheless considered important enough to report).

Some of the `NodeConditions` discovered by Node Problem Detector are:

  * `KernelDeadlock`
  * `ReadonlyFilesystem`
  * `FrequentKubeletRestart`
  * `FrequentDockerRestart`
  * `FrequentContainerdRestart`
  * `FrequentUnregisterNetDevice`
  * `KubeletUnhealthy`
  * `ContainerRuntimeUnhealthy`
  * `CorruptDockerOverlay2`



Some examples of the kinds of `Events` reported by Node Problem Detector are:

  * `Warning TaskHung node/vm-worker-1-user-a12fabb4a99cb92-ddfce8832fd90f6f.lab.anthos kernel: task docker:7 blocked for more than 300 seconds.`
  * `Warning KernelOops node/vm-worker-1-user-a12fabb4a99cb92-ddfce8832fd90f6f.lab.anthos kernel: BUG: unable to handle kernel NULL pointer dereference at 00x0.`



## How to view detected problems

Run the following `kubectl describe` command on a node to look for `NodeConditions` and `Events`:
    
    
    kubectl --kubeconfig=KUBECONFIG_PATH describe node NODE_NAME

In the command, replace the following entries with information specific to your environment:

  * `KUBECONFIG_PATH`: the path to the target cluster kubeconfig file. (The path to the kubeconfig file is usually `bmctl-workspace/CLUSTER_NAME/CLUSTER_NAME-kubeconfig`. However, if you specified your workspace with the WORKSPACE_DIR flag, the path is `WORKSPACE_DIR/CLUSTER_NAME/CLUSTER_NAME-kubeconfig`).

  * `NODE_NAME`: the name of the node about which you want health information.




## How to enable/disable Node Problem Detector

Here are the steps to take to enable Node Problem Detector on a given cluster:

  1. Edit the cluster's `ConfigMap` file which is called `node-problem-detector-config`
         
         kubectl --kubeconfig=KUBECONFIG_PATH edit configmap \
                node-problem-detector-config --namespace=CLUSTER_NAMESPACE

This command automatically starts up a text editor (such as vim or nano) in which you can edit the `node-problem-detector-config` file. In the command, replace the following entries with information specific to your cluster environment:

     * KUBECONFIG_PATH: the path to the admin cluster kubeconfig file. (The path to the kubeconfig file is usually `bmctl-workspace/CLUSTER_NAME/CLUSTER_NAME-kubeconfig`. However, if you specified your workspace with the WORKSPACE_DIR flag, the path is `WORKSPACE_DIR/CLUSTER_NAME/CLUSTER_NAME-kubeconfig`).
     * CLUSTER_NAMESPACE: the namespace of the cluster in which you want to enable Node Problem Detector.
  2. Initially, the `node-problem-detector-config` `ConfigMap` doesn't have a `data` field. Add the `data` field to the configuration map with the following key-value pair:
         
         data:
           enabled: "true"
         




To disable Node Problem Detector in a cluster namespace, perform the preceding steps 1 and 2, but in step 2, change the value of the `enabled` key to 'false'.

## How to stop/start Node Problem Detector

Node Problem Detector runs as a `systemd` service on each node. To manage Node Problem Detector for a given node, use SSH to access the node, and run the following `systemctl` commands.

To disable Node Problem Detector, run the following command:
    
    
    systemctl stop node-problem-detector
    

To restart Node Problem Detector, run the following command:
    
    
    systemctl restart node-problem-detector
    

To check if Node Problem Detector is running on a particular node, run the following command:
    
    
    systemctl is-active node-problem-detector
    

## Unsupported features

Distributed Cloud doesn't support the following customizations of Node Problem Detector:

  * Exporting Node Problem Detector reports to other monitoring systems, such as Stackdriver or Prometheus.
  * Customizing which `NodeConditions` or `Events` to look for.
  * Running user-defined monitoring scripts.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
