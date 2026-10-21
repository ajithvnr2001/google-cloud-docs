---
url: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/application/ao-user/vms/vm-introduction/
title: VMs overview \u00a0|\u00a0 Google Distributed Cloud air-gapped \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T11:16:08.733431+00:00
---

# VMs overview  |  Google Distributed Cloud air-gapped  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/application/ao-user/vms/vm-introduction/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Distributed, hybrid, and multicloud ](https://docs.cloud.google.com/docs/dhm-cloud)
  * [ Google Distributed Cloud ](https://docs.cloud.google.com/distributed-cloud/docs)
  * [ Air-gapped ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdch)
  * [ 1.16.2 (Latest) ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag)



Send feedback 

#  VMs overview Stay organized with collections  Save and categorize content based on your preferences. 

Google Distributed Cloud (GDC) air-gapped virtual machine (VM) management lets you provision and deploy VMs, and manage each VM through its lifecycle.

The VM manager features the following areas:

  * [**VM lifecycle**](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/application/ao-user/vms/manage-vms/operations-and-lifecycle/start-and-stop-vm): Provision and manage VMs of arbitrary shape and size, using `kubectl` commands, the API, Distributed Cloud CLI, or the GDC console.
  * [**Image management**](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/application/ao-user/vms/create-custom-images/create-custom-images): Use either an operating system (OS) image Distributed Cloud provides or a custom OS image. You can build custom OS images from a provided OS image, or from your own image.
  * [**Guest OS agent**](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/application/ao-user/vms/manage-the-os/guest-environment): Manage your VM access and observability. Serve advanced package tool (APT) packages, with their dependencies, to your VMs.
  * [**Networking**](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/application/ao-user/vms/connect-to-vm/connect-to-a-vm): Integrate with Distributed Cloud networking to maintain stable ingress and egress IP addresses.
  * [**Storage**](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/application/ao-user/vms/manage-storage/add-a-vm-disk): Access durable boot or secondary disks, disk snapshots, and machine backups through tight integration with storage.
  * [**Disaster recovery**](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform-application/pa-ao-operations/vm-backup/restore-backup/create-vm-from-backup): Use disk-level snapshots and complete VM backups for disaster recovery.



## VM instruction sets

Instructions in this documentation set are presented for the `kubectl` CLI, the GDC console, the gdcloud CLI, or the API, as applicable. In cases where only `kubectl` or the GDC console is available, the instruction set reflects that status. For example, if a feature supports only two of the three instruction sets, you see only those two sets of instructions.

Use these instructions after you [download and install gdcloud CLI](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/resources/gdcloud-download) on your computer and have completed any open tasks listed on the [Preparation](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/application/ao-user/vms/preparation) page.

## What's next

To get started, go to the [Create and start a VM instance](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/application/ao-user/vms/create-a-vm/create-and-start) page. 

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
