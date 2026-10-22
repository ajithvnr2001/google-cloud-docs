---
url: https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/repair-admin-control-plane/
title: Repair the admin cluster's control-plane VM \u00a0|\u00a0 Google Distributed Cloud software only for VMware \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:57:13.618683+00:00
---

# Repair the admin cluster's control-plane VM  |  Google Distributed Cloud software only for VMware  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/repair-admin-control-plane/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Google Distributed Cloud ](https://docs.cloud.google.com/distributed-cloud)
  * [ Documentation ](https://docs.cloud.google.com/kubernetes-engine/enterprise/clusters/docs)
  * [ GDC for VMware ](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs)
  * [ Guides ](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/overview)



Send feedback 

#  Repair the admin cluster's control-plane VM Stay organized with collections  Save and categorize content based on your preferences. 

In a Google Distributed Cloud implementation, the control-plane VM for an admin cluster has two attached disks:

  * The boot disk has the operating system for the VM.

  * The data disk has credentials and the etcd database, which stores the state of the admin cluster. That is, the data disk stores all of the Kubernetes objects for the admin cluster.




This page shows you how to recover when the control-plane VM is lost or the boot disk is compromised. For example:

  * The boot disk becomes read-only due to spam journal logs.
  * The Docker overlay filesystem gets corrupted.



This page does not cover recovery of the data disk. For instructions on how to recover the data disk, see [Restoring an admin cluster](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/back-up-and-restore-an-admin-cluster-with-gkectl).

## Repair the control-plane VM

**Warning:** Don't run `gkectl repair admin-master` after a failed admin upgrade attempt. Instead, [resume the admin upgrade](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/upgrading#about_resume_admin).

The steps that you do to repair the admin cluster's control-plane VM differ slightly depending on whether you have a high-availability (HA) admin cluster or a non-HA admin cluster.

### HA

An HA admin cluster has three control plane VMs. You must have at least two VMs to bring up the cluster control plane. If three VMs have failed, repair the failed VMs one at a time. After the second VM is repaired and running, the cluster control plane should come back up.

  1. Run the following command:
         
         gkectl repair admin-master --config ADMIN_CLUSTER_CONFIG --kubeconfig ADMIN_CLUSTER_KUBECONFIG
         

Replace the following:

     * `ADMIN_CLUSTER_CONFIG` with the path of your admin cluster configuration file.

     * `ADMIN_CLUSTER_KUBECONFIG` with the path of your admin cluster's kubeconfig file.

The output of the command is similar to the following:
    
    Please select the control plane VM template to be used for re-creating the admin cluster's control plane VM.
    [1] VM template:         /atl-qual-vc07/vm/gke-admin-57f8g-fx9f4c729448z2v8-2-tmpl
        GKE on-prem version: 1.16.0-gke.550
        Creation time:       2023-07-25 01:52:51.815518 +0000 UTC
        CPU:                 4 CPU(s)
        Memory:              16384 MB
        Data disk:           [vsanDatastore] 37a73d64-b823-47cd-2e0c-00620b9189a0/gke-admin-57f8g/default/gke-admin-57f8g-2-data.vmdk
    
    [2] VM template:         /atl-qual-vc07/vm/gke-admin-57f8g-fx9f4c729448z2v8-0-tmpl
        GKE on-prem version: 1.16.0-gke.550
        Creation time:       2023-07-25 01:52:54.228252 +0000 UTC
        CPU:                 4 CPU(s)
        Memory:              16384 MB
        Data disk:           [vsanDatastore] 37a73d64-b823-47cd-2e0c-00620b9189a0/gke-admin-57f8g/default/gke-admin-57f8g-0-data.vmdk
    
    [3] VM template:         /atl-qual-vc07/vm/gke-admin-57f8g-fx9f4c729448z2v8-1-tmpl
        GKE on-prem version: 1.16.0-gke.550
        Creation time:       2023-07-25 01:52:54.210705 +0000 UTC
        CPU:                 4 CPU(s)
        Memory:              16384 MB
        Data disk:           [vsanDatastore] 37a73d64-b823-47cd-2e0c-00620b9189a0/gke-admin-57f8g/default/gke-admin-57f8g-1-data.vmdk
    
    Please enter your numeric choice:
    

  2. Enter the number for the VM that you want to repair. If you don't see the VM in the output, contact Google Cloud Support.

If you have three VMs that need to be repaired, `gkectl repair admin-master` outputs an error message similar to the following after repairing the first VM:
         
         If you are repairing admin control plane VM for HA admin cluster,
         it's possible that the API server is still down after repairing one
         of the VMs. Try continue fixing other control plane VMs listed to
         recover the quorum of control plane.
         

In this case, re-run the command to repair the second VM.




### Non-HA

Run the following command:
    
    
    gkectl repair admin-master \
      --config ADMIN_CLUSTER_CONFIG \
      --kubeconfig ADMIN_CLUSTER_KUBECONFIG
    

Replace the following:

  * `ADMIN_CLUSTER_CONFIG` with the path of your admin cluster configuration file.
  * `ADMIN_CLUSTER_KUBECONFIG` with the path of your admin cluster's `kubeconfig` file.



The admin cluster's control-plane VM is cloned into a VM template, which has all the information needed to re-create the VM. The `gkectl repair admin-master` command uses the VM template to create a new VM. Then it attaches a new boot disk and the existing data disk.

If your cluster nodes get their addresses from a DHCP server, the new VM might have a different IP address from the original VM.

## What's next

  * If you need additional assistance, reach out to [Cloud Customer Care](https://cloud.google.com/support-hub). 

You can also see [Getting support](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/getting-support) for more information about support resources, including the following:

    * [Requirements](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/getting-support#support_requirements) for opening a support case.
    * [Tools](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/getting-support#support_tools) to help you troubleshoot, such as logs and metrics.
    * Supported [components](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/getting-support#whats_supported), [versions](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/getting-support#version-support), and [features](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/getting-support#supported_features) of Google Distributed Cloud for VMware (software only).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-14 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-14 UTC."],[],[]] 
