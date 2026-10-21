---
url: https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.15/how-to/repair-admin-control-plane/
title: Repairing the admin cluster's control-plane VM \u00a0|\u00a0 Google Distributed Cloud Virtual for VMware \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T17:12:11.260845+00:00
---

# Repairing the admin cluster's control-plane VM  |  Google Distributed Cloud Virtual for VMware  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.15/how-to/repair-admin-control-plane/

**Version 1.15**. This version is no longer supported. For more information see the [ version support policy](https://cloud.google.com/anthos/clusters/docs/on-prem/latest/getting-support#version_support_policy). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Google Distributed Cloud ](https://docs.cloud.google.com/distributed-cloud)
  * [ Documentation ](https://docs.cloud.google.com/kubernetes-engine/enterprise/clusters/docs)
  * [ GDCV for VMware 1.15 ](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.15)
  * [ Guides ](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.15/overview)



Send feedback 

#  Repairing the admin cluster's control-plane VM Stay organized with collections  Save and categorize content based on your preferences. 

Version 1.15 keyboard_arrow_down

  * [ Latest version ](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/latest/how-to/multi-nic)
  * [ Version 1.16 ](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.16/how-to/multi-nic)
  * [ Earlier versions (unsupported) ](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/latest/version-history#expandable-1)



In a Google Distributed Cloud implementation, the control-plane VM for an admin cluster has two attached disks:

  * The boot disk has the operating system for the VM.

  * The data disk has credentials and the etcd database, which stores the state of the admin cluster. That is, the data disk stores all of the Kubernetes objects for the admin cluster.




This page shows how to recover when the control-plane VM is lost or the boot disk is compromised. For example:

  * The boot disk becomes read-only due to spam journal logs.
  * The Docker overlay filesystem gets corrupted.



This page does not cover recovery of the data disk. For instructions on how to recover the data disk, see [Restoring an admin cluster](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.15/how-to/back-up-and-restore-an-admin-cluster-with-gkectl).

## Repairing the control-plane VM

**Warning:** Don't run `gkectl repair admin-master` after a failed admin upgrade attempt. Instead, [resume the admin upgrade](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.15/how-to/upgrading#about_resume_admin).

To repair the admin cluster's control-plane VM:
    
    
    gkectl repair admin-master --config ADMIN_CLUSTER_CONFIG --kubeconfig ADMIN_CLUSTER_KUBECONFIG
    

Replace:

  * ADMIN_CLUSTER_CONFIG with the path of your admin cluster configuration file.

  * ADMIN_CLUSTER_KUBECONFIG with the path of your admin cluster's kubeconfig file.




## Notes

The admin cluster's control-plane VM is cloned into a VM template, which has all the information needed to re-create the VM. The `gkectl repair admin-master` command uses the VM template to create a new VM. Then it attaches a new boot disk and the existing data disk.

If your cluster nodes get their addresses from a DHCP server, the new VM might have a different IP address from the original VM.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
