---
url: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/application/ao-user/vms/preparation/
title: IAM permissions preparation \u00a0|\u00a0 Google Distributed Cloud air-gapped \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T10:30:14.068028+00:00
---

# IAM permissions preparation  |  Google Distributed Cloud air-gapped  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/application/ao-user/vms/preparation/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Distributed, hybrid, and multicloud ](https://docs.cloud.google.com/docs/dhm-cloud)
  * [ Google Distributed Cloud ](https://docs.cloud.google.com/distributed-cloud/docs)
  * [ Air-gapped ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdch)
  * [ 1.16.2 (Latest) ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag)



Send feedback 

#  IAM permissions preparation Stay organized with collections  Save and categorize content based on your preferences. 

This document outlines the Identity and Access Management (IAM) roles and permissions necessary for requesting resource access from your IAM Project Admin. You must have the necessary IAM roles and permissions to perform tasks on virtual machines (VMs) in Google Distributed Cloud (GDC) air-gapped.

This document is for developers in platform administrator or application operator groups that create and manage VMs in a GDC environment. For more information, see [Audiences for GDC air-gapped documentation](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/resources/audiences).

## About IAM

Distributed Cloud offers Identity and Access Management (IAM) for granular access to specific Distributed Cloud resources and prevents unwanted access to other resources. IAM operates on the security principle of least privilege and provides control over who has permission to given resources using IAM roles and permissions.

## Before you begin

To use gdcloud CLI commands, complete the required steps from the [gdcloud command-line interface (CLI)](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/resources/gdcloud-overview) sections. All commands for Google Distributed Cloud air-gapped use the `gdcloud` or `kubectl` CLI, and require an operating system (OS) environment.

### Get the kubeconfig file path

To run commands against the Management API server, ensure you have the following resources:

  1. [Sign in and generate](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/application/ao-user/iam/sign-in#cli) the kubeconfig file for the Management API server if you don't have one.

  2. Use the path to the kubeconfig file of the Management API server to replace `MANAGEMENT_API_SERVER` in these instructions.




### Request IAM roles

Contact your IAM Project Admin to request the following roles on your project:

  * **Virtual Machine Project Admin** (project-vm-admin): create, modify, list, and delete VMs in the project namespace.

  * **Virtual Machine Image Project Admin** (project-vm-image-admin): create, list, and delete VM images in the project namespace.




All VM roles must bind to the namespace of the project where the VM resides.

For a list of all predefined roles for Application Operators (AO), see [Role descriptions](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/application/ao-user/iam/role-descriptions).

To grant or receive access to VM resources, see [Grant access to project resources](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/application/ao-user/iam/role-bindings).

## Verify user access to VM resources

Follow the steps to [sign in](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/application/ao-user/iam/sign-in) to the GDC console or gdcloud CLI to verify access to VM resources and workloads:

### Console

  1. [Sign in](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/application/ao-user/iam/sign-in#console) to the GDC console as the user requesting or verifying permissions.
  2. Confirm you're in the correct project by verifying the Organization and Project names on the GDC console home screen.
  3. In the navigation menu, click **Virtual Machines** > **Instances**.
  4. To check whether you have access to create VMs in the project, click **Create Instance**. 
     * If you can proceed with VM creation, you have permissions to create VMs.
     * If the **Create Instance** button is unavailable or you encounter an error message indicating a lack of permissions, contact your IAM Project Admin and request the Virtual Machine Project Admin (`project-vm-admin`) role in the namespace of the project where the VM resides.
  5. To determine whether you can view and create images, click **Virtual Machines** > **Import** > **Create Image**. 
     * If you can proceed with image import, you have permissions to create `VirtualMachineImageImport` resources.
     * If the **Import** or **Create Image** options are unavailable or you encounter a permissions error, contact your IAM Project Admin and request the Virtual Machine Image Project Admin (`project-vm-image-admin`) role in the namespace of the project where the VM resides.



### CLI

  1. [Sign in](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/application/ao-user/iam/sign-in#cli) with your account credentials or the credentials of the user requesting or verifying permissions.

  2. Use the `kubectl` command to verify whether you, or the user, can create virtual machines:
         
         kubectl --kubeconfig MANAGEMENT_API_SERVER \
           -n PROJECT \
           auth can-i create virtualmachines.virtualmachine.gdc.goog
         

Replace the variables by using the following definitions:

Variable | Replacement  
---|---  
`MANAGEMENT_API_SERVER` | The system kubeconfig file from `gdcloud auth login`.  
`PROJECT` | The project name where you create VM images  
     * If the output is `yes`, you have permissions to create a VM in the project `PROJECT`.
     * If the output is `no`, you don't have permissions. Contact your IAM Project Admin and request the Virtual Machine Project Admin (`project-vm-admin`) role in the namespace of the project where the VM resides.
  3. Verify whether you have access to project-level VM images. Run the `kubectl` commands to verify if you can create and use `VirtualMachineImage` resources at the project level:
         
         kubectl --kubeconfig MANAGEMENT_API_SERVER auth can-i get virtualmachineimages.virtualmachine.gdc.goog -n PROJECT \
         kubectl --kubeconfig MANAGEMENT_API_SERVER auth can-i create virtualmachineimageimports.virtualmachine.gdc.goog -n PROJECT
         

Replace the variables by using the following definitions.

Variable | Replacement  
---|---  
`MANAGEMENT_API_SERVER` | The Management API server `kubeconfig` path  
`PROJECT` | The project name where you create VM images  
     * If the output is `yes`, you have permissions to access custom VM images in the project PROJECT.
     * If the output is `no`, you don't have permissions. Contact your IAM Project Admin and request the Virtual Machine Image Project Admin (`project-vm-image-admin`) role in the namespace of the project where the VM resides.



## What's next?

  * [Manage access to standard clusters](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/application/ao-user/iam/standard-clusters)
  * [Create and start a VM](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/application/ao-user/vms/create-a-vm/create-and-start)
  * [Supported VM images](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/application/ao-user/vms/create-a-vm/supported-vm-images)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-21 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-21 UTC."],[],[]] 
