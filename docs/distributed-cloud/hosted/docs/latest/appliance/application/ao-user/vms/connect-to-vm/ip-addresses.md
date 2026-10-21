---
url: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/application/ao-user/vms/connect-to-vm/ip-addresses/
title: Enable IP addresses \u00a0|\u00a0 Google Distributed Cloud Hosted Appliance \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T19:22:06.492954+00:00
---

# Enable IP addresses  |  Google Distributed Cloud Hosted Appliance  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/application/ao-user/vms/connect-to-vm/ip-addresses/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Distributed, hybrid, and multicloud ](https://docs.cloud.google.com/docs/dhm-cloud)
  * [ Google Distributed Cloud ](https://docs.cloud.google.com/distributed-cloud/docs)
  * [ Air-gapped ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdch)
  * [ Appliance ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance)
  * [ 1.0.7 ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance)



Send feedback 

#  Enable IP addresses Stay organized with collections  Save and categorize content based on your preferences. 

You can enable any virtual machine (VM) instance to be reachable from either the external network or another organization, known as VM Ingress. A VM workload in an organization project can reach either the external network or the current VM being exposed to services in other organizations, known as VM Egress.

You can use `VirtualMachineExternalAccess` (VMEA) to control VM Ingress and VM Egress together. You can find both the ingress and egress IP addresses that you have enabled for a VM instance on the Google Distributed Cloud (GDC) air-gapped appliance VMM API or through the GDC console.

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

## Configure VM External Access

`VirtualMachineExternalAccess` (VMEA) controls VM Ingress and VM Egress. VMEA cannot control VM Ingress and VM Egress separately. The ingress and egress of a VM must be enabled or disabled together at the same time.

You can configure and control VMEA either from UI or from GDC air-gapped appliance VMM API. A VM can only have a single VMEA. If a VM does not have a VMEA, both the ingress and egress is disabled by default.

### Enable external access

To enable a VM with external access for data transfer in and data transfer out, you can configure the VMEA from GDC console or the GDC air-gapped appliance [Virtual Machine Manager API](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/apis/service/virtualmachine/vmm-api-overview).

By default, the intra-project network traffic is allowed, and you can directly access your VM inside the project. A **network policy** blocks all ingress traffic to the VM from outside the project. You must manually create a new network policy to let your source IP address to access the VM through data transfer in. This network policy can either be a [cross-project traffic network policy](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/application/ao-user/vms/connect-to-vm/network-policy#cross-project-traffic) or a [cross-organization traffic network policy](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/application/ao-user/vms/connect-to-vm/network-policy#cross-org-traffic). The location depends on what you want to access the VM from.

You can enable and disable the external access of a VM by specifying `true` or `false` in the `enabled` field of the VMEA spec. For VM Ingress, you can configure data transfer in ports by specifying the name, protocol and port number for each port you want to add in the `ports` field of VMEA spec.

To enable external access of a VM by creating a new VMEA, complete the following:

###  Console 

  1. During the VM creation process using the Console, navigate to the **Network details** page from the **Create VM instance** page.
  2. Locate **Network** in the vertical navigation menu of the page.
  3. Check **Allow external access** to enable external access on the VM.

**Note:** You cannot change external access status once you've created a VM.

![Enable external access on VM creation](https://docs.cloud.google.com/static/distributed-cloud/hosted/docs/latest/appliance/application/ao-user/vms/images/vm-console-allow-external-access.png)

###  API 

Run the following command:
    
    
    kubectl --kubeconfig MANAGEMENT_API_SERVER apply -n PROJECT -f - <<EOF
    apiVersion: virtualmachine.gdc.goog/v1
    kind: VirtualMachineExternalAccess
    metadata:
       name: VM_NAME
    spec:
       enabled: true
       ports:
         - name: PORT_NAME
           protocol: PROTOCOL
           port: PORT_NUMBER
    EOF
    

Replace the following variables:

  * MANAGEMENT_API_SERVER: the kubeconfig file to the Management API server.
  * VM_NAME: the name of your VM.
  * PORT_NAME: the port name.
  * PROTOCOL: the protocol you want the ingress service to use. The protocol name must be capitalized and a Kubernetes supported protocol, such as `TCP`, `UDP`, or `SCTP`.
  * PORT_NUMBER: the port number.

**Note:** Update `enabled` field to `true`.

To enable external access of a VM by editing an existing VMEA through the VMM API, run the following:
    
    
    kubectl --kubeconfig MANAGEMENT_API_SERVER edit virtualmachineexternalaccesses.virtualmachine.gdc.goog VM_NAME -n PROJECT
    

### Disable external access

If a VM does not have a corresponding VMEA, both of the ingress and egress are disabled. If a VM has a corresponding VMEA, you can disable the VMEA by either setting the `enabled` field to `false` or directly deleting the VMEA. You can do these operations through the GDC air-gapped appliance VMM API.

To disable external access, complete the following steps:

###  API 

Disable external access by deleting a VMEA:
    
    
    kubectl --kubeconfig MANAGEMENT_API_SERVER delete virtualmachineexternalaccesses.virtualmachine.gdc.goog VM_NAME -n PROJECT
    

Replace the following:

  * MANAGEMENT_API_SERVER: the kubeconfig file to the Management API server.
  * VM_NAME: the name of the VM.
  * PROJECT: the GDC air-gapped appliance project where the VM resides.



Disable external access by editing a VMEA:
    
    
    kubectl --kubeconfig MANAGEMENT_API_SERVER edit virtualmachineexternalaccesses.virtualmachine.gdc.goog VM_NAME -n PROJECT
    

Update the `enabled` field to `false`.

### Ingress

#### View Ingress IP addresses

If a VM is enabled with Ingress, an ingress IP address shows on the GDC console after creation. You can also find this ingress IP address from the **VM details** page in the GDC console.

To fetch the IP address, use the GDC air-gapped appliance VMM API. Complete the following:

###  API 

Fetch the IP address:
    
    
    kubectl --kubeconfig MANAGEMENT_API_SERVER get virtualmachineexternalaccesses.virtualmachine.gdc.goog VM_NAME -n PROJECT -ojsonpath='{.status.ingressIP}'
    

For a VM with a different operating system (OS), use the `ssh` command to enter the VM with the ingress IP address with the port you have enabled with TCP.

#### Edit Ingress

After you enable VMEA for a VM, you can customize the ingress by editing the VMEA. You can directly edit the spec of the VM ingress from the GDC console. You can also use the `kubectl` CLI to edit the VM ingress from the spec of the VMEA.

To edit the VMEA to customize the ingress, complete the following:

For example, use following commands to add port PORT_NUMBER on an existing VM ingress using TCP protocol:

###  Console 

Directly edit the ports on the VM Ingress service from the GDC console:

  1. In the vertical navigation menu, click **Instances**.
  2. On the page, scroll to **Network details**.
  3. Click the edit icon on **Ingress Ports** to edit the ingress port.

![Console UI showing Network details list with edit icon on Ingress Ports](https://docs.cloud.google.com/static/distributed-cloud/hosted/docs/latest/appliance/application/ao-user/vms/images/vm-console-edit-ingress.png)




###  API 
    
    
    kubectl --kubeconfig MANAGEMENT_API_SERVER patch virtualmachineexternalaccesses.virtualmachine.gdc.goog VM_NAME -n PROJECT --type "json" -p '[{"op":"add","path":"/spec/ports/-","value": {"name":"PORT_NAME","port":PORT_NUMBER, "Protocol":"TCP"}}]'
    

Replace the following:

  * MANAGEMENT_API_SERVER: the kubeconfig file to the Management API server.
  * VM_NAME: the name of the VM.
  * PROJECT: the GDC air-gapped appliance project where the VM resides.
  * PORT_NAME: the name of the port to add.
  * PORT_NUMBER: the port number.



#### Enable Ingress with non-TCP protocol

GDC air-gapped appliance lets you enable your VM Ingress with different protocols. By default, a VM Ingress service uses TCP protocol. You can add your own non-TCP protocol ingress for your VM. GDC air-gapped appliance supports the following protocols:

  * Transmission control protocol (TCP).
  * User datagram protocol (UDP).
  * Stream control transmission protocol (SCTP).



You can enable data transfer in with non-TCP protocol by specifying different protocol names when creating VMEA.

**Note:** In prior GDC air-gapped appliance versions, you can create multiple ingresses with different IP addresses. In versions after 1.11, you can only have one VM Ingress with a single IP address.

### Egress

A VM workload in an organization project can reach the external network, or be exposed to services in other organizations. If you enable data transfer out for the VM, you see an egress IP address generated. The VM connects to the external services with this IP address.

To make this IP address data transfer out of the external network, you might need to apply project network policies. For more information, refer to [Egress cross-organization traffic network policy](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/application/ao-user/vms/connect-to-vm/network-policy#egress-network-policy-crossorg).

#### View Egress IP address

If a VM is enabled with Egress, an egress IP address shows on the GDC console after creation. You can also find this egress IP address from the **VM details** page.

To view the egress IP address, complete the following:

###  API 

Fetch the IP address:
    
    
    kubectl --kubeconfig MANAGEMENT_API_SERVER get virtualmachineexternalaccesses.virtualmachine.gdc.goog VM_NAME -n PROJECT -ojsonpath='{.status.egressIP}'
    

Replace the following:

  * MANAGEMENT_API_SERVER: the kubeconfig file to the Management API server.
  * VM_NAME: the name of the VM.
  * PROJECT: the GDC air-gapped appliance project where the VM resides.



VM Egress is based on a project. VMs within the same project contain the same Egress IP address.

#### Control Egress

In previous GDC air-gapped appliance versions, you had to reboot the VM to reflect egress changes to a running VM. In version 1.11, you can enable and disable the VM egress without rebooting the VM. This change takes effect right after you update the VMEA. 

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
