---
url: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform-application/pa-ao-operations/vm-backup/clean-up-labels-after-restore/
title: Clean up labels after restoring VM-attached disks \u00a0|\u00a0 Google Distributed Cloud air-gapped \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T20:04:57.635372+00:00
---

# Clean up labels after restoring VM-attached disks  |  Google Distributed Cloud air-gapped  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform-application/pa-ao-operations/vm-backup/clean-up-labels-after-restore/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Distributed, hybrid, and multicloud ](https://docs.cloud.google.com/docs/dhm-cloud)
  * [ Google Distributed Cloud ](https://docs.cloud.google.com/distributed-cloud/docs)
  * [ Air-gapped ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdch)
  * [ 1.16.2 (Latest) ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag)



Send feedback 

#  Clean up labels after restoring VM-attached disks Stay organized with collections  Save and categorize content based on your preferences. 

This page guides you through how to prevent potential data loss or restore failures when working with disks that were restored from backups of disks attached to virtual machines (VMs).

Restoring an individual disk that was attached to a VM can leave behind specific labels on the restored disk resource and its underlying `PersistentVolumeClaim` (PVC) resource. Failure to remove the labels as described can lead to:

  * Failures during subsequent full VM restore operations.
  * Unintended modification or replacement of the restored disk's underlying PVC during a subsequent full VM restore, potentially leading to data loss on the restored disk.

**Important:** These steps are mandatory immediately after you restore an individual disk if that disk was originally attached to a VM, especially if you intend to perform full VM backups and restores involving the original VM at a later time.

## Before you begin

To clean up the labels after restoring a VM-attached disk, you must have the following:

  * The necessary identity and access role. Ask your Organization IAM Admin to grant you the DBS Debugger (`dbs-debugger`) role.
  * Access to the appropriate kubeconfig files for the clusters managing these resources.
  * The kubectl command-line tool installed and configured.



## Clean up labels

You must perform the cleanup for both the `VirtualMachineDisk` resource and its underlying `PersistentVolumeClaim` (PVC) resource.

### Clean up the VM disk labels

To clean up the labels of a restored VM disk, follow these steps:

  1. Get the kubeconfig file for the management API server and set the `KUBECONFIG` environment variable:
         
         export KUBECONFIG=PATH_TO_MANAGEMENT_API_KUBECONFIG
         

Replace `PATH_TO_MANAGEMENT_API_KUBECONFIG` with the path to the kubeconfig file. For more information, see [Zonal Management API server resources](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform/pa-user/iam/sign-in#zonal-resources-kubeconfig).

  2. Check that the restored `VirtualMachineDisk` resource exists in the specified namespace:
         
         kubectl get virtualmachinedisks.virtualmachine.gdc.goog \
         -n NAMESPACE RESTORED_VM_DISK_NAME
         

Replace the following:

     * `NAMESPACE`: the project namespace.
     * `RESTORED_VM_DISK_NAME`: the full name of the restored disk using the values gathered in the prerequisites. The value for this variable can be derived from `RESTORED_PREFIX`-`VM_DISK_NAME`.
  3. Remove the backup scope label from the `VirtualMachineDisk` resource. The trailing hyphen after the label key signifies removal:
         
         kubectl label virtualmachinedisks.virtualmachine.gdc.goog -n NAMESPACE \
             RESTORED_VM_DISK_NAME bpvms/VM_NAME-
         

Replace `VM_NAME` with the name of the restored VM.

  4. Optional: To verify that the `bpvms/VM_NAME` label is no longer present, you can re-run the corresponding `kubectl get` command, adjusting for the specific resource type and cluster:
         
         kubectl get virtualmachinedisks.virtualmachine.gdc.goog \
         -n NAMESPACE VM_NAME
         




### Clean up the PVC labels

To clean up the labels of the underlying PVC, follow these steps:

  1. Get the kubeconfig file for the org infrastructure cluster and set the `KUBECONFIG` environment variable:
         
         export KUBECONFIG=PATH_TO_ORG_INFRA_KUBECONFIG
         

Replace `PATH_TO_ORG_INFRA_KUBECONFIG` with the path to the kubeconfig file.

  2. Check that the underlying PVC for the restored disk exists in the specified namespace:
         
         kubectl get pvc -n NAMESPACE \
             RESTORED_VM_DISK_NAME
         

Replace the following:

     * `NAMESPACE`: the project namespace.
     * `RESTORED_VM_DISK_NAME`: the name of the restored VM disk.
  3. Remove the backup scope label from the PVC. The trailing hyphen after the label key signifies removal:
         
         kubectl label pvc -n NAMESPACE RESTORED_VM_DISK_NAME bpvms/VM_NAME-
         

Replace `VM_NAME` with the name of the restored VM.

  4. Optional: To verify that the `bpvms/VM_NAME` label is no longer present, you can re-run the corresponding `kubectl get` command, adjusting for the specific resource type and cluster:
         
         kubectl get pvc -n NAMESPACE \
             VM_NAME
         




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
