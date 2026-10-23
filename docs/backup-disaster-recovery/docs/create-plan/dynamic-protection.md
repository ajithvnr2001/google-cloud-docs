---
url: https://docs.cloud.google.com/backup-disaster-recovery/docs/create-plan/dynamic-protection/
title: Automate protection of Compute Engine instances in the appliance management console \u00a0|\u00a0 Backup and DR \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:20:32.659200+00:00
---

# Automate protection of Compute Engine instances in the appliance management console  |  Backup and DR  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/backup-disaster-recovery/docs/create-plan/dynamic-protection/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Storage ](https://docs.cloud.google.com/docs/storage)
  * [ Backup and DR ](https://docs.cloud.google.com/backup-disaster-recovery/docs)
  * [ Guides ](https://docs.cloud.google.com/backup-disaster-recovery/docs/concepts/backup-dr)



Send feedback 

#  Automate protection of Compute Engine instances in the appliance management console Stay organized with collections  Save and categorize content based on your preferences. 

This page details how to automate backups for Compute Engine instances using [Tags](https://docs.cloud.google.com/resource-manager/docs/tags/tags-overview) in the appliance management console.

**Note:** Dynamic tag based protection is allowed for the backup/recovery appliance deployed from the Google Cloud console only. Migrated backup/recovery appliances and their profiles cannot be used to auto-protect VMs in this way.

## Configure backup for new Compute Engine instances

A Compute Engine instance is a VM hosted on Google Cloud. Each instance stores data on Persistent Disks that are attached to the instance. You can [create an instance](https://docs.cloud.google.com/compute/docs/instances/create-start-instance) or [create a group of managed instances](https://docs.cloud.google.com/compute/docs/instance-groups/creating-groups-of-managed-instances) by using the Google Cloud console, the [gcloud CLI](https://docs.cloud.google.com/sdk/gcloud), or the Compute Engine API.

For more detailed information, see [Compute Engine](https://docs.cloud.google.com/compute).

## Prerequisite to automate backups

Before you start automating backups of Compute Engine instances, read the following procedures to prepare for backups:

  * [Create a backup plan template](https://docs.cloud.google.com/backup-disaster-recovery/docs/quickstarts/gce-instances-backup-recovery#template)



After setting up Backup and DR and creating a backup plan template, you can automate protection of your Compute Engine instances by applying the backup plan template to the instance using Tags.

## Permissions

To create, update, and delete Tags definitions for Compute Engine resources, you need the `Tag Administrator` role. For more information on the `tagUser` role, see [Required permissions](https://docs.cloud.google.com/resource-manager/docs/tags/tags-creating-and-managing#required-permissions).

To use dynamic tagging to back up a Compute Engine instance, you must grant the Backup and DR Compute Engine Operator (`roles/backupdr.computeEngineOperator`) Identity and Access Management (IAM) role to the backup/recovery appliance service agent within the Compute Engine project.

### Administer Dynamic Protection Tags

To create, update, and delete Dynamic Protection Tags, you need to have the [appropriate permissions](https://docs.cloud.google.com/backup-disaster-recovery/docs/access-control) for your role to be sure you have one of the following roles assigned:

  * Backup and DR Admin

  * Backup and DR Backup User

  * Backup and DR User V2

  * Project Editor

  * Project Owner

  * a custom role that includes the following permissions:




#### Required permissions

  * `backupdr.managementServers.listDynamicProtection`
  * `backupdr.managementServers.getDynamicProtection`
  * `backupdr.managementServers.createDynamicProtection`
  * `backupdr.managementServers.deleteDynamicProtection`
  * `compute.instances.listEffectiveTags`



Learn more about [Backup and DR roles](https://docs.cloud.google.com/backup-disaster-recovery/docs/access-control#roles).

## Apply a backup plan template using Tags automatically

This section helps you in automating the application of a backup plan to a Compute Engine instance using Tags. First you create a mapping of backup plans to Tags in the appliance management console. Then you create Tags through [IAM](https://docs.cloud.google.com/iam/docs) using the same values assigned in the appliance management console.

**Note:** The protection engine runs daily at 4:15 AM and 4:15 PM local time. If you set a protection tag at 5:00 PM on Monday, the Compute Engine instance won't be protected until 4:15 AM on Tuesday local time.

### Create Dynamic Protection Tag values

Use these instructions to create Dynamic Protection Tag values that can be used with your Compute Engine instances:

  1. In the Backup and DR appliance management console, click the **Backup Plans** drop-down menu and select **Dynamic Protection Tags**.

  2. Click **Create Dynamic Protection Tag**.

  3. Enter a unique **Tag Value** that follows these [naming requirements](https://docs.cloud.google.com/resource-manager/docs/tags/tags-overview#tags_and_labels).

  4. From the **Application type** list, select **Compute Engine**.

  5. Choose a corresponding **Template** and **Profile** to be associated with this Tag Value.

**Note:** Each Tag Value requires a unique Template and Profile.
  6. Click **Save**. A Dynamic Protection Tag value is created.




### Create Dynamic Protection Tags

Use these instructions to create Dynamic Protection Tags to attach to your Compute Engine instances in order to automate protection:

  1. To create, update, and delete tag definitions, you need the Tag Administrator role, or another role that includes [specific permissions](https://docs.cloud.google.com/resource-manager/docs/tags/tags-creating-and-managing#required-permissions).

  2. Open the **Tags** page in the Google Cloud console. 

[Open Tags page](https://console.cloud.google.com/iam-admin/tags)

  3. From the **Scope picker** at the top of the page, select the organization or project under which you want to create a tag key.

  4. Click add **Create**.

  5. In the **Tag key** box, enter `backupdr-dynamicprotect` as the tag key. This is a mandatory step for successful automation. Be mindful of spelling errors and be sure to include the hyphen.

  6. Optional: In the **Tag key description** box, enter a description of your tag key.

  7. Click add **Add value** and enter each Tag value that you just created.


**Note:** Each Tag value must match the exact spelling of the Dynamic Protection Tag values that you previously set in the Google Cloud console.

  1. In the **Tag value** box, enter the display name of your tag value. This becomes part of the namespaced name of your tag.

  2. In the **Tag value description** box, enter a description of the Template and Profile that are associated with this Tag value.

  3. When you have finished adding Tag values, click **Create tag key**.


**Note:** You can [add, edit, or delete Tag values at a later time](https://docs.cloud.google.com/resource-manager/docs/tags/tags-creating-and-managing#adding_tag_values).**Note:** Be sure that you aren't protecting the same Compute Engine instance twice if managed by two different backup/recovery appliances in two different management server instances. To do so, avoid creating the same dynamic protection tag values in different appliance management consoles.

### Adding Dynamic Protection Tags to a resource

Now that you have created Dynamic Protection Tag Values and linked them to a Dynamic Protection Tag, the next step is to assign a Tags to a Compute Engine instance. Tag based protection doesn't work if your instances are protected within a [logical group](https://docs.cloud.google.com/backup-disaster-recovery/docs/configuration/manage-logical-groups#protect-lg). [Remove logical group](https://docs.cloud.google.com/backup-disaster-recovery/docs/configuration/manage-logical-groups#delete-lg) and try using the dynamic protection.

**Note:** Don't add tags to a backup appliance Compute Engine instance that is created by Backup and DR.

Your Dynamic Protection Tags can be attached to Compute Engine instances using these instructions:

  1. In the Google Cloud console, go to the **Compute Engine** > **VM instances** page.

[Go to VM instances](https://console.cloud.google.com/compute/instances)

  2. In the **Name** column, click the name of the VM to which you want to add tags.

  3. From the **VM instance** details page, complete the following steps:

     1. Click **Edit**.
     2. In the **Basic** section, click **Manage Tags** and add the tags that you want for the instance.
  4. Select the `backupdr-dynamicprotect:` key and a corresponding **Tag Value** that maps to a Template and Profile that you set in the Google Cloud console.

  5. Click **Save**.




## Adding tags to a resource during resource creation

In certain scenarios, you might want to tag resources during resource creation, rather than after the resource is created.

###  Console 

  1. In the Google Cloud console, go to the **VM instances** page.

[Go to VM instances](https://console.cloud.google.com/compute/instances)

  2. Select your project and click **Continue**.

  3. Click **Create instance**.

  4. Click **Manage Tags and Labels**.

  5. Click **Add Tags**.

  6. Follow the instructions in the side panel to select the `backupdr-dynamicprotect` to add to the instance.

  7. Click **Save**.

  8. Complete other steps in [Create and start a VM instance](https://docs.cloud.google.com/compute/docs/instances/create-start-instance) to finish creating the instance.




###  gcloud 

To use gcloud CLI or APIs, follow the SDK documentation to do the following:

  * [Create a Tag Key](https://docs.cloud.google.com/sdk/gcloud/reference/resource-manager/tags/keys/create)

  * [Create a Tag Value](https://docs.cloud.google.com/sdk/gcloud/reference/resource-manager/tags/values/create)

  * [Create a Tag Binding](https://docs.cloud.google.com/sdk/gcloud/reference/resource-manager/tags/bindings/create)


**Note:** Be sure to set a pre-fixed **Tag Key** of `backupdr-dynamicprotect` for this automation to work as intended.

###  Terraform 

Use the following Terraform template to get started with using Dynamic Protection Tags. This template assumes you haven't already created any Dynamic Protection tag keys in the Google Cloud console and will set it up for you. The template creates a new Compute Engine instance and binds it to a dynamic protection tag. You can wait for the scheduled dynamic protection job to run at 4:15 AM or 4:15 PM local time for it to take effect, or you can run a dynamic protection job on-demand by following the steps in Run Manual Auto Protection.
    
    
    variable "project_id" {
      description = "The ID of the existing Google Cloud project"
      type        = string
    }
    
    variable "region" {
      description = "The Google Cloud region where demo-instance should be created"
      type        = string
    }
    
    variable "zone" {
      description = "The Google Cloud zone where demo-instance should be created"
      type        = string
    }
    
    provider "google" {
      project = var.project_id
      region = var.region
      zone  = var.zone
    }
    
    data "google_project" "project" {
      project_id = var.project_id
    }
    
    # Reference: https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/tags_tag_key
    resource "google_tags_tag_key" "key" {
      parent = "projects/${var.project_id}"
      short_name = "backupdr-dynamicprotect"
      description = "Tag key for Dynamic Protection."
    }
    
    # Reference: https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/tags_tag_value
    resource "google_tags_tag_value" "value" {
      parent = "tagKeys/${google_tags_tag_key.key.name}"
      short_name = "backupdr-gold" # This value should be present in the "Management Console UI" > "Backup Plans" > "Dynamic Protection Tags"
      description = "Tag value for gold plan."
    }
    
    # Reference: https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/compute_instance
    # Ensure not to define tag in "resource_manager_tags" block while creating VM instance. It'll destroy the VM
    # when tag value is changed/removed later. Instead define a separate tag binding using "google_tags_tag_binding"
    # or "google_tags_location_tag_binding" resource. It'll modify just tag binding and VM instance won't be affected.
    
    resource "google_compute_instance" "vm_instance" {
      name         = "demo-instance"
      machine_type = "e2-micro"
      zone         = var.zone
    
      boot_disk {
        initialize_params {
          image = "debian-cloud/debian-11"
        }
      }
    
      network_interface {
        network = "default"
    
        access_config {
          // Ephemeral public IP
        }
      }
    }
    
    # Reference: https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/google_tags_location_tag_binding
    resource "google_tags_location_tag_binding" "binding" {
        parent    = "//compute.googleapis.com/projects/${data.google_project.project.number}/zones/${var.zone}/instances/${google_compute_instance.vm_instance.instance_id}"
        tag_value = "tagValues/${google_tags_tag_value.value.name}"
        location  = var.zone
    }
    
    # Reference for Tag bindings at project/org level: https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/tags_tag_binding
    

## Detach a tag from a resource

You can detach a tag from a resource by deleting the tag binding resource.

**Note:** If you intend to remove protection for a Compute Engine instance, you can detach the tag from the Compute Engine instance. The Dynamic Protection engine will automatically detect that you no longer want to protect this Compute Engine instance and remove any assigned protection.

To review instructions on how to detach tags, see [Detaching a tag from a resource](https://docs.cloud.google.com/resource-manager/docs/tags/tags-creating-and-managing#detaching) in the Resource Manager documentation.

###  Console 

  1. In the Google Cloud console, go to the **VM instances** page.

[Go to VM instances](https://console.cloud.google.com/compute/instances)

  2. Select your project and click **Continue**.

  3. In the **Name** column, click the name of the VM for which you want to add tags.

  4. From the **VM instance** details page, complete the following steps:

  5. Click **Edit**.

  6. In the **Basic** section, click **Manage Tags** and remove the `backupdr-dynamicprotect` for the instance.

  7. Click **Save**.




###  gcloud 

To use gcloud CLI follow the documentation to [use ](https://docs.cloud.google.com/resource-manager/docs/tags/tags-creating-and-managing#detaching)[gcloud CLI](https://docs.cloud.google.com/sdk/gcloud) to detach a Tag from a resource.

## Run Manual Auto Protection

Although the protection engine runs daily at 4:15 AM and 4:15 PM local time, you can also make an on-demand run of the Dynamic Protection engine using the following command steps:

  1. Set the appliance management console endpoint by entering a value that starts with 'https://bmc-' and ends with '.com'. For example, `https://bmc-PROJECT_NUMBER-GENERATED_ID-dot-REGION.backupdr.googleusercontent.com`
         
         export MC_ENDPOINT="MC_ENDPOINT_edited_value"
         

  2. Generate a bearer token:
         
         echo "Generating a new bearer token..."
         export BEARER_TOKEN=$(gcloud auth print-access-token)
         echo "Bearer token generated: BEARER_TOKEN=$BEARER_TOKEN"
         

  3. Get a new session ID:
         
         echo "Generating a new session id..."
         export SESSION_RESPONSE=$(curl -XPOST -H "Authorization: Bearer $BEARER_TOKEN" -H "Content-Type: application/json" -d '{}' "$MC_ENDPOINT/actifio/session" 2>&-)
         export SESSION_ID=$(echo $SESSION_RESPONSE | jq -r '.session_id')
         
         if [ -z ${SESSION_ID} ]
           then echo "Issue with generating a new session id. Response: $SESSION_RESPONSE";
           return 1;
         fi
         
         echo "Session id generated: SESSION_ID=$SESSION_ID"
         

After you have set an endpoint, generated a bearer token, and gotten a session ID, you can trigger dynamic protection jobs for an hour until the session ID expires.

  4. Trigger a dynamic protection job

A dynamic protection job updates all Compute Engine instances with their current tags, and assigns backup plans based on the tags. The triggered job can take a few minutes depending on the number of changes pending for your workloads.
         
         echo "Triggering dynamic protection job.."
         
         curl -H "Authorization: Bearer $BEARER_TOKEN" -H "backupdr-management-session: Actifio $SESSION_ID" -H "Content-Type: application/json" -XPOST -d '{}' "$MC_ENDPOINT/actifio/dynamicprotection/job/gceinstance"
         
         echo "Dynamic protection job triggered."
         




## Use Dynamic Protection with the Resource Manager

You can use dynamic protection tags with [Resource Manager](https://docs.cloud.google.com/resource-manager), automating protection of your Compute Engine instances at a higher organizational level. Use the Resource Manager to tag resources at the project level or higher to be sure protection is inherited across all your resources. Learn more about [Tag Inheritance](https://docs.cloud.google.com/resource-manager/docs/tags/tags-overview#inheritance).

## Migrate manual protection to Dynamic Protection

If you intend to migrate your already protected resources to using dynamic protection using Tags, you must enable the migration flag in your project. After you've enabled migration, any manually protected instances can now use dynamic protection. Adding tags and resources automatically protects based on the tag and it removes the existing manual protection.

Before you begin, follow the steps in Run Manual Auto Protection to set up the session.

**Note:** Switching from user-initiated protection to tag-based protection won't affect the incremental nature of backups; they will remain incremental.

### Bash

Run the following commands.

  1. Set the appliance management console endpoint by entering a value that starts with 'https://bmc-' and ends with '.com'. For example, `https://bmc-PROJECT_NUMBER-GENERATED_ID-dot-REGION.backupdr.googleusercontent.com`
         
         #!/bin/bash
         
          export MC_ENDPOINT="MC_ENDPOINT_edited_value"
         
         

  2. Enable migration.
         
         curl -H "Authorization: Bearer $BEARER_TOKEN" -H "backupdr-management-session: Actifio $SESSION_ID" -H "Content-Type: application/json" -XPATCH -d '{ "enableMigrationToTagBasedProtection":"true"}' "$MC_ENDPOINT/actifio/dynamicprotection/jobconfig"
         




### Appliance management console

To enable migration of manually protected Compute Engine instances to tag-based protection, follow these steps:

  1. Toggle **Enable migration to tag based protection** to ON status
  2. Confirm the Enable Migration dialog. Manually protected Compute Engine instances will be reprotected using the tag defined on the VM.



To disable migration of manually protected Compute Engine instances to tag-based protection, follow these steps:

  1. Toggle **Enable migration to tag based protection** to OFF status.
  2. Confirm the Disable Migration dialog. This disables the migration of manually protected Compute Engine instances to tag based protection.

**Note:** Turning off the migration doesn't alter the protection of already protected Compute Engine instances. If you want to use a different backup plan, then manually assign the intended plan to the protected Compute Engine instances.

## Events and notifications

After the dynamic protection engine runs, you can review the progress from the [monitor events](https://docs.cloud.google.com/backup-disaster-recovery/docs/monitor-reports/monitor-events). The appliance management console receives summary notifications after performing dynamic protection actions. Error notifications are sent if a user action is needed.

## Best practices

Dynamic protection can increase the number of backup jobs running and the amount of storage used. For best results, consider the following:

  * Increase backup windows. A window of 6 to 10 hours can usually allow all jobs to run to completion.

  * A restored VM will carry over the same protection tag as the source VM along with the same backup plan, however the protection type will change from tag based protection to user initiated protection. The resource will continue to be protected using the carried over backup plan. To change the protection type back to tag based protection, you can remove the carried over protection backup plan and trigger dynamic protection job on-demand or wait for its next scheduled execution so that application is assigned tag based protection again.

  * A mounted VM on any existing host or newly created host won't carry over the same protection tag as the source VM, so it won't be protected automatically after the mount operation. If a newly mounted VM needs to be protected, then you can apply a tag binding to the new VM similar to the source VM.




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
