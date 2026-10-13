---
url: https://docs.cloud.google.com/compute/docs/gcloud-compute/common-commands/
title: Common gcloud compute commands \u00a0|\u00a0 Compute Engine \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:01:02.927130+00:00
---

# Common gcloud compute commands  |  Compute Engine  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/compute/docs/gcloud-compute/common-commands/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ Compute Engine ](https://docs.cloud.google.com/compute/docs)
  * [ APIs & Reference ](https://docs.cloud.google.com/compute/docs/apis)



Send feedback 

#  Common gcloud compute commands Stay organized with collections  Save and categorize content based on your preferences. 

This document lists some of the most commonly used `gcloud compute` commands.

## Before you begin

  * If you haven't already, set up [authentication](https://docs.cloud.google.com/compute/docs/authentication). Authentication verifies your identity for access to Google Cloud services and APIs. To run code or samples from a local development environment, you can authenticate to Compute Engine by selecting one of the following options: 
    1. [Install](https://docs.cloud.google.com/sdk/docs/install) the Google Cloud CLI. After installation, [initialize](https://docs.cloud.google.com/sdk/docs/initializing) the Google Cloud CLI by running the following command: 
           
           gcloud init

If you're using an external identity provider (IdP), you must first [ sign in to the gcloud CLI with your federated identity](https://docs.cloud.google.com/iam/docs/workforce-log-in-gcloud). 

**Note:** If you installed the gcloud CLI previously, make sure you have the latest version by running `gcloud components update`. 
    2. [ Set a default region and zone](https://docs.cloud.google.com/compute/docs/gcloud-compute#set_default_zone_and_region_in_your_local_client).



## Describing projects

Run the following command to query information about your Compute Engine project, such as project metadata, ssh keys, and quota metrics:
    
    
     gcloud compute project-info describe
    

For more information about describing your project, see the [`gcloud compute project-info describe`](https://docs.cloud.google.com/sdk/gcloud/reference/compute/project-info/describe) reference documentation.

## Working with VMs

The following examples show common tasks when working with virtual machine (VM) instances. For more information about virtual machine (VM) instances, see [Virtual machine instances](https://docs.cloud.google.com/compute/docs/instances).

### Creating VMs

Run the following command to create a VM:
    
    
    gcloud compute instances create VM_NAME \
        [--image IMAGE | --image-family IMAGE_FAMILY] \
        --image-project IMAGE_PROJECT
    

Replace the following:

  * `VM_NAME`: the [name](https://docs.cloud.google.com/compute/docs/naming-resources#resource-name-format) of the new VM.
  * `IMAGE` or `IMAGE_FAMILY`: Specify one of the following: 
    * `IMAGE`: required version of a public image. For example, `--image debian-10-buster-v20200309`.
    * `IMAGE_FAMILY`: an [image family](https://docs.cloud.google.com/compute/docs/images/os-details#general-info). This creates the VM from the most recent, non-deprecated OS image. For example, if you specify `--image-family debian-10`, Compute Engine creates a VM from the latest version of the OS image in the Debian 10 image family.
  * `IMAGE_PROJECT`: the [project](https://docs.cloud.google.com/compute/docs/images/os-details#general-info) containing the image.



For more information about creating VMs, see [Creating and starting a VM instance](https://docs.cloud.google.com/compute/docs/instances/create-start-instance) and the [`gcloud compute instances create`](https://docs.cloud.google.com/sdk/gcloud/reference/compute/instances/create) reference documentation.

### Listing VMs

Run the following command to display all VMs in a project:
    
    
    gcloud compute instances list
    

For more information about listing VMs, see the [`gcloud compute instances list`](https://docs.cloud.google.com/sdk/gcloud/reference/compute/instances/list) reference documentation.

### Listing VMs with GPUs

Run the following command to display all the VMs with GPUs in a project:
    
    
    gcloud compute instances list --filter="guestAccelerators.acceleratorCount>0" --format="table(name,zone,guestAccelerators.acceleratorType,guestAccelerators.acceleratorCount,disks.type)"
    

### Listing VMs with local SSDs

Run the following command to display all the VMs with local SSDs in a project:
    
    
    gcloud compute instances list  --filter="disks.type='SCRATCH'"  --format="table(name,zone,guestAccelerators.acceleratorType,guestAccelerators.acceleratorCount,disks.type)"
    

### Describing VMs

Run the following command to display all data associated with a VM:
    
    
    gcloud compute instances describe VM_NAME
    

Replace `VM_NAME` with the name of the VM.

For more information about describing VMs, see the [`gcloud compute instances describe`](https://docs.cloud.google.com/sdk/gcloud/reference/compute/instances/describe) reference documentation.

### Starting VMs

Run the following command to start a stopped VM:
    
    
    gcloud compute instances start VM_NAME
    

Replace `VM_NAME` with the name of the VM.

For more information about starting VMs, see [Starting and stopping an instance](https://docs.cloud.google.com/compute/docs/instances/stop-start-instance) and the [`gcloud compute instances start`](https://docs.cloud.google.com/sdk/gcloud/reference/compute/instances/start) reference documentation.

### Stopping VMs

Run the following command to stop a VM:
    
    
    gcloud compute instances stop VM_NAME
    

Replace `VM_NAME` with the name of the VM.

For more information about stopping VMs, see [Starting and stopping an instance](https://docs.cloud.google.com/compute/docs/instances/stop-start-instance) and the [`gcloud compute instances stop`](https://docs.cloud.google.com/sdk/gcloud/reference/compute/instances/stop) reference documentation.

### Adding labels to VMs

Run the following command to add labels to VMs:
    
    
    gcloud compute instances add-labels VM_NAME \
        --labels=KEY=VALUE
    

Replace the following:

  * `VM_NAME`: the name of the VM.
  * `KEY=VALUE`: the key-value pair of the label.



For more information about labeling VMs, see [Labeling resources](https://docs.cloud.google.com/compute/docs/labeling-resources) and the [`gcloud compute instances add-labels`](https://docs.cloud.google.com/sdk/gcloud/reference/compute/instances/add-labels) reference documentation.

## Connecting to VMs

### Using SSH to connect to instances

Run the following command to connect to a VM using SSH:
    
    
    gcloud compute ssh VM_NAME
    

Replace `VM_NAME` with the name of the VM.

For more information about connecting to VMs using SSH, see [Connecting to Linux VMs](https://docs.cloud.google.com/compute/docs/instances/connecting-to-instance) and the [`gcloud compute ssh`](https://docs.cloud.google.com/sdk/gcloud/reference/compute/ssh) reference documentation.

### Using SCP to transfer files to instances

Run the following command to copy files to a VM:
    
    
    gcloud compute scp LOCAL_FILE_PATH VM_NAME:REMOTE_DIRECTORY
    

Run the following command to copy files from a VM:
    
    
    gcloud compute scp VM_NAME:REMOTE_DIRECTORY LOCAL_FILE_PATH
    

Replace the following:

  * `LOCAL_FILE_PATH`: The path to the file on your workstation.
  * `VM_NAME`: The name of your VM.
  * `REMOTE_DIRECTORY`: The path to the directory on your VM.



For more information about transferring files to and from VMs using SCP, see [Transferring files using the Google Cloud CLI](https://docs.cloud.google.com/compute/docs/instances/transfer-files#transfergcloud) and the [`gcloud compute scp`](https://docs.cloud.google.com/sdk/gcloud/reference/compute/scp) reference documentation.

## Working with disks

The following example shows a common task when working with disks. For more information about disks, see [Storage options](https://docs.cloud.google.com/compute/docs/disks).

### Listing disks

Run the following command to display all disks in a project:
    
    
    gcloud compute disks list
    

For more information about listing disks, see the [`gcloud compute disks list`](https://docs.cloud.google.com/sdk/gcloud/reference/compute/disks/list) reference documentation.

## Working with snapshots

The following examples show common tasks when working with snapshots. For more information about snapshots, see [Persistent disk snapshots](https://docs.cloud.google.com/compute/docs/disks/snapshots).

### Listing snapshots

Run the following command to display all snapshots in a project:
    
    
    gcloud compute snapshots list
    

For more information about describing snapshots, see the [`gcloud compute snapshots list`](https://docs.cloud.google.com/sdk/gcloud/reference/compute/snapshots/list) reference documentation.

### Describing snapshots

Run the following command to display all data associated with a snapshot:
    
    
    gcloud compute snapshots describe SNAPSHOT_NAME
    

Replace `SNAPSHOT_NAME` with the name of the snapshot.

For more information about describing snapshots, see the [`gcloud compute snapshots describe`](https://docs.cloud.google.com/sdk/gcloud/reference/compute/snapshots/describe) reference documentation.

### Deleting snapshots

Run the following command to delete a snapshot:
    
    
    gcloud compute snapshots delete SNAPSHOT_NAME
    

Replace `SNAPSHOT_NAME` with the name of the snapshot.

For more information about deleting snapshots, see [Deleting a snapshot](https://docs.cloud.google.com/compute/docs/disks/manage-snapshots#delete_a_snapshot) and the [`gcloud compute snapshots delete`](https://docs.cloud.google.com/sdk/gcloud/reference/compute/snapshots/delete) reference documentation.

## Working with firewall rules

The following examples show common tasks when working with firewall rules. For more information about firewall rules, see [VPC firewall rules overview](https://docs.cloud.google.com/vpc/docs/firewalls).

### Describing firewall rules

Run the following command to display all data associated with a firewall rule:
    
    
    gcloud compute firewall-rules describe FIREWALL_RULE_NAME
    

Replace `FIREWALL_RULE_NAME` with the name of the firewall rule.

For more information about describing firewall rules, see the [`gcloud compute firewall-rules describe`](https://docs.cloud.google.com/sdk/gcloud/reference/compute/firewall-rules/describe) reference documentation.

### Creating firewall rules

Run the following command to create a firewall rule:
    
    
    gcloud compute firewall-rules create FIREWALL_RULE_NAME \
        [--allow=PROTOCOL:PORT | --action=ACTION --rules=PROTOCOL:PORT]
    

Specify either `--allow` or `--action` and `--rules`, and replace the following:

  * `FIREWALL_RULE_NAME`: the name of the firewall rule.
  * `ACTION`: the action on match. Either `allow` or `deny`.
  * `PROTOCOL:PORT`: the protocol and port whose traffic will be affected by the firewall rule.



For more information about creating firewall rules, see [Creating firewall rules](https://docs.cloud.google.com/vpc/docs/using-firewalls#creating_firewall_rules) and the [`gcloud compute firewall-rules create`](https://docs.cloud.google.com/sdk/gcloud/reference/compute/firewall-rules/create) reference documentation.

## Working with managed instances groups (MIGs)

The following examples show common tasks when working with MIGs. For more information about MIGs, see [Managed instance groups (MIGs)](https://docs.cloud.google.com/compute/docs/instance-groups#managed_instance_groups).

### Creating managed instance groups

Run the following command to create a MIG:
    
    
    gcloud compute instance-groups managed create INSTANCE_GROUP_NAME \
        --size=SIZE \
        --template=INSTANCE_TEMPLATE_URL
    

Replace the following:

  * `INSTANCE_GROUP_NAME`: the name for this instance group
  * `SIZE`: the size of the instance group
  * `INSTANCE_TEMPLATE_URL`: the URL of the instance template that you want to use to create instances in the MIG. The URL can contain either the [ID](https://docs.cloud.google.com/compute/docs/instance-templates/get-list-delete-instance-templates#get_information_about_an_instance_template) or name of the instance template. Specify one of the following values: 
    * For a regional instance template: `projects/PROJECT_ID/regions/REGION/instanceTemplates/INSTANCE_TEMPLATE_ID`
    * For a global instance template: `INSTANCE_TEMPLATE_ID`



For more information about creating MIGs, see [Basic scenarios for creating a MIG](https://docs.cloud.google.com/compute/docs/instance-groups/creating-groups-of-managed-instances#create_managed_group) and the [`gcloud compute instance-groups managed create`](https://docs.cloud.google.com/sdk/gcloud/reference/compute/instance-groups/managed/create) reference documentation.

### Setting autoscaling

Run the following command to set autoscaling on a MIG, based on CPU utilization:
    
    
    gcloud compute instance-groups managed set-autoscaling INSTANCE_GROUP_NAME \
        --max-num-replicas=MAX_NUM_REPLICAS \
        --target-cpu-utilization=TARGET_CPU_UTILIZATION
    

Replace the following:

  * `INSTANCE_GROUP_NAME`: the name of a MIG
  * `MAX_NUM_REPLICAS`: the maximum number of replicas the autoscaler can create
  * `TARGET_CPU_UTILIZATION`: the CPU level the autoscaler should maintain, between `0.0` and `1.0`

**Note:** You can set autoscaling based on one or more signals. For more information, see [Autoscaling policy](https://docs.cloud.google.com/compute/docs/autoscaler#autoscaling_policy).

For more information about setting autoscaling, see [Autoscaling groups of instances](https://docs.cloud.google.com/compute/docs/autoscaler) and the [`gcloud compute instance-groups managed set-autoscaling`](https://docs.cloud.google.com/sdk/gcloud/reference/compute/instance-groups/managed/set-autoscaling) reference documentation.

## Working with metadata

The following example shows a common task when working with metadata. For more information about metadata, see [About VM metadata](https://docs.cloud.google.com/compute/docs/metadata/overview).

### Adding project-level metadata

Run the following command to add metadata to your project:
    
    
    gcloud compute project-info add-metadata \
        --metadata=KEY=VALUE,[KEY=VALUE]
    

Replace the following:

  * `KEY=VALUE`: the metadata key-value pair



For more information about adding metadata to VMs, see [Set custom project metadata](https://docs.cloud.google.com/compute/docs/metadata/setting-custom-metadata#set-custom-project-wide-metadata) and the [`gcloud compute project-info add-metadata`](https://docs.cloud.google.com/sdk/gcloud/reference/compute/project-info/add-metadata) reference documentation.

### Adding instance-level metadata

Run the following command to add metadata to a VM:
    
    
    gcloud compute instances add-metadata VM_NAME \
        --metadata=KEY=VALUE,[KEY=VALUE]
    

Replace the following:

  * `VM_NAME`: the name of the VM
  * `KEY=VALUE`: the metadata key-value pair



For more information about adding metadata to VMs, see [Set custom instance metadata](https://docs.cloud.google.com/compute/docs/metadata/setting-custom-metadata#set-custom-instance-metadata) and the [`gcloud compute instances add-metadata`](https://docs.cloud.google.com/sdk/gcloud/reference/compute/instances/add-metadata) reference documentation.

## Getting help pages

The following commands show how to access different types of help, from general help about the `gcloud compute`command, to specific help about a resource group (`instances`) or a command (`create`). Comprehensive help for all resources and commands follows this pattern:
    
    
    gcloud compute --help
    
    
    gcloud compute instances --help
    
    
    gcloud compute instances create --help

Quick help can be obtained by using the `-h` flag instead of the `--help` flag. You can also review all of the comprehensive help at [Google Cloud CLI Reference](https://docs.cloud.google.com/sdk/gcloud/reference/compute).

For comprehensive help with commands specifically for configuring the gcloud CLI, run:
    
    
    gcloud topic TOPIC

Replace `TOPIC` with the topic you want help with. For a list of topics you can get help for, see the [`gcloud topic`](https://docs.cloud.google.com/sdk/gcloud/reference/topic) reference documentation.

## What's next?

  * View [The Google Cloud CLI cheat sheet](https://docs.cloud.google.com/sdk/docs/cheatsheet) for information about go-to commands for several Google Cloud products.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
