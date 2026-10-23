---
url: https://docs.cloud.google.com/compute/docs/tutorials/migrate-workload-to-stateful-mig/
title: Migrate an existing workload to a stateful managed instance group \u00a0|\u00a0 Compute Engine \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T12:57:02.641762+00:00
---

# Migrate an existing workload to a stateful managed instance group  |  Compute Engine  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/compute/docs/tutorials/migrate-workload-to-stateful-mig/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ Compute Engine ](https://docs.cloud.google.com/compute/docs)
  * [ Guides ](https://docs.cloud.google.com/compute/docs/overview)



Send feedback 

#  Migrate an existing workload to a stateful managed instance group Stay organized with collections  Save and categorize content based on your preferences. 

If you have an existing stateful application on standalone (unmanaged) Compute Engine virtual machine (VM) instances, you can migrate that application to a [stateful managed instance group (MIG)](https://docs.cloud.google.com/compute/docs/instance-groups/stateful-migs).

By configuring a stateful MIG and using managed instances, you can get the following benefits:

  * Preserved state: preservation of instance names, disks, and metadata even if an instance is recreated.
  * Autohealing: automatic recreation of VMs with failed workloads within the same zone.
  * Automated updates: graceful deployments of new instance configurations or software versions to VMs in a MIG.

**Note:** This document provides step-by-step instructions and conceptual information. If you want to automate the migration with a Python3 script, see [How to migrate a group of individual instances to a stateful MIG using Python script](https://cloud.google.com/blog/topics/developers-practitioners/how-migrate-group-individual-instances-stateful-mig-using-python-script) or the [migration script on GitHub](https://github.com/GoogleCloudPlatform/compute-migration-scripts/tree/main/instances-to-stateful-mig).

## Limitations

  * You must stop your existing VMs to migrate their existing disks or, alternatively, to take consistent snapshots for use by the new managed instances.
  * You must delete existing VMs if you want to reuse their VM names.
  * Your application must be capable of running on VMs with the same machine type. If your existing application requires multiple instances of different machine types, create multiple instance templates and MIGs, one per machine type.
  * Your application must start when the VM starts. You can use a custom image or a startup script. Each option is discussed below.
  * You cannot update operating system or software by rolling out boot image updates in a MIG if you choose to create stateful boot disks.
  * You can achieve multi-zone high availability only by creating redundant replicas in multiple zones and by configuring application-level data replication. Stateful MIG autoheals instances within the same zone only and does not orchestrate cross-zone failover.
  * You cannot use autoscaling with a stateful MIG.
  * Review the stateful MIG [limitations](https://docs.cloud.google.com/compute/docs/instance-groups/configuring-stateful-migs#limitations).



## Costs

This tutorial uses billable components of Google Cloud including: 

  * Compute Engine



Use the [pricing calculator](https://cloud.google.com/products/calculator/) to generate a cost estimate based on your projected usage.

## Before you begin

This guide uses the gcloud CLI. You can access this tool using [Cloud Shell](https://docs.cloud.google.com/shell/docs/using-cloud-shell). Or, if you want to run the gcloud CLI on your local computer instead, [download and install the latest gcloud CLI](https://docs.cloud.google.com/sdk/docs#install_the_latest_cloud_sdk_version).

## Migration overview

  1. Understand the components that make up a stateful MIG.
  2. Review your existing setup to determine common VM specifications.
  3. Optionally, create a custom image to serve as a common boot disk image.
  4. Create an instance template to specify common VM configuration for the MIG.
  5. Create an empty MIG.
  6. Convert your existing VMs into managed instances in the MIG, including per-instance configurations.
  7. Configure autohealing for the MIG to improve your application's resilience.
  8. Optionally, to reduce configuration overhead, replace per-instance configurations with a stateful policy.



## Components

You configure your stateful MIG's managed instances through several components:

  * An [instance template](https://docs.cloud.google.com/compute/docs/instance-templates) contains common configuration for VMs in the MIG, including machine type, boot disk image, optional specifications for additional disks, and an optional [startup script](https://docs.cloud.google.com/compute/docs/instances/startup-scripts).
  * An optional [custom image](https://docs.cloud.google.com/compute/docs/images#custom_images) contains your application and serves as a common boot disk image.
  * A [per-instance configuration](https://docs.cloud.google.com/compute/docs/instance-groups/stateful-migs#per_instance_configs) contains instance-specific stateful items. For example, you can attach an existing disk to a specific instance in the group. This disk might be detached from an existing standalone instance, recovered from a snapshot, or a regional disk. The disk's device name does not need to be defined in your instance template.
  * An optional [stateful policy](https://docs.cloud.google.com/compute/docs/instance-groups/stateful-migs#stateful_policy) contains common stateful items. For example, it defines all disks with a specific device name (as defined in the instance template) as stateful for all instances in the group.



### Which components do you need to use?

The components that you need to use depends on your existing setup. The following table provides a high-level summary of some possible configurations for an application that runs on one or multiple instances. Later in this tutorial you'll review your existing setup to determine which of these configurations you need to use.

Do you have any stateful data or configuration on your boot disks that you must maintain? | How does your application start? |   
---|---|---  
| Application is configured on an existing boot disk | Application is configured with a startup script  
No: boot disks are stateless | 

  1. Use an instance template with a custom image
  2. Add per-instance configurations (or a stateful policy) for stateful data disks

| 

  1. Use an instance template with a startup script
  2. Add per-instance configurations (or a stateful policy) for stateful data disks

  
Yes: at least one boot disk is stateful | 

  1. Use an instance template with a custom image
  2. Add per-instance configurations (or a stateful policy) for stateful boot and data disks

| 

  1. Use an instance template with a startup script
  2. Add per-instance configurations (or a stateful policy) for stateful boot and data disks

  
  
## Review your existing setup

Review your existing standalone instances to inspect each instance's machine type, disks, and metadata.

Use the [`instances describe` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/instances/describe) for each of your instances.
    
    
    gcloud compute instances describe INSTANCE_NAME
    

Answer the following questions to prepare for subsequent steps in this guide.

**Questions** | **Implications**  
---|---  
**VM properties** |   
What is the machine type that you want to use for your group? | Specify this machine type in your MIG's instance template.  
How does your application start: is it pre-configured on a boot disk or is it installed, configured, and launched by a startup script? | If your application is pre-configured on a boot disk, create a custom image then specify that image in your MIG's instance template.  
  
If your application is launched by a startup script, specify that startup script in your MIG's instance template.  
  
If your application requires both a custom boot disk image and a startup script, specify both in the instance template.   
Do you want to preserve existing instance names? | You must delete existing standalone instances to free up the instance names.  
  
If your boot disks remain stateless and if you ever want to use automated rolling updates in your MIG, review the documentation for [Preserving instance names](https://docs.cloud.google.com/compute/docs/instance-groups/rolling-out-updates-to-managed-instance-groups#preserving_instance_names).   
**Stateful items** |   
For each instance, is there any instance-specific metadata that you need to preserve? | Specify instance-specific metadata using per-instance configurations.  
Are your boot disks stateful? In other words, is there any data that lives on any boot disk that you must preserve the state of? | If you need to preserve the state of your boot disks, then you cannot update operating system or software by rolling out boot disk image updates.   
**Pro Tip:** Consider storing data on an additional persistent disk and keeping the boot disk, containing the application, stateless. Such a configuration makes your application resilient to boot disk file system corruption. This configuration also simplifies VM updates because the MIG can recreate boot disks based on the immutable source image that you specify in the MIG's instance template.  
Do all of the instances have the same kinds of disks? For example, do they all have one data disk? Or do they have and require unique disk configurations?  |  If all instances have a common disk configuration, then define those common device names in your instance template–for example, `data-disk`. This lets you use a stateful policy to declare those disks as stateful across your MIG, with less overhead than per-instance configurations.   
If you were to grow the group, is the size of the current disks sufficient? | Specify the disk sizes you need in your instance template. New instances will get the disks you specify, provided those disks are not redefined in a stateful policy or per-instance configurations.  
  
This guide starts by creating per-instance configurations for existing stateful disks. But you can convert those configurations to a stateful policy later provided that the disks have common device names that you declare in the group's instance template.

### Example setup

This guide uses the following basic example to illustrate the migration steps. Suppose you have a stateful application running on three standalone Compute Engine VMs. Assume the following VM specifications:

  * Each VM has the same machine type.
  * Each VM exists in the same project and zone.
  * Each VM's boot disk has the same application, which is configured on the boot disk to start when the VM starts.
  * Each VM's boot disk does not contain any other data or configuration that you must preserve.
  * Each VM has a secondary persistent disk with stateful data, that is, data for which you must maintain the current state.



Edit the values below for use throughout this tutorial.
    
    
    - Machine type: n2-standard-2
    - Project: my-project
    - Zone: europe-west1-c
    - Name of one of the VMs to migrate: my-instance-1
    

## Create a custom image

If your application or any of its requirements are already configured on an existing boot disk, create a custom image that you can reuse. Alternatively, if your application is installed, configured, and launched solely by using a startup script, skip this step and proceed to Create an instance template.

In the example scenario discussed earlier, the boot disk of each existing standalone VM contains the configured application. So you can follow the steps to [create a custom image](https://docs.cloud.google.com/compute/docs/images/create-custom#creating_a_custom_image) based on any one of those VMs.

  1. Stop one of the instances.
         
         gcloud compute instances stop my-instance-1

  2. Determine the source for the disk by describing the instance.
         
         gcloud compute instances describe my-instance-1

The output is similar to the following:
         
         ...
         disks:
         – autoDelete: true
           **boot: true
           ...
           source: https://www.googleapis.com/compute/v1/projects/ my-project/zones/europe-west1-c/disks/my-instance-1**
           ...
         

Locate the `source` field in the output, and note the full URL of the boot disk in that field.

  3. Use the [`images create` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/images/create) to prepare a custom image that uses the same source.
         
         gcloud compute images create my-boot-image \
             --source-disk=https://www.googleapis.com/compute/v1/projects/my-project/zones/europe-west1-c/disks/my-instance-1
         

The output is similar to the following:
         
         Created [https://www.googleapis.com/compute/v1/projects/my-project/global/images/my-boot-image].
         




## Create an instance template

An instance template is an immutable Compute Engine resource that stores VM configuration. Once you create a template, you cannot update it. If you need to change it later, create a new template then roll out the new template to the group.

Follow the steps in [Creating a new instance template](https://docs.cloud.google.com/compute/docs/instance-templates/create-instance-templates#creating_a_new_instance_template), using the following settings.

  * **Machine type** : Specify a [machine type](https://docs.cloud.google.com/compute/docs/machine-resource) that works for all of your existing instances.

  * **Startup script** : If you launch your application using a startup script, specify that script.

  * **Boot disk** :

    * **Image** : Specify a common boot disk image for all VMs in the MIG. For example, if you created a custom image based on an existing VM's boot disk, specify that. If you need to use an existing boot disk for a specific VM, you can explicitly specify the boot disk for that VM with a per-instance configuration, when you convert that VM to a managed instance, as explained later in this document.
    * **Device name** : Specify a device name that reflects the purpose of the disk–for example, `boot-disk`. This lets you configure a single stateful policy to preserve all disks in the MIG with that device name.
    * **Size** : Specify a boot disk size that is sufficient for existing instances as well as future instances, in case you want to add any.
  * **Additional disks** : By default, when you add instances to the MIG, the MIG creates disks based on the template. Note that an instance template does not support configuring regional disks, but you can configure regional disks later using per-instance configurations instead.

    * **Device name** : For each disk, specify a device name that reflects the purpose of the disk–for example, `data-disk`.
    * **Size** : Specify a disk size that is sufficient for future instances, in case you add any.



For the purpose of this migration, the specification that matters most for each additional disk is the device name, which you will use as a key for specifying which disks are stateful. Having a common device name for similar disks enables you to use a common stateful policy to preserve all of those disks across the MIG. The specification of size or image for additional disks in the instance template will only be used for creating new disks for new instances that you might create beyond those that you are migrating. When migrating existing instances, you will preserve existing data disks by detaching them from the original instances and then re-attaching those same disks to the new managed instances, as explained later in this document.

**Pro Tip:** Specify custom device names for your disks, such as `boot-disk` or `data-disk`, instead of using autogenerated names. Meaningful device names make your stateful configuration easier to set up, read, and understand.

The following [`instance-templates create` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/instance-templates/create) creates a template for the example scenario. The command includes an `--image` flag that points to the custom boot image created earlier, as well as an additional data disk.
    
    
    gcloud compute instance-templates create my-instance-template \
     --machine-type=n2-standard-2 \
     --image=https://www.googleapis.com/compute/v1/projects/my-project/global/images/my-boot-image \
     --boot-disk-device-name=boot-disk \
     --create-disk=mode=rw,size=100,type=pd-standard,device-name=data-disk
    

The output is similar to the following:
    
    
    Created [https://www.googleapis.com/compute/v1/projects/my-project/global/instanceTemplates/my-instance-template].
    NAME                     MACHINE_TYPE   PREEMPTIBLE  CREATION_TIMESTAMP
    my-instance-template  n2-standard-2               2021-04-27T11:02:07.552-07:00
    

Note the URL of the template, which you can find in the first line of the output.

## Create a managed instance group

The next step is to create a managed instance group (MIG). To create a single-zone MIG, follow the instructions to [Create a MIG in a single zone](https://docs.cloud.google.com/compute/docs/instance-groups/create-zonal-mig). Or, if you want to protect against zonal failure by using a regional MIG, follow the instructions to [Create a MIG with VMs in multiple zones in a region](https://docs.cloud.google.com/compute/docs/instance-groups/distributing-instances-with-regional-instance-groups).

**Note:** Regional managed instance groups do not perform automatic stateful cross-zone failover. If your application supports data replication, then you can achieve resilience against zonal failure by doing the following: 

  * Create a regional MIG with redundant VM replicas in multiple zones.
  * Add the MIG to a [load balancer](https://docs.cloud.google.com/compute/docs/instance-groups/adding-an-instance-group-to-a-load-balancer). 
  * Rely on application-level data replication across instances in different zones. In the event of a zonal failure, the VM instances in the failed zone become unavailable. However your users are still served by the available replicas in the healthy zones.

Examples of applications that support this approach include Cassandra, ElasticSearch, and Kafka. 

When you create your MIG, include the following specifications:

  * Set the group size to `0`. You will add instances later.
  * If you are creating a regional MIG, set the [instance redistribution type](https://docs.cloud.google.com/compute/docs/instance-groups/regional-mig-enable-disable-proactive-redistribution) to `NONE` so that the MIG does not automatically redistribute instances across zones.



The following [`instance-groups managed create` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/instance-groups/managed/create) creates a zonal MIG for the example setup described earlier. To create a regional MIG, replace `--zone=ZONE` with `--region=REGION`.
    
    
    gcloud compute instance-groups managed create my-mig \
        --size=0 \
        --template=https://www.googleapis.com/compute/v1/projects/my-project/global/instanceTemplates/my-instance-template \
        --zone=europe-west1-c
    

The output is similar to the following:
    
    
    Created [https://www.googleapis.com/compute/v1/projects/my-project/zones/europe-west1-c/instanceGroupManagers/my-mig].
    NAME    LOCATION        SCOPE  BASE_INSTANCE_NAME  SIZE  TARGET_SIZE  INSTANCE_TEMPLATE         AUTOSCALED
    my-mig  europe-west1-c  zone   my-mig              0     0            my-instance-template      no
    

After creating that resource you can use it to interact with the MIG, for example to set policies on the group, and to add or remove instances from the group.

## Convert existing VMs to managed instances

For each of your existing unmanaged VMs, use the following procedure to turn it into a managed instance in your MIG. This procedure migrates existing disks to the new managed instances. Alternatively, you can [create snapshots](https://docs.cloud.google.com/compute/docs/disks/create-snapshots#creating_snapshots) of existing disks and then [create disks based on those snapshots](https://docs.cloud.google.com/compute/docs/disks/restore-snapshot#create-disk-from-snapshot) for use by the managed instances.

  1. Describe the existing VM.
         
         gcloud compute instances describe my-instance-1
         

Make a note of items that you want to preserve from the existing VM, which can include the following:

     * Instance name
     * Boot disk
     * Secondary disks
     * Instance metadata
  2. Stop the existing VM.
         
         gcloud compute instances stop my-instance-1
         

  3. Detach all stateful disks, including the boot disk if you plan to reuse it.
         
         gcloud compute instances detach-disk my-instance-1 --disk=my-data-disk-1
         

  4. Delete the existing VM so that you can create another one with the same name. If you don't want to preserve instance names, you can delete the existing VM later to stop paying for it.
         
         gcloud compute instances delete my-instance-1
         

  5. Follow the steps to [create a managed instance](https://docs.cloud.google.com/compute/docs/instance-groups/add-remove-vms-in-mig#creating_instances_with_specific_names_in_migs).

     * You can reuse the name of the original instance if you have deleted the original instance. Or provide a new name.
     * Specify stateful disks or metadata that this managed instance requires. The MIG stores these instance-specific items in a per-instance configuration:

       * Specify one or more disks, such as disks that were detached from the original VM instance.

**Tip:** Set the same device name for disks that serve the same purpose across the instances. For example, set the device name to `data-disk` for similar data disks in each instance.
       * Specify metadata from the original VM instance.

For example, the following command creates a managed instance with the same name as the original VM and reuses the original data disk. The boot disk for the VM is created from the image that's specified in the group's instance template.
    
    gcloud compute instance-groups managed create-instance my-mig \
        --instance=my-instance-1    \
        --stateful-metadata=role=primary      \
        --stateful-disk=device-name=data-disk,source=https://www.googleapis.com/compute/v1/projects/my-project/zones/europe-west1-c/disks/my-data-disk-1 \
        --zone=europe-west1-c
    

If you need to reuse a boot disk from an old VM, use the same command with an additional `--stateful-disk` flag. Use the same device name for the boot disk as you specified in the instance template–for example:
    
    gcloud compute instance-groups managed create-instance my-mig \
        --instance=my-instance-1 \
        --stateful-metadata=role=secondary    \
        --stateful-disk=device-name=data-disk,source=https://www.googleapis.com/compute/v1/projects/my-project/zones/europe-west1-c/disks/my-data-disk-1 \
        --stateful-disk=device-name=boot-disk,source=https://www.googleapis.com/compute/v1/projects/my-project/zones/europe-west1-c/disks/my-instance-1-boot-disk \
        --zone=europe-west1-c
    

  6. Repeat the steps for each of your existing unmanaged VMs.




If you want to view the resulting per-instance configurations, run the [`instance-configs list` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/instance-groups/managed/instance-configs/list).
    
    
    gcloud compute instance-groups managed instance-configs list my-mig \
        --zone=europe-west1-c
    

To view the [preserved state](https://docs.cloud.google.com/compute/docs/instance-groups/how-stateful-migs-work#preserved_state_of_a_managed_instance) of an instance, run the [`describe-instance` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/instance-groups/managed/describe-instance).
    
    
    gcloud compute instance-groups managed describe-instance my-mig \
      --instance=my-instance-1 \
      --zone=europe-west1-c
    

For more information, see [Applying, viewing, and removing stateful configuration in MIGs](https://docs.cloud.google.com/compute/docs/instance-groups/applying-viewing-removing-stateful-config-in-migs).

## Configuring autohealing

MIGs automatically heal managed instances that stop running. To further improve the availability of your application and to verify that your application is responding, [set up an application-based health check and autohealing](https://docs.cloud.google.com/compute/docs/instance-groups/autohealing-instances-in-migs). See the [example health check setup](https://docs.cloud.google.com/compute/docs/instance-groups/autohealing-instances-in-migs#setting_up_an_autohealing_policy) for sample commands.

## Using a stateful policy instead of per-instance configurations

A stateful policy lets you declare disks that have a common device name as stateful across the MIG. A single stateful policy is less work to manage than multiple per-instance configurations. For example, with a stateful policy, you can designate all disks with device name `data-disk` to be stateful for all instances in the MIG.

If your MIG meets the following conditions, you can replace per-instance configurations with a stateful policy:

  * All VMs have the same device name (eg, `data-disk`) for similar stateful disks. This device name is defined in the MIG's instance template.
  * No VM has unique stateful metadata specified in a per-instance configuration. If you do have stateful metadata defined in a per-instance configuration, then you can remove the disk from the per-instance configuration, but you must keep the per-instance configuration to maintain that instance-specific stateful metadata.



Use the following steps to replace multiple per-instance configurations with a single stateful policy.

  1. Configure stateful disks in a stateful policy. Follow the instructions in [Setting and updating stateful configuration for disks in an existing MIG](https://docs.cloud.google.com/compute/docs/instance-groups/configuring-stateful-disks-in-migs#setting_and_updating_stateful_configuration_for_disks_in_an_existing_mig).

For the example scenario, use the following command. It declares that all disks in the MIG that have a specific device name will be preserved.
         
         gcloud compute instance-groups managed update my-mig \
           --stateful-disk=device-name=data-disk,auto-delete=never
         

  2. If you need to preserve instance-specific metadata, [update the per-instance configuration](https://docs.cloud.google.com/sdk/gcloud/reference/compute/instance-groups/managed/instance-configs/update). Otherwise, [delete the per-instance configuration](https://docs.cloud.google.com/compute/docs/instance-groups/applying-viewing-removing-stateful-config-in-migs#removing_stateful_configuration_for_a_specific_vm). Apply the configuration change immediately with the `--update-instance` flag. For example, to delete the per-instance configuration, use the following command:
         
         gcloud compute instance-groups managed instance-configs delete my-mig \
           --instances=my-instance-1 \
           --update-instance
         

  3. (Optional.) Verify that the stateful items are now stored in the preserved state from policy (`preservedStateFromPolicy`) for each managed instance. For more information, see [Viewing the preserved states of managed instances](https://docs.cloud.google.com/compute/docs/instance-groups/applying-viewing-removing-stateful-config-in-migs#viewing_the_preserved_states_of_managed_instances).




## Adding more VMs

If you need to add VMs to grow your application, you can add extra VMs by [increasing your MIG's size](https://docs.cloud.google.com/compute/docs/instance-groups/add-remove-vms-in-mig#resize_managed_group) or by [manually creating](https://docs.cloud.google.com/compute/docs/instance-groups/add-remove-vms-in-mig#creating_instances_with_specific_names_in_migs) more instances. The MIG creates all its VMs, including their persistent disks, based on the group's instance template. If the group has a stateful policy, any items you list in the stateful policy are preserved across restart, recreation, autohealing, and update operations for all new and existing instances in the group. If you need to configure stateful disks or metadata only for specific VMs in your group, use [per-instance configurations](https://docs.cloud.google.com/compute/docs/instance-groups/stateful-migs#per_instance_configs).

## What's next

  * Learn more about [Working with managed instances](https://docs.cloud.google.com/compute/docs/instance-groups/working-with-managed-instances).
  * Learn [How stateful MIGs work](https://docs.cloud.google.com/compute/docs/instance-groups/how-stateful-migs-work).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
