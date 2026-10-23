---
url: https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/vm-runtime/high-availability-policy-vms/
title: Configure a high availability policy for VMs \u00a0|\u00a0 Google Distributed Cloud software only for bare metal \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:23:40.678864+00:00
---

# Configure a high availability policy for VMs  |  Google Distributed Cloud software only for bare metal  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/vm-runtime/high-availability-policy-vms/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Distributed, hybrid, and multicloud ](https://docs.cloud.google.com/docs/dhm-cloud)
  * [ Google Distributed Cloud ](https://docs.cloud.google.com/distributed-cloud/docs)
  * [ GDC for bare metal ](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs)
  * [ Guides ](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/concepts/about-bare-metal)



Send feedback 

#  Configure a high availability policy for VMs Stay organized with collections  Save and categorize content based on your preferences. 

This document shows you how to configure the high-availability policy for virtual machines (VMs) that run using VM Runtime on GDC.

When you [enable VM Runtime on GDC](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/vm-runtime/enable-disable), the cluster creates a VMHighAvailabilityPolicy object named `default`. This object specifies the default recovery strategy in case a cluster node that is running a VM fails. Possible default recovery strategies are:

  * **Reschedule** : Reschedule the VM on another cluster node.
  * **Ignore** : Do nothing.



Initially, the default recovery strategy is set to `Reschedule`.

A default recovery strategy of `Reschedule` is appropriate in the following situation:

  * Your cluster has at least two worker nodes.

  * Your VM disks are provisioned using a network-file-based storage class. That is, the storage class is based on a network file system that coordinates POSIX file locks across different clients. [Network File System (NFS)](https://kubernetes.io/docs/concepts/storage/storage-classes/#nfs) is an example of a network-file-based storage class.




If your VMs are using local storage or a block-based storage system, we recommend that you set the default recovery strategy to `Ignore`. We make this recommendation for the following reasons:

  * If your VMs use local storage, and a node fails, there is no way to recover the stored data and move it to a new node.

  * If your VMs use a block-based storage system, the storage might not have sufficient detachment guarantees. That could lead to concurrent disk access and data corruption during VM scheduling.




## Inspect the VMHighAvailabilityPolicy object

Verify that there is a VMHighAvailabilityPolicy object:
    
    
    kubectl --kubeconfig USER_CLUSTER_KUBECONFIG get VMHighAvailabilityPolicy --namespace vm-system
    

Replace USER_CLUSTER_KUBECONFIG with the path of your user cluster kubeconfig file.

The output shows that there is a VMHighAvailabilityPolicy object named `default`. In the output, you can also see the current value of `defaultRecoveryStrategy`. For example, the following output shows that the current value of `defaultRecoveryStrategy` is `Reschedule`:
    
    
    vm-system   default   5m55s   Reschedule   15s   1m30s
    

Get a detailed view of the VMHighAvailabilityPolicy object:
    
    
    kubectl --kubeconfig USER_CLUSTER_KUBECONFIG get VMHighAvailabilityPolicy \
        --namespace vm-system --output yaml
    

Example output:
    
    
    apiVersion: vm.cluster.gke.io/v1alpha1
    kind: VMHighAvailabilityPolicy
    metadata:
      ...
      labels:
        app.kubernetes.io/component: kubevirt
        app.kubernetes.io/managed-by: virt-operator
        kubevirt.io: virt-api
      name: default
      namespace: vm-system
      ..
    spec:
      defaultRecoveryStrategy: Reschedule
      nodeHeartbeatInterval: 15s
      nodeMonitorGracePeriod: 1m30s
    

## Change the default recovery strategy

In certain situations, we recommend that you change the default recovery strategy. For example if your VMs are using local storage or a file system that is not network-file-based, then we recommend that you change the value of `defaultRecoveryStrategy` to `Ignore`.

To change the value of `defaultRecoveryStrategy`, open the VMHighAvailabilityPolicy object for editing:
    
    
    kubectl --kubeconfig USER_CLUSTER_KUBECONFIG edit VMHighAvailabilityPolicy \
        default --namespace vm-system
    

In your text editor, change the value of `defaultRecoveryStrategy` to a value of your choice: `Reschedule` or `Ignore`. Close the text editor.

## Override the default recovery strategy for a VM

The default recovery strategy applies to all VMs running in the cluster. However, you might need to override the default recovery strategy for individual VMs.

For example, suppose that most of your VMs are provisioned with a network-file-based storage class, but a few VMs are provisioned with a block-based storage class. For each VM that uses block-based storage, we recommend that you override the default recovery strategy by setting the recovery strategy for the individual VM to `Ignore`.

To override the default recovery strategy for a VM, add a `vm.cluster.gke.io/vm-ha-recovery-strategy` annotation to both the VirtualMachineInstance (VMI) object and the GVM object.

For example, these commands set the recovery strategy to `Ignore` for a VM named `my-vm`:
    
    
    kubectl --kubeconfig USER_CLUSTER_KUBECONFIG \
      annotate vmi my-vm \
      vm.cluster.gke.io/vm-ha-recovery-strategy=Ignore --overwrite
    
    kubectl --kubeconfig USER_CLUSTER_KUBECONFIG \
      annotate gvm my-vm \
      vm.cluster.gke.io/vm-ha-recovery-strategy=Ignore --overwrite
    

If you want to remove the annotations later, use a hyphen at the end of the annotation name. For example:
    
    
    kubectl --kubeconfig USER_CLUSTER_KUBECONFIG \
      annotate vmi my-vm \
      vm.cluster.gke.io/vm-ha-recovery-strategy-
    
    kubectl --kubeconfig USER_CLUSTER_KUBECONFIG \
      annotate gvm my-vm \
      vm.cluster.gke.io/vm-ha-recovery-strategy-
    

## Advanced configuration

In addition to configuring the default recovery strategy, you can configure the following:

  * **Node heartbeat interval** : The time between heartbeats sent by each cluster node

  * **Node monitor grace period** : The maximum amount of time a node can fail to send a heartbeat before it is considered unhealthy




In most cases, the default values for heartbeat interval and grace period are appropriate. However, you might choose to adjust these values if you want to fine tune the tradeoff between speed of recovery and overhead. A shorter heartbeat interval will shorten recovery time, but will also increase overhead. In a large cluster, you might choose to lengthen the heartbeat interval, because frequent heartbeats from many nodes could create an unacceptable load on the Kubernetes API server.

Keep the heartbeat interval lower than the grace period to avoid cases where a single missed heartbeat results in a node being deemed unhealthy.

Run `kubectl edit` to open the VMHighAvailabilityPolicy object for editing. Set `nodeHeartbeatInterval` and `nodeMonitorGracePeriod` to values of your choice.
    
    
    spec:
      defaultRecoveryStrategy: Reschedule
      nodeHeartbeatInterval: 15s
      nodeMonitorGracePeriod: 1m30s
    

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
