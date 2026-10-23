---
url: https://docs.cloud.google.com/migrate/virtual-machines/docs/5.0/support/troubleshooting/
title: Troubleshoot Migrate to Virtual Machines \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:54:04.256869+00:00
---

# Troubleshoot Migrate to Virtual Machines  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/migrate/virtual-machines/docs/5.0/support/troubleshooting/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Migration ](https://docs.cloud.google.com/docs/migration)
  * [ Migrate to Virtual Machines ](https://docs.cloud.google.com/migrate/virtual-machines/docs/5.0)
  * [ Guides ](https://docs.cloud.google.com/migrate/virtual-machines/docs/5.0/discover/lifecycle)



Send feedback 

#  Troubleshoot Migrate to Virtual Machines Stay organized with collections  Save and categorize content based on your preferences. 

Learn about troubleshooting steps that you might find helpful if you run into problems using Migrate to Virtual Machines. 

## Error: Required compute.subnetworks.use permission

A [Shared VPC](https://docs.cloud.google.com/vpc/docs/shared-vpc) allows an organization to connect resources from multiple projects to a common [Virtual Private Cloud (VPC) network](https://docs.cloud.google.com/vpc/docs/vpc), so that they can communicate with each other securely and efficiently using internal IPs from that network.

Migrate to Virtual Machines lets you deploy a Compute Engine instance to a project that has access to a Shared VPC. However, if you have not assigned the `compute.subnetworks.use` role to the Migrate to Virtual Machines default service account, you see an error message in the following format when you try to deploy the Compute Engine instance:

`"Create instance of VM "my-vm" from source "my-proj" to target project "target-proj" using Compute Engine instance name "instance-id" failed due to: Required 'compute.subnetworks.use' permission for 'projects/vpc-proj/regions/us-central1/subnetworks/shared-central1'`

Ensure that you assign the `compute.subnetworks.use` role on the Shared VPC host project to the Migrate to Virtual Machines default service account as described in [Configuring permissions for a Shared VPC](https://docs.cloud.google.com/migrate/virtual-machines/docs/5.0/get-started/shared-vpc).

## Error: The user does not have access to service account

As part of [Configuring the target for a migrated VM](https://docs.cloud.google.com/migrate/virtual-machines/docs/5.0/migrate/migrating-vms#configure-target), Migrate to Virtual Machines lets you assign a service account to a Compute Engine instance running on a target project.

However, to be able to assign a service account to a Compute Engine instance running on a target project, the default Migrate to Virtual Machines service account on the host project must have the `Service Account User` role on the target service account.

If you assign a service account to a Compute Engine instance, but the host project does not have the `Service Account User` role on the target service account, then you see the following error when you try to test-clone or cut-over the VM:

`Test-Clone of VM "my-vm" from source "source-vm" to target project "target-proj" using Compute Engine instance name "my-instance" failed due to: The user does not have access to service account 'target-service-account-email'. User: 'host-user-account-email'. Ask a project owner to grant you the iam.serviceAccountUser role on the service account`

Ensure that the default Migrate to Virtual Machines service account is configured correctly to allow access to the target service account. See [Configuring permissions on target project service account](https://docs.cloud.google.com/migrate/virtual-machines/docs/5.0/get-started/target-sa-compute-engine) for more.

## Error: Report generation failed due to vCenter maximum query limit exceeded

To help you determine the optimal settings for the Compute Engine target, Migrate to Virtual Machines lets you create a [source VM utilization report](https://docs.cloud.google.com/migrate/virtual-machines/docs/5.0/migrate/create-report). This report displays information about resource allocation and utilization for the source VMs deployed on vCenter.

The report is generated from data collected on vCenter. When generating the report, you might see an error in the following format indicating that a vCenter quota limit has been reached:

`Report generation for source source connected to vCenter vcenter failed due to vCenter maximum query limit exceeded. Details: VC message`

See this [vSphere article](https://kb.vmware.com/s/article/2107096) for more information on increasing the quota limit.

## Error: Instance created in Migrate to Virtual Machines is not booting

When your source VM boot disk isn't the first disk on your VM's list of disks, you may receive a serial console error that shows the following message:
    
    
    drive 0x000f2410: PCHS=0/0/0 translation=lba LCHS=1024/255/63 s=104857600
    drive 0x000f23d0: PCHS=0/0/0 translation=lba LCHS=1024/255/63 s=167772160
    drive 0x000f2390: PCHS=0/0/0 translation=lba LCHS=1024/255/63 s=83886080
    Sending Seabios boot VM event.
    Booting from Hard Disk 0...
    

In order to mitigate this error, clone your disks and connect those clones in the correct order to a new VM on Migrate to Virtual Machines.

To clone your disk and connect it in the correct order, follow these steps:

  1. Stop your replicated VM.
  2. Clone your original boot disk:
         
         gcloud compute disks create -project=$PROJECT --zone=$ZONE --source-disk=$DISK new-disk-name

  3. Run the following command to reassign the license to your cloned boot disk and add relevant tags (Example with `windows2008-r2`):
         
         gcloud compute disks create --project=$PROJECT --zone=$ZONE --source-disk=disk created on step #2 --licenses=projects/windows-cloud/global/licenses/windows-server-2008-r2-dc --guest-os-features=VIRTIO_SCSI_MULTIQUEUE,MULTI_IP_SUBNET,WINDOWS new-disk-name

  4. Edit the VM:

     1. Detach your current boot disk and attach it on the **Additional disks**.
     2. Remove the original boot disk from the **Additional disks**.
     3. Attach the created disk from **Step 3** on the **Boot Disk**.
     4. Save your changes.



After confirming your VM's boot process, you can delete your original boot disk.

## Error: Windows VM is running `chkdsk' on the first boot of a clone

The Migrate to Virtual Machines test-clone phase instantiates a clone of the VM in the cloud based off of a snapshot taken while the source VM is running.

In some cases, this may trigger an automatic `chkdsk` scan operation in Windows VMs while the clone is booting in cloud. If such errors are blocking verification steps, consider shutting the VM down between replication cycles to allow Migrate to Virtual Machines to take a snapshot while the VM is off.

This does not affect the VM when it is cut over, as the VM is shut down as part of the cut-over process before Migrate to Virtual Machines completes the final sync phase.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
