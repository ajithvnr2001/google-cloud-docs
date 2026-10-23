---
url: https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/vm-runtime/delete/
title: Delete a VM in Google Distributed Cloud \u00a0|\u00a0 Google Distributed Cloud software only for bare metal \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:22:56.725764+00:00
---

# Delete a VM in Google Distributed Cloud  |  Google Distributed Cloud software only for bare metal  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/vm-runtime/delete/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Distributed, hybrid, and multicloud ](https://docs.cloud.google.com/docs/dhm-cloud)
  * [ Google Distributed Cloud ](https://docs.cloud.google.com/distributed-cloud/docs)
  * [ GDC for bare metal ](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs)
  * [ Guides ](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/concepts/about-bare-metal)



Send feedback 

#  Delete a VM in Google Distributed Cloud Stay organized with collections  Save and categorize content based on your preferences. 

This document is intended for application owners that run Google Distributed Cloud. This document shows you how to delete virtual machines (VMs) that use VM Runtime on GDC. You can choose to delete both the VM and associated disk resources, only the VM resource, or only the disk resources.

## Before you begin

To complete this document, you need access to the following resources:

  * A VM that runs in one of your clusters. If needed, [create a VM in Google Distributed Cloud](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/vm-runtime/quickstart).
  * The `virtctl` client tool installed as a plugin for `kubectl`. If needed, [install the virtctl client tool](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/vm-runtime/quickstart#install_the_virtctl_client_tool).



## Delete the VM and disk resources

This option deletes the VM resource and any associated virtual disks.

  * Use `kubectl` to delete both the VM and it's associated disk resources:
        
        kubectl virt delete vm VM_NAME --all
        

Replace `VM_NAME` with the name of the VM that you want to delete.

If you want to check the resources used by the VM that would be deleted, specify the `--dry-run` flag together with `--all`.

If you want to delete the VM without also deleting the disk resource, don't include the `--all` flag, as shown in the next section.




## Delete the VM resource

This option only deletes the VM resource. Any associated virtual disks remain as part of the cluster. This option lets you create another VM and resuse the disk resource. The lifecycle of the VM can be managed separately to the lifecycle of the disk resource.

  * Use `kubectl` to delete only the VM:
        
        kubectl virt delete vm VM_NAME
        

Replace `VM_NAME` with the name of the VM that you want to delete.




## Delete the VM disk resource

This option deletes a virtual disk resource. If the associated VM still runs in the cluster, the VM resource isn't deleted. This approach lets you delete a disk resource that remains if you previously deleted a VM without using the `--all` parameter.

  * Use `kubectl` to delete only the VM's disk resources:
        
        kubectl virt delete disk DISK_NAME
        

Replace `DISK_NAME` with the name of the disk that you want to delete. For example, the default boot disk for a VM is named `DISK_NAME-boot-dv`. You can list all existing disks using `kubectl get datavolume`.

If you try to delete a VM's disk before deleting the VM, the disk is marked for deletion. The disk is only deleted when you also delete the VM.




## What's next

  * [Create and manage disks in Google Distributed Cloud](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/vm-runtime/create-manage-disks).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
