---
url: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/application/ao-user/vms/manage-vms/operations-and-lifecycle/vm-instance-lifecycle/
title: Manage the VM instance lifecycle \u00a0|\u00a0 Google Distributed Cloud Hosted Appliance \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T12:59:41.396141+00:00
---

# Manage the VM instance lifecycle  |  Google Distributed Cloud Hosted Appliance  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/application/ao-user/vms/manage-vms/operations-and-lifecycle/vm-instance-lifecycle/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Distributed, hybrid, and multicloud ](https://docs.cloud.google.com/docs/dhm-cloud)
  * [ Google Distributed Cloud ](https://docs.cloud.google.com/distributed-cloud/docs)
  * [ Air-gapped ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdch)
  * [ Appliance ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance)
  * [ 1.0.7 ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance)



Send feedback 

#  Manage the VM instance lifecycle Stay organized with collections  Save and categorize content based on your preferences. 

A VM instance can transition through many states throughout its lifecycle. When you create a VM, Google Distributed Cloud (GDC) air-gapped appliance provisions resources to start the VM. Next, the VM moves into the start state, where it prepares for a first boot. During and after start-up, a VM is considered to be running. During its lifetime, a running VM can be repeatedly stopped and restarted, or suspended and resumed.

## VM status definitions

State | Definition  
---|---  
`Pending` | The VM is accepted by the system and is waiting for allocation.  
`Provisioning` | Resources associated with the VM, such as `VirtualMachineDisk`, are being provisioned and prepared.  
`Starting` | The VM is being prepared to run.  
`Running` | The VM is running.  
`Stopping` | The VM is in the process of stopping.  
`Stopped` | The VM is stopped and isn't expected to start.  
`Paused` | The VM is paused and in a frozen state, which is preserved. The VM cannot be accessed.  
`Terminating` | The VM and its associated resources are undergoing the deletion process.  
`ErrorConfiguration` | The VM has a configuration error. The invalid configuration states can be caused by the following:  
| `MachineTypeNotFound` \- VM type the VM refers to is not found or is being deleted.  
| `MachineDiskMisconfig` \- The VM disk is incorrectly configured.  
| `InterfaceCreationFailed` \- The network interface creation failed.  
`CrashLoopBackOff` | The VM is currently in a crash loop and is waiting to be retried.  
`PendingIPAllocation` | The VM is waiting for the system to assign it an IP address.  
`Unknown` | The VM state could not be obtained, typically due to an error in communicating with the host on which it's running.  
`ErrorUnschedulable` | An error has occurred while scheduling the VM, for example, due to resource requests or scheduling constraints that cannot be satisfied or supported.  
`DiskError` | The VM has an error with one or more of the attached disks.  
`WaitingForDisk` | The VM is waiting for one or more of the attached `VirtualMachineDisk` to be ready.  
`CrashLoopBackoff` | The VM has been consistently crashing for some reason.  
  
## Before you begin

To use `gdcloud` command-line interface (CLI) commands, ensure that you have downloaded, installed, and configured the [`gdcloud` CLI](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/resources/gdcloud-overview). All commands for GDC air-gapped appliance use the `gdcloud` or `kubectl` CLI, and require an operating system (OS) environment.

### Get the kubeconfig file path

To run commands against the Management API server, ensure you have the following resources:

  1. Locate the Management API server name, or ask your Platform Administrator (PA) what the server name is.

  2. [Sign in and generate](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/application/ao-user/iam/sign-in#cli) the kubeconfig file for the Management API server if you don't have one.

  3. Use the path to replace `MANAGEMENT_API_SERVER{"</var>"}}` in these instructions.




### Request permissions and access

To perform the tasks listed in this page, you must have the Project VirtualMachine Admin role. Follow the steps to either [verify](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/application/ao-user/vms/preparation) or have your Project IAM Admin [assign](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/application/ao-user/vms/preparation#grant-user-access-vm-resources) you the Project VirtualMachine Admin (`project-vm-admin`) role in the namespace of the project where the VM resides.

For VM operations using the GDC console or the gdcloud CLI, request your Project IAM Admin to assign you both the Project VirtualMachine Admin role and the Project Viewer (`project-viewer`) role.

## Check VM status

Every VM reports its status as part of the VM's properties. Check a VM's status for any of the following reasons:

  * If there are issues with the VM.
  * To confirm the VM is running after it has started.
  * To verify the VM is in the `Paused` or `Stopped` state.



### List VMs to check status

The following procedure shows how to list VMs, view their status, and get additional status information.

  1. List all VMs and view the status of each:
         
         kubectl --kubeconfig MANAGEMENT_API_SERVER \
             get virtualmachines.virtualmachine.gdc.goog -n PROJECT
         

Replace the variables in the code examples with your own values according to the following table.

Variable| Definition | `MANAGEMENT_API_SERVER` | The Management API server `kubeconfig` file.  
---|---  
`PROJECT` | The GDC project in which the VM resides.  
  
Example output:
         
         NAME          STATUS                    AGE
         vm-1          Running                    1d
         vm-2          Stopped                    8d
         vm-3          ErrorConfiguration         1d
         

  2. Get additional details about a particular VM's status:
         
         kubectl  --kubeconfig MANAGEMENT_API_SERVER \
             get virtualmachines.virtualmachine.gdc.goog VM_NAME -n PROJECT -o \
             jsonpath='{"State:"}{.status.state}{"\n"}{"Reason:"}{.status.reason}{"\n"}{"Message:"}{.status.message}{"\n"}'
         

Replace the following:

     * `MANAGEMENT_API_SERVER` with the `kubeconfig` file for the Management API server you obtained from the `gdcloud auth login` command.
     * `VM_NAME` with the name of the new VM.
     * `PROJECT` with the GDC project in which the VM resides.

Example output showing `Reason` and `Message` values:
    
    State: ErrorConfiguration
    Reason: MachineDiskNotFound
    Message: VirtualMachineDisk disk-1 in namespace project-1 does not exist.
    

You might also get empty fields for `Reason` and `Message`. This indicates there was nothing for the system to report regarding them.

Example output with `Reason` and `Message` empty:
    
    State: Running
    Reason:
    Message:
    




## Stop, or restart a VM

During the VM lifecycle you might need to stop and restart a VM, or delete a VM to respond to a status change or generally manage the VM. See these pages to stop, reset, or delete a VM:

  * [Stop a VM](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/application/ao-user/vms/manage-vms/operations-and-lifecycle/start-and-stop-vm#stop-a-vm)
  * [Restart a VM](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/application/ao-user/vms/manage-vms/operations-and-lifecycle/start-and-stop-vm#restart-a-vm)
  * [Delete a VM](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/application/ao-user/vms/manage-vms/operations-and-lifecycle/delete-vms)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
