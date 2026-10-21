---
url: https://docs.cloud.google.com/compute/docs/instances/customize-visible-cores/
title: Customize the number of visible CPU cores \u00a0|\u00a0 Compute Engine \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T13:25:26.029971+00:00
---

# Customize the number of visible CPU cores  |  Compute Engine  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/compute/docs/instances/customize-visible-cores/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ Compute Engine ](https://docs.cloud.google.com/compute/docs)
  * [ Guides ](https://docs.cloud.google.com/compute/docs/overview)



Send feedback 

#  Customize the number of visible CPU cores Stay organized with collections  Save and categorize content based on your preferences. 

Linux  Windows 

Customizing the number of visible CPU cores can provide granular control over licensing costs, while maintaining the performance of networking and persistent disks. This customization reduces the number of vCPUs that are available to the virtual machine (VM) instance; it doesn't change the machine type or price.

Compute Engine implements each virtual CPU (vCPU) as a single hardware multithread that runs on a physical CPU core. To reduce the number of vCPUs that are available to a VM, Compute Engine lets you customize the number of visible CPU cores.

Visible cores are the CPU cores in the underlying hardware that your VMs consume. By default, the number of CPU cores that are visible to a VM is the number of vCPUs on the machine type divided by the number of [threads per core](https://docs.cloud.google.com/compute/docs/instances/set-threads-per-core):

`Visible CPU cores` = `vCPUs` on the machine type / `threads per core`

For example, the `c2-standard-60` machine type specifies 60 vCPUs. Assuming the default of 2 threads per core, the number of visible CPU cores is 30. If you reduce the number of visible cores from 30 to 20, the number of functional vCPUs is reduced from 60 to 40.

Consider customizing the number of visible CPU cores if both of the following apply:

  * You run software, such as [Windows Server or SQL Server](https://docs.cloud.google.com/compute/disks-image-pricing#premiumimages), that is licensed based on the number of available vCPUs.

  * You use [predefined machine types](https://docs.cloud.google.com/compute/docs/machine-resource), which don't let you modify the number of vCPUs or the amount of RAM.




Before customizing the number of vCPUs that are available to a VM, first consider using a [custom machine type](https://docs.cloud.google.com/compute/docs/general-purpose-machines#custom_machine_types).

### Required roles

To get the permissions that you need to customize the number of visible CPU cores, ask your administrator to grant you the [Compute Instance Admin (v1) ](https://docs.cloud.google.com/iam/docs/roles-permissions/compute#compute.instanceAdmin.v1) (`roles/compute.instanceAdmin.v1`) IAM role on the project. For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

This predefined role contains the permissions required to customize the number of visible CPU cores. To see the exact permissions that are required, expand the **Required permissions** section: 

#### Required permissions

The following permissions are required to customize the number of visible CPU cores:

  * To customize the number of visible CPU cores during VM creation: 
    * `compute.instances.create` on the project
    * To use a custom image to create the VM: `compute.images.useReadOnly` on the image
    * To use a snapshot to create the VM: `compute.snapshots.useReadOnly` on the snapshot
    * To use an instance template to create the VM: `compute.instanceTemplates.useReadOnly` on the instance template
    * To assign a [legacy network](https://docs.cloud.google.com/vpc/docs/legacy) to the VM: `compute.networks.use` on the project
    * To specify a static IP address for the VM: `compute.addresses.use` on the project
    * To assign an external IP address to the VM when using a legacy network: `compute.networks.useExternalIp` on the project
    * To specify a subnet for the VM: `compute.subnetworks.use` on the project or on the chosen subnet
    * To assign an external IP address to the VM when using a VPC network: `compute.subnetworks.useExternalIp` on the project or on the chosen subnet
    * To set VM instance metadata for the VM: `compute.instances.setMetadata` on the project
    * To set tags for the VM: `compute.instances.setTags` on the VM
    * To set labels for the VM: `compute.instances.setLabels` on the VM
    * To set a service account for the VM to use: `compute.instances.setServiceAccount` on the VM
    * To create a new disk for the VM: `compute.disks.create` on the project
    * To attach an existing disk in read-only or read-write mode: `compute.disks.use` on the disk
    * To attach an existing disk in read-only mode: `compute.disks.useReadOnly` on the disk
  * To customize the number of visible CPU cores on a group of VMs by using an instance template: You need all the permissions you would use during VM creation and the `compute.instanceTemplates.create` on the project 



You might also be able to get these permissions with [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

## vCPUs and the number of threads per core

The total vCPUs on a machine type is the number of visible CPU cores multiplied by the number of threads per core. For most machine series, the number of threads per core is 2, but you can [manually set the number of threads per core](https://docs.cloud.google.com/compute/docs/instances/set-threads-per-core) to 1.

The following table shows how visible CPU cores, number of threads per core, and total available vCPUs are related using the `c2-standard-60` machine type as an example.

Machine type | Visible CPU cores | Threads per core | Available vCPUs  
---|---|---|---  
`c2-standard-60` | `30` (default) | `2` (default) | `60`  
`c2-standard-60` | `30` (default) | `1` | `30`  
`c2-standard-60` | `20` | `2` (default) | `40`  
`c2-standard-60` | `20` | `1` | `20`  
  
## Performance considerations

This section explains how reducing the number of visible cores can impact the performance of your VM.

#### Persistent disk

The performance limits of persistent disks depend on the machine type and aren't affected by the number of visible CPU cores. For more information, see [Block storage performance](https://docs.cloud.google.com/compute/docs/disks/performance#machine-type-disk-limits).

#### Networking egress

The bandwidth limits of networking egress match the machine type and aren't affected by the number of visible CPU cores. However, networking performance does vary depending on the number of vCPUs that are accessible to the VM. For example, a `n2-standard-16` machine type with one visible CPU core might not be able to fully use a 32 Gbps connection.

## Pricing

This section explains how reducing the number of visible cores can impact the cost of your VMs.

#### Operating system licensing costs

You can lower licensing costs for some operating systems by reducing the number of visible CPU cores. Applicable operating systems are those that charge you for each vCPU that is available to the VM; for example, Windows Server and SQL Server. For more information about the licensing options for these operating systems on Compute Engine, see [Microsoft licenses](https://docs.cloud.google.com/compute/docs/instances/windows/ms-licensing).

#### VM costs, quota, and capacity

VM costs, quota, and capacity remain the same when you customize the number of visible CPU cores because Compute Engine charges, tracks quota, and allocates space on machine types for VMs as if they are using the number of CPU cores of the machine type. For more information about how Compute Engine bills for VMs, see [VM instance pricing](https://cloud.google.com/compute/vm-instance-pricing).

## Limitations

  * You cannot customize the number of visible CPU cores while a VM is in the `RUNNING` state. For more information about VM states, see [VM instance lifecycle](https://docs.cloud.google.com/compute/docs/instances/instance-lifecycle).

  * In the Google Cloud console, when the number of visible cores is reduced, the CPU utilization metric can't scale up to 100%. It is limited to the number of visible CPU cores divided by the maximum number of CPU cores.

  * You can't use this feature to customize the number of visible CPU cores for [bare metal instances](https://docs.cloud.google.com/compute/docs/instances/bare-metal-instances).




## Supported machine types and valid values for each

Many [machine types](https://docs.cloud.google.com/compute/docs/machine-resource) support customization of the number of visible CPU cores. The value for the visible CPU core count must be a whole number. The maximum value is the number of vCPUs—or GPUs for accelerator-optimized machine types—on the machine type divided by the number of [threads per core](https://docs.cloud.google.com/compute/docs/instances/set-threads-per-core) for the VM.

The following table shows the machine types that support this customization, along with the corresponding valid values for visible CPU cores for machine types in those families.

Machine type family | Predefined vCPU count* | Valid values for visible CPU cores  
---|---|---  
General-purpose  
C4 | 4, 8, 16, 24, 32, 48 | Any  
C4 | 96 | Multiples of 2  
C4 | 144 | Multiples of 3  
C4 | 192 | Multiples of 4  
C4 | 288 | Multiples of 6  
C4D | ≤ 192 | Any  
C4D | > 192 | Multiples of 2  
C4N | ≤ 48 | Any  
C4N | 96 | Multiples of 2  
C4N | > 96 | Multiples of 4  
C3D | ≤ 180 | Any  
C3D | 360 | Multiples of 2  
C3 | 4, 8, 22, 44 | Multiples of 1  
C3 | 88 | Multiples of 2  
C3 | 176 | Multiples of 4  
E2 | ≤ 32 | Any  
N2 | ≤ 32 | Any  
N2 | > 32 | Multiples of 2  
N2D | ≤ 24 | Any  
N2D | > 24 | Multiples of 2  
N4 | ≤ 80 | Any  
N4D | ≤ 96 | Any  
N1 | ≤ 64 | Any  
N1 | > 64 | Multiples of 2  
N1 (TPU optimized) | 48 | Any  
N1 (TPU optimized) | 96 | Multiples of 2  
Storage-optimized  
Z4D | ≤ 192 | Any  
Z4D | 384 | Multiples of 2  
Z3 | ≤ 44 | Any  
Z3 | 88 | Multiples of 2  
Z3 | 176 | Multiples of 4  
Compute-optimized  
H4D | 192 | Multiples of 4  
H3 | 88 | Multiples of 4  
C2 | 4, 8, 16, 30 | Any  
C2 | 60 | Multiples of 2  
Memory-optimized  
M4N | 16, 28, 32, 56 | Any  
M4N | 64, 112 | Multiples of 2  
M4N | 224 | Multiples of 4  
M4 | 16, 28, 32, 56 | Any  
M4 | 64, 112 | Multiples of 2  
M4 | 224 | Multiples of 4  
M3 | 128 | Multiples of 2  
M3 | 32, 64 | Any  
M2 | 208 | Multiples of 4  
M2 | 416 | Multiples of 8  
M1 | 40 | Any  
M1 | 80, 96 | Multiples of 2  
M1 | 160 | Multiples of 4  
Accelerator-optimized  
A4 | 224 | Multiples of 2  
A3 | 26, 52, 104, 208, 224 | Multiples of 2  
A2 | ≤ 48 | Any  
A2 | 96 | Multiples of 2  
G2 | ≤ 48 | Any  
G2 | 96 | Multiples of 2  
G4 | All machine types | Multiples of 2  
  
* The name for most machine types contain the vCPU count. However, for accelerator-optimized machine types other than G2 and G4, the name for the machine type contains the predefined GPU count. To see the vCPU count for the accelerator-optimized machine types, review the [Accelerator-optimized machine family](https://docs.cloud.google.com/compute/docs/accelerator-optimized-machines) documentation.

## Customize the number of visible CPU cores during VM creation

To customize the number of visible CPU cores while creating a single VM, follow the steps explained in this section.

The following example shows how to create a SQL Server VM with a reduced number of visible CPU cores.

###  Console 

To customize the number of visible CPU cores while creating a VM, do the following:

  * In **Machine configuration** > **Advanced configurations** > **Visible core count** , select the number of visible cores.



###  gcloud 

To create a SQL Server VM with a reduced number of visible CPU cores, use the following [`gcloud compute instances create` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/instances/create):
    
    
    gcloud compute instances create VM_NAME \
        --image-project=windows-sql-cloud \
        --image-family=sql-ent-2019-win-2019 \
        --machine-type=MACHINE_TYPE \
        --visible-core-count=VISIBLE_CORE_COUNT \
        --zone=ZONE
    

Replace the following:

  * `VM_NAME`: the name of the VM.

  * `MACHINE_TYPE`: a supported machine type, for example, `c2-standard-60`.

  * `VISIBLE_CORE_COUNT`: the number of visible CPU cores. For example, when using the `c2-standard-60` machine type, if set to `20`, and the number of threads per core is `2`, 40 of the 60 CPUs are visible.

  * `ZONE`: the zone to create the VM in.




###  REST 

To create a SQL Server VM with a reduced number of visible CPU cores, use the following [`instances.insert` method](https://docs.cloud.google.com/compute/docs/reference/rest/v1/instances/insert):
    
    
    POST https://compute.googleapis.com/compute/v1/projects/PROJECT_ID/zones/ZONE/instances
    
    {
      "name": "VM_NAME",
      ...
      "advanced_machine_features": {
        ...
        "visibleCoreCount": "VISIBLE_CORE_COUNT"
      },
      ...
    }
    

Replace the following:

  * `PROJECT_ID`: the ID of the project.

  * `ZONE`: the zone in which to create the VM.

  * `VM_NAME`: the name of the VM.

  * `VISIBLE_CORE_COUNT`: the number of visible CPU cores. For example, when using the `c2-standard-60` machine type, if set to `20`, and the number of threads per core is `2`, 40 of the 60 CPUs are visible.




## Customize the number of visible CPU cores on a group of VMs by using an instance template

To customize the number of visible CPU cores while creating a VM by using an instance template, follow the steps explained in this section.

The following example shows how to create a group of identical SQL Server VMs with a reduced number of visible CPU cores by using an instance template.

###  Console 

To customize the number of visible CPU cores while creating an instance template, do the following:

  * In **Machine configuration** > **Advanced configurations** > **Visible core count** , select the number of visible cores.



###  gcloud 

  1. Create an instance template for SQL Server VMs, each with a reduced number of visible CPU cores, by using the following [`gcloud compute instance-templates create` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/instance-templates/create):
         
         gcloud compute instance-templates create INSTANCE_TEMPLATE_NAME \
            --image-project=windows-sql-cloud \
            --image-family=sql-ent-2019-win-2019 \
            --machine-type=MACHINE_TYPE \
            --visible-core-count=VISIBLE_CORE_COUNT \
            --zone=ZONE
         

Replace the following:

     * `INSTANCE_TEMPLATE_NAME`: the name of the instance template.

     * `MACHINE_TYPE`: a supported machine type, for example, `c2-standard-60`.

     * `VISIBLE_CORE_COUNT`: the number of visible CPU cores. For example, when using the `c2-standard-60` machine type, if set to `20`, and the number of threads per core is `2`, 40 of the 60 CPUs are visible.

     * `ZONE`: the zone to create the VMs in.

  2. Create the SQL Server VMs, each with a reduced number of visible CPU cores, by using the following [`gcloud compute instances create` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/instances/create):
         
         gcloud compute instances create INSTANCE_NAMES \
            --source-instance-template=INSTANCE_TEMPLATE_NAME
         

Replace the following:

     * `INSTANCE_NAMES`: the names of the VMs, separated by spaces, to create from the instance template

     * `INSTANCE_TEMPLATE_NAME`: the name of the instance template from which to create the VMs




###  REST 

  1. Create an instance template for SQL Server VMs, each with a reduced number of visible CPU cores, by using the following [`instanceTemplates.insert` method](https://docs.cloud.google.com/compute/docs/reference/rest/v1/instanceTemplates/insert):
         
         POST https://compute.googleapis.com/compute/v1/projects/PROJECT_ID/global/instanceTemplates
         
         {
          "name": "INSTANCE_TEMPLATE_NAME",
          ...
          "advanced_machine_features": {
            ...
            "visible_core_count": "VISIBLE_CORE_COUNT"
          },
          ...
         }
         

Replace the following:

     * `PROJECT_ID`: the ID of the project.

     * `INSTANCE_TEMPLATE_NAME`: the name of the instance template.

     * `VISIBLE_CORE_COUNT`: the number of visible CPU cores. For example, when using the `c2-standard-60` machine type, if set to `20`, and the number of threads per core is `2`, 40 of the 60 CPUs are visible.

  2. Create the SQL Server VMs, each with a reduced number of visible CPU cores, by using the following [`instances.insert` method](https://docs.cloud.google.com/compute/docs/reference/rest/v1/instances/insert):
         
         POST https://compute.googleapis.com/compute/v1/projects/PROJECT_ID/zones/ZONE/instances?sourceInstanceTemplate=INSTANCE_TEMPLATE_NAME
         
         {
          "name": "VM_NAME",
          ...
         }
         

Replace the following:

     * `PROJECT_ID`: the ID of the project

     * `ZONE`: the zone to create the VM in

     * `INSTANCE_TEMPLATE_NAME`: the name of the instance template from which to create the VMs

     * `VM_NAME`: the name of the VM to create from the instance template




## Customize the number of visible CPU cores

To customize the number of visible CPU cores on an existing VM, follow the steps explained in this section.

If you customized the number of visible CPU cores on a group of VMs by using an instance template, you must create a new instance template and then create new VMs from that instance template. For more information about instance templates, see [Instance templates](https://docs.cloud.google.com/compute/docs/instance-templates).

###  Console 

To customize the number of visible CPU cores on an existing VM, do the following:

  1. Stop the VM.

  2. In **Machine configuration** > **Advanced configurations** > **Visible core count** , select the number of visible cores.

  3. Restart the VM.




###  gcloud 

To update the value for the number of visible CPU cores on an existing VM, use the following steps. For more information, see [Update instance properties](https://docs.cloud.google.com/compute/docs/instances/update-instance-properties#update).

  1. Export the existing VM properties to a file by using the [`gcloud compute instances export` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/instances/export).

  2. In the file containing the exported properties, modify or add the value for the following:
         
         advancedMachineFeatures:
          visibleCoreCount: VISIBLE_CORE_COUNT
         

  3. Update the VM's properties by using the [`gcloud compute instances update-from-file` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/instances/update-from-file) with `--most-disruptive-allowed-action=RESTART`.




###  REST 

To update the visible CPU core count of the VM, use the following [`instances.update` method](https://docs.cloud.google.com/compute/docs/reference/rest/v1/instances/update):
    
    
    PUT https://compute.googleapis.com/compute/v1/projects/PROJECT_ID/zones/ZONE/instances/VM_NAME?most_disruptive_allowed_action=RESTART
    
    {
      ...
      "advanced_machine_features": {
        ...
        "visible_core_count": "VISIBLE_CORE_COUNT"
      },
      ...
    }
    

Replace the following:

  * `PROJECT_ID`: the ID of the project

  * `ZONE`: the zone that contains the VM

  * `VM_NAME`: the name of the VM from which to export properties

  * `VISIBLE_CORE_COUNT`: the number of visible CPU cores




## What's next

  * Learn how to [view the number of visible CPU cores](https://docs.cloud.google.com/compute/docs/instances/view-visible-cores).

  * Learn about the [licensing options for Microsoft software](https://docs.cloud.google.com/compute/docs/instances/windows/ms-licensing).

  * Learn how to [set the number of threads per core](https://docs.cloud.google.com/compute/docs/instances/set-threads-per-core).

  * Learn about the [operating systems that you can run on Compute Engine VMs](https://docs.cloud.google.com/compute/docs/images/os-details).




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
