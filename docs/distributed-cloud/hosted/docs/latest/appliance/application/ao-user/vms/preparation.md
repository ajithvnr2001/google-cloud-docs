---
url: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/application/ao-user/vms/preparation/
title: IAM permissions preparation \u00a0|\u00a0 Google Distributed Cloud Hosted Appliance \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T12:56:23.589921+00:00
---

# IAM permissions preparation  |  Google Distributed Cloud Hosted Appliance  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/application/ao-user/vms/preparation/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Distributed, hybrid, and multicloud ](https://docs.cloud.google.com/docs/dhm-cloud)
  * [ Google Distributed Cloud ](https://docs.cloud.google.com/distributed-cloud/docs)
  * [ Air-gapped ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdch)
  * [ Appliance ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance)
  * [ 1.0.7 ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance)



Send feedback 

#  IAM permissions preparation Stay organized with collections  Save and categorize content based on your preferences. 

This document outlines the Identity and Access Management (IAM) roles and permissions necessary for requesting resource access from your Project IAM administrator. You must have the necessary IAM roles and permissions to perform tasks on virtual machines (VMs) in Google Distributed Cloud (GDC) air-gapped appliance.

This document is for developers in platform administrator or application operator groups that create and manage VMs in a GDC environment.

## About IAM

GDC air-gapped appliance offers Identity and Access Management (IAM) for granular access to specific GDC air-gapped appliance resources and prevents unwanted access to other resources. IAM operates on the security principle of least privilege and provides control over who has permission to given resources using IAM roles and permissions.

## Before you begin

To use gdcloud CLI commands, complete the required steps from the [gdcloud command-line interface (CLI)](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/resources/gdcloud-overview) sections. All commands for Google Distributed Cloud air-gapped appliance use the `gdcloud` or `kubectl` CLI, and require an operating system (OS) environment.

### Get the kubeconfig file paths

  1. Run [`gdcloud auth login`](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/application/ao-user/iam/sign-in#sign-in) to the **Management API server**.

     1. Record the path to the generated file. The following is an example of the path to record:   
`/tmp/admin-kubeconfig-with-user-identity.yaml`.

     2. Use the path to replace `MANAGEMENT_API_SERVER` in these instructions.




### Request IAM roles

Contact your Project IAM Admin to request the following roles on your project:

  * **Project VirtualMachine Admin** (project-vm-admin): create, modify, list, and delete VMs in the project namespace.

  * **Project VirtualMachine Image Admin** (project-vm-image-admin): create, list, and delete VM images in the project namespace.




All VM roles must bind to the namespace of the project where the VM resides.

For a list of all predefined roles for Application Operators (AO), see [Role descriptions](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/application/ao-user/iam/role-descriptions).

To grant or receive access to VM resources, see [Grant access to project resources](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/application/ao-user/iam/role-bindings).

## Verify user access to VM resources

Follow the steps to [sign in](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/application/ao-user/iam/sign-in) to the GDC console or gdcloud CLI to verify access to VM resources and workloads:

### Console

  1. [Sign in](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/application/ao-user/iam/sign-in#console) to the GDC console as the user requesting or verifying permissions.
  2. Confirm you're in the correct project by verifying the Organization and Project names on the GDC console home screen.
  3. In the navigation menu, click **Virtual Machines** > **Instances**.
  4. To check whether you have access to create VMs in the project, click **Create Instance**. 
     * If you can proceed with VM creation, you have permissions to create VMs.
     * If the **Create Instance** button is unavailable or you encounter an error message indicating a lack of permissions, contact your Project IAM Admin and request the Project VirtualMachine Admin (`project-vm-admin`) role in the namespace of the project where the VM resides.
  5. To determine whether you can view and create images, click **Virtual Machines** > **Import** > **Create Image**. 
     * If you can proceed with image import, you have permissions to create `VirtualMachineImageImport` resources.
     * If the **Import** or **Create Image** options are unavailable or you encounter a permissions error, contact your Project IAM Admin and request the Project VirtualMachine Image Admin (`project-vm-image-admin`) role in the namespace of the project where the VM resides.



### CLI

  1. [Sign in](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/application/ao-user/iam/sign-in#cli) as the user requesting or verifying permissions.

  2. Verify whether you, or the user, can create virtual machines:
         
         kubectl --kubeconfig MANAGEMENT_API_SERVER auth can-i create virtualmachines.virtualmachine.gdc.goog -n PROJECT
         

Replace the variables by using the following definitions:

Variable | Replacement  
---|---  
`MANAGEMENT_API_SERVER` | The Management API server `kubeconfig` path  
`PROJECT` | The project name where you create VM images  
     * If the output is `yes`, you have permissions to create a VM in the project `PROJECT`.  

     * If the output is `no`, you don't have permissions. Contact your Project IAM Admin and request the Project VirtualMachine Admin (`project-vm-admin`) role in the namespace of the project where the VM resides.
  3. Verify whether you have access to project-level VM images. Run the `kubectl` commands to verify if you can create and use `VirtualMachineImage` resources at the project level:
         
         kubectl --kubeconfig MANAGEMENT_API_SERVER auth can-i get virtualmachineimages.virtualmachine.gdc.goog -n PROJECT \
         kubectl --kubeconfig MANAGEMENT_API_SERVER auth can-i create virtualmachineimageimports.virtualmachine.gdc.goog -n PROJECT
         

Replace the variables by using the following definitions.

Variable | Replacement  
---|---  
`MANAGEMENT_API_SERVER` | The Management API server `kubeconfig` path  
`PROJECT` | The project name where you create VM images  
     * If the output is `yes`, the user has permissions to access custom VM images in the project PROJECT.
     * If the output is `no`, you don't have permissions. Contact your Project IAM Admin and request the Project VirtualMachine Image Admin (`project-vm-image-admin`) role in the namespace of the project where the VM resides.



## What's next?

  * [Create and start a VM](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/application/ao-user/vms/create-a-vm/create-and-start)
  * [Supported VM images](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/application/ao-user/vms/create-a-vm/supported-vm-images)
  * [Create custom images](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/application/ao-user/vms/create-custom-images/create-custom-images)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
