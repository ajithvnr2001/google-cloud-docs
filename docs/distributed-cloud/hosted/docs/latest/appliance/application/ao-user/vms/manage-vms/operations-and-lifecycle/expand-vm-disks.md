---
url: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/application/ao-user/vms/manage-vms/operations-and-lifecycle/expand-vm-disks/
title: Expand VM disks \u00a0|\u00a0 Google Distributed Cloud Hosted Appliance \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:16:26.661595+00:00
---

# Expand VM disks  |  Google Distributed Cloud Hosted Appliance  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/application/ao-user/vms/manage-vms/operations-and-lifecycle/expand-vm-disks/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Distributed, hybrid, and multicloud ](https://docs.cloud.google.com/docs/dhm-cloud)
  * [ Google Distributed Cloud ](https://docs.cloud.google.com/distributed-cloud/docs)
  * [ Air-gapped ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdch)
  * [ Appliance ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance)
  * [ 1.0.7 ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance)



Send feedback 

#  Expand VM disks Stay organized with collections  Save and categorize content based on your preferences. 

You can increase the size of your virtual machine (VM) disk partition when your VM instance requires additional storage space or increased performance limits.

You can only increase, and not decrease, the size of a disk. To decrease the disk size, you must create a new disk with a smaller size. Until you delete the original, larger disk, you are charged for both disks.

This page provides instructions to increase the size of both boot and non-boot disks.

## Before you begin

To get the permissions you need to perform disk expansion, ask your Project IAM Admin to grant you the Project VirtualMachine Admin (`project-vm-admin`) role in the namespace where the VM resides. Follow the steps to [verify](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/application/ao-user/vms/preparation#verify-user-access) that you have the required permissions.

## Disk expansion

Follow the gdcloud or API steps to expand the disk size.

###  gdcloud 

Expand the VM disk:
    
    
     gdcloud compute disks resize DISK_NAME --project=PROJECT --size=NEW_SIZE
    

  * Replace `DISK_NAME` with the name of the disk.

  * Replace `PROJECT` with the name of the GDC project in which the VM lives.

  * Replace `NEW_SIZE` with the new size of the disk.




###  API 

  1. Expand the `VirtualMachineDisk` by updating the `.spec.size` field:
         
         kubectl --kubeconfig MANAGEMENT_API_SERVER \
             apply -n PROJECT -f - <<EOF
         apiVersion: virtualmachine.gdc.goog/v1
         kind: VirtualMachineDisk
         metadata:
           name: VM_BOOT_DISK_NAME
         spec:
           source:
             image:
               name: BOOT_DISK_IMAGE_NAME
               namespace: vm-system
           size: BOOT_DISK_SIZE
         EOF
         

Replace the following variables:

Variable| Definition | `MANAGEMENT_API_SERVER` | The Management API server kubeconfig file.  
---|---  
`PROJECT` | The GDC project to create the VM.  
`VM_BOOT_DISK_NAME` | The name of the new VM boot disk.  
`BOOT_DISK_IMAGE_NAME` | The name of the image to use for the new VM boot disk.  
`BOOT_DISK_SIZE` | The size of the boot disk, such as `20Gi`.  
This value must always be greater than or equal to the `minimumDiskSize` of the boot disk image.  
  2. Wait until the `.spec.size` field updates to the new size.




## Expand the file systems and partitions

After expanding the block device, you must expand the guest's partition and file system so that applications can consume the additional space. Some OS's do this automatically using `cloud-init`.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
