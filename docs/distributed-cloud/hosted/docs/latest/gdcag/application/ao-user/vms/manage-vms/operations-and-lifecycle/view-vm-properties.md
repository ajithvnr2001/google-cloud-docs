---
url: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/application/ao-user/vms/manage-vms/operations-and-lifecycle/view-vm-properties/
title: View VM properties \u00a0|\u00a0 Google Distributed Cloud air-gapped \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:08:01.796399+00:00
---

# View VM properties  |  Google Distributed Cloud air-gapped  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/application/ao-user/vms/manage-vms/operations-and-lifecycle/view-vm-properties/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Distributed, hybrid, and multicloud ](https://docs.cloud.google.com/docs/dhm-cloud)
  * [ Google Distributed Cloud ](https://docs.cloud.google.com/distributed-cloud/docs)
  * [ Air-gapped ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdch)
  * [ 1.16.2 (Latest) ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag)



Send feedback 

#  View VM properties Stay organized with collections  Save and categorize content based on your preferences. 

This document explains how to view the properties of a virtual machine (VM) instance in Google Distributed Cloud (GDC) air-gapped.

View VMs that you create within a project and see details associated with each, such as the ingress IP address, the egress IP address, and the VM status, for example, `Running`.

This document is for developers in platform administrator or application operator groups that view VM properties in a Distributed Cloud environment. For more information, see [Audiences for GDC air-gapped documentation](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/resources/audiences).

## Before you begin

To use `gdcloud` command-line interface (CLI) commands, ensure that you have downloaded, installed, and configured the [`gdcloud` CLI](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/resources/gdcloud-overview). All commands for Distributed Cloud use the `gdcloud` or `kubectl` CLI, and require an operating system (OS) environment.

### Get the kubeconfig file path

To run commands against the Management API server, ensure you have the following resources:

  1. [Sign in and generate](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/application/ao-user/iam/sign-in#cli) the kubeconfig file for the Management API server if you don't have one.

  2. Use the path to the kubeconfig file of the Management API server to replace `MANAGEMENT_API_SERVER` in these instructions.




### Request IAM roles

Contact your Project IAM Admin to request the following roles on your project:

  * **Virtual Machine Project Admin** (`project-vm-admin`): create, modify, list, and delete VMs in the project namespace.

  * **Project Viewer**(`project-viewer`): view all resources within the project namespaces.




All VM roles must bind to the namespace of the project where the VM resides. Follow the steps to [verify](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/application/ao-user/vms/preparation#verify-user-access) your access.

## Get a list of VMs

You can list the VMs available in a project by using the GDC console, gdcloud CLI, or `kubectl`.

###  Console 

  1. In the navigation menu, click **Virtual Machines > Instances**.

  2. The VM instances page shows a list of VMs.

  3. Click the name of a VM instance to view its details.




###  gdcloud 

To list VM instances:
    
    
    gdcloud compute instances list \
      --project PROJECT
    

  * Replace `PROJECT` with the name of the GDC project in which the VM lives.



###  kubectl 

Get a list of VMs:
    
    
    kubectl --kubeconfig MANAGEMENT_API_SERVER \
      -n PROJECT \
      get virtualmachines.virtualmachine.gdc.goog
    

  * Replace `MANAGEMENT_API_SERVER` with the kubeconfig file for the Management API server.
  * Replace `PROJECT` with the name of the GDC project in which the VM lives.



## Locate IP addresses for a VM

See the [IP addresses](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/application/ao-user/vms/connect-to-vm/ip-addresses) page for instructions on viewing the IP address information for a given VM.

## View a VM source image

You can view the source image of a VM.

###  kubectl 

To get the VM boot disk:
    
    
      DISK=`kubectl --kubeconfig MANAGEMENT_API_SERVER \
        -n PROJECT \
        get virtualmachines.virtualmachine.gdc.goog VM_NAME \
        -o jsonpath={.spec.disks[?(@.boot==true)].virtualMachineDiskRef.name}`
    

To view the source image:
    
    
      kubectl --kubeconfig MANAGEMENT_API_SERVER \
        -n PROJECT \
        get virtualmachinedisk.virtualmachine.gdc.goog $DISK \
        -o jsonpath={.spec.source.image.name}
    

  * Replace `MANAGEMENT_API_SERVER` with the kubeconfig file for the Management API server.
  * Replace `PROJECT` with the GDC project in which the VM lives.
  * Replace `VM_NAME` with the name of the VM.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
