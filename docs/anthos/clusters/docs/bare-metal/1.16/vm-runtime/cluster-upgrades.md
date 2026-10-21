---
url: https://docs.cloud.google.com/anthos/clusters/docs/bare-metal/1.16/vm-runtime/cluster-upgrades/
title: Upgrade VM Runtime on GDC from a Preview version \u00a0|\u00a0 Google Distributed Cloud Virtual for Bare Metal \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-15T20:47:20.447817+00:00
---

# Upgrade VM Runtime on GDC from a Preview version  |  Google Distributed Cloud Virtual for Bare Metal  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/anthos/clusters/docs/bare-metal/1.16/vm-runtime/cluster-upgrades/

**Version 1.16**. This version is no longer supported. For information about how to upgrade to version 1.28, see [ Upgrade clusters](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/how-to/upgrade) in the latest documentation. For more information about supported and unsupported versions, see the [Versioning](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/version-history) page in the latest documentation.

  * [ Home ](https://docs.cloud.google.com/)
  * [ Google Distributed Cloud ](https://docs.cloud.google.com/distributed-cloud)
  * [ Documentation ](https://docs.cloud.google.com/kubernetes-engine/enterprise/clusters/docs)
  * [ GDCV for Bare Metal 1.16 ](https://docs.cloud.google.com/anthos/clusters/docs/bare-metal/1.16)
  * [ Guides ](https://docs.cloud.google.com/anthos/clusters/docs/bare-metal/1.16/concepts/about-bare-metal)



Send feedback 

#  Upgrade VM Runtime on GDC from a Preview version Stay organized with collections  Save and categorize content based on your preferences. 

Version 1.16 keyboard_arrow_down

  * [ Latest ](https://docs.cloud.google.com/anthos/clusters/docs/bare-metal/latest/vm-runtime/cluster-upgrades)
  * [ Version 1.16 ](https://docs.cloud.google.com/anthos/clusters/docs/bare-metal/1.16/vm-runtime/cluster-upgrades)
  * [ Earlier versions (unsupported) ](https://docs.cloud.google.com/anthos/clusters/docs/bare-metal/1.16/getting-support#version-support)



VM Runtime on GDC is released for General Availability (GA) with the release of Google Distributed Cloud version 1.12.0. All earlier releases of VM Runtime on GDC are in [Preview](https://cloud.google.com/products/#product-launch-stages). You can't upgrade from a Preview version to the GA version without first deleting your VMs and disabling VM Runtime on GDC. Once you've upgraded your clusters, then you can enable VM Runtime on GDC again and recreate your VMs.

To upgrade from a pre-GA version of VM Runtime on GDC:

  1. Delete all VMs and their resources from the cluster.

**Note:** If you have version 1.11 clusters, you can delete VMs and resource and disable VM Runtime on GDC with a single command. For information on how to use `bmctl` to disable VM Runtime on GDC, see [Disable VM Runtime on GDC](https://docs.cloud.google.com/anthos/clusters/docs/bare-metal/1.11/how-to/vm-workloads#disable) in the version 1.11 documentation.

For instructions for version 1.10 clusters, see [Delete VMs and their resources](https://docs.cloud.google.com/anthos/clusters/docs/bare-metal/1.10/how-to/vm-workloads#delete_vms_and_their_resources) in the 1.10 documentation. For instructions for 1.11 clusters, see [Delete VMs and their resources](https://docs.cloud.google.com/anthos/clusters/docs/bare-metal/1.10/how-to/vm-workloads#delete_vms_and_their_resources) in the 1.11 documentation.

  2. Disable VM Runtime on GDC.

For instructions for version 1.10 clusters, see [Disable VM Runtime on GDC](https://docs.cloud.google.com/anthos/clusters/docs/bare-metal/1.10/how-to/vm-workloads#disable_anthos_vm_runtime) in the 1.10 documentation. For instructions for 1.11 clusters, see [Disable VM Runtime on GDC](https://docs.cloud.google.com/anthos/clusters/docs/bare-metal/1.10/how-to/vm-workloads#disable) in the 1.11 documentation.

  3. If Multus is installed on your cluster, uninstall it.

Multus is used with the [multi-NIC for pods](https://docs.cloud.google.com/anthos/clusters/docs/bare-metal/1.16/how-to/multi-nic) feature.

  4. Upgrade the cluster to version 1.12.0 or higher.

You can't skip minor versions when upgrading your Google Distributed Cloud. For example, if you have a version 1.10 cluster, you must first upgrade to version 1.11 before you can upgrade to version 1.12.0 or higher. For more information, see [Upgrade clusters](https://docs.cloud.google.com/anthos/clusters/docs/bare-metal/1.16/how-to/upgrade).

  5. Enable VM Runtime on GDC on your 1.12.0 cluster.

For instructions, see [Enable VM Runtime on GDC](https://docs.cloud.google.com/anthos/clusters/docs/bare-metal/1.16/vm-runtime/enable-disable#enable).

  6. Recreate your VMs.

Due to changes in the VM schema for the GA release of VM Runtime on GDC, you must recreate your VMs. For use with VM Runtime on GDC on version 1.12.0 or higher clusters.




## What's next

  * [Quickstart: Create a VM in Google Distributed Cloud](https://docs.cloud.google.com/anthos/clusters/docs/bare-metal/1.16/vm-runtime/quickstart)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
