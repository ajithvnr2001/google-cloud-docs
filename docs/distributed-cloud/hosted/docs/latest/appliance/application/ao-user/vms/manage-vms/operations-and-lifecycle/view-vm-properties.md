---
url: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/application/ao-user/vms/manage-vms/operations-and-lifecycle/view-vm-properties/
title: View VM properties \u00a0|\u00a0 Google Distributed Cloud Hosted Appliance \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:16:25.714718+00:00
---

# View VM properties  |  Google Distributed Cloud Hosted Appliance  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/application/ao-user/vms/manage-vms/operations-and-lifecycle/view-vm-properties/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Distributed, hybrid, and multicloud ](https://docs.cloud.google.com/docs/dhm-cloud)
  * [ Google Distributed Cloud ](https://docs.cloud.google.com/distributed-cloud/docs)
  * [ Air-gapped ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdch)
  * [ Appliance ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance)
  * [ 1.0.7 ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance)



Send feedback 

#  View VM properties Stay organized with collections  Save and categorize content based on your preferences. 

View virtual machines (VMs) that have been created within a project and see details associated with each, such as the ingress IP address, the egress IP address, and the VM's status, such as `Running`.

## Before you begin

To use `gdcloud` command-line interface (CLI) commands, ensure that you have downloaded, installed, and configured the [`gdcloud` CLI](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/resources/gdcloud-overview). All commands for GDC air-gapped appliance use the `gdcloud` or `kubectl` CLI, and require an operating system (OS) environment.

### Get the kubeconfig file path

To run commands against the Management API server, ensure you have the following resources:

  1. Locate the Management API server name, or ask your Platform Administrator (PA) what the server name is.

  2. [Sign in and generate](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/application/ao-user/iam/sign-in#cli) the kubeconfig file for the Management API server if you don't have one.

  3. Use the path to replace `MANAGEMENT_API_SERVER{"</var>"}}` in these instructions.




### Request permissions and access

To perform the tasks listed in this page, you must have the Project VirtualMachine Admin role. Follow the steps to either [verify](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/application/ao-user/vms/preparation#verify-user-access) or have your Project IAM Admin [assign](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/application/ao-user/vms/preparation#grant-user-access-vm-resources) you the Project VirtualMachine Admin (`project-vm-admin`) role in the namespace of the project where the VM resides.

For VM operations using the GDC console or the gdcloud CLI, request your Project IAM Admin to assign you both the Project VirtualMachine Admin role and the Project Viewer (`project-viewer`) role.

## Get a list of VMs

You can list the VMs available in a project by using the GDC console or `kubectl`.

###  Console 

  1. In the navigation menu, click **Virtual Machines > Instances**.

  2. The VM instances page shows a list of VMs.

  3. Click the name of a VM instance to view its details.




###  gdcloud 

To list VM instances:
    
    
    gdcloud compute instances list --project PROJECT
    

  * Replace `PROJECT` with the name of the GDC project in which the VM lives.



###  kubectl 

Get a list of VMs:
    
    
    kubectl --kubeconfig MANAGEMENT_API_SERVER \
        get virtualmachines.virtualmachine.gdc.goog -n PROJECT
    

  * Replace `MANAGEMENT_API_SERVER` with the kubeconfig file for the Management API server.
  * Replace `PROJECT` with the name of the GDC project in which the VM lives.



## Locate IP addresses for a VM

See the [IP addresses](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/application/ao-user/vms/connect-to-vm/ip-addresses) page for instructions on viewing the IP address information for a given VM.

## View a VM source image

You can view the source image of a VM.

###  kubectl 

To get the VM boot disk:
    
    
      DISK=`kubectl --kubeconfig MANAGEMENT_API_SERVER get virtualmachines.virtualmachine.gdc.goog \
        -n PROJECT VM_NAME \
        -o jsonpath={.spec.disks[?(@.boot==true)].virtualMachineDiskRef.name}`
    

To view the source image:
    
    
      kubectl --kubeconfig MANAGEMENT_API_SERVER get virtualmachinedisk.virtualmachine.gdc.goog \
        -n PROJECT $DISK -o jsonpath={.spec.source.image.name}
    

  * Replace `MANAGEMENT_API_SERVER` with the kubeconfig file for the Management API server.
  * Replace `PROJECT` with the GDC project in which the VM lives.
  * Replace `VM_NAME` with the name of the VM.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
