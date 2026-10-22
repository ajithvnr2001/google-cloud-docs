---
url: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/application/ao-user/vms/manage-the-os/startup-script-vm-instance/
title: Use a startup script on Linux VMs \u00a0|\u00a0 Google Distributed Cloud air-gapped \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:08:18.618675+00:00
---

# Use a startup script on Linux VMs  |  Google Distributed Cloud air-gapped  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/application/ao-user/vms/manage-the-os/startup-script-vm-instance/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Distributed, hybrid, and multicloud ](https://docs.cloud.google.com/docs/dhm-cloud)
  * [ Google Distributed Cloud ](https://docs.cloud.google.com/distributed-cloud/docs)
  * [ Air-gapped ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdch)
  * [ 1.16.2 (Latest) ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag)



Send feedback 

#  Use a startup script on Linux VMs Stay organized with collections  Save and categorize content based on your preferences. 

This document explains how to use startup scripts to start up a virtual machine (VM) instance and its associated programs in Google Distributed Cloud (GDC) air-gapped.

A startup script is an automation tool that performs tasks during the VM start-up process. Use startup scripts to automate VM configuration and deployment tasks on new or existing instances, saving you time and reducing manual configuration effort.

This document is for developers in platform administrator or application operator groups that want to use startup scripts for VMs in a Distributed Cloud environment. For more information, see [Audiences for GDC air-gapped documentation](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/resources/audiences).

## Before you begin

To use `gdcloud` command-line interface (CLI) commands, ensure that you have downloaded, installed, and configured the [`gdcloud` CLI](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/resources/gdcloud-overview). All commands for Distributed Cloud use the `gdcloud` or `kubectl` CLI, and require an operating system (OS) environment.

### Get the kubeconfig file path

To run commands against the Management API server, ensure you have the following resources:

  1. [Sign in and generate](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/application/ao-user/iam/sign-in#cli) the kubeconfig file for the Management API server if you don't have one.

  2. Use the path to the kubeconfig file of the Management API server to replace `MANAGEMENT_API_SERVER` in these instructions.




### Request IAM roles

To use startup scripts for a VM, contact your Project IAM Admin to request the following roles on your project:

  * **Virtual Machine Project Admin** (`project-vm-admin`): create, modify, list, and delete VMs in the project namespace.

  * **Secret Admin** (`secret-admin`): get, list, create, update, delete, patch, and watch Kubernetes secrets in the project namespace. Use this role to specify startup script secrets. You don't need this role to specify plain text startup scripts.




All VM roles must bind to the namespace of the project where the VM resides. Follow the steps to [verify](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/application/ao-user/vms/preparation#verify-user-access) your access.

## Pass a startup script

You can use either bash or non-bash scripts as startup scripts. To do so, include `#!/bin/…` at the beginning of the script to indicate the script interpreter. For example, to use a Python 3 startup script, add `#! /usr/bin/python3` to the beginning of the script.

Google Distributed Cloud (GDC) air-gapped runs startup scripts in order they appear in the `startupScripts` array.

The following table shows the script format to use based on your script size:

**Script size** | **Script format**  
---|---  
Scripts up to 2048 bytes | Clear text  
Scripts greater than 2048 bytes | Kubernetes secret  
  
### Define a startup script

To use a startup script you must add the `startupScripts` field to the VM `spec` field. Within this field you can specify multiple startup scripts as clear text or as a Kubernetes secret.

The following example specifies the startup scripts as clear text and a Kubernetes secret:
    
    
    apiVersion: virtualmachine.gdc.goog/v1
    kind: VirtualMachine
    metadata:
      name: "my-vm"
    spec:
      # …
      startupScripts:
      - name: hello-world
        script: |
          #!/bin/bash
          echo hello
      - name: add-user
        scriptSecretRef:
          name: add-user
    ---
    
    apiVersion: v1
    kind: Secret
    type: Opaque
    metadata:
      name: add-user
    data:
      script:
        IyEvYmluL2Jhc2gKYWRkdXNlciB1c2VyCg==
    

Review the following considerations:

  * The startup script runs on _every boot_.
  * The startup script has default root privileges.
  * In the Kubernetes secret, the name of the `scriptSecretRef` in the VM `spec` must match the `metadata.name` field.
  * In the Kubernetes secret, specify the startup script content by adding a key `script` to the `data` field.



## Create a new VM with a startup script

These instructions apply regardless of what you use as the image to create your VM. Complete the following:

  1. To create a startup script as a Kubernetes secret, run:
         
         cat <<EOF >>FILE_NAME
         STARTUP_SCRIPT_CONTENT
         EOF
         
         
         kubectl --kubeconfig MANAGEMENT_API_SERVER \
           -n PROJECT \
           create secret generic SECRET_NAME \
           --from-file=script=FILE_NAME
         
         
         rm FILE_NAME
         

  2. Reference the steps to create a VM as described on the [create a VM](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/application/ao-user/vms/create-a-vm/create-and-start) page. At [step one](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/application/ao-user/vms/create-a-vm/create-and-start#create-vm-from-provided-image) add the startup script or scripts to the `spec` field before you run the command to create a VM.

This example defines a startup script with both clear text and a Kubernetes secret:
         
         apiVersion: virtualmachine.gdc.goog/v1
         kind: VirtualMachine
         metadata:
           name: VM_NAME
           namespace: PROJECT
         spec:
           # …
           startupScripts:
           - name: CLEAR_TEXT_SCRIPT_NAME
             script: |
               #!/bin/bash
               CLEAR_TEXT_SCRIPT
           - name: SECRET_SCRIPT_NAME
             scriptSecretRef:
               name: SECRET_NAME
         

These variables are defined as follows:

Variable| Definition | `MANAGEMENT_API_SERVER` | The Management API server kubeconfig file.  
---|---  
`PROJECT` | The Distributed Cloud project in which you want to create the VM.  
`VM_NAME` | The name of the VM.  
`FILE_NAME` | The name of the file to store the startup script.  
`STARTUP_SCRIPT_CONTENT` | The commands to run as part of the startup script  
`CLEAR_TEXT_SCRIPT_NAME` | The name of the clear text startup script.  
`CLEAR_TEXT_SCRIPT` | The clear text script you define.  
`SECRET_NAME` | The name of the Kubernetes secret.  
`SECRET_SCRIPT_NAME` | The name of the startup script as a Kubernetes secret.  
  3. Proceed with the following steps to create a VM.

The following is an example of how to create a VM with startup scripts that adds a new user using a Kubernetes secret and clear text.
         
         kubectl --kubeconfig MANAGEMENT_API_SERVER \
           -n PROJECT \
           apply -f - <<EOF
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
         ---
         apiVersion: v1
         kind: Secret
         type: Opaque
         metadata:
           name: add-user
         data:
           script:
             IyEvYmluL2Jhc2gKYWRkdXNlciB1c2VyCg==
         ---
         apiVersion: virtualmachine.gdc.goog/v1
         kind: VirtualMachine
         metadata:
           name: VM_NAME
         spec:
           compute:
             virtualMachineType: MACHINE_TYPE
           disks:
           - virtualMachineDiskRef:
               name: VM_BOOT_DISK_NAME
             boot: true
             autoDelete: BOOT_DISK_AUTO_DELETE
           startupScripts:
           - name: add-user
             scriptSecretRef:
               name: add-user
           - name: add-to-sudoers
             script: |
               #!/bin/bash
               usermod -aG sudo user
         EOF
         

In the example the variables are defined as follows.

Variable| Definition | `MANAGEMENT_API_SERVER` | The Management API server kubeconfig file.  
---|---  
`PROJECT` | The Distributed Cloud project in which you want to create the VM.  
`VM_NAME` | The name of the new VM.  
`VM_BOOT_DISK_NAME` | The name of the new VM boot disk.  
`BOOT_DISK_IMAGE_NAME` | The name of the image to be used for the new VM boot disk.  
`BOOT_DISK_SIZE` | The size of the boot disk, such as `20G`.  
This value must always be greater than or equal to the `minimumDiskSize` of the boot disk image.  
`BOOT_DISK_AUTO_DELETE` | Either `true` or `false`, indicating whether the boot disk is automatically deleted when the VM instance gets deleted.  
`MACHINE_TYPE` | The predefined machine type for the new VM. To select an available machine type, run this command:  
` kubectl --kubeconfig MANAGEMENT_API_SERVER get virtualmachinetype.virtualmachine.gdc.goog --namespace vm-system `  



## Update an existing VM with a startup script

You can also update an existing VM with a startup script. The VM must be shut down before you perform the update.

Follow the steps to [update VM properties](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/application/ao-user/vms/manage-vms/operations-and-lifecycle/update-vm-properties#update-properties) and update the `spec` field with the startup script that you would like to run.

## View the output of a startup script

  1. Follow the steps to [connect to a VM](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/application/ao-user/vms/connect-to-vm/connect-to-a-vm).
  2. Run the following command inside the guest VM to get the logs of the startup script that you ran:
         
         sudo journalctl -u cloud-final
         

The startup script logs begin with the following:
         
         Started to run the command: /var/lib/google/startup-scripts/<script-name> ...
         




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
