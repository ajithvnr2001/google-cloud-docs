---
url: https://docs.cloud.google.com/compute/docs/dynamic-resource-management/
title: Next generation dynamic resource management \u00a0|\u00a0 Compute Engine \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:18:56.928001+00:00
---

# Next generation dynamic resource management  |  Compute Engine  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/compute/docs/dynamic-resource-management/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ Compute Engine ](https://docs.cloud.google.com/compute/docs)
  * [ Guides ](https://docs.cloud.google.com/compute/docs/overview)



Send feedback 

#  Next generation dynamic resource management Stay organized with collections  Save and categorize content based on your preferences. 

[N4A VMs](https://docs.cloud.google.com/compute/docs/general-purpose-machines#n4a_series) powered by Google Axion processors, [N4D VMs](https://docs.cloud.google.com/compute/docs/general-purpose-machines#n4d_series) powered by 5th generation AMD EPYC Turin processors, and [N4 VMs](https://docs.cloud.google.com/compute/docs/general-purpose-machines#n4_series) powered by 5th generation Intel Xeon processors use [Titanium](https://cloud.google.com/titanium). These machine series also use next generation dynamic resource management to drive cost efficiency by making better use of the physical resources available on host machines, and also uses a custom-built CPU scheduler and performance-aware live migration to balance workload performance needs with available resources. These are the same technologies that Google Search, Google Ads, Google Maps, and YouTube services use to run their latency-sensitive workloads efficiently.

Next generation dynamic resource management also has better NUMA affinity, more accurate prediction of resource requirements, and faster rebalancing using performance-aware live migration.

## How dynamic resource management works

Virtual CPUs (vCPUs) are implemented as threads that are scheduled to run on demand like any other thread on a host. When the vCPU has work to do, the work is assigned to an available physical CPU on which to run until it goes to sleep again. Similarly, virtual RAM is mapped to physical host pages using page tables that are populated when a guest-physical page is first accessed. This mapping remains fixed until the VM indicates that a guest-physical page is no longer needed.

Dynamic resource management enables Compute Engine to better use the available physical CPUs by scheduling VMs to servers based on resource demand, and scheduling vCPU threads to physical CPUs such that wait time is minimized. In most cases, we can do this seamlessly, so Google Cloud can run VMs more efficiently on fewer servers.

## Components of dynamic resource management

Compute Engine uses the following technologies for dynamic resource management:

### Larger, more efficient physical servers

Core count and RAM density have steadily increased such that now the host servers have far more resources than any individual VM. Google continually benchmarks new hardware and looks for platforms that are cost-effective and perform well for the widest variety of cloud workloads and services, allowing you to take advantage of the newest technologies when they're available.

### Intelligent VM placement

Google's cluster management system observes the CPU, RAM, and other resource demands of VMs running on a physical server. It uses this information to predict how a newly added VM will perform on that server. It then searches across thousands of servers to find the best location to add a VM. These observations ensure that when a new VM is placed, it is compatible with its neighbors and unlikely to experience interference from those instances.

### Performance-aware live migration

After VMs are placed on a host, Compute Engine continuously monitors VM performance and wait times. If the resource demands of the VMs increase, Compute Engine can use [live migration](https://docs.cloud.google.com/compute/docs/instances/live-migration-process) to transparently shift workloads to other hosts in the data center. The live migration policy is guided by a predictive approach that gives Compute Engine time to shift the load, often before any wait time is experienced by the VMs.

### Hypervisor CPU scheduler

The hypervisor CPU scheduler dynamically maps virtual CPU and memory to the physical CPU and memory of the host server on demand. This dynamic management drives cost efficiency in VMs by making better use of the physical resources. Efficient use of resources means Compute Engine can run VMs more efficiently on fewer servers, allowing Google Cloud to pass on savings to users.

**Note:** Dynamic resource management applies to [N4A](https://docs.cloud.google.com/compute/docs/general-purpose-machines#n4a_machine_types), [N4D](https://docs.cloud.google.com/compute/docs/general-purpose-machines#n4d_machine_types), [N4](https://docs.cloud.google.com/compute/docs/general-purpose-machines#n4_machine_types), and [E2](https://docs.cloud.google.com/compute/docs/general-purpose-machines#e2_machine_types) VMs.

## First generation dynamic resource management

E2 was the first VM series to offer dynamic resource management using a virtio memory balloon device.

### Virtio memory balloon device with E2 VMs

Memory ballooning is an interface mechanism between host and guest to dynamically adjust the size of the reserved memory for the guest. E2 uses a [virtio memory balloon device ](https://docs.oasis-open.org/virtio/virtio/v1.1/csprd01/virtio-v1.1-csprd01.html#x1-2790005) to implement memory ballooning. Through the virtio memory balloon device, a host can explicitly ask a guest to yield a certain amount of free memory pages (also called memory balloon inflation), and reclaim the memory so that the host can use the free memory for other VMs. Likewise, the virtio memory balloon device can return memory pages back to the guest by deflating the memory balloon. E2 VMs are the only machine family that uses the memory balloon device.

Compute Engine E2 VM instances that are based on a [public image](https://docs.cloud.google.com/compute/docs/images#os-compute-support) have a [virtio memory balloon device ](https://docs.oasis-open.org/virtio/virtio/v1.1/csprd01/virtio-v1.1-csprd01.html#x1-2790005), which monitors the guest operating system's memory use. The guest operating system communicates its available memory to the host system. The host reallocates any unused memory to other processes on demand, thereby using memory more effectively. Compute Engine collects and uses this data to make more accurate [rightsizing recommendations](https://docs.cloud.google.com/compute/docs/instances/apply-machine-type-recommendations-for-instances).

#### Verifying the driver installation

To check if your image has the virtio memory balloon device driver installed and loaded, run the following command.

###  Linux 

Most Linux distributions include the virtio memory balloon device driver. To verify that your image has the driver installed and loaded, run:
    
    
    sudo modinfo virtio_balloon > /dev/null && echo Balloon driver is \
    installed || echo Balloon driver is not installed; sudo lsmod | grep \
    virtio_balloon > /dev/null && echo Balloon driver is loaded || echo \
    Balloon driver is not loaded

In [Linux kernels](https://en.wikipedia.org/wiki/Linux_kernel_version_history) before 5.2, the Linux memory system sometimes mistakenly prevents large allocations when the balloon device is present. This is rarely an issue in practice, but we recommend changing the virtual memory `overcommit_memory` setting to `1` to prevent the issue from occurring. This change is already made by default in all Google-provided images published since February 9, 2021.

To fix the setting, use the following command to change the value from `0` to `1`:
    
    
    sudo /sbin/sysctl -w vm.overcommit_memory=1

To persist this change across reboots, add the following to your `/etc/sysctl.conf` file:
    
    
    vm.overcommit_memory=1

###  Windows 

Compute Engine [Windows images](https://docs.cloud.google.com/compute/docs/instances/windows#windows_server) include the virtio balloon device. However, custom Windows images don't. To verify whether your Windows image has the driver installed, run:
    
    
    googet verify google-compute-engine-driver-balloon
    

#### Disabling the virtio memory balloon device

Using the virtio memory balloon device enables Compute Engine to utilize memory resources more effectively so Google Cloud can offer E2 VMs at lower prices. You can opt out of the virtio memory balloon device by disabling the device driver. After disabling the virtio memory balloon device, you will continue to receive [rightsizing recommendations](https://docs.cloud.google.com/compute/docs/instances/apply-machine-type-recommendations-for-instances); however, they might not be as accurate.

###  Linux 

To disable the device in Linux, run the following command:
    
    
    sudo rmmod virtio_balloon
    

You can add this command to the VM's [startup script](https://docs.cloud.google.com/compute/docs/startupscript) to automatically disable the device upon VM boot.

###  Windows 

To disable the device on Windows, run the following command:
    
    
    googet -noconfirm remove google-compute-engine-driver-balloon
    

You can put this command into the VM's [startup script](https://docs.cloud.google.com/compute/docs/startupscript#providing_a_startup_script_for_windows_instances) to automatically disable the device upon VM boot.

## What's next

  * Read the blog about [Dynamic resource management](https://cloud.google.com/blog/products/compute/understanding-dynamic-resource-management-in-e2-vms).
  * Review the [N4D machine series](https://docs.cloud.google.com/compute/docs/general-purpose-machines#n4d_series) information.
  * Review the [N4 machine series](https://docs.cloud.google.com/compute/docs/general-purpose-machines#n4_series) information.
  * Review the [N4A machine series](https://docs.cloud.google.com/compute/docs/general-purpose-machines#n4a_series) information.
  * Review the [E2 machine series](https://docs.cloud.google.com/compute/docs/general-purpose-machines#e2_machine_types) information.
  * [Create a VM](https://docs.cloud.google.com/compute/docs/instances/create-start-instance).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
