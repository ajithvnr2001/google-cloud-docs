---
url: https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/how-to/node-problem-detector/
title: Node Problem Detector \u00a0|\u00a0 Google Distributed Cloud software only for bare metal \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T09:12:03.899668+00:00
---

# Node Problem Detector  |  Google Distributed Cloud software only for bare metal  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/how-to/node-problem-detector/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Distributed, hybrid, and multicloud ](https://docs.cloud.google.com/docs/dhm-cloud)
  * [ Google Distributed Cloud ](https://docs.cloud.google.com/distributed-cloud/docs)
  * [ GDC for bare metal ](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs)
  * [ Guides ](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/concepts/about-bare-metal)



Send feedback 

#  Node Problem Detector Stay organized with collections  Save and categorize content based on your preferences. 

[Node Problem Detector](https://github.com/kubernetes/node-problem-detector) is an open source library that monitors the health of nodes and detects common node problems, such as hardware, kernel, or container runtime issues. In Google Distributed Cloud, it runs as a [systemd](https://www.freedesktop.org/wiki/Software/systemd/) service on each node.

Starting with Google Distributed Cloud release 1.10.0, Node Problem Detector is enabled by default.

If you need additional assistance, reach out to [Cloud Customer Care](https://cloud.google.com/support-hub). You can also see [Getting support](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/getting-support) for more information about support resources, including the following: 

  * [Requirements](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/getting-support#intro-support) for opening a support case.
  * [Tools](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/getting-support#support-tools) to help you troubleshoot, such as your environment configuration, logs, and metrics.
  * Supported [components](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/getting-support#what-we-support).



## What problems does it detect?

Node Problem Detector can detect the following kinds of issues:

  * Container runtime problems, such as unresponsive runtime daemons
  * Hardware problems, such as CPU, memory, or disk failures
  * Kernel problems, such as kernel deadlock conditions or corrupted file systems



It runs on a node and reports problems to the Kubernetes API server as either a [`NodeCondition`](https://kubernetes.io/docs/concepts/architecture/nodes/#condition) or as an [`Event`](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.23/#event-v1-core). A `NodeCondition` is a problem that makes a node unable to run pods whereas an `Event` is a temporary problem that has a limited effect on pods, but is nonetheless considered important enough to report.

The following table describes the `NodeConditions` discovered by Node Problem Detector and whether or not they can be repaired automatically:

Condition | Reason | Auto repair supported1  
---|---|---  
`KernelDeadlock` | Kernel processes are stuck waiting for other kernel processes to release required resources. | No  
`ReadonlyFilesystem` | The cluster is unable to write to the file system due to a problem, such as the disk being full. | No  
`FrequentKubeletRestart` | The kubelet is restarting frequently, which prevents the node from running pods effectively. | No  
`FrequentDockerRestart` | The Docker daemon has restarted more than 5 times in 20 minutes. | No  
`FrequentContainerdRestart` | The container runtime has restarted more than 5 times in 20 minutes. | No  
`FrequentUnregisterNetDevice` | The node is experiencing frequent unregistration of network devices. | No  
`CorruptDockerOverlay2` | There are file system issues or inconsistencies within the Docker overlay2 storage driver directory. | No  
`OrphanContainers`2 | A pod specific to a container has been deleted, but the corresponding container still exists in the node. | No  
`ContainerRuntimeUnhealthy` | The container runtime isn't functioning correctly, preventing pods from running or scheduling on the node. | Yes  
`FailedCgroupRemoval`2 | Some cgroups are in a frozen state. | Yes  
`KubeletUnhealthy` | The node isn't functioning properly or isn't responding to the control plane. | Yes  
  
1 For versions 1.32 and higher, the ability to automatically repair detected problems is supported for select conditions.

2 Supported for versions 1.32 and higher.

Some examples of the kinds of `Events` reported by Node Problem Detector are:

  * `Warning TaskHung node/vm-worker-1-user-a12fabb4a99cb92-ddfce8832fd90f6f.lab.anthos kernel: task docker:7 blocked for more than 300 seconds.`
  * `Warning KernelOops node/vm-worker-1-user-a12fabb4a99cb92-ddfce8832fd90f6f.lab.anthos kernel: BUG: unable to handle kernel NULL pointer dereference at 00x0.`



## What problems does it repair?

Starting in version 1.32, when Node Problem Detector discovers select `NodeConditions`, it can automatically repair the corresponding problem on the node. The following `NodeConditions` support automatic repair:

  * `ContainerRuntimeUnhealthy`
  * `FailedCgroupRemoval`
  * `KubeletUnhealthy`



## How to view detected problems

Run the following `kubectl describe` command to look for `NodeConditions` and `Events`:
    
    
    kubectl describe node NODE_NAME \
        --kubeconfig=KUBECONFIG
    

Replace the following:

  * `NODE_NAME`: the name of the node you're checking.

  * `KUBECONFIG`: the path of the cluster kubeconfig file.




## How to enable and disable Node Problem Detector

By default, Node Problem Detector is enabled, but it can be disabled in the `node-problem-detector-config` ConfigMap resource. Unless you explicitly disable it, Node Problem Detector continuously monitors nodes for specific conditions that indicate problems for the node.

To disable Node Problem Detector on a given cluster, use the following steps:

  1. Edit the `node-problem-detector-config` ConfigMap resource:
         
         kubectl edit configmap node-problem-detector-config \
             --kubeconfig=KUBECONFIG \
             --namespace=CLUSTER_NAMESPACE
         

Replace the following:

     * `KUBECONFIG`: the path of the cluster kubeconfig file.

     * `CLUSTER_NAMESPACE`: the namespace of the cluster in which you want to enable Node Problem Detector.

This command automatically starts up a text editor in which you can edit the `node-problem-detector-config` resource.

  2. Set `data.enabled` to `false` in the `node-problem-detector-config` resource definition.
         
         apiVersion: v1
         kind: ConfigMap
         metadata:
           creationTimestamp: "2025-04-19T21:36:44Z"
           name: node-problem-detector-config
         ...** data:
           enabled: "false"**
         

Initially, the `node-problem-detector-config` ConfigMap doesn't have a `data` field, so you may need to add it.

  3. To update the resource, save your changes and close the editor.




To re-enable Node Problem Detector, perform the preceding steps, but set `data.enabled` to `true` in the `node-problem-detector-config` resource definition.

## How to enable and disable automatic repair

Starting in version 1.32, Node Problem Detector checks for specific `NodeConditions` and automatically repairs the corresponding problem on the node. By default, automatic repair is enabled for supported `NodeConditions`, but it can be disabled in the `node-problem-detector-config` ConfigMap resource.

To disable the automatic repair behavior on a given cluster, use the following steps:

  1. Edit the `node-problem-detector-config` ConfigMap resource:
         
         kubectl edit configmap node-problem-detector-config \
             --kubeconfig=KUBECONFIG \
             --namespace=CLUSTER_NAMESPACE
         

Replace the following:

     * `KUBECONFIG`: the path of the cluster kubeconfig file.

     * `CLUSTER_NAMESPACE`: the namespace of the cluster in which you want to enable Node Problem Detector.

This command automatically starts up a text editor in which you can edit the `node-problem-detector-config` resource.

  2. Set `data.check-only` to `true` in the `node-problem-detector-config` resource definition.
         
         apiVersion: v1
         kind: ConfigMap
         metadata:
           creationTimestamp: "2025-04-19T21:36:44Z"
           name: node-problem-detector-config
         ...
         data:
           enabled: "true"**  check-only: "true"**
         

Initially, the `node-problem-detector-config` ConfigMap doesn't have a `data` field, so you may need to add it. Setting `check-only` to `"true"` disables automatic repair for all supported conditions.

  3. To update the resource, save your changes and close the editor.




To re-enable automatic repair for all `NodeConditions` that support it, set `data.check-only` to `"false"` in the `node-problem-detector-config` ConfigMap.

## How to stop and restart Node Problem Detector

Node Problem Detector runs as a `systemd` service on each node. To manage Node Problem Detector for a given node, use SSH to access the node, and run the following `systemctl` commands.

  * To disable Node Problem Detector, run the following command:
        
        systemctl stop node-problem-detector
        

  * To restart Node Problem Detector, run the following command:
        
        systemctl restart node-problem-detector
        

  * To check if Node Problem Detector is running on a particular node, run the following command:
        
        systemctl is-active node-problem-detector
        




## Unsupported features

Google Distributed Cloud doesn't support the following customizations of Node Problem Detector:

  * Exporting Node Problem Detector reports to other monitoring systems, such as Cloud Monitoring or Prometheus.
  * Customizing which `NodeConditions` or `Events` to look for.
  * Running user-defined monitoring scripts.



## What's next

If you need additional assistance, reach out to [Cloud Customer Care](https://cloud.google.com/support-hub). You can also see [Getting support](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/getting-support) for more information about support resources, including the following: 

  * [Requirements](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/getting-support#intro-support) for opening a support case.
  * [Tools](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/getting-support#support-tools) to help you troubleshoot, such as your environment configuration, logs, and metrics.
  * Supported [components](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/getting-support#what-we-support).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
