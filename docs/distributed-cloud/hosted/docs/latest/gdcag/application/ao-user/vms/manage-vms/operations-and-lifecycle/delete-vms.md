---
url: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/application/ao-user/vms/manage-vms/operations-and-lifecycle/delete-vms/
title: Delete VMs \u00a0|\u00a0 Google Distributed Cloud air-gapped \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T07:11:52.159505+00:00
---

# Delete VMs  |  Google Distributed Cloud air-gapped  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/application/ao-user/vms/manage-vms/operations-and-lifecycle/delete-vms/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Distributed, hybrid, and multicloud ](https://docs.cloud.google.com/docs/dhm-cloud)
  * [ Google Distributed Cloud ](https://docs.cloud.google.com/distributed-cloud/docs)
  * [ Air-gapped ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdch)
  * [ 1.16.2 (Latest) ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag)



Send feedback 

#  Delete VMs Stay organized with collections  Save and categorize content based on your preferences. 

This document explains how to delete a virtual machine (VM) instance in Google Distributed Cloud (GDC) air-gapped.

Deleting a virtual machine (VM) removes the VM and its associated resources from your project. If you don't want to delete an instance, you can temporarily stop it. For more information, see [Stop and start a VM](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/application/ao-user/vms/manage-vms/operations-and-lifecycle/start-and-stop-vm).

This document is for developers in platform administrator or application operator groups that delete VMs in a Distributed Cloud environment. For more information, see [Audiences for GDC air-gapped documentation](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/resources/audiences).

## Before you begin

To use `gdcloud` command-line interface (CLI) commands, ensure that you have downloaded, installed, and configured the [`gdcloud` CLI](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/resources/gdcloud-overview). All commands for Distributed Cloud use the `gdcloud` or `kubectl` CLI, and require an operating system (OS) environment.

### Get the kubeconfig file path

To run commands against the Management API server, ensure you have the following resources:

  1. [Sign in and generate](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/application/ao-user/iam/sign-in#cli) the kubeconfig file for the Management API server if you don't have one.

  2. Use the path to the kubeconfig file of the Management API server to replace `MANAGEMENT_API_SERVER` in these instructions.




### Request permissions and access

### Request IAM roles

Contact your Project IAM Admin to request the following roles on your project:

  * **Virtual Machine Project Admin** (`project-vm-admin`): create, modify, list, and delete VMs in the project namespace.

  * **Project Viewer**(`project-viewer`): view all resources within the project namespaces.




All VM roles must bind to the namespace of the project where the VM resides. Follow the steps to [verify](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/application/ao-user/vms/preparation#verify-user-access) your access.

## Delete a VM

Delete a VM by using the GDC console or `kubectl`. The VM must not be in a terminating or unknown state.

###  Console 

  1. In the navigation menu, click **Virtual Machines > Instances**.

  2. In the list of VMs, select the checkbox for the VM that you want to delete.

  3. Click **Delete**.

  4. In the confirmation dialog, click **Delete**.




###  gdcloud 

To delete a VM:
    
    
    gdcloud compute instances delete VM_NAME \
      --project PROJECT
    

  * Replace `VM_NAME` with the name of the VM.
  * Replace `PROJECT` with the name of the GDC project in which the VM lives.



###  kubectl 

  1. Delete the VM:
         
         kubectl --kubeconfig MANAGEMENT_API_SERVER \
           -n PROJECT \
           delete virtualmachines.virtualmachine.gdc.goog VM_NAME
         

  2. Replace `VM_NAME` and `PROJECT` with the name and project name, respectively, of the VM.

  3. Verify that you've deleted the VM:
         
         kubectl --kubeconfig MANAGEMENT_API_SERVER \
           -n PROJECT \
           get virtualmachines.virtualmachine.gdc.goog VM_NAME
         

Replace `PROJECT` with the VM project name.




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
