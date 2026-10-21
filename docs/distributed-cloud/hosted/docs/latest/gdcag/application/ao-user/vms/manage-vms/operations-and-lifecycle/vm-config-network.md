---
url: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/application/ao-user/vms/manage-vms/operations-and-lifecycle/vm-config-network/
title: Configure Tier 1 networking for a VM \u00a0|\u00a0 Google Distributed Cloud air-gapped \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-15T08:27:35.676503+00:00
---

# Configure Tier 1 networking for a VM  |  Google Distributed Cloud air-gapped  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/application/ao-user/vms/manage-vms/operations-and-lifecycle/vm-config-network/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Distributed, hybrid, and multicloud ](https://docs.cloud.google.com/docs/dhm-cloud)
  * [ Google Distributed Cloud ](https://docs.cloud.google.com/distributed-cloud/docs)
  * [ Air-gapped ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdch)
  * [ 1.16.2 (Latest) ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag)



Send feedback 

#  Configure Tier 1 networking for a VM Stay organized with collections  Save and categorize content based on your preferences. 

This document describes how to configure Tier 1 networking performance for certain virtual machine (VM) instances in Google Distributed Cloud (GDC) air-gapped. VMs with Tier 1 networking configurations are especially useful for large, distributed compute workloads with lots of heavy internode communications, such as high performance computing (HPC), machine learning (ML), and deep learning (DL).

This document is for developers in platform administrator or application operator groups that configure networking for VMs in a Distributed Cloud environment. For more information, see [Audiences for GDC air-gapped documentation](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/resources/audiences).

## Before you begin

To use `gdcloud` command-line interface (CLI) commands, ensure that you have downloaded, installed, and configured the [`gdcloud` CLI](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/resources/gdcloud-overview). All commands for Distributed Cloud use the `gdcloud` or `kubectl` CLI, and require an operating system (OS) environment.

### Get the kubeconfig file path

To run commands against the Management API server, ensure you have the following resources:

  1. [Sign in and generate](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/application/ao-user/iam/sign-in#cli) the kubeconfig file for the Management API server if you don't have one.

  2. Use the path to the kubeconfig file of the Management API server to replace `MANAGEMENT_API_SERVER` in these instructions.


**Important:** VM names must only contain alphanumeric characters and dashes. Using symbols other than alphanumeric characters and dashes, such as a period, results in connection failures to the VM. The VM name must be no longer than 53 characters.

### Request IAM roles

Contact your Project IAM Admin to request the following roles on your project:

  * **Virtual Machine Project Admin** (`project-vm-admin`): create, modify, list, and delete VMs in the project namespace.

  * **Project Viewer**(`project-viewer`): view all resources within the project namespaces.




All VM roles must bind to the namespace of the project where the VM resides. Follow the steps to [verify](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/application/ao-user/vms/preparation#verify-user-access) your access.

## Limitations

Tier 1 networking is supported with N2, N3, N4, A2, and A3 machine types that have at least 4 vCPUs.

## Bandwidth tiers

The ingress and egress bandwidth limit represents the maximum possible amount of data per unit of time, such as gigabits per second (Gbps), that GDC allows a VM instance to transmit or receive from its network interfaces (NICs). The bandwidth includes data transferred between VM instances and object storage.

GDC has the following bandwidth limits:

  * The default bandwidth limit is 10 Gbps.
  * Tier 1 networking increases the maximum egress bandwidth limit for compute instances. The maximum egress bandwidth limit ranges from 16 Gbps to 32 Gbps, depending on the size and machine type of your instance.
  * The actual egress bandwidth is always less than or equal to the egress bandwidth limit.



To achieve the highest possible egress bandwidth, all of the following must be true:

  * The sending and receiving compute instances must be in the same zone.
  * Packets sent between the instances must use internal IP address destinations.
  * The number of TCP flows must be between 4 and 128 flows.
  * The sending instances must have TCP Segmentation Offload (TSO) enabled, and the receiving instances must have Generic Receive Offload (GRO) enabled.
  * The guest OS on the sending instance has Transmit Packet Steering (XPS) and Interrupt Request (IRQ) pinning configured. For more information, see Configure guest OS pinning.



### N2 and N3 VMs

vCPUs | Internal IP | Tier 1 Internal IP  
---|---|---  
2 | 10 Gbps | Not applicable  
4 | 10 Gbps | Not applicable  
8 | 10 Gbps | 16 Gbps  
12 | 10 Gbps | 25 Gbps  
16 | 10 Gbps | 32 Gbps  
32 | 10 Gbps | 32 Gbps  
64 | 10 Gbps | 32 Gbps  
  
### N4 VMs

vCPUs | Internal IP | Tier 1 Internal IP  
---|---|---  
4 | 10 Gbps | Not applicable  
8 | 10 Gbps | Not applicable  
16 | 10 Gbps | 32 Gbps  
32 | 10 Gbps | 32 Gbps  
48 | 10 Gbps | 32 Gbps  
64 | 10 Gbps | 32 Gbps  
80 | 10 Gbps | 32 Gbps  
160 | 10 Gbps | 32 Gbps  
  
### A2 VMs

vCPUs | Internal IP | Tier 1 Internal IP  
---|---|---  
12 | 10 Gbps | 18 Gbps  
24 | 10 Gbps | 32 Gbps  
  
### A3 VMs

vCPUs | Internal IP | Tier 1 Internal IP  
---|---|---  
28 | 10 Gbps | 32 Gbps  
56 | 10 Gbps | 32 Gbps  
112 | 10 Gbps | 32 Gbps  
  
## Configure a VM with Tier 1 networking

Create instances and containers that use Tier 1 networking:

###  gdcloud 
    
    
    gdcloud compute instances create VM_NAME \
        --machine-type=MACHINE_TYPE \
        --image=BOOT_DISK_IMAGE_NAME --image-project=vm-system \
        --boot-disk-size=BOOT_DISK_SIZE \
        --network-performance-tier=tier_1
    

Replace the following:

Variable| Definition | `VM_NAME` | The name of the new VM. The name must only contain alphanumeric characters and dashes, and be no longer than 53 characters.  
---|---  
`MACHINE_TYPE` | The predefined machine type for the new VM. Select an available machine type:  
` gdcloud compute machine-types list `  
`BOOT_DISK_IMAGE_NAME` | The name of the image to use for the new VM boot disk.  
`BOOT_DISK_SIZE` | The size of the boot disk, such as `20GB`.  
This value must always be greater than or equal to the `minimumDiskSize` of the boot disk image.  
  
###  API 
    
    
    kubectl --kubeconfig MANAGEMENT_API_SERVER \
        apply -n PROJECT -f - <<EOF
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
      network:
        networkPerformanceTier: Tier_1
    EOF
    

Replace the following:

Variable| Definition | `MANAGEMENT_API_SERVER` | The Management API server kubeconfig file.  
---|---  
`PROJECT` | The Distributed Cloud project to create the VM.  
`VM_BOOT_DISK_NAME` | The name of the new VM boot disk.  
`BOOT_DISK_IMAGE_NAME` | The name of the image to use for the new VM boot disk.  
`BOOT_DISK_SIZE` | The size of the boot disk, such as `20Gi`.  
This value must always be greater than or equal to the `minimumDiskSize` of the boot disk image.  
`VM_NAME` | The name of the new VM. The name must only contain alphanumeric characters and dashes, and be no longer than 53 characters.  
`MACHINE_TYPE` | The predefined machine type for the new VM. Select an available machine type:  
` kubectl --kubeconfig MANAGEMENT_API_SERVER get virtualmachineimage.virtualmachine.gdc.goog --namespace PROJECT `  
`BOOT_DISK_AUTO_DELETE` | Either `true` or `false`, indicating whether the boot disk is automatically deleted when the VM instance gets deleted.  
  
## Configure guest OS pinning for consistent performance

To prevent network throughput drops and maintain consistent network bandwidth on guest VMs using Tier 1 networking, configure Transmit Packet Steering (XPS) and Interrupt Request (IRQ) pinning in the guest operating system.

Without these configurations, the guest OS scheduler might consolidate all transmit queues and network interrupts onto a single CPU core under heavy network load, limiting throughput.

Before configuring XPS and IRQ pinning, find the number of virtual CPUs (vCPUs) assigned to your VM by running the following command on the guest VM:
    
    
    nproc
    

Use this number to replace `NUM_VCPUS` in the following configurations.

### Configure XPS pinning

Distribute the transmit (TX) queues across the virtual CPUs (vCPUs) assigned to the VM. A uniform distribution improves cache locality and balances processing.

To configure XPS pinning on the guest VM, run the following script:
    
    
    NUM_VCPUS=NUM_VCPUS
    
    for i in $(seq 0 $((NUM_VCPUS - 1))); do
        cpu=$(( i % (NUM_VCPUS / 4) ))
        mask=$(printf "%x" $((1 << cpu)))
        echo "Queue tx-$i -> CPU $cpu (mask $mask)"
        echo $mask > /sys/class/net/enp1s0/queues/tx-$i/xps_cpus
    done
    

**Note:** Replace `enp1s0` with the name of your network device if different, and replace `NUM_VCPUS` with the actual number of vCPUs assigned to your guest VM.

### Configure IRQ pinning

Bind the network interface interrupts directly to the specific CPU cores responsible for processing those queues. This alignment minimizes Inter-Processor Interrupts (IPIs) and cache invalidations.

To configure IRQ pinning on the guest VM, run the following script:
    
    
    NUM_VCPUS=NUM_VCPUS
    irqs=$(grep "virtio0-" /proc/interrupts | awk -F: '{print $1}' | tr -d ' ')
    
    idx=0
    for irq in $irqs; do
        cpu=$(( idx % (NUM_VCPUS / 4) ))
        mask=$(printf "%x" $((1 << cpu)))
        echo "Mapping IRQ $irq to CPU $cpu (mask $mask)"
        echo $mask > /proc/irq/$irq/smp_affinity
        idx=$(( idx + 1 ))
    done
    

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
