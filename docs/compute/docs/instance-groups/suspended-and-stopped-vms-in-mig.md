---
url: https://docs.cloud.google.com/compute/docs/instance-groups/suspended-and-stopped-vms-in-mig/
title: About suspending and stopping VMs in a MIG \u00a0|\u00a0 Compute Engine \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:08:38.706362+00:00
---

# About suspending and stopping VMs in a MIG  |  Compute Engine  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/compute/docs/instance-groups/suspended-and-stopped-vms-in-mig/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ Compute Engine ](https://docs.cloud.google.com/compute/docs)
  * [ Guides ](https://docs.cloud.google.com/compute/docs/overview)



Send feedback 

#  About suspending and stopping VMs in a MIG Stay organized with collections  Save and categorize content based on your preferences. 

This document describes the suspend and stop actions on virtual machine (VM) instances in a managed instance group (MIG). It also describes how suspending and stopping VMs in a MIG can help you save costs and reduce the waiting time when you need more VMs in the group.

MIGs let you suspend and stop VMs to achieve the following:

  * **Pause an application or a service** that you are not using to save costs by not paying for compute resources.
  * **Accelerate MIG scale out** by starting pre-initialized VMs from the standby pool of stopped and suspended VMs.



## Use cases

The following sections describe typical use cases for the standby pool in a MIG.

### Pause an application or a service

You can [suspend](https://docs.cloud.google.com/compute/docs/instances/suspend-resume-instance) or stop VMs in a MIG to pause your application and resume it when needed, according to your computation, working hours, peak time, and budget constraints. You can keep the results of your current computations on persistent disks or, in the case of suspended VMs, in memory.

For example, you might want to suspend or stop the VMs in a MIG in the following scenarios:

  * You have heavy workloads during weekdays and want to suspend VMs on weekends to save on costs.
  * You have a testing environment that is needed during implementation changes, and you want to stop it when you are not actively developing.



### Accelerate MIG scale out

You can keep a standby pool of pre-initialized VMs ready to start when the MIG resizes up. Instead of creating new VMs and waiting for your app to initialize and become ready to run, the MIG starts or resumes VMs from the standby pool. In such case, the VM initialization is completed in advance, not in a critical moment of increased load.

Standby pools are helpful for applications that take long time to initialize, for example in the following scenarios:

  * Applications that need to download up-to-date content to persistent disks.
  * Applications that need to cache extra content in memory—via downloads from external storage, from local computation, or a combination of both.
  * Applications that need to install fresh software during the initialization, such as Kubernetes nodes.



## Preserved resources

The following table shows the resources that are preserved when you suspend and stop VMs in a MIG.

Preserved | Suspended VM | Stopped VM  
---|---|---  
VM name |  |   
Internal IP |  |   
External IP (ephemeral) |  |   
External IP (static*) |  |   
Disks† |  |   
Metadata |  |   
Memory |  |   
  
*To preserve an external IP when you stop or suspend a VM in a MIG, use the [stateful MIG configuration](https://docs.cloud.google.com/compute/docs/instance-groups/configuring-stateful-ip-addresses-in-migs) to promote the external IP to a static IP.

†If a VM has any Local SSD disks attached, when you stop or suspend the VM, the data on the Local SSD disks is not preserved. 

**Note:** You can keep a VM in suspended state for [up to 60 days](https://docs.cloud.google.com/compute/docs/instances/suspend-resume-instance#how_suspension_works). After 60 days in the suspended state, the VM is terminated. The MIG then creates a new VM and puts it in the suspended state, according to the configuration of the standby pool. If you haven't created a [stateful configuration in the MIG](https://docs.cloud.google.com/compute/docs/instance-groups/configuring-stateful-migs), then the MIG doesn't preserve the VM name, IP addresses, and disks when recreating the VM.

## Behavior and configuration

Standby pool is formed by stopped and suspended pools of VMs. All stopped VMs become a part of the stopped pool, and all suspended VMs become part of the suspended pool. If you configured autoscaling in a MIG, after you suspend or stop a VM, the MIG immediately creates new VMs to maintain the recommended size of the MIG.

**Important:** If you have a [Google Cloud load balancer](https://docs.cloud.google.com/load-balancing/docs/load-balancing-overview) configured in your MIG, stopped or suspended VMs are automatically excluded from the backend service and don't receive traffic.

### Target sizes of suspended and stopped pools

Similar to the target size of the MIG, stopped and suspended pools have their own target sizes. You can control the standby pool target size in the following ways:

  * By configuring the values of the stopped and suspended target sizes.
  * By manually stopping and suspending VMs, which then automatically changes the target sizes.



When you change target sizes for stopped or suspended pools, the MIG behaves as follows:

  * When you increase the size of suspended or stopped pools, the MIG creates new VMs, waits until the VMs are initialized, and then suspends or stops the VMs accordingly. For regional MIGs, VMs are created in accordance with the [target distribution shape](https://docs.cloud.google.com/compute/docs/instance-groups/regional-mig-distribution-shape) configured.
  * When you decrease the size of suspended or stopped pools, the MIG arbitrarily selects which suspended or stopped VMs to delete.
  * When you change the MIG target size and the size of suspended or stopped pool simultaneously, the MIG attempts to minimize the number of operations required to apply your changes. This means that the MIG might resume or start VMs from the standby pool, or suspend or stop some running VMs.



### Standby policy

The standby policy defines the behavior of the standby pool based on the following parameters that you specify:

  * **Mode:** The mode in which the MIG uses suspended and stopped VMs. This can be `manual` or `scale-out-pool` mode.
  * **Initial delay:** The time for which the MIG runs a newly created VM before suspending or stopping it. Configure the initial delay to allow enough time for your app to pre-initialize and be ready to run when the VM starts or resumes.



### Mode

You can choose how to manage standby pools by setting the operation mode. There are two possible options: `manual` mode and `scale-out-pool` mode.

#### Manual mode (default)

In manual mode, you have full control over which VMs are stopped and suspended in the MIG. Manual mode is the default mode of standby pool.

Manual mode is useful in the following cases:

  * To pause your workload and save on costs of idle running VMs.
  * To integrate the MIG with third-party autoscalers that require advanced management of individual VMs.
  * To stop selected VMs for debugging purposes.



With manual mode, MIG doesn't apply any automations to the standby pool:

  * When you or autoscaler increases the target size of the MIG, the MIG doesn't automatically start or resume VMs, but creates new ones.
  * When you or autoscaler decreases the target size of the MIG, the MIG doesn't automatically stop or suspend running VMs, but deletes them.



#### Scale out pool mode

In scale out pool mode, the MIG uses the VMs from the standby pools to accelerate the scale out by resuming or starting them. Then, the MIG automatically replenishes the standby pool with new VMs to maintain the target sizes.

Scale out pool mode is useful to accelerate the scale out of the MIG in the following cases:

  * If you use Compute Engine autoscaler.
  * If you use third-party autoscalers and you want to preserve any existing integration.
  * If you manually increase the target size of running VMs.



In scale out pool mode, the MIG behaves as follows:

  * When you or autoscaler increases the target size of running VMs in the MIG, the MIG takes action in the following order:

    1. The MIG resumes suspended VMs in case any are available in the zones where the MIG scales out.
    2. After resuming the suspended VMs, if the target size of the MIG is not yet reached, the MIG starts stopped VMs if any are available in the zones where the MIG scales out.
    3. After starting the VMs, if the target size of the MIG is still not reached, it creates new VMs from scratch.

After the standby pool is used to accelerate scale out, the MIG does the following:

    1. It creates new VMs to replenish the suspended and stopped pools based on their target sizes, and in accordance with the target distribution shape in case of a regional MIG.
    2. It puts the new VMs in the running state.
    3. It suspends or stops the new VMs after the initial delay is passed.
  * When you or autoscaler decreases the target size of the MIG, the MIG doesn't automatically stop or suspend running VMs but deletes them.


**Note:** When a regional MIG scales out, depending on its [target distribution shape](https://docs.cloud.google.com/compute/docs/instance-groups/regional-migs#target_distribution_shape), the scale out might occur in a zone or zones that at that moment don't have stopped or suspended VMs. In that case, the MIG creates VMs from scratch in the required zone or zones.

### Initial delay

To make sure that your VM is initialized correctly, specify the initial delay in the standby policy. The initial delay is the time that VMs wait before stopping or suspending after they are created. This gives your initialization script the time to complete.

The initial delay occurs in the following cases:

  * A new VM is created with the intended target state of `SUSPENDED` or `TERMINATED`.
  * An existing instance in the `RUNNING` state is suspended or stopped.



In both cases, the instance is allowed to initialize before it is suspended or stopped.

When you want to use standby pool to accelerate the scale out of MIG it is recommended that you measure the time required for your application to initialize on the selected machine type to assure that it is sufficient for your application to be fully ready before suspending or stopping. Otherwise, resuming or starting VMs from standby pool might take longer that creating VMs from scratch.

### Target status for VMs in MIGs

MIGs have a declarative API. This means that you declare the target status for the VMs in the MIG, and the API request is successful when the target status is saved. The MIG then performs the necessary operations to reach the target status, and you can check the [current action](https://docs.cloud.google.com/compute/docs/instance-groups/rolling-out-updates-to-managed-instance-groups#current_actions_on_instances) and current status of all the VMs using API.

Suspending and stopping VMs in a MIG works in the same declarative way. When you send a request to suspend or stop VMs, the MIG stores the information about the target status for each VM and starts the necessary operations to reach it.

When you [list managed VMs](https://docs.cloud.google.com/compute/docs/instance-groups/getting-info-about-migs#listing_a_migs_managed_instances) in a MIG, you can see the `targetStatus` field. It describes the final status of a VM, when the MIG is stable. It can be one of the following values:

  * `RUNNING`
  * `STOPPED`
  * `SUSPENDED`



VMs in a MIG can have the same [lifecycle statuses](https://docs.cloud.google.com/compute/docs/instances/instance-lifecycle) of single VMs. The following are examples of possible operations on a MIG, and the associated values of the `targetStatus` field:

  * Create the new VM and suspend it after the initialization. 
    * Target status of the VM: `SUSPENDED`.
  * Resume a previously suspended VM. 
    * Target status of the VM: `RUNNING`
  * Stop a previously running VM. 
    * Target status of the VM: `STOPPED`
  * Start a previously stopped VM. 
    * Target status of the VM: `RUNNING`



## Limitations

  * The following limitations for [suspending standalone VMs](https://docs.cloud.google.com/compute/docs/instances/suspend-resume-instance) also apply to suspending VMs in a MIG: 
    * You can't suspend an instance that uses a [GPU](https://docs.cloud.google.com/compute/docs/gpus).
    * You can't suspend a bare metal instance.
    * You can't suspend an instance by using the standard processes that are built into the guest environment. Commands, such as the `systemctl suspend` command in Ubuntu 16.04 and later, are not available. The in-guest signal is ignored.
    * You can only suspend an instance for up to 60 days before Compute Engine automatically stops the instance.
    * You can't suspend instances with more than 208 GB of memory.
    * You can suspend preemptible instances, but the preemptible instance might be terminated before it is successfully suspended.
    * You can't suspend a Confidential VM.
    * You can't suspend a compute instance that has CSEK-protected ([Deprecated](https://docs.cloud.google.com/compute/docs/deprecations)) disks attached.
  * In a regional MIG with `EVEN` target distribution shape and instance redistribution enabled, you cannot suspend, stop, resume, or start specific VMs in the group. To manage a standby pool, set the target sizes of the suspended and stopped pools.
  * You cannot use scale out pool mode if you've configured a second instance template for [canary update](https://docs.cloud.google.com/compute/docs/instance-groups/rolling-out-updates-to-managed-instance-groups#canary_updates) in the MIG.
  * You cannot suspend or stop VMs in a MIG if you've [turned off repairs](https://docs.cloud.google.com/compute/docs/instance-groups/about-repair) in the MIG.
  * You can only suspend an instance for up to 60 days before the VM is automatically stopped.



## Pricing

Each stopped and suspended VM is billed for the following items:

  * Any persistent disk usage for the boot disk, and any additional disks attached to the VM. For more information, see [Persistent Disk pricing](https://docs.cloud.google.com/persistent-disk#persistent-disk-pricing). 
  * Any static IPs attached to the VM. For more information, see [IP pricing](https://cloud.google.com/compute/pricing#ipaddress). 
  * In the case of suspended VMs, the VM memory and device state. For more information, see [VM instance pricing](https://docs.cloud.google.com/compute/vm-instance-pricing#suspended_vm_instances). 



## What's next

  * Learn how to [manually suspend or stop VMs in a MIG](https://docs.cloud.google.com/compute/docs/instance-groups/manually-suspend-or-stop-vms-in-mig).
  * Learn how to [accelerate scale out with suspended and stopped VMs](https://docs.cloud.google.com/compute/docs/instance-groups/accelerate-mig-scale-out-with-standby-pools).
  * Learn more about [updates for suspended and stopped VMs](https://docs.cloud.google.com/compute/docs/instance-groups/updating-migs#update_standby_pool).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
