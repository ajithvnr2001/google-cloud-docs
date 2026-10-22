---
url: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/application/ao-user/vms/manage-the-os/guest-environment/
title: Guest environment \u00a0|\u00a0 Google Distributed Cloud air-gapped \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T10:30:15.446561+00:00
---

# Guest environment  |  Google Distributed Cloud air-gapped  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/application/ao-user/vms/manage-the-os/guest-environment/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Distributed, hybrid, and multicloud ](https://docs.cloud.google.com/docs/dhm-cloud)
  * [ Google Distributed Cloud ](https://docs.cloud.google.com/distributed-cloud/docs)
  * [ Air-gapped ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdch)
  * [ 1.16.2 (Latest) ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag)



Send feedback 

#  Guest environment Stay organized with collections  Save and categorize content based on your preferences. 

This document describes the steps to configure and manage a guest environment on a virtual machine (VM) instance in Google Distributed Cloud (GDC) air-gapped.

The Distributed Cloud guest environment is a necessary component to configure SSH keys on your virtual machines (VM) to both connect and transfer files remotely. You must have the guest environment before you [connect to a VM](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/application/ao-user/vms/connect-to-vm/connect-to-a-vm) and [transfer files](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/application/ao-user/vms/connect-to-vm/transfer-files), where you configure the SSH keys and use the secure copy (SCP) command-line tool. The guest environment is installed and enabled by default on all GDC VMs. 

This document is for developers in platform administrator or application operator groups that manage the guest environment for VMs in a Distributed Cloud environment. For more information, see [Audiences for GDC air-gapped documentation](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/resources/audiences).

### Request IAM roles

To manage the guest environment in a VM system within the project namespace, contact your IAM Project Admin to request the **Virtual Machine Project Admin** (`project-vm-admin`) role.

All VM roles must bind to the namespace of the project where the VM resides. Follow the steps to [verify](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/application/ao-user/vms/preparation#verify-user-access) your access.

## Disable access management

Follow these steps to disable the access management feature while keeping the guest environment enabled:

  1. Stop your VM.
  2. Edit the VM `spec` field:
         
         kubectl --kubeconfig MANAGEMENT_API_SERVER \
           -n VM_NAMESPACE \
           edit virtualmachines.virtualmachine.gdc.goog VM_NAME
         

Replace `VM_NAME` with your VM name, and `VM_NAMESPACE` with your VM namespace.

  3. Add the following fields to the `spec` field:
         
         apiVersion: virtualmachine.gdc.goog/v1
         kind: VirtualMachine
         metadata:
           name: vm-example
           namespace: project-example
         spec:
           guestEnvironment:
             accessManagement:
               enable: false
         

The `name` field contains your VM name, and the `namespace` field contains your VM namespace.

  4. [Restart your VM](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/application/ao-user/vms/manage-vms/operations-and-lifecycle/start-and-stop-vm#restart-a-vm).




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-21 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-21 UTC."],[],[]] 
