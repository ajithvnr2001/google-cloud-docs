---
url: https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/vm-runtime/list-view-vms/
title: List and view VM information using VM Runtime on GDC \u00a0|\u00a0 Google Distributed Cloud software only for bare metal \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:57:06.669175+00:00
---

# List and view VM information using VM Runtime on GDC  |  Google Distributed Cloud software only for bare metal  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/vm-runtime/list-view-vms/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Distributed, hybrid, and multicloud ](https://docs.cloud.google.com/docs/dhm-cloud)
  * [ Google Distributed Cloud ](https://docs.cloud.google.com/distributed-cloud/docs)
  * [ GDC for bare metal ](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs)
  * [ Guides ](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/concepts/about-bare-metal)



Send feedback 

#  List and view VM information using VM Runtime on GDC Stay organized with collections  Save and categorize content based on your preferences. 

This document is intended for application owners that run Google Distributed Cloud. This document shows you how to list VMs that run on Google Distributed Cloud using VM Runtime on GDC. You can also view additional information for each VM.

## Before you begin

To complete this document, you need access to the following resources:

  * A VM that runs in one of your clusters. If needed, [create a VM in Google Distributed Cloud](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/vm-runtime/quickstart).
  * The `virtctl` client tool installed as a plugin for `kubectl`. If needed, [install the virtctl client tool](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/vm-runtime/quickstart#install_the_virtctl_client_tool).



## List VMs

You can list VMs and their status across all namespaces, or only VMs in a specific namespace.

### All namespaces

To view a list of VMs in your cluster, use the `kubectl` command.

  * View a list of all VMs using `kubectl get gvm`:
        
        kubectl get gvm --all-namespaces
        

The following example output shows the VM information:
        
        NAME   STATUS    AGE   IP
        vm1    Running   7m    192.168.2.72
        vm2    Running   4m    192.168.2.73
        




### Single namespace

To view a list of VMs in a specific namespace, use the `--namespace` parameter with the `kubectl` command.

  * View a list of VMs in a namespace using `kubectl get gvm`:
        
        kubectl get gvm --namespace NAMESPACE_NAME
        

Replace `NAMESPACE_NAME` with the namespace you want to view.

The following example output shows the VM information:
        
        NAME   STATUS    AGE   IP
        vm1    Running   7m    192.168.2.72
        




## View VM information

If you want to view information about a specific VM in your cluster, use `kubectl`. This option is useful to view additional configuration information for a VM, such as storage or networking.

  * View detailed information about a VM using `kubectl describe gvm`:
        
        kubectl describe gvm VM_NAME --namespace NAMESPACE_NAME
        

Replace the following values:

    * `VM_NAME`: the name of your VM.
    * `NAMESPACE_NAME`: the namespace for your VM.

The following example output snippet shows the detailed information for the VM that you specify:
    
    Name:         vm1
    Namespace:    default
    Labels:       <none>
    Annotations:  <none>
    API Version:  vm.cluster.gke.io/v1
    Kind:         VirtualMachine
    Metadata:
      Creation Timestamp:  2022-04-25T23:36:24Z
      Finalizers:
        vm.cluster.gke.io/vm-finalizer
      Generation:  1
      Managed Fields:
        API Version:  vm.cluster.gke.io/v1
        Fields Type:  FieldsV1
        fieldsV1:
    ...
    Spec:
      Compute:
      Interfaces:
        Name:          eth0
        Network Name:  pod-network
      Virt Spec:
        Template:
          Metadata:
            Creation Timestamp:  <nil>
            Labels:
              kubevirt.io/vm:  vm1
          Spec:
            Domain:
              Cpu:
                Cores:  2
              Devices:
                Disks:
                  Boot Order:  1
                  Disk:
                    Bus:  virtio
                  Name:   vm1-boot-dv
              Resources:
                Requests:
                  Memory:  4Gi
            Volumes:
              Data Volume:
                Name:  vm1-boot-dv
              Name:    vm1-boot-dv
    Status:
      ...
      Interfaces:
        Dns Config:
          Nameservers:
            172.26.232.10
        Ip Addresses:
          192.168.4.118
        Mac Address:    f8:8f:ca:00:00:01
        Name:           eth0
        Resource Name:  vm1-eth0-f8b63
        Routes:
          To:  192.168.0.0/16
          To:  172.26.232.0/24
      State:   Running
    Events:    <none>
    




## What's next

  * [Manage the power state of VMs in Google Distributed Cloud](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/vm-runtime/manage-power-state).
  * [Edit a VM in Google Distributed Cloud in Google Distributed Cloud](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/vm-runtime/edit-vm).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-14 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-14 UTC."],[],[]] 
