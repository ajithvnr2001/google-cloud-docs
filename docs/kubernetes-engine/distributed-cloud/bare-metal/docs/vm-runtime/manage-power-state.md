---
url: https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/vm-runtime/manage-power-state/
title: Manage the power state of VMs that use VM Runtime on GDC \u00a0|\u00a0 Google Distributed Cloud software only for bare metal \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:57:21.095600+00:00
---

# Manage the power state of VMs that use VM Runtime on GDC  |  Google Distributed Cloud software only for bare metal  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/vm-runtime/manage-power-state/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Distributed, hybrid, and multicloud ](https://docs.cloud.google.com/docs/dhm-cloud)
  * [ Google Distributed Cloud ](https://docs.cloud.google.com/distributed-cloud/docs)
  * [ GDC for bare metal ](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs)
  * [ Guides ](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/concepts/about-bare-metal)



Send feedback 

#  Manage the power state of VMs that use VM Runtime on GDC Stay organized with collections  Save and categorize content based on your preferences. 

This document is intended for application owners that run Google Distributed Cloud. This document shows you how to manage the power state of virtual machines (VMs) that use VM Runtime on GDC.

You can stop, start, and restart VMs as needed to support the lifecycle of your applications. For example, you may want to change the number of assigned vCPUs or amount of memory. After you edit the configuration of your VM, you must cycle the power state to apply the changes.

## Before you begin

To complete this document, you need access to the following resources:

  * A VM that runs in one of your clusters. If needed, [create a VM in Google Distributed Cloud](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/vm-runtime/quickstart).
  * The `virtctl` client tool installed as a plugin for `kubectl`. If needed, [install the virtctl client tool](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/vm-runtime/quickstart#install_the_virtctl_client_tool).



## Stop a VM

When you stop a VM, compute resources such as CPU and memory are freed from the underlying host. The VM is shut down.

To stop a VM that's in a running state, use the following steps.

  1. Use `kubectl` to stop a VM:
         
         kubectl virt stop VM_NAME
         

Replace `VM_NAME` with the name of the VM that you want to stop.

  2. Check the `STATUS` of your VM:
         
         kubectl get gvm VM_NAME
         

The following example output shows the VM in a `Stopped` state:
         
         NAME   STATUS    AGE   IP
           vm1    Stopped   1m    192.168.2.72
         




## Start a VM

To start a VM that's in a stopped state, use the following steps.

  1. Use `kubectl` to start a VM:
         
         kubectl virt start VM_NAME
         

Replace `VM_NAME` with the name of the VM that you want to start.

  2. Check the `STATUS` of your VM:
         
         kubectl get gvm VM_NAME
         

The following example output shows the VM in a `Running` state:
         
         NAME   STATUS    AGE   IP
           vm1    Running   1m    192.168.2.72
         




## Restart a VM

To restart a VM that's in a running state, use the following steps.

  1. Use `kubectl` to restart a VM:
         
         kubectl virt restart VM_NAME
         

Replace `VM_NAME` with the name of the VM that you want to restart.

  2. Check the `STATUS` of your VM:
         
         kubectl get gvm VM_NAME
         

The following example output shows the VM in a `Stopping` state:
         
         NAME   STATUS    AGE   IP
           vm1    Stopping  7s    192.168.2.72
         

  3. Check the `STATUS` of your VM again after a minute or two:
         
         kubectl get gvm VM_NAME
         

After the VM has successfully restarted, the following example output shows the VM in a `Running` state again:
         
         NAME   STATUS    AGE   IP
           vm1    Running   1m    192.168.2.73
         

This example VM uses an ephemeral pod IP address, so the address changes when the VM restarts.




## What's next

  * [Edit a VM in Google Distributed Cloud](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/vm-runtime/edit-vm).
  * When you no longer need VMs, [Delete a VM in Google Distributed Cloud](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/vm-runtime/delete).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-14 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-14 UTC."],[],[]] 
