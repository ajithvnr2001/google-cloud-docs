---
url: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/application/ao-user/vms/connect-to-vm/ip-addresses/
title: Enable IP addresses \u00a0|\u00a0 Google Distributed Cloud air-gapped \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:08:25.642754+00:00
---

# Enable IP addresses  |  Google Distributed Cloud air-gapped  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/application/ao-user/vms/connect-to-vm/ip-addresses/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Distributed, hybrid, and multicloud ](https://docs.cloud.google.com/docs/dhm-cloud)
  * [ Google Distributed Cloud ](https://docs.cloud.google.com/distributed-cloud/docs)
  * [ Air-gapped ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdch)
  * [ 1.16.2 (Latest) ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag)



Send feedback 

#  Enable IP addresses Stay organized with collections  Save and categorize content based on your preferences. 

This document explains how to configure IP addresses on a virtual machine (VM) instance in Google Distributed Cloud (GDC) air-gapped.

You can enable any virtual machine (VM) instance to be reachable from either the external network or another organization, known as VM Ingress. A VM workload in an organization project can reach either the external network or the current VM being exposed to services in other organizations, known as VM Egress.

You can control VM ingress and egress using one of the following approaches:

  * **External Load Balancer and Cloud NAT gateway (preferred)** : [Create an External Load Balancer (ELB)](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform/pa-user/elb-service) for ingress and [create a Cloud NAT gateway](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform/pa-user/cloud-nat-gateway) for egress.
  * **`VirtualMachineExternalAccess` (VMEA)**: Control VM ingress and egress together using the Distributed Cloud VMM API or the Distributed Cloud CLI. Distributed Cloud deprecates configuring VMEA using the GDC console, and VMEA is no longer the preferred option. You can still view the ingress and egress IP addresses that you enabled for a VM instance using the Distributed Cloud VMM API or the GDC console.



This document is for developers in platform administrator or application operator groups that configure IP addresses for VMs in a Distributed Cloud environment. For more information, see [Audiences for GDC air-gapped documentation](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/resources/audiences).

## Before you begin

To use `gdcloud` command-line interface (CLI) commands, ensure that you have downloaded, installed, and configured the [`gdcloud` CLI](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/resources/gdcloud-overview). All commands for Distributed Cloud use the `gdcloud` or `kubectl` CLI, and require an operating system (OS) environment.

### Get the kubeconfig file path

To run commands against the Management API server, ensure you have the following resources:

  1. [Sign in and generate](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/application/ao-user/iam/sign-in#cli) the kubeconfig file for the Management API server if you don't have one.

  2. Use the path to the kubeconfig file of the Management API server to replace `MANAGEMENT_API_SERVER` in these instructions.




### Request IAM roles

Contact your Project IAM Admin to request the following roles on your project:

  * **Virtual Machine Project Admin** (`project-vm-admin`): create, modify, list, and delete VMs in the project namespace.

  * **Project Viewer**(`project-viewer`): view all resources within the project namespaces.




All VM roles must bind to the namespace of the project where the VM resides. Follow the steps to [verify](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/application/ao-user/vms/preparation#verify-user-access) your access.

## Configure `VirtualMachineExternalAccess` (VMEA)

**Note:** Distributed Cloud deprecates configuring `VirtualMachineExternalAccess` using the GDC console, and `VirtualMachineExternalAccess` is no longer the preferred method for managing external networking for VMs. Although you can still configure `VirtualMachineExternalAccess` using the Distributed Cloud VMM API or the gdcloud CLI, [create an External Load Balancer (ELB)](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform/pa-user/elb-service) for ingress and [create a Cloud NAT gateway](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform/pa-user/cloud-nat-gateway) for egress instead.

`VirtualMachineExternalAccess` (VMEA) is one mechanism for controlling VM Ingress and VM Egress. VMEA can't control VM Ingress and VM Egress separately. The ingress and egress of a VM must be enabled or disabled together at the same time.

You can configure and control VMEA either from UI or from Distributed Cloud VMM API. A VM can only have a single VMEA. If a VM does not have a VMEA, both the ingress and egress is disabled by default.

### Enable external access

To enable a VM with external access for data transfer in and data transfer out, you can configure the VMEA from GDC console or the Distributed Cloud [Virtual Machine Manager API](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/apis/service/virtualmachine/vmm-api-overview).

By default, the intra-project network traffic is allowed, and you can directly access your VM inside the project. A **network policy** blocks all ingress traffic to the VM from outside the project. You must manually create a new network policy to let your source IP address to access the VM through data transfer in. This network policy can either be a [cross-project traffic network policy](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/application/ao-user/vms/connect-to-vm/network-policy#cross-project-traffic) or a [cross-organization traffic network policy](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/application/ao-user/vms/connect-to-vm/network-policy#cross-org-traffic). The location depends on what you want to access the VM from.

You can enable and disable the external access of a VM by specifying `true` or `false` in the `enabled` field of the VMEA spec. For VM Ingress, you can configure data transfer in ports by specifying the name, protocol and port number for each port you want to add in the `ports` field of VMEA spec.

To enable external access of a VM by creating a new VMEA, complete the following:

###  API 

Run the following command:
    
    
    kubectl --kubeconfig MANAGEMENT_API_SERVER \
      apply -n PROJECT -f - <<EOF
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

  * MANAGEMENT_API_SERVER: the kubeconfig file to the Management API server
  * VM_NAME: the name of your VM
  * PORT_NAME: the port name
  * PROTOCOL: the protocol you want the ingress service to use. The protocol name must be capitalized and a Kubernetes supported protocol, such as `TCP`, `UDP`, or `SCTP`
  * PORT_NUMBER: the port number

**Note:** Update `enabled` field to `true`.

To enable external access of a VM by editing an existing VMEA through the VMM API, run the following:
    
    
    kubectl --kubeconfig MANAGEMENT_API_SERVER \
      -n PROJECT \
      edit virtualmachineexternalaccesses.virtualmachine.gdc.goog VM_NAME
    

###  gdcloud 

Use the `gdcloud compute` command with the `--enable-external-access` flag to enable external access on a VM instance:
    
    
    gdcloud compute instances create VM_NAME \
      --project PROJECT \
      --machine-type MACHINE_TYPE \
      --image IMAGE \
      --image-project IMAGE_PROJECT \
      --enable-external-access
    

Replace the following variables:

  * VM_NAME: the name of the VM
  * PROJECT: the Distributed Cloud project where the VM resides
  * MACHINE_TYPE: the name of the predefined machine type for the virtual machine instance
  * IMAGE: the boot image name for the instance
  * IMAGE_PROJECT: the project of the boot image for the instance



### Disable external access

If a VM does not have a corresponding VMEA, both of the ingress and egress are disabled. If a VM has a corresponding VMEA, you can disable the VMEA by either setting the `enabled` field to `false` or directly deleting the VMEA. You can do these operations through the Distributed Cloud VMM API.

To disable external access, complete the following steps:

###  API 

Disable external access by deleting a VMEA:
    
    
    kubectl --kubeconfig MANAGEMENT_API_SERVER \
      -n PROJECT \
      delete virtualmachineexternalaccesses.virtualmachine.gdc.goog VM_NAME
    

Replace the following:

  * MANAGEMENT_API_SERVER: the kubeconfig file to the Management API server
  * VM_NAME: the name of the VM
  * PROJECT: the Distributed Cloud project where the VM resides



Disable external access by editing a VMEA:
    
    
    kubectl --kubeconfig MANAGEMENT_API_SERVER \
      -n PROJECT \
      edit virtualmachineexternalaccesses.virtualmachine.gdc.goog VM_NAME
    

Update the `enabled` field to `false`.

### Ingress

#### View Ingress IP addresses

If a VM is enabled with Ingress, an ingress IP address shows on the GDC console after creation. You can also find this ingress IP address from the **VM details** page in the GDC console.

To fetch the IP address, use the Distributed Cloud VMM API. Complete the following:

###  API 

Fetch the IP address:
    
    
    kubectl --kubeconfig MANAGEMENT_API_SERVER \
      -n PROJECT \
      get virtualmachineexternalaccesses.virtualmachine.gdc.goog VM_NAME \
      -ojsonpath='{.status.ingressIP}'
    

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

![Console UI showing Network details list with edit icon on Ingress Ports](https://docs.cloud.google.com/static/distributed-cloud/hosted/docs/latest/gdcag/application/ao-user/vms/images/vm-console-edit-ingress.png)




###  API 
    
    
    kubectl --kubeconfig MANAGEMENT_API_SERVER \
      -n PROJECT \
      patch virtualmachineexternalaccesses.virtualmachine.gdc.goog VM_NAME \
      --type "json" -p '[{"op":"add","path":"/spec/ports/-","value": {"name":"PORT_NAME","port":PORT_NUMBER, "Protocol":"TCP"}}]'
    

Replace the following:

  * MANAGEMENT_API_SERVER: the kubeconfig file to the Management API server
  * VM_NAME: the name of the VM
  * PROJECT: the Distributed Cloud project where the VM resides
  * PORT_NAME: the name of the port to add
  * PORT_NUMBER: the port number



#### Enable Ingress with non-TCP protocol

Distributed Cloud lets you enable your VM Ingress with different protocols. By default, a VM Ingress service uses TCP protocol. You can add your own non-TCP protocol ingress for your VM. Distributed Cloud supports the following protocols:

  * Transmission control protocol (TCP).
  * User datagram protocol (UDP).
  * Stream control transmission protocol (SCTP).



You can enable data transfer in with non-TCP protocol by specifying different protocol names when creating VMEA.

**Note:** In prior Distributed Cloud versions, you can create multiple ingresses with different IP addresses. In versions after 1.11, you can only have one VM Ingress with a single IP address.

### Egress

A VM workload in an organization project can reach the external network, or be exposed to services in other organizations. If you enable data transfer out for the VM, you see an egress IP address generated. The VM connects to the external services with this IP address.

To make this IP address data transfer out of the external network, you might need to apply project network policies. For more information, refer to [Egress cross-organization traffic network policy](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/application/ao-user/vms/connect-to-vm/network-policy#egress-network-policy-crossorg).

If a VM is configured for egressing traffic using a [Cloud NAT Gateway](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform/pa-user/cloud-nat), the following annotation must be added to the Virtual Machine External Access object to preserve egress connectivity: `egress.networking.gke.io/use-cloud-nat:"true"`

#### View Egress IP address

If a VM is enabled with Egress, an egress IP address shows on the GDC console after creation. You can also find this egress IP address from the **VM details** page.

To view the egress IP address, complete the following:

###  API 

Fetch the IP address:
    
    
    kubectl --kubeconfig MANAGEMENT_API_SERVER \
      -n PROJECT \
      get virtualmachineexternalaccesses.virtualmachine.gdc.goog VM_NAME \
      -ojsonpath='{.status.egressIP}'
    

Replace the following:

  * MANAGEMENT_API_SERVER: the kubeconfig file to the Management API server
  * VM_NAME: the name of the VM
  * PROJECT: the Distributed Cloud project where the VM resides



VM Egress is based on a project. VMs within the same project contain the same Egress IP address.

#### Control Egress

In previous Distributed Cloud versions, you had to reboot the VM to reflect egress changes to a running VM. In version 1.11, you can enable and disable the VM egress without rebooting the VM. This change takes effect right after you update the VMEA.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
