---
url: https://docs.cloud.google.com/anthos/clusters/docs/bare-metal/1.16/vm-runtime/connect-vms/
title: Connect to VMs that use VM Runtime on GDC \u00a0|\u00a0 Google Distributed Cloud Virtual for Bare Metal \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-15T20:47:08.908243+00:00
---

# Connect to VMs that use VM Runtime on GDC  |  Google Distributed Cloud Virtual for Bare Metal  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/anthos/clusters/docs/bare-metal/1.16/vm-runtime/connect-vms/

**Version 1.16**. This version is no longer supported. For information about how to upgrade to version 1.28, see [ Upgrade clusters](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/how-to/upgrade) in the latest documentation. For more information about supported and unsupported versions, see the [Versioning](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/version-history) page in the latest documentation.

  * [ Home ](https://docs.cloud.google.com/)
  * [ Google Distributed Cloud ](https://docs.cloud.google.com/distributed-cloud)
  * [ Documentation ](https://docs.cloud.google.com/kubernetes-engine/enterprise/clusters/docs)
  * [ GDCV for Bare Metal 1.16 ](https://docs.cloud.google.com/anthos/clusters/docs/bare-metal/1.16)
  * [ Guides ](https://docs.cloud.google.com/anthos/clusters/docs/bare-metal/1.16/concepts/about-bare-metal)



Send feedback 

#  Connect to VMs that use VM Runtime on GDC Stay organized with collections  Save and categorize content based on your preferences. 

Version 1.16 keyboard_arrow_down

  * [ Latest ](https://docs.cloud.google.com/anthos/clusters/docs/bare-metal/latest/vm-runtime/connect-vms)
  * [ Version 1.16 ](https://docs.cloud.google.com/anthos/clusters/docs/bare-metal/1.16/vm-runtime/connect-vms)
  * [ Earlier versions (unsupported) ](https://docs.cloud.google.com/anthos/clusters/docs/bare-metal/1.16/getting-support#version-support)



**Preview**

This product or feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA products and features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

This document is intended for application owners that run Google Distributed Cloud. This document shows you how to connect to virtual machines (VMs) that use VM Runtime on GDC. You can connect to VMs directly using an IP address, or using built-in tools for SSH or console access.

## Before you begin

To complete this document, you need access to the following resources:

  * A VM that runs in one of your clusters. If needed, [create a VM in Distributed Cloud](https://docs.cloud.google.com/anthos/clusters/docs/bare-metal/1.16/vm-runtime/quickstart).
  * The `virtctl` client tool installed as a plugin for `kubectl`. If needed, [install the virtctl client tool](https://docs.cloud.google.com/anthos/clusters/docs/bare-metal/1.16/vm-runtime/quickstart#install_the_virtctl_client_tool).



## Configure passwordless SSH access to VMs

Direct, passwordless SSH access to your VM is facilitated by a guest agent that's installed by VM Runtime on GDC. Among other duties, the guest agent installs and expires SSH keys. This capability enables an SSH tunnel for accessing your VM from clients outside the cluster network.

### Enable the guest agent

To enable the guest agent:

**Note:** For Windows guest operating systems, there are additional steps required to start the guest agent, initially. For instructions, see the Windows guest OS tab in Create initial user credentials.

  1. Check your `VirtualMachine` custom resource to confirm it's configured to enable the guest agent:
         
         kubectl get gvm VM_NAME -o yaml --kubeconfig KUBECONFIG
         

The `spec.osType` field should be set to the operating system of your VM, `Linux` or `Windows`. The `spec.guestEnvironment` section shouldn't be explicitly configured as empty. If the section is configured as empty (`guestEnvironment: {}`), you can remove it entirely to enable the guest agent.

Your `VirtualMachine` custom resource for the VM you want to access should look like this:
         
         apiVersion: vm.cluster.gke.io/v1
         kind: VirtualMachine
         metadata:
           name: sample-vm
         spec:
           compute:
             cpu:
               vcpus: 2
             memory:
               capacity: 4Gi
         ...**  osType: Linux**
         ...
         

  2. If necessary, use `kubectl edit` to update the `VirtualMachine` custom resource.

  3. To verify the guest agent is working, check the `status` in your VM custom resource:
         
         kubectl get gvm VM_NAME --kubeconfig KUBECONFIG
         

When the guest agent is working, you see `status: "True"` for the `GuestEnvironmentEnabled` and `GuestEnvironmentDataSynced` conditions.
         
         apiVersion: vm.cluster.gke.io/v1
         kind: VirtualMachine
         metadata:
           ...
           name: vm-sample-01
           ...
         status:
           conditions:
           - lastTransitionTime: "2022-10-05T22:40:26Z"
             message: ""
             observedGeneration: 1
             reason: UserConfiguration**    status: "True"
             type: GuestEnvironmentEnabled**
           - lastTransitionTime: "2022-10-06T21:55:57Z"
             message: ""
             observedGeneration: 1
             reason: GuestEnvironmentDataSynced**    status: "True"
             type: GuestEnvironmentSynced**
           ...
         




### Enable passwordless SSH access

To enable passwordless SSH access for your VM:

  1. Create a `VirtualMachineAccessRequest` manifest file, such as `vm-access-request.yaml`, in the editor of your choice:
         
         apiVersion: vm.cluster.gke.io/v1
         kind: VirtualMachineAccessRequest
         metadata:
           name: VMAR_NAME
           namespace: VM_NAMESPACE
         spec:
           vm: VM_NAME
           user: USERNAME
           ssh:
             key: PUBLIC_SSH_KEY
             ttl: EXPIRATION_TIME
         

Replace the following:

     * `VMAR_NAME`: the name of the access request resource.
     * `VM_NAMESPACE`: the namespace for the VM you want to access.
     * `VM_NAME`: the name of the VM you want to access.
     * `USERNAME`: the username for user who is accessing the VM.
     * `PUBLIC_SSH_KEY`: the public key for SSH access. Typically, this is the contents of the `id_rsa.pub` file.
     * `EXPIRATION_TIME`: the `ttl` (time-to-live) field specifies the how long the SSH key is valid.

For example, if you specify `30m` the SSH key expires after 30 minutes.

This flag uses the following units:

       * `s` for seconds
       * `m` for minutes
       * `h` for hours
       * `d` for days
  2. Use `kubectl apply` to create the `VirtualMachineAccessRequest` from the manifest file. For example, if you named your manifest file `vm-access-request.yaml`,
         
         kubectl apply -f MANIFEST --kubeconfig KUBECONFIG
         

Replace the following:

     * `MANIFEST`: the name of the access request manifest file. For example, `vm-access-request.yaml`.
     * `KUBECONFIG`: the path to the kubeconfig file of the cluster that hosts the VM you are accessing.
  3. To verify that your access request configuration succeeded, check the status of the `VirtualMachineAccessRequest`:
         
         kubectl get vmar VMAR_NAME -o yaml --kubeconfig KUBECONFIG
         

When the configuration is successful, the `status` section includes `state: configured`:
         
         apiVersion: vm.cluster.gke.io/v1
         kind: VirtualMachineAccessRequest
         metadata:
           ...
           annotations:
             kubectl.kubernetes.io/last-applied-configuration: |
               {"apiVersion":"vm.cluster.gke.io/v1","kind":"VirtualMachineAccessRequest",
               "metadata":{"annotations":{},"name":"vmar-sample","namespace":"default"},
               "spec":{"ssh":{"key":"ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABgQ...jMLHFc=
                   sample-user@sample-host","ttl":"5h"},"user":"sample-user","vm":"vm-sample-01"}}
           creationTimestamp: "2022-10-06T21:55:57Z"
           finalizers:
           - vm.cluster.gke.io/vmar-finalizer
           generation: 2
           name: vmar-sample
           namespace: default
           resourceVersion: "13033921"
           uid: 282d72ad-f48d-4e89-af22-336940ac9f58
         spec:
           ssh:
             key: ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABgQ...jMLHFc= sample-user@sample-host
             ttl: 5m0s
           user: sample-user
           vm: vm-sample-01
         status:
           processedAt: "2022-10-06T21:55:57Z"**  state: configured**
         




### Disable the guest agent

When you create a new VM and set the `osType` field, the guest agent is enabled. While this feature is in Preview, you can disable it by editing the `VirtualMachine` custom resource. Disabling the guest agent disables passwordless SSH access to your VM.

**Note:** Features listed as Preview are covered by the [Pre-GA Offerings Terms](https://cloud.google.com/terms/service-terms#1) of the Google Cloud Terms of Service. Pre-GA products and features might have limited support, and changes to pre-GA products and features might not be compatible with other pre-GA versions. For more information, see the [launch stage descriptions](https://cloud.google.com/products#product-launch-stages). Preview offerings are intended for use in test environments only.

To disable the guest agent:

  1. Use `kubectl` to stop your VM before you make changes to the configuration:
         
         kubectl virt stop VM_NAME --kubeconfig KUBECONFIG
         



  1. Edit your VM resource:
         
         kubectl edit gvm VM_NAME --kubeconfig KUBECONFIG
         

  2. Update the `VirtualMachine` configuration to add an empty `spec.guestEnvironment` explicitly:
         
         apiVersion: vm.cluster.gke.io/v1alpha1
         kind: VirtualMachine
         metadata:
           name: vm-example
           namespace: default
         spec:
           compute:
           ...
           osType: Linux**  guestEnvironment: {}**
         

  3. Save and close the updated VM manifest in your editor.

  4. Use `kubectl` to start the VM:
         
         kubectl virt start VM_NAME --kubeconfig KUBECONFIG
         




## Connect using an IP address

If your VM has an accessible IP address and you already have the credentials to access the VM, you can connect using a protocol such as SSH, VNC, or RDP.

### Connect through IP address

If you can connect directly to your VM's IP address, use one of the following methods:

###  SSH 

  1. Get the details of your VM to view its IP address:
         
         kubectl get gvm VM_NAME --namespace VM_NAMESPACE --kubeconfig KUBECONFIG
         

Replace the following values:

     * `VM_NAME`: name for your VM.
     * `VM_NAMESPACE`: the namespace for your VM.

The following example output shows the VM information and IP address:
    
    NAME   STATUS    AGE   IP
    vm1    Running   7m    10.200.0.21
    

  2. Connect to your VM using an SSH client:
         
         ssh USERNAME@IP_ADDRESS -i PATH_TO_KEY
         

Replace the following values:

     * `USERNAME`: the username for an account on your VM.
     * `IP_ADDRESS`: the IP address of your VM obtained in the previous step.
     * `PATH_TO_KEY`: the path to the private SSH key.



###  VNC or RDP 

[Virtual Network Computing (VNC)](https://en.wikipedia.org/wiki/Virtual_Network_Computing) and [Remote Desktop Protocol (RDP)](https://en.wikipedia.org/wiki/Remote_Desktop_Protocol) let you use the graphical console to access your VM. When you use an IP address, you must enable VNC or RDP in the guest OS before you can use either to connect to the VM. For information about enabling and using VNC or RDP, consult the documentation for your guest OS.

You also need existing credentials to sign in to the VM, such as those you define to create initial user credentials when you create a VM.

  1. Get the details of your VM to view its IP address:
         
         kubectl get gvm VM_NAME --namespace VM_NAMESPACE --kubeconfig KUBECONFIG
         

Replace the following values:

     * `VM_NAME`: name for your VM.
     * `VM_NAMESPACE`: the namespace for your VM.

The following example output shows the VM information and IP address:
    
    NAME   STATUS    AGE   IP
    vm1    Running   7m    10.200.0.21
    

  2. Connect to the IP address of your VM obtained in the previous step using a client tool and the appropriate port such as VNC port `5900` or RDP port `3389`.




### Connect through a Service

If your VM connects to the default `pod-network` and you can't communicate directly to the IP address of your VM, expose the VM behind a load balancer `Service`.

  1. Create a `Service` manifest, such as `my-service-load-balancer.yaml`, in the editor of your choice:
         
         nano my-service-load-balancer.yaml
         

  2. Copy and paste the following YAML manifest:
         
         apiVersion: v1
         kind: Service
         metadata:
           name: VM_NAME-service
         spec:
           selector:
             kubevirt/vm: VM_NAME
           ports:
           - name: PORT_NAME
             protocol: PROTOCOL_TYPE
             port: EXTERNAL_PORT
             targetPort: TARGET_PORT
           type: LoadBalancer
         

In this `Service` manifest type, replace the following values:

     * `VM_NAME`: the name for your VM to expose for remote access.
     * `PORT_NAME`: the name of your protocol, such as `ssh`, `vnc`, or `rdp`.
     * `PROTOCOL_TYPE`: the protocol type, such as `tcp` for SSH and RDP, or `udp` for VNC.
     * `EXTERNAL_PORT`: the external port number to expose and that you use to connect to.
     * `TARGET_PORT`: the target port, such as `22` for SSH.
  3. Save and close the `Service` manifest in your editor.

  4. Create the `Service` using `kubectl`:
         
         kubectl apply -f my-service-load-balancer.yaml  --kubeconfig KUBECONFIG
         

  5. Get the `EXTERNAL-IP` address of the load balancer service:
         
         kubectl get service VM_NAME-service --kubeconfig KUBECONFIG
         

The IP address of the load balancer is displayed, as shown in the following example output:
         
         NAME          TYPE           CLUSTER-IP       EXTERNAL-IP   PORT(S)        AGE
         vm1-service   LoadBalancer   172.26.232.167   10.200.0.51   22:31141/TCP   6d20h
         

  6. Connect to the `EXTERNAL-IP` address of the load balancer with a standard protocol, such as using an SSH client:
         
         ssh USERNAME@LOAD_BALANCER_IP_ADDRESS  -i PATH_TO_KEY
         

Replace the following values:

     * `USERNAME`: the username for an account on your VM.
     * `LOAD_BALANCER_IP_ADDRESS`: the IP address of your load balancer.
     * `PATH_TO_KEY`: the path to the private SSH key.



## Connect directly using SSH

If your client is connected to the same physical network as your Anthos cluster on bare metal nodes and you don't require the use of SSH tunnels to connect to the cluster, you can connect using `kubectl virt ssh`.

  1. To use SSH to connect a Linux VM from the console with the `virtctl` add-on:
         
         kubectl virt ssh USERNAME@VM_NAME --namespace VM_NAMESPACE --kubeconfig KUBECONFIG
         

Replace the following values:

     * `USERNAME`: the username to access your VM. This account is created if it doesn't exist on the VM.
     * `VM_NAME`: the name of your VM.
  2. After you have successfully connected using SSH the VM and no longer need the connection, exit the SSH session:
         
         exit
         




## Connect directly using the console

If you don't have direct network connectivity to your Linux VM for SSH access, connect to the console of the VM using the VM Runtime on GDC console. This method opens a serial console. Upon connection, you are given a command prompt, instead of a graphical console.

  1. To access a Linux VM from the console, use the `virtctl` add-on:
         
         kubectl virt console VM_NAME --kubeconfig KUBECONFIG
         

Replace `VM_NAME` with the name of your VM.

When prompted, enter the user credentials for your VM. These credentials must exist on the VM, or be applied when the VM is created. If needed see the following section to create initial user credentials when you create a VM.

  2. After you've successfully connected to the console of the VM and no longer need the connection, exit the VM session and console:
         
         Ctrl + ]
         




## Connect directly using VNC

You can use the `kubectl virt vnc` command to open the Virtual Network Computing (VNC) graphical console to access your VMs. This method works for VMs running either a Windows or a Linux guest OS. When you use the `kubectl virt vnc` command, VM Runtime on GDC opens VNC for you, so you aren't required to enable VNC in the guest OS.

You need existing credentials to sign in to the VM, such as those you define to create initial user credentials when you create a VM.

  1. To access a VM using VNC, use the `virtctl` add-on:
         
         kubectl virt vnc VM_NAME --kubeconfig KUBECONFIG
         

Replace `VM_NAME` with the name of your VM.

When prompted, enter the user credentials for your VM.

  2. After you've successfully connected to the VNC session of the VM and no longer need the connection, log off from the VM to close the VNC connection.




## Create initial user credentials

When you connect to your VM using the console, you must specify user credentials. The process for creating initial user credentials differs for Linux and Windows guest operating systems.

###  Linux guest OS 

For Linux VMs, user credentials can be built in to your custom images, or can be specified when you create a VM.

  * Use the `--configure-initial-password` parameter with `kubectl virt create` command:
        
        kubectl virt create vm VM_NAME \
            --image ubuntu20.04 \
            --os-type Linux \
            --configure-initial-password USERNAME:PASSWORD \
            --kubeconfig KUBECONFIG
        

Replace the following values:

    * `VM_NAME`: name for your VM.
    * `USERNAME`: username for the account to create on the VM.
    * `PASSWORD`: password for the user account.

This example command creates a Linux VM that runs Ubuntu 20.04. It's recommended that you change the initial credentials after you first sign in to the VM.


**Note:** To change credentials on an existing VM, connect to the VM using `kubectl virt console VM_NAME` and then update the credentials within the guest OS.

###  Windows guest OS 

Use the following steps to reset a password for an existing user or create the initial password for a new user:

  1. Enable the guest agent in your Windows VM:

     1. Configure the VM to enable the guest agent.

     2. Use VNC or RDP to connect to the VM.

     3. In the VM, navigate to the `guest agent` drive. In most cases, this is drive `E:`.

     4. Use PowerShell to run `install.ps1`.

This installs and starts the guest agent. The guest agent starts automatically for subsequent VM reboots.

     5. Close the remote session.

  2. On your admin workstation, use the following command to reset (or set if you use a new username) the Windows VM password:
         
         kubectl virt reset-windows-password VM_NAME \
             --user=USERNAME \
             --namespace=VM_NAMESPACE
         

Replace the following:

     * `VM_NAME`: the name of the VM.
     * `USERNAME`: the username you want to reset (or set) the password for. If the username is new, the command creates a new Windows account and sets the initial password.
     * `VM_NAMESPACE`: (Optional) the namespace of the VM. This flag is optional. If not specified, the default namespace, `default`, is used.

To reset (or set) password without a confirmation prompt, use the optional `--force` flag. When you use the `--force` flag, the prompt warns you of the consequences of resetting the password for an existing account. Without the `--force` flag, the command prompts you to confirm the password reset with the following text:
    
    This command creates an account and sets an initial password for the
    user USERNAME if the account does not already exist.
    If the account already exists, resetting the password can cause the
    LOSS OF ENCRYPTED DATA secured with the current password, including
    files and stored passwords.
    
    Would you like to set or reset the password for USERNAME (Y/n)?
    

After you confirm (or force) the password reset, the command returns the new password for the specified VM and username:
    
    Resetting and retrieving password for USERNAME on VM_NAME
    
    vm_name:    VM_NAME
    username:   USERNAME
    password:   PASSWORD
    




## What's next

  * [Manage the power state of a VM in Distributed Cloud](https://docs.cloud.google.com/anthos/clusters/docs/bare-metal/1.16/vm-runtime/manage-power-state).
  * [Edit a VM in Distributed Cloud](https://docs.cloud.google.com/anthos/clusters/docs/bare-metal/1.16/vm-runtime/edit-vm).
  * [View VM console logs in Distributed Cloud](https://docs.cloud.google.com/anthos/clusters/docs/bare-metal/1.16/vm-runtime/view-console-logs).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
