---
url: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/application/ao-user/vms/manage-the-os/windows-startup-script/
title: Use a startup script on Windows VMs \u00a0|\u00a0 Google Distributed Cloud air-gapped \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T10:25:14.428806+00:00
---

# Use a startup script on Windows VMs  |  Google Distributed Cloud air-gapped  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/application/ao-user/vms/manage-the-os/windows-startup-script/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Distributed, hybrid, and multicloud ](https://docs.cloud.google.com/docs/dhm-cloud)
  * [ Google Distributed Cloud ](https://docs.cloud.google.com/distributed-cloud/docs)
  * [ Air-gapped ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdch)
  * [ 1.16.2 (Latest) ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag)



Send feedback 

#  Use a startup script on Windows VMs Stay organized with collections  Save and categorize content based on your preferences. 

A startup script performs tasks during the start-up process for a virtual machine (VM). This document provides you with the steps to follow for using startup scripts on VM instances. 

A startup script is an automation tool that performs tasks during the VM start-up process. Use startup scripts to automate VM configuration and deployment tasks on new or existing instances, saving you time and reducing manual configuration effort.

This document is for developers in platform administrator or application operator groups that want to use startup scripts for VMs in a Distributed Cloud environment. For more information, see [Audiences for GDC air-gapped documentation](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/resources/audiences).

## Before you begin

To use `gdcloud` command-line interface (CLI) commands, ensure that you have downloaded, installed, and configured the [`gdcloud` CLI](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/resources/gdcloud-overview). All commands for Distributed Cloud use the `gdcloud` or `kubectl` CLI, and require an operating system (OS) environment.

### Get the kubeconfig file path

To run commands against the Management API server, ensure you have the following resources:

  1. [Sign in and generate](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/application/ao-user/iam/sign-in#cli) the kubeconfig file for the Management API server if you don't have one.

  2. Use the path to the kubeconfig file of the Management API server to replace `MANAGEMENT_API_SERVER` in these instructions.




### Request IAM roles

To use startup scripts for a VM, contact your IAM Project Admin to request the following roles on your project:

  * **Virtual Machine Project Admin** (`project-vm-admin`): create, modify, list, and delete VMs in the project namespace.

  * **Secret Admin** (`secret-admin`): get, list, create, update, delete, patch, and watch Kubernetes secrets in the project namespace. Use this role to specify startup script secrets. You don't need this role to specify plain text startup scripts.




All VM roles must bind to the namespace of the project where the VM resides. Follow the steps to [verify](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/application/ao-user/vms/preparation#verify-user-access) your access.

## Format Windows startup script names

Startup scripts for Windows VMs must follow a specific naming format with the script name and the file extension appended, separated by dashes. For example, `create-directory-ps1`, with `create-directory` as the script name and `ps1` as the file extension. Incorrect formats include using periods in place of dashes and omitting the file extension, such as `create-directory.ps1` and `create-directory`.

The following shows the file extensions to use for Windows startup scripts:

  * **`ps1`** : Contains PowerShell commands.
  * **`cmd`** : Contains batch commands for the Command Prompt interpreter.
  * **`bat`** : Contains batch commands.



## Run Windows startup scripts in order

You can use multiple startup scripts. The type of file containing the script impacts the order of running each script. The following table shows the order of running Windows startup scripts:

Windows script | Order to run  
---|---  
Powershell script | First on every boot.  
Batch script | Second on every boot.  
Command script | Third on every boot.  
  
If two startup scripts have the same file extension, the scripts are run based on the file extension and name in alphabetical order. For example, if your startup script names are `alpha-script-ps1` and `beta-script-ps1`, `alpha-script-ps1` runs before `beta-script-ps1`.

The following example VM specification shows the Windows startup script order and structure in the `startupScripts` field:
    
    
    # …
      startupScripts:
      - name: create-directory-ps1
        script: |-
          New-Item -ItemType Directory -Path C:\ -Name NewDir
          Get-ChildItem -Path C:\
      - name: hello-world-bat
        script: |-
          ECHO "Hello World!"
      - name: list-directories-cmd
        script: |-
          dir C:\Windows  > files.txt
    # …
    

## Pass a startup script

Distributed Cloud runs startup scripts in alphabetical order, based on the name of each startup script.

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
      name: "vm-test"
    spec:
      # …
      startupScripts:
      - name: create-directory-ps1
        script: |-
          New-Item -ItemType Directory -Path C:\ -Name NewDir
          Get-ChildItem -Path C:\
      - name: list-directories-cmd
        scriptSecretRef:
          name: list-directories
    ---
    apiVersion: v1
    kind: Secret
    type: Opaque
    metadata:
      name: list-directories
    data:
      script:
        ZGlyIEM6XFdpbmRvd3MgID4gZmlsZXMudHh0Cg==
    

Review the following considerations:

  * The startup script runs on _every boot_.
  * The startup script has default root privileges.
  * In the Kubernetes secret, the name of the `scriptSecretRef` in the VM `spec` must match the `metadata.name` field.
  * In the Kubernetes secret, specify the startup script content by adding a key `script` to the `data` field.



## Create a new VM with a Windows startup script

To create a VM with a Windows startup script, follow the steps in [Create a new VM with a startup script](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/application/ao-user/vms/manage-the-os/startup-script-vm-instance#create-new-vm-startup-script).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-21 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-21 UTC."],[],[]] 
