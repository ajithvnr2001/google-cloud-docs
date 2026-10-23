---
url: https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/vm-runtime/numa/
title: Configure NUMA-aware VMs \u00a0|\u00a0 Google Distributed Cloud software only for bare metal \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:22:59.547889+00:00
---

# Configure NUMA-aware VMs  |  Google Distributed Cloud software only for bare metal  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/vm-runtime/numa/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Distributed, hybrid, and multicloud ](https://docs.cloud.google.com/docs/dhm-cloud)
  * [ Google Distributed Cloud ](https://docs.cloud.google.com/distributed-cloud/docs)
  * [ GDC for bare metal ](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs)
  * [ Guides ](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/concepts/about-bare-metal)



Send feedback 

#  Configure NUMA-aware VMs Stay organized with collections  Save and categorize content based on your preferences. 

**Preview**

This product or feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA products and features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

This document describes how to configure clusters and VMs to support high performance and low latency workloads with the computing efficiencies of non-uniform memory access (NUMA). There are instructions for tuning Kubernetes settings for cluster nodes. This document also includes instructions for configuring Virtual Machines (VMs) with NUMA affinity so that they get scheduled on and take advantage of the _NUMA nodes_.

With a NUMA-aware VM, all the communication within the VM is local to the NUMA node. The NUMA-aware VM avoids data transactions to and from remote resources that can degrade VM performance.

## Configure nodes to use NUMA

The following sections describe how to configure the critical Kubernetes components to tune the node and make sure it can schedule NUMA-aware containers. These NUMA nodes are tuned to optimize CPU and memory performance. Follow the instructions for each node that you want to run NUMA-aware VMs.

### Update the kubelet configuration

As part of the node configuration to support NUMA node affinity, you need to make the following changes in the kubelet configuration:

  * Enable the CPU Manager with a `static` policy
  * Enable the Memory Manager with a `Static` policy
  * Enable the Topology manager with `restricted` topology



To configure kubelet on your worker node:

**Note:** You may need to use `sudo` to run some of the following commands. 

  1. Locate the `kubelet` file on your worker node and open it for editing:
         
         edit /etc/default/kubelet
         

If you don't see the `kubelet` file, create it with the following command:
         
         echo "KUBELET_EXTRA_ARGS=\"\"" >> /etc/default/kubelet
         

This command creates the `kubelet` file with an empty `KUBELET_EXTRA_ARGS=""` section.

  2. To enable the CPU Manager with a `static` policy, add the `--cpu-manager-policy=static` flag to the `KUBELET_EXTRA_ARGS=""` section of the file:
         
         KUBELET_EXTRA_ARGS="**--cpu-manager-policy=static** "
         

  3. To enable the Memory Manager with a `Static` policy, add the `--memory-manager-policy=Static` flag to the `KUBELET_EXTRA_ARGS=""` section of the file:
         
         KUBELET_EXTRA_ARGS="--cpu-manager-policy=static **--memory-manager-policy=Static** "
         

  4. To enable the Topology Manager with a `restricted` policy, add the `--topology-manager-policy=restricted` flag to the `KUBELET_EXTRA_ARGS=""` section of the file:
         
         KUBELET_EXTRA_ARGS="--cpu-manager-policy=static --memory-manager-policy=Static **--topology-manager-policy=restricted** "
         

  5. Check the current amount of memory reserved by Google Distributed Cloud:
         
         cat /var/lib/kubelet/kubeadm-flags.env
         

The output should look like the following:
         
         KUBELET_KUBEADM_ARGS="--anonymous-auth=false --authentication-token-webhook=true --authorization-mode=Webhook --container-runtime=remote --container-runtime-endpoint=unix:///run/containerd/containerd.sock --feature-gates=SeccompDefault=true **--kube-reserved=cpu=100m,memory=3470Mi** --max-pods=110 --node-ip=192.168.1.190 --node-labels=baremetal.cluster.gke.io/k8s-ip=192.168.1.190,baremetal.cluster.gke.io/namespace=cluster-user001,baremetal.cluster.gke.io/node-pool=node-pool-1,cloud.google.com/gke-nodepool=node-pool-1 --pod-infra-container-image=gcr.io/anthos-baremetal-release/pause-amd64:3.1-gke.5 --provider-id=baremetal://192.168.1.190 --read-only-port=10255 --rotate-server-certificates=true --seccomp-default=true"

The `--kube-reserved=cpu=100m,memory=3470Mi` setting indicates that Google Distributed Cloud has reserved 3,470 mebibytes of memory on the node.

  6. Set the `--reserved-memory` flag in the `KUBELET_EXTRA_ARGS` section of the `kubelet` file to 100 mebibytes more than the current reserved memory to account for the eviction threshold. If there is no reserved memory, you can skip this step.

For example, with the reserved memory of `3470Mi` from the example in the preceding step, you reserve `3570Mi` of memory in the `kubelet` file:
         
         KUBELET_EXTRA_ARGS="--cpu-manager-policy=static --memory-manager-policy=Static --topology-manager-policy=restricted **--reserved-memory=0:memory=3570Mi** "
         

  7. Remove CPU and memory state files from the `/var/lib` directory:
         
         rm /var/lib/cpu_manager_state
         rm /var/lib/memory_manager_state
         

  8. Restart kubelet:
         
         systemctl start kubelet
         




For more information about these policy settings, see the following Kubernetes documentation:

  * [CPU Management Policies](https://kubernetes.io/docs/tasks/administer-cluster/cpu-management-policies/#cpu-management-policies)
  * [Memory Manager configuration](https://kubernetes.io/docs/tasks/administer-cluster/memory-manager/#memory-manager-configuration)
  * [Topology Manager restricted policy](https://kubernetes.io/docs/tasks/administer-cluster/topology-manager/#policy-restricted)



### Configure the node to use hugepages

Once you have enabled Memory Manager with the `Static` policy, you can add hugepages to further improve container workload performance on your NUMA nodes. Hugepages, as the name suggests, let you specify memory pages that are larger than the standard 4 kibibyte (KiB). VM Runtime on GDC supports 2 mebibyte (MiB) and 1 gibibyte (GiB) hugepages. You can set hugepages for a node at runtime, or for when the node machine boots. We recommend that you configure hugepages on each node that you want to run NUMA-aware VMs.

  1. To configure the number of hugepages of a specific size on your NUMA node at runtime, use the following command:
         
         echo HUGEPAGE_QTY > \
             /sys/devices/system/node/NUMA_NODE/hugepages/hugepages-HUGEPAGE_SIZEkB/nr_hugepages
         

Replace the following:

     * `HUGEPAGE_QTY`: the number of hugepages to allocate of the specified size.

     * `NUMA_NODE`: the NUMA node, such as `node0`, to which you're allocating hugepages.

     * `HUGEPAGE_SIZE`: the size of the hugepages in kibibytes, `2048` (2 MiB) or`1048576` (1 GiB).




## Configure a VM to use the NUMA node

Once your cluster nodes are tuned for NUMA, you can create NUMA-aware VMs. NUMA-aware VMs are scheduled on NUMA nodes.

To create a NUMA-aware VM:

  1. Follow the instructions to [create a VM from a manifest](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/vm-runtime/tutorial-create-vm#create_a_vm).

Use the following `compute` settings to configure your VM to be NUMA-aware:

     * `spec.compute.guaranteed`: Set `guaranteed` to `true`. With this setting, the `virt-launcher` Pod is configured to be placed in the Kubernetes Guaranteed [Quality of Service (QoS) class](https://kubernetes.io/docs/tasks/configure-pod-container/quality-service-pod/#create-a-pod-that-gets-assigned-a-qos-class-of-guaranteed).

     * `spec.compute.advancedCompute`:

       * `dedicatedCPUPlacement`: Set `dedicatedCPUPlacement` to `true`. This setting pins virtual CPUs to the physical CPUs of the node.
       * `hugePageSize`: Set `hugePageSize` to either `2Mi` or `1Gi` to specify the hugepages size for your VM to use, 2 mebibyte or 1 gibibyte.
       * `numaGuestMappingPassthrough`: Include an empty structure (`{}`) for this setting. This setting establishes NUMA affinity so that your VM is scheduled on NUMA nodes only.

The following example VirtualMachine manifest shows how a NUMA-aware VM configuration might look:
    
    apiVersion: vm.cluster.gke.io/v1
    kind: VirtualMachine
    metadata:
      name: vm1
    spec:
      compute:
        cpu:
          vcpus: 2**    guaranteed: true
        advancedCompute:
          dedicatedCPUPlacement: true
          hugePageSize: 2Mi
          numaGuestMappingPassthrough: {}**
        memory:
          capacity: 256Mi
      interfaces:
      - name: eth0
        networkName: pod-network
        default: true
      disks:
      - virtualMachineDiskName: disk-from-gcs
        boot: true
        readOnly: true
    




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
