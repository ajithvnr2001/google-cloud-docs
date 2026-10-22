---
url: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/application/ao-user/vms/connect-to-vm/connect-to-a-vm/
title: Connect to a VM \u00a0|\u00a0 Google Distributed Cloud Hosted Appliance \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:15:37.774781+00:00
---

# Connect to a VM  |  Google Distributed Cloud Hosted Appliance  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/application/ao-user/vms/connect-to-vm/connect-to-a-vm/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Distributed, hybrid, and multicloud ](https://docs.cloud.google.com/docs/dhm-cloud)
  * [ Google Distributed Cloud ](https://docs.cloud.google.com/distributed-cloud/docs)
  * [ Air-gapped ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdch)
  * [ Appliance ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance)
  * [ 1.0.7 ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance)



Send feedback 

#  Connect to a VM Stay organized with collections  Save and categorize content based on your preferences. 

Google Distributed Cloud (GDC) air-gapped appliance uses key-based SSH authentication to establish connections to virtual machine (VM) instances. By default, passwords aren't configured for local users on VMs with an operating system (OS).

## Before you begin

Before connecting to a VM, you must meet the following prerequisites:

  * [Enable access management](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/application/ao-user/vms/manage-the-os/guest-environment). You _cannot_ proceed without access management enabled on the guest environment. By default, access management is enabled on new VMs.
  * [Enable VM external access](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/application/ao-user/vms/connect-to-vm/ip-addresses) for any peer on Transmission Control Protocol (TCP) port 22. 


* [Set up a `ProjectNetworkPolicy`](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/application/ao-user/vms/connect-to-vm/network-policy) (PNP) custom resource in the project where the VM resides. 

  * By setting up a PNP in the project, you can access the VM outside of the project or organization.
  * To diagnose if you don't have a PNP, ask your Infrastructure Operator (IO).


* Login access to the cluster. Follow the CLI steps in [Sign in](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/application/ao-user/iam/sign-in#cli) to log in to the cluster.

To use `gdcloud` command-line interface (CLI) commands, ensure that you have downloaded, installed, and configured the [`gdcloud` CLI](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/resources/gdcloud-overview). All commands for GDC air-gapped appliance use the `gdcloud` or `kubectl` CLI, and require an operating system (OS) environment.

### Get the kubeconfig file path

To run commands against the Management API server, ensure you have the following resources:

  1. Locate the Management API server name, or ask your Platform Administrator (PA) what the server name is.

  2. [Sign in and generate](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/application/ao-user/iam/sign-in#cli) the kubeconfig file for the Management API server if you don't have one.

  3. Use the path to replace `MANAGEMENT_API_SERVER{"</var>"}}` in these instructions.




### Request permissions and access

To perform the tasks listed in this page, you must have the Project VirtualMachine Admin role. Follow the steps to either [verify](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/application/ao-user/vms/preparation#verify-user-access) or have your Project IAM Admin [assign](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/application/ao-user/vms/preparation#grant-user-access-vm-resources) you the Project VirtualMachine Admin (`project-vm-admin`) role in the namespace of the project where the VM resides.

For VM operations using the GDC console or the gdcloud CLI, request your Project IAM Admin to assign you both the Project VirtualMachine Admin role and the Project Viewer (`project-viewer`) role.

## Establish a VM connection

This section describes how to establish a connection to a VM with a specific operating system (OS).

### Connect to a VM

To establish a connection to a VM with a specific OS, use the GDC console, gdcloud CLI, or the [Virtual Machine Manager API](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/apis/service/virtualmachine/vmm-api-overview).

### Console

  1. In the navigation menu, click **Virtual Machines > Instances**.

  2. In the list of VMs, find the row for the running VM that you want to connect to. In the **Connect** column, click **SSH**.

  3. An SSH browser terminal opens. Enter any command in the shell or click **FTP** to navigate the file structure and upload files.




###  gdcloud 

Connect to a VM using SSH by running the [`gdcloud compute ssh` command](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/resources/gdcloud-reference/gdcloud-compute-ssh)
    
    
    gdcloud compute ssh VM_NAME --project=PROJECT_ID
    

Replace the following variables:

  * VM_NAME: the name of the VM.
  * PROJECT_ID: the ID of the project that contains the VM.



If you have [set default properties](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/resources/gdcloud-manage-properties#set-properties) for the CLI, you can omit the `--project` flag from this command. For example:
    
    
    gdcloud compute ssh VM_NAME
    

###  API 

Connect to a VM:

  * Open a terminal.
  * Create an SSH key pair.
  * Upload the public key and username with a time-to-live (TTL) value.



GDC retrieves the SSH key and username and creates a user account with the username. On VMs, GDC stores the public key in your user's `~/.ssh/authorized_keys` file on the VM.

Complete the following steps to connect to a VM from the command line:

  1. Create an SSH key pair and a username.

On OS workstations, use the `ssh-keygen` utility to create a new SSH key pair. The following code sample creates an RSA (Rivest–Shamir–Adleman) key pair:
         
         ssh-keygen -t rsa -f ~/.ssh/KEY_FILENAME -C USERNAME -b 2048
         

Replace the variables by using the following definitions.

Variable| Definition | `KEY_FILENAME` | The name for your SSH key file. For example, the `my-ssh-key` filename generates a private key file named `my-ssh-key` and a public key file named `my-ssh-key.pub`.  
---|---  
`USERNAME` | Your username on the VM, such as `testuser` or `testuser_gmail_com`.  
  
The `ssh-keygen` utility saves your private key file in the `~/.ssh/KEY_FILENAME` path and your public key file in the `~/.ssh/KEY_FILENAME.pub` path.

A public key for the user, `testuser`, is similar to the following example:
         
         ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABAQDAu5kKQCPF... testuser
         

  2. Upload your key to the VM and create a Kubernetes resource with your public key, username, and time to live (TTL) value for the key.

The following example uses an `access_request.yaml` file to grant access to the VM instance with the `KEY_FILENAME` private key and a TTL value of ten minutes:
         
         apiVersion: virtualmachine.gdc.goog/v1
         kind: VirtualMachineAccessRequest
         metadata:
           namespace: VM_NAMESPACE
           name: AR_NAME
         spec:
           ssh:
             key: |
               ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABAQDAu5kKQCPF... cloudysanfrancisco
             ttl: 10m
           user: USERNAME
           vm: VM_NAME
         

Replace the variables, using the following definitions:

Variable| Definition | `VM_NAMESPACE` | The namespace for the VM.  
---|---  
`AR_NAME` | The access request name.  
`USERNAME` | Your username on the VM, such as `testuser` or `testuser_gmail_com`.  
`VM_NAME` | The name of the VM instance.  
**Important:** After reaching the TTL value of ten minutes, the VM denies future connections with that key unless you add it again.
  3. Create the key:
         
         kubectl create -f access_request.yaml --kubeconfig MANAGEMENT_API_SERVER
         

  4. Check the status of your access request:
         
         kubectl get virtualmachineaccessrequests.virtualmachine.gdc.goog -n VM_NAMESPACE --kubeconfig MANAGEMENT_API_SERVER
         

Replace `VM_NAMESPACE` with the namespace for the VM.

A `configured` status indicates that you can connect to the VM.

  5. Connect to the VM:
         
         ssh -i PATH_TO_PRIVATE_KEY USERNAME@EXTERNAL_IP
         

Replace the following values:

     * `PATH_TO_PRIVATE_KEY` with the path to the private SSH key file that corresponds to the public key you added to the VM.
     * `USERNAME` with the username that you specified when you created the SSH key. For example, `cloudysanfrancisco_example_com` or `cloudysanfrancisco`.
     * `EXTERNAL_IP` with the external [ingress IP address](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/application/ao-user/vms/connect-to-vm/ip-addresses) of the VM.



### Troubleshooting

This section describes how to troubleshoot issues that might occur while connecting to a VM instance after creating the access request.

Work through the following steps to identify possible issues:

  1. Verify that the VM is running. Replace the editable variables with your values in the following command:
         
         kubectl get virtualmachines.virtualmachine.gdc.goog VM_NAME -n VM_NAMESPACE --kubeconfig MANAGEMENT_API_SERVER
         

If the VM is not running, you cannot connect or configure new requests.

  2. Verify that the VM has been running for a few minutes. If the VM has just started, the required services for SSH access might not be running yet. Typically, they run within five minutes of the boot.

  3. Verify that you didn't exceed the TTL value on the access request. The key is removed after time reaches the TTL value.

  4. If your `VirtualMachineAccessRequest` shows a `configured` status, verify the following requirements:

     1. You [enabled data transfer in](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/application/ao-user/vms/connect-to-vm/ip-addresses) to your VM on port 22.
     2. Your machine routes to the VM. For example, you can use the  
`curl -vso /dev/null --connect-timeout 5 EXTERNAL_IP:22` command to check routing.
  5. If your `VirtualMachineAccessRequest` shows a `failed` status, view the complete status and review the error message indicating what caused the request to fail:
         
         kubectl describe virtualmachineaccessrequest.virtualmachine.gdc.goog AR_NAME -n VM_NAMESPACE --kubeconfig MANAGEMENT_API_SERVER
         

Replace the editable variables in the preceding command with your own values.

  6. If the status of your `VirtualMachineAccessRequest` is blank, the guest environment might not be running.




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
