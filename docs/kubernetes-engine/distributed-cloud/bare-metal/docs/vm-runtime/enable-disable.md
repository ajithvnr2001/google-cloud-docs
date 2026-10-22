---
url: https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/vm-runtime/enable-disable/
title: Enable or disable VM Runtime on GDC \u00a0|\u00a0 Google Distributed Cloud software only for bare metal \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T10:14:56.030447+00:00
---

# Enable or disable VM Runtime on GDC  |  Google Distributed Cloud software only for bare metal  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/vm-runtime/enable-disable/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Distributed, hybrid, and multicloud ](https://docs.cloud.google.com/docs/dhm-cloud)
  * [ Google Distributed Cloud ](https://docs.cloud.google.com/distributed-cloud/docs)
  * [ GDC for bare metal ](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs)
  * [ Guides ](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/concepts/about-bare-metal)



Send feedback 

#  Enable or disable VM Runtime on GDC Stay organized with collections  Save and categorize content based on your preferences. 

This document shows you how to enable or disable VM Runtime on Google Distributed Cloud by either updating the `VMRuntime` custom resource or running `bmctl` commands.

## Before you begin

To enable or disable VM Runtime on GDC, you need access to the following resources and tools:

  * Access to Google Distributed Cloud version 1.12.0 (`anthosBareMetalVersion: 1.12.0`) or higher cluster. You can use any cluster type capable of running workloads. If needed, [try Google Distributed Cloud on Compute Engine](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/try/gce-vms) or see the [cluster creation overview](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/installing/creating-clusters/create-clusters-overview).
  * The `bmctl` command-line tool. For more information, see [Download and install the `bmctl` tool](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/vm-runtime/quickstart#installing-bmctl).



## Enable VM Runtime on GDC

VM Runtime on GDC is automatically installed in Google Distributed Cloud version 1.10 or higher, but is disabled by default. Before you can run VM resources in your Google Distributed Cloud, you must enable the VM Runtime on GDC.

###  bmctl 

  * To enable the runtime, use the `bmctl` tool:
        
        bmctl enable vmruntime --kubeconfig KUBECONFIG_PATH
        

Provide the path to the kubeconfig file for your cluster. Google Distributed Cloud generates the kubeconfig file on the admin workstation when you create a cluster. By default, the path is `bmctl-workspace/CLUSTER_NAME/CLUSTER_NAME-kubeconfig`.

If VM Runtime on GDC is already enabled, the command returns an error.




Additional settings, such as for emulation or image format, can be configured by editing the `VMRuntime` custom resource.

###  Custom resource 

To enable the runtime, update the `VMRuntime` custom resource. This custom resource is installed by default.

  1. Edit the `VMRuntime` custom resource:
         
         kubectl edit vmruntime
         

  2. Set `enabled:true` in the spec:
         
         apiVersion: vm.cluster.gke.io/v1
         kind: VMRuntime
         metadata:
           name: vmruntime
         spec:
           enabled: true
           # useEmulation defaults to "false" if not set.
           useEmulation: true
           # vmImageFormat defaults to "qcow2" if not set.
           vmImageFormat: qcow2
         

In the preceding `spec` section, the following values can be set:

     * `enabled`: set to true to enable VM Runtime on GDC
     * `useEmulation`: If your node doesn't support hardware virtualization, or you aren't sure, set the value to true. If available, hardware virtualization provides better performance than software emulation. The `useEmulation` field defaults to `false`, if it isn't specified.
     * `vmImageFormat`: Supports two disk image format values: `raw` and `qcow2`. If you don't set `vmImageFormat`, the VM Runtime on GDC uses the `raw` disk image format to create VMs. The `raw` format may provide improved performance over `qcow2`, a copy on write format, but may use more disk. For more information about the image formats for your VM, see [Disk image file formats](https://www.qemu.org/docs/master/system/images.html#disk-image-file-formats) in the QEMU documentation.
  3. Save the custom resource in your editor.

  4. Verify that the `VMRuntime` custom resource is enabled:
         
         kubectl describe vmruntime vmruntime
         

The details of the `VMRuntime` custom resource include a `Status` section. VM Runtime on GDC is enabled and working when `VMRuntime.Status.Ready` shows as `true`.




## Disable VM Runtime on GDC

When you no longer need to use VM Runtime on GDC, you can disable this feature.

###  bmctl 

  * To disable the runtime, use the `bmctl` tool:
        
        bmctl disable vmruntime --kubeconfig KUBECONFIG_PATH \
          --force=true
        

Provide the path to the kubeconfig file for your cluster and values for the following configuration options:

    * `--force`: Set to `true` to confirm you want to delete existing VM resources. The default value is `false`.



###  Custom resource 

To disable the runtime, update the `VMRuntime` custom resource:

  1. Edit the `VMRuntime` custom resource:
         
         kubectl edit vmruntime
         

  2. Set `enabled:false` in the spec:
         
         apiVersion: vm.cluster.gke.io/v1`
         kind: VMRuntime
         metadata:
           name: vmruntime
         spec:
           enabled: false
           useEmulation: true
           vmImageFormat: qcow2
         

  3. Save the updated custom resource specification in your editor.

  4. To verify that the `VMRuntime` custom resource is disabled, view the pods that run in the `vm-system` namespace:
         
         kubectl get pods --namespace vm-system
         

VM Runtime on GDC is disabled when only the pods that belong to the `vmruntime-controller-manager` deployment are running in the namespace.




### Understand the behavior for running VMs

The `baremetal.cluster.gke.io/vmrumtime-force-disable`annotation can be used on VM Runtime on GDC resource to define the behavior when the runtime is disabled while VMs are running in the cluster.

The following example shows that the value of this annotation is set to `false` by default:
    
    
    // VM runtime yaml file
    apiVersion: vm.cluster.gke.io/v1
    kind: VMRuntime
    metadata:**  annotations:
        baremetal.cluster.gke.io/vmrumtime-force-disable: "false"**
      name: vmruntime
    [...]
    

When this annotation is set to `false`, VM Runtime on GDC tries to protect running VMs. Delete all running VMs before the VM Runtime on GDC is disabled, or specify the `--force=true` parameter with the `bmctl disable vmruntime` command as shown in the previous section.

The following table explains what happens to running VMs when this annotation is set to `true` or `false` and if you specify the `--force=true` parameter or not:

**Cluster state** | **\--force parameter** | **vmrumtime-force-disable annotation** | **Behavior**  
---|---|---|---  
No VMs | N/A | N/A | Disable VM Runtime on GDC.  
Existing VMs | True  | True | Delete all running VMs and the related resources. Disable the VM Runtime on GDC.  
True  | False | Delete all running VMs and the related resources. Disable the VM Runtime on GDC.  
False  | True | Prompt to delete running VMs and related resources. When all running VMs have been deleted, disable VM Runtime on GDC.  
False  | False | Don't delete any existing VMs that are running. Don't disable the VM Runtime on GDC. The `bmctl` command returns an error.  
  
## VM Runtime on GDC preflight check

The VM Runtime on GDC preflight check validates a set of prerequisites on the machine's environment before using VM Runtime on GDC and VMs. VM creation is blocked if VM Runtime on GDC preflight check failed. The VM Runtime on GDC preflight check runs automatically when `spec.enabled` is set to true.

**Note:** You can skip the VM Runtime on GDC preflight check on selected nodes before triggering the preflight check. For example, if you want to skip the preflight check for nodes, you can label the node with `kubevm.io/VM-SkipSchedule` as follows:
    
    
    kubectl label nodes NODE_NAME "kubevm.io/VM-SkipSchedule"= --kubeconfig KUBECONFIG_PATH
    

The VM Runtime on GDC preflight check runs when you perform any of the following operations:

  1. Enable VM Runtime on GDC

  2. Enable VM Runtime on GDC features, such as useEmulation

  3. Upgrade clusters

  4. Remove `kubevm.io/VM-SkipSchedule` label at nodes

  5. Independently create VM Runtime on GDC preflight check object by running the `bmctl check vmruntimepfc --kubeconfig KUBECONFIG_PATH` command or applying a `VMRuntimePreflightCheck` YAML manifest.




You can launch VMs when the latest VM Runtime on GDC preflight check succeeds. If the preflight check fails, VM creation is blocked and you get preflight check errors.

### Verifying preflight check success

To verify if the preflight checks were successful, run the following commands:

  1. Find the last preflight checks performed:
         
         kubectl get vmruntimepfc -n vm-system --kubeconfig KUBECONFIG_PATH
         

The output should look like the following sample:
         
         NAME                                                             PASS    AGE
         vmruntime-preflight-check-6ee61513-ea5d-4340-9374-90396cac129e   false   42s
         vmruntime-preflight-check-f8d71751-a01c-471e-bab5-3370fc2addd5   true    21s
         

  2. To find the status of a preflight check, run the following command:
         
         kubectl get vmruntime vmruntime -o yaml --kubeconfig KUBECONFIG_PATH
         
         
         ...
           preflightCheckSummary:
           preflightCheckSummary:
             featureStatuses:
               CPU:
                 passed: true
               KVM:
                 passed: true
             preflightCheckName: vmruntime-preflight-check-f8d71751-a01c-471e-bab5-3370fc2addd5
             preflightCheckPassed: true
         ...
         




### Debug preflight check fails

If the preflight check fails, perform the following steps to debug:

  1. Find the last preflight checks performed.
         
         kubectl get vmruntimepfc -n vm-system
         

  2. Check the status of that preflight check for details.
         
         kubectl get vmruntimepfc -n vm-system \
             vmruntime-preflight-check-6ee61513-ea5d-4340-9374-90396cac129e -o yaml \
             --kubeconfig KUBECONFIG_PATH
         
         
         ...
         status:
         checks:
           worker-0--52229ee15841099-22c41577139a7b8c.lab.anthos:
             passed: false
             results:
             - checkName: CPU
               passed: true
             - checkName: KVM
               message: |
                 command terminated with exit code 1
                 ls: /mnt/dev/kvm: No such file or directory
               passed: false
         ...
         

  3. Fix the issue and run VM Runtime on GDC preflight check again. The following shows an example VMRuntimePreflightCheck YAML manifest:
         
         apiVersion: vm.cluster.gke.io/v1
         kind: VMRuntimePreflightCheck
         metadata:
           name: vmruntime-preflight-check-manual
           namespace: vm-system
         




## What's next

  * [Create a VM in Google Distributed Cloud](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/vm-runtime/quickstart).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-21 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-21 UTC."],[],[]] 
