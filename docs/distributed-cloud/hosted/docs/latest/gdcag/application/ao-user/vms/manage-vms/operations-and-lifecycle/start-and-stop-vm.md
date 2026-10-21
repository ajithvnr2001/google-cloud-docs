---
url: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/application/ao-user/vms/manage-vms/operations-and-lifecycle/start-and-stop-vm/
title: Start and stop a VM \u00a0|\u00a0 Google Distributed Cloud air-gapped \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-15T03:43:14.002705+00:00
---

# Start and stop a VM  |  Google Distributed Cloud air-gapped  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/application/ao-user/vms/manage-vms/operations-and-lifecycle/start-and-stop-vm/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Distributed, hybrid, and multicloud ](https://docs.cloud.google.com/docs/dhm-cloud)
  * [ Google Distributed Cloud ](https://docs.cloud.google.com/distributed-cloud/docs)
  * [ Air-gapped ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdch)
  * [ 1.16.2 (Latest) ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag)



Send feedback 

#  Start and stop a VM Stay organized with collections  Save and categorize content based on your preferences. 

This document explains how to start, stop and restart a virtual machine (VM) instance in Google Distributed Cloud (GDC) air-gapped.

You can stop, start, and restart VMs to support the lifecycle of your applications. For example, you might want to change the number of assigned virtual centralized processing units (vCPUs) or the amount of memory allocated to a VM. You must stop the VM before you edit the configuration. After you finish, you must cycle the power state to apply the changes.

This document is for developers in platform administrator or application operator groups that need to start, stop and restart VM instances in a Distributed Cloud environment. For more information, see [Audiences for GDC air-gapped documentation](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/resources/audiences).

## Before you begin

To use `gdcloud` command-line interface (CLI) commands, ensure that you have downloaded, installed, and configured the [`gdcloud` CLI](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/resources/gdcloud-overview). All commands for Distributed Cloud use the `gdcloud` or `kubectl` CLI, and require an operating system (OS) environment.

### Get the kubeconfig file path

To run commands against the Management API server, ensure you have the following resources:

  1. [Sign in and generate](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/application/ao-user/iam/sign-in#cli) the kubeconfig file for the Management API server if you don't have one.

  2. Use the path to the kubeconfig file of the Management API server to replace `MANAGEMENT_API_SERVER` in these instructions.




If you want to minimize your VM start up time, follow the directions in [Minimize the VM start time ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/application/ao-user/vms/manage-vms/operations-and-lifecycle/minimize-vm-start) before you start your VM.

### Request IAM roles

Contact your Project IAM Admin to request the following roles on your project:

  * **Virtual Machine Project Admin** (`project-vm-admin`): create, modify, list, and delete VMs in the project namespace.

  * **Project Viewer**(`project-viewer`): view all resources within the project namespaces.




All VM roles must bind to the namespace of the project where the VM resides. Follow the steps to [verify](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/application/ao-user/vms/preparation#verify-user-access) your access.

## Stop a VM

When you stop a virtual machine (VM), the hypervisor deallocates all resources associated with the instance. The VM is shut down.

Stop a VM that's in a running state by using the GDC console or `kubectl`.

###  Console 

  1. In the navigation menu, click **Virtual Machines > Instances**.

  2. In the list of VMs, select the checkbox for the running VM that you want to stop.

  3. Click **Stop**.

  4. In the confirmation dialog, click **Stop**.




###  gdcloud 

To stop a VM:
    
    
    gdcloud compute instances stop VM_NAME \
      --project PROJECT
    

  * Replace `VM_NAME` with the name of the VM.
  * Replace `PROJECT` with the name of the GDC project in which the VM lives.



###  kubectl 

  1. Run the following command:
         
         kubectl --kubeconfig MANAGEMENT_API_SERVER_KUBECONFIG \
            -n PROJECT \
            edit virtualmachines.virtualmachine.gdc.goog VM_NAME
         

  2. Look for the field `runningState` in the `spec` of the VM and change the value of the field to `Stopped`. If `runningState` is not in the `spec` add `runningState` to the `spec` and set the value to `Stopped`.
         
         spec:
            runningState: Stopped
         

  3. Verify the status of the VM:
         
         kubectl --kubeconfig MANAGEMENT_API_SERVER_KUBECONFIG \
            -n PROJECT \
            get virtualmachines.virtualmachine.gdc.goog VM_NAME
         

Use these definitions for the preceding variables.

Variable| Definition  
---|---  
`MANAGEMENT_API_SERVER_KUBECONFIG`| The Management API server kubeconfig file.  
`VM_NAME`| The VM's name.  
`PROJECT`| The VM's project name.  



## Start a VM

Start a VM from a stopped state by using the console or `kubectl`.

###  Console 

  1. In the navigation menu, click **Virtual Machines > Instances**.

  2. In the list of VMs, select the checkbox for the stopped VM that you want to start.

  3. Click **Start**.

  4. In the confirmation dialog, click **Start**.




###  gdcloud 

To start a VM:
    
    
    gdcloud compute instances start VM_NAME --project PROJECT
    

  * Replace `VM_NAME` with the name of the VM.
  * Replace `PROJECT` with the name of the GDC project in which the VM lives.



###  kubectl 

  1. Run the following command:
         
         kubectl --kubeconfig MANAGEMENT_API_SERVER_KUBECONFIG \
           -n PROJECT \
           edit virtualmachines.virtualmachine.gdc.goog VM_NAME
         

  2. Look for the field `runningState` in the `spec` of the VM and change the value of the field to `Running`.
         
         spec:
            runningState: Running
         

  3. Verify the VM status:
         
         kubectl --kubeconfig MANAGEMENT_API_SERVER_KUBECONFIG \
           -n PROJECT \
           get virtualmachines.virtualmachine.gdc.goog VM_NAME
         

Use these definitions for the variables in the example code.

Variable| Definition  
---|---  
`MANAGEMENT_API_SERVER_KUBECONFIG`| The Management API server kubeconfig file.  
`MANAGEMENT_API_SERVER_NAME`| The name of the Management API server.  
`VM_NAME`| The VM's name.  
`PROJECT`| The VM's project name.  



## Restart a VM

When you restart a VM, the machine resets to its initial state and the memory contents of the machine are wiped.

Restart a VM that is in a running state by using the console or `kubectl`.

###  Console 

  1. In the navigation menu, click **Virtual Machines > Instances**.

  2. In the list of VMs, select the checkbox for the running VM that you want to restart.

  3. Click **Reset**.

  4. In the confirmation dialog, click **Reset**.




###  gdcloud 

To reset a VM:
    
    
    gdcloud compute instances reset VM_NAME --project PROJECT
    

  * Replace `VM_NAME` with the name of the VM.
  * Replace `PROJECT` with the name of the GDC project in which the VM lives.



###  kubectl 

  1. Start a local proxy to the Management API server:
         
         kubectl --kubeconfig MANAGEMENT_API_SERVER_KUBECONFIG proxy --port=8001 &
         PROXY_PID=$!
         

Replace `MANAGEMENT_API_SERVER_KUBECONFIG` with the Management API server kubeconfig file.

  2. Make an API request to restart the VM through the proxy:
         
         curl -s -i -X PUT \
           http://127.0.0.1:8001/apis/virtualmachineoperations.gdc.goog/v1/namespaces/PROJECT/virtualmachines/VM_NAME/restart | head -n 1
         

     * Replace VM_NAME with the name of the VM.
     * Replace PROJECT with the name of the GDC project in which the VM lives.

A successful request returns `HTTP/1.1 202 Accepted`.

  3. Stop the proxy:
         
         kill $PROXY_PID
         

  4. Verify the VM status:
         
         kubectl --kubeconfig MANAGEMENT_API_SERVER_KUBECONFIG \
           -n PROJECT \
           get virtualmachines.virtualmachine.gdc.goog VM_NAME
         




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
