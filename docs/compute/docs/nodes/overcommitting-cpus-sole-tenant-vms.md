---
url: https://docs.cloud.google.com/compute/docs/nodes/overcommitting-cpus-sole-tenant-vms/
title: Overcommit CPUs on sole-tenant VMs \u00a0|\u00a0 Compute Engine \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-15T13:41:14.504983+00:00
---

# Overcommit CPUs on sole-tenant VMs  |  Compute Engine  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/compute/docs/nodes/overcommitting-cpus-sole-tenant-vms/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ Compute Engine ](https://docs.cloud.google.com/compute/docs)
  * [ Guides ](https://docs.cloud.google.com/compute/docs/overview)



Send feedback 

#  Overcommit CPUs on sole-tenant VMs Stay organized with collections  Save and categorize content based on your preferences. 

Linux  Windows 

CPU overcommit on [sole-tenant nodes](https://docs.cloud.google.com/compute/docs/nodes/sole-tenant-nodes) lets you schedule instances that can share their spare CPU cycles with each other. This lets you overprovision sole-tenant node resources and schedule more VM CPUs on a sole-tenant node than are normally available. CPU overcommit is especially valuable for workloads that are underutilized but might experience relatively uncorrelated bursts.

CPU overcommit can help you reduce per-VM costs by spreading the cost of a sole- tenant node across more VMs. It can also reduce per-VM licensing costs when using per-socket or per-core licenses.

VMs with overcommitted CPUs can utilize otherwise unused CPU resources in the following ways:

  * If a sole-tenant node isn't full, overcommitted VMs can utilize unallocated cores.

  * If another VM on a sole-tenant node isn't utilizing all of its CPU resources—for example, because the CPU is idle—an overcommitted VM can use those CPU resources.




## Overcommit level

You can specify the value for the minimum number of CPUs that are allocated to a VM when you create a VM or after you stop a VM. The overcommit level represents the minimum number of underlying CPU threads that are guaranteed to be available for a VM. If the VM has more vCPUs than underlying threads available, the VM's vCPUs share the underlying compute resources and run with degraded performance.

You can set this value for each VM, which lets you provision VMs with different ratios of CPU overcommit on a single sole-tenant node. Lower values reduce capacity requirements at the potential expense of performance if correlated bursts occur. Determining an optimal value for the minimum number of CPUs requires an understanding of your workload utilization and iterative modification of the value.

When setting this value, keep in mind the following:

  * If you don't set the value for the minimum number of CPUs, or you set the value for the minimum number of CPUs equal to the number of CPUs on the VM's machine type, the VM's allowable overcommit ratio is 1.0. With an overcommit ratio of 1.0, all of the CPUs are accessible only to this VM, and there are no CPU resources available to be overcommitted to other VMs.

  * The minimum number of CPUs can't be greater than the number of CPUs specified by the VM's machine type.

  * The sum of the values for the minimum number of CPUs for all of the VMs on a sole-tenant node can't exceed the CPU capacity of that [sole-tenant node type](https://docs.cloud.google.com/compute/docs/nodes/sole-tenant-nodes#node_types), which on the `n1-node-96-624` node type is 96.




The value for the number of CPUs specified by the VM's machine type is a static value, and represents the number of CPUs that a VM can burst up to from the minimum number if those CPUs are available. If you require a number of CPUs different from those provided by [predefined machine types](https://docs.cloud.google.com/compute/docs/machine-resource#predefined-types), you can use a [custom machine type](https://docs.cloud.google.com/compute/docs/machine-resource#custom-types).

## Considerations

Before configuring the CPU overcommit levels for VMs, consider the criticality of your workload. Less critical workloads, such as development and test workloads, can potentially tolerate higher overcommit levels. More critical workloads, such as a production payments system, might not tolerate as much overcommit or any at all.

Also consider the utilization of your workload. Workloads with high CPU utilization are not good candidates for CPU overcommit because they won't have spare utilization cycles for other overcommitted VMs to utilize. Additionally, workloads with low average CPU utilization, but low utilization peak, might benefit from different sizes of machine types.

Using CPU overcommit benefits uncorrelated bursty workloads that have high peak utilization and low average utilization because these workloads are more likely to have available CPU resources to share across VMs when some VMs need to burst their utilization. If all of the VMs on a host burst at one time, the host won't have sufficient resources for your VMs.

**Caution:** Depending on the nature of the workload, overcommitting CPUs on sole-tenant nodes might result in performance fluctuations.

## Limitations

Workload limitations
    

CPU overcommit is best suited for workloads without stringent performance requirements—for example, development and test workloads, and virtual desktop infrastructures.

    

High levels of CPU overcommit might not be appropriate for workloads that are sensitive to performance.

    

For workloads with average and peak utilization that is consistently low, Google recommends _rightsizing_. That is, instead of overcommitting CPUs, we recommend modifying the size of the VM instance to match the resource requirements of that workload.

    

If your instances are too highly overcommitted, [move them to another sole-tenant node](https://docs.cloud.google.com/compute/docs/nodes/updating-vm-tenancy).

Machine type limitations
    

You can only overcommit CPUs on the following:

  * [N1 machine series](https://docs.cloud.google.com/compute/docs/general-purpose-machines#n1_machines) VMs that are provisioned on node groups that are based on the `n1-node-96-624` [node type](https://docs.cloud.google.com/compute/docs/nodes/sole-tenant-nodes#node_types)

  * [N2 machine series](https://docs.cloud.google.com/compute/docs/general-purpose-machines#n2_series) VMs that are provisioned on node groups that are based on the following [node types](https://docs.cloud.google.com/compute/docs/nodes/sole-tenant-nodes#node_types):

    * `n2-node-80-640`
    * `n2-node-128-864`
  * [N2D machine series](https://docs.cloud.google.com/compute/docs/general-purpose-machines#n2d_machines) VMs that are provisioned on node groups that are based on the following [node types](https://docs.cloud.google.com/compute/docs/nodes/sole-tenant-nodes#node_types):

    * `n2d-node-224-896`
    * `n2d-node-224-1792`
  * [N4 machine series](https://docs.cloud.google.com/compute/docs/general-purpose-machines#n4_series) VMs that are provisioned on node groups that are based on the following [node types](https://docs.cloud.google.com/compute/docs/nodes/sole-tenant-nodes#node_types):

    * `n4-node-224-1372`
  * [N4A machine series](https://docs.cloud.google.com/compute/docs/general-purpose-machines#n4a_series) VMs that are provisioned on node groups that are based on the following [node types](https://docs.cloud.google.com/compute/docs/nodes/sole-tenant-nodes#node_types):

    * `n4a-node-96-624`


Overcommit level limitations
    

You can only configure the minimum CPU on each sole-tenant node to half of the VM's CPUs, allowing for a maximum sole-tenant node overcommit ratio of 2.0.

VM scheduling limitations
    

Sole-tenant node groups based on sole-tenant node templates that aren't configured for CPU overcommit don't allow for provisioning of VMs with CPU overcommit enabled. That is, you can't schedule a VM with a specified minimum number of CPUs on a sole-tenant node group that is not configured for CPU overcommit.

## Quota

CPU quota is based on the number of vCPUs of the [sole-tenant node type](https://docs.cloud.google.com/compute/docs/nodes/sole-tenant-nodes#node_types), not the potential maximum of vCPUs available for overcommitting.

## Costs

Sole-tenant nodes that have CPU overcommit selected on their node template are charged an additional 25%. This charge is in addition to the [10% premium for running VMs on sole-tenant nodes](https://docs.cloud.google.com/compute/sole-tenant-pricing#nodes). The CPU overcommit premium is fixed, regardless of the CPU overcommit level and how many VMs are scheduled on the sole-tenant node.

Sole-tenant nodes offer [committed use discounts](https://docs.cloud.google.com/compute/docs/instances/signing-up-committed-use-discounts). [Sustained use discounts](https://docs.cloud.google.com/compute/docs/sustained-use-discounts) are available for the sole-tenancy premium and the CPU overcommit premium.

To estimate the cost of running VMs on sole-tenant nodes, see the [Pricing Calculator](https://cloud.google.com/products/calculator).

## Configure sole-tenant VMs for overcommitting

To configure sole-tenant VMs to have CPU resources available for overcommitting, do the following:

  1. Create a sole-tenant node template that has CPU overcommit enabled. You must enable CPU overcommit while creating the node template. You can't enable CPU overcommit after creating a node template.

  2. Create a sole-tenant node group based on the sole-tenant node template that has CPU overcommit enabled.

  3. Create a VM and do the following:

     1. Choose a machine type for the VM. The number of CPUs on the machine type represents the maximum number of CPUs that the VM can burst up to from the minimum number of CPUs if the minimum number of CPUs is less than the number of CPUs specified by the machine type.

You can choose a different machine type for each VM on a sole-tenant node, provided you don't exceed the CPU and memory capacity of the sole-tenant node.

     2. Specify the minimum number of CPUs to allocate to that single VM, or use a [managed instance group](https://docs.cloud.google.com/compute/docs/instance-groups#managed_instance_groups) to create multiple VMs that have the same CPU overcommit level.




## Before you begin

  * [Create a sole-tenant node template](https://docs.cloud.google.com/compute/docs/nodes/provisioning-sole-tenant-vms#create_a_sole-tenant_node_template) and specify `--cpu-overcommit-type=enabled`. 
  * [Create a sole-tenant node group](https://docs.cloud.google.com/compute/docs/nodes/provisioning-sole-tenant-vms#create_a_sole-tenant_node_group) based on the sole-tenant node template with CPU overcommit enabled. 
  * If you haven't already, set up [authentication](https://docs.cloud.google.com/compute/docs/authentication). Authentication verifies your identity for access to Google Cloud services and APIs. To run code or samples from a local development environment, you can authenticate to Compute Engine by selecting one of the following options: 

Select the tab for how you plan to use the samples on this page:

### Console

When you use the Google Cloud console to access Google Cloud services and APIs, you don't need to set up authentication. 

### gcloud

    1. [Install](https://docs.cloud.google.com/sdk/docs/install) the Google Cloud CLI. After installation, [initialize](https://docs.cloud.google.com/sdk/docs/initializing) the Google Cloud CLI by running the following command: 
           
           gcloud init

If you're using an external identity provider (IdP), you must first [ sign in to the gcloud CLI with your federated identity](https://docs.cloud.google.com/iam/docs/workforce-log-in-gcloud). 

**Note:** If you installed the gcloud CLI previously, make sure you have the latest version by running `gcloud components update`. 
    2. [ Set a default region and zone](https://docs.cloud.google.com/compute/docs/gcloud-compute#set_default_zone_and_region_in_your_local_client).

### REST

To use the REST API samples on this page in a local development environment, you use the credentials you provide to the gcloud CLI. 

[Install](https://docs.cloud.google.com/sdk/docs/install) the Google Cloud CLI. 

If you're using an external identity provider (IdP), you must first [ sign in to the gcloud CLI with your federated identity](https://docs.cloud.google.com/iam/docs/workforce-log-in-gcloud). 

For more information, see [Authenticate for using REST](https://docs.cloud.google.com/docs/authentication/rest) in the Google Cloud authentication documentation. 




## Set the CPU overcommit level

The following procedures show you how to create a sole-tenant VM with CPU resources available for overcommitting. If you need to modify the CPU overcommit level of a VM that is running, you must first stop the VM.

###  Console 

In the Google Cloud console, create a sole-tenant VM on a sole-tenant node group that was created from a sole-tenant node template that has CPU overcommit enabled:

  1. Go to the **Sole-tenant nodes** page.

[Go to Sole-tenant nodes](https://console.cloud.google.com/compute/soleTenancy)

  2. Click **Node Groups**.

  3. Click the sole-tenant node group on which to create a VM.

  4. Click **Create instance**.

  5. Specify the **Name** , **Region** , and **Zone** for the VM.

  6. Under **Machine configuration** , choose a fixed or custom **Machine type** with at least 4 vCPUs.

  7. Under **CPU overcommit** , select **Enable CPU overcommit**.

  8. Under **Minimum vCPUs Allocated** , adjust the slider or manually enter the number of vCPUs to specify the level of overcommit for the CPUs on this VM.

  9. Click **Create** to create a VM instance that has CPU resources available for overcommitting.




###  gcloud 

The following example shows how to use the [`gcloud compute instances create` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/instances/create) to create a sole-tenant VM on a predefined machine type with CPU resources available for overcommitting.
    
    
    gcloud compute instances create VM_NAME \
        --machine-type=MACHINE_TYPE \
        --min-node-cpu=MIN_VCPUS \
        --node-group=GROUP_NAME

Replace the following:

  * `VM_NAME`: the name of the VM to overcommit CPUs on.

  * `MACHINE_TYPE`: the [machine type](https://docs.cloud.google.com/compute/docs/machine-resource) to provision the sole-tenant VM on. The number of CPUs specified by the machine type is the maximum number of CPUs the VM can burst up to from MIN_VCPUS.

  * `MIN_VCPUS`: the minimum number of vCPUs guaranteed to be available to this VM.

  * `GROUP_NAME`: the name of the sole-tenant node group to provision the VM on.




**Setting the overcommit level on a custom machine type**

To create a sole-tenant VM with CPU resources available for overcommitting on a custom machine type, omit the `--machine-type` flag, and instead, use the `--custom-cpu` and `--custom-memory` flags to specify the number of CPUs and the amount of memory, in gigabytes, for the custom machine.

###  REST 

The following example shows how to use the [`instances.insert` method](https://docs.cloud.google.com/compute/docs/reference/rest/v1/instances/insert) to create a sole-tenant VM on a fixed machine type with CPU resources available for overcommitting.
    
    
    POST https://compute.googleapis.com/compute/v1/projects/PROJECT_ID/zones/ZONE/instances
    
    {
      "machineType": "zones/MACHINE_TYPE_ZONE/machineTypes/MACHINE_TYPE",
      "name": "VM_NAME",
      "scheduling": {
        "minNodeCpus": MIN_VCPUS,
        "nodeAffinities": [
          {
            "key": "compute.googleapis.com/node-group-name",
            "operator": "IN",
            "values": [
              "GROUP_NAME"
            ]
          }
        ]
      },
      ...
    }
    
    

Replace the following:

  * `PROJECT_ID`: the [ID of your project](https://docs.cloud.google.com/resource-manager/docs/creating-managing-projects#identifying_projects).

  * `ZONE`: the zone for this request.

  * `MACHINE_TYPE_ZONE`: the zone hosting the machine type.

  * `MACHINE_TYPE`: the [machine type](https://docs.cloud.google.com/compute/docs/machine-resource) to provision the sole-tenant VM on. The number of CPUs specified by the machine type is the maximum number of CPUs the VM can burst up to from `MIN_VCPUS`.

  * `VM_NAME`: the name of the sole-tenant VM to overcommit CPUs on.

  * `MIN_VCPUS`: the minimum number of vCPUs guaranteed to be available to this VM.

  * `GROUP_NAME`: the name of the sole-tenant node group to provision the VM on.




**Setting the overcommit level on a custom machine type**

To create a sole-tenant VM with CPU resources available for overcommitting on a custom machine type, replace the value for the `machineType` field with `zones/zone/machineTypes/custom-CPUS-MEMORY`, replacing `CPUS` with the number of CPUs and `MEMORY` with the amount of memory, in megabytes, for the custom machine type.

## Update the CPU overcommit level

The following procedures show you how to update the CPU overcommit level of a sole-tenant VM.

###  gcloud 

  1. To modify the CPU overcommit level of a VM that is running, you must first stop the VM. To stop a VM, use the [`gcloud compute instances stop` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/instances/stop) as follows:
         
         gcloud compute instances stop VM_NAME
         

Replace `VM_NAME` with the name of the instance that you want to stop.

  2. To update the CPU overcommit level of a sole-tenant VM, use the [`gcloud compute instances set-scheduling` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/instances/set-scheduling) as follows:
         
         gcloud compute instances set-scheduling VM_NAME \
           --min-node-cpu=MIN_VCPUS

Replace the following:

     * `VM_NAME`: the name of the sole-tenant VM to modify the CPU overcommit level.

     * `MIN_VCPUS`: the minimum number of vCPUs guaranteed to be available to this VM.

  3. Restart the VM by using the [`gcloud compute instances start` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/instances/start):
         
         gcloud compute instances start VM_NAME
         

Replace `VM_NAME` with the name of the instance that you want to restart.




###  REST 

  1. To modify the CPU overcommit level of a VM that is running, you must first stop the VM. To stop a VM, construct a `POST` request using the [`instances.stop` method](https://docs.cloud.google.com/compute/docs/reference/latest/instances/stop) as follows:
         
         POST https://compute.googleapis.com/compute/v1/projects/PROJECT_ID/zones/ZONE/instances/VM_NAME/stop
         

Replace the following:

     * `PROJECT_ID`: the [ID of your project](https://docs.cloud.google.com/resource-manager/docs/creating-managing-projects#identifying_projects).

     * `ZONE`: the zone for this request.

     * `VM_NAME`: the name of the sole-tenant VM to modify the CPU overcommit level.

  2. To update the CPU overcommit level of a sole-tenant VM, use the [`instances.setScheduling` method](https://docs.cloud.google.com/compute/docs/reference/rest/v1/instances/setScheduling) as follows:
         
         POST https://compute.googleapis.com/compute/v1/projects/PROJECT_ID/zones/ZONE/instances/VM_NAME/setScheduling
         {
         "minNodeCpus":MIN_VCPUS
         }
         

Replace the following:

     * `PROJECT_ID`: the [ID of your project](https://docs.cloud.google.com/resource-manager/docs/creating-managing-projects#identifying_projects).

     * `ZONE`: the zone for this request.

     * `VM_NAME`: the name of the sole-tenant VM to modify the CPU overcommit level.

     * `MIN_VCPUS`: the minimum number of vCPUs guaranteed to be available to this VM.

  3. Restart the VM by constructing a `POST` request using the [`instances.start` method](https://docs.cloud.google.com/compute/docs/reference/rest/v1/instances/start) as follows:
         
         POST https://compute.googleapis.com/compute/v1/projects/PROJECT_ID/zones/ZONE/instances/VM_NAME/start
         

Replace the following:

     * `PROJECT_ID`: the [ID of your project](https://docs.cloud.google.com/resource-manager/docs/creating-managing-projects#identifying_projects).

     * `ZONE`: the zone for this request.

     * `VM_NAME`: the name of the sole-tenant VM to restart.




## Disable CPU overcommitment for sole-tenant VMs

The following procedures show you how to disable the CPU overcommitment of a sole-tenant VM.

###  gcloud 

  1. To disable the CPU overcommitment of a VM that is running, you must first stop the VM. To stop a VM, use the [`gcloud compute instances stop` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/instances/stop) as follows:
         
         gcloud compute instances stop VM_NAME
         

Replace `VM_NAME` with the name of the instance that you want to stop.

  2. To disable CPU overcommitment, use the [`gcloud compute instances set-scheduling` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/instances/set-scheduling) with the `--clear-min-node-cpu` flag:
         
         gcloud compute instances set-scheduling VM_NAME \
           --clear-min-node-cpu
         

Replace `VM_NAME` with the name of the sole-tenant VM to disable CPU overcommitment.

  3. Restart the VM by using the [`gcloud compute instances start` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/instances/start):
         
         gcloud compute instances start VM_NAME
         

Replace `VM_NAME` with the name of the instance that you want to restart.




###  REST 

  1. To disable the CPU overcommitment of a VM that is running, you must first stop the VM. To stop a VM, construct a `POST` request using the [`instances.stop` method](https://docs.cloud.google.com/compute/docs/reference/rest/v1/instances/stop) as follows:
         
         POST https://compute.googleapis.com/compute/v1/projects/PROJECT_ID/zones/ZONE/instances/VM_NAME/stop
         

Replace the following:

     * `PROJECT_ID`: the [ID of your project](https://docs.cloud.google.com/resource-manager/docs/creating-managing-projects#identifying_projects).

     * `ZONE`: the zone for this request.

     * `VM_NAME`: the name of the sole-tenant VM to stop.

  2. To disable CPU overcommitment, use the [`instances.setScheduling` method](https://docs.cloud.google.com/compute/docs/reference/rest/v1/instances/setScheduling) as follows:
         
         POST https://compute.googleapis.com/compute/v1/projects/PROJECT_ID/zones/ZONE/instances/VM_NAME/setScheduling
         {
         "minNodeCpus":null
         }
         

Replace the following:

     * `PROJECT_ID`: the [ID of your project](https://docs.cloud.google.com/resource-manager/docs/creating-managing-projects#identifying_projects).

     * `ZONE`: the zone for this request.

     * `VM_NAME`: the name of the sole-tenant VM to disable CPU overcommitment.

  3. Restart the VM by constructing a `POST` request using the [`instances.start` method](https://docs.cloud.google.com/compute/docs/reference/rest/v1/instances/start) as follows:
         
         POST https://compute.googleapis.com/compute/v1/projects/PROJECT_ID/zones/ZONE/instances/VM_NAME/start
         

Replace the following:

     * `PROJECT_ID`: the [ID of your project](https://docs.cloud.google.com/resource-manager/docs/creating-managing-projects#identifying_projects).

     * `ZONE`: the zone for this request.

     * `VM_NAME`: the name of the sole-tenant VM to restart.




## View CPU usage

To check the CPU usage of sole-tenant VMs in a sole-tenant node group, do the following:

  1. In the Google Cloud console, go to the **Sole-tenant nodes** page.

[Go to Sole-tenant nodes](https://console.cloud.google.com/compute/soleTenancy)

  2. Click **Node groups**.

  3. Click the sole-tenant node group containing the sole-tenant node that has the VM with overcommitted CPUs.

  4. Click the sole-tenant node that has the VM with overcommitted CPUs.

  5. Under the name of the sole-tenant node, view the **CPU usage** , **CPU overcommit type** , and the **Min CPU usage**.

     * **CPU usage** shows the total of the maximum number of CPUs for all of the VMs on this sole-tenant node divided by the number of CPUs specified by the sole-tenant node type.

The number of CPUs on the node available for overcommitting is the numerator minus the denominator, and the overcommit level is the quotient of the numerator and the denominator.

     * **Min CPU usage** shows the sum of the minimum number of CPUs allocated for all of the VMs on a sole-tenant node divided by the number of CPUs specified by the node type.




## Optimize CPU overcommit levels

To help optimize tuning of your CPU overcommit levels, Compute Engine provides the **Scheduler Wait Time** metric. The **Scheduler Wait Time** metric indicates the aggregate wait time for all vCPUs on the VM and helps you determine the impact of CPU overcommit on the VM's performance.

Workload sensitivity varies, but a general rule is to use 20 milliseconds of scheduler wait time accrued per second (20 msps) as the maximum wait time for each vCPU. For example, if a VM is set to 8 vCPUs, then a rule-of-thumb threshold is 160 msps, which results in an acceptable average **Scheduler Wait Time** of 20 msps per vCPU. The performance requirements of your workload will ultimately dictate acceptable thresholds.

  1. In the Google Cloud console, go to the **Monitoring** page.

[Go to Monitoring](https://console.cloud.google.com/monitoring)

  2. Click **Metrics explorer**.

  3. In the **Resource type** field, enter **VM Instance**.

  4. In the **Metric** field, enter **Scheduler Wait Time**.

  5. Optionally, set up alerting to trigger alerts for VM wait time thresholds by clicking **Alerting**.




## What's next

  * [Learn more about sole-tenant nodes](https://docs.cloud.google.com/compute/docs/nodes/sole-tenant-nodes)

  * [Learn how to bring your own licenses](https://docs.cloud.google.com/compute/docs/nodes/bringing-your-own-licenses)




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
