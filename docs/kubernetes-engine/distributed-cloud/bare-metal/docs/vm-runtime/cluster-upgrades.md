---
url: https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/vm-runtime/cluster-upgrades/
title: Upgrade VM Runtime on GDC from a Preview version \u00a0|\u00a0 Google Distributed Cloud software only for bare metal \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:57:03.146458+00:00
---

# Upgrade VM Runtime on GDC from a Preview version  |  Google Distributed Cloud software only for bare metal  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/vm-runtime/cluster-upgrades/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Distributed, hybrid, and multicloud ](https://docs.cloud.google.com/docs/dhm-cloud)
  * [ Google Distributed Cloud ](https://docs.cloud.google.com/distributed-cloud/docs)
  * [ GDC for bare metal ](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs)
  * [ Guides ](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/concepts/about-bare-metal)



Send feedback 

#  Upgrade VM Runtime on GDC from a Preview version Stay organized with collections  Save and categorize content based on your preferences. 

VM Runtime on GDC is released for General Availability (GA) with the release of Google Distributed Cloud version 1.12.0. All earlier releases of VM Runtime on GDC are in [Preview](https://cloud.google.com/products/#product-launch-stages). You can't upgrade from a Preview version to the GA version without first deleting your VMs and disabling VM Runtime on GDC. Once you've upgraded your clusters, then you can enable VM Runtime on GDC again and recreate your VMs.

To upgrade from a pre-GA version of VM Runtime on GDC:

  1. Delete all VMs and their resources from the cluster.

**Note:** If you have version 1.11 or later clusters, you can delete VMs and resource and disable VM Runtime on GDC with a single command. For information on how to use `bmctl` to disable VM Runtime on GDC, see [Disable VM Runtime on GDC](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/vm-runtime/enable-disable#disable) in the version 1.11 documentation.

For instructions for version 1.10 clusters, see [Delete VMs and their resources](https://docs.cloud.google.com/anthos/clusters/docs/bare-metal/1.10/how-to/vm-workloads#delete_vms_and_their_resources) in the 1.10 documentation. For instructions for 1.11 and later clusters, see [Delete VMs in Google Distributed Cloud](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/vm-runtime/delete).

  2. Disable VM Runtime on GDC.

  3. If Multus is installed on your cluster, uninstall it.

Multus is used with the [multi-NIC for pods](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/how-to/multi-nic) feature.

  4. Upgrade the cluster.

You can't skip minor versions when upgrading your Google Distributed Cloud. For example, if you have a version 1.10 cluster, you must first upgrade to version 1.11 before you can upgrade to version 1.12.0 or higher. For more information, see [Upgrade clusters](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/how-to/upgrade).

  5. Enable VM Runtime on GDC on your 1.12.0 or higher cluster.

For instructions, see [Enable VM Runtime on GDC](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/vm-runtime/enable-disable#enable).

  6. Recreate your VMs.

Due to changes in the VM schema for the GA release of VM Runtime on GDC, you must recreate your VMs. For use with VM Runtime on GDC on version 1.12.0 or higher clusters.




## What's next

  * [Quickstart: Create a VM in Google Distributed Cloud](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/vm-runtime/quickstart)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-14 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-14 UTC."],[],[]] 
